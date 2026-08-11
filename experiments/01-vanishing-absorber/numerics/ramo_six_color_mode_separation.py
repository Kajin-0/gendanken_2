"""Exact two-mode spatial-separation witness for six-color Ramo first differences.

Let a first-difference sequence contain exactly two spatial modes

    d_m = a q1^m + b q2^m,  m=0,...,4.

Define the adjacent 2x2 Hankel minors

    W_m = d_m d_{m+2} - d_{m+1}^2.

Then exactly

    W_m = a b (q1 q2)^m (q1-q2)^2.

Consequences:
- one mode / zero amplitude / merged roots => W_m=0;
- W_{m+1}/W_m = q1 q2;
- six-color rank-two closure: W_1^2 = W_0 W_2;
- the 2x2 linear system used to recover the recurrence coefficients has
  determinant W_0, so coefficient recovery is ill-conditioned as
  1/[a b (q1-q2)^2];
- root recovery adds the quadratic discriminant sqrt(S^2-4P)=q1-q2 and is
  additionally sensitive as the roots coalesce.

This script verifies the identities and numerically demonstrates the expected
near-coalescence conditioning of the direct recurrence estimator.
"""

from __future__ import annotations

import numpy as np


def sequence(a: complex, b: complex, q1: complex, q2: complex) -> np.ndarray:
    m = np.arange(5)
    return a * q1**m + b * q2**m


def minors(d: np.ndarray) -> np.ndarray:
    return np.asarray(
        [d[m] * d[m + 2] - d[m + 1] ** 2 for m in range(3)],
        dtype=complex,
    )


def recover_SP(d: np.ndarray) -> tuple[complex, complex]:
    # d_{m+2}=S d_{m+1}-P d_m for m=0,1.
    M = np.asarray(((d[1], -d[0]), (d[2], -d[1])), dtype=complex)
    rhs = np.asarray((d[2], d[3]), dtype=complex)
    S, P = np.linalg.solve(M, rhs)
    return complex(S), complex(P)


def sorted_roots(S: complex, P: complex) -> np.ndarray:
    roots = np.roots((1.0, -S, P))
    return roots[np.argsort(roots.real)]


def main() -> None:
    a = 0.73 - 0.21j
    b = -0.38 + 0.44j
    q1 = 0.91 + 0.08j
    q2 = 0.72 - 0.05j

    d = sequence(a, b, q1, q2)
    W = minors(d)
    predicted = np.asarray(
        [a * b * (q1 * q2) ** m * (q1 - q2) ** 2 for m in range(3)]
    )

    print("Six-color two-mode spatial-separation witness")
    print(f"max exact minor error = {np.max(np.abs(W-predicted)):.3e}")
    print(f"W1/W0 = {W[1]/W[0]:.12f}; q1*q2 = {q1*q2:.12f}")
    print(f"|W1^2-W0 W2| = {abs(W[1]**2-W[0]*W[2]):.3e}")

    assert np.max(np.abs(W - predicted)) < 2.0e-15
    assert abs(W[1] / W[0] - q1 * q2) < 2.0e-14
    assert abs(W[1] ** 2 - W[0] * W[2]) < 2.0e-15

    S, P = recover_SP(d)
    assert abs(S - (q1 + q2)) < 2.0e-14
    assert abs(P - q1 * q2) < 2.0e-14

    # Near-coalescence conditioning of the direct recurrence estimator.
    # Use a deterministic perturbation with fixed absolute size and verify that
    # the recurrence-coefficient sensitivity grows approximately as delta^-2.
    base = 0.82 + 0.04j
    perturb = np.asarray((1, -2, 1.5, -0.7, 0.3), dtype=complex)
    eps = 1.0e-12
    deltas = np.asarray((0.12, 0.06, 0.03, 0.015))
    coefficient_errors = []
    witness_scales = []

    for delta in deltas:
        qa = base + 0.5 * delta
        qb = base - 0.5 * delta
        dd = sequence(1.0 + 0.2j, 0.8 - 0.1j, qa, qb)
        WW = minors(dd)
        witness_scales.append(abs(WW[0]))

        S0, P0 = recover_SP(dd)
        Sp, Pp = recover_SP(dd + eps * perturb)
        coefficient_errors.append(np.hypot(abs(Sp - S0), abs(Pp - P0)))

    witness_scales = np.asarray(witness_scales)
    coefficient_errors = np.asarray(coefficient_errors)

    # W0 must scale as delta^2 exactly for fixed amplitudes/base product up to the
    # mild product change induced by symmetric splitting (here m=0, so exact).
    ratios_W = witness_scales[:-1] / witness_scales[1:]
    print("near-coalescence W0 ratios for halved delta = " + ", ".join(f"{x:.4f}" for x in ratios_W))
    assert np.max(np.abs(ratios_W - 4.0)) < 2.0e-8

    # The explicit linear-system estimator becomes rapidly unstable.  Do not
    # assert a universal exponent for every perturbation direction; simply
    # require monotonic strong growth as roots merge.
    growth = coefficient_errors[1:] / coefficient_errors[:-1]
    print("coefficient-error growth for halved delta = " + ", ".join(f"{x:.3f}" for x in growth))
    assert np.all(growth > 2.5)

    print()
    print(
        "PASS: two-mode detectability is controlled exactly by a b (q1-q2)^2. "
        "The six-color minors form a geometric sequence, while recurrence/root "
        "recovery becomes singular as either mode disappears or the roots merge."
    )


if __name__ == "__main__":
    main()
