"""Growth-programmable translated-gradient validation profile.

The preceding conceptual design used a Gaussian modulation of composition slope.
HgCdTe MBE/MOCVD literature instead motivates a profile that can be specified as
piecewise growth segments. This script replaces the Gaussian by a compact smooth
trapezoid in *composition slope* while preserving the same front/back
compositions and total thickness.

Nominal profile
---------------
L = 7.6 um, x_front = 0.55, x_back = 0.32.

The unit feature h(z) has
- total width = 1.0 um,
- 0.10 um linear entrance ramp,
- 0.80 um flat high-gradient segment,
- 0.10 um linear exit ramp.

The slope magnitude is

    s(z) = s0 [1 + a (h(z)-<h>)],  a=4,

so the spatial integral of slope, and therefore both endpoint compositions, are
independent of feature position. The profile remains monotonic. This is a
numerical representation of a programmable graded segment, not a fabrication
recipe.

Measurement/nuisance model is identical to the corrected matched-contact design:
- lambda 2.00-2.80 um, 0.01 um spacing;
- f = 0.25, 0.50, 1, 2, 3 GHz;
- finite-RF deterministic-transit Jacobian, v0=1e5 m/s;
- illustrative 25% feature-supported transport perturbation;
- common matched nuisance shapes: cubic smooth bulk + four near-junction
  exponentials;
- wavelength-independent complex response removed at each RF.

Primary objective is maximum absolute nuisance-orthogonal complex response norm,
not principal angle alone.

No novelty claim and no assertion that the imposed transport perturbation follows
the composition-gradient field in a real detector.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import cumulative_trapezoid

from hgcdte_matched_contact_translated_gradient_design import (
    FREQUENCIES_GHZ,
    L_UM,
    N_FINE,
    POSITION_GRID_UM,
    REFERENCE_NOISE_DEG,
    X_BACK,
    X_FRONT,
    cell_centers,
    gradient_field_v_cm,
    nuisance_spatial_matrix,
    pabs_and_mean_depth,
    phase_projection,
)
from hgcdte_shortwave_finite_rf_jacobian import (
    PERTURBATION_FRACTION,
    Q0_PS_PER_UM,
    center_wavelength,
    finite_rf_jacobian,
    project_residual,
    response_matrix,
    target_vector,
)

FEATURE_TOTAL_WIDTH_UM = 1.0
FEATURE_RAMP_UM = 0.10
SLOPE_MODULATION = 4.0


def programmed_feature(z_um: np.ndarray, z0_um: float) -> np.ndarray:
    """Compact unit-height trapezoid with linear 0.1-um edge ramps."""
    half = 0.5 * FEATURE_TOTAL_WIDTH_UM
    flat_half = half - FEATURE_RAMP_UM
    distance = np.abs(z_um - z0_um)

    h = np.zeros_like(z_um)
    h[distance <= flat_half] = 1.0
    transition = (distance > flat_half) & (distance < half)
    h[transition] = (
        half - distance[transition]
    ) / FEATURE_RAMP_UM
    return h


def programmed_profile(z0_um: float):
    z = np.linspace(0.0, L_UM, N_FINE)
    h = programmed_feature(z, z0_um)
    h_mean = float(np.trapezoid(h, z) / L_UM)

    base_slope = (X_FRONT - X_BACK) / L_UM
    slope = base_slope * (1.0 + SLOPE_MODULATION * (h - h_mean))
    if np.min(slope) <= 0.0:
        raise RuntimeError("Programmed profile is no longer monotonic")

    x = X_FRONT - np.concatenate(([0.0], cumulative_trapezoid(slope, z)))
    return z, x, h, slope


def transport_delta_q(z: np.ndarray, support_fine: np.ndarray) -> np.ndarray:
    centers = cell_centers()
    support = np.interp(centers, z, support_fine)
    support /= np.max(support)
    return Q0_PS_PER_UM * (
        1.0 / (1.0 - PERTURBATION_FRACTION * support) - 1.0
    )


def pair_metrics(z1_um: float, z2_um: float):
    z1, x1, h1, slope1 = programmed_profile(z1_um)
    z2, x2, h2, slope2 = programmed_profile(z2_um)

    J1, H1 = finite_rf_jacobian(z1, x1, FREQUENCIES_GHZ)
    J2, H2 = finite_rf_jacobian(z2, x2, FREQUENCIES_GHZ)

    dq1 = transport_delta_q(z1, h1)
    dq2 = transport_delta_q(z2, h2)
    target_response = (
        np.einsum("flj,j->fl", J2, dq2)
        - np.einsum("flj,j->fl", J1, dq1)
    )

    spatial = nuisance_spatial_matrix()
    common_response = np.einsum("flj,jk->flk", J2 - J1, spatial)

    target_complex = target_vector(target_response, "complex")
    common_complex = response_matrix(common_response, "complex")
    complex_angle, complex_residual = project_residual(
        target_complex, common_complex
    )

    target_phase = target_vector(target_response, "phase")
    common_phase = response_matrix(common_response, "phase")
    phase_angle, phase_residual_deg = phase_projection(
        target_phase, common_phase
    )

    independent_complex = np.column_stack(
        (
            response_matrix(
                np.einsum("flj,jk->flk", J2, spatial), "complex"
            ),
            response_matrix(
                np.einsum("flj,jk->flk", J1, spatial), "complex"
            ),
        )
    )
    independent_complex_angle, independent_complex_residual = project_residual(
        target_complex, independent_complex
    )

    independent_phase = np.column_stack(
        (
            response_matrix(
                np.einsum("flj,jk->flk", J2, spatial), "phase"
            ),
            response_matrix(
                np.einsum("flj,jk->flk", J1, spatial), "phase"
            ),
        )
    )
    independent_phase_angle, independent_phase_residual = phase_projection(
        target_phase, independent_phase
    )

    centered = center_wavelength(target_response[..., None])[..., 0]
    f1_index = FREQUENCIES_GHZ.index(1.0)
    phase_1ghz_pp_deg = float(
        np.ptp(np.degrees(centered[f1_index].imag))
    )

    pabs1, mean1 = pabs_and_mean_depth(z1, x1)
    pabs2, mean2 = pabs_and_mean_depth(z2, x2)

    field1 = gradient_field_v_cm(x1, slope1)
    field2 = gradient_field_v_cm(x2, slope2)

    return {
        "z1": z1_um,
        "z2": z2_um,
        "field1_min": float(np.min(field1)),
        "field1_max": float(np.max(field1)),
        "field2_min": float(np.min(field2)),
        "field2_max": float(np.max(field2)),
        "min_pabs": float(min(np.min(pabs1), np.min(pabs2))),
        "min_abs_H": float(min(np.min(np.abs(H1)), np.min(np.abs(H2)))),
        "mean_depth_2um": (float(mean1[0]), float(mean2[0])),
        "mean_depth_2p8um": (float(mean1[-1]), float(mean2[-1])),
        "phase_1ghz_pp_deg": phase_1ghz_pp_deg,
        "complex_angle_deg": complex_angle,
        "complex_residual": complex_residual,
        "phase_angle_deg": phase_angle,
        "phase_residual_deg": phase_residual_deg,
        "independent_complex_angle_deg": independent_complex_angle,
        "independent_complex_residual": independent_complex_residual,
        "independent_phase_angle_deg": independent_phase_angle,
        "independent_phase_residual_deg": independent_phase_residual,
    }


def main() -> None:
    candidates = []
    for i, z1 in enumerate(POSITION_GRID_UM):
        for z2 in POSITION_GRID_UM[i + 1 :]:
            if z2 - z1 < 0.4 - 1.0e-12:
                continue
            candidates.append(pair_metrics(float(z1), float(z2)))

    best_residual = max(candidates, key=lambda row: row["complex_residual"])
    best_angle = max(candidates, key=lambda row: row["complex_angle_deg"])

    print("Programmed translated-gradient matched-control design")
    print(
        f"feature total width={FEATURE_TOTAL_WIDTH_UM:.2f} um, "
        f"edge ramp={FEATURE_RAMP_UM:.2f} um, "
        f"modulation={SLOPE_MODULATION:.1f}"
    )
    print(f"candidate pairs = {len(candidates)}")
    print()

    print(
        "best nuisance-orthogonal-signal pair = "
        f"{best_residual['z1']:.2f} -> {best_residual['z2']:.2f} um"
    )
    print(
        "  field range device 1 = "
        f"{best_residual['field1_min']:.1f}-"
        f"{best_residual['field1_max']:.1f} V/cm"
    )
    print(
        "  field range device 2 = "
        f"{best_residual['field2_min']:.1f}-"
        f"{best_residual['field2_max']:.1f} V/cm"
    )
    print(f"  minimum Pabs = {best_residual['min_pabs']:.6f}")
    print(f"  minimum |H| = {best_residual['min_abs_H']:.6f}")
    print(
        "  mean generation depths @2.00 um = "
        f"{best_residual['mean_depth_2um'][0]:.3f}, "
        f"{best_residual['mean_depth_2um'][1]:.3f} um"
    )
    print(
        "  mean generation depths @2.80 um = "
        f"{best_residual['mean_depth_2p8um'][0]:.3f}, "
        f"{best_residual['mean_depth_2p8um'][1]:.3f} um"
    )
    print(
        f"  1-GHz phase p-p = {best_residual['phase_1ghz_pp_deg']:.6f} deg"
    )
    print(
        f"  matched complex angle = {best_residual['complex_angle_deg']:.6f} deg"
    )
    print(
        f"  matched complex residual = {best_residual['complex_residual']:.9f}"
    )
    print(
        f"  matched phase angle = {best_residual['phase_angle_deg']:.6f} deg"
    )
    print(
        f"  matched phase residual = {best_residual['phase_residual_deg']:.6f} deg"
    )
    print(
        f"  independent-nuisance complex angle = "
        f"{best_residual['independent_complex_angle_deg']:.6f} deg"
    )
    print(
        f"  independent-nuisance phase angle = "
        f"{best_residual['independent_phase_angle_deg']:.6f} deg"
    )
    print()

    print(
        "largest angle-only pair = "
        f"{best_angle['z1']:.2f} -> {best_angle['z2']:.2f} um; "
        f"angle={best_angle['complex_angle_deg']:.6f} deg; "
        f"residual={best_angle['complex_residual']:.9f}"
    )

    complex_snr = (
        best_residual["complex_residual"]
        / np.deg2rad(REFERENCE_NOISE_DEG)
    )
    complex_sigma3_deg = np.degrees(best_residual["complex_residual"] / 3.0)
    phase_snr = best_residual["phase_residual_deg"] / REFERENCE_NOISE_DEG
    phase_sigma3_deg = best_residual["phase_residual_deg"] / 3.0
    print()
    print("provisional common-nuisance detection resource")
    print(
        f"  complex SNR @0.10-deg-equivalent component noise = {complex_snr:.3f}"
    )
    print(
        f"  complex 3-sigma component-noise limit = {complex_sigma3_deg:.6f} deg"
    )
    print(
        f"  phase-only SNR @0.10 deg = {phase_snr:.3f}"
    )
    print(
        f"  phase-only 3-sigma sigma_phi limit = {phase_sigma3_deg:.6f} deg"
    )
    print(
        f"  phase-only white-noise time multiplier from 0.10 deg = "
        f"{(REFERENCE_NOISE_DEG / phase_sigma3_deg)**2:.3f}x"
    )

    # Stable regression anchors for the current explicit design.
    assert abs(best_residual["z1"] - 2.6) < 1.0e-12
    assert abs(best_residual["z2"] - 3.2) < 1.0e-12
    assert 213.0 < best_residual["field1_min"] < 216.0
    assert 1950.0 < best_residual["field1_max"] < 1970.0
    assert 1938.0 < best_residual["field2_max"] < 1960.0
    assert best_residual["min_pabs"] > 0.9967
    assert best_residual["min_abs_H"] > 0.987
    assert 0.183 < best_residual["phase_1ghz_pp_deg"] < 0.185
    assert 14.39 < best_residual["complex_angle_deg"] < 14.42
    assert 0.00786 < best_residual["complex_residual"] < 0.00789
    assert 8.74 < best_residual["phase_angle_deg"] < 8.77
    assert 0.274 < best_residual["phase_residual_deg"] < 0.277
    assert 0.23 < best_residual["independent_complex_angle_deg"] < 0.24
    assert 0.052 < best_residual["independent_phase_angle_deg"] < 0.054

    assert abs(best_angle["z1"] - 1.4) < 1.0e-12
    assert abs(best_angle["z2"] - 1.8) < 1.0e-12
    assert 22.0 < best_angle["complex_angle_deg"] < 22.03
    assert best_angle["complex_residual"] < best_residual["complex_residual"]

    assert complex_snr > 4.50
    assert 0.149 < complex_sigma3_deg < 0.152
    assert 2.74 < phase_snr < 2.77
    assert 0.091 < phase_sigma3_deg < 0.093

    print()
    print(
        "PASS: replacing the Gaussian slope perturbation with a compact, "
        "piecewise-programmable 1-um graded segment preserves the 2.6->3.2 um "
        "residual-signal optimum and substantially increases separation from "
        "common matched bulk/contact nuisance responses. Under the current "
        "optimistic complex-noise convention the illustrative signal exceeds "
        "3 sigma already at 0.10-deg-equivalent component noise. Independent "
        "device-specific nuisance amplitudes still collapse the separation, so "
        "matched fabrication remains essential."
    )


if __name__ == "__main__":
    main()
