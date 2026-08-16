"""Signed 100-MHz threshold scan for wavelength-calibration nuisance modes.

For each local wavelength-registration mode (common, channel-linear, channel-
curvature), determine which sign produces positive apparent diffusion in the
exact uniform-velocity D_micro=0 null, then quantify:

  * the amplitude where false D_eff equals the central heterogeneous exact
    counterexample D_eff at 100 MHz;
  * the associated maximum mean-depth shift;
  * the SNR ordering at that matched-D point;
  * finite crossovers between positive-D detection and one-mode rejection over
    a declared amplitude interval.

The mode amplitude A is in nm of wavelength offset.  For linear and curvature
modes, max(|mode|)=1, so |A| is the maximum channel wavelength offset.  These
are controlled theoretical directions, not experimental error bars.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np
from scipy.optimize import brentq

import realistic_geometry_closure_stress as base
import paper02_kernel_aware_depletion_frequency_law as law
import paper02_exact_planar_continuum_crosscheck as exact
import paper02_kernel_misspecification_stress as ks
from paper02_same_frequency_hidden_risk import analyze_one


F = 100e6
N = len(base.OPTICS)
LINEAR = np.linspace(-1.0, 1.0, N)
CURVATURE = LINEAR**2
CURVATURE -= np.mean(CURVATURE)
CURVATURE /= np.max(np.abs(CURVATURE))
MODES = {
    'common': np.ones(N),
    'linear': LINEAR,
    'curvature': CURVATURE,
}
SCAN_MAG_NM = np.asarray((1e-6,3e-6,1e-5,3e-5,1e-4,3e-4,1e-3,3e-3,1e-2,3e-2,1e-1,3e-1,1.0,3.0,5.0),float)


def build_points():
    z_m=ks.Z_M
    hetero=exact.exact_point_transfer(z_m,law.FREQUENCIES)
    v=exact.exact_speed_m_per_s(z_m)
    transit=float(np.trapezoid(1.0/v,z_m))
    vu=float(ks.L_M/transit)
    uniform=ks.uniform_point_transfer(vu)
    idx=int(np.where(law.FREQUENCIES==F)[0][0])
    return hetero[idx],uniform[idx],vu


def currents(point,kernels):
    return np.asarray([np.trapezoid(g*point,ks.Z_UM) for g in kernels],complex)


def eval100(point,mode,amplitude_nm,nominal):
    kernels=ks.wavelength_kernels(float(amplitude_nm)*mode)
    J=currents(point,kernels)
    r,_coeff,_model,fit=law.kernel_aware_root(J)
    gamma=-r
    D,w=law.solve_dw_one_frequency(gamma,F)
    stat=analyze_one(J,F)
    kd=ks.kernel_diagnostics(kernels,nominal)
    return {
        'D':float(D),'w':float(w),'fit':float(fit),
        'SD':float(stat['snr_required_positive_D_db']),
        'Srej':float(stat['snr_required_one_mode_rejection_db']),
        'hidden':bool(stat['positive_D_detectable_before_one_mode_rejection']),
        'max_mean_shift_nm':float(kd['max_abs_mean_shift_nm']),
        'rms_mean_shift_nm':float(kd['rms_mean_shift_nm']),
        'L1':float(kd['max_kernel_L1_distance']),
    }


def choose_positive_sign(point,mode,nominal):
    h=1e-4
    plus=eval100(point,mode,+h,nominal)['D']
    minus=eval100(point,mode,-h,nominal)['D']
    if plus>0 and plus>=minus:
        return +1
    if minus>0:
        return -1
    raise RuntimeError('no positive-D sign near zero')


def roots_from_grid(func,xs):
    roots=[]
    vals=[]
    for x in xs:
        vals.append(float(func(float(x))))
    for x0,x1,y0,y1 in zip(xs[:-1],xs[1:],vals[:-1],vals[1:]):
        if not(np.isfinite(y0) and np.isfinite(y1)):
            continue
        if y0==0:
            roots.append(float(x0))
        elif y0*y1<0:
            roots.append(float(brentq(func,float(x0),float(x1),xtol=1e-12,rtol=1e-11)))
    # de-duplicate
    out=[]
    for r in roots:
        if not out or abs(r-out[-1])>1e-8*max(1.0,abs(r)):
            out.append(r)
    return out


def run(args):
    point_h,point_u,vu=build_points()
    nominal=ks.nominal_kernels()
    J_h=currents(point_h,nominal)
    rh,*_=law.kernel_aware_root(J_h)
    D_target=float(law.solve_dw_one_frequency(-rh,F)[0])

    rows=[]; summary={}
    dense=np.geomspace(1e-6,5.0,120)
    for name,mode in MODES.items():
        sign=choose_positive_sign(point_u,mode,nominal)
        for mag in SCAN_MAG_NM:
            q=eval100(point_u,mode,sign*mag,nominal)
            rows.append({
                'mode':name,'positive_D_sign':sign,'magnitude_nm':float(mag),
                'signed_amplitude_nm':float(sign*mag),
                'D100_m2_per_s':q['D'],'w100_m_per_s':q['w'],'fit100_rel':q['fit'],
                'S_D_100_db':q['SD'],'S_reject_100_db':q['Srej'],'hidden_100':q['hidden'],
                'max_abs_mean_shift_nm':q['max_mean_shift_nm'],'rms_mean_shift_nm':q['rms_mean_shift_nm'],
                'max_kernel_L1_distance':q['L1'],
            })

        def ftarget(mag): return eval100(point_u,mode,sign*mag,nominal)['D']-D_target
        target_roots=roots_from_grid(ftarget,dense)
        target_mag=target_roots[0] if target_roots else None

        def forder(mag):
            q=eval100(point_u,mode,sign*mag,nominal)
            return q['SD']-q['Srej']
        cross=roots_from_grid(forder,dense)

        matched=None
        if target_mag is not None:
            q=eval100(point_u,mode,sign*target_mag,nominal)
            matched={
                'magnitude_nm':float(target_mag),
                'signed_amplitude_nm':float(sign*target_mag),
                'max_abs_mean_depth_shift_nm':q['max_mean_shift_nm'],
                'D100_m2_per_s':q['D'],'w100_m_per_s':q['w'],
                'S_D_100_db':q['SD'],'S_reject_100_db':q['Srej'],'hidden_100':q['hidden'],
                'fit100_rel':q['fit'],
            }
        summary[name]={
            'positive_D_sign':sign,
            'target_D_m2_per_s':D_target,
            'matched_target':matched,
            'ordering_crossover_magnitudes_nm':cross,
            'hidden_at_smallest_scanned_magnitude':bool(eval100(point_u,mode,sign*dense[0],nominal)['hidden']),
            'hidden_at_largest_scanned_magnitude':bool(eval100(point_u,mode,sign*dense[-1],nominal)['hidden']),
        }

    payload={
        'status':'CHECKED signed 100-MHz kernel-mode thresholds',
        'scope':{
            'uniform_transport_truth_D_micro':0.0,
            'uniform_velocity_m_per_s':vu,
            'inverse_uses_nominal_theoretical_kernels':True,
            'modes_are_controlled_theoretical_directions_not_error_bars':True,
        },
        'mode_vectors':{k:v.tolist() for k,v in MODES.items()},
        'heterogeneous_exact_target_D100_m2_per_s':D_target,
        'summary':summary,
        'rows':rows,
    }
    oc=Path(args.output_csv); oj=Path(args.output_summary)
    oc.parent.mkdir(parents=True,exist_ok=True); oj.parent.mkdir(parents=True,exist_ok=True)
    with oc.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    oj.write_text(json.dumps(payload,indent=2,sort_keys=True),encoding='utf-8')
    print(json.dumps(summary,indent=2,sort_keys=True))


def parser():
    p=argparse.ArgumentParser()
    p.add_argument('--output-csv',default='paper02_signed_kernel_mode_thresholds.csv')
    p.add_argument('--output-summary',default='paper02_signed_kernel_mode_thresholds_summary.json')
    return p


if __name__=='__main__':
    run(parser().parse_args())
