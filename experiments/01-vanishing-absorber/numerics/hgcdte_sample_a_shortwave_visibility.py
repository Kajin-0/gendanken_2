"""Short-wave spectral visibility of the retained nonlinear region in sample A.

The current mid/deep inverse uses wavelengths beginning near 2.8 um. Sample A's
retained nonlinear/high-field region sits close to the front collecting junction,
where the front-collection survival kernel approaches a wavelength-independent
constant and differential timing becomes gauge-like.

This script uses the published sample-A composition-fit functional form and the
72-member textual-constraint sensitivity family. The composition-gradient field
*excess above the fitted linear-region field* is used only as a spatial support
template for the nonlinear region; it is NOT assumed that transport delay is
proportional to field.

To put spectral visibility on the same phase scale as prior repository tests, an
explicitly illustrative transport perturbation is also imposed:

    v(z) = 1e5 m/s * [1 - 0.25 w(z)]

where w(z) is the normalized nonlinear-region support template. The sign/25%
size are not device claims. The purpose is to compare wavelength bands under one
fixed perturbation.

Optics use current Hansen + Moazzami Beer-Lambert kernels at 300 K. The 2.0 um
lower endpoint is at the short-wavelength edge of the spectral range used to
establish the current Moazzami fit; do not extrapolate the result below 2 um
without a validated optical model.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import cumulative_trapezoid

from hgcdte_sample_a_constraint_family_joint_iso_kernel import (
    HC_EV_UM,
    N_CELL,
    W_A_UM,
    X_A_LOW,
    alpha_moazzami,
    deg_dx_hansen,
    dx_dz_fit,
    eg_hansen,
    sample_a_profiles,
    sample_b_profile,
    slope_from_linear_field,
    x_fit,
)

F_HZ = 1.0e9
V0_M_S = 1.0e5
PERTURBATION_FRACTION = 0.25
PABS_MIN = 0.05

MIDDEEP_BAND = (2.8, 3.83)
SHORT_BANDS = (
    (2.4, 2.8),
    (2.2, 2.8),
    (2.0, 2.8),
)


def optical_kernel_and_moments(
    z_um: np.ndarray,
    x: np.ndarray,
    wavelength_um: float,
    T: float = 300.0,
) -> tuple[float, float, float, np.ndarray]:
    z_cm = z_um * 1.0e-4
    alpha = alpha_moazzami(HC_EV_UM / wavelength_um, x, T)
    tau = np.concatenate(([0.0], cumulative_trapezoid(alpha, z_cm)))
    p_abs = float(1.0 - np.exp(-tau[-1]))
    if p_abs <= 1.0e-15:
        return p_abs, np.nan, np.nan, np.zeros(N_CELL)

    density_cm = alpha * np.exp(-tau) / p_abs
    density_cm /= np.trapezoid(density_cm, z_cm)
    mean_cm = float(np.trapezoid(z_cm * density_cm, z_cm))
    var_cm2 = float(np.trapezoid((z_cm - mean_cm) ** 2 * density_cm, z_cm))

    cdf = (1.0 - np.exp(-tau)) / p_abs
    survival = 1.0 - cdf
    survival_integral = np.concatenate(
        ([0.0], cumulative_trapezoid(survival, z_um))
    )
    edges_um = np.linspace(0.0, float(z_um[-1]), N_CELL + 1)
    row = np.diff(np.interp(edges_um, z_um, survival_integral))

    return (
        p_abs,
        mean_cm * 1.0e4,
        np.sqrt(max(var_cm2, 0.0)) * 1.0e4,
        row,
    )


def nonlinear_support(
    z_um: np.ndarray,
    metadata: dict[str, float | str],
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return fine field/excess and normalized cell support template."""
    linear_field = float(metadata["linear_field"])
    delta_z = float(metadata["delta_z"])
    z_cut = float(metadata["z_cut"])
    d_um = W_A_UM + z_cut
    slope = slope_from_linear_field(linear_field, X_A_LOW)
    z_original = z_cut + z_um

    x_original = x_fit(
        z_original,
        X_A_LOW,
        slope,
        d_um,
        delta_z,
    )
    field = np.abs(
        deg_dx_hansen(x_original, 300.0)
        * dx_dz_fit(
            z_original,
            X_A_LOW,
            slope,
            d_um,
            delta_z,
        )
        * 1.0e4
    )
    excess = np.maximum(field - linear_field, 0.0)

    centers_um = (np.arange(N_CELL) + 0.5) * W_A_UM / N_CELL
    cell_support = np.interp(centers_um, z_um, excess)
    if np.max(cell_support) <= 0.0:
        raise RuntimeError("Sample-A profile has no nonlinear-field excess")
    cell_support /= np.max(cell_support)
    return field, excess, cell_support


