"""Stochastic diffusion/recombination stress of the corrected HgCdTe four-color signal.

This extends hgcdte_ramo_four_color_gradient_prediction.py from deterministic
high-Peclet propagation to the backward-resolvent of an additive Shockley-Ramo
current functional:

    D J'' + v(z) J' - (kappa+s) J = -v(z).

Uniform planar weighting and one signal carrier are assumed; the irrelevant qEw
factor is suppressed.  The collector condition is J(L)=0.

To prevent the earlier finite-entrance-boundary confound, the z=0 condition is
NOT reflecting.  The graded domain is matched to a hypothetical semi-infinite
homogeneous continuation z<0 with constant v(0).  Boundedness upstream gives

    J'(0) = r_plus [J(0)-Jp],
    Jp = v0/(kappa+s),
    r_plus = (-v0 + sqrt(v0^2+4D(kappa+s)))/(2D).

Thus the calculation asks a clean bulk-theory question rather than modeling an
actual surface.

The same four real Hansen/Moazzami generation kernels (mean depths 2.5,3.0,3.5,
4.0 um) are used.  A homogeneous reference with identical D,kappa,optics and
constant path-harmonic drift provides the optical-shape floor.

No calibrated-device claim.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.optimize import brentq
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import spsolve


HC_EV_UM = 1.2398419843320026
KB = 1.380649e-23
Q = 1.602176634e-19
T_K = 300.0
L_UM = 7.6
X_FRONT = 0.55
X_BACK = 0.32
MOBILITY_M2_VS = 0.90
D_M2_S = MOBILITY_M2_VS * KB * T_K / Q
SAT_FIELD_V_M = 8.0e5
SAT_EXPONENT = 2.2

N_FINE = 10001
Z_FINE_UM = np.linspace(0.0, L_UM, N_FINE)
X_FINE = X_FRONT + (X_BACK - X_FRONT) * Z_FINE_UM / L_UM

N_BVP = 5000
Z_UM = np.linspace(0.0, L_UM, N_BVP + 1)
Z_M = Z_UM * 1e-6
DX_M = Z_M[1] - Z_M[0]
X = X_FRONT + (X_BACK - X_FRONT) * Z_UM / L_UM

TARGET_MEANS_UM = (2.5, 3.0, 3.5, 4.0)
FREQUENCIES_HZ = (100e6, 500e6, 1e9)
LIFETIMES_NS = (np.inf, 10.0, 1.0)


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


def optical_kernel_fine(wavelength_um: float):
    gap = eg_hansen(X_FINE)
    E = HC_EV_UM / wavelength_um
    fraction = (E - gap) / E
    alpha = np.zeros_like(X_FINE)
    mask = fraction > 0
    alpha[mask] = (
        k_moazzami(X_FINE[mask])
        * fraction[mask] ** n_moazzami(X_FINE[mask])
    )
    alpha = np.maximum(alpha, 0.0)
    tau = np.concatenate(
        ([0.0], cumulative_trapezoid(alpha, Z_FINE_UM * 1e-4))
    )
    density = alpha * 1e-4 * np.exp(-tau)
    pabs = float(1.0 - np.exp(-tau[-1]))
    density /= np.trapezoid(density, Z_FINE_UM)
    mean = float(np.trapezoid(Z_FINE_UM * density, Z_FINE_UM))
    return pabs, mean, density


def wavelength_for_mean(target_um: float) -> float:
    return float(
        brentq(
            lambda wavelength: optical_kernel_fine(wavelength)[1] - target_um,
            1.95,
            3.20,
        )
    )


def velocity_profile() -> np.ndarray:
    dx_dz_m = (X_BACK - X_FRONT) / (L_UM * 1e-6)
    force = np.abs(deg_dx_hansen(X) * dx_dz_m)
    v_field = (
        MOBILITY_M2_VS * force
        / (1.0 + (force / SAT_FIELD_V_M) ** SAT_EXPONENT)
    )
    gap = eg_hansen(X)
    dln_gap_dz = deg_dx_hansen(X) * dx_dz_m / gap
    v_dos = D_M2_S * 1.5 * dln_gap_dz
    return v_field + v_dos


V = velocity_profile()
V_HARM = 1.0 / float(np.trapezoid(1.0 / V, Z_UM) / L_UM)


def kernels_on_bvp_grid():
    wavelengths = [wavelength_for_mean(m) for m in TARGET_MEANS_UM]
    out = []
    pabs = []
    for wavelength in wavelengths:
        p, _, density = optical_kernel_fine(wavelength)
        k = np.interp(Z_UM, Z_FINE_UM, density)
        k /= np.trapezoid(k, Z_UM)
        out.append(k)
        pabs.append(p)
    return np.asarray(wavelengths), np.asarray(pabs), out


def solve_variable(frequency_hz: float, kappa: float) -> np.ndarray:
    s = 1j * 2.0 * np.pi * frequency_hz
    lam = kappa + s
    v0 = V[0]
    r_plus = (-v0 + np.sqrt(v0 * v0 + 4.0 * D_M2_S * lam)) / (2.0 * D_M2_S)
    Jp = v0 / lam

    rows: list[int] = []
    cols: list[int] = []
    vals: list[complex] = []
    rhs = np.zeros(N_BVP + 1, dtype=complex)

    # Second-order Robin match to the bounded semi-infinite homogeneous continuation.
    rows += [0, 0, 0]
    cols += [0, 1, 2]
    vals += [
        -3.0 / (2.0 * DX_M) - r_plus,
        4.0 / (2.0 * DX_M),
        -1.0 / (2.0 * DX_M),
    ]
    rhs[0] = -r_plus * Jp

    for i in range(1, N_BVP):
        lower = D_M2_S / DX_M**2 - V[i] / (2.0 * DX_M)
        center = -2.0 * D_M2_S / DX_M**2 - lam
        upper = D_M2_S / DX_M**2 + V[i] / (2.0 * DX_M)
        rows += [i, i, i]
        cols += [i - 1, i, i + 1]
        vals += [lower, center, upper]
        rhs[i] = -V[i]

    rows.append(N_BVP)
    cols.append(N_BVP)
    vals.append(1.0)
    rhs[-1] = 0.0

    matrix = csr_matrix(
        (np.asarray(vals, dtype=complex), (rows, cols)),
        shape=(N_BVP + 1, N_BVP + 1),
    )
    return spsolve(matrix, rhs)


def homogeneous_point_current(frequency_hz: float, kappa: float) -> np.ndarray:
    s = 1j * 2.0 * np.pi * frequency_hz
    lam = kappa + s
    gamma = (
        np.sqrt(V_HARM**2 + 4.0 * D_M2_S * lam) - V_HARM
    ) / (2.0 * D_M2_S)
    distance_m = (L_UM - Z_UM) * 1e-6
    # Common prefactor V_HARM/lam cancels from closure.
    return 1.0 - np.exp(-gamma * distance_m)


def channel_currents(point_current: np.ndarray, kernels: list[np.ndarray]):
    return np.asarray(
        [np.trapezoid(k * point_current, Z_UM) for k in kernels]
    )


def closure(currents: np.ndarray) -> complex:
    d = np.diff(currents)
    return complex(2.0 * np.log(d[1]) - np.log(d[0]) - np.log(d[2]))


def kappa_from_lifetime_ns(tau_ns: float) -> float:
    return 0.0 if np.isinf(tau_ns) else 1.0 / (tau_ns * 1e-9)


def main() -> None:
    wavelengths, pabs, kernels = kernels_on_bvp_grid()
    print("HgCdTe four-color stochastic diffusion/recombination stress")
    print(f"D={D_M2_S:.9f} m^2/s, v_harm={V_HARM:.3f} m/s")
    print("wavelengths um = " + ", ".join(f"{x:.9f}" for x in wavelengths))
    print("Pabs = " + ", ".join(f"{x:.9f}" for x in pabs))
    print()

    stored = {}
    for tau_ns in LIFETIMES_NS:
        kappa = kappa_from_lifetime_ns(tau_ns)
        label = "infinite" if np.isinf(tau_ns) else f"{tau_ns:g} ns"
        print(f"lifetime = {label}")
        for frequency in FREQUENCIES_HZ:
            variable = closure(channel_currents(solve_variable(frequency, kappa), kernels))
            homogeneous = closure(
                channel_currents(
                    homogeneous_point_current(frequency, kappa), kernels
                )
            )
            excess = variable - homogeneous
            stored[(tau_ns, int(frequency))] = (variable, homogeneous, excess)
            print(
                f"  {frequency/1e6:7.1f} MHz: "
                f"var={np.degrees(variable.imag):+.9f} deg, "
                f"opt={np.degrees(homogeneous.imag):+.9f} deg, "
                f"excess={np.degrees(excess.imag):+.9f} deg"
            )
        print()

    # Anchors.
    assert min(pabs) > 0.9993
    no_rec_100 = stored[(np.inf, int(100e6))][2]
    tau10_100 = stored[(10.0, int(100e6))][2]
    tau1_100 = stored[(1.0, int(100e6))][2]
    assert -0.0122 < np.degrees(no_rec_100.imag) < -0.0117
    assert -0.0123 < np.degrees(tau10_100.imag) < -0.0118
    assert -0.0130 < np.degrees(tau1_100.imag) < -0.0124

    no_rec_500 = stored[(np.inf, int(500e6))][2]
    assert -0.0600 < np.degrees(no_rec_500.imag) < -0.0575

    print(
        "PASS: finite Einstein diffusion and uniform Markov recombination do not "
        "erase the corrected four-color gradient signal in this explicit bulk "
        "stress.  The no-recombination 100-MHz excess stays near -0.012 deg, "
        "and even a 1-ns uniform lifetime changes the scale only modestly."
    )


if __name__ == "__main__":
    main()
