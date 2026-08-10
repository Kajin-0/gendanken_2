"""Calibration-prior requirement for the short-wave sample-A contrast experiment.

The 2.0-2.8 um scan gives much more raw phase leverage on sample A's retained
nonlinear/high-field region than the mid/deep scan. But paired A-B data also
contain smooth transport contributions from both devices. This script asks how
well those smooth contributions must be calibrated before an A-localized
contrast becomes statistically distinguishable.

Model
-----
- 300 K, lambda = 2.00-2.80 um in 0.01 um steps (81 wavelengths).
- All 72 sample-A composition sensitivity profiles.
- Current central sample-B Hansen/Moazzami Beer-Lambert optical model.
- A-localized illustrative transport perturbation:
      v(z)=1e5 m/s * [1 - 0.25 w_A(z)]
  where w_A is the normalized nonlinear-gradient-field excess support.
  This is an illustrative visibility target, NOT a device prediction and NOT
  an assumption that transport is proportional to field.
- Six smooth nuisance modes: first three short-wave transport modes of A plus
  first three short-wave transport modes of B.
- Common wavelength-independent phase projected out.
- Each anomaly/nuisance spectral response column is normalized to RMS=1.
  Therefore its coefficient has units of phase RMS [deg] over the wavelength
  grid. A nuisance prior sigma_prior is thus a *phase-equivalent spectral-mode
  prior*, not a microscopic velocity uncertainty.
- Independent equal per-wavelength phase noise, nominally 0.10 deg. This is a
  provisional covariance model only.

The Fisher matrix is

    F = X.T X / sigma_phi^2 + P^{-1},

where only the six nuisance coefficients receive independent Gaussian priors.
The posterior anomaly uncertainty is sqrt[(F^{-1})_00].
"""

from __future__ import annotations

import numpy as np

from hgcdte_sample_a_constraint_family_joint_iso_kernel import (
    optical_kernel,
    sample_a_profiles,
    sample_b_profile,
)
from hgcdte_sample_a_shortwave_visibility import nonlinear_support

LAMBDA_GRID = np.arange(2.00, 2.8001, 0.01)
N_SMOOTH = 3
F_HZ = 1.0e9
V0_M_S = 1.0e5
PERTURBATION_FRACTION = 0.25
NOMINAL_SIGMA_PHASE_DEG = 0.10
PRIOR_SIGMAS_DEG = (0.0, 0.005, 0.010, 0.020, 0.030, 0.050, 0.100)


def project_common(values: np.ndarray) -> np.ndarray:
    """Project wavelength-independent phase from a vector or column matrix."""
    if values.ndim == 1:
        return values - np.mean(values)
    return values - np.mean(values, axis=0, keepdims=True)


def rms(values: np.ndarray) -> float:
    return float(np.sqrt(np.mean(values**2)))


def normalize_rms(values: np.ndarray) -> np.ndarray:
    scale = rms(values)
    if scale <= 0.0:
        raise RuntimeError("Cannot normalize zero spectral response")
    return values / scale


def matrix_for_profile(z_um: np.ndarray, x: np.ndarray) -> np.ndarray:
    return np.asarray(
        [optical_kernel(z_um, x, wavelength, 300.0)[1] for wavelength in LAMBDA_GRID]
    )


def smooth_response_modes(matrix: np.ndarray) -> np.ndarray:
    centered = project_common(matrix)
    _, _, vt = np.linalg.svd(centered, full_matrices=False)
    responses = project_common(matrix @ vt[:N_SMOOTH].T)
    return responses


def physical_anomaly_response(
    matrix_a: np.ndarray,
    z_um: np.ndarray,
    metadata: dict[str, float | str],
) -> tuple[np.ndarray, float]:
    _, _, support = nonlinear_support(z_um, metadata)
    velocity = V0_M_S * (1.0 - PERTURBATION_FRACTION * support)
    delta_q_ps_per_um = 1.0e6 / velocity - 1.0e6 / V0_M_S

    delay_ps = project_common(matrix_a @ delta_q_ps_per_um)
    phase_deg = -360.0 * F_HZ * 1.0e-12 * delay_ps
    return phase_deg, rms(phase_deg)


