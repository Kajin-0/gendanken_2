"""Causal split between point-source and finite-kernel electrostatic confounds.

The current planar-depletion example uses a 3 um space-charge region at the
collector side of a 7.6 um absorber, so the depletion boundary is z=4.6 um.
The six nominal spectral-depth means are 2.0--4.5 um.  Their centers therefore
lie outside the depletion region, but the calibrated generation kernels have
finite tails that overlap it.

This script asks whether the false diffusion is already present for ideal point
sources at those six means or is generated mainly by the interaction between
finite generation width and the downstream field-gradient region.

It also evaluates an equal-spaced point-source set wholly inside depletion as a
positive control for the deterministic field-gradient theorem.
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
from paper02_kernel_aware_depletion_frequency_law import kernel_aware_root


FREQUENCIES = np.asarray((0.0, 100e6, 500e6, 1e9), dtype=float)
H_M = 0.5e-6
OUTSIDE_DEPTHS_UM = np.arange(2.0, 4.51, 0.5)
INSIDE_DEPTHS_UM = np.arange(4.8, 7.31, 0.5)


def point_currents(scenario, depths_um, numerical):
    g = base.geometry(scenario, numerical["nx"], numerical["nz"])
    J = np.zeros((len(FREQUENCIES), len(depths_um)), dtype=complex)
    reached = []
    for m, z0 in enumerate(depths_um):
        H, _, ok, _ = base.trajectory(g, 0.0, float(z0), numerical["ds_um"])
        J[:, m] = H
        reached.append(bool(ok))
    return J, all(reached)


def roots_from_point_sequence(J):
    rows = []
    gammas = []
    for jf, f in enumerate(FREQUENCIES):
        A, q, model, fit_rel = best_rank_one(np.diff(J[jf]))
        gamma = -np.log(q) / H_M
        gammas.append(gamma)
        rows.append(
            {
                "frequency_hz": float(f),
                "q_real": float(q.real),
                "q_imag": float(q.imag),
                "gamma_real_per_m": float(gamma.real),
                "gamma_imag_per_m": float(gamma.imag),
                "rank1_fit_rel": float(fit_rel),
            }
        )
    return np.asarray(gammas), rows


def solve_dw(gamma, frequency_hz):
    g2 = gamma * gamma
    M = np.asarray(((g2.real, gamma.real), (g2.imag, gamma.imag)), dtype=float)
    rhs = np.asarray((0.0, -2.0 * np.pi * frequency_hz), dtype=float)
    D, w = np.linalg.solve(M, rhs)
    return float(D), float(w)


def residual(gamma, f, D, w):
    if f <= 0:
        return 0.0
    rhs = -1j * 2.0 * np.pi * f
    return float(abs(D * gamma * gamma + w * gamma - rhs) / abs(rhs))


def summarize_point(label, J, reached):
    gammas, rows = roots_from_point_sequence(J)
    idx = int(np.where(FREQUENCIES == 100e6)[0][0])
    D, w = solve_dw(gammas[idx], 100e6)
    for row, g, f in zip(rows, gammas, FREQUENCIES):
        row["case"] = label
        row["law_residual_from_100mhz"] = residual(g, f, D, w)
    return rows, {
        "all_trajectories_reached": reached,
        "effective_D_m2_per_s_from_100mhz": D,
        "effective_w_m_per_s_from_100mhz": w,
        "physically_positive_D_w": bool(D > 0 and w > 0),
        "max_rank1_fit_rel": max(r["rank1_fit_rel"] for r in rows),
        "law_residual_1ghz": next(r["law_residual_from_100mhz"] for r in rows if r["frequency_hz"] == 1e9),
    }


def summarize_kernel(J):
    rows = []
    gammas = []
    for jf, f in enumerate(FREQUENCIES):
        r, _, _, fit_rel = kernel_aware_root(J[jf])
        gamma = -r
        gammas.append(gamma)
        rows.append(
            {
                "case": "finite_calibrated_kernels",
                "frequency_hz": float(f),
                "q_real": float("nan"),
                "q_imag": float("nan"),
                "gamma_real_per_m": float(gamma.real),
                "gamma_imag_per_m": float(gamma.imag),
                "rank1_fit_rel": float(fit_rel),
            }
        )
    gammas = np.asarray(gammas)
    idx = int(np.where(FREQUENCIES == 100e6)[0][0])
    D, w = solve_dw(gammas[idx], 100e6)
    for row, g, f in zip(rows, gammas, FREQUENCIES):
        row["law_residual_from_100mhz"] = residual(g, f, D, w)
    return rows, {
        "effective_D_m2_per_s_from_100mhz": D,
        "effective_w_m_per_s_from_100mhz": w,
        "physically_positive_D_w": bool(D > 0 and w > 0),
        "max_one_mode_fit_rel": max(r["rank1_fit_rel"] for r in rows),
        "law_residual_1ghz": next(r["law_residual_from_100mhz"] for r in rows if r["frequency_hz"] == 1e9),
    }


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

    depleted = base.Scenario("planar_depletion", 1.0, 3.0, 0.05)
    try:
        J_out, reached_out = point_currents(depleted, OUTSIDE_DEPTHS_UM, numerical)
        J_in, reached_in = point_currents(depleted, INSIDE_DEPTHS_UM, numerical)
        J_kernel, _ = sweep.currents_with_beam(depleted, 2.0, 0.0, **numerical)
    finally:
        base.FREQUENCIES = old_frequencies

    rows_out, summary_out = summarize_point("point_sources_2.0_to_4.5um", J_out, reached_out)
    rows_in, summary_in = summarize_point("point_sources_4.8_to_7.3um", J_in, reached_in)
    rows_kernel, summary_kernel = summarize_kernel(J_kernel)
    rows = rows_out + rows_in + rows_kernel

    payload = {
        "status": "CONDITIONAL causal split",
        "geometry": {
            "absorber_thickness_um": float(base.L_UM),
            "depletion_width_um": 3.0,
            "depletion_start_um": float(base.L_UM - 3.0),
            "space_charge_drop_v": 0.05,
            "bias_v": float(args.bias_v),
        },
        "outside_point_sources": {
            "depths_um": OUTSIDE_DEPTHS_UM.tolist(),
            **summary_out,
        },
        "inside_point_sources": {
            "depths_um": INSIDE_DEPTHS_UM.tolist(),
            **summary_in,
        },
        "finite_calibrated_kernels": summary_kernel,
        "interpretation_gate": {
            "finite_kernel_interaction_supported_if": "outside-point |D_eff| << finite-kernel D_eff while inside-depletion point sources have positive D_eff",
        },
    }

    out_csv = Path(args.output_csv)
    out_json = Path(args.output_summary)
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    with out_csv.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    out_json.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


def parser():
    p = argparse.ArgumentParser()
    p.add_argument("--bias-v", type=float, default=0.30)
    p.add_argument("--x-extent-um", type=float, default=3.5)
    p.add_argument("--nx", type=int, default=121)
    p.add_argument("--nz", type=int, default=91)
    p.add_argument("--nx-src", type=int, default=13)
    p.add_argument("--nz-src", type=int, default=41)
    p.add_argument("--ds-um", type=float, default=0.020)
    p.add_argument("--output-csv", default="paper02_point_vs_kernel_causal_test.csv")
    p.add_argument("--output-summary", default="paper02_point_vs_kernel_causal_test_summary.json")
    return p


if __name__ == "__main__":
    run(parser().parse_args())
