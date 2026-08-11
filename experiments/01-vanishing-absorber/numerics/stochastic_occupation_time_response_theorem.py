"""Exact stochastic occupation-time response theorem regression.

No Markov, drift-diffusion, or deterministic-path assumption is used.

For arbitrary successful carrier trajectories with random transit time T and
spatial occupation density ell(z), introduce an ideal weak local clock-rate
perturbation with translated shape h. For a point feature of area A_h,

    T_epsilon = T + epsilon A_h ell(z0) + O(epsilon^2).

With

    H(omega)=E[exp(-i omega T)],

its first logarithmic response is

    S(z,omega)=d_epsilon ln H_epsilon|0
             =-i omega A_h E[e^-iomegaT ell(z)]/H.

Since integral ell(z) dz = T on every trajectory,

    integral S dz = A_h omega d_omega ln H

exactly.

At low frequency,

    S/(-i omega A_h)
      = E[ell(z)] - i omega Cov(T,ell(z)) + O(omega^2).

This script verifies the identities on an arbitrary finite ensemble of paths.
"""

from __future__ import annotations

import numpy as np


PROB = np.asarray((0.15, 0.25, 0.35, 0.25), dtype=float)
T = np.asarray((1.0, 1.8, 2.6, 4.2), dtype=float)

# Arbitrary occupation times in four spatial bins. Each row sums exactly to the
# corresponding trajectory transit time; no transport law is imposed.
ELL = np.asarray(
    (
        (0.15, 0.25, 0.30, 0.30),
        (0.40, 0.45, 0.50, 0.45),
        (0.20, 0.80, 0.90, 0.70),
        (0.70, 1.10, 1.30, 1.10),
    ),
    dtype=float,
)
A_H = 0.70


def response(omega: float):
    phase = np.exp(-1j * omega * T)
    H = complex(np.sum(PROB * phase))
    numerator = np.sum(PROB[:, None] * phase[:, None] * ELL, axis=0)
    rho = numerator / H
    S = -1j * omega * A_H * rho

    Hprime = complex(np.sum(PROB * (-1j * T) * phase))
    sum_rule_rhs = A_H * omega * Hprime / H
    return H, rho, S, sum_rule_rhs


def main() -> None:
    assert np.max(np.abs(np.sum(ELL, axis=1) - T)) < 1.0e-15

    print("Stochastic occupation-time response theorem")
    max_sum_rule_error = 0.0
    for omega in (0.05, 0.50, 1.30):
        H, rho, S, rhs = response(omega)
        error = abs(np.sum(S) - rhs)
        max_sum_rule_error = max(max_sum_rule_error, error)
        print(
            f"omega={omega:.2f}: |H|={abs(H):.9f}, "
            f"sum-rule error={error:.3e}"
        )

    mean_ell = np.sum(PROB[:, None] * ELL, axis=0)
    mean_T = float(np.sum(PROB * T))
    cov_T_ell = (
        np.sum(PROB[:, None] * T[:, None] * ELL, axis=0)
        - mean_T * mean_ell
    )

    omega_small = 1.0e-4
    _, rho_small, _, _ = response(omega_small)
    rho_series = mean_ell - 1j * omega_small * cov_T_ell
    low_frequency_error = float(np.max(np.abs(rho_small - rho_series)))

    print()
    print("low-frequency occupation expansion")
    print("  mean occupation = " + ", ".join(f"{x:.6f}" for x in mean_ell))
    print(
        "  Cov(T,ell) = "
        + ", ".join(f"{x:.6f}" for x in cov_T_ell)
    )
    print(f"  O(omega^2) residual at omega=1e-4 = {low_frequency_error:.3e}")

    # Integrated low-frequency coefficients obey occupation-time moment sum rules.
    assert abs(np.sum(mean_ell) - mean_T) < 1.0e-14
    assert abs(np.sum(cov_T_ell) - np.var(T, ddof=0, where=np.ones_like(T,dtype=bool), mean=mean_T)) < 1e-12 if False else True
    # Explicit weighted variance because np.var has no probability weights.
    var_T = float(np.sum(PROB * (T - mean_T) ** 2))
    assert abs(np.sum(cov_T_ell) - var_T) < 1.0e-14

    assert max_sum_rule_error < 5.0e-15
    assert low_frequency_error < 1.0e-8

    print()
    print(
        "PASS: arbitrary stochastic trajectories obey the exact occupation-time "
        "response and global sum rule. The low-RF response maps mean local "
        "occupation time, while its next complex term maps Cov(T,ell_z)."
    )


if __name__ == "__main__":
    main()
