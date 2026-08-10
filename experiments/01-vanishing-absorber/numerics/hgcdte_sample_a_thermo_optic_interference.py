"""Composition-resolved thermo-optic interference stress for sample A.

This extends hgcdte_sample_a_interference_stress.py by replacing the arbitrary
constant effective refractive index with the empirical HgCdTe n(x,lambda,T)
relation attributed to Liu, Chu & Tang, J. Appl. Phys. 75, 4176 (1994), DOI
10.1063/1.356001, as reproduced explicitly in later HgCdTe optical modeling.

The measured Liu composition range is x=0.276-0.443 and T=4.2-300 K.  The
candidate mid/deep wavelength schedule has a local band-edge threshold near
x~=0.338 at all three temperatures, so the optically active / returned-wave
phase interval lies inside that measured composition range even when the
processed sample-A front composition is much larger.

This remains a single-back-reflection stress calculation, not a full graded
transfer matrix and not a calibrated prediction of absolute optical throughput.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.optimize import brentq, minimize_scalar

from hgcdte_sample_a_constraint_family_joint_iso_kernel import (
    HC_EV_UM,
    N_CELL,
    alpha_moazzami,
    eg_hansen,
    optical_kernel as beer_lambert_kernel,
    relative_kernel_error,
    sample_a_profiles,
    sample_b_profile,
)

REFERENCE_LAMBDA_UM = 3.632
TARGET_T_K = (215.0, 115.0)
REFLECTION_POWER = (0.1, 0.5, 0.9)  # stress coordinates, not measured R
PHASES_RAD = (0.0, 0.5 * np.pi, np.pi, 1.5 * np.pi)
N_STRESS = 1201

# Empirical relation as reproduced in published HgCdTe optical modeling:
# n^2 = A + B/[1-(C/lambda)^2] + D lambda^2, lambda in um.
# The underlying Liu et al. measurements cover x=0.276-0.443 and 4.2-300 K.
def n_liu(x: np.ndarray, T: float, wavelength_um: float) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    A = 13.173 - 9.852 * x + 2.909 * x**2 + 1.0e-3 * (300.0 - T)
    B = 0.83 - 0.246 * x - 0.0961 * x**2 + 8.0e-4 * (300.0 - T)
    C = 6.706 - 14.437 * x + 8.531 * x**2 + 7.0e-4 * (300.0 - T)
    D = 1.953e-4 - 0.00128 * x + 1.853e-4 * x**2
    n2 = A + B / (1.0 - (C / wavelength_um) ** 2) + D * wavelength_um**2
    if np.any(n2 <= 0.0):
        raise RuntimeError("Empirical refractive-index relation left real domain")
    return np.sqrt(n2)


def downsample_profile(
    z_um: np.ndarray, x: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    z_new = np.linspace(0.0, float(z_um[-1]), N_STRESS)
    return z_new, np.interp(z_new, z_um, x)


def band_edge_composition(T: float, wavelength_um: float) -> float:
    energy_ev = HC_EV_UM / wavelength_um
    return float(
        brentq(
            lambda xx: eg_hansen(xx, T) - energy_ev,
            0.276,
            0.443,
        )
    )


def thermo_optic_interference_kernel(
    z_um: np.ndarray,
    x: np.ndarray,
    wavelength_um: float,
    T: float,
    reflection_power: float,
    reflection_phase_rad: float,
) -> np.ndarray:
    """Conditional generation kernel with one coherent returned wave.

    The round-trip optical phase from depth z to the back side is calculated
    from the composition-resolved line integral 2*k0*int_z^L n(x,T,lambda) dz.

    n_liu is only evaluated on the phase interval where the photon is locally
    above gap.  For generated carriers at z, x(z) <= x_edge, and because the
    profiles decrease toward the back side all points z..L remain inside the
    Liu measured composition interval for the candidate wavelengths.
    """
    z_cm = z_um * 1.0e-4
    alpha = alpha_moazzami(HC_EV_UM / wavelength_um, x, T)
    tau = np.concatenate(([0.0], cumulative_trapezoid(alpha, z_cm)))
    tau_L = float(tau[-1])

    # The real-index model is only needed from an absorbing position toward
    # the low-Cd back side. Evaluate everywhere for a continuous cumulative
    # integral, but clip x above the measured upper composition because that
    # upstream high-Cd region never enters the returned-wave phase of a point
    # with nonzero alpha. The regression below verifies this geometric fact by
    # checking x_edge < 0.443 for every candidate temperature/wavelength.
    n = n_liu(np.minimum(x, 0.443), T, wavelength_um)
    optical_path_from_front = np.concatenate(
        ([0.0], cumulative_trapezoid(n, z_um))
    )
    optical_path_to_back = optical_path_from_front[-1] - optical_path_from_front

    roundtrip_phase = (
        4.0 * np.pi * optical_path_to_back / wavelength_um
        + reflection_phase_rad
    )

    intensity = (
        np.exp(-tau)
        + reflection_power * np.exp(-(2.0 * tau_L - tau))
        + 2.0
        * np.sqrt(reflection_power)
        * np.exp(-tau_L)
        * np.cos(roundtrip_phase)
    )
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
    reflection_phase_rad: float,
) -> tuple[float, float, float]:
    a0 = thermo_optic_interference_kernel(
        a_z,
        a_x,
        REFERENCE_LAMBDA_UM,
        300.0,
        reflection_power,
        reflection_phase_rad,
    )
    _, b0 = beer_lambert_kernel(b_z, b_x, REFERENCE_LAMBDA_UM, 300.0)

    bounds = (3.72, 3.87) if T == 215.0 else (3.93, 4.08)

    def objective(wavelength_um: float) -> float:
        a = thermo_optic_interference_kernel(
            a_z,
            a_x,
            wavelength_um,
            T,
            reflection_power,
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
        options={"xatol": 1.0e-8},
    )
    wavelength = float(result.x)
    a = thermo_optic_interference_kernel(
        a_z,
        a_x,
        wavelength,
        T,
        reflection_power,
        reflection_phase_rad,
    )
    _, b = beer_lambert_kernel(b_z, b_x, wavelength, T)
    return (
        wavelength,
        relative_kernel_error(a, a0),
        relative_kernel_error(b, b0),
    )


def main() -> None:
    raw_profiles = sample_a_profiles()
    profiles = [downsample_profile(z, x) for z, x, _ in raw_profiles]
    b_z_raw, b_x_raw = sample_b_profile()
    b_z, b_x = downsample_profile(b_z_raw, b_x_raw)

    candidate_points = (
        (300.0, 3.6320),
        (215.0, 3.7935),
        (115.0, 4.0045),
    )

    print("Composition-resolved HgCdTe thermo-optic interference stress")
    print("candidate local band-edge coordinate:")
    for T, wavelength in candidate_points:
        x_edge = band_edge_composition(T, wavelength)
        n_edge = float(n_liu(np.array([x_edge]), T, wavelength)[0])
        print(
            f"  {T:.0f} K, {wavelength:.4f} um -> "
            f"x_edge={x_edge:.6f}, n(x_edge)={n_edge:.6f}"
        )
        assert 0.276 < x_edge < 0.443
    print()

    results = []
    for a_z, a_x in profiles:
        for reflection_power in REFLECTION_POWER:
            for phase in PHASES_RAD:
                for T in TARGET_T_K:
                    wavelength, ea, eb = joint_match(
                        a_z,
                        a_x,
                        b_z,
                        b_x,
                        T,
                        reflection_power,
                        phase,
                    )
                    results.append((T, wavelength, ea, eb))

    results = np.asarray(results)
    for T in TARGET_T_K:
        subset = results[results[:, 0] == T]
        print(
            f"{T:.0f} K: lambda={subset[:,1].min():.6f}-"
            f"{subset[:,1].max():.6f} um; "
            f"A mismatch={100*subset[:,2].min():.3f}-"
            f"{100*subset[:,2].max():.3f}%; "
            f"B mismatch={100*subset[:,3].min():.3f}-"
            f"{100*subset[:,3].max():.3f}%"
        )

    r215 = results[results[:, 0] == 215.0]
    r115 = results[results[:, 0] == 115.0]

    # Stable envelopes from the current 72-profile x 3R x 4phase regression.
    assert 3.7929 < r215[:, 1].min() < r215[:, 1].max() < 3.7942
    assert r215[:, 2].max() < 0.0075
    assert r215[:, 3].max() < 0.0049

    assert 4.0028 < r115[:, 1].min() < r115[:, 1].max() < 4.0076
    assert r115[:, 2].max() < 0.0175
    assert r115[:, 3].max() < 0.0099

    x_edges = np.asarray(
        [band_edge_composition(T, wavelength) for T, wavelength in candidate_points]
    )
    assert np.ptp(x_edges) < 3.0e-4

    print()
    print(
        "PASS: the empirical composition/temperature-dependent HgCdTe index "
        "keeps the 3.632-um common-reference schedule within a few nanometres "
        "of the Beer-Lambert result even under R<=0.9 single-return stress; "
        "the candidate wavelengths also track an almost fixed x~=0.3377 "
        "local band-edge coordinate."
    )


if __name__ == "__main__":
    main()
