"""Dense-frequency physical-law test for the planar depletion confound.

The Paper-02 factorial decomposition showed that a planar device with a 3 um,
0.05 V space-charge/depletion perturbation can mimic the reference transport
signature while remaining close to rank one.  This script asks whether the
cross-frequency homogeneous drift-diffusion law rejects that deterministic,
spatially nonuniform electrostatic transport.

Important: the simulated trajectories contain no diffusion and no
recombination.  Any positive D inferred by the homogeneous law is therefore an
effective/spurious diffusion parameter produced by model mismatch.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np

import realistic_geometry_closure_stress as base
import paper02_geometry_parameter_sweep as sweep
from paper02_geometry_factorial_decomposition import best_rank_one


FREQUENCIES = np.asarray(
    (
        0.0,
        25e6,
        50e6,
        100e6,
        200e6,
        300e6,
        500e6,
        750e6,
        1e9,
        1.5e9,
        2e9,
        3e9,
    ),
    dtype=float,
)

H_M = 0.5e-6
CALIBRATION_FREQUENCY_HZ = 100e6
LOW_BAND_MAX_HZ = 200e6


def gamma_from_q(q: complex) -> complex:
    return -np.log(q) / H_M


def solve_dw_one_frequency(gamma: complex, frequency_hz: float):
    """Solve real D,w from D gamma^2 + w gamma = -i omega."""
    g2 = gamma * gamma
    M = np.asarray(
        (
            (g2.real, gamma.real),
            (g2.imag, gamma.imag),
        ),
        dtype=float,
    )
    rhs = np.asarray((0.0, -2.0 * np.pi * frequency_hz), dtype=float)
    D, w = np.linalg.solve(M, rhs)
    return float(D), float(w)


def solve_dw_low_band(gammas, frequencies):
    rows = []
    rhs = []
    for gamma, f in zip(gammas, frequencies):
        if f <= 0 or f > LOW_BAND_MAX_HZ:
            continue
        g2 = gamma * gamma
        rows.append((g2.real, gamma.real))
        rhs.append(0.0)
        rows.append((g2.imag, gamma.imag))
        rhs.append(-2.0 * np.pi * f)
    x, *_ = np.linalg.lstsq(np.asarray(rows), np.asarray(rhs), rcond=None)
    return float(x[0]), float(x[1])


def law_residual(gamma, frequency_hz, D, w):
    lhs = D * gamma * gamma + w * gamma
    rhs = -1j * 2.0 * np.pi * frequency_hz
    error = lhs - rhs
    if frequency_hz <= 0:
        rel = abs(error)
    else:
        rel = abs(error) / abs(rhs)
    return error, float(rel)


def run(args):
    old_frequencies = base.FREQUENCIES
    base.FREQUENCIES = FREQUENCIES.copy()
    base.V_BIAS = float(args.bias_v)
    base.X_EXTENT_UM = float(args.x_extent_um)

    numerical = {
        "nx": args.nx,
        "nz": args.nz,
        "nx_src": args.nx_src,
        "nz_src": args.nz_src,
        "ds_um": args.ds_um,
    }

    planar = base.Scenario("planar", 1.0, 0.0, 0.0)
    depleted = base.Scenario("planar_depletion", 1.0, 3.0, 0.05)

    try:
        Jp, dp = sweep.currents_with_beam(
            planar,
            2.0,
            0.0,
            **numerical,
        )
        Jd, dd = sweep.currents_with_beam(
            depleted,
            2.0,
            0.0,
            **numerical,
        )
    finally:
        base.FREQUENCIES = old_frequencies

    rows = []
    gamma_planar = []
    gamma_depleted = []

    for jf, f in enumerate(FREQUENCIES):
        _, qp, fitp = best_rank_one(np.diff(Jp[jf]))
        _, qd, fitd = best_rank_one(np.diff(Jd[jf]))
        gp = gamma_from_q(qp)
        gd = gamma_from_q(qd)
        gamma_planar.append(gp)
        gamma_depleted.append(gd)

        rows.append(
            {
                "frequency_hz": float(f),
                "planar_q_real": float(qp.real),
                "planar_q_imag": float(qp.imag),
                "depleted_q_real": float(qd.real),
                "depleted_q_imag": float(qd.imag),
                "planar_gamma_real_per_m": float(gp.real),
                "planar_gamma_imag_per_m": float(gp.imag),
                "depleted_gamma_real_per_m": float(gd.real),
                "depleted_gamma_imag_per_m": float(gd.imag),
                "planar_rank1_fit_rel": float(fitp),
                "depleted_rank1_fit_rel": float(fitd),
            }
        )

    gamma_planar = np.asarray(gamma_planar)
    gamma_depleted = np.asarray(gamma_depleted)

    cal_idx = int(np.where(FREQUENCIES == CALIBRATION_FREQUENCY_HZ)[0][0])
    D_one, w_one = solve_dw_one_frequency(
        gamma_depleted[cal_idx],
        CALIBRATION_FREQUENCY_HZ,
    )
    D_low, w_low = solve_dw_low_band(gamma_depleted, FREQUENCIES)

    for row, gd, f in zip(rows, gamma_depleted, FREQUENCIES):
        e1, r1 = law_residual(gd, f, D_one, w_one)
        el, rl = law_residual(gd, f, D_low, w_low)
        row.update(
            {
                "one_rf_error_real_per_s": float(e1.real),
                "one_rf_error_imag_per_s": float(e1.imag),
                "one_rf_relative_law_residual": r1,
                "low_band_error_real_per_s": float(el.real),
                "low_band_error_imag_per_s": float(el.imag),
                "low_band_relative_law_residual": rl,
            }
        )

    nonzero = [r for r in rows if r["frequency_hz"] > 0]
    below_1pct_one = [
        r["frequency_hz"]
        for r in nonzero
        if r["one_rf_relative_law_residual"] < 0.01
    ]
    below_1pct_low = [
        r["frequency_hz"]
        for r in nonzero
        if r["low_band_relative_law_residual"] < 0.01
    ]

    payload = {
        "status": "CONDITIONAL deterministic depletion-field confound",
        "model_truth": {
            "diffusion_in_trajectory_model": False,
            "recombination_in_trajectory_model": False,
            "depletion_width_um": 3.0,
            "space_charge_drop_v": 0.05,
            "contact_fraction": 1.0,
        },
        "numerical": numerical,
        "law_convention": "D*gamma^2 + w*gamma = -i*omega; kappa=0",
        "one_rf_identification": {
            "calibration_frequency_hz": CALIBRATION_FREQUENCY_HZ,
            "effective_D_m2_per_s": D_one,
            "effective_w_m_per_s": w_one,
            "physically_admissible_D_positive_w_positive": bool(D_one > 0 and w_one > 0),
            "highest_sampled_frequency_below_1pct_residual_hz": (
                max(below_1pct_one) if below_1pct_one else None
            ),
        },
        "low_band_fit": {
            "max_fit_frequency_hz": LOW_BAND_MAX_HZ,
            "effective_D_m2_per_s": D_low,
            "effective_w_m_per_s": w_low,
            "physically_admissible_D_positive_w_positive": bool(D_low > 0 and w_low > 0),
            "highest_sampled_frequency_below_1pct_residual_hz": (
                max(below_1pct_low) if below_1pct_low else None
            ),
        },
        "diagnostics": {
            "depleted_dc_rank1_fit_rel": rows[0]["depleted_rank1_fit_rel"],
            "max_depleted_rank1_fit_rel": max(r["depleted_rank1_fit_rel"] for r in rows),
            "max_one_rf_residual_through_1ghz": max(
                r["one_rf_relative_law_residual"]
                for r in rows
                if 0 < r["frequency_hz"] <= 1e9
            ),
            "max_low_band_residual_through_1ghz": max(
                r["low_band_relative_law_residual"]
                for r in rows
                if 0 < r["frequency_hz"] <= 1e9
            ),
        },
    }

    out_csv = Path(args.output_csv)
    out_json = Path(args.output_summary)
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    out_json.parent.mkdir(parents=True, exist_ok=True)

    with out_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    out_json.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))
    print(f"wrote {out_csv}")
    print(f"wrote {out_json}")


def parser():
    p = argparse.ArgumentParser()
    p.add_argument("--bias-v", type=float, default=0.30)
    p.add_argument("--x-extent-um", type=float, default=3.5)
    p.add_argument("--nx", type=int, default=121)
    p.add_argument("--nz", type=int, default=91)
    p.add_argument("--nx-src", type=int, default=13)
    p.add_argument("--nz-src", type=int, default=41)
    p.add_argument("--ds-um", type=float, default=0.020)
    p.add_argument("--output-csv", default="paper02_planar_depletion_frequency_law.csv")
    p.add_argument("--output-summary", default="paper02_planar_depletion_frequency_law_summary.json")
    return p


if __name__ == "__main__":
    run(parser().parse_args())
