"""Single-return interference stress test for the provisional A/B iso-kernel schedule.

This is NOT a calibrated transfer-matrix model.

Why this exists
---------------
The 2023 sample-A experiment reports interference near cutoff, so pure
Beer-Lambert generation is not a sufficient final optical model. A full
transfer matrix would require the actual sample-A composition profile plus
composition/wavelength/temperature-dependent complex refractive indices and
interface stack details that are not yet recovered.

Before adding those uncertain details, this script asks a falsification-style
question: does the provisional 3.632 um common reference survive a deliberately
broad coherent single-back-reflection perturbation?

For forward optical depth tau(z), total depth tau_L, effective back-reflection
power ratio R, effective refractive index n_eff, and unknown reflection phase
theta, use the exact two-wave intensity for one returned wave:

 I(z) = exp[-tau(z)]
      + R exp[-(2 tau_L - tau(z))]
      + 2 sqrt(R) exp[-tau_L]
          cos[4 pi n_eff (L-z)/lambda + theta].

This is |E_forward + E_return|^2 and is nonnegative before roundoff clipping.
Generation is g(z)=alpha(z) I(z).

R up to 0.9 and n_eff=2.8-4.2 are sensitivity/stress coordinates, NOT measured
sample-A values or uncertainty intervals. The primary result scans all 72
sample-A profile-family members, three R values, three n_eff values and four
reflection phases. A second deliberately over-broad diagnostic lets n_eff jump
independently between 300 K and the comparison temperature on six
representative sample-A profiles. That second test is not a physical thermo-
optic model; it identifies sensitivity to unknown temperature-dependent
optical phase.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.optimize import minimize_scalar

from hgcdte_sample_a_constraint_family_joint_iso_kernel import (
    HC_EV_UM,
    N_CELL,
    alpha_moazzami,
    optical_kernel as beer_lambert_kernel,
    relative_kernel_error,
    sample_a_profiles,
    sample_b_profile,
)

REFERENCE_LAMBDA_UM = 3.632
TARGET_T_K = (215.0, 115.0)

# Stress ranges, not uncertainty intervals.
REFLECTION_POWER = (0.1, 0.5, 0.9)
N_EFFECTIVE = (2.8, 3.5, 4.2)
PHASES_RAD = (0.0, 0.5 * np.pi, np.pi, 1.5 * np.pi)

# Downsample the profile-family fine grid for a practical deterministic stress
# regression. This remains substantially finer than the 80-cell timing kernel.
N_STRESS = 1801


def downsample_profile(
    z_um: np.ndarray, x: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    z_new = np.linspace(0.0, float(z_um[-1]), N_STRESS)
    return z_new, np.interp(z_new, z_um, x)


def interference_kernel(
    z_um: np.ndarray,
    x: np.ndarray,
    wavelength_um: float,
    T: float,
    reflection_power: float,
    n_eff: float,
    reflection_phase_rad: float,
) -> np.ndarray:
    z_cm = z_um * 1.0e-4
    alpha = alpha_moazzami(HC_EV_UM / wavelength_um, x, T)
    tau = np.concatenate(([0.0], cumulative_trapezoid(alpha, z_cm)))
    tau_L = float(tau[-1])

    k_um = 2.0 * np.pi * n_eff / wavelength_um
    returned_phase = 2.0 * k_um * (z_um[-1] - z_um) + reflection_phase_rad

    intensity = (
        np.exp(-tau)
        + reflection_power * np.exp(-(2.0 * tau_L - tau))
        + 2.0
        * np.sqrt(reflection_power)
        * np.exp(-tau_L)
        * np.cos(returned_phase)
    )

    # Exact two-wave form is nonnegative; clipping only guards floating error.
    intensity = np.maximum(intensity, 0.0)
    generation_per_cm = alpha * intensity
    norm = float(np.trapezoid(generation_per_cm, z_cm))
    if norm <= 1.0e-15:
        return np.zeros(N_CELL)

    density_per_cm = generation_per_cm / norm
    cdf = np.concatenate(([0.0], cumulative_trapezoid(density_per_cm, z_cm)))
    cdf = np.clip(cdf, 0.0, 1.0)
    survival = 1.0 - cdf

    survival_integral = np.concatenate(
        ([0.0], cumulative_trapezoid(survival, z_um))
    )
    edges_um = np.linspace(0.0, float(z_um[-1]), N_CELL + 1)
    return np.diff(np.interp(edges_um, z_um, survival_integral))


def joint_match(
    a_z: np.ndarray,
    a_x: np.ndarray,
    b_z: np.ndarray,
    b_x: np.ndarray,
    T: float,
    reflection_power: float,
    n_300: float,
    n_T: float,
    reflection_phase_rad: float,
) -> tuple[float, float, float]:
    a0 = interference_kernel(
        a_z,
        a_x,
        REFERENCE_LAMBDA_UM,
        300.0,
        reflection_power,
        n_300,
        reflection_phase_rad,
    )
    _, b0 = beer_lambert_kernel(b_z, b_x, REFERENCE_LAMBDA_UM, 300.0)

    bounds = (3.70, 3.90) if T == 215.0 else (3.90, 4.12)

    def objective(wavelength_um: float) -> float:
        a = interference_kernel(
            a_z,
            a_x,
            wavelength_um,
            T,
            reflection_power,
            n_T,
            reflection_phase_rad,
        )
        _, b = beer_lambert_kernel(b_z, b_x, wavelength_um, T)
        ea = relative_kernel_error(a, a0)
        eb = relative_kernel_error(b, b0)
        return ea**2 + eb**2

    result = minimize_scalar(
        objective,
        bounds=bounds,
        method="bounded",
        options={"xatol": 2.0e-7},
    )
    wavelength = float(result.x)
    a = interference_kernel(
        a_z,
        a_x,
        wavelength,
        T,
        reflection_power,
        n_T,
        reflection_phase_rad,
    )
    _, b = beer_lambert_kernel(b_z, b_x, wavelength, T)
    return (
        wavelength,
        relative_kernel_error(a, a0),
        relative_kernel_error(b, b0),
    )


def representative_profiles(profiles):
    x_front = np.asarray([profile[1][0] for profile in profiles])
    z_cut = np.asarray([profile[2]["z_cut"] for profile in profiles])
    indices = {
        int(np.argmin(x_front)),
        int(np.argmax(x_front)),
        int(np.argmin(z_cut)),
        int(np.argmax(z_cut)),
        int(np.argmin(np.abs(x_front - 0.50))),
        int(np.argmin(np.abs(x_front - 0.80))),
    }
    return [profiles[index] for index in sorted(indices)]


def report(label: str, data: np.ndarray) -> None:
    print(label)
    for T in TARGET_T_K:
        subset = data[data[:, 0] == T]
        print(
            f"  {T:.0f} K: lambda={subset[:,1].min():.6f}-"
            f"{subset[:,1].max():.6f} um; "
            f"A mismatch={100*subset[:,2].min():.3f}-"
            f"{100*subset[:,2].max():.3f}%; "
            f"B mismatch={100*subset[:,3].min():.3f}-"
            f"{100*subset[:,3].max():.3f}%"
        )


def main() -> None:
    raw_profiles = sample_a_profiles()
    profiles = [
        (*downsample_profile(z, x), metadata)
        for z, x, metadata in raw_profiles
    ]
    b_z_raw, b_x_raw = sample_b_profile()
    b_z, b_x = downsample_profile(b_z_raw, b_x_raw)

    print("Sample-A single-return interference stress test")
    print(f"sample-A profiles = {len(profiles)}")
    print(
        "R stress = " + ", ".join(f"{value:.1f}" for value in REFLECTION_POWER)
    )
    print(
        "n_eff stress = " + ", ".join(f"{value:.1f}" for value in N_EFFECTIVE)
    )
    print("reflection phases = 0, pi/2, pi, 3pi/2")
    print()

    # Primary stress: same unknown effective n at both temperatures.
    primary = []
    for a_z, a_x, _ in profiles:
        for reflection_power in REFLECTION_POWER:
            for n_eff in N_EFFECTIVE:
                for phase in PHASES_RAD:
                    for T in TARGET_T_K:
                        wavelength, ea, eb = joint_match(
                            a_z,
                            a_x,
                            b_z,
                            b_x,
                            T,
                            reflection_power,
                            n_eff,
                            n_eff,
                            phase,
                        )
                        primary.append((T, wavelength, ea, eb))
    primary = np.asarray(primary)
    report("fixed-n interference stress", primary)
    print()

    # Secondary over-broad diagnostic: let n change independently from one end
    # of the stress interval to the other. This is intentionally NOT a physical
    # thermo-optic trajectory.
    secondary = []
    for a_z, a_x, _ in representative_profiles(profiles):
        for n_300 in (N_EFFECTIVE[0], N_EFFECTIVE[-1]):
            for n_T in (N_EFFECTIVE[0], N_EFFECTIVE[-1]):
                for phase in PHASES_RAD:
                    for T in TARGET_T_K:
                        wavelength, ea, eb = joint_match(
                            a_z,
                            a_x,
                            b_z,
                            b_x,
                            T,
                            0.9,
                            n_300,
                            n_T,
                            phase,
                        )
                        secondary.append((T, wavelength, ea, eb))
    secondary = np.asarray(secondary)
    report("independent endpoint-n diagnostic (R=0.9)", secondary)
    print()

    p215 = primary[primary[:, 0] == 215.0]
    p115 = primary[primary[:, 0] == 115.0]
    s215 = secondary[secondary[:, 0] == 215.0]
    s115 = secondary[secondary[:, 0] == 115.0]

    # Stable envelopes. Primary result: even very large coherent single-return
    # perturbations move the optimal common wavelength only a few nanometres.
    assert 3.7927 < p215[:, 1].min() < p215[:, 1].max() < 3.7944
    assert p215[:, 2].max() < 0.0090
    assert p215[:, 3].max() < 0.0050

    assert 4.0022 < p115[:, 1].min() < p115[:, 1].max() < 4.0082
    assert p115[:, 2].max() < 0.0200
    assert p115[:, 3].max() < 0.0102

    # If effective n is allowed to jump independently across the entire broad
    # 2.8-4.2 stress range, optical phase becomes the larger uncertainty.
    assert 3.7901 < s215[:, 1].min() < s215[:, 1].max() < 3.7961
    assert s215[:, 2].max() < 0.041
    assert s215[:, 3].max() < 0.0062

    assert 3.9995 < s115[:, 1].min() < s115[:, 1].max() < 4.0106
    assert s115[:, 2].max() < 0.044
    assert s115[:, 3].max() < 0.0118

    print(
        "PASS: the provisional 3.632-um common reference survives broad "
        "single-return interference amplitude/phase stress. The schedule is "
        "more sensitive to an unknown temperature-dependent optical phase "
        "(represented here by an intentionally extreme independent n jump) "
        "than to reflection strength alone."
    )


if __name__ == "__main__":
    main()
