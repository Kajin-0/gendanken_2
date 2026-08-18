"""Targeted optimizer-integrity repair for the frozen coplanar 500-MHz bootstrap.

The statistical experiment is unchanged. Only the accelerated nonlinear root
optimizer is strengthened after the original three-start real-axis refit failed
the predeclared <=1.001 fast/full residual-ratio integrity check.

The calibrated six-channel fit admits the same spectral-alias branches already
searched by the full multistart fitter.  The repaired accelerated fitter therefore
starts around the baseline branch and its +/- 2*pi/0.5-um aliases, with the same
small real/imaginary perturbations around each admissible branch.  No noise seed,
bootstrap population, SNR coordinate, alpha, power rule, or integrity tolerance is
changed.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
import paper03_second_geometry_gate as cop
import paper03_stageA_resolvent as resolvent
import paper03_stageA_statistical_bootstrap as boot
import realistic_geometry_closure_stress as base

PERT=0.03
ALIAS_SPACING=2.0*np.pi/0.5

def robust_fast_refit(y, baseline_r):
    starts=[]
    for alias in (0.0,-ALIAS_SPACING,+ALIAS_SPACING):
        center=complex(baseline_r.real,baseline_r.imag+alias)
        if not (boot.ROOT_LOWER[1] < center.imag < boot.ROOT_UPPER[1]):
            continue
        starts.extend((
            np.asarray((center.real,center.imag),float),
            np.asarray((center.real+PERT,center.imag),float),
            np.asarray((center.real-PERT,center.imag),float),
            np.asarray((center.real,center.imag+PERT),float),
            np.asarray((center.real,center.imag-PERT),float),
        ))
    best=None
    for x0 in starts:
        x0=np.minimum(np.maximum(x0,boot.ROOT_LOWER+1e-10),boot.ROOT_UPPER-1e-10)
        opt=least_squares(
            lambda x: boot.profiled_residual(y,x),x0,
            bounds=(boot.ROOT_LOWER,boot.ROOT_UPPER),
            xtol=1e-10,ftol=1e-10,gtol=1e-10,max_nfev=100,
        )
        r=boot.profiled_residual(y,opt.x); n2=float(np.dot(r,r))
        if best is None or n2<best[0]:
            best=(n2,r,complex(float(opt.x[0]),float(opt.x[1])))
    if best is None: raise RuntimeError('robust fast refit failed')
    return best[1],best[2]

def main():
    boot.fast_refit=robust_fast_refit
    J,diag,_,_=cop.solve_grid(161,121,17)
    gate=boot.rf_gate(J,2)
    if gate['frequency_hz']!=float(base.FREQUENCIES[2]): raise AssertionError('RF mismatch')
    for c in gate['fast_refit_spot_checks_at_analytic_snr'].values():
        if c['max_fast_over_full_residual_norm_ratio']>1.001:
            raise AssertionError('repaired fast/full refit mismatch')
    out={
        'schema':'paper03-second-geometry-bootstrap-500-repair-v2',
        'status':'LOCKED COPLANAR 500-MHZ BOOTSTRAP OPTIMIZER REPAIR / NON-CLAIM',
        'repair_scope':'optimizer branch starts/tolerances only; statistical seeds/populations/SNR grid/alpha/power rule and <=1.001 integrity criterion unchanged',
        'optimizer':{
            'branch_centers':'baseline and admissible +/-2*pi/0.5-um spectral aliases',
            'local_starts':'center plus +/-0.03 real and +/-0.03 imaginary',
            'xtol':1e-10,'ftol':1e-10,'gtol':1e-10,'max_nfev':100,
        },
        'original_failed_job':95543826151,
        'grid':[161,121],'source_quadrature':17,'forward_diagnostics':diag,
        'bootstrap':{
            'alpha':boot.ALPHA,'target_power':boot.TARGET_POWER,
            'n_null':boot.N_NULL,'n_alt':boot.N_ALT,
            'snr_offsets_db':list(boot.SNR_OFFSETS_DB),
        },
        'rf_gate':gate,'science_interpretation_ready':False,
    }
    Path('paper03_second_geometry_bootstrap_500_repair.json').write_text(
        json.dumps(resolvent.json_safe(out),indent=2,allow_nan=False)+'\n'
    )
    print(gate['lowest_tested_snr_with_power_ge_0p90_db'],gate['predeclared_early_warning_condition_supported'],gate['conservative_tested_warning_margin_db'])
if __name__=='__main__': main()
