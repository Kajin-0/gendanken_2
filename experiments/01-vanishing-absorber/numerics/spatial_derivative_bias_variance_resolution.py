"""Bias-variance resolution laws for spatial derivatives of complex log response.

Let y(z)=ln F(z,omega). For independent per-point noise variance sigma_y^2 in
one real response component:

Centered first derivative from z0+-h:
    Var[y'] = sigma_y^2/(2 h^2)
    Bias[y'] = y''' h^2/6 + O(h^4)

Centered second derivative from z0-h,z0,z0+h:
    Var[y''] = 6 sigma_y^2/h^4
    Bias[y''] = y'''' h^2/12 + O(h^4)

For a quartic test function these biases are exact. Minimizing leading MSE gives

    h1* = (3 sigma_y/|y'''|)^(1/3)
    h2* = 864^(1/8) (sigma_y/|y''''|)^(1/4).

The first derivative is sufficient for the exact uniform-segment propagation
experiment. The arbitrary-profile local closure requires the second derivative
through A=y''+(y')^2 and is therefore much more differentiation-noise limited.
"""

from __future__ import annotations

import numpy as np


SIGMA = 1.0e-4
Y3 = 1.5
Y4 = 2.0


def first_mse(h: np.ndarray) -> np.ndarray:
    variance = SIGMA**2 / (2.0 * h**2)
    bias2 = (Y3 * h**2 / 6.0) ** 2
    return variance + bias2


def second_mse(h: np.ndarray) -> np.ndarray:
    variance = 6.0 * SIGMA**2 / h**4
    bias2 = (Y4 * h**2 / 12.0) ** 2
    return variance + bias2


def main() -> None:
    h1_exact = (3.0 * SIGMA / abs(Y3)) ** (1.0 / 3.0)
    h2_exact = (864.0 * SIGMA**2 / Y4**2) ** (1.0 / 8.0)

    grid1 = np.logspace(np.log10(h1_exact) - 1.0, np.log10(h1_exact) + 1.0, 20001)
    grid2 = np.logspace(np.log10(h2_exact) - 1.0, np.log10(h2_exact) + 1.0, 20001)

    h1_num = float(grid1[np.argmin(first_mse(grid1))])
    h2_num = float(grid2[np.argmin(second_mse(grid2))])

    print("Spatial derivative bias-variance resolution")
    print(f"sigma_y={SIGMA:.3e}, |y'''|={Y3:.3f}, |y''''|={Y4:.3f}")
    print(f"first derivative analytic h* = {h1_exact:.9f}")
    print(f"first derivative grid h*     = {h1_num:.9f}")
    print(f"second derivative analytic h* = {h2_exact:.9f}")
    print(f"second derivative grid h*     = {h2_num:.9f}")

    # Integration-time scaling if sigma_y proportional to t^(-1/2).
    for time_factor in (64.0, 256.0, 65536.0):
        h1_ratio = time_factor ** (-1.0 / 6.0)
        h2_ratio = time_factor ** (-1.0 / 8.0)
        print(
            f"time x{time_factor:.0f}: "
            f"h1*/h1={h1_ratio:.6f}, h2*/h2={h2_ratio:.6f}"
        )

    assert abs(h1_num / h1_exact - 1.0) < 3.0e-4
    assert abs(h2_num / h2_exact - 1.0) < 3.0e-4

    # 64x time halves first-derivative optimum spacing exactly.
    assert abs(64.0 ** (-1.0 / 6.0) - 0.5) < 1.0e-14
    # 256x time halves second-derivative optimum spacing exactly.
    assert abs(256.0 ** (-1.0 / 8.0) - 0.5) < 1.0e-14

    print()
    print(
        "PASS: under the leading central-difference bias/noise model, the "
        "uniform two-depth slope experiment obeys a cube-root spatial-noise "
        "law, while arbitrary-profile closure requiring curvature obeys a "
        "fourth-root law. With white averaging noise these become t^(-1/6) "
        "and t^(-1/8), respectively."
    )


if __name__ == "__main__":
    main()