def principal_angle_deg(target: np.ndarray, nuisance: np.ndarray) -> float:
    """Smallest angle from target vector to the nuisance column subspace."""
    u, singular, _ = np.linalg.svd(nuisance, full_matrices=False)
    rank = int(np.sum(singular > singular[0] * 1.0e-12))
    basis = u[:, :rank]
    cosine = np.linalg.norm(basis.T @ target) / np.linalg.norm(target)
    return float(np.degrees(np.arccos(np.clip(cosine, -1.0, 1.0))))


def design_for_profile(
    matrix_a: np.ndarray,
    matrix_b: np.ndarray,
    z_um: np.ndarray,
    metadata: dict[str, float | str],
) -> tuple[np.ndarray, float, float]:
    response_a = smooth_response_modes(matrix_a)
    response_b = smooth_response_modes(matrix_b)

    phase_anomaly, physical_rms_deg = physical_anomaly_response(
        matrix_a, z_um, metadata
    )

    nuisance = np.column_stack((response_a, -response_b))
    target_shape = normalize_rms(phase_anomaly)
    nuisance_shapes = np.column_stack(
        [normalize_rms(nuisance[:, j]) for j in range(nuisance.shape[1])]
    )

    angle = principal_angle_deg(target_shape, nuisance_shapes)
    design = np.column_stack((target_shape, nuisance_shapes))
    return design, physical_rms_deg, angle


def anomaly_sigma_deg(
    design: np.ndarray,
    sigma_phase_deg: float,
    nuisance_prior_deg: float,
) -> float:
    """Posterior 1-sigma anomaly phase-RMS amplitude."""
    if nuisance_prior_deg == 0.0:
        # Limit of perfectly known nuisance amplitudes.
        return float(sigma_phase_deg / np.linalg.norm(design[:, 0]))

    fisher = design.T @ design / sigma_phase_deg**2
    fisher[1:, 1:] += np.eye(design.shape[1] - 1) / nuisance_prior_deg**2
    covariance = np.linalg.inv(fisher)
    return float(np.sqrt(covariance[0, 0]))


def family_snr(
    designs: list[np.ndarray],
    physical_rms: np.ndarray,
    sigma_phase_deg: float,
    nuisance_prior_deg: float,
) -> tuple[np.ndarray, np.ndarray]:
    sigmas = np.asarray(
        [
            anomaly_sigma_deg(design, sigma_phase_deg, nuisance_prior_deg)
            for design in designs
        ]
    )
    return sigmas, physical_rms / sigmas


def max_noise_for_worst_case_three_sigma(
    designs: list[np.ndarray],
    physical_rms: np.ndarray,
    nuisance_prior_deg: float,
) -> float:
    """Largest equal per-wavelength sigma_phi giving min family SNR >= 3."""
    low = 1.0e-5
    high = 0.20

    # If even the near-zero-noise end does not reach 3 sigma, return NaN.
    _, snr_low = family_snr(
        designs, physical_rms, low, nuisance_prior_deg
    )
    if np.min(snr_low) < 3.0:
        return float("nan")

    for _ in range(70):
        midpoint = 0.5 * (low + high)
        _, snr_mid = family_snr(
            designs, physical_rms, midpoint, nuisance_prior_deg
        )
        if np.min(snr_mid) >= 3.0:
            low = midpoint
        else:
            high = midpoint
    return float(low)


