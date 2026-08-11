"""Boundary-matched correction to the first HgCdTe three-color closure prediction.

The earlier worked example compared a finite-slab graded-transport BVP with a
homogeneous *infinite/exponential* propagation reference. That comparison
incorrectly assigned finite entrance-boundary curvature to the transport
gradient.

This correction keeps EVERYTHING matched between the graded and homogeneous
controls except v(z):

- same 7.6 um finite slab;
- same reflecting optical entrance u'(0)=0;
- same absorbing collector u(L)=1;
- same three real HgCdTe optical generation kernels;
- same D;
- homogeneous control uses the spatially averaged drift.

It also solves the backward moment hierarchy directly to show that the low-RF
three-color phase closure is the discrete curvature of mean transit time and
that almost all of the ~3.4 ps curvature in the original calculation comes from
the reflecting entrance boundary, not the modest drift gradient.

The old script/file are retained as provenance but their interpretation is
superseded by this boundary-matched calculation.
"""

from __future__ import annotations

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import spsolve

import hgcdte_three_color_transport_closure_prediction as old


FREQUENCIES_HZ = old.FREQUENCIES_HZ
V_MEAN = float(np.trapezoid(old.V, old.Z_UM) / old.L_UM)
V_HOM = np.full_like(old.V, V_MEAN)


def operator_matrix(v: np.ndarray, omega: float = 0.0) -> csr_matrix:
    rows: list[int] = []
    cols: list[int] = []
    values: list[complex] = []

    # Same second-order reflecting entrance condition used in the original BVP.
    rows += [0, 0, 0]
    cols += [0, 1, 2]
    values += [-3.0, 4.0, -1.0]

    for i in range(1, old.N):
        lower = old.D_M2_S / old.DX_M**2 - v[i] / (2.0 * old.DX_M)
        center = -2.0 * old.D_M2_S / old.DX_M**2 - 1j * omega
        upper = old.D_M2_S / old.DX_M**2 + v[i] / (2.0 * old.DX_M)

        rows += [i, i, i]
        cols += [i - 1, i, i + 1]
        values += [lower, center, upper]

    rows.append(old.N)
    cols.append(old.N)
    values.append(1.0)

    return csr_matrix(
        (np.asarray(values, dtype=complex), (rows, cols)),
        shape=(old.N + 1, old.N + 1),
    )


def solve_rf(v: np.ndarray, frequency_hz: float) -> np.ndarray:
    matrix = operator_matrix(v, 2.0 * np.pi * frequency_hz)
    rhs = np.zeros(old.N + 1, dtype=complex)
    rhs[-1] = 1.0
    return spsolve(matrix, rhs)


def solve_moments(v: np.ndarray, order: int = 4) -> list[np.ndarray]:
    """Raw point-source first-passage moments m_n(z)."""
    matrix = operator_matrix(v, 0.0).real.tocsr()
    out: list[np.ndarray] = []
    previous = np.ones(old.N + 1)

    for n in range(1, order + 1):
        rhs = np.zeros(old.N + 1)
        rhs[1 : old.N] = -n * previous[1 : old.N]
        moment = spsolve(matrix, rhs)
        out.append(moment)
        previous = moment

    return out


def optical_triplet():
    wavelengths = np.asarray(
        [old.solve_wavelength_for_mean(target) for target in old.TARGET_MEAN_DEPTHS_UM]
    )
    optical = [old.optical_kernel(wavelength) for wavelength in wavelengths]
    kernels = [row[4] for row in optical]
    return wavelengths, optical, kernels


def average_cumulants(moment_profiles: list[np.ndarray], kernel: np.ndarray):
    raw = [float(np.trapezoid(m * kernel, old.Z_UM)) for m in moment_profiles]
    k1 = raw[0]
    k2 = raw[1] - k1**2
    k3 = raw[2] - 3.0 * raw[1] * k1 + 2.0 * k1**3
    k4 = (
        raw[3]
        - 4.0 * raw[2] * k1
        - 3.0 * raw[1] ** 2
        + 12.0 * raw[1] * k1**2
        - 6.0 * k1**4
    )
    return np.asarray((k1, k2, k3, k4))


def complex_closure(v: np.ndarray, frequency_hz: float, kernels: list[np.ndarray]):
    u = solve_rf(v, frequency_hz)
    H = np.asarray([np.trapezoid(kernel * u, old.Z_UM) for kernel in kernels])
    return complex(2.0 * np.log(H[1]) - np.log(H[0]) - np.log(H[2]))


