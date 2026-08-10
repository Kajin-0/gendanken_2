"""Same-wafer translated-gradient depth-series design.

Motivation
----------
A two-device translated-gradient control is scientifically much stronger than the
published A/B pair, but two separate growths can still differ in bulk/contact
transport. This script asks whether several translated feature depths on one
nominal growth can distinguish the predicted relocation fingerprint from a
smooth lateral fabrication drift.

This is an INFORMATION-DESIGN calculation, not a demonstrated HgCdTe fabrication
recipe. A HgCdTe-specific moving-shutter / selective-growth implementation has
not yet been established in the repository literature audit.

Model
-----
- current growth-programmable 1-um HgCdTe gradient feature;
- L=7.6 um, x_front=0.55, x_back=0.32;
- finite-RF deterministic-transit Jacobian;
- f = 0.25, 0.5, 1, 2, 3 GHz;
- lambda = 2.00-2.40 um in 0.025-um steps;
- illustrative 25% feature-supported transport change;
- common bulk nuisance: 1,z,z^2,z^3;
- front-interface exponentials with ell=0.30,0.50,0.75,1.00 um;
- back-interface exponentials with the same scales;
- statistics-like optical weighting proportional to Pabs^(1/2);
- arbitrary wavelength-independent phase and log-magnitude intercept for every
  independent device contrast and RF frequency.

Device-common response is removed using an orthonormal Helmert contrast basis.
For every physical nuisance spatial template, its amplitude across the depth
series is allowed to follow

    a0 + a1 xi + ... + ap xi^p,

where xi is the normalized lateral/device coordinate. Thus p=2 means every
bulk/interface nuisance amplitude may have an arbitrary QUADRATIC lateral trend.

The score is the nuisance-orthogonal complex-response norm divided by
sqrt(N_device * N_lambda), so it is proportional to SNR at fixed total
measurement resource under the stated equal-frequency component-noise model.

No novelty claim and no assertion that the illustrative transport change is a
real HgCdTe device prediction.
"""

from __future__ import annotations

import itertools
import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.linalg import qr

from hgcdte_matched_contact_translated_gradient_design import (
    FREQUENCIES_GHZ,
    L_UM,
    cell_centers,
)
from hgcdte_programmed_translated_gradient_design import (
    programmed_profile,
    transport_delta_q,
)
from hgcdte_sample_a_constraint_family_joint_iso_kernel import (
    HC_EV_UM,
    N_CELL,
    alpha_moazzami,
)
from hgcdte_shortwave_finite_rf_jacobian import finite_rf_jacobian

WAVELENGTHS_UM = np.arange(2.00, 2.4001, 0.025)
CANDIDATE_DEPTHS_UM = np.arange(2.00, 5.6001, 0.20)
MIN_DEPTH_SPACING_UM = 0.40
BETA = 0.5  # statistics-like sigma ~ Pabs^(-1/2)


def pabs_grid(z_um: np.ndarray, x: np.ndarray) -> np.ndarray:
    z_cm = z_um * 1.0e-4
    values = []
    for wavelength in WAVELENGTHS_UM:
        alpha = alpha_moazzami(HC_EV_UM / float(wavelength), x, 300.0)
        tau = np.concatenate(([0.0], cumulative_trapezoid(alpha, z_cm)))
        values.append(float(1.0 - np.exp(-tau[-1])))
    return np.asarray(values)


def nuisance_spatial_matrix() -> np.ndarray:
    z = cell_centers()
    u = z / L_UM
    columns = [np.ones(N_CELL), u, u**2, u**3]
    for ell in (0.30, 0.50, 0.75, 1.00):
        columns.append(np.exp(-z / ell))
    for ell in (0.30, 0.50, 0.75, 1.00):
        columns.append(np.exp(-(L_UM - z) / ell))
    return np.column_stack(columns)


NUISANCE_SPATIAL = nuisance_spatial_matrix()


