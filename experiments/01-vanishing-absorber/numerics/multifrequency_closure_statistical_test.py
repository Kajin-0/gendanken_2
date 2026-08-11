"""GLS significance test for multi-frequency real drift-diffusion closure.

At one depth, suppose N RF frequencies produce estimates

    theta_j = (D_app_j, w_app_j)

with an approximately Gaussian known covariance C. Under the local Markov null,
all theta_j share one common two-component value. Stack the 2N measurements and
fit the two common parameters by generalized least squares. The minimized
quadratic residual has asymptotic/linearized

    Q ~ chi-square_(2N-2)

under the null.

Under a fixed alternative with mean closure violation mu_perp, Q is noncentral
chi-square with noncentrality lambda = mu_perp^T C^-1 mu_perp.

This script records reference thresholds and verifies the equal-variance closed
form for three frequencies.
"""

from __future__ import annotations

import numpy as np
from scipy.stats import chi2, ncx2
from scipy.optimize import brentq


P_THREE_SIGMA = 0.9973


def gls_statistic(values: np.ndarray, covariance: np.ndarray):
    """values shape (N,2); covariance shape (2N,2N)."""
    n = values.shape[0]
    y = values.reshape(-1)
    X = np.tile(np.eye(2), (n, 1))
    precision = np.linalg.inv(covariance)
    fisher = X.T @ precision @ X
    theta = np.linalg.solve(fisher, X.T @ precision @ y)
    residual = y - X @ theta
    Q = float(residual @ precision @ residual)
    return Q, theta


def noncentrality(values_mean: np.ndarray, covariance: np.ndarray) -> float:
    Q, _ = gls_statistic(values_mean, covariance)
    return Q


def required_lambda(df: int, false_alarm_cdf: float, power: float) -> float:
    threshold = chi2.ppf(false_alarm_cdf, df)

    def objective(lam: float) -> float:
        return 1.0 - ncx2.cdf(threshold, df, lam) - power

    return float(brentq(objective, 0.0, 500.0))


def main() -> None:
    print("Multi-frequency local-Markov closure significance test")
    print()

    for n in (2, 3, 4):
        df = 2 * n - 2
        threshold = chi2.ppf(P_THREE_SIGMA, df)
        lam90 = required_lambda(df, P_THREE_SIGMA, 0.90)
        print(
            f"N={n} frequencies: df={df}, "
            f"3-sigma-like Q threshold={threshold:.6f}, "
            f"lambda for 90% power={lam90:.6f} "
            f"(sqrt lambda={np.sqrt(lam90):.6f})"
        )

    # Equal independent coefficient errors, three frequencies.
    sigma_D = 0.010
    sigma_w = 0.020
    covariance = np.diag(
        [sigma_D**2, sigma_w**2] * 3
    )

    # Symmetric D-only dispersion: D0-Delta, D0, D0+Delta; w constant.
    D0 = 0.08
    w0 = 1.55
    Delta = 0.03
    mean_alt = np.asarray(
        (
            (D0 - Delta, w0),
            (D0, w0),
            (D0 + Delta, w0),
        )
    )
    Q_alt, theta_fit = gls_statistic(mean_alt, covariance)
    closed_form = 2.0 * (Delta / sigma_D) ** 2

    print()
    print("three-frequency equal-variance example")
    print(f"  fitted common D,w = {theta_fit[0]:.6f}, {theta_fit[1]:.6f}")
    print(f"  GLS noncentrality/Q(mean alternative) = {Q_alt:.6f}")
    print(f"  closed form 2(Delta/sigma_D)^2 = {closed_form:.6f}")

    assert abs(Q_alt - closed_form) < 2.0e-12

    df3 = 4
    q3 = chi2.ppf(P_THREE_SIGMA, df3)
    lam90_3 = required_lambda(df3, P_THREE_SIGMA, 0.90)
    assert 16.24 < q3 < 16.27
    assert 24.74 < lam90_3 < 24.77

    # For the symmetric D-only pattern lambda=2(Delta/sigma)^2.
    Delta_over_sigma_for_90 = np.sqrt(lam90_3 / 2.0)
    print(
        "  symmetric D-only half-span Delta/sigma needed for 90% power "
        f"at the 3-sigma-like threshold = {Delta_over_sigma_for_90:.6f}"
    )

    print()
    print(
        "PASS: after covariance propagation, multi-frequency closure becomes a "
        "standard overdetermined GLS hypothesis test with 2N-2 closure degrees "
        "of freedom. Its power is controlled by the covariance-whitened "
        "noncentrality of the true coefficient dispersion."
    )


if __name__ == "__main__":
    main()
