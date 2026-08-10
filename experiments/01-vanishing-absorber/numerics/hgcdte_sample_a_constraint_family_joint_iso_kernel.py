"""Constraint-family joint iso-kernel test for published HgCdTe samples A/B.

This is NOT a digitization or calibrated reconstruction of sample A.

The 2023 Xu et al. article gives the composition fit form and several textual
constraints but the numerical Fig. 3 fit parameters are not machine-readable.
This script asks a narrower robustness question:

    Does the existence/location of a useful common A/B temperature iso-kernel
    wavelength depend strongly on the unresolved sample-A profile parameters?

Sample A is represented by an explicit sensitivity family constrained by the
published processed thickness, nominal FTIR composition, ~4 um nonlinear
interdiffusion width, 100-200 V/cm linear-field range with A about 30 V/cm
larger than B, and ~2000 V/cm processed surface nonlinear field. The ranges
around 4 um and 2000 V/cm are sensitivity ranges, NOT reported uncertainties.
Both mathematical roots of the surface-field constraint are retained.

Optics use the same Hansen gap and Moazzami above-gap Beer-Lambert model as the
existing sample-B repository calculations. Reflection/interference/Urbach
absorption are omitted; this is especially important for sample A near cutoff.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.optimize import brentq, minimize_scalar
from scipy.special import erf

HC_EV_UM = 1.2398419843320026
N_FINE = 4001
N_CELL = 80

# Published / repository-conditional inputs.
W_A_UM = 7.6
X_A_LOW = 0.320  # conditional: reported FTIR x treated as growth-surface endpoint
W_B_UM = 3.7
X_B_LOW = 0.316
B_FIELD_300_V_CM = 150.0  # current central sample-B repository envelope

# Text-constrained sample-A sensitivity family.
# The article says both linear fields are 100-200 V/cm and A exceeds B by ~30.
A_LINEAR_FIELDS_V_CM = (130.0, 150.0, 180.0, 200.0)
# Article says nonlinear/interdiffusion region thickness is close to 4 um.
# +/-0.5 um is a sensitivity span, not an experimental error bar.
A_DELTA_Z_UM = (3.5, 4.0, 4.5)
# Article says processed A surface field reaches ~2000 V/cm.
# +/-200 V/cm is a sensitivity span, not an experimental error bar.
A_FRONT_FIELDS_V_CM = (1800.0, 2000.0, 2200.0)

REFERENCE_LAMBDAS_UM = (3.410, 3.632, 3.840)
TARGET_T_K = (215.0, 115.0)
SEARCH_LAMBDA_UM = (2.0, 6.0)


def eg_hansen(x: np.ndarray | float, T: float) -> np.ndarray | float:
    return (
        -0.302
        + 1.93 * x
        + 5.35e-4 * T * (1.0 - 2.0 * x)
        - 0.81 * x**2
        + 0.832 * x**3
    )


def deg_dx_hansen(x: np.ndarray | float, T: float) -> np.ndarray | float:
    return 1.93 - 2.0 * 0.81 * x + 3.0 * 0.832 * x**2 - 2.0 * 5.35e-4 * T


def k_moazzami(x: np.ndarray | float, T: float) -> np.ndarray | float:
    return (
        -20060.0
        + 115750.0 * x
        + 32.43 * T
        - 64170.0 * x**2
        + 0.43231 * T**2
        - 101.92 * x * T
    )


def n_moazzami(x: np.ndarray | float, T: float) -> np.ndarray | float:
    return 0.74487 - 0.44513 * x + (0.000799 - 0.000757 * x) * T


def alpha_moazzami(E: float, x: np.ndarray, T: float) -> np.ndarray:
    gap = eg_hansen(x, T)
    fraction = (E - gap) / E
    alpha = np.zeros_like(x, dtype=float)
    mask = fraction > 0.0
    alpha[mask] = k_moazzami(x[mask], T) * fraction[mask] ** n_moazzami(
        x[mask], T
    )
    return np.maximum(alpha, 0.0)


def x_fit(
    z_um: np.ndarray | float,
    xs: float,
    s_um_inv: float,
    d_um: float,
    dz_um: float,
):
    """Xu et al. 2023 composition-fit functional form."""
    return (
        xs
        + s_um_inv * (d_um - z_um)
        + (1.0 - xs - s_um_inv * d_um)
        * (1.0 - erf(2.0 * z_um / dz_um) ** 3)
    )


def dx_dz_fit(
    z_um: np.ndarray | float,
    xs: float,
    s_um_inv: float,
    d_um: float,
    dz_um: float,
):
    coefficient = 1.0 - xs - s_um_inv * d_um
    u = 2.0 * z_um / dz_um
    nonlinear_derivative = (
        coefficient
        * 12.0
        / (np.sqrt(np.pi) * dz_um)
        * erf(u) ** 2
        * np.exp(-u**2)
    )
    return -s_um_inv - nonlinear_derivative


def gradient_field_v_cm(
    z_um: float | np.ndarray,
    xs: float,
    s_um_inv: float,
    d_um: float,
    dz_um: float,
    T: float = 300.0,
):
    x = x_fit(z_um, xs, s_um_inv, d_um, dz_um)
    return np.abs(
        deg_dx_hansen(x, T)
        * dx_dz_fit(z_um, xs, s_um_inv, d_um, dz_um)
        * 1.0e4
    )


def slope_from_linear_field(
    field_v_cm: float, x_ref: float, T: float = 300.0
) -> float:
    """Convert a local linear-gradient field to dx/dz in 1/um."""
    return field_v_cm / (float(deg_dx_hansen(x_ref, T)) * 1.0e4)


def sample_b_profile() -> tuple[np.ndarray, np.ndarray]:
    target_gap = (
        eg_hansen(X_B_LOW, 300.0)
        + B_FIELD_300_V_CM * W_B_UM * 1.0e-4
    )
    x_high = brentq(
        lambda xx: eg_hansen(xx, 300.0) - target_gap,
        X_B_LOW,
        0.60,
    )
    u = np.linspace(0.0, W_B_UM, N_FINE)
    x = x_high + (X_B_LOW - x_high) * u / W_B_UM
    return u, x


def sample_a_profiles() -> list[
    tuple[np.ndarray, np.ndarray, dict[str, float | str]]
]:
    profiles = []
    for linear_field in A_LINEAR_FIELDS_V_CM:
        s = slope_from_linear_field(linear_field, X_A_LOW)
        for dz_um in A_DELTA_Z_UM:
            for front_field in A_FRONT_FIELDS_V_CM:

                def root_function(z_cut_um: float) -> float:
                    d_um = W_A_UM + z_cut_um
                    return (
                        gradient_field_v_cm(
                            z_cut_um,
                            X_A_LOW,
                            s,
                            d_um,
                            dz_um,
                        )
                        - front_field
                    )

                z_scan = np.linspace(1.0e-4, 7.0, 4000)
                values = np.asarray([root_function(z) for z in z_scan])
                roots = []
                for left, right, f_left, f_right in zip(
                    z_scan[:-1],
                    z_scan[1:],
                    values[:-1],
                    values[1:],
                ):
                    if f_left * f_right < 0.0:
                        roots.append(brentq(root_function, left, right))

                # The nonlinear-field curve can cross the reported surface-field
                # scale on both rising and falling sides. Retain both rather than
                # choosing a branch from prose alone.
                for branch_index, z_cut_um in enumerate(roots):
                    d_um = W_A_UM + z_cut_um
                    u = np.linspace(0.0, W_A_UM, N_FINE)
                    x = x_fit(
                        z_cut_um + u,
                        X_A_LOW,
                        s,
                        d_um,
                        dz_um,
                    )
                    if np.any(np.diff(x) > 1.0e-8):
                        continue
                    profiles.append(
                        (
                            u,
                            x,
                            {
                                "linear_field": linear_field,
                                "delta_z": dz_um,
                                "front_field": front_field,
                                "branch": (
                                    "rising"
                                    if branch_index == 0
                                    else "falling"
                                ),
                                "z_cut": float(z_cut_um),
                                "d": float(d_um),
                                "x_front": float(x[0]),
                                "x_back": float(x[-1]),
                            },
                        )
                    )
    return profiles


def optical_kernel(
    u_um: np.ndarray,
    x_profile: np.ndarray,
    wavelength_um: float,
    T: float,
):
    u_cm = u_um * 1.0e-4
    alpha = alpha_moazzami(HC_EV_UM / wavelength_um, x_profile, T)
    tau = np.concatenate(([0.0], cumulative_trapezoid(alpha, u_cm)))
    p_abs = float(1.0 - np.exp(-tau[-1]))
    if p_abs <= 1.0e-14:
        return p_abs, np.zeros(N_CELL)

    cdf = (1.0 - np.exp(-tau)) / p_abs
    survival = 1.0 - cdf
    survival_integral = np.concatenate(
        ([0.0], cumulative_trapezoid(survival, u_um))
    )
    edges_um = np.linspace(0.0, u_um[-1], N_CELL + 1)
    row = np.diff(np.interp(edges_um, u_um, survival_integral))
    return p_abs, row


def relative_error(row: np.ndarray, reference: np.ndarray) -> float:
    return float(np.linalg.norm(row - reference) / np.linalg.norm(reference))


def joint_match(
    a_u: np.ndarray,
    a_x: np.ndarray,
    b_u: np.ndarray,
    b_x: np.ndarray,
    reference_lambda_um: float,
    T: float,
):
    p_a0, a0 = optical_kernel(a_u, a_x, reference_lambda_um, 300.0)
    p_b0, b0 = optical_kernel(b_u, b_x, reference_lambda_um, 300.0)
    if p_a0 <= 1.0e-14 or p_b0 <= 1.0e-14:
        raise RuntimeError("Reference wavelength has zero modeled absorption")

    def objective(wavelength_um: float) -> float:
        p_a, a = optical_kernel(a_u, a_x, wavelength_um, T)
        p_b, b = optical_kernel(b_u, b_x, wavelength_um, T)
        if p_a <= 1.0e-14 or p_b <= 1.0e-14:
            return 1.0e6
        e_a = relative_error(a, a0)
        e_b = relative_error(b, b0)
        return e_a**2 + e_b**2

    result = minimize_scalar(
        objective,
        bounds=SEARCH_LAMBDA_UM,
        method="bounded",
        options={"xatol": 1.0e-9},
    )
    wavelength = float(result.x)
    p_a, a = optical_kernel(a_u, a_x, wavelength, T)
    p_b, b = optical_kernel(b_u, b_x, wavelength, T)
    return (
        wavelength,
        relative_error(a, a0),
        relative_error(b, b0),
        p_a,
        p_b,
        p_a0,
        p_b0,
    )


def summarize(values: np.ndarray, column: int) -> tuple[float, float]:
    return float(np.min(values[:, column])), float(np.max(values[:, column]))


def main() -> None:
    b_u, b_x = sample_b_profile()
    a_family = sample_a_profiles()

    print("Sample-A constraint-family / joint A-B iso-kernel test")
    print(f"sample-A admissible sensitivity profiles = {len(a_family)}")
    branches = {meta["branch"] for _, _, meta in a_family}
    print(f"surface-field roots retained = {sorted(branches)}")
    x_front = np.asarray([meta["x_front"] for _, _, meta in a_family])
    z_cut = np.asarray([meta["z_cut"] for _, _, meta in a_family])
    print(f"A x_front family = {x_front.min():.3f} to {x_front.max():.3f}")
    print(f"A z_cut family = {z_cut.min():.3f} to {z_cut.max():.3f} um")
    print()

    stored = {}
    for reference_lambda in REFERENCE_LAMBDAS_UM:
        reference_pabs_a = np.asarray(
            [
                optical_kernel(u, x, reference_lambda, 300.0)[0]
                for u, x, _ in a_family
            ]
        )
        p_b0 = optical_kernel(b_u, b_x, reference_lambda, 300.0)[0]
        print(
            f"300 K common reference {reference_lambda:.3f} um: "
            f"A Pabs={reference_pabs_a.min():.3f}-{reference_pabs_a.max():.3f}, "
            f"B Pabs={p_b0:.3f}"
        )

        for T in TARGET_T_K:
            results = np.asarray(
                [
                    joint_match(
                        u,
                        x,
                        b_u,
                        b_x,
                        reference_lambda,
                        T,
                    )
                    for u, x, _ in a_family
                ]
            )
            stored[(reference_lambda, T)] = results
            lam_min, lam_max = summarize(results, 0)
            ea_min, ea_max = summarize(results, 1)
            eb_min, eb_max = summarize(results, 2)
            pa_min, pa_max = summarize(results, 3)
            pb_min, pb_max = summarize(results, 4)
            print(
                f"  {T:.0f} K joint lambda={lam_min:.6f}-{lam_max:.6f} um; "
                f"A mismatch={100*ea_min:.3f}-{100*ea_max:.3f}%; "
                f"B mismatch={100*eb_min:.3f}-{100*eb_max:.3f}%; "
                f"A Pabs={pa_min:.3f}-{pa_max:.3f}; "
                f"B Pabs={pb_min:.3f}-{pb_max:.3f}"
            )
        print()

    # Regression envelopes for the strongest provisional common reference.
    r215 = stored[(3.632, 215.0)]
    r115 = stored[(3.632, 115.0)]
    assert len(a_family) == 72
    assert 3.7933 < np.min(r215[:, 0]) < np.max(r215[:, 0]) < 3.7937
    assert np.max(r215[:, 1]) < 0.0024
    assert np.max(r215[:, 2]) < 0.0046
    assert 4.0040 < np.min(r115[:, 0]) < np.max(r115[:, 0]) < 4.0050
    assert np.max(r115[:, 1]) < 0.0045
    assert np.max(r115[:, 2]) < 0.0088
    assert np.min(r115[:, 3]) > 0.21
    assert np.min(r115[:, 4]) > 0.35

    # The deepest reference is mathematically excellent but signal-starved in A.
    deep115 = stored[(3.840, 115.0)]
    assert np.max(deep115[:, 1]) < 0.0015
    assert np.max(deep115[:, 2]) < 0.0016
    assert np.max(deep115[:, 3]) < 0.03

    print(
        "PASS: within the explicit sample-A sensitivity family and Beer-Lambert "
        "optics, the 3.632-um common reference has a stable joint temperature "
        "schedule (~3.7935 um at 215 K, ~4.0045 um at 115 K) with sub-percent "
        "kernel mismatch in both devices; the 3.840-um reference is more exactly "
        "matched but sample A is too weakly absorbed for it to be the preferred "
        "first experiment."
    )


if __name__ == "__main__":
    main()
