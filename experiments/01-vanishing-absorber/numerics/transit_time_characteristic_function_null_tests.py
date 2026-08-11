"""Parameter-free null tests for any positive classical transit-time distribution.

If a DC-normalized transport response is

    H(omega) = E[exp(-i omega T)]

for a real random transit time T, then H is a characteristic function.
Consequences include

    H(0)=1,
    H(-omega)=H(omega)*,
    |H(omega)|<=1,

and positive-semidefiniteness of every matrix

    K_jk = H(omega_j-omega_k).

A particularly simple two-harmonic inequality follows with
Z=exp(-i omega T):

    |H(2 omega)-H(omega)^2| <= 1-|H(omega)|^2.

It is just |E[(Z-EZ)^2]| <= E[|Z-EZ|^2].

This script checks the inequality and Toeplitz PSD on arbitrary discrete timing
distributions and constructs a deliberately invalid response that violates them.
"""

from __future__ import annotations

import numpy as np


def H_discrete(omega: float, times: np.ndarray, probabilities: np.ndarray) -> complex:
    return complex(np.sum(probabilities * np.exp(-1j * omega * times)))


def harmonic_gap(omega: float, times: np.ndarray, probabilities: np.ndarray):
    h1 = H_discrete(omega, times, probabilities)
    h2 = H_discrete(2.0 * omega, times, probabilities)
    lhs = abs(h2 - h1 * h1)
    rhs = 1.0 - abs(h1) ** 2
    return lhs, rhs


def characteristic_matrix(
    frequencies: np.ndarray,
    times: np.ndarray,
    probabilities: np.ndarray,
) -> np.ndarray:
    n = len(frequencies)
    K = np.empty((n, n), dtype=complex)
    for j in range(n):
        for k in range(n):
            K[j, k] = H_discrete(
                frequencies[j] - frequencies[k], times, probabilities
            )
    return K


def main() -> None:
    distributions = (
        (
            np.asarray((0.2, 0.7, 1.5, 2.8)),
            np.asarray((0.10, 0.25, 0.40, 0.25)),
        ),
        (
            np.asarray((0.05, 1.0, 5.0)),
            np.asarray((0.70, 0.20, 0.10)),
        ),
    )
    frequencies = np.asarray((0.0, 0.6, 1.7, 3.1))

    print("Transit-time characteristic-function null tests")
    for index, (times, probabilities) in enumerate(distributions, start=1):
        probabilities = probabilities / np.sum(probabilities)
        worst_margin = np.inf
        for omega in np.linspace(0.05, 5.0, 300):
            lhs, rhs = harmonic_gap(omega, times, probabilities)
            worst_margin = min(worst_margin, rhs - lhs)

        K = characteristic_matrix(frequencies, times, probabilities)
        eigenvalues = np.linalg.eigvalsh(K)

        print(f"distribution {index}")
        print(f"  minimum harmonic-inequality margin = {worst_margin:.3e}")
        print(f"  minimum characteristic-matrix eigenvalue = {eigenvalues.min():.3e}")

        assert worst_margin > -2.0e-15
        assert eigenvalues.min() > -2.0e-14

    # Deliberately invalid harmonic pair. Choose H(omega)=0.9 and H(2omega)=-0.9.
    # Then lhs=|-0.9-0.81|=1.71 while rhs=0.19.
    h1_bad = 0.9 + 0.0j
    h2_bad = -0.9 + 0.0j
    lhs_bad = abs(h2_bad - h1_bad**2)
    rhs_bad = 1.0 - abs(h1_bad) ** 2

    print("invalid synthetic harmonic pair")
    print(f"  lhs={lhs_bad:.6f}, rhs={rhs_bad:.6f}")
    assert lhs_bad > rhs_bad

    print()
    print(
        "PASS: any positive classical transit-time distribution obeys the "
        "two-harmonic inequality and positive-semidefinite characteristic "
        "matrices. Violating these constraints falsifies the timing-distribution "
        "observable before any drift-diffusion model is considered."
    )


if __name__ == "__main__":
    main()
