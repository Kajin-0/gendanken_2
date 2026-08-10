"""Multi-distance p-HgCdTe transport-witness measurement design.

This script converts the witness-posterior requirements into directly measurable
packet-observable requirements for a uniform-composition Shockley-Haynes / pulse-
transport witness.

Uniform drift-diffusion reference
---------------------------------
For a packet traveling distance L at approximately uniform drift velocity v,

    mean t(L) = t0 + L/v,

    Var[t](L) = sigma0^2 + 2 D L / v^3,

and for uniform first-order loss

    ln Q(L) = ln Q0 - L/(v tau).

Thus multiple propagation distances make

    t0, sigma0^2, ln Q0

intercepts, while the slopes determine

    v, D, tau.

This is exactly the covariance structure desired by the relocation inverse:
common time zero, pulse width and injection amplitude need not be known a priori.

Central scale only
------------------
To produce timing/voltage numbers, use the same synthetic central velocity law
as the witness-posterior regression:

    v = mu E/[1+(E/d)^r]
    mu = 9000 cm2/Vs
    d = 8 kV/cm
    r = 2.2

with

    D = mu kT/q
    tau = 1 ns
    T = 300 K.

These are NOT proposed material constants.

Distances
---------
Primary compact set:
    5,10,20,40,70,100 um.

At each field, points with synthetic Q/Q0 < 0.05 are omitted from the slope
precision estimate.

A second extended set to 200 um illustrates how longer paths relax high-field
D precision at the cost of larger voltage and more recombination loss.

Precision metrics
-----------------
1. For t=t0+bL with equal independent centroid error sigma_t,

       sigma_b = sigma_t / sqrt(sum (L-Lbar)^2).

   The script reports sigma_t that would give 25% or 10% relative v precision.

2. For ln Q=a-L/(v tau), the script reports equal sigma_lnQ per point giving
   50% slope/tau precision (assuming v is separately known).

3. For variance versus distance, assume an illustrative common RMS temporal
   width sigma0=30 ps and equal RMS-width measurement error sigma_width. A
   weighted linear fit of variance versus L gives the sigma_width that produces
   50% relative D uncertainty.

The 30-ps intercept is only a design stress. A real instrument response must be
measured, and its covariance propagated.

No novelty claim.
"""

from __future__ import annotations

import numpy as np

T_K = 300.0
KBT_OVER_Q_V = 8.617333262145e-5 * T_K
MU_CM2_VS = 9000.0
D_KV_CM = 8.0
R = 2.2
TAU_NS = 1.0

FIELDS_V_CM = np.asarray((100.0, 300.0, 500.0, 1000.0, 1500.0, 2000.0, 2500.0, 3000.0))
COMPACT_DISTANCES_UM = np.asarray((5.0, 10.0, 20.0, 40.0, 70.0, 100.0))
EXTENDED_DISTANCES_UM = np.asarray((5.0, 10.0, 20.0, 40.0, 80.0, 120.0, 160.0, 200.0))
Q_MIN = 0.05
SIGMA0_PS = 30.0


def velocity_cm_s(field_v_cm: float) -> float:
    return float(
        MU_CM2_VS
        * field_v_cm
        / (1.0 + (abs(field_v_cm) / (1000.0 * D_KV_CM)) ** R)
    )


def usable_points(field_v_cm: float, distances_um: np.ndarray):
    velocity = velocity_cm_s(field_v_cm)
    length_cm = distances_um * 1.0e-4
    time_s = length_cm / velocity
    survival = np.exp(-time_s / (TAU_NS * 1.0e-9))
    mask = survival >= Q_MIN
    return velocity, length_cm[mask], time_s[mask], survival[mask]


def centroid_precision_for_relative_velocity(
    field_v_cm: float,
    distances_um: np.ndarray,
    relative_velocity_sigma: float,
):
    velocity, length_cm, time_s, survival = usable_points(
        field_v_cm,
        distances_um,
    )
    sxx = float(np.sum((length_cm - np.mean(length_cm)) ** 2))
    slope = 1.0 / velocity
    sigma_t = relative_velocity_sigma * slope * np.sqrt(sxx)
    return sigma_t, length_cm, time_s, survival


def log_amplitude_precision_for_relative_tau(
    field_v_cm: float,
    distances_um: np.ndarray,
    relative_tau_sigma: float,
):
    velocity, length_cm, _, survival = usable_points(field_v_cm, distances_um)
    sxx = float(np.sum((length_cm - np.mean(length_cm)) ** 2))
    slope_abs = 1.0 / (velocity * TAU_NS * 1.0e-9)
    sigma_lnq = relative_tau_sigma * slope_abs * np.sqrt(sxx)
    return sigma_lnq, survival


