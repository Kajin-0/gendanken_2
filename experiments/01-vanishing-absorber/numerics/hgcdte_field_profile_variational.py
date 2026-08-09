"""Regression for HGCDTE_FIELD_PROFILE_VARIATIONAL_BOUND.md.

Tests the convexity/Jensen field-profile result for homogeneous local transport
and WKB leakage. This is a mathematical scaling regression, not a device
simulator.
"""

import math
import random


def velocity(f, r=2.0):
    """Dimensionless v/(mu d) with f=F/d."""
    return f / (1.0 + f**r)


def leakage(f, p=2.0, k=3.0):
    """Dimensionless g/(A d^p)."""
    return f**p * math.exp(-k / f)


def reciprocal_velocity(f, r=2.0):
    return 1.0 / velocity(f, r)


def phi_second(f, p, k, r):
    """d^2 g / dU^2 on rising branch, U=1/f+f^(r-1)."""
    q = (r - 1.0) * f**r
    assert 0.0 < q < 1.0
    poly = (
        (1.0 - q) * k**2
        + f * k * (2.0 * p - q * (2.0 * p - r))
        + f**2 * p * (p + 1.0 - q * (p - r + 1.0))
    )
    return f**p * math.exp(-k / f) * poly / (1.0 - q) ** 3


def lower_field_same_velocity(f_hi, r=2.0):
    """Find lower-branch field with same velocity by bisection."""
    f_pk = (r - 1.0) ** (-1.0 / r)
    assert f_hi > f_pk
    target = velocity(f_hi, r)
    lo, hi = 1e-12, f_pk
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if velocity(mid, r) < target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def rising_field_from_u(u_target, r=2.0):
    f_pk = (r - 1.0) ** (-1.0 / r)
    lo, hi = 1e-12, f_pk
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        u_mid = reciprocal_velocity(mid, r)
        # U decreases with f on the rising branch.
        if u_mid > u_target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def main():
    # Algebraic convexity stress over broad parameter ranges.
    for r in [1.1, 1.5, 2.0, 3.0, 5.0]:
        f_pk = (r - 1.0) ** (-1.0 / r)
        for p in [0.2, 0.5, 1.0, 2.0, 4.0]:
            for k in [0.01, 0.1, 1.0, 10.0, 100.0]:
                for frac in [0.01, 0.1, 0.5, 0.9, 0.999]:
                    f = frac * f_pk
                    assert phi_second(f, p, k, r) > 0.0

    # Falling branch is dominated: same velocity at lower F, less leakage.
    for f_hi in [1.1, 1.5, 2.0, 5.0]:
        f_lo = lower_field_same_velocity(f_hi, r=2.0)
        assert abs(velocity(f_lo, 2.0) - velocity(f_hi, 2.0)) < 1e-12
        assert f_lo < 1.0 < f_hi
        assert leakage(f_lo, 2.0, 3.0) < leakage(f_hi, 2.0, 3.0)

    # Jensen test on random profiles restricted to the rising branch.
    rng = random.Random(20260809)
    for _ in range(500):
        fs = [10 ** rng.uniform(-1.5, -0.001) for _ in range(64)]
        # r=2 has f_pk=1.
        ubar = sum(reciprocal_velocity(f, 2.0) for f in fs) / len(fs)
        f0 = rising_field_from_u(ubar, 2.0)
        gbar = sum(leakage(f, 2.0, 3.0) for f in fs) / len(fs)
        g0 = leakage(f0, 2.0, 3.0)
        assert gbar + 1e-14 >= g0

    print("convexity, branch-dominance, and Jensen checks passed")


if __name__ == "__main__":
    main()
