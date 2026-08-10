"""Physical-nuisance design for downstream graded-HgCdTe relocation metrology.

This file uses the physics-derived downstream first-passage drift-diffusion
operator rather than the earlier ad hoc 25% local-delay perturbation.

Important numerical correction
------------------------------
Do NOT finite-difference `np.log(H)` directly at high RF. The principal complex
logarithm can cross a branch cut and create artificial 2*pi phase derivative
spikes. All derivatives here use the branch-safe identity

    d ln H / dp = (1/H) dH/dp

with dH/dp evaluated by centered finite differences.

A previous revision of this file used direct principal-log differences and
therefore overstated high-RF mechanism separation. That result is superseded.

Target coordinate
-----------------
The realized optical x(z) profile is fixed. For transport sensitivity only,

    s_eff(z;eta)=s0 + eta [s(z)-s0].

eta=1 gives the full programmed local-gradient transport field; eta=0 replaces
its localized slope deviation by a smooth same-endpoint background while keeping
the same optical x(z). `eta` is a statistical mechanism coordinate, not a
physically switchable field.

Central sensitivity point
-------------------------
T=300 K
mu=9000 cm2/Vs
chi_E=0.5
tau_rec=1 ns
v_sat=1e5 m/s
entrance S=1e5 cm/s.

These are sensitivity coordinates, NOT a calibrated device parameter set.

Physical nuisance parameters
----------------------------
Marginalize the eta derivative against free common derivatives with respect to

    ln mu, ln chi_E, ln tau_rec, ln v_sat, ln S.

Also allow one arbitrary wavelength-independent phase and ln|H| offset for every
device and RF frequency.

Measurement weighting
---------------------
A provisional statistics-like complex-log-response weight is

    w(lambda,f)=|H| sqrt(Pabs*Cdc).

This is only a design stress, not measured covariance.

Corrected result
----------------
After branch-safe differentiation, the central reduced model remains highly
mechanism-degenerate. High RF gives a large measurable transport response, but
letting the generic high-field transport law float freely removes almost all of
the localized-gradient attribution information.

For RF = 0.5,1,2,3 GHz and lambda=2.00-2.40 um, the best fixed-resource depth
counts on the current 0.2-um grid are approximately

    2 depths: 5.2,5.6 um
    3 depths: 2.4,5.2,5.6 um  <- best score
    4 depths: 3.4,4.4,5.2,5.6 um
    5 depths: 2.4,3.4,4.4,5.2,5.6 um.

The best three-depth target lies only ~0.12 deg from the five-parameter physical
nuisance span. Adding devices or high RF does not solve this structural
attribution problem by itself.

The next design resource is therefore INDEPENDENT calibration/constraint of the
generic transport law, especially the high-field velocity relation, rather than
more uncalibrated spectral/RF dimensions.

No novelty claim.
"""

from __future__ import annotations

import itertools
import numpy as np
from scipy.linalg import qr

from hgcdte_downstream_drift_diffusion_relocation import (
    LAMBDA_GRID_UM,
    programmed_profile,
    generation_density,
    solve_backward_transform,
)

CENTRAL = {
    "eta": 1.0,
    "mobility_cm2_vs": 9000.0,
    "field_fraction": 0.50,
    "tau_rec_ns": 1.0,
    "velocity_sat_m_s": 1.0e5,
    "surface_recombination_cm_s": 1.0e5,
}

POSITION_GRID_UM = np.arange(2.0, 5.6001, 0.2)
POSITION_MIN_SPACING_UM = 0.4
DESIGN_RF_GHZ = (0.5, 1.0, 2.0, 3.0)
NUISANCE_NAMES = ("mu", "chi", "tau", "vsat", "surface")
FINITE_DIFFERENCE_STEP = 0.01


