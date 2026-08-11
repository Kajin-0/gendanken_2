"""Regression for polynomial observation-forcing annihilation.

Checks the five-color second-difference closure for a homogeneous deterministic
transport channel with a linear Shockley-Ramo weighting field.
"""

from __future__ import annotations

import math
import numpy as np


L = 7.6e-6
V = 3.45e4
F = 100e6
S = 1j * 2.0 * np.pi * F
H = 0.5e-6
Z = np.asarray((2.25, 2.75, 3.25, 3.75, 4.25)) * 1e-6
ZC = 3.25e-6

# 1% fractional weighting-field variation across 1.5 um.
BETA = 0.01 / 1.5e-6


def point_current(z: float) -> complex:
    x = np.linspace(z, L, 30001)
    ew = 1.0 + BETA * (x - ZC)
    phase = np.exp(-S * (x - z) / V)
    return complex(np.trapezoid(ew * phase, x))


def log_geometric_closure(values: np.ndarray) -> complex:
    return complex(2.0 * np.log(values[1]) - np.log(values[0]) - np.log(values[2]))


def main() -> None:
    currents = np.asarray([point_current(z) for z in Z])

    d1 = np.diff(currents)
    c4 = log_geometric_closure(d1[:3])

    d2 = np.diff(currents, n=2)
    c5 = log_geometric_closure(d2)

    print("linear weighting-field observation stress")
    print(f"four-color first-difference phase = {np.degrees(c4.imag):+.9f} deg")
    print(f"five-color second-difference |closure| = {abs(c5):.3e}")
    print()

    for p in range(4):
        n = p + 1
        coefficient = math.sqrt(math.comb(2 * n + 4, n + 2))
        print(
            f"p={p}, n={n}, colors={p+4}, "
            f"noise coefficient={coefficient:.9f}"
        )

    assert 0.0017 < np.degrees(c4.imag) < 0.0020
    assert abs(c5) < 1e-9
    assert abs(math.sqrt(math.comb(6, 3)) - math.sqrt(20.0)) < 1e-14
    assert abs(math.sqrt(math.comb(8, 4)) - math.sqrt(70.0)) < 1e-14

    print()
    print(
        "PASS: second spatial differences annihilate a linear observation "
        "particular term and restore an exact one-mode geometric closure."
    )


if __name__ == "__main__":
    main()
