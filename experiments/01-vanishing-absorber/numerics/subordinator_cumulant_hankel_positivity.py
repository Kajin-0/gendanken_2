"""Cumulant Hankel positivity for homogeneous regenerative first passage.

For a timing subordinator with distance d and Levy measure nu(dt), finite
cumulants n>=2 satisfy

    kappa_n = d * integral t^n nu(dt).

Thus [kappa_{i+j+2}] is a Gram/Hankel moment matrix and must be PSD. In
particular

    kappa_n^2 <= kappa_{n-1} kappa_{n+1},

with the n=2 inequality also valid when deterministic drift contributes to
kappa1 because that only increases kappa1.

Observable consequences:

    skewness >= CV,
    excess kurtosis >= skewness^2.

The script checks the hierarchy for a compound-Poisson-plus-drift subordinator
and contrasts the sharper inverse-Gaussian drift-diffusion ratios.
"""

from __future__ import annotations

import numpy as np


DISTANCE = 2.3
DRIFT_TIME_PER_DISTANCE = 0.40
POISSON_RATE_PER_DISTANCE = 1.7

# Positive jump-time distribution in the Levy measure.
JUMP_T = np.asarray((0.15, 0.7, 1.8, 3.0), dtype=float)
JUMP_P = np.asarray((0.25, 0.35, 0.30, 0.10), dtype=float)
JUMP_P /= np.sum(JUMP_P)


def compound_poisson_cumulants(max_n: int) -> dict[int, float]:
    out: dict[int, float] = {}
    jump_moments = {
        n: float(np.sum(JUMP_P * JUMP_T**n)) for n in range(1, max_n + 1)
    }
    out[1] = DISTANCE * (
        DRIFT_TIME_PER_DISTANCE
        + POISSON_RATE_PER_DISTANCE * jump_moments[1]
    )
    for n in range(2, max_n + 1):
        out[n] = DISTANCE * POISSON_RATE_PER_DISTANCE * jump_moments[n]
    return out


def hankel_from_cumulants(kappa: dict[int, float], size: int) -> np.ndarray:
    return np.asarray(
        [[kappa[i + j + 2] for j in range(size)] for i in range(size)],
        dtype=float,
    )


def inverse_gaussian_cumulants(D: float, w: float, d: float, max_n: int):
    def odd_df(m: int) -> int:
        if m <= 0:
            return 1
        out = 1
        for value in range(1, m + 1, 2):
            out *= value
        return out

    return {
        n: odd_df(2 * n - 3) * (2.0 * D) ** (n - 1) * d / w ** (2 * n - 1)
        for n in range(1, max_n + 1)
    }


def standardized(kappa: dict[int, float]):
    cv = np.sqrt(kappa[2]) / kappa[1]
    skew = kappa[3] / kappa[2] ** 1.5
    excess = kappa[4] / kappa[2] ** 2
    return float(cv), float(skew), float(excess)


def main() -> None:
    k = compound_poisson_cumulants(8)
    cv, skew, excess = standardized(k)

    print("Subordinator cumulant Hankel positivity")
    print("compound-Poisson + deterministic-drift example")
    print(f"  CV={cv:.9f}, skew={skew:.9f}, excess={excess:.9f}")
    print(f"  skew/CV={skew/cv:.9f}  (must be >=1)")
    print(f"  excess/skew^2={excess/skew**2:.9f}  (must be >=1)")

    assert skew >= cv
    assert excess >= skew**2

    for n in range(2, 7):
        margin = k[n - 1] * k[n + 1] - k[n] ** 2
        print(f"  log-convex margin n={n}: {margin:.9e}")
        assert margin >= -1.0e-13

    for size in (2, 3, 4):
        H = hankel_from_cumulants(k, size)
        eig = np.linalg.eigvalsh(H)
        print(f"  cumulant Hankel size {size}: min eigenvalue={eig.min():.9e}")
        assert eig.min() > -1.0e-12

    # Sharper inverse-Gaussian / drift-diffusion benchmark.
    kig = inverse_gaussian_cumulants(0.20, 1.0e5, 2.0e-6, 6)
    cv_ig, skew_ig, excess_ig = standardized(kig)
    print()
    print("uniform drift-diffusion inverse-Gaussian benchmark")
    print(f"  skew/CV={skew_ig/cv_ig:.12f}  target 3")
    print(f"  excess/skew^2={excess_ig/skew_ig**2:.12f}  target 5/3")
    assert abs(skew_ig / cv_ig - 3.0) < 2.0e-14
    assert abs(excess_ig / skew_ig**2 - 5.0 / 3.0) < 2.0e-14

    print()
    print(
        "PASS: homogeneous regenerative timing gives a positive Hankel moment "
        "hierarchy for higher cumulants. Drift-diffusion occupies a much "
        "smaller subset with exact stronger cumulant ratios."
    )


if __name__ == "__main__":
    main()
