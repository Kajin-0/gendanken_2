"""Spectral Hankel rank theorem for homogeneous finite-dimensional transport.

At one fixed complex frequency s, suppose propagation over one equal spatial step
Delta z is represented by an n-dimensional linear state transition M_s. A
scalar collected response sampled at equally spaced source coordinates is

    y_m = c^T M_s^m b.

This includes non-diagonalizable M. By Cayley-Hamilton, y_m obeys a linear
recurrence of order <=n, and every Hankel matrix

    H_pq = y_{p+q}

has rank <=n. Thus all (n+1)x(n+1) Hankel determinants vanish.

n=1 gives y_1^2=y_0 y_2, the three-color geometric-mean law.
n=2 generically violates the three-color law but obeys a five-color 3x3 Hankel
closure.

The script checks n=1,2 and a non-diagonalizable n=3 realization.
"""

from __future__ import annotations

import numpy as np


def sequence(M: np.ndarray, b: np.ndarray, c: np.ndarray, count: int) -> np.ndarray:
    state = b.astype(complex)
    out = []
    for _ in range(count):
        out.append(complex(c @ state))
        state = M @ state
    return np.asarray(out)


def hankel(y: np.ndarray, size: int, offset: int = 0) -> np.ndarray:
    return np.asarray(
        [[y[offset + i + j] for j in range(size)] for i in range(size)],
        dtype=complex,
    )


def recurrence_residuals(y: np.ndarray, M: np.ndarray) -> np.ndarray:
    # numpy.poly returns [1,a_{n-1},...,a0] for det(lambda I-M).
    coeff = np.poly(M)
    n = M.shape[0]
    residuals = []
    for m in range(len(y) - n):
        # y_{m+n} + a_{n-1} y_{m+n-1}+...+a0 y_m
        window = y[m : m + n + 1]
        residuals.append(np.dot(coeff[::-1], window))
    return np.asarray(residuals)


def main() -> None:
    # One scalar propagation mode.
    r = 0.82 * np.exp(0.37j)
    M1 = np.asarray([[r]], dtype=complex)
    y1 = sequence(M1, np.asarray([1.2]), np.asarray([0.9]), 7)
    det2_1 = np.linalg.det(hankel(y1, 2))

    # Two observable propagation modes.
    r1 = 0.91 * np.exp(0.22j)
    r2 = 0.67 * np.exp(0.74j)
    M2 = np.diag((r1, r2)).astype(complex)
    b2 = np.asarray((1.0, 0.55), dtype=complex)
    c2 = np.asarray((0.75, 0.45), dtype=complex)
    y2 = sequence(M2, b2, c2, 9)
    det2_2 = np.linalg.det(hankel(y2, 2))
    det3_2 = np.linalg.det(hankel(y2, 3))

    # Three-dimensional realization with a 2x2 Jordan block, showing that the
    # rank theorem does not require diagonalizability / a pure sum of distinct
    # exponentials.
    rj = 0.78 * np.exp(0.31j)
    r3 = 0.59 * np.exp(0.93j)
    M3 = np.asarray(
        (
            (rj, 0.12 + 0.03j, 0.0),
            (0.0, rj, 0.0),
            (0.0, 0.0, r3),
        ),
        dtype=complex,
    )
    b3 = np.asarray((1.0, 0.6, 0.4), dtype=complex)
    c3 = np.asarray((0.8, 0.5, 0.7), dtype=complex)
    y3 = sequence(M3, b3, c3, 12)
    det3_3 = np.linalg.det(hankel(y3, 3))
    det4_3 = np.linalg.det(hankel(y3, 4))

    rec1 = recurrence_residuals(y1, M1)
    rec2 = recurrence_residuals(y2, M2)
    rec3 = recurrence_residuals(y3, M3)

    print("Spectral Hankel hidden-transport rank theorem")
    print(f"n=1: |2x2 Hankel det| = {abs(det2_1):.3e}")
    print()
    print("n=2 observable hidden-state example")
    print(f"  |2x2 Hankel det| = {abs(det2_2):.6e}  (three-color law fails)")
    print(f"  |3x3 Hankel det| = {abs(det3_2):.3e}  (five-color rank-2 closure)")
    print(f"  max recurrence residual = {np.max(np.abs(rec2)):.3e}")
    print()
    print("n=3 non-diagonalizable example")
    print(f"  |3x3 Hankel det| = {abs(det3_3):.6e}")
    print(f"  |4x4 Hankel det| = {abs(det4_3):.3e}")
    print(f"  max recurrence residual = {np.max(np.abs(rec3)):.3e}")

    assert abs(det2_1) < 2.0e-15
    assert np.max(np.abs(rec1)) < 2.0e-15

    assert abs(det2_2) > 1.0e-4
    assert abs(det3_2) < 2.0e-15
    assert np.max(np.abs(rec2)) < 2.0e-14

    # Rank is generically 3 for this realization: 3x3 determinant nonzero,
    # while every 4x4 determinant must vanish.
    assert abs(det3_3) > 1.0e-7
    assert abs(det4_3) < 2.0e-15
    assert np.max(np.abs(rec3)) < 5.0e-14

    print()
    print(
        "PASS: equally spaced internal-depth responses reveal finite hidden "
        "propagation dimension through Hankel rank. Three colors test rank 1; "
        "five colors can test rank <=2; in general 2n+1 samples support an "
        "(n+1)x(n+1) Hankel determinant null."
    )


if __name__ == "__main__":
    main()
