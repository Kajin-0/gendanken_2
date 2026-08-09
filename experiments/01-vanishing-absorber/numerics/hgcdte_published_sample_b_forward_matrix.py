"""Dimensional forward matrix for the 2023 graded-HgCdTe sample B.

This is a literature-instantiated optical/timing-kernel calculation, not a
calibrated reconstruction of the published device's carrier velocity.

Primary inputs:
- Xu et al. (2023): processed sample-B thickness ~3.7 um, nominal x~0.316,
  nonlinear interdiffusion region removed, linear-gradient built-in field
  ~100-200 V/cm.
- Hansen, Schmit & Casselman (1982): HgCdTe Eg(x,T), with +0.832*x^3.
- Moazzami et al. (2005): above-bandgap absorption coefficient alpha(E,x,T).

Coordinate:
z=0 is the high-Cd / junction-side entrance of the retained linear-gradient
region; z=W is the low-Cd side near the sapphire-supported growth surface.
For a front-side junction, mean carrier delay from a generation point z is
modeled as integral_0^z q(s) ds. Therefore the timing kernel is the generation
SURVIVAL function P(Z_g >= s), not the CDF used for collection at z=W.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.optimize import brentq

HC_EV_UM = 1.2398419843320026
T_K = 300.0
W_UM = 3.7
W_CM = W_UM * 1.0e-4
X_LOW = 0.316

FIELD_VALUES = (100.0, 150.0, 200.0)  # V/cm literature bracket
N_FINE = 4001
N_CELL = 80
LAMBDA_GRID = np.arange(2.80, 3.951, 0.01)
PABS_MIN = 0.05

F_PHASE_HZ = 1.0e9
V_SCALE_M_S = 1.0e5
TABLE_LAMBDAS = (2.80, 3.20, 3.37, 3.50, 3.70, 3.85, 3.88)


def eg_hansen(x: np.ndarray | float, T: float = T_K) -> np.ndarray | float:
    """HgCdTe band gap in eV, Hansen-Schmit-Casselman (1982)."""
    return (
        -0.302
        + 1.93 * x
        + 5.35e-4 * T * (1.0 - 2.0 * x)
        - 0.81 * x**2
        + 0.832 * x**3
    )


def deg_dx_hansen(x: np.ndarray | float, T: float = T_K) -> np.ndarray | float:
    return 1.93 - 2.0 * 0.81 * x + 3.0 * 0.832 * x**2 - 2.0 * 5.35e-4 * T


def k_moazzami(x: np.ndarray | float, T: float = T_K) -> np.ndarray | float:
    return (
        -20060.0
        + 115750.0 * x
        + 32.43 * T
        - 64170.0 * x**2
        + 0.43231 * T**2
        - 101.92 * x * T
    )


def n_moazzami(x: np.ndarray | float, T: float = T_K) -> np.ndarray | float:
    return 0.74487 - 0.44513 * x + (0.000799 - 0.000757 * x) * T


def alpha_moazzami(
    photon_energy_ev: float, x: np.ndarray, T: float = T_K
) -> np.ndarray:
    """Above-gap alpha in cm^-1; sub-gap/Urbach absorption omitted."""
    eg = eg_hansen(x, T)
    excess_fraction = (photon_energy_ev - eg) / photon_energy_ev
    alpha = np.zeros_like(x, dtype=float)
    mask = excess_fraction > 0.0
    alpha[mask] = k_moazzami(x[mask], T) * excess_fraction[mask] ** n_moazzami(
        x[mask], T
    )
    return alpha


def infer_x_high(field_v_cm: float) -> float:
    """Infer high-Cd endpoint from Delta Eg = F W and nominal low-Cd x."""
    eg_low = float(eg_hansen(X_LOW))
    target = eg_low + field_v_cm * W_CM
    return float(brentq(lambda xx: eg_hansen(xx) - target, X_LOW, 0.60))


def linear_x_profile(field_v_cm: float) -> tuple[np.ndarray, np.ndarray]:
    """Linear x(z), high Cd at z=0 and nominal low Cd at z=W."""
    z_um = np.linspace(0.0, W_UM, N_FINE)
    x_high = infer_x_high(field_v_cm)
    x = x_high + (X_LOW - x_high) * z_um / W_UM
    return z_um, x


def optical_distribution(
    wavelength_um: float, field_v_cm: float
) -> tuple[float, float, float, np.ndarray]:
    """Return Pabs, conditional mean/std depth [um], and exact timing row."""
    z_um, x = linear_x_profile(field_v_cm)
    z_cm = z_um * 1.0e-4
    photon_energy = HC_EV_UM / wavelength_um
    alpha = alpha_moazzami(photon_energy, x)

    tau = np.concatenate(([0.0], cumulative_trapezoid(alpha, z_cm)))
    cdf_unconditional = 1.0 - np.exp(-tau)
    p_abs = float(cdf_unconditional[-1])

    if p_abs <= 1.0e-15:
        return p_abs, np.nan, np.nan, np.zeros(N_CELL)

    cdf = cdf_unconditional / p_abs
    survival = 1.0 - cdf

    # Conditional generation density for accurate moments.
    p_density_cm = alpha * np.exp(-tau) / p_abs
    mean_cm = float(np.trapezoid(z_cm * p_density_cm, z_cm))
    variance_cm2 = float(
        np.trapezoid((z_cm - mean_cm) ** 2 * p_density_cm, z_cm)
    )
    mean_um = mean_cm * 1.0e4
    std_um = np.sqrt(max(variance_cm2, 0.0)) * 1.0e4

    # Exact piecewise-constant-q discretization:
    # A_ij = integral_cell P(Z_g >= s | lambda_i, abs) ds.
    edges_um = np.linspace(0.0, W_UM, N_CELL + 1)
    survival_integral = np.concatenate(
        ([0.0], cumulative_trapezoid(survival, z_um))
    )
    integral_at_edges = np.interp(edges_um, z_um, survival_integral)
    timing_row_um = np.diff(integral_at_edges)

    return p_abs, mean_um, std_um, timing_row_um


def field_from_linear_x(field_target: float) -> tuple[float, float]:
    _, x = linear_x_profile(field_target)
    dxdz_cm = (X_LOW - x[0]) / W_CM
    field = -deg_dx_hansen(x) * dxdz_cm
    return float(np.min(field)), float(np.max(field))


def main() -> None:
    eg_low = float(eg_hansen(X_LOW))
    print("Published sample-B dimensional forward matrix")
    print(f"T = {T_K:.0f} K, W = {W_UM:.2f} um, nominal x_low = {X_LOW:.3f}")
    print(
        f"Eg_low = {eg_low:.6f} eV, lambda_low = {HC_EV_UM / eg_low:.4f} um"
    )
    print()

    mode_counts = {}
    for field in FIELD_VALUES:
        x_high = infer_x_high(field)
        eg_high = float(eg_hansen(x_high))
        lambda_high = HC_EV_UM / eg_high
        fmin, fmax = field_from_linear_x(field)

        rows = []
        p_abs_values = []
        means = []
        for wavelength in LAMBDA_GRID:
            p_abs, mean_um, _, timing_row = optical_distribution(wavelength, field)
            rows.append(timing_row)
            p_abs_values.append(p_abs)
            means.append(mean_um)

        rows = np.asarray(rows)
        p_abs_values = np.asarray(p_abs_values)
        means = np.asarray(means)
        keep = p_abs_values >= PABS_MIN
        A = rows[keep]

        singular = np.linalg.svd(A, compute_uv=False)
        relative = singular / singular[0]
        counts = tuple(
            int(np.sum(relative > threshold))
            for threshold in (1e-1, 1e-2, 1e-3, 1e-4)
        )
        mode_counts[field] = counts

        kept_lambdas = LAMBDA_GRID[keep]
        print(f"field target = {field:.0f} V/cm")
        print(f"  x_high = {x_high:.6f}")
        print(f"  Eg_high = {eg_high:.6f} eV")
        print(f"  local-gap interval = {lambda_high:.4f} to {HC_EV_UM / eg_low:.4f} um")
        print(f"  realized field range from linear-x profile = {fmin:.3f} to {fmax:.3f} V/cm")
        print(
            f"  >=5% absorption wavelength range = "
            f"{kept_lambdas[0]:.2f} to {kept_lambdas[-1]:.2f} um"
        )
        print(
            "  modes above relative singular thresholds "
            f"[1e-1,1e-2,1e-3,1e-4] = {counts}"
        )
        print()

        assert x_high > X_LOW
        assert abs(np.mean((fmin, fmax)) - field) / field < 0.01
        finite = np.isfinite(means)
        assert np.all(np.diff(p_abs_values) <= 2.0e-8)
        assert np.all(np.diff(means[finite]) >= -2.0e-3)

    # Stable deterministic conditioning regression for the central profile.
    assert mode_counts[150.0] == (2, 5, 10, 21)

    print("Central 150 V/cm profile: generation-depth / phase scale")
    ref_mean = None
    omega = 2.0 * np.pi * F_PHASE_HZ
    for wavelength in TABLE_LAMBDAS:
        p_abs, mean_um, std_um, _ = optical_distribution(wavelength, 150.0)
        if ref_mean is None:
            ref_mean = mean_um
        delta_z_m = (mean_um - ref_mean) * 1.0e-6
        delta_t_s = delta_z_m / V_SCALE_M_S
        delta_phi_deg = -omega * delta_t_s * 180.0 / np.pi
        print(
            f"  {wavelength:4.2f} um: "
            f"Pabs={p_abs:6.3f}, "
            f"<z>={mean_um:5.3f} um, "
            f"sigma_z={std_um:5.3f} um, "
            f"DeltaT={delta_t_s*1e12:6.2f} ps, "
            f"DeltaPhi@1GHz={delta_phi_deg:7.3f} deg"
        )

    p0, z0, _, _ = optical_distribution(TABLE_LAMBDAS[0], 150.0)
    p1, z1, _, _ = optical_distribution(TABLE_LAMBDAS[-1], 150.0)
    phase_span_deg = (
        omega * ((z1 - z0) * 1.0e-6 / V_SCALE_M_S) * 180.0 / np.pi
    )
    assert p0 > 0.99
    assert p1 > PABS_MIN
    assert 9.0 < phase_span_deg < 12.0

    print()
    print(
        f"PASS: central-profile 2.80 -> 3.88 um mean-depth shift "
        f"= {z1-z0:.3f} um, illustrative 1-GHz phase span "
        f"= {phase_span_deg:.3f} deg at v={V_SCALE_M_S:.1e} m/s"
    )


if __name__ == "__main__":
    main()
