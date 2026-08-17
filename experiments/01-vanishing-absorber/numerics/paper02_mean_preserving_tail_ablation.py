"""Mean-preserving depletion-tail ablation for Paper 02.

The direct tail-ablation result strongly implicates finite kernel overlap with the
collector-side field-gradient region, but simply truncating and renormalizing a
kernel also moves its mean generation depth.  This control removes all support
inside depletion while restoring each channel's original mean depth by an
exponential tilt of the surviving upstream density.

For each channel:

    g_mp(z) proportional to g(z) * exp(lambda_m * (z-z_ref)),  z < z_d
              0,                                             z >= z_d

where lambda_m is chosen so that <z>_mp equals the original <z> exactly.

Because all six original means are below z_d=4.6 um, such an upstream-only
mean-preserving density exists.  The exact modified kernels are used in both the
forward optical average and the kernel-aware one-mode inverse.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np
from scipy.optimize import brentq

import realistic_geometry_closure_stress as base
import paper02_geometry_parameter_sweep as sweep
from paper02_kernel_aware_depletion_frequency_law import kernel_aware_root


FREQUENCIES = np.asarray((0.0, 100e6, 500e6, 1e9), dtype=float)
DEPLETION_WIDTH_UM = 3.0
SPACE_CHARGE_DROP_V = 0.05
CAL_FREQ_HZ = 100e6


def norm_density(d):
    n = float(np.trapezoid(d, base.OPT_Z_UM))
    if n <= 0:
        raise ValueError("nonpositive density norm")
    return d / n


def mean_depth(d):
    d = norm_density(np.asarray(d, dtype=float))
    return float(np.trapezoid(base.OPT_Z_UM * d, base.OPT_Z_UM))


def overlap(d, zd):
    d = norm_density(np.asarray(d, dtype=float))
    mask = base.OPT_Z_UM >= zd
    return float(np.trapezoid(d[mask], base.OPT_Z_UM[mask]))


def tilted_upstream_density(d0, zd, target_mean):
    z = base.OPT_Z_UM
    mask = z < zd
    base_up = np.where(mask, np.asarray(d0, dtype=float), 0.0)
    if float(np.trapezoid(base_up, z)) <= 0:
        raise ValueError("no upstream support")

    zref = float(target_mean)

    def density_for_lambda(lam):
        expo = lam * (z - zref)
        expo = np.where(mask, expo, -np.inf)
        finite = expo[np.isfinite(expo)]
        shift = float(np.max(finite)) if finite.size else 0.0
        weight = np.where(mask, np.exp(expo - shift), 0.0)
        return norm_density(base_up * weight)

    def f(lam):
        return mean_depth(density_for_lambda(lam)) - target_mean

    lo, hi = -1.0, 1.0
    flo, fhi = f(lo), f(hi)
    for _ in range(30):
        if flo <= 0 <= fhi:
            break
        if flo > 0:
            lo *= 2.0
            flo = f(lo)
        if fhi < 0:
            hi *= 2.0
            fhi = f(hi)
    else:
        raise RuntimeError(
            f"failed to bracket mean-preserving tilt for target {target_mean:.9f} um: "
            f"f({lo})={flo}, f({hi})={fhi}"
        )

    lam = float(brentq(f, lo, hi, xtol=1e-13, rtol=1e-13, maxiter=500))
    d = density_for_lambda(lam)
    return d, lam


def make_kernel_sets(original, zd):
    truncated = []
    matched = []
    metadata = []
    mask_up = base.OPT_Z_UM < zd

    for ch, row in enumerate(original):
        d0 = norm_density(np.asarray(row[3], dtype=float))
        mu0 = mean_depth(d0)
        p0 = overlap(d0, zd)

        dt = norm_density(np.where(mask_up, d0, 0.0))
        mut = mean_depth(dt)

        dm, lam = tilted_upstream_density(d0, zd, mu0)
        mum = mean_depth(dm)
        pm = overlap(dm, zd)

        rt = list(row)
        rt[3] = dt
        rm = list(row)
        rm[3] = dm
        truncated.append(tuple(rt))
        matched.append(tuple(rm))

        metadata.append(
            {
                "channel": ch,
                "original_mean_um": mu0,
                "original_depletion_overlap": p0,
                "truncated_mean_um": mut,
                "matched_mean_um": mum,
                "matched_mean_error_um": mum - mu0,
                "matched_depletion_overlap": pm,
                "tilt_lambda_per_um": lam,
            }
        )

    return truncated, matched, metadata


def solve_dw(gamma, f):
    g2 = gamma * gamma
    M = np.asarray(((g2.real, gamma.real), (g2.imag, gamma.imag)), dtype=float)
    rhs = np.asarray((0.0, -2.0 * np.pi * f), dtype=float)
    D, w = np.linalg.solve(M, rhs)
    return float(D), float(w)


def law_residual(gamma, f, D, w):
    if f <= 0:
        return 0.0
    rhs = -1j * 2.0 * np.pi * f
    return float(abs(D * gamma * gamma + w * gamma - rhs) / abs(rhs))


def evaluate(label, kernels, scenario, numerical):
    base.OPTICS = kernels
    J, diag = sweep.currents_with_beam(scenario, 2.0, 0.0, **numerical)
    gammas = []
    fits = []
    for jf, _ in enumerate(FREQUENCIES):
        r, _, _, fit = kernel_aware_root(J[jf])
        gammas.append(-r)
        fits.append(float(fit))
    gammas = np.asarray(gammas)
    i100 = int(np.where(FREQUENCIES == CAL_FREQ_HZ)[0][0])
    i1g = int(np.where(FREQUENCIES == 1e9)[0][0])
    D, w = solve_dw(gammas[i100], CAL_FREQ_HZ)
    return {
        "case": label,
        "effective_D_m2_per_s": D,
        "effective_w_m_per_s": w,
        "positive_D_w": bool(D > 0 and w > 0),
        "law_residual_1ghz": law_residual(gammas[i1g], 1e9, D, w),
        "max_kernel_one_mode_fit_rel": max(fits),
        "collected_fraction": float(diag["collected"]),
        "dc_ramo_error": float(diag["dc_error"]),
    }


def run(args):
    original = list(base.OPTICS)
    old_freq = base.FREQUENCIES
    base.FREQUENCIES = FREQUENCIES.copy()
    base.V_BIAS = float(args.bias_v)
    base.X_EXTENT_UM = float(args.x_extent_um)

    zd = float(base.L_UM - DEPLETION_WIDTH_UM)
    truncated, matched, metadata = make_kernel_sets(original, zd)
    scenario = base.Scenario("planar_depletion", 1.0, DEPLETION_WIDTH_UM, SPACE_CHARGE_DROP_V)
    numerical = {
        "nx": args.nx,
        "nz": args.nz,
        "nx_src": args.nx_src,
        "nz_src": args.nz_src,
        "ds_um": args.ds_um,
    }

    try:
        results = [
            evaluate("physical_full_kernels", original, scenario, numerical),
            evaluate("tails_removed_renormalized", truncated, scenario, numerical),
            evaluate("tails_removed_mean_preserved", matched, scenario, numerical),
        ]
    finally:
        base.OPTICS = original
        base.FREQUENCIES = old_freq

    by_case = {r["case"]: r for r in results}
    dfull = by_case["physical_full_kernels"]["effective_D_m2_per_s"]
    dmatch = by_case["tails_removed_mean_preserved"]["effective_D_m2_per_s"]

    payload = {
        "status": "CONDITIONAL mean-preserving tail ablation",
        "geometry": {
            "absorber_thickness_um": float(base.L_UM),
            "depletion_start_um": zd,
            "depletion_width_um": DEPLETION_WIDTH_UM,
            "space_charge_drop_v": SPACE_CHARGE_DROP_V,
        },
        "kernel_metadata": metadata,
        "results": results,
        "causal_gate": {
            "full_D_eff_m2_per_s": dfull,
            "mean_preserved_zero_overlap_D_eff_m2_per_s": dmatch,
            "collapse_ratio": abs(dmatch) / max(abs(dfull), 1e-30),
            "max_abs_mean_error_um": max(abs(m["matched_mean_error_um"]) for m in metadata),
            "supported_if": "zero-overlap kernels with original means preserved still collapse |D_eff| relative to physical full kernels",
        },
    }

    out_csv = Path(args.output_results)
    out_meta = Path(args.output_metadata)
    out_json = Path(args.output_summary)
    for p in (out_csv, out_meta, out_json):
        p.parent.mkdir(parents=True, exist_ok=True)

    with out_csv.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(results[0].keys()))
        w.writeheader()
        w.writerows(results)
    with out_meta.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(metadata[0].keys()))
        w.writeheader()
        w.writerows(metadata)
    out_json.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


def parser():
    p = argparse.ArgumentParser()
    p.add_argument("--bias-v", type=float, default=0.30)
    p.add_argument("--x-extent-um", type=float, default=3.5)
    p.add_argument("--nx", type=int, default=121)
    p.add_argument("--nz", type=int, default=91)
    p.add_argument("--nx-src", type=int, default=13)
    p.add_argument("--nz-src", type=int, default=41)
    p.add_argument("--ds-um", type=float, default=0.020)
    p.add_argument("--output-results", default="paper02_mean_preserving_tail_ablation_results.csv")
    p.add_argument("--output-metadata", default="paper02_mean_preserving_tail_ablation_metadata.csv")
    p.add_argument("--output-summary", default="paper02_mean_preserving_tail_ablation_summary.json")
    return p


if __name__ == "__main__":
    run(parser().parse_args())
