"""Minimal transport collision for the downstream-compensated matched-contact family.

This file does NOT assign the published device's electron/hole band-edge
orientation. Instead F(z)>0 is explicitly interpreted as an effective field
magnitude that assists the collected minority carrier toward z=0.

Two deliberately simple transport limits are compared using exactly the same
field profiles:

1. deterministic local drift
       v(z)=mu F(z)
       T_drift(z)=int_0^z ds/[mu F(s)]

2. Einstein drift-diffusion first passage
       D=mu V_T
       dz = -mu F(z) dt + sqrt(2D)dW
   with absorbing collection at z=0 and reflecting back boundary at z=L.
   The mean first-passage time obeys
       D T'' - mu F T' = -1,
       T(0)=0, T'(L)=0.

Writing U=mu*T removes the mobility from the differential equation:
       V_T U'' - F U' = -1.
Hence the spectral SHAPE of the drift-diffusion timing perturbation is mobility
independent; absolute time scales as 1/mu.

The contrast optics are included explicitly. The model-discrimination observable
is the difference between:
- null: contrast optical generation p_beta(z,lambda) propagated through control
  transport T0(z);
- alternative: the SAME contrast optical generation propagated through the
  contrast transport T_beta(z).
This isolates the transport-model contribution once x_beta(z) is known.

No velocity saturation, hot-electron effects, recombination, traps, junction
field, self-consistent space charge, or calibrated boundary physics are included.
The point is to test model dependence, not to predict device speed.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import cumulative_trapezoid

from hgcdte_sample_a_constraint_family_joint_iso_kernel import (
    HC_EV_UM,
    alpha_moazzami,
)
from hgcdte_matched_contact_downstream_compensation import (
    BETA_VALUES,
    L_UM,
    control_profile,
    contrast_profile,
)

K_B_EV_K = 8.617333262e-5
T_K = 300.0
V_T = K_B_EV_K * T_K
LAMBDA_GRID = np.arange(2.80, 3.8301, 0.01)
REFERENCE_MOBILITY_CM2_VS = 1.0e4
REFERENCE_RF_HZ = 1.0e9


def deterministic_U(z_um: np.ndarray, field_v_cm: np.ndarray) -> np.ndarray:
    """Return U=mu*T for deterministic local drift, units cm^2/V."""
    z_cm = z_um * 1.0e-4
    return np.concatenate(
        ([0.0], cumulative_trapezoid(1.0 / field_v_cm, z_cm))
    )


def drift_diffusion_U(z_um: np.ndarray, field_v_cm: np.ndarray) -> np.ndarray:
    """Return U=mu*T for absorbing-front / reflecting-back first passage."""
    z_cm = z_um * 1.0e-4

    # y=dU/dz obeys y'-(F/V_T)y=-1/V_T with y(L)=0.
    action = np.concatenate(
        ([0.0], cumulative_trapezoid(field_v_cm / V_T, z_cm))
    )
    integrating_factor = np.exp(-action)

    cumulative = np.concatenate(
        ([0.0], cumulative_trapezoid(integrating_factor / V_T, z_cm))
    )
    reverse_integral = cumulative[-1] - cumulative
    y = reverse_integral / integrating_factor

    return np.concatenate(([0.0], cumulative_trapezoid(y, z_cm)))


def generation_density(
    z_um: np.ndarray,
    x: np.ndarray,
    wavelength_um: float,
) -> tuple[float, np.ndarray]:
    """Conditional generation density per cm."""
    z_cm = z_um * 1.0e-4
    alpha = alpha_moazzami(HC_EV_UM / wavelength_um, x, T_K)
    tau = np.concatenate(([0.0], cumulative_trapezoid(alpha, z_cm)))
    p_abs = float(1.0 - np.exp(-tau[-1]))
    density = alpha * np.exp(-tau) / p_abs
    density /= np.trapezoid(density, z_cm)
    return p_abs, density


def mean_U_spectrum(
    z_um: np.ndarray,
    x_for_generation: np.ndarray,
    U: np.ndarray,
) -> np.ndarray:
    z_cm = z_um * 1.0e-4
    values = []
    for wavelength in LAMBDA_GRID:
        _, density = generation_density(z_um, x_for_generation, wavelength)
        values.append(float(np.trapezoid(U * density, z_cm)))
    return np.asarray(values)


def phase_metrics(delta_U: np.ndarray, mobility_cm2_vs: float):
    """Differential spectral phase after removing wavelength-independent delay."""
    delay_ps = delta_U / mobility_cm2_vs * 1.0e12
    centered_ps = delay_ps - np.mean(delay_ps)
    phase_deg = -360.0 * REFERENCE_RF_HZ * 1.0e-12 * centered_ps
    return (
        float(np.ptp(phase_deg)),
        float(np.sqrt(np.mean(phase_deg**2))),
        float(np.min(delay_ps)),
        float(np.max(delay_ps)),
    )


def main() -> None:
    z, x0, _, field0 = control_profile()
    U0_drift = deterministic_U(z, field0)
    U0_dd = drift_diffusion_U(z, field0)

    print("Matched-contact first-passage transport collision")
    print(
        "F(z) is an assumed collection-assisting effective field magnitude; "
        "electron/hole band-edge orientation is not asserted here."
    )
    print(f"T={T_K:.0f} K, V_T={V_T:.6f} V")
    print(
        f"control integrated field drop = "
        f"{np.trapezoid(field0,z*1e-4):.6f} V "
        f"(~{np.trapezoid(field0,z*1e-4)/V_T:.2f} kT/q)"
    )
    print()
    print(
        f"control back transit at mu={REFERENCE_MOBILITY_CM2_VS:.1e} cm2/Vs:"
    )
    print(
        f"  deterministic drift = "
        f"{U0_drift[-1]/REFERENCE_MOBILITY_CM2_VS*1e12:.3f} ps"
    )
    print(
        f"  drift-diffusion first passage = "
        f"{U0_dd[-1]/REFERENCE_MOBILITY_CM2_VS*1e12:.3f} ps"
    )
    print()

    stored = {}
    for beta in BETA_VALUES:
        _, x1, _, field1, _, _ = contrast_profile(beta)
        U1_drift = deterministic_U(z, field1)
        U1_dd = drift_diffusion_U(z, field1)

        # Transport-only model discrimination using the SAME known contrast
        # generation kernel in null and alternative.
        null_drift = mean_U_spectrum(z, x1, U0_drift)
        alt_drift = mean_U_spectrum(z, x1, U1_drift)
        null_dd = mean_U_spectrum(z, x1, U0_dd)
        alt_dd = mean_U_spectrum(z, x1, U1_dd)

        drift_metrics = phase_metrics(
            alt_drift - null_drift, REFERENCE_MOBILITY_CM2_VS
        )
        dd_metrics = phase_metrics(
            alt_dd - null_dd, REFERENCE_MOBILITY_CM2_VS
        )
        stored[beta] = (drift_metrics, dd_metrics, U1_drift, U1_dd)

        print(f"beta={beta:.0f}")
        print(
            f"  back transit deterministic = "
            f"{U1_drift[-1]/REFERENCE_MOBILITY_CM2_VS*1e12:.3f} ps"
        )
        print(
            f"  back transit drift-diffusion = "
            f"{U1_dd[-1]/REFERENCE_MOBILITY_CM2_VS*1e12:.3f} ps"
        )
        print(
            f"  deterministic model-discrimination phase p-p/RMS @1GHz = "
            f"{drift_metrics[0]:.3f}/{drift_metrics[1]:.3f} deg"
        )
        print(
            f"  drift-diffusion model-discrimination phase p-p/RMS @1GHz = "
            f"{dd_metrics[0]:.3f}/{dd_metrics[1]:.3f} deg"
        )
        print(
            "  all quoted phase values scale exactly as "
            f"({REFERENCE_MOBILITY_CM2_VS:.0f} cm2/Vs)/mu in these surrogates"
        )
        print()

    # The same endpoint bandgap drop is redistributed, not increased.
    for beta in BETA_VALUES:
        _, _, _, field1, _, _ = contrast_profile(beta)
        assert abs(
            np.trapezoid(field1, z * 1.0e-4)
            - np.trapezoid(field0, z * 1.0e-4)
        ) < 5.0e-4

    # Regression anchors.
    d1, q1, _, _ = stored[1.0]
    d2, q2, _, _ = stored[2.0]
    d3, q3, U3d, U3q = stored[3.0]

    assert 10.67 < d1[0] < 10.69
    assert 33.68 < d2[0] < 33.71
    assert 87.7 < d3[0] < 87.9

    assert 4.28 < q1[0] < 4.30
    assert 7.61 < q2[0] < 7.63
    assert 10.15 < q3[0] < 10.17

    assert U3d[-1] > U0_drift[-1]
    assert U3q[-1] < U0_dd[-1]

    print(
        "PASS: the sign and magnitude of the buried-gradient timing response are "
        "strongly transport-model dependent even when the same effective field "
        "is assumed to assist collection. Deterministic local drift predicts a "
        "large transit penalty from the low-field compensation, whereas an "
        "absorbing-front/reflecting-back Einstein drift-diffusion first-passage "
        "model predicts a modest net speedup. Therefore the matched-contact "
        "geometry is promising for validation, but its timing response cannot be "
        "predicted credibly without specifying diffusion, boundaries, recombination, "
        "and high-field transport."
    )


if __name__ == "__main__":
    main()
