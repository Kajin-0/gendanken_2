"""Joint A/B transport-mode identifiability for the paired phase observable.

The paired same-source measurement is excellent for cancelling arbitrary source
phase, but its data contain A transport minus B transport. This script asks
whether several *independent* smooth transport modes in A and B can be
separated simultaneously, or whether their spectral response subspaces overlap.

Inputs:
- current central sample-B Beer-Lambert/Hansen/Moazzami optical matrix;
- all 72 sample-A composition sensitivity profiles;
- front-collection cell-integrated timing kernels;
- common wavelength grid 2.80-3.95 um, retaining wavelengths with Pabs>=0.05
  in both devices;
- first 1, 2, or 3 right-singular transport modes of each device's separately
  common-phase-centered optical operator.

The main geometry diagnostic column-normalizes the paired response matrix after
projecting out the wavelength-independent phase. Therefore the resulting
singular spectrum measures *response-shape degeneracy*, not absolute sensitivity
or a complete Fisher covariance.

No calibrated sample-A transport and no novelty claim.
"""

from __future__ import annotations

import numpy as np

from hgcdte_sample_a_constraint_family_joint_iso_kernel import (
    N_CELL,
    optical_kernel,
    sample_a_profiles,
    sample_b_profile,
)

LAMBDA_GRID = np.arange(2.80, 3.951, 0.01)
PABS_MIN = 0.05


def matrix_for_profile(
    z_um: np.ndarray,
    x: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    rows = []
    pabs = []
    for wavelength in LAMBDA_GRID:
        p, row = optical_kernel(z_um, x, wavelength, 300.0)
        pabs.append(p)
        rows.append(row)
    return np.asarray(rows), np.asarray(pabs)


def project_common(data: np.ndarray) -> np.ndarray:
    n = data.shape[0]
    one = np.ones(n)
    return data - one[:, None] * ((one @ data) / (one @ one))[None, :]


def normalized_paired_spectrum(
    A: np.ndarray,
    B: np.ndarray,
    n_modes: int,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    Ac = A - np.mean(A, axis=0, keepdims=True)
    Bc = B - np.mean(B, axis=0, keepdims=True)

    _, _, Vta = np.linalg.svd(Ac, full_matrices=False)
    _, _, Vtb = np.linalg.svd(Bc, full_matrices=False)

    RA = A @ Vta[:n_modes].T
    RB = B @ Vtb[:n_modes].T

    # Paired data are A response minus B response.
    G = project_common(np.column_stack((RA, -RB)))

    norms = np.linalg.norm(G, axis=0)
    if np.any(norms <= 0.0):
        raise RuntimeError("Degenerate zero response column")
    Gn = G / norms
    singular = np.linalg.svd(Gn, compute_uv=False)
    return singular / singular[0], RA, RB


def principal_angles_deg(RA: np.ndarray, RB: np.ndarray) -> np.ndarray:
    """Principal angles between A and B spectral-response subspaces."""
    A = project_common(RA)
    B = project_common(RB)
    QA, _ = np.linalg.qr(A)
    QB, _ = np.linalg.qr(B)
    cosines = np.linalg.svd(QA.T @ QB, compute_uv=False)
    angles = np.degrees(np.arccos(np.clip(cosines, -1.0, 1.0)))
    return np.sort(angles)


def main() -> None:
    b_z, b_x = sample_b_profile()
    B_all, pabs_b = matrix_for_profile(b_z, b_x)

    spectra = {1: [], 2: [], 3: []}
    angles = []
    n_wavelengths = []
    lambda_max = []

    for a_z, a_x, _ in sample_a_profiles():
        A_all, pabs_a = matrix_for_profile(a_z, a_x)
        keep = (pabs_a >= PABS_MIN) & (pabs_b >= PABS_MIN)
        A = A_all[keep]
        B = B_all[keep]
        wavelengths = LAMBDA_GRID[keep]

        n_wavelengths.append(len(wavelengths))
        lambda_max.append(float(wavelengths[-1]))

        for n_modes in (1, 2, 3):
            singular, RA, RB = normalized_paired_spectrum(A, B, n_modes)
            spectra[n_modes].append(singular)
            if n_modes == 3:
                angles.append(principal_angles_deg(RA, RB))

    for n_modes in spectra:
        spectra[n_modes] = np.asarray(spectra[n_modes])
    angles = np.asarray(angles)

    print("Paired A/B joint transport-mode identifiability")
    print(f"sample-A sensitivity profiles = {len(angles)}")
    print(
        f"common retained wavelength count = {min(n_wavelengths)}-"
        f"{max(n_wavelengths)}"
    )
    print(
        f"long-wave retained endpoint = {min(lambda_max):.2f}-"
        f"{max(lambda_max):.2f} um"
    )
    print()

    for n_modes in (1, 2, 3):
        values = spectra[n_modes]
        weakest = values[:, -1]
        print(
            f"{n_modes}+{n_modes} independent normalized transport columns: "
            f"weakest singular ratio = {weakest.min():.6f}-"
            f"{weakest.max():.6f}, median={np.median(weakest):.6f}"
        )
    print()

    values = spectra[3]
    print("3+3 normalized paired singular spectrum across A-profile family")
    for mode_index in range(values.shape[1]):
        column = values[:, mode_index]
        print(
            f"  s{mode_index+1}/s1 = {column.min():.6f}-"
            f"{column.max():.6f}, median={np.median(column):.6f}"
        )
    print()

    print("principal angles between first-three A and B response subspaces")
    for index in range(3):
        column = angles[:, index]
        print(
            f"  theta{index+1} = {column.min():.3f}-"
            f"{column.max():.3f} deg, median={np.median(column):.3f} deg"
        )
    print()

    counts_01 = np.sum(values > 0.10, axis=1)
    counts_005 = np.sum(values > 0.05, axis=1)
    print(
        "paired normalized shape modes above 0.10: "
        f"{counts_01.min()}-{counts_01.max()} "
        f"(median {np.median(counts_01):.0f})"
    )
    print(
        "paired normalized shape modes above 0.05: "
        f"{counts_005.min()}-{counts_005.max()} "
        f"(median {np.median(counts_005):.0f})"
    )

    # Stable regressions.
    weak1 = spectra[1][:, -1]
    weak2 = spectra[2][:, -1]
    weak3 = spectra[3][:, -1]

    assert 0.059 < weak1.min() < 0.060
    assert 0.19 < weak1.max() < 0.20

    assert 0.0084 < weak2.min() < 0.0087
    assert 0.040 < weak2.max() < 0.041

    assert 0.0018 < weak3.min() < 0.0019
    assert 0.0075 < weak3.max() < 0.0077

    assert 0.20 < angles[:, 0].min() < 0.22
    assert angles[:, 0].max() < 0.88
    assert 3.5 < angles[:, 1].min() < 3.6
    assert 15.6 < angles[:, 1].max() < 15.8
    assert 33.5 < angles[:, 2].min() < 33.6
    assert 65.3 < angles[:, 2].max() < 65.4

    assert counts_01.min() == 4 and counts_01.max() == 5
    assert counts_005.min() == 4 and counts_005.max() == 5

    print()
    print(
        "PASS: paired A-B spectra contain several useful contrast directions, "
        "but the smooth A and B response subspaces overlap too strongly for a "
        "well-conditioned symmetric reconstruction of three arbitrary modes in "
        "each device. Calibrate/constrain B first, then infer additional A "
        "transport structure from the paired contrast."
    )


if __name__ == "__main__":
    main()
