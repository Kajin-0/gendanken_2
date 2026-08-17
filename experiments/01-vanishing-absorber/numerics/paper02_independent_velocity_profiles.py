"""Independent-profile generality test for the Paper-02 false diffusion.

This calculation deliberately removes the 2-D Poisson solver and finite-contact
geometry.  It prescribes deterministic one-dimensional velocity profiles and
solves the exact planar Shockley-Ramo source-response ODE

    dH/dz = -1/L + i*omega*H/v(z),   H(L)=0.

The same six calibrated HgCdTe optical kernels are then applied and the same
kernel-aware one-mode inverse is used.  Microscopic diffusion and recombination
are absent by construction.

The downstream velocity is uniform for z < z_d and then follows independent
linear or exponential acceleration/deceleration families for z >= z_d.  The
prediction is sign-sensitive:

  downstream acceleration  -> positive apparent D_eff,
  uniform velocity          -> D_eff ~= 0,
  downstream deceleration   -> negative/non-admissible D_eff,

provided finite optical kernels overlap the nonuniform region.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp

import realistic_geometry_closure_stress as base
from paper02_kernel_aware_depletion_frequency_law import kernel_aware_root


FREQUENCIES = np.asarray(
    (0.0, 25e6, 50e6, 100e6, 200e6, 500e6, 750e6, 1e9),
    dtype=float,
)
CAL_FREQ_HZ = 100e6
V0_M_PER_S = 2.65565e4
ZD_UM = 4.6


@dataclass(frozen=True)
class Profile:
    name: str
    family: str
    endpoint_ratio: float


PROFILES = (
    Profile("uniform", "uniform", 1.0),
    Profile("linear_decel_050", "linear", 0.50),
    Profile("linear_decel_075", "linear", 0.75),
    Profile("linear_accel_125", "linear", 1.25),
    Profile("linear_accel_150", "linear", 1.50),
    Profile("linear_accel_200", "linear", 2.00),
    Profile("exp_decel_050", "exponential", 0.50),
    Profile("exp_decel_075", "exponential", 0.75),
    Profile("exp_accel_125", "exponential", 1.25),
    Profile("exp_accel_150", "exponential", 1.50),
    Profile("exp_accel_200", "exponential", 2.00),
)


def velocity(profile: Profile, z_m: float) -> float:
    z_um = z_m * 1e6
    if profile.family == "uniform" or z_um <= ZD_UM:
        return V0_M_PER_S

    xi = (z_um - ZD_UM) / (float(base.L_UM) - ZD_UM)
    xi = float(np.clip(xi, 0.0, 1.0))
    R = float(profile.endpoint_ratio)

    if profile.family == "linear":
        return V0_M_PER_S * (1.0 + (R - 1.0) * xi)
    if profile.family == "exponential":
        return V0_M_PER_S * np.exp(np.log(R) * xi)
    raise ValueError(profile.family)


def point_response(profile: Profile, frequency_hz: float) -> np.ndarray:
    """Solve exact planar Ramo response H(z,omega) on the optical z grid."""
    L_m = float(base.L_UM) * 1e-6
    omega = 2.0 * np.pi * float(frequency_hz)

    def rhs(z, y):
        H = y[0]
        return np.asarray((-1.0 / L_m + 1j * omega * H / velocity(profile, z),), dtype=complex)

    sol = solve_ivp(
        rhs,
        (L_m, 0.0),
        np.asarray((0.0 + 0.0j,), dtype=complex),
        dense_output=True,
        rtol=2e-11,
        atol=2e-13,
        max_step=0.01e-6,
    )
    if not sol.success:
        raise RuntimeError(sol.message)

    z_m = np.asarray(base.OPT_Z_UM, dtype=float) * 1e-6
    return np.asarray(sol.sol(z_m)[0], dtype=complex)


def spectral_currents(profile: Profile) -> np.ndarray:
    J = np.zeros((len(FREQUENCIES), len(base.OPTICS)), dtype=complex)
    for jf, f in enumerate(FREQUENCIES):
        H = point_response(profile, f)
        for m, row in enumerate(base.OPTICS):
            J[jf, m] = np.trapezoid(np.asarray(row[3]) * H, base.OPT_Z_UM)
    return J


def solve_dw(gamma: complex, f: float):
    g2 = gamma * gamma
    M = np.asarray(((g2.real, gamma.real), (g2.imag, gamma.imag)), dtype=float)
    rhs = np.asarray((0.0, -2.0 * np.pi * f), dtype=float)
    D, w = np.linalg.solve(M, rhs)
    return float(D), float(w)


def law_residual(gamma, f, D, w):
    if f <= 0:
        return 0.0
    rhs = -1j * 2.0 * np.pi * f
    return float(abs(D * gamma * gamma + w * gamma - rhs) / abs(rhs))


def local_weak_gradient_prediction(profile: Profile):
    """Weak-gradient point-source sign/scale at the depletion boundary.

    This is not expected to equal the finite-kernel inversion quantitatively;
    it is recorded only as a sign/scale diagnostic for the independent family.
    """
    L_m = float(base.L_UM) * 1e-6
    zd_m = ZD_UM * 1e-6
    W_m = L_m - zd_m
    R = float(profile.endpoint_ratio)
    if profile.family == "uniform":
        vprime = 0.0
    elif profile.family == "linear":
        vprime = V0_M_PER_S * (R - 1.0) / W_m
    elif profile.family == "exponential":
        vprime = V0_M_PER_S * np.log(R) / W_m
    else:
        raise ValueError(profile.family)
    return 0.5 * W_m * W_m * vprime


def run(args):
    old_freq = base.FREQUENCIES
    base.FREQUENCIES = FREQUENCIES.copy()
    rows = []
    frequency_rows = []

    try:
        for profile in PROFILES:
            print(profile.name, flush=True)
            J = spectral_currents(profile)
            gammas = []
            fits = []

            for jf, f in enumerate(FREQUENCIES):
                r, _, _, fit = kernel_aware_root(J[jf])
                gamma = -r
                gammas.append(gamma)
                fits.append(float(fit))

            gammas = np.asarray(gammas)
            i100 = int(np.where(FREQUENCIES == CAL_FREQ_HZ)[0][0])
            D, w = solve_dw(gammas[i100], CAL_FREQ_HZ)

            for f, gamma, fit in zip(FREQUENCIES, gammas, fits):
                frequency_rows.append(
                    {
                        "profile": profile.name,
                        "family": profile.family,
                        "endpoint_ratio": profile.endpoint_ratio,
                        "frequency_hz": float(f),
                        "gamma_real_per_m": float(gamma.real),
                        "gamma_imag_per_m": float(gamma.imag),
                        "kernel_one_mode_fit_rel": float(fit),
                        "law_residual_from_100mhz": law_residual(gamma, f, D, w),
                    }
                )

            i1g = int(np.where(FREQUENCIES == 1e9)[0][0])
            rows.append(
                {
                    "profile": profile.name,
                    "family": profile.family,
                    "endpoint_ratio": float(profile.endpoint_ratio),
                    "endpoint_velocity_m_per_s": V0_M_PER_S * profile.endpoint_ratio,
                    "effective_D_m2_per_s": D,
                    "effective_w_m_per_s": w,
                    "positive_D_w": bool(D > 0 and w > 0),
                    "law_residual_1ghz": law_residual(gammas[i1g], 1e9, D, w),
                    "max_kernel_one_mode_fit_rel": max(fits),
                    "weak_gradient_D_at_boundary_m2_per_s": local_weak_gradient_prediction(profile),
                }
            )
    finally:
        base.FREQUENCIES = old_freq

    uniform = next(r for r in rows if r["profile"] == "uniform")
    accel = [r for r in rows if r["endpoint_ratio"] > 1.0]
    decel = [r for r in rows if r["endpoint_ratio"] < 1.0]

    payload = {
        "status": "CONDITIONAL independent deterministic velocity-profile stress",
        "model_truth": {
            "microscopic_diffusion": 0.0,
            "recombination": 0.0,
            "planar_weighting_field": True,
            "upstream_velocity_m_per_s": V0_M_PER_S,
            "nonuniform_region_start_um": ZD_UM,
            "absorber_thickness_um": float(base.L_UM),
        },
        "profiles": rows,
        "generality_gate": {
            "uniform_abs_D_eff": abs(uniform["effective_D_m2_per_s"]),
            "all_acceleration_D_positive": all(r["effective_D_m2_per_s"] > 0 for r in accel),
            "all_deceleration_D_negative": all(r["effective_D_m2_per_s"] < 0 for r in decel),
            "supported_if": "uniform gives D_eff~0, independent acceleration families give positive D_eff, and deceleration reverses the sign",
        },
    }

    out_results = Path(args.output_results)
    out_frequency = Path(args.output_frequency)
    out_summary = Path(args.output_summary)
    for p in (out_results, out_frequency, out_summary):
        p.parent.mkdir(parents=True, exist_ok=True)

    with out_results.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    with out_frequency.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(frequency_rows[0].keys()))
        w.writeheader()
        w.writerows(frequency_rows)
    out_summary.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


def parser():
    p = argparse.ArgumentParser()
    p.add_argument("--output-results", default="paper02_independent_velocity_profiles_results.csv")
    p.add_argument("--output-frequency", default="paper02_independent_velocity_profiles_frequency.csv")
    p.add_argument("--output-summary", default="paper02_independent_velocity_profiles_summary.json")
    return p


if __name__ == "__main__":
    run(parser().parse_args())
