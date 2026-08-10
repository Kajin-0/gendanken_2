"""Joint depth / spectral design for an interface-safe programmed gradient pair.

This supersedes the earlier restricted 0.8-3.2 um feature-position search.
That grid inherited the near-junction sample-A focus and artificially prevented
purpose-built features from moving deeper into the absorber.

The design question is now:

    For a compact 1-um programmed composition-gradient segment, where should
    two matched copies be placed and what contiguous wavelength band should be
    used to maximize nuisance-orthogonal wavelength x RF information at fixed
    total averaging resource?

Important additions
-------------------
- front AND back interface nuisance shapes are included;
- the entire 1-um feature is required to remain a chosen clearance from both
  interfaces;
- phase/log-magnitude precision is allowed to degrade with absorbed signal;
- fixed total wavelength-time resource is enforced, so adding wavelengths is
  not free;
- wavelength-independent complex offsets are represented explicitly at every RF
  instead of removed by unweighted mean subtraction.

Noise envelopes
---------------
For an individual channel, sigma is taken proportional to Pabs**(-beta):

    beta = 0.5  statistics-like
    beta = 1.0  additive-like phase limit.

For two independent matched-device channels, differential variance is
proportional to P1**(-2 beta) + P2**(-2 beta).

For a candidate containing N_lambda equally timed wavelengths, the design score
is

    score = ||r_white|| / sqrt(N_lambda),

where r_white is the target residual after whitening and projection of common
bulk/interface nuisances plus one arbitrary phase and one arbitrary log-magnitude
intercept per RF frequency. This score is proportional to fixed-total-time SNR.

The 25% feature-supported transport perturbation is still illustrative and is
NOT a device prediction.

No novelty claim.
"""

from __future__ import annotations

import numpy as np

from hgcdte_matched_contact_translated_gradient_design import (
    FREQUENCIES_GHZ,
    L_UM,
    REFERENCE_NOISE_DEG,
    cell_centers,
)
from hgcdte_programmed_translated_gradient_design import (
    FEATURE_TOTAL_WIDTH_UM,
    programmed_profile,
    transport_delta_q,
)
from hgcdte_shortwave_finite_rf_jacobian import (
    finite_rf_jacobian,
    generation_probabilities,
    project_residual,
)

WAVELENGTH_GRID_UM = np.arange(2.00, 3.8501, 0.025)
POSITION_STEP_UM = 0.10
UPPER_SCAN_UM = np.arange(2.20, 2.8001, 0.025)
CLEARANCES_UM = (0.5, 1.0, 1.5, 2.0)
BETA_VALUES = (0.5, 1.0)


def spatial_nuisance_matrix() -> np.ndarray:
    z = cell_centers()
    u = z / L_UM
    columns = [np.ones_like(z), u, u**2, u**3]
    for ell in (0.30, 0.50, 0.75, 1.00):
        columns.append(np.exp(-z / ell))
    for ell in (0.30, 0.50, 0.75, 1.00):
        columns.append(np.exp(-(L_UM - z) / ell))
    return np.column_stack(columns)


NUISANCE_SPATIAL = spatial_nuisance_matrix()


def finite_rf_grid(z_um: np.ndarray, x: np.ndarray):
    """Finite-RF Jacobian, baseline H, and Pabs on the full wavelength grid."""
    J, H = finite_rf_jacobian(
        z_um,
        x,
        FREQUENCIES_GHZ,
        wavelengths=WAVELENGTH_GRID_UM,
    )
    pabs = np.asarray(
        [
            generation_probabilities(z_um, x, float(wavelength))[3]
            if len(generation_probabilities(z_um, x, float(wavelength))) == 4
            else np.nan
            for wavelength in WAVELENGTH_GRID_UM
        ]
    )
    # The current shared generation_probabilities helper returns three values,
    # so calculate Pabs explicitly from its source optical model only if needed.
    if np.any(~np.isfinite(pabs)):
        from scipy.integrate import cumulative_trapezoid
        from hgcdte_sample_a_constraint_family_joint_iso_kernel import (
            HC_EV_UM,
            alpha_moazzami,
        )

        pabs = []
        z_cm = z_um * 1.0e-4
        for wavelength in WAVELENGTH_GRID_UM:
            alpha = alpha_moazzami(HC_EV_UM / float(wavelength), x, 300.0)
            tau = np.concatenate(([0.0], cumulative_trapezoid(alpha, z_cm)))
            pabs.append(float(1.0 - np.exp(-tau[-1])))
        pabs = np.asarray(pabs)
    return J, H, pabs


def raw_vector(response: np.ndarray) -> np.ndarray:
    return np.concatenate((response.imag.reshape(-1), response.real.reshape(-1)))


