"""Predeclared parametric-bootstrap gate for Paper 03 Stage A.

Implements PAPER03_STAGEA_STATISTICAL_PREDECLARATION_2026-08-17.md.
The six-channel calibrated-kernel one-mode null is nonlinearly refit for every
noise realization.  No physical root interpretation is performed here.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import numpy as np
from scipy.optimize import brentq, least_squares
from scipy.stats import chi2, ncx2

import paper03_stageA_kernel_blind_gate as kernel
import paper03_stageA_resolvent as resolvent
import realistic_geometry_closure_stress as base


ALPHA = 0.002699796063260207
TARGET_POWER = 0.90
N_NULL = 4000
N_ALT = 2000
SNR_OFFSETS_DB = (-4.0, -2.0, 0.0, 2.0, 4.0)
ALL6 = np.arange(len(base.DEPTHS), dtype=int)
ROOT_LOWER = np.asarray((-25.0, -15.0), float)
ROOT_UPPER = np.asarray((25.0, 15.0), float)
FAST_ROOT_PERTURB = 0.03


def complex_from_fit(fit: dict[str, Any], key: str) -> np.ndarray:
    return np.asarray(fit[key]["real"], float) + 1j * np.asarray(fit[key]["imag"], float)


def profiled_residual(y: np.ndarray, x: np.ndarray) -> np.ndarray:
    r = complex(float(x[0]), float(x[1]))
    _, residual, _, _, _ = kernel.profile_linear_coefficients(y, ALL6, r)
    return np.concatenate((residual.real, residual.imag))


def fast_refit(y: np.ndarray, baseline_r: complex) -> tuple[np.ndarray, complex]:
    """Bounded three-start root refit with complex A,B profiled exactly."""
    starts = (
        np.asarray((baseline_r.real, baseline_r.imag), float),
        np.asarray((baseline_r.real + FAST_ROOT_PERTURB, baseline_r.imag), float),
        np.asarray((baseline_r.real - FAST_ROOT_PERTURB, baseline_r.imag), float),
    )
    best = None
    for x0 in starts:
        x0 = np.minimum(np.maximum(x0, ROOT_LOWER + 1e-10), ROOT_UPPER - 1e-10)
        opt = least_squares(
            lambda x: profiled_residual(y, x),
            x0,
            bounds=(ROOT_LOWER, ROOT_UPPER),
            xtol=3e-9,
            ftol=3e-9,
            gtol=3e-9,
            max_nfev=50,
        )
        residual = profiled_residual(y, opt.x)
        norm2 = float(np.dot(residual, residual))
        if best is None or norm2 < best[0]:
            best = (norm2, residual, complex(float(opt.x[0]), float(opt.x[1])))
    if best is None:
        raise RuntimeError("fast nonlinear refit failed")
    return best[1], best[2]


def full_refit_residual(y: np.ndarray) -> np.ndarray:
    fit = kernel.kernel_one_mode_fit(y, ALL6)
    return complex_from_fit(fit, "residual")


def analytic_lambda_required(nu: int) -> tuple[float, float]:
    critical = float(chi2.ppf(1.0 - ALPHA, nu))
    fun = lambda lam: 1.0 - ncx2.cdf(critical, nu, lam) - TARGET_POWER
    lam = float(brentq(fun, 0.0, 1000.0))
    return critical, lam


def summarize_statistic(x: np.ndarray) -> dict[str, float]:
    return {
        "mean": float(np.mean(x)),
        "median": float(np.median(x)),
        "q90": float(np.quantile(x, 0.90)),
        "q99": float(np.quantile(x, 0.99)),
        "q997": float(np.quantile(x, 0.997)),
        "max": float(np.max(x)),
    }


def run_ensemble(
    mean: np.ndarray,
    sigma: float,
    baseline_r: complex,
    n: int,
    seed: int,
) -> np.ndarray:
    rng = np.random.default_rng(seed)
    out = np.empty(n, float)
    for k in range(n):
        noise = sigma * (
            rng.standard_normal(len(mean)) + 1j * rng.standard_normal(len(mean))
        )
        y = mean + noise
        residual, _ = fast_refit(y, baseline_r)
        out[k] = float(np.vdot(residual, residual).real / sigma**2)
    return out


def spot_check_fast_refit(
    mean: np.ndarray,
    sigma: float,
    baseline_r: complex,
    seed: int,
    n: int = 6,
) -> dict[str, Any]:
    rng = np.random.default_rng(seed)
    ratios = []
    absolute = []
    for _ in range(n):
        y = mean + sigma * (
            rng.standard_normal(len(mean)) + 1j * rng.standard_normal(len(mean))
        )
        rf, _ = fast_refit(y, baseline_r)
        rfull = full_refit_residual(y)
        nf = float(np.linalg.norm(rf))
        ng = float(np.linalg.norm(rfull))
        ratios.append(nf / max(ng, np.finfo(float).tiny))
        absolute.append(nf - ng)
    return {
        "n": n,
        "max_fast_over_full_residual_norm_ratio": float(max(ratios)),
        "median_fast_over_full_residual_norm_ratio": float(np.median(ratios)),
        "max_absolute_residual_norm_excess": float(max(absolute)),
    }


def rf_gate(J: np.ndarray, kf: int) -> dict[str, Any]:
    f = float(base.FREQUENCIES[kf])
    y = np.asarray(J[kf], complex)
    fit = kernel.kernel_one_mode_fit(y, ALL6)
    null_mean = complex_from_fit(fit, "predicted")
    deterministic_residual = y - null_mean
    baseline_r = complex(fit["r_per_um"]["real"], fit["r_per_um"]["imag"])
    step = float(np.mean(np.abs(np.diff(y))))
    residual_norm = float(np.linalg.norm(deterministic_residual))

    nu = 2 * len(y) - 6
    analytic_critical, lambda_required = analytic_lambda_required(nu)
    analytic_snr = np.sqrt(lambda_required) * step / residual_norm
    analytic_snr_db = float(20.0 * np.log10(analytic_snr))
    grid_db = [analytic_snr_db + x for x in SNR_OFFSETS_DB]

    rows = []
    for j, snr_db in enumerate(grid_db):
        sigma = step / 10.0 ** (snr_db / 20.0)
        seed_null = int(100000 + kf * 10000 + j * 100)
        seed_alt = int(200000 + kf * 10000 + j * 100)
        print(
            f"bootstrap f={f/1e6:.0f} MHz snr={snr_db:.3f} dB "
            f"null={N_NULL} alt={N_ALT}",
            flush=True,
        )
        tnull = run_ensemble(null_mean, sigma, baseline_r, N_NULL, seed_null)
        talt = run_ensemble(y, sigma, baseline_r, N_ALT, seed_alt)
        empirical_critical = float(
            np.quantile(tnull, 1.0 - ALPHA, method="higher")
        )
        empirical_power = float(np.mean(talt > empirical_critical))
        power_se = float(np.sqrt(empirical_power * (1.0 - empirical_power) / N_ALT))
        analytic_null_exceedance = float(np.mean(tnull > analytic_critical))
        rows.append(
            {
                "snr_db": float(snr_db),
                "sigma_over_step": float(sigma / step),
                "null_seed": seed_null,
                "alternative_seed": seed_alt,
                "empirical_null_critical": empirical_critical,
                "analytic_chi_square_critical": analytic_critical,
                "empirical_null_exceedance_at_analytic_critical": analytic_null_exceedance,
                "null_statistic": summarize_statistic(tnull),
                "empirical_alternative_power": empirical_power,
                "power_monte_carlo_standard_error": power_se,
            }
        )

    passing = [r for r in rows if r["empirical_alternative_power"] >= TARGET_POWER]
    lowest_passing = None if not passing else min(r["snr_db"] for r in passing)
    claim_snr = float(base.GRADIENT_SNR_DB[f])
    early_warning = lowest_passing is not None and lowest_passing <= claim_snr

    # Fixed spot check at the central analytic candidate, for both null and alt.
    central = rows[2]
    sigma_c = step / 10.0 ** (central["snr_db"] / 20.0)
    spot_null = spot_check_fast_refit(
        null_mean, sigma_c, baseline_r, seed=300000 + kf * 1000
    )
    spot_alt = spot_check_fast_refit(
        y, sigma_c, baseline_r, seed=400000 + kf * 1000
    )

    return {
        "frequency_hz": f,
        "step_amplitude": step,
        "deterministic_one_mode_residual_norm": residual_norm,
        "deterministic_contrast_normalized_residual": float(
            fit["contrast_normalized_residual"]
        ),
        "baseline_fit_root_per_um": {
            "real": baseline_r.real,
            "imag": baseline_r.imag,
        },
        "regular_residual_dof": nu,
        "analytic": {
            "alpha": ALPHA,
            "target_power": TARGET_POWER,
            "chi_square_critical": analytic_critical,
            "required_noncentrality": lambda_required,
            "required_snr_db": analytic_snr_db,
        },
        "bootstrap_rows": rows,
        "lowest_tested_snr_with_power_ge_0p90_db": lowest_passing,
        "frozen_transport_claim_snr_db": claim_snr,
        "predeclared_early_warning_condition_supported": bool(early_warning),
        "conservative_tested_warning_margin_db": (
            None if lowest_passing is None else float(claim_snr - lowest_passing)
        ),
        "fast_refit_spot_checks_at_analytic_snr": {
            "null": spot_null,
            "alternative": spot_alt,
        },
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("paper03_stageA_statistical_bootstrap.json"),
    )
    args = p.parse_args()

    finite = next(s for s in base.SCENARIOS if s.name == "finite75_depletion")
    J, forward = kernel.build_fixed_field_case(
        finite,
        nx=201,
        nz=151,
        nx_src=17,
        diffusion_m2_s=2.5e-3,
        lifetime_s=float("inf"),
    )

    gates = [rf_gate(J, kf) for kf in (1, 2, 3)]

    # Spot-check requirement: the fast high-SNR local refit must agree closely
    # with the full multistart fitter. This tolerance is an implementation gate,
    # not a scientific threshold.
    for g in gates:
        for check in g["fast_refit_spot_checks_at_analytic_snr"].values():
            if check["max_fast_over_full_residual_norm_ratio"] > 1.001:
                raise AssertionError(
                    "fast bootstrap refit disagrees with full multistart fitter"
                )

    result = {
        "schema": "paper03-stageA-statistical-bootstrap-v1",
        "status": "PREDECLARED PARAMETRIC BOOTSTRAP RESULT / NON-CLAIM",
        "predeclaration": "PAPER03_STAGEA_STATISTICAL_PREDECLARATION_2026-08-17.md",
        "noise_convention": {
            "equation": "n=sigma*(xi_R+i*xi_I), xi_R,xi_I iid N(0,1)",
            "sigma_definition": "standard deviation of each real and imaginary current quadrature",
            "step_definition": "mean absolute adjacent difference across all six deterministic channels",
            "snr_definition": "20*log10(step/sigma)",
            "complex_rms_conversion_warning": "a complex-RMS convention differs by sqrt(2), approximately 3.01 dB",
        },
        "bootstrap": {
            "alpha": ALPHA,
            "target_power": TARGET_POWER,
            "n_null_per_candidate": N_NULL,
            "n_alternative_per_candidate": N_ALT,
            "snr_offsets_from_analytic_db": list(SNR_OFFSETS_DB),
            "empirical_null_quantile_method": "higher",
        },
        "forward": {
            "stage_B_self_consistent_semiconductor": False,
            "scenario": finite.__dict__,
            "diffusion_m2_s": 2.5e-3,
            "lifetime_s": "inf",
            "grid": [201, 151],
            "lateral_quadrature": 17,
            "diagnostics": forward,
        },
        "rf_gates": gates,
        "all_three_predeclared_early_warning_conditions_supported": bool(
            all(g["predeclared_early_warning_condition_supported"] for g in gates)
        ),
        "science_interpretation_ready": False,
        "remaining_before_interpretation": [
            "inspect bootstrap calibration and finite-sample uncertainty",
            "broader geometry/diffusion/lifetime regime map",
            "second geometry family",
            "stochastic coarse-observable cross-formulation validation",
            "Stage-B self-consistent semiconductor validation",
            "focused prior-art audit",
        ],
    }

    args.output.write_text(
        json.dumps(resolvent.json_safe(result), indent=2, allow_nan=False) + "\n",
        encoding="utf-8",
    )

    for g in gates:
        print(
            f"{g['frequency_hz']/1e6:.0f} MHz: analytic={g['analytic']['required_snr_db']:.3f} dB, "
            f"lowest tested >=90%={g['lowest_tested_snr_with_power_ge_0p90_db']}, "
            f"claim={g['frozen_transport_claim_snr_db']:.3f} dB, "
            f"early={g['predeclared_early_warning_condition_supported']}"
        )
        for row in g["bootstrap_rows"]:
            print(
                f"  {row['snr_db']:.3f} dB: power={row['empirical_alternative_power']:.4f} "
                f"crit={row['empirical_null_critical']:.3f} "
                f"null@analytic={row['empirical_null_exceedance_at_analytic_critical']:.4f}"
            )
        print(json.dumps(g["fast_refit_spot_checks_at_analytic_snr"], indent=2))
    print(
        "all_three_predeclared_early_warning_conditions_supported =",
        result["all_three_predeclared_early_warning_conditions_supported"],
    )
    print("science_interpretation_ready = false")
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
