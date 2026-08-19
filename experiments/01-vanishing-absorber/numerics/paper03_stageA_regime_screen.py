"""Predeclared 60-point Stage-A regime-map screen for Paper 03.

Implements PAPER03_STAGEA_REGIME_MAP_PREDECLARATION_2026-08-17.md.
The 81x61 screen is a selection calculation only.  It uses the deterministic
backward resolvent, full calibrated optical kernels, the kernel-aware all-six
one-mode fit, and the local regular analytic rejection-SNR approximation.
No screen point is promoted to a scientific Outcome-A/B result without the
predeclared selected-point refinement/bootstrap stages.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any

import numpy as np
from scipy.interpolate import RegularGridInterpolator

import paper03_stageA_kernel_blind_gate as kernel
import paper03_stageA_resolvent as resolvent
import paper03_stageA_statistical_bootstrap as bootstrap
import realistic_geometry_closure_stress as base


NX, NZ = 81, 61
NX_SRC = 9
ALPHA = bootstrap.ALPHA
TARGET_POWER = bootstrap.TARGET_POWER
REGULAR_DOF = 6
ANALYTIC_CRITICAL, LAMBDA_REQUIRED = bootstrap.analytic_lambda_required(REGULAR_DOF)


@dataclass(frozen=True)
class ScreenPoint:
    block: str
    point_id: str
    contact_fraction: float
    depletion_width_um: float
    space_charge_drop_v: float
    diffusion_m2_s: float
    lifetime_s: float
    beam_sigma_um: float
    beam_center_um: float

    def scenario(self) -> base.Scenario:
        return base.Scenario(
            name=self.point_id,
            contact_fraction=self.contact_fraction,
            depletion_width_um=self.depletion_width_um,
            space_charge_drop_v=self.space_charge_drop_v,
        )


def lifetime_label(tau: float) -> str:
    return "inf" if np.isinf(tau) else f"{tau*1e9:g}ns"


def make_points() -> list[ScreenPoint]:
    points: list[ScreenPoint] = []
    idx = 0
    for fc in (0.50, 0.75, 0.875, 1.00):
        for wd, vsc in ((0.0, 0.0), (3.0, 0.05)):
            for D in (1.0e-3, 2.5e-3, 5.0e-3):
                for tau in (5.0e-9, float("inf")):
                    idx += 1
                    points.append(
                        ScreenPoint(
                            block="A",
                            point_id=f"A{idx:02d}",
                            contact_fraction=fc,
                            depletion_width_um=wd,
                            space_charge_drop_v=vsc,
                            diffusion_m2_s=D,
                            lifetime_s=tau,
                            beam_sigma_um=2.0,
                            beam_center_um=0.0,
                        )
                    )
    if idx != 48:
        raise AssertionError(idx)

    idx = 0
    for fc in (0.50, 0.75, 0.875):
        for sigma in (1.0, 2.0):
            for center in (0.0, 1.5):
                idx += 1
                points.append(
                    ScreenPoint(
                        block="B",
                        point_id=f"B{idx:02d}",
                        contact_fraction=fc,
                        depletion_width_um=3.0,
                        space_charge_drop_v=0.05,
                        diffusion_m2_s=2.5e-3,
                        lifetime_s=float("inf"),
                        beam_sigma_um=sigma,
                        beam_center_um=center,
                    )
                )
    if idx != 12 or len(points) != 60:
        raise AssertionError((idx, len(points)))
    return points


def integrate_beam(
    gen: resolvent.DiscreteGenerator,
    U: np.ndarray,
    beam_sigma_um: float,
    beam_center_um: float,
    nx_src: int = NX_SRC,
) -> np.ndarray:
    """Full calibrated-kernel integration for an arbitrary lateral Gaussian."""
    xq_um, wx = base.gauss(-base.X_EXTENT_UM, base.X_EXTENT_UM, nx_src)
    beam = np.exp(-0.5 * ((xq_um - beam_center_um) / beam_sigma_um) ** 2)
    beam /= np.sum(wx * beam)

    z_um = np.asarray(base.OPT_Z_UM, float)
    points = np.column_stack(
        (
            np.repeat(z_um * 1e-6, len(xq_um)),
            np.tile(xq_um * 1e-6, len(z_um)),
        )
    )
    J = np.zeros((len(base.FREQUENCIES), len(base.DEPTHS)), dtype=complex)
    for kf in range(len(base.FREQUENCIES)):
        grid = resolvent.full_grid(gen, U[kf])
        interp = RegularGridInterpolator(
            (gen.zs, gen.xs), grid, method="linear", bounds_error=True
        )
        vals = interp(points).reshape(len(z_um), len(xq_um))
        for ix in range(len(xq_um)):
            Hz = vals[:, ix]
            for m, optical in enumerate(base.OPTICS):
                J[kf, m] += (
                    wx[ix]
                    * beam[ix]
                    * np.trapezoid(optical[3] * Hz, z_um)
                )
    return J


def solve_point(point: ScreenPoint) -> tuple[np.ndarray, dict[str, Any]]:
    cfg = resolvent.ResolventConfig(
        diffusion_m2_s=point.diffusion_m2_s,
        lifetime_s=point.lifetime_s,
        nx=NX,
        nz=NZ,
        nx_src=NX_SRC,
    )
    gen = resolvent.build_generator(point.scenario(), cfg)
    U, diag = resolvent.solve_resolvent(gen, cfg)
    J = integrate_beam(gen, U, point.beam_sigma_um, point.beam_center_um)
    if diag["max_linear_relative_residual"] >= 1e-8:
        raise AssertionError(f"linear residual failure {point.point_id}")
    if diag["committor_relative_residual"] >= 1e-8:
        raise AssertionError(f"committor residual failure {point.point_id}")
    if np.isinf(point.lifetime_s):
        if diag["dc_committor_ramo_max_abs_error"] >= 1e-8:
            raise AssertionError(f"dc Ramo failure {point.point_id}")
    return J, diag


def reference_key(point: ScreenPoint) -> tuple[float, str, float, float]:
    return (
        point.diffusion_m2_s,
        lifetime_label(point.lifetime_s),
        point.beam_sigma_um,
        point.beam_center_um,
    )


def reference_point(point: ScreenPoint) -> ScreenPoint:
    return ScreenPoint(
        block="REF",
        point_id="REF",
        contact_fraction=1.0,
        depletion_width_um=0.0,
        space_charge_drop_v=0.0,
        diffusion_m2_s=point.diffusion_m2_s,
        lifetime_s=point.lifetime_s,
        beam_sigma_um=point.beam_sigma_um,
        beam_center_um=point.beam_center_um,
    )


def raw_phase(J: np.ndarray, kf: int) -> float:
    return float(np.degrees(base.metrics(J)[kf]["c4"].imag))


def metric_row(
    point: ScreenPoint,
    J: np.ndarray,
    Jref: np.ndarray,
    diag: dict[str, Any],
    kf: int,
) -> dict[str, Any]:
    f = float(base.FREQUENCIES[kf])
    if f <= 0:
        raise ValueError("nonzero RF only")
    y = np.asarray(J[kf], complex)
    fit = kernel.kernel_one_mode_fit(y, np.arange(len(base.DEPTHS)))
    residual = np.asarray(fit["residual"]["real"], float) + 1j * np.asarray(
        fit["residual"]["imag"], float
    )
    residual_norm = float(np.linalg.norm(residual))
    step = float(np.mean(np.abs(np.diff(y))))
    if residual_norm <= np.finfo(float).tiny:
        analytic_snr = float("inf")
    else:
        analytic_snr = float(np.sqrt(LAMBDA_REQUIRED) * step / residual_norm)
    analytic_snr_db = (
        float("inf") if not np.isfinite(analytic_snr) else float(20*np.log10(analytic_snr))
    )
    claim_snr_db = float(base.GRADIENT_SNR_DB[f])
    warning_margin = claim_snr_db - analytic_snr_db
    phase = raw_phase(J, kf)
    ref_phase = raw_phase(Jref, kf)
    target = float(base.GRADIENT_TARGET_DEG[f])
    contact_half = point.contact_fraction * base.WIDTH_UM / 2.0
    return {
        "block": point.block,
        "point_id": point.point_id,
        "frequency_hz": f,
        "contact_fraction": point.contact_fraction,
        "depletion_width_um": point.depletion_width_um,
        "depletion_fraction": point.depletion_width_um / base.L_UM,
        "space_charge_drop_v": point.space_charge_drop_v,
        "space_charge_ratio": point.space_charge_drop_v / base.V_BIAS,
        "diffusion_m2_s": point.diffusion_m2_s,
        "lifetime_s": "inf" if np.isinf(point.lifetime_s) else point.lifetime_s,
        "beam_sigma_um": point.beam_sigma_um,
        "beam_center_um": point.beam_center_um,
        "beta": point.beam_sigma_um / contact_half,
        "xi": point.beam_center_um / contact_half,
        "raw_phase_deg": phase,
        "reference_raw_phase_deg": ref_phase,
        "finite_minus_reference_phase_deg": phase - ref_phase,
        "mimic_fraction": abs((phase - ref_phase) / target),
        "rho1_all6": float(fit["contrast_normalized_residual"]),
        "one_mode_root_per_um": fit["r_per_um"],
        "one_mode_profile_condition": float(fit["profile_design_condition_number"]),
        "step_amplitude": step,
        "one_mode_residual_norm": residual_norm,
        "analytic_rejection_snr_db": analytic_snr_db,
        "transport_claim_snr_db": claim_snr_db,
        "analytic_warning_margin_db": warning_margin,
        "order_one_screen": bool(abs((phase-ref_phase)/target) >= 0.5),
        "analytic_hidden_risk_screen": bool(
            abs((phase-ref_phase)/target) >= 0.5 and warning_margin <= 0.0
        ),
        "max_linear_relative_residual": float(diag["max_linear_relative_residual"]),
        "committor_relative_residual": float(diag["committor_relative_residual"]),
        "dc_committor_ramo_max_abs_error": diag["dc_committor_ramo_max_abs_error"],
    }


def point_key_from_row(row: dict[str, Any]) -> tuple[Any, ...]:
    return (
        row["block"], row["point_id"]
    )


def lex_key(point: dict[str, Any]) -> tuple[Any, ...]:
    tau = point["lifetime_s"]
    tau_order = 1 if tau == "inf" else 0
    tau_value = float("inf") if tau == "inf" else float(tau)
    return (
        point["block"],
        point["contact_fraction"],
        point["depletion_width_um"],
        point["space_charge_drop_v"],
        point["diffusion_m2_s"],
        tau_order,
        tau_value,
        point["beam_sigma_um"],
        point["beam_center_um"],
        point["point_id"],
    )


def aggregate(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    groups: dict[tuple[Any, ...], list[dict[str, Any]]] = {}
    for row in rows:
        groups.setdefault(point_key_from_row(row), []).append(row)
    out = []
    for (_, point_id), rr in groups.items():
        rr = sorted(rr, key=lambda x: x["frequency_hz"])
        template = rr[0]
        max_m = max(rr, key=lambda x: x["mimic_fraction"])
        min_w = min(rr, key=lambda x: x["analytic_warning_margin_db"])
        max_w = max(rr, key=lambda x: x["analytic_warning_margin_db"])
        max_rho = max(rr, key=lambda x: x["rho1_all6"])
        out.append(
            {
                "block": template["block"],
                "point_id": point_id,
                "contact_fraction": template["contact_fraction"],
                "depletion_width_um": template["depletion_width_um"],
                "space_charge_drop_v": template["space_charge_drop_v"],
                "diffusion_m2_s": template["diffusion_m2_s"],
                "lifetime_s": template["lifetime_s"],
                "beam_sigma_um": template["beam_sigma_um"],
                "beam_center_um": template["beam_center_um"],
                "max_mimic_fraction": max_m["mimic_fraction"],
                "max_mimic_frequency_hz": max_m["frequency_hz"],
                "min_analytic_warning_margin_db": min_w["analytic_warning_margin_db"],
                "min_warning_frequency_hz": min_w["frequency_hz"],
                "max_analytic_warning_margin_db": max_w["analytic_warning_margin_db"],
                "max_warning_frequency_hz": max_w["frequency_hz"],
                "max_rho1_all6": max_rho["rho1_all6"],
                "max_rho_frequency_hz": max_rho["frequency_hz"],
                "has_order_one_row": bool(any(r["order_one_screen"] for r in rr)),
                "has_analytic_hidden_risk_row": bool(
                    any(r["analytic_hidden_risk_screen"] for r in rr)
                ),
            }
        )
    return sorted(out, key=lex_key)


def choose_with_ties(candidates: list[dict[str, Any]], key, reverse: bool = False):
    if not candidates:
        return None
    values = [key(x) for x in candidates]
    target = max(values) if reverse else min(values)
    tied = [x for x in candidates if np.isclose(key(x), target, rtol=1e-12, atol=1e-14)]
    return sorted(tied, key=lex_key)[0]


def select_points(points: list[dict[str, Any]], rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_id = {(p["block"], p["point_id"]): p for p in points}
    row_by_point = {}
    for r in rows:
        row_by_point.setdefault((r["block"], r["point_id"]), []).append(r)

    selected: list[dict[str, Any]] = []
    seen_coords = set()

    def coord(p):
        return (
            p["contact_fraction"], p["depletion_width_um"], p["space_charge_drop_v"],
            p["diffusion_m2_s"], p["lifetime_s"], p["beam_sigma_um"], p["beam_center_um"]
        )

    def add(reason: str, p: dict[str, Any] | None):
        if p is None:
            return
        c = coord(p)
        if c in seen_coords:
            return
        seen_coords.add(c)
        selected.append({"selection_reason": reason, **p})

    nominal_candidates = [
        p for p in points
        if p["block"] == "A"
        and p["contact_fraction"] == 0.75
        and p["depletion_width_um"] == 3.0
        and p["space_charge_drop_v"] == 0.05
        and p["diffusion_m2_s"] == 2.5e-3
        and p["lifetime_s"] == "inf"
        and p["beam_sigma_um"] == 2.0
        and p["beam_center_um"] == 0.0
    ]
    add("S0_nominal_anchor", sorted(nominal_candidates, key=lex_key)[0])

    add("S1_maximum_confound", choose_with_ties(points, lambda p: p["max_mimic_fraction"], reverse=True))

    order_rows = [r for r in rows if r["order_one_screen"]]
    if order_rows:
        worst_row = choose_with_ties(order_rows, lambda r: r["analytic_warning_margin_db"])
        add("S2_worst_warning_margin_order_one", by_id[(worst_row["block"], worst_row["point_id"])])

        boundary_row = choose_with_ties(order_rows, lambda r: abs(r["analytic_warning_margin_db"]))
        add("S3_closest_analytic_warning_boundary", by_id[(boundary_row["block"], boundary_row["point_id"])])

        strongest_row = choose_with_ties(order_rows, lambda r: r["analytic_warning_margin_db"], reverse=True)
        add("S4_strongest_early_warning_order_one", by_id[(strongest_row["block"], strongest_row["point_id"])])

    add("S5_largest_calibrated_one_mode_mismatch", choose_with_ties(points, lambda p: p["max_rho1_all6"], reverse=True))

    block_b_rows = [r for r in rows if r["block"] == "B"]
    b_order = [r for r in block_b_rows if r["order_one_screen"]]
    if b_order:
        b_row = choose_with_ties(b_order, lambda r: r["analytic_warning_margin_db"])
    else:
        b_row = choose_with_ties(block_b_rows, lambda r: r["mimic_fraction"], reverse=True)
    if b_row is not None:
        add("S6_optical_offset_stress", by_id[(b_row["block"], b_row["point_id"])])

    if order_rows:
        # Detector-point maximum mimic closest to 0.5 from above.
        eligible = [p for p in points if p["max_mimic_fraction"] >= 0.5]
        add("S7_weakest_still_order_one_confound", choose_with_ties(eligible, lambda p: p["max_mimic_fraction"] - 0.5))

    return selected[:8]


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("paper03_stageA_regime_screen.json"),
    )
    args = p.parse_args()

    screen_points = make_points()
    reference_cache: dict[tuple[float, str, float, float], tuple[np.ndarray, dict[str, Any]]] = {}
    rows: list[dict[str, Any]] = []
    point_records = []

    for i, point in enumerate(screen_points, start=1):
        print(
            f"screen {i:02d}/60 {point.block}:{point.point_id} "
            f"fc={point.contact_fraction} wd={point.depletion_width_um} "
            f"D={point.diffusion_m2_s:g} tau={lifetime_label(point.lifetime_s)} "
            f"beam=({point.beam_sigma_um},{point.beam_center_um})",
            flush=True,
        )
        J, diag = solve_point(point)
        rk = reference_key(point)
        if rk not in reference_cache:
            reference_cache[rk] = solve_point(reference_point(point))
        Jref, _ = reference_cache[rk]
        local_rows = [metric_row(point, J, Jref, diag, kf) for kf in (1, 2, 3)]
        rows.extend(local_rows)
        point_records.append(
            {
                "block": point.block,
                "point_id": point.point_id,
                "contact_fraction": point.contact_fraction,
                "depletion_width_um": point.depletion_width_um,
                "space_charge_drop_v": point.space_charge_drop_v,
                "diffusion_m2_s": point.diffusion_m2_s,
                "lifetime_s": "inf" if np.isinf(point.lifetime_s) else point.lifetime_s,
                "beam_sigma_um": point.beam_sigma_um,
                "beam_center_um": point.beam_center_um,
                "solver_diagnostics": diag,
            }
        )

    aggregated = aggregate(rows)
    selected = select_points(aggregated, rows)
    order_rows = [r for r in rows if r["order_one_screen"]]
    hidden_rows = [r for r in rows if r["analytic_hidden_risk_screen"]]

    result = {
        "schema": "paper03-stageA-regime-screen-v1",
        "status": "PREDECLARED 81x61 SCREENING / SELECTION RESULT / NON-CLAIM",
        "predeclaration": "PAPER03_STAGEA_REGIME_MAP_PREDECLARATION_2026-08-17.md",
        "numerical": {
            "grid": [NX, NZ],
            "lateral_quadrature": NX_SRC,
            "full_optical_support": True,
            "screening_only": True,
        },
        "analytic_statistical_coordinate": {
            "alpha": ALPHA,
            "target_power": TARGET_POWER,
            "regular_residual_dof": REGULAR_DOF,
            "chi_square_critical": ANALYTIC_CRITICAL,
            "required_noncentrality": LAMBDA_REQUIRED,
            "is_bootstrap": False,
        },
        "counts": {
            "declared_points": 60,
            "frequency_rows": len(rows),
            "order_one_rows": len(order_rows),
            "analytic_hidden_risk_rows": len(hidden_rows),
            "points_with_order_one_row": sum(p["has_order_one_row"] for p in aggregated),
            "points_with_analytic_hidden_risk_row": sum(
                p["has_analytic_hidden_risk_row"] for p in aggregated
            ),
        },
        "screen_points": point_records,
        "frequency_rows": rows,
        "aggregated_points": aggregated,
        "predeclared_selected_points": selected,
        "science_interpretation_ready": False,
        "next_gate": (
            "Recompute selected unique points at 161x121 and 201x151 / 17-point "
            "quadrature and apply the retained 2%-of-target refinement criterion "
            "before any Outcome-A/B interpretation."
        ),
    }

    args.output.write_text(
        json.dumps(resolvent.json_safe(result), indent=2, allow_nan=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result["counts"], indent=2))
    print("selected points:")
    print(json.dumps(selected, indent=2))
    if hidden_rows:
        print("analytic hidden-risk screening rows:")
        for r in sorted(hidden_rows, key=lambda x: x["analytic_warning_margin_db"]):
            print(
                r["block"], r["point_id"], r["frequency_hz"],
                "mimic=", f"{r['mimic_fraction']:.4g}",
                "margin=", f"{r['analytic_warning_margin_db']:.4g} dB"
            )
    print("science_interpretation_ready = false")
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
