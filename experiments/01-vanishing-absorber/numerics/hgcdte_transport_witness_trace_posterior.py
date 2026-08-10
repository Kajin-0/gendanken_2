"""End-to-end multi-distance witness trace -> relocation posterior calculation.

This is the conservative successor to the first witness-posterior calculation.
It allows independent field-dependent lifetime nodes tau(E,x), not one lifetime
amplitude per composition.

The transport solver and direct witness interpolation are imported from
`hgcdte_transport_witness_posterior_propagation.py`. The witness posterior now
contains, at x=0.35,0.43,0.51 and E=0.1,0.3,0.5,1,1.5,2,2.5,3 kV/cm:

    24 independent log v nodes
    24 independent log D nodes
    24 independent log tau nodes.

Synthetic central truth is used only to calculate regression sensitivities. It
is NOT a proposed 300-K HgCdTe constitutive law.

Multi-distance measurement model
--------------------------------
Use transport distances
    5,10,20,40,70,100 um
and retain synthetic points with Q/Q0 >= 0.05.

For each field:

    mean t = t0 + L/v
    Var t  = sigma0^2 + 2 D L/v^3
    ln Q   = ln Q0 - L/(v tau).

The slope covariance produces field-dependent log-prior uncertainties on
v,D,tau. The common intercepts t0, sigma0^2 and ln Q0 do not need to be known.

Two trace-error scenarios are highlighted:

Moderate:
    centroid sigma_t = 25 ps
    RMS packet-width sigma = 2 ps
    sigma_lnQ = 0.10 per trace.

Conservative:
    centroid sigma_t = 50 ps
    RMS packet-width sigma = 5 ps
    sigma_lnQ = 0.20 per trace.

The synthetic common temporal-width intercept is 30 ps RMS. Its absolute value
is a design stress, not an instrument specification.

Detector-side model
-------------------
- feature depths 2.6,4.4,5.6 um;
- lambda 2.00-2.40 um;
- f = 0.5,1,2,3 GHz;
- high-Cd entrance -> low-Cd collection;
- quasi-neutral gap-force + DOS drift;
- direct interpolated v(E,x),D(E,x),tau(E,x);
- free majority-band tilt rho and free entrance surface-loss amplitude;
- free wavelength-independent phase and ln|H| intercept for every device/RF;
- provisional detector component noise = 0.10-degree-equivalent;
- provisional weight |H| sqrt(Pabs*Cdc).

All response derivatives use the branch-safe identity
    d ln H/dp = (dH/dp)/H.

Main current scales at the canonical 641-point spatial grid
----------------------------------------------------------
Velocity-only trace posterior:
    25-ps centroid error -> mechanism SNR ~5.0
    50 ps -> ~4.0
    75 ps -> ~3.2
    100 ps -> ~2.6.

Whole-packet posterior:
    25 ps / 2 ps width / 0.10 lnQ -> ~14 sigma
    50 ps / 5 ps width / 0.20 lnQ -> ~6.9 sigma.

Allowing effectively unbounded COMMON multiplicative calibration scales in all
three witness families changes these whole-packet SNRs only modestly. The useful
information comes mainly from transport SHAPE versus field/composition, not one
absolute global scale.

These are conditional Fisher scales, not expected laboratory detection
significances. No novelty claim.
"""

from __future__ import annotations

import numpy as np
from scipy.linalg import qr

from hgcdte_transport_witness_posterior_propagation import (
    X_WITNESS,
    E_WITNESS_V_CM,
    V_WITNESS_0,
    D_WITNESS_0,
    TAU_WITNESS_0,
    WAVELENGTHS_UM,
    FREQUENCIES_GHZ,
    FEATURE_DEPTHS_UM,
    SIGMA_COMPONENT_DEG,
    SURFACE_CM_S,
    FD_STEP,
    transfer,
)

DISTANCES_UM = np.asarray((5.0, 10.0, 20.0, 40.0, 70.0, 100.0))
Q_MIN = 0.05
SYNTHETIC_TAU_NS = 1.0
SYNTHETIC_SIGMA0_PS = 30.0

# These match the synthetic witness center in the imported module.
MU_CM2_VS = 9000.0
D_KV_CM = 8.0
R = 2.2
T_K = 300.0
KBT_OVER_Q_V = 8.617333262145e-5 * T_K


def parameter_names():
    names = ["eta"]
    for prefix in ("v", "D", "tau"):
        for ix in range(len(X_WITNESS)):
            for ie in range(len(E_WITNESS_V_CM)):
                names.append(f"{prefix}_{ix}_{ie}")
    names.extend(("rho", "surface"))
    return names


