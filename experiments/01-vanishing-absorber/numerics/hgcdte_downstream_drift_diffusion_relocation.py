"""Physics-derived downstream drift-diffusion relocation response in graded HgCdTe.

This file supersedes the earlier *mechanism* calculations that imposed an
illustrative 25% local change in path-delay density. The earlier files remain
useful geometry/provenance studies, but a graded-HgCdTe built-in field must be
handled with the correct transport direction.

Orientation
-----------
z=0 is the HIGH-Cd optical entrance; z=L is the LOW-Cd collecting junction.
The composition decreases monotonically from x=0.55 to x=0.32. The graded-gap
field is taken to drive minority electrons toward +z, consistent with the
high-speed graded-HgCdTe orientation modeled/measured by Sang et al. (2022).

This is deliberately different from the 2023 Xu sample-A geometry, where the
junction was placed at the high-Cd end and the strong nonlinear gradient could
repel p-region photoelectrons away from that junction.

Transport model
---------------
For an electron starting at z, the Laplace/Fourier transform u(z,s) of first
passage to the collecting boundary solves the backward equation

    D u'' + v(z) u' - (1/tau_rec + s) u = 0,

with

    u(L,s)=1

and a reflecting or Robin-loss optical-entrance boundary

    D u'(0,s) = S u(0,s).

Einstein diffusion is used:

    D = mu kT/q.

Following the phenomenological graded-HgCdTe continuity model of Sang et al.,
the effective transport field is taken proportional to the local bandgap slope,

    E_eff(z) = chi_E |dEg/dz|/q.

`chi_E` is kept explicit because the use of the full bandgap gradient as an
effective electron-driving field is phenomenological; this script does NOT
claim that chi_E=1 is a microscopic conduction-band-offset identity.

Optional smooth velocity saturation is included only as a sensitivity stress:

    v = mu E / (1 + mu E / v_sat).

Optics
------
Generation is Beer-Lambert with the canonical Hansen gap and Moazzami absorption
model already used elsewhere in the repository, illuminated from z=0. The
high-Cd entrance is relatively transparent at short wavelength until the local
gap permits absorption, so wavelength remains an internal position encoder.

The normalized complex transport transfer is

    H(lambda,Omega) = int p(z|lambda) u(z,iOmega) dz
                      / int p(z|lambda) u(z,0) dz.

The denominator conditions on DC collection and therefore separates RF timing
from simple recombination/collection-efficiency loss.

Relocation observable
---------------------
Two translated x(z) profiles have slightly different optical kernels even with
the built-in field disabled. To avoid calling that optical difference a
transport signal, define for each device

    Delta_field = ln H_field - ln H_field_off

and compare

    R = Delta_field(z2) - Delta_field(z1).

A wavelength-independent complex term is then removed separately at each RF.
This is the field-induced relocation fingerprint.

All mobility, lifetime, field-fraction and velocity-saturation values below are
sensitivity coordinates, not calibrated predictions for a fabricated device.
No novelty claim.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve

from hgcdte_programmed_translated_gradient_design import (
    L_UM,
    programmed_feature,
)
from hgcdte_sample_a_constraint_family_joint_iso_kernel import (
    HC_EV_UM,
    X_A_LOW,
    alpha_moazzami,
    deg_dx_hansen,
)

# Purpose-built profile endpoints inherited from the programmed-relocation branch.
X_FRONT = 0.55
X_BACK = 0.32
SLOPE_MODULATION = 4.0
T_K = 300.0
KBT_OVER_Q_V = 8.617333262145e-5 * T_K

LAMBDA_GRID_UM = np.arange(2.00, 2.4001, 0.025)
REFERENCE_PAIR_UM = (4.1, 5.6)
REFERENCE_MU_CM2_VS = 9000.0
REFERENCE_FIELD_FRACTION = 0.50
REFERENCE_TAU_NS = 1.0
REFERENCE_F_GHZ = 1.0


def programmed_profile(z0_um: float, n_grid: int = 801):
    """Return z,x,feature,slope for the mean-preserving programmed profile."""
    z_um = np.linspace(0.0, L_UM, n_grid)
    feature = programmed_feature(z_um, z0_um)
    feature_mean = float(np.trapezoid(feature, z_um) / L_UM)

    base_slope = (X_FRONT - X_BACK) / L_UM
    slope_per_um = base_slope * (
        1.0 + SLOPE_MODULATION * (feature - feature_mean)
    )
    if np.min(slope_per_um) <= 0.0:
        raise RuntimeError("Programmed profile is no longer monotonic")

    x = X_FRONT - np.concatenate(
        ([0.0], cumulative_trapezoid(slope_per_um, z_um))
    )
    return z_um, x, feature, slope_per_um


def generation_density(
    z_um: np.ndarray,
    x: np.ndarray,
    wavelength_um: float,
):
    """Conditional Beer-Lambert generation density per cm and Pabs."""
    z_cm = z_um * 1.0e-4
    alpha = alpha_moazzami(HC_EV_UM / wavelength_um, x, T_K)
    tau = np.concatenate(([0.0], cumulative_trapezoid(alpha, z_cm)))
    p_abs = float(1.0 - np.exp(-tau[-1]))
    if p_abs <= 1.0e-14:
        raise RuntimeError("Zero modeled absorption at requested wavelength")

    density_per_cm = alpha * np.exp(-tau)
    normalization = float(np.trapezoid(density_per_cm, z_cm))
    density_per_cm /= normalization
    return density_per_cm, p_abs


def effective_field_v_cm(
    x: np.ndarray,
    slope_per_um: np.ndarray,
    field_fraction: float,
) -> np.ndarray:
    """Phenomenological Sang-type bandgap-gradient drive toward +z."""
    return (
        field_fraction
        * np.abs(deg_dx_hansen(x, T_K))
        * slope_per_um
        * 1.0e4
    )


def drift_velocity_cm_s(
    field_v_cm: np.ndarray,
    mobility_cm2_vs: float,
    velocity_sat_m_s: float | None,
) -> np.ndarray:
    velocity = mobility_cm2_vs * field_v_cm
    if velocity_sat_m_s is not None:
        velocity_sat_cm_s = velocity_sat_m_s * 100.0
        velocity = velocity / (1.0 + velocity / velocity_sat_cm_s)
    return velocity


def solve_backward_transform(
    z_um: np.ndarray,
    x: np.ndarray,
    slope_per_um: np.ndarray,
    mobility_cm2_vs: float,
    field_fraction: float,
    tau_rec_ns: float,
    frequency_ghz: float,
    velocity_sat_m_s: float | None = None,
    surface_recombination_cm_s: float = 0.0,
):
    """Solve D u'' + v u' -(1/tau+iOmega)u=0 with collection at z=L."""
    z_cm = z_um * 1.0e-4
    dz_cm = float(z_cm[1] - z_cm[0])
    n = len(z_cm)

    diffusion_cm2_s = mobility_cm2_vs * KBT_OVER_Q_V
    field = effective_field_v_cm(x, slope_per_um, field_fraction)
    velocity = drift_velocity_cm_s(
        field,
        mobility_cm2_vs,
        velocity_sat_m_s,
    )

    if np.isinf(tau_rec_ns):
        recombination_rate_s = 0.0
    else:
        recombination_rate_s = 1.0 / (tau_rec_ns * 1.0e-9)
    omega = 2.0 * np.pi * frequency_ghz * 1.0e9
    sink = recombination_rate_s + 1j * omega

    matrix = lil_matrix((n, n), dtype=complex)
    rhs = np.zeros(n, dtype=complex)

    # D u'(0)=S u(0): S=0 is reflecting; larger S is an entrance-loss stress.
    matrix[0, 0] = -(
        1.0
        + surface_recombination_cm_s * dz_cm / diffusion_cm2_s
    )
    matrix[0, 1] = 1.0

    left = (
        diffusion_cm2_s / dz_cm**2
        - velocity[1:-1] / (2.0 * dz_cm)
    )
    center = -2.0 * diffusion_cm2_s / dz_cm**2 - sink
    right = (
        diffusion_cm2_s / dz_cm**2
        + velocity[1:-1] / (2.0 * dz_cm)
    )

    for i in range(1, n - 1):
        matrix[i, i - 1] = left[i - 1]
        matrix[i, i] = center
        matrix[i, i + 1] = right[i - 1]

    matrix[-1, -1] = 1.0
    rhs[-1] = 1.0

    transform = spsolve(matrix.tocsr(), rhs)
    return transform, field, velocity, diffusion_cm2_s


