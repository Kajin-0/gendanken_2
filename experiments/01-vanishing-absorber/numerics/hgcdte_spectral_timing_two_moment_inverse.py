"""Synthetic two-moment inversion for graded-HgCdTe spectral timing.

This is not a calibrated HgCdTe model.

The test creates separate spatial regions for
- slow mean transport q1(x)=1/v(x), and
- enhanced timing broadening q2(x).

Finite wavelength-dependent generation kernels are used.  Mean timing and
variance data include independent wavelength-independent nuisance offsets plus
measurement noise.  The regression verifies that the two profiles can be
recovered separately in a controlled case.
"""

from __future__ import annotations

import numpy as np


L = 1.0
EG_IN = 2.0
EG_OUT = 1.0
G = 1.0
BETA = 0.5
N_EDGE = BETA + 1.0
ELL_ALPHA = 0.06

N_X = 60
N_E = 90
COMMON_MEAN = 0.12
COMMON_VAR = 0.01
MEAN_NOISE_FRACTION = 1.0e-3
VAR_NOISE_FRACTION = 2.0e-3
LAMBDA_Q1 = 0.10
LAMBDA_Q2 = 0.01
SEED = 20260809


def grids() -> tuple[np.ndarray, np.ndarray, float]:
    dx = L / N_X
    x = (np.arange(N_X) + 0.5) * dx
    energies = np.linspace(1.08, 1.95, N_E)
    return x, energies, dx


def generation_probabilities(energies: np.ndarray) -> np.ndarray:
    """Cell absorption probabilities conditioned on absorption."""
    edges = np.linspace(0.0, L, N_X + 1)
    P = np.zeros((energies.size, N_X))

    for i, e_gamma in enumerate(energies):
        xg = (EG_IN - e_gamma) / G
        d = L - xg
        tau = (d / ELL_ALPHA) ** N_EDGE
        norm = 1.0 - np.exp(-tau)

        cdf = np.zeros_like(edges)
        for k, s in enumerate(edges):
            if s <= xg:
                cdf[k] = 0.0
            else:
                z = s - xg
                y = min((z / ELL_ALPHA) ** N_EDGE, tau)
                cdf[k] = (1.0 - np.exp(-y)) / norm

        P[i] = np.diff(cdf)

    assert np.allclose(P.sum(axis=1), 1.0)
    return P


def cumulative_timing_matrix(P: np.ndarray, dx: float) -> np.ndarray:
    """A_ik = dx * Prob(generation cell <= k)."""
    return np.cumsum(P, axis=1) * dx


def second_difference_matrix(n: int) -> np.ndarray:
    D2 = np.zeros((n - 2, n))
    for i in range(n - 2):
        D2[i, i : i + 3] = (1.0, -2.0, 1.0)
    return D2


def solve_with_constant(A: np.ndarray, y: np.ndarray, lam: float) -> tuple[np.ndarray, float]:
    D2 = second_difference_matrix(A.shape[1])
    A_aug = np.column_stack((A, np.ones(A.shape[0])))
    D_aug = np.column_stack((D2, np.zeros(D2.shape[0])))

    lhs = A_aug.T @ A_aug + lam * (D_aug.T @ D_aug)
    rhs = A_aug.T @ y
    solution = np.linalg.solve(lhs, rhs)
    return solution[:-1], float(solution[-1])


def downstream_integral(profile: np.ndarray, dx: float) -> np.ndarray:
    return np.array([np.sum(profile[j:]) * dx for j in range(profile.size)])


def rms_relative_error(estimate: np.ndarray, truth: np.ndarray) -> float:
    return float(np.sqrt(np.mean(((estimate - truth) / truth) ** 2)))


def main() -> None:
    x, energies, dx = grids()
    P = generation_probabilities(energies)
    A = cumulative_timing_matrix(P, dx)

    # Mean-transport profile: a localized slow region near x=0.42.
    v_true = (
        0.9
        + 0.25 * x
        - 0.25 * np.exp(-0.5 * ((x - 0.42) / 0.07) ** 2)
    )
    q1_true = 1.0 / v_true

    # Broadening profile: deliberately place enhanced broadening elsewhere.
    q2_true = 0.05 + 0.10 * np.exp(-0.5 * ((x - 0.72) / 0.06) ** 2)

    mean_given_x = downstream_integral(q1_true, dx)
    var_given_x = downstream_integral(q2_true, dx)

    mu_true = P @ mean_given_x
    generation_var_true = P @ (mean_given_x**2) - mu_true**2
    variance_true = P @ var_given_x + generation_var_true

    # Algebraic consistency with the common cumulative kernel A.
    assert np.allclose(mu_true, A @ q1_true)
    assert np.allclose(P @ var_given_x, A @ q2_true)

    rng = np.random.default_rng(SEED)

    sigma_mean = MEAN_NOISE_FRACTION * np.ptp(mu_true)
    mu_meas = mu_true + COMMON_MEAN + rng.normal(0.0, sigma_mean, N_E)

    q1_hat, c1_hat = solve_with_constant(A, mu_meas, LAMBDA_Q1)
    assert np.all(q1_hat > 0.0)
    v_hat = 1.0 / q1_hat

    # Recompute generation-position variance from the reconstructed first moment.
    mean_given_x_hat = downstream_integral(q1_hat, dx)
    mu_intrinsic_hat = P @ mean_given_x_hat
    generation_var_hat = P @ (mean_given_x_hat**2) - mu_intrinsic_hat**2

    sigma_var = VAR_NOISE_FRACTION * np.ptp(variance_true)
    var_meas = variance_true + COMMON_VAR + rng.normal(0.0, sigma_var, N_E)

    corrected_second_data = var_meas - generation_var_hat
    q2_hat, c2_hat = solve_with_constant(A, corrected_second_data, LAMBDA_Q2)
    assert np.all(q2_hat > 0.0)

    v_error = rms_relative_error(v_hat, v_true)
    q2_error = rms_relative_error(q2_hat, q2_true)

    # Mean profile should be easier than second-moment profile.
    assert v_error < 0.03
    assert q2_error < 0.10

    # Recover the two deliberately separated anomalies at different positions.
    slow_true = int(np.argmin(v_true))
    slow_hat = int(np.argmin(v_hat))
    broad_true = int(np.argmax(q2_true))
    broad_hat = int(np.argmax(q2_hat))

    assert abs(slow_hat - slow_true) <= 2
    assert abs(broad_hat - broad_true) <= 2
    assert abs(slow_true - broad_true) > 8

    assert abs(c1_hat - COMMON_MEAN) < 0.005
    assert abs(c2_hat - COMMON_VAR) < 0.004

    print("PASS: synthetic two-moment spectral timing inversion")
    print(f"velocity RMS relative error = {v_error:.4%}")
    print(f"q2 RMS relative error = {q2_error:.4%}")
    print(f"slow region true/recovered x = {x[slow_true]:.4f}/{x[slow_hat]:.4f}")
    print(f"broad region true/recovered x = {x[broad_true]:.4f}/{x[broad_hat]:.4f}")
    print(f"common mean delay true/recovered = {COMMON_MEAN:.5f}/{c1_hat:.5f}")
    print(f"common variance true/recovered = {COMMON_VAR:.5f}/{c2_hat:.5f}")


if __name__ == "__main__":
    main()
