"""Covariance-geometry stress test for Paper 02.

Purpose
-------
The canonical same-frequency and multi-frequency discrimination calculations use
independent, equal real/imaginary quadrature noise.  This script asks which
conclusions survive when the measurement covariance is anisotropic or
correlated, while keeping the optical kernels and deterministic forward model
unchanged.

The calculation is deliberately split from kernel/model uncertainty.  Here the
forward model and inverse use the same theoretical generation kernels.  Only
the measurement metric changes.

Same-frequency calculation
--------------------------
For each covariance shape R (normalized to unit mean quadrature variance), the
one-mode model

    J_m = C + K F_m(r)

is re-fit by generalized least squares.  This matters because the deterministic
pseudo-true root of a misspecified model can itself depend on the metric.  The
script then computes, under the same R,

  * positive-D detection SNR;
  * one-mode-rejection SNR;
  * the hidden-risk ordering;
  * the covariance condition number and root uncertainty.

The channel-SNR convention is

    S = RMS_m |J_m| / sigma_bar,

where sigma_bar^2 is the mean diagonal quadrature variance.  Every covariance
shape is normalized so mean(diag(R)) = 1, making S directly comparable across
cases.

Multi-frequency calculation
---------------------------
The fitted root covariance at each RF point is first propagated from the full
six-channel generalized least-squares fit.  Cross-frequency correlation is then
introduced in standardized root coordinates while preserving every marginal
2x2 root covariance.  The wrong homogeneous D,w law is re-fit using the full
covariance, and the SNR for 90% rejection power at alpha=0.0027 is recomputed.

Scientific scope
----------------
This is a theoretical robustness test of the declared surrogate.  The covariance
families are controlled stress directions, not claims about a particular
instrument.  Kernel uncertainty is intentionally excluded and handled in a
separate calculation.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np
from scipy.linalg import block_diag
from scipy.optimize import least_squares, brentq
from scipy.stats import chi2, ncx2, norm

import realistic_geometry_closure_stress as base
import paper02_geometry_parameter_sweep as sweep
from paper02_kernel_aware_depletion_frequency_law import (
    kernel_aware_root,
    kernel_basis,
)
from paper02_bias_bound_linearization import (
    kernel_basis_derivative,
    diffusion_gradient,
)
from paper02_end_to_end_rejection_snr import (
    gamma_dd,
    solve_dw_from_gamma,
)


SAME_FREQUENCIES = np.asarray((100e6, 500e6, 1e9), dtype=float)
MULTI_FREQUENCIES = np.asarray(
    (100e6, 200e6, 300e6, 500e6, 750e6, 1e9, 1.5e9, 2e9, 3e9),
    dtype=float,
)
FORWARD_FREQUENCIES = np.concatenate((np.asarray((0.0,)), MULTI_FREQUENCIES))
ALPHA = 0.0027
POWER = 0.90
NU_CHANNEL = 6
N_CHANNEL = 6


def real_stack(z: np.ndarray) -> np.ndarray:
    z = np.asarray(z, dtype=complex)
    return np.concatenate((z.real, z.imag))


def normalize_mean_variance(R: np.ndarray) -> np.ndarray:
    """Normalize a symmetric covariance shape to mean diagonal variance 1."""
    R = np.asarray(R, dtype=float)
    R = 0.5 * (R + R.T)
    scale = float(np.mean(np.diag(R)))
    if not np.isfinite(scale) or scale <= 0:
        raise ValueError("invalid covariance normalization")
    R = R / scale
    eig = np.linalg.eigvalsh(R)
    if float(np.min(eig)) <= 1e-10:
        raise ValueError(f"covariance not safely positive definite: min eig={np.min(eig)}")
    return R


def full_from_channel_cov(Rch: np.ndarray, quadrature_corr: float = 0.0) -> np.ndarray:
    """Return 12x12 covariance in [Re channels, Im channels] ordering."""
    Rch = np.asarray(Rch, dtype=float)
    q = float(quadrature_corr)
    if abs(q) >= 1.0:
        raise ValueError("quadrature correlation must satisfy |q|<1")
    top = np.hstack((Rch, q * Rch))
    bot = np.hstack((q * Rch, Rch))
    return normalize_mean_variance(np.vstack((top, bot)))


def ar1_channel(rho: float) -> np.ndarray:
    idx = np.arange(N_CHANNEL)
    return np.asarray(rho ** np.abs(idx[:, None] - idx[None, :]), dtype=float)


def equicorr_channel(rho: float) -> np.ndarray:
    return (1.0 - rho) * np.eye(N_CHANNEL) + rho * np.ones((N_CHANNEL, N_CHANNEL))


def lowrank_channel(mode: np.ndarray, strength: float) -> np.ndarray:
    u = np.asarray(mode, dtype=float)
    u = u / np.linalg.norm(u)
    return np.eye(N_CHANNEL) + float(strength) * np.outer(u, u)


def covariance_cases() -> list[dict]:
    m = np.arange(N_CHANNEL, dtype=float)
    common = np.ones(N_CHANNEL)
    slope = m - np.mean(m)
    curvature = slope**2
    curvature -= np.mean(curvature)

    cases = [
        {"name": "iid", "family": "iid", "parameter": 0.0, "R": np.eye(2 * N_CHANNEL)},
    ]
    for rho in (0.25, 0.50, 0.80):
        cases.append(
            {
                "name": f"equicorr_rho_{rho:.2f}",
                "family": "channel_equicorrelation",
                "parameter": rho,
                "R": full_from_channel_cov(equicorr_channel(rho)),
            }
        )
        cases.append(
            {
                "name": f"ar1_rho_{rho:.2f}",
                "family": "channel_AR1",
                "parameter": rho,
                "R": full_from_channel_cov(ar1_channel(rho)),
            }
        )

    # Low-rank directions separate exact/near tangent noise from normal-like
    # spectral structure.  strength=9 gives a 10:1 eigenvalue ratio before the
    # equal-average-variance normalization.
    for label, mode in (("common", common), ("slope", slope), ("curvature", curvature)):
        cases.append(
            {
                "name": f"lowrank_{label}_q9",
                "family": f"lowrank_{label}",
                "parameter": 9.0,
                "R": full_from_channel_cov(lowrank_channel(mode, 9.0)),
            }
        )

    for q in (-0.50, 0.50):
        cases.append(
            {
                "name": f"quadrature_corr_{q:+.2f}",
                "family": "real_imag_correlation",
                "parameter": q,
                "R": full_from_channel_cov(np.eye(N_CHANNEL), quadrature_corr=q),
            }
        )
    return cases


def weighted_linear_fit(y: np.ndarray, r_per_m: complex, L: np.ndarray):
    F = kernel_basis(r_per_m)
    derivs = (
        np.ones(len(F), dtype=complex),
        1j * np.ones(len(F), dtype=complex),
        F,
        1j * F,
    )
    A = np.column_stack([real_stack(d) for d in derivs])
    yr = real_stack(y)
    Aw = np.linalg.solve(L, A)
    yw = np.linalg.solve(L, yr)
    beta, *_ = np.linalg.lstsq(Aw, yw, rcond=None)
    model_r = A @ beta
    model = model_r[:N_CHANNEL] + 1j * model_r[N_CHANNEL:]
    C = complex(beta[0], beta[1])
    K = complex(beta[2], beta[3])
    return C, K, model, yr - model_r


def weighted_kernel_root(y: np.ndarray, R: np.ndarray):
    """Generalized-LS one-mode fit with C,K profiled at every complex r."""
    R = normalize_mean_variance(R)
    L = np.linalg.cholesky(R)
    r0, _coeff0, _model0, _fit0 = kernel_aware_root(y)
    rho0 = r0 * 1e-6
    rms = max(float(np.sqrt(np.mean(np.abs(y) ** 2))), 1e-30)

    def residual(x):
        r = (x[0] + 1j * x[1]) / 1e-6
        _C, _K, _model, e = weighted_linear_fit(y, r, L)
        return np.linalg.solve(L, e) / rms

    fit = least_squares(
        residual,
        np.asarray((rho0.real, rho0.imag), dtype=float),
        xtol=1e-13,
        ftol=1e-13,
        gtol=1e-13,
        max_nfev=4000,
    )
    r = (fit.x[0] + 1j * fit.x[1]) / 1e-6
    C, K, model, e = weighted_linear_fit(y, r, L)
    ew = np.linalg.solve(L, e)
    fit_rel_weighted = float(np.linalg.norm(ew) / (rms * np.sqrt(2 * N_CHANNEL)))
    return r, C, K, model, e, fit_rel_weighted


def full_real_jacobian(C: complex, K: complex, r: complex) -> np.ndarray:
    F = kernel_basis(r)
    Fr = kernel_basis_derivative(r)
    derivs = (
        np.ones(len(F), dtype=complex),
        1j * np.ones(len(F), dtype=complex),
        F,
        1j * F,
        K * Fr,
        1j * K * Fr,
    )
    return np.column_stack([real_stack(d) for d in derivs])


def lambda_required(nu: int, alpha: float = ALPHA, power: float = POWER):
    threshold = float(chi2.ppf(1.0 - alpha, nu))

    def objective(lam):
        return float(ncx2.sf(threshold, nu, lam) - power)

    hi = 10.0
    while objective(hi) < 0.0:
        hi *= 2.0
        if hi > 1e8:
            raise RuntimeError("failed to bracket required noncentrality")
    lam = float(brentq(objective, 0.0, hi, xtol=1e-13, rtol=1e-13))
    return threshold, lam


def same_frequency_row(J: np.ndarray, f: float, case: dict) -> dict:
    R = case["R"]
    r, C, K, model, e, fit_rel_w = weighted_kernel_root(J, R)
    gamma = -r
    D, w = solve_dw_from_gamma(gamma, f)
    rms = float(np.sqrt(np.mean(np.abs(J) ** 2)))
    Sigma1 = rms**2 * R
    W1 = np.linalg.inv(Sigma1)

    er = real_stack(J - model)
    lambda1 = float(er @ W1 @ er)
    threshold, lambda_req = lambda_required(NU_CHANNEL)
    snr_reject = float(np.sqrt(lambda_req / lambda1)) if lambda1 > 0 else float("inf")

    G = full_real_jacobian(C, K, r)
    fisher = G.T @ W1 @ G
    cov_param1 = np.linalg.inv(fisher)
    cov_gamma1 = cov_param1[4:6, 4:6]
    dD_da, dD_db = diffusion_gradient(gamma)
    grad_D = np.asarray((dD_da, dD_db), dtype=float)
    sigma_D1 = float(np.sqrt(grad_D @ cov_gamma1 @ grad_D))
    z_req = float(norm.ppf(1.0 - ALPHA) + norm.ppf(POWER))
    snr_D = float(z_req * sigma_D1 / D) if D > 0 else float("inf")

    eig_cov = np.linalg.eigvalsh(R)
    eig_root = np.linalg.eigvalsh(cov_gamma1)
    return {
        "case": case["name"],
        "family": case["family"],
        "parameter": float(case["parameter"]),
        "frequency_hz": float(f),
        "cov_condition": float(np.max(eig_cov) / np.min(eig_cov)),
        "D_eff_m2_per_s": float(D),
        "w_eff_m_per_s": float(w),
        "weighted_fit_rel": fit_rel_w,
        "lambda_model_at_snr1": lambda1,
        "snr_required_one_mode_rejection": snr_reject,
        "snr_required_one_mode_rejection_db": float(20.0 * np.log10(snr_reject)) if np.isfinite(snr_reject) else float("inf"),
        "sigma_D_at_snr1_m2_per_s": sigma_D1,
        "root_sigma_major_at_snr1_per_m": float(np.sqrt(np.max(eig_root))),
        "root_sigma_minor_at_snr1_per_m": float(np.sqrt(np.min(eig_root))),
        "snr_required_positive_D": snr_D,
        "snr_required_positive_D_db": float(20.0 * np.log10(snr_D)) if np.isfinite(snr_D) else float("inf"),
        "hidden_risk_ratio_Sreject_over_SD": float(snr_reject / snr_D) if np.isfinite(snr_D) else 0.0,
        "positive_D_detectable_before_one_mode_rejection": bool(snr_D < snr_reject),
        "chi2_threshold": threshold,
        "lambda_required": lambda_req,
    }


def standardized_root_covariance(cov_blocks: list[np.ndarray], Rf: np.ndarray) -> np.ndarray:
    """Preserve each 2x2 marginal while imposing correlation in whitened root coordinates."""
    Ls = [np.linalg.cholesky(c) for c in cov_blocks]
    D = block_diag(*Ls)
    core = np.kron(Rf, np.eye(2))
    return D @ core @ D.T


def fit_homogeneous_full_cov(frequencies, gammas, Cfull):
    L = np.linalg.cholesky(Cfull)
    y = np.empty(2 * len(gammas), dtype=float)
    y[0::2] = np.real(gammas)
    y[1::2] = np.imag(gammas)

    D0, w0 = solve_dw_from_gamma(gammas[0], frequencies[0])
    D0 = max(D0, 1e-10)
    w0 = max(w0, 1.0)

    def residual(logp):
        D, w = np.exp(logp)
        gm = gamma_dd(frequencies, D, w)
        m = np.empty_like(y)
        m[0::2] = gm.real
        m[1::2] = gm.imag
        return np.linalg.solve(L, y - m)

    fit = least_squares(
        residual,
        np.log((D0, w0)),
        xtol=1e-13,
        ftol=1e-13,
        gtol=1e-13,
        max_nfev=5000,
    )
    D, w = np.exp(fit.x)
    rw = residual(fit.x)
    return float(D), float(w), float(rw @ rw)


def frequency_correlation_cases(n: int) -> list[dict]:
    idx = np.arange(n)
    out = [{"name": "freq_independent", "family": "frequency_iid", "parameter": 0.0, "R": np.eye(n)}]
    for rho in (0.25, 0.50, 0.80):
        out.append(
            {
                "name": f"freq_ar1_rho_{rho:.2f}",
                "family": "frequency_AR1",
                "parameter": rho,
                "R": rho ** np.abs(idx[:, None] - idx[None, :]),
            }
        )
        out.append(
            {
                "name": f"freq_equicorr_rho_{rho:.2f}",
                "family": "frequency_equicorrelation",
                "parameter": rho,
                "R": (1.0 - rho) * np.eye(n) + rho * np.ones((n, n)),
            }
        )
    return out


def multi_frequency_rows(J_by_f: np.ndarray) -> list[dict]:
    # First propagate the canonical IID channel covariance into each fitted root.
    gammas = []
    covs = []
    for J in J_by_f:
        r, C, K, _model, _e, _fit = weighted_kernel_root(J, np.eye(2 * N_CHANNEL))
        gamma = -r
        rms = float(np.sqrt(np.mean(np.abs(J) ** 2)))
        G = full_real_jacobian(C, K, r)
        W1 = np.eye(2 * N_CHANNEL) / (rms**2)
        cov = np.linalg.inv(G.T @ W1 @ G)[4:6, 4:6]
        gammas.append(gamma)
        covs.append(cov)
    gammas = np.asarray(gammas, dtype=complex)

    rows = []
    for n in range(2, len(MULTI_FREQUENCIES) + 1):
        fs = MULTI_FREQUENCIES[:n]
        gs = gammas[:n]
        cs = covs[:n]
        nu = 2 * n - 2
        qcrit, lam_req = lambda_required(nu)
        for case in frequency_correlation_cases(n):
            Cfull = standardized_root_covariance(cs, case["R"])
            D, w, lam1 = fit_homogeneous_full_cov(fs, gs, Cfull)
            snr = float(np.sqrt(lam_req / lam1)) if lam1 > 0 else float("inf")
            rows.append(
                {
                    "case": case["name"],
                    "family": case["family"],
                    "parameter": float(case["parameter"]),
                    "max_frequency_hz": float(fs[-1]),
                    "n_complex_frequencies": int(n),
                    "dof": int(nu),
                    "best_fit_D_m2_per_s": D,
                    "best_fit_w_m_per_s": w,
                    "lambda_at_snr1": lam1,
                    "chi2_threshold": qcrit,
                    "lambda_required": lam_req,
                    "required_rms_channel_snr": snr,
                    "required_rms_channel_snr_db": float(20.0 * np.log10(snr)) if np.isfinite(snr) else float("inf"),
                }
            )
    return rows


def summarize_same(rows: list[dict]) -> dict:
    iid = {(r["frequency_hz"]): r for r in rows if r["case"] == "iid"}
    summary = {}
    for f in SAME_FREQUENCIES:
        rr = [r for r in rows if r["frequency_hz"] == float(f)]
        base_row = iid[float(f)]
        hidden = [r["case"] for r in rr if r["positive_D_detectable_before_one_mode_rejection"]]
        summary[str(int(f))] = {
            "iid": {
                "S_D_db": base_row["snr_required_positive_D_db"],
                "S_reject_db": base_row["snr_required_one_mode_rejection_db"],
                "hidden_risk": base_row["positive_D_detectable_before_one_mode_rejection"],
            },
            "hidden_risk_cases": hidden,
            "min_S_D_db": float(min(r["snr_required_positive_D_db"] for r in rr)),
            "max_S_D_db": float(max(r["snr_required_positive_D_db"] for r in rr)),
            "min_S_reject_db": float(min(r["snr_required_one_mode_rejection_db"] for r in rr)),
            "max_S_reject_db": float(max(r["snr_required_one_mode_rejection_db"] for r in rr)),
            "D_eff_range_m2_per_s": [
                float(min(r["D_eff_m2_per_s"] for r in rr)),
                float(max(r["D_eff_m2_per_s"] for r in rr)),
            ],
        }
    return summary


def summarize_multi(rows: list[dict]) -> dict:
    out = {}
    for fmax in sorted(set(r["max_frequency_hz"] for r in rows)):
        rr = [r for r in rows if r["max_frequency_hz"] == fmax]
        iid = next(r for r in rr if r["case"] == "freq_independent")
        out[str(int(fmax))] = {
            "iid_required_snr_db": iid["required_rms_channel_snr_db"],
            "min_required_snr_db": float(min(r["required_rms_channel_snr_db"] for r in rr)),
            "max_required_snr_db": float(max(r["required_rms_channel_snr_db"] for r in rr)),
            "worst_case": max(rr, key=lambda r: r["required_rms_channel_snr_db"])["case"],
            "best_case": min(rr, key=lambda r: r["required_rms_channel_snr_db"])["case"],
        }
    return out


def run(args):
    old_freq = base.FREQUENCIES
    base.FREQUENCIES = FORWARD_FREQUENCIES.copy()
    base.V_BIAS = float(args.bias_v)
    base.X_EXTENT_UM = float(args.x_extent_um)
    scenario = base.Scenario("planar_depletion", 1.0, 3.0, 0.05)
    numerical = {
        "nx": args.nx,
        "nz": args.nz,
        "nx_src": args.nx_src,
        "nz_src": args.nz_src,
        "ds_um": args.ds_um,
    }

    try:
        J_forward, diag = sweep.currents_with_beam(scenario, 2.0, 0.0, **numerical)
    finally:
        base.FREQUENCIES = old_freq

    J_rf = J_forward[1:]
    f_to_index = {float(f): i for i, f in enumerate(MULTI_FREQUENCIES)}
    cases = covariance_cases()
    same_rows = []
    for f in SAME_FREQUENCIES:
        J = J_rf[f_to_index[float(f)]]
        for case in cases:
            same_rows.append(same_frequency_row(J, float(f), case))

    multi_rows = multi_frequency_rows(J_rf)

    payload = {
        "status": "CHECKED covariance-geometry stress for Paper 02 theoretical reference model",
        "scope": {
            "measurement_covariance_only": True,
            "optical_kernel_uncertainty_included": False,
            "forward_and_inverse_use_same_theoretical_kernels": True,
            "covariance_families_are_stress_directions_not_instrument_claims": True,
        },
        "test": {
            "alpha": ALPHA,
            "power": POWER,
            "snr_definition": "S = RMS_m |J_m| / sqrt(mean quadrature variance)",
            "mean_quadrature_variance_normalized_across_same_frequency_cases": True,
        },
        "device_stress": {
            "microscopic_D": 0.0,
            "recombination": 0.0,
            "contact_fraction": 1.0,
            "depletion_width_um": 3.0,
            "poisson_curvature_parameter_delta_v": 0.05,
            "bias_v": float(args.bias_v),
            "collection_fraction": float(diag["collected"]),
            "dc_ramo_error": float(diag["dc_error"]),
        },
        "numerical": numerical,
        "same_frequency_summary": summarize_same(same_rows),
        "multi_frequency_summary": summarize_multi(multi_rows),
        "same_frequency_rows": same_rows,
        "multi_frequency_rows": multi_rows,
    }

    out_same = Path(args.output_same)
    out_multi = Path(args.output_multi)
    out_json = Path(args.output_summary)
    for p in (out_same, out_multi, out_json):
        p.parent.mkdir(parents=True, exist_ok=True)

    with out_same.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(same_rows[0].keys()))
        w.writeheader()
        w.writerows(same_rows)
    with out_multi.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(multi_rows[0].keys()))
        w.writeheader()
        w.writerows(multi_rows)
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
    p.add_argument("--output-same", default="paper02_covariance_geometry_same_frequency.csv")
    p.add_argument("--output-multi", default="paper02_covariance_geometry_multi_frequency.csv")
    p.add_argument("--output-summary", default="paper02_covariance_geometry_summary.json")
    return p


if __name__ == "__main__":
    run(parser().parse_args())
