"""Execution-only selected-point bootstrap shard for Paper 03 Stage A.

The selected detector coordinates are fixed by
PAPER03_STAGEA_REGIME_MAP_PREDECLARATION_2026-08-17.md Section 12 and recorded
before output inspection in
PAPER03_STAGEA_SELECTED_BOOTSTRAP_EXECUTION_LOCK_2026-08-17.md.

This wrapper deliberately reuses paper03_stageA_statistical_bootstrap.rf_gate()
without changing alpha, power, sample counts, SNR offsets, noise convention,
nonlinear refit, or deterministic seed schedule.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import paper03_stageA_regime_refine as refine
import paper03_stageA_resolvent as resolvent
import paper03_stageA_statistical_bootstrap as bootstrap
import realistic_geometry_closure_stress as base


POINTS = {
    "R2_A04": {
        "manifest_id": "R2_A04",
        "selection_reasons": [
            "S2_worst_warning_margin_order_one",
            "S3_closest_analytic_warning_boundary",
        ],
        "contact_fraction": 0.50,
        "depletion_width_um": 0.0,
        "space_charge_drop_v": 0.0,
        "diffusion_m2_s": 2.5e-3,
        "lifetime_s": "inf",
        "beam_sigma_um": 2.0,
        "beam_center_um": 0.0,
    },
    "R1_B04": {
        "manifest_id": "R1_B04",
        "selection_reasons": [
            "S1_maximum_confound",
            "S6_optical_offset_stress",
        ],
        "contact_fraction": 0.50,
        "depletion_width_um": 3.0,
        "space_charge_drop_v": 0.05,
        "diffusion_m2_s": 2.5e-3,
        "lifetime_s": "inf",
        "beam_sigma_um": 1.0,
        "beam_center_um": 1.5,
    },
}


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--manifest-id", choices=tuple(POINTS), required=True)
    p.add_argument("--rf-index", type=int, choices=(1, 2, 3), required=True)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()

    point = dict(POINTS[args.manifest_id])
    J, diagnostics = refine.solve_coordinate(point, 201, 151)
    gate = bootstrap.rf_gate(J, args.rf_index)

    expected_f = float(base.FREQUENCIES[args.rf_index])
    if gate["frequency_hz"] != expected_f:
        raise AssertionError("RF-index/frequency mismatch")
    for check in gate["fast_refit_spot_checks_at_analytic_snr"].values():
        if check["max_fast_over_full_residual_norm_ratio"] > 1.001:
            raise AssertionError("fast bootstrap refit disagrees with full multistart fitter")

    result = {
        "schema": "paper03-stageA-selected-bootstrap-shard-v1",
        "status": "PREDECLARED SELECTED-POINT PARAMETRIC BOOTSTRAP / NON-CLAIM",
        "predeclaration": "PAPER03_STAGEA_REGIME_MAP_PREDECLARATION_2026-08-17.md",
        "execution_lock": "PAPER03_STAGEA_SELECTED_BOOTSTRAP_EXECUTION_LOCK_2026-08-17.md",
        "manifest_id": args.manifest_id,
        "selection_reasons": point["selection_reasons"],
        "coordinate": {
            k: point[k]
            for k in (
                "contact_fraction",
                "depletion_width_um",
                "space_charge_drop_v",
                "diffusion_m2_s",
                "lifetime_s",
                "beam_sigma_um",
                "beam_center_um",
            )
        },
        "forward": {
            "stage_B_self_consistent_semiconductor": False,
            "grid": [201, 151],
            "lateral_quadrature": 17,
            "solver_diagnostics": diagnostics,
        },
        "bootstrap": {
            "alpha": bootstrap.ALPHA,
            "target_power": bootstrap.TARGET_POWER,
            "n_null_per_candidate": bootstrap.N_NULL,
            "n_alternative_per_candidate": bootstrap.N_ALT,
            "snr_offsets_from_analytic_db": list(bootstrap.SNR_OFFSETS_DB),
            "seed_schedule": "unchanged paper03_stageA_statistical_bootstrap.rf_gate common-random-number schedule",
        },
        "rf_gate": gate,
        "science_interpretation_ready": False,
    }

    args.output.write_text(
        json.dumps(resolvent.json_safe(result), indent=2, allow_nan=False) + "\n",
        encoding="utf-8",
    )
    print(args.manifest_id, expected_f, gate["predeclared_early_warning_condition_supported"])
    print("analytic SNR dB =", gate["analytic"]["required_snr_db"])
    print("lowest tested >=90% dB =", gate["lowest_tested_snr_with_power_ge_0p90_db"])
    print("claim SNR dB =", gate["frozen_transport_claim_snr_db"])
    print("tested warning margin dB =", gate["conservative_tested_warning_margin_db"])
    print("science_interpretation_ready = false")


if __name__ == "__main__":
    main()
