"""Numerical convergence gate for the Paper 02 inferential chain.

The original geometry stress test checked convergence of the four-color closure
phase after changing several numerical controls at once.  Paper 02 now makes a
stronger and more nonlinear statement: a deterministic depletion-field model
with microscopic D=0 can produce a positive kernel-aware effective diffusion
coefficient D_eff when interpreted through a homogeneous drift-diffusion law.
The relevant numerical object to converge is therefore the *inference*, not
only the raw closure phase.

This script perturbs the three dominant numerical controls independently:

1. 2-D electrostatic / weighting-potential mesh (nx, nz),
2. source / optical-kernel quadrature (nx_src, nz_src), and
3. trajectory integration step ds.

Seven unique configurations are evaluated: one shared baseline plus a coarser
and finer setting on each axis.  For every configuration the script executes
the same finite-kernel inverse used by
paper02_kernel_aware_depletion_frequency_law.py and records

- same-frequency D_eff and w_eff at 100, 500, and 1000 MHz,
- the low-band joint D,w fit,
- the 100-MHz-anchored law residual at 1 GHz,
- the maximum one-mode kernel fit residual through 1 GHz,
- outside-depletion and inside-depletion point-source causal controls,
- collection and DC Shockley-Ramo diagnostics.

A convergence decision is based on the baseline-to-fine change for each axis.
The coarse-to-baseline change is retained as a trend diagnostic but is not used
as a hard pass criterion because non-monotone cancellation can occur in a
multistage inverse.  The tolerances are declared in this file and written to the
JSON output.  They are numerical reproducibility tolerances, not experimental
uncertainties and not device-calibration claims.

Scientific status: CHECKED only after this script has executed successfully and
the generated JSON reports overall_pass=true.  Merely committing this script is
not numerical evidence.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import asdict, dataclass, replace
import json
from pathlib import Path
import sys

import numpy as np

import realistic_geometry_closure_stress as base
import paper02_geometry_parameter_sweep as sweep
from paper02_geometry_factorial_decomposition import best_rank_one
import paper02_kernel_aware_depletion_frequency_law as law


PROBE_FREQUENCIES_HZ = (100e6, 500e6, 1e9)
CAUSAL_FREQUENCIES_HZ = np.asarray((0.0, 100e6), dtype=float)
OUTSIDE_DEPTHS_UM = np.arange(2.0, 4.51, 0.5)
INSIDE_DEPTHS_UM = np.arange(4.8, 7.31, 0.5)
H_M = 0.5e-6


@dataclass(frozen=True)
class NumericalConfig:
    nx: int = 121
    nz: int = 91
    nx_src: int = 13
    nz_src: int = 41
    ds_um: float = 0.020


BASELINE = NumericalConfig()
CONFIGS = {
    "baseline": BASELINE,
    "mesh_coarse": replace(BASELINE, nx=81, nz=61),
    "mesh_fine": replace(BASELINE, nx=161, nz=121),
    "quadrature_coarse": replace(BASELINE, nx_src=9, nz_src=31),
    "quadrature_fine": replace(BASELINE, nx_src=17, nz_src=61),
    "step_coarse": replace(BASELINE, ds_um=0.035),
    "step_fine": replace(BASELINE, ds_um=0.0125),
}

AXES = {
    "field_mesh": ("mesh_coarse", "baseline", "mesh_fine"),
    "source_quadrature": ("quadrature_coarse", "baseline", "quadrature_fine"),
    "trajectory_step": ("step_coarse", "baseline", "step_fine"),
}

# These tolerances apply to the final refinement step (baseline -> fine).
# Relative tolerances are dimensionless fractions, not percentages.
TOLERANCES = {
    "D_eff_probe_relative": 0.020,
    "w_eff_probe_relative": 0.005,
    "low_band_D_relative": 0.020,
    "low_band_w_relative": 0.005,
    "law_residual_1ghz_absolute": 0.002,
    "max_kernel_fit_through_1ghz_absolute": 2.0e-5,
    "outside_point_D_change_over_finite_D100": 0.010,
    "inside_point_D_relative": 0.020,
    "dc_ramo_error_absolute_max": 1.0e-10,
    "minimum_collection_fraction": 0.999,
}


def _config_kwargs(cfg: NumericalConfig):
    return {
        "nx": cfg.nx,
        "nz": cfg.nz,
        "nx_src": cfg.nx_src,
        "nz_src": cfg.nz_src,
        "ds_um": cfg.ds_um,
    }


def _frequency_index(freqs: np.ndarray, target_hz: float) -> int:
    idx = np.where(np.isclose(freqs, target_hz, rtol=0.0, atol=1.0))[0]
    if len(idx) != 1:
        raise RuntimeError(f"frequency {target_hz:g} Hz is not uniquely present")
    return int(idx[0])


def _finite_kernel_metrics(cfg: NumericalConfig):
    old_frequencies = base.FREQUENCIES
    old_bias = base.V_BIAS
    old_extent = base.X_EXTENT_UM
    base.FREQUENCIES = law.FREQUENCIES.copy()
    base.V_BIAS = 0.30
    base.X_EXTENT_UM = 3.5

    depleted = base.Scenario("planar_depletion", 1.0, 3.0, 0.05)
    try:
        J, diag = sweep.currents_with_beam(
            depleted,
            2.0,
            0.0,
            **_config_kwargs(cfg),
        )
    finally:
        base.FREQUENCIES = old_frequencies
        base.V_BIAS = old_bias
        base.X_EXTENT_UM = old_extent

    gammas = []
    kernel_fit_rel = []
    for jf, _f in enumerate(law.FREQUENCIES):
        r, _coeff, _model, fit_rel = law.kernel_aware_root(J[jf])
        gammas.append(-r)
        kernel_fit_rel.append(float(fit_rel))
    gammas = np.asarray(gammas, dtype=complex)
    kernel_fit_rel = np.asarray(kernel_fit_rel, dtype=float)

    probe = {}
    for f in PROBE_FREQUENCIES_HZ:
        idx = _frequency_index(law.FREQUENCIES, f)
        D, w = law.solve_dw_one_frequency(gammas[idx], f)
        probe[str(int(f))] = {
            "D_eff_m2_per_s": D,
            "w_eff_m_per_s": w,
            "gamma_real_per_m": float(gammas[idx].real),
            "gamma_imag_per_m": float(gammas[idx].imag),
            "kernel_fit_rel": float(kernel_fit_rel[idx]),
        }

    D_low, w_low = law.solve_dw_low_band(gammas, law.FREQUENCIES)
    idx100 = _frequency_index(law.FREQUENCIES, 100e6)
    D100 = probe[str(int(100e6))]["D_eff_m2_per_s"]
    w100 = probe[str(int(100e6))]["w_eff_m_per_s"]

    law_residuals = []
    for gamma, f in zip(gammas, law.FREQUENCIES):
        if f <= 0:
            continue
        _e, rel = law.law_residual(gamma, float(f), D100, w100)
        law_residuals.append((float(f), float(rel)))

    residual_1ghz = next(rel for f, rel in law_residuals if f == 1e9)
    max_law_through_1ghz = max(rel for f, rel in law_residuals if f <= 1e9)
    max_kernel_fit_through_1ghz = float(
        np.max(kernel_fit_rel[law.FREQUENCIES <= 1e9])
    )

    return {
        "probe": probe,
        "low_band": {
            "D_eff_m2_per_s": float(D_low),
            "w_eff_m_per_s": float(w_low),
        },
        "frequency_law": {
            "anchored_at_hz": 100e6,
            "relative_residual_1ghz": float(residual_1ghz),
            "max_relative_residual_through_1ghz": float(max_law_through_1ghz),
            "max_kernel_fit_rel_through_1ghz": max_kernel_fit_through_1ghz,
        },
        "diagnostics": {
            "collection_fraction": float(diag["collected"]),
            "dc_ramo_error": float(diag["dc_error"]),
            "max_trajectory_ps": float(1e12 * diag["tmax_s"]),
        },
    }


def _point_sequence(g, depths_um, ds_um):
    J = np.zeros((len(CAUSAL_FREQUENCIES_HZ), len(depths_um)), dtype=complex)
    reached = []
    dc_error = 0.0
    for m, z0 in enumerate(depths_um):
        H, _t, ok, phi0 = base.trajectory(g, 0.0, float(z0), ds_um)
        J[:, m] = H
        reached.append(bool(ok))
        dc_error = max(dc_error, abs(H[0].real - (1.0 - phi0)))
    return J, all(reached), float(dc_error)


def _point_D100(J):
    jf = 1  # [0, 100 MHz]
    _A, q, _model, fit_rel = best_rank_one(np.diff(J[jf]))
    gamma = -np.log(q) / H_M
    D, w = law.solve_dw_one_frequency(gamma, 100e6)
    return {
        "D_eff_m2_per_s": float(D),
        "w_eff_m_per_s": float(w),
        "rank1_fit_rel": float(fit_rel),
        "gamma_real_per_m": float(gamma.real),
        "gamma_imag_per_m": float(gamma.imag),
    }


def _causal_point_metrics(cfg: NumericalConfig):
    """Point controls depend only on mesh and ds, not source quadrature."""
    old_frequencies = base.FREQUENCIES
    old_bias = base.V_BIAS
    base.FREQUENCIES = CAUSAL_FREQUENCIES_HZ.copy()
    base.V_BIAS = 0.30
    depleted = base.Scenario("planar_depletion", 1.0, 3.0, 0.05)
    try:
        g = base.geometry(depleted, cfg.nx, cfg.nz)
        J_out, reached_out, dc_out = _point_sequence(
            g, OUTSIDE_DEPTHS_UM, cfg.ds_um
        )
        J_in, reached_in, dc_in = _point_sequence(
            g, INSIDE_DEPTHS_UM, cfg.ds_um
        )
    finally:
        base.FREQUENCIES = old_frequencies
        base.V_BIAS = old_bias

    return {
        "outside_depletion": {
            **_point_D100(J_out),
            "all_trajectories_reached": bool(reached_out),
            "dc_ramo_error": dc_out,
        },
        "inside_depletion": {
            **_point_D100(J_in),
            "all_trajectories_reached": bool(reached_in),
            "dc_ramo_error": dc_in,
        },
    }


def evaluate_config(cfg: NumericalConfig, point_cache):
    finite = _finite_kernel_metrics(cfg)
    cache_key = (cfg.nx, cfg.nz, cfg.ds_um)
    if cache_key not in point_cache:
        point_cache[cache_key] = _causal_point_metrics(cfg)
    point = point_cache[cache_key]

    D100 = finite["probe"][str(int(100e6))]["D_eff_m2_per_s"]
    denom = max(abs(D100), 1e-30)
    point = json.loads(json.dumps(point))  # detach cached object before annotation
    point["outside_depletion"]["abs_D_over_finite_kernel_D100"] = (
        abs(point["outside_depletion"]["D_eff_m2_per_s"]) / denom
    )
    point["inside_depletion"]["D_over_finite_kernel_D100"] = (
        point["inside_depletion"]["D_eff_m2_per_s"] / denom
    )

    return {
        "numerical": asdict(cfg),
        "finite_kernel": finite,
        "causal_point_controls": point,
    }


def _rel_change(a, b, floor=1e-30):
    return float(abs(b - a) / max(abs(b), floor))


def _abs_change(a, b):
    return float(abs(b - a))


def _metric_value(result, name):
    fk = result["finite_kernel"]
    cp = result["causal_point_controls"]
    if name.startswith("D_"):
        f = int(name.split("_")[1]) * 1e6
        return fk["probe"][str(int(f))]["D_eff_m2_per_s"]
    if name.startswith("w_"):
        f = int(name.split("_")[1]) * 1e6
        return fk["probe"][str(int(f))]["w_eff_m_per_s"]
    table = {
        "D_low": fk["low_band"]["D_eff_m2_per_s"],
        "w_low": fk["low_band"]["w_eff_m_per_s"],
        "law_residual_1ghz": fk["frequency_law"]["relative_residual_1ghz"],
        "max_kernel_fit_1ghz": fk["frequency_law"]["max_kernel_fit_rel_through_1ghz"],
        "D_out": cp["outside_depletion"]["D_eff_m2_per_s"],
        "D_in": cp["inside_depletion"]["D_eff_m2_per_s"],
    }
    return float(table[name])


def _comparison_rule(metric, medium_result, fine_result):
    if metric.startswith("D_") and metric not in ("D_low", "D_out", "D_in"):
        return "relative", TOLERANCES["D_eff_probe_relative"], None
    if metric.startswith("w_") and metric != "w_low":
        return "relative", TOLERANCES["w_eff_probe_relative"], None
    if metric == "D_low":
        return "relative", TOLERANCES["low_band_D_relative"], None
    if metric == "w_low":
        return "relative", TOLERANCES["low_band_w_relative"], None
    if metric == "law_residual_1ghz":
        return "absolute", TOLERANCES["law_residual_1ghz_absolute"], None
    if metric == "max_kernel_fit_1ghz":
        return "absolute", TOLERANCES["max_kernel_fit_through_1ghz_absolute"], None
    if metric == "D_out":
        D100 = abs(
            fine_result["finite_kernel"]["probe"][str(int(100e6))][
                "D_eff_m2_per_s"
            ]
        )
        return (
            "scaled_absolute",
            TOLERANCES["outside_point_D_change_over_finite_D100"],
            max(D100, 1e-30),
        )
    if metric == "D_in":
        return "relative", TOLERANCES["inside_point_D_relative"], None
    raise KeyError(metric)


def _change(a, b, mode, scale=None):
    if mode == "relative":
        return _rel_change(a, b)
    if mode == "absolute":
        return _abs_change(a, b)
    if mode == "scaled_absolute":
        return _abs_change(a, b) / float(scale)
    raise KeyError(mode)


def build_convergence(results):
    metrics = [
        "D_100",
        "D_500",
        "D_1000",
        "w_100",
        "w_500",
        "w_1000",
        "D_low",
        "w_low",
        "law_residual_1ghz",
        "max_kernel_fit_1ghz",
        "D_out",
        "D_in",
    ]
    axes_out = {}
    all_checks = []

    for axis, (coarse_name, medium_name, fine_name) in AXES.items():
        coarse = results[coarse_name]
        medium = results[medium_name]
        fine = results[fine_name]
        rows = []
        for metric in metrics:
            a = _metric_value(coarse, metric)
            b = _metric_value(medium, metric)
            c = _metric_value(fine, metric)
            mode, tol, scale = _comparison_rule(metric, medium, fine)
            coarse_change = _change(a, b, mode, scale)
            fine_change = _change(b, c, mode, scale)
            passed = bool(np.isfinite(fine_change) and fine_change <= tol)
            trend_improved = bool(
                np.isfinite(coarse_change)
                and np.isfinite(fine_change)
                and fine_change <= coarse_change
            )
            row = {
                "metric": metric,
                "coarse": float(a),
                "baseline": float(b),
                "fine": float(c),
                "change_mode": mode,
                "coarse_to_baseline_change": float(coarse_change),
                "baseline_to_fine_change": float(fine_change),
                "tolerance": float(tol),
                "pass": passed,
                "refinement_trend_improved": trend_improved,
            }
            rows.append(row)
            all_checks.append((axis, metric, passed))
        axes_out[axis] = rows

    integrity = []
    for name, r in results.items():
        fkdiag = r["finite_kernel"]["diagnostics"]
        cp = r["causal_point_controls"]
        checks = {
            "finite_kernel_collection": bool(
                fkdiag["collection_fraction"]
                >= TOLERANCES["minimum_collection_fraction"]
            ),
            "finite_kernel_dc_ramo": bool(
                fkdiag["dc_ramo_error"]
                <= TOLERANCES["dc_ramo_error_absolute_max"]
            ),
            "outside_points_reached": bool(
                cp["outside_depletion"]["all_trajectories_reached"]
            ),
            "inside_points_reached": bool(
                cp["inside_depletion"]["all_trajectories_reached"]
            ),
            "outside_point_dc_ramo": bool(
                cp["outside_depletion"]["dc_ramo_error"]
                <= TOLERANCES["dc_ramo_error_absolute_max"]
            ),
            "inside_point_dc_ramo": bool(
                cp["inside_depletion"]["dc_ramo_error"]
                <= TOLERANCES["dc_ramo_error_absolute_max"]
            ),
        }
        integrity.append(
            {
                "configuration": name,
                "checks": checks,
                "pass": all(checks.values()),
            }
        )

    # The sign stability is scientifically relevant because Paper 02's
    # confound is specifically a positive inferred D from microscopic D=0.
    sign_checks = []
    for axis, (_coarse, medium_name, fine_name) in AXES.items():
        medium = results[medium_name]
        fine = results[fine_name]
        for metric in ("D_100", "D_500", "D_1000", "D_in"):
            b = _metric_value(medium, metric)
            c = _metric_value(fine, metric)
            sign_checks.append(
                {
                    "axis": axis,
                    "metric": metric,
                    "baseline_positive": bool(b > 0),
                    "fine_positive": bool(c > 0),
                    "pass": bool(b > 0 and c > 0),
                }
            )

    overall = bool(
        all(p for _a, _m, p in all_checks)
        and all(x["pass"] for x in integrity)
        and all(x["pass"] for x in sign_checks)
    )
    return {
        "axes": axes_out,
        "integrity": integrity,
        "positive_D_sign_stability": sign_checks,
        "overall_pass": overall,
    }


def write_csv(path: Path, convergence):
    rows = []
    for axis, axis_rows in convergence["axes"].items():
        for row in axis_rows:
            rows.append({"axis": axis, **row})
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


def write_markdown(path: Path, payload):
    lines = [
        "# Paper 02 inference convergence gate",
        "",
        f"**Overall:** {'PASS' if payload['convergence']['overall_pass'] else 'FAIL'}",
        "",
        "This report tests numerical convergence of the inferred transport quantities, not only the raw closure phase.",
        "",
    ]
    for axis, rows in payload["convergence"]["axes"].items():
        lines += [
            f"## {axis.replace('_', ' ').title()}",
            "",
            "| Metric | Coarse | Baseline | Fine | Final change | Tolerance | Gate |",
            "|---|---:|---:|---:|---:|---:|:---:|",
        ]
        for r in rows:
            lines.append(
                f"| {r['metric']} | {r['coarse']:.8g} | {r['baseline']:.8g} | "
                f"{r['fine']:.8g} | {r['baseline_to_fine_change']:.3g} | "
                f"{r['tolerance']:.3g} | {'PASS' if r['pass'] else 'FAIL'} |"
            )
        lines.append("")

    lines += ["## Integrity checks", ""]
    for row in payload["convergence"]["integrity"]:
        failed = [k for k, v in row["checks"].items() if not v]
        lines.append(
            f"- **{row['configuration']}**: "
            + ("PASS" if not failed else "FAIL: " + ", ".join(failed))
        )
    lines += [
        "",
        "## Interpretation boundary",
        "",
        "A PASS establishes numerical stability of this deterministic surrogate and its inverse under the declared refinement tests. It does not establish experimental feasibility, device calibration, or uniqueness of the physical interpretation.",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def parser():
    p = argparse.ArgumentParser()
    p.add_argument(
        "--output-summary",
        default="results/paper02_inference_convergence_summary.json",
    )
    p.add_argument(
        "--output-csv",
        default="results/paper02_inference_convergence.csv",
    )
    p.add_argument(
        "--output-markdown",
        default="results/PAPER02_INFERENCE_CONVERGENCE.md",
    )
    p.add_argument(
        "--no-fail",
        action="store_true",
        help="write all diagnostics but return success even if a gate fails",
    )
    return p


def main():
    args = parser().parse_args()
    point_cache = {}
    results = {}
    for name, cfg in CONFIGS.items():
        print(f"[paper02 convergence] evaluating {name}: {cfg}", flush=True)
        results[name] = evaluate_config(cfg, point_cache)

    convergence = build_convergence(results)
    payload = {
        "status": (
            "CHECKED numerical convergence gate passed"
            if convergence["overall_pass"]
            else "OPEN numerical convergence gate failed"
        ),
        "model_scope": {
            "microscopic_diffusion_m2_per_s": 0.0,
            "recombination": 0.0,
            "contact_fraction": 1.0,
            "depletion_width_um": 3.0,
            "space_charge_drop_v": 0.05,
            "bias_v": 0.30,
            "kernel_status": "theoretical wavelength-dependent generation kernels supplied exactly to the inverse",
        },
        "baseline": asdict(BASELINE),
        "configurations": {k: asdict(v) for k, v in CONFIGS.items()},
        "tolerances": TOLERANCES,
        "results": results,
        "convergence": convergence,
    }

    out_json = Path(args.output_summary)
    out_csv = Path(args.output_csv)
    out_md = Path(args.output_markdown)
    for p in (out_json, out_csv, out_md):
        p.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
    write_csv(out_csv, convergence)
    write_markdown(out_md, payload)

    print(json.dumps({
        "status": payload["status"],
        "overall_pass": convergence["overall_pass"],
        "summary": str(out_json),
        "csv": str(out_csv),
        "markdown": str(out_md),
    }, indent=2))

    if not convergence["overall_pass"] and not args.no_fail:
        sys.exit(2)


if __name__ == "__main__":
    main()
