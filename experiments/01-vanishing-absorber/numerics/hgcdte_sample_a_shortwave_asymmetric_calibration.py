"""Asymmetric A/B smooth-mode calibration budget for short-wave contrast.

The earlier global short-wave design used one common prior width for all six
smooth nuisance modes. This script gives the first three A smooth modes a prior
sigma_A and the three B smooth modes a separate prior sigma_B, then solves the
same convex maximin fixed-time wavelength allocation.

The main question is whether excellent sample-B calibration alone can make the
A-localized anomaly identifiable, or whether the sample-A smooth baseline must
also be constrained tightly.

No real-device anomaly amplitude, covariance validation, or novelty claim.
"""

from __future__ import annotations

import numpy as np
from scipy.optimize import minimize

from hgcdte_sample_a_shortwave_calibration_prior import NOMINAL_SIGMA_PHASE_DEG
from hgcdte_sample_a_shortwave_two_band_design import (
    LAMBDA_GRID,
    TOTAL_TIME_UNITS,
    build_family,
)
from hgcdte_sample_a_shortwave_global_design import augmented_designs

N_PROFILE = 72
N_PARAMETER = 8


def solve_asymmetric(
    designs: np.ndarray,
    physical_rms: np.ndarray,
    sigma_a_deg: float,
    sigma_b_deg: float,
    initial_weights: np.ndarray | None = None,
):
    x = augmented_designs(designs)
    scale = TOTAL_TIME_UNITS / NOMINAL_SIGMA_PHASE_DEG**2

    prior = np.zeros((N_PARAMETER, N_PARAMETER))
    # Use a numerically large precision for the exact-known limit.
    prior[1:4, 1:4] = (
        np.eye(3) / sigma_a_deg**2
        if sigma_a_deg > 0.0
        else np.eye(3) * 1.0e18
    )
    prior[4:7, 4:7] = (
        np.eye(3) / sigma_b_deg**2
        if sigma_b_deg > 0.0
        else np.eye(3) * 1.0e18
    )

    e0 = np.zeros(N_PARAMETER)
    e0[0] = 1.0

    def evaluate(weights: np.ndarray):
        fisher = (
            scale * np.einsum("i,pia,pib->pab", weights, x, x)
            + prior[None, :, :]
        )
        rhs = np.broadcast_to(e0, (N_PROFILE, N_PARAMETER))[..., None]
        z = np.linalg.solve(fisher, rhs)[..., 0]
        g = z[:, 0] / physical_rms**2
        projection = np.einsum("pia,pa->pi", x, z)
        grad_g = -scale * projection**2 / physical_rms[:, None] ** 2
        return g, grad_g

    if initial_weights is None:
        weights0 = np.full(len(LAMBDA_GRID), 1.0 / len(LAMBDA_GRID))
    else:
        weights0 = np.asarray(initial_weights, dtype=float).copy()
        weights0 /= np.sum(weights0)

    g0, _ = evaluate(weights0)
    y0 = np.concatenate((weights0, [1.01 * np.max(g0)]))

    def objective(y):
        return float(y[-1])

    def objective_jac(y):
        grad = np.zeros_like(y)
        grad[-1] = 1.0
        return grad

    def equality(y):
        return float(np.sum(y[:-1]) - 1.0)

    def equality_jac(y):
        grad = np.zeros_like(y)
        grad[:-1] = 1.0
        return grad

    def inequalities(y):
        g, _ = evaluate(y[:-1])
        return y[-1] - g

    def inequalities_jac(y):
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
            {"type": "ineq", "fun": inequalities, "jac": inequalities_jac},
        ],
        options={"maxiter": 1800, "ftol": 1.0e-10, "disp": False},
    )

    if not result.success:
        raise RuntimeError(result.message)

    weights = result.x[:-1]
    g, _ = evaluate(weights)
    snr = 1.0 / np.sqrt(g)
    return weights, snr


def one_side_threshold(
    designs: np.ndarray,
    physical_rms: np.ndarray,
    side: str,
) -> float:
    low = 0.006
    high = 0.009
    initial = None

    for _ in range(11):
        mid = 0.5 * (low + high)
        if side == "A":
            weights, snr = solve_asymmetric(
                designs, physical_rms, mid, 0.0, initial
            )
        else:
            weights, snr = solve_asymmetric(
                designs, physical_rms, 0.0, mid, initial
            )
        initial = weights
        if np.min(snr) >= 3.0:
            low = mid
        else:
            high = mid
    return low


def main() -> None:
    designs, physical_rms = build_family()

    cases = (
        (0.000, 0.010),
        (0.010, 0.000),
        (0.005, 0.005),
        (0.005, 0.010),
        (0.010, 0.005),
    )

    print("Asymmetric short-wave A/B smooth-mode calibration")
    for sigma_a, sigma_b in cases:
        weights, snr = solve_asymmetric(
            designs, physical_rms, sigma_a, sigma_b
        )
        support = [
            (float(LAMBDA_GRID[i]), float(weights[i]))
            for i in np.where(weights > 1.0e-4)[0]
        ]
        print(
            f"sigma_A={sigma_a:.3f}, sigma_B={sigma_b:.3f} deg: "
            f"SNR min/median={np.min(snr):.6f}/{np.median(snr):.6f}; "
            f"fraction>=3={np.mean(snr >= 3.0):.3f}"
        )
        print(f"  support={support}")

    sigma_a_axis = one_side_threshold(designs, physical_rms, "A")
    sigma_b_axis = one_side_threshold(designs, physical_rms, "B")
    sigma_equal_ellipse = 1.0 / np.sqrt(
        1.0 / sigma_a_axis**2 + 1.0 / sigma_b_axis**2
    )

    print()
    print(f"A-only prior axis (B known): {sigma_a_axis:.6f} deg")
    print(f"B-only prior axis (A known): {sigma_b_axis:.6f} deg")
    print(
        "equal-prior value implied by ellipse: "
        f"{sigma_equal_ellipse:.6f} deg"
    )
    print(
        "approximate robust boundary: "
        f"(sigma_A/{sigma_a_axis:.6f})^2 + "
        f"(sigma_B/{sigma_b_axis:.6f})^2 <= 1"
    )

    # Regression anchors.
    _, s_b_loose = solve_asymmetric(designs, physical_rms, 0.0, 0.010)
    _, s_a_loose = solve_asymmetric(designs, physical_rms, 0.010, 0.0)
    _, s_equal = solve_asymmetric(designs, physical_rms, 0.005, 0.005)

    assert 2.528 < np.min(s_b_loose) < 2.530
    assert 2.501 < np.min(s_a_loose) < 2.503
    assert 3.0926 < np.min(s_equal) < 3.0929

    assert 0.00739 < sigma_a_axis < 0.00740
    assert 0.00756 < sigma_b_axis < 0.00758
    assert 0.00527 < sigma_equal_ellipse < 0.00530

    print()
    print(
        "PASS: neither a perfectly calibrated B with a 0.010-deg A baseline "
        "nor a perfectly calibrated A baseline with a 0.010-deg B control can "
        "guarantee 3 sigma. Both sides must be constrained. The fixed-time "
        "3-sigma trade space is well summarized by an approximately elliptical "
        "A/B phase-equivalent calibration budget, with equal priors near the "
        "previous ~0.00528-deg global threshold."
    )


if __name__ == "__main__":
    main()
