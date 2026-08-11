"""Spatial occupation-time decomposition of transit-time cumulants.

For arbitrary successful trajectories with transit time T and occupation density
ell(z), define

    rho_s(z)=E[e^(sT) ell(z)] / E[e^(sT)].

This is the eta-derivative at eta=0 of

    ln E[e^(sT + eta ell(z))],

so

    rho_s(z)=sum_n s^n/n! * kappa(ell(z), T,...,T).

Because integral ell(z) dz=T trajectory by trajectory,

    integral kappa(ell(z), T^n) dz = kappa_{n+1}(T).

The script verifies n=0,1,2 and the second-order frequency expansion on an
arbitrary finite trajectory ensemble.
"""

from __future__ import annotations

import numpy as np


P = np.asarray((0.15, 0.25, 0.35, 0.25), dtype=float)
T = np.asarray((1.0, 1.8, 2.6, 4.2), dtype=float)
ELL = np.asarray(
    (
        (0.15, 0.25, 0.30, 0.30),
        (0.40, 0.45, 0.50, 0.45),
        (0.20, 0.80, 0.90, 0.70),
        (0.70, 1.10, 1.30, 1.10),
    ),
    dtype=float,
)


def weighted_mean(x):
    return np.sum(P * x)


def rho(omega: float):
    phase = np.exp(-1j * omega * T)
    return np.sum(P[:, None] * phase[:, None] * ELL, axis=0) / np.sum(P * phase)


def main() -> None:
    mu_T = weighted_mean(T)
    mu_ell = np.sum(P[:, None] * ELL, axis=0)

    E_T2 = weighted_mean(T**2)
    E_ellT = np.sum(P[:, None] * ELL * T[:, None], axis=0)
    kappa_ell_T = E_ellT - mu_ell * mu_T

    E_ellT2 = np.sum(P[:, None] * ELL * T[:, None] ** 2, axis=0)
    kappa_ell_TT = (
        E_ellT2
        - 2.0 * mu_T * E_ellT
        - mu_ell * E_T2
        + 2.0 * mu_ell * mu_T**2
    )

    var_T = weighted_mean((T - mu_T) ** 2)
    kappa3_T = weighted_mean((T - mu_T) ** 3)

    print("Occupation-time cumulant hierarchy")
    print(f"integral kappa(ell)       = {np.sum(mu_ell):.12f}; E[T]={mu_T:.12f}")
    print(
        f"integral kappa(ell,T)     = {np.sum(kappa_ell_T):.12f}; "
        f"Var(T)={var_T:.12f}"
    )
    print(
        f"integral kappa(ell,T,T)   = {np.sum(kappa_ell_TT):.12f}; "
        f"kappa3(T)={kappa3_T:.12f}"
    )

    assert abs(np.sum(mu_ell) - mu_T) < 1.0e-14
    assert abs(np.sum(kappa_ell_T) - var_T) < 1.0e-14
    assert abs(np.sum(kappa_ell_TT) - kappa3_T) < 2.0e-14

    omega = 1.0e-3
    series = (
        mu_ell
        + (-1j * omega) * kappa_ell_T
        + ((-1j * omega) ** 2 / 2.0) * kappa_ell_TT
    )
    error = float(np.max(np.abs(rho(omega) - series)))
    print(f"second-order rho_omega series error at omega=1e-3 = {error:.3e}")
    assert error < 1.0e-9

    print()
    print(
        "PASS: local occupation-time mixed cumulants integrate to successive "
        "global transit-time cumulants. A frequency-resolved local clock scan "
        "therefore provides a spatial decomposition of the full timing-cumulant "
        "hierarchy, not only mean delay and variance."
    )


if __name__ == "__main__":
    main()
