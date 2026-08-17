"""Signed kernel-calibration threshold scan for Paper 02.

This follows the broad kernel-misspecification stress with two focused tasks:

1. quantify the signed differential wavelength-registration slope needed to
   create a false positive D_eff in a uniform deterministic D_micro=0 null;
2. verify the analytic control that a *global affine depth-coordinate warp* of
   every kernel rescales the homogeneous root but cannot create diffusion from
   exact D=0.

The differential wavelength error is parameterized by A_nm:

    delta_lambda_m = A_nm * s_m,
    s = [-1,-0.6,-0.2,+0.2,+0.6,+1].

Thus A_nm is the maximum signed endpoint wavelength error and the endpoint span
is 2|A_nm|.  Positive and negative signs are both tested; no sign is selected
post hoc.

All calculations use exact planar continuum point responses.  The inverse uses
the nominal theoretical kernels.  These are controlled theoretical stress
coordinates, not empirical calibration-error bars.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np
from scipy.optimize import brentq

import realistic_geometry_closure_stress as base
import paper02_kernel_aware_depletion_frequency_law as law
import paper02_exact_planar_continuum_crosscheck as exact
import paper02_kernel_misspecification_stress as ks


F100 = 100e6
F500 = 500e6
F1000 = 1e9
CENTERED = np.linspace(-1.0, 1.0, len(base.OPTICS))
SCAN_ABS_NM = np.asarray((0.0, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0), dtype=float)
SIGNED_SCAN_NM = np.asarray(sorted(set(np.concatenate((-SCAN_ABS_NM[1:], SCAN_ABS_NM)))), dtype=float)


def nominal_kernels():
    return ks.nominal_kernels()


def linear_wavelength_kernels(amplitude_nm: float):
    offsets = float(amplitude_nm) * CENTERED
    return ks.wavelength_kernels(offsets), offsets


def affine_depth_warp(g: np.ndarray, b: float, center_um: float = 3.25) -> np.ndarray:
    """Push nominal density through z_true=center+b(z_nom-center)."""
    if b <= 0:
        raise ValueError("affine scale b must be positive")
    # z_nom = center + (z_true-center)/b; density transforms by 1/b.
    z_nom = center_um + (ks.Z_UM - center_um) / float(b)
    out = np.interp(z_nom, ks.Z_UM, np.asarray(g, dtype=float), left=0.0, right=0.0) / float(b)
    return ks.normalize_kernel(out)


def transports():
    z_m = ks.Z_M
    point_hetero = exact.exact_point_transfer(z_m, law.FREQUENCIES)
    v_exact = exact.exact_speed_m_per_s(z_m)
    transit = float(np.trapezoid(1.0 / v_exact, z_m))
    v_harmonic = float(ks.L_M / transit)
    point_uniform = ks.uniform_point_transfer(v_harmonic)
    return point_hetero, point_uniform, v_harmonic


def evaluate(point: np.ndarray, kernels: list[np.ndarray]) -> dict:
    J = ks.channel_currents(point, kernels)
    return ks.infer_case(J)


def p(result: dict, f: float) -> dict:
    return result["probe"][str(int(f))]


def row_from_result(transport: str, model: str, amplitude: float, kernels, result, nominal):
    kd = ks.kernel_diagnostics(kernels, nominal)
    q100, q500, q1000 = p(result, F100), p(result, F500), p(result, F1000)
    return {
        "transport": transport,
        "error_model": model,
        "amplitude": float(amplitude),
        "max_abs_mean_shift_nm": kd["max_abs_mean_shift_nm"],
        "rms_mean_shift_nm": kd["rms_mean_shift_nm"],
        "max_abs_sigma_change_nm": kd["max_abs_sigma_change_nm"],
        "max_kernel_L1_distance": kd["max_kernel_L1_distance"],
        "D100_m2_per_s": q100["D_eff_m2_per_s"],
        "w100_m_per_s": q100["w_eff_m_per_s"],
        "fit100_rel": q100["kernel_fit_rel"],
        "S_D_100_db": q100["snr_required_positive_D_db"],
        "S_reject_100_db": q100["snr_required_one_mode_rejection_db"],
        "hidden_100": q100["positive_D_detectable_before_one_mode_rejection"],
        "D500_m2_per_s": q500["D_eff_m2_per_s"],
        "hidden_500": q500["positive_D_detectable_before_one_mode_rejection"],
        "D1000_m2_per_s": q1000["D_eff_m2_per_s"],
        "hidden_1000": q1000["positive_D_detectable_before_one_mode_rejection"],
        "law_residual_1GHz": result["anchored_100MHz_law_residual_at_1GHz"],
        "low_band_D_m2_per_s": result["low_band_D_eff_m2_per_s"],
        "low_band_w_m_per_s": result["low_band_w_eff_m_per_s"],
    }


def signed_linear_scan(point_hetero, point_uniform, nominal):
    rows = []
    cache = {}
    for amp in SIGNED_SCAN_NM:
        kernels, _offsets = linear_wavelength_kernels(amp)
        for label, point in (("heterogeneous_exact", point_hetero), ("uniform_velocity_null", point_uniform)):
            result = evaluate(point, kernels)
            cache[(label, float(amp))] = result
            rows.append(row_from_result(label, "differential_wavelength_slope_nm", amp, kernels, result, nominal))
    return rows, cache


def scalar_uniform_metrics(amplitude_nm: float, point_uniform) -> tuple[float, float, float, float]:
    kernels, _ = linear_wavelength_kernels(amplitude_nm)
    result = evaluate(point_uniform, kernels)
    q = p(result, F100)
    return (
        float(q["D_eff_m2_per_s"]),
        float(q["snr_required_positive_D_db"]),
        float(q["snr_required_one_mode_rejection_db"]),
        float(ks.kernel_diagnostics(kernels, nominal_kernels())["max_abs_mean_shift_nm"]),
    )


def scalar_hetero_D(amplitude_nm: float, point_hetero) -> float:
    kernels, _ = linear_wavelength_kernels(amplitude_nm)
    return float(p(evaluate(point_hetero, kernels), F100)["D_eff_m2_per_s"])


def bracket_positive_root(func, lo=1e-7, hi=1.0, n=80):
    xs = np.geomspace(lo, hi, n)
    last_x, last_y = 0.0, float(func(0.0))
    for x in xs:
        y = float(func(float(x)))
        if np.isfinite(last_y) and np.isfinite(y) and last_y * y <= 0 and x != last_x:
            return float(last_x), float(x)
        last_x, last_y = float(x), y
    return None


def threshold_summary(point_hetero, point_uniform, nominal):
    D_target = float(p(evaluate(point_hetero, nominal), F100)["D_eff_m2_per_s"])

    def f_target(a):
        return scalar_uniform_metrics(a, point_uniform)[0] - D_target

    br = bracket_positive_root(f_target)
    target_amp = float(brentq(f_target, *br, xtol=1e-10, rtol=1e-10)) if br else None

    def f_hidden(a):
        _D, sd, sr, _depth = scalar_uniform_metrics(a, point_uniform)
        return sd - sr

    brh = bracket_positive_root(f_hidden)
    hidden_amp = float(brentq(f_hidden, *brh, xtol=1e-10, rtol=1e-10)) if brh else None

    def f_plus10(a):
        return scalar_hetero_D(a, point_hetero) - 1.10 * D_target

    def f_minus10_mag(a):
        # reverse slope: evaluate negative amplitude and solve for 0.90*Dtarget
        return scalar_hetero_D(-a, point_hetero) - 0.90 * D_target

    brp = bracket_positive_root(f_plus10)
    brm = bracket_positive_root(f_minus10_mag)
    plus10 = float(brentq(f_plus10, *brp, xtol=1e-10, rtol=1e-10)) if brp else None
    minus10 = float(brentq(f_minus10_mag, *brm, xtol=1e-10, rtol=1e-10)) if brm else None

    def pack(amp):
        if amp is None:
            return None
        D, sd, sr, depth = scalar_uniform_metrics(amp, point_uniform)
        return {
            "amplitude_nm": float(amp),
            "endpoint_wavelength_span_nm": float(2.0 * abs(amp)),
            "max_abs_mean_depth_shift_nm": depth,
            "uniform_null_D100_m2_per_s": D,
            "uniform_null_S_D_100_db": sd,
            "uniform_null_S_reject_100_db": sr,
        }

    return {
        "heterogeneous_nominal_D100_m2_per_s": D_target,
        "uniform_null_slope_amplitude_where_false_D_equals_heterogeneous_nominal": pack(target_amp),
        "uniform_null_slope_amplitude_where_100MHz_hidden_risk_begins": pack(hidden_amp),
        "heterogeneous_slope_amplitude_for_plus10pct_D100_nm": plus10,
        "heterogeneous_reverse_slope_magnitude_for_minus10pct_D100_nm": minus10,
    }


def affine_control(point_uniform, nominal, v_uniform):
    rows = []
    for b in (0.995, 1.000, 1.005):
        kernels = [affine_depth_warp(g, b) for g in nominal]
        result = evaluate(point_uniform, kernels)
        q = p(result, F100)
        rows.append(
            {
                "depth_scale_b": b,
                "max_abs_mean_shift_nm": ks.kernel_diagnostics(kernels, nominal)["max_abs_mean_shift_nm"],
                "D100_m2_per_s": float(q["D_eff_m2_per_s"]),
                "w100_m_per_s": float(q["w_eff_m_per_s"]),
                "predicted_w_m_per_s": float(v_uniform / b),
                "relative_w_error_vs_affine_prediction": float(abs(q["w_eff_m_per_s"] - v_uniform / b) / (v_uniform / b)),
                "fit100_rel": float(q["kernel_fit_rel"]),
            }
        )
    return rows


def run(args):
    nominal = nominal_kernels()
    point_hetero, point_uniform, v_uniform = transports()
    scan_rows, _cache = signed_linear_scan(point_hetero, point_uniform, nominal)
    thresholds = threshold_summary(point_hetero, point_uniform, nominal)
    affine = affine_control(point_uniform, nominal, v_uniform)

    payload = {
        "status": "CHECKED signed kernel-calibration threshold scan",
        "scope": {
            "exact_planar_continuum": True,
            "microscopic_D": 0.0,
            "inverse_uses_nominal_theoretical_kernels": True,
            "differential_wavelength_slope_is_controlled_stress_not_empirical_error_bar": True,
            "both_slope_signs_tested": True,
        },
        "differential_wavelength_parameterization": {
            "channel_shape": CENTERED.tolist(),
            "definition": "delta_lambda_m = A_nm * channel_shape[m]",
            "endpoint_span": "2*abs(A_nm)",
        },
        "uniform_velocity_m_per_s": v_uniform,
        "thresholds": thresholds,
        "affine_depth_scale_control": affine,
        "scan_rows": scan_rows,
    }

    out_csv = Path(args.output_csv)
    out_json = Path(args.output_summary)
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    with out_csv.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(scan_rows[0].keys()))
        w.writeheader()
        w.writerows(scan_rows)
    out_json.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps({"thresholds": thresholds, "affine_depth_scale_control": affine}, indent=2, sort_keys=True))


def parser():
    p = argparse.ArgumentParser()
    p.add_argument("--output-csv", default="paper02_kernel_calibration_threshold.csv")
    p.add_argument("--output-summary", default="paper02_kernel_calibration_threshold_summary.json")
    return p


if __name__ == "__main__":
    run(parser().parse_args())
