"""End-to-end theoretical SNR requirement for rejecting the Paper-02 confound.

This calculation closes the loop from six complex spectral-channel measurements
through the calibrated one-mode root estimator and then through a joint
homogeneous drift-diffusion fit across RF frequency.

Noise model (explicitly theoretical): at each RF frequency, every channel has
independent Gaussian noise with equal standard deviation in its real and
imaginary quadratures.  The quoted channel SNR S is

    S = RMS_m |J_m| / sigma_quadrature

at each frequency.  The same S is assumed at every included RF frequency.
Different experimental covariance models can be substituted later.

For S=1 we compute the real 12x6 Jacobian of the calibrated one-mode channel
model with respect to Re/Im(C,K,r).  This gives the 2x2 covariance of the fitted
complex root after profiling C and K.  Because covariance scales as 1/S^2, the
noncentrality for model rejection scales as S^2.

For each cumulative RF band beginning at 100 MHz, D and w are jointly re-fit to
the deterministic zero-diffusion planar-depletion roots under the propagated
covariance.  The minimized Mahalanobis distance is the alternative
noncentrality at S=1.  We then solve for the SNR required to obtain 90% power at
alpha=0.0027 using the corresponding noncentral chi-square distribution.

The forward solve includes DC only so that the existing exact Ramo-consistency
diagnostic remains meaningful.  DC is not included in the RF statistical fit.

This is a model-based theoretical design example, not an instrument claim.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np
from scipy.linalg import block_diag
from scipy.optimize import least_squares, brentq
from scipy.stats import chi2, ncx2

import realistic_geometry_closure_stress as base
import paper02_geometry_parameter_sweep as sweep
from paper02_kernel_aware_depletion_frequency_law import kernel_aware_root, kernel_basis
from paper02_bias_bound_linearization import kernel_basis_derivative


FREQUENCIES = np.asarray(
    (100e6, 200e6, 300e6, 500e6, 750e6, 1e9, 1.5e9, 2e9, 3e9),
    dtype=float,
)
FORWARD_FREQUENCIES = np.concatenate((np.asarray((0.0,)), FREQUENCIES))
ALPHA = 0.0027
POWER = 0.90


def real_stack(z: np.ndarray) -> np.ndarray:
    z = np.asarray(z, dtype=complex)
    return np.concatenate((z.real, z.imag))


def complex_model_real_jacobian(C, K, r):
    """12x6 Jacobian for real params Re/Im(C,K,r)."""
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


def root_covariance_at_snr1(J):
    """Covariance of [Re gamma, Im gamma] for RMS-channel SNR=1."""
    r, coeff, model, fit_rel = kernel_aware_root(J)
    C, K = coeff
    G = complex_model_real_jacobian(C, K, r)
    rms_channel = float(np.sqrt(np.mean(np.abs(J) ** 2)))
    sigma_quad = rms_channel  # definition of SNR=1
    cov_param = sigma_quad**2 * np.linalg.inv(G.T @ G)
    cov_r = cov_param[4:6, 4:6]
    gamma = -r
    return gamma, cov_r, {
        "rms_channel": rms_channel,
        "kernel_fit_rel": float(fit_rel),
        "cov_gamma_snr1": cov_r.tolist(),
    }


def gamma_dd(f, D, w):
    omega = 2.0 * np.pi * np.asarray(f, dtype=float)
    D = float(D)
    w = float(w)
    if D < 1e-14:
        return -1j * omega / w
    return (-w + np.sqrt(w * w - 4j * D * omega)) / (2.0 * D)


def solve_dw_from_gamma(gamma, f):
    omega = 2.0 * np.pi * float(f)
    a, b = float(gamma.real), float(gamma.imag)
    s = a * a + b * b
    D = -omega * a / (b * s)
    w = omega * (a * a - b * b) / (b * s)
    return float(D), float(w)


def fit_homogeneous(frequencies, gammas, cov_blocks):
    C = block_diag(*cov_blocks)
    L = np.linalg.cholesky(C)

    def whiten(v):
        return np.linalg.solve(L, v)

    y = np.empty(2 * len(gammas), dtype=float)
    y[0::2] = np.real(gammas)
    y[1::2] = np.imag(gammas)

    D0, w0 = solve_dw_from_gamma(gammas[0], frequencies[0])
    D0 = max(D0, 1e-8)
    w0 = max(w0, 1.0)

    def residual(logp):
        D, w = np.exp(logp)
        gm = gamma_dd(frequencies, D, w)
        m = np.empty_like(y)
        m[0::2] = gm.real
        m[1::2] = gm.imag
        return whiten(y - m)

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
    lam_snr1 = float(np.dot(rw, rw))
    return float(D), float(w), lam_snr1, C


def lambda_required(nu, alpha=ALPHA, power=POWER):
    q = float(chi2.ppf(1.0 - alpha, nu))

    def f(lam):
        return float(ncx2.sf(q, nu, lam) - power)

    hi = 10.0
    while f(hi) < 0:
        hi *= 2.0
        if hi > 1e6:
            raise RuntimeError("failed to bracket noncentrality")
    lam = float(brentq(f, 0.0, hi, xtol=1e-12, rtol=1e-12))
    return q, lam


def run(args):
    old_freq = base.FREQUENCIES
    base.FREQUENCIES = FORWARD_FREQUENCIES.copy()
    base.V_BIAS = float(args.bias_v)
    base.X_EXTENT_UM = float(args.x_extent_um)

    numerical = {
        "nx": args.nx,
        "nz": args.nz,
        "nx_src": args.nx_src,
        "nz_src": args.nz_src,
        "ds_um": args.ds_um,
    }
    scenario = base.Scenario("planar_depletion", 1.0, 3.0, 0.05)

    try:
        J_forward, diag = sweep.currents_with_beam(scenario, 2.0, 0.0, **numerical)
        J = J_forward[1:]
        gammas = []
        covs = []
        per_frequency = []
        for jf, f in enumerate(FREQUENCIES):
            gamma, cov, meta = root_covariance_at_snr1(J[jf])
            gammas.append(gamma)
            covs.append(cov)
            eig = np.linalg.eigvalsh(cov)
            per_frequency.append(
                {
                    "frequency_hz": float(f),
                    "gamma_real_per_m": float(gamma.real),
                    "gamma_imag_per_m": float(gamma.imag),
                    "kernel_fit_rel": meta["kernel_fit_rel"],
                    "rms_channel": meta["rms_channel"],
                    "root_sigma_major_per_m_at_snr1": float(np.sqrt(np.max(eig))),
                    "root_sigma_minor_per_m_at_snr1": float(np.sqrt(np.min(eig))),
                    "root_cov_re_im_at_snr1": float(cov[0, 1]),
                }
            )
    finally:
        base.FREQUENCIES = old_freq

    gammas = np.asarray(gammas)

    band_rows = []
    for n in range(2, len(FREQUENCIES) + 1):
        fs = FREQUENCIES[:n]
        gs = gammas[:n]
        cs = covs[:n]
        D, w, lam1, C = fit_homogeneous(fs, gs, cs)
        nu = 2 * n - 2
        q, lam_req = lambda_required(nu)
        if lam1 <= 0:
            snr_req = float("inf")
        else:
            snr_req = float(np.sqrt(lam_req / lam1))
        band_rows.append(
            {
                "max_frequency_hz": float(fs[-1]),
                "n_complex_frequencies": int(n),
                "dof": int(nu),
                "best_fit_D_m2_per_s": D,
                "best_fit_w_m_per_s": w,
                "lambda_at_channel_snr1": lam1,
                "chi2_threshold": q,
                "lambda_required": lam_req,
                "required_rms_channel_snr": snr_req,
                "required_rms_channel_snr_db": float(20.0 * np.log10(snr_req)) if np.isfinite(snr_req) else float("inf"),
                "approx_rms_channel_phase_sigma_deg": float(np.degrees(1.0 / snr_req)) if np.isfinite(snr_req) and snr_req > 0 else 0.0,
            }
        )

    payload = {
        "status": "CONDITIONAL end-to-end statistical discrimination example",
        "noise_model": {
            "quadrature_noise": "independent equal Gaussian real/imag noise per spectral channel",
            "snr_definition": "S = RMS_m |J_m| / sigma_quadrature at each RF frequency",
            "same_snr_assumed_across_frequencies": True,
            "cross_frequency_correlation": False,
        },
        "test": {
            "alpha": ALPHA,
            "power": POWER,
            "homogeneous_fit_parameters": ["D", "w"],
            "microscopic_truth_D": 0.0,
            "recombination": 0.0,
        },
        "device_stress": {
            "contact_fraction": 1.0,
            "depletion_width_um": 3.0,
            "space_charge_drop_v": 0.05,
            "bias_v": float(args.bias_v),
            "collection_fraction": float(diag["collected"]),
            "dc_ramo_error": float(diag["dc_error"]),
        },
        "numerical": numerical,
        "per_frequency": per_frequency,
        "bands": band_rows,
    }

    out_band = Path(args.output_bands)
    out_freq = Path(args.output_frequency)
    out_json = Path(args.output_summary)
    for p in (out_band, out_freq, out_json):
        p.parent.mkdir(parents=True, exist_ok=True)

    with out_band.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(band_rows[0].keys()))
        w.writeheader()
        w.writerows(band_rows)
    with out_freq.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(per_frequency[0].keys()))
        w.writeheader()
        w.writerows(per_frequency)
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
    p.add_argument("--output-bands", default="paper02_end_to_end_rejection_bands.csv")
    p.add_argument("--output-frequency", default="paper02_end_to_end_rejection_frequency.csv")
    p.add_argument("--output-summary", default="paper02_end_to_end_rejection_summary.json")
    return p


if __name__ == "__main__":
    run(parser().parse_args())
