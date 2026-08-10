"""Can mid/deep or combined spectral data self-calibrate the short-wave A baseline?

The short-wave A-localized anomaly is almost degenerate with three smooth A and
three smooth B transport modes. Previous design notes treated those smooth-mode
amplitudes as externally calibrated priors. This script asks whether the needed
A smooth-mode knowledge can instead be obtained from the existing mid/deep
spectral branch, or from one broad 2.00-3.83 um phase fit with no smooth priors.

Two diagnostics are reported over all 72 sample-A profile-family members:

1. Mid/deep -> short-wave A-mode transfer.
   Define the first three short-wave A spatial SVD modes and normalize each so
   its short-wave spectral response has RMS one. Fit those same modes using
   only 2.80-3.83 um A phase data at 0.10 deg equal noise. The resulting
   coefficient uncertainty is directly in short-wave-equivalent RMS degrees.

2. Broad self-calibration.
   Use 2.00-3.83 um phase data to fit simultaneously one A-localized anomaly,
   three short-wave-defined A smooth modes, three short-wave-defined B smooth
   modes, and one common phase intercept, with no smooth-mode priors.

No real-device anomaly amplitude, covariance validation, or novelty claim.
"""

from __future__ import annotations

import numpy as np

from hgcdte_sample_a_constraint_family_joint_iso_kernel import (
    optical_kernel,
    sample_a_profiles,
    sample_b_profile,
)
from hgcdte_sample_a_shortwave_calibration_prior import (
    F_HZ,
    LAMBDA_GRID,
    NOMINAL_SIGMA_PHASE_DEG,
    PERTURBATION_FRACTION,
    V0_M_S,
    normalize_rms,
    project_common,
)
from hgcdte_sample_a_shortwave_visibility import nonlinear_support

MID_LAMBDA = np.arange(2.80, 3.8301, 0.01)
ALL_LAMBDA = np.arange(2.00, 3.8301, 0.01)
N_SMOOTH = 3


def matrix_grid(z_um: np.ndarray, x: np.ndarray, wavelengths: np.ndarray):
    return np.asarray(
        [
            optical_kernel(z_um, x, float(wavelength), 300.0)[1]
            for wavelength in wavelengths
        ]
    )


def normalized_shortwave_spatial_modes(matrix_short: np.ndarray):
    centered = project_common(matrix_short)
    _, _, vt = np.linalg.svd(centered, full_matrices=False)
    modes = vt[:N_SMOOTH].T
    responses = centered @ modes
    response_rms = np.sqrt(np.mean(responses**2, axis=0))
    return modes / response_rms[None, :]


def middeep_a_mode_uncertainty(
    z_um: np.ndarray,
    x: np.ndarray,
    sigma_phi_deg: float = NOMINAL_SIGMA_PHASE_DEG,
):
    matrix_short = matrix_grid(z_um, x, LAMBDA_GRID)
    modes = normalized_shortwave_spatial_modes(matrix_short)

    matrix_mid = matrix_grid(z_um, x, MID_LAMBDA)
    responses_mid = project_common(matrix_mid) @ modes

    fisher = responses_mid.T @ responses_mid / sigma_phi_deg**2
    covariance = np.linalg.inv(fisher)
    return np.sqrt(np.diag(covariance))


def combined_self_calibration(
    z_um: np.ndarray,
    x: np.ndarray,
    metadata: dict[str, float | str],
    b_z: np.ndarray,
    b_x: np.ndarray,
    b_modes: np.ndarray,
    sigma_phi_deg: float = NOMINAL_SIGMA_PHASE_DEG,
):
    matrix_short_a = matrix_grid(z_um, x, LAMBDA_GRID)
    a_modes = normalized_shortwave_spatial_modes(matrix_short_a)

    matrix_all_a = matrix_grid(z_um, x, ALL_LAMBDA)
    matrix_all_b = matrix_grid(b_z, b_x, ALL_LAMBDA)

    response_a = matrix_all_a @ a_modes
    response_b = matrix_all_b @ b_modes

    _, _, support = nonlinear_support(z_um, metadata)
    velocity = V0_M_S * (1.0 - PERTURBATION_FRACTION * support)
    delta_q = 1.0e6 / velocity - 1.0e6 / V0_M_S
    phase_all = -360.0 * F_HZ * 1.0e-12 * (matrix_all_a @ delta_q)

    phase_short = project_common(phase_all[: len(LAMBDA_GRID)])
    physical_short_rms = float(np.sqrt(np.mean(phase_short**2)))
    anomaly_shape = phase_all / physical_short_rms

    design = np.column_stack(
        (
            anomaly_shape,
            response_a,
            -response_b,
            np.ones(len(ALL_LAMBDA)),
        )
    )

    fisher = design.T @ design / sigma_phi_deg**2
    covariance = np.linalg.inv(fisher)
    anomaly_sigma = float(np.sqrt(covariance[0, 0]))
    anomaly_snr = physical_short_rms / anomaly_sigma

    nuisance = design[:, 1:]
    u, singular, _ = np.linalg.svd(nuisance, full_matrices=False)
    rank = int(np.sum(singular > singular[0] * 1.0e-12))
    basis = u[:, :rank]
    cosine = np.linalg.norm(basis.T @ design[:, 0]) / np.linalg.norm(design[:, 0])
    angle = float(np.degrees(np.arccos(np.clip(cosine, -1.0, 1.0))))

    return anomaly_snr, angle


