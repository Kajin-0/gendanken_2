"""Matched-contact buried-gradient family with downstream-only compensation.

This supersedes the earlier broad compensation construction as the preferred
validation thought-device geometry.

Control:
    L=7.6 um, x_front=0.40, x_back=0.32, linear composition.

Contrast:
    w_beta(z) = 1 + beta G(z) - c_beta H_back(z)
    dx/dz = -(Delta x/L) w_beta(z)

G is a narrow buried gradient enhancement centered at 4.90 um with sigma=0.20
um. H_back is a smooth step that turns on around 5.70 um, i.e. BEHIND the
feature relative to collection at z=0. c_beta enforces int w dz=L exactly.

This placement is important: carriers generated around the buried feature
travel toward z=0 and see the enhanced-gradient region but do not traverse the
compensating low-gradient region behind it. The first ~4.2 um of the profile is
essentially identical to the control.

The family beta=(1,2,3) remains strictly monotonic. The positive gradient-field
excess is used only as a spatial support template; no field->velocity law is
assumed in this file.

Finite-RF complex separation is evaluated against independent smooth A/B bulk
terms plus a MATCHED contact nuisance whose same near-junction perturbation acts
in both devices. Statistics-like and additive-like Pabs weighting are included.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import cumulative_trapezoid

from hgcdte_sample_a_constraint_family_joint_iso_kernel import (
    HC_EV_UM,
    N_CELL,
    alpha_moazzami,
    deg_dx_hansen,
    optical_kernel,
)
from hgcdte_shortwave_finite_rf_jacobian import (
    finite_rf_jacobian,
    response_matrix,
    target_vector,
    project_residual,
)

L_UM = 7.6
X_FRONT = 0.40
X_BACK = 0.32
DELTA_X = X_FRONT - X_BACK
N_FINE = 4001

FEATURE_CENTER_UM = 4.90
FEATURE_SIGMA_UM = 0.20
COMPENSATION_CENTER_UM = 5.70
COMPENSATION_SMOOTH_UM = 0.12
BETA_VALUES = (1.0, 2.0, 3.0)

LAMBDA_CANDIDATE = np.arange(2.80, 3.9001, 0.01)
PABS_MIN = 0.05
FREQUENCIES_GHZ = (0.25, 0.50, 1.0, 2.0, 3.0)
CONTACT_SCALES_UM = (0.20, 0.50, 0.75, 1.00)


def control_profile():
    z = np.linspace(0.0, L_UM, N_FINE)
    x = X_FRONT - DELTA_X * z / L_UM
    dx_dz = np.full_like(z, -DELTA_X / L_UM)
    field = np.abs(deg_dx_hansen(x, 300.0) * dx_dz * 1.0e4)
    return z, x, dx_dz, field


def contrast_profile(beta: float):
    z = np.linspace(0.0, L_UM, N_FINE)
    G = np.exp(-0.5 * ((z - FEATURE_CENTER_UM) / FEATURE_SIGMA_UM) ** 2)
    H = 0.5 * (
        1.0
        + np.tanh(
            (z - COMPENSATION_CENTER_UM) / COMPENSATION_SMOOTH_UM
        )
    )

    c_beta = beta * float(np.trapezoid(G, z)) / float(np.trapezoid(H, z))
    weight = 1.0 + beta * G - c_beta * H

    integral_weight = np.concatenate(
        ([0.0], cumulative_trapezoid(weight, z))
    )
    x = X_FRONT - (DELTA_X / L_UM) * integral_weight
    dx_dz = -(DELTA_X / L_UM) * weight
    field = np.abs(deg_dx_hansen(x, 300.0) * dx_dz * 1.0e4)
    return z, x, dx_dz, field, c_beta, weight


def p_absorption(z_um, x, wavelength_um):
    alpha = alpha_moazzami(HC_EV_UM / wavelength_um, x, 300.0)
    tau = float(np.trapezoid(alpha, z_um * 1.0e-4))
    return float(1.0 - np.exp(-tau))


def cell_centers():
    edges = np.linspace(0.0, L_UM, N_CELL + 1)
    return 0.5 * (edges[:-1] + edges[1:])


def metrics(beta: float, exponent: float):
    z, x0, _, field0 = control_profile()
    _, x1, _, field1, c_beta, weight = contrast_profile(beta)

    p0 = np.asarray(
        [p_absorption(z, x0, wavelength) for wavelength in LAMBDA_CANDIDATE]
    )
    p1 = np.asarray(
        [p_absorption(z, x1, wavelength) for wavelength in LAMBDA_CANDIDATE]
    )
    keep = (p0 >= PABS_MIN) & (p1 >= PABS_MIN)
    wavelengths = LAMBDA_CANDIDATE[keep]
    p0 = p0[keep]
    p1 = p1[keep]

    J0, _ = finite_rf_jacobian(
        z, x0, FREQUENCIES_GHZ, wavelengths=wavelengths
    )
    J1, _ = finite_rf_jacobian(
        z, x1, FREQUENCIES_GHZ, wavelengths=wavelengths
    )

    centers = cell_centers()
    field0_cell = np.interp(centers, z, field0)
    field1_cell = np.interp(centers, z, field1)
    support = np.maximum(field1_cell - field0_cell, 0.0)
    support /= np.max(support)

    smooth = np.column_stack(
        (np.ones(N_CELL), centers / L_UM, (centers / L_UM) ** 2)
    )
    contact = np.column_stack(
        [np.exp(-centers / scale) for scale in CONTACT_SCALES_UM]
    )

    smooth_1 = response_matrix(
        np.einsum("flj,jk->flk", J1, smooth), "complex"
    )
    smooth_0 = response_matrix(
        np.einsum("flj,jk->flk", J0, smooth), "complex"
    )
    matched_contact = response_matrix(
        np.einsum("flj,jk->flk", J1, contact)
        - np.einsum("flj,jk->flk", J0, contact),
        "complex",
    )

    nuisance = np.column_stack((smooth_1, smooth_0, matched_contact))
    target = target_vector(np.einsum("flj,j->fl", J1, support), "complex")

    whitening_lambda = np.minimum(p0, p1) ** exponent
    one_block = np.tile(whitening_lambda, len(FREQUENCIES_GHZ))
    whitening = np.concatenate((one_block, one_block))

    angle, residual_norm = project_residual(
        target * whitening, nuisance * whitening[:, None]
    )
    target_norm = float(np.linalg.norm(target * whitening))

    kernel_mismatch = []
    for wavelength in wavelengths:
        _, row0 = optical_kernel(z, x0, wavelength, 300.0)
        _, row1 = optical_kernel(z, x1, wavelength, 300.0)
        kernel_mismatch.append(
            np.linalg.norm(row1 - row0) / np.linalg.norm(row0)
        )

    centroid = float(np.sum(centers * support) / np.sum(support))
    rms_width = float(
        np.sqrt(
            np.sum((centers - centroid) ** 2 * support) / np.sum(support)
        )
    )

    front1 = z <= 1.0
    prefeature = z <= 4.2
    peak_index = int(np.argmax(field1))

    return {
        "c_beta": c_beta,
        "weight_min": float(np.min(weight)),
        "peak_field": float(np.max(field1)),
        "minimum_field": float(np.min(field1)),
        "peak_z": float(z[peak_index]),
        "peak_x": float(x1[peak_index]),
        "max_x_difference": float(np.max(np.abs(x1 - x0))),
        "front1_x_difference": float(np.max(np.abs(x1[front1] - x0[front1]))),
        "prefeature_x_difference": float(
            np.max(np.abs(x1[prefeature] - x0[prefeature]))
        ),
        "support_centroid": centroid,
        "support_rms_width": rms_width,
        "max_kernel_mismatch": float(np.max(kernel_mismatch)),
        "pabs_contrast_min": float(np.min(p1)),
        "lambda_max": float(wavelengths[-1]),
        "angle": angle,
        "residual_norm": residual_norm,
        "target_norm": target_norm,
    }


def main() -> None:
    z, x0, _, field0 = control_profile()
    _, _, _, _, c_unit, _ = contrast_profile(1.0)
    beta_ceiling = 1.0 / c_unit

    print("Matched-contact downstream-compensated buried-gradient family")
    print(
        f"control x={X_FRONT:.3f}->{X_BACK:.3f}, L={L_UM:.1f} um, "
        f"median field={np.median(field0):.2f} V/cm"
    )
    print(
        f"feature center={FEATURE_CENTER_UM:.2f} um, sigma={FEATURE_SIGMA_UM:.2f} um"
    )
    print(
        f"compensation begins near {COMPENSATION_CENTER_UM:.2f} um; "
        f"monotonic beta ceiling ~{beta_ceiling:.3f}"
    )
    print()

    stored = {}
    for beta in BETA_VALUES:
        stats = metrics(beta, 0.5)
        additive = metrics(beta, 1.0)
        stored[beta] = (stats, additive)

        print(f"beta={beta:.0f}")
        print(
            f"  peak/min field={stats['peak_field']:.2f}/"
            f"{stats['minimum_field']:.2f} V/cm"
        )
        print(
            f"  max |Delta x|={stats['max_x_difference']:.6f}; "
            f"front-1um mismatch={stats['front1_x_difference']:.3e}; "
            f"through-4.2um mismatch={stats['prefeature_x_difference']:.3e}"
        )
        print(
            f"  support center/RMS width={stats['support_centroid']:.3f}/"
            f"{stats['support_rms_width']:.3f} um"
        )
        print(
            f"  max optical-kernel mismatch={100*stats['max_kernel_mismatch']:.2f}%"
        )
        print(
            f"  statistics-like angle={stats['angle']:.4f} deg, "
            f"residual={stats['residual_norm']:.9f}"
        )
        print(
            f"  additive-like angle={additive['angle']:.4f} deg, "
            f"residual={additive['residual_norm']:.9f}"
        )
        print()

    s1, a1 = stored[1.0]
    s2, a2 = stored[2.0]
    s3, a3 = stored[3.0]

    assert 283.5 < s1["peak_field"] < 283.8
    assert 425.2 < s2["peak_field"] < 425.5
    assert 566.8 < s3["peak_field"] < 567.2

    assert 104.1 < s1["minimum_field"] < 104.5
    assert 66.7 < s2["minimum_field"] < 67.1
    assert 29.3 < s3["minimum_field"] < 29.8
    assert s3["weight_min"] > 0.20
    assert beta_ceiling > 3.78

    assert s3["front1_x_difference"] < 1.0e-12
    assert s3["prefeature_x_difference"] < 3.7e-6
    assert 4.89 < s3["support_centroid"] < 4.91
    assert 0.19 < s3["support_rms_width"] < 0.21

    assert 0.08 < s1["max_kernel_mismatch"] < 0.09
    assert 0.15 < s2["max_kernel_mismatch"] < 0.16
    assert 0.22 < s3["max_kernel_mismatch"] < 0.23

    assert 1.90 < s1["angle"] < 1.92
    assert 1.68 < s2["angle"] < 1.70
    assert 1.45 < s3["angle"] < 1.47
    assert 1.51 < a1["angle"] < 1.52
    assert 1.39 < a3["angle"] < 1.41

    print(
        "PASS: moving the endpoint compensation behind the buried feature keeps "
        "the collection-side path essentially identical to the control while "
        "preserving strict monotonicity. The beta=1/2/3 ladder gives ~284/425/"
        "567 V/cm buried peaks, and its realistic-weighted complex fingerprints "
        "remain ~1.4-1.9 deg away from the matched-contact/smooth-bulk nuisance "
        "span. This supersedes the earlier broad-compensation construction as "
        "the preferred matched-contact thought-device family."
    )


if __name__ == "__main__":
    main()
