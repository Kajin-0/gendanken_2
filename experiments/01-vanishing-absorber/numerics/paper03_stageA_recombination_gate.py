"""Finite-recombination numerical gate for Paper 03 Stage A.

The deterministic backward resolvent already includes independent exponential
bulk killing through kappa=1/tau. This script validates the originally declared
Stage-A sensitivity coordinate tau=5 ns without changing the fixed-field
geometry model into a self-consistent semiconductor calculation.

The same numerical discipline used for the infinite-lifetime case is retained:
spatial refinement, lateral source-quadrature refinement, same-physics planar
reference, and the calibrated arbitrary-kernel one-mode fit. No fitted spatial
root is assigned a microscopic mechanism in this gate.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

import paper03_stageA_kernel_blind_gate as kernel
import paper03_stageA_resolvent as resolvent
import realistic_geometry_closure_stress as base


D_M2_S = 2.5e-3
TAU_S = 5.0e-9
SPATIAL_PHASE_FRACTION_GATE = 0.02
SOURCE_PHASE_FRACTION_GATE = 0.005


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("paper03_stageA_recombination_gate.json"),
    )
    args = p.parse_args()

    finite = next(s for s in base.SCENARIOS if s.name == "finite75_depletion")
    planar = next(s for s in base.SCENARIOS if s.name == "planar")

    J161, d161 = kernel.build_fixed_field_case(
        finite,
        nx=161,
        nz=121,
        nx_src=17,
        diffusion_m2_s=D_M2_S,
        lifetime_s=TAU_S,
    )
    J201, d201 = kernel.build_fixed_field_case(
        finite,
        nx=201,
        nz=151,
        nx_src=17,
        diffusion_m2_s=D_M2_S,
        lifetime_s=TAU_S,
    )

    # Pure lateral quadrature refinement on the same 201x151 killed resolvent.
    cfg = resolvent.ResolventConfig(
        diffusion_m2_s=D_M2_S,
        lifetime_s=TAU_S,
        nx=201,
        nz=151,
        nx_src=17,
    )
    gen = resolvent.build_generator(finite, cfg)
    U, drepeat = resolvent.solve_resolvent(gen, cfg)
    J201_13 = kernel.integrate_full_support(gen, U, 13)
    J201_17_repeat = kernel.integrate_full_support(gen, U, 17)
    repeat_rel = float(
        np.linalg.norm(J201_17_repeat - J201)
        / max(np.linalg.norm(J201), np.finfo(float).tiny)
    )
    if repeat_rel >= 1e-12:
        raise AssertionError(f"201x151 repeat integration mismatch: {repeat_rel}")

    grid = kernel.compare_phase_change(J161, J201)
    source = kernel.compare_phase_change(J201_13, J201)
    spatial_pass = (
        grid["worst_change_fraction_of_frozen_target"]
        <= SPATIAL_PHASE_FRACTION_GATE
    )
    source_pass = (
        source["worst_change_fraction_of_frozen_target"]
        <= SOURCE_PHASE_FRACTION_GATE
    )

    Jplanar, dplanar = kernel.build_fixed_field_case(
        planar,
        nx=201,
        nz=151,
        nx_src=17,
        diffusion_m2_s=D_M2_S,
        lifetime_s=TAU_S,
    )

    pf = kernel.raw_phase_map(J201)
    pp = kernel.raw_phase_map(Jplanar)
    baseline = []
    for f in base.FREQUENCIES:
        f = float(f)
        if f <= 0.0:
            continue
        excess = pf[f] - pp[f]
        target = float(base.GRADIENT_TARGET_DEG[f])
        baseline.append(
            {
                "frequency_hz": f,
                "finite_raw_phase_deg": pf[f],
                "planar_same_physics_raw_phase_deg": pp[f],
                "finite_minus_planar_phase_deg": excess,
                "signed_fraction_of_frozen_transport_target": excess / target,
                "absolute_fraction_of_frozen_transport_target": abs(excess / target),
            }
        )

    finite_fit = kernel.fit_frequency_table(J201)
    planar_fit = kernel.fit_frequency_table(Jplanar)

    result = {
        "schema": "paper03-stageA-recombination-v1",
        "status": "FINITE-RECOMBINATION NUMERICAL / KERNEL GATE; NON-CLAIM",
        "forward": {
            "stage": "A",
            "self_consistent_semiconductor": False,
            "scenario": finite.__dict__,
            "diffusion_m2_s": D_M2_S,
            "lifetime_s": TAU_S,
            "kappa_per_s": 1.0 / TAU_S,
            "recombination_model": "independent exponential bulk killing in the backward resolvent",
        },
        "numerical_checks": {
            "finite_161": d161,
            "finite_201": d201,
            "repeat_201_solver": drepeat,
            "grid_161_to_201": {
                **grid,
                "predeclared_threshold_fraction": SPATIAL_PHASE_FRACTION_GATE,
                "passed": bool(spatial_pass),
            },
            "source_quadrature_13_to_17": {
                **source,
                "predeclared_threshold_fraction": SOURCE_PHASE_FRACTION_GATE,
                "passed": bool(source_pass),
            },
            "repeat_relative_error": repeat_rel,
            "planar_201": dplanar,
        },
        "same_physics_planar_reference": baseline,
        "kernel_aware_one_mode_fits": {
            "finite75_depletion": finite_fit,
            "planar": planar_fit,
        },
        "root_interpretation_allowed": False,
        "science_interpretation_ready": False,
        "remaining_before_interpretation": [
            "kernel-aware model-order/statistical calibration",
            "stochastic coarse-observable cross-formulation validation",
            "broader diffusion/lifetime regime map",
            "Stage-B self-consistent semiconductor validation",
        ],
    }

    args.output.write_text(
        json.dumps(resolvent.json_safe(result), indent=2, allow_nan=False) + "\n",
        encoding="utf-8",
    )

    print("grid:", json.dumps(result["numerical_checks"]["grid_161_to_201"], indent=2))
    print("source:", json.dumps(result["numerical_checks"]["source_quadrature_13_to_17"], indent=2))
    print("baseline:", json.dumps(baseline, indent=2))
    for label, rows in result["kernel_aware_one_mode_fits"].items():
        print(label)
        for row in rows:
            print(
                row["frequency_hz"],
                row["central4"]["contrast_normalized_residual"],
                row["all6"]["contrast_normalized_residual"],
            )
    print("science_interpretation_ready = false")
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
