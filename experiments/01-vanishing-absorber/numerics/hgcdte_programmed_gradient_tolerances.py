"""Mismatch and profile-knowledge tolerances for the programmed gradient pair.

Nominal purpose-built pair:
- L = 7.6 um;
- x_front = 0.55, x_back = 0.32;
- compact 1.0-um slope feature with 0.10-um edge ramps;
- slope modulation a = 4;
- feature centers z1=2.6 um and z2=3.2 um;
- lambda = 2.00-2.80 um;
- f = 0.25, 0.50, 1, 2, 3 GHz.

Two tolerance classes are reported.

1. Response-space matching. Common smooth/contact nuisance coefficients float
   freely; differential mismatch coefficients receive equal independent Gaussian
   priors after each mismatch-response column is RMS-normalized.

2. Unmodelled profile-coordinate error. The realized pair is perturbed while the
   fit still uses the nominal common-nuisance projector and target. The largest
   symmetric perturbation is reported for which the recovered target amplitude
   stays within +/-10% and the residual fingerprint cosine remains >=0.99.

These are model-knowledge tolerances, not guaranteed manufacturing tolerances.
A measured realized profile can be inserted directly in the forward model.

No novelty claim.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import cumulative_trapezoid

from hgcdte_matched_contact_translated_gradient_design import (
    FREQUENCIES_GHZ,
    L_UM,
    N_FINE,
    X_BACK,
    X_FRONT,
    cell_centers,
    nuisance_spatial_matrix,
)
from hgcdte_programmed_translated_gradient_design import (
    FEATURE_RAMP_UM,
    FEATURE_TOTAL_WIDTH_UM,
    SLOPE_MODULATION,
)
from hgcdte_shortwave_finite_rf_jacobian import (
    PERTURBATION_FRACTION,
    Q0_PS_PER_UM,
    finite_rf_jacobian,
    response_matrix,
    target_vector,
)

Z1_UM = 2.6
Z2_UM = 3.2


def rms(values: np.ndarray) -> float:
    return float(np.sqrt(np.mean(np.asarray(values) ** 2)))


def programmed_feature(
    z_um: np.ndarray,
    z0_um: float,
    total_width_um: float,
    ramp_um: float,
) -> np.ndarray:
    half = 0.5 * total_width_um
    if ramp_um <= 0.0 or ramp_um >= half:
        raise ValueError("ramp must lie between zero and half total width")
    flat_half = half - ramp_um
    distance = np.abs(z_um - z0_um)
    h = np.zeros_like(z_um)
    h[distance <= flat_half] = 1.0
    transition = (distance > flat_half) & (distance < half)
    h[transition] = (half - distance[transition]) / ramp_um
    return h


def profile(
    z0_um: float,
    total_width_um: float = FEATURE_TOTAL_WIDTH_UM,
    ramp_um: float = FEATURE_RAMP_UM,
    modulation: float = SLOPE_MODULATION,
    x_front: float = X_FRONT,
    x_back: float = X_BACK,
):
    z = np.linspace(0.0, L_UM, N_FINE)
    h = programmed_feature(z, z0_um, total_width_um, ramp_um)
    h_mean = float(np.trapezoid(h, z) / L_UM)
    base_slope = (x_front - x_back) / L_UM
    slope = base_slope * (1.0 + modulation * (h - h_mean))
    if np.min(slope) <= 0.0:
        raise RuntimeError("Perturbed programmed profile is nonmonotonic")
    x = x_front - np.concatenate(([0.0], cumulative_trapezoid(slope, z)))
    return z, x, h


def delta_q(z: np.ndarray, h: np.ndarray) -> np.ndarray:
    centers = cell_centers()
    support = np.interp(centers, z, h)
    support /= np.max(support)
    return Q0_PS_PER_UM * (
        1.0 / (1.0 - PERTURBATION_FRACTION * support) - 1.0
    )


def pair_forward(
    z1_um: float = Z1_UM,
    z2_um: float = Z2_UM,
    width1_um: float = FEATURE_TOTAL_WIDTH_UM,
    width2_um: float = FEATURE_TOTAL_WIDTH_UM,
    ramp1_um: float = FEATURE_RAMP_UM,
    ramp2_um: float = FEATURE_RAMP_UM,
    modulation1: float = SLOPE_MODULATION,
    modulation2: float = SLOPE_MODULATION,
    x_front1: float = X_FRONT,
    x_front2: float = X_FRONT,
    x_back1: float = X_BACK,
    x_back2: float = X_BACK,
):
    z1, x1, h1 = profile(
        z1_um, width1_um, ramp1_um, modulation1, x_front1, x_back1
    )
    z2, x2, h2 = profile(
        z2_um, width2_um, ramp2_um, modulation2, x_front2, x_back2
    )
    J1, _ = finite_rf_jacobian(z1, x1, FREQUENCIES_GHZ)
    J2, _ = finite_rf_jacobian(z2, x2, FREQUENCIES_GHZ)
    target = (
        np.einsum("flj,j->fl", J2, delta_q(z2, h2))
        - np.einsum("flj,j->fl", J1, delta_q(z1, h1))
    )
    return J1, J2, target


def normalize_columns(matrix: np.ndarray):
    scales = np.sqrt(np.mean(matrix**2, axis=0))
    if np.any(scales <= 0.0):
        raise RuntimeError("zero response column")
    return matrix / scales[None, :]


def nominal_geometry(mode: str):
    J1, J2, target = pair_forward()
    spatial = nuisance_spatial_matrix()
    common = np.einsum("flj,jk->flk", J2 - J1, spatial)
    differential = np.einsum(
        "flj,jk->flk", 0.5 * (J2 + J1), spatial
    )

    if mode == "phase":
        target_data = np.degrees(target_vector(target, "phase"))
        common_data = np.degrees(response_matrix(common, "phase"))
        diff_data = np.degrees(response_matrix(differential, "phase"))
        conversion = 1.0
    elif mode == "complex":
        target_data = target_vector(target, "complex")
        common_data = response_matrix(common, "complex")
        diff_data = response_matrix(differential, "complex")
        conversion = np.pi / 180.0
    else:
        raise ValueError(mode)

    amplitude = rms(target_data)
    target_shape = target_data / amplitude
    common_norm = normalize_columns(common_data)
    diff_norm = normalize_columns(diff_data)
    return target_shape, amplitude, common_norm, diff_norm, conversion


def snr_with_match_prior(
    mode: str,
    sigma_meas_deg: float,
    sigma_match_deg: float,
) -> float:
    target, amplitude, common, differential, conversion = nominal_geometry(mode)
    sigma_meas = sigma_meas_deg * conversion
    sigma_match = sigma_match_deg * conversion

    design = np.column_stack((target, common, differential))
    fisher = design.T @ design / sigma_meas**2
    start = 1 + common.shape[1]
    if sigma_match_deg == 0.0:
        # Perfect differential matching: remove differential columns entirely.
        design0 = np.column_stack((target, common))
        fisher0 = design0.T @ design0 / sigma_meas**2
        covariance = np.linalg.inv(fisher0)
    else:
        fisher[start:, start:] += (
            np.eye(differential.shape[1]) / sigma_match**2
        )
        covariance = np.linalg.inv(fisher)
    sigma_target = float(np.sqrt(covariance[0, 0]))
    return amplitude / sigma_target


def max_match_prior(mode: str, sigma_meas_deg: float) -> float:
    if snr_with_match_prior(mode, sigma_meas_deg, 0.0) < 3.0:
        return float("nan")
    low, high = 0.0, 0.10
    for _ in range(70):
        midpoint = 0.5 * (low + high)
        if snr_with_match_prior(mode, sigma_meas_deg, midpoint) >= 3.0:
            low = midpoint
        else:
            high = midpoint
    return low


def nominal_projector():
    J1, J2, target = pair_forward()
    common = np.einsum(
        "flj,jk->flk", J2 - J1, nuisance_spatial_matrix()
    )
    nuisance = response_matrix(common, "complex")
    u, singular, _ = np.linalg.svd(nuisance, full_matrices=False)
    rank = int(np.sum(singular > singular[0] * 1.0e-10))
    basis = u[:, :rank]
    target0 = target_vector(target, "complex")
    residual0 = target0 - basis @ (basis.T @ target0)
    return basis, residual0


def compare_to_nominal(target: np.ndarray, basis: np.ndarray, residual0: np.ndarray):
    y = target_vector(target, "complex")
    residual = y - basis @ (basis.T @ y)
    amplitude = float(residual0 @ residual / (residual0 @ residual0))
    cosine = float(
        residual0 @ residual
        / (np.linalg.norm(residual0) * np.linalg.norm(residual))
    )
    return amplitude, cosine


def passes(target: np.ndarray, basis: np.ndarray, residual0: np.ndarray):
    amplitude, cosine = compare_to_nominal(target, basis, residual0)
    return abs(amplitude - 1.0) <= 0.10 and cosine >= 0.99


def mismatch_targets(parameter: str, magnitude: float):
    targets = []
    for sign in (-1.0, 1.0):
        d = sign * magnitude
        if parameter == "common_position":
            kwargs = {"z1_um": Z1_UM + d, "z2_um": Z2_UM + d}
        elif parameter == "separation":
            kwargs = {
                "z1_um": Z1_UM - d / 2.0,
                "z2_um": Z2_UM + d / 2.0,
            }
        elif parameter == "differential_width":
            kwargs = {
                "width1_um": FEATURE_TOTAL_WIDTH_UM - d / 2.0,
                "width2_um": FEATURE_TOTAL_WIDTH_UM + d / 2.0,
            }
        elif parameter == "differential_ramp":
            kwargs = {
                "ramp1_um": FEATURE_RAMP_UM - d / 2.0,
                "ramp2_um": FEATURE_RAMP_UM + d / 2.0,
            }
        elif parameter == "differential_front_x":
            kwargs = {
                "x_front1": X_FRONT - d / 2.0,
                "x_front2": X_FRONT + d / 2.0,
            }
        elif parameter == "differential_back_x":
            kwargs = {
                "x_back1": X_BACK - d / 2.0,
                "x_back2": X_BACK + d / 2.0,
            }
        elif parameter == "differential_modulation":
            kwargs = {
                "modulation1": SLOPE_MODULATION - d / 2.0,
                "modulation2": SLOPE_MODULATION + d / 2.0,
            }
        else:
            raise ValueError(parameter)
        targets.append(pair_forward(**kwargs)[2])
    return targets


def symmetric_tolerance(
    parameter: str,
    initial_high: float,
    basis: np.ndarray,
    residual0: np.ndarray,
):
    def ok(magnitude: float):
        return all(
            passes(target, basis, residual0)
            for target in mismatch_targets(parameter, magnitude)
        )

    low, high = 0.0, initial_high
    for _ in range(8):
        if not ok(high):
            break
        high *= 2.0
    for _ in range(45):
        midpoint = 0.5 * (low + high)
        if ok(midpoint):
            low = midpoint
        else:
            high = midpoint
    return low


def main() -> None:
    complex_match = max_match_prior("complex", 0.10)
    phase_match_005 = max_match_prior("phase", 0.05)
    phase_snr_01 = snr_with_match_prior("phase", 0.10, 0.0)

    print("Programmed translated-gradient response-space matching")
    print(
        f"complex sigma_meas=0.10 deg-equivalent -> "
        f"max mismatch prior={complex_match:.9f} deg RMS"
    )
    print(
        f"phase sigma_meas=0.05 deg -> "
        f"max mismatch prior={phase_match_005:.9f} deg RMS"
    )
    print(
        f"phase sigma_meas=0.10 deg, perfect differential match -> "
        f"SNR={phase_snr_01:.6f}"
    )
    print()

    basis, residual0 = nominal_projector()
    settings = {
        "common_position": 0.10,
        "separation": 0.10,
        "differential_width": 0.03,
        "differential_ramp": 0.03,
        "differential_front_x": 0.002,
        "differential_back_x": 0.010,
        "differential_modulation": 0.20,
    }
    tolerances = {}
    print("unmodelled programmed-profile coordinate tolerance")
    print("criterion: fitted nominal amplitude +/-10%, residual cosine >=0.99")
    for parameter, high in settings.items():
        value = symmetric_tolerance(parameter, high, basis, residual0)
        tolerances[parameter] = value
        print(f"  {parameter}: {value:.9f}")

    assert 0.00644 < complex_match < 0.00648
    assert 0.0241 < phase_match_005 < 0.0245
    assert 2.74 < phase_snr_01 < 2.77

    assert 0.082 < tolerances["common_position"] < 0.084
    assert 0.073 < tolerances["separation"] < 0.075
    assert 0.0215 < tolerances["differential_width"] < 0.0230
    assert 0.0225 < tolerances["differential_ramp"] < 0.0240
    assert 0.00135 < tolerances["differential_front_x"] < 0.00145
    assert 0.0060 < tolerances["differential_back_x"] < 0.0065
    assert 0.126 < tolerances["differential_modulation"] < 0.130

    print()
    print(
        "PASS: the programmed 1-um gradient segment retains useful tolerance to "
        "profile placement and shape errors. At the current optimistic complex-"
        "response noise point (0.10-deg-equivalent per component), equal "
        "differential nuisance-mode priors can be about 0.00646 deg RMS and the "
        "illustrative target still reaches 3 sigma. The strict unmodelled-profile "
        "criterion allows ~0.083-um common placement error, ~0.074-um separation "
        "error, ~0.022-um width/ramp mismatch, and ~0.0014 differential front "
        "composition. These are knowledge tolerances; independently measured "
        "realized x(z) should replace the nominal profile in the forward model."
    )


if __name__ == "__main__":
    main()
