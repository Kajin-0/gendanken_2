"""Six-color first-difference root closure for a finite scalar DD boundary.

For uniform coefficients and raw planar Shockley-Ramo current, the backward
resolvent with any linear boundary conditions has

    J(z,s) = Jp(s) + A(s) exp(r_plus z) + B(s) exp(r_minus z),

where the two homogeneous roots obey

    D r^2 + w r - (kappa+s) = 0.

First differences remove Jp.  Six equally spaced source coordinates produce
five first differences, sufficient for a rank-two Hankel check and recovery of
both spatial multipliers.

The recovered exponents must satisfy

    r+ + r- = -w/D
    r+ r-  = -(kappa+i omega)/D.

Thus the sum is real/RF-independent; the product has real constant -kappa/D
and imaginary part exactly -omega/D.  Boundary amplitudes are irrelevant.
"""

from __future__ import annotations

import numpy as np


D_TRUE = 0.13
W_TRUE = 1.55
K_TRUE = 0.37
DZ = 0.11
Z0 = 0.43
Z = Z0 + DZ * np.arange(6)
OMEGAS = (0.6, 1.4, 3.2, 5.5)


def roots(omega: float) -> np.ndarray:
    disc = np.sqrt(W_TRUE**2 + 4.0 * D_TRUE * (K_TRUE + 1j * omega))
    return np.asarray(
        ((-W_TRUE + disc) / (2.0 * D_TRUE),
         (-W_TRUE - disc) / (2.0 * D_TRUE)),
        dtype=complex,
    )


def current(z: np.ndarray, omega: float) -> np.ndarray:
    rp, rm = roots(omega)
    # Deliberately arbitrary frequency-dependent boundary/mode amplitudes and
    # particular offset.  Root closure must not depend on them.
    A = (0.8 + 0.2j) * np.exp(0.07j * omega)
    B = (-0.23 + 0.31j) * (1.0 + 0.04 * omega)
    Jp = 0.6 / (K_TRUE + 1j * omega) + 0.13j
    return Jp + A * np.exp(rp * z) + B * np.exp(rm * z)


def rank2_hankel(d: np.ndarray) -> complex:
    H = np.asarray(
        ((d[0], d[1], d[2]),
         (d[1], d[2], d[3]),
         (d[2], d[3], d[4])),
        dtype=complex,
    )
    return complex(np.linalg.det(H))


def recover_multipliers(d: np.ndarray) -> np.ndarray:
    M = np.asarray(((d[1], -d[0]), (d[2], -d[1])), dtype=complex)
    rhs = np.asarray((d[2], d[3]), dtype=complex)
    S, P = np.linalg.solve(M, rhs)
    return np.roots((1.0, -S, P))


def recover_exponents(q: np.ndarray, expected: np.ndarray) -> np.ndarray:
    raw = np.log(q) / DZ
    out = []
    used = set()
    for target in expected:
        best = None
        best_error = None
        for j, value in enumerate(raw):
            if j in used:
                continue
            k = round((target.imag - value.imag) * DZ / (2.0 * np.pi))
            candidate = value + 2j * np.pi * k / DZ
            error = abs(candidate - target)
            if best is None or error < best_error:
                best = (j, candidate)
                best_error = error
        used.add(best[0])
        out.append(best[1])
    return np.asarray(out)


def main() -> None:
    print("Six-color finite-boundary Ramo root closure with recombination")
    max_hankel = 0.0
    max_D_rel = 0.0
    max_w_rel = 0.0
    max_k_rel = 0.0

    for omega in OMEGAS:
        J = current(Z, omega)
        d = np.diff(J)
        hdet = rank2_hankel(d)
        max_hankel = max(max_hankel, abs(hdet))

        r = recover_exponents(recover_multipliers(d), roots(omega))
        root_sum = np.sum(r)
        root_product = np.prod(r)

        D_rec = -omega / root_product.imag
        w_rec = -D_rec * root_sum.real
        k_rec = -D_rec * root_product.real

        max_D_rel = max(max_D_rel, abs(D_rec / D_TRUE - 1.0))
        max_w_rel = max(max_w_rel, abs(w_rec / W_TRUE - 1.0))
        max_k_rel = max(max_k_rel, abs(k_rec / K_TRUE - 1.0))

        print(
            f"omega={omega:.2f}: |Hankel|={abs(hdet):.3e}, "
            f"sum={root_sum.real:+.9f}{root_sum.imag:+.2e}j, "
            f"product={root_product.real:+.9f}{root_product.imag:+.9f}j, "
            f"D={D_rec:.9f}, w={w_rec:.9f}, k={k_rec:.9f}"
        )

        assert abs(root_sum.imag) < 2.0e-10
        assert root_product.imag < 0.0

    assert max_hankel < 5.0e-12
    assert max_D_rel < 2.0e-9
    assert max_w_rel < 2.0e-9
    assert max_k_rel < 2.0e-9

    print()
    print(
        "PASS: arbitrary finite-boundary amplitudes leave a rank-two first-"
        "difference sequence whose recovered roots obey one real scalar DD + "
        "recombination quadratic.  Six colors recover D,w,kappa without fitting "
        "the boundary amplitudes, and RF frequency overdetermines the model."
    )


if __name__ == "__main__":
    main()
