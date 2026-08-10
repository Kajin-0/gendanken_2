"""Global fixed-time wavelength allocation for short-wave sample-A contrast.

This extends hgcdte_sample_a_shortwave_two_band_design.py by allowing arbitrary
nonnegative time weights across all 81 wavelengths in 2.00-2.80 um.

For each sample-A profile p, the normalized spectral design contains

    anomaly + 3 smooth A modes + 3 smooth B modes + common phase intercept.

The six smooth modes receive independent Gaussian phase-equivalent priors. The
common phase and anomaly are unregularized. With total time fixed, the Fisher
matrix is affine in wavelength weights w_i:

    F_p(w) = T/sigma0^2 * sum_i w_i x_pi x_pi^T + P.

The normalized anomaly variance

    g_p(w) = e0^T F_p(w)^(-1) e0 / A_p^2

is convex in w. Therefore minimizing max_p g_p(w) over the wavelength simplex
is a convex maximin design problem. It is solved in epigraph form with analytic
gradients using SLSQP.

No real-device anomaly amplitude, covariance validation, or novelty claim.
"""

from __future__ import annotations

import numpy as np
from scipy.optimize import minimize

from hgcdte_sample_a_shortwave_calibration_prior import (
    NOMINAL_SIGMA_PHASE_DEG,
)
from hgcdte_sample_a_shortwave_two_band_design import (
    LAMBDA_GRID,
    TOTAL_TIME_UNITS,
    build_family,
    exhaustive_best_pair,
)

N_PROFILE = 72
N_PARAMETER = 8  # anomaly + 6 smooth nuisances + common phase
GLOBAL_PRIORS_DEG = (0.002, 0.005, 0.006, 0.008, 0.010)


def augmented_designs(designs: np.ndarray) -> np.ndarray:
    ones = np.ones((designs.shape[0], designs.shape[1], 1))
    return np.concatenate((designs, ones), axis=2)


def solve_global_design(
    designs: np.ndarray,
    physical_rms: np.ndarray,
    nuisance_prior_deg: float,
    initial_weights: np.ndarray | None = None,
):
    """Solve the convex maximin wavelength-time allocation problem."""
    x = augmented_designs(designs)
    information_scale = TOTAL_TIME_UNITS / NOMINAL_SIGMA_PHASE_DEG**2

    prior_information = np.zeros((N_PARAMETER, N_PARAMETER))
    prior_information[1:7, 1:7] = (
        np.eye(6) / nuisance_prior_deg**2
    )

    e0 = np.zeros(N_PARAMETER)
    e0[0] = 1.0

    def evaluate(weights: np.ndarray):
        fisher = (
            information_scale
            * np.einsum("i,pia,pib->pab", weights, x, x)
            + prior_information[None, :, :]
        )

        rhs = np.broadcast_to(e0, (N_PROFILE, N_PARAMETER))[..., None]
        z = np.linalg.solve(fisher, rhs)[..., 0]

        variance = z[:, 0]
        inverse_snr2 = variance / physical_rms**2

        # d[e0^T F^-1 e0]/dw_i
        # = -T/sigma0^2 * (x_i^T F^-1 e0)^2.
        projection = np.einsum("pia,pa->pi", x, z)
        gradient = (
            -information_scale
            * projection**2
            / physical_rms[:, None] ** 2
        )
        return inverse_snr2, gradient

    if initial_weights is None:
        weights0 = np.full(len(LAMBDA_GRID), 1.0 / len(LAMBDA_GRID))
    else:
        weights0 = np.asarray(initial_weights, dtype=float).copy()
        weights0 /= np.sum(weights0)

    g0, _ = evaluate(weights0)
    y0 = np.concatenate((weights0, [1.01 * np.max(g0)]))

    def objective(y: np.ndarray) -> float:
        return float(y[-1])

    def objective_jac(y: np.ndarray) -> np.ndarray:
        grad = np.zeros_like(y)
        grad[-1] = 1.0
        return grad

    def equality(y: np.ndarray) -> float:
        return float(np.sum(y[:-1]) - 1.0)

    def equality_jac(y: np.ndarray) -> np.ndarray:
        grad = np.zeros_like(y)
        grad[:-1] = 1.0
        return grad

    def inequalities(y: np.ndarray) -> np.ndarray:
        g, _ = evaluate(y[:-1])
        return y[-1] - g

    def inequalities_jac(y: np.ndarray) -> np.ndarray:
        _, grad_g = evaluate(y[:-1])
        jac = np.empty((N_PROFILE, len(LAMBDA_GRID) + 1))
        jac[:, :-1] = -grad_g
        jac[:, -1] = 1.0
        return jac

    result = minimize(
        objective,
        y0,
        jac=objective_jac,
        method="SLSQP",
        bounds=[(0.0, 1.0)] * len(LAMBDA_GRID) + [(0.0, None)],
        constraints=[
            {"type": "eq", "fun": equality, "jac": equality_jac},
            {
                "type": "ineq",
                "fun": inequalities,
                "jac": inequalities_jac,
            },
        ],
        options={"maxiter": 2000, "ftol": 1.0e-10, "disp": False},
    )

    weights = result.x[:-1]
    g, _ = evaluate(weights)
    snr = 1.0 / np.sqrt(g)
    return result, weights, snr


