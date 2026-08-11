"""Cumulant-ratio interpretation as breadth of the spatial Levy delay spectrum.

For a homogeneous regenerative timing subordinator, n>=2 cumulants per distance
are moments m_n=int t^n nu(dt). Define

    R_n = kappa_{n+1} kappa_{n-1}/kappa_n^2
        = m_{n+1} m_{n-1}/m_n^2.

Under the normalized tilted measure

    P_{n-1}(dt) = t^(n-1) nu(dt)/m_{n-1},

R_n = E[t^2]/E[t]^2 = 1 + CV_tilted^2.

Examples:
- fixed-size Poisson waiting jumps: R_n=1;
- exponential waiting jumps: R_n=(n+1)/n;
- inverse-Gaussian drift-diffusion first passage:
  R_n=(2n-1)/(2n-3).

The script verifies these and shows how a two-scale delay spectrum can produce a
much larger R_3.
"""

from __future__ import annotations

import math
import numpy as np


def ratio_from_moments(moment, n: int) -> float:
    return moment(n - 1) * moment(n + 1) / moment(n) ** 2


def fixed_jump_moment(n: int, rate: float = 2.0, tau: float = 1.7) -> float:
    return rate * tau**n


def exponential_jump_moment(n: int, rate: float = 2.0, beta: float = 1.7) -> float:
    return rate * math.factorial(n) / beta**n


def dd_moment(n: int, D: float = 0.3, w: float = 1.4) -> float:
    def odd_df(m: int) -> int:
        if m <= 0:
            return 1
        out = 1
        for value in range(1, m + 1, 2):
            out *= value
        return out

    return odd_df(2 * n - 3) * (2.0 * D) ** (n - 1) / w ** (2 * n - 1)


def discrete_moment(times: np.ndarray, weights: np.ndarray, n: int) -> float:
    return float(np.sum(weights * times**n))


def main() -> None:
    print("Cumulant ratio as Levy-delay-spectrum breadth")

    for n in range(2, 6):
        r_fixed = ratio_from_moments(fixed_jump_moment, n)
        r_exp = ratio_from_moments(exponential_jump_moment, n)
        r_dd = ratio_from_moments(dd_moment, n)

        print(
            f"n={n}: fixed={r_fixed:.12f}, "
            f"exponential={r_exp:.12f}, DD={r_dd:.12f}"
        )

        assert abs(r_fixed - 1.0) < 2.0e-14
        assert abs(r_exp - (n + 1.0) / n) < 2.0e-14
        assert abs(r_dd - (2.0 * n - 1.0) / (2.0 * n - 3.0)) < 3.0e-14

    # Explicitly verify R_n=1+CV^2 under the t^(n-1)-tilted positive measure.
    times = np.asarray((0.4, 1.0, 2.5, 7.0), dtype=float)
    weights = np.asarray((0.30, 0.25, 0.30, 0.15), dtype=float)
    n = 3

    moment = lambda k: discrete_moment(times, weights, k)
    R = ratio_from_moments(moment, n)

    tilted_weights = weights * times ** (n - 1)
    tilted_weights /= np.sum(tilted_weights)
    mean = float(np.sum(tilted_weights * times))
    variance = float(np.sum(tilted_weights * (times - mean) ** 2))
    cv2 = variance / mean**2

    print()
    print("multiscale discrete delay spectrum, n=3")
    print(f"  R_3={R:.12f}")
    print(f"  1+CV_tilted^2={1.0+cv2:.12f}")
    assert abs(R - (1.0 + cv2)) < 2.0e-14
    assert R > 1.5

    print()
    print(
        "PASS: adjacent cumulant ratios are exactly one plus the squared "
        "coefficient of variation of a moment-tilted Levy delay spectrum. They "
        "therefore quantify delay-scale breadth rather than being arbitrary "
        "shape constants."
    )


if __name__ == "__main__":
    main()
