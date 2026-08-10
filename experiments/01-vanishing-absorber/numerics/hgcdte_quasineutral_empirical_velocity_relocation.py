"""Quasi-neutral downstream HgCdTe relocation with empirical velocity law.

This is the next transport refinement after
`hgcdte_downstream_drift_diffusion_relocation.py` and the corrected physical-
nuisance audit.

Physics boundary
----------------
For a p-type quasi-neutral graded absorber,

    E_v ~= E_F + kT ln(N_A/N_v),

so

    dE_c/dz ~= dE_g/dz + kT d/dz ln(N_A/N_v).

Thus the *total* minority-electron conduction-band drive is close to the full
gap gradient when N_A/N_v varies slowly. The 2025 electron-affinity result that
~2/3 of a composition-driven gap change appears intrinsically in E_c is not in
conflict with this: the equilibrium electrostatic potential supplies the
remaining majority-band pinning.

For nondegenerate electrons N_c proportional to m_e^(3/2). Using the standard
HgCdTe device-model approximation m_e proportional to E_g gives

    d ln N_c / dz = 1.5 d ln E_g / dz.

The reduced particle drift used here is therefore

    v(z) = v_field(E_force) + D d ln N_c/dz,

with

    E_force = |dE_g/dz|/q - (kT/q) d ln(N_A/N_v)/dz.

The total majority-band tilt is parameterized by

    rho = ln[(N_A/N_v)(L)/(N_A/N_v)(0)],

and treated as linear across the absorber in this first stress. This is a
sensitivity coordinate, not a claim that the real doping profile is linear.

Empirical velocity law
----------------------
Use the impulse-response-calibrated HgCdTe APD form

    v_field = mu E / [1 + (|E|/d)^r].

Rothman et al. (2010) directly measured minority-electron drift velocity,
diffusion and lifetime versus field by Shockley-Haynes methods in p-type HgCdTe.
Guerra et al. (2026) use the above empirical law and report fitted d/r values
of roughly

    SWIR x=0.4, 80 K:  d ~10-11 kV/cm, r ~1.9-2.2
    MWIR x=0.3, 160 K: d ~4-8 kV/cm,  r ~1.9-2.8,

depending on the avalanche-model fit.

Those low-temperature APD fits are NOT a calibrated 300 K law for the proposed
structure. They are used only to define a deliberately broad physical scale.
The current central stress uses d=8 kV/cm, r=2.2.

At the purpose-built ~1.9 kV/cm local gap-gradient field, the velocity reduction
from this law is only ~4% for d=8 kV/cm, ~16% for d=4 kV/cm and ~2% for
d=12 kV/cm. Therefore the experiment is below the APD saturation-field scale,
not deep inside it.

Mechanism coordinate
--------------------
The measured optical x(z) is held fixed. In the *transport force* only,

    s_eff = s0 + eta [s(z)-s0].

eta=1 contains the localized programmed gradient; eta=0 retains only the smooth
same-endpoint gradient. eta is a nested statistical mechanism parameter, not a
physically switchable field.

Physical nuisance parameters
----------------------------
Marginalize the eta derivative against free

    ln(mu), ln(d), r, rho, ln(tau_rec), ln(S),

plus one wavelength-independent phase and ln|H| offset for every device/RF
channel. Complex derivatives use the branch-safe identity

    d ln H/dp = (dH/dp)/H.

A provisional statistics-like information weight

    |H| sqrt(Pabs * Cdc)

is used. It must ultimately be replaced by measured covariance.

Main conditional result
-----------------------
For lambda=2.00-2.40 um, f=0.5,1,2,3 GHz, sigma_component=0.10 deg-equivalent,
and the current central model:

- if d and r are completely unbounded local nuisance amplitudes, the best
  3-depth design remains weak (~1.1 sigma);
- broad scale constraints sigma_ln(d)=0.7 (about factor 2 per sigma) and
  sigma_r=0.5 raise the linearized eta significance to ~12.8 sigma while mu,
  tau, surface loss and rho remain free;
- even broader sigma_ln(d)=1.0, sigma_r=0.7 plus sigma_rho=2 gives ~9.7 sigma.

This does NOT mean the real experiment is guaranteed to achieve those sigma
values. It means the earlier structural collapse required the empirical velocity
curve to vary over a range much broader than existing HgCdTe transport data
suggest. The correct next experiment is a same-material velocity/diffusion/
lifetime calibration, not another arbitrary spectral dimension.

No novelty claim.
"""

