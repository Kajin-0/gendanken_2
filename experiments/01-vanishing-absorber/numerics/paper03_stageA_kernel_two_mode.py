"""Kernel-aware two-mode diagnostic for Paper 03 Stage A.

The calibrated optical kernels are not rigid translations, so a second-mode
question must be posed in kernel space rather than by applying the raw Hankel
identity as though the samples were point sources.  This diagnostic fits

    J_m = A + B1 M_m(r1) + B2 M_m(r2),
    M_m(r) = integral g_m(z) exp(r z) dz,

using all six calibrated channels.

This is a diagnostic model-order extension, not a claim that Paper-01 Rev9
proved an arbitrary-kernel rank-two theorem, and not a physical assignment of
r1/r2. Six complex channels provide 12 real data components and the model has
10 real parameters, leaving only two real residual degrees of freedom in a
regular distinct-root parameterization. Therefore residual reduction alone is
not sufficient evidence. We also report root separation, profile conditioning,
coefficient balance, multistart/global-search agreement, and grid stability.

No result is interpreted as detector physics until statistical calibration,
cross-RF physical-law testing, stochastic cross-formulation checks, finite
recombination, and Stage-B self-consistent semiconductor validation are done.
"""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path
from typing import Any

import numpy as np
from scipy.optimize import differential_evolution, least_squares

import paper03_stageA_kernel_blind_gate as one
import paper03_stageA_resolvent as resolvent
import realistic_geometry_closure_stress as base


ALL6 = np.arange(len(base.DEPTHS), dtype=int)
ROOT_LOWER = np.asarray((-25.0, -15.0, -25.0, -15.0), float)
ROOT_UPPER = np.asarray((25.0, 15.0, 25.0, 15.0), float)


def canonical_roots(r1: complex, r2: complex) -> tuple[complex, complex]:
    roots = sorted((r1, r2), key=lambda z: (float(z.real), float(z.imag)))
    return roots[0], roots[1]


def profile_two_mode(
    J: np.ndarray,
    roots: tuple[complex, complex],
) -> tuple[np.ndarray, np.ndarray, float, tuple[complex, complex, complex]]:
    y = np.asarray(J[ALL6], complex)
    r1, r2 = roots
    M1 = one.moment_vector(r1, ALL6)
    M2 = one.moment_vector(r2, ALL6)
    s1 = max(float(np.linalg.norm(M1)), np.finfo(float).tiny)
    s2 = max(float(np.linalg.norm(M2)), np.finfo(float).tiny)
    X = np.column_stack(
        (
            np.ones(len(ALL6), dtype=complex),
            M1 / s1,
            M2 / s2,
        )
    )
    coeff, *_ = np.linalg.lstsq(X, y, rcond=None)
    pred = X @ coeff
    residual = pred - y
    A = complex(coeff[0])
    B1 = complex(coeff[1] / s1)
    B2 = complex(coeff[2] / s2)
    return pred, residual, float(np.linalg.cond(X)), (A, B1, B2)


def residual_vector(J: np.ndarray, x: np.ndarray) -> np.ndarray:
    r1 = complex(float(x[0]), float(x[1]))
    r2 = complex(float(x[2]), float(x[3]))
    _, residual, _, _ = profile_two_mode(J, (r1, r2))
    y = np.asarray(J[ALL6], complex)
    scale = max(float(np.linalg.norm(y - np.mean(y))), np.finfo(float).tiny)
    rr = residual / scale
    return np.concatenate((rr.real, rr.imag))


def objective(J: np.ndarray, x: np.ndarray) -> float:
    return float(np.linalg.norm(residual_vector(J, x)))


