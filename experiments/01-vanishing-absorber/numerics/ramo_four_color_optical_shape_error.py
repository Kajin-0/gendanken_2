"""Low-gamma optical-shape error of the Ramo four-color current closure.

For four source kernels with equally spaced mean generation coordinates
mu_m=mu0+m h, define the planar homogeneous raw-current response (common factors
removed)

    J_m = 1 - E_m[exp(-gamma D)].

Let the centered variance of kernel m be v_m.  The logarithmic first-difference
closure is

    C4 = 2 log(J2-J1) - log(J1-J0) - log(J3-J2).

A centered-moment expansion predicts

    C4 = gamma * Delta^3(v)/(2 h) + O(gamma^2),

where Delta^3(v)=v3-3 v2+3 v1-v0.

Thus constant, linear, and quadratic variance evolution have no O(gamma)
contamination.  This regression uses exact Gaussian kernels, for which the
source transform is analytic, and verifies the asymptotic coefficient.
"""

from __future__ import annotations

import numpy as np


H = 1.0
MU = np.arange(4, dtype=float) * H


def J_gaussian(mu: float, variance: float, gamma: complex) -> complex:
    transform = np.exp(-gamma * mu + 0.5 * gamma * gamma * variance)
    return 1.0 - transform


def closure(variances: np.ndarray, gamma: complex) -> complex:
    J = np.asarray(
        [J_gaussian(mu, var, gamma) for mu, var in zip(MU, variances)]
    )
    d = np.diff(J)
    return complex(2.0 * np.log(d[1]) - np.log(d[0]) - np.log(d[2]))


def third_difference(v: np.ndarray) -> float:
    return float(v[3] - 3.0 * v[2] + 3.0 * v[1] - v[0])


def main() -> None:
    families = {
        "constant": 0.20 + 0.0 * MU,
        "linear": 0.20 + 0.03 * MU,
        "quadratic": 0.20 + 0.01 * MU**2,
        "cubic": 0.20 + 0.002 * MU**3,
    }

    eps = 1.0e-4
    gamma = 1j * eps

    print("Ramo four-color optical shape-evolution asymptotics")
    for name, variances in families.items():
        C = closure(variances, gamma)
        predicted_linear = gamma * third_difference(variances) / (2.0 * H)
        print(
            f"{name:9s}: C={C.real:+.3e}{C.imag:+.3e}j, "
            f"linear prediction={predicted_linear.real:+.3e}"
            f"{predicted_linear.imag:+.3e}j"
        )

        if name in ("constant", "linear"):
            assert abs(C) < 2.0e-11
        elif name == "quadratic":
            # No O(gamma) term; residual starts at O(gamma^2).
            assert abs(C / gamma) < 2.0e-5
            assert abs(C) > 1.0e-11
        else:
            # Cubic variance has nonzero third difference and must reproduce the
            # linear coefficient as gamma -> 0.
            relative = abs((C - predicted_linear) / predicted_linear)
            assert relative < 3.0e-4

    print()
    print(
        "PASS: with equally spaced mean generation depths, the leading "
        "four-color Ramo optical-width error is proportional to the third "
        "discrete difference of source variance. Smooth variance evolution up "
        "through quadratic order is automatically absent at O(gamma)."
    )


if __name__ == "__main__":
    main()
