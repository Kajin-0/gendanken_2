"""Robust two-band design for the short-wave sample-A contrast experiment.

This follows HGCDTE_SAMPLE_A_SHORTWAVE_CALIBRATION_REQUIREMENT.md.

The dense 2.00-2.80 um scan establishes that a localized sample-A nonlinear-
region response is strongly degenerate with six smooth A/B transport nuisance
modes. Here the total coherent averaging resource is held fixed at the amount
used by the 81-point reference scan and is concentrated into two wavelengths.

Because an arbitrary wavelength-independent differential phase remains, a
two-wavelength measurement contains one gauge-free observable: their phase
difference. For fixed total time T=t1+t2 and white phase variance proportional
to 1/t, Var(phi1-phi2)=sigma0^2(1/t1+1/t2), so equal time t1=t2=T/2 is exactly
optimal.

The six smooth-mode coefficients receive independent Gaussian priors with the
same phase-equivalent RMS convention as the preceding calibration calculation.
The exhaustive pair search maximizes the worst-case anomaly detection SNR over
all 72 sample-A profile-family members.

No real-device anomaly amplitude, covariance, or novelty claim.
"""

from __future__ import annotations

import numpy as np

from hgcdte_sample_a_constraint_family_joint_iso_kernel import (
    sample_a_profiles,
    sample_b_profile,
)
from hgcdte_sample_a_shortwave_calibration_prior import (
    LAMBDA_GRID,
    NOMINAL_SIGMA_PHASE_DEG,
    design_for_profile,
    matrix_for_profile,
)

TOTAL_TIME_UNITS = float(len(LAMBDA_GRID))
PRIORS_DEG = (0.0, 0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.010)


def build_family():
    """Return dense normalized design matrices and physical anomaly RMS values."""
    b_z, b_x = sample_b_profile()
    matrix_b = matrix_for_profile(b_z, b_x)

    designs = []
    physical_rms = []
    for z_um, x, metadata in sample_a_profiles():
        matrix_a = matrix_for_profile(z_um, x)
        design, signal_rms, _ = design_for_profile(
            matrix_a, matrix_b, z_um, metadata
        )
        designs.append(design)
        physical_rms.append(signal_rms)

    return np.asarray(designs), np.asarray(physical_rms)


def pair_snr(
    designs: np.ndarray,
    physical_rms: np.ndarray,
    j: int,
    k: int,
    nuisance_prior_deg: float,
    total_time_units: float = TOTAL_TIME_UNITS,
) -> np.ndarray:
    """Detection SNR for an equal-time two-wavelength difference.

    Each dense design column has unit RMS over the 81-point reference grid.
    Column 0 is the A-localized anomaly shape; columns 1: are the six smooth
    A/B nuisance shapes.

    The unknown wavelength-independent phase disappears in the pair
    difference. Independent smooth-mode priors add phase-difference variance

        sigma_prior^2 * ||Delta n||^2.

    With equal time at the two wavelengths, white measurement variance is

        4 sigma0^2 / T.
    """
    delta_h = designs[:, j, 0] - designs[:, k, 0]
    delta_n = designs[:, j, 1:] - designs[:, k, 1:]

    measurement_variance = (
        4.0 * NOMINAL_SIGMA_PHASE_DEG**2 / total_time_units
    )
    nuisance_variance = nuisance_prior_deg**2 * np.sum(delta_n**2, axis=1)
    effective_variance = measurement_variance + nuisance_variance

    anomaly_sigma = np.sqrt(effective_variance) / np.abs(delta_h)
    return physical_rms / anomaly_sigma


def exhaustive_best_pair(
    designs: np.ndarray,
    physical_rms: np.ndarray,
    nuisance_prior_deg: float,
):
    """Maximin pair over the 0.01-um wavelength grid."""
    best = None
    for j in range(len(LAMBDA_GRID) - 1):
        for k in range(j + 1, len(LAMBDA_GRID)):
            snr = pair_snr(
                designs,
                physical_rms,
                j,
                k,
                nuisance_prior_deg,
            )
            record = (
                float(np.min(snr)),
                float(np.median(snr)),
                float(np.max(snr)),
                float(np.mean(snr >= 3.0)),
                j,
                k,
            )
            if best is None or record[0] > best[0]:
                best = record
    return best


def dense_uniform_snr(
    designs: np.ndarray,
    physical_rms: np.ndarray,
    nuisance_prior_deg: float,
    time_multiplier: float = 1.0,
) -> np.ndarray:
    """Dense-scan SNR with an explicit unknown common differential phase."""
    snr = []
    information_scale = time_multiplier / NOMINAL_SIGMA_PHASE_DEG**2

    for design, signal in zip(designs, physical_rms):
        augmented = np.column_stack((design, np.ones(len(LAMBDA_GRID))))
        fisher = information_scale * (augmented.T @ augmented)

        if nuisance_prior_deg > 0.0:
            fisher[1:7, 1:7] += (
                np.eye(6) / nuisance_prior_deg**2
            )
            sigma = float(np.sqrt(np.linalg.inv(fisher)[0, 0]))
        else:
            # Smooth nuisance modes known exactly; only anomaly + intercept fit.
            reduced = augmented[:, [0, 7]]
            reduced_fisher = information_scale * (reduced.T @ reduced)
            sigma = float(np.sqrt(np.linalg.inv(reduced_fisher)[0, 0]))

        snr.append(signal / sigma)

    return np.asarray(snr)