def local_seeds(J: np.ndarray, one_fit: dict[str, Any]) -> list[np.ndarray]:
    r0 = complex(one_fit["r_per_um"]["real"], one_fit["r_per_um"]["imag"])
    seeds: list[np.ndarray] = []

    # Split around the one-mode optimum over several scales, including a
    # near-confluent stress. These are deterministic seeds, not prior beliefs.
    for dr in (0.02, 0.10, 0.50, 2.0, 6.0):
        for angle in (0.0, np.pi / 2.0, np.pi / 4.0, -np.pi / 4.0):
            delta = dr * np.exp(1j * angle)
            a, b = r0 - delta, r0 + delta
            seeds.append(np.asarray((a.real, a.imag, b.real, b.imag), float))

    # A modest generic grid helps avoid assuming the second root is near r0.
    generic = (
        complex(-8.0, -2.0),
        complex(-8.0, 2.0),
        complex(-2.0, -1.0),
        complex(-2.0, 1.0),
        complex(2.0, -1.0),
        complex(2.0, 1.0),
        complex(8.0, -2.0),
        complex(8.0, 2.0),
    )
    for a, b in itertools.combinations(generic, 2):
        seeds.append(np.asarray((a.real, a.imag, b.real, b.imag), float))

    out: list[np.ndarray] = []
    seen = set()
    for x in seeds:
        x = np.minimum(np.maximum(x, ROOT_LOWER + 1e-9), ROOT_UPPER - 1e-9)
        key = tuple(np.round(x, 8))
        if key not in seen:
            seen.add(key)
            out.append(x)
    return out


def fit_two_mode(J: np.ndarray, *, seed: int) -> dict[str, Any]:
    y = np.asarray(J[ALL6], complex)
    contrast_scale = max(float(np.linalg.norm(y - np.mean(y))), np.finfo(float).tiny)
    one_fit = one.kernel_one_mode_fit(J, ALL6)

    bounds = list(zip(ROOT_LOWER, ROOT_UPPER))
    de = differential_evolution(
        lambda x: objective(J, np.asarray(x, float)),
        bounds=bounds,
        seed=seed,
        popsize=10,
        maxiter=90,
        tol=1e-8,
        polish=False,
        workers=1,
        updating="immediate",
    )

    seeds = [np.asarray(de.x, float), *local_seeds(J, one_fit)]
    candidates: list[tuple[float, np.ndarray, int]] = []
    for x0 in seeds:
        try:
            opt = least_squares(
                lambda x: residual_vector(J, x),
                x0,
                bounds=(ROOT_LOWER, ROOT_UPPER),
                xtol=1e-12,
                ftol=1e-12,
                gtol=1e-12,
                max_nfev=1400,
            )
        except Exception:
            continue
        if not np.all(np.isfinite(opt.x)) or not np.isfinite(opt.cost):
            continue
        candidates.append((objective(J, opt.x), np.asarray(opt.x, float), int(opt.nfev)))

    if not candidates:
        raise RuntimeError("no finite kernel-aware two-mode fit candidate")
    candidates.sort(key=lambda row: row[0])
    best_rho, xbest, nfev = candidates[0]
    rb1 = complex(float(xbest[0]), float(xbest[1]))
    rb2 = complex(float(xbest[2]), float(xbest[3]))
    pred, residual, cond, coeff = profile_two_mode(J, (rb1, rb2))
    A, B1, B2 = coeff

    # Canonical ordering is only for comparison/reporting. Coefficients are
    # reordered with their roots, and no physical label is attached.
    if (rb2.real, rb2.imag) < (rb1.real, rb1.imag):
        rb1, rb2 = rb2, rb1
        B1, B2 = B2, B1

    second_rho = candidates[1][0] if len(candidates) > 1 else None
    one_rho = float(one_fit["contrast_normalized_residual"])
    amp_hi = max(abs(B1), abs(B2), np.finfo(float).tiny)
    amp_lo = min(abs(B1), abs(B2))

    return {
        "n_complex_channels": 6,
        "n_real_data": 12,
        "n_real_parameters_regular_distinct_root": 10,
        "n_real_residual_dof_regular_distinct_root": 2,
        "one_mode_contrast_normalized_residual": one_rho,
        "two_mode_contrast_normalized_residual": float(best_rho),
        "residual_reduction_factor_one_over_two": float(
            one_rho / max(best_rho, np.finfo(float).tiny)
        ),
        "r1_per_um": {"real": float(rb1.real), "imag": float(rb1.imag)},
        "r2_per_um": {"real": float(rb2.real), "imag": float(rb2.imag)},
        "root_separation_per_um": float(abs(rb1 - rb2)),
        "profile_design_condition_number": cond,
        "B1": {"real": float(B1.real), "imag": float(B1.imag)},
        "B2": {"real": float(B2.real), "imag": float(B2.imag)},
        "smaller_over_larger_profiled_mode_amplitude": float(amp_lo / amp_hi),
        "A": {"real": float(A.real), "imag": float(A.imag)},
        "global_DE_contrast_normalized_residual_before_polish": float(de.fun),
        "global_DE_nit": int(de.nit),
        "number_of_finite_polished_candidates": int(len(candidates)),
        "best_local_nfev": nfev,
        "second_best_contrast_normalized_residual": (
            None if second_rho is None else float(second_rho)
        ),
        "predicted": {"real": pred.real.tolist(), "imag": pred.imag.tolist()},
        "residual": {"real": residual.real.tolist(), "imag": residual.imag.tolist()},
        "contrast_scale": contrast_scale,
        "one_mode_fit": one_fit,
        "interpretation_warning": (
            "Two-mode residual reduction is a flexible model-order diagnostic. "
            "Roots are not physical until branch/permutation, uncertainty, and "
            "cross-RF physical-law constraints are imposed. Near-coalescent roots "
            "may represent a confluent-like limit and can be ill-conditioned."
        ),
    }