def response_at_depth(z0_um: float):
    z, x, feature, _ = programmed_profile(float(z0_um))
    jacobian, _ = finite_rf_jacobian(
        z,
        x,
        FREQUENCIES_GHZ,
        wavelengths=WAVELENGTHS_UM,
    )
    dq = transport_delta_q(z, feature)
    target = np.einsum("flj,j->fl", jacobian, dq)
    nuisance = np.einsum("flj,jk->flk", jacobian, NUISANCE_SPATIAL)
    return target, nuisance, pabs_grid(z, x)


def helmert(n: int) -> np.ndarray:
    """Return (n-1)x n orthonormal device-contrast matrix."""
    matrix = np.zeros((n - 1, n))
    for i in range(1, n):
        matrix[i - 1, :i] = 1.0 / np.sqrt(i * (i + 1.0))
        matrix[i - 1, i] = -i / np.sqrt(i * (i + 1.0))
    return matrix


def project_residual_qr(target: np.ndarray, nuisance: np.ndarray) -> np.ndarray:
    """Project target from nuisance column span using pivoted QR."""
    qmat, rmat, _ = qr(nuisance, mode="economic", pivoting=True)
    diagonal = np.abs(np.diag(rmat))
    if len(diagonal) == 0 or diagonal[0] == 0.0:
        return target
    rank = int(np.sum(diagonal > diagonal[0] * 1.0e-10))
    return target - qmat[:, :rank] @ (qmat[:, :rank].T @ target)


def series_score(
    depths_um: tuple[float, ...],
    cache: dict[float, tuple[np.ndarray, np.ndarray, np.ndarray]],
    drift_order: int,
):
    n_device = len(depths_um)
    data = [cache[round(float(depth), 6)] for depth in depths_um]

    target = np.asarray([row[0] for row in data])
    nuisance = np.asarray([row[1] for row in data])
    pabs = np.asarray([row[2] for row in data])

    # Statistics-like signal whitening. Over 2.0-2.4 um Pabs remains very high,
    # but retain the correction rather than silently assuming exact equality.
    weight = pabs**BETA
    target = target * weight[:, None, :]
    nuisance = nuisance * weight[:, None, :, None]

    contrast = helmert(n_device)
    target_contrast = np.einsum("ad,dfl->afl", contrast, target)

    xi = np.linspace(-1.0, 1.0, n_device)
    nuisance_blocks = []
    for order in range(drift_order + 1):
        block = nuisance * (xi**order)[:, None, None, None]
        block = np.einsum("ad,dflk->aflk", contrast, block)
        nuisance_blocks.append(
            np.concatenate(
                (
                    block.imag.reshape(-1, block.shape[-1]),
                    block.real.reshape(-1, block.shape[-1]),
                ),
                axis=0,
            )
        )

    target_vector = np.concatenate(
        (target_contrast.imag.ravel(), target_contrast.real.ravel())
    )

    # Remove arbitrary wavelength-independent complex offset separately for each
    # independent device contrast and RF frequency.
    n_contrast = n_device - 1
    n_frequency = len(FREQUENCIES_GHZ)
    n_lambda = len(WAVELENGTHS_UM)
    n_complex_block = n_contrast * n_frequency * n_lambda
    intercepts = []
    for c in range(n_contrast):
        for f_index in range(n_frequency):
            basis = np.zeros((n_contrast, n_frequency, n_lambda))
            basis[c, f_index, :] = 1.0
            intercepts.append(
                np.concatenate((basis.ravel(), np.zeros(n_complex_block)))
            )
            intercepts.append(
                np.concatenate((np.zeros(n_complex_block), basis.ravel()))
            )

    nuisance_matrix = np.column_stack(nuisance_blocks + intercepts)
    residual = project_residual_qr(target_vector, nuisance_matrix)

    target_norm = float(np.linalg.norm(target_vector))
    residual_norm = float(np.linalg.norm(residual))
    score = residual_norm / np.sqrt(n_device * n_lambda)
    angle = float(
        np.degrees(
            np.arcsin(np.clip(residual_norm / target_norm, 0.0, 1.0))
        )
    )
    return score, angle, residual_norm, float(np.min(pabs))


