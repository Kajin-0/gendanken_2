"""Locked one-mode parametric-bootstrap shard for the Paper-03 coplanar family.

The statistical contract is inherited unchanged from the predeclared Stage-A
bootstrap.  The coplanar topology uses a hardened local root optimizer because
the original three-start real-axis implementation failed its frozen fast/full
refit-integrity gate at 500 MHz.  This is an implementation repair, not a
change to noise draws, alpha, power, SNR grid, model, bounds, or the 1.001
agreement criterion.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
import paper03_second_geometry_gate as cop
import paper03_stageA_resolvent as resolvent
import paper03_stageA_statistical_bootstrap as boot
import realistic_geometry_closure_stress as base


def coplanar_fast_refit(y: np.ndarray, baseline_r: complex):
    """Profile A,B exactly and harden only the coplanar root minimization."""
    d = boot.FAST_ROOT_PERTURB
    offsets = (
        0j, d, -d, 1j*d, -1j*d,
        d+1j*d, d-1j*d, -d+1j*d, -d-1j*d,
    )
    best = None
    for off in offsets:
        z0 = baseline_r + off
        x0 = np.asarray((z0.real, z0.imag), float)
        x0 = np.minimum(np.maximum(x0, boot.ROOT_LOWER + 1e-10), boot.ROOT_UPPER - 1e-10)
        opt = least_squares(
            lambda x: boot.profiled_residual(y, x),
            x0,
            bounds=(boot.ROOT_LOWER, boot.ROOT_UPPER),
            xtol=1e-10,
            ftol=1e-10,
            gtol=1e-10,
            max_nfev=120,
        )
        residual = boot.profiled_residual(y, opt.x)
        norm2 = float(np.dot(residual, residual))
        if best is None or norm2 < best[0]:
            best = (norm2, residual, complex(float(opt.x[0]), float(opt.x[1])))
    if best is None:
        raise RuntimeError("coplanar fast nonlinear refit failed")
    return best[1], best[2]


def main():
    p=argparse.ArgumentParser(); p.add_argument("--rf-index",type=int,choices=(1,2,3),required=True); p.add_argument("--output",type=Path,required=True); a=p.parse_args()
    J,diag,_,_=cop.solve_grid(161,121,17)

    # Use the hardened optimizer inside the otherwise unchanged locked rf_gate.
    original_fast_refit = boot.fast_refit
    boot.fast_refit = coplanar_fast_refit
    try:
        gate=boot.rf_gate(J,a.rf_index)
    finally:
        boot.fast_refit = original_fast_refit

    if gate["frequency_hz"] != float(base.FREQUENCIES[a.rf_index]): raise AssertionError("RF mismatch")
    for check in gate["fast_refit_spot_checks_at_analytic_snr"].values():
        if check["max_fast_over_full_residual_norm_ratio"]>1.001: raise AssertionError("fast/full refit mismatch")
    out={"schema":"paper03-second-geometry-bootstrap-shard-v2","status":"LOCKED COPLANAR PARAMETRIC BOOTSTRAP / NON-CLAIM","lock":"PAPER03_SECOND_GEOMETRY_ANALYSIS_LOCK_2026-08-17.md","optimizer_repair":{"reason":"v1 three-start real-axis optimizer failed frozen 1.001 fast/full integrity gate at 500 MHz","statistical_contract_changed":False,"noise_draws_changed":False,"alpha_power_snr_grid_changed":False,"fast_full_gate_changed":False,"starts":"baseline plus symmetric real/imaginary/diagonal +/-0.03 per um","max_nfev":120,"tolerances":1e-10},"grid":[161,121],"source_quadrature":17,"forward_diagnostics":diag,"bootstrap":{"alpha":boot.ALPHA,"target_power":boot.TARGET_POWER,"n_null":boot.N_NULL,"n_alt":boot.N_ALT,"snr_offsets_db":list(boot.SNR_OFFSETS_DB)},"rf_gate":gate,"science_interpretation_ready":False}
    a.output.write_text(json.dumps(resolvent.json_safe(out),indent=2,allow_nan=False)+"\n")
    print(gate["frequency_hz"],gate["predeclared_early_warning_condition_supported"],gate["conservative_tested_warning_margin_db"])

if __name__=="__main__": main()
