"""Same-frequency hidden-risk test for Paper 02.

A small deterministic residual relative to the full six-channel vector is not by
itself a model-acceptance statement.  This script puts the one-mode goodness-of-
fit test and the positive-D detection test on the same explicit theoretical
noise scale.

Noise model:
  * six complex spectral channels at one RF frequency;
  * independent equal Gaussian noise in every real/imag quadrature;
  * S = RMS_m |J_m| / sigma_quadrature.

At each frequency the kernel-aware one-mode model has three complex parameters
(C,K,r): 6 real parameters fit to 12 real observations, leaving nu=6 local
residual degrees of freedom.

We compute:
  1. S_reject: RMS-channel SNR required for 90% power to reject the one-mode
     channel manifold at alpha=0.0027, using the exact fitted deterministic
     residual as the noncentral alternative;
  2. S_D: RMS-channel SNR required for 90% power in an idealized one-sided
     Gaussian test of D>0 against D=0 at the same alpha, propagating the full
     12x6 channel Jacobian into the fitted complex root and then D(gamma).

If S_D < S_reject, a positive apparent D can become statistically significant
before the same-frequency one-mode model is rejectable: a genuine hidden-risk
ordering under this noise model.  If S_reject <= S_D, the same-frequency model
check warns at least as early and the paper must weaken that claim.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np
from scipy.stats import chi2, ncx2, norm
from scipy.optimize import brentq

import realistic_geometry_closure_stress as base
import paper02_geometry_parameter_sweep as sweep
from paper02_kernel_aware_depletion_frequency_law import kernel_aware_root
from paper02_end_to_end_rejection_snr import (
    complex_model_real_jacobian,
    solve_dw_from_gamma,
)
from paper02_bias_bound_linearization import diffusion_gradient


FREQUENCIES = np.asarray((100e6, 500e6, 1e9), dtype=float)
ALPHA = 0.0027
POWER = 0.90
NU_CHANNEL = 6


def lambda_required(nu: int, alpha=ALPHA, power=POWER) -> tuple[float, float]:
    threshold = float(chi2.ppf(1.0 - alpha, nu))

    def objective(lam):
        return float(ncx2.sf(threshold, nu, lam) - power)

    hi = 10.0
    while objective(hi) < 0.0:
        hi *= 2.0
        if hi > 1e7:
            raise RuntimeError("failed to bracket required noncentrality")
    lam = float(brentq(objective, 0.0, hi, xtol=1e-13, rtol=1e-13))
    return threshold, lam


def analyze_one(J: np.ndarray, f: float) -> dict:
    r, coeff, model, fit_rel = kernel_aware_root(J)
    C, K = coeff
    gamma = -r
    D, w = solve_dw_from_gamma(gamma, f)

    rms_channel = float(np.sqrt(np.mean(np.abs(J) ** 2)))
    residual = np.asarray(J - model, dtype=complex)
    residual_norm = float(np.linalg.norm(residual))

    # At S=1, sigma_quadrature = rms_channel.
    lambda_channel_snr1 = residual_norm**2 / (rms_channel**2)
    chi2_threshold, lambda_req = lambda_required(NU_CHANNEL)
    if lambda_channel_snr1 > 0:
        snr_reject = float(np.sqrt(lambda_req / lambda_channel_snr1))
    else:
        snr_reject = float("inf")

    # Root covariance at S=1 from the full real 12x6 local channel Jacobian.
    G = complex_model_real_jacobian(C, K, r)
    cov_param_snr1 = rms_channel**2 * np.linalg.inv(G.T @ G)
    cov_gamma_snr1 = cov_param_snr1[4:6, 4:6]

    dD_da, dD_db = diffusion_gradient(gamma)
    grad_D = np.asarray((dD_da, dD_db), dtype=float)
    sigma_D_snr1 = float(np.sqrt(grad_D @ cov_gamma_snr1 @ grad_D))

    # Idealized one-sided Gaussian D>0 test with the same alpha and power.
    # For estimator mean D and sigma=sigma_D_snr1/S, required standardized
    # separation is z_(1-alpha)+z_power.
    z_req = float(norm.ppf(1.0 - ALPHA) + norm.ppf(POWER))
    if D > 0:
        snr_D = float(z_req * sigma_D_snr1 / D)
    else:
        snr_D = float("inf")

    return {
        "frequency_hz": float(f),
        "D_eff_m2_per_s": float(D),
        "w_eff_m_per_s": float(w),
        "kernel_fit_rel_full_vector": float(fit_rel),
        "rms_channel": rms_channel,
        "residual_norm": residual_norm,
        "lambda_channel_at_snr1": float(lambda_channel_snr1),
        "channel_residual_dof": NU_CHANNEL,
        "chi2_reject_threshold": chi2_threshold,
        "lambda_required_90pct_power": lambda_req,
        "snr_required_one_mode_rejection": snr_reject,
        "snr_required_one_mode_rejection_db": float(20.0 * np.log10(snr_reject)),
        "sigma_D_at_channel_snr1_m2_per_s": sigma_D_snr1,
        "one_sided_z_separation_required": z_req,
        "snr_required_positive_D": snr_D,
        "snr_required_positive_D_db": float(20.0 * np.log10(snr_D)) if np.isfinite(snr_D) else float("inf"),
        "hidden_risk_ratio_Sreject_over_SD": float(snr_reject / snr_D) if np.isfinite(snr_D) else 0.0,
        "positive_D_detectable_before_one_mode_rejection": bool(snr_D < snr_reject),
    }


def run(args):
    old_freq = base.FREQUENCIES
    base.FREQUENCIES = np.concatenate((np.asarray((0.0,)), FREQUENCIES))
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
        J_forward, diag = sweep.currents_with_beam(
            scenario, 2.0, 0.0, **numerical
        )
        J = J_forward[1:]
        rows = [analyze_one(j, f) for j, f in zip(J, FREQUENCIES)]
    finally:
        base.FREQUENCIES = old_freq

    row100 = rows[0]
    payload = {
        "status": "CHECKED same-frequency hidden-risk ordering under explicit theoretical noise model",
        "noise_model": {
            "channels": 6,
            "complex_channels": True,
            "independent_equal_real_imag_quadrature_noise": True,
            "snr_definition": "S = RMS_m |J_m| / sigma_quadrature",
            "alpha": ALPHA,
            "power": POWER,
        },
        "device": {
            "contact_fraction": 1.0,
            "depletion_width_um": 3.0,
            "space_charge_drop_v": 0.05,
            "bias_v": float(args.bias_v),
            "microscopic_D": 0.0,
            "recombination": 0.0,
            "collection_fraction": float(diag["collected"]),
            "dc_ramo_error": float(diag["dc_error"]),
        },
        "central_100mhz_ordering": {
            "snr_positive_D": row100["snr_required_positive_D"],
            "snr_one_mode_rejection": row100["snr_required_one_mode_rejection"],
            "ratio_rejection_to_D_detection": row100["hidden_risk_ratio_Sreject_over_SD"],
            "positive_D_detectable_first": row100["positive_D_detectable_before_one_mode_rejection"],
        },
        "rows": rows,
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


def parser():
    p = argparse.ArgumentParser()
    p.add_argument("--bias-v", type=float, default=0.30)
    p.add_argument("--x-extent-um", type=float, default=3.5)
    p.add_argument("--nx", type=int, default=121)
    p.add_argument("--nz", type=int, default=91)
    p.add_argument("--nx-src", type=int, default=13)
    p.add_argument("--nz-src", type=int, default=41)
    p.add_argument("--ds-um", type=float, default=0.020)
    p.add_argument("--output-csv", default="paper02_same_frequency_hidden_risk.csv")
    p.add_argument("--output-summary", default="paper02_same_frequency_hidden_risk_summary.json")
    return p


if __name__ == "__main__":
    run(parser().parse_args())
