"""Exact 1-D drift-diffusion complex propagation inversion regression.

For constant downstream drift v>0, diffusion D>0, no recombination, and an
absorbing collector at x=L with the upstream boundary taken sufficiently far
away, the first-passage Laplace transform from a localized generation point x is

    U(x,s) = exp[-gamma(s) (L-x)],

    gamma(s) = (sqrt(v^2 + 4 D s) - v)/(2D).

At s=i omega, two localized generation depths determine gamma from the complex
transfer ratio. If gamma=a+i b, then

    D = omega*a / [b(a^2+b^2)]
    v = omega*(b^2-a^2) / [b(a^2+b^2)].

This file checks the closed-form inverse and the low-frequency expansion.
"""

from __future__ import annotations

import numpy as np


def gamma_exact(v: float, D: float, omega: float) -> complex:
    return (np.sqrt(v * v + 4j * D * omega) - v) / (2.0 * D)


def invert_gamma(gamma: complex, omega: float) -> tuple[float, float]:
    a = float(np.real(gamma))
    b = float(np.imag(gamma))
    modulus2 = a * a + b * b
    D = omega * a / (b * modulus2)
    v = omega * (b * b - a * a) / (b * modulus2)
    return v, D


def main() -> None:
    test_cases = (
        (1.30, 0.070, 4.0),
        (2.10, 0.120, 1.5),
        (0.85, 0.025, 7.0),
        (3.00, 0.400, 0.8),
    )

    max_v_rel = 0.0
    max_D_rel = 0.0

    for v, D, omega in test_cases:
        gamma = gamma_exact(v, D, omega)
        v_rec, D_rec = invert_gamma(gamma, omega)
        max_v_rel = max(max_v_rel, abs(v_rec / v - 1.0))
        max_D_rel = max(max_D_rel, abs(D_rec / D - 1.0))

    # Direct two-depth transfer-ratio check.
    v, D, omega = 1.7, 0.09, 3.2
    L = 2.0
    x1, x2 = 0.35, 1.25
    gamma = gamma_exact(v, D, omega)
    H1 = np.exp(-gamma * (L - x1))
    H2 = np.exp(-gamma * (L - x2))
    gamma_ratio = (np.log(H2) - np.log(H1)) / (x2 - x1)
    v_ratio, D_ratio = invert_gamma(gamma_ratio, omega)

    # Low-frequency expansion. eta=D*omega/v^2.
    # gamma = i omega/v + D omega^2/v^3 - 2 i D^2 omega^3/v^5 + ...
    v0, D0 = 2.0, 0.08
    omega0 = 0.20
    gamma0 = gamma_exact(v0, D0, omega0)
    gamma_series = (
        1j * omega0 / v0
        + D0 * omega0**2 / v0**3
        - 2j * D0**2 * omega0**3 / v0**5
    )
    expansion_rel = abs(gamma0 - gamma_series) / abs(gamma0)

    eta = D0 * omega0 / v0**2

    print("Exact drift-diffusion complex propagation inversion")
    print(f"max relative v inversion error = {max_v_rel:.3e}")
    print(f"max relative D inversion error = {max_D_rel:.3e}")
    print(
        "two-depth ratio recovery: "
        f"v={v_ratio:.12f} (target {v:.12f}), "
        f"D={D_ratio:.12f} (target {D:.12f})"
    )
    print(f"low-frequency eta=D*omega/v^2 = {eta:.3e}")
    print(f"third-order gamma expansion relative error = {expansion_rel:.3e}")

    assert max_v_rel < 5.0e-14
    assert max_D_rel < 5.0e-14
    assert abs(v_ratio / v - 1.0) < 5.0e-14
    assert abs(D_ratio / D - 1.0) < 5.0e-14
    assert expansion_rel < 5.0e-7

    print()
    print(
        "PASS: one complex spatial propagation constant exactly determines "
        "constant drift velocity and diffusion coefficient in the stated "
        "first-passage model. The low-frequency phase is deterministic to "
        "leading order while log-magnitude acquires the leading diffusion term."
    )


if __name__ == "__main__":
    main()
