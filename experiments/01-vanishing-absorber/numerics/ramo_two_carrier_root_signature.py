"""RF spatial-root signature of a conventional electron-hole Ramo signal.

For deterministic planar electron-hole transport at fixed RF,

    J(z) = C0 + Ce exp(+i omega z/ve) + Ch exp(-i omega z/vh).

First differences are rank two. Six equally spaced generation coordinates allow
recovery of the two multipliers and hence the two spatial exponents.  Their
sum/product obey

    re + rh = i omega (1/ve - 1/vh)
    re * rh = omega^2/(ve vh)

(up to consistent log branches).

This is qualitatively distinct from a finite-boundary scalar drift-diffusion
root pair, whose sum is real/RF-independent and whose product is purely
imaginary/linear in omega.
"""

from __future__ import annotations

import numpy as np


VE = 1.8
VH = 0.72
DZ = 0.08
Z0 = 0.40
Z = Z0 + DZ * np.arange(6)
OMEGAS = (0.7, 1.6, 3.4)
L = 2.4


def current(z: np.ndarray, omega: float) -> np.ndarray:
    electron = VE * (1.0 - np.exp(-1j * omega * (L - z) / VE))
    hole = VH * (1.0 - np.exp(-1j * omega * z / VH))
    return electron + hole


def recurrence_roots_from_differences(J: np.ndarray) -> np.ndarray:
    d = np.diff(J)
    # d2 = S d1 - P d0; d3 = S d2 - P d1.
    M = np.asarray(((d[1], -d[0]), (d[2], -d[1])), dtype=complex)
    rhs = np.asarray((d[2], d[3]), dtype=complex)
    S, P = np.linalg.solve(M, rhs)
    return np.roots((1.0, -S, P))


def unwrap_root_exponents(q: np.ndarray, omega: float) -> np.ndarray:
    raw = np.log(q) / DZ
    expected = np.asarray((1j * omega / VE, -1j * omega / VH))
    out = []
    used = set()
    for target in expected:
        best = None
        best_key = None
        for j, value in enumerate(raw):
            if j in used:
                continue
            # Adjust 2pi i branches to nearest target.
            k = round((target.imag - value.imag) * DZ / (2.0 * np.pi))
            candidate = value + 2j * np.pi * k / DZ
            key = abs(candidate - target)
            if best is None or key < best_key:
                best = (j, candidate)
                best_key = key
        used.add(best[0])
        out.append(best[1])
    return np.asarray(out)


def main() -> None:
    print("Conventional electron-hole spatial-root signature")
    max_root_error = 0.0
    for omega in OMEGAS:
        J = current(Z, omega)
        q = recurrence_roots_from_differences(J)
        r = unwrap_root_exponents(q, omega)
        target = np.asarray((1j * omega / VE, -1j * omega / VH))
        max_root_error = max(max_root_error, float(np.max(np.abs(r - target))))

        root_sum = np.sum(r)
        root_product = np.prod(r)
        sum_target = 1j * omega * (1.0 / VE - 1.0 / VH)
        product_target = omega**2 / (VE * VH)

        print(
            f"omega={omega:.2f}: sum={root_sum.real:+.3e}{root_sum.imag:+.6f}j, "
            f"product={root_product.real:+.6f}{root_product.imag:+.3e}j"
        )

        assert abs(root_sum - sum_target) < 2.0e-11
        assert abs(root_product - product_target) < 2.0e-11

        # Explicitly fails the scalar finite-boundary signature.
        assert abs(root_sum.real) < 1.0e-10
        assert abs(root_sum.imag) > 1.0e-3
        assert root_product.real > 1.0e-3
        assert abs(root_product.imag) < 1.0e-10

    assert max_root_error < 2.0e-11

    print()
    print(
        "PASS: a conventional electron-hole rank-two terminal-current signal "
        "has an imaginary RF-linear root sum and a real RF-quadratic product, "
        "clearly distinct from the real-constant / imaginary-linear scalar "
        "finite-boundary drift-diffusion signature."
    )


if __name__ == "__main__":
    main()
