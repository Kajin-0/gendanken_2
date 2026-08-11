"""Conventional electron-hole Shockley-Ramo counterexample to the one-carrier closure.

A point-generated electron-hole pair in a planar detector with constant weighting
field produces the sum of two rectangular induced-current pulses.  At fixed RF
and equally spaced generation coordinates z_m, the raw complex terminal current
has the form

    J_m = C0 + Ce * qe**m + Ch * qh**m.

Therefore:
- the one-carrier four-color first-difference geometric closure generally fails;
- first differences have rank <=2;
- six colors (five first differences) satisfy a 3x3 Hankel determinant exactly.

This is an intentionally ordinary counterexample: failure of the minimal
four-color law does not imply exotic/nonlocal transport.
"""

from __future__ import annotations

import numpy as np


L = 2.4
Z0 = 0.45
DZ = 0.23
Z = Z0 + DZ * np.arange(6)
OMEGA = 3.1
VE = 1.8
VH = 0.72


def raw_pair_current(z: np.ndarray) -> np.ndarray:
    # Overall q/L/s factors are omitted because closure is homogeneous in J.
    electron = VE * (1.0 - np.exp(-1j * OMEGA * (L - z) / VE))
    hole = VH * (1.0 - np.exp(-1j * OMEGA * z / VH))
    return electron + hole


def one_carrier_closure(J: np.ndarray) -> complex:
    d = np.diff(J[:4])
    return d[1] ** 2 - d[0] * d[2]


def rank2_difference_hankel(J: np.ndarray) -> complex:
    d = np.diff(J)
    H = np.asarray(
        (
            (d[0], d[1], d[2]),
            (d[1], d[2], d[3]),
            (d[2], d[3], d[4]),
        ),
        dtype=complex,
    )
    return complex(np.linalg.det(H))


def main() -> None:
    J = raw_pair_current(Z)
    c4 = one_carrier_closure(J)
    h6 = rank2_difference_hankel(J)

    print("Conventional electron-hole Ramo spatial-rank counterexample")
    print(f"|one-carrier four-color residual| = {abs(c4):.6e}")
    print(f"|six-color rank-two difference Hankel| = {abs(h6):.6e}")

    assert abs(c4) > 1.0e-3
    assert abs(h6) < 1.0e-12

    print()
    print(
        "PASS: an entirely conventional electron-hole pair breaks the minimal "
        "single-carrier four-color closure but satisfies the expected rank-two "
        "first-difference closure.  Closure failure must therefore be followed "
        "by mode counting before any anomalous-transport interpretation."
    )


if __name__ == "__main__":
    main()
