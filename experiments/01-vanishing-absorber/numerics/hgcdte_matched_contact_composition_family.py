"""Explicit monotonic matched-contact composition family for validation devices.

Purpose
-------
Translate the abstract buried-feature optimum into a composition profile that
preserves the collection-side semiconductor environment and both composition
endpoints.

Control:
    L = 7.6 um, x_front = 0.40, x_back = 0.32, linear x(z).

Contrast family:
    dx/dz = -(Delta x/L) * w_beta(z)

    w_beta(z) = 1 + beta G(z) - c_beta H(z)

where G is a buried Gaussian gradient enhancement centered at 4.9 um and H is
a smooth compensation window that turns on only after ~1.5 um. c_beta is chosen
so int_0^L w_beta dz = L exactly. Hence every profile has identical x_front,
x_back, and total thickness. Because G and H are negligible near the front, the
first ~1 um of x(z) and dx/dz remains essentially identical to the control.

The compensation is not a proposed growth recipe. It is a smooth mathematical
construction proving that a buried gradient contrast can coexist with matched
front/contact conditions and monotonic composition.

The family beta=(1,3,5) gives progressively stronger buried composition-gradient
fields while remaining monotonic. Finite-RF mechanism separation is evaluated
with separate smooth A/B bulk terms plus a matched-contact nuisance whose same
spatial perturbation acts in both devices. Statistics-like and additive-like
Pabs weighting are included.

No microscopic law relating composition-gradient field to carrier velocity is
assumed. The positive field excess is used only as a spatial support template.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import cumulative_trapezoid

from hgcdte_sample_a_constraint_family_joint_iso_kernel import (
    HC_EV_UM,
    N_CELL,
    alpha_moazzami,
    deg_dx_hansen,
    eg_hansen,
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
FEATURE_SIGMA_UM = 0.35
COMPENSATION_START_UM = 1.50
COMPENSATION_SMOOTH_UM = 0.15
BETA_VALUES = (1.0, 3.0, 5.0)

LAMBDA_CANDIDATE = np.arange(2.80, 3.9001, 0.01)
PABS_MIN = 0.05
FREQUENCIES_GHZ = (0.25, 0.50, 1.0, 2.0, 3.0)
CONTACT_SCALES_UM = (0.20, 0.50, 0.75, 1.00)


def control_profile() -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    z = np.linspace(0.0, L_UM, N_FINE)
    x = X_FRONT - DELTA_X * z / L_UM
    dx_dz = np.full_like(z, -DELTA_X / L_UM)
    field = np.abs(deg_dx_hansen(x, 300.0) * dx_dz * 1.0e4)
    return z, x, dx_dz, field


def contrast_profile(
    beta: float,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, float, np.ndarray]:
    z = np.linspace(0.0, L_UM, N_FINE)

    G = np.exp(
        -0.5 * ((z - FEATURE_CENTER_UM) / FEATURE_SIGMA_UM) ** 2
    )
    H = 0.5 * (
        1.0
        + np.tanh(
            (z - COMPENSATION_START_UM) / COMPENSATION_SMOOTH_UM
        )
    )

    integral_G = float(np.trapezoid(G, z))
    integral_H = float(np.trapezoid(H, z))
    c_beta = beta * integral_G / integral_H

    weight = 1.0 + beta * G - c_beta * H
    integral_weight = np.concatenate(
        ([0.0], cumulative_trapezoid(weight, z))
    )

    # By construction integral(weight)=L, so both composition endpoints match.
    x = X_FRONT - (DELTA_X / L_UM) * integral_weight
    dx_dz = -(DELTA_X / L_UM) * weight
    field = np.abs(deg_dx_hansen(x, 300.0) * dx_dz * 1.0e4)

    return z, x, dx_dz, field, c_beta, weight


def p_absorption(z_um: np.ndarray, x: np.ndarray, wavelength_um: float) -> float:
    alpha = alpha_moazzami(HC_EV_UM / wavelength_um, x, 300.0)
    tau = float(np.trapezoid(alpha, z_um * 1.0e-4))
    return float(1.0 - np.exp(-tau))


def cell_centers() -> np.ndarray:
    edges = np.linspace(0.0, L_UM, N_CELL + 1)
    return 0.5 * (edges[:-1] + edges[1:])


def matched_geometry_metrics(beta: float, exponent: float):
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
        (
            np.ones(N_CELL),
            centers / L_UM,
            (centers / L_UM) ** 2,
        )
    )
    contact = np.column_stack(
        [np.exp(-centers / scale) for scale in CONTACT_SCALES_UM]
    )

    # Allow independent smooth bulk changes in control/contrast, but treat the
    # contact perturbation as matched: the same spatial contact change acts in
    # each device, and only their optical/Jacobian difference survives pairing.
    smooth_contrast = response_matrix(
        np.einsum("flj,jk->flk", J1, smooth), "complex"
    )
    smooth_control = response_matrix(
        np.einsum("flj,jk->flk", J0, smooth), "complex"
    )
    contact_difference = response_matrix(
        np.einsum("flj,jk->flk", J1, contact)
        - np.einsum("flj,jk->flk", J0, contact),
        "complex",
    )

    nuisance = np.column_stack(
        (smooth_contrast, smooth_control, contact_difference)
    )
    target = target_vector(np.einsum("flj,j->fl", J1, support), "complex")

    # Conservative paired-signal proxy: whiten with the weaker absorbed signal.
    whitening_lambda = np.minimum(p0, p1) ** exponent
    per_frequency = np.tile(whitening_lambda, len(FREQUENCIES_GHZ))
    whitening = np.concatenate((per_frequency, per_frequency))

    angle, residual_norm = project_residual(
        target * whitening,
        nuisance * whitening[:, None],
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

    front = z <= 1.0
    peak_index = int(np.argmax(field1))

    return {
        "beta": beta,
        "c_beta": c_beta,
        "weight_min": float(np.min(weight)),
        "peak_field": float(np.max(field1)),
        "minimum_field": float(np.min(field1)),
        "peak_x": float(x1[peak_index]),
        "peak_z": float(z[peak_index]),
        "max_x_difference": float(np.max(np.abs(x1 - x0))),
        "front_x_difference": float(np.max(np.abs(x1[front] - x0[front]))),
        "front_gradient_fraction": float(
            np.max(np.abs(weight[front] - 1.0))
        ),
        "support_centroid": centroid,
        "support_rms_width": rms_width,
        "lambda_max": float(wavelengths[-1]),
        "pabs_contrast_min": float(np.min(p1)),
        "max_kernel_mismatch": float(np.max(kernel_mismatch)),
        "angle": angle,
        "residual_norm": residual_norm,
        "target_norm": target_norm,
    }


def main() -> None:
    z, x0, _, field0 = control_profile()
    baseline_field = float(np.median(field0))

    # Exact monotonicity ceiling from the broad compensation region where
    # G~0 and H~1: c_beta < 1.
    _, _, _, _, c_unit, _ = contrast_profile(1.0)
    beta_monotonic_ceiling = 1.0 / c_unit

    print("Matched-contact monotonic buried-gradient composition family")
    print(
        f"control: x={X_FRONT:.3f}->{X_BACK:.3f}, L={L_UM:.1f} um, "
        f"median field={baseline_field:.2f} V/cm"
    )
    print(
        f"buried gradient center={FEATURE_CENTER_UM:.2f} um, "
        f"Gaussian sigma={FEATURE_SIGMA_UM:.2f} um"
    )
    print(
        f"compensation turns on after ~{COMPENSATION_START_UM:.2f} um; "
        f"strict monotonic beta ceiling ~{beta_monotonic_ceiling:.3f}"
    )
    print()

    stored = {}
    for beta in BETA_VALUES:
        stats = matched_geometry_metrics(beta, exponent=0.5)
        additive = matched_geometry_metrics(beta, exponent=1.0)
        stored[beta] = (stats, additive)

        print(f"beta={beta:.0f}")
        print(
            f"  peak/min field = {stats['peak_field']:.2f}/"
            f"{stats['minimum_field']:.2f} V/cm at z~{stats['peak_z']:.3f} um"
        )
        print(
            f"  peak local x={stats['peak_x']:.6f}, "
            f"local gap lambda={HC_EV_UM/eg_hansen(stats['peak_x'],300.0):.4f} um"
        )
        print(
            f"  max |Delta x|={stats['max_x_difference']:.6f}; "
            f"max front-1um |Delta x|={stats['front_x_difference']:.3e}; "
            f"front gradient mismatch={100*stats['front_gradient_fraction']:.4f}%"
        )
        print(
            f"  field-excess support centroid={stats['support_centroid']:.3f} um, "
            f"RMS width={stats['support_rms_width']:.3f} um"
        )
        print(
            f"  max control/contrast optical-kernel mismatch="
            f"{100*stats['max_kernel_mismatch']:.2f}%"
        )
        print(
            f"  statistics-like: angle={stats['angle']:.4f} deg, "
            f"recoverable residual={stats['residual_norm']:.9f}"
        )
        print(
            f"  additive-like:   angle={additive['angle']:.4f} deg, "
            f"recoverable residual={additive['residual_norm']:.9f}"
        )
        print()

    # Regression anchors for the middle-strength validation candidate.
    stats3, add3 = stored[3.0]
    assert 506.1 < stats3["peak_field"] < 506.4
    assert 80.4 < stats3["minimum_field"] < 80.7
    assert stats3["weight_min"] > 0.56
    assert stats3["front_x_difference"] < 4.4e-7
    assert stats3["front_gradient_fraction"] < 5.5e-4
    assert 0.0115 < stats3["max_x_difference"] < 0.0118
    assert 4.89 < stats3["support_centroid"] < 4.91
    assert 0.26 < stats3["support_rms_width"] < 0.28
    assert 0.21 < stats3["max_kernel_mismatch"] < 0.22
    assert 0.71 < stats3["angle"] < 0.73
    assert 0.73 < add3["angle"] < 0.74

    # Dose-response field ladder.
    assert 263.1 < stored[1.0][0]["peak_field"] < 263.5
    assert 749.0 < stored[5.0][0]["peak_field"] < 749.5
    assert beta_monotonic_ceiling > 6.9

    print(
        "PASS: a strictly monotonic family can keep both composition endpoints "
        "fixed and preserve the first ~1 um near the collecting contact to "
        "sub-1e-6 composition while moving a controllable gradient enhancement "
        "to ~4.9 um depth. The beta=1/3/5 ladder gives buried peak fields of "
        "~263/506/749 V/cm. This establishes a physically constrained matched-"
        "contact validation geometry; it does not yet establish a microscopic "
        "transport response or a fabrication recipe."
    )


if __name__ == "__main__":
    main()