def summarize_support(weights: np.ndarray, threshold: float = 1.0e-4):
    indices = np.where(weights > threshold)[0]
    return [(float(LAMBDA_GRID[i]), float(weights[i])) for i in indices]


def cluster_metrics(weights: np.ndarray):
    """Summarize lower/upper short-wave clusters around the observed gap."""
    low = LAMBDA_GRID <= 2.20
    high = LAMBDA_GRID >= 2.60

    low_weight = float(np.sum(weights[low]))
    high_weight = float(np.sum(weights[high]))

    low_center = float(
        np.sum(weights[low] * LAMBDA_GRID[low]) / low_weight
    )
    high_center = float(
        np.sum(weights[high] * LAMBDA_GRID[high]) / high_weight
    )
    return low_weight, low_center, high_weight, high_center


def global_prior_threshold(
    designs: np.ndarray,
    physical_rms: np.ndarray,
) -> float:
    low = 0.005
    high = 0.006
    initial = None

    for _ in range(12):
        mid = 0.5 * (low + high)
        result, weights, snr = solve_global_design(
            designs,
            physical_rms,
            mid,
            initial_weights=initial,
        )
        if not result.success:
            raise RuntimeError(result.message)
        initial = weights
        if np.min(snr) >= 3.0:
            low = mid
        else:
            high = mid

    return low


def main() -> None:
    designs, physical_rms = build_family()
    assert designs.shape == (72, 81, 7)

    print("Global short-wave fixed-time design")
    print(
        f"grid = {LAMBDA_GRID[0]:.2f}-{LAMBDA_GRID[-1]:.2f} um, "
        f"N={len(LAMBDA_GRID)}"
    )
    print(f"total time = {TOTAL_TIME_UNITS:.0f} dense-point units")
    print()

    stored = {}
    for prior in GLOBAL_PRIORS_DEG:
        result, weights, snr = solve_global_design(
            designs,
            physical_rms,
            prior,
        )
        if not result.success:
            raise RuntimeError(result.message)

        stored[prior] = (weights, snr)
        low_w, low_c, high_w, high_c = cluster_metrics(weights)

        pair = exhaustive_best_pair(designs, physical_rms, prior)
        pair_worst = pair[0]
        relative_gain = 100.0 * (np.min(snr) / pair_worst - 1.0)

        print(f"prior={prior:.3f} deg")
        print(
            f"  global SNR min/median/max = {np.min(snr):.6f}/"
            f"{np.median(snr):.6f}/{np.max(snr):.6f}"
        )
        print(f"  active support = {summarize_support(weights)}")
        print(
            f"  lower cluster: time={low_w:.6f}, center={low_c:.6f} um"
        )
        print(
            f"  upper cluster: time={high_w:.6f}, center={high_c:.6f} um"
        )
        print(
            f"  improvement over exhaustive best pair = {relative_gain:.6f}%"
        )
        print()

    threshold = global_prior_threshold(designs, physical_rms)
    print(
        "global arbitrary-support prior threshold for worst-case >=3 sigma: "
        f"~{threshold:.6f} deg"
    )

    # Stable numerical regressions.
    w002, s002 = stored[0.002]
    assert 4.23 < np.min(s002) < 4.24
    assert abs(np.sum(w002[LAMBDA_GRID == 2.00]) - 0.5) < 1.0e-4
    assert abs(np.sum(w002[(LAMBDA_GRID > 2.719) & (LAMBDA_GRID < 2.721)]) - 0.5) < 1.0e-4

    w005, s005 = stored[0.005]
    assert 3.0926 < np.min(s005) < 3.0929
    low_w, _, high_w, high_c = cluster_metrics(w005)
    assert abs(low_w - 0.5) < 2.0e-4
    assert abs(high_w - 0.5) < 2.0e-4
    assert 2.687 < high_c < 2.690

    w010, s010 = stored[0.010]
    assert 1.9590 < np.min(s010) < 1.9596
    low_w, low_c, high_w, high_c = cluster_metrics(w010)
    assert abs(low_w - 0.5) < 5.0e-4
    assert abs(high_w - 0.5) < 5.0e-4
    assert 2.04 < low_c < 2.06
    assert 2.687 < high_c < 2.690

    assert 0.00527 < threshold < 0.00529

    print()
    print(
        "PASS: the convex arbitrary-support optimization confirms that the "
        "short-wave fixed-time design effectively collapses into two spectral "
        "clusters. At a 0.005-deg smooth-mode prior the simple 2.00/2.69-um "
        "pair is already essentially globally optimal. At 0.010 deg, even the "
        "global allocation remains below 2 sigma worst case, so adding more "
        "wavelengths cannot rescue inadequate smooth-mode calibration at the "
        "same total measurement time."
    )


if __name__ == "__main__":
    main()
