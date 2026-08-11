"""Regression checks for the exact DC+RF inversion conditioning theorem.

This is a theory regression, not an experimental forecast.
"""

from __future__ import annotations

import numpy as np
from scipy.optimize import brentq


def chi_from_xi(xi: float) -> float:
    return float(
        brentq(
            lambda chi: chi * (1.0 + chi**2) / (1.0 - chi**2) ** 2 - xi,
            1.0e-14,
            1.0 - 1.0e-12,
        )
    )


def condition_numbers(chi: float) -> tuple[float, float]:
    common = np.sqrt(chi**4 + 6.0 * chi**2 + 1.0)
    kd = common / chi
    kv = np.sqrt(1.0 + chi**2) * common / (1.0 - chi**2)
    return float(kd), float(kv)


def root_displacement(D: float, V: float, omega: float) -> complex:
    return complex((np.sqrt(V**2 + 4.0j * D * omega) - V) / (2.0 * D))


def invert_delta_root(delta: complex, omega: float) -> tuple[float, float]:
    u = delta.real
    v = delta.imag
    r2 = u * u + v * v
    D = omega * u / (v * r2)
    V = omega * (v * v - u * u) / (v * r2)
    return float(D), float(V)


def main() -> None:
    D = 0.02327
    V = 34473.5

    print("DC+RF inversion conditioning regression")
    print(f"reference D={D:.8f} m^2/s, V*={V:.3f} m/s")
    print()

    for frequency in (100e6, 500e6, 1e9, 5e9, 10e9):
        omega = 2.0 * np.pi * frequency
        delta = root_displacement(D, V, omega)
        D_back, V_back = invert_delta_root(delta, omega)
        xi = D * omega / V**2
        chi = delta.real / delta.imag
        chi_from = chi_from_xi(xi)
        kd, kv = condition_numbers(chi)

        assert np.isclose(D_back, D, rtol=2e-13, atol=0.0)
        assert np.isclose(V_back, V, rtol=2e-13, atol=0.0)
        assert np.isclose(chi_from, chi, rtol=2e-12, atol=2e-14)

        print(
            f"{frequency/1e9:7.3f} GHz: "
            f"xi={xi:.9f}, chi={chi:.9f}, KD={kd:.6f}, KV={kv:.6f}"
        )

    chi_star = 1.0 / np.sqrt(3.0)
    xi_star = chi_star * (1.0 + chi_star**2) / (1.0 - chi_star**2) ** 2
    kd_star, kv_star = condition_numbers(chi_star)
    omega_star = np.sqrt(3.0) * V**2 / D
    f_star = omega_star / (2.0 * np.pi)

    assert np.isclose(xi_star, np.sqrt(3.0), rtol=1e-14)
    assert np.isclose(kd_star, np.sqrt(28.0 / 3.0), rtol=1e-14)
    assert np.isclose(kv_star, np.sqrt(28.0 / 3.0), rtol=1e-14)
    assert 14.0e9 < f_star < 14.2e9

    print()
    print(
        f"balanced optimum: chi=1/sqrt(3)={chi_star:.9f}, "
        f"xi=sqrt(3)={xi_star:.9f}, K={kd_star:.9f}, "
        f"f*={f_star/1e9:.6f} GHz"
    )
    print("PASS: exact inversion, chi-xi mapping, and conditioning optimum verified.")


if __name__ == "__main__":
    main()
