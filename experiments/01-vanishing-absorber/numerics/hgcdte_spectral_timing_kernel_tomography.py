"""Regression for HGCDTE_SPECTRAL_TIMING_KERNEL_TOMOGRAPHY.md.

This is a synthetic inverse-problem check, not a calibrated HgCdTe model.

It verifies three statements for a linear gap and a power-law absorption edge:

1. Away from downstream truncation, the spectral derivative of mean delay
   equals the stationary optical-kernel average of inverse velocity.
2. For a narrow kernel and a slowly varying velocity profile, the inferred
   effective velocity is close to the true velocity evaluated near the mean
   generation offset.
3. Near the long-wave cutoff, finite eligible-region truncation invalidates
   the stationary-kernel approximation and the naive point inversion can be
   strongly biased.
"""

from __future__ import annotations

import math
import numpy as np


EG_OUT = 1.0
EG_IN = 2.0
G = 1.0
L = 1.0
BETA = 0.5
N = BETA + 1.0
ELL_ALPHA = 0.05


def velocity(x: np.ndarray | float) -> np.ndarray | float:
    """Synthetic nonuniform positive collection velocity."""
    return 0.7 + 0.6 * np.asarray(x)


def path_delay(x: np.ndarray | float) -> np.ndarray | float:
    """Exact integral int_x^L ds / velocity(s)."""
    x = np.asarray(x)
    return np.log((0.7 + 0.6 * L) / (0.7 + 0.6 * x)) / 0.6


def kernel(z: np.ndarray) -> np.ndarray:
    """Stationary Weibull generation-offset density."""
    return (
        N
        / ELL_ALPHA
        * (z / ELL_ALPHA) ** (N - 1.0)
        * np.exp(-(z / ELL_ALPHA) ** N)
    )


def tau_for_energy(e_gamma: float) -> float:
    d = (e_gamma - EG_OUT) / G
    return (d / ELL_ALPHA) ** N


def mean_delay(e_gamma: float, points: int = 16000) -> float:
    xg = (EG_IN - e_gamma) / G
    d = L - xg
    if d <= 0.0:
        return 0.0

    z = np.linspace(0.0, d, points)
    p = kernel(z)
    norm = 1.0 - math.exp(-tau_for_energy(e_gamma))
    return float(np.trapezoid(p * path_delay(xg + z), z) / norm)


def derivative(e_gamma: float, h: float = 2.0e-4) -> float:
    return (mean_delay(e_gamma + h) - mean_delay(e_gamma - h)) / (2.0 * h)


def stationary_kernel_inverse_velocity(e_gamma: float, points: int = 20000) -> float:
    xg = (EG_IN - e_gamma) / G
    d = L - xg
    z = np.linspace(0.0, d, points)
    return float(np.trapezoid(kernel(z) / velocity(xg + z), z))


def main() -> None:
    # High-optical-depth cases: stationary-kernel identity should hold.
    for e_gamma in (1.30, 1.50, 1.70):
        tau = tau_for_energy(e_gamma)
        assert tau > 10.0

        lhs = G * derivative(e_gamma)
        rhs = stationary_kernel_inverse_velocity(e_gamma)
        rel = abs(lhs - rhs) / rhs
        assert rel < 5.0e-4, (e_gamma, lhs, rhs, rel)

    # Narrow-kernel / slowly varying profile: inferred harmonic-like velocity
    # lies close to the physical velocity evaluated near the mean optical offset.
    mean_offset = ELL_ALPHA * math.gamma(1.0 + 1.0 / N)
    e_gamma = 1.50
    xg = (EG_IN - e_gamma) / G
    v_spec = 1.0 / (G * derivative(e_gamma))
    v_shift = float(velocity(xg + mean_offset))
    assert abs(v_spec - v_shift) / v_shift < 5.0e-3

    # Near cutoff the eligible region truncates the kernel.  Demonstrate that
    # treating the measurement as an untruncated stationary convolution fails.
    e_cut = 1.10
    assert tau_for_energy(e_cut) < 3.0
    lhs_cut = G * derivative(e_cut)
    rhs_cut = stationary_kernel_inverse_velocity(e_cut)
    truncation_mismatch = abs(lhs_cut - rhs_cut) / rhs_cut
    assert truncation_mismatch > 0.05

    print("PASS: finite-depth spectral timing tomography regression")
    print(f"mean optical offset = {mean_offset:.6f}")
    print(f"mid-band v_spec = {v_spec:.6f}, v(xg+<z>) = {v_shift:.6f}")
    print(f"near-cutoff stationary-kernel mismatch = {truncation_mismatch:.3%}")


if __name__ == "__main__":
    main()
