"""Deterministic stress tests for PASSIVE_MULTIMODE_TRANSFER_AREA_BOUND.md.

Requires NumPy only.

The analytic theorem is not used to compute the directly integrated transfer
spectrum.  The script performs three separate checks:

1. solve the controllability Lyapunov equation for random passive networks and
   verify 0 <= Q_L <= I;
2. verify the derived H2 transfer area never exceeds
   2 min(Tr Gamma_L, Tr Gamma_R);
3. for one deterministic three-mode network, integrate the actual frequency-
   domain transfer matrix over a large finite window and compare that numerical
   integral with the independently computed Gramian/H2 value.

This is a falsification/regression test, not a proof.
"""

from __future__ import annotations

import numpy as np


SEED = 20260808
TOL_EIG = 2e-10
TOL_BOUND = 2e-10
DIRECT_REL_TOL = 5e-3


def hermitian_psd_sqrt(matrix: np.ndarray) -> np.ndarray:
    """Return the Hermitian positive-semidefinite square root."""
    vals, vecs = np.linalg.eigh(matrix)
    vals = np.maximum(vals, 0.0)
    return (vecs * np.sqrt(vals)) @ vecs.conj().T


def random_psd(
    rng: np.random.Generator,
    n: int,
    scale: float,
    floor: float = 0.0,
) -> np.ndarray:
    x = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    matrix = scale * (x @ x.conj().T) / (2.0 * n)
    if floor:
        matrix = matrix + floor * np.eye(n)
    return matrix


def solve_continuous_lyapunov(A: np.ndarray, source: np.ndarray) -> np.ndarray:
    """Solve A X + X A^dagger + source = 0 by vectorization.

    Implemented directly with NumPy so SciPy is not required.
    """
    n = A.shape[0]
    operator = np.kron(np.eye(n), A) + np.kron(A.conj(), np.eye(n))
    rhs = -source.reshape(n * n, order="F")
    vec_x = np.linalg.solve(operator, rhs)
    x = vec_x.reshape((n, n), order="F")
    return 0.5 * (x + x.conj().T)


def make_passive_network(
    rng: np.random.Generator,
    n: int,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    x = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    H = (x + x.conj().T) / (2.0 * np.sqrt(n))

    gamma_l = random_psd(rng, n, scale=0.50, floor=0.05)
    gamma_r = random_psd(rng, n, scale=0.45, floor=0.05)
    gamma_i = random_psd(rng, n, scale=0.05)

    A = -1j * H - (gamma_l + gamma_r + gamma_i)
    return A, gamma_l, gamma_r, gamma_i


def h2_area_from_gramian(
    A: np.ndarray,
    gamma_l: np.ndarray,
    gamma_r: np.ndarray,
) -> tuple[float, np.ndarray]:
    q_l = solve_continuous_lyapunov(A, 2.0 * gamma_l)
    area = float(np.real(2.0 * np.trace(gamma_r @ q_l)))
    return area, q_l


def direct_frequency_area(
    A: np.ndarray,
    gamma_l: np.ndarray,
    gamma_r: np.ndarray,
    window_multiplier: float = 100.0,
    points: int = 40001,
) -> float:
    """Directly integrate Tr[G^dagger G] d omega /(2 pi)."""
    n = A.shape[0]
    identity = np.eye(n)
    b_l = hermitian_psd_sqrt(2.0 * gamma_l)
    c_r = hermitian_psd_sqrt(2.0 * gamma_r)

    spectral_scale = max(1.0, float(np.max(np.abs(np.linalg.eigvals(A)))))
    omega = np.linspace(
        -window_multiplier * spectral_scale,
        window_multiplier * spectral_scale,
        points,
    )

    transfer_power = np.empty(points)
    for index, w in enumerate(omega):
        g = c_r @ np.linalg.solve(1j * w * identity - A, b_l)
        transfer_power[index] = float(np.real(np.trace(g.conj().T @ g)))

    return float(np.trapezoid(transfer_power, omega) / (2.0 * np.pi))


def random_stress() -> None:
    rng = np.random.default_rng(SEED)
    print("Random passive-network stress test")
    print("n   trials   max(area/bound)   min eig(Q)   max eig(Q)")

    for n, trials in ((1, 100), (2, 100), (4, 100), (8, 100)):
        max_ratio = 0.0
        min_q = np.inf
        max_q = -np.inf

        for _ in range(trials):
            A, gamma_l, gamma_r, _ = make_passive_network(rng, n)
            area, q_l = h2_area_from_gramian(A, gamma_l, gamma_r)
            bound = 2.0 * min(
                float(np.real(np.trace(gamma_l))),
                float(np.real(np.trace(gamma_r))),
            )

            eig_q = np.linalg.eigvalsh(q_l)
            min_q = min(min_q, float(eig_q[0]))
            max_q = max(max_q, float(eig_q[-1]))
            max_ratio = max(max_ratio, area / bound)

            assert eig_q[0] >= -TOL_EIG
            assert eig_q[-1] <= 1.0 + TOL_EIG
            assert area <= bound * (1.0 + TOL_BOUND)

        print(
            f"{n:<3d} {trials:<8d} {max_ratio:>16.9f} "
            f"{min_q:>12.3e} {max_q:>12.9f}"
        )


def direct_spectral_check() -> None:
    """Compare direct frequency integration with the Gramian H2 value."""
    rng = np.random.default_rng(SEED + 1)
    A, gamma_l, gamma_r, _ = make_passive_network(rng, 3)

    gramian_area, _ = h2_area_from_gramian(A, gamma_l, gamma_r)
    direct_area = direct_frequency_area(A, gamma_l, gamma_r)
    bound = 2.0 * min(
        float(np.real(np.trace(gamma_l))),
        float(np.real(np.trace(gamma_r))),
    )

    rel_error = abs(direct_area - gramian_area) / gramian_area

    print("\nDirect spectral integration check")
    print(f"Gramian/H2 area       = {gramian_area:.12g}")
    print(f"Direct spectral area  = {direct_area:.12g}")
    print(f"Relative difference   = {rel_error:.6g}")
    print(f"Trace bound            = {bound:.12g}")
    print(f"Area / bound           = {gramian_area / bound:.9f}")

    # The direct integral uses a finite frequency window, so compare to a
    # practical truncation tolerance rather than machine precision.
    assert rel_error < DIRECT_REL_TOL
    assert gramian_area <= bound * (1.0 + TOL_BOUND)


if __name__ == "__main__":
    random_stress()
    direct_spectral_check()
    print("\nAll passive multimode transfer-area checks passed.")