def transfer_eta(
    z0_um: float,
    frequencies_ghz: tuple[float, ...],
    wavelengths_um: np.ndarray = LAMBDA_GRID_UM,
    eta: float = 1.0,
    mobility_cm2_vs: float = 9000.0,
    field_fraction: float = 0.50,
    tau_rec_ns: float = 1.0,
    velocity_sat_m_s: float = 1.0e5,
    surface_recombination_cm_s: float = 1.0e5,
    n_grid: int = 201,
):
    z_um, x, _, slope = programmed_profile(z0_um, n_grid)
    smooth_slope = (0.55 - 0.32) / 7.6
    effective_slope = smooth_slope + eta * (slope - smooth_slope)

    dc_transform, _, _, _ = solve_backward_transform(
        z_um,
        x,
        effective_slope,
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
    z_cm = z_um * 1.0e-4

    dc_collection = np.asarray(
        [
            float(np.real(np.trapezoid(density * dc_transform, z_cm)))
            for density, _ in optical
        ]
    )

    rows = []
    for frequency in frequencies_ghz:
        transform, _, _, _ = solve_backward_transform(
            z_um,
            x,
            effective_slope,
            mobility_cm2_vs,
            field_fraction,
            tau_rec_ns,
            float(frequency),
            velocity_sat_m_s,
            surface_recombination_cm_s,
        )
        rows.append(
            [
                np.trapezoid(density * transform, z_cm) / collection
                for (density, _), collection in zip(optical, dc_collection)
            ]
        )

    pabs = np.asarray([item[1] for item in optical])
    return np.asarray(rows), pabs, dc_collection


def raw_log_derivatives(
    z0_um: float,
    frequencies_ghz: tuple[float, ...],
    n_grid: int = 201,
):
    """Branch-safe finite differences of d ln H / dp = (dH/dp)/H."""
    kwargs = dict(
        frequencies_ghz=frequencies_ghz,
        eta=CENTRAL["eta"],
        mobility_cm2_vs=CENTRAL["mobility_cm2_vs"],
        field_fraction=CENTRAL["field_fraction"],
        tau_rec_ns=CENTRAL["tau_rec_ns"],
        velocity_sat_m_s=CENTRAL["velocity_sat_m_s"],
        surface_recombination_cm_s=CENTRAL["surface_recombination_cm_s"],
        n_grid=n_grid,
    )
    h0, pabs, dc_collection = transfer_eta(z0_um, **kwargs)
    step = FINITE_DIFFERENCE_STEP
    derivatives = {}

    plus = dict(kwargs)
    minus = dict(kwargs)
    plus["eta"] += step
    minus["eta"] -= step
    h_plus = transfer_eta(z0_um, **plus)[0]
    h_minus = transfer_eta(z0_um, **minus)[0]
    derivatives["eta"] = (h_plus - h_minus) / (2.0 * step * h0)

    mapping = {
        "mu": "mobility_cm2_vs",
        "chi": "field_fraction",
        "tau": "tau_rec_ns",
        "vsat": "velocity_sat_m_s",
        "surface": "surface_recombination_cm_s",
    }
    for name, key in mapping.items():
        plus = dict(kwargs)
        minus = dict(kwargs)
        plus[key] *= np.exp(step)
        minus[key] *= np.exp(-step)
        h_plus = transfer_eta(z0_um, **plus)[0]
        h_minus = transfer_eta(z0_um, **minus)[0]
        derivatives[name] = (h_plus - h_minus) / (2.0 * step * h0)

    return h0, pabs, dc_collection, derivatives


def qr_project_residual(target: np.ndarray, nuisance: np.ndarray) -> np.ndarray:
    qmat, rmat, _ = qr(nuisance, mode="economic", pivoting=True)
    diagonal = np.abs(np.diag(rmat))
    if len(diagonal) == 0 or diagonal[0] == 0.0:
        return target
    rank = int(np.sum(diagonal > diagonal[0] * 1.0e-10))
    return target - qmat[:, :rank] @ (qmat[:, :rank].T @ target)


def build_cache(frequencies_ghz: tuple[float, ...]):
    return {
        round(float(z0), 6): raw_log_derivatives(float(z0), frequencies_ghz)
        for z0 in POSITION_GRID_UM
    }


def design_score(depths_um: tuple[float, ...], frequencies_ghz, cache):
    data = [cache[round(float(z), 6)] for z in depths_um]
    n_device = len(depths_um)
    n_frequency = len(frequencies_ghz)
    n_lambda = len(LAMBDA_GRID_UM)

    weights = np.asarray(
        [
            np.sqrt(pabs * dc_collection)[None, :] * np.abs(h0)
            for h0, pabs, dc_collection, _ in data
        ]
    )

    def parameter_array(name: str):
        return np.stack([item[3][name] for item in data])

    def flatten_weighted(values: np.ndarray):
        return np.concatenate(
            ((values.imag * weights).ravel(), (values.real * weights).ravel())
        )

    target = flatten_weighted(parameter_array("eta"))
    nuisance_columns = [
        flatten_weighted(parameter_array(name)) for name in NUISANCE_NAMES
    ]

    # One free wavelength-independent phase and magnitude offset per device/RF.
    for device in range(n_device):
        for frequency in range(n_frequency):
            phase = np.zeros((n_device, n_frequency, n_lambda), dtype=complex)
            phase[device, frequency, :] = 1j
            nuisance_columns.append(flatten_weighted(phase))

            magnitude = np.zeros((n_device, n_frequency, n_lambda), dtype=complex)
            magnitude[device, frequency, :] = 1.0
            nuisance_columns.append(flatten_weighted(magnitude))

    residual = qr_project_residual(target, np.column_stack(nuisance_columns))
    residual_norm = float(np.linalg.norm(residual))
    target_norm = float(np.linalg.norm(target))
    angle = float(
        np.degrees(np.arcsin(np.clip(residual_norm / target_norm, 0.0, 1.0)))
    )
    score = residual_norm / np.sqrt(n_device * n_frequency * n_lambda)
    minimum_h = float(min(np.min(np.abs(item[0])) for item in data))
    return score, angle, residual_norm, target_norm, minimum_h


def optimize_depths(n_device: int, cache):
    best = None
    count = 0
    for depths in itertools.combinations(POSITION_GRID_UM, n_device):
        if np.min(np.diff(depths)) < POSITION_MIN_SPACING_UM - 1.0e-12:
            continue
        depths = tuple(float(value) for value in depths)
        result = design_score(depths, DESIGN_RF_GHZ, cache)
        count += 1
        if best is None or result[0] > best[1][0]:
            best = (depths, result)
    if best is None:
        raise RuntimeError("No admissible depth design")
    return count, best


def main() -> None:
    cache = build_cache(DESIGN_RF_GHZ)
    print("Branch-safe physical-nuisance relocation design")
    print(f"RF support = {DESIGN_RF_GHZ} GHz")
    print(
        f"lambda = {LAMBDA_GRID_UM[0]:.2f}-{LAMBDA_GRID_UM[-1]:.2f} um, "
        f"N={len(LAMBDA_GRID_UM)}"
    )
    print()

    designs = {}
    for n_device in (2, 3, 4, 5):
        count, best = optimize_depths(n_device, cache)
        designs[n_device] = best
        print(f"N_device={n_device}; tested={count}")
        print("  depths = " + ", ".join(f"{z:.1f}" for z in best[0]))
        print(
            f"  score={best[1][0]:.9f}; angle={best[1][1]:.6f} deg; "
            f"min |H|={best[1][4]:.6f}"
        )
        print()

    best_three = designs[3][0]
    rf_tests = {
        "low": (0.25, 0.50, 1.0),
        "mid_high": DESIGN_RF_GHZ,
        "high_only": (1.5, 2.0, 2.5, 3.0),
    }
    rf_results = {}
    for label, frequencies in rf_tests.items():
        test_cache = {
            round(float(z), 6): raw_log_derivatives(float(z), frequencies)
            for z in best_three
        }
        value = design_score(best_three, frequencies, test_cache)
        rf_results[label] = value
        print(
            f"RF {label} {frequencies}: score={value[0]:.9f}; "
            f"angle={value[1]:.6f} deg; min |H|={value[4]:.6f}"
        )

    # Regression anchors from the corrected branch-safe calculation.
    assert designs[2][0] == (
        5.200000000000003,
        5.600000000000003,
    )
    assert designs[3][0] == (
        2.4000000000000004,
        5.200000000000003,
        5.600000000000003,
    )
    assert designs[4][0] == (
        3.4000000000000012,
        4.400000000000002,
        5.200000000000003,
        5.600000000000003,
    )
    assert 0.000158 < designs[3][1][0] < 0.000160
    assert 0.121 < designs[3][1][1] < 0.123
    assert designs[4][1][0] < designs[3][1][0]
    assert designs[5][1][0] < designs[3][1][0]

    assert 0.000137 < rf_results["low"][0] < 0.000140
    assert 0.000158 < rf_results["mid_high"][0] < 0.000160
    assert 0.000145 < rf_results["high_only"][0] < 0.000148

    print()
    print(
        "PASS: branch-safe differentiation removes the false high-RF Fisher "
        "advance. The physics-derived transport response itself remains large, "
        "but the localized-gradient mechanism derivative is still nearly inside "
        "the span of generic mobility/field/lifetime/velocity/surface changes. "
        "Three depths are enough to saturate the current no-prior design; adding "
        "more uncalibrated devices or RF points does not resolve attribution. "
        "Independent transport-law calibration or informative physical priors are "
        "therefore mandatory before claiming the localized gradient caused a "
        "measured timing change."
    )


if __name__ == "__main__":
    main()