def transfer_for_profile(
    z0_um: float,
    frequencies_ghz: tuple[float, ...] = (REFERENCE_F_GHZ,),
    wavelengths_um: np.ndarray = LAMBDA_GRID_UM,
    mobility_cm2_vs: float = REFERENCE_MU_CM2_VS,
    field_fraction: float = REFERENCE_FIELD_FRACTION,
    tau_rec_ns: float = REFERENCE_TAU_NS,
    velocity_sat_m_s: float | None = None,
    surface_recombination_cm_s: float = 0.0,
    n_grid: int = 801,
):
    z_um, x, _, slope = programmed_profile(z0_um, n_grid)

    dc_transform, field, velocity, diffusion = solve_backward_transform(
        z_um,
        x,
        slope,
        mobility_cm2_vs,
        field_fraction,
        tau_rec_ns,
        0.0,
        velocity_sat_m_s,
        surface_recombination_cm_s,
    )

    optical = [
        generation_density(z_um, x, float(wavelength))
        for wavelength in wavelengths_um
    ]

    transfer = []
    for frequency in frequencies_ghz:
        rf_transform, _, _, _ = solve_backward_transform(
            z_um,
            x,
            slope,
            mobility_cm2_vs,
            field_fraction,
            tau_rec_ns,
            float(frequency),
            velocity_sat_m_s,
            surface_recombination_cm_s,
        )

        row = []
        for density_per_cm, _ in optical:
            numerator = np.trapezoid(
                density_per_cm * rf_transform,
                z_um * 1.0e-4,
            )
            denominator = np.trapezoid(
                density_per_cm * dc_transform,
                z_um * 1.0e-4,
            )
            row.append(numerator / denominator)
        transfer.append(row)

    pabs = np.asarray([item[1] for item in optical])
    mean_generation_um = np.asarray(
        [
            np.trapezoid(
                z_um * item[0],
                z_um * 1.0e-4,
            )
            for item in optical
        ]
    )

    return (
        np.asarray(transfer),
        pabs,
        mean_generation_um,
        field,
        velocity,
        diffusion,
    )


