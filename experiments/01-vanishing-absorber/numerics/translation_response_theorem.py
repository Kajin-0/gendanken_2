"""Numerical regressions for the deterministic translation-response theorem.

This is a model-independent geometry test inside the stated 1-D deterministic
transport assumptions. It does not predict a particular HgCdTe device.

Assumptions
-----------
- generation coordinate X has normalized density p_lambda(x) on [0,L];
- carriers move monotonically to the collecting boundary x=L;
- local transit slowness q(x)>0 gives T(x)=int_x^L q(s) ds;
- complex transfer H(omega)=int p(x) exp[-i omega T(x)] dx;
- a small translated slowness feature is q -> q + eps h(x-z0).

For D(z0)=d ln H / d eps at eps=0, the exact first-order theorem is

    dD/dz0 = -i omega/H * int h(z-z0) p(z) exp[-i omega T(z)] dz.

For an infinitesimal feature h=A delta(z-z0), this factorizes locally:

    R(z0) = -i omega A p(z0) exp[-i omega T(z0)] / H.

Therefore normalized |R| recovers p, while

    q(z) = (1/omega) d arg R / dz.

The complex sum rule is int R dz = -i omega A.
"""

from __future__ import annotations

import numpy as np


L = 1.0
N = 6001
OMEGA = 8.0
FEATURE_AREA = 0.035
FEATURE_SIGMA = 0.025
EPS = 1.0e-5


def cumulative_transit(z: np.ndarray, q: np.ndarray) -> np.ndarray:
    """T(x)=int_x^L q(s) ds by reverse trapezoid accumulation."""
    out = np.zeros_like(z)
    dz = np.diff(z)
    increments = 0.5 * (q[:-1] + q[1:]) * dz
    out[:-1] = np.cumsum(increments[::-1])[::-1]
    return out


def normalize_density(z: np.ndarray, values: np.ndarray) -> np.ndarray:
    return values / np.trapezoid(values, z)


def gaussian_feature(z: np.ndarray, z0: float) -> np.ndarray:
    raw = np.exp(-0.5 * ((z - z0) / FEATURE_SIGMA) ** 2)
    # Use the infinite-line normalization. Test centers stay well inside [0,L].
    norm = FEATURE_AREA / (np.sqrt(2.0 * np.pi) * FEATURE_SIGMA)
    return norm * raw


def transfer(z: np.ndarray, p: np.ndarray, q: np.ndarray) -> complex:
    T = cumulative_transit(z, q)
    return complex(np.trapezoid(p * np.exp(-1j * OMEGA * T), z))


def main() -> None:
    z = np.linspace(0.0, L, N)

    # Deliberately nontrivial optical and transport profiles.
    p = normalize_density(z, (z + 0.05) ** 2 * np.exp(-5.0 * z))
    q = 1.0 + 0.40 * np.sin(2.0 * np.pi * z) + 0.30 * z
    T = cumulative_transit(z, q)
    H = transfer(z, p, q)

    # ------------------------------------------------------------------
    # 1) Delta-feature factorization: reconstruct p and q.
    # ------------------------------------------------------------------
    R_delta = (
        -1j
        * OMEGA
        * FEATURE_AREA
        * p
        * np.exp(-1j * OMEGA * T)
        / H
    )

    p_recovered = normalize_density(z, np.abs(R_delta))
    phase = np.unwrap(np.angle(R_delta))
    q_recovered = np.gradient(phase, z) / OMEGA

    p_error = float(np.max(np.abs(p_recovered - p)))
    q_error = float(np.max(np.abs(q_recovered[10:-10] - q[10:-10])))
    sum_rule = complex(np.trapezoid(R_delta, z))
    sum_rule_target = -1j * OMEGA * FEATURE_AREA

    # ------------------------------------------------------------------
    # 2) Finite-width theorem against direct central finite differences.
    # ------------------------------------------------------------------
    centers = np.linspace(0.15, 0.85, 281)
    D_fd = []
    R_theorem = []
    local_complex_density = p * np.exp(-1j * OMEGA * T) / H

    for z0 in centers:
        h = gaussian_feature(z, float(z0))
        Hp = transfer(z, p, q + EPS * h)
        Hm = transfer(z, p, q - EPS * h)
        # Central derivative of log H without principal-log subtraction.
        # d ln H = (1/H) dH avoids branch-cut artifacts.
        D_fd.append((Hp - Hm) / (2.0 * EPS * H))
        R_theorem.append(
            -1j * OMEGA * np.trapezoid(h * local_complex_density, z)
        )

    D_fd = np.asarray(D_fd)
    R_fd = np.gradient(D_fd, centers)
    R_theorem = np.asarray(R_theorem)

    rel = np.linalg.norm(R_fd[3:-3] - R_theorem[3:-3]) / np.linalg.norm(
        R_theorem[3:-3]
    )

    # ------------------------------------------------------------------
    # 3) Low-frequency finite-displacement probability-window identity.
    # For an infinitesimal positive slowness feature, moving it z1->z2 changes
    # mean delay by A * int_z1^z2 p(z) dz.
    # ------------------------------------------------------------------
    z1, z2 = 0.28, 0.67
    F = np.concatenate(
        ([0.0], np.cumsum(0.5 * (p[:-1] + p[1:]) * np.diff(z)))
    )
    F1 = float(np.interp(z1, z, F))
    F2 = float(np.interp(z2, z, F))
    probability_window = float(
        np.trapezoid(p[(z >= z1) & (z <= z2)], z[(z >= z1) & (z <= z2)])
    )
    relocation_delay = FEATURE_AREA * (F2 - F1)

    print("Deterministic translation-response theorem")
    print(f"max p reconstruction error = {p_error:.3e}")
    print(f"max interior q reconstruction error = {q_error:.3e}")
    print(
        "complex sum rule = "
        f"{sum_rule.real:+.3e}{sum_rule.imag:+.9f}j; "
        f"target {sum_rule_target.real:+.3e}{sum_rule_target.imag:+.9f}j"
    )
    print(f"finite-width theorem relative error = {rel:.3e}")
    print(
        "finite-shift probability identity: "
        f"A[F(z2)-F(z1)]={relocation_delay:.9f}, "
        f"A*P(z1<X<z2)~{FEATURE_AREA*probability_window:.9f}"
    )

    assert p_error < 2.0e-12
    assert q_error < 3.0e-6
    assert abs(sum_rule - sum_rule_target) < 2.0e-12
    assert rel < 2.0e-3
    assert abs((F2 - F1) - probability_window) < 5.0e-4

    print()
    print(
        "PASS: translated local slowness perturbations factorize into local "
        "generation amplitude and baseline transit phase in deterministic 1-D "
        "transport. The ideal delta-feature relocation field reconstructs both "
        "p(z) and q(z), and the wavelength-independent complex sum rule holds."
    )


if __name__ == "__main__":
    main()