def dense_time_multiplier_for_target(
    designs: np.ndarray,
    physical_rms: np.ndarray,
    nuisance_prior_deg: float,
    target_worst_snr: float,
) -> float:
    """Dense uniform time multiplier needed to match a target worst-case SNR."""
    low = 1.0
    high = 2.0
    while np.min(
        dense_uniform_snr(
            designs, physical_rms, nuisance_prior_deg, high
        )
    ) < target_worst_snr:
        high *= 2.0
        if high > 1.0e8:
            return float("nan")

    for _ in range(50):
        mid = 0.5 * (low + high)
        worst = float(
            np.min(
                dense_uniform_snr(
                    designs, physical_rms, nuisance_prior_deg, mid
                )
            )
        )
        if worst >= target_worst_snr:
            high = mid
        else:
            low = mid
    return high


def robust_prior_threshold(
    designs: np.ndarray,
    physical_rms: np.ndarray,
    target_snr: float = 3.0,
) -> tuple[float, tuple]:
    """Largest smooth-mode prior width for which some pair guarantees target."""
    low = 0.0
    high = 0.012
    best = exhaustive_best_pair(designs, physical_rms, low)

    for _ in range(35):
        mid = 0.5 * (low + high)
        candidate = exhaustive_best_pair(designs, physical_rms, mid)
        if candidate[0] >= target_snr:
            low = mid
            best = candidate
        else:
            high = mid

    return low, best


def main() -> None:
    designs, physical_rms = build_family()

    print("Robust two-band short-wave design")
    print(
        f"dense reference = {len(LAMBDA_GRID)} wavelengths, "
        f"{LAMBDA_GRID[0]:.2f}-{LAMBDA_GRID[-1]:.2f} um"
    )
    print(
        f"total time resource = {TOTAL_TIME_UNITS:.0f} equal dense-point units"
    )
    print(
        "two-band allocation = 50/50 exactly, because the unknown common phase "
        "leaves a single phase-difference observable"
    )
    print(f"sample-A profile family = {len(designs)}")
    print()

    stored = {}
    for prior in PRIORS_DEG:
        best = exhaustive_best_pair(designs, physical_rms, prior)
        stored[prior] = best
        worst, median, maximum, fraction, j, k = best
        print(
            f"prior={prior:.3f} deg: "
            f"lambda=({LAMBDA_GRID[j]:.2f}, {LAMBDA_GRID[k]:.2f}) um; "
            f"SNR min/median/max={worst:.3f}/{median:.3f}/{maximum:.3f}; "
            f"fraction>=3={fraction:.3f}"
        )

    print()
    for prior in (0.002, 0.005, 0.010):
        pair = stored[prior]
        dense = dense_uniform_snr(designs, physical_rms, prior)
        multiplier = dense_time_multiplier_for_target(
            designs, physical_rms, prior, pair[0]
        )
        print(
            f"prior={prior:.3f}: dense worst={np.min(dense):.3f}; "
            f"best-pair worst={pair[0]:.3f}; "
            f"dense time multiplier to match pair={multiplier:.3f}"
        )

    threshold, best_at_threshold = robust_prior_threshold(
        designs, physical_rms
    )
    _, _, _, _, j, k = best_at_threshold
    print()
    print(
        "largest phase-equivalent smooth-mode prior that still permits a "
        f"worst-case 3-sigma two-band design = {threshold:.6f} deg"
    )
    print(
        f"threshold pair ~= ({LAMBDA_GRID[j]:.2f}, "
        f"{LAMBDA_GRID[k]:.2f}) um"
    )

    # Stable regression anchors.
    p002 = stored[0.002]
    p005 = stored[0.005]
    p010 = stored[0.010]

    assert LAMBDA_GRID[p002[4]] == 2.00
    assert 2.719 < LAMBDA_GRID[p002[5]] < 2.721
    assert 4.23 < p002[0] < 4.24
    assert p002[3] == 1.0

    assert LAMBDA_GRID[p005[4]] == 2.00
    assert 2.689 < LAMBDA_GRID[p005[5]] < 2.691
    assert 3.09 < p005[0] < 3.10
    assert p005[3] == 1.0

    assert 2.039 < LAMBDA_GRID[p010[4]] < 2.041
    assert 2.689 < LAMBDA_GRID[p010[5]] < 2.691
    assert 1.95 < p010[0] < 1.97
    assert 0.59 < p010[3] < 0.61

    assert 0.00527 < threshold < 0.00529

    print()
    print(
        "PASS: after explicitly removing the wavelength-independent phase, "
        "the robust fixed-resource short-wave design is genuinely two-band. "
        "At a 0.005-deg smooth-mode prior the 2.00/2.69-um pair moves every "
        "current sample-A profile above 3 sigma for the illustrative anomaly. "
        "At 0.010 deg no two-band pair can do so; calibration, rather than "
        "wavelength count, is the limiting resource in that regime."
    )


if __name__ == "__main__":
    main()