def root_set_distance(a: dict[str, Any], b: dict[str, Any]) -> dict[str, float]:
    ar = (
        complex(a["r1_per_um"]["real"], a["r1_per_um"]["imag"]),
        complex(a["r2_per_um"]["real"], a["r2_per_um"]["imag"]),
    )
    br = (
        complex(b["r1_per_um"]["real"], b["r1_per_um"]["imag"]),
        complex(b["r2_per_um"]["real"], b["r2_per_um"]["imag"]),
    )
    direct = abs(ar[0] - br[0]) + abs(ar[1] - br[1])
    swap = abs(ar[0] - br[1]) + abs(ar[1] - br[0])
    if direct <= swap:
        pairs = ((ar[0], br[0]), (ar[1], br[1]))
    else:
        pairs = ((ar[0], br[1]), (ar[1], br[0]))
    distances = [abs(x - y) for x, y in pairs]
    scale = max(*(abs(x) for x in ar), *(abs(x) for x in br), 1e-12)
    return {
        "sum_abs_root_change_per_um": float(sum(distances)),
        "max_abs_root_change_per_um": float(max(distances)),
        "max_root_change_relative_to_largest_root_magnitude": float(max(distances) / scale),
    }


def validate_exact_two_mode() -> dict[str, Any]:
    r_true = (complex(-3.0, 0.7), complex(1.4, -0.45))
    A = complex(0.25, -0.1)
    B1 = complex(0.9, 0.25)
    B2 = complex(-0.55, 0.35)
    J = A + B1 * one.moment_vector(r_true[0], ALL6) + B2 * one.moment_vector(r_true[1], ALL6)
    fit = fit_two_mode(J, seed=901)
    if fit["two_mode_contrast_normalized_residual"] >= 1e-8:
        raise AssertionError("exact two-mode regression residual failed")

    fitted = (
        complex(fit["r1_per_um"]["real"], fit["r1_per_um"]["imag"]),
        complex(fit["r2_per_um"]["real"], fit["r2_per_um"]["imag"]),
    )
    true_sorted = canonical_roots(*r_true)
    fit_sorted = canonical_roots(*fitted)
    err = max(abs(true_sorted[0] - fit_sorted[0]), abs(true_sorted[1] - fit_sorted[1]))
    if err >= 2e-4:
        raise AssertionError(f"exact two-mode root recovery failed: {err}")
    return {
        "true_roots_per_um": [
            {"real": z.real, "imag": z.imag} for z in true_sorted
        ],
        "fit_roots_per_um": [
            {"real": z.real, "imag": z.imag} for z in fit_sorted
        ],
        "max_root_error_per_um": float(err),
        "contrast_normalized_residual": fit["two_mode_contrast_normalized_residual"],
    }


