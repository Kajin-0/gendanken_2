"""Regression for the graded HgCdTe spectral-delay peak branch.

Checks:
1. continuity and extremum of the high-optical-depth ballistic delay;
2. high-energy approach to the full-length vK floor;
3. endpoint maximum of the finite-relaxation exit mean energy.

This is not a calibrated HgCdTe detector simulation.
"""

import math


def phi(z, e):
    if z <= 0.0:
        return 0.0
    return math.sqrt(e * z) + z ** 1.5 / (3.0 * math.sqrt(e))


def theta_below(s):
    return math.sqrt(s) / math.sqrt(1.0 + s) * (1.0 + 4.0 * s / 3.0)


def theta_above(s, R, xi_e):
    e = R + xi_e * (1.0 + s - R)
    z_s = xi_e * (1.0 + s - R)
    z_0 = z_s + (R - 1.0)
    return phi(z_0, e) - phi(z_s, e)


def theta_high_qe(s, R, xi_e):
    if s <= R - 1.0:
        return theta_below(s)
    return theta_above(s, R, xi_e)


def exit_energy(u, delta_e, K, xi_e):
    return K + (xi_e * u - K) * math.exp(-(delta_e - u) / K)


def endpoint_max(delta_e, K, xi_e):
    earliest = K * (1.0 - math.exp(-delta_e / K))
    latest = xi_e * delta_e
    return max(earliest, latest)


def main():
    # Continuous at the entrance-gap photon energy.
    for R in (1.2, 1.5, 2.0, 3.0):
        s_peak = R - 1.0
        target = theta_below(s_peak)
        for xi in (0.25, 0.5, 1.0):
            assert abs(theta_above(s_peak, R, xi) - target) < 1e-13

    # Increase below the entrance gap, decrease above it for xi_e > 0.
    for R in (1.5, 2.0, 3.0):
        for xi in (0.25, 0.5, 1.0):
            s_peak = R - 1.0
            below = [theta_high_qe(s_peak * f, R, xi) for f in (0.2, 0.4, 0.6, 0.8, 1.0)]
            assert all(b > a for a, b in zip(below, below[1:]))
            above = [theta_high_qe(s_peak + x, R, xi) for x in (0.0, 0.5, 1.0, 2.0, 5.0, 20.0)]
            assert all(b < a for a, b in zip(above, above[1:]))

    # High-energy transit approaches L/vK -> theta = R-1.
    for R in (1.5, 2.0, 3.0):
        for xi in (0.25, 0.5, 1.0):
            val = theta_high_qe(1.0e6, R, xi)
            assert abs(val - (R - 1.0)) < 1e-4

    # Finite-relaxation exit energy has no interior maximum.
    for delta_e in (0.05, 0.2, 1.0):
        for K in (0.02, 0.1, 0.5, 2.0):
            for xi in (0.0, 0.25, 0.5, 0.8, 1.0):
                target = endpoint_max(delta_e, K, xi)
                sampled = max(
                    exit_energy(delta_e * i / 10000.0, delta_e, K, xi)
                    for i in range(10001)
                )
                assert abs(sampled - target) < 1e-10

    # Flat-heavy-hole limit: latest-generation endpoint fixes the maximum.
    for delta_e in (0.05, 0.2, 1.0):
        for K in (0.01, 0.1, 1.0, 10.0):
            assert abs(endpoint_max(delta_e, K, 1.0) - delta_e) < 1e-14

    print("spectral delay peak / hot-energy endpoint regression: PASS")
    print()
    print("R=2, xi_e=1")
    print("Egamma/E0   theta")
    for ratio in (1.05, 1.10, 1.25, 1.50, 2.00, 2.50, 3.00, 4.00, 6.00):
        s = ratio - 1.0
        print(f"{ratio:9.2f}   {theta_high_qe(s, 2.0, 1.0):.9f}")


if __name__ == "__main__":
    main()
