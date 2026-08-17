"""Local tangent/normal projection of optical-kernel calibration modes.

This calculation evaluates the *derivative at zero calibration error* for three
signed wavelength-registration nuisance coordinates in the exact uniform-
velocity, D_micro=0 planar null:

  common:    delta_lambda_m = eps
  linear:    delta_lambda_m = eps * s_m
  curvature: delta_lambda_m = eps * c_m

where eps is in nm, s spans -1..+1 across the six channels, and c is a centered
quadratic channel pattern.

At eps=0 the nominal kernel-aware one-mode inverse is exact.  Therefore the
first derivative of the nuisance channel vector can be decomposed unambiguously
into the six-real-dimensional one-mode tangent and its normal complement.

Outputs include:
  * tangent and normal derivative norms;
  * root and D derivatives per nm;
  * first-order same-frequency SNR coefficients for positive-D detection and
    one-mode rejection;
  * asymptotic ordering for the sign that makes D positive;
  * finite-difference linearization checks at +/- h.

The purpose is to distinguish a genuinely near-tangent calibration direction
from a finite-amplitude optimizer artifact.  It is a theoretical local result,
not an empirical calibration tolerance.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np
from scipy.stats import norm

import realistic_geometry_closure_stress as base
import paper02_kernel_aware_depletion_frequency_law as law
import paper02_exact_planar_continuum_crosscheck as exact
import paper02_kernel_misspecification_stress as ks
from paper02_end_to_end_rejection_snr import complex_model_real_jacobian
from paper02_bias_bound_linearization import diffusion_gradient
from paper02_same_frequency_hidden_risk import lambda_required, ALPHA, POWER, NU_CHANNEL


FREQUENCIES = (100e6, 500e6, 1e9)
N = len(base.OPTICS)
SLOPE = np.linspace(-1.0, 1.0, N)
CURV = SLOPE**2
CURV -= np.mean(CURV)
CURV /= np.max(np.abs(CURV))


def real_stack(z):
    z = np.asarray(z, dtype=complex)
    return np.concatenate((z.real, z.imag))


def mode_vector(name: str) -> np.ndarray:
    if name == "common":
        return np.ones(N)
    if name == "linear":
        return SLOPE.copy()
    if name == "curvature":
        return CURV.copy()
    raise ValueError(name)


def uniform_point_transfer():
    z_m = ks.Z_M
    v_exact = exact.exact_speed_m_per_s(z_m)
    transit = float(np.trapezoid(1.0 / v_exact, z_m))
    v_harmonic = float(ks.L_M / transit)
    return ks.uniform_point_transfer(v_harmonic), v_harmonic


def channels_for_eps(point_all, mode: np.ndarray, eps_nm: float, frequency_hz: float):
    kernels = ks.wavelength_kernels(float(eps_nm) * mode)
    idx = int(np.where(law.FREQUENCIES == float(frequency_hz))[0][0])
    return ks.channel_currents(point_all[[idx]], kernels)[0]


def analyze_mode(point_all, v_uniform, frequency_hz: float, name: str, h_nm: float):
    mode = mode_vector(name)
    J0 = channels_for_eps(point_all, mode, 0.0, frequency_hz)
    Jp = channels_for_eps(point_all, mode, +h_nm, frequency_hz)
    Jm = channels_for_eps(point_all, mode, -h_nm, frequency_hz)
    dJ = (Jp - Jm) / (2.0 * h_nm)

    r0, coeff, model0, fit0 = law.kernel_aware_root(J0)
    C, K = coeff
    gamma0 = -r0
    G = complex_model_real_jacobian(C, K, r0)
    eprime = real_stack(dJ)

    # IID reference metric at channel SNR=1.
    rms = float(np.sqrt(np.mean(np.abs(J0) ** 2)))
    W1 = np.eye(2 * N) / rms**2
    fisher = G.T @ W1 @ G
    cov_param1 = np.linalg.inv(fisher)

    dtheta = np.linalg.solve(fisher, G.T @ W1 @ eprime)
    tangent = G @ dtheta
    normal = eprime - tangent
    total_w2 = float(eprime @ W1 @ eprime)
    tangent_w2 = float(tangent @ W1 @ tangent)
    normal_w2 = float(normal @ W1 @ normal)

    # r params are columns 4,5. gamma=-r.
    dgamma = -(dtheta[4] + 1j * dtheta[5])
    dD_da, dD_db = diffusion_gradient(gamma0)
    dD_deps = float(dD_da * dgamma.real + dD_db * dgamma.imag)

    cov_gamma1 = cov_param1[4:6, 4:6]
    gradD = np.asarray((dD_da, dD_db), dtype=float)
    sigmaD1 = float(np.sqrt(gradD @ cov_gamma1 @ gradD))
    zreq = float(norm.ppf(1.0 - ALPHA) + norm.ppf(POWER))

    # For small signed eps with sign chosen so D>0:
    # S_D ~ A_D/|eps| and S_reject ~ A_R/|eps|.
    A_D = float(zreq * sigmaD1 / abs(dD_deps)) if dD_deps != 0 else float("inf")
    _q, lambda_req = lambda_required(NU_CHANNEL)
    A_R = float(np.sqrt(lambda_req / normal_w2)) if normal_w2 > 0 else float("inf")
    asymptotic_ratio = float(A_R / A_D) if np.isfinite(A_D) else 0.0

    def finite(eps):
        J = channels_for_eps(point_all, mode, eps, frequency_hz)
        r, _coeff, m, _fit = law.kernel_aware_root(J)
        gamma = -r
        D, w = law.solve_dw_one_frequency(gamma, frequency_hz)
        residual_w = float(np.linalg.norm(real_stack(J - m)) / rms)
        return D, w, gamma, residual_w

    Dp, wp, gp, resp = finite(+h_nm)
    Dm, wm, gm, resm = finite(-h_nm)
    Dlin_p = dD_deps * h_nm
    Dlin_m = -dD_deps * h_nm

    return {
        "frequency_hz": float(frequency_hz),
        "mode": name,
        "finite_difference_h_nm": float(h_nm),
        "nominal_D_m2_per_s": float(law.solve_dw_one_frequency(gamma0, frequency_hz)[0]),
        "nominal_w_m_per_s": float(law.solve_dw_one_frequency(gamma0, frequency_hz)[1]),
        "uniform_velocity_truth_m_per_s": float(v_uniform),
        "nominal_kernel_fit_rel": float(fit0),
        "dD_d_eps_m2_per_s_per_nm": dD_deps,
        "dgamma_real_d_eps_per_m_per_nm": float(dgamma.real),
        "dgamma_imag_d_eps_per_m_per_nm": float(dgamma.imag),
        "weighted_total_derivative_norm": float(np.sqrt(total_w2)),
        "weighted_tangent_derivative_norm": float(np.sqrt(tangent_w2)),
        "weighted_normal_derivative_norm": float(np.sqrt(normal_w2)),
        "tangent_energy_fraction": float(tangent_w2 / total_w2) if total_w2 > 0 else 0.0,
        "normal_energy_fraction": float(normal_w2 / total_w2) if total_w2 > 0 else 0.0,
        "tangent_to_normal_norm_ratio": float(np.sqrt(tangent_w2 / normal_w2)) if normal_w2 > 0 else float("inf"),
        "positive_D_sign_of_eps": 1 if dD_deps > 0 else (-1 if dD_deps < 0 else 0),
        "asymptotic_S_D_times_abs_eps": A_D,
        "asymptotic_S_reject_times_abs_eps": A_R,
        "asymptotic_Sreject_over_SD": asymptotic_ratio,
        "asymptotic_positive_D_detectable_before_rejection": bool(A_D < A_R),
        "finite_plus_h_D": float(Dp),
        "finite_minus_h_D": float(Dm),
        "linearized_plus_h_D": float(Dlin_p),
        "linearized_minus_h_D": float(Dlin_m),
        "finite_plus_h_w": float(wp),
        "finite_minus_h_w": float(wm),
        "finite_plus_h_residual_over_nominal_rms": resp,
        "finite_minus_h_residual_over_nominal_rms": resm,
        "relative_D_linearization_error_plus": float(abs(Dp-Dlin_p)/max(abs(Dlin_p),1e-30)),
        "relative_D_linearization_error_minus": float(abs(Dm-Dlin_m)/max(abs(Dlin_m),1e-30)),
    }


def run(args):
    point, v_uniform = uniform_point_transfer()
    rows = [
        analyze_mode(point, v_uniform, f, mode, args.h_nm)
        for f in FREQUENCIES
        for mode in ("common", "linear", "curvature")
    ]
    payload = {
        "status": "CHECKED local signed kernel-nuisance tangent/normal projection",
        "scope": {
            "transport_truth": "uniform deterministic planar D_micro=0",
            "inverse": "nominal theoretical-kernel one-mode inverse",
            "metric": "IID equal real/imag quadrature",
            "calibration_modes_are_theoretical_local_directions": True,
        },
        "channel_linear_mode": SLOPE.tolist(),
        "channel_curvature_mode": CURV.tolist(),
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
    print(json.dumps(rows, indent=2, sort_keys=True))


def parser():
    p = argparse.ArgumentParser()
    p.add_argument("--h-nm", type=float, default=0.001)
    p.add_argument("--output-csv", default="paper02_kernel_nuisance_tangent_projection.csv")
    p.add_argument("--output-summary", default="paper02_kernel_nuisance_tangent_projection_summary.json")
    return p


if __name__ == "__main__":
    run(parser().parse_args())
