"""Propagate a direct HgCdTe transport-witness posterior into relocation metrology.

Purpose
-------
The current relocation experiment should not infer an arbitrary empirical
velocity law from detector data alone. A companion p-type HgCdTe witness
experiment measures v(E,x), D(E,x), and tau(E,x) directly.

This script asks the practical design question:

    How accurate must that witness measurement be before the localized-gradient
    relocation parameter is identifiable at the current provisional complex-
    response noise scale?

Unlike `hgcdte_quasineutral_empirical_velocity_relocation.py`, the witness
posterior here is carried as DIRECT transport values rather than as priors on
mu,d,r.

Witness grid
------------
Compositions:
    x = 0.35, 0.43, 0.51.

Fields:
    E = 0.1, 0.3, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0 kV/cm.

The full 24-node velocity surface and full 24-node diffusion surface are
bilinearly interpolated in (x,E). The three composition-dependent lifetime
values are represented as rows over the same field grid in the synthetic
central model but receive one log-amplitude nuisance parameter per composition
in this first posterior stress.

Central synthetic truth
-----------------------
Only to generate a controlled regression target:

    v = mu E/[1+(E/d)^r]
    mu = 9000 cm2/Vs
    d = 8 kV/cm
    r = 2.2

    D = mu kT/q
    tau = 1 ns.

These are NOT asserted 300 K material constants. Crucially, the Fisher model
allows the individual witness v and D nodes to move independently, so the
posterior is not forced to retain the empirical analytic law or Einstein
relation.

Relocation model
----------------
- high-Cd optical entrance, low-Cd collecting junction;
- quasi-neutral gap-driven force with a majority-band tilt coordinate rho;
- first-passage backward drift-diffusion equation;
- DOS drift D d ln(Nc)/dz using the existing m_e proportional to Eg baseline;
- wavelengths 2.00-2.40 um in 0.025-um steps;
- RF = 0.5,1,2,3 GHz;
- translated feature centers 2.6,4.4,5.6 um;
- one wavelength-independent phase and ln|H| offset per device/RF;
- provisional complex-component noise = 0.10 degree-equivalent;
- provisional signal weight |H| sqrt(Pabs*Cdc).

Mechanism parameter
-------------------
The measured optical x(z) is fixed. In the TRANSPORT force only,

    s_eff = s0 + eta [s(z)-s0].

eta=1 contains the localized programmed slope enhancement; eta=0 retains only
the smooth same-endpoint slope. eta is a nested statistical mechanism
coordinate, not a physically switchable field.

Important corrections
---------------------
- Complex derivatives use d ln H/dp=(dH/dp)/H; never direct finite differences
  of principal log(H).
- D(E,x) is an independent witness surface. Einstein diffusion is used only to
  synthesize the central truth and is NOT imposed on the posterior.
- Witness prior covariance can contain an arbitrary common multiplicative
  systematic plus independent shape error. This prevents the many witness nodes
  from spuriously averaging one global calibration error to zero.

Main current scales
-------------------
At 641 spatial points, with D/tau unconstrained and sigma_rho=1.6:

    equal independent log-v node sigma for 3-sigma eta
        ~0.22-0.24

(961 points gives ~0.23; exact last digits are not a physical specification).

If D and tau are each known only to sigma_ln ~0.5, the allowed equal log-v node
uncertainty relaxes to roughly

        ~0.74.

If the endpoint composition velocity surfaces x=0.35/0.51 are known to
sigma_ln(v)=0.2 while the middle x=0.43 surface is the only missing composition
constraint, the middle surface must be known to roughly

        sigma_ln(v_mid) ~0.39

at 641 points for the current 3-sigma threshold.

Finally, with independent shape errors

    sigma_ln(v node)=0.2
    sigma_ln(D node)=0.5
    sigma_ln(tau node)=0.5

but essentially unbounded COMMON multiplicative calibration scales for v,D,tau,
the mechanism SNR remains ~5.8 in the current linearized model. The witness must
therefore determine transport SHAPE versus E and x much more strongly than one
absolute global scale.

These are conditional Fisher scales, not expected laboratory significances.
No novelty claim.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.linalg import qr
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve

from hgcdte_downstream_drift_diffusion_relocation import (
    HC_EV_UM,
    KBT_OVER_Q_V,
    alpha_moazzami,
    programmed_profile,
)
from hgcdte_sample_a_constraint_family_joint_iso_kernel import (
    deg_dx_hansen,
    eg_hansen,
)

T_K = 300.0
L_UM = 7.6
X_FRONT = 0.55
X_BACK = 0.32

X_WITNESS = np.asarray((0.35, 0.43, 0.51))
E_WITNESS_V_CM = np.asarray((100.0, 300.0, 500.0, 1000.0, 1500.0, 2000.0, 2500.0, 3000.0))

WAVELENGTHS_UM = np.arange(2.00, 2.4001, 0.025)
FREQUENCIES_GHZ = (0.5, 1.0, 2.0, 3.0)
FEATURE_DEPTHS_UM = (2.6, 4.4, 5.6)

SIGMA_COMPONENT_DEG = 0.10
SURFACE_CM_S = 1.0e5
CENTRAL_MU = 9000.0
CENTRAL_D_KV_CM = 8.0
CENTRAL_R = 2.2
CENTRAL_TAU_NS = 1.0
FD_STEP = 0.004

# 641 points is the canonical posterior regression. Higher-grid spot checks place
# the velocity-only 3-sigma threshold near the same ~0.23 scale.
N_GRID = 641


def synthetic_velocity(field_v_cm: float | np.ndarray) -> np.ndarray:
    field = np.asarray(field_v_cm, dtype=float)
    return (
        CENTRAL_MU
        * field
        / (1.0 + (np.abs(field) / (1000.0 * CENTRAL_D_KV_CM)) ** CENTRAL_R)
    )


def synthetic_diffusion(field_v_cm: float | np.ndarray) -> np.ndarray:
    field = np.asarray(field_v_cm, dtype=float)
    return np.full_like(field, CENTRAL_MU * KBT_OVER_Q_V, dtype=float)


V_WITNESS_0 = np.asarray(
    [[synthetic_velocity(field) for field in E_WITNESS_V_CM] for _ in X_WITNESS]
)
D_WITNESS_0 = np.asarray(
    [[synthetic_diffusion(field) for field in E_WITNESS_V_CM] for _ in X_WITNESS]
)
TAU_WITNESS_0 = np.full(
    (len(X_WITNESS), len(E_WITNESS_V_CM)),
    CENTRAL_TAU_NS,
)


def bilinear_extrapolate(
    x_nodes: np.ndarray,
    e_nodes: np.ndarray,
    values: np.ndarray,
    x_query: np.ndarray,
    e_query: np.ndarray,
) -> np.ndarray:
    """Bilinear interpolation with linear edge extrapolation.

    The programmed feature extends only slightly beyond the x=0.35/0.51 witness
    nodes (~0.344-0.517 in the current design). A real experiment should either
    extend the witness nodes or propagate this edge extrapolation uncertainty.
    """
    xq = np.asarray(x_query)
    eq = np.asarray(e_query)

    ix = np.searchsorted(x_nodes, xq) - 1
    ie = np.searchsorted(e_nodes, eq) - 1
    ix = np.clip(ix, 0, len(x_nodes) - 2)
    ie = np.clip(ie, 0, len(e_nodes) - 2)

    tx = (xq - x_nodes[ix]) / (x_nodes[ix + 1] - x_nodes[ix])
    te = (eq - e_nodes[ie]) / (e_nodes[ie + 1] - e_nodes[ie])

    v00 = values[ix, ie]
    v10 = values[ix + 1, ie]
    v01 = values[ix, ie + 1]
    v11 = values[ix + 1, ie + 1]

    return (
        (1.0 - tx) * (1.0 - te) * v00
        + tx * (1.0 - te) * v10
        + (1.0 - tx) * te * v01
        + tx * te * v11
    )


def generation_density(z_um: np.ndarray, x: np.ndarray, wavelength_um: float):
    z_cm = z_um * 1.0e-4
    alpha = alpha_moazzami(HC_EV_UM / wavelength_um, x, T_K)
    tau = np.concatenate(([0.0], cumulative_trapezoid(alpha, z_cm)))
    p_abs = float(1.0 - np.exp(-tau[-1]))
    density = alpha * np.exp(-tau)
    density /= np.trapezoid(density, z_cm)
    return density, p_abs


def dln_nc_dz_cm(z_um: np.ndarray, x: np.ndarray) -> np.ndarray:
    gap = np.asarray(eg_hansen(x, T_K), dtype=float)
    return np.gradient(1.5 * np.log(gap), z_um * 1.0e-4)


def force_field_v_cm(
    x: np.ndarray,
    slope_per_um: np.ndarray,
    eta: float,
    rho: float,
) -> np.ndarray:
    smooth_slope = (X_FRONT - X_BACK) / L_UM
    effective_slope = smooth_slope + eta * (slope_per_um - smooth_slope)

    gap_force = np.asarray(deg_dx_hansen(x, T_K), dtype=float) * effective_slope * 1.0e4
    majority_tilt = -KBT_OVER_Q_V * rho / (L_UM * 1.0e-4)
    return gap_force + majority_tilt


def local_transport(
    z_um: np.ndarray,
    x: np.ndarray,
    slope_per_um: np.ndarray,
    eta: float,
    rho: float,
    velocity_nodes: np.ndarray,
    diffusion_nodes: np.ndarray,
    lifetime_nodes: np.ndarray,
):
    field = force_field_v_cm(x, slope_per_um, eta, rho)

    velocity_field = bilinear_extrapolate(
        X_WITNESS,
        E_WITNESS_V_CM,
        velocity_nodes,
        x,
        field,
    )
    diffusion = bilinear_extrapolate(
        X_WITNESS,
        E_WITNESS_V_CM,
        diffusion_nodes,
        x,
        field,
    )
    lifetime_ns = bilinear_extrapolate(
        X_WITNESS,
        E_WITNESS_V_CM,
        lifetime_nodes,
        x,
        field,
    )

    # Independent measured D enters both spreading and the DOS drift correction.
    velocity = velocity_field + diffusion * dln_nc_dz_cm(z_um, x)
    return velocity, diffusion, lifetime_ns


def solve_backward(
    z_um: np.ndarray,
    x: np.ndarray,
    slope_per_um: np.ndarray,
    eta: float,
    rho: float,
    velocity_nodes: np.ndarray,
    diffusion_nodes: np.ndarray,
    lifetime_nodes: np.ndarray,
    frequency_ghz: float,
    surface_cm_s: float,
):
    z_cm = z_um * 1.0e-4
    dz_cm = float(z_cm[1] - z_cm[0])
    n = len(z_cm)

    velocity, diffusion, lifetime_ns = local_transport(
        z_um,
        x,
        slope_per_um,
        eta,
        rho,
        velocity_nodes,
        diffusion_nodes,
        lifetime_nodes,
    )

    omega = 2.0 * np.pi * frequency_ghz * 1.0e9
    sink = 1.0 / (lifetime_ns * 1.0e-9) + 1j * omega

    matrix = lil_matrix((n, n), dtype=complex)
    rhs = np.zeros(n, dtype=complex)

    matrix[0, 0] = -(1.0 + surface_cm_s * dz_cm / diffusion[0])
    matrix[0, 1] = 1.0

    for index in range(1, n - 1):
        matrix[index, index - 1] = (
            diffusion[index] / dz_cm**2
            - velocity[index] / (2.0 * dz_cm)
        )
        matrix[index, index] = -2.0 * diffusion[index] / dz_cm**2 - sink[index]
        matrix[index, index + 1] = (
            diffusion[index] / dz_cm**2
            + velocity[index] / (2.0 * dz_cm)
        )

    matrix[-1, -1] = 1.0
    rhs[-1] = 1.0
    return spsolve(matrix.tocsr(), rhs)


def transfer(
    feature_depth_um: float,
    eta: float = 1.0,
    rho: float = 0.0,
    velocity_nodes: np.ndarray = V_WITNESS_0,
    diffusion_nodes: np.ndarray = D_WITNESS_0,
    lifetime_nodes: np.ndarray = TAU_WITNESS_0,
    surface_cm_s: float = SURFACE_CM_S,
):
    z_um, x, _, slope = programmed_profile(feature_depth_um, N_GRID)
    z_cm = z_um * 1.0e-4
    optical = [
        generation_density(z_um, x, float(wavelength))
        for wavelength in WAVELENGTHS_UM
    ]

    dc = solve_backward(
        z_um,
        x,
        slope,
        eta,
        rho,
        velocity_nodes,
        diffusion_nodes,
        lifetime_nodes,
        0.0,
        surface_cm_s,
    )
    collection = np.asarray(
        [float(np.real(np.trapezoid(density * dc, z_cm))) for density, _ in optical]
    )

    rows = []
    for frequency in FREQUENCIES_GHZ:
        transform = solve_backward(
            z_um,
            x,
            slope,
            eta,
            rho,
            velocity_nodes,
            diffusion_nodes,
            lifetime_nodes,
            float(frequency),
            surface_cm_s,
        )
        rows.append(
            [
                np.trapezoid(density * transform, z_cm) / collected
                for (density, _), collected in zip(optical, collection)
            ]
        )

    p_abs = np.asarray([value for _, value in optical])
    return np.asarray(rows), p_abs, collection


def parameter_names():
    names = ["eta"]
    for ix in range(len(X_WITNESS)):
        for ie in range(len(E_WITNESS_V_CM)):
            names.append(f"v_{ix}_{ie}")
    for ix in range(len(X_WITNESS)):
        for ie in range(len(E_WITNESS_V_CM)):
            names.append(f"D_{ix}_{ie}")
    for ix in range(len(X_WITNESS)):
        names.append(f"tau_{ix}")
    names.extend(("rho", "surface"))
    return names


PARAMETERS = parameter_names()
PARAMETER_INDEX = {name: index for index, name in enumerate(PARAMETERS)}
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

    for ix in range(len(X_WITNESS)):
        for ie in range(len(E_WITNESS_V_CM)):
            plus_nodes = D_WITNESS_0.copy()
            minus_nodes = D_WITNESS_0.copy()
            plus_nodes[ix, ie] *= np.exp(FD_STEP)
            minus_nodes[ix, ie] *= np.exp(-FD_STEP)
            plus = transfer(feature_depth_um, diffusion_nodes=plus_nodes)[0]
            minus = transfer(feature_depth_um, diffusion_nodes=minus_nodes)[0]
            derivatives[f"D_{ix}_{ie}"] = (plus - minus) / (2.0 * FD_STEP * h0)

    for ix in range(len(X_WITNESS)):
        plus_nodes = TAU_WITNESS_0.copy()
        minus_nodes = TAU_WITNESS_0.copy()
        plus_nodes[ix, :] *= np.exp(FD_STEP)
        minus_nodes[ix, :] *= np.exp(-FD_STEP)
        plus = transfer(feature_depth_um, lifetime_nodes=plus_nodes)[0]
        minus = transfer(feature_depth_um, lifetime_nodes=minus_nodes)[0]
        derivatives[f"tau_{ix}"] = (plus - minus) / (2.0 * FD_STEP * h0)

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


def build_projected_parameter_matrix():
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
            (
                (values.imag * weights).ravel(),
                (values.real * weights).ravel(),
            )
        )

    parameter_matrix = np.column_stack(
        [flatten(stack(name)) for name in PARAMETERS]
    )

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
    projected = parameter_matrix - basis @ (basis.T @ parameter_matrix)
    return projected


def add_independent_prior(fisher: np.ndarray, indices: list[int], sigma: float):
    for index in indices:
        fisher[index, index] += 1.0 / sigma**2


def add_correlated_log_prior(
    fisher: np.ndarray,
    indices: list[int],
    sigma_shape: float,
    sigma_common: float,
):
    """Prior covariance = shape^2 I + common^2 11^T."""
    n = len(indices)
    covariance = sigma_shape**2 * np.eye(n) + sigma_common**2 * np.ones((n, n))
    fisher[np.ix_(indices, indices)] += np.linalg.inv(covariance)


def mechanism_snr(
    matrix: np.ndarray,
    sigma_v: float | None = None,
    sigma_D: float | None = None,
    sigma_tau: float | None = None,
    sigma_rho: float | None = 1.6,
    velocity_row_sigmas: tuple[float | None, float | None, float | None] | None = None,
    correlated_common: float | None = None,
):
    sigma_measure = np.deg2rad(SIGMA_COMPONENT_DEG)
    fisher = matrix.T @ matrix / sigma_measure**2

    if velocity_row_sigmas is not None:
        for ix, sigma in enumerate(velocity_row_sigmas):
            if sigma is None:
                continue
            indices = [PARAMETER_INDEX[f"v_{ix}_{ie}"] for ie in range(len(E_WITNESS_V_CM))]
            add_independent_prior(fisher, indices, sigma)
    elif sigma_v is not None:
        if correlated_common is None:
            add_independent_prior(fisher, V_INDICES, sigma_v)
        else:
            add_correlated_log_prior(
                fisher,
                V_INDICES,
                sigma_v,
                correlated_common,
            )

    if sigma_D is not None:
        if correlated_common is None:
            add_independent_prior(fisher, D_INDICES, sigma_D)
        else:
            add_correlated_log_prior(
                fisher,
                D_INDICES,
                sigma_D,
                correlated_common,
            )

    if sigma_tau is not None:
        if correlated_common is None:
            add_independent_prior(fisher, TAU_INDICES, sigma_tau)
        else:
            add_correlated_log_prior(
                fisher,
                TAU_INDICES,
                sigma_tau,
                correlated_common,
            )

    if sigma_rho is not None:
        index = PARAMETER_INDEX["rho"]
        fisher[index, index] += 1.0 / sigma_rho**2

    covariance = np.linalg.pinv(fisher, rcond=1.0e-12)
    return float(1.0 / np.sqrt(covariance[0, 0]))


def threshold_for_three_sigma(
    matrix: np.ndarray,
    sigma_D: float | None,
    sigma_tau: float | None,
    sigma_rho: float = 1.6,
):
    low = 1.0e-3
    high = 3.0
    for _ in range(70):
        midpoint = 0.5 * (low + high)
        snr = mechanism_snr(
            matrix,
            sigma_v=midpoint,
            sigma_D=sigma_D,
            sigma_tau=sigma_tau,
            sigma_rho=sigma_rho,
        )
        if snr >= 3.0:
            low = midpoint
        else:
            high = midpoint
    return float(low)


def threshold_middle_witness(matrix: np.ndarray):
    low = 1.0e-3
    high = 5.0
    for _ in range(70):
        midpoint = 0.5 * (low + high)
        snr = mechanism_snr(
            matrix,
            sigma_D=None,
            sigma_tau=None,
            sigma_rho=1.6,
            velocity_row_sigmas=(0.2, midpoint, 0.2),
        )
        if snr >= 3.0:
            low = midpoint
        else:
            high = midpoint
    return float(low)


def main() -> None:
    matrix = build_projected_parameter_matrix()

    velocity_only_threshold = threshold_for_three_sigma(
        matrix,
        sigma_D=None,
        sigma_tau=None,
    )
    full_packet_threshold = threshold_for_three_sigma(
        matrix,
        sigma_D=0.5,
        sigma_tau=0.5,
    )
    middle_threshold = threshold_middle_witness(matrix)

    print("Direct transport-witness posterior propagation")
    print(f"spatial grid = {N_GRID}")
    print(f"witness compositions = {tuple(X_WITNESS)}")
    print(
        "witness fields kV/cm = "
        + ", ".join(f"{field/1000:.1f}" for field in E_WITNESS_V_CM)
    )
    print(f"relocation depths um = {FEATURE_DEPTHS_UM}")
    print()

    print("3-sigma equal log-velocity-node threshold")
    print(
        "  D,tau unconstrained; sigma_rho=1.6: "
        f"sigma_ln(v) <= {velocity_only_threshold:.6f}"
    )
    print(
        "  sigma_ln(D)=sigma_ln(tau)=0.5; sigma_rho=1.6: "
        f"sigma_ln(v) <= {full_packet_threshold:.6f}"
    )
    print()

    print("middle-composition witness requirement")
    print(
        "  endpoint x=0.35/0.51 velocity surfaces at sigma_ln(v)=0.2; "
        "D,tau unconstrained"
    )
    print(
        f"  x=0.43 surface requires sigma_ln(v_mid) <= {middle_threshold:.6f} "
        "for current 3-sigma threshold"
    )
    print()

    correlated_snr = mechanism_snr(
        matrix,
        sigma_v=0.2,
        sigma_D=0.5,
        sigma_tau=0.5,
        sigma_rho=1.6,
        correlated_common=10.0,
    )
    print("correlated-scale stress")
    print(
        "  sigma_shape ln(v)=0.2, ln(D)=0.5, ln(tau)=0.5; "
        "common log-scale sigma=10 for each family"
    )
    print(f"  mechanism SNR = {correlated_snr:.6f}")
    print()

    # Regression envelopes intentionally allow modest grid dependence in the
    # velocity-only threshold. Independent D/tau extraction is far more stable.
    assert 0.20 < velocity_only_threshold < 0.26
    assert 0.72 < full_packet_threshold < 0.76
    assert 0.36 < middle_threshold < 0.42
    assert 5.7 < correlated_snr < 5.9

    print(
        "PASS: direct witness measurements make the relocation problem much less "
        "demanding than an unconstrained constitutive-law inversion. If velocity "
        "alone carries the posterior, the full eight-field surface needs roughly "
        "20-25% log precision per node in the current linearized model. If the "
        "same packet traces also constrain D and tau only to factor-~1.6 scales, "
        "velocity precision can be looser than a factor of two. The middle x=0.43 "
        "witness is quantitatively necessary to control composition curvature. "
        "Large common calibration-scale errors are much less damaging than errors "
        "in transport SHAPE versus field/composition."
    )


if __name__ == "__main__":
    main()
