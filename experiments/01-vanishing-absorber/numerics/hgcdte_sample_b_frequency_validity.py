"""RF-frequency validity of the mean-delay phase approximation for sample B.

Uses the literature-constrained 150 V/cm sample-B optical generation kernels
and a deliberately simple deterministic transit law T=z/v.  It compares the
exact optical timing transfer H=<exp(-i Omega z/v)> against the first-moment
phase -Omega<z>/v.

This isolates phase nonlinearity caused by optical generation-depth spread.
It does not include additional carrier diffusion/scattering or electrical
transfer functions, which can only tighten the safe low-frequency range.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.optimize import brentq

from hgcdte_published_sample_b_forward_matrix import (
    FIELD_VALUES,
    HC_EV_UM,
    N_FINE,
    T_K,
    W_CM,
    W_UM,
    X_LOW,
    alpha_moazzami,
    eg_hansen,
)

FIELD_V_CM = 150.0
VELOCITIES = (1.0e5, 5.0e4, 3.0e4, 1.0e4)
FREQUENCIES_GHZ = (1.0, 2.0, 5.0)
TEST_WAVELENGTHS = (2.80, 3.20, 3.37, 3.50, 3.70, 3.85, 3.88)

PHASE_ERROR_LIMIT_DEG = 0.10
MAGNITUDE_LIMIT = 0.98


def x_high_for_field(field_v_cm: float) -> float:
    eg_low = float(eg_hansen(X_LOW))
    target = eg_low + field_v_cm * W_CM
    return float(brentq(lambda xx: eg_hansen(xx) - target, X_LOW, 0.60))


def fine_generation_distribution(wavelength_um: float) -> tuple[np.ndarray, np.ndarray]:
    z_um = np.linspace(0.0, W_UM, N_FINE)
    z_cm = z_um * 1.0e-4
    x_high = x_high_for_field(FIELD_V_CM)
    x = x_high + (X_LOW - x_high) * z_um / W_UM

    energy = HC_EV_UM / wavelength_um
    alpha = alpha_moazzami(energy, x, T_K)
    tau = np.concatenate(([0.0], cumulative_trapezoid(alpha, z_cm)))
    p_abs = 1.0 - np.exp(-tau[-1])
    if p_abs <= 0.0:
        raise RuntimeError("No absorption")

    density_cm = alpha * np.exp(-tau) / p_abs
    density_cm /= np.trapezoid(density_cm, z_cm)
    return z_cm * 1.0e-2, density_cm  # z in m; density still per cm for dz_cm integration


def exact_transfer(
    wavelength_um: float,
    velocity_m_s: float,
    frequency_hz: float,
) -> tuple[complex, float]:
    z_m, density_cm = fine_generation_distribution(wavelength_um)
    z_cm = z_m * 1.0e2
    omega = 2.0 * np.pi * frequency_hz

    H = np.trapezoid(
        density_cm * np.exp(-1j * omega * z_m / velocity_m_s),
        z_cm,
    )
    mean_z_m = float(np.trapezoid(density_cm * z_m, z_cm))
    return H, mean_z_m


def phase_error_deg(
    wavelength_um: float,
    velocity_m_s: float,
    frequency_hz: float,
) -> tuple[float, float]:
    H, mean_z_m = exact_transfer(wavelength_um, velocity_m_s, frequency_hz)
    exact_phase = np.angle(H)
    first_moment_phase = -2.0 * np.pi * frequency_hz * mean_z_m / velocity_m_s
    wrapped_error = np.angle(np.exp(1j * (exact_phase - first_moment_phase)))
    return abs(float(np.degrees(wrapped_error))), abs(H)


def worst_case(velocity_m_s: float, frequency_hz: float) -> tuple[float, float]:
    errors = []
    magnitudes = []
    for wavelength in TEST_WAVELENGTHS:
        error, magnitude = phase_error_deg(wavelength, velocity_m_s, frequency_hz)
        errors.append(error)
        magnitudes.append(magnitude)
    return max(errors), min(magnitudes)


def frequency_envelope(velocity_m_s: float) -> tuple[float, float]:
    grid_hz = np.linspace(0.05e9, 10.0e9, 800)
    phase_ok = []
    magnitude_ok = []
    for frequency in grid_hz:
        error, magnitude = worst_case(velocity_m_s, frequency)
        if error < PHASE_ERROR_LIMIT_DEG:
            phase_ok.append(frequency)
        if magnitude > MAGNITUDE_LIMIT:
            magnitude_ok.append(frequency)

    return max(phase_ok), max(magnitude_ok)


def main() -> None:
    print("Sample-B optical-generation RF validity")
    print("exact H=<exp(-i Omega z/v)> vs first-moment phase")
    print()

    for velocity in VELOCITIES:
        print(f"v = {velocity:.2e} m/s")
        for frequency_ghz in FREQUENCIES_GHZ:
            error, magnitude = worst_case(velocity, frequency_ghz * 1.0e9)
            print(
                f"  f={frequency_ghz:.1f} GHz: "
                f"worst phase error={error:.4f} deg, min |H|={magnitude:.4f}"
            )

        f_phase, f_mag = frequency_envelope(velocity)
        print(
            f"  max f for <{PHASE_ERROR_LIMIT_DEG:.2f} deg optical phase bias "
            f"~ {f_phase/1e9:.3f} GHz"
        )
        print(
            f"  max f for optical |H|>{MAGNITUDE_LIMIT:.2f} "
            f"~ {f_mag/1e9:.3f} GHz"
        )
        print(
            f"  magnitude criterion: f W / v ~ "
            f"{f_mag * W_UM * 1e-6 / velocity:.3f}"
        )
        print()

    # Stable envelopes from the current optical kernel set.
    e_1e5, m_1e5 = worst_case(1.0e5, 1.0e9)
    e_3e4, m_3e4 = worst_case(3.0e4, 1.0e9)
    e_1e4, m_1e4 = worst_case(1.0e4, 1.0e9)

    assert e_1e5 < 0.002 and m_1e5 > 0.998
    assert 0.03 < e_3e4 < 0.06 and m_3e4 > 0.98
    assert 1.0 < e_1e4 < 1.5 and 0.84 < m_1e4 < 0.87

    _, fmag_1e5 = frequency_envelope(1.0e5)
    dimensionless = fmag_1e5 * W_UM * 1e-6 / 1.0e5
    assert 0.12 < dimensionless < 0.14

    print(
        "PASS: optical-generation broadening alone gives an approximate "
        "|H|>0.98 envelope f <~ 0.13 v/W for the current sample-B kernels"
    )


if __name__ == "__main__":
    main()