def raw_matrix(response: np.ndarray) -> np.ndarray:
    return np.concatenate(
        (
            response.imag.reshape(-1, response.shape[-1]),
            response.real.reshape(-1, response.shape[-1]),
        ),
        axis=0,
    )


def complex_intercepts(n_lambda: int) -> np.ndarray:
    """One arbitrary phase and log-magnitude offset per RF frequency."""
    n_f = len(FREQUENCIES_GHZ)
    n = n_f * n_lambda
    matrix = np.zeros((2 * n, 2 * n_f))
    for fi in range(n_f):
        rows = np.arange(fi * n_lambda, (fi + 1) * n_lambda)
        matrix[rows, fi] = 1.0
        matrix[n + rows, n_f + fi] = 1.0
    return matrix


def build_cache(positions: np.ndarray):
    cache = {}
    for center in positions:
        z, x, support, _ = programmed_profile(float(center))
        J, H, pabs = finite_rf_grid(z, x)
        cache[float(center)] = {
            "J": J,
            "H": H,
            "Pabs": pabs,
            "dq": transport_delta_q(z, support),
        }
    return cache


def score_candidate(
    left: dict,
    right: dict,
    indices: np.ndarray,
    beta: float,
):
    J1 = left["J"][:, indices, :]
    J2 = right["J"][:, indices, :]
    dq1 = left["dq"]
    dq2 = right["dq"]

    target = (
        np.einsum("flj,j->fl", J2, dq2)
        - np.einsum("flj,j->fl", J1, dq1)
    )
    common = np.einsum("flj,jk->flk", J2 - J1, NUISANCE_SPATIAL)

    data = raw_vector(target)
    nuisance = np.column_stack(
        (raw_matrix(common), complex_intercepts(len(indices)))
    )

    p1 = left["Pabs"][indices]
    p2 = right["Pabs"][indices]
    relative_sigma = np.sqrt(p1 ** (-2.0 * beta) + p2 ** (-2.0 * beta))
    sigma_rows = np.tile(relative_sigma, len(FREQUENCIES_GHZ))
    sigma_rows = np.concatenate((sigma_rows, sigma_rows))

    angle_deg, residual_norm = project_residual(
        data / sigma_rows,
        nuisance / sigma_rows[:, None],
    )
    score = residual_norm / np.sqrt(len(indices))
    return {
        "score": float(score),
        "angle_deg": float(angle_deg),
        "residual": float(residual_norm),
        "pabs_min": float(min(np.min(p1), np.min(p2))),
    }


def positions_for_clearance(clearance_um: float) -> np.ndarray:
    half = 0.5 * FEATURE_TOTAL_WIDTH_UM
    minimum = clearance_um + half
    maximum = L_UM - clearance_um - half
    start = np.ceil(minimum / POSITION_STEP_UM) * POSITION_STEP_UM
    stop = np.floor(maximum / POSITION_STEP_UM) * POSITION_STEP_UM
    return np.round(np.arange(start, stop + 0.5 * POSITION_STEP_UM, POSITION_STEP_UM), 10)


def optimize_clearance(clearance_um: float, beta: float):
    positions = positions_for_clearance(clearance_um)
    cache = build_cache(positions)
    best = None

    upper_indices = [
        int(np.argmin(np.abs(WAVELENGTH_GRID_UM - upper))) + 1
        for upper in UPPER_SCAN_UM
    ]
    for i, z1 in enumerate(positions):
        for z2 in positions[i + 1 :]:
            if z2 - z1 < 0.4 - 1.0e-12:
                continue
            for stop in upper_indices:
                indices = np.arange(0, stop)
                result = score_candidate(cache[float(z1)], cache[float(z2)], indices, beta)
                row = {
                    **result,
                    "z1": float(z1),
                    "z2": float(z2),
                    "lambda_min": float(WAVELENGTH_GRID_UM[0]),
                    "lambda_max": float(WAVELENGTH_GRID_UM[stop - 1]),
                    "n_lambda": int(stop),
                }
                if best is None or row["score"] > best["score"]:
                    best = row
    return best


def exhaustive_band_check(z1: float, z2: float, beta: float):
    positions = np.asarray([z1, z2])
    cache = build_cache(positions)
    best = None
    for start in range(0, len(WAVELENGTH_GRID_UM) - 4):
        for stop in range(start + 5, len(WAVELENGTH_GRID_UM) + 1):
            indices = np.arange(start, stop)
            result = score_candidate(cache[z1], cache[z2], indices, beta)
            row = {
                **result,
                "lambda_min": float(WAVELENGTH_GRID_UM[start]),
                "lambda_max": float(WAVELENGTH_GRID_UM[stop - 1]),
                "n_lambda": int(len(indices)),
            }
            if best is None or row["score"] > best["score"]:
                best = row
    return best