def main() -> None:
    wavelengths, optical, kernels = optical_triplet()

    moments_grad = solve_moments(old.V)
    moments_hom = solve_moments(V_HOM)

    cumulants_grad = np.asarray(
        [average_cumulants(moments_grad, kernel) for kernel in kernels]
    )
    cumulants_hom = np.asarray(
        [average_cumulants(moments_hom, kernel) for kernel in kernels]
    )

    curvature_grad = 2.0 * cumulants_grad[1] - cumulants_grad[0] - cumulants_grad[2]
    curvature_hom = 2.0 * cumulants_hom[1] - cumulants_hom[0] - cumulants_hom[2]
    curvature_excess = curvature_grad - curvature_hom

    print("HgCdTe three-color finite-boundary correction")
    print(f"homogeneous matched drift = {V_MEAN:.6f} m/s")
    print()
    print("three generation-depth timing statistics")
    for target, wavelength, kg, kh in zip(
        old.TARGET_MEAN_DEPTHS_UM, wavelengths, cumulants_grad, cumulants_hom
    ):
        print(
            f"mean generation={target:.1f} um, lambda={wavelength:.9f} um: "
            f"graded <T>={kg[0]*1e12:.6f} ps, "
            f"homogeneous-boundary <T>={kh[0]*1e12:.6f} ps"
        )

    print()
    print("discrete timing-cumulant curvature C_n=2k_n,2-k_n,1-k_n,3")
    print(f"  graded C1 = {curvature_grad[0]*1e12:.9f} ps")
    print(f"  homogeneous finite-boundary C1 = {curvature_hom[0]*1e12:.9f} ps")
    print(f"  gradient-only excess C1 = {curvature_excess[0]*1e12:.9f} ps")
    print(f"  graded C2 = {curvature_grad[1]*1e24:.9f} ps^2")
    print(f"  homogeneous finite-boundary C2 = {curvature_hom[1]*1e24:.9f} ps^2")

    print()
    print("frequency-domain boundary-matched closure")
    table = []
    for frequency in FREQUENCIES_HZ:
        graded = complex_closure(old.V, frequency, kernels)
        homogeneous = complex_closure(V_HOM, frequency, kernels)
        excess = graded - homogeneous
        table.append((frequency, graded, homogeneous, excess))
        print(
            f"{frequency/1e6:7.1f} MHz: "
            f"graded phase={np.degrees(graded.imag): .9f} deg; "
            f"hom-boundary phase={np.degrees(homogeneous.imag): .9f} deg; "
            f"gradient excess={np.degrees(excess.imag): .9f} deg; "
            f"gradient excess logmag={excess.real: .9e}"
        )

    # Direct low-RF timing interpretation: Im L = -omega C1 + O(omega^3).
    f_low, Lg_low, Lh_low, Lex_low = table[0]
    omega_low = 2.0 * np.pi * f_low
    c1_from_rf_grad = -Lg_low.imag / omega_low
    c1_from_rf_hom = -Lh_low.imag / omega_low

    print()
    print("10-MHz RF -> timing-curvature check")
    print(f"  graded C1 from RF = {c1_from_rf_grad*1e12:.9f} ps")
    print(f"  homogeneous C1 from RF = {c1_from_rf_hom*1e12:.9f} ps")

    # Regression anchors from the corrected matched-boundary computation.
    assert 3.40 < curvature_grad[0] * 1e12 < 3.45
    assert 3.44 < curvature_hom[0] * 1e12 < 3.49
    assert -0.06 < curvature_excess[0] * 1e12 < -0.02

    by_f = {int(row[0]): row for row in table}
    excess_100 = by_f[int(100e6)][3]
    excess_500 = by_f[int(500e6)][3]
    excess_1000 = by_f[int(1e9)][3]

    assert 0.0010 < np.degrees(excess_100.imag) < 0.0018
    assert 0.008 < np.degrees(excess_500.imag) < 0.012
    assert 0.035 < np.degrees(excess_1000.imag) < 0.045

    assert abs(c1_from_rf_grad / curvature_grad[0] - 1.0) < 3.0e-3
    assert abs(c1_from_rf_hom / curvature_hom[0] - 1.0) < 3.0e-3

    print()
    print(
        "PASS / CORRECTION: the original ~0.1-1 deg full three-color phase "
        "closure is real for the finite-slab model, but it is NOT primarily a "
        "signature of the modest HgCdTe drift gradient. A matched homogeneous "
        "finite-slab control reproduces nearly all of the low-RF mean-time "
        "curvature. The drift-gradient-only excess is only ~0.0014 deg at "
        "100 MHz, ~0.0097 deg at 500 MHz, and ~0.040 deg at 1 GHz. The entrance "
        "boundary must therefore be modeled/matched before interpreting "
        "three-color phase curvature as bulk transport inhomogeneity."
    )


if __name__ == "__main__":
    main()
