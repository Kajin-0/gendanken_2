"""Universal cumulant nulls for homogeneous 1-D drift-diffusion first passage.

For conditioned uniform drift w>0, diffusion D>0, and travel distance d>0,

    F_d(s)=exp[-d phi(s)],
    phi(s)=(sqrt(w^2+4Ds)-w)/(2D).

The successful transit-time distribution is inverse Gaussian. Its cumulants are

    kappa_n=(2n-3)!! (2D)^(n-1) d / w^(2n-1), n>=1,

where (-1)!!=1.

Consequences independent of D,w,d:

    kappa_{n+1} kappa_{n-1}/kappa_n^2=(2n-1)/(2n-3), n>=2.

In particular

    kappa3*kappa1/kappa2^2 = 3,
    kappa4*kappa2/kappa3^2 = 5/3,
    skewness = 3*CV,
    excess kurtosis = 15*CV^2 = (5/3)*skewness^2.

Uniform Markov recombination before DC conditioning only replaces physical drift
v by conditioned drift w=sqrt(v^2+4D kappa); all parameter-free ratios survive.
"""

from __future__ import annotations

import math
import numpy as np


def odd_double_factorial(m: int) -> int:
    if m <= 0:
        return 1
    out = 1
    for value in range(1, m + 1, 2):
        out *= value
    return out


def cumulant(n: int, D: float, w: float, d: float) -> float:
    return (
        odd_double_factorial(2 * n - 3)
        * (2.0 * D) ** (n - 1)
        * d
        / w ** (2 * n - 1)
    )


def main() -> None:
    parameter_sets = (
        (0.20, 1.0e5, 2.0e-6),
        (0.035, 3.2e4, 6.0e-6),
        (0.80, 2.5e5, 0.7e-6),
    )

    print("Homogeneous drift-diffusion first-passage cumulant nulls")

    for D, w, d in parameter_sets:
        k = {n: cumulant(n, D, w, d) for n in range(1, 7)}
        cv = math.sqrt(k[2]) / k[1]
        skew = k[3] / k[2] ** 1.5
        excess = k[4] / k[2] ** 2

        print(f"D={D:.6g}, w={w:.6g}, d={d:.6g}")
        print(f"  CV={cv:.9e}, skew={skew:.9e}, excess={excess:.9e}")
        print(f"  skew/(3 CV)={skew/(3*cv):.12f}")
        print(f"  excess/(15 CV^2)={excess/(15*cv**2):.12f}")

        assert abs(skew / (3.0 * cv) - 1.0) < 2.0e-14
        assert abs(excess / (15.0 * cv**2) - 1.0) < 2.0e-14
        assert abs(excess / skew**2 - 5.0 / 3.0) < 2.0e-14

        for n in range(2, 6):
            ratio = k[n + 1] * k[n - 1] / k[n] ** 2
            target = (2.0 * n - 1.0) / (2.0 * n - 3.0)
            assert abs(ratio - target) < 3.0e-14

    # Uniform recombination changes only the conditioned drift.
    D = 0.20
    v = 1.0e5
    kill = 4.0e8
    w_cond = math.sqrt(v * v + 4.0 * D * kill)
    d = 3.0e-6
    k = {n: cumulant(n, D, w_cond, d) for n in range(1, 5)}
    ratio_recombined = k[4] * k[2] / k[3] ** 2

    print()
    print("uniform-recombination conditioned example")
    print(f"  physical v={v:.6g}, kill={kill:.6g}, conditioned w={w_cond:.6g}")
    print(f"  kappa4*kappa2/kappa3^2={ratio_recombined:.12f}")
    assert abs(ratio_recombined - 5.0 / 3.0) < 2.0e-14

    print()
    print(
        "PASS: the entire inverse-Gaussian first-passage cumulant ratio "
        "hierarchy is parameter-free. Uniform recombination changes the "
        "conditioned drift scale but not these normalized timing nulls."
    )


if __name__ == "__main__":
    main()
