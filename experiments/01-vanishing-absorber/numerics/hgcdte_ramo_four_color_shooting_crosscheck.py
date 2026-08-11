"""Independent shooting-method cross-check of the stochastic HgCdTe four-color result.

The canonical stochastic implementation solves a sparse finite-difference BVP:

    D J'' + v(z) J' - (kappa+s) J = -v(z),

with J(L)=0 and a Robin condition at z=0 matching a bounded semi-infinite
homogeneous continuation.

This file deliberately uses a different numerical construction:
1. integrate one forced initial-value solution from z=0 to L;
2. integrate one homogeneous sensitivity solution corresponding to unit change
   in J(0), with the Robin derivative changed consistently;
3. solve one scalar complex equation so the linear combination satisfies J(L)=0.

DOP853 adaptive IVP integration replaces the finite-difference BVP.  The same
Hansen/Moazzami optics and graded transport profile are reconstructed locally.

The regression verifies the no-recombination gradient-sensitive four-color
closure at 100 MHz, 500 MHz, and 1 GHz against the canonical values.  This is an
independent numerical implementation, not a new physical model.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import cumulative_trapezoid, solve_ivp
from scipy.optimize import brentq


HC_EV_UM = 1.2398419843320026
KB = 1.380649e-23
Q = 1.602176634e-19
T_K = 300.0
L_UM = 7.6
L_M = L_UM * 1.0e-6
X_FRONT = 0.55
X_BACK = 0.32
MOBILITY_M2_VS = 0.90
D_M2_S = MOBILITY_M2_VS * KB * T_K / Q
SAT_FIELD_V_M = 8.0e5
SAT_EXPONENT = 2.2

Z_FINE_UM = np.linspace(0.0, L_UM, 20001)
X_FINE = X_FRONT + (X_BACK - X_FRONT) * Z_FINE_UM / L_UM
TARGET_MEANS_UM = (2.5, 3.0, 3.5, 4.0)
FREQUENCIES_HZ = (100e6, 500e6, 1e9)


def eg_hansen(x, T=T_K):
    return (
        -0.302 + 1.93 * x + 5.35e-4 * T * (1.0 - 2.0 * x)
        - 0.81 * x**2 + 0.832 * x**3
    )


def deg_dx_hansen(x, T=T_K):
    return 1.93 - 1.62 * x + 3.0 * 0.832 * x**2 - 2.0 * 5.35e-4 * T


def k_moazzami(x, T=T_K):
    return (
        -20060.0 + 115750.0 * x + 32.43 * T - 64170.0 * x**2
        + 0.43231 * T**2 - 101.92 * x * T
    )


def n_moazzami(x, T=T_K):
    return 0.74487 - 0.44513 * x + (0.000799 - 0.000757 * x) * T


def optical_kernel(wavelength_um: float):
    E = HC_EV_UM / wavelength_um
    gap = eg_hansen(X_FINE)
    frac = (E - gap) / E
    alpha = np.zeros_like(frac)
    mask = frac > 0.0
    alpha[mask] = (
        k_moazzami(X_FINE[mask])
        * frac[mask] ** n_moazzami(X_FINE[mask])
    )
    alpha = np.maximum(alpha, 0.0)
    tau = np.concatenate(
        ([0.0], cumulative_trapezoid(alpha, Z_FINE_UM * 1.0e-4))
    )
    density = alpha * 1.0e-4 * np.exp(-tau)
    pabs = float(1.0 - np.exp(-tau[-1]))
    density /= np.trapezoid(density, Z_FINE_UM)
    mean = float(np.trapezoid(Z_FINE_UM * density, Z_FINE_UM))
    return pabs, mean, density


def wavelength_for_mean(target_um: float) -> float:
    return float(
        brentq(
            lambda wavelength: optical_kernel(wavelength)[1] - target_um,
            1.95,
            3.20,
        )
    )


def velocity(z_m: np.ndarray) -> np.ndarray:
    x = X_FRONT + (X_BACK - X_FRONT) * z_m / L_M
    dx_dz_m = (X_BACK - X_FRONT) / L_M
    force = np.abs(deg_dx_hansen(x) * dx_dz_m)
    v_field = (
        MOBILITY_M2_VS * force
        / (1.0 + (force / SAT_FIELD_V_M) ** SAT_EXPONENT)
    )
    dln_gap_dz = deg_dx_hansen(x) * dx_dz_m / eg_hansen(x)
    v_dos = D_M2_S * 1.5 * dln_gap_dz
    return v_field + v_dos


V0 = float(velocity(np.asarray((0.0,)))[0])
Z_V = np.linspace(0.0, L_M, 20001)
V_HARM = 1.0 / float(np.trapezoid(1.0 / velocity(Z_V), Z_V) / L_M)


def shooting_solution(frequency_hz: float, kappa: float = 0.0):
    lam = kappa + 1j * 2.0 * np.pi * frequency_hz
    r_plus = (
        -V0 + np.sqrt(V0 * V0 + 4.0 * D_M2_S * lam)
    ) / (2.0 * D_M2_S)
    Jp = V0 / lam

    # Dimensionless coordinate xi=z/L improves numerical conditioning.
    def forced_rhs(xi, y):
        v = float(velocity(np.asarray((xi * L_M,)))[0])
        J, Y = y  # Y=dJ/dxi
        return np.asarray(
            (
                Y,
                (L_M**2 / D_M2_S)
                * (lam * J - (v / L_M) * Y - v),
            ),
            dtype=complex,
        )

    def homogeneous_rhs(xi, y):
        v = float(velocity(np.asarray((xi * L_M,)))[0])
        J, Y = y
        return np.asarray(
            (
                Y,
                (L_M**2 / D_M2_S)
                * (lam * J - (v / L_M) * Y),
            ),
            dtype=complex,
        )

    # Forced solution with J(0)=0 and Robin-consistent derivative.
    y_forced = np.asarray((0.0, -L_M * r_plus * Jp), dtype=complex)
    # Homogeneous sensitivity for a unit change in J(0).
    y_sensitivity = np.asarray((1.0, L_M * r_plus), dtype=complex)

    forced = solve_ivp(
        forced_rhs,
        (0.0, 1.0),
        y_forced,
        method="DOP853",
        rtol=1.0e-10,
        atol=1.0e-12,
        dense_output=True,
    )
    sensitivity = solve_ivp(
        homogeneous_rhs,
        (0.0, 1.0),
        y_sensitivity,
        method="DOP853",
        rtol=1.0e-10,
        atol=1.0e-12,
        dense_output=True,
    )

    if not forced.success or not sensitivity.success:
        raise RuntimeError("shooting IVP integration failed")

    amplitude = -forced.y[0, -1] / sensitivity.y[0, -1]

    def evaluate(z_um: np.ndarray) -> np.ndarray:
        xi = np.asarray(z_um) / L_UM
        return forced.sol(xi)[0] + amplitude * sensitivity.sol(xi)[0]

    return evaluate


def homogeneous_point_current(frequency_hz: float) -> np.ndarray:
    lam = 1j * 2.0 * np.pi * frequency_hz
    gamma = (
        np.sqrt(V_HARM**2 + 4.0 * D_M2_S * lam) - V_HARM
    ) / (2.0 * D_M2_S)
    distance_m = (L_UM - Z_FINE_UM) * 1.0e-6
    return 1.0 - np.exp(-gamma * distance_m)


def channel_currents(point_current: np.ndarray, kernels: list[np.ndarray]):
    return np.asarray(
        [np.trapezoid(k * point_current, Z_FINE_UM) for k in kernels]
    )


def closure(currents: np.ndarray) -> complex:
    d = np.diff(currents)
    return complex(2.0 * np.log(d[1]) - np.log(d[0]) - np.log(d[2]))


def main() -> None:
    wavelengths = [wavelength_for_mean(m) for m in TARGET_MEANS_UM]
    optical = [optical_kernel(wavelength) for wavelength in wavelengths]
    kernels = [row[2] for row in optical]

    print("Independent shooting cross-check of stochastic HgCdTe four-color result")
    print("wavelengths um = " + ", ".join(f"{x:.9f}" for x in wavelengths))

    expected_deg = {
        int(100e6): -0.0119784,
        int(500e6): -0.0587271,
        int(1e9): -0.1104053,
    }

    for frequency in FREQUENCIES_HZ:
        evaluate = shooting_solution(frequency)
        variable_point = evaluate(Z_FINE_UM)
        variable = closure(channel_currents(variable_point, kernels))
        homogeneous = closure(
            channel_currents(homogeneous_point_current(frequency), kernels)
        )
        excess = variable - homogeneous
        phase_deg = float(np.degrees(excess.imag))
        target = expected_deg[int(frequency)]
        print(
            f"{frequency/1e6:7.1f} MHz: excess phase={phase_deg:+.9f} deg, "
            f"canonical={target:+.7f} deg, diff={phase_deg-target:+.3e} deg"
        )
        assert abs(phase_deg - target) < 2.0e-6

    print()
    print(
        "PASS: an adaptive shooting/IVP implementation independently reproduces "
        "the sparse finite-difference stochastic HgCdTe four-color closure at "
        "100 MHz, 500 MHz, and 1 GHz."
    )


if __name__ == "__main__":
    main()
