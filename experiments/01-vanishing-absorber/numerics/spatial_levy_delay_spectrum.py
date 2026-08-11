"""Spatial Levy delay spectrum for homogeneous regenerative first passage.

A timing convolution semigroup over distance has

    E[e^{-s T_d}] = exp[-d Phi(s)],
    Phi(s)=a s + integral (1-e^{-s t}) nu(t) dt.

For uniform Brownian drift-diffusion first passage,

    Phi_DD(s)=(sqrt(w^2+4Ds)-w)/(2D)

and the Levy density is

    nu_DD(t)=1/(2 sqrt(pi D)) * t^(-3/2) * exp[-w^2 t/(4D)].

This script verifies the Levy integral against the exact exponent and then adds
a compound-Poisson exponential waiting channel

    nu_trap(t)=lambda*beta*exp(-beta t),

whose exponent is lambda*s/(beta+s). The addition illustrates how a regenerative
trap waiting-time mechanism adds positive spectral weight to the per-distance
delay spectrum.
"""

from __future__ import annotations

import math
import numpy as np
from scipy.integrate import quad


D = 0.70
W = 1.40
TRAP_RATE_PER_DISTANCE = 0.35
TRAP_BETA = 1.80


def phi_dd(s: complex) -> complex:
    return (np.sqrt(W * W + 4.0 * D * s) - W) / (2.0 * D)


def nu_dd(t: float) -> float:
    return (
        1.0
        / (2.0 * math.sqrt(math.pi * D))
        * t ** (-1.5)
        * math.exp(-(W * W) * t / (4.0 * D))
    )


def nu_trap(t: float) -> float:
    return TRAP_RATE_PER_DISTANCE * TRAP_BETA * math.exp(-TRAP_BETA * t)


def levy_integral_real_s(s: float, density) -> float:
    value, _ = quad(
        lambda t: (1.0 - math.exp(-s * t)) * density(t),
        0.0,
        np.inf,
        epsabs=2.0e-11,
        epsrel=2.0e-11,
        limit=500,
    )
    return float(value)


def levy_integral_iomega(omega: float, density) -> complex:
    real, _ = quad(
        lambda t: (1.0 - math.cos(omega * t)) * density(t),
        0.0,
        np.inf,
        epsabs=2.0e-10,
        epsrel=2.0e-10,
        limit=700,
    )
    imag, _ = quad(
        lambda t: math.sin(omega * t) * density(t),
        0.0,
        np.inf,
        epsabs=2.0e-10,
        epsrel=2.0e-10,
        limit=700,
    )
    return complex(real, imag)


def moment(density, n: int) -> float:
    value, _ = quad(
        lambda t: t**n * density(t),
        0.0,
        np.inf,
        epsabs=2.0e-10,
        epsrel=2.0e-10,
        limit=700,
    )
    return float(value)


def main() -> None:
    print("Spatial Levy delay spectrum")
    print("drift-diffusion Levy density -> exact inverse-Gaussian exponent")

    for s in (0.1, 0.5, 2.0, 10.0):
        numeric = levy_integral_real_s(s, nu_dd)
        exact = float(np.real(phi_dd(s)))
        error = abs(numeric - exact)
        print(f"  s={s:4.1f}: numeric={numeric:.12f}, exact={exact:.12f}, error={error:.3e}")
        assert error < 3.0e-11

    # Levy moments per unit distance reproduce all timing cumulants. For DD,
    # integral t nu dt = 1/w and higher moments give the inverse-Gaussian
    # cumulant densities.
    print()
    print("per-distance cumulants from Levy moments")
    for n in range(1, 5):
        numeric = moment(nu_dd, n)
        if n == 1:
            exact = 1.0 / W
        else:
            odd_df = math.prod(range(1, 2 * n - 2, 2))
            exact = odd_df * (2.0 * D) ** (n - 1) / W ** (2 * n - 1)
        print(f"  n={n}: numeric={numeric:.12f}, exact={exact:.12f}")
        assert abs(numeric / exact - 1.0) < 3.0e-10

    print()
    print("RF exponent with added exponential trap-wait spectrum")
    for omega in (0.2, 1.0, 4.0):
        numeric = levy_integral_iomega(omega, nu_dd) + levy_integral_iomega(
            omega, nu_trap
        )
        exact = phi_dd(1j * omega) + (
            TRAP_RATE_PER_DISTANCE * (1j * omega) / (TRAP_BETA + 1j * omega)
        )
        error = abs(numeric - exact)
        print(
            f"  omega={omega:.2f}: Re Phi={numeric.real:.9f}, "
            f"Im Phi={numeric.imag:.9f}, error={error:.3e}"
        )
        assert error < 2.0e-9

    print()
    print(
        "PASS: the uniform drift-diffusion propagation exponent is exactly the "
        "Levy-Khintchine transform of a positive t^(-3/2) exponential-cutoff "
        "delay spectrum. An independent regenerative trap-wait process adds its "
        "own positive Levy spectral weight linearly in the spatial exponent."
    )


if __name__ == "__main__":
    main()
