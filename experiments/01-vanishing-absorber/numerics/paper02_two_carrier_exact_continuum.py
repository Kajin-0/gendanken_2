"""Exact-planar two-carrier closure stress for Paper 02 Rev. 8.

This script responds to the carrier-species issue recorded in
PAPER02_TWO_CARRIER_GATE_2026-08-16.md.  It intentionally reuses the frozen
Rev. 7 exact-planar downstream transfer and optical kernels.

A complete planar electron-hole pair contains two source-coordinate modes even
when both velocities are spatially uniform.  Therefore the pair signal is fit
with a two-root finite-kernel model

    J_m = C + K_d F_m(r_d) + K_u F_m(r_u)

rather than forcing it through the Rev. 7 one-root inverse.  The first hard
control is a uniform-pair null.  Only if that null is recovered accurately is
the heterogeneous downstream-carrier result interpreted.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np
from scipy.optimize import least_squares

import realistic_geometry_closure_stress as base
import paper02_exact_planar_continuum_crosscheck as exact
import paper02_kernel_aware_depletion_frequency_law as law


PROBE_FREQUENCIES = np.asarray((100e6, 500e6, 1e9), dtype=float)
SPEED_RATIOS = np.asarray((0.05, 0.10, 0.25, 0.50, 1.0, 2.0, 4.0, 10.0, 20.0))
CORE_MIN_RATIO = 0.10
CORE_MAX_RATIO = 10.0
DC_TOL = 1e-12
UNIFORM_CENTERED_REL_TOL = 1e-8
UNIFORM_D_TOL = 1e-7
ROOT_SCALE_M = 1e-6


def uniform_down_transfer(z_m: np.ndarray, frequencies_hz: np.ndarray, v_m_per_s: float) -> np.ndarray:
    """Downstream carrier, z -> L, uniform positive speed magnitude."""
    z_m = np.asarray(z_m, dtype=float)
    out = np.empty((len(frequencies_hz), len(z_m)), dtype=complex)
    for jf, f in enumerate(frequencies_hz):
        if f == 0.0:
            out[jf] = (exact.L_M - z_m) / exact.L_M
            continue
        omega = 2.0 * np.pi * float(f)
        out[jf] = (v_m_per_s / (1j * omega * exact.L_M)) * (
            1.0 - np.exp(-1j * omega * (exact.L_M - z_m) / v_m_per_s)
        )
    return out


def uniform_up_transfer(z_m: np.ndarray, frequencies_hz: np.ndarray, v_m_per_s: float) -> np.ndarray:
    """Counterpropagating carrier, z -> 0, with polarity chosen to add induced current."""
    z_m = np.asarray(z_m, dtype=float)
    out = np.empty((len(frequencies_hz), len(z_m)), dtype=complex)
    for jf, f in enumerate(frequencies_hz):
        if f == 0.0:
            out[jf] = z_m / exact.L_M
            continue
        omega = 2.0 * np.pi * float(f)
        out[jf] = (v_m_per_s / (1j * omega * exact.L_M)) * (
            1.0 - np.exp(-1j * omega * z_m / v_m_per_s)
        )
    return out


def channel_currents(point_transfer: np.ndarray) -> np.ndarray:
    z_um = base.OPT_Z_UM
    return np.asarray(
        [
            [np.trapezoid(opt[3] * point_transfer[jf], z_um) for opt in base.OPTICS]
            for jf in range(point_transfer.shape[0])
        ],
        dtype=complex,
    )


def pair_linear_fit(J: np.ndarray, r_down: complex, r_up: complex):
    Fd = law.kernel_basis(r_down)
    Fu = law.kernel_basis(r_up)
    X = np.column_stack((np.ones(len(J), dtype=complex), Fd, Fu))
    coeff, *_ = np.linalg.lstsq(X, J, rcond=None)
    model = X @ coeff
    err = model - J
    centered = J - np.mean(J)
    centered_scale = max(float(np.linalg.norm(centered)), 1e-30)
    full_scale = max(float(np.linalg.norm(J)), 1e-30)
    return {
        "coeff": coeff,
        "model": model,
        "full_rel": float(np.linalg.norm(err) / full_scale),
        "centered_rel": float(np.linalg.norm(err) / centered_scale),
        "design_condition": float(np.linalg.cond(X)),
    }


def _residual_vector(J: np.ndarray, x: np.ndarray) -> np.ndarray:
    # x contains roots in dimensionless per-micrometre coordinates.
    rd = (x[0] + 1j * x[1]) / ROOT_SCALE_M
    ru = (x[2] + 1j * x[3]) / ROOT_SCALE_M
    fit = pair_linear_fit(J, rd, ru)
    err = fit["model"] - J
    centered_scale = max(float(np.linalg.norm(J - np.mean(J))), 1e-30)
    err = err / centered_scale
    return np.concatenate((err.real, err.imag))


def fit_pair_roots(J: np.ndarray, rd_seed: complex, ru_seed: complex):
    rho_d = rd_seed * ROOT_SCALE_M
    rho_u = ru_seed * ROOT_SCALE_M
    seeds = []
    for sd, su in ((1.0, 1.0), (0.9, 1.0), (1.1, 1.0), (1.0, 0.9), (1.0, 1.1), (0.9, 1.1), (1.1, 0.9)):
        seeds.append(np.asarray((rho_d.real, max(rho_d.imag * sd, 1e-8), rho_u.real, min(rho_u.imag * su, -1e-8)), dtype=float))

    lower = np.asarray((-20.0, 1e-10, -20.0, -20.0), dtype=float)
    upper = np.asarray((20.0, 20.0, 20.0, -1e-10), dtype=float)
    candidates = []
    for x0 in seeds:
        x0 = np.minimum(np.maximum(x0, lower + 1e-12), upper - 1e-12)
        opt = least_squares(
            lambda x: _residual_vector(J, x),
            x0,
            bounds=(lower, upper),
            xtol=1e-13,
            ftol=1e-13,
            gtol=1e-13,
            max_nfev=8000,
        )
        rd = (opt.x[0] + 1j * opt.x[1]) / ROOT_SCALE_M
        ru = (opt.x[2] + 1j * opt.x[3]) / ROOT_SCALE_M
        lf = pair_linear_fit(J, rd, ru)
        s = np.linalg.svd(opt.jac, compute_uv=False)
        jac_cond = float(s[0] / s[-1]) if len(s) and s[-1] > 0 else float("inf")
        candidates.append((lf["centered_rel"], opt.cost, rd, ru, lf, opt, jac_cond))

    best = min(candidates, key=lambda q: (q[0], q[1]))
    _, _, rd, ru, lf, opt, jac_cond = best
    return {
        "r_down": rd,
        "r_up": ru,
        "fit": lf,
        "optimizer_success": bool(opt.success),
        "optimizer_status": int(opt.status),
        "optimizer_nfev": int(opt.nfev),
        "jacobian_condition": jac_cond,
        "root_separation_relative": float(abs(rd - ru) / max(abs(rd), abs(ru), 1e-30)),
        "multistart_count": len(candidates),
    }


def root_relative_error(fit: complex, expected: complex) -> float:
    return float(abs(fit - expected) / max(abs(expected), 1e-30))


def main(args):
    z_m = base.OPT_Z_UM * 1e-6
    frequencies = PROBE_FREQUENCIES.copy()
    v_down_ref = float(exact.exact_speed_m_per_s(np.asarray((0.0,)))[0])

    # Exact Rev. 7 heterogeneous downstream transfer and a uniform downstream null.
    H_down_het = exact.exact_point_transfer(z_m, frequencies)
    H_down_uni = uniform_down_transfer(z_m, frequencies, v_down_ref)
    J_down_het = channel_currents(H_down_het)

    # Single-carrier exact-continuum reference roots for comparison and hetero seeds.
    single_roots = []
    single_reference = {}
    for jf, f in enumerate(frequencies):
        r, _c, _m, rel = law.kernel_aware_root(J_down_het[jf])
        gamma = -r
        D, w = law.solve_dw_one_frequency(gamma, float(f))
        single_roots.append(r)
        single_reference[str(int(f))] = {
            "r_real_per_m": float(r.real),
            "r_imag_per_m": float(r.imag),
            "D_eff_m2_per_s": float(D),
            "w_eff_m_per_s": float(w),
            "kernel_fit_rel": float(rel),
        }

    # Hard full-collection dc pair identity, tested directly on the point grid.
    Hddc = uniform_down_transfer(z_m, np.asarray((0.0,)), v_down_ref)[0]
    # Any positive uniform countercarrier speed has the same dc identity.
    Hudc = uniform_up_transfer(z_m, np.asarray((0.0,)), v_down_ref)[0]
    dc_pair_error = float(np.max(np.abs(Hddc + Hudc - 1.0)))

    rows = []
    uniform_core_pass = True
    hetero_positive_core = 0
    hetero_core_total = 0

    for ratio in SPEED_RATIOS:
        v_up = float(ratio * v_down_ref)
        H_up = uniform_up_transfer(z_m, frequencies, v_up)
        J_uni = channel_currents(H_down_uni + H_up)
        J_het = channel_currents(H_down_het + H_up)

        for jf, f in enumerate(frequencies):
            omega = 2.0 * np.pi * float(f)
            rd_expected = 1j * omega / v_down_ref
            ru_expected = -1j * omega / v_up

            fit_u = fit_pair_roots(J_uni[jf], rd_expected, ru_expected)
            gd_u = -fit_u["r_down"]
            D_u, w_u = law.solve_dw_one_frequency(gd_u, float(f))
            rd_err = root_relative_error(fit_u["r_down"], rd_expected)
            ru_err = root_relative_error(fit_u["r_up"], ru_expected)

            core = bool(CORE_MIN_RATIO <= ratio <= CORE_MAX_RATIO)
            uniform_pass = bool(
                fit_u["optimizer_success"]
                and fit_u["fit"]["centered_rel"] <= UNIFORM_CENTERED_REL_TOL
                and abs(D_u) <= UNIFORM_D_TOL
                and fit_u["r_down"].imag > 0
                and fit_u["r_up"].imag < 0
            )
            if core:
                uniform_core_pass = uniform_core_pass and uniform_pass

            # Seed the heterogeneous downstream root from the independently fitted
            # Rev. 7 single-carrier exact-continuum root, while retaining the
            # physical pure-drift countercarrier seed.
            fit_h = fit_pair_roots(J_het[jf], single_roots[jf], ru_expected)
            gd_h = -fit_h["r_down"]
            D_h, w_h = law.solve_dw_one_frequency(gd_h, float(f))
            D_ref = single_reference[str(int(f))]["D_eff_m2_per_s"]
            rel_D_shift = float(abs(D_h - D_ref) / max(abs(D_ref), 1e-30))

            identifiable = bool(uniform_pass and fit_h["optimizer_success"])
            if core and identifiable:
                hetero_core_total += 1
                if D_h > 0:
                    hetero_positive_core += 1

            rows.append({
                "speed_ratio_vup_over_vdown": float(ratio),
                "frequency_hz": float(f),
                "v_down_ref_m_per_s": v_down_ref,
                "v_up_m_per_s": v_up,
                "core_speed_ratio": core,
                "uniform_pass": uniform_pass,
                "uniform_D_down_m2_per_s": float(D_u),
                "uniform_w_down_m_per_s": float(w_u),
                "uniform_r_down_real_per_m": float(fit_u["r_down"].real),
                "uniform_r_down_imag_per_m": float(fit_u["r_down"].imag),
                "uniform_r_up_real_per_m": float(fit_u["r_up"].real),
                "uniform_r_up_imag_per_m": float(fit_u["r_up"].imag),
                "uniform_r_down_relative_error": rd_err,
                "uniform_r_up_relative_error": ru_err,
                "uniform_centered_fit_rel": float(fit_u["fit"]["centered_rel"]),
                "uniform_full_fit_rel": float(fit_u["fit"]["full_rel"]),
                "uniform_design_condition": float(fit_u["fit"]["design_condition"]),
                "uniform_jacobian_condition": float(fit_u["jacobian_condition"]),
                "uniform_root_separation_relative": float(fit_u["root_separation_relative"]),
                "heterogeneous_identifiable_by_uniform_gate": identifiable,
                "heterogeneous_D_down_m2_per_s": float(D_h),
                "heterogeneous_w_down_m_per_s": float(w_h),
                "heterogeneous_r_down_real_per_m": float(fit_h["r_down"].real),
                "heterogeneous_r_down_imag_per_m": float(fit_h["r_down"].imag),
                "heterogeneous_r_up_real_per_m": float(fit_h["r_up"].real),
                "heterogeneous_r_up_imag_per_m": float(fit_h["r_up"].imag),
                "heterogeneous_centered_fit_rel": float(fit_h["fit"]["centered_rel"]),
                "heterogeneous_full_fit_rel": float(fit_h["fit"]["full_rel"]),
                "heterogeneous_design_condition": float(fit_h["fit"]["design_condition"]),
                "heterogeneous_jacobian_condition": float(fit_h["jacobian_condition"]),
                "heterogeneous_root_separation_relative": float(fit_h["root_separation_relative"]),
                "single_carrier_reference_D_m2_per_s": float(D_ref),
                "heterogeneous_relative_D_shift_from_single": rel_D_shift,
                "heterogeneous_positive_D": bool(D_h > 0),
            })

    core_rows = [r for r in rows if r["core_speed_ratio"]]
    identifiable_core = [r for r in core_rows if r["heterogeneous_identifiable_by_uniform_gate"]]
    positive_core = [r for r in identifiable_core if r["heterogeneous_positive_D"]]

    if not uniform_core_pass or dc_pair_error > DC_TOL:
        classification = "GATE_A_FAIL_DO_NOT_INTERPRET_HETEROGENEOUS_RESULT"
    elif len(identifiable_core) == 0:
        classification = "PAIR_MODES_NOT_IDENTIFIABLE_IN_CORE_SWEEP"
    elif len(positive_core) == len(identifiable_core):
        classification = "B1_MECHANISM_SURVIVES_ALL_IDENTIFIABLE_CORE_PAIR_CASES"
    elif len(positive_core) >= 3:
        classification = "B2_MECHANISM_SURVIVES_ONLY_PART_OF_IDENTIFIABLE_PAIR_SWEEP"
    else:
        classification = "B3_MECHANISM_NOT_ROBUST_IN_PAIR_AWARE_CORE_SWEEP"

    payload = {
        "status": "CHECKED exact-planar two-carrier closure stress" if uniform_core_pass and dc_pair_error <= DC_TOL else "TWO-CARRIER CONTROL GATE FAILED",
        "predeclared_gate_file": "PAPER02_TWO_CARRIER_GATE_2026-08-16.md",
        "classification": classification,
        "model_truth": {
            "microscopic_diffusion_m2_per_s": 0.0,
            "recombination": 0.0,
            "downstream_heterogeneous_profile": "exact Rev7 planar Poisson-curvature velocity profile",
            "countercarrier_profile": "uniform velocity, swept independently",
            "pair_dc_full_collection_identity": "H_down(z,0)+H_up(z,0)=1",
        },
        "inverse_model": "J_m=C+K_down*F_m(r_down)+K_up*F_m(r_up), complex linear coefficients profiled",
        "v_down_ref_m_per_s": v_down_ref,
        "dc_pair_identity_max_abs_error": dc_pair_error,
        "dc_gate_tolerance": DC_TOL,
        "uniform_centered_fit_tolerance": UNIFORM_CENTERED_REL_TOL,
        "uniform_D_tolerance_m2_per_s": UNIFORM_D_TOL,
        "uniform_core_gate_pass": bool(uniform_core_pass),
        "speed_ratios": [float(x) for x in SPEED_RATIOS],
        "probe_frequencies_hz": [float(x) for x in frequencies],
        "single_carrier_exact_reference": single_reference,
        "core_summary": {
            "row_count": len(core_rows),
            "identifiable_row_count": len(identifiable_core),
            "positive_D_row_count": len(positive_core),
            "min_heterogeneous_D_m2_per_s": float(min((r["heterogeneous_D_down_m2_per_s"] for r in identifiable_core), default=float("nan"))),
            "max_heterogeneous_D_m2_per_s": float(max((r["heterogeneous_D_down_m2_per_s"] for r in identifiable_core), default=float("nan"))),
            "max_uniform_abs_D_m2_per_s": float(max((abs(r["uniform_D_down_m2_per_s"]) for r in core_rows), default=float("nan"))),
            "max_uniform_centered_fit_rel": float(max((r["uniform_centered_fit_rel"] for r in core_rows), default=float("nan"))),
            "max_heterogeneous_centered_fit_rel": float(max((r["heterogeneous_centered_fit_rel"] for r in identifiable_core), default=float("nan"))),
            "max_relative_D_shift_from_single": float(max((r["heterogeneous_relative_D_shift_from_single"] for r in identifiable_core), default=float("nan"))),
        },
        "rows": rows,
    }

    out_json = Path(args.output_json)
    out_csv = Path(args.output_csv)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
    with out_csv.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)

    print(json.dumps(payload, indent=2, sort_keys=True))


def parser():
    p = argparse.ArgumentParser()
    p.add_argument("--output-json", default="results/paper02_two_carrier_exact_continuum_summary.json")
    p.add_argument("--output-csv", default="results/paper02_two_carrier_exact_continuum_rows.csv")
    return p


if __name__ == "__main__":
    main(parser().parse_args())
