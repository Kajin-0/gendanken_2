"""Particle-count convergence gate for Paper 03 Stage A.

This file does not add physics.  It attacks the first numerical weakness exposed
by the Stage-A smoke artifact: finite-particle noise in the diffusion forward
calculation.  Two independent replicas are run at each particle count and the
replica disagreement is measured in both the spectral first differences and the
four-color phase statistic.

No result from this script is a detector-physics claim.  The initial precision
gate is intentionally tied to the frozen reference transport-phase scale so
that Monte-Carlo noise must become small compared with the effect the hierarchy
is eventually being asked to discriminate.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict
import json
from pathlib import Path
from typing import Any

import numpy as np

import paper03_combined_physics_challenge as stage
import realistic_geometry_closure_stress as base


PARTICLE_COUNTS = (24, 96, 384)
SEEDS = {
    24: (2001, 2002),
    96: (2101, 2102),
    384: (2201, 2202),
}

# This is a numerical-readiness coordinate, not a physical significance level.
# Before interpreting an O(1)-of-target confound, the independent-replica
# half-spread of the four-color phase should be <=5% of the frozen target at
# each nonzero RF.  A stricter gate may be adopted later, but not weakened after
# inspecting a desired scientific result.
MAX_PHASE_HALF_SPREAD_FRACTION_OF_TARGET = 0.05


def metric_map(blind: dict[str, Any]) -> dict[float, dict[str, Any]]:
    return {
        float(m["frequency_hz"]): m
        for m in blind["metrics"]
    }


def first_difference_disagreement(a: np.ndarray, b: np.ndarray) -> float:
    da = np.diff(np.asarray(a, complex), axis=1)
    db = np.diff(np.asarray(b, complex), axis=1)
    mean = 0.5 * (da + db)
    return float(
        np.linalg.norm(da - db)
        / max(np.linalg.norm(mean), np.finfo(float).tiny)
    )


def run_replica_pair(
    scenario: base.Scenario,
    particles: int,
    seed_a: int,
    seed_b: int,
    *,
    ds_um: float,
    rms_diffusion_step_um: float,
    nx: int,
    nz: int,
    nx_src: int,
    nz_src: int,
) -> dict[str, Any]:
    common = dict(
        diffusion_m2_s=2.5e-3,
        lifetime_s=float("inf"),
        particles_per_source=particles,
        ds_um=ds_um,
        nx=nx,
        nz=nz,
        nx_src=nx_src,
        nz_src=nz_src,
        rms_diffusion_step_um=rms_diffusion_step_um,
        max_time_s=5.0e-9,
        max_steps=12000,
    )
    ca = stage.StochasticConfig(seed=seed_a, **common)
    cb = stage.StochasticConfig(seed=seed_b, **common)

    Ja, da = stage.stochastic_currents(scenario, ca)
    Jb, db = stage.stochastic_currents(scenario, cb)
    Jm = 0.5 * (Ja + Jb)

    ba = stage.blind_analysis(Ja)
    bb = stage.blind_analysis(Jb)
    bm = stage.blind_analysis(Jm)
    ma, mb, mm = metric_map(ba), metric_map(bb), metric_map(bm)

    rf_rows = []
    for f in base.FREQUENCIES:
        f = float(f)
        if f <= 0.0:
            continue
        phase_a = float(ma[f]["closure4_phase_deg"])
        phase_b = float(mb[f]["closure4_phase_deg"])
        phase_mean = float(mm[f]["closure4_phase_deg"])
        half_spread = 0.5 * abs(phase_a - phase_b)
        target = abs(float(base.GRADIENT_TARGET_DEG[f]))
        frac = half_spread / target
        rf_rows.append(
            {
                "frequency_hz": f,
                "phase_replica_a_deg": phase_a,
                "phase_replica_b_deg": phase_b,
                "phase_replica_mean_deg": phase_mean,
                "phase_replica_half_spread_deg": float(half_spread),
                "phase_half_spread_fraction_of_frozen_target": float(frac),
                "mean_sigma2_over_sigma1": float(mm[f]["sigma2_over_sigma1"]),
                "mean_sigma3_over_sigma2": float(mm[f]["sigma3_over_sigma2"]),
                "mean_rank2_3sigma_current_step_snr_db": float(
                    mm[f]["rank2_3sigma_current_step_snr_db"]
                ),
                "principal_log_root_sum_imag_per_m": float(
                    mm[f]["root_sum_imag_per_m"]
                ),
            }
        )

    dc_err = max(
        float(da["max_endpoint_ramo_error"]),
        float(db["max_endpoint_ramo_error"]),
    )
    assert dc_err < 1e-12

    return {
        "particles_per_source": int(particles),
        "replica_seeds": [int(seed_a), int(seed_b)],
        "config_a": asdict(ca),
        "config_b": asdict(cb),
        "first_difference_replica_disagreement": first_difference_disagreement(Ja, Jb),
        "max_endpoint_ramo_error": dc_err,
        "replica_a_sampled_path_fractions": da["sampled_path_fractions"],
        "replica_b_sampled_path_fractions": db["sampled_path_fractions"],
        "rf_phase_rows": rf_rows,
        "blind_analysis_scope": (
            "Inherited raw six-channel geometry diagnostics only.  The full "
            "kernel-aware Paper-01 consistency inverse is not yet implemented "
            "in Stage A; principal-log root sums are therefore diagnostic, "
            "not a branch-controlled physical-root claim."
        ),
    }


def finite_json(obj: Any) -> Any:
    """Produce standards-compliant JSON without NaN/Infinity tokens."""
    if isinstance(obj, dict):
        return {str(k): finite_json(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [finite_json(v) for v in obj]
    if isinstance(obj, np.generic):
        return finite_json(obj.item())
    if isinstance(obj, float):
        if np.isnan(obj):
            return "nan"
        if np.isposinf(obj):
            return "inf"
        if np.isneginf(obj):
            return "-inf"
        return obj
    return obj


def fit_scaling(rows: list[dict[str, Any]]) -> dict[str, float]:
    n = np.asarray([r["particles_per_source"] for r in rows], float)
    e = np.asarray([r["first_difference_replica_disagreement"] for r in rows], float)
    slope, intercept = np.polyfit(np.log(n), np.log(e), 1)
    return {
        "loglog_slope": float(slope),
        "loglog_intercept": float(intercept),
        "expected_independent_sampling_slope": -0.5,
    }


def run(tier: str) -> dict[str, Any]:
    scenario = next(s for s in base.SCENARIOS if s.name == "finite75_depletion")
    if tier == "quick":
        counts = PARTICLE_COUNTS
        numerical = {
            "ds_um": 0.050,
            "rms_diffusion_step_um": 0.080,
            "nx": 81,
            "nz": 61,
            "nx_src": 5,
            "nz_src": 17,
        }
    else:
        raise ValueError(tier)

    rows = []
    for n in counts:
        a, b = SEEDS[n]
        print(f"particle convergence: N={n} seeds=({a},{b})", flush=True)
        rows.append(
            run_replica_pair(
                scenario,
                n,
                a,
                b,
                **numerical,
            )
        )

    phase_gate_rows = []
    for r in rows:
        worst = max(
            x["phase_half_spread_fraction_of_frozen_target"]
            for x in r["rf_phase_rows"]
        )
        phase_gate_rows.append(
            {
                "particles_per_source": r["particles_per_source"],
                "worst_phase_half_spread_fraction_of_frozen_target": float(worst),
                "initial_phase_precision_gate_passed": bool(
                    worst <= MAX_PHASE_HALF_SPREAD_FRACTION_OF_TARGET
                ),
            }
        )

    highest = phase_gate_rows[-1]
    return {
        "schema": "paper03-stageA-particle-convergence-v1",
        "status": "NUMERICAL CONVERGENCE GATE / NON-CLAIM",
        "tier": tier,
        "scenario": {
            "name": scenario.name,
            "contact_fraction": scenario.contact_fraction,
            "depletion_width_um": scenario.depletion_width_um,
            "space_charge_drop_v": scenario.space_charge_drop_v,
        },
        "hidden_forward_coordinate": {
            "diffusion_m2_s": 2.5e-3,
            "lifetime_s": "inf",
        },
        "numerical": numerical,
        "particle_rows": rows,
        "sampling_scaling": fit_scaling(rows),
        "initial_phase_precision_gate": {
            "definition": (
                "independent-replica four-color phase half-spread <= 5% of "
                "the frozen reference transport phase at every nonzero RF"
            ),
            "threshold_fraction": MAX_PHASE_HALF_SPREAD_FRACTION_OF_TARGET,
            "rows": phase_gate_rows,
            "highest_particle_count_passed": bool(
                highest["initial_phase_precision_gate_passed"]
            ),
        },
        "science_interpretation_ready": False,
        "remaining_before_interpretation": [
            "pass or tighten the particle precision gate",
            "perform trajectory-step / diffusion-step convergence",
            "implement the kernel-aware blind consistency analysis",
            "complete and independently validate Stage-B self-consistent semiconductor forward physics",
        ],
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--tier", choices=("quick",), default="quick")
    p.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("paper03_stageA_particle_convergence.json"),
    )
    args = p.parse_args()

    result = run(args.tier)
    args.output.write_text(
        json.dumps(finite_json(result), indent=2, allow_nan=False) + "\n",
        encoding="utf-8",
    )

    print(json.dumps(result["sampling_scaling"], indent=2))
    print(json.dumps(result["initial_phase_precision_gate"], indent=2))
    print("science_interpretation_ready = false")
    print(f"wrote {args.output}")
    print("PASS: numerical convergence study completed; no physics claim made.")


if __name__ == "__main__":
    main()
