"""Bias-variance optimum for a symmetric complex spatial-slope estimate.

Let f(z)=ln H(z) and gamma=f'. Estimate gamma at z0 from two noisy points
separated by Delta:

    gamma_hat = [f(z0+Delta/2)-f(z0-Delta/2)]/Delta.

For independent endpoint log-magnitude/phase noises with per-endpoint complex
mean-square noise s^2=sigma_A^2+sigma_phi^2,

    E|noise|^2 = 2 s^2/Delta^2.

The central-difference bias is

    bias = Delta^2 gamma''(z0)/24 + O(Delta^4).

Thus the leading complex MSE is

    MSE = 2 s^2/Delta^2 + |gamma''|^2 Delta^4/576,

with optimum

    Delta_opt = [24 s/|gamma''|]^(1/3).

A cubic log-transfer makes the expansion exact and is used here as a regression.
"""

from __future__ import annotations

import numpy as np


GAMMA0 = 0.30 + 2.00j
GAMMA_SECOND = 1.50 + 0.80j
SIGMA_LOGMAG = 0.010
SIGMA_PHASE = 0.015


def log_transfer(z: float) -> complex:
    # f'(0)=GAMMA0 and gamma''(0)=f'''(0)=GAMMA_SECOND.
    return GAMMA0 * z + GAMMA_SECOND * z**3 / 6.0


def exact_noiseless_estimate(delta: float) -> complex:
    return (log_transfer(delta / 2.0) - log_transfer(-delta / 2.0)) / delta


def theoretical_mse(delta: np.ndarray) -> np.ndarray:
    s2 = SIGMA_LOGMAG**2 + SIGMA_PHASE**2
    return (
        2.0 * s2 / delta**2
        + abs(GAMMA_SECOND) ** 2 * delta**4 / 576.0
    )


def main() -> None:
    s = np.sqrt(SIGMA_LOGMAG**2 + SIGMA_PHASE**2)
    delta_opt = (24.0 * s / abs(GAMMA_SECOND)) ** (1.0 / 3.0)

    bias_exact = exact_noiseless_estimate(delta_opt) - GAMMA0
    bias_pred = GAMMA_SECOND * delta_opt**2 / 24.0

    grid = np.linspace(0.05, 1.50, 20000)
    mse = theoretical_mse(grid)
    delta_grid = float(grid[np.argmin(mse)])

    noise_at_opt = 2.0 * s**2 / delta_opt**2
    bias2_at_opt = abs(bias_pred) ** 2
    mse_at_opt = noise_at_opt + bias2_at_opt
    rms_at_opt = np.sqrt(mse_at_opt)
    rms_closed = np.sqrt(3.0) * s / delta_opt

    print("Symmetric-depth complex-slope bias-variance optimum")
    print(f"closed-form Delta_opt = {delta_opt:.9f}")
    print(f"dense-grid Delta_opt = {delta_grid:.9f}")
    print(f"exact/predicted bias difference = {abs(bias_exact-bias_pred):.3e}")
    print(f"noise variance / bias^2 at optimum = {noise_at_opt/bias2_at_opt:.9f}")
    print(f"RMS optimum direct/closed = {rms_at_opt:.9f}/{rms_closed:.9f}")

    assert abs(delta_grid / delta_opt - 1.0) < 2.0e-4
    assert abs(bias_exact - bias_pred) < 2.0e-15
    assert abs(noise_at_opt / bias2_at_opt - 2.0) < 2.0e-12
    assert abs(rms_at_opt / rms_closed - 1.0) < 2.0e-12

    print()
    print(
        "PASS: the optimal symmetric generation-depth separation follows the "
        "cube-root law Delta_opt=(24 s/|gamma''|)^(1/3). At the optimum the "
        "statistical variance is exactly twice the squared curvature bias in "
        "the leading-order model."
    )


if __name__ == "__main__":
    main()
