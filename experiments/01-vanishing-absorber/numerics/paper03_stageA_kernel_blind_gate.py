"""Kernel-aware blind-analysis gate for Paper 03 Stage A.

This script deliberately separates three issues that the earlier raw geometry
closure mixed together:

1. deterministic fixed-field drift-diffusion forward solution;
2. same-physics planar/same-optics reference subtraction;
3. the Paper-01 Rev9 arbitrary-kernel one-mode model

       J_m = A + B M_m(r),
       M_m(r) = integral g_m(z) exp(r z) dz.

The six wavelength kernels in the HgCdTe stress change shape, so the geometric
first-difference identity is not the exact one-mode null.  The nonlinear
kernel-aware fit below profiles out complex A and B and fits only complex r.
Both the original central quartet and all six calibrated channels are reported.

This remains Stage A: the electrostatic field is the controlled geometry stress,
not a self-consistent semiconductor Poisson/drift-diffusion solution.  Results
remain NON-CLAIM until the blind hierarchy, stochastic cross-check, finite
recombination, and Stage-B gates are complete.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import numpy as np
from scipy.interpolate import RegularGridInterpolator
from scipy.optimize import least_squares

import paper03_combined_physics_challenge as stage
import paper03_stageA_resolvent as resolvent
import realistic_geometry_closure_stress as base


Z_UM = np.asarray(base.OPT_Z_UM, float)
Z_REF_UM = 0.5 * (float(Z_UM[0]) + float(Z_UM[-1]))

# Trapezoid quadrature weights for the calibrated optical kernels.
DZ = np.diff(Z_UM)
if not np.allclose(DZ, DZ[0], rtol=1e-10, atol=1e-14):
    raise RuntimeError("kernel grid is unexpectedly nonuniform")
WZ = np.full(len(Z_UM), float(DZ[0]))
WZ[0] *= 0.5
WZ[-1] *= 0.5
KERNEL_MATRIX = np.asarray([row[3] for row in base.OPTICS], float) * WZ[None, :]
KERNEL_NORMALIZATION = KERNEL_MATRIX @ np.ones(len(Z_UM))

CENTRAL4 = np.asarray((1, 2, 3, 4), dtype=int)
ALL6 = np.arange(len(base.DEPTHS), dtype=int)

# This is a numerical source-quadrature readiness threshold, fixed before the
# 17-point result is read.  It is not a physics significance threshold.
SOURCE_QUADRATURE_PHASE_FRACTION_GATE = 0.005


def integrate_full_support(
    gen: resolvent.DiscreteGenerator,
    U: np.ndarray,
    nx_src: int,
) -> np.ndarray:
    """Integrate over the full calibrated optical support, including contacts."""
    xq_um, wx = base.gauss(-base.X_EXTENT_UM, base.X_EXTENT_UM, nx_src)
    beam = np.exp(-0.5 * (xq_um / base.X_SIGMA_UM) ** 2)
    beam /= np.sum(wx * beam)

    points = np.column_stack(
        (
            np.repeat(Z_UM * 1e-6, len(xq_um)),
            np.tile(xq_um * 1e-6, len(Z_UM)),
        )
    )

    J = np.zeros((len(base.FREQUENCIES), len(base.DEPTHS)), dtype=complex)
    for kf in range(len(base.FREQUENCIES)):
        grid = resolvent.full_grid(gen, U[kf])
        interp = RegularGridInterpolator(
            (gen.zs, gen.xs), grid, method="linear", bounds_error=True
        )
        vals = interp(points).reshape(len(Z_UM), len(xq_um))
        for ix in range(len(xq_um)):
            Hz = vals[:, ix]
            for m, optical in enumerate(base.OPTICS):
                J[kf, m] += (
                    wx[ix]
                    * beam[ix]
                    * np.trapezoid(optical[3] * Hz, Z_UM)
                )
    return J


def build_fixed_field_case(
    scenario: base.Scenario,
    *,
    nx: int,
    nz: int,
    nx_src: int,
    diffusion_m2_s: float = 2.5e-3,
    lifetime_s: float = float("inf"),
) -> tuple[np.ndarray, dict[str, Any]]:
    cfg = resolvent.ResolventConfig(
        diffusion_m2_s=diffusion_m2_s,
        lifetime_s=lifetime_s,
        nx=nx,
        nz=nz,
        nx_src=nx_src,
    )
    gen = resolvent.build_generator(scenario, cfg)
    U, diag = resolvent.solve_resolvent(gen, cfg)
    J = integrate_full_support(gen, U, nx_src)
    if not np.all(np.isfinite(J.real)) or not np.all(np.isfinite(J.imag)):
        raise AssertionError("non-finite full-support current")
    if diag["max_linear_relative_residual"] >= 1e-8:
        raise AssertionError("linear residual gate failed")
    if diag["committor_relative_residual"] >= 1e-8:
        raise AssertionError("committor residual gate failed")
    if np.isinf(lifetime_s) and diag["dc_committor_ramo_max_abs_error"] >= 1e-8:
        raise AssertionError("dc committor/Ramo gate failed")
    return J, {
        "scenario": scenario.__dict__,
        "config": cfg.__dict__,
        "solver_diagnostics": diag,
    }


def moment_vector(r_per_um: complex, indices: np.ndarray) -> np.ndarray:
    expo = np.exp(r_per_um * (Z_UM - Z_REF_UM))
    return (KERNEL_MATRIX[indices] @ expo).astype(complex)


def profile_linear_coefficients(
    J: np.ndarray,
    indices: np.ndarray,
    r_per_um: complex,
) -> tuple[np.ndarray, np.ndarray, float, complex, complex]:
    y = np.asarray(J[indices], complex)
    M = moment_vector(r_per_um, indices)
    mscale = max(float(np.linalg.norm(M)), np.finfo(float).tiny)
    X = np.column_stack((np.ones(len(indices), dtype=complex), M / mscale))
    coeff, *_ = np.linalg.lstsq(X, y, rcond=None)
    pred = X @ coeff
    residual = pred - y
    cond = float(np.linalg.cond(X))
    A = complex(coeff[0])
    B = complex(coeff[1] / mscale)
    return pred, residual, cond, A, B


def seed_roots(J: np.ndarray, indices: np.ndarray) -> list[tuple[float, float]]:
    seeds: list[tuple[float, float]] = []
    for re in (-18.0, -10.0, -5.0, -2.0, -0.5, 0.5, 2.0, 5.0, 10.0, 18.0):
        for im in (-8.0, -1.0, 0.0, 1.0, 8.0):
            seeds.append((re, im))

    y = np.asarray(J[indices], complex)
    if len(y) >= 4:
        d = np.diff(y)
        ratios = []
        for a, b in zip(d[:-1], d[1:]):
            if abs(a) > 1e-14 * max(1.0, np.max(np.abs(y))):
                ratios.append(b / a)
        if ratios:
            q = sum(ratios) / len(ratios)
            if q != 0:
                r0 = np.log(q) / 0.5
                for alias in (-1, 0, 1):
                    rr = complex(r0.real, r0.imag + alias * 2.0 * np.pi / 0.5)
                    if -24.5 < rr.real < 24.5 and -14.5 < rr.imag < 14.5:
                        seeds.append((float(rr.real), float(rr.imag)))
    # Stable de-duplication while preserving order.
    out: list[tuple[float, float]] = []
    seen = set()
    for s in seeds:
        key = (round(s[0], 8), round(s[1], 8))
        if key not in seen:
            seen.add(key)
            out.append(s)
    return out


def kernel_one_mode_fit(J: np.ndarray, indices: np.ndarray) -> dict[str, Any]:
    y = np.asarray(J[indices], complex)
    contrast = y - np.mean(y)
    scale = max(float(np.linalg.norm(contrast)), np.finfo(float).tiny)

    def fun(x: np.ndarray) -> np.ndarray:
        r = complex(float(x[0]), float(x[1]))
        _, residual, _, _, _ = profile_linear_coefficients(J, indices, r)
        rr = residual / scale
        return np.concatenate((rr.real, rr.imag))

    candidates = []
    for seed in seed_roots(J, indices):
        try:
            opt = least_squares(
                fun,
                np.asarray(seed, float),
                bounds=([-25.0, -15.0], [25.0, 15.0]),
                xtol=1e-12,
                ftol=1e-12,
                gtol=1e-12,
                max_nfev=800,
            )
        except Exception:
            continue
        if not np.all(np.isfinite(opt.x)) or not np.isfinite(opt.cost):
            continue
        candidates.append((float(np.linalg.norm(fun(opt.x))), opt))

    if not candidates:
        raise RuntimeError("kernel-aware nonlinear fit found no finite candidate")
    candidates.sort(key=lambda item: item[0])
    rel, best = candidates[0]
    rbest = complex(float(best.x[0]), float(best.x[1]))
    pred, residual, cond, A, B = profile_linear_coefficients(J, indices, rbest)

    second = candidates[1][0] if len(candidates) > 1 else None
    return {
        "indices": indices.tolist(),
        "mean_depths_um": base.DEPTHS[indices].tolist(),
        "n_complex_channels": int(len(indices)),
        "n_real_residual_dof_after_A_B_r": int(2 * len(indices) - 6),
        "r_per_um": {"real": float(rbest.real), "imag": float(rbest.imag)},
        "A": {"real": float(A.real), "imag": float(A.imag)},
        "B_centered_moment_basis": {"real": float(B.real), "imag": float(B.imag)},
        "contrast_normalized_residual": float(np.linalg.norm(residual) / scale),
        "max_abs_residual_over_rms_contrast": float(
            np.max(np.abs(residual)) / max(scale / np.sqrt(len(indices)), np.finfo(float).tiny)
        ),
        "profile_design_condition_number": cond,
        "optimizer_cost": float(best.cost),
        "optimizer_nfev": int(best.nfev),
        "number_of_finite_multistarts": int(len(candidates)),
        "second_best_contrast_normalized_residual": (
            None if second is None else float(second)
        ),
        "predicted": {
            "real": pred.real.tolist(),
            "imag": pred.imag.tolist(),
        },
        "residual": {
            "real": residual.real.tolist(),
            "imag": residual.imag.tolist(),
        },
    }


def validate_kernel_fit() -> dict[str, Any]:
    r_true = complex(-3.0, 0.7)
    A_true = complex(0.4, 0.2)
    B_true = complex(1.2, -0.1)
    M = moment_vector(r_true, ALL6)
    J = A_true + B_true * M
    fit = kernel_one_mode_fit(J, ALL6)
    r_fit = complex(fit["r_per_um"]["real"], fit["r_per_um"]["imag"])
    if fit["contrast_normalized_residual"] >= 1e-9:
        raise AssertionError("known one-mode kernel regression residual failed")
    if abs(r_fit - r_true) >= 1e-5:
        raise AssertionError(f"known one-mode kernel root recovery failed: {r_fit}")
    return {
        "true_r_per_um": {"real": r_true.real, "imag": r_true.imag},
        "fit_r_per_um": fit["r_per_um"],
        "contrast_normalized_residual": fit["contrast_normalized_residual"],
    }


def raw_phase_map(J: np.ndarray) -> dict[float, float]:
    metrics = stage.blind_analysis(J)["metrics"]
    return {
        float(m["frequency_hz"]): float(m["closure4_phase_deg"])
        for m in metrics
    }


def compare_phase_change(Ja: np.ndarray, Jb: np.ndarray) -> dict[str, Any]:
    pa, pb = raw_phase_map(Ja), raw_phase_map(Jb)
    rows = []
    for f in base.FREQUENCIES:
        f = float(f)
        if f <= 0.0:
            continue
        target = abs(float(base.GRADIENT_TARGET_DEG[f]))
        rows.append(
            {
                "frequency_hz": f,
                "phase_a_deg": pa[f],
                "phase_b_deg": pb[f],
                "absolute_change_deg": abs(pb[f] - pa[f]),
                "change_fraction_of_frozen_target": abs(pb[f] - pa[f]) / target,
            }
        )
    return {
        "rows": rows,
        "worst_change_fraction_of_frozen_target": float(
            max(x["change_fraction_of_frozen_target"] for x in rows)
        ),
    }


def fit_frequency_table(J: np.ndarray) -> list[dict[str, Any]]:
    out = []
    for kf, f in enumerate(base.FREQUENCIES):
        out.append(
            {
                "frequency_hz": float(f),
                "central4": kernel_one_mode_fit(J[kf], CENTRAL4),
                "all6": kernel_one_mode_fit(J[kf], ALL6),
            }
        )
    return out


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("paper03_stageA_kernel_blind_gate.json"),
    )
    args = p.parse_args()

    kernel_regression = validate_kernel_fit()
    if float(np.max(np.abs(KERNEL_NORMALIZATION - 1.0))) >= 1e-8:
        raise AssertionError("optical kernels are not normalized")

    finite = next(s for s in base.SCENARIOS if s.name == "finite75_depletion")
    planar = next(s for s in base.SCENARIOS if s.name == "planar")

    # Full-support grid continuation: retain the original 2%-of-target spatial
    # threshold and separately predeclare 0.5% for the 13->17 lateral quadrature.
    Jf161, df161 = build_fixed_field_case(finite, nx=161, nz=121, nx_src=17)
    Jf201_17, df201 = build_fixed_field_case(finite, nx=201, nz=151, nx_src=17)

    # Reuse the same 201x151 generator/solution for a pure source-quadrature check.
    cfg201 = resolvent.ResolventConfig(
        diffusion_m2_s=2.5e-3,
        lifetime_s=float("inf"),
        nx=201,
        nz=151,
        nx_src=17,
    )
    gen201 = resolvent.build_generator(finite, cfg201)
    U201, d201_repeat = resolvent.solve_resolvent(gen201, cfg201)
    Jf201_13 = integrate_full_support(gen201, U201, 13)
    Jf201_17_repeat = integrate_full_support(gen201, U201, 17)
    repeat_error = float(
        np.linalg.norm(Jf201_17_repeat - Jf201_17)
        / max(np.linalg.norm(Jf201_17), np.finfo(float).tiny)
    )
    if repeat_error >= 1e-12:
        raise AssertionError(f"repeat full-support integration mismatch: {repeat_error}")

    grid_check = compare_phase_change(Jf161, Jf201_17)
    quadrature_check = compare_phase_change(Jf201_13, Jf201_17)
    quadrature_pass = (
        quadrature_check["worst_change_fraction_of_frozen_target"]
        <= SOURCE_QUADRATURE_PHASE_FRACTION_GATE
    )

    Jplanar, dplanar = build_fixed_field_case(planar, nx=201, nz=151, nx_src=17)
    phase_finite = raw_phase_map(Jf201_17)
    phase_planar = raw_phase_map(Jplanar)
    baseline_rows = []
    for f in base.FREQUENCIES:
        f = float(f)
        if f <= 0.0:
            continue
        excess = phase_finite[f] - phase_planar[f]
        target = float(base.GRADIENT_TARGET_DEG[f])
        baseline_rows.append(
            {
                "frequency_hz": f,
                "finite75_depletion_raw_phase_deg": phase_finite[f],
                "planar_same_physics_raw_phase_deg": phase_planar[f],
                "finite_minus_planar_phase_deg": excess,
                "signed_fraction_of_frozen_transport_target": excess / target,
                "absolute_fraction_of_frozen_transport_target": abs(excess / target),
            }
        )

    result = {
        "schema": "paper03-stageA-kernel-blind-v1",
        "status": "KERNEL-AWARE BLIND DEVELOPMENT GATE / NON-CLAIM",
        "forward_model": {
            "stage": "A",
            "self_consistent_semiconductor": False,
            "diffusion_m2_s": 2.5e-3,
            "lifetime_s": "inf",
            "finite_scenario": finite.__dict__,
            "planar_scenario": planar.__dict__,
        },
        "kernel_model": {
            "equation": "J_m=A+B*M_m(r); M_m(r)=integral g_m(z)*exp(r*z) dz",
            "centered_exponential_reference_um": Z_REF_UM,
            "kernel_normalization": KERNEL_NORMALIZATION.tolist(),
            "known_one_mode_regression": kernel_regression,
            "fit_scope": (
                "A and B are profiled complex linear coefficients; complex r is "
                "fit by bounded multistart nonlinear least squares. Central4 and "
                "all6 fits are reported independently at each RF."
            ),
        },
        "numerical_checks": {
            "finite_161": df161,
            "finite_201": df201,
            "finite_201_repeat_solver": d201_repeat,
            "full_support_grid_161_to_201": grid_check,
            "source_quadrature_13_to_17": {
                **quadrature_check,
                "predeclared_threshold_fraction": SOURCE_QUADRATURE_PHASE_FRACTION_GATE,
                "passed": bool(quadrature_pass),
            },
            "repeat_201x151_17point_relative_error": repeat_error,
            "planar_201": dplanar,
        },
        "same_physics_planar_reference": baseline_rows,
        "kernel_aware_one_mode_fits": {
            "finite75_depletion": fit_frequency_table(Jf201_17),
            "planar": fit_frequency_table(Jplanar),
        },
        "raw_geometry_diagnostics": {
            "finite75_depletion": stage.blind_analysis(Jf201_17),
            "planar": stage.blind_analysis(Jplanar),
            "warning": (
                "These raw geometric closure/Hankel/root diagnostics are not the "
                "exact null for evolving optical kernel shapes and are retained "
                "only for comparison with the historical geometry stress."
            ),
        },
        "science_interpretation_ready": False,
        "remaining_before_interpretation": [
            "interpret the kernel-aware residual only after noise/statistical calibration",
            "build a kernel-aware higher-order alternative if one mode fails",
            "complete a coarse-observable stochastic cross-formulation check",
            "add and converge finite recombination",
            "complete Stage-B self-consistent semiconductor validation",
        ],
    }

    args.output.write_text(
        json.dumps(resolvent.json_safe(result), indent=2, allow_nan=False) + "\n",
        encoding="utf-8",
    )

    print("known one-mode regression:", json.dumps(kernel_regression, indent=2))
    print("grid check:", json.dumps(grid_check, indent=2))
    print("quadrature check:", json.dumps(result["numerical_checks"]["source_quadrature_13_to_17"], indent=2))
    print("same-physics planar reference:", json.dumps(baseline_rows, indent=2))
    for label, table in result["kernel_aware_one_mode_fits"].items():
        print(label)
        for row in table:
            print(
                row["frequency_hz"],
                "central4 rho=",
                row["central4"]["contrast_normalized_residual"],
                "all6 rho=",
                row["all6"]["contrast_normalized_residual"],
            )
    print("science_interpretation_ready = false")
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
