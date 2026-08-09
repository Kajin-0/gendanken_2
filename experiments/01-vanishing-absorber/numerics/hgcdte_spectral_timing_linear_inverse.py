"""Synthetic inversion for HGCDTE_SPECTRAL_TIMING_LINEAR_INVERSE.md.

This is not a calibrated HgCdTe device model.

The script creates a known nonuniform effective carrier-velocity profile,
constructs finite wavelength-dependent generation kernels for a linear graded
absorber, adds a wavelength-independent common timing delay and measurement
noise, and reconstructs the spatial delay density q(x)=1/v(x) from the full
timing-vs-photon-energy dataset.

It tests whether the proposed inverse method provides information beyond a
simple wavelength-dependent bandwidth comparison.
"""

from __future__ import annotations

import numpy as np


L = 1.0
EG_IN = 2.0
EG_OUT = 1.0
G = 1.0
BETA = 0.5
N_EDGE = BETA + 1.0
ELL_ALPHA = 0.07

N_X = 80
N_E = 90
COMMON_DELAY = 0.15
NOISE_FRACTION = 1.0e-3
REGULARIZATION = 0.10
SEED = 20260809


def build_grid() -> tuple[np.ndarray, float]:
    dx = L / N_X
    x = (np.arange(N_X) + 0.5) * dx
    return x, dx


def true_velocity(x: np.ndarray) -> np.ndarray:
    """Synthetic positive profile with one localized slow-transport region."""
    baseline = 0.9 + 0.35 * x
    slow_region = 0.28 * np.exp(-0.5 * ((x - 0.55) / 0.09) ** 2)
    return baseline - slow_region


def build_forward_matrix(x: np.ndarray, dx: float, energies: np.ndarray) -> np.ndarray:
    """Build A_ij = K_i(x_j) dx using conditional generation CDF kernels."""
    A = np.zeros((energies.size, x.size))

    for i, e_gamma in enumerate(energies):
        xg = (EG_IN - e_gamma) / G
        d = L - xg
        tau = (d / ELL_ALPHA) ** N_EDGE
        norm = 1.0 - np.exp(-tau)

        for j, s in enumerate(x):
            if s <= xg:
                cdf = 0.0
            else:
                z = s - xg
                y = min((z / ELL_ALPHA) ** N_EDGE, tau)
                cdf = (1.0 - np.exp(-y)) / norm

            A[i, j] = cdf * dx

    return A


def second_difference_matrix(n: int) -> np.ndarray:
    D2 = np.zeros((n - 2, n))
    for i in range(n - 2):
        D2[i, i : i + 3] = (1.0, -2.0, 1.0)
    return D2


def solve_regularized(
    A: np.ndarray,
    measured: np.ndarray,
    regularization: float,
) -> tuple[np.ndarray, float]:
    """Solve for q plus an unregularized additive common timing offset."""
    n_x = A.shape[1]
    D2 = second_difference_matrix(n_x)

    A_aug = np.column_stack((A, np.ones(A.shape[0])))
    D_aug = np.column_stack((D2, np.zeros(D2.shape[0])))

    lhs = A_aug.T @ A_aug + regularization * (D_aug.T @ D_aug)
    rhs = A_aug.T @ measured
    solution = np.linalg.solve(lhs, rhs)

    q_hat = solution[:-1]
    common_hat = float(solution[-1])
    return q_hat, common_hat


def rms_relative_error(estimate: np.ndarray, truth: np.ndarray) -> float:
    return float(np.sqrt(np.mean(((estimate - truth) / truth) ** 2)))


def main() -> None:
    x, dx = build_grid()
    v_true = true_velocity(x)
    q_true = 1.0 / v_true

    energies = np.linspace(1.08, 1.95, N_E)
    A = build_forward_matrix(x, dx, energies)

    intrinsic = A @ q_true

    # Noiseless consistency check: the inverse should recover the synthetic
    # profile to high accuracy with only weak smoothness regularization.
    noiseless = intrinsic + COMMON_DELAY
    q0, c0 = solve_regularized(A, noiseless, regularization=1.0e-5)
    assert np.all(q0 > 0.0)
    v0 = 1.0 / q0
    err0 = rms_relative_error(v0, v_true)
    assert err0 < 5.0e-3
    assert abs(c0 - COMMON_DELAY) < 5.0e-4

    # Add timing noise at 0.1% of the intrinsic spectral timing dynamic range.
    rng = np.random.default_rng(SEED)
    sigma = NOISE_FRACTION * np.ptp(intrinsic)
    measured = intrinsic + COMMON_DELAY + rng.normal(0.0, sigma, size=N_E)

    q_hat, c_hat = solve_regularized(A, measured, REGULARIZATION)
    assert np.all(q_hat > 0.0)
    v_hat = 1.0 / q_hat

    err = rms_relative_error(v_hat, v_true)
    assert err < 0.03
    assert abs(c_hat - COMMON_DELAY) < 0.005

    # The localized slow region should be recovered to within two spatial cells.
    i_true = int(np.argmin(v_true))
    i_hat = int(np.argmin(v_hat))
    assert abs(i_hat - i_true) <= 2

    print("PASS: synthetic spectral timing linear inversion")
    print(f"noiseless velocity RMS relative error = {err0:.6%}")
    print(f"noisy velocity RMS relative error = {err:.6%}")
    print(f"true common delay = {COMMON_DELAY:.6f}")
    print(f"recovered common delay = {c_hat:.6f}")
    print(f"true slow-region x = {x[i_true]:.6f}")
    print(f"recovered slow-region x = {x[i_hat]:.6f}")
    print(f"timing-noise sigma = {sigma:.6e}")


if __name__ == "__main__":
    main()
