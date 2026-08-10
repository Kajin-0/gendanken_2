"""Mechanism confounding: nonlinear-gradient support versus contact/bulk changes.

A detected short-wave A-specific timing feature is only scientifically useful if
it can be distinguished from ordinary near-junction/contact and smooth bulk
transport changes. This script uses the finite-RF complex Jacobian from
hgcdte_shortwave_finite_rf_jacobian.py and compares the repository's
illustrative sample-A nonlinear-gradient support with simple physically
motivated nuisance templates.

Data:
- lambda = 2.00-2.80 um, 0.01 um steps;
- f = 0.25, 0.5, 1, 2, 3 GHz;
- phase + log-magnitude;
- wavelength-independent complex response removed separately at each f;
- all 72 sample-A profile-family members;
- central sample-B optical model;
- baseline v0=1e5 m/s.

Nuisance templates:
- A smooth bulk: 1, z/L, (z/L)^2;
- B smooth bulk: 1, z/L, (z/L)^2;
- one effective A near-junction exponential exp(-z/ell_c), with ell_c scanned.

The exponential is an effective transport-artifact support coordinate, NOT a
claim that a real metal/HgCdTe contact physically extends by ell_c.
"""

from __future__ import annotations

import numpy as np

from hgcdte_sample_a_constraint_family_joint_iso_kernel import (
    N_CELL,
    sample_a_profiles,
    sample_b_profile,
)
from hgcdte_sample_a_shortwave_visibility import nonlinear_support
from hgcdte_shortwave_finite_rf_jacobian import (
    PERTURBATION_FRACTION,
    Q0_PS_PER_UM,
    finite_rf_jacobian,
    response_matrix,
    target_vector,
    project_residual,
)

FREQUENCIES_GHZ = (0.25, 0.50, 1.0, 2.0, 3.0)
CONTACT_SCALES_UM = (0.05, 0.10, 0.20, 0.30, 0.50, 0.75, 1.00, 1.50, 2.00)


def centers(length_um: float) -> np.ndarray:
    edges = np.linspace(0.0, length_um, N_CELL + 1)
    return 0.5 * (edges[:-1] + edges[1:])


def complex_response(jacobian: np.ndarray, spatial: np.ndarray) -> np.ndarray:
    """Return centered phase+log-magnitude vector for one spatial template."""
    response = np.einsum("flj,j->fl", jacobian, spatial)
    return target_vector(response, "complex")


def complex_response_matrix(
    jacobian: np.ndarray,
    spatial_matrix: np.ndarray,
) -> np.ndarray:
    response = np.einsum("flj,jk->flk", jacobian, spatial_matrix)
    return response_matrix(response, "complex")


def angle_between(a: np.ndarray, b: np.ndarray) -> float:
    cosine = abs(float(np.dot(a, b))) / (np.linalg.norm(a) * np.linalg.norm(b))
    return float(np.degrees(np.arccos(np.clip(cosine, -1.0, 1.0))))


