"""Deterministic regression for ADAPTIVE_FEEDFORWARD_MODE_CAPACITY.md.

Requires NumPy only.

Checks:
1. random trace-nonincreasing instruments satisfy sum_j eta_j <= min(M, r*d);
2. the conditional successful-branch entropy satisfies
       H >= max(0, ln(M*eta_bar/r));
3. an explicit partition instrument saturates the rank and entropy bounds when
   M = r*d.

This is a falsification/regression test, not a proof.
"""

from __future__ import annotations

import math
import numpy as np


RNG = np.random.default_rng(20260808)


def random_instrument(M: int, r: int, d: int):
    """Return d random Kraus maps C^M -> C^r scaled so sum K^dag K <= I."""
    maps = []
    for _ in range(d):
        K = (
            RNG.normal(size=(r, M))
            + 1j * RNG.normal(size=(r, M))
        ) / math.sqrt(2.0 * M)
        maps.append(K)

    S = sum(K.conj().T @ K for K in maps)
    lam_max = float(np.linalg.eigvalsh(S).max())
    if lam_max > 1.0:
        scale = 1.0 / math.sqrt(lam_max)
        maps = [scale * K for K in maps]
    return maps


def metrics(maps, M: int, r: int):
    etas = np.zeros(M)
    for j in range(M):
        etas[j] = sum(float(np.vdot(K[:, j], K[:, j]).real) for K in maps)

    p = np.array(
        [float(np.trace(K.conj().T @ K).real) / M for K in maps],
        dtype=float,
    )
    eta_bar = float(p.sum())

    if eta_bar > 0.0:
        q = p / eta_bar
        H = -sum(x * math.log(x) for x in q if x > 0.0)
    else:
        H = 0.0

    H_floor = max(0.0, math.log(M * eta_bar / r)) if eta_bar > 0 else 0.0
    return etas, eta_bar, H, H_floor


def partition_instrument(r: int, d: int):
    """Tight construction for M=r*d."""
    M = r * d
    maps = []
    for m in range(d):
        K = np.zeros((r, M), dtype=complex)
        start = m * r
        for a in range(r):
            K[a, start + a] = 1.0
        maps.append(K)
    return maps


def run_random_stress():
    worst_rank_margin = float("inf")
    worst_entropy_margin = float("inf")

    cases = 0
    for M in (2, 3, 5, 8, 12):
        for r in (1, 2, 3, 4):
            if r > M:
                continue
            for d in (1, 2, 3, 5, 8):
                for _ in range(100):
                    maps = random_instrument(M, r, d)
                    etas, eta_bar, H, H_floor = metrics(maps, M, r)

                    rank_bound = min(M, r * d)
                    rank_margin = rank_bound - float(etas.sum())
                    entropy_margin = H - H_floor

                    worst_rank_margin = min(worst_rank_margin, rank_margin)
                    worst_entropy_margin = min(worst_entropy_margin, entropy_margin)
                    cases += 1

    tol = 2e-11
    assert worst_rank_margin >= -tol, worst_rank_margin
    assert worst_entropy_margin >= -tol, worst_entropy_margin

    print(f"random cases: {cases}")
    print(f"worst rank-bound margin: {worst_rank_margin:.3e}")
    print(f"worst entropy-bound margin: {worst_entropy_margin:.3e}")


def run_tight_case():
    r, d = 3, 4
    M = r * d
    maps = partition_instrument(r, d)
    etas, eta_bar, H, H_floor = metrics(maps, M, r)

    completeness = sum(K.conj().T @ K for K in maps)
    assert np.allclose(completeness, np.eye(M), atol=1e-13)
    assert np.allclose(etas, np.ones(M), atol=1e-13)
    assert abs(eta_bar - 1.0) < 1e-13
    assert abs(H - math.log(d)) < 1e-13
    assert abs(H_floor - math.log(M / r)) < 1e-13

    print("tight partition case:")
    print(f"  M={M}, r={r}, d={d}")
    print(f"  sum eta_j={etas.sum():.12f} = r*d")
    print(f"  H={H:.12f} = ln(M/r)")


if __name__ == "__main__":
    run_random_stress()
    run_tight_case()
