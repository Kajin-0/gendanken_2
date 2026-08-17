"""Kernel-aware dense-frequency test for the planar depletion confound.

This is the stricter follow-up to paper02_planar_depletion_frequency_law.py.
The earlier test reduced the six wavelength channels to an approximately
geometric sequence.  Rev. 9 explicitly allows calibrated wavelength-dependent
kernel shapes, so this calculation instead fits the exact one-mode averaged
form

    J_m = C + K F_m(r),
    F_m(r) = integral g_m(z) [exp(r(z-zref))-1]/r dz,

with the r->0 affine limit evaluated continuously.  For a point response
C + B exp(r z), this reparameterization is algebraically equivalent but avoids
the severe A/B cancellation near r=0.

For each RF frequency only the complex root r is nonlinear; C and K are solved
by complex linear least squares.  The physical downstream exponent used by the
repository convention is gamma=-r for the present increasing-z coordinate.

The simulated depleted trajectories contain no diffusion and no recombination.
If the kernel-aware roots nevertheless satisfy a physically admissible
homogeneous drift-diffusion law with D>0 across a useful RF band, that D is a
spurious effective parameter caused by spatial electrostatic heterogeneity.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np
from scipy.optimize import least_squares

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
Z_REF_M = float(np.mean(base.DEPTHS)) * 1e-6


def kernel_basis(r_per_m: complex) -> np.ndarray:
    """Return calibrated finite-kernel basis F_m(r) in metres."""
    z_um = base.OPT_Z_UM
    z_m = z_um * 1e-6
    dz = z_m - Z_REF_M

    if abs(r_per_m) < 1e-8:
        point = dz.astype(complex)
    else:
        point = np.expm1(r_per_m * dz) / r_per_m

    return np.asarray(
        [np.trapezoid(row[3] * point, z_um) for row in base.OPTICS],
        dtype=complex,
    )


def linear_fit_for_r(J: np.ndarray, r_per_m: complex):
    F = kernel_basis(r_per_m)
    X = np.column_stack((np.ones(len(F), dtype=complex), F))
    coeff, *_ = np.linalg.lstsq(X, J, rcond=None)
    model = X @ coeff
    scale = max(float(np.linalg.norm(J)), 1e-30)
    rel = float(np.linalg.norm(model - J) / scale)
    return coeff, model, rel


def kernel_aware_root(J: np.ndarray):
    """Fit complex r after eliminating the two complex linear coefficients."""
    # Use the geometric-sequence estimate only as an optimizer seed.
    _, q0, _, _ = best_rank_one(np.diff(J))
    r0 = np.log(q0) / H_M
    rho0 = r0 * 1e-6  # dimensionless root per micrometre for conditioning
    scale = max(float(np.linalg.norm(J)), 1e-30)

    def residual(x):
        r = (x[0] + 1j * x[1]) / 1e-6
        _, model, _ = linear_fit_for_r(J, r)
        e = (model - J) / scale
        return np.concatenate((e.real, e.imag))

    fit = least_squares(
        residual,
        np.asarray((rho0.real, rho0.imag), dtype=float),
        xtol=1e-13,
        ftol=1e-13,
        gtol=1e-13,
        max_nfev=3000,
    )
    r = (fit.x[0] + 1j * fit.x[1]) / 1e-6
    coeff, model, rel = linear_fit_for_r(J, r)
    return r, coeff, model, rel


def solve_dw_one_frequency(gamma: complex, frequency_hz: float):
    g2 = gamma * gamma
    M = np.asarray(
        ((g2.real, gamma.real), (g2.imag, gamma.imag)),
        dtype=float,
    )
    rhs = np.asarray((0.0, -2.0 * np.pi * frequency_hz), dtype=float)
    D, w = np.linalg.solve(M, rhs)
    return float(D), float(w)


def solve_dw_low_band(gammas, frequencies):
    M = []
    rhs = []
    for gamma, f in zip(gammas, frequencies):
        if f <= 0 or f > LOW_BAND_MAX_HZ:
            continue
        g2 = gamma * gamma
        M.extend(((g2.real, gamma.real), (g2.imag, gamma.imag)))
        rhs.extend((0.0, -2.0 * np.pi * f))
    x, *_ = np.linalg.lstsq(np.asarray(M), np.asarray(rhs), rcond=None)
    return float(x[0]), float(x[1])


def law_residual(gamma, frequency_hz, D, w):
    lhs = D * gamma * gamma + w * gamma
    rhs = -1j * 2.0 * np.pi * frequency_hz
    e = lhs - rhs
    return e, float(abs(e) / abs(rhs)) if frequency_hz > 0 else float(abs(e))


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
        Jp, _ = sweep.currents_with_beam(planar, 2.0, 0.0, **numerical)
        Jd, _ = sweep.currents_with_beam(depleted, 2.0, 0.0, **numerical)
    finally:
        base.FREQUENCIES = old_frequencies

    rows = []
    gp_all = []
    gd_all = []

    for jf, f in enumerate(FREQUENCIES):
        rp, cp, mp, fitp = kernel_aware_root(Jp[jf])
        rd, cd, md, fitd = kernel_aware_root(Jd[jf])
        gp = -rp
        gd = -rd
        gp_all.append(gp)
        gd_all.append(gd)

        rows.append(
            {
                "frequency_hz": float(f),
                "planar_r_real_per_m": float(rp.real),
                "planar_r_imag_per_m": float(rp.imag),
                "depleted_r_real_per_m": float(rd.real),
                "depleted_r_imag_per_m": float(rd.imag),
                "planar_gamma_real_per_m": float(gp.real),
                "planar_gamma_imag_per_m": float(gp.imag),
                "depleted_gamma_real_per_m": float(gd.real),
                "depleted_gamma_imag_per_m": float(gd.imag),
                "planar_kernel_fit_rel": float(fitp),
                "depleted_kernel_fit_rel": float(fitd),
            }
        )

    gp_all = np.asarray(gp_all)
    gd_all = np.asarray(gd_all)

    cal_idx = int(np.where(FREQUENCIES == CALIBRATION_FREQUENCY_HZ)[0][0])
    D_one, w_one = solve_dw_one_frequency(gd_all[cal_idx], CALIBRATION_FREQUENCY_HZ)
    D_low, w_low = solve_dw_low_band(gd_all, FREQUENCIES)

    for row, gd, f in zip(rows, gd_all, FREQUENCIES):
        e1, rel1 = law_residual(gd, f, D_one, w_one)
        el, rell = law_residual(gd, f, D_low, w_low)
        row.update(
            {
                "one_rf_error_real_per_s": float(e1.real),
                "one_rf_error_imag_per_s": float(e1.imag),
                "one_rf_relative_law_residual": rel1,
                "low_band_error_real_per_s": float(el.real),
                "low_band_error_imag_per_s": float(el.imag),
                "low_band_relative_law_residual": rell,
            }
        )

    nonzero = [r for r in rows if r["frequency_hz"] > 0]
    below_one = [r["frequency_hz"] for r in nonzero if r["one_rf_relative_law_residual"] < 0.01]
    below_low = [r["frequency_hz"] for r in nonzero if r["low_band_relative_law_residual"] < 0.01]

    payload = {
        "status": "CONDITIONAL kernel-aware deterministic depletion-field confound",
        "model_truth": {
            "diffusion_in_trajectory_model": False,
            "recombination_in_trajectory_model": False,
            "contact_fraction": 1.0,
            "depletion_width_um": 3.0,
            "space_charge_drop_v": 0.05,
        },
        "fit_model": "J_m=C+K*integral[g_m(z)*(exp(r(z-zref))-1)/r]dz; gamma=-r",
        "z_ref_um": Z_REF_M * 1e6,
        "numerical": numerical,
        "one_rf_identification": {
            "calibration_frequency_hz": CALIBRATION_FREQUENCY_HZ,
            "effective_D_m2_per_s": D_one,
            "effective_w_m_per_s": w_one,
            "physically_admissible_D_positive_w_positive": bool(D_one > 0 and w_one > 0),
            "highest_sampled_frequency_below_1pct_residual_hz": max(below_one) if below_one else None,
        },
        "low_band_fit": {
            "max_fit_frequency_hz": LOW_BAND_MAX_HZ,
            "effective_D_m2_per_s": D_low,
            "effective_w_m_per_s": w_low,
            "physically_admissible_D_positive_w_positive": bool(D_low > 0 and w_low > 0),
            "highest_sampled_frequency_below_1pct_residual_hz": max(below_low) if below_low else None,
        },
        "diagnostics": {
            "max_planar_kernel_fit_rel": max(r["planar_kernel_fit_rel"] for r in rows),
            "max_depleted_kernel_fit_rel": max(r["depleted_kernel_fit_rel"] for r in rows),
            "max_depleted_kernel_fit_rel_through_1ghz": max(
                r["depleted_kernel_fit_rel"] for r in rows if r["frequency_hz"] <= 1e9
            ),
            "max_one_rf_law_residual_through_1ghz": max(
                r["one_rf_relative_law_residual"] for r in rows if 0 < r["frequency_hz"] <= 1e9
            ),
            "max_low_band_law_residual_through_1ghz": max(
                r["low_band_relative_law_residual"] for r in rows if 0 < r["frequency_hz"] <= 1e9
            ),
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
    p.add_argument("--output-csv", default="paper02_kernel_aware_depletion_frequency_law.csv")
    p.add_argument("--output-summary", default="paper02_kernel_aware_depletion_frequency_law_summary.json")
    return p


if __name__ == "__main__":
    run(parser().parse_args())