def reference_snr(score: float, n_reference_wavelengths: int = 81):
    """Illustrative fixed-time SNR for 0.10-deg full-absorption channel noise.

    Frequencies are held fixed between compared designs. The differential
    two-channel sqrt(2) noise is already included in the whitening weights.
    """
    return (
        score
        * np.sqrt(n_reference_wavelengths)
        / np.deg2rad(REFERENCE_NOISE_DEG)
    )


def main() -> None:
    print("Programmed translated-gradient joint depth / spectral design")
    print("front + back interface nuisances included")
    print()

    stored = {}
    for clearance in CLEARANCES_UM:
        result = optimize_clearance(clearance, beta=1.0)
        stored[(clearance, 1.0)] = result
        print(
            f"clearance={clearance:.1f} um, additive-like beta=1: "
            f"z={result['z1']:.1f}->{result['z2']:.1f} um, "
            f"lambda={result['lambda_min']:.2f}-{result['lambda_max']:.3f} um, "
            f"N={result['n_lambda']}, score={result['score']:.9f}, "
            f"angle={result['angle_deg']:.3f} deg, "
            f"Pabs_min={result['pabs_min']:.6f}"
        )
    print()

    recommended = stored[(1.5, 1.0)]
    statistics = optimize_clearance(1.5, beta=0.5)
    stored[(1.5, 0.5)] = statistics
    print("1.5-um interface-clearance noise-model check")
    print(
        f"statistics-like beta=0.5 -> z={statistics['z1']:.1f}->"
        f"{statistics['z2']:.1f} um, lambda={statistics['lambda_min']:.2f}-"
        f"{statistics['lambda_max']:.3f} um, score={statistics['score']:.9f}"
    )
    print(
        f"additive-like beta=1 -> z={recommended['z1']:.1f}->"
        f"{recommended['z2']:.1f} um, lambda={recommended['lambda_min']:.2f}-"
        f"{recommended['lambda_max']:.3f} um, score={recommended['score']:.9f}"
    )

    exhaustive = exhaustive_band_check(4.1, 5.6, beta=1.0)
    print()
    print("exhaustive contiguous-band check for recommended pair")
    print(
        f"lambda={exhaustive['lambda_min']:.3f}-"
        f"{exhaustive['lambda_max']:.3f} um, N={exhaustive['n_lambda']}, "
        f"score={exhaustive['score']:.9f}, "
        f"Pabs_min={exhaustive['pabs_min']:.6f}"
    )
    print(
        "illustrative fixed-81-wavelength-time SNR at 0.10-deg full-absorption "
        f"individual-channel component noise = {reference_snr(exhaustive['score']):.3f}"
    )

    restricted = exhaustive_band_check(2.6, 3.2, beta=1.0)
    gain = exhaustive["score"] / restricted["score"]
    print()
    print("comparison with earlier restricted 2.6->3.2 pair")
    print(
        f"restricted best band={restricted['lambda_min']:.3f}-"
        f"{restricted['lambda_max']:.3f} um, score={restricted['score']:.9f}"
    )
    print(f"recommended / restricted fixed-time information amplitude = {gain:.3f}x")

    # Regression anchors from the independently checked design calculation.
    assert abs(recommended["z1"] - 4.1) < 1.0e-12
    assert abs(recommended["z2"] - 5.6) < 1.0e-12
    assert abs(recommended["lambda_max"] - 2.4) < 1.0e-9
    assert 0.00272 < recommended["score"] < 0.00274
    assert recommended["pabs_min"] > 0.990

    assert abs(statistics["z1"] - 4.1) < 1.0e-12
    assert abs(statistics["z2"] - 5.6) < 1.0e-12
    assert abs(statistics["lambda_max"] - 2.4) < 1.0e-9

    assert abs(exhaustive["lambda_min"] - 2.0) < 1.0e-12
    assert abs(exhaustive["lambda_max"] - 2.4) < 1.0e-9
    assert exhaustive["n_lambda"] == 17
    assert 1.88 < gain < 1.90

    margin2 = stored[(2.0, 1.0)]
    assert abs(margin2["z1"] - 3.8) < 1.0e-12
    assert abs(margin2["z2"] - 5.1) < 1.0e-12
    assert margin2["score"] > 0.00250

    print()
    print(
        "PASS: once the inherited shallow position limit is removed and both "
        "interfaces are treated as possible confounders, the purpose-built "
        "programmed-gradient experiment moves deeper and uses a shorter, strongly "
        "absorbed spectral band. Requiring the full feature to remain 1.5 um "
        "from both interfaces gives a robust 4.1->5.6 um pair with a 2.00-2.40 um "
        "scan under both statistics-like and additive-like phase-noise scaling. "
        "Its fixed-time nuisance-orthogonal information amplitude is ~1.9x the "
        "earlier restricted 2.6->3.2 design."
    )


if __name__ == "__main__":
    main()
