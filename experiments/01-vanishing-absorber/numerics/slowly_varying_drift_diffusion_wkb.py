"""Slowly varying 1-D drift-diffusion WKB/local-propagation regression.

For

    D(z) u'' + v(z) u' - s u = 0,

write gamma=u'/u. The exact Riccati equation is

    D(gamma' + gamma^2) + v gamma - s = 0.

The local algebraic branch gamma0 solves

    D gamma0^2 + v gamma0 - s = 0,

and the first slow-variation correction is

    gamma1 = D (D' gamma0^2 + v' gamma0)/(v + 2D gamma0)^2.

This regression integrates the exact Riccati equation along a slowly varying
branch and checks that gamma0+gamma1 improves the local approximation.
It is an asymptotic-theory regression, not a device prediction.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import solve_ivp


L = 1.0
OMEGA = 3.0
S = 1j * OMEGA


def velocity(z: np.ndarray | float) -> np.ndarray | float:
    return 1.5 * (1.0 + 0.15 * np.sin(np.pi * z))


def velocity_prime(z: np.ndarray | float) -> np.ndarray | float:
    return 1.5 * 0.15 * np.pi * np.cos(np.pi * z)


def diffusion(z: np.ndarray | float) -> np.ndarray | float:
    return 0.05 * (1.0 + 0.10 * np.cos(np.pi * z))


def diffusion_prime(z: np.ndarray | float) -> np.ndarray | float:
    return -0.05 * 0.10 * np.pi * np.sin(np.pi * z)


def gamma0(z: np.ndarray | float) -> np.ndarray | complex:
    v = velocity(z)
    D = diffusion(z)
    return (np.sqrt(v * v + 4.0 * D * S) - v) / (2.0 * D)


def gamma1(z: np.ndarray) -> np.ndarray:
    g0 = gamma0(z)
    v = velocity(z)
    D = diffusion(z)
    vp = velocity_prime(z)
    Dp = diffusion_prime(z)
    return D * (Dp * g0**2 + vp * g0) / (v + 2.0 * D * g0) ** 2


def riccati_rhs(z: float, y: np.ndarray) -> list[float]:
    g = y[0] + 1j * y[1]
    v = float(velocity(z))
    D = float(diffusion(z))
    gp = (S - v * g - D * g * g) / D
    return [float(np.real(gp)), float(np.imag(gp))]


def main() -> None:
    # Seed the slowly varying physical branch at z=0 with the local root and
    # integrate forward. This tests the asymptotic branch itself rather than a
    # particular finite-device entrance boundary layer.
    g_init = complex(gamma0(0.0))
    sol = solve_ivp(
        riccati_rhs,
        (0.0, L),
        (g_init.real, g_init.imag),
        rtol=1.0e-10,
        atol=1.0e-12,
        max_step=1.0e-3,
        dense_output=True,
    )

    z = np.linspace(0.10, 0.90, 801)
    exact = sol.sol(z)[0] + 1j * sol.sol(z)[1]
    leading = gamma0(z)
    corrected = leading + gamma1(z)

    err0 = np.abs((exact - leading) / exact)
    err1 = np.abs((exact - corrected) / exact)

    # Dimensionless first-correction estimator |gamma1/gamma0|.
    eps_wkb = np.abs(gamma1(z) / leading)

    print("Slowly varying drift-diffusion local propagation")
    print(
        "leading gamma0 relative error median/max = "
        f"{np.median(err0):.6f}/{np.max(err0):.6f}"
    )
    print(
        "gamma0+gamma1 relative error median/max = "
        f"{np.median(err1):.6f}/{np.max(err1):.6f}"
    )
    print(
        "|gamma1/gamma0| median/max = "
        f"{np.median(eps_wkb):.6f}/{np.max(eps_wkb):.6f}"
    )

    assert np.median(err0) < 0.008
    assert np.max(err0) < 0.015
    assert np.median(err1) < 0.0011
    assert np.max(err1) < 0.0014
    assert np.median(err1) < 0.20 * np.median(err0)

    print()
    print(
        "PASS: the local algebraic propagation constant is accurate at the "
        "percent level for this explicit slowly varying stress, and the first "
        "gradient correction reduces the median error to about 0.1%. This "
        "supports using the local complex spatial/spectral slope as a controlled "
        "estimator of v(z),D(z) when the WKB parameter is small."
    )


if __name__ == "__main__":
    main()
