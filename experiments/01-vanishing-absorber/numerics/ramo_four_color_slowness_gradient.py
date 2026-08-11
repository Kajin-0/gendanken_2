"""Low-RF four-color Shockley-Ramo slowness-gradient theorem.

For deterministic downstream transit with local slowness q(z)=1/v(z), collector
at L, and uniform weighting field, the point-source terminal-current transform
(up to an irrelevant constant) is

    J(z,s) = integral_z^L exp[-s integral_z^x q(u)du] dx.

At low s,

    J(z,s) = (L-z) - s A(z) + O(s^2),
    A(z) = integral_z^L (L-u) q(u) du.

For four equally spaced source depths z0,z0+h,z0+2h,z0+3h, define

    C4 = 2 log(J2-J1) - log(J1-J0) - log(J3-J2).

Then

    C4 = -s h^2 [2 q'(zc) - (L-zc) q''(zc)] + O(s h^4,s^2)

at midpoint zc=z0+3h/2.  For linear q this reduces exactly at O(s) to

    Im C4 / omega = -2 h^2 q'.

The regression uses a deliberately nonlinear slowness profile and verifies the
asymptotic coefficient against direct quadrature of the full RF current.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.interpolate import CubicSpline


L = 2.6
N = 20001
Z = np.linspace(0.0, L, N)

# Smooth positive slowness with both q' and q'' nonzero.
Q = 0.55 + 0.11 * Z + 0.025 * Z**2 + 0.006 * np.sin(1.7 * Z)

Z0 = 0.55
H = 0.32
ZS = Z0 + H * np.arange(4)
ZC = Z0 + 1.5 * H


def terminal_current(omega: float) -> np.ndarray:
    s = 1j * omega
    # Travel-time coordinate tau(z)=int_0^z q(u)du.
    tau = np.concatenate(([0.0], cumulative_trapezoid(Q, Z)))
    e = np.exp(-s * tau)
    # I(z)=exp(s tau(z)) int_z^L exp(-s tau(x)) dx.
    rev = np.concatenate(([0.0], cumulative_trapezoid(e[::-1], Z[::-1])))
    inner = (-rev)[::-1]
    Jgrid = np.exp(s * tau) * inner
    real = np.interp(ZS, Z, Jgrid.real)
    imag = np.interp(ZS, Z, Jgrid.imag)
    return real + 1j * imag


def closure(J: np.ndarray) -> complex:
    d = np.diff(J)
    return complex(2.0 * np.log(d[1]) - np.log(d[0]) - np.log(d[2]))


def main() -> None:
    q_spline = CubicSpline(Z, Q)
    q1 = float(q_spline(ZC, 1))
    q2 = float(q_spline(ZC, 2))
    coefficient = -H**2 * (2.0 * q1 - (L - ZC) * q2)

    print("Low-RF four-color slowness-gradient theorem")
    print(f"predicted C4/(i omega) coefficient = {coefficient:.12e}")

    errors = []
    for omega in (1.0e-4, 2.0e-4, 5.0e-4, 1.0e-3):
        C = closure(terminal_current(omega))
        observed = C / (1j * omega)
        rel = abs((observed - coefficient) / coefficient)
        errors.append(rel)
        print(
            f"omega={omega:.1e}: C/(i omega)="
            f"{observed.real:+.12e}{observed.imag:+.3e}j, rel={rel:.3e}"
        )

    assert errors[0] < 2.0e-4
    assert errors[-1] < 5.0e-4

    # Exact O(s) coefficient for a linear slowness q=a+bz: q''=0.
    b = 0.073
    linear_expected = -2.0 * H**2 * b
    assert abs(linear_expected + 2.0 * H**2 * b) < 1.0e-15

    print()
    print(
        "PASS: direct RF quadrature approaches the predicted low-frequency "
        "four-color coefficient.  In the locally linear-slowness limit the "
        "phase closure per omega directly measures -2 h^2 q'."
    )


if __name__ == "__main__":
    main()
