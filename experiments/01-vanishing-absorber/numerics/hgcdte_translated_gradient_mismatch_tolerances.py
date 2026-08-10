"""Mismatch tolerances for the matched-contact translated-gradient pair.

Nominal purpose-built pair:
- L = 7.6 um;
- x_front = 0.55, x_back = 0.32;
- mean-preserving Gaussian slope modulation;
- sigma = 0.35 um, a = 4;
- feature centers z1=2.6 um and z2=3.2 um;
- lambda = 2.00-2.80 um;
- f = 0.25, 0.50, 1, 2, 3 GHz.

The nominal target is the differential response of the same illustrative 25%
transport perturbation translated with the internal gradient feature.

Two questions are asked.

1. Response-space matching requirement.
   Write each nuisance coefficient as

       q2 = c + delta/2,
       q1 = c - delta/2.

   Common c is unconstrained; differential mismatch delta receives a Gaussian
   prior after each mismatch-response column is normalized to RMS=1. The script
   finds the prior required for 3-sigma detection at explicit measurement-noise
   reference points.

2. Unmodelled fabrication-coordinate tolerance.
   Perturb the nominal pair, but still project/fits against the nominal common
   nuisance model. Find the largest symmetric perturbation for which the fitted
   nominal target amplitude remains within +/-10% and the residual-target cosine
   remains >=0.99.

These are model/knowledge tolerances, not guaranteed manufacturing tolerances.
If the realized x(z), feature width, etc. are measured and used in the forward
model, the corresponding fabrication tolerance can be relaxed.

No novelty claim.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import cumulative_trapezoid

from hgcdte_matched_contact_translated_gradient_design import (
    FREQUENCIES_GHZ,
    L_UM,
    N_FINE,
    REFERENCE_NOISE_DEG,
    X_BACK,
    X_FRONT,
    cell_centers,
    nuisance_spatial_matrix,
)
from hgcdte_shortwave_finite_rf_jacobian import (
    LAMBDA_GRID,
    PERTURBATION_FRACTION,
    Q0_PS_PER_UM,
    finite_rf_jacobian,
    project_residual,
    response_matrix,
    target_vector,
)

Z1_UM = 2.6
Z2_UM = 3.2
SIGMA_UM = 0.35
MODULATION = 4.0


def rms(values: np.ndarray) -> float:
    return float(np.sqrt(np.mean(np.asarray(values) ** 2)))


def normalize_columns(matrix: np.ndarray):
    scales = np.sqrt(np.mean(matrix**2, axis=0))
    if np.any(scales <= 0.0):
        raise RuntimeError("Zero nuisance response column")
    return matrix / scales[None, :], scales


def profile(
    z0_um: float,
    sigma_um: float = SIGMA_UM,
    modulation: float = MODULATION,
    x_front: float = X_FRONT,
    x_back: float = X_BACK,
):
    z = np.linspace(0.0, L_UM, N_FINE)
    g = np.exp(-0.5 * ((z - z0_um) / sigma_um) ** 2)
    g_mean = float(np.trapezoid(g, z) / L_UM)
    base_slope = (x_front - x_back) / L_UM
    slope = base_slope * (1.0 + modulation * (g - g_mean))
    if np.min(slope) <= 0.0:
        raise RuntimeError("Nonmonotonic perturbed composition profile")
    x = x_front - np.concatenate(([0.0], cumulative_trapezoid(slope, z)))
    return z, x, g


def delta_q(z: np.ndarray, support_fine: np.ndarray) -> np.ndarray:
    centers = cell_centers()
    support = np.interp(centers, z, support_fine)
    support /= np.max(support)
    return Q0_PS_PER_UM * (
        1.0 / (1.0 - PERTURBATION_FRACTION * support) - 1.0
    )


def pair_forward(
    z1_um: float = Z1_UM,
    z2_um: float = Z2_UM,
    sigma1_um: float = SIGMA_UM,
    sigma2_um: float = SIGMA_UM,
    modulation1: float = MODULATION,
    modulation2: float = MODULATION,
    x_front1: float = X_FRONT,
    x_front2: float = X_FRONT,
    x_back1: float = X_BACK,
    x_back2: float = X_BACK,
):
    z1, x1, g1 = profile(
        z1_um, sigma1_um, modulation1, x_front1, x_back1
    )
    z2, x2, g2 = profile(
        z2_um, sigma2_um, modulation2, x_front2, x_back2
    )
    J1, _ = finite_rf_jacobian(z1, x1, FREQUENCIES_GHZ)
    J2, _ = finite_rf_jacobian(z2, x2, FREQUENCIES_GHZ)
    dq1 = delta_q(z1, g1)
    dq2 = delta_q(z2, g2)
    target = (
        np.einsum("flj,j->fl", J2, dq2)
        - np.einsum("flj,j->fl", J1, dq1)
    )
    return J1, J2, target


def nominal_geometry():
    J1, J2, target = pair_forward()
    spatial = nuisance_spatial_matrix()
    common = np.einsum("flj,jk->flk", J2 - J1, spatial)
    differential = np.einsum(
        "flj,jk->flk", 0.5 * (J2 + J1), spatial
    )
    return J1, J2, target, common, differential


def phase_degrees(response: np.ndarray) -> np.ndarray:
    return np.degrees(target_vector(response, "phase"))


def phase_matrix_degrees(response: np.ndarray) -> np.ndarray:
    return np.degrees(response_matrix(response, "phase"))


def matching_snr_phase(
    target: np.ndarray,
    common: np.ndarray,
    differential: np.ndarray,
    sigma_meas_deg: float,
    sigma_match_deg: float,
):
    target_deg = phase_degrees(target)
    amplitude = rms(target_deg)
    target_shape = target_deg / amplitude
    common_norm, _ = normalize_columns(phase_matrix_degrees(common))
    diff_norm, _ = normalize_columns(phase_matrix_degrees(differential))

    if sigma_match_deg == 0.0:
        design = np.column_stack((target_shape, common_norm))
        fisher = design.T @ design / sigma_meas_deg**2
    else:
        design = np.column_stack((target_shape, common_norm, diff_norm))
        fisher = design.T @ design / sigma_meas_deg**2
        start = 1 + common_norm.shape[1]
        fisher[start:, start:] += (
            np.eye(diff_norm.shape[1]) / sigma_match_deg**2
        )

    covariance = np.linalg.inv(fisher)
    sigma_target = float(np.sqrt(covariance[0, 0]))
    return amplitude / sigma_target


def matching_snr_complex(
    target: np.ndarray,
    common: np.ndarray,
    differential: np.ndarray,
    sigma_meas_eq_deg: float,
    sigma_match_eq_deg: float,
):
    target_complex = target_vector(target, "complex")
    amplitude = rms(target_complex)
    target_shape = target_complex / amplitude
    common_norm, _ = normalize_columns(response_matrix(common, "complex"))
    diff_norm, _ = normalize_columns(
        response_matrix(differential, "complex")
    )

    sigma_meas = np.deg2rad(sigma_meas_eq_deg)
    if sigma_match_eq_deg == 0.0:
        design = np.column_stack((target_shape, common_norm))
        fisher = design.T @ design / sigma_meas**2
    else:
        design = np.column_stack((target_shape, common_norm, diff_norm))
        fisher = design.T @ design / sigma_meas**2
        start = 1 + common_norm.shape[1]
        sigma_match = np.deg2rad(sigma_match_eq_deg)
        fisher[start:, start:] += (
            np.eye(diff_norm.shape[1]) / sigma_match**2
        )

    covariance = np.linalg.inv(fisher)
    sigma_target = float(np.sqrt(covariance[0, 0]))
    return amplitude / sigma_target


def max_match_prior(snr_function, sigma_meas: float) -> float:
    if snr_function(sigma_meas, 0.0) < 3.0:
        return float("nan")
    low = 0.0
    high = 0.20
    for _ in range(70):
        midpoint = 0.5 * (low + high)
        if snr_function(sigma_meas, midpoint) >= 3.0:
            low = midpoint
        else:
            high = midpoint
    return low


def nominal_projector(target: np.ndarray, common: np.ndarray):
    nuisance = response_matrix(common, "complex")
    u, singular, _ = np.linalg.svd(nuisance, full_matrices=False)
    rank = int(np.sum(singular > singular[0] * 1.0e-10))
    basis = u[:, :rank]

    target_vector_nominal = target_vector(target, "complex")
    residual = target_vector_nominal - basis @ (
        basis.T @ target_vector_nominal
    )
    return basis, residual


def compare_to_nominal(
    actual_target: np.ndarray,
    basis: np.ndarray,
    nominal_residual: np.ndarray,
):
    actual = target_vector(actual_target, "complex")
    actual_residual = actual - basis @ (basis.T @ actual)
    denominator = float(nominal_residual @ nominal_residual)
    amplitude = float(nominal_residual @ actual_residual / denominator)
    cosine = float(
        nominal_residual @ actual_residual
        / (np.linalg.norm(nominal_residual) * np.linalg.norm(actual_residual))
    )
    return amplitude, cosine


def tolerance_ok(amplitude: float, cosine: float) -> bool:
    return abs(amplitude - 1.0) <= 0.10 and cosine >= 0.99


def mismatch_targets(parameter: str, magnitude: float):
    targets = []
    for sign in (-1.0, 1.0):
        d = sign * magnitude
        if parameter == "common_position":
            args = {"z1_um": Z1_UM + d, "z2_um": Z2_UM + d}
        elif parameter == "separation":
            args = {
                "z1_um": Z1_UM - d / 2.0,
                "z2_um": Z2_UM + d / 2.0,
            }
        elif parameter == "differential_width":
            args = {
                "sigma1_um": SIGMA_UM - d / 2.0,
                "sigma2_um": SIGMA_UM + d / 2.0,
            }
        elif parameter == "differential_front_x":
            args = {
                "x_front1": X_FRONT - d / 2.0,
                "x_front2": X_FRONT + d / 2.0,
            }
        elif parameter == "differential_back_x":
            args = {
                "x_back1": X_BACK - d / 2.0,
                "x_back2": X_BACK + d / 2.0,
            }
        elif parameter == "differential_modulation":
            args = {
                "modulation1": MODULATION - d / 2.0,
                "modulation2": MODULATION + d / 2.0,
            }
        else:
            raise ValueError(parameter)
        targets.append(pair_forward(**args)[2])
    return targets


def symmetric_tolerance(
    parameter: str,
    initial_high: float,
    basis: np.ndarray,
    nominal_residual: np.ndarray,
):
    def passes(magnitude: float):
        for target in mismatch_targets(parameter, magnitude):
            amplitude, cosine = compare_to_nominal(
                target, basis, nominal_residual
            )
            if not tolerance_ok(amplitude, cosine):
                return False
        return True

    low = 0.0
    high = initial_high
    for _ in range(8):
        if not passes(high):
            break
        high *= 2.0

    for _ in range(45):
        midpoint = 0.5 * (low + high)
        if passes(midpoint):
            low = midpoint
        else:
            high = midpoint
    return low


def main() -> None:
    _, _, target, common, differential = nominal_geometry()

    phase_function = lambda meas, match: matching_snr_phase(
        target, common, differential, meas, match
    )
    complex_function = lambda meas, match: matching_snr_complex(
        target, common, differential, meas, match
    )

    phase_match = max_match_prior(phase_function, 0.010)
    complex_match = max_match_prior(complex_function, 0.030)

    print("Translated-gradient response-space matching requirement")
    print(
        f"phase-only: sigma_meas=0.010 deg -> "
        f"max mismatch prior={phase_match:.9f} deg RMS"
    )
    print(
        f"complex: sigma_meas=0.030-deg-equivalent -> "
        f"max mismatch prior={complex_match:.9f} deg-equivalent RMS"
    )
    print()

    basis, nominal_residual = nominal_projector(target, common)
    settings = {
        "common_position": 0.20,
        "separation": 0.20,
        "differential_width": 0.05,
        "differential_front_x": 0.005,
        "differential_back_x": 0.010,
        "differential_modulation": 0.25,
    }

    tolerances = {}
    print("unmodelled fabrication-coordinate tolerance")
    print("criterion: nominal fitted amplitude within +/-10%, cosine >=0.99")
    for parameter, high in settings.items():
        tolerance = symmetric_tolerance(
            parameter, high, basis, nominal_residual
        )
        tolerances[parameter] = tolerance
        print(f"  {parameter}: {tolerance:.9f}")

    assert 0.00252 < phase_match < 0.00255
    assert 0.00289 < complex_match < 0.00292

    assert 0.116 < tolerances["common_position"] < 0.118
    assert 0.065 < tolerances["separation"] < 0.067
    assert 0.0102 < tolerances["differential_width"] < 0.0105
    assert 0.00130 < tolerances["differential_front_x"] < 0.00135
    assert 0.0071 < tolerances["differential_back_x"] < 0.0074
    assert 0.145 < tolerances["differential_modulation"] < 0.148

    print()
    print(
        "PASS: the purpose-built pair tolerates roughly 0.1-um common feature-"
        "position error and ~0.066-um separation error under the stated model, "
        "but differential feature width and front composition are more demanding. "
        "At the chosen measurement-noise operating points, residual bulk/contact "
        "mismatch modes must be known at a few-millidegree response-equivalent "
        "level. These are knowledge/model tolerances; measured realized profiles "
        "can be inserted into the forward model and need not equal the nominal "
        "design this closely."
    )


if __name__ == "__main__":
    main()
