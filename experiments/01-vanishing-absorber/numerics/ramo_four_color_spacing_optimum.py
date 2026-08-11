"""Bias-noise optimum for four-color Shockley-Ramo closure spacing.

In mean-depth coordinates, suppose the leading calibrated-but-unmodeled smooth
optical/source-shape closure systematic is

    bias(C4) = A h^2,

while independent equal complex current noise gives, at low RF where the current
step is |Delta J| ~= G_J h,

    sigma(C4) = B/h,
    B = sqrt(20) sigma_J/G_J.

Then

    MSE(h)=A^2 h^4 + B^2/h^2

has the exact optimum

    h* = [B/(sqrt(2) A)]^(1/3).

For the leading variance-shape error A=|gamma v'''|/2 this becomes

    h* = [sqrt(40) sigma_J/(G_J |gamma v'''|)]^(1/3).

At h*, noise variance equals twice the squared systematic bias.  If
sigma_J ~ t^-1/2, h* ~ t^-1/6.

This is a conditional design law, not a universal information bound.
"""

from __future__ import annotations

import numpy as np


def mse(h: float, A: float, B: float) -> float:
    return A * A * h**4 + B * B / h**2


def optimum(A: float, B: float) -> float:
    return (B / (np.sqrt(2.0) * A)) ** (1.0 / 3.0)


def main() -> None:
    A = 0.017
    B = 0.0034
    hstar = optimum(A, B)

    # Dense numerical check around the analytic stationary point.
    grid = np.linspace(0.05 * hstar, 4.0 * hstar, 200001)
    numerical = grid[np.argmin([mse(h, A, B) for h in grid])]

    bias2 = (A * hstar**2) ** 2
    noise_var = (B / hstar) ** 2

    print("Four-color spacing bias-noise optimum")
    print(f"analytic h* = {hstar:.12e}")
    print(f"numerical h* = {numerical:.12e}")
    print(f"numerical/analytic = {numerical/hstar:.9f}")
    print(f"noise variance / bias^2 at optimum = {noise_var/bias2:.12f}")

    assert abs(numerical / hstar - 1.0) < 3.0e-5
    assert abs(noise_var / bias2 - 2.0) < 1.0e-12

    # White averaging sigma_J ~ t^-1/2 implies h* ~ t^-1/6.
    ratio_t = 64.0
    h_ratio = (
        (B / np.sqrt(ratio_t)) / (np.sqrt(2.0) * A)
    ) ** (1.0 / 3.0) / hstar
    assert abs(h_ratio - ratio_t ** (-1.0 / 6.0)) < 1.0e-14

    # Substitute A=|gamma v'''|/2 and B=sqrt(20)sigma/G.
    gamma_abs = 0.8
    v3_abs = 0.12
    sigma_J = 2.0e-4
    GJ = 0.7
    direct = optimum(gamma_abs * v3_abs / 2.0, np.sqrt(20.0) * sigma_J / GJ)
    compact = (
        np.sqrt(40.0) * sigma_J / (GJ * gamma_abs * v3_abs)
    ) ** (1.0 / 3.0)
    assert abs(direct / compact - 1.0) < 1.0e-14

    print()
    print(
        "PASS: the four-color closure spacing has a cube-root optimum when "
        "h^2 smooth optical bias is balanced against h^-1 independent-current "
        "noise.  The optimal spacing improves only as t^-1/6 under white "
        "averaging."
    )


if __name__ == "__main__":
    main()
