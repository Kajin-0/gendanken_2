"""RF shard for the predeclared Paper-03 Stage-A bootstrap.

This is an execution-only wrapper around
``paper03_stageA_statistical_bootstrap.rf_gate``. It changes no statistical
coordinate: same deterministic forward case, SNR offsets, null/alternative
sample counts, seeds, nonlinear refit, alpha, and target power. The purpose is
only to run 100 MHz, 500 MHz, and 1 GHz concurrently in CI.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import paper03_stageA_kernel_blind_gate as kernel
import paper03_stageA_resolvent as resolvent
import paper03_stageA_statistical_bootstrap as boot
import realistic_geometry_closure_stress as base


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--rf-index", type=int, choices=(1, 2, 3), required=True)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()

    finite = next(s for s in base.SCENARIOS if s.name == "finite75_depletion")
    J, forward = kernel.build_fixed_field_case(
        finite,
        nx=201,
        nz=151,
        nx_src=17,
        diffusion_m2_s=2.5e-3,
        lifetime_s=float("inf"),
    )
    gate = boot.rf_gate(J, args.rf_index)

    for check in gate["fast_refit_spot_checks_at_analytic_snr"].values():
        if check["max_fast_over_full_residual_norm_ratio"] > 1.001:
            raise AssertionError(
                "fast bootstrap refit disagrees with full multistart fitter"
            )

    result = {
        "schema": "paper03-stageA-statistical-bootstrap-shard-v1",
        "status": "PREDECLARED PARAMETRIC BOOTSTRAP RF SHARD / NON-CLAIM",
        "execution_only_shard": True,
        "scientific_code_path": "paper03_stageA_statistical_bootstrap.rf_gate",
        "predeclaration": "PAPER03_STAGEA_STATISTICAL_PREDECLARATION_2026-08-17.md",
        "rf_index": args.rf_index,
        "bootstrap": {
            "alpha": boot.ALPHA,
            "target_power": boot.TARGET_POWER,
            "n_null_per_candidate": boot.N_NULL,
            "n_alternative_per_candidate": boot.N_ALT,
            "snr_offsets_from_analytic_db": list(boot.SNR_OFFSETS_DB),
            "empirical_null_quantile_method": "higher",
        },
        "forward": {
            "stage_B_self_consistent_semiconductor": False,
            "scenario": finite.__dict__,
            "diffusion_m2_s": 2.5e-3,
            "lifetime_s": "inf",
            "grid": [201, 151],
            "lateral_quadrature": 17,
            "diagnostics": forward,
        },
        "rf_gate": gate,
        "science_interpretation_ready": False,
    }
    args.output.write_text(
        json.dumps(resolvent.json_safe(result), indent=2, allow_nan=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(gate, indent=2))
    print("science_interpretation_ready = false")
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
