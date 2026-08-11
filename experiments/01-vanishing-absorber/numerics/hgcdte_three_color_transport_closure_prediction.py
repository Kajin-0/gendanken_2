"""HgCdTe worked prediction for the three-color closure theorem.

Theory question
---------------
How large is the three-color complex closure residual from a modest physically
motivated HgCdTe transport gradient, compared with the false residual caused by
real wavelength-dependent optical-kernel shape evolution alone?

This is a theory worked example, NOT a calibrated device prediction.

Profile / optics
----------------
- T = 300 K
- L = 7.6 um
- monotonic linear composition x=0.55 at optical entrance -> x=0.32 at collector
- Hansen gap
- Moazzami above-gap absorption
- Beer-Lambert generation, conditional on absorption

Three wavelengths are solved so mean generation depths are exactly

    2, 4, 6 um.

Transport stress
----------------
- electron mobility mu = 9000 cm^2/Vs (explicit sensitivity coordinate)
- Einstein D=mu*kT/q
- force-equivalent field from full quasi-neutral gap gradient
- empirical high-field velocity reduction d=8 kV/cm, r=2.2
- DOS correction D*(3/2)*d_z ln(Eg)
- no bulk killing/recombination in this first closure example
- reflecting optical entrance, absorbing collector

The finite-RF first-passage BVP is solved by centered finite differences with a
second-order Neumann entrance condition.

Comparison model
----------------
The same three real HgCdTe optical kernels are propagated through one homogeneous
transport law using the spatially averaged drift. Its closure residual is the
optical-shape-evolution false-positive floor for this explicit reference.

No novelty claim.
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

MOBILITY_M2_VS = 0.90  # 9000 cm^2/Vs; conditional scale
SAT_FIELD_V_M = 8.0e5  # 8 kV/cm
SAT_EXPONENT = 2.2
D_M2_S = MOBILITY_M2_VS * KB * T_K / Q

N = 3200
Z_UM = np.linspace(0.0, L_UM, N + 1)
Z_M = Z_UM * 1.0e-6
DX_M = Z_M[1] - Z_M[0]
X = X_FRONT + (X_BACK - X_FRONT) * Z_UM / L_UM

TARGET_MEAN_DEPTHS_UM = np.asarray((2.0, 4.0, 6.0))
FREQUENCIES_HZ = (10e6, 50e6, 100e6, 250e6, 500e6, 1e9)


def eg_hansen(x, T=T_K):
    return (
        -0.302
        + 1.93 * x
        + 5.35e-4 * T * (1.0 - 2.0 * x)
        - 0.81 * x**2
        + 0.832 * x**3
    )


def deg_dx_hansen(x, T=T_K):
    return 1.93 - 2.0 * 0.81 * x + 3.0 * 0.832 * x**2 - 2.0 * 5.35e-4 * T


def k_moazzami(x, T=T_K):
    return (
        -20060.0
        + 115750.0 * x
        + 32.43 * T
        - 64170.0 * x**2
        + 0.43231 * T**2
        - 101.92 * x * T
    )


def n_moazzami(x, T=T_K):
    return 0.74487 - 0.44513 * x + (0.000799 - 0.000757 * x) * T


def alpha_moazzami(E: float, x: np.ndarray, T=T_K):
    gap = eg_hansen(x, T)
    fraction = (E - gap) / E
    out = np.zeros_like(x, dtype=float)
    mask = fraction > 0.0
    out[mask] = k_moazzami(x[mask], T) * fraction[mask] ** n_moazzami(
        x[mask], T
    )
    return np.maximum(out, 0.0)


def optical_kernel(wavelength_um: float):
    alpha = alpha_moazzami(HC_EV_UM / wavelength_um, X)
    tau = np.concatenate(
        ([0.0], cumulative_trapezoid(alpha, Z_UM * 1.0e-4))
    )
    density = alpha * 1.0e-4 * np.exp(-tau)  # probability density per um
    pabs = float(1.0 - np.exp(-tau[-1]))
    density /= pabs
    density /= np.trapezoid(density, Z_UM)

    mean = float(np.trapezoid(Z_UM * density, Z_UM))
    variance = float(np.trapezoid((Z_UM - mean) ** 2 * density, Z_UM))
    kappa3 = float(np.trapezoid((Z_UM - mean) ** 3 * density, Z_UM))
    return pabs, mean, variance, kappa3, density


def solve_wavelength_for_mean(target_um: float) -> float:
    return float(
        brentq(
            lambda wavelength: optical_kernel(wavelength)[1] - target_um,
            1.95,
            3.20,
        )
    )


def transport_velocity() -> np.ndarray:
    dx_dz_m = (X_BACK - X_FRONT) / (L_UM * 1.0e-6)
    force_field_v_m = np.abs(deg_dx_hansen(X) * dx_dz_m)

    v_field = (
        MOBILITY_M2_VS
        * force_field_v_m
        / (1.0 + (np.abs(force_field_v_m) / SAT_FIELD_V_M) ** SAT_EXPONENT)
    )

    # Nc proportional to (m*)^(3/2), m* proportional to Eg in the repository
    # reduced model, so d ln Nc/dz = 3/2 d ln Eg/dz.
    gap = eg_hansen(X)
    dln_gap_dz = deg_dx_hansen(X) * dx_dz_m / gap
    v_dos = D_M2_S * 1.5 * dln_gap_dz
    return v_field + v_dos


V = transport_velocity()


def solve_first_passage(frequency_hz: float) -> np.ndarray:
    omega = 2.0 * np.pi * frequency_hz

    rows: list[int] = []
    cols: list[int] = []
    values: list[complex] = []

    # Reflecting entrance u'(0)=0 using second-order forward difference.
    rows += [0, 0, 0]
    cols += [0, 1, 2]
    values += [-3.0, 4.0, -1.0]

    for i in range(1, N):
        lower = D_M2_S / DX_M**2 - V[i] / (2.0 * DX_M)
        center = -2.0 * D_M2_S / DX_M**2 - 1j * omega
        upper = D_M2_S / DX_M**2 + V[i] / (2.0 * DX_M)

        rows += [i, i, i]
        cols += [i - 1, i, i + 1]
        values += [lower, center, upper]

    # Absorbing/collecting boundary u(L)=1.
    rows.append(N)
    cols.append(N)
    values.append(1.0)

    matrix = csr_matrix(
        (np.asarray(values, dtype=complex), (rows, cols)),
        shape=(N + 1, N + 1),
    )
    rhs = np.zeros(N + 1, dtype=complex)
    rhs[-1] = 1.0
    return spsolve(matrix, rhs)


def closure(log_responses: np.ndarray) -> complex:
    return complex(2.0 * log_responses[1] - log_responses[0] - log_responses[2])


def homogeneous_optical_closure(
    frequency_hz: float,
    kernels: list[np.ndarray],
    mean_velocity: float,
) -> complex:
    omega = 2.0 * np.pi * frequency_hz
    Gamma = (
        np.sqrt(mean_velocity**2 + 4j * D_M2_S * omega) - mean_velocity
    ) / (2.0 * D_M2_S)

    responses = np.asarray(
        [
            np.trapezoid(kernel * np.exp(Gamma * Z_M), Z_UM)
            for kernel in kernels
        ]
    )
    return closure(np.log(responses))


def main() -> None:
    wavelengths = np.asarray(
        [solve_wavelength_for_mean(target) for target in TARGET_MEAN_DEPTHS_UM]
    )
    optical = [optical_kernel(wavelength) for wavelength in wavelengths]
    kernels = [row[4] for row in optical]

    print("HgCdTe three-color transport closure prediction")
    print(
        f"profile: L={L_UM:.1f} um, x={X_FRONT:.2f}->{X_BACK:.2f}, T={T_K:.0f} K"
    )
    print(f"D(Einstein)={D_M2_S:.9f} m^2/s")
    print(
        "transport v min/mean/max = "
        f"{V.min():.3f}/{np.trapezoid(V,Z_UM)/L_UM:.3f}/{V.max():.3f} m/s"
    )
    print()

    for target, wavelength, row in zip(TARGET_MEAN_DEPTHS_UM, wavelengths, optical):
        pabs, mean, variance, kappa3, _ = row
        print(
            f"mean depth target={target:.1f} um -> lambda={wavelength:.9f} um, "
            f"Pabs={pabs:.9f}, sigma_z={np.sqrt(variance):.6f} um, "
            f"kappa3={kappa3:.6f} um^3"
        )

    mean_velocity = float(np.trapezoid(V, Z_UM) / L_UM)

    print()
    print("frequency, full graded closure, homogeneous optical false floor")
    table = []
    for frequency in FREQUENCIES_HZ:
        u = solve_first_passage(frequency)
        responses = np.asarray(
            [np.trapezoid(kernel * u, Z_UM) for kernel in kernels]
        )
        full = closure(np.log(responses))
        optical_floor = homogeneous_optical_closure(
            frequency, kernels, mean_velocity
        )
        table.append((frequency, full, optical_floor))

        print(
            f"{frequency/1e6:7.1f} MHz: "
            f"full phase={np.degrees(full.imag): .9f} deg, "
            f"full logmag={full.real: .9e}; "
            f"opt phase={np.degrees(optical_floor.imag): .9f} deg, "
            f"opt logmag={optical_floor.real: .9e}"
        )

    # Stable anchors for this explicit conditional model.
    assert 2.0592 < wavelengths[0] < 2.0595
    assert 2.3937 < wavelengths[1] < 2.3941
    assert 2.8743 < wavelengths[2] < 2.8749
    assert min(row[0] for row in optical) > 0.949

    assert 3.21e4 < V.min() < 3.23e4
    assert 3.75e4 < V.max() < 3.77e4

    by_f = {int(row[0]): row for row in table}
    full_100 = by_f[int(100e6)][1]
    opt_100 = by_f[int(100e6)][2]
    full_500 = by_f[int(500e6)][1]
    opt_500 = by_f[int(500e6)][2]
    full_1000 = by_f[int(1e9)][1]
    opt_1000 = by_f[int(1e9)][2]

    assert -0.124 < np.degrees(full_100.imag) < -0.122
    assert abs(np.degrees(opt_100.imag)) < 4.0e-5
    assert -0.59 < np.degrees(full_500.imag) < -0.57
    assert 0.003 < np.degrees(opt_500.imag) < 0.005
    assert -1.00 < np.degrees(full_1000.imag) < -0.97
    assert 0.025 < np.degrees(opt_1000.imag) < 0.030

    print()
    print(
        "PASS: in this explicit graded-HgCdTe theory stress, a modest spatial "
        "transport variation produces an O(omega) phase three-color closure "
        "violation that exceeds the homogeneous real-optics shape-evolution "
        "floor by orders of magnitude at low/moderate RF. This is a falsifiable "
        "worked prediction, not a calibrated device forecast."
    )


if __name__ == "__main__":
    main()