def main() -> None:
    b_z, b_x = sample_b_profile()
    b_jac, _ = finite_rf_jacobian(b_z, b_x, FREQUENCIES_GHZ)
    z_b = centers(float(b_z[-1]))
    b_bulk = np.column_stack(
        (
            np.ones(N_CELL),
            z_b / b_z[-1],
            (z_b / b_z[-1]) ** 2,
        )
    )
    b_bulk_response = complex_response_matrix(b_jac, b_bulk)

    polynomial_angle = []
    best_contact_angle = []
    best_contact_scale = []
    polynomial_plus_contact = {
        scale: [] for scale in (0.30, 0.50, 0.75, 1.00)
    }

    for a_z, a_x, metadata in sample_a_profiles():
        a_jac, _ = finite_rf_jacobian(a_z, a_x, FREQUENCIES_GHZ)
        z_a = centers(float(a_z[-1]))

        _, _, support = nonlinear_support(a_z, metadata)
        delta_q = Q0_PS_PER_UM * (
            1.0 / (1.0 - PERTURBATION_FRACTION * support) - 1.0
        )
        target = complex_response(a_jac, delta_q)

        a_bulk = np.column_stack(
            (
                np.ones(N_CELL),
                z_a / a_z[-1],
                (z_a / a_z[-1]) ** 2,
            )
        )
        a_bulk_response = complex_response_matrix(a_jac, a_bulk)
        bulk_nuisance = np.column_stack((a_bulk_response, b_bulk_response))

        theta_bulk, _ = project_residual(target, bulk_nuisance)
        polynomial_angle.append(theta_bulk)

        contact_angles = []
        for scale in CONTACT_SCALES_UM:
            contact = np.exp(-z_a / scale)
            contact_response = complex_response(a_jac, contact)
            contact_angles.append(angle_between(target, contact_response))

        contact_angles = np.asarray(contact_angles)
        best = int(np.argmin(contact_angles))
        best_contact_angle.append(float(contact_angles[best]))
        best_contact_scale.append(CONTACT_SCALES_UM[best])

        for scale in polynomial_plus_contact:
            contact = np.exp(-z_a / scale)[:, None]
            contact_response = complex_response_matrix(a_jac, contact)
            nuisance = np.column_stack((bulk_nuisance, contact_response))
            theta, _ = project_residual(target, nuisance)
            polynomial_plus_contact[scale].append(theta)

    polynomial_angle = np.asarray(polynomial_angle)
    best_contact_angle = np.asarray(best_contact_angle)
    best_contact_scale = np.asarray(best_contact_scale)

    print("Mechanism confounding: A nonlinear-region support vs contact/bulk")
    print(f"A profiles = {len(polynomial_angle)}")
    print(f"RF set = {FREQUENCIES_GHZ} GHz")
    print()

    print(
        "A/B quadratic smooth-bulk nuisance angle min/median/max = "
        f"{polynomial_angle.min():.6f}/"
        f"{np.median(polynomial_angle):.6f}/"
        f"{polynomial_angle.max():.6f} deg"
    )
    print(
        "best single A contact-exponential angle min/median/max = "
        f"{best_contact_angle.min():.6f}/"
        f"{np.median(best_contact_angle):.6f}/"
        f"{best_contact_angle.max():.6f} deg"
    )
    scales, counts = np.unique(best_contact_scale, return_counts=True)
    print(
        "best effective contact scale counts = "
        + ", ".join(f"{s:.2f} um:{c}" for s, c in zip(scales, counts))
    )
    print()

    for scale, values in polynomial_plus_contact.items():
        values = np.asarray(values)
        print(
            f"bulk + one A exp(-z/{scale:.2f}um) angle "
            f"min/median/max = {values.min():.9f}/"
            f"{np.median(values):.9f}/{values.max():.9f} deg"
        )

    # Regression anchors from the current sensitivity family.
    assert 0.060 < polynomial_angle.min() < 0.061
    assert 0.159 < np.median(polynomial_angle) < 0.160
    assert 1.94 < polynomial_angle.max() < 1.95

    assert 0.246 < best_contact_angle.min() < 0.248
    assert 1.26 < np.median(best_contact_angle) < 1.27
    assert 3.59 < best_contact_angle.max() < 3.61
    assert set(scales.tolist()) == {0.5, 0.75}

    p05 = np.asarray(polynomial_plus_contact[0.50])
    p075 = np.asarray(polynomial_plus_contact[0.75])
    assert np.median(p05) < 0.015
    assert p05.max() < 0.10
    assert np.median(p075) < 0.009
    assert p075.max() < 0.12

    print()
    print(
        "PASS: the illustrative nonlinear-gradient-region timing fingerprint "
        "is not mechanism-unique. A single effective near-junction exponential "
        "already lies within ~0.25-3.6 deg of the target fingerprint; after "
        "allowing ordinary quadratic A/B bulk changes plus one 0.5-0.75 um "
        "near-junction template, the remaining principal angle is typically "
        "~0.01 deg or less. A detected short-wave A-specific feature therefore "
        "cannot be attributed to the composition-gradient region without an "
        "independent contact/interface control or a purpose-built matched-contact "
        "device pair."
    )


if __name__ == "__main__":
    main()
