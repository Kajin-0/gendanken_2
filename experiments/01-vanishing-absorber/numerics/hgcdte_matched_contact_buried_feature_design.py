"""Matched-contact validation design: where should a buried transport feature sit?

The published sample-A nonlinear region lies near the collecting junction, where
the spectral timing inverse is gauge-like and contact/interface transport can
mimic the target almost perfectly. This script asks a constructive design
question for a purpose-built matched-contact thought device:

    Where should a localized buried transport perturbation be placed so its
    wavelength x RF complex fingerprint is maximally distinguishable from
    contact and smooth-bulk nuisance mechanisms?

Reference control profile
-------------------------
- total HgCdTe thickness L = 7.6 um;
- monotonic linear composition x=0.40 at collecting/front side -> x=0.32 back;
- this gives a ~140 V/cm composition-gradient field near x~0.36 at 300 K,
  comparable to the weak linear-gradient scale in the published control sample;
- same front composition/contact stack is assumed for control and contrast.

Candidate buried transport support
----------------------------------
Gaussian support exp[-(z-z0)^2/(2 sigma_z^2)] with centers 0.25-7.0 um and
widths 0.2, 0.35, 0.5, 0.75, 1.0 um. The support is a transport-design
coordinate only; this script does not yet construct a realizable composition
profile that produces it.

Nuisance span
-------------
- uniform, linear, quadratic smooth differential bulk transport;
- near-junction exponentials with effective scales 0.2, 0.5, 0.75, 1.0 um.

Measurement space
-----------------
- lambda = 2.80-3.83 um, retaining Pabs>=0.05;
- f = 0.25, 0.5, 1, 2, 3 GHz;
- phase + log-magnitude finite-RF Jacobian;
- wavelength-independent complex response removed separately at each f.

Three noise-weighting diagnostics are used:
- equal response noise;
- statistics-like sigma ~ Pabs^-1/2 -> whitening ~ sqrt(Pabs);
- additive-like sigma ~ Pabs^-1 -> whitening ~ Pabs.

The objective is the whitened target norm remaining after orthogonal projection
onto the physical nuisance span. It is proportional to Fisher SNR for a fixed
peak spatial perturbation and equal normalized covariance under each weighting.

No fabrication claim, calibrated transport, or novelty claim.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import cumulative_trapezoid

from hgcdte_sample_a_constraint_family_joint_iso_kernel import (
    HC_EV_UM,
    N_CELL,
    alpha_moazzami,
    deg_dx_hansen,
)
from hgcdte_shortwave_finite_rf_jacobian import (
    finite_rf_jacobian,
    response_matrix,
    target_vector,
)

L_UM = 7.6
X_FRONT = 0.40
X_BACK = 0.32
N_FINE = 4001
FREQUENCIES_GHZ = (0.25, 0.50, 1.0, 2.0, 3.0)
LAMBDA_CANDIDATE = np.arange(2.80, 3.9001, 0.01)
PABS_MIN = 0.05

FEATURE_CENTERS_UM = np.arange(0.25, 7.0001, 0.25)
FEATURE_WIDTHS_UM = (0.20, 0.35, 0.50, 0.75, 1.00)
CONTACT_SCALES_UM = (0.20, 0.50, 0.75, 1.00)

NOISE_EXPONENTS = {
    "equal": 0.0,
    "statistics": 0.5,
    "additive": 1.0,
}


def reference_profile() -> tuple[np.ndarray, np.ndarray]:
    z = np.linspace(0.0, L_UM, N_FINE)
    x = X_FRONT + (X_BACK - X_FRONT) * z / L_UM
    return z, x


def p_absorption(z_um: np.ndarray, x: np.ndarray, wavelength_um: float) -> float:
    alpha = alpha_moazzami(HC_EV_UM / wavelength_um, x, 300.0)
    tau = np.concatenate(
        ([0.0], cumulative_trapezoid(alpha, z_um * 1.0e-4))
    )
    return float(1.0 - np.exp(-tau[-1]))


def retained_wavelengths(z_um: np.ndarray, x: np.ndarray):
    pabs = np.asarray(
        [p_absorption(z_um, x, wavelength) for wavelength in LAMBDA_CANDIDATE]
    )
    keep = pabs >= PABS_MIN
    return LAMBDA_CANDIDATE[keep], pabs[keep]


def cell_centers() -> np.ndarray:
    edges = np.linspace(0.0, L_UM, N_CELL + 1)
    return 0.5 * (edges[:-1] + edges[1:])


def complex_response(jacobian: np.ndarray, spatial: np.ndarray) -> np.ndarray:
    response = np.einsum("flj,j->fl", jacobian, spatial)
    return target_vector(response, "complex")


def complex_response_matrix(
    jacobian: np.ndarray,
    spatial_matrix: np.ndarray,
) -> np.ndarray:
    response = np.einsum("flj,jk->flk", jacobian, spatial_matrix)
    return response_matrix(response, "complex")


def whitening_vector(pabs: np.ndarray, exponent: float) -> np.ndarray:
    per_frequency = np.tile(pabs**exponent, len(FREQUENCIES_GHZ))
    return np.concatenate((per_frequency, per_frequency))


def projected_metrics(
    target: np.ndarray,
    nuisance: np.ndarray,
) -> tuple[float, float, float]:
    u, singular, _ = np.linalg.svd(nuisance, full_matrices=False)
    rank = int(np.sum(singular > singular[0] * 1.0e-11))
    basis = u[:, :rank]
    residual = target - basis @ (basis.T @ target)

    target_norm = float(np.linalg.norm(target))
    residual_norm = float(np.linalg.norm(residual))
    fraction = residual_norm / target_norm
    angle = float(np.degrees(np.arcsin(np.clip(fraction, 0.0, 1.0))))
    return angle, residual_norm, target_norm


def main() -> None:
    z_um, x = reference_profile()
    wavelengths, pabs = retained_wavelengths(z_um, x)
    jacobian, transfer = finite_rf_jacobian(
        z_um,
        x,
        FREQUENCIES_GHZ,
        wavelengths=wavelengths,
    )

    centers = cell_centers()
    smooth = np.column_stack(
        (
            np.ones(N_CELL),
            centers / L_UM,
            (centers / L_UM) ** 2,
        )
    )
    contacts = np.column_stack(
        [np.exp(-centers / scale) for scale in CONTACT_SCALES_UM]
    )
    nuisance_spatial = np.column_stack((smooth, contacts))
    nuisance_raw = complex_response_matrix(jacobian, nuisance_spatial)

    baseline_slope_per_um = abs((X_BACK - X_FRONT) / L_UM)
    baseline_field_v_cm = float(
        deg_dx_hansen(0.36, 300.0) * baseline_slope_per_um * 1.0e4
    )

    print("Matched-contact buried-feature validation design")
    print(
        f"reference x(z): {X_FRONT:.3f} -> {X_BACK:.3f} over {L_UM:.1f} um"
    )
    print(
        f"baseline composition-gradient field near x=0.36: "
        f"~{baseline_field_v_cm:.1f} V/cm"
    )
    print(
        f"retained lambda = {wavelengths[0]:.2f}-{wavelengths[-1]:.2f} um "
        f"({len(wavelengths)} points), Pabs(last)={pabs[-1]:.4f}"
    )
    print(
        f"minimum optical-only |H| through 3 GHz = {np.min(np.abs(transfer)):.6f}"
    )
    print()

    stored = {}
    for label, exponent in NOISE_EXPONENTS.items():
        whitening = whitening_vector(pabs, exponent)
        nuisance = nuisance_raw * whitening[:, None]
        records = []

        for width in FEATURE_WIDTHS_UM:
            for center in FEATURE_CENTERS_UM:
                feature = np.exp(-0.5 * ((centers - center) / width) ** 2)
                target = complex_response(jacobian, feature) * whitening
                angle, residual_norm, target_norm = projected_metrics(
                    target, nuisance
                )
                records.append(
                    (width, center, angle, residual_norm, target_norm)
                )

        stored[label] = records
        best = max(records, key=lambda row: row[3])
        print(
            f"{label}: best residual-information support -> "
            f"sigma={best[0]:.2f} um, center={best[1]:.2f} um, "
            f"angle={best[2]:.4f} deg, residual_norm={best[3]:.9f}"
        )

        # Compare the physically robust width=0.5 um around the near-junction
        # region and buried optimum.
        width05 = [row for row in records if row[0] == 0.50]
        near = min(width05, key=lambda row: abs(row[1] - 0.75))
        buried = max(width05, key=lambda row: row[3])
        ratio = buried[3] / near[3]
        print(
            f"  width=0.50 um: near-junction center={near[1]:.2f} um "
            f"residual={near[3]:.9f}; buried center={buried[1]:.2f} um "
            f"residual={buried[3]:.9f}; amplitude ratio={ratio:.2f}x; "
            f"information ratio={ratio**2:.1f}x"
        )
        print()

    # Local composition / gap coordinate at the realistic-noise optima.
    for center in (4.75, 5.00):
        local_x = X_FRONT + (X_BACK - X_FRONT) * center / L_UM
        # Hansen Eg inline through imported derivative module is not necessary
        # for the regression; report x for interpretation.
        print(
            f"center {center:.2f} um -> local composition x~{local_x:.6f}"
        )

    stats = stored["statistics"]
    additive = stored["additive"]

    stats_best = max(stats, key=lambda row: row[3])
    add_best = max(additive, key=lambda row: row[3])

    assert stats_best[0] == 0.50
    assert stats_best[1] == 5.00
    assert 1.18 < stats_best[2] < 1.19
    assert 0.00219 < stats_best[3] < 0.00220

    assert add_best[0] == 0.50
    assert add_best[1] == 4.75
    assert 0.99 < add_best[2] < 1.00
    assert 0.00175 < add_best[3] < 0.00177

    stats_width05 = [row for row in stats if row[0] == 0.50]
    stats_near = min(stats_width05, key=lambda row: abs(row[1] - 0.75))
    stats_buried = max(stats_width05, key=lambda row: row[3])
    stats_ratio = stats_buried[3] / stats_near[3]
    assert 22.9 < stats_ratio < 23.1

    add_width05 = [row for row in additive if row[0] == 0.50]
    add_near = min(add_width05, key=lambda row: abs(row[1] - 0.75))
    add_buried = max(add_width05, key=lambda row: row[3])
    add_ratio = add_buried[3] / add_near[3]
    assert 19.7 < add_ratio < 20.0

    print()
    print(
        "PASS: once contact and smooth-bulk nuisances are treated as mechanism "
        "competitors, a purpose-built buried feature around 4.75-5.0 um depth "
        "and ~0.5 um width is far more identifiable than the published-like "
        "near-junction geometry. Under statistics-like and additive-like signal "
        "weighting the recoverable response amplitude improves by ~23x and ~20x, "
        "respectively, corresponding to roughly 500x and 400x information. "
        "This is a validation-structure design result, not yet a realizable "
        "composition-profile prescription."
    )


if __name__ == "__main__":
    main()
