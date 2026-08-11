"""Noise significance of the two-mode Hankel-minor witness.

For four consecutive raw current samples J0..J3 define

    d0=J1-J0, d1=J2-J1, d2=J3-J2
    W0=d0*d2-d1^2.

For a genuine two-mode first-difference sequence

    d_m=a q1^m+b q2^m,

    W0=a b (q1-q2)^2.

With independent circular complex current noise E|eps_m|^2=sigma_J^2,
linearization gives

    delta W0 = -d2 eps0 + (d2+2d1) eps1
               -(d0+2d1) eps2 + d0 eps3.

Thus

    Var_complex(W0)=sigma_J^2 * sum |c_m|^2.

This script verifies the covariance by Monte Carlo and demonstrates the
sqrt(20)|d| limit when d0=d1=d2=d.
"""

from __future__ import annotations

import numpy as np

RNG = np.random.default_rng(9042)
SIGMA = 2.5e-5
NMC = 300000

A = 0.73 - 0.21j
B = -0.38 + 0.44j
Q1 = 0.91 + 0.08j
Q2 = 0.72 - 0.05j


def first_differences(a: complex, b: complex, q1: complex, q2: complex) -> np.ndarray:
    m = np.arange(3)
    return a * q1**m + b * q2**m


def currents_from_differences(d: np.ndarray) -> np.ndarray:
    J = np.empty(4, dtype=complex)
    J[0] = 0.4 + 0.2j
    J[1:] = J[0] + np.cumsum(d)
    return J


def witness(J: np.ndarray) -> np.ndarray:
    d = np.diff(J, axis=-1)
    return d[..., 0] * d[..., 2] - d[..., 1] ** 2


def coefficients(J: np.ndarray) -> np.ndarray:
    d0, d1, d2 = np.diff(J)
    return np.asarray(
        (-d2, d2 + 2.0 * d1, -(d0 + 2.0 * d1), d0),
        dtype=complex,
    )


def main() -> None:
    d = first_differences(A, B, Q1, Q2)
    J = currents_from_differences(d)
    W = witness(J)
    W_exact = A * B * (Q1 - Q2) ** 2
    assert abs(W - W_exact) < 2.0e-15

    c = coefficients(J)
    predicted_var = SIGMA**2 * float(np.sum(np.abs(c) ** 2))

    noise = (
        RNG.normal(size=(NMC, 4)) + 1j * RNG.normal(size=(NMC, 4))
    ) * (SIGMA / np.sqrt(2.0))
    Ws = witness(J[None, :] + noise)
    residual = Ws - np.mean(Ws)
    mc_var = float(np.mean(np.abs(residual) ** 2))

    print("Two-mode Hankel-minor witness noise")
    print(f"|W0| = {abs(W):.9e}")
    print(f"predicted complex variance = {predicted_var:.9e}")
    print(f"Monte-Carlo complex variance = {mc_var:.9e}")
    print(f"MC/pred = {mc_var/predicted_var:.6f}")
    print(f"witness SNR = {abs(W)/np.sqrt(predicted_var):.3f}")

    assert abs(mc_var / predicted_var - 1.0) < 0.02

    # Equal-step limit.
    deq = 0.17 - 0.04j
    Jeq = currents_from_differences(np.asarray((deq, deq, deq)))
    ceq = coefficients(Jeq)
    norm = np.sqrt(np.sum(np.abs(ceq) ** 2)) / abs(deq)
    print(f"equal-step coefficient norm / |d| = {norm:.12f}")
    assert abs(norm - np.sqrt(20.0)) < 2.0e-14

    # Verify quadratic disappearance of the witness at root coalescence while
    # the noise scale stays finite for fixed nonzero combined amplitude.
    base = 0.84 + 0.03j
    deltas = np.asarray((0.16, 0.08, 0.04, 0.02))
    normalized = []
    for delta in deltas:
        dd = first_differences(1.0, 0.8, base + delta / 2, base - delta / 2)
        JJ = currents_from_differences(dd)
        WW = witness(JJ)
        noise_scale = np.sqrt(np.sum(np.abs(coefficients(JJ)) ** 2))
        normalized.append(abs(WW) / noise_scale)
    normalized = np.asarray(normalized)
    ratios = normalized[:-1] / normalized[1:]
    print("witness/noise ratios for halved root split = " + ", ".join(f"{x:.3f}" for x in ratios))
    assert np.all((ratios > 3.7) & (ratios < 4.3))

    print()
    print(
        "PASS: the observable second-mode signal vanishes quadratically with "
        "root separation while the current-noise scale remains finite.  The "
        "Hankel minor itself is therefore the natural pre-fit significance test "
        "for whether a second spatial mode is resolvable."
    )


if __name__ == "__main__":
    main()
