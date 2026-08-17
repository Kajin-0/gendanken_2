"""Post-gate adversarial refinement for the Paper-03 Stage-A resolvent.

The predeclared 2%-of-frozen-target grid gate already passed on the
121x91 -> 161x121 pair. Because that pass was close to the threshold, this
script adds a finer 201x151 solve without changing the gate or relabeling this
extra check as predeclared. It is confirmation only, not a new acceptance rule
and not a detector-physics claim.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import paper03_stageA_resolvent as r
import realistic_geometry_closure_stress as base


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name(
            "paper03_stageA_resolvent_extended_check.json"
        ),
    )
    args = p.parse_args()

    scenario = next(s for s in base.SCENARIOS if s.name == "finite75_depletion")
    grids = ((121, 91), (161, 121), (201, 151))
    cases = []
    for nx, nz in grids:
        print(f"post-gate resolvent grid {nx}x{nz}", flush=True)
        cfg = r.ResolventConfig(
            diffusion_m2_s=2.5e-3,
            lifetime_s=float("inf"),
            nx=nx,
            nz=nz,
            nx_src=13,
        )
        cases.append(r.run_case(scenario, cfg))

    pairs = []
    for a, b in zip(cases[:-1], cases[1:]):
        pairs.append(
            {
                "from_grid": [a["config"]["nx"], a["config"]["nz"]],
                "to_grid": [b["config"]["nx"], b["config"]["nz"]],
                **r.convergence_pair(a, b),
            }
        )

    result = {
        "schema": "paper03-stageA-resolvent-postgate-v1",
        "status": "POST-GATE ADVERSARIAL REFINEMENT / NON-CLAIM",
        "predeclared_gate_changed": False,
        "predeclared_gate_threshold_fraction": 0.02,
        "reason": (
            "The 121x91 -> 161x121 pair passed the predeclared 2% phase-scale "
            "gate at a worst fraction of 0.0199410, close enough to justify "
            "one finer confirmation grid."
        ),
        "scenario": scenario.__dict__,
        "cases": cases,
        "grid_pairs": pairs,
        "postgate_finest_pair_below_original_threshold": bool(
            pairs[-1]["worst_phase_change_fraction_of_frozen_target"] <= 0.02
        ),
        "science_interpretation_ready": False,
        "remaining_before_interpretation": [
            "stochastic cross-formulation check at coarse observables",
            "source-quadrature convergence",
            "kernel-aware blind consistency inverse",
            "Stage-B self-consistent semiconductor forward-model validation",
        ],
    }

    args.output.write_text(
        json.dumps(r.json_safe(result), indent=2, allow_nan=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result["grid_pairs"], indent=2))
    print(
        "postgate_finest_pair_below_original_threshold =",
        result["postgate_finest_pair_below_original_threshold"],
    )
    print("science_interpretation_ready = false")
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
