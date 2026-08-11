"""Three-color complex closure as a discrete curvature of timing cumulants.

For any three positive transit-time distributions with characteristic functions
H_j(omega), define

    L(omega)=2 ln H_2 - ln H_1 - ln H_3

on the analytic log branch around omega=0. Since

    ln H_j = sum_n (-i omega)^n kappa_{n,j}/n!,

exactly

    L = sum_n (-i omega)^n C_n/n!,
    C_n=2 kappa_{n,2}-kappa_{n,1}-kappa_{n,3}.

If the three channels correspond to equally spaced internal coordinates z-h,z,z+h
and kappa_n(z) is smooth, C_n=-h^2 kappa_n''+O(h^4). Thus RF orders
spatially resolve curvature of mean delay, variance, skewness, etc.

This regression uses arbitrary discrete timing distributions, checks the first
four cumulants against finite derivatives of L at omega=0, and verifies the
spatial-curvature expansion on synthetic smooth cumulant fields.
"""

from __future__ import annotations

import math
import numpy as np


# Three arbitrary discrete transit-time distributions.
TIMES = (
    np.asarray((0.4, 1.0, 1.8, 3.1)),
    np.asarray((0.5, 1.2, 2.0, 3.4)),
    np.asarray((0.7, 1.4, 2.4, 3.9)),
)
PROBS = (
    np.asarray((0.15, 0.35, 0.30, 0.20)),
    np.asarray((0.10, 0.30, 0.40, 0.20)),
    np.asarray((0.20, 0.25, 0.35, 0.20)),
)


def H(index: int, omega: float) -> complex:
    p = PROBS[index] / np.sum(PROBS[index])
    t = TIMES[index]
    return complex(np.sum(p * np.exp(-1j * omega * t)))


def cumulants(index: int) -> np.ndarray:
    p = PROBS[index] / np.sum(PROBS[index])
    t = TIMES[index]
    mu = float(np.sum(p * t))
    centered = t - mu
    k2 = float(np.sum(p * centered**2))
    k3 = float(np.sum(p * centered**3))
    mu4 = float(np.sum(p * centered**4))
    k4 = mu4 - 3.0 * k2**2
    return np.asarray((mu, k2, k3, k4))


def closure(omega: float) -> complex:
    # Near zero, principal logarithms lie on the analytic branch.
    return 2.0 * np.log(H(1, omega)) - np.log(H(0, omega)) - np.log(H(2, omega))


def main() -> None:
    kappas = np.asarray([cumulants(j) for j in range(3)])
    C = 2.0 * kappas[1] - kappas[0] - kappas[2]

    print("Three-color timing-cumulant curvature hierarchy")
    for n, value in enumerate(C, start=1):
        print(f"C_{n}=2 kappa_{n},2-kappa_{n},1-kappa_{n},3 = {value:.12f}")

    # Compare exact closure to fourth-order cumulant series at small omega.
    omega = 2.0e-3
    series = sum(
        ((-1j * omega) ** n) * C[n - 1] / math.factorial(n)
        for n in range(1, 5)
    )
    exact = closure(omega)
    error = abs(exact - series)
    print(f"fourth-order series error at omega={omega:g} = {error:.3e}")
    assert error < 2.0e-13

    # Direct leading-order finite derivative checks.
    eps = 1.0e-5
    Lp = closure(eps)
    Lm = closure(-eps)
    d1 = (Lp - Lm) / (2.0 * eps)
    d2 = (Lp - 2.0 * closure(0.0) + Lm) / eps**2
    assert abs(d1 - (-1j) * C[0]) < 1.0e-8
    assert abs(d2 - (-1.0) * C[1]) < 5.0e-6

    # Smooth spatial example: kappa_n(z)=a+bz+cz^2+dz^4. Equal-spacing
    # closure equals -h^2 kappa'' - h^4 kappa''''/12 exactly for this polynomial.
    h = 0.30
    z0 = 1.1
    coefficients = (
        (1.0, 0.4, 0.12, 0.010),
        (0.3, -0.1, 0.08, 0.006),
        (0.05, 0.03, -0.02, 0.004),
    )
    for a, b, c, d in coefficients:
        f = lambda z: a + b * z + c * z**2 + d * z**4
        C_exact = 2.0 * f(z0) - f(z0 - h) - f(z0 + h)
        f2 = 2.0 * c + 12.0 * d * z0**2
        f4 = 24.0 * d
        C_taylor = -h**2 * f2 - h**4 * f4 / 12.0
        assert abs(C_exact - C_taylor) < 2.0e-14

    print()
    print(
        "PASS: the complex three-color closure is exactly the generating "
        "function of discrete timing-cumulant curvature. At equally spaced "
        "internal coordinates, successive RF orders measure spatial curvature "
        "of mean delay, variance, skewness, and higher cumulants."
    )


if __name__ == "__main__":
    main()
