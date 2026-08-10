"""Self-consistent matched-contact translated-gradient validation design.

Purpose
-------
The published sample-A nonlinear region lies close to the collecting interface,
where spectral timing is both gauge-like and strongly confounded with contact
transport. This script asks a constructive device-design question:

    Can the same localized composition-gradient enhancement be translated to
    two buried depths while keeping the front/back compositions identical, and
    does the resulting wavelength x RF response become distinguishable from
    common matched contact/bulk nuisance changes?

This is a conceptual design study, not a fabrication recipe or device
prediction.

Profile construction
--------------------
Use a 7.6 um monotonic HgCdTe composition profile with fixed endpoints

    x(0) = 0.55,  x(L) = 0.32.

The local composition-slope magnitude is

    s(z) = s0 * [1 + a (g(z;z0,sigma) - <g>)],

where g is a Gaussian. Subtracting the spatial mean keeps the total composition
change, and therefore both endpoint compositions, exactly fixed while moving the
internal gradient enhancement. With sigma=0.35 um and a=4 the local Hansen-gap
gradient field is about 1.9 kV/cm, close to the scale motivating the published
sample-A branch, while the surrounding field is about 220 V/cm.

Measurement model
-----------------
- lambda = 2.00-2.80 um in 0.01 um steps;
- f = 0.25, 0.5, 1, 2, 3 GHz;
- finite-RF deterministic-transit Jacobian, baseline v0 = 1e5 m/s;
- illustrative 25% support-shaped transport perturbation;
- phase + log-magnitude complex response;
- wavelength-independent complex response removed separately at each RF.

Matched nuisance stress
-----------------------
Common fabrication/contact changes use one shared amplitude in both devices for
spatial templates

    1, z/L, (z/L)^2, (z/L)^3,
    exp(-z/0.30), exp(-z/0.50), exp(-z/0.75), exp(-z/1.00).

Their differential response is therefore (J2-J1) q_nuis. A second, deliberately
adversarial stress allows those nuisance amplitudes to vary independently in the
two devices. The large difference between these cases quantifies why matched
fabrication is scientifically essential.

The primary design objective is the *absolute nuisance-orthogonal complex
response norm*, not principal angle alone. A large angle with very small raw
signal is not automatically the best experiment.

No novelty claim.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import cumulative_trapezoid

from hgcdte_sample_a_constraint_family_joint_iso_kernel import (
    HC_EV_UM,
    N_CELL,
    alpha_moazzami,
    deg_dx_hansen,
)
from hgcdte_shortwave_finite_rf_jacobian import (
    LAMBDA_GRID,
    PERTURBATION_FRACTION,
    Q0_PS_PER_UM,
    center_wavelength,
    finite_rf_jacobian,
    generation_probabilities,
    project_residual,
    response_matrix,
    target_vector,
)

L_UM = 7.6
X_FRONT = 0.55
X_BACK = 0.32
N_FINE = 4001
SIGMA_UM = 0.35
SLOPE_MODULATION = 4.0
FREQUENCIES_GHZ = (0.25, 0.50, 1.0, 2.0, 3.0)
POSITION_GRID_UM = np.arange(0.8, 3.2001, 0.2)
REFERENCE_NOISE_DEG = 0.10


def translated_profile(z0_um: float):
    z = np.linspace(0.0, L_UM, N_FINE)
    g = np.exp(-0.5 * ((z - z0_um) / SIGMA_UM) ** 2)
    g_mean = float(np.trapezoid(g, z) / L_UM)

    base_slope = (X_FRONT - X_BACK) / L_UM
    slope = base_slope * (1.0 + SLOPE_MODULATION * (g - g_mean))
    if np.min(slope) <= 0.0:
        raise RuntimeError("Profile is no longer monotonic")

    x = X_FRONT - np.concatenate(([0.0], cumulative_trapezoid(slope, z)))
    return z, x, g, slope


def gradient_field_v_cm(x: np.ndarray, slope_um_inv: np.ndarray) -> np.ndarray:
    return np.abs(deg_dx_hansen(x, 300.0) * slope_um_inv * 1.0e4)


def cell_centers() -> np.ndarray:
    edges = np.linspace(0.0, L_UM, N_CELL + 1)
    return 0.5 * (edges[:-1] + edges[1:])


def transport_delta_q(z: np.ndarray, g: np.ndarray) -> np.ndarray:
    centers = cell_centers()
    support = np.interp(centers, z, g)
    support /= np.max(support)
    return Q0_PS_PER_UM * (
        1.0 / (1.0 - PERTURBATION_FRACTION * support) - 1.0
    )


def nuisance_spatial_matrix() -> np.ndarray:
    z = cell_centers()
    u = z / L_UM
    return np.column_stack(
        (
            np.ones(N_CELL),
            u,
            u**2,
            u**3,
            np.exp(-z / 0.30),
            np.exp(-z / 0.50),
            np.exp(-z / 0.75),
            np.exp(-z / 1.00),
        )
    )


def phase_projection(target: np.ndarray, nuisance: np.ndarray):
    theta, residual = project_residual(target, nuisance)
    return theta, float(np.degrees(residual))


def pabs_and_mean_depth(z: np.ndarray, x: np.ndarray):
    """Return modeled absorption probability and conditional mean depth."""
    pabs = []
    means = []
    z_cm = z * 1.0e-4
    for wavelength in LAMBDA_GRID:
        probability, centers, _ = generation_probabilities(
            z, x, float(wavelength)
        )
        alpha = alpha_moazzami(HC_EV_UM / float(wavelength), x, 300.0)
        tau = np.concatenate(([0.0], cumulative_trapezoid(alpha, z_cm)))
        pabs.append(float(1.0 - np.exp(-tau[-1])))
        means.append(float(probability @ centers))
    return np.asarray(pabs), np.asarray(means)


def pair_metrics(z1_um: float, z2_um: float):
    z1, x1, g1, slope1 = translated_profile(z1_um)
    z2, x2, g2, slope2 = translated_profile(z2_um)

    J1, H1 = finite_rf_jacobian(z1, x1, FREQUENCIES_GHZ)
    J2, H2 = finite_rf_jacobian(z2, x2, FREQUENCIES_GHZ)

    dq1 = transport_delta_q(z1, g1)
    dq2 = transport_delta_q(z2, g2)
    response = (
        np.einsum("flj,j->fl", J2, dq2)
        - np.einsum("flj,j->fl", J1, dq1)
    )

    spatial = nuisance_spatial_matrix()

    # Common matched nuisance amplitudes.
    common_response = np.einsum("flj,jk->flk", J2 - J1, spatial)
    target_complex = target_vector(response, "complex")
    common_complex = response_matrix(common_response, "complex")
    common_complex_angle, common_complex_residual = project_residual(
        target_complex, common_complex
    )

    target_phase = target_vector(response, "phase")
    common_phase = response_matrix(common_response, "phase")
    common_phase_angle, common_phase_residual = phase_projection(
        target_phase, common_phase
    )

    # Adversarial independent nuisance amplitudes in the two devices.
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

    centered = center_wavelength(response[..., None])[..., 0]
    f1_index = FREQUENCIES_GHZ.index(1.0)
    phase_1ghz_deg = np.degrees(centered[f1_index].imag)

    pabs1, mean1 = pabs_and_mean_depth(z1, x1)
    pabs2, mean2 = pabs_and_mean_depth(z2, x2)

    field1 = gradient_field_v_cm(x1, slope1)
    field2 = gradient_field_v_cm(x2, slope2)

    return {
        "z1": z1_um,
        "z2": z2_um,
        "field1_max": float(np.max(field1)),
        "field2_max": float(np.max(field2)),
        "min_pabs": float(min(np.min(pabs1), np.min(pabs2))),
        "min_abs_H": float(min(np.min(np.abs(H1)), np.min(np.abs(H2)))),
        "mean_depth_2um": (float(mean1[0]), float(mean2[0])),
        "mean_depth_2p8um": (float(mean1[-1]), float(mean2[-1])),
        "phase_1ghz_pp_deg": float(np.ptp(phase_1ghz_deg)),
        "common_complex_angle_deg": common_complex_angle,
        "common_complex_residual": common_complex_residual,
        "common_phase_angle_deg": common_phase_angle,
        "common_phase_residual_deg": common_phase_residual,
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

    # Primary objective: maximum absolute nuisance-orthogonal complex signal.
    best_residual = max(
        candidates, key=lambda row: row["common_complex_residual"]
    )
    # Geometry-only diagnostic: maximum principal angle can occur elsewhere.
    best_angle = max(
        candidates, key=lambda row: row["common_complex_angle_deg"]
    )

    print("Matched-contact translated-gradient pair design")
    print(
        f"fixed endpoints x_front={X_FRONT:.3f}, x_back={X_BACK:.3f}, "
        f"L={L_UM:.1f} um"
    )
    print(
        f"gradient feature sigma={SIGMA_UM:.2f} um, "
        f"modulation a={SLOPE_MODULATION:.1f}"
    )
    print(f"candidate pairs = {len(candidates)}")
    print()

    print(
        "best nuisance-orthogonal-signal pair = "
        f"{best_residual['z1']:.2f} -> {best_residual['z2']:.2f} um"
    )
    print(
        "  local field maxima = "
        f"{best_residual['field1_max']:.1f}, "
        f"{best_residual['field2_max']:.1f} V/cm"
    )
    print(f"  minimum Pabs = {best_residual['min_pabs']:.6f}")
    print(f"  minimum |H| = {best_residual['min_abs_H']:.6f}")
    print(
        "  mean generation depth @2.00 um = "
        f"{best_residual['mean_depth_2um'][0]:.3f}, "
        f"{best_residual['mean_depth_2um'][1]:.3f} um"
    )
    print(
        "  mean generation depth @2.80 um = "
        f"{best_residual['mean_depth_2p8um'][0]:.3f}, "
        f"{best_residual['mean_depth_2p8um'][1]:.3f} um"
    )
    print(
        f"  1-GHz differential phase p-p = "
        f"{best_residual['phase_1ghz_pp_deg']:.6f} deg"
    )
    print(
        f"  matched common nuisance: complex angle = "
        f"{best_residual['common_complex_angle_deg']:.6f} deg, "
        f"residual = {best_residual['common_complex_residual']:.9f}"
    )
    print(
        f"  matched common nuisance: phase angle = "
        f"{best_residual['common_phase_angle_deg']:.6f} deg, "
        f"residual norm = {best_residual['common_phase_residual_deg']:.6f} deg"
    )
    print(
        f"  independent nuisance stress: complex angle = "
        f"{best_residual['independent_complex_angle_deg']:.6f} deg"
    )
    print(
        f"  independent nuisance stress: phase angle = "
        f"{best_residual['independent_phase_angle_deg']:.6f} deg"
    )
    print()
    print(
        "largest geometry-only complex angle occurs at "
        f"{best_angle['z1']:.2f} -> {best_angle['z2']:.2f} um: "
        f"angle={best_angle['common_complex_angle_deg']:.6f} deg, "
        f"residual={best_angle['common_complex_residual']:.9f}"
    )

    complex_noise_rad = np.deg2rad(REFERENCE_NOISE_DEG)
    complex_snr = best_residual["common_complex_residual"] / complex_noise_rad
    phase_snr = best_residual["common_phase_residual_deg"] / REFERENCE_NOISE_DEG
    complex_sigma_3 = np.degrees(
        best_residual["common_complex_residual"] / 3.0
    )
    phase_sigma_3 = best_residual["common_phase_residual_deg"] / 3.0
    print()
    print("illustrative no-prior noise resource under matched nuisances")
    print(
        f"  if phase and ln|H| components each have 0.10-deg-equivalent noise: "
        f"complex SNR={complex_snr:.3f}"
    )
    print(
        f"  3-sigma equivalent complex-component noise <= "
        f"{complex_sigma_3:.6f} deg"
    )
    print(
        f"  white-noise time multiplier from 0.10 deg = "
        f"{(REFERENCE_NOISE_DEG / complex_sigma_3)**2:.2f}x"
    )
    print(
        f"  phase-only SNR @0.10 deg = {phase_snr:.3f}; "
        f"3-sigma sigma_phi <= {phase_sigma_3:.6f} deg"
    )
    print(
        f"  phase-only white-noise time multiplier = "
        f"{(REFERENCE_NOISE_DEG / phase_sigma_3)**2:.1f}x"
    )

    assert abs(best_residual["z1"] - 2.6) < 1.0e-12
    assert abs(best_residual["z2"] - 3.2) < 1.0e-12
    assert abs(best_angle["z1"] - 2.8) < 1.0e-12
    assert abs(best_angle["z2"] - 3.2) < 1.0e-12
    assert 7.15 < best_angle["common_complex_angle_deg"] < 7.18
    assert best_angle["common_complex_residual"] < best_residual[
        "common_complex_residual"
    ]

    assert 1890.0 < best_residual["field1_max"] < 1920.0
    assert 1880.0 < best_residual["field2_max"] < 1910.0
    assert best_residual["min_pabs"] > 0.996
    assert best_residual["min_abs_H"] > 0.987
    assert 0.144 < best_residual["phase_1ghz_pp_deg"] < 0.146
    assert 5.47 < best_residual["common_complex_angle_deg"] < 5.49
    assert 0.00245 < best_residual["common_complex_residual"] < 0.00247
    assert 1.99 < best_residual["common_phase_angle_deg"] < 2.01
    assert 0.051 < best_residual["common_phase_residual_deg"] < 0.052
    assert 0.065 < best_residual["independent_complex_angle_deg"] < 0.067
    assert 0.027 < best_residual["independent_phase_angle_deg"] < 0.028

    print()
    print(
        "PASS: a mean-preserving translated internal gradient can keep the front/"
        "back compositions identical while moving a ~1.9-kV/cm buried feature. "
        "On the stated 2.0-2.8 um / 0.25-3 GHz grid, translating that feature "
        "from 2.6 to 3.2 um maximizes the absolute common-nuisance-orthogonal "
        "complex signal. A 2.8-to-3.2 um pair has a larger principal angle but "
        "a smaller residual signal, demonstrating why angle alone is not the "
        "design objective. The separation collapses if the two devices are "
        "allowed arbitrary independent bulk/contact changes, so matched "
        "fabrication is an identifiability condition."
    )


if __name__ == "__main__":
    main()
