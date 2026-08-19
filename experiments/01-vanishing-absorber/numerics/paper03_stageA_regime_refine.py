"""Refine predeclared Stage-A regime-screen selections.

The input manifest is generated only from the committed selection rules in
PAPER03_STAGEA_REGIME_MAP_PREDECLARATION_2026-08-17.md after the full 60-point
screen completes.  This script does not choose attractive points itself.

Each unique selected detector coordinate is recomputed at 161x121 and 201x151
with 17-point lateral quadrature.  The retained numerical readiness rule is the
same <=2%-of-frozen-target raw phase change at every nonzero RF.  Refined
same-physics mimic, calibrated-kernel one-mode residual, and analytic rejection
SNR are reported.  Bootstrap selection is determined from the predeclared rule
labels carried in the manifest; this file performs no new bootstrap.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import numpy as np

import paper03_stageA_kernel_blind_gate as kernel
import paper03_stageA_regime_screen as screen
import paper03_stageA_resolvent as resolvent
import paper03_stageA_statistical_bootstrap as bootstrap
import realistic_geometry_closure_stress as base


GRIDS = ((161, 121), (201, 151))
NX_SRC = 17
PHASE_REFINEMENT_FRACTION_GATE = 0.02
ALL6 = np.arange(len(base.DEPTHS), dtype=int)
_, LAMBDA_REQUIRED = bootstrap.analytic_lambda_required(6)


def tau_value(x: Any) -> float:
    if x == "inf":
        return float("inf")
    return float(x)


def scenario_from(p: dict[str, Any], name: str) -> base.Scenario:
    return base.Scenario(
        name=name,
        contact_fraction=float(p["contact_fraction"]),
        depletion_width_um=float(p["depletion_width_um"]),
        space_charge_drop_v=float(p["space_charge_drop_v"]),
    )


def solve_coordinate(
    p: dict[str, Any],
    nx: int,
    nz: int,
    *,
    reference: bool = False,
) -> tuple[np.ndarray, dict[str, Any]]:
    if reference:
        scenario = base.Scenario("same_physics_reference", 1.0, 0.0, 0.0)
    else:
        scenario = scenario_from(p, p.get("manifest_id", "selected"))
    cfg = resolvent.ResolventConfig(
        diffusion_m2_s=float(p["diffusion_m2_s"]),
        lifetime_s=tau_value(p["lifetime_s"]),
        nx=nx,
        nz=nz,
        nx_src=NX_SRC,
    )
    gen = resolvent.build_generator(scenario, cfg)
    U, diag = resolvent.solve_resolvent(gen, cfg)
    J = screen.integrate_beam(
        gen,
        U,
        float(p["beam_sigma_um"]),
        float(p["beam_center_um"]),
        nx_src=NX_SRC,
    )
    if diag["max_linear_relative_residual"] >= 1e-8:
        raise AssertionError("linear solver gate failed")
    if diag["committor_relative_residual"] >= 1e-8:
        raise AssertionError("committor gate failed")
    if np.isinf(tau_value(p["lifetime_s"])):
        if diag["dc_committor_ramo_max_abs_error"] >= 1e-8:
            raise AssertionError("dc committor/Ramo gate failed")
    return J, diag


def phase(J: np.ndarray, kf: int) -> float:
    return float(np.degrees(base.metrics(J)[kf]["c4"].imag))


def refined_frequency_row(
    p: dict[str, Any],
    J: np.ndarray,
    Jref: np.ndarray,
    kf: int,
) -> dict[str, Any]:
    f = float(base.FREQUENCIES[kf])
    y = np.asarray(J[kf], complex)
    fit = kernel.kernel_one_mode_fit(y, ALL6)
    residual = np.asarray(fit["residual"]["real"], float) + 1j*np.asarray(
        fit["residual"]["imag"], float
    )
    residual_norm = float(np.linalg.norm(residual))
    step = float(np.mean(np.abs(np.diff(y))))
    snr = float(np.sqrt(LAMBDA_REQUIRED)*step/max(residual_norm, np.finfo(float).tiny))
    snr_db = float(20*np.log10(snr))
    pcase, pref = phase(J, kf), phase(Jref, kf)
    target = float(base.GRADIENT_TARGET_DEG[f])
    mimic = abs((pcase-pref)/target)
    claim = float(base.GRADIENT_SNR_DB[f])
    return {
        "frequency_hz": f,
        "raw_phase_deg": pcase,
        "same_physics_reference_phase_deg": pref,
        "finite_minus_reference_phase_deg": pcase-pref,
        "mimic_fraction": mimic,
        "rho1_all6": float(fit["contrast_normalized_residual"]),
        "one_mode_profile_condition": float(fit["profile_design_condition_number"]),
        "analytic_rejection_snr_db": snr_db,
        "transport_claim_snr_db": claim,
        "analytic_warning_margin_db": claim-snr_db,
        "order_one_refined": bool(mimic >= 0.50),
        "analytic_hidden_risk_refined": bool(mimic >= 0.50 and claim-snr_db <= 0),
    }


def refine_point(p: dict[str, Any]) -> dict[str, Any]:
    case = {}
    refs = {}
    diags = {}
    ref_diags = {}
    for nx, nz in GRIDS:
        key = f"{nx}x{nz}"
        print(f"  {p['manifest_id']} grid {key}", flush=True)
        case[key], diags[key] = solve_coordinate(p, nx, nz)
        refs[key], ref_diags[key] = solve_coordinate(p, nx, nz, reference=True)

    phase_changes = []
    for kf in (1,2,3):
        f = float(base.FREQUENCIES[kf])
        a = phase(case["161x121"], kf)
        b = phase(case["201x151"], kf)
        frac = abs(b-a)/abs(float(base.GRADIENT_TARGET_DEG[f]))
        phase_changes.append(
            {
                "frequency_hz": f,
                "phase_161_deg": a,
                "phase_201_deg": b,
                "change_fraction_of_frozen_target": float(frac),
                "passed": bool(frac <= PHASE_REFINEMENT_FRACTION_GATE),
            }
        )
    numerical_pass = all(x["passed"] for x in phase_changes)
    rows = [
        refined_frequency_row(p, case["201x151"], refs["201x151"], kf)
        for kf in (1,2,3)
    ]
    return {
        "manifest_id": p["manifest_id"],
        "selection_reasons": p["selection_reasons"],
        "coordinate": {
            k: p[k] for k in (
                "contact_fraction","depletion_width_um","space_charge_drop_v",
                "diffusion_m2_s","lifetime_s","beam_sigma_um","beam_center_um"
            )
        },
        "numerical": {
            "phase_refinement_threshold_fraction": PHASE_REFINEMENT_FRACTION_GATE,
            "phase_changes": phase_changes,
            "selected_point_refinement_passed": bool(numerical_pass),
            "case_solver_diagnostics": diags,
            "reference_solver_diagnostics": ref_diags,
        },
        "refined_frequency_rows": rows,
        "max_refined_mimic_fraction": float(max(r["mimic_fraction"] for r in rows)),
        "min_refined_analytic_warning_margin_db": float(min(r["analytic_warning_margin_db"] for r in rows)),
        "has_refined_order_one_row": bool(any(r["order_one_refined"] for r in rows)),
        "has_refined_analytic_hidden_risk_row": bool(any(r["analytic_hidden_risk_refined"] for r in rows)),
    }


def bootstrap_selection(refined: list[dict[str, Any]]) -> list[dict[str, Any]]:
    selected = []
    seen = set()

    def add(reason: str, p: dict[str, Any]):
        mid = p["manifest_id"]
        if mid in seen:
            return
        seen.add(mid)
        selected.append({
            "bootstrap_reason": reason,
            "manifest_id": mid,
            "coordinate": p["coordinate"],
        })

    # S2 if refined order-one.
    for p in refined:
        if "S2_worst_warning_margin_order_one" in p["selection_reasons"] and p["has_refined_order_one_row"]:
            add("S2_refined_order_one", p)
    # S3 if distinct and refined order-one.
    for p in refined:
        if "S3_closest_analytic_warning_boundary" in p["selection_reasons"] and p["has_refined_order_one_row"]:
            add("S3_refined_order_one", p)
    # S1 only if distinct and refined max mimic >1.
    for p in refined:
        if "S1_maximum_confound" in p["selection_reasons"] and p["max_refined_mimic_fraction"] > 1.0:
            add("S1_refined_mimic_gt_1", p)
    return selected


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    manifest = json.loads(args.manifest.read_text())
    points = manifest["selected_unique_points"]
    if not 1 <= len(points) <= 8:
        raise AssertionError("manifest must contain 1..8 predeclared selected points")

    refined = []
    for i,p in enumerate(points, start=1):
        print(f"refine {i}/{len(points)} {p['manifest_id']} reasons={p['selection_reasons']}", flush=True)
        refined.append(refine_point(p))

    boot = bootstrap_selection(refined)
    result = {
        "schema": "paper03-stageA-regime-refinement-v1",
        "status": "PREDECLARED SELECTED-POINT REFINEMENT / NON-CLAIM",
        "manifest": manifest,
        "grids": [list(g) for g in GRIDS],
        "lateral_quadrature": NX_SRC,
        "phase_refinement_fraction_gate": PHASE_REFINEMENT_FRACTION_GATE,
        "selected_point_results": refined,
        "counts": {
            "selected_unique_points": len(refined),
            "numerically_passed": int(sum(p["numerical"]["selected_point_refinement_passed"] for p in refined)),
            "refined_points_with_order_one_row": int(sum(p["has_refined_order_one_row"] for p in refined)),
            "refined_points_with_analytic_hidden_risk_row": int(sum(p["has_refined_analytic_hidden_risk_row"] for p in refined)),
        },
        "predeclared_new_bootstrap_points": boot,
        "nominal_bootstrap_reuse_allowed": True,
        "science_interpretation_ready": False,
    }
    args.output.write_text(
        json.dumps(resolvent.json_safe(result), indent=2, allow_nan=False)+"\n",
        encoding="utf-8",
    )
    print(json.dumps(result["counts"], indent=2))
    print("new bootstrap selections:")
    print(json.dumps(boot, indent=2))
    print("science_interpretation_ready = false")


if __name__ == "__main__":
    main()
