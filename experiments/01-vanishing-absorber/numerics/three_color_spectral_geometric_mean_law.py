"""Exact three-color spectral geometric-mean law for a uniform transport segment.

Assume the wavelength-dependent generation profile is one fixed normalized shape
translated in depth:

    p_lambda(z)=g(z-z_g).

For a spatially homogeneous first-passage process in the local segment, let the
un-normalized point-source RF and DC collection fields be exponential:

    U_s(z)=C_s exp(gamma_s z),
    U_0(z)=C_0 exp(gamma_0 z).

The distributed-generation DC-normalized response is

    H(z_g)= [int g(z-z_g) U_s(z) dz]
            /[int g(z-z_g) U_0(z) dz]
          = B(s) exp[(gamma_s-gamma_0) z_g],

for ANY fixed generation shape g with the needed transforms finite.

Therefore three wavelengths whose generation centers are equally spaced obey

    H_2^2 = H_1 H_3

exactly, including finite generation width and local Markov killing that is
removed by DC normalization.
"""

from __future__ import annotations

import numpy as np


# Deliberately asymmetric, bimodal finite-width generation shape. The theorem
# does not rely on Gaussianity, symmetry, or narrow width.
U = np.linspace(-0.50, 0.70, 5001)
G = (
    np.exp(-((U + 0.18) / 0.16) ** 2)
    + 0.35 * np.exp(-((U - 0.32) / 0.09) ** 2)
)
G = G / np.trapezoid(G, U)

GAMMA_RF = 0.31 + 0.82j
GAMMA_DC = 0.11 + 0.00j
CENTERS = np.asarray((1.20, 2.00, 2.80))


def distributed_response(center: float) -> complex:
    z = U + center
    numerator = np.trapezoid(G * np.exp(GAMMA_RF * z), U)
    denominator = np.trapezoid(G * np.exp(GAMMA_DC * z), U)
    return complex(numerator / denominator)


def main() -> None:
    H = np.asarray([distributed_response(zg) for zg in CENTERS])
    Gamma = GAMMA_RF - GAMMA_DC

    B = (
        np.trapezoid(G * np.exp(GAMMA_RF * U), U)
        / np.trapezoid(G * np.exp(GAMMA_DC * U), U)
    )
    factorization = B * np.exp(Gamma * CENTERS)

    geometric_mean_error = abs(H[1] ** 2 - H[0] * H[2])
    factorization_error = float(np.max(np.abs(H - factorization)))

    slope12 = np.log(H[1] / H[0]) / (CENTERS[1] - CENTERS[0])
    slope23 = np.log(H[2] / H[1]) / (CENTERS[2] - CENTERS[1])

    print("Three-color spectral geometric-mean law")
    print("arbitrary fixed finite-width generation kernel")
    for i, value in enumerate(H, start=1):
        print(
            f"  H{i} = {value.real:.12f} + i {value.imag:.12f}"
        )
    print(f"factorization max error = {factorization_error:.3e}")
    print(f"|H2^2-H1*H3| = {geometric_mean_error:.3e}")
    print(f"pair slope 1-2 = {slope12.real:.12f} + i {slope12.imag:.12f}")
    print(f"pair slope 2-3 = {slope23.real:.12f} + i {slope23.imag:.12f}")
    print(f"target Gamma    = {Gamma.real:.12f} + i {Gamma.imag:.12f}")

    assert factorization_error < 2.0e-15
    assert geometric_mean_error < 2.0e-15
    assert abs(slope12 - Gamma) < 2.0e-14
    assert abs(slope23 - Gamma) < 2.0e-14

    # Deliberately change the kernel shape only at the middle wavelength.
    G_mid = G * (1.0 + 0.25 * U)
    G_mid = G_mid / np.trapezoid(G_mid, U)
    zmid = U + CENTERS[1]
    H_mid_changed = (
        np.trapezoid(G_mid * np.exp(GAMMA_RF * zmid), U)
        / np.trapezoid(G_mid * np.exp(GAMMA_DC * zmid), U)
    )
    violation = abs(H_mid_changed**2 - H[0] * H[2])
    print()
    print(f"shape-evolved middle-kernel violation = {violation:.6e}")
    assert violation > 1.0e-3

    print()
    print(
        "PASS: a rigidly translated generation kernel of arbitrary width/shape "
        "obeys the exact complex geometric-mean law in a homogeneous transport "
        "segment. Generation-shape evolution breaks the parameter-free closure."
    )


if __name__ == "__main__":
    main()
