"""Exact-planar continuum cross-check for the Paper 02 central stress.

Scientific status
-----------------
POST-HOC cross-check discovered during hostile review of Rev. 5.  This is not a
predeclared convergence gate and must never be represented as one.

Why this exists
---------------
The central Paper 02 transport stress uses a full-width collecting contact.
For that special case the physical potential is one-dimensional and has an
exact piecewise solution, while the Shockley--Ramo weighting potential is
exactly phi_w=z/L.  Therefore the central finite-kernel inference can be
recomputed without the 2-D finite-difference electrostatic mesh or trajectory
stepping used by the general geometry solver.

The script:
  1. constructs the exact planar electric field for the manuscript parameters;
  2. applies the same saturated-drift velocity law as the numerical solver;
  3. evaluates the deterministic point-source Ramo transfer by quadrature;
  4. averages the same six theoretical HgCdTe generation kernels;
  5. applies the same kernel-aware homogeneous inverse;
  6. compares the exact-continuum inference with a freshly recomputed numerical
     baseline and with the already-declared numerical-convergence tolerances;
  7. reports exact upstream and inside-region point-source controls.

Agreement with the old tolerances is a convenient scale test only.  Since this
cross-check was designed after the mesh-refinement result was known, its status
is explicitly post-hoc regardless of whether all comparisons pass.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from scipy.integrate import cumulative_trapezoid

import realistic_geometry_closure_stress as base
from paper02_geometry_factorial_decomposition import best_rank_one
import paper02_inference_convergence_gate as gate
import paper02_kernel_aware_depletion_frequency_law as law


L_M = base.L_UM * 1e-6
WD_M = 3.0e-6
A_M = L_M - WD_M
V_BIAS = 0.30
DELTA_V = 0.05
MU = base.MU
V_SAT = base.V_SAT

OUTSIDE_DEPTHS_UM = gate.OUTSIDE_DEPTHS_UM
INSIDE_DEPTHS_UM = gate.INSIDE_DEPTHS_UM


def exact_field_v_per_m(z_m: np.ndarray) -> np.ndarray:
    """Exact positive dV/dz for the full-contact planar continuum solution."""
    z_m = np.asarray(z_m, dtype=float)
    slope = (V_BIAS - DELTA_V) / L_M
    return slope + (2.0 * DELTA_V / WD_M**2) * np.maximum(z_m - A_M, 0.0)


def exact_speed_m_per_s(z_m: np.ndarray) -> np.ndarray:
    E = exact_field_v_per_m(z_m)
    v0 = MU * E
    return v0 / np.sqrt(1.0 + (v0 / V_SAT) ** 2)


def _remaining_integral(y: np.ndarray, x: np.ndarray) -> np.ndarray:
    c = np.concatenate(([0.0 + 0.0j], cumulative_trapezoid(y, x)))
    return c[-1] - c


def exact_point_transfer(z_m: np.ndarray, frequencies_hz: np.ndarray) -> np.ndarray:
    """Return H[f,z] for deterministic planar Shockley--Ramo collection."""
    v = exact_speed_m_per_s(z_m)
    travel = np.concatenate(([0.0], cumulative_trapezoid(1.0 / v, z_m)))
    out = np.empty((len(frequencies_hz), len(z_m)), dtype=complex)

    for jf, f in enumerate(frequencies_hz):
        omega = 2.0 * np.pi * float(f)
        if f == 0.0:
            out[jf] = (L_M - z_m) / L_M
            continue
        phase = np.exp(-1j * omega * travel)
        rem = _remaining_integral(phase, z_m)
        out[jf] = np.exp(1j * omega * travel) * rem / L_M

    return out


def exact_channel_currents(point_transfer: np.ndarray) -> np.ndarray:
    z_um = base.OPT_Z_UM
    return np.asarray(
        [
            [np.trapezoid(opt[3] * point_transfer[jf], z_um) for opt in base.OPTICS]
            for jf in range(point_transfer.shape[0])
        ],
        dtype=complex,
    )


def infer_finite_kernel(J: np.ndarray):
    gammas = []
    fit_rel = []
    for jf, _f in enumerate(law.FREQUENCIES):
        r, _coeff, _model, rel = law.kernel_aware_root(J[jf])
        gammas.append(-r)
        fit_rel.append(float(rel))
    gammas = np.asarray(gammas, dtype=complex)
    fit_rel = np.asarray(fit_rel, dtype=float)

    probe = {}
    for f in gate.PROBE_FREQUENCIES_HZ:
        idx = gate._frequency_index(law.FREQUENCIES, f)
        D, w = law.solve_dw_one_frequency(gammas[idx], f)
        probe[str(int(f))] = {
            "D_eff_m2_per_s": float(D),
            "w_eff_m_per_s": float(w),
            "gamma_real_per_m": float(gammas[idx].real),
            "gamma_imag_per_m": float(gammas[idx].imag),
            "kernel_fit_rel": float(fit_rel[idx]),
        }

    D_low, w_low = law.solve_dw_low_band(gammas, law.FREQUENCIES)
    p100 = probe[str(int(100e6))]
    _e, residual_1ghz = law.law_residual(
        gammas[gate._frequency_index(law.FREQUENCIES, 1e9)],
        1e9,
        p100["D_eff_m2_per_s"],
        p100["w_eff_m_per_s"],
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
            "max_kernel_fit_rel_through_1ghz": float(
                np.max(fit_rel[law.FREQUENCIES <= 1e9])
            ),
        },
    }


def infer_point_sequence(point_transfer: np.ndarray, depths_um: np.ndarray):
    idx100 = gate._frequency_index(law.FREQUENCIES, 100e6)
    J = np.asarray(
        [
            np.interp(depths_um, base.OPT_Z_UM, point_transfer[jf])
            for jf in range(len(law.FREQUENCIES))
        ],
        dtype=complex,
    )
    _A, q, _model, fit_rel = best_rank_one(np.diff(J[idx100]))
    gamma = -np.log(q) / gate.H_M
    D, w = law.solve_dw_one_frequency(gamma, 100e6)
    return {
        "D_eff_m2_per_s": float(D),
        "w_eff_m_per_s": float(w),
        "gamma_real_per_m": float(gamma.real),
        "gamma_imag_per_m": float(gamma.imag),
        "rank1_fit_rel": float(fit_rel),
    }


def rel_change(numerical: float, exact: float, floor: float = 1e-30) -> float:
    return float(abs(numerical - exact) / max(abs(exact), floor))


def build_comparison(numerical, exact):
    rows = []
    overall = True

    for f_mhz in (100, 500, 1000):
        key = str(int(f_mhz * 1e6))
        for quantity, tol_key in (
            ("D_eff_m2_per_s", "D_eff_probe_relative"),
            ("w_eff_m_per_s", "w_eff_probe_relative"),
        ):
            n = numerical["probe"][key][quantity]
            e = exact["probe"][key][quantity]
            change = rel_change(n, e)
            tol = float(gate.TOLERANCES[tol_key])
            passed = bool(change <= tol)
            overall = overall and passed
            rows.append(
                {
                    "metric": f"{quantity}_{f_mhz}MHz",
                    "numerical_baseline": float(n),
                    "exact_continuum": float(e),
                    "relative_difference": change,
                    "comparison_tolerance": tol,
                    "pass_against_existing_tolerance": passed,
                }
            )

    for quantity, tol_key in (
        ("D_eff_m2_per_s", "low_band_D_relative"),
        ("w_eff_m_per_s", "low_band_w_relative"),
    ):
        n = numerical["low_band"][quantity]
        e = exact["low_band"][quantity]
        change = rel_change(n, e)
        tol = float(gate.TOLERANCES[tol_key])
        passed = bool(change <= tol)
        overall = overall and passed
        rows.append(
            {
                "metric": f"low_band_{quantity}",
                "numerical_baseline": float(n),
                "exact_continuum": float(e),
                "relative_difference": change,
                "comparison_tolerance": tol,
                "pass_against_existing_tolerance": passed,
            }
        )

    n = numerical["frequency_law"]["relative_residual_1ghz"]
    e = exact["frequency_law"]["relative_residual_1ghz"]
    change = float(abs(n - e))
    tol = float(gate.TOLERANCES["law_residual_1ghz_absolute"])
    passed = bool(change <= tol)
    overall = overall and passed
    rows.append(
        {
            "metric": "law_residual_1ghz",
            "numerical_baseline": float(n),
            "exact_continuum": float(e),
            "absolute_difference": change,
            "comparison_tolerance": tol,
            "pass_against_existing_tolerance": passed,
        }
    )

    n = numerical["frequency_law"]["max_kernel_fit_rel_through_1ghz"]
    e = exact["frequency_law"]["max_kernel_fit_rel_through_1ghz"]
    change = float(abs(n - e))
    tol = float(gate.TOLERANCES["max_kernel_fit_through_1ghz_absolute"])
    passed = bool(change <= tol)
    overall = overall and passed
    rows.append(
        {
            "metric": "max_kernel_fit_rel_through_1ghz",
            "numerical_baseline": float(n),
            "exact_continuum": float(e),
            "absolute_difference": change,
            "comparison_tolerance": tol,
            "pass_against_existing_tolerance": passed,
        }
    )

    return rows, bool(overall)


def write_markdown(payload, path: Path):
    exact = payload["exact_continuum"]
    comp = payload["comparison"]
    lines = [
        "# Paper 02 exact planar continuum cross-check",
        "",
        "**Status:** **CHECKED POST-HOC EXACT-CONTINUUM CROSS-CHECK**" if comp["overall_pass_against_existing_tolerances"] else "**Status:** **POST-HOC CROSS-CHECK FAILED EXISTING NUMERICAL TOLERANCE SCALE**",
        "",
        "> This check was designed after the mesh-refinement result was known. It is therefore post-hoc and is not represented as a predeclared convergence gate.",
        "",
        "The full-contact central stress has an exact one-dimensional electrostatic solution and planar weighting potential. This calculation removes the 2-D field mesh and trajectory stepping from the central inference and then applies the same six optical kernels and kernel-aware inverse.",
        "",
        "## Exact-continuum inference",
        "",
        "| RF | D_eff (m^2/s) | w_eff (m/s) | kernel-fit residual |",
        "|---:|---:|---:|---:|",
    ]
    for f_mhz in (100, 500, 1000):
        r = exact["probe"][str(int(f_mhz * 1e6))]
        lines.append(
            f"| {f_mhz} MHz | {r['D_eff_m2_per_s']:.9e} | {r['w_eff_m_per_s']:.6f} | {r['kernel_fit_rel']:.9e} |"
        )
    lines += [
        "",
        f"Low-band joint fit: `D={exact['low_band']['D_eff_m2_per_s']:.9e} m^2/s`, `w={exact['low_band']['w_eff_m_per_s']:.6f} m/s`.",
        "",
        f"100-MHz-anchored homogeneous-law residual at 1 GHz: `{exact['frequency_law']['relative_residual_1ghz']:.9e}`.",
        "",
        "## Numerical baseline versus exact continuum",
        "",
        "| Metric | Numerical baseline | Exact continuum | Difference | Existing tolerance scale | Pass |",
        "|---|---:|---:|---:|---:|:---:|",
    ]
    for row in comp["rows"]:
        diff = row.get("relative_difference", row.get("absolute_difference"))
        mode = "rel" if "relative_difference" in row else "abs"
        lines.append(
            f"| {row['metric']} | {row['numerical_baseline']:.9e} | {row['exact_continuum']:.9e} | {diff:.9e} ({mode}) | {row['comparison_tolerance']:.9e} | {'PASS' if row['pass_against_existing_tolerance'] else 'FAIL'} |"
        )
    lines += [
        "",
        "## Exact point-source controls",
        "",
        f"Upstream sequence: `D_eff={payload['point_controls']['outside_depletion']['D_eff_m2_per_s']:.9e} m^2/s`.",
        "",
        f"Inside-region sequence: `D_eff={payload['point_controls']['inside_depletion']['D_eff_m2_per_s']:.9e} m^2/s`.",
        "",
        "## Interpretation",
        "",
        "Agreement here strengthens numerical attribution inside the declared deterministic surrogate. It does not establish experimental kernel calibration, device-level uniqueness, experimental feasibility, or novelty priority.",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def run(args):
    z_m = base.OPT_Z_UM * 1e-6
    point = exact_point_transfer(z_m, law.FREQUENCIES)
    channels = exact_channel_currents(point)
    exact = infer_finite_kernel(channels)

    # Freshly recompute the same numerical baseline used by the convergence gate.
    numerical = gate._finite_kernel_metrics(gate.BASELINE)
    rows, overall = build_comparison(numerical, exact)

    point_controls = {
        "outside_depletion": infer_point_sequence(point, OUTSIDE_DEPTHS_UM),
        "inside_depletion": infer_point_sequence(point, INSIDE_DEPTHS_UM),
    }

    payload = {
        "status": "CHECKED POST-HOC exact planar continuum cross-check" if overall else "POST-HOC exact planar continuum cross-check outside existing tolerance scale",
        "epistemic_note": "Designed after the numerical mesh-refinement result was known; not a predeclared convergence gate.",
        "model_truth": {
            "microscopic_diffusion_m2_per_s": 0.0,
            "recombination": 0.0,
            "full_contact_planar_weighting_potential": True,
            "absorber_thickness_um": float(base.L_UM),
            "depletion_width_um": 3.0,
            "bias_v": V_BIAS,
            "poisson_curvature_parameter_delta_v": DELTA_V,
            "mobility_m2_per_v_s": float(MU),
            "v_sat_m_per_s": float(V_SAT),
        },
        "exact_field": {
            "upstream_field_v_per_cm": float(exact_field_v_per_m(np.asarray([0.0]))[0] / 100.0),
            "collector_edge_field_v_per_cm": float(exact_field_v_per_m(np.asarray([L_M]))[0] / 100.0),
            "characteristic_curvature_field_v_per_cm": float((DELTA_V / WD_M) / 100.0),
        },
        "exact_continuum": exact,
        "numerical_baseline": numerical,
        "comparison": {
            "basis": "Existing predeclared numerical-convergence tolerance scales reused only as post-hoc agreement scales.",
            "rows": rows,
            "overall_pass_against_existing_tolerances": overall,
        },
        "point_controls": point_controls,
    }

    out_json = Path(args.output_json)
    out_md = Path(args.output_markdown)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
    write_markdown(payload, out_md)

    print(json.dumps(payload, indent=2, sort_keys=True))
    if not overall:
        raise SystemExit("Exact-continuum comparison exceeded an existing numerical-convergence tolerance scale")


def parser():
    p = argparse.ArgumentParser()
    p.add_argument(
        "--output-json",
        default="results/paper02_exact_planar_continuum_crosscheck_summary.json",
    )
    p.add_argument(
        "--output-markdown",
        default="results/PAPER02_EXACT_PLANAR_CONTINUUM_CROSSCHECK.md",
    )
    return p


if __name__ == "__main__":
    run(parser().parse_args())
