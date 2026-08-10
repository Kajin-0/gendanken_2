"""Finite-width generation-kernel translation invariance regression.

In a uniform drift-diffusion region with complex spatial propagation constant
`gamma`, a localized-source transfer has spatial dependence exp[gamma z]. If
wavelength translates a normalized generation kernel without changing its shape,

    p(z;zg) = g(z-zg),

then

    H(zg) = const * exp(gamma*zg)

for arbitrary kernel width, so d ln H/dzg = gamma exactly (away from physical
boundary clipping).

For a Gaussian whose variance changes with a scan coordinate a,

    d ln H/da = gamma*dzg/da + (gamma^2/2)*d(sigma^2)/da.

This file verifies both identities numerically.
"""

from __future__ import annotations

import numpy as np


GAMMA = 0.37 + 2.15j
Z = np.linspace(-6.0, 6.0, 60001)


def gaussian_density(z: np.ndarray, center: float, sigma: float) -> np.ndarray:
    p = np.exp(-0.5 * ((z - center) / sigma) ** 2)
    return p / np.trapezoid(p, z)


def H_numeric(center: float, sigma: float) -> complex:
    p = gaussian_density(Z, center, sigma)
    return complex(np.trapezoid(p * np.exp(GAMMA * Z), Z))


def log_derivative_center(center: float, sigma: float, step: float = 1e-4) -> complex:
    Hp = H_numeric(center + step, sigma)
    Hm = H_numeric(center - step, sigma)
    H0 = H_numeric(center, sigma)
    # d ln H = (1/H) dH avoids principal-log branch artifacts.
    return (Hp - Hm) / (2.0 * step * H0)


def main() -> None:
    widths = (0.03, 0.10, 0.30, 0.70)
    derivative_errors = []
    for sigma in widths:
        estimate = log_derivative_center(0.25, sigma)
        derivative_errors.append(abs(estimate - GAMMA) / abs(GAMMA))

    # Scan parameter a changes both center and width.
    # center(a)=z0+c*a, sigma^2(a)=s0^2+k*a.
    a0 = 0.20
    z0 = -0.10
    c = 0.65
    s0 = 0.25
    k = 0.08

    def center_of_a(a: float) -> float:
        return z0 + c * a

    def sigma_of_a(a: float) -> float:
        return float(np.sqrt(s0 * s0 + k * a))

    da = 1.0e-5
    Hp = H_numeric(center_of_a(a0 + da), sigma_of_a(a0 + da))
    Hm = H_numeric(center_of_a(a0 - da), sigma_of_a(a0 - da))
    H0 = H_numeric(center_of_a(a0), sigma_of_a(a0))
    derivative_numeric = (Hp - Hm) / (2.0 * da * H0)
    derivative_exact = GAMMA * c + 0.5 * GAMMA**2 * k
    shape_error = abs(derivative_numeric - derivative_exact) / abs(derivative_exact)

    print("Generation-kernel translation invariance")
    print(
        "arbitrary-width d ln H/dzg relative errors = "
        + ", ".join(f"{e:.3e}" for e in derivative_errors)
    )
    print(
        "changing-Gaussian-shape derivative relative error = "
        f"{shape_error:.3e}"
    )
    print(
        "exact shape term = (gamma^2/2) d(sigma^2)/da = "
        f"{(0.5 * GAMMA**2 * k).real:+.6f}"
        f"{(0.5 * GAMMA**2 * k).imag:+.6f}j"
    )

    assert max(derivative_errors) < 2.0e-8
    assert shape_error < 2.0e-8

    print()
    print(
        "PASS: generation width alone does not bias the complex spatial slope "
        "when the kernel translates rigidly. Only scan-dependent kernel-shape "
        "change contributes the predicted additional complex term."
    )


if __name__ == "__main__":
    main()