PARAMETERS = parameter_names()
INDEX = {name: i for i, name in enumerate(PARAMETERS)}
V_INDICES = [i for i, name in enumerate(PARAMETERS) if name.startswith("v_")]
D_INDICES = [i for i, name in enumerate(PARAMETERS) if name.startswith("D_")]
TAU_INDICES = [i for i, name in enumerate(PARAMETERS) if name.startswith("tau_")]


def branch_safe_derivatives(feature_depth_um: float):
    h0, p_abs, collection = transfer(feature_depth_um)
    derivatives = {}

    plus = transfer(feature_depth_um, eta=1.0 + FD_STEP)[0]
    minus = transfer(feature_depth_um, eta=1.0 - FD_STEP)[0]
    derivatives["eta"] = (plus - minus) / (2.0 * FD_STEP * h0)

    for ix in range(len(X_WITNESS)):
        for ie in range(len(E_WITNESS_V_CM)):
            plus_nodes = V_WITNESS_0.copy()
            minus_nodes = V_WITNESS_0.copy()
            plus_nodes[ix, ie] *= np.exp(FD_STEP)
            minus_nodes[ix, ie] *= np.exp(-FD_STEP)
            plus = transfer(feature_depth_um, velocity_nodes=plus_nodes)[0]
            minus = transfer(feature_depth_um, velocity_nodes=minus_nodes)[0]
            derivatives[f"v_{ix}_{ie}"] = (plus - minus) / (2.0 * FD_STEP * h0)

            plus_nodes = D_WITNESS_0.copy()
            minus_nodes = D_WITNESS_0.copy()
            plus_nodes[ix, ie] *= np.exp(FD_STEP)
            minus_nodes[ix, ie] *= np.exp(-FD_STEP)
            plus = transfer(feature_depth_um, diffusion_nodes=plus_nodes)[0]
            minus = transfer(feature_depth_um, diffusion_nodes=minus_nodes)[0]
            derivatives[f"D_{ix}_{ie}"] = (plus - minus) / (2.0 * FD_STEP * h0)

            plus_nodes = TAU_WITNESS_0.copy()
            minus_nodes = TAU_WITNESS_0.copy()
            plus_nodes[ix, ie] *= np.exp(FD_STEP)
            minus_nodes[ix, ie] *= np.exp(-FD_STEP)
            plus = transfer(feature_depth_um, lifetime_nodes=plus_nodes)[0]
            minus = transfer(feature_depth_um, lifetime_nodes=minus_nodes)[0]
            derivatives[f"tau_{ix}_{ie}"] = (plus - minus) / (2.0 * FD_STEP * h0)

    plus = transfer(feature_depth_um, rho=FD_STEP)[0]
    minus = transfer(feature_depth_um, rho=-FD_STEP)[0]
    derivatives["rho"] = (plus - minus) / (2.0 * FD_STEP * h0)

    plus = transfer(
        feature_depth_um,
        surface_cm_s=SURFACE_CM_S * np.exp(FD_STEP),
    )[0]
    minus = transfer(
        feature_depth_um,
        surface_cm_s=SURFACE_CM_S * np.exp(-FD_STEP),
    )[0]
    derivatives["surface"] = (plus - minus) / (2.0 * FD_STEP * h0)

    return h0, p_abs, collection, derivatives


def projected_parameter_matrix():
    data = {
        depth: branch_safe_derivatives(depth)
        for depth in FEATURE_DEPTHS_UM
    }

    n_device = len(FEATURE_DEPTHS_UM)
    n_frequency = len(FREQUENCIES_GHZ)
    n_lambda = len(WAVELENGTHS_UM)

    weights = np.asarray(
        [
            np.abs(data[depth][0])
            * np.sqrt(data[depth][1][None, :] * data[depth][2][None, :])
            for depth in FEATURE_DEPTHS_UM
        ]
    )

    def stack(name: str):
        return np.stack([data[depth][3][name] for depth in FEATURE_DEPTHS_UM])

    def flatten(values: np.ndarray):
        return np.concatenate(
            ((values.imag * weights).ravel(), (values.real * weights).ravel())
        )

    matrix = np.column_stack([flatten(stack(name)) for name in PARAMETERS])

    offsets = []
    for device in range(n_device):
        for frequency in range(n_frequency):
            phase = np.zeros((n_device, n_frequency, n_lambda), dtype=complex)
            phase[device, frequency, :] = 1j
            offsets.append(flatten(phase))

            magnitude = np.zeros((n_device, n_frequency, n_lambda), dtype=complex)
            magnitude[device, frequency, :] = 1.0
            offsets.append(flatten(magnitude))

    offset_matrix = np.column_stack(offsets)
    qmat, rmat, _ = qr(offset_matrix, mode="economic", pivoting=True)
    diagonal = np.abs(np.diag(rmat))
    rank = int(np.sum(diagonal > diagonal[0] * 1.0e-10))
    basis = qmat[:, :rank]
    return matrix - basis @ (basis.T @ matrix)