def field_induced_log_transfer(
    z0_um: float,
    **kwargs,
):
    with_field = transfer_for_profile(z0_um, **kwargs)[0]
    no_field_kwargs = dict(kwargs)
    no_field_kwargs["field_fraction"] = 0.0
    without_field = transfer_for_profile(z0_um, **no_field_kwargs)[0]
    return np.log(with_field) - np.log(without_field), with_field


def relocation_signature(
    z1_um: float,
    z2_um: float,
    **kwargs,
):
    first, h1 = field_induced_log_transfer(z1_um, **kwargs)
    second, h2 = field_induced_log_transfer(z2_um, **kwargs)
    response = second - first
    response -= np.mean(response, axis=1, keepdims=True)
    return response, h1, h2


def phase_peak_to_peak_deg(response: np.ndarray, frequency_index: int = 0) -> float:
    return float(np.ptp(np.degrees(response[frequency_index].imag)))


def complex_rms(response: np.ndarray) -> float:
    return float(np.sqrt(np.mean(np.abs(response) ** 2)))


def main() -> None:
    z1, z2 = REFERENCE_PAIR_UM

    response, h1, h2 = relocation_signature(
        z1,
        z2,
        n_grid=801,
    )
    central_pp = phase_peak_to_peak_deg(response)
    central_phase_rms = float(
        np.sqrt(np.mean(np.degrees(response[0].imag) ** 2))
    )

    _, pabs1, mean1, field1, _, diffusion = transfer_for_profile(z1)
    _, pabs2, mean2, field2, _, _ = transfer_for_profile(z2)

    print("Downstream drift-diffusion translated-gradient response")
    print(
        "orientation: high-Cd optical entrance z=0 -> low-Cd collection z=L"
    )
    print(
        f"central mu={REFERENCE_MU_CM2_VS:.0f} cm2/Vs, "
        f"chi_E={REFERENCE_FIELD_FRACTION:.2f}, "
        f"tau={REFERENCE_TAU_NS:.2f} ns"
    )
    print(
        f"Einstein D = {diffusion:.3f} cm2/s; "
        f"effective E range device1={field1.min():.1f}-{field1.max():.1f} V/cm; "
        f"device2={field2.min():.1f}-{field2.max():.1f} V/cm"
    )
    print(
        f"reference relocation {z1:.1f}->{z2:.1f} um: "
        f"1-GHz field-induced phase p-p={central_pp:.6f} deg; "
        f"phase RMS={central_phase_rms:.6f} deg"
    )
    print(
        f"minimum normalized |H| = {min(np.min(np.abs(h1)), np.min(np.abs(h2))):.6f}"
    )
    print(
        f"Pabs range = {min(pabs1.min(), pabs2.min()):.6f}-"
        f"{max(pabs1.max(), pabs2.max()):.6f}"
    )
    print()

    print("internal generation sweep")
    for index, wavelength in enumerate(LAMBDA_GRID_UM[::4]):
        j = index * 4
        print(
            f"  {wavelength:.2f} um: mean z = "
            f"{mean1[j]:.3f} / {mean2[j]:.3f} um"
        )
    print()

    print("spatial-grid convergence, reference 1-GHz phase p-p")
    convergence = {}
    for n_grid in (201, 401, 801, 1601):
        result, _, _ = relocation_signature(z1, z2, n_grid=n_grid)
        value = phase_peak_to_peak_deg(result)
        convergence[n_grid] = value
        print(f"  N={n_grid}: {value:.9f} deg")
    print()

    print("broad transport stress, 1 GHz, no velocity cap")
    stress = []
    min_abs_h = []
    for mobility in (3000.0, 9000.0, 20000.0, 40000.0):
        for field_fraction in (0.10, 0.25, 0.50, 1.00):
            for tau_ns in (np.inf, 3.0, 1.0, 0.5, 0.2):
                result, h_a, h_b = relocation_signature(
                    z1,
                    z2,
                    mobility_cm2_vs=mobility,
                    field_fraction=field_fraction,
                    tau_rec_ns=tau_ns,
                    n_grid=401,
                )
                stress.append(phase_peak_to_peak_deg(result))
                min_abs_h.append(
                    min(np.min(np.abs(h_a)), np.min(np.abs(h_b)))
                )
    stress = np.asarray(stress)
    print(
        f"  phase p-p min/median/max = {stress.min():.6f}/"
        f"{np.median(stress):.6f}/{stress.max():.6f} deg"
    )
    print(f"  minimum |H| anywhere in stress = {min(min_abs_h):.6f}")
    print()

    print("central velocity-saturation stress")
    saturation = {}
    for velocity_sat in (None, 5.0e5, 2.0e5, 1.0e5, 5.0e4):
        result, _, _ = relocation_signature(
            z1,
            z2,
            velocity_sat_m_s=velocity_sat,
            n_grid=401,
        )
        saturation[velocity_sat] = phase_peak_to_peak_deg(result)
        label = "none" if velocity_sat is None else f"{velocity_sat:.1e} m/s"
        print(f"  v_sat={label}: {saturation[velocity_sat]:.6f} deg")
    print()

    print("central optical-entrance surface-recombination stress")
    surface = {}
    for surface_velocity in (0.0, 1.0e4, 1.0e5, 1.0e6):
        result, _, _ = relocation_signature(
            z1,
            z2,
            surface_recombination_cm_s=surface_velocity,
            n_grid=401,
        )
        surface[surface_velocity] = phase_peak_to_peak_deg(result)
        print(
            f"  S={surface_velocity:.1e} cm/s: "
            f"{surface[surface_velocity]:.6f} deg"
        )
    print()

    # Coarse raw relocation search. This is NOT a final nuisance-aware optimum.
    centers = np.arange(2.0, 5.6001, 0.2)
    cache = {}
    for center in centers:
        cache[round(float(center), 6)] = field_induced_log_transfer(
            float(center),
            n_grid=401,
        )[0]

    candidates = []
    for i, first_center in enumerate(centers):
        for second_center in centers[i + 1 :]:
            first = cache[round(float(first_center), 6)]
            second = cache[round(float(second_center), 6)]
            raw = second - first
            raw -= np.mean(raw, axis=1, keepdims=True)
            candidates.append(
                (
                    complex_rms(raw),
                    phase_peak_to_peak_deg(raw),
                    float(first_center),
                    float(second_center),
                )
            )
    candidates.sort(reverse=True)
    best = candidates[0]
    print("coarse RAW field-induced relocation search")
    print(
        f"  best complex RMS pair = {best[2]:.1f}/{best[3]:.1f} um; "
        f"complex RMS={best[0]:.9f}; phase p-p={best[1]:.6f} deg"
    )
    print("  NOTE: interface/nuisance covariance has not yet been projected.")
    print()

    # Numerical regressions.
    assert 1.80 < central_pp < 1.82
    assert 0.62 < central_phase_rms < 0.64
    assert min(pabs1.min(), pabs2.min()) > 0.990
    assert 0.62 < min(np.min(np.abs(h1)), np.min(np.abs(h2))) < 0.64

    assert 1.84 < convergence[201] < 1.85
    assert 1.80 < convergence[401] < 1.81
    assert 1.81 < convergence[801] < 1.82
    assert 1.81 < convergence[1601] < 1.82

    assert 0.19 < stress.min() < 0.20
    assert 2.19 < np.median(stress) < 2.20
    assert 11.65 < stress.max() < 11.67

    assert 0.90 < saturation[5.0e4] < 0.94
    assert 1.43 < surface[1.0e6] < 1.46

    assert abs(best[2] - 2.0) < 1.0e-12
    assert abs(best[3] - 5.6) < 1.0e-12
    assert best[1] > 2.8

    print(
        "PASS: with the transport orientation aligned to the collecting junction, "
        "a physics-derived first-passage drift-diffusion model gives a degree-"
        "scale field-induced translated-gradient RF signature for the central "
        "stress and retains at least ~0.2 deg over a broad mobility/field/lifetime "
        "envelope. The old ad hoc 25% timing template is therefore superseded as "
        "the mechanism model. The old 4.1/5.6-um geometry is also not a final "
        "optimum: a raw central-model search pushes toward a wider 2.0/5.6-um "
        "relocation, so all geometry/RF/wavelength optimization must be redone "
        "with this operator and realistic nuisance covariance."
    )


if __name__ == "__main__":
    main()