def support_depth_metrics(
    z_um: np.ndarray,
    excess: np.ndarray,
) -> tuple[float, float]:
    area = float(np.trapezoid(excess, z_um))
    centroid = float(np.trapezoid(z_um * excess, z_um) / area)
    cumulative = np.concatenate(([0.0], cumulative_trapezoid(excess, z_um)))
    cumulative /= cumulative[-1]
    z90 = float(np.interp(0.90, cumulative, z_um))
    return centroid, z90


def phase_signal_for_band(
    z_um: np.ndarray,
    x: np.ndarray,
    support: np.ndarray,
    lambda_min_um: float,
    lambda_max_um: float,
) -> tuple[float, float]:
    wavelengths = np.arange(lambda_min_um, lambda_max_um + 1.0e-12, 0.01)

    velocity = V0_M_S * (1.0 - PERTURBATION_FRACTION * support)
    q = 1.0e6 / velocity  # ps/um
    q0 = np.full_like(q, 1.0e6 / V0_M_S)
    delta_q = q - q0

    phase = []
    for wavelength in wavelengths:
        p_abs, _, _, row = optical_kernel_and_moments(z_um, x, wavelength)
        if p_abs < PABS_MIN:
            continue
        # 1 ps gives 360 f 1e-12 degrees.
        phase.append(-360.0 * F_HZ * 1.0e-12 * float(row @ delta_q))

    phase = np.asarray(phase)
    phase -= np.mean(phase)
    return float(np.sqrt(np.mean(phase**2))), float(np.ptp(phase))


def current_band_visibility(
    z_um: np.ndarray,
    x: np.ndarray,
    excess: np.ndarray,
) -> float:
    wavelengths = np.arange(MIDDEEP_BAND[0], MIDDEEP_BAND[1] + 1.0e-12, 0.01)
    rows = []
    for wavelength in wavelengths:
        p_abs, _, _, row = optical_kernel_and_moments(z_um, x, wavelength)
        if p_abs >= PABS_MIN:
            rows.append(row)
    A = np.asarray(rows)
    A_delta = A - np.mean(A, axis=0, keepdims=True)
    column_visibility = np.linalg.norm(A_delta, axis=0)
    column_visibility /= np.max(column_visibility)

    centers_um = (np.arange(N_CELL) + 0.5) * W_A_UM / N_CELL
    weights = np.interp(centers_um, z_um, excess)
    weights /= np.sum(weights)
    return float(weights @ column_visibility)


def band_edge_x(wavelength_um: float) -> float:
    energy = HC_EV_UM / wavelength_um
    grid = np.linspace(0.2, 0.9, 5000)
    values = np.abs(eg_hansen(grid, 300.0) - energy)
    return float(grid[np.argmin(values)])


