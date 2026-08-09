"""Singular-value audit for the spectral timing transport inverse.

This is a normalized conditioning study, not a calibrated HgCdTe device model.

The script builds the cumulative timing-kernel matrix for a linear graded gap
and a Weibull generation kernel, then counts singular modes above several
relative singular-value thresholds as the optical generation width is varied.

The purpose is to demonstrate that the number of wavelength samples is not
the number of independently recoverable transport degrees of freedom.
"""

from __future__ import annotations

import numpy as np


L = 1.0
EG_IN = 2.0
EG_OUT = 1.0
G = 1.0
BETA = 0.5
N_EDGE = BETA + 1.0
N_X = 100
N_E = 160

ELL_VALUES = (0.02, 0.05, 0.10, 0.20)
THRESHOLDS = (1.0e-1, 1.0e-2, 1.0e-3, 1.0e-4)


def build_matrix(ell_alpha: float) -> np.ndarray:
    dx = L / N_X
    x = (np.arange(N_X) + 0.5) * dx

    # Nearly full graded-gap sweep.  Avoid the exact endpoints where the
    # conditional generation normalization becomes singular or the entrance
    # coordinate is exactly pinned.
    energies = np.linspace(EG_OUT + 0.001, EG_IN - 0.001, N_E)

    A = np.zeros((N_E, N_X))

    for i, e_gamma in enumerate(energies):
        xg = (EG_IN - e_gamma) / G
        d = L - xg
        tau = (d / ell_alpha) ** N_EDGE
        norm = 1.0 - np.exp(-tau)

        for j, s in enumerate(x):
            if s <= xg:
                cdf = 0.0
            else:
                z = s - xg
                y = min((z / ell_alpha) ** N_EDGE, tau)
                cdf = (1.0 - np.exp(-y)) / norm

            A[i, j] = cdf * dx

    return A


def relative_mode_counts(A: np.ndarray) -> tuple[np.ndarray, list[int]]:
    singular = np.linalg.svd(A, compute_uv=False)
    relative = singular / singular[0]
    counts = [int(np.sum(relative > threshold)) for threshold in THRESHOLDS]
    return relative, counts


def main() -> None:
    all_counts = []

    for ell in ELL_VALUES:
        A = build_matrix(ell)
        relative, counts = relative_mode_counts(A)
        all_counts.append(counts)

        print(f"ell_alpha/L = {ell:.3f}")
        for threshold, count in zip(THRESHOLDS, counts):
            print(f"  modes above {threshold:.0e}: {count}")
        print("  first ten relative singular values:")
        print(" ", np.array2string(relative[:10], precision=5))

    counts = np.asarray(all_counts)

    # Broader optical kernels must not increase the number of reasonably
    # conditioned spatial modes in this fixed normalized experiment.
    for column in range(counts.shape[1]):
        assert np.all(np.diff(counts[:, column]) <= 0)

    # Concrete regression values for the 1e-2 relative threshold.
    expected_1e2 = np.array([29, 18, 13, 10])
    assert np.array_equal(counts[:, 1], expected_1e2)

    print("PASS: broader optical kernels reduce recoverable inverse modes")


if __name__ == "__main__":
    main()
