"""Deterministic stress tests for PASSIVE_MULTIMODE_TRANSFER_AREA_BOUND.md.

Requires NumPy only.

The canonical analytic result is

    I_LR <= 2 L R / (L + R),

where

    I_LR = integral Tr[G_RL^dagger G_RL] d omega / (2 pi),
    L = Tr Gamma_L,
    R = Tr Gamma_R.

The script performs independent numerical checks of:

1. the passive controllability-Gramian inequality 0 <= Q_L <= I;
2. the diagonal Lyapunov identity

       q_i = ell_i / (ell_i + r_i + iota_i)

   in the eigenbasis of Q_L;
3. the harmonic transfer-area bound;
4. direct frequency integration of a representative multimode transfer matrix
   versus the separately computed Gramian/H2 area.

This is a falsification/regression test, not a proof.
"""

from __future__ import annotations

import numpy as np


SEED = 20260808
TOL_EIG = 2e-10
TOL_BOUND = 2e-10
TOL_DIAGONAL_IDENTITY = 2e-9
DIRECT_REL_TOL = 5e-3


def hermitian_psd_sqrt(matrix: np.ndarray) -> np.ndarray:
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
    """Solve A X + X A^dagger + source = 0 by vectorization."""
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


def harmonic_bound(gamma_l: np.ndarray, gamma_r: np.ndarray) -> float:
    left = float(np.real(np.trace(gamma_l)))
    right = float(np.real(np.trace(gamma_r)))
    if left + right == 0.0:
        return 0.0
    return 2.0 * left * right / (left + right)


def diagonal_identity_error(
    q_l: np.ndarray,
    gamma_l: np.ndarray,
    gamma_r: np.ndarray,
    gamma_i: np.ndarray,
) -> float:
    """Check q_i = ell_i/(ell_i+r_i+iota_i) in the Q eigenbasis."""
    q_values, U = np.linalg.eigh(q_l)

    left_diag = np.real(np.diag(U.conj().T @ gamma_l @ U))
    right_diag = np.real(np.diag(U.conj().T @ gamma_r @ U))
    loss_diag = np.real(np.diag(U.conj().T @ gamma_i @ U))
    total_diag = left_diag + right_diag + loss_diag

    mask = total_diag > 1e-12
    if not np.any(mask):
        return 0.0

    predicted = left_diag[mask] / total_diag[mask]
    return float(np.max(np.abs(q_values[mask] - predicted)))


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
    print(
        "n   trials   max(area/harmonic)   min eig(Q)   "
        "max eig(Q)   max diag error"
    )

    for n, trials in ((1, 100), (2, 100), (4, 100), (8, 100)):
        max_ratio = 0.0
        min_q = np.inf
        max_q = -np.inf
        max_diag_error = 0.0

        for _ in range(trials):
            A, gamma_l, gamma_r, gamma_i = make_passive_network(rng, n)
            area, q_l = h2_area_from_gramian(A, gamma_l, gamma_r)
            bound = harmonic_bound(gamma_l, gamma_r)

            eig_q = np.linalg.eigvalsh(q_l)
            diag_error = diagonal_identity_error(
                q_l,
                gamma_l,
                gamma_r,
                gamma_i,
            )

            min_q = min(min_q, float(eig_q[0]))
            max_q = max(max_q, float(eig_q[-1]))
            max_ratio = max(max_ratio, area / bound)
            max_diag_error = max(max_diag_error, diag_error)

            assert eig_q[0] >= -TOL_EIG
            assert eig_q[-1] <= 1.0 + TOL_EIG
            assert diag_error <= TOL_DIAGONAL_IDENTITY
            assert area <= bound * (1.0 + TOL_BOUND)

        print(
            f"{n:<3d} {trials:<8d} {max_ratio:>18.9f} "
            f"{min_q:>12.3e} {max_q:>12.9f} "
            f"{max_diag_error:>14.3e}"
        )


def single_mode_tightness_check() -> None:
    """One passive resonance must exactly saturate the harmonic bound."""
    gamma_l = 0.37
    gamma_r = 1.13

    A = np.array([[-(gamma_l + gamma_r) - 1j * 0.71]], dtype=complex)
    left = np.array([[gamma_l]], dtype=complex)
    right = np.array([[gamma_r]], dtype=complex)

    area, _ = h2_area_from_gramian(A, left, right)
    bound = harmonic_bound(left, right)

    print("\nSingle-mode tightness check")
    print(f"Exact H2 area          = {area:.12g}")
    print(f"Harmonic bound         = {bound:.12g}")
    print(f"Relative difference    = {abs(area - bound) / bound:.3e}")

    assert np.isclose(area, bound, rtol=1e-12, atol=1e-12)


def direct_spectral_check() -> None:
    """Compare direct frequency integration with the Gramian H2 value."""
    rng = np.random.default_rng(SEED + 1)
    A, gamma_l, gamma_r, _ = make_passive_network(rng, 3)

    gramian_area, _ = h2_area_from_gramian(A, gamma_l, gamma_r)
    direct_area = direct_frequency_area(A, gamma_l, gamma_r)
    bound = harmonic_bound(gamma_l, gamma_r)

    rel_error = abs(direct_area - gramian_area) / gramian_area

    print("\nDirect spectral integration check")
    print(f"Gramian/H2 area       = {gramian_area:.12g}")
    print(f"Direct spectral area  = {direct_area:.12g}")
    print(f"Relative difference   = {rel_error:.6g}")
    print(f"Harmonic bound         = {bound:.12g}")
    print(f"Area / bound           = {gramian_area / bound:.9f}")

    assert rel_error < DIRECT_REL_TOL
    assert gramian_area <= bound * (1.0 + TOL_BOUND)


if __name__ == "__main__":
    random_stress()
    single_mode_tightness_check()
    direct_spectral_check()
    print("\nAll passive multimode harmonic-bound checks passed.")
