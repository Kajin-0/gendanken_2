"""Regression for graded neutral HgCdTe collection/absorption derivations.

Checks:
- uniform-generation collection formula and transit 3 dB constant;
- Beer-Lambert closed response;
- sharp-edge graded external-QE optima;
- square-root / general power-law edge quadrature examples.

This is a deterministic scaling regression, not a calibrated HgCdTe simulator.
"""

import cmath
import math

from scipy.integrate import quad
from scipy.optimize import brentq, minimize_scalar


def eta_uniform(xi):
    if abs(xi) < 1e-12:
        return 1.0
    return (1.0 - math.exp(-xi)) / xi


def h_uniform(omega_t, xi):
    z = complex(xi, omega_t)
    if abs(z) < 1e-12:
        return 1.0 + 0j
    return (1.0 - cmath.exp(-z)) / z


def h_uniform_norm(omega_t, xi):
    return h_uniform(omega_t, xi) / eta_uniform(xi)


def omega3_uniform(xi):
    def f(om):
        return abs(h_uniform_norm(om, xi)) ** 2 - 0.5

    return brentq(f, 1e-12, max(100.0, 20.0 * (1.0 + xi)))


def h_beer(a, z):
    z = complex(z)
    if abs(a - z) < 1e-9:
        return a * math.exp(-a) / (1.0 - math.exp(-a))
    return a * (cmath.exp(-z) - math.exp(-a)) / ((a - z) * (1.0 - math.exp(-a)))


def eta_sharp(r, a0, chi):
    a = a0 * r
    xi = chi * r * r
    if abs(a - xi) < 1e-9:
        return a * math.exp(-a)
    return a * (math.exp(-xi) - math.exp(-a)) / (a - xi)


def eta_power(r, a0, chi, m):
    a = a0 * r
    xi = chi * r * r
    gamma = 1.0 / (m + 1.0)
    integral = quad(
        lambda t: math.exp(-a * t + xi * t**gamma),
        0.0,
        1.0,
        epsabs=1e-12,
        epsrel=1e-12,
        limit=300,
    )[0]
    return a * math.exp(-xi) * integral


def optimum(fun):
    res = minimize_scalar(lambda r: -fun(r), bounds=(1e-8, 1.0), method="bounded")
    return res.x, -res.fun


def main():
    # Exact DC collection identity.
    assert abs(eta_uniform(1.0) - (1.0 - math.exp(-1.0))) < 1e-14

    # Transit-limited 3 dB constant.
    om0 = omega3_uniform(1e-10)
    ct = om0 / (2.0 * math.pi)
    assert abs(ct - 0.4429464706894523) < 2e-10

    # Representative finite-lifetime points.
    for xi, eta_ref, om_ref in [
        (0.1, 0.9516258196, 2.7839560957),
        (1.0, 0.6321205588, 2.8685967620),
        (2.0, 0.4323323584, 3.1293249225),
        (10.0, 0.0999954600, 10.0017396450),
    ]:
        assert abs(eta_uniform(xi) - eta_ref) < 2e-10
        assert abs(omega3_uniform(xi) - om_ref) < 3e-8

    # Beer-Lambert tends to uniform-generation response as optical thickness -> 0.
    z = complex(0.7, 0.3)
    assert abs(h_beer(1e-7, z) - h_uniform(0.3, 0.7)) < 2e-8

    # Sharp-edge dimensionless examples.
    sharp_cases = [
        (3.0, 0.3, 0.763, 0.799),
        (10.0, 0.1, 0.478, 0.974),
    ]
    for a0, chi, r_ref, eta_ref in sharp_cases:
        r, eta = optimum(lambda rr: eta_sharp(rr, a0, chi))
        assert abs(r - r_ref) < 0.003
        assert abs(eta - eta_ref) < 0.003

    # Square-root continuous edge examples (m=1/2).
    sqrt_cases = [
        (3.0, 0.3, 0.797, 0.807),
        (10.0, 0.1, 0.505, 0.979),
    ]
    for a0, chi, r_ref, eta_ref in sqrt_cases:
        r, eta = optimum(lambda rr: eta_power(rr, a0, chi, 0.5))
        assert abs(r - r_ref) < 0.003
        assert abs(eta - eta_ref) < 0.003

    # Infinite grading loses optical depth for all tested power-law exponents.
    for m in [-0.5, 0.0, 0.5, 1.0, 2.0, 4.0]:
        e1 = eta_power(1e-3, 3.0, 1.0, m)
        e2 = eta_power(5e-4, 3.0, 1.0, m)
        assert e2 < e1
        # eta ~ a0 r as r -> 0.
        assert abs(e2 / (3.0 * 5e-4) - 1.0) < 0.01

    print(f"transit constant f3dB*T = {ct:.12f}")
    print("graded collection/absorption checks passed")


if __name__ == "__main__":
    main()