def main() -> None:
    b_z, b_x = sample_b_profile()
    b_short = matrix_grid(b_z, b_x, LAMBDA_GRID)
    b_modes = normalized_shortwave_spatial_modes(b_short)

    a_mode_sigma = []
    broad_snr = []
    broad_angle = []

    for z_um, x, metadata in sample_a_profiles():
        a_mode_sigma.append(middeep_a_mode_uncertainty(z_um, x))
        snr, angle = combined_self_calibration(
            z_um,
            x,
            metadata,
            b_z,
            b_x,
            b_modes,
        )
        broad_snr.append(snr)
        broad_angle.append(angle)

    a_mode_sigma = np.asarray(a_mode_sigma)
    broad_snr = np.asarray(broad_snr)
    broad_angle = np.asarray(broad_angle)

    print("Mid/deep A calibration -> short-wave-equivalent smooth-mode sigma")
    for mode in range(N_SMOOTH):
        values = a_mode_sigma[:, mode]
        print(
            f"mode {mode+1}: min/median/max = "
            f"{np.min(values):.6f}/{np.median(values):.6f}/"
            f"{np.max(values):.6f} deg"
        )
        print(
            f"  fraction <=0.005 deg = {np.mean(values <= 0.005):.3f}"
        )

    worst_mode_per_profile = np.max(a_mode_sigma, axis=1)
    sigma_needed_mid = (
        NOMINAL_SIGMA_PHASE_DEG
        * 0.005
        / worst_mode_per_profile
    )
    print()
    print(
        "mid/deep per-wavelength sigma_phi needed so all three A modes reach "
        "0.005 deg in each profile:"
    )
    print(
        f"  min/median/max across profiles = "
        f"{np.min(sigma_needed_mid):.9f}/"
        f"{np.median(sigma_needed_mid):.9f}/"
        f"{np.max(sigma_needed_mid):.9f} deg"
    )

    print()
    print("Broad 2.00-3.83 um no-prior self-calibration")
    print(
        f"anomaly SNR @0.10 deg per wavelength: "
        f"{np.min(broad_snr):.6f}-{np.max(broad_snr):.6f}, "
        f"median={np.median(broad_snr):.6f}"
    )
    print(
        f"anomaly angle to smooth+common nuisance span: "
        f"{np.min(broad_angle):.6f}-{np.max(broad_angle):.6f} deg, "
        f"median={np.median(broad_angle):.6f}"
    )

    required_sigma = NOMINAL_SIGMA_PHASE_DEG * broad_snr / 3.0
    print(
        "equal per-wavelength sigma_phi required for 3-sigma anomaly "
        "detection profile-by-profile:"
    )
    print(
        f"  min/median/max = {np.min(required_sigma):.9f}/"
        f"{np.median(required_sigma):.9f}/"
        f"{np.max(required_sigma):.9f} deg"
    )
    print(
        "  worst-profile white-noise time multiplier relative to 0.10 deg = "
        f"{(NOMINAL_SIGMA_PHASE_DEG / np.min(required_sigma))**2:.1f}"
    )

    # Regression anchors.
    assert 0.27 < np.min(a_mode_sigma[:, 0]) < 0.28
    assert 1.12 < np.median(a_mode_sigma[:, 0]) < 1.13
    assert 4.91 < np.max(a_mode_sigma[:, 0]) < 4.92

    assert np.mean(a_mode_sigma[:, 0] <= 0.005) == 0.0
    assert np.mean(a_mode_sigma[:, 1] <= 0.005) == 0.0

    assert 0.061 < np.min(broad_snr) < 0.062
    assert 0.134 < np.median(broad_snr) < 0.135
    assert np.max(broad_snr) < 0.565

    assert 0.00205 < np.min(required_sigma) < 0.00206
    assert 2300.0 < (
        NOMINAL_SIGMA_PHASE_DEG / np.min(required_sigma)
    ) ** 2 < 2400.0

    print()
    print(
        "PASS: mid/deep A phase data are far too weakly coupled to the leading "
        "short-wave A smooth mode to supply a ~0.005-deg prior at the current "
        "phase-noise scale. A broad no-prior spectral self-fit is also severely "
        "ill-conditioned. Independent physical calibration/constraints or a "
        "causal differential perturbation that cancels the static A baseline "
        "is therefore required; simply adding spectral points is not enough."
    )


if __name__ == "__main__":
    main()
