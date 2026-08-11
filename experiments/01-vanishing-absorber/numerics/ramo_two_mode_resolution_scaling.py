"""Dimensionless two-mode detection threshold from the Hankel-minor witness.

Near root coalescence and q~1, let

    d_m = a q1^m + b q2^m,
    eta = sigma_J / |d|,

where |d| is the local first-difference current scale.  The exact second-mode
signal is W0=a b (q1-q2)^2 and the equal-step witness-noise scale is
sqrt(20)|d| sigma_J.  Approximating d~a+b gives

    Z2 ~= [|a b|/|a+b|^2] |Delta q|^2 /(sqrt(20) eta).

For equal in-phase mode amplitudes a=b,

    Z2 ~= |Delta q|^2 /(4 sqrt(20) eta).

A target Z then requires

    |Delta q| >= sqrt[4 sqrt(20) Z eta].

For Z=3 the coefficient is ~7.3258 sqrt(eta).
"""

from __future__ import annotations

import numpy as np


def amplitude_factor(r: complex) -> float:
    return abs(r) / abs(1.0 + r) ** 2


def delta_threshold(eta: float, Z: float = 3.0, r: complex = 1.0) -> float:
    f = amplitude_factor(r)
    return float(np.sqrt(Z * np.sqrt(20.0) * eta / f))


def main() -> None:
    coefficient_equal = delta_threshold(1.0, Z=3.0, r=1.0)
    print("Two-mode spatial-multiplier resolution scaling")
    print(f"equal-mode 3-sigma coefficient = {coefficient_equal:.12f} * sqrt(eta)")
    assert 7.32 < coefficient_equal < 7.34

    for eta in (1e-3, 1e-4, 1e-5, 1e-6):
        threshold = delta_threshold(eta, r=1.0)
        print(f"eta={eta:.0e}: equal-mode |Delta q| >= {threshold:.6f}")

    assert 0.073 < delta_threshold(1e-4) < 0.074
    assert 0.023 < delta_threshold(1e-5) < 0.024

    # Weaker second mode: r=b/a in phase with the first.
    for r in (1.0, 0.3, 0.1, 0.03):
        f = amplitude_factor(r)
        threshold = delta_threshold(1e-4, r=r)
        print(
            f"r={r:.2f}: amplitude factor={f:.6f}, "
            f"3-sigma Deltaq @eta=1e-4 = {threshold:.6f}"
        )

    # For positive in-phase r, factor is maximal at r=1 by AM-GM.
    grid = np.logspace(-3, 3, 10000)
    factors = np.asarray([amplitude_factor(float(r)) for r in grid])
    r_best = grid[np.argmax(factors)]
    assert 0.99 < r_best < 1.01
    assert abs(np.max(factors) - 0.25) < 1.0e-7

    print()
    print(
        "PASS: second-mode detectability has a simple square-root noise law. "
        "For equal visible modes, a 3-sigma detection requires |q1-q2| about "
        "7.33 sqrt(sigma_J/|d|); weaker mode amplitudes increase the required "
        "spatial-root separation."
    )


if __name__ == "__main__":
    main()
