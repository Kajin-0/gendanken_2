"""Exact affine depth-coordinate control for Paper 02 kernel uncertainty.

This replaces the sampled-density warp used as an auxiliary control in the first
kernel-threshold run.  That density-warp implementation introduced finite-grid /
boundary interpolation error and is not used as theorem evidence.

Here the nominal kernel coordinate u is retained exactly and the analytic
uniform-drift point response is evaluated at

    z_true = z_c + b (u-z_c)

before integration.  For b<=1 the whole transformed interval stays inside the
absorber.  Because a uniform deterministic Ramo response is affine-exponential
in source depth, the nominal-kernel inverse should recover

    gamma_eff = b gamma_true,
    D_eff = 0,
    w_eff = w_true / b

up to numerical optimization/quadrature precision.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np

import realistic_geometry_closure_stress as base
import paper02_kernel_aware_depletion_frequency_law as law
import paper02_exact_planar_continuum_crosscheck as exact
import paper02_kernel_misspecification_stress as ks


CENTER_UM = 0.5 * base.L_UM
SCALES = (0.990, 0.995, 1.000)


def uniform_velocity() -> float:
    z_m = ks.Z_M
    v_exact = exact.exact_speed_m_per_s(z_m)
    transit = float(np.trapezoid(1.0 / v_exact, z_m))
    return float(ks.L_M / transit)


def analytic_uniform_H(z_true_um: np.ndarray, frequency_hz: float, v: float) -> np.ndarray:
    z = np.asarray(z_true_um, dtype=float) * 1e-6
    if frequency_hz == 0.0:
        return (ks.L_M - z) / ks.L_M
    omega = 2.0 * np.pi * float(frequency_hz)
    return v * (1.0 - np.exp(-1j * omega * (ks.L_M - z) / v)) / (1j * omega * ks.L_M)


def transformed_channels(b: float, v: float) -> np.ndarray:
    u = ks.Z_UM
    z_true = CENTER_UM + float(b) * (u - CENTER_UM)
    nominal = ks.nominal_kernels()
    return np.asarray(
        [
            [np.trapezoid(g * analytic_uniform_H(z_true, f, v), u) for g in nominal]
            for f in law.FREQUENCIES
        ],
        dtype=complex,
    )


def run(args):
    v = uniform_velocity()
    nominal_means = np.asarray([ks.kernel_mean(g) for g in ks.nominal_kernels()])
    rows = []
    for b in SCALES:
        J = transformed_channels(b, v)
        result = ks.infer_case(J)
        transformed_means = CENTER_UM + b * (nominal_means - CENTER_UM)
        for f in (100e6, 500e6, 1e9):
            q = result["probe"][str(int(f))]
            rows.append(
                {
                    "depth_scale_b": float(b),
                    "frequency_hz": float(f),
                    "max_abs_mean_depth_shift_nm": float(1e3 * np.max(np.abs(transformed_means - nominal_means))),
                    "D_eff_m2_per_s": float(q["D_eff_m2_per_s"]),
                    "w_eff_m_per_s": float(q["w_eff_m_per_s"]),
                    "predicted_w_m_per_s": float(v / b),
                    "relative_w_error": float(abs(q["w_eff_m_per_s"] - v / b) / (v / b)),
                    "kernel_fit_rel": float(q["kernel_fit_rel"]),
                }
            )

    max_D = float(max(abs(r["D_eff_m2_per_s"]) for r in rows))
    max_werr = float(max(r["relative_w_error"] for r in rows))
    max_fit = float(max(r["kernel_fit_rel"] for r in rows))
    payload = {
        "status": "CHECKED exact affine depth-coordinate control",
        "supersedes_control_only": "sampled-density affine control embedded in first paper02_kernel_calibration_threshold run",
        "note": "The signed differential-wavelength threshold results are independent of the superseded sampled-density affine control.",
        "theory": {
            "gamma_eff": "b * gamma_true",
            "D_eff_for_true_D_zero": 0.0,
            "w_eff": "w_true / b",
        },
        "uniform_velocity_m_per_s": v,
        "max_abs_D_eff_m2_per_s": max_D,
        "max_relative_w_error": max_werr,
        "max_kernel_fit_rel": max_fit,
        "rows": rows,
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
    p.add_argument("--output-csv", default="paper02_exact_affine_depth_control.csv")
    p.add_argument("--output-summary", default="paper02_exact_affine_depth_control_summary.json")
    return p


if __name__ == "__main__":
    run(parser().parse_args())