def synthetic_velocity(field_v_cm: float) -> float:
    return float(
        MU_CM2_VS
        * field_v_cm
        / (1.0 + (abs(field_v_cm) / (1000.0 * D_KV_CM)) ** R)
    )


def usable_distances(field_v_cm: float):
    velocity = synthetic_velocity(field_v_cm)
    length_cm = DISTANCES_UM * 1.0e-4
    time_s = length_cm / velocity
    survival = np.exp(-time_s / (SYNTHETIC_TAU_NS * 1.0e-9))
    mask = survival >= Q_MIN
    return velocity, length_cm[mask], time_s[mask], survival[mask]


def cv_to_sigma_ln(relative_sigma: float) -> float:
    return float(np.sqrt(np.log1p(relative_sigma**2)))


def trace_prior_at_field(
    field_v_cm: float,
    centroid_sigma_ps: float,
    width_sigma_ps: float,
    sigma_lnq: float,
):
    velocity, length_cm, _, _ = usable_distances(field_v_cm)
    sxx = float(np.sum((length_cm - np.mean(length_cm)) ** 2))

    # v from mean-time slope.
    slope_t = 1.0 / velocity
    sigma_slope_t = centroid_sigma_ps * 1.0e-12 / np.sqrt(sxx)
    rel_v = sigma_slope_t / slope_t

    # D from temporal-variance slope.
    diffusion = MU_CM2_VS * KBT_OVER_Q_V
    slope_var = 2.0 * diffusion / velocity**3
    sigma0_s = SYNTHETIC_SIGMA0_PS * 1.0e-12
    observed_sigma = np.sqrt(sigma0_s**2 + slope_var * length_cm)
    sigma_variance = 2.0 * observed_sigma * width_sigma_ps * 1.0e-12
    design = np.column_stack((np.ones(len(length_cm)), length_cm))
    weight = np.diag(1.0 / sigma_variance**2)
    covariance = np.linalg.inv(design.T @ weight @ design)
    rel_D = float(np.sqrt(covariance[1, 1]) / slope_var)

    # tau from log-charge slope, including independently measured v uncertainty.
    slope_q = 1.0 / (velocity * SYNTHETIC_TAU_NS * 1.0e-9)
    rel_slope_q = sigma_lnq / (np.sqrt(sxx) * slope_q)
    rel_tau = float(np.sqrt(rel_slope_q**2 + rel_v**2))

    return (
        cv_to_sigma_ln(rel_v),
        cv_to_sigma_ln(rel_D),
        cv_to_sigma_ln(rel_tau),
    )


def add_node_priors(
    fisher: np.ndarray,
    velocity_sigmas: np.ndarray | None,
    diffusion_sigmas: np.ndarray | None,
    lifetime_sigmas: np.ndarray | None,
    sigma_rho: float = 1.6,
    common_scale_sigma: float | None = None,
):
    def add_family(prefix: str, family_indices: list[int], field_sigmas: np.ndarray | None):
        if field_sigmas is None:
            return
        sigmas = np.asarray(
            [field_sigmas[ie] for _ in X_WITNESS for ie in range(len(E_WITNESS_V_CM))]
        )
        if common_scale_sigma is None:
            precision = np.diag(1.0 / sigmas**2)
        else:
            covariance = np.diag(sigmas**2) + common_scale_sigma**2 * np.ones(
                (len(sigmas), len(sigmas))
            )
            precision = np.linalg.inv(covariance)
        fisher[np.ix_(family_indices, family_indices)] += precision

    add_family("v", V_INDICES, velocity_sigmas)
    add_family("D", D_INDICES, diffusion_sigmas)
    add_family("tau", TAU_INDICES, lifetime_sigmas)

    if sigma_rho is not None:
        index = INDEX["rho"]
        fisher[index, index] += 1.0 / sigma_rho**2