def optimize_series(
    n_device: int,
    drift_order: int,
    cache: dict[float, tuple[np.ndarray, np.ndarray, np.ndarray]],
):
    best = None
    count = 0
    for depths in itertools.combinations(CANDIDATE_DEPTHS_UM, n_device):
        if np.min(np.diff(depths)) < MIN_DEPTH_SPACING_UM - 1.0e-12:
            continue
        rounded = tuple(float(value) for value in depths)
        result = series_score(rounded, cache, drift_order)
        count += 1
        if best is None or result[0] > best[1][0]:
            best = (rounded, result)
    if best is None:
        raise RuntimeError("No admissible series")
    return count, best


def main() -> None:
    all_depths = set(float(value) for value in CANDIDATE_DEPTHS_UM)
    # Include the earlier boundary-safe ideal pair reference explicitly.
    all_depths.update((4.1, 5.6))
    cache = {
        round(depth, 6): response_at_depth(depth)
        for depth in sorted(all_depths)
    }

    ideal_pair = series_score((4.1, 5.6), cache, drift_order=0)

    designs = {}
    for n_device, drift_order in ((3, 1), (4, 2), (5, 2), (6, 2), (7, 3)):
        count, best = optimize_series(n_device, drift_order, cache)
        designs[(n_device, drift_order)] = (count, best)

    print("Same-wafer translated-gradient depth-series design")
    print(
        f"lambda={WAVELENGTHS_UM[0]:.2f}-{WAVELENGTHS_UM[-1]:.2f} um; "
        f"N_lambda={len(WAVELENGTHS_UM)}; beta={BETA:.1f}"
    )
    print(
        "reference ideal 4.1/5.6-um pair, common nuisance only: "
        f"score={ideal_pair[0]:.9f}, angle={ideal_pair[1]:.6f} deg"
    )
    print()

    for key in ((3, 1), (4, 2), (5, 2), (6, 2), (7, 3)):
        count, (depths, result) = designs[key]
        ratio = result[0] / ideal_pair[0]
        print(
            f"N={key[0]}, nuisance lateral polynomial order={key[1]}, "
            f"tested={count}"
        )
        print("  depths um = " + ", ".join(f"{z:.1f}" for z in depths))
        print(
            f"  score={result[0]:.9f}, angle={result[1]:.6f} deg, "
            f"min Pabs={result[3]:.6f}"
        )
        print(f"  score / ideal-pair score = {ratio:.3f}")
        print()

    six_depths, six = designs[(6, 2)][1]
    seven_depths, seven = designs[(7, 3)][1]

    # Regression anchors from the current explicit 0.2-um depth grid.
    assert six_depths == (
        2.0,
        2.4000000000000004,
        2.8000000000000007,
        4.600000000000002,
        5.200000000000003,
        5.600000000000003,
    )
    assert 0.00140 < six[0] < 0.00143
    assert 5.1 < six[1] < 5.4
    assert 0.86 < six[0] / ideal_pair[0] < 0.88

    assert seven_depths == (
        2.0,
        2.4000000000000004,
        2.8000000000000007,
        4.400000000000002,
        4.8000000000000025,
        5.200000000000003,
        5.600000000000003,
    )
    assert 0.00093 < seven[0] < 0.00096
    assert 3.5 < seven[1] < 3.8
    assert 0.57 < seven[0] / ideal_pair[0] < 0.59
    assert min(six[3], seven[3], ideal_pair[3]) > 0.990

    print(
        "PASS: a translated-feature DEPTH SERIES changes the mechanism-control "
        "logic qualitatively. A two-device comparison cannot distinguish the "
        "desired relocation signal from an arbitrary linear device-to-device "
        "nuisance drift. With several depths, however, the predicted nonlinear "
        "dependence on feature position can be tested against smooth lateral "
        "fabrication trends. On the current grid, six selected depths retain "
        "~87% of the ideal perfectly matched pair information amplitude while "
        "allowing every modeled bulk/front/back-interface nuisance amplitude to "
        "vary quadratically across the series; seven depths retain ~58% while "
        "allowing cubic drift. Fabrication of such a same-wafer series remains "
        "an OPEN engineering question rather than a demonstrated HgCdTe MBE process."
    )


if __name__ == "__main__":
    main()
