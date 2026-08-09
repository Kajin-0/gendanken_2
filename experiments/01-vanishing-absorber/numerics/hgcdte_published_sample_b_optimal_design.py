"""D-optimal wavelength/time design for the published sample-B inverse.

The active inverse aims first at three smooth differential transport modes.
A fourth parameter is an unknown wavelength-independent phase nuisance.

This script uses the literature-constrained 150 V/cm sample-B optical matrix,
constructs the first three smooth spatial modes from the common-mode-centered
optical operator, and optimizes fractional measurement time over the retained
wavelength grid.

Three simple per-unit-time phase-variance models are compared:
- equal:       c_i = 1
- statistics:  c_i proportional to 1/Pabs
- additive:    c_i proportional to 1/Pabs^2

For variance c_i/t_i, the Fisher contribution is
(t_i/c_i) h_i h_i^T.  The multiplicative D-optimal-design algorithm maximizes
log det of the four-parameter Fisher matrix subject to sum_i t_i = 1.

The result is an experimental-design calculation, not a claim about a specific
instrument or the actual sample-B transport profile.
"""

from __future__ import annotations

import numpy as np

from hgcdte_published_sample_b_forward_matrix import (
    LAMBDA_GRID,
    PABS_MIN,
    optical_distribution,
)

FIELD_V_CM = 150.0
N_TRANSPORT_MODES = 3
SUPPORT_THRESHOLD = 1.0e-4
CONVERGENCE_TOL = 1.0e-10
MAX_ITER = 100_000


def build_operator() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    rows = []
    pabs = []
    for wavelength in LAMBDA_GRID:
        p, _, _, timing_row = optical_distribution(wavelength, FIELD_V_CM)
        rows.append(timing_row)
        pabs.append(p)

    rows = np.asarray(rows)
    pabs = np.asarray(pabs)
    keep = pabs >= PABS_MIN
    return rows[keep], pabs[keep], LAMBDA_GRID[keep]


def transport_mode_basis(A: np.ndarray) -> np.ndarray:
    """First 3 right singular modes after removing equal-weight common row."""
    A_centered = A - np.mean(A, axis=0, keepdims=True)
    _, _, Vt = np.linalg.svd(A_centered, full_matrices=False)
    return Vt[:N_TRANSPORT_MODES].T


def d_optimal_weights(H: np.ndarray) -> tuple[np.ndarray, np.ndarray, int]:
    """Approximate D-optimal design by the standard multiplicative update."""
    n, p_dim = H.shape
    weights = np.ones(n) / n

    for iteration in range(MAX_ITER):
        fisher = (H.T * weights) @ H
        inverse = np.linalg.inv(fisher)
        sensitivity = np.einsum("ij,jk,ik->i", H, inverse, H)
        updated = weights * sensitivity / p_dim
        updated /= np.sum(updated)

        if np.max(np.abs(updated - weights)) < CONVERGENCE_TOL:
            weights = updated
            break
        weights = updated

    fisher = (H.T * weights) @ H
    return weights, fisher, iteration


def consolidate_adjacent_support(
    wavelengths: np.ndarray,
    pabs: np.ndarray,
    weights: np.ndarray,
) -> list[tuple[float, float, float]]:
    indices = np.flatnonzero(weights > SUPPORT_THRESHOLD)
    groups: list[list[int]] = []
    current = [int(indices[0])]

    for index in indices[1:]:
        index = int(index)
        if index == current[-1] + 1:
            current.append(index)
        else:
            groups.append(current)
            current = [index]
    groups.append(current)

    result = []
    for group in groups:
        group = np.asarray(group)
        total = float(np.sum(weights[group]))
        wavelength = float(np.sum(weights[group] * wavelengths[group]) / total)
        absorbed = float(np.sum(weights[group] * pabs[group]) / total)
        result.append((wavelength, absorbed, total))
    return result


def main() -> None:
    A, pabs, wavelengths = build_operator()
    V = transport_mode_basis(A)
    mode_response = A @ V

    cases = {
        "equal": np.ones_like(pabs),
        "statistics-like": 1.0 / pabs,
        "additive-like": 1.0 / pabs**2,
    }

    expected_bands = {
        "equal": np.array([2.80, 3.43, 3.681, 3.89]),
        "statistics-like": np.array([2.80, 3.41, 3.632, 3.84]),
        "additive-like": np.array([2.80, 3.40, 3.596, 3.78]),
    }

    print("Published sample-B D-optimal wavelength/time design")
    print(
        f"retained grid: {wavelengths[0]:.2f}-{wavelengths[-1]:.2f} um, "
        f"N={len(wavelengths)}"
    )
    print("parameters: 3 transport-mode amplitudes + 1 common phase nuisance")
    print()

    for name, variance_coefficient in cases.items():
        # Per-unit-time Fisher row after whitening by variance coefficient.
        H = np.column_stack((mode_response, np.ones(len(wavelengths))))
        H = H / np.sqrt(variance_coefficient)[:, None]

        weights, fisher_opt, iterations = d_optimal_weights(H)
        fisher_uniform = (H.T / len(H)) @ H

        det_ratio = float(np.linalg.det(fisher_opt) / np.linalg.det(fisher_uniform))
        information_scale_gain = det_ratio ** (1.0 / H.shape[1])
        time_fraction_same_information = 1.0 / information_scale_gain

        support = consolidate_adjacent_support(wavelengths, pabs, weights)
        bands = np.array([entry[0] for entry in support])

        print(name)
        print(f"  iterations = {iterations}")
        print(f"  D-information-scale gain vs uniform time = {information_scale_gain:.4f}")
        print(
            "  total-time fraction for same generalized information volume = "
            f"{time_fraction_same_information:.4f}"
        )
        for wavelength, absorbed, fraction in support:
            print(
                f"  band ~{wavelength:.3f} um: "
                f"Pabs~{absorbed:.3f}, time fraction~{fraction:.3f}"
            )
        print()

        # Stable design regressions; grid-adjacent pairs represent one continuous band.
        assert len(support) == 4
        assert np.all(np.abs(bands - expected_bands[name]) < 0.006)
        assert np.all(np.abs(np.array([entry[2] for entry in support]) - 0.25) < 0.002)

        if name == "statistics-like":
            assert 1.32 < information_scale_gain < 1.35
            assert 0.74 < time_fraction_same_information < 0.76
        if name == "additive-like":
            assert 1.33 < information_scale_gain < 1.36
            assert 0.74 < time_fraction_same_information < 0.76

    print(
        "PASS: the optimal reduced-rank design uses four complementary spectral "
        "bands and shifts the long-wave band away from cutoff as its noise cost rises"
    )


if __name__ == "__main__":
    main()