def width_precision_for_relative_diffusion(
    field_v_cm: float,
    distances_um: np.ndarray,
    relative_D_sigma: float,
    sigma0_ps: float = SIGMA0_PS,
):
    velocity, length_cm, _, survival = usable_points(field_v_cm, distances_um)
    diffusion = MU_CM2_VS * KBT_OVER_Q_V
    slope = 2.0 * diffusion / velocity**3

    sigma0_s = sigma0_ps * 1.0e-12
    observed_sigma = np.sqrt(sigma0_s**2 + slope * length_cm)

    # Calculate relative slope/D error for 1-ps RMS width measurement error.
    sigma_width_1ps = 1.0e-12
    sigma_variance = 2.0 * observed_sigma * sigma_width_1ps
    design = np.column_stack((np.ones(len(length_cm)), length_cm))
    weight = np.diag(1.0 / sigma_variance**2)
    covariance = np.linalg.inv(design.T @ weight @ design)
    sigma_slope_for_1ps = float(np.sqrt(covariance[1, 1]))
    relative_for_1ps = sigma_slope_for_1ps / slope

    allowed_sigma_width_ps = relative_D_sigma / relative_for_1ps
    return allowed_sigma_width_ps, observed_sigma * 1.0e12, survival


def summarize(distances_um: np.ndarray, title: str):
    print(title)
    print("distances um = " + ", ".join(f"{value:.0f}" for value in distances_um))
    print()

    for field in FIELDS_V_CM:
        velocity, length_cm, time_s, survival = usable_points(field, distances_um)
        sigma_t_25, _, _, _ = centroid_precision_for_relative_velocity(
            field,
            distances_um,
            0.25,
        )
        sigma_t_10, _, _, _ = centroid_precision_for_relative_velocity(
            field,
            distances_um,
            0.10,
        )
        sigma_lnq_50, _ = log_amplitude_precision_for_relative_tau(
            field,
            distances_um,
            0.50,
        )
        sigma_width_50, observed_sigma, _ = width_precision_for_relative_diffusion(
            field,
            distances_um,
            0.50,
        )

        voltage_max = field * np.max(length_cm)
        span_ns = (time_s[-1] - time_s[0]) * 1.0e9
        print(
            f"E={field/1000:.1f} kV/cm; usable N={len(length_cm)}; "
            f"max L={np.max(length_cm)*1e4:.0f} um; "
            f"Vmax={voltage_max:.1f} V; Qmin={np.min(survival):.3f}"
        )
        print(
            f"  transit span={span_ns:.3f} ns; "
            f"sigma_t/trace for 25% v={sigma_t_25*1e12:.1f} ps; "
            f"for 10% v={sigma_t_10*1e12:.1f} ps"
        )
        print(
            f"  sigma_lnQ/point for 50% tau={sigma_lnq_50:.3f}; "
            f"sigma_width for 50% D={sigma_width_50:.2f} ps"
        )
        print(
            f"  observed RMS-width range with sigma0={SIGMA0_PS:.0f} ps: "
            f"{observed_sigma[0]:.1f}-{observed_sigma[-1]:.1f} ps"
        )
    print()


def main() -> None:
    print("HgCdTe multi-distance transport-witness measurement scales")
    print(
        f"central synthetic mu={MU_CM2_VS:.0f} cm2/Vs, d={D_KV_CM:.1f} kV/cm, "
        f"r={R:.1f}, tau={TAU_NS:.1f} ns"
    )
    print(
        "All precision numbers are regression-design scales, not instrument "
        "specifications or material predictions."
    )
    print()

    summarize(COMPACT_DISTANCES_UM, "COMPACT WITNESS SET")
    summarize(EXTENDED_DISTANCES_UM, "EXTENDED HIGH-FIELD D STRESS")

    # Canonical compact-set regression anchors.
    sigma_t_25_3k, _, _, _ = centroid_precision_for_relative_velocity(
        3000.0,
        COMPACT_DISTANCES_UM,
        0.25,
    )
    sigma_t_10_3k, _, _, _ = centroid_precision_for_relative_velocity(
        3000.0,
        COMPACT_DISTANCES_UM,
        0.10,
    )
    sigma_lnq_3k, _ = log_amplitude_precision_for_relative_tau(
        3000.0,
        COMPACT_DISTANCES_UM,
        0.50,
    )
    sigma_width_3k, _, _ = width_precision_for_relative_diffusion(
        3000.0,
        COMPACT_DISTANCES_UM,
        0.50,
    )
    sigma_width_3k_long, _, _ = width_precision_for_relative_diffusion(
        3000.0,
        EXTENDED_DISTANCES_UM,
        0.50,
    )

    assert 86.0 < sigma_t_25_3k * 1.0e12 < 87.0
    assert 34.0 < sigma_t_10_3k * 1.0e12 < 35.0
    assert 0.17 < sigma_lnq_3k < 0.18
    assert 2.0 < sigma_width_3k < 2.2
    assert 4.4 < sigma_width_3k_long < 4.7

    print(
        "PASS: a multi-distance witness converts the required transport posterior "
        "into modest slope measurements. For the compact 5-100 um set, even the "
        "3-kV/cm velocity point needs only ~87-ps centroid precision per trace for "
        "25% v precision, and ~17% log-amplitude precision per point gives a "
        "50% lifetime slope. High-field diffusion is the hardest observable: "
        "with a 30-ps common width, 50% D at 3 kV/cm requires ~2-ps RMS width "
        "precision over 5-100 um; extending the path to 200 um relaxes that to "
        "~4.5 ps at the cost of ~60 V."
    )


if __name__ == "__main__":
    main()