def fit_case_table(J: np.ndarray, seed_base: int) -> list[dict[str, Any]]:
    rows = []
    for kf, f in enumerate(base.FREQUENCIES):
        print(f"two-mode fit f={f/1e6:.1f} MHz", flush=True)
        rows.append(
            {
                "frequency_hz": float(f),
                "fit": fit_two_mode(J[kf], seed=seed_base + kf),
            }
        )
    return rows


def table_by_frequency(rows: list[dict[str, Any]]) -> dict[float, dict[str, Any]]:
    return {float(r["frequency_hz"]): r["fit"] for r in rows}


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("paper03_stageA_kernel_two_mode.json"),
    )
    args = p.parse_args()

    regression = validate_exact_two_mode()
    finite = next(s for s in base.SCENARIOS if s.name == "finite75_depletion")
    planar = next(s for s in base.SCENARIOS if s.name == "planar")

    # Reuse the numerically validated Stage-A forward formulation. The two grids
    # provide a root-stability attack in addition to residual convergence.
    J161, d161 = one.build_fixed_field_case(finite, nx=161, nz=121, nx_src=17)
    J201, d201 = one.build_fixed_field_case(finite, nx=201, nz=151, nx_src=17)
    Jp201, dp201 = one.build_fixed_field_case(planar, nx=201, nz=151, nx_src=17)

    f161 = fit_case_table(J161, 1100)
    f201 = fit_case_table(J201, 1200)
    p201 = fit_case_table(Jp201, 1300)
    a161, a201 = table_by_frequency(f161), table_by_frequency(f201)

    stability = []
    for f in base.FREQUENCIES:
        f = float(f)
        stability.append(
            {
                "frequency_hz": f,
                **root_set_distance(a161[f], a201[f]),
                "rho_161": a161[f]["two_mode_contrast_normalized_residual"],
                "rho_201": a201[f]["two_mode_contrast_normalized_residual"],
                "condition_161": a161[f]["profile_design_condition_number"],
                "condition_201": a201[f]["profile_design_condition_number"],
            }
        )

    result = {
        "schema": "paper03-stageA-kernel-two-mode-v1",
        "status": "KERNEL-AWARE TWO-MODE DIAGNOSTIC / NON-CLAIM",
        "model": {
            "equation": "J_m=A+B1*M_m(r1)+B2*M_m(r2)",
            "channels": 6,
            "regular_distinct_root_real_residual_dof": 2,
            "is_paper01_rev9_arbitrary_kernel_rank2_theorem": False,
            "physical_root_assignment_allowed": False,
        },
        "exact_two_mode_regression": regression,
        "forward": {
            "stage_B_self_consistent_semiconductor": False,
            "diffusion_m2_s": 2.5e-3,
            "lifetime_s": "inf",
            "finite_161_diagnostics": d161,
            "finite_201_diagnostics": d201,
            "planar_201_diagnostics": dp201,
        },
        "finite75_depletion": {
            "grid_161x121": f161,
            "grid_201x151": f201,
            "root_set_grid_stability": stability,
        },
        "planar_201x151": p201,
        "science_interpretation_ready": False,
        "remaining_before_interpretation": [
            "assess whether fitted second roots are stable/conditioned rather than residual-only overfit",
            "apply cross-RF branch/permutation-aware physical root-law tests if roots are stable enough",
            "statistically calibrate one-mode rejection and model-order selection",
            "complete stochastic coarse-observable cross-formulation validation",
            "add and converge finite recombination",
            "complete Stage-B self-consistent semiconductor validation",
        ],
    }

    args.output.write_text(
        json.dumps(resolvent.json_safe(result), indent=2, allow_nan=False) + "\n",
        encoding="utf-8",
    )

    print("exact regression:", json.dumps(regression, indent=2))
    for label, rows in (("finite161", f161), ("finite201", f201), ("planar201", p201)):
        print(label)
        for row in rows:
            fit = row["fit"]
            print(
                row["frequency_hz"],
                "rho1=", fit["one_mode_contrast_normalized_residual"],
                "rho2=", fit["two_mode_contrast_normalized_residual"],
                "sep=", fit["root_separation_per_um"],
                "cond=", fit["profile_design_condition_number"],
            )
    print("grid stability:", json.dumps(stability, indent=2))
    print("science_interpretation_ready = false")
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