def mechanism_snr(
    matrix: np.ndarray,
    velocity_sigmas: np.ndarray | None,
    diffusion_sigmas: np.ndarray | None,
    lifetime_sigmas: np.ndarray | None,
    sigma_rho: float = 1.6,
    common_scale_sigma: float | None = None,
):
    sigma_measure = np.deg2rad(SIGMA_COMPONENT_DEG)
    fisher = matrix.T @ matrix / sigma_measure**2
    add_node_priors(
        fisher,
        velocity_sigmas,
        diffusion_sigmas,
        lifetime_sigmas,
        sigma_rho,
        common_scale_sigma,
    )
    covariance = np.linalg.pinv(fisher, rcond=1.0e-12)
    return float(1.0 / np.sqrt(covariance[0, 0]))


def trace_prior_arrays(centroid_sigma_ps: float, width_sigma_ps: float, sigma_lnq: float):
    rows = np.asarray(
        [
            trace_prior_at_field(field, centroid_sigma_ps, width_sigma_ps, sigma_lnq)
            for field in E_WITNESS_V_CM
        ]
    )
    return rows[:, 0], rows[:, 1], rows[:, 2]


def velocity_only_sigmas(centroid_sigma_ps: float):
    values = []
    # Width / amplitude arguments are irrelevant to the returned v component.
    for field in E_WITNESS_V_CM:
        sigma_v, _, _ = trace_prior_at_field(field, centroid_sigma_ps, 2.0, 0.10)
        values.append(sigma_v)
    return np.asarray(values)


def main() -> None:
    matrix = projected_parameter_matrix()

    print("Multi-distance witness trace -> relocation posterior")
    print("fields kV/cm = " + ", ".join(f"{e/1000:.1f}" for e in E_WITNESS_V_CM))
    print("distances um = " + ", ".join(f"{d:.0f}" for d in DISTANCES_UM))
    print()

    print("velocity-only centroid cases")
    velocity_results = {}
    for centroid_sigma in (25.0, 50.0, 75.0, 100.0):
        sigma_v = velocity_only_sigmas(centroid_sigma)
        snr = mechanism_snr(matrix, sigma_v, None, None)
        velocity_results[centroid_sigma] = snr
        print(
            f"  sigma_t={centroid_sigma:.0f} ps -> mechanism SNR={snr:.6f}; "
            f"high-field sigma_ln(v)={sigma_v[-1]:.4f}"
        )
    print()

    scenarios = {
        "moderate": (25.0, 2.0, 0.10),
        "conservative": (50.0, 5.0, 0.20),
    }
    whole_packet_results = {}
    for name, values in scenarios.items():
        sigma_v, sigma_D, sigma_tau = trace_prior_arrays(*values)
        snr = mechanism_snr(matrix, sigma_v, sigma_D, sigma_tau)
        correlated = mechanism_snr(
            matrix,
            sigma_v,
            sigma_D,
            sigma_tau,
            common_scale_sigma=10.0,
        )
        whole_packet_results[name] = (snr, correlated)
        print(name)
        print(
            f"  trace errors: sigma_t={values[0]:.0f} ps, "
            f"sigma_width={values[1]:.1f} ps, sigma_lnQ={values[2]:.2f}"
        )
        print(f"  independent-posterior mechanism SNR={snr:.6f}")
        print(
            "  with effectively unbounded common v/D/tau scale biases: "
            f"SNR={correlated:.6f}"
        )
        print(
            "  high-field log sigmas (v,D,tau) = "
            f"{sigma_v[-1]:.4f}, {sigma_D[-1]:.4f}, {sigma_tau[-1]:.4f}"
        )
        print()

    assert 4.9 < velocity_results[25.0] < 5.1
    assert 3.8 < velocity_results[50.0] < 4.1
    assert 3.1 < velocity_results[75.0] < 3.3
    assert 2.5 < velocity_results[100.0] < 2.7

    assert 13.8 < whole_packet_results["moderate"][0] < 14.3
    assert 13.6 < whole_packet_results["moderate"][1] < 14.2
    assert 6.7 < whole_packet_results["conservative"][0] < 7.1
    assert 6.4 < whole_packet_results["conservative"][1] < 6.9

    print(
        "PASS: a multi-distance packet experiment produces transport-posterior "
        "precision in the range required by the relocation inverse under the "
        "current synthetic central model. Even velocity-only traces with ~75-ps "
        "centroid uncertainty cross the provisional 3-sigma mechanism threshold. "
        "Whole-packet centroid/width/amplitude fits provide much stronger margins "
        "and remain robust to huge common multiplicative calibration biases."
    )


if __name__ == "__main__":
    main()
