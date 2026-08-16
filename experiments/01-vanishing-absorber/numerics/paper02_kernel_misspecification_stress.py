"""Optical-kernel misspecification stress for Paper 02.

This calculation is separate from paper02_covariance_geometry_stress.py.
Measurement noise remains the canonical independent equal-quadrature reference
model.  Here the *true* wavelength-dependent generation kernels are perturbed,
while the inverse continues to use the nominal theoretical kernels.

Two deterministic transport truths are tested:

  1. the exact full-contact planar heterogeneous counterexample used in the
     Paper-02 continuum cross-check (D_micro=0);
  2. a uniform-velocity full-contact planar null with D_micro=0, for which the
     nominal one-mode kernel-aware inverse is exact.

The perturbations are controlled uncertainty directions rather than claims about
an instrument:

  * common wavelength registration offsets;
  * wavelength-dependent linear / curvature registration errors;
  * kernel-width errors recentered to preserve each nominal mean depth;
  * symmetric tail broadening recentered to preserve each nominal mean depth.

For every case the script records actual mean-depth shifts, L1 kernel changes,
same-frequency D_eff, one-mode fit residuals, the 100-MHz-anchored frequency-law
mismatch, and the canonical positive-D-vs-model-rejection SNR ordering.

Scientific purpose: determine whether kernel error merely perturbs the central
heterogeneity-induced D_eff, or can itself generate apparent diffusion in the
uniform deterministic null.  The result is a model-uncertainty stress, not an
experimental calibration claim.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np
from scipy.integrate import cumulative_trapezoid

import realistic_geometry_closure_stress as base
import paper02_kernel_aware_depletion_frequency_law as law
import paper02_exact_planar_continuum_crosscheck as exact
from paper02_same_frequency_hidden_risk import analyze_one


FREQUENCIES = law.FREQUENCIES.copy()
PROBES = (100e6, 500e6, 1e9)
Z_UM = base.OPT_Z_UM
Z_M = Z_UM * 1e-6
L_M = base.L_UM * 1e-6
N_CHANNEL = len(base.OPTICS)


def normalize_kernel(g: np.ndarray) -> np.ndarray:
    g = np.maximum(np.asarray(g, dtype=float), 0.0)
    area = float(np.trapezoid(g, Z_UM))
    if area <= 0 or not np.isfinite(area):
        raise ValueError("kernel normalization failed")
    return g / area


def kernel_mean(g: np.ndarray) -> float:
    g = normalize_kernel(g)
    return float(np.trapezoid(Z_UM * g, Z_UM))


def kernel_sigma(g: np.ndarray) -> float:
    g = normalize_kernel(g)
    mu = kernel_mean(g)
    return float(np.sqrt(np.trapezoid((Z_UM - mu) ** 2 * g, Z_UM)))


def shift_kernel(g: np.ndarray, delta_um: float) -> np.ndarray:
    """Rigidly shift a density by delta_um on the fixed absorber grid."""
    src = Z_UM - float(delta_um)
    out = np.interp(src, Z_UM, np.asarray(g, dtype=float), left=0.0, right=0.0)
    return normalize_kernel(out)


def recenter_kernel(g: np.ndarray, target_mean_um: float) -> np.ndarray:
    """Shift once/twice to restore the target mean after a shape perturbation."""
    out = normalize_kernel(g)
    for _ in range(3):
        delta = float(target_mean_um - kernel_mean(out))
        if abs(delta) < 1e-10:
            break
        out = shift_kernel(out, delta)
    return normalize_kernel(out)


def stretch_about_mean(g: np.ndarray, factor: float, mean_um: float) -> np.ndarray:
    if factor <= 0:
        raise ValueError("width factor must be positive")
    src = mean_um + (Z_UM - mean_um) / float(factor)
    out = np.interp(src, Z_UM, np.asarray(g, dtype=float), left=0.0, right=0.0) / float(factor)
    return recenter_kernel(out, mean_um)


def symmetric_tail_mix(g: np.ndarray, eps: float, shift_um: float, mean_um: float) -> np.ndarray:
    if not (0 <= eps < 0.5):
        raise ValueError("tail mixing epsilon outside range")
    gm = shift_kernel(g, -shift_um)
    gp = shift_kernel(g, +shift_um)
    out = (1.0 - 2.0 * eps) * np.asarray(g) + eps * gm + eps * gp
    return recenter_kernel(out, mean_um)


def nominal_kernels() -> list[np.ndarray]:
    return [normalize_kernel(row[3]) for row in base.OPTICS]


def wavelength_kernels(offsets_nm: np.ndarray) -> list[np.ndarray]:
    offsets_nm = np.asarray(offsets_nm, dtype=float)
    if offsets_nm.shape != (N_CHANNEL,):
        raise ValueError("wrong wavelength-offset shape")
    return [
        normalize_kernel(base.optical_kernel(float(wl + dnm * 1e-3))[3])
        for wl, dnm in zip(base.WAVELENGTHS, offsets_nm)
    ]


def perturbation_cases() -> list[dict]:
    nominal = nominal_kernels()
    means = np.asarray([kernel_mean(g) for g in nominal])
    idx = np.arange(N_CHANNEL, dtype=float)
    centered = idx - np.mean(idx)
    centered /= np.max(np.abs(centered))
    curv = centered**2
    curv -= np.mean(curv)
    curv /= np.max(np.abs(curv))

    cases = [
        {"name": "nominal", "family": "nominal", "parameter": 0.0, "kernels": nominal, "wavelength_offsets_nm": np.zeros(N_CHANNEL)},
    ]

    for dnm in (-5.0, -1.0, 1.0, 5.0):
        offsets = np.full(N_CHANNEL, dnm)
        cases.append(
            {
                "name": f"wavelength_common_{dnm:+.0f}nm",
                "family": "wavelength_common",
                "parameter": dnm,
                "kernels": wavelength_kernels(offsets),
                "wavelength_offsets_nm": offsets,
            }
        )

    for amp in (1.0, 5.0):
        offsets = amp * centered
        cases.append(
            {
                "name": f"wavelength_linear_pm{amp:.0f}nm",
                "family": "wavelength_linear",
                "parameter": amp,
                "kernels": wavelength_kernels(offsets),
                "wavelength_offsets_nm": offsets,
            }
        )
        offsets = amp * curv
        cases.append(
            {
                "name": f"wavelength_curvature_pm{amp:.0f}nm",
                "family": "wavelength_curvature",
                "parameter": amp,
                "kernels": wavelength_kernels(offsets),
                "wavelength_offsets_nm": offsets,
            }
        )

    for factor in (0.90, 0.95, 1.05, 1.10):
        kernels = [stretch_about_mean(g, factor, mu) for g, mu in zip(nominal, means)]
        cases.append(
            {
                "name": f"width_scale_{factor:.2f}",
                "family": "mean_preserving_width_scale",
                "parameter": factor,
                "kernels": kernels,
                "wavelength_offsets_nm": np.full(N_CHANNEL, np.nan),
            }
        )

    for eps in (0.005, 0.010, 0.020):
        kernels = [symmetric_tail_mix(g, eps, 0.50, mu) for g, mu in zip(nominal, means)]
        cases.append(
            {
                "name": f"mean_preserving_tailmix_eps_{eps:.3f}",
                "family": "mean_preserving_symmetric_tail_mix",
                "parameter": eps,
                "kernels": kernels,
                "wavelength_offsets_nm": np.full(N_CHANNEL, np.nan),
            }
        )
    return cases


def remaining_integral(y: np.ndarray, x: np.ndarray) -> np.ndarray:
    c = np.concatenate(([0.0 + 0.0j], cumulative_trapezoid(y, x)))
    return c[-1] - c


def uniform_point_transfer(v_m_per_s: float) -> np.ndarray:
    travel = Z_M / float(v_m_per_s)
    out = np.empty((len(FREQUENCIES), len(Z_M)), dtype=complex)
    for jf, f in enumerate(FREQUENCIES):
        omega = 2.0 * np.pi * float(f)
        if f == 0.0:
            out[jf] = (L_M - Z_M) / L_M
            continue
        phase = np.exp(-1j * omega * travel)
        rem = remaining_integral(phase, Z_M)
        out[jf] = np.exp(1j * omega * travel) * rem / L_M
    return out


def channel_currents(point: np.ndarray, kernels: list[np.ndarray]) -> np.ndarray:
    return np.asarray(
        [
            [np.trapezoid(g * point[jf], Z_UM) for g in kernels]
            for jf in range(point.shape[0])
        ],
        dtype=complex,
    )


def kernel_diagnostics(kernels: list[np.ndarray], nominal: list[np.ndarray]) -> dict:
    means = np.asarray([kernel_mean(g) for g in kernels])
    means0 = np.asarray([kernel_mean(g) for g in nominal])
    sigmas = np.asarray([kernel_sigma(g) for g in kernels])
    sigmas0 = np.asarray([kernel_sigma(g) for g in nominal])
    l1 = np.asarray([np.trapezoid(np.abs(g - g0), Z_UM) for g, g0 in zip(kernels, nominal)])
    return {
        "means_um": means.tolist(),
        "sigmas_um": sigmas.tolist(),
        "max_abs_mean_shift_nm": float(1e3 * np.max(np.abs(means - means0))),
        "rms_mean_shift_nm": float(1e3 * np.sqrt(np.mean((means - means0) ** 2))),
        "max_abs_sigma_change_nm": float(1e3 * np.max(np.abs(sigmas - sigmas0))),
        "max_kernel_L1_distance": float(np.max(l1)),
    }


def infer_case(J: np.ndarray) -> dict:
    gammas = []
    fit_rels = []
    roots = []
    for jf, f in enumerate(FREQUENCIES):
        r, _coeff, _model, fit_rel = law.kernel_aware_root(J[jf])
        roots.append(r)
        gammas.append(-r)
        fit_rels.append(float(fit_rel))
    gammas = np.asarray(gammas, dtype=complex)
    fit_rels = np.asarray(fit_rels, dtype=float)

    probe = {}
    for f in PROBES:
        idx = int(np.where(FREQUENCIES == f)[0][0])
        D, w = law.solve_dw_one_frequency(gammas[idx], f)
        stat = analyze_one(J[idx], f)
        probe[str(int(f))] = {
            "D_eff_m2_per_s": float(D),
            "w_eff_m_per_s": float(w),
            "gamma_real_per_m": float(gammas[idx].real),
            "gamma_imag_per_m": float(gammas[idx].imag),
            "kernel_fit_rel": float(fit_rels[idx]),
            "snr_required_positive_D_db": float(stat["snr_required_positive_D_db"]),
            "snr_required_one_mode_rejection_db": float(stat["snr_required_one_mode_rejection_db"]),
            "positive_D_detectable_before_one_mode_rejection": bool(stat["positive_D_detectable_before_one_mode_rejection"]),
        }

    D_low, w_low = law.solve_dw_low_band(gammas, FREQUENCIES)
    p100 = probe[str(int(100e6))]
    _e, law1g = law.law_residual(
        gammas[int(np.where(FREQUENCIES == 1e9)[0][0])],
        1e9,
        p100["D_eff_m2_per_s"],
        p100["w_eff_m_per_s"],
    )
    return {
        "probe": probe,
        "low_band_D_eff_m2_per_s": float(D_low),
        "low_band_w_eff_m_per_s": float(w_low),
        "anchored_100MHz_law_residual_at_1GHz": float(law1g),
        "max_kernel_fit_rel_through_1GHz": float(np.max(fit_rels[FREQUENCIES <= 1e9])),
    }


def flatten_row(transport: str, case: dict, diag: dict, result: dict) -> dict:
    p100 = result["probe"][str(int(100e6))]
    p500 = result["probe"][str(int(500e6))]
    p1g = result["probe"][str(int(1e9))]
    offsets = np.asarray(case["wavelength_offsets_nm"], dtype=float)
    finite_offsets = offsets[np.isfinite(offsets)]
    return {
        "transport": transport,
        "case": case["name"],
        "family": case["family"],
        "parameter": float(case["parameter"]),
        "max_abs_wavelength_offset_nm": float(np.max(np.abs(finite_offsets))) if len(finite_offsets) else float("nan"),
        "max_abs_mean_shift_nm": diag["max_abs_mean_shift_nm"],
        "rms_mean_shift_nm": diag["rms_mean_shift_nm"],
        "max_abs_sigma_change_nm": diag["max_abs_sigma_change_nm"],
        "max_kernel_L1_distance": diag["max_kernel_L1_distance"],
        "D100_m2_per_s": p100["D_eff_m2_per_s"],
        "D500_m2_per_s": p500["D_eff_m2_per_s"],
        "D1000_m2_per_s": p1g["D_eff_m2_per_s"],
        "fit100_rel": p100["kernel_fit_rel"],
        "fit500_rel": p500["kernel_fit_rel"],
        "fit1000_rel": p1g["kernel_fit_rel"],
        "S_D_100_db": p100["snr_required_positive_D_db"],
        "S_reject_100_db": p100["snr_required_one_mode_rejection_db"],
        "hidden_100": p100["positive_D_detectable_before_one_mode_rejection"],
        "S_D_500_db": p500["snr_required_positive_D_db"],
        "S_reject_500_db": p500["snr_required_one_mode_rejection_db"],
        "hidden_500": p500["positive_D_detectable_before_one_mode_rejection"],
        "S_D_1000_db": p1g["snr_required_positive_D_db"],
        "S_reject_1000_db": p1g["snr_required_one_mode_rejection_db"],
        "hidden_1000": p1g["positive_D_detectable_before_one_mode_rejection"],
        "low_band_D_m2_per_s": result["low_band_D_eff_m2_per_s"],
        "low_band_w_m_per_s": result["low_band_w_eff_m_per_s"],
        "anchored_100MHz_law_residual_at_1GHz": result["anchored_100MHz_law_residual_at_1GHz"],
        "max_kernel_fit_rel_through_1GHz": result["max_kernel_fit_rel_through_1GHz"],
    }


def summarize(rows: list[dict]) -> dict:
    out = {}
    for transport in sorted(set(r["transport"] for r in rows)):
        rr = [r for r in rows if r["transport"] == transport]
        nom = next(r for r in rr if r["case"] == "nominal")
        non = [r for r in rr if r["case"] != "nominal"]
        out[transport] = {
            "nominal": {
                "D100": nom["D100_m2_per_s"],
                "D500": nom["D500_m2_per_s"],
                "D1000": nom["D1000_m2_per_s"],
                "law_residual_1GHz": nom["anchored_100MHz_law_residual_at_1GHz"],
            },
            "D100_range_m2_per_s": [float(min(r["D100_m2_per_s"] for r in rr)), float(max(r["D100_m2_per_s"] for r in rr))],
            "D500_range_m2_per_s": [float(min(r["D500_m2_per_s"] for r in rr)), float(max(r["D500_m2_per_s"] for r in rr))],
            "D1000_range_m2_per_s": [float(min(r["D1000_m2_per_s"] for r in rr)), float(max(r["D1000_m2_per_s"] for r in rr))],
            "max_abs_D100_change_from_nominal_m2_per_s": float(max(abs(r["D100_m2_per_s"] - nom["D100_m2_per_s"]) for r in non)),
            "largest_D100_case": max(rr, key=lambda r: r["D100_m2_per_s"])["case"],
            "smallest_D100_case": min(rr, key=lambda r: r["D100_m2_per_s"])["case"],
            "positive_D100_cases": [r["case"] for r in non if r["D100_m2_per_s"] > 0],
            "hidden_100_cases": [r["case"] for r in rr if r["hidden_100"]],
            "hidden_500_cases": [r["case"] for r in rr if r["hidden_500"]],
            "hidden_1000_cases": [r["case"] for r in rr if r["hidden_1000"]],
            "max_kernel_fit_rel_through_1GHz": float(max(r["max_kernel_fit_rel_through_1GHz"] for r in rr)),
            "max_law_residual_1GHz": float(max(r["anchored_100MHz_law_residual_at_1GHz"] for r in rr)),
        }
    return out


def run(args):
    nominal = nominal_kernels()
    cases = perturbation_cases()

    # Exact heterogeneous planar stress.
    point_hetero = exact.exact_point_transfer(Z_M, FREQUENCIES)

    # Uniform deterministic null matched to the total transit time of the exact
    # heterogeneous profile, so bandwidth scales remain comparable.
    v_exact = exact.exact_speed_m_per_s(Z_M)
    transit = float(np.trapezoid(1.0 / v_exact, Z_M))
    v_harmonic = float(L_M / transit)
    point_uniform = uniform_point_transfer(v_harmonic)

    rows = []
    detailed = []
    for case in cases:
        diag = kernel_diagnostics(case["kernels"], nominal)
        for label, point in (("heterogeneous_exact", point_hetero), ("uniform_velocity_null", point_uniform)):
            J = channel_currents(point, case["kernels"])
            result = infer_case(J)
            rows.append(flatten_row(label, case, diag, result))
            detailed.append(
                {
                    "transport": label,
                    "case": case["name"],
                    "family": case["family"],
                    "parameter": float(case["parameter"]),
                    "wavelength_offsets_nm": np.asarray(case["wavelength_offsets_nm"], dtype=float).tolist(),
                    "kernel_diagnostics": diag,
                    "inference": result,
                }
            )

    payload = {
        "status": "CHECKED theoretical optical-kernel misspecification stress",
        "scope": {
            "measurement_covariance": "canonical independent equal real/imag quadrature reference",
            "inverse_kernels": "nominal theoretical HgCdTe kernels",
            "true_kernels": "controlled perturbed kernels",
            "experimental_calibration_claim": False,
            "perturbations_are_stress_directions_not_empirical_error_bars": True,
        },
        "transport_truths": {
            "heterogeneous_exact": {
                "microscopic_D": 0.0,
                "recombination": 0.0,
                "description": "exact full-contact planar heterogeneous counterexample",
            },
            "uniform_velocity_null": {
                "microscopic_D": 0.0,
                "recombination": 0.0,
                "velocity_m_per_s": v_harmonic,
                "description": "uniform deterministic planar null; nominal kernel-aware one-mode model is exact",
            },
        },
        "nominal_kernel_sigmas_um": [kernel_sigma(g) for g in nominal],
        "summary": summarize(rows),
        "rows": rows,
        "detailed": detailed,
    }

    out_csv = Path(args.output_csv)
    out_json = Path(args.output_summary)
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    with out_csv.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    out_json.write_text(json.dumps(payload, indent=2, sort_keys=True, allow_nan=True), encoding="utf-8")
    print(json.dumps({"status": payload["status"], "summary": payload["summary"]}, indent=2, sort_keys=True))


def parser():
    p = argparse.ArgumentParser()
    p.add_argument("--output-csv", default="paper02_kernel_misspecification_stress.csv")
    p.add_argument("--output-summary", default="paper02_kernel_misspecification_stress_summary.json")
    return p


if __name__ == "__main__":
    run(parser().parse_args())
