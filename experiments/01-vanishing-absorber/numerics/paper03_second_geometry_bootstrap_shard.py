"""Locked one-mode parametric-bootstrap shard for the Paper-03 coplanar family."""
from __future__ import annotations
import argparse, json
from pathlib import Path
import paper03_second_geometry_gate as cop
import paper03_stageA_resolvent as resolvent
import paper03_stageA_statistical_bootstrap as boot
import realistic_geometry_closure_stress as base


def main():
    p=argparse.ArgumentParser(); p.add_argument("--rf-index",type=int,choices=(1,2,3),required=True); p.add_argument("--output",type=Path,required=True); a=p.parse_args()
    J,diag,_,_=cop.solve_grid(161,121,17)
    gate=boot.rf_gate(J,a.rf_index)
    if gate["frequency_hz"] != float(base.FREQUENCIES[a.rf_index]): raise AssertionError("RF mismatch")
    for check in gate["fast_refit_spot_checks_at_analytic_snr"].values():
        if check["max_fast_over_full_residual_norm_ratio"]>1.001: raise AssertionError("fast/full refit mismatch")
    out={"schema":"paper03-second-geometry-bootstrap-shard-v1","status":"LOCKED COPLANAR PARAMETRIC BOOTSTRAP / NON-CLAIM","lock":"PAPER03_SECOND_GEOMETRY_ANALYSIS_LOCK_2026-08-17.md","grid":[161,121],"source_quadrature":17,"forward_diagnostics":diag,"bootstrap":{"alpha":boot.ALPHA,"target_power":boot.TARGET_POWER,"n_null":boot.N_NULL,"n_alt":boot.N_ALT,"snr_offsets_db":list(boot.SNR_OFFSETS_DB)},"rf_gate":gate,"science_interpretation_ready":False}
    a.output.write_text(json.dumps(resolvent.json_safe(out),indent=2,allow_nan=False)+"\n")
    print(gate["frequency_hz"],gate["predeclared_early_warning_condition_supported"],gate["conservative_tested_warning_margin_db"])

if __name__=="__main__": main()