def main() -> None:
    profiles = sample_a_profiles()
    b_z, b_x = sample_b_profile()

    support_centroids = []
    support_z90 = []
    mid_visibility = []
    phase_by_band = {MIDDEEP_BAND: []}
    for band in SHORT_BANDS:
        phase_by_band[band] = []

    a_means_20 = []
    a_means_28 = []
    a_pabs_20 = []
    a_pabs_28 = []

    for z_um, x, metadata in profiles:
        _, excess, support = nonlinear_support(z_um, metadata)
        centroid, z90 = support_depth_metrics(z_um, excess)
        support_centroids.append(centroid)
        support_z90.append(z90)
        mid_visibility.append(current_band_visibility(z_um, x, excess))

        for band in phase_by_band:
            phase_by_band[band].append(
                phase_signal_for_band(z_um, x, support, band[0], band[1])
            )

        p20, m20, _, _ = optical_kernel_and_moments(z_um, x, 2.0)
        p28, m28, _, _ = optical_kernel_and_moments(z_um, x, 2.8)
        a_pabs_20.append(p20)
        a_pabs_28.append(p28)
        a_means_20.append(m20)
        a_means_28.append(m28)

    p_b20, m_b20, _, _ = optical_kernel_and_moments(b_z, b_x, 2.0)
    p_b28, m_b28, _, _ = optical_kernel_and_moments(b_z, b_x, 2.8)

    support_centroids = np.asarray(support_centroids)
    support_z90 = np.asarray(support_z90)
    mid_visibility = np.asarray(mid_visibility)

    print("Sample-A nonlinear-region short-wave visibility")
    print(
        f"nonlinear-support centroid = {support_centroids.min():.3f}-"
        f"{support_centroids.max():.3f} um, median={np.median(support_centroids):.3f} um"
    )
    print(
        f"90% support depth = {support_z90.min():.3f}-"
        f"{support_z90.max():.3f} um, median={np.median(support_z90):.3f} um"
    )
    print(
        "field-support-weighted normalized visibility in 2.8-3.83 um band = "
        f"{mid_visibility.min():.5f}-{mid_visibility.max():.5f}, "
        f"median={np.median(mid_visibility):.5f}"
    )
    print()

    for band, values in phase_by_band.items():
        values = np.asarray(values)
        rms = values[:, 0]
        p2p = values[:, 1]
        print(
            f"band {band[0]:.1f}-{band[1]:.2f} um: "
            f"illustrative phase RMS={rms.min():.4f}-{rms.max():.4f} deg, "
            f"median={np.median(rms):.4f}; "
            f"p-p={p2p.min():.4f}-{p2p.max():.4f} deg, "
            f"median={np.median(p2p):.4f}"
        )
    print()

    a_means_20 = np.asarray(a_means_20)
    a_means_28 = np.asarray(a_means_28)
    a_pabs_20 = np.asarray(a_pabs_20)
    a_pabs_28 = np.asarray(a_pabs_28)

    print("2.0 -> 2.8 um generation-depth contrast")
    print(
        f"sample A mean depth @2.0 = {a_means_20.min():.3f}-"
        f"{a_means_20.max():.3f} um, median={np.median(a_means_20):.3f}"
    )
    print(
        f"sample A mean depth @2.8 = {a_means_28.min():.3f}-"
        f"{a_means_28.max():.3f} um, median={np.median(a_means_28):.3f}"
    )
    print(
        f"sample A median depth shift = "
        f"{np.median(a_means_28)-np.median(a_means_20):.3f} um"
    )
    print(
        f"sample B mean depth = {m_b20:.3f} -> {m_b28:.3f} um "
        f"(shift {m_b28-m_b20:.3f} um)"
    )
    print(
        f"sample A Pabs @2.0 = {a_pabs_20.min():.6f}-"
        f"{a_pabs_20.max():.6f}; @2.8 = {a_pabs_28.min():.6f}-"
        f"{a_pabs_28.max():.6f}"
    )
    print(
        f"sample B Pabs @2.0={p_b20:.6f}, @2.8={p_b28:.6f}"
    )
    print()

    print("300 K local band-edge composition coordinates")
    for wavelength in (2.8, 2.6, 2.4, 2.2, 2.0):
        print(f"  {wavelength:.1f} um -> x_edge~{band_edge_x(wavelength):.4f}")

    # Stable regressions from current 72-profile family.
    assert 0.46 > support_centroids.min() > 0.45
    assert 1.42 < support_centroids.max() < 1.44
    assert 0.0024 < mid_visibility.min() < 0.0027
    assert 0.042 < mid_visibility.max() < 0.044

    mid = np.asarray(phase_by_band[MIDDEEP_BAND])[:, 1]
    short20 = np.asarray(phase_by_band[(2.0, 2.8)])[:, 1]
    short22 = np.asarray(phase_by_band[(2.2, 2.8)])[:, 1]

    assert 0.0022 < mid.min() < 0.0025
    assert 0.046 < mid.max() < 0.048
    assert 0.016 < np.median(mid) < 0.018

    assert 0.108 < short20.min() < 0.109
    assert 0.370 < short20.max() < 0.372
    assert 0.210 < np.median(short20) < 0.212

    assert 0.063 < short22.min() < 0.065
    assert 0.292 < short22.max() < 0.295

    assert 1.49 < np.median(a_means_20) < 1.51
    assert 3.32 < np.median(a_means_28) < 3.34
    assert 0.29 < (m_b28 - m_b20) < 0.31
    assert p_b20 > 0.9999 and p_b28 > 0.997
    assert np.min(a_pabs_20) > 0.99999
    assert np.min(a_pabs_28) > 0.997

    print()
    print(
        "PASS: the current mid/deep band is intrinsically weak for a transport "
        "perturbation tied to sample A's near-junction nonlinear region, while "
        "a dedicated 2.0-2.8 um scan moves generation through that region, "
        "keeps both devices strongly absorbing, and increases the illustrative "
        "1-GHz differential phase scale by more than an order of magnitude."
    )


if __name__ == "__main__":
    main()
