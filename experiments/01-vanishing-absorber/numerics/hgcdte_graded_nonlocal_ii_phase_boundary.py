"""Regression for HGCDTE_GRADED_NONLOCAL_II_PHASE_BOUNDARY.md.

This is a deterministic check of the analytic mean-energy phase boundary.
It is not a calibrated HgCdTe impact-ionization simulator.
"""

import math


def A(r):
    if abs(r) < 1e-8:
        return 1.0 - r / 2.0 + r * r / 6.0
    return -math.expm1(-r) / r


def zeta_critical(r, chi):
    return chi / (chi + A(r))


def epsilon_fraction(y, r, zeta):
    """epsilon(x)/Eg0 for y=x/L in a linear gradient."""
    if r == 0.0:
        return zeta * y
    return zeta * (1.0 - math.exp(-r * y)) / r


def threshold_fraction(y, zeta, chi):
    """Eth(x)/Eg0."""
    return chi * (1.0 - zeta * y)


def has_crossing_scan(r, zeta, chi, n=20000):
    previous = epsilon_fraction(0.0, r, zeta) - threshold_fraction(0.0, zeta, chi)
    for i in range(1, n + 1):
        y = i / n
        value = epsilon_fraction(y, r, zeta) - threshold_fraction(y, zeta, chi)
        if value >= 0.0 or previous * value <= 0.0:
            return True
        previous = value
    return False


def main():
    # Ballistic limit: chi=1 -> zeta_c=1/2.
    assert abs(zeta_critical(1e-10, 1.0) - 0.5) < 1e-8

    # Stronger relaxation must make threshold harder to reach.
    values = [zeta_critical(r, 1.0) for r in (0.01, 0.1, 1.0, 10.0, 100.0)]
    assert all(b > a for a, b in zip(values, values[1:]))
    assert values[-1] > 0.98

    # Analytic phase boundary versus direct scan.
    for chi in (0.8, 1.0, 1.2):
        for r in (0.02, 0.2, 1.0, 3.0, 10.0):
            zc = zeta_critical(r, chi)
            below = max(1e-6, zc * (1.0 - 1e-4))
            above = min(0.999999, zc * (1.0 + 1e-4))
            assert not has_crossing_scan(r, below, chi)
            assert has_crossing_scan(r, above, chi)

    # Exit equality is the boundary because epsilon rises and Eth falls.
    for r in (0.05, 0.5, 2.0, 8.0):
        chi = 1.0
        zc = zeta_critical(r, chi)
        lhs = zc * A(r)
        rhs = chi * (1.0 - zc)
        assert abs(lhs - rhs) < 1e-14

    print("graded nonlocal II phase-boundary regression: PASS")
    print("r      zeta_c(chi=1)")
    for r in (0.0, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0):
        rr = 1e-12 if r == 0.0 else r
        print(f"{r:4.1f}   {zeta_critical(rr, 1.0):.8f}")


if __name__ == "__main__":
    main()
