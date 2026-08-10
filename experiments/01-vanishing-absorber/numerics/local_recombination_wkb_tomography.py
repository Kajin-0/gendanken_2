"""Local recombination WKB tomography regression.

For slowly varying v(z), D(z), kappa(z), the local algebraic first-passage root is

    gamma_s(z) = [sqrt(v^2 + 4D(kappa+s)) - v]/(2D).

At leading WKB order the DC-normalized RF slope

    Gamma = gamma_{i omega} - gamma_0

has exactly the uniform recombination-free form with

    Vstar(z) = sqrt(v(z)^2 + 4D(z)kappa(z)).

Thus local normalized RF estimates D,Vstar; adding the local DC collection slope
gamma0 estimates v,kappa. This script integrates the exact Riccati equation for
smooth variable coefficients and quantifies the leading local inversion error.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import solve_ivp


L = 1.0
OMEGA = 2.5


def velocity(z: np.ndarray | float) -> np.ndarray | float:
    return 1.6 * (1.0 + 0.10 * np.sin(np.pi * z))


def diffusion(z: np.ndarray | float) -> np.ndarray | float:
    return 0.06 * (1.0 + 0.08 * np.cos(np.pi * z))


def kappa(z: np.ndarray | float) -> np.ndarray | float:
    return 0.40 * (1.0 + 0.12 * np.sin(2.0 * np.pi * z))


def local_root(z: float, s: complex) -> complex:
    v = float(velocity(z))
    D = float(diffusion(z))
    k = float(kappa(z))
    return (np.sqrt(v * v + 4.0 * D * (k + s)) - v) / (2.0 * D)


def integrate_riccati(s: complex):
    g_init = local_root(0.0, s)

    def rhs(z: float, y: np.ndarray) -> list[float]:
        g = y[0] + 1j * y[1]
        v = float(velocity(z))
        D = float(diffusion(z))
        k = float(kappa(z))
        gp = ((k + s) - v * g - D * g * g) / D
        return [float(np.real(gp)), float(np.imag(gp))]

    return solve_ivp(
        rhs,
        (0.0, L),
        (g_init.real, g_init.imag),
        rtol=1.0e-10,
        atol=1.0e-12,
        max_step=1.0e-3,
        dense_output=True,
    )


def invert_conditional_gamma(Gamma: np.ndarray):
    a = np.real(Gamma)
    b = np.imag(Gamma)
    modulus2 = a * a + b * b
    D = OMEGA * a / (b * modulus2)
    Vstar = OMEGA * (b * b - a * a) / (b * modulus2)
    return D, Vstar


def stats(app: np.ndarray, true: np.ndarray) -> tuple[float, float]:
    rel = np.abs(app / true - 1.0)
    return float(np.median(rel)), float(np.max(rel))


def main() -> None:
    sol0 = integrate_riccati(0.0)
    solw = integrate_riccati(1j * OMEGA)

    z = np.linspace(0.10, 0.90, 801)
    gamma0 = sol0.sol(z)[0] + 1j * sol0.sol(z)[1]
    gammaw = solw.sol(z)[0] + 1j * solw.sol(z)[1]
    Gamma = gammaw - gamma0

    D_app, Vstar_app = invert_conditional_gamma(Gamma)
    gamma0_real = np.real(gamma0)
    v_app = Vstar_app - 2.0 * D_app * gamma0_real
    kappa_app = Vstar_app * gamma0_real - D_app * gamma0_real**2

    D_true = diffusion(z)
    v_true = velocity(z)
    kappa_true = kappa(z)
    Vstar_true = np.sqrt(v_true**2 + 4.0 * D_true * kappa_true)

    D_stat = stats(D_app, D_true)
    V_stat = stats(Vstar_app, Vstar_true)
    v_stat = stats(v_app, v_true)
    k_stat = stats(kappa_app, kappa_true)

    print("Local recombination WKB tomography")
    print(f"D relative error median/max = {D_stat[0]:.6f}/{D_stat[1]:.6f}")
    print(f"Vstar relative error median/max = {V_stat[0]:.6f}/{V_stat[1]:.6f}")
    print(f"v relative error median/max = {v_stat[0]:.6f}/{v_stat[1]:.6f}")
    print(f"kappa relative error median/max = {k_stat[0]:.6f}/{k_stat[1]:.6f}")

    assert D_stat[0] < 0.013
    assert D_stat[1] < 0.026
    assert V_stat[0] < 0.006
    assert V_stat[1] < 0.011
    assert v_stat[0] < 0.007
    assert v_stat[1] < 0.012
    assert k_stat[0] < 0.016
    assert k_stat[1] < 0.027

    print()
    print(
        "PASS: for this explicit smooth variable-coefficient stress, the local "
        "uniform recombination identifiability formulas recover D,Vstar,v,kappa "
        "to percent-level accuracy away from the seeded boundary. The exact "
        "uniform degeneracy therefore survives as the leading local WKB law, "
        "with spatial-gradient corrections providing the expected bias."
    )


if __name__ == "__main__":
    main()
