"""Ablation test for finite optical-kernel overlap with the depletion region.

The point-source causal control showed that ideal sources at 2.0--4.5 um give
D_eff ~= 0 when the depletion region begins at 4.6 um, while the physical finite
kernels centered over the same range give D_eff ~= 2.61e-3 m^2/s.

This script directly manipulates only the part of each calibrated generation
kernel lying inside the depletion region.  For tail scale s,

    g_s(z) proportional to g(z)                    for z < z_d
                         s * g(z)                  for z >= z_d

with each channel renormalized after scaling.  The exact modified kernels are
then used in both the forward current average and the kernel-aware one-mode fit.
Thus no coordinate-shape mismatch is introduced by the ablation.

If depletion overlap is causal, s=0 should collapse the false diffusion toward
zero and D_eff should grow systematically as the tail weight is restored.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np

import realistic_geometry_closure_stress as base
import paper02_geometry_parameter_sweep as sweep
from paper02_kernel_aware_depletion_frequency_law import kernel_aware_root


FREQUENCIES = np.asarray((0.0, 100e6, 500e6, 1e9), dtype=float)
TAIL_SCALES = (0.0, 0.10, 0.25, 0.50, 0.75, 1.0, 1.25, 1.50, 2.0)
DEPLETION_WIDTH_UM = 3.0
SPACE_CHARGE_DROP_V = 0.05
CAL_FREQ_HZ = 100e6


def density_integral(density):
    return float(np.trapezoid(density, base.OPT_Z_UM))


def density_mean(density):
    norm = density_integral(density)
    return float(np.trapezoid(base.OPT_Z_UM * density, base.OPT_Z_UM) / norm)


def modify_kernels(original_optics, tail_scale, depletion_start_um):
    mask_tail = base.OPT_Z_UM >= depletion_start_um
    modified = []
    metadata = []

    for channel, row in enumerate(original_optics):
        density0 = np.asarray(row[3], dtype=float)
        norm0 = density_integral(density0)
        if norm0 <= 0:
            raise ValueError("nonpositive kernel normalization")
        density0 = density0 / norm0

        original_overlap = float(
            np.trapezoid(density0[mask_tail], base.OPT_Z_UM[mask_tail])
        )
        original_mean = density_mean(density0)

        factor = np.ones_like(density0)
        factor[mask_tail] = float(tail_scale)
        density = density0 * factor
        norm = density_integral(density)
        if norm <= 0:
            raise ValueError("tail ablation removed entire kernel")
        density /= norm

        overlap = float(
            np.trapezoid(density[mask_tail], base.OPT_Z_UM[mask_tail])
        )
        mean = density_mean(density)

        new_row = list(row)
        new_row[3] = density
        modified.append(tuple(new_row))
        metadata.append(
            {
                "channel": int(channel),
                "original_mean_um": original_mean,
                "modified_mean_um": mean,
                "original_depletion_overlap": original_overlap,
                "modified_depletion_overlap": overlap,
            }
        )

    return modified, metadata


def solve_dw(gamma, frequency_hz):
    g2 = gamma * gamma
    M = np.asarray(((g2.real, gamma.real), (g2.imag, gamma.imag)), dtype=float)
    rhs = np.asarray((0.0, -2.0 * np.pi * frequency_hz), dtype=float)
    D, w = np.linalg.solve(M, rhs)
    return float(D), float(w)


def law_residual(gamma, f, D, w):
    if f <= 0:
        return 0.0
    rhs = -1j * 2.0 * np.pi * f
    return float(abs(D * gamma * gamma + w * gamma - rhs) / abs(rhs))


def run(args):
    original_optics = list(base.OPTICS)
    original_frequencies = base.FREQUENCIES
    base.FREQUENCIES = FREQUENCIES.copy()
    base.V_BIAS = float(args.bias_v)
    base.X_EXTENT_UM = float(args.x_extent_um)

    depletion_start_um = float(base.L_UM - DEPLETION_WIDTH_UM)
    scenario = base.Scenario(
        "planar_depletion",
        1.0,
        DEPLETION_WIDTH_UM,
        SPACE_CHARGE_DROP_V,
    )
    numerical = {
        "nx": args.nx,
        "nz": args.nz,
        "nx_src": args.nx_src,
        "nz_src": args.nz_src,
        "ds_um": args.ds_um,
    }

    result_rows = []
    overlap_rows = []

    try:
        for tail_scale in TAIL_SCALES:
            modified, meta = modify_kernels(
                original_optics,
                tail_scale,
                depletion_start_um,
            )
            base.OPTICS = modified

            J, diag = sweep.currents_with_beam(
                scenario,
                2.0,
                0.0,
                **numerical,
            )

            gammas = []
            fit_rels = []
            for jf, f in enumerate(FREQUENCIES):
                r, _, _, fit_rel = kernel_aware_root(J[jf])
                gammas.append(-r)
                fit_rels.append(float(fit_rel))
            gammas = np.asarray(gammas)

            idx = int(np.where(FREQUENCIES == CAL_FREQ_HZ)[0][0])
            D, w = solve_dw(gammas[idx], CAL_FREQ_HZ)
            residual_1g = law_residual(
                gammas[int(np.where(FREQUENCIES == 1e9)[0][0])],
                1e9,
                D,
                w,
            )

            overlaps = np.asarray([m["modified_depletion_overlap"] for m in meta])
            original_overlaps = np.asarray([m["original_depletion_overlap"] for m in meta])
            means = np.asarray([m["modified_mean_um"] for m in meta])

            result_rows.append(
                {
                    "tail_scale": float(tail_scale),
                    "effective_D_m2_per_s": D,
                    "effective_w_m_per_s": w,
                    "positive_D_w": bool(D > 0 and w > 0),
                    "law_residual_1ghz": residual_1g,
                    "max_kernel_one_mode_fit_rel": max(fit_rels),
                    "mean_depletion_overlap": float(np.mean(overlaps)),
                    "min_depletion_overlap": float(np.min(overlaps)),
                    "max_depletion_overlap": float(np.max(overlaps)),
                    "overlap_span": float(np.max(overlaps) - np.min(overlaps)),
                    "mean_modified_source_depth_um": float(np.mean(means)),
                    "source_depth_span_um": float(np.max(means) - np.min(means)),
                    "collected_fraction": float(diag["collected"]),
                    "dc_ramo_error": float(diag["dc_error"]),
                }
            )

            for m in meta:
                overlap_rows.append(
                    {
                        "tail_scale": float(tail_scale),
                        **m,
                    }
                )

    finally:
        base.OPTICS = original_optics
        base.FREQUENCIES = original_frequencies

    d0 = next(r["effective_D_m2_per_s"] for r in result_rows if r["tail_scale"] == 0.0)
    d1 = next(r["effective_D_m2_per_s"] for r in result_rows if r["tail_scale"] == 1.0)
    full_overlap_meta = [r for r in overlap_rows if r["tail_scale"] == 1.0]

    payload = {
        "status": "CONDITIONAL finite-kernel tail ablation",
        "geometry": {
            "absorber_thickness_um": float(base.L_UM),
            "depletion_start_um": depletion_start_um,
            "depletion_width_um": DEPLETION_WIDTH_UM,
            "space_charge_drop_v": SPACE_CHARGE_DROP_V,
            "bias_v": float(args.bias_v),
        },
        "tail_scales": list(TAIL_SCALES),
        "causal_gate": {
            "D_eff_tail_scale_0": d0,
            "D_eff_tail_scale_1": d1,
            "absolute_collapse_ratio": abs(d0) / max(abs(d1), 1e-30),
            "supported_if": "|D_eff(s=0)| << |D_eff(s=1)| with exact modified kernels used in forward and inverse models",
        },
        "physical_kernel_depletion_overlap_by_channel": [
            {
                "channel": r["channel"],
                "mean_depth_um": r["original_mean_um"],
                "depletion_overlap": r["original_depletion_overlap"],
            }
            for r in full_overlap_meta
        ],
        "results": result_rows,
    }

    out_results = Path(args.output_results)
    out_overlap = Path(args.output_overlap)
    out_summary = Path(args.output_summary)
    for p in (out_results, out_overlap, out_summary):
        p.parent.mkdir(parents=True, exist_ok=True)

    with out_results.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(result_rows[0].keys()))
        w.writeheader()
        w.writerows(result_rows)

    with out_overlap.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(overlap_rows[0].keys()))
        w.writeheader()
        w.writerows(overlap_rows)

    out_summary.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
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
    p.add_argument("--output-results", default="paper02_kernel_tail_ablation_results.csv")
    p.add_argument("--output-overlap", default="paper02_kernel_tail_ablation_overlap.csv")
    p.add_argument("--output-summary", default="paper02_kernel_tail_ablation_summary.json")
    return p


if __name__ == "__main__":
    run(parser().parse_args())
