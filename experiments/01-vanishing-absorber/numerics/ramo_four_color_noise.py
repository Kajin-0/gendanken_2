"""Linearized noise propagation for the four-color Shockley-Ramo closure.

Let four complex current samples J0..J3 have independent circular complex noise
with E|epsilon_m|^2 = sigma_J^2.  Define first differences d_m=J_{m+1}-J_m and

    C4 = 2 log d1 - log d0 - log d2.

At high SNR,

    delta C4 = c0 eps0 + c1 eps1 + c2 eps2 + c3 eps3

with

    c0 =  1/d0
    c1 = -1/d0 - 2/d1
    c2 =  2/d1 + 1/d2
    c3 = -1/d2.

Therefore Var_complex(C4)=sigma_J^2 sum |c_m|^2.  In the equal-difference
limit d0=d1=d2=d the coefficients are (1,-3,3,-1)/d and the complex RMS is
sqrt(20) sigma_J/|d|.

The same script checks Monte-Carlo convergence and the noise of the propagation
exponent estimate gamma=-log(d1/d0)/h.
"""

from __future__ import annotations

import numpy as np


RNG = np.random.default_rng(4127)
SIGMA = 2.0e-4
D = 0.14 + 0.09j
H = 0.35
Q = 0.93 - 0.11j
NMC = 250000


J_TRUE = np.asarray(
    (
        0.2 + 0.1j,
        0.2 + 0.1j + D,
        0.2 + 0.1j + D + D * Q,
        0.2 + 0.1j + D + D * Q + D * Q**2,
    ),
    dtype=complex,
)


def coeffs(J: np.ndarray) -> np.ndarray:
    d0, d1, d2 = np.diff(J)
    return np.asarray(
        (
            1.0 / d0,
            -1.0 / d0 - 2.0 / d1,
            2.0 / d1 + 1.0 / d2,
            -1.0 / d2,
        ),
        dtype=complex,
    )


def closure(J: np.ndarray) -> np.ndarray:
    d = np.diff(J, axis=-1)
    return 2.0 * np.log(d[..., 1]) - np.log(d[..., 0]) - np.log(d[..., 2])


def gamma_est(J: np.ndarray) -> np.ndarray:
    d = np.diff(J, axis=-1)
    return -np.log(d[..., 1] / d[..., 0]) / H


def main() -> None:
    c = coeffs(J_TRUE)
    predicted_var = SIGMA**2 * float(np.sum(np.abs(c) ** 2))

    # Circular complex noise with E|eps|^2=SIGMA^2.
    noise = (
        RNG.normal(size=(NMC, 4)) + 1j * RNG.normal(size=(NMC, 4))
    ) * (SIGMA / np.sqrt(2.0))
    samples = J_TRUE[None, :] + noise

    C0 = closure(J_TRUE)
    C = closure(samples)
    dc = C - C0
    mc_var = float(np.mean(np.abs(dc - np.mean(dc)) ** 2))

    d0, d1, _ = np.diff(J_TRUE)
    gamma_coeff = np.asarray(
        (1.0 / d0, -(1.0 / d0 + 1.0 / d1), 1.0 / d1, 0.0),
        dtype=complex,
    ) / H
    predicted_gamma_var = SIGMA**2 * float(np.sum(np.abs(gamma_coeff) ** 2))
    g0 = gamma_est(J_TRUE)
    g = gamma_est(samples)
    dg = g - g0
    mc_gamma_var = float(np.mean(np.abs(dg - np.mean(dg)) ** 2))

    equal_coeff_norm = np.sqrt(1.0 + 9.0 + 9.0 + 1.0)

    print("Four-color closure noise propagation")
    print(f"predicted Var(C4) = {predicted_var:.9e}")
    print(f"Monte-Carlo Var(C4) = {mc_var:.9e}")
    print(f"ratio MC/pred = {mc_var/predicted_var:.6f}")
    print(f"predicted Var(gamma) = {predicted_gamma_var:.9e}")
    print(f"Monte-Carlo Var(gamma) = {mc_gamma_var:.9e}")
    print(f"ratio MC/pred gamma = {mc_gamma_var/predicted_gamma_var:.6f}")
    print(f"equal-difference coefficient norm = sqrt(20) = {equal_coeff_norm:.12f}")

    assert abs(mc_var / predicted_var - 1.0) < 0.02
    assert abs(mc_gamma_var / predicted_gamma_var - 1.0) < 0.02
    assert abs(equal_coeff_norm - np.sqrt(20.0)) < 1.0e-14

    print()
    print(
        "PASS: linearized covariance predicts the complex closure and propagation-"
        "exponent noise.  In the equal-difference limit the closure is exactly "
        "a (1,-3,3,-1) third-difference stencil with sqrt(20) complex-noise "
        "amplification relative to one sample divided by the current step."
    )


if __name__ == "__main__":
    main()