from __future__ import annotations

import itertools
import numpy as np
from scipy.linalg import qr
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve

from hgcdte_downstream_drift_diffusion_relocation import (
    KBT_OVER_Q_V,
    LAMBDA_GRID_UM,
    generation_density,
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

FREQUENCIES_GHZ = (0.5, 1.0, 2.0, 3.0)
POSITION_GRID_UM = np.arange(2.0, 5.6001, 0.2)
MIN_SPACING_UM = 0.4
SIGMA_COMPONENT_DEG = 0.10
FD_STEP = 0.01

CENTRAL = {
    "eta": 1.0,
    "mu_cm2_vs": 9000.0,
    "d_kv_cm": 8.0,
    "r": 2.2,
    "rho": 0.0,
    "tau_ns": 1.0,
    "surface_cm_s": 1.0e5,
}

NUISANCE_NAMES = ("mu", "d", "r", "rho", "tau", "surface")


def dln_nc_dz_cm(z_um: np.ndarray, x: np.ndarray) -> np.ndarray:
    """Nondegenerate N_c correction using m_e proportional to E_g."""
    gap = np.asarray(eg_hansen(x, T_K), dtype=float)
    ln_nc = 1.5 * np.log(gap)
    return np.gradient(ln_nc, z_um * 1.0e-4)


def local_velocity_cm_s(
    z_um: np.ndarray,
    x: np.ndarray,
    slope_per_um: np.ndarray,
    eta: float,
    mu_cm2_vs: float,
    d_kv_cm: float,
    r: float,
    rho: float,
):
    smooth_slope = (X_FRONT - X_BACK) / L_UM
    effective_slope = smooth_slope + eta * (slope_per_um - smooth_slope)

    # Positive +z force: E_g decreases from high-Cd entrance to low-Cd junction.
    gap_field_v_cm = (
        np.asarray(deg_dx_hansen(x, T_K), dtype=float)
        * effective_slope
        * 1.0e4
    )

    # From dE_c/dz = dE_g/dz + kT d ln(N_A/N_v)/dz.
    majority_tilt_v_cm = -KBT_OVER_Q_V * rho / (L_UM * 1.0e-4)
    force_field_v_cm = gap_field_v_cm + majority_tilt_v_cm

    d_v_cm = d_kv_cm * 1.0e3
    field_drift = (
        mu_cm2_vs
        * force_field_v_cm
        / (1.0 + (np.abs(force_field_v_cm) / d_v_cm) ** r)
    )

    diffusion_cm2_s = mu_cm2_vs * KBT_OVER_Q_V
    dos_drift = diffusion_cm2_s * dln_nc_dz_cm(z_um, x)
    return field_drift + dos_drift, diffusion_cm2_s, gap_field_v_cm


def solve_backward(
    z_um: np.ndarray,
    x: np.ndarray,
    slope_per_um: np.ndarray,
    eta: float,
    mu_cm2_vs: float,
    d_kv_cm: float,
    r: float,
    rho: float,
    tau_ns: float,
    surface_cm_s: float,
    frequency_ghz: float,
):
    z_cm = z_um * 1.0e-4
    dz_cm = float(z_cm[1] - z_cm[0])
    n = len(z_cm)

    velocity, diffusion, gap_field = local_velocity_cm_s(
        z_um,
        x,
        slope_per_um,
        eta,
        mu_cm2_vs,
        d_kv_cm,
        r,
        rho,
    )

    recombination = 1.0 / (tau_ns * 1.0e-9)
    omega = 2.0 * np.pi * frequency_ghz * 1.0e9
    sink = recombination + 1j * omega

    matrix = lil_matrix((n, n), dtype=complex)
    rhs = np.zeros(n, dtype=complex)

    matrix[0, 0] = -(1.0 + surface_cm_s * dz_cm / diffusion)
    matrix[0, 1] = 1.0

    for i in range(1, n - 1):
        matrix[i, i - 1] = diffusion / dz_cm**2 - velocity[i] / (2.0 * dz_cm)
        matrix[i, i] = -2.0 * diffusion / dz_cm**2 - sink
        matrix[i, i + 1] = diffusion / dz_cm**2 + velocity[i] / (2.0 * dz_cm)

    matrix[-1, -1] = 1.0
    rhs[-1] = 1.0
    transform = spsolve(matrix.tocsr(), rhs)
    return transform, gap_field, velocity, diffusion


def transfer(
    z0_um: float,
    eta: float = CENTRAL["eta"],
    mu_cm2_vs: float = CENTRAL["mu_cm2_vs"],
    d_kv_cm: float = CENTRAL["d_kv_cm"],
    r: float = CENTRAL["r"],
    rho: float = CENTRAL["rho"],
    tau_ns: float = CENTRAL["tau_ns"],
    surface_cm_s: float = CENTRAL["surface_cm_s"],
    n_grid: int = 151,
):
    z_um, x, _, slope = programmed_profile(z0_um, n_grid)
    optical = [generation_density(z_um, x, float(w)) for w in LAMBDA_GRID_UM]
    z_cm = z_um * 1.0e-4

    dc, field, velocity, diffusion = solve_backward(
        z_um, x, slope, eta, mu_cm2_vs, d_kv_cm, r, rho,
        tau_ns, surface_cm_s, 0.0,
    )
    collection = np.asarray(
        [float(np.real(np.trapezoid(density * dc, z_cm))) for density, _ in optical]
    )

    rows = []
    for frequency in FREQUENCIES_GHZ:
        transform, _, _, _ = solve_backward(
            z_um, x, slope, eta, mu_cm2_vs, d_kv_cm, r, rho,
            tau_ns, surface_cm_s, frequency,
        )
        rows.append(
            [
                np.trapezoid(density * transform, z_cm) / c
                for (density, _), c in zip(optical, collection)
            ]
        )

    return (
        np.asarray(rows),
        np.asarray([pabs for _, pabs in optical]),
        collection,
        field,
        velocity,
        diffusion,
    )


def branch_safe_derivatives(z0_um: float):
    base = dict(CENTRAL)
    h0, pabs, collection, _, _, _ = transfer(z0_um, **base)
    derivatives = {}

    plus = dict(base)
    minus = dict(base)
    plus["eta"] += FD_STEP
    minus["eta"] -= FD_STEP
    derivatives["eta"] = (
        transfer(z0_um, **plus)[0] - transfer(z0_um, **minus)[0]
    ) / (2.0 * FD_STEP * h0)

    log_mapping = {
        "mu": "mu_cm2_vs",
        "d": "d_kv_cm",
        "tau": "tau_ns",
        "surface": "surface_cm_s",
    }
    for name, key in log_mapping.items():
        plus = dict(base)
        minus = dict(base)
        plus[key] *= np.exp(FD_STEP)
        minus[key] *= np.exp(-FD_STEP)
        derivatives[name] = (
            transfer(z0_um, **plus)[0] - transfer(z0_um, **minus)[0]
        ) / (2.0 * FD_STEP * h0)

    plus = dict(base)
    minus = dict(base)
    plus["r"] += FD_STEP
    minus["r"] -= FD_STEP
    derivatives["r"] = (
        transfer(z0_um, **plus)[0] - transfer(z0_um, **minus)[0]
    ) / (2.0 * FD_STEP * h0)

    plus = dict(base)
    minus = dict(base)
    plus["rho"] += FD_STEP
    minus["rho"] -= FD_STEP
    derivatives["rho"] = (
        transfer(z0_um, **plus)[0] - transfer(z0_um, **minus)[0]
    ) / (2.0 * FD_STEP * h0)

    return h0, pabs, collection, derivatives


def project_offsets(columns: np.ndarray, offsets: np.ndarray) -> np.ndarray:
    qmat, rmat, _ = qr(offsets, mode="economic", pivoting=True)
    diagonal = np.abs(np.diag(rmat))
    rank = int(np.sum(diagonal > diagonal[0] * 1.0e-10))
    basis = qmat[:, :rank]
    return columns - basis @ (basis.T @ columns)


def project_nuisance(target: np.ndarray, nuisance: np.ndarray) -> np.ndarray:
    qmat, rmat, _ = qr(nuisance, mode="economic", pivoting=True)
    diagonal = np.abs(np.diag(rmat))
    rank = int(np.sum(diagonal > diagonal[0] * 1.0e-10))
    basis = qmat[:, :rank]
    return target - basis @ (basis.T @ target)


def projected_parameter_matrix(depths, cache):
    data = [cache[round(float(z), 6)] for z in depths]
    n_device = len(depths)
    n_frequency = len(FREQUENCIES_GHZ)
    n_lambda = len(LAMBDA_GRID_UM)

    weights = np.asarray(
        [
            np.abs(h0) * np.sqrt(pabs[None, :] * collection[None, :])
            for h0, pabs, collection, _ in data
        ]
    )

    def stack_parameter(name):
        return np.stack([item[3][name] for item in data])

    def flatten(values):
        return np.concatenate(
            ((values.imag * weights).ravel(), (values.real * weights).ravel())
        )

    columns = [flatten(stack_parameter("eta"))]
    columns += [flatten(stack_parameter(name)) for name in NUISANCE_NAMES]
    parameter_matrix = np.column_stack(columns)

    offset_columns = []
    for device in range(n_device):
        for frequency in range(n_frequency):
            phase = np.zeros((n_device, n_frequency, n_lambda), dtype=complex)
            phase[device, frequency, :] = 1j
            offset_columns.append(flatten(phase))

            magnitude = np.zeros((n_device, n_frequency, n_lambda), dtype=complex)
            magnitude[device, frequency, :] = 1.0
            offset_columns.append(flatten(magnitude))

    return project_offsets(parameter_matrix, np.column_stack(offset_columns))


def no_prior_score(depths, cache):
    matrix = projected_parameter_matrix(depths, cache)
    residual = project_nuisance(matrix[:, 0], matrix[:, 1:])
    score = np.linalg.norm(residual) / np.sqrt(
        len(depths) * len(FREQUENCIES_GHZ) * len(LAMBDA_GRID_UM)
    )
    angle = float(
        np.degrees(
            np.arcsin(
                np.clip(np.linalg.norm(residual) / np.linalg.norm(matrix[:, 0]), 0, 1)
            )
        )
    )
    return float(score), angle


def mechanism_snr(depths, cache, priors=None):
    matrix = projected_parameter_matrix(depths, cache)
    sigma = np.deg2rad(SIGMA_COMPONENT_DEG)
    fisher = matrix.T @ matrix / sigma**2

    if priors:
        for name, prior_sigma in priors.items():
            index = 1 + NUISANCE_NAMES.index(name)
            fisher[index, index] += 1.0 / prior_sigma**2

    covariance = np.linalg.inv(fisher)
    return float(1.0 / np.sqrt(covariance[0, 0]))


def optimize_depths(n_device, cache):
    best = None
    for depths in itertools.combinations(POSITION_GRID_UM, n_device):
        if np.min(np.diff(depths)) < MIN_SPACING_UM - 1.0e-12:
            continue
        result = no_prior_score(depths, cache)
        if best is None or result[0] > best[1][0]:
            best = (tuple(float(z) for z in depths), result)
    if best is None:
        raise RuntimeError("No admissible depth design")
    return best


def relocation_phase_pp_deg(z1, z2):
    h11 = transfer(z1, eta=1.0)[0]
    h10 = transfer(z1, eta=0.0)[0]
    h21 = transfer(z2, eta=1.0)[0]
    h20 = transfer(z2, eta=0.0)[0]

    ratio = (h21 / h20) / (h11 / h10)
    phase = np.unwrap(np.angle(ratio), axis=1)
    phase -= np.mean(phase, axis=1, keepdims=True)
    f1 = FREQUENCIES_GHZ.index(1.0)
    return float(np.ptp(np.degrees(phase[f1])))


def main():
    cache = {
        round(float(z), 6): branch_safe_derivatives(float(z))
        for z in POSITION_GRID_UM
    }

    best2 = optimize_depths(2, cache)
    best3 = optimize_depths(3, cache)

    print("Quasi-neutral empirical-velocity translated-gradient design")
    print(
        f"central d={CENTRAL['d_kv_cm']:.1f} kV/cm, r={CENTRAL['r']:.1f}, "
        f"mu={CENTRAL['mu_cm2_vs']:.0f} cm2/Vs"
    )
    print(f"best 2-depth no-prior: {best2[0]}, score/angle={best2[1]}")
    print(f"best 3-depth no-prior: {best3[0]}, score/angle={best3[1]}")
    print()

    depths = best3[0]
    no_prior = mechanism_snr(depths, cache)
    broad_velocity = mechanism_snr(
        depths,
        cache,
        priors={"d": 0.7, "r": 0.5},
    )
    broad_all = mechanism_snr(
        depths,
        cache,
        priors={"d": 1.0, "r": 0.7, "rho": 2.0},
    )

    print(f"mechanism SNR @0.10-deg-equivalent component noise")
    print(f"  all six physical nuisances unbounded: {no_prior:.6f}")
    print(f"  sigma_ln(d)=0.7, sigma_r=0.5: {broad_velocity:.6f}")
    print(
        "  sigma_ln(d)=1.0, sigma_r=0.7, sigma_rho=2.0: "
        f"{broad_all:.6f}"
    )
    print()

    old_pair_pp = relocation_phase_pp_deg(4.1, 5.6)
    wide_pair_pp = relocation_phase_pp_deg(2.8, 5.6)
    print(f"1-GHz field-feature relocation phase p-p")
    print(f"  4.1/5.6 um: {old_pair_pp:.6f} deg")
    print(f"  2.8/5.6 um: {wide_pair_pp:.6f} deg")
    print()

    # Central local nonlinearity scale.
    local_field = 1900.0
    for d_kv in (4.0, 8.0, 12.0):
        factor = 1.0 / (1.0 + (local_field / (1000.0 * d_kv)) ** CENTRAL["r"])
        print(
            f"velocity factor at E={local_field:.0f} V/cm, d={d_kv:.0f} kV/cm: "
            f"{factor:.6f} (reduction {(1-factor)*100:.2f}%)"
        )

    # Regression anchors.
    assert best2[0] == (2.8000000000000007, 5.600000000000003)
    assert best3[0] == (
        2.6000000000000005,
        4.400000000000002,
        5.600000000000003,
    )
    assert 0.000105 < best2[1][0] < 0.000108
    assert 0.000132 < best3[1][0] < 0.000134
    assert 0.112 < best3[1][1] < 0.115

    assert 1.08 < no_prior < 1.10
    assert 12.7 < broad_velocity < 12.9
    assert 9.6 < broad_all < 9.9

    assert 9.0 < old_pair_pp < 9.2
    assert 14.1 < wide_pair_pp < 14.4

    print()
    print(
        "PASS: once the interior field is constrained by quasi-neutral band "
        "self-consistency and the high-field velocity response is parameterized "
        "with an empirical HgCdTe law, the apparent mechanism singularity is "
        "seen to depend on allowing d and r completely unbounded. Broad velocity-"
        "law constraints of the scale already present in HgCdTe transport/APD "
        "measurements restore strong linearized attribution in the central model. "
        "A dedicated same-material Shockley-Haynes or impulse-response calibration "
        "is therefore the decisive next experimental control."
    )


if __name__ == "__main__":
    main()
