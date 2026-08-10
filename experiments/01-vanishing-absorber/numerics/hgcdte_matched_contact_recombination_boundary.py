"""Finite-recombination/back-boundary bracket for the matched-contact ladder.

This extends hgcdte_matched_contact_first_passage_surrogate.py without claiming
that the effective composition-gradient field has a known carrier sign in a
real device.  F(z)>0 is again interpreted conditionally as an assisting field
magnitude toward the collecting boundary z=0.

Transport model
---------------
SDE on 0<z<L:
    dz = -mu F(z) dt + sqrt(2D) dW,
    D = mu V_T.

Uniform bulk recombination is represented as Poisson killing with rate
    k = 1/tau_bulk.

For a carrier starting at z, define
    h(z) = E[ exp(-k T) I(front collection) ]
where front collection occurs at z=0.  Then h is the collection probability in
this killed process and obeys
    D h'' - mu F h' - k h = 0.

The first time-weighted collected moment
    m(z) = E[ T exp(-kT) I(front collection) ]
obeys
    D m'' - mu F m' - k m = -h.

The conditional mean collection time is m/h.

Two rigorous limiting back boundaries are used rather than inventing an
uncertain Robin coefficient:
- reflecting back surface: h'(L)=m'(L)=0;
- perfectly recombining/lossy back surface: h(L)=m(L)=0.

Front boundaries are h(0)=1, m(0)=0.

Sensitivity coordinates
-----------------------
- mu_ref = 1e4 cm^2/V/s only sets the absolute time scale;
- tau_bulk = infinity, 3, 1, 0.3, 0.1 ns are sensitivity coordinates, NOT a
  claimed lifetime range for the thought device;
- an added common assisting field = 0, 100, 300 V/cm is also a sensitivity
  coordinate, representing possible common junction/bulk drift not included in
  the composition-gradient profile itself.

For each beta=1,2,3 contrast profile, the SAME contrast optical generation
kernel is propagated through the control and contrast transport operators. This
isolates the timing effect of field redistribution once x_beta(z) is known.

No velocity saturation, traps, nonlocal transport, or self-consistent space
charge are included.  The purpose is to test whether the Einstein
first-passage sign survives finite lifetime and extreme back-boundary changes.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.sparse import csc_matrix, lil_matrix
from scipy.sparse.linalg import splu

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
MU_REF_CM2_VS = 1.0e4
D_REF_CM2_S = MU_REF_CM2_VS * V_T
N_TRANSPORT = 1201
LAMBDA_GRID = np.arange(2.80, 3.8301, 0.01)
REFERENCE_RF_HZ = 1.0e9

TAU_BULK_S = (np.inf, 3.0e-9, 1.0e-9, 0.3e-9, 0.1e-9)
COMMON_FIELDS_V_CM = (0.0, 100.0, 300.0)
BACK_BOUNDARIES = ("reflecting", "lossy")


def interpolate_profile(z_um: np.ndarray, values: np.ndarray):
    z_new = np.linspace(0.0, L_UM, N_TRANSPORT)
    return z_new, np.interp(z_new, z_um, values)


def build_operator(
    z_um: np.ndarray,
    field_v_cm: np.ndarray,
    tau_bulk_s: float,
    common_field_v_cm: float,
    back_boundary: str,
):
    """Sparse backward operator for h and m."""
    z_cm = z_um * 1.0e-4
    dz = float(z_cm[1] - z_cm[0])
    n = len(z_cm)

    field = field_v_cm + common_field_v_cm
    drift = MU_REF_CM2_VS * field
    kill = 0.0 if np.isinf(tau_bulk_s) else 1.0 / tau_bulk_s

    matrix = lil_matrix((n, n), dtype=float)

    # Front collection boundary.
    matrix[0, 0] = 1.0

    # Central second-order interior stencil.  Cell Peclet number is small on the
    # present grid, so this is stable for all sensitivity coordinates used here.
    for i in range(1, n - 1):
        matrix[i, i - 1] = (
            D_REF_CM2_S / dz**2 + drift[i] / (2.0 * dz)
        )
        matrix[i, i] = -2.0 * D_REF_CM2_S / dz**2 - kill
        matrix[i, i + 1] = (
            D_REF_CM2_S / dz**2 - drift[i] / (2.0 * dz)
        )

    if back_boundary == "reflecting":
        # Second-order Neumann derivative at z=L.
        matrix[-1, -1] = 3.0
        matrix[-1, -2] = -4.0
        matrix[-1, -3] = 1.0
    elif back_boundary == "lossy":
        # Perfectly recombining / absorbing back-surface limit.
        matrix[-1, -1] = 1.0
    else:
        raise ValueError(back_boundary)

    return splu(csc_matrix(matrix))


def solve_collection_moments(
    z_um: np.ndarray,
    field_v_cm: np.ndarray,
    tau_bulk_s: float,
    common_field_v_cm: float,
    back_boundary: str,
):
    """Return front-collection probability h and time-weighted moment m."""
    solver = build_operator(
        z_um,
        field_v_cm,
        tau_bulk_s,
        common_field_v_cm,
        back_boundary,
    )
    n = len(z_um)

    rhs_h = np.zeros(n)
    rhs_h[0] = 1.0
    h = solver.solve(rhs_h)

    rhs_m = np.zeros(n)
    rhs_m[1:-1] = -h[1:-1]
    m = solver.solve(rhs_m)

    return h, m


def generation_density(z_um: np.ndarray, x: np.ndarray, wavelength_um: float):
    """Conditional Beer-Lambert generation density per cm."""
    z_cm = z_um * 1.0e-4
    alpha = alpha_moazzami(HC_EV_UM / wavelength_um, x, T_K)
    tau = np.concatenate(([0.0], cumulative_trapezoid(alpha, z_cm)))
    p_abs = float(1.0 - np.exp(-tau[-1]))
    if p_abs <= 1.0e-14:
        raise RuntimeError("Zero modeled absorption in retained wavelength band")

    density = alpha * np.exp(-tau) / p_abs
    density /= np.trapezoid(density, z_cm)
    return density


def collected_spectrum(
    z_um: np.ndarray,
    x_generation: np.ndarray,
    h: np.ndarray,
    m: np.ndarray,
):
    """Mean time of collected carriers and collection probability vs lambda."""
    z_cm = z_um * 1.0e-4
    mean_time = []
    collection = []

    for wavelength in LAMBDA_GRID:
        density = generation_density(z_um, x_generation, wavelength)
        collected_weight = float(np.trapezoid(density * h, z_cm))
        time_weight = float(np.trapezoid(density * m, z_cm))
        mean_time.append(time_weight / collected_weight)
        collection.append(collected_weight)

    return np.asarray(mean_time), np.asarray(collection)


def timing_metrics(delta_time_s: np.ndarray):
    delta_ps = delta_time_s * 1.0e12
    endpoint_ps = float(delta_ps[-1] - delta_ps[0])
    peak_to_peak_ps = float(np.ptp(delta_ps))
    rms_centered_ps = float(
        np.sqrt(np.mean((delta_ps - np.mean(delta_ps)) ** 2))
    )
    phase_pp_deg = 360.0 * REFERENCE_RF_HZ * 1.0e-12 * peak_to_peak_ps
    return {
        "mean_ps": float(np.mean(delta_ps)),
        "endpoint_ps": endpoint_ps,
        "peak_to_peak_ps": peak_to_peak_ps,
        "rms_centered_ps": rms_centered_ps,
        "phase_pp_deg": phase_pp_deg,
    }


def main() -> None:
    z_fine, x0_fine, _, field0_fine = control_profile()
    z, field0 = interpolate_profile(z_fine, field0_fine)
    x0 = np.interp(z, z_fine, x0_fine)

    print("Matched-contact finite-recombination / back-boundary bracket")
    print(f"T={T_K:.0f} K, V_T={V_T:.6f} V")
    print(
        f"mu_ref={MU_REF_CM2_VS:.1e} cm2/Vs, "
        f"D_ref={D_REF_CM2_S:.3f} cm2/s"
    )
    print(
        "tau values and common fields are sensitivity coordinates, not measured "
        "properties of the thought device."
    )
    print()

    all_rows = {beta: [] for beta in BETA_VALUES}

    for beta in BETA_VALUES:
        _, x_beta_fine, _, field_beta_fine, _, _ = contrast_profile(beta)
        x_beta = np.interp(z, z_fine, x_beta_fine)
        field_beta = np.interp(z, z_fine, field_beta_fine)

        for back in BACK_BOUNDARIES:
            for tau_bulk in TAU_BULK_S:
                for common_field in COMMON_FIELDS_V_CM:
                    h0, m0 = solve_collection_moments(
                        z,
                        field0,
                        tau_bulk,
                        common_field,
                        back,
                    )
                    h1, m1 = solve_collection_moments(
                        z,
                        field_beta,
                        tau_bulk,
                        common_field,
                        back,
                    )

                    # Use the SAME contrast generation profile in null and
                    # alternative to isolate transport after x_beta(z) is known.
                    t0, c0 = collected_spectrum(z, x_beta, h0, m0)
                    t1, c1 = collected_spectrum(z, x_beta, h1, m1)
                    metrics = timing_metrics(t1 - t0)

                    all_rows[beta].append(
                        {
                            "back": back,
                            "tau": tau_bulk,
                            "common_field": common_field,
                            **metrics,
                            "collection_ratio_min": float(np.min(c1 / c0)),
                            "collection_ratio_max": float(np.max(c1 / c0)),
                        }
                    )

        rows = all_rows[beta]
        mean_values = np.asarray([row["mean_ps"] for row in rows])
        endpoint_values = np.asarray([row["endpoint_ps"] for row in rows])
        pp_values = np.asarray([row["peak_to_peak_ps"] for row in rows])
        phase_values = np.asarray([row["phase_pp_deg"] for row in rows])
        cmin = np.asarray([row["collection_ratio_min"] for row in rows])
        cmax = np.asarray([row["collection_ratio_max"] for row in rows])

        print(f"beta={beta:.0f}")
        print(
            f"  mean transport change over lambda = "
            f"{mean_values.min():.3f} to {mean_values.max():.3f} ps"
        )
        print(
            f"  endpoint differential [dt(3.83)-dt(2.80)] = "
            f"{endpoint_values.min():.3f} to {endpoint_values.max():.3f} ps"
        )
        print(
            f"  spectral timing p-p = {pp_values.min():.3f} to "
            f"{pp_values.max():.3f} ps"
        )
        print(
            f"  equivalent phase p-p @1GHz = {phase_values.min():.3f} to "
            f"{phase_values.max():.3f} deg"
        )
        print(
            f"  collection-probability ratio contrast/control = "
            f"{cmin.min():.3f} to {cmax.max():.3f}"
        )
        print()

    # Regression / sign anchors.
    b1 = all_rows[1.0]
    b2 = all_rows[2.0]
    b3 = all_rows[3.0]

    mean1 = np.asarray([row["mean_ps"] for row in b1])
    mean2 = np.asarray([row["mean_ps"] for row in b2])
    mean3 = np.asarray([row["mean_ps"] for row in b3])
    assert np.max(mean1) < -0.52
    assert np.max(mean2) < -1.06
    assert np.max(mean3) < -1.65

    phase1 = np.asarray([row["phase_pp_deg"] for row in b1])
    phase2 = np.asarray([row["phase_pp_deg"] for row in b2])
    phase3 = np.asarray([row["phase_pp_deg"] for row in b3])
    assert 0.44 < phase1.min() < 0.45
    assert 4.28 < phase1.max() < 4.30
    assert 0.84 < phase2.min() < 0.85
    assert 7.61 < phase2.max() < 7.63
    assert 1.19 < phase3.min() < 1.20
    assert 10.15 < phase3.max() < 10.17

    # Beta=3 endpoint differential remains negative throughout this complete
    # drift-diffusion sensitivity bracket.
    endpoint3 = np.asarray([row["endpoint_ps"] for row in b3])
    assert np.max(endpoint3) < -0.73

    # Collection efficiency is not invariant once killing/back loss is included.
    min_ratio3 = min(row["collection_ratio_min"] for row in b3)
    max_ratio3 = max(row["collection_ratio_max"] for row in b3)
    assert 0.84 < min_ratio3 < 0.86
    assert 1.13 < max_ratio3 < 1.14

    print(
        "PASS: inside the Einstein drift-diffusion family, the buried-gradient "
        "ladder's mean timing change remains a speedup across both extreme back "
        "boundaries, five bulk-lifetime sensitivities, and 0-300 V/cm added "
        "common assisting field. The effect shrinks strongly as killing/common "
        "field increase, and collection probability can also change materially. "
        "This robustness does NOT resolve the earlier deterministic-drift "
        "collision; it shows only that finite lifetime and back loss do not by "
        "themselves flip the Einstein first-passage result over this bracket."
    )


if __name__ == "__main__":
    main()
