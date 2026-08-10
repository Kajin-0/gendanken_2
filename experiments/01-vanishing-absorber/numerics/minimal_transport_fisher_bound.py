"""Fisher-information regression for the minimal two-depth DC + complex-RF test.

Natural parameters are theta=(D,Vstar,gamma0), where DC-normalized RF obeys

    D Gamma^2 + Vstar Gamma = i omega

and the DC log-collection spatial slope is gamma0.

For two generation coordinates separated by Delta z, the measured real data are

    m = Delta z * [gamma0, Re Gamma, Im Gamma].

The exact complex sensitivities follow by implicit differentiation:

    dGamma/dD = -Gamma^2/(Vstar+2D Gamma)
    dGamma/dV = -Gamma/(Vstar+2D Gamma).

This file checks those derivatives against finite differences and constructs the
Fisher/CRLB matrices.
"""

from __future__ import annotations

import numpy as np


D = 0.08
VSTAR = 1.60
GAMMA0 = 0.24
OMEGA = 3.0
DELTA_Z = 0.85
SIGMA_DC = 0.010
SIGMA_LOGMAG = 0.003
SIGMA_PHASE = 0.002


def Gamma_of(D_value: float, V_value: float) -> complex:
    return (
        np.sqrt(V_value * V_value + 4j * D_value * OMEGA) - V_value
    ) / (2.0 * D_value)


def analytic_derivatives(Gamma: complex) -> tuple[complex, complex]:
    denom = VSTAR + 2.0 * D * Gamma
    dD = -(Gamma * Gamma) / denom
    dV = -Gamma / denom
    return dD, dV


def main() -> None:
    Gamma = Gamma_of(D, VSTAR)
    dD, dV = analytic_derivatives(Gamma)

    step_D = 1.0e-6
    step_V = 1.0e-6
    dD_fd = (
        Gamma_of(D + step_D, VSTAR) - Gamma_of(D - step_D, VSTAR)
    ) / (2.0 * step_D)
    dV_fd = (
        Gamma_of(D, VSTAR + step_V) - Gamma_of(D, VSTAR - step_V)
    ) / (2.0 * step_V)

    err_D = abs(dD - dD_fd) / abs(dD)
    err_V = abs(dV - dV_fd) / abs(dV)

    # Jacobian rows correspond to [DC log amplitude, RF log magnitude, RF phase].
    J = DELTA_Z * np.array(
        [
            [0.0, 0.0, 1.0],
            [np.real(dD), np.real(dV), 0.0],
            [np.imag(dD), np.imag(dV), 0.0],
        ]
    )
    C = np.diag([SIGMA_DC**2, SIGMA_LOGMAG**2, SIGMA_PHASE**2])
    F = J.T @ np.linalg.inv(C) @ J
    Cov_natural = np.linalg.inv(F)

    # Transform from (D,Vstar,gamma0) to (D,v,kappa).
    v = VSTAR - 2.0 * D * GAMMA0
    kappa = VSTAR * GAMMA0 - D * GAMMA0**2
    K = np.array(
        [
            [1.0, 0.0, 0.0],
            [-2.0 * GAMMA0, 1.0, -2.0 * D],
            [-GAMMA0**2, GAMMA0, v],
        ]
    )
    Cov_physical = K @ Cov_natural @ K.T
    sigma_phys = np.sqrt(np.diag(Cov_physical))

    # Low-frequency leading scalings.
    sigma_V_asym = VSTAR**2 * SIGMA_PHASE / (DELTA_Z * OMEGA)
    sigma_D_asym = VSTAR**3 * SIGMA_LOGMAG / (DELTA_Z * OMEGA**2)
    sigma_g0_exact = SIGMA_DC / DELTA_Z

    print("Minimal transport Fisher bound")
    print(f"analytic dGamma/dD finite-difference relative error = {err_D:.3e}")
    print(f"analytic dGamma/dV finite-difference relative error = {err_V:.3e}")
    print(f"natural CRLB std(D,Vstar,gamma0) = {np.sqrt(np.diag(Cov_natural))}")
    print(f"physical CRLB std(D,v,kappa) = {sigma_phys}")
    print(
        "low-frequency leading scales: "
        f"sigma_D~{sigma_D_asym:.6e}, "
        f"sigma_V~{sigma_V_asym:.6e}, "
        f"sigma_gamma0={sigma_g0_exact:.6e}"
    )
    print(f"nominal physical v={v:.6f}, kappa={kappa:.6f}")

    assert err_D < 2.0e-9
    assert err_V < 2.0e-9
    assert np.all(np.linalg.eigvalsh(F) > 0.0)
    assert abs(np.sqrt(Cov_natural[2, 2]) - sigma_g0_exact) < 1.0e-12

    print()
    print(
        "PASS: the exact Fisher derivatives match finite differences and the "
        "minimal DC + complex-RF experiment has full local rank in the natural "
        "parameterization. Uncertainties scale inversely with generation-depth "
        "separation, while low-frequency diffusion information enters through "
        "log-magnitude at omega^2."
    )


if __name__ == "__main__":
    main()