def main() -> None:
    b_z, b_x = sample_b_profile()
    matrix_b = matrix_for_profile(b_z, b_x)

    designs: list[np.ndarray] = []
    physical_rms = []
    angles = []

    for z_um, x, metadata in sample_a_profiles():
        matrix_a = matrix_for_profile(z_um, x)
        design, signal_rms, angle = design_for_profile(
            matrix_a, matrix_b, z_um, metadata
        )
        designs.append(design)
        physical_rms.append(signal_rms)
        angles.append(angle)

    physical_rms = np.asarray(physical_rms)
    angles = np.asarray(angles)

    print("Short-wave A-localized contrast: smooth-mode calibration requirement")
    print(f"wavelengths = {len(LAMBDA_GRID)} ({LAMBDA_GRID[0]:.2f}-{LAMBDA_GRID[-1]:.2f} um)")
    print(f"sample-A profiles = {len(designs)}")
    print(
        "principal angle of anomaly response to six-mode smooth nuisance subspace: "
        f"{angles.min():.6f}-{angles.max():.6f} deg, "
        f"median={np.median(angles):.6f} deg"
    )
    print(
        "illustrative 25% anomaly physical phase RMS @1 GHz: "
        f"{physical_rms.min():.6f}-{physical_rms.max():.6f} deg, "
        f"median={np.median(physical_rms):.6f} deg"
    )
    print()

    stored = {}
    for prior in PRIOR_SIGMAS_DEG:
        sigmas, snr = family_snr(
            designs,
            physical_rms,
            NOMINAL_SIGMA_PHASE_DEG,
            prior,
        )
        stored[prior] = (sigmas, snr)
        label = "known nuisance" if prior == 0.0 else f"prior={prior:.3f} deg"
        print(label)
        print(
            f"  posterior anomaly sigma = {sigmas.min():.6f}-"
            f"{sigmas.max():.6f} deg, median={np.median(sigmas):.6f}"
        )
        print(
            f"  detection SNR = {snr.min():.3f}-"
            f"{snr.max():.3f}, median={np.median(snr):.3f}"
        )
        print(f"  fraction >=3 sigma = {np.mean(snr >= 3.0):.3f}")
    print()

    print("per-wavelength sigma_phi required for >=3 sigma over all 72 profiles")
    thresholds = {}
    for prior in (0.0, 0.002, 0.005):
        threshold = max_noise_for_worst_case_three_sigma(
            designs, physical_rms, prior
        )
        thresholds[prior] = threshold
        label = "known nuisance" if prior == 0.0 else f"prior={prior:.3f} deg"
        print(f"  {label}: sigma_phi <= {threshold:.6f} deg")

    # Stable numerical regressions.
    assert 0.006 < angles.min() < 0.007
    assert 0.70 < angles.max() < 0.72
    assert 0.028 < np.median(angles) < 0.031

    assert 0.0314 < physical_rms.min() < 0.0316
    assert 0.1205 < physical_rms.max() < 0.1207
    assert 0.0650 < np.median(physical_rms) < 0.0653

    sig0, snr0 = stored[0.0]
    assert np.allclose(sig0, 1.0 / 90.0, rtol=1.0e-10, atol=1.0e-12)
    assert 2.82 < snr0.min() < 2.84
    assert 5.85 < np.median(snr0) < 5.87
    assert 0.91 < np.mean(snr0 >= 3.0) < 0.92

    sig005, snr005 = stored[0.005]
    assert 0.01316 < sig005.min() < 0.01318
    assert 2.38 < snr005.min() < 2.40
    assert 4.93 < np.median(snr005) < 4.96
    assert 0.79 < np.mean(snr005 >= 3.0) < 0.80

    sig01, snr01 = stored[0.010]
    assert 0.01796 < sig01.min() < 0.01799
    assert 1.74 < snr01.min() < 1.76
    assert 3.61 < np.median(snr01) < 3.63
    assert np.mean(snr01 >= 3.0) == 0.50

    _, snr03 = stored[0.030]
    assert snr03.max() < 2.77
    assert np.mean(snr03 >= 3.0) == 0.0

    assert 0.0943 < thresholds[0.0] < 0.0945
    assert 0.0908 < thresholds[0.002] < 0.0910
    assert 0.0696 < thresholds[0.005] < 0.0698

    print()
    print(
        "PASS: the short-wave scan raises raw A-localized phase visibility, "
        "but the anomaly response lies almost inside the six-mode smooth A/B "
        "spectral subspace. Detectability therefore depends critically on "
        "calibrating/constraining those smooth modes; at 0.10 deg measurement "
        "noise a 0.01-deg phase-equivalent nuisance prior gives only 50% of "
        "the current profile family >=3 sigma for the illustrative 25% anomaly."
    )


if __name__ == "__main__":
    main()
