"""Finite-RF complex Jacobian for the short-wave sample-A change profile.

The low-frequency timing inverse uses the survival kernel A(lambda). Simple
optical-load differencing does not change that spatial operator. At finite RF,
however, a local delay perturbation is weighted by the accumulated baseline
transit phase and the small-signal complex response is

    d ln H_i / d q_j
      = -i Omega / H_i
        * int p_i(z) exp[-i Omega T0(z)] L_j(z) dz,

where L_j(z) is the path length through spatial cell j for a carrier generated
at z. In the Omega->0 limit this reduces to -i Omega A_ij.

This script tests whether finite-frequency phase and log-magnitude responses
rotate an illustrative sample-A nonlinear-region change away from six smooth
A/B transport nuisance modes enough to remove the wavelength-only degeneracy.

Baseline transport is deliberately simple and explicit:
    v0 = 1e5 m/s, q0 = 10 ps/um,
    deterministic front-directed transit T0(z)=q0*z.

The 25% support-shaped A perturbation is the same illustrative scale used in
previous short-wave files. It is not a device prediction.

Optics are Hansen + Moazzami Beer-Lambert. Eighty spatial cells are used. The
complex Jacobian is evaluated with cell-binned generation probability. No
stochastic carrier dynamics, electrical pole, or calibrated covariance is
included.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import cumulative_trapezoid

from hgcdte_sample_a_constraint_family_joint_iso_kernel import (
    HC_EV_UM,
    N_CELL,
    alpha_moazzami,
    sample_a_profiles,
    sample_b_profile,
)
from hgcdte_sample_a_shortwave_visibility import nonlinear_support

LAMBDA_GRID = np.arange(2.00, 2.8001, 0.01)
BASELINE_V_M_S = 1.0e5
Q0_PS_PER_UM = 1.0e6 / BASELINE_V_M_S
PERTURBATION_FRACTION = 0.25

FREQUENCY_SETS_GHZ = {
    "1GHz": (1.0,),
    "multi": (0.25, 0.50, 1.0, 2.0, 3.0),
}

REFERENCE_PHASE_NOISE_DEG = 0.10


def generation_probabilities(
    z_um: np.ndarray,
    x: np.ndarray,
    wavelength_um: float,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Conditional generation probabilities in 80 uniform spatial cells."""
    edges = np.linspace(0.0, float(z_um[-1]), N_CELL + 1)
    alpha = alpha_moazzami(HC_EV_UM / wavelength_um, x, 300.0)
    tau = np.concatenate(
        ([0.0], cumulative_trapezoid(alpha, z_um * 1.0e-4))
    )
    tau_edges = np.interp(edges, z_um, tau)
    p_abs = 1.0 - np.exp(-tau_edges[-1])
    if p_abs <= 1.0e-14:
        raise RuntimeError("Zero modeled absorption at requested wavelength")

    probability = (
        np.exp(-tau_edges[:-1]) - np.exp(-tau_edges[1:])
    ) / p_abs
    probability /= np.sum(probability)
    centers = 0.5 * (edges[:-1] + edges[1:])
    return probability, centers, edges


def path_overlap(centers_um: np.ndarray, edges_um: np.ndarray) -> np.ndarray:
    """Path length through each cell for generation at each cell center."""
    starts = edges_um[:-1]
    widths = np.diff(edges_um)
    return np.clip(
        centers_um[:, None] - starts[None, :],
        0.0,
        widths[None, :],
    )


def low_frequency_matrix(
    z_um: np.ndarray,
    x: np.ndarray,
    wavelengths: np.ndarray | None = None,
) -> np.ndarray:
    """Mean-delay spatial matrix from cell-binned generation probability."""
    if wavelengths is None:
        wavelengths = LAMBDA_GRID

    rows = []
    for wavelength in wavelengths:
        probability, centers, edges = generation_probabilities(
            z_um, x, float(wavelength)
        )
        rows.append(probability @ path_overlap(centers, edges))
    return np.asarray(rows)


