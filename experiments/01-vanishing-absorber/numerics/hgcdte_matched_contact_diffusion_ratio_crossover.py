"""Continuous transport crossover between local drift and drift-diffusion.

For local drift-diffusion

    D T'' - mu F T' = -1,

write

    Theta = D/mu   [volts],
    U = mu T.

Then

    Theta U'' - F U' = -1.

Theta therefore controls the relative diffusion/drift weighting independently
of the absolute mobility scale. The deterministic local-drift limit is
Theta->0. The nondegenerate Einstein reference at 300 K is
Theta_E = k_B T/q ~=25.85 mV.

This script uses the preferred downstream-compensated matched-contact family,
reflecting back boundary, infinite bulk lifetime, and common assisting-field
sensitivities 0, 100, 300 V/cm. For beta=1,2,3 it locates where two transport
observables change sign as Theta is swept:

1. wavelength-averaged contrast-minus-control mean timing shift;
2. gauge-free endpoint differential
       deltaT(3.83 um)-deltaT(2.80 um).

The SAME contrast optical generation kernel is used for null and alternative,
so the sign change is a transport-model effect rather than a control/contrast
optical-generation difference.

No claim is made that D/mu in a real graded HgCdTe device equals the classical
Einstein value. Theta is the experimentally/model-relevant transport ratio to
be constrained.
"""

from __future__ import annotations

from functools import lru_cache

import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.optimize import brentq
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
from hgcdte_matched_contact_recombination_boundary import (
    K_B_EV_K,
    LAMBDA_GRID,
    MU_REF_CM2_VS,
    N_TRANSPORT,
)

T_K = 300.0
THETA_EINSTEIN_V = K_B_EV_K * T_K
COMMON_FIELDS_V_CM = (0.0, 100.0, 300.0)
SEARCH_THETA_V = (0.5e-3, 50.0e-3)
N_SCAN = 55


def interpolate_profile(z_um: np.ndarray, values: np.ndarray):
    z_new = np.linspace(0.0, L_UM, N_TRANSPORT)
    return z_new, np.interp(z_new, z_um, values)


def trapezoid_weights(z_cm: np.ndarray) -> np.ndarray:
    weights = np.empty_like(z_cm)
    weights[0] = 0.5 * (z_cm[1] - z_cm[0])
    weights[-1] = 0.5 * (z_cm[-1] - z_cm[-2])
    weights[1:-1] = 0.5 * (z_cm[2:] - z_cm[:-2])
    return weights


def generation_weight_matrix(z_um: np.ndarray, x: np.ndarray) -> np.ndarray:
    """Rows integrate conditional generation density against any T(z)."""
    z_cm = z_um * 1.0e-4
    quadrature = trapezoid_weights(z_cm)
    rows = []

    for wavelength in LAMBDA_GRID:
        alpha = alpha_moazzami(HC_EV_UM / wavelength, x, T_K)
        tau = np.concatenate(([0.0], cumulative_trapezoid(alpha, z_cm)))
        p_abs = float(1.0 - np.exp(-tau[-1]))
        if p_abs <= 1.0e-14:
            raise RuntimeError("Zero modeled absorption in crossover wavelength band")
        density = alpha * np.exp(-tau) / p_abs
        density /= np.sum(density * quadrature)
        rows.append(density * quadrature)

    return np.asarray(rows)


def solve_mean_time(
    z_um: np.ndarray,
    field_v_cm: np.ndarray,
    theta_v: float,
    common_field_v_cm: float,
):
    """Mean first-passage time for reflecting back boundary, no killing."""
    z_cm = z_um * 1.0e-4
    dz = float(z_cm[1] - z_cm[0])
    n = len(z_cm)

    diffusion = MU_REF_CM2_VS * theta_v
    drift = MU_REF_CM2_VS * (field_v_cm + common_field_v_cm)

    matrix = lil_matrix((n, n), dtype=float)
    matrix[0, 0] = 1.0

    for i in range(1, n - 1):
        matrix[i, i - 1] = diffusion / dz**2 + drift[i] / (2.0 * dz)
        matrix[i, i] = -2.0 * diffusion / dz**2
        matrix[i, i + 1] = diffusion / dz**2 - drift[i] / (2.0 * dz)

    matrix[-1, -1] = 3.0
    matrix[-1, -2] = -4.0
    matrix[-1, -3] = 1.0

    rhs = np.zeros(n)
    rhs[1:-1] = -1.0
    return splu(csc_matrix(matrix)).solve(rhs)


def build_context(beta: float):
    z0_fine, _, _, field0_fine = control_profile()
    _, x1_fine, _, field1_fine, _, _ = contrast_profile(beta)

    z, field0 = interpolate_profile(z0_fine, field0_fine)
    x1 = np.interp(z, z0_fine, x1_fine)
    field1 = np.interp(z, z0_fine, field1_fine)
    generation_weights = generation_weight_matrix(z, x1)

    return {
        "z": z,
        "field0": field0,
        "field1": field1,
        "generation_weights": generation_weights,
    }


