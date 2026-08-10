"""Physical-nuisance design for downstream graded-HgCdTe relocation metrology.

This is the first design calculation built on the physics-derived downstream
first-passage drift-diffusion operator rather than the earlier ad hoc 25% local
delay perturbation.

Target parameter
----------------
The realized optical composition profile x(z) is held fixed. In the transport
field only, decompose the composition-slope magnitude as

    s_eff(z; eta) = s0 + eta [s(z)-s0],

where s0=(x_front-x_back)/L and s(z) is the programmed profile slope.

eta=1 -> full programmed local-gradient transport field;
eta=0 -> smooth same-endpoint background field evaluated on the same optical
         x(z) profile.

`eta` is a statistical mechanism coordinate, not a physically switchable field.
Its derivative asks whether wavelength x RF data require the localized excess
field pattern beyond a smooth graded-transport background.

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
The eta derivative is marginalized against free common derivatives with respect
to

    ln mu, ln chi_E, ln tau_rec, ln v_sat, ln S.

An arbitrary wavelength-independent phase and log-magnitude offset is also
allowed independently for every device and RF frequency.

Measurement weighting
---------------------
A provisional statistics-like complex-log-response weight is

    w(lambda,f) = |H| sqrt(Pabs * Cdc),

where Cdc is the modeled DC collection probability. This captures the basic
fact that high-RF points and weakly collected wavelengths carry less phase/
log-magnitude information. It is NOT a replacement for measured covariance.

Design score
------------
After whitening and nuisance projection,

    score = ||d_eta_perp|| / sqrt(N_device N_f N_lambda).

This is proportional to a fixed-total-resource mechanism SNR under the stated
noise convention. Absolute score is not an experimental sigma value.

Main result
-----------
On the current feature-center grid 2.0-5.6 um in 0.2-um steps, using the dense
2.00-2.40 um wavelength grid and RF support 1.5,2.0,2.5,3.0 GHz, the best
four-depth design is approximately

    2.4, 2.8, 5.2, 5.6 um.

A fifth depth adds only about 0.5% fixed-time score. High RF is essential: for
this four-depth set, 1.5/3.0 GHz already carries nearly the same information as
four high-RF points, whereas 0.25/0.5/1.0 GHz is strongly degenerate with the
physical transport nuisances.

The exact wavelength support is deliberately NOT frozen here. A fine-grid
sparse optimizer exploits sharp optical-threshold structure and must first be
stressed against composition/absorption-model uncertainty.

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
    effective_field_v_cm,
    drift_velocity_cm_s,
    KBT_OVER_Q_V,
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
OPT_RF_GHZ = (1.5, 2.0, 2.5, 3.0)
RF_CANDIDATE_GHZ = (0.25, 0.50, 0.75, 1.0, 1.5, 2.0, 2.5, 3.0)
NUISANCE_NAMES = ("mu", "chi", "tau", "vsat", "surface")
FINITE_DIFFERENCE_LOG_STEP = 0.01


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
    """Return normalized H, Pabs and DC collection for one feature depth."""
    z_um, x, _, slope = programmed_profile(z0_um, n_grid)
    smooth_slope = (0.55 - 0.32) / 7.6
    effective_slope = smooth_slope + eta * (slope - smooth_slope)

    field = effective_field_v_cm(x, effective_slope, field_fraction)

    # Reuse the canonical backward solver by providing an equivalent slope and
    # field fraction. Since effective_field_v_cm is linear in slope, the direct
    # solver call below is exact for the current reduced model.
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
            float(
                np.real(
                    np.trapezoid(density * dc_transform, z_cm)
                )
            )
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
    """Finite-difference mechanism/nuisance derivatives of complex ln H."""
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

    derivatives = {}
    step = FINITE_DIFFERENCE_LOG_STEP

    plus = dict(kwargs)
    minus = dict(kwargs)
    plus["eta"] += step
    minus["eta"] -= step
    derivatives["eta"] = (
        np.log(transfer_eta(z0_um, **plus)[0])
        - np.log(transfer_eta(z0_um, **minus)[0])
    ) / (2.0 * step)

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
        derivatives[name] = (
            np.log(transfer_eta(z0_um, **plus)[0])
            - np.log(transfer_eta(z0_um, **minus)[0])
        ) / (2.0 * step)

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
        round(float(z0), 6): raw_log_derivatives(
            float(z0), frequencies_ghz
        )
        for z0 in POSITION_GRID_UM
    }


def design_score(
    depths_um: tuple[float, ...],
    frequencies_ghz: tuple[float, ...],
    cache,
):
    data = [cache[round(float(z), 6)] for z in depths_um]
    n_device = len(depths_um)
    n_frequency = len(frequencies_ghz)
    n_lambda = len(LAMBDA_GRID_UM)

    weights = []
    for h0, pabs, dc_collection, _ in data:
        weights.append(
            np.sqrt(pabs * dc_collection)[None, :] * np.abs(h0)
        )
    weights = np.asarray(weights)

    def parameter_array(name: str):
        return np.stack([item[3][name] for item in data])

    def flatten_weighted(values: np.ndarray):
        return np.concatenate(
            (
                (values.imag * weights).ravel(),
                (values.real * weights).ravel(),
            )
        )

    target = flatten_weighted(parameter_array("eta"))
    nuisance_columns = [
        flatten_weighted(parameter_array(name))
        for name in NUISANCE_NAMES
    ]

    # Free wavelength-independent phase and ln|H| offset for every device/RF.
    for device in range(n_device):
        for frequency in range(n_frequency):
            phase_offset = np.zeros(
                (n_device, n_frequency, n_lambda), dtype=complex
            )
            phase_offset[device, frequency, :] = 1j
            nuisance_columns.append(flatten_weighted(phase_offset))

            magnitude_offset = np.zeros(
                (n_device, n_frequency, n_lambda), dtype=complex
            )
            magnitude_offset[device, frequency, :] = 1.0
            nuisance_columns.append(flatten_weighted(magnitude_offset))

    nuisance = np.column_stack(nuisance_columns)
    residual = qr_project_residual(target, nuisance)

    residual_norm = float(np.linalg.norm(residual))
    target_norm = float(np.linalg.norm(target))
    angle = float(
        np.degrees(
            np.arcsin(np.clip(residual_norm / target_norm, 0.0, 1.0))
        )
    )
    score = residual_norm / np.sqrt(n_device * n_frequency * n_lambda)
    minimum_h = float(
        min(np.min(np.abs(item[0])) for item in data)
    )
    return score, angle, residual_norm, target_norm, minimum_h


def optimize_depths(n_device: int, cache):
    best = None
    count = 0
    for depths in itertools.combinations(POSITION_GRID_UM, n_device):
        if np.min(np.diff(depths)) < POSITION_MIN_SPACING_UM - 1.0e-12:
            continue
        depths = tuple(float(value) for value in depths)
        result = design_score(depths, OPT_RF_GHZ, cache)
        count += 1
        if best is None or result[0] > best[1][0]:
            best = (depths, result)
    if best is None:
        raise RuntimeError("No admissible depth design")
    return count, best


def main() -> None:
    cache = build_cache(OPT_RF_GHZ)

    print("Physics-derived localized-gradient mechanism design")
    print(f"RF support = {OPT_RF_GHZ} GHz")
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

    four_depths = designs[4][0]

    # RF ablation on the final four-depth geometry. Build separate caches so the
    # per-RF free offsets are handled correctly.
    rf_tests = {
        "low": (0.25, 0.50, 1.0),
        "sparse_high": (1.5, 3.0),
        "high": OPT_RF_GHZ,
    }
    rf_results = {}
    for label, frequencies in rf_tests.items():
        test_cache = {
            round(float(z), 6): raw_log_derivatives(float(z), frequencies)
            for z in four_depths
        }
        value = design_score(four_depths, frequencies, test_cache)
        rf_results[label] = value
        print(
            f"RF {label} {frequencies}: score={value[0]:.9f}; "
            f"angle={value[1]:.6f} deg; min |H|={value[4]:.6f}"
        )

    # Regression anchors.
    assert designs[2][0] == (
        2.8000000000000007,
        5.600000000000003,
    )
    assert designs[3][0] == (
        2.4000000000000004,
        2.8000000000000007,
        5.600000000000003,
    )
    assert designs[4][0] == (
        2.4000000000000004,
        2.8000000000000007,
        5.200000000000003,
        5.600000000000003,
    )
    assert 0.00513 < designs[4][1][0] < 0.00516
    assert 4.49 < designs[4][1][1] < 4.52
    assert 0.144 < designs[4][1][4] < 0.146

    assert 0.00516 < designs[5][1][0] < 0.00519
    assert designs[5][1][0] / designs[4][1][0] < 1.01

    assert rf_results["low"][0] < 1.4e-4
    assert 0.00509 < rf_results["sparse_high"][0] < 0.00512
    assert 0.00513 < rf_results["high"][0] < 0.00516

    print()
    print(
        "PASS: after replacing arbitrary delay nuisances with a physical central "
        "transport parameterization, high-RF complex response becomes the main "
        "mechanism-separation resource. On the current grid, four feature depths "
        "2.4/2.8/5.2/5.6 um with 1.5-3 GHz data nearly saturate fixed-time "
        "information; a fifth depth adds <1%. Low <=1-GHz data remain strongly "
        "degenerate with mobility/lifetime/field/velocity-law changes. Exact "
        "wavelength supports are not frozen until optical-profile uncertainty is "
        "included."
    )


if __name__ == "__main__":
    main()
