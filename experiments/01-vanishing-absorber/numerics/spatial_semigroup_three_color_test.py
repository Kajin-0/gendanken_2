"""Spatial first-passage semigroup and three-color closure regression.

For a scalar spatially homogeneous continuous-path strong-Markov first-passage
process with a fixed local state at each crossing, the successful Laplace/RF
transform over distance d obeys

    U_s(a+b)=U_s(a) U_s(b),

hence U_s(d)=exp[-gamma_s d] after normalization U_s(0)=1 and continuity.
The DC-normalized field is also exponential.

A rigidly translated finite-width generation kernel therefore obeys the exact
three-color geometric-mean law at equally spaced generation coordinates.

As a simple hidden-state counterexample, an unresolved mixture of two
propagation populations has

    F(d)=p exp(-Gamma1 d)+(1-p) exp(-Gamma2 d),

which is not a scalar semigroup and generically violates three-color closure.
"""

from __future__ import annotations

import numpy as np


DELTA = 0.8
DISTANCES = np.asarray((1.0, 1.0 + DELTA, 1.0 + 2.0 * DELTA))
GAMMA = 0.24 + 0.91j


def closure_error(values: np.ndarray) -> complex:
    return values[1] ** 2 - values[0] * values[2]


def main() -> None:
    scalar = np.exp(-GAMMA * DISTANCES)
    err_scalar = closure_error(scalar)

    # Hidden two-population transport: both components separately obey a
    # homogeneous semigroup, but the unresolved mixture does not.
    p = 0.62
    gamma1 = 0.18 + 0.72j
    gamma2 = 0.43 + 1.21j
    mixture = (
        p * np.exp(-gamma1 * DISTANCES)
        + (1.0 - p) * np.exp(-gamma2 * DISTANCES)
    )
    err_mix = closure_error(mixture)

    # Direct semigroup check for scalar propagation.
    a, b = 0.7, 1.3
    Ua = np.exp(-GAMMA * a)
    Ub = np.exp(-GAMMA * b)
    Uab = np.exp(-GAMMA * (a + b))

    print("Spatial first-passage semigroup / three-color closure")
    print(f"scalar semigroup |U(a+b)-U(a)U(b)| = {abs(Uab-Ua*Ub):.3e}")
    print(f"scalar three-color closure error = {abs(err_scalar):.3e}")
    print(f"hidden-population closure error = {abs(err_mix):.6e}")

    assert abs(Uab - Ua * Ub) < 2.0e-15
    assert abs(err_scalar) < 2.0e-15
    assert abs(err_mix) > 1.0e-3

    print()
    print(
        "PASS: scalar homogeneous first-passage propagation has the exact "
        "spatial semigroup/geometric-mean closure, while an unresolved mixture "
        "of two homogeneous propagation populations generically breaks it."
    )


if __name__ == "__main__":
    main()
