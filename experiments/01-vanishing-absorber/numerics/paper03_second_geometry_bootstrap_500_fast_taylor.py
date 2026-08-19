"""Accelerated integrity-gated 500-MHz coplanar bootstrap.

This changes only the accelerated nonlinear root optimizer.  The statistical
experiment, deterministic currents, noise seeds/populations, SNR grid, alpha,
power target, empirical quantile rule, and <=1.001 fast/full integrity gate are
unchanged.

The six calibrated kernel moments are analytic in complex r. Around the three
already-admissible spectral-alias branch centers (baseline and +/-2*pi/0.5 um),
we precompute a 14th-order Taylor expansion of the *exact full-kernel moments*.
The Taylor model is used only to locate a local optimum. Each candidate is then
scored with the original exact full-kernel profiled residual; the lowest exact
residual is returned. The existing rf_gate fixed 12-draw full-multistart spot
check remains authoritative and must satisfy <=1.001 before the result passes.
"""
from __future__ import annotations

import json
from math import factorial
from pathlib import Path

import numpy as np
from scipy.optimize import least_squares

import paper03_second_geometry_gate as cop
import paper03_stageA_kernel_blind_gate as kernel
import paper03_stageA_resolvent as resolvent
import paper03_stageA_statistical_bootstrap as boot
import realistic_geometry_closure_stress as base

ORDER = 14
ALIAS_SPACING = 2.0*np.pi/0.5
LOCAL_HALF_WIDTH = 1.5
_CACHE = {}


def _branch_data(baseline_r: complex):
    key=(round(float(baseline_r.real),12),round(float(baseline_r.imag),12))
    if key in _CACHE:
        return _CACHE[key]
    z=np.asarray(kernel.Z_UM,float)-float(kernel.Z_REF_UM)
    branches=[]
    for alias in (0.0,-ALIAS_SPACING,+ALIAS_SPACING):
        c=complex(baseline_r.real,baseline_r.imag+alias)
        if not (boot.ROOT_LOWER[1] < c.imag < boot.ROOT_UPPER[1]):
            continue
        e=np.exp(c*z)
        deriv=[]
        for k in range(ORDER+1):
            deriv.append((kernel.KERNEL_MATRIX @ (e*(z**k)))/factorial(k))
        branches.append((c,np.asarray(deriv,complex)))
    _CACHE[key]=branches
    return branches


def _moment_taylor(r: complex, center: complex, deriv: np.ndarray) -> np.ndarray:
    d=r-center
    powers=np.asarray([d**k for k in range(ORDER+1)],complex)
    return powers @ deriv


def _profile_taylor(y: np.ndarray, x: np.ndarray, center: complex, deriv: np.ndarray) -> np.ndarray:
    r=complex(float(x[0]),float(x[1]))
    M=_moment_taylor(r,center,deriv)
    mscale=max(float(np.linalg.norm(M)),np.finfo(float).tiny)
    X=np.column_stack((np.ones(len(boot.ALL6),dtype=complex),M/mscale))
    coeff,*_=np.linalg.lstsq(X,y,rcond=None)
    residual=X@coeff-y
    return np.concatenate((residual.real,residual.imag))


def taylor_fast_refit(y: np.ndarray, baseline_r: complex):
    candidates=[]
    for center,deriv in _branch_data(baseline_r):
        lo=np.maximum(boot.ROOT_LOWER,np.asarray((center.real-LOCAL_HALF_WIDTH,center.imag-LOCAL_HALF_WIDTH)))
        hi=np.minimum(boot.ROOT_UPPER,np.asarray((center.real+LOCAL_HALF_WIDTH,center.imag+LOCAL_HALF_WIDTH)))
        x0=np.asarray((center.real,center.imag),float)
        opt=least_squares(
            lambda x:_profile_taylor(y,x,center,deriv),x0,bounds=(lo,hi),
            xtol=1e-10,ftol=1e-10,gtol=1e-10,max_nfev=60,
        )
        # Scientific/statistical score remains the exact original full-kernel residual.
        exact=boot.profiled_residual(y,opt.x)
        n2=float(np.dot(exact,exact))
        candidates.append((n2,exact,complex(float(opt.x[0]),float(opt.x[1]))))
    if not candidates:
        raise RuntimeError('Taylor accelerated refit found no admissible branch')
    candidates.sort(key=lambda row:row[0])
    return candidates[0][1],candidates[0][2]


def main():
    boot.fast_refit=taylor_fast_refit
    J,diag,_,_=cop.solve_grid(161,121,17)
    gate=boot.rf_gate(J,2)
    if gate['frequency_hz'] != 500e6:
        raise AssertionError('RF mismatch')
    max_ratio=max(c['max_fast_over_full_residual_norm_ratio'] for c in gate['fast_refit_spot_checks_at_analytic_snr'].values())
    if max_ratio>1.001:
        raise AssertionError(f'Taylor fast/full refit mismatch: {max_ratio}')
    out={
        'schema':'paper03-second-geometry-bootstrap-500-fast-taylor-v1',
        'status':'LOCKED 500-MHZ BOOTSTRAP / OPTIMIZER-ONLY ACCELERATION / NON-CLAIM',
        'statistical_contract_changed':False,
        'optimizer':{
            'branch_centers':'baseline and admissible +/-2*pi/0.5-um aliases',
            'kernel_moment_locator':'14th-order local Taylor expansion of exact full-kernel moments',
            'local_half_width_per_um':LOCAL_HALF_WIDTH,
            'scientific_score':'original exact full-kernel profiled residual at each located root',
            'full_multistart_integrity_gate':0.001,
            'max_fast_over_full_residual_norm_ratio':float(max_ratio),
        },
        'forward_diagnostics':diag,
        'bootstrap':{
            'alpha':boot.ALPHA,'target_power':boot.TARGET_POWER,
            'n_null':boot.N_NULL,'n_alt':boot.N_ALT,
            'snr_offsets_db':list(boot.SNR_OFFSETS_DB),
        },
        'rf_gate':gate,
        'science_interpretation_ready':False,
    }
    Path('paper03_second_geometry_bootstrap_500_fast_taylor.json').write_text(
        json.dumps(resolvent.json_safe(out),indent=2,allow_nan=False)+'\n'
    )
    print('lowest=',gate['lowest_tested_snr_with_power_ge_0p90_db'])
    print('margin=',gate['conservative_tested_warning_margin_db'])
    print('max fast/full=',max_ratio)

if __name__=='__main__':
    main()