def finite_rf_jacobian(
    z_um: np.ndarray,
    x: np.ndarray,
    frequencies_ghz: tuple[float, ...],
    wavelengths: np.ndarray | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    """Return d ln H / d q_j and baseline H for each f,lambda.

    If `wavelengths` is omitted, use the canonical 2.00-2.80 um short-wave
    grid. An explicit grid is accepted so the same validated finite-RF operator
    can be reused by later mid/deep or purpose-built device design studies.
    """
    if wavelengths is None:
        wavelengths = LAMBDA_GRID
    wavelengths = np.asarray(wavelengths, dtype=float)

    edges = np.linspace(0.0, float(z_um[-1]), N_CELL + 1)
    centers = 0.5 * (edges[:-1] + edges[1:])
    overlap = path_overlap(centers, edges)
    baseline_time_ps = Q0_PS_PER_UM * centers

    probability_by_lambda = []
    for wavelength in wavelengths:
        probability, _, _ = generation_probabilities(
            z_um, x, float(wavelength)
        )
        probability_by_lambda.append(probability)
    probability_by_lambda = np.asarray(probability_by_lambda)

    jacobian = []
    transfer = []
    for f_ghz in frequencies_ghz:
        omega = 2.0 * np.pi * f_ghz * 1.0e9
        phase = np.exp(-1j * omega * baseline_time_ps * 1.0e-12)

        H = probability_by_lambda @ phase
        weighted_overlap = (
            (probability_by_lambda * phase[None, :]) @ overlap
        )
        J = (
            -1j
            * omega
            * 1.0e-12
            * weighted_overlap
            / H[:, None]
        )
        jacobian.append(J)
        transfer.append(H)

    return np.asarray(jacobian), np.asarray(transfer)


def first_three_spatial_modes(matrix: np.ndarray) -> np.ndarray:
    centered = matrix - np.mean(matrix, axis=0, keepdims=True)
    _, _, vt = np.linalg.svd(centered, full_matrices=False)
    return vt[:3].T


def center_wavelength(response: np.ndarray) -> np.ndarray:
    """Remove arbitrary wavelength-independent response separately at each f."""
    return response - np.mean(response, axis=1, keepdims=True)


def response_matrix(response: np.ndarray, mode: str) -> np.ndarray:
    """Convert nf x nlambda x nparam complex response to real data matrix."""
    response = center_wavelength(response)
    if mode == "phase":
        return response.imag.reshape(-1, response.shape[-1])
    if mode == "complex":
        phase = response.imag.reshape(-1, response.shape[-1])
        magnitude = response.real.reshape(-1, response.shape[-1])
        return np.concatenate((phase, magnitude), axis=0)
    raise ValueError(mode)


def target_vector(response: np.ndarray, mode: str) -> np.ndarray:
    response = center_wavelength(response[..., None])
    if mode == "phase":
        return response.imag.reshape(-1)
    if mode == "complex":
        return np.concatenate(
            (response.imag.reshape(-1), response.real.reshape(-1))
        )
    raise ValueError(mode)


def project_residual(
    target: np.ndarray,
    nuisance: np.ndarray,
) -> tuple[float, float]:
    """Principal angle and residual norm fraction after nuisance projection."""
    u, singular, _ = np.linalg.svd(nuisance, full_matrices=False)
    rank = int(np.sum(singular > singular[0] * 1.0e-10))
    basis = u[:, :rank]
    projection = basis @ (basis.T @ target)
    residual = target - projection
    fraction = float(np.linalg.norm(residual) / np.linalg.norm(target))
    angle = float(np.degrees(np.arcsin(np.clip(fraction, 0.0, 1.0))))
    return angle, float(np.linalg.norm(residual))


def main() -> None:
    b_z, b_x = sample_b_profile()
    b_low = low_frequency_matrix(b_z, b_x)
    b_modes = first_three_spatial_modes(b_low)

    b_jacobian = {
        name: finite_rf_jacobian(b_z, b_x, frequencies)[0]
        for name, frequencies in FREQUENCY_SETS_GHZ.items()
    }

    angle = {
        name: {"phase": [], "complex": []}
        for name in FREQUENCY_SETS_GHZ
    }
    fixed_time_snr = {
        name: {"phase": [], "complex": []}
        for name in FREQUENCY_SETS_GHZ
    }
    min_abs_h = {
        name: 1.0 for name in FREQUENCY_SETS_GHZ
    }

    for a_z, a_x, metadata in sample_a_profiles():
        a_low = low_frequency_matrix(a_z, a_x)
        a_modes = first_three_spatial_modes(a_low)

        _, _, support = nonlinear_support(a_z, metadata)
        delta_q = Q0_PS_PER_UM * (
            1.0 / (1.0 - PERTURBATION_FRACTION * support) - 1.0
        )

        for name, frequencies in FREQUENCY_SETS_GHZ.items():
            a_jac, a_H = finite_rf_jacobian(a_z, a_x, frequencies)
            min_abs_h[name] = min(
                min_abs_h[name], float(np.min(np.abs(a_H)))
            )

            a_smooth = np.einsum("flj,jk->flk", a_jac, a_modes)
            b_smooth = np.einsum(
                "flj,jk->flk", b_jacobian[name], b_modes
            )
            physical_target = np.einsum("flj,j->fl", a_jac, delta_q)

            for mode in ("phase", "complex"):
                nuisance = np.column_stack(
                    (
                        response_matrix(a_smooth, mode),
                        response_matrix(b_smooth, mode),
                    )
                )
                target = target_vector(physical_target, mode)
                theta, residual_norm = project_residual(target, nuisance)
                angle[name][mode].append(theta)

                # Fixed total coherent-time comparison: splitting the one-RF
                # reference resource over N_f frequencies increases equal
                # per-point phase/log-amplitude noise by sqrt(N_f).
                sigma = (
                    np.deg2rad(REFERENCE_PHASE_NOISE_DEG)
                    * np.sqrt(len(frequencies))
                )
                fixed_time_snr[name][mode].append(residual_norm / sigma)

    print("Finite-RF complex Jacobian geometry")
    print(
        f"baseline v={BASELINE_V_M_S:.1e} m/s, "
        f"q0={Q0_PS_PER_UM:.3f} ps/um"
    )
    print(f"sample-A profiles = {len(sample_a_profiles())}")
    print()

    for name, frequencies in FREQUENCY_SETS_GHZ.items():
        print(f"frequency set {name}: {frequencies} GHz")
        print(f"  minimum modeled |H_A| = {min_abs_h[name]:.6f}")
        for mode in ("phase", "complex"):
            values = np.asarray(angle[name][mode])
            snr = np.asarray(fixed_time_snr[name][mode])
            print(
                f"  {mode} target-to-6-nuisance angle "
                f"min/median/max = {values.min():.6f}/"
                f"{np.median(values):.6f}/{values.max():.6f} deg"
            )
            print(
                f"    no-prior fixed-time illustrative SNR "
                f"min/median/max = {snr.min():.6f}/"
                f"{np.median(snr):.6f}/{snr.max():.6f}"
            )
        print()

    one_phase = np.asarray(angle["1GHz"]["phase"])
    multi_complex = np.asarray(angle["multi"]["complex"])
    improvement = np.median(multi_complex) / np.median(one_phase)
    print(
        "median geometric angle improvement, multi-RF complex / "
        f"1-GHz phase-only = {improvement:.2f}x"
    )

    # Stable numerical regressions for the canonical short-wave grid.
    assert 0.997 < min_abs_h["1GHz"] < 0.999
    assert 0.981 < min_abs_h["multi"] < 0.983

    assert 0.028 < one_phase.min() < 0.029
    assert 0.051 < np.median(one_phase) < 0.053
    assert one_phase.max() < 0.58

    assert 0.049 < multi_complex.min() < 0.051
    assert 0.63 < np.median(multi_complex) < 0.65
    assert 1.35 < multi_complex.max() < 1.38
    assert 12.0 < improvement < 12.5

    multi_snr = np.asarray(fixed_time_snr["multi"]["complex"])
    assert 0.012 < multi_snr.min() < 0.014
    assert 0.088 < np.median(multi_snr) < 0.092
    assert multi_snr.max() < 0.42

    print()
    print(
        "PASS: finite RF and complex magnitude/phase do rotate the effective "
        "spatial Jacobian, but not enough to remove the present A/B smooth-mode "
        "degeneracy. Over 0.25-3 GHz the median principal angle improves by "
        "~12x versus 1-GHz phase only, yet the worst profiles remain below "
        "~0.05 deg and a no-prior fixed-time fit stays far below 1 sigma. RF "
        "diversity is therefore useful leverage, not a substitute for physical "
        "constraints or validated nuisance calibration."
    )


if __name__ == "__main__":
    main()
