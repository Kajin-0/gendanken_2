"""Independent coarse-observable cross-check for Paper 03 Stage A.

Implements PAPER03_STAGEA_CROSS_FORMULATION_PREDECLARATION_2026-08-17.md.
The stochastic Euler--Maruyama path solver is compared with the deterministic
backward resolvent at five fixed source points.  The compared quantities are
selected-contact hitting probability and direct single-source Shockley--Ramo
responses, not nonlinear spectral closure statistics.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import numpy as np
from scipy.interpolate import RegularGridInterpolator
from scipy.sparse.linalg import spsolve

import paper03_combined_physics_challenge as stochastic
import paper03_stageA_resolvent as resolvent
import realistic_geometry_closure_stress as base


D_M2_S = 2.5e-3
TAU_S = float("inf")
N_PATHS = 4000
FIELD_GRID = (201, 151)
DETERMINISTIC_GRIDS = ((121, 91), (201, 151))
DS_UM = 0.020
RMS_DIFFUSION_STEP_UM = 0.040
MAX_TIME_S = 5.0e-9
MAX_STEPS = 20000
FATE_LIMIT_FRACTION = 1.0e-3
SIGMA_MULTIPLIER = 4.0
SOURCE_POINTS_UM = (
    (0.0, 2.5),
    (0.0, 4.0),
    (2.0, 3.0),
    (-2.0, 3.0),
    (5.0, 3.0),
)
SEEDS = (51001, 51002, 51003, 51004, 51005)


def embed_committor(gen: resolvent.DiscreteGenerator) -> np.ndarray:
    """Selected-contact hitting probability on the full deterministic grid."""
    p = spsolve((-gen.Q).tocsc(), gen.b_selected)
    full = np.zeros(len(gen.xs) * len(gen.zs), float)
    full[gen.transient_flat] = np.asarray(p, float)
    full = full.reshape(len(gen.zs), len(gen.xs))
    full[gen.selected_mask] = 1.0
    full[gen.bottom_mask] = 0.0
    return full


def deterministic_point_table(
    scenario: base.Scenario,
    nx: int,
    nz: int,
) -> tuple[dict[tuple[float, float], dict[str, Any]], dict[str, Any]]:
    cfg = resolvent.ResolventConfig(
        diffusion_m2_s=D_M2_S,
        lifetime_s=TAU_S,
        nx=nx,
        nz=nz,
        nx_src=1,
    )
    gen = resolvent.build_generator(scenario, cfg)
    U, diag = resolvent.solve_resolvent(gen, cfg)
    pgrid = embed_committor(gen)
    pinterp = RegularGridInterpolator(
        (gen.zs, gen.xs), pgrid, method="linear", bounds_error=True
    )
    hinterps = []
    for kf in range(len(base.FREQUENCIES)):
        hinterps.append(
            RegularGridInterpolator(
                (gen.zs, gen.xs),
                resolvent.full_grid(gen, U[kf]),
                method="linear",
                bounds_error=True,
            )
        )

    out: dict[tuple[float, float], dict[str, Any]] = {}
    for x_um, z_um in SOURCE_POINTS_UM:
        point = np.asarray([[z_um * 1e-6, x_um * 1e-6]], float)
        psel = float(pinterp(point)[0])
        H = np.asarray([h(point)[0] for h in hinterps], complex)
        out[(x_um, z_um)] = {
            "p_selected": psel,
            "H": H,
        }
    return out, diag


def stochastic_point(
    g: dict[str, Any],
    x_um: float,
    z_um: float,
    seed: int,
) -> dict[str, Any]:
    cfg = stochastic.StochasticConfig(
        diffusion_m2_s=D_M2_S,
        lifetime_s=TAU_S,
        particles_per_source=N_PATHS,
        seed=seed,
        ds_um=DS_UM,
        nx=FIELD_GRID[0],
        nz=FIELD_GRID[1],
        nx_src=1,
        nz_src=1,
        rms_diffusion_step_um=RMS_DIFFUSION_STEP_UM,
        max_time_s=MAX_TIME_S,
        max_steps=MAX_STEPS,
    )
    rng = np.random.default_rng(seed)
    H = np.empty((N_PATHS, len(base.FREQUENCIES)), complex)
    selected = np.empty(N_PATHS, float)
    fates: dict[str, int] = {}
    max_ramo_error = 0.0
    for k in range(N_PATHS):
        path = stochastic.stochastic_path(g, x_um, z_um, cfg, rng)
        H[k] = path.H
        selected[k] = 1.0 if path.fate == "selected_contact" else 0.0
        fates[path.fate] = fates.get(path.fate, 0) + 1
        max_ramo_error = max(max_ramo_error, path.endpoint_ramo_error)

    mean_H = np.mean(H, axis=0)
    if N_PATHS > 1:
        se_real = np.std(H.real, axis=0, ddof=1) / np.sqrt(N_PATHS)
        se_imag = np.std(H.imag, axis=0, ddof=1) / np.sqrt(N_PATHS)
        se_p = float(np.std(selected, ddof=1) / np.sqrt(N_PATHS))
    else:
        se_real = np.zeros(len(base.FREQUENCIES))
        se_imag = np.zeros(len(base.FREQUENCIES))
        se_p = 0.0

    unresolved = fates.get("step_limit", 0) + fates.get("time_limit", 0)
    return {
        "mean_p_selected": float(np.mean(selected)),
        "se_p_selected": se_p,
        "mean_H": mean_H,
        "se_H_real": np.asarray(se_real, float),
        "se_H_imag": np.asarray(se_imag, float),
        "fates": fates,
        "unresolved_fraction": float(unresolved / N_PATHS),
        "max_endpoint_ramo_error": float(max_ramo_error),
        "seed": seed,
    }


def scalar_check(
    name: str,
    mc: float,
    se: float,
    coarse: float,
    fine: float,
) -> dict[str, Any]:
    delta = abs(mc - fine)
    discretization = abs(fine - coarse)
    allowance = SIGMA_MULTIPLIER * se + discretization
    return {
        "observable": name,
        "monte_carlo": float(mc),
        "monte_carlo_standard_error": float(se),
        "deterministic_coarse": float(coarse),
        "deterministic_fine": float(fine),
        "absolute_mc_minus_fine": float(delta),
        "absolute_fine_minus_coarse": float(discretization),
        "acceptance_allowance": float(allowance),
        "passed": bool(delta <= allowance),
        "normalized_excess_over_allowance": float(
            delta / max(allowance, np.finfo(float).tiny)
        ),
    }


def compare_point(
    point: tuple[float, float],
    mc: dict[str, Any],
    coarse: dict[str, Any],
    fine: dict[str, Any],
) -> dict[str, Any]:
    checks = [
        scalar_check(
            "p_selected",
            mc["mean_p_selected"],
            mc["se_p_selected"],
            coarse["p_selected"],
            fine["p_selected"],
        ),
        scalar_check(
            "H_DC_real",
            float(mc["mean_H"][0].real),
            float(mc["se_H_real"][0]),
            float(coarse["H"][0].real),
            float(fine["H"][0].real),
        ),
    ]
    for kf, f in enumerate(base.FREQUENCIES[1:], start=1):
        label = f"H_{f/1e6:.0f}MHz"
        checks.append(
            scalar_check(
                label + "_real",
                float(mc["mean_H"][kf].real),
                float(mc["se_H_real"][kf]),
                float(coarse["H"][kf].real),
                float(fine["H"][kf].real),
            )
        )
        checks.append(
            scalar_check(
                label + "_imag",
                float(mc["mean_H"][kf].imag),
                float(mc["se_H_imag"][kf]),
                float(coarse["H"][kf].imag),
                float(fine["H"][kf].imag),
            )
        )

    fate_ok = mc["unresolved_fraction"] <= FATE_LIMIT_FRACTION
    return {
        "source_point_um": {"x": point[0], "z": point[1]},
        "monte_carlo": {
            "seed": mc["seed"],
            "paths": N_PATHS,
            "fates": mc["fates"],
            "unresolved_fraction": mc["unresolved_fraction"],
            "max_endpoint_ramo_error": mc["max_endpoint_ramo_error"],
        },
        "checks": checks,
        "observable_checks_passed": bool(all(c["passed"] for c in checks)),
        "unresolved_fate_gate_passed": bool(fate_ok),
        "point_passed": bool(all(c["passed"] for c in checks) and fate_ok),
    }


def json_safe(obj: Any) -> Any:
    if isinstance(obj, dict):
        return {str(k): json_safe(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [json_safe(v) for v in obj]
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    if isinstance(obj, np.generic):
        return json_safe(obj.item())
    if isinstance(obj, complex):
        return {"real": float(obj.real), "imag": float(obj.imag)}
    if isinstance(obj, float):
        if np.isnan(obj):
            return "nan"
        if np.isposinf(obj):
            return "inf"
        if np.isneginf(obj):
            return "-inf"
    return obj


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("paper03_stageA_cross_formulation.json"),
    )
    args = parser.parse_args()

    scenario = next(s for s in base.SCENARIOS if s.name == "finite75_depletion")
    print("building deterministic comparison grids", flush=True)
    coarse, diag_coarse = deterministic_point_table(scenario, *DETERMINISTIC_GRIDS[0])
    fine, diag_fine = deterministic_point_table(scenario, *DETERMINISTIC_GRIDS[1])

    print("building stochastic interpolation fields", flush=True)
    g = base.geometry(scenario, *FIELD_GRID)
    points = []
    for point, seed in zip(SOURCE_POINTS_UM, SEEDS):
        print(f"MC point={point} N={N_PATHS} seed={seed}", flush=True)
        mc = stochastic_point(g, point[0], point[1], seed)
        points.append(compare_point(point, mc, coarse[point], fine[point]))

    all_observables = [c for p in points for c in p["checks"]]
    overall = all(p["point_passed"] for p in points)
    result = {
        "schema": "paper03-stageA-cross-formulation-v1",
        "status": "PREDECLARED NUMERICAL CROSS-FORMULATION CHECK / NON-CLAIM",
        "predeclaration": "PAPER03_STAGEA_CROSS_FORMULATION_PREDECLARATION_2026-08-17.md",
        "physical_coordinate": {
            "scenario": scenario.__dict__,
            "diffusion_m2_s": D_M2_S,
            "lifetime_s": "inf",
        },
        "stochastic": {
            "field_grid": list(FIELD_GRID),
            "paths_per_source": N_PATHS,
            "trajectory_drift_step_um": DS_UM,
            "maximum_requested_diffusion_rms_step_um": RMS_DIFFUSION_STEP_UM,
            "maximum_time_s": MAX_TIME_S,
            "maximum_steps": MAX_STEPS,
            "seeds": list(SEEDS),
        },
        "deterministic": {
            "coarse_grid": list(DETERMINISTIC_GRIDS[0]),
            "fine_grid": list(DETERMINISTIC_GRIDS[1]),
            "coarse_solver_diagnostics": diag_coarse,
            "fine_solver_diagnostics": diag_fine,
        },
        "acceptance": {
            "equation": "abs(MC-fine) <= 4*SE_MC + abs(fine-coarse)",
            "monte_carlo_se_multiplier": SIGMA_MULTIPLIER,
            "maximum_unresolved_fate_fraction": FATE_LIMIT_FRACTION,
        },
        "points": points,
        "summary": {
            "scalar_observable_count": len(all_observables),
            "scalar_observable_pass_count": int(sum(c["passed"] for c in all_observables)),
            "point_pass_count": int(sum(p["point_passed"] for p in points)),
            "maximum_normalized_excess_over_allowance": float(
                max(c["normalized_excess_over_allowance"] for c in all_observables)
            ),
            "maximum_endpoint_ramo_error": float(
                max(p["monte_carlo"]["max_endpoint_ramo_error"] for p in points)
            ),
            "maximum_unresolved_fraction": float(
                max(p["monte_carlo"]["unresolved_fraction"] for p in points)
            ),
            "overall_predeclared_cross_formulation_pass": bool(overall),
        },
        "science_interpretation_ready": False,
    }

    args.output.write_text(
        json.dumps(json_safe(result), indent=2, allow_nan=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result["summary"], indent=2))
    for p in points:
        print(p["source_point_um"], "pass=", p["point_passed"])
        for c in p["checks"]:
            print(
                " ", c["observable"], "pass=", c["passed"],
                "ratio=", f"{c['normalized_excess_over_allowance']:.4g}"
            )
    print("science_interpretation_ready = false")
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