def make_observer(context: dict, common_field_v_cm: float):
    """Return cached transport observables as a function of Theta."""

    @lru_cache(maxsize=256)
    def observe(theta_key: float):
        theta_v = float(theta_key)
        T0 = solve_mean_time(
            context["z"], context["field0"], theta_v, common_field_v_cm
        )
        T1 = solve_mean_time(
            context["z"], context["field1"], theta_v, common_field_v_cm
        )

        spectrum0 = context["generation_weights"] @ T0
        spectrum1 = context["generation_weights"] @ T1
        delta_ps = (spectrum1 - spectrum0) * 1.0e12

        return (
            float(np.mean(delta_ps)),
            float(delta_ps[-1] - delta_ps[0]),
            float(np.ptp(delta_ps)),
        )

    return observe


def bracket_roots(grid: np.ndarray, values: np.ndarray, function):
    roots = []
    for left, right, f_left, f_right in zip(
        grid[:-1], grid[1:], values[:-1], values[1:]
    ):
        if f_left * f_right < 0.0:
            roots.append(brentq(function, left, right, xtol=2.0e-9))
    return roots


def scan_context(context: dict, common_field_v_cm: float):
    observe = make_observer(context, common_field_v_cm)
    grid = np.linspace(SEARCH_THETA_V[0], SEARCH_THETA_V[1], N_SCAN)
    values = np.asarray([observe(float(theta)) for theta in grid])

    mean_roots = bracket_roots(
        grid,
        values[:, 0],
        lambda theta: observe(float(theta))[0],
    )
    endpoint_roots = bracket_roots(
        grid,
        values[:, 1],
        lambda theta: observe(float(theta))[1],
    )
    at_einstein = observe(float(THETA_EINSTEIN_V))

    return mean_roots, endpoint_roots, {
        "mean_ps": at_einstein[0],
        "endpoint_ps": at_einstein[1],
        "peak_to_peak_ps": at_einstein[2],
    }


def main() -> None:
    print("Matched-contact D/mu transport-sign crossover")
    print(f"300 K Einstein reference D/mu = {1e3*THETA_EINSTEIN_V:.3f} mV")
    print(
        f"root search = {1e3*SEARCH_THETA_V[0]:.1f}-"
        f"{1e3*SEARCH_THETA_V[1]:.1f} mV"
    )
    print()

    results = {}
    for beta in BETA_VALUES:
        context = build_context(beta)
        print(f"beta={beta:.0f}")

        for common_field in COMMON_FIELDS_V_CM:
            mean_roots, endpoint_roots, at_einstein = scan_context(
                context, common_field
            )
            results[(beta, common_field)] = (
                mean_roots,
                endpoint_roots,
                at_einstein,
            )

            mean_text = (
                ", ".join(f"{1e3*r:.3f}" for r in mean_roots)
                if mean_roots
                else "none in search interval"
            )
            endpoint_text = (
                ", ".join(f"{1e3*r:.3f}" for r in endpoint_roots)
                if endpoint_roots
                else "none in search interval"
            )

            print(f"  common field {common_field:.0f} V/cm")
            print(f"    mean-timing zero(s): {mean_text} mV")
            print(f"    endpoint-differential zero(s): {endpoint_text} mV")
            print(
                f"    at D/mu=kT/q: mean={at_einstein['mean_ps']:.3f} ps, "
                f"endpoint={at_einstein['endpoint_ps']:.3f} ps, "
                f"p-p={at_einstein['peak_to_peak_ps']:.3f} ps"
            )
        print()

    r10 = results[(1.0, 0.0)]
    r20 = results[(2.0, 0.0)]
    r30 = results[(3.0, 0.0)]

    assert len(r10[0]) == 0
    assert 9.14e-3 < r10[1][0] < 9.17e-3

    assert 6.62e-3 < r20[0][0] < 6.65e-3
    assert 13.44e-3 < r20[1][0] < 13.48e-3

    assert 8.91e-3 < r30[0][0] < 8.95e-3
    assert 15.82e-3 < r30[1][0] < 15.86e-3

    endpoint_roots_all = [
        root
        for _, endpoint_roots, _ in results.values()
        for root in endpoint_roots
    ]
    maximum_endpoint_root = max(endpoint_roots_all)
    assert 21.37e-3 < maximum_endpoint_root < 21.43e-3
    assert maximum_endpoint_root < THETA_EINSTEIN_V

    for _, _, at_einstein in results.values():
        assert at_einstein["endpoint_ps"] < 0.0
        assert at_einstein["mean_ps"] < 0.0

    print(
        "largest endpoint-differential crossover over beta/common-field bracket = "
        f"{1e3*maximum_endpoint_root:.3f} mV"
    )
    print(
        f"classical 300 K kT/q sits {1e3*(THETA_EINSTEIN_V-maximum_endpoint_root):.3f} "
        "mV above that crossover."
    )
    print()
    print(
        "PASS: the deterministic-versus-diffusive disagreement is a continuous "
        "D/mu crossover rather than an arbitrary numerical contradiction. For "
        "the stronger beta=2/3 devices with zero common field, the wavelength-"
        "averaged timing change flips near ~6.63/~8.93 mV and the gauge-free "
        "endpoint differential flips near ~13.46/~15.84 mV. Across the complete "
        "0-300 V/cm common-field bracket, the largest endpoint crossover is "
        "~21.41 mV, below the classical 300 K Einstein value 25.85 mV. Thus a "
        "nondegenerate Einstein model lies consistently on the speedup side, "
        "while sufficiently small D/mu approaches the local-drift penalty. The "
        "real device prediction now hinges on constraining D/mu and carrier/band-"
        "edge orientation rather than on lifetime or back-boundary choice alone."
    )


if __name__ == "__main__":
    main()
