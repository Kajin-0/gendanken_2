"""Regression for HGCDTE_LINEAR_GRADED_KANE_WKB.md.

Checks the closed linear-band-edge WKB action against direct numerical
integration and verifies the fixed-conduction-slope grading ratio.
This is not a calibrated HgCdTe current simulator.
"""

import math


def numerical_action(delta0, s_c, s_v, hbar_v=1.0, n=500000):
    """Midpoint integration for E=0, Ec0=+delta0, Ev0=-delta0."""
    assert s_c > 0.0 and s_v > 0.0
    x_c = delta0 / s_c
    x_v = -delta0 / s_v
    dx = (x_c - x_v) / n
    total = 0.0
    for i in range(n):
        x = x_v + (i + 0.5) * dx
        e_c = delta0 - s_c * x
        e_v = -delta0 - s_v * x
        kappa = math.sqrt(max(0.0, e_c * (-e_v))) / hbar_v
        total += kappa * dx
    return 2.0 * total


def closed_action(delta0, s_c, s_v, hbar_v=1.0):
    x_c = delta0 / s_c
    x_v = -delta0 / s_v
    return (
        math.pi
        * math.sqrt(s_c * s_v)
        * (x_c - x_v) ** 2
        / (4.0 * hbar_v)
    )


def ratio(eta):
    assert 0.0 <= eta < 0.5
    return (1.0 - eta) ** 2 / (1.0 - 2.0 * eta) ** 1.5


def main():
    # Direct numerical verification of the exact WKB integral.
    for s_c, s_v in [(1.0, 1.0), (1.0, 0.8), (2.0, 0.4), (3.0, 1.7)]:
        exact = closed_action(0.7, s_c, s_v)
        numeric = numerical_action(0.7, s_c, s_v)
        assert abs(numeric - exact) / exact < 2e-9

    # Constant-gap common-field limit: S = pi Delta^2/(hbar v slope).
    delta0 = 0.6
    slope = 1.3
    exact = closed_action(delta0, slope, slope)
    reference = math.pi * delta0**2 / slope
    assert abs(exact - reference) < 1e-14

    # Fixed conduction slope grading ratio.
    s = 1.0
    for eta in [0.0, 0.1, 0.2, 0.3, 0.4, 0.45, 0.49]:
        s_v = (1.0 - 2.0 * eta) * s
        action = closed_action(delta0, s, s_v)
        action0 = closed_action(delta0, s, s)
        assert abs(action / action0 - ratio(eta)) < 1e-13

    # Strict monotonicity over the admitted range.
    previous = ratio(0.0)
    for i in range(1, 500):
        eta = 0.499 * i / 500.0
        current = ratio(eta)
        assert current > previous
        previous = current

    print("linear graded Kane WKB checks passed")
    for eta in [0.1, 0.2, 0.3, 0.4, 0.45, 0.49]:
        print(f"eta={eta:.2f} action_ratio={ratio(eta):.9f}")


if __name__ == "__main__":
    main()
