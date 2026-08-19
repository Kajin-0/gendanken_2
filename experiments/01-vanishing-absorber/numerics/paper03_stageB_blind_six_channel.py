"""Final generic Stage-B blind six-channel gate for Paper 03.

Implements PAPER03_STAGEB_BLIND_SIX_CHANNEL_LOCK_2026-08-18.md.
The forward generator and blind analyzer are separated by an explicit data-only
interface.  The blind analyzer receives currents, RF coordinates, and calibrated
discrete depth kernels only; it never receives psi, n, geometry/contact labels,
or generator coefficients.
"""
from __future__ import annotations

import argparse
import json
from dataclasses import replace
from pathlib import Path
from typing import Any

import numpy as np
from scipy.sparse import identity
from scipy.sparse.linalg import spsolve

import paper03_combined_physics_challenge as stage
import paper03_stageA_kernel_blind_gate as one
import paper03_stageA_kernel_two_mode as two
import paper03_stageA_resolvent as resolvent
import paper03_stageA_statistical_bootstrap as boot
import paper03_stageB_mesh_weighting_reciprocity as stageb_gate
import paper03_stageB_operating_state as op
import realistic_geometry_closure_stress as base


MESHES=((51,39),(61,47))
FREQUENCIES=np.asarray((0.0,100e6,500e6,1e9),float)
X_SIGMA_M=2.0e-6
X_SUPPORT_M=3.5e-6
SHAPE_GATE=0.02
PHASE_TARGET_GATE=0.02
ROOT_STABILITY_GATE=0.05
ROOT_LAW_NUMERICAL_FACTOR=5.0
ORDER_ONE_MIMIC=0.5
ALL6=np.arange(6,dtype=int)


def json_complex(z: complex)->dict[str,float]:
    return {'real':float(np.real(z)),'imag':float(np.imag(z))}


def array_complex(a: np.ndarray)->dict[str,list]:
    a=np.asarray(a,complex)
    return {'real':a.real.tolist(),'imag':a.imag.tolist()}


def build_sources(nx:int,nz:int,p:op.Params)->tuple[np.ndarray,np.ndarray,np.ndarray]:
    x=op.xs(nx,p)
    z=(np.arange(nz)+0.5)*p.thickness_m/nz
    zum=z*1e6
    beam=np.exp(-0.5*(x/X_SIGMA_M)**2)
    beam=np.where(np.abs(x)<=X_SUPPORT_M,beam,0.0)
    if not np.any(beam>0): raise AssertionError('empty lateral source support')
    depth=[]
    sources=[]
    for optical in base.OPTICS:
        kz=np.interp(zum,np.asarray(base.OPT_Z_UM,float),np.asarray(optical[3],float))
        kz=np.maximum(kz,0.0)
        if not np.any(kz>0): raise AssertionError('empty depth kernel')
        raw=kz[:,None]*beam[None,:]
        s=raw/max(float(np.sum(raw)),np.finfo(float).tiny)
        sources.append(s.ravel())
        depth.append(np.sum(s,axis=1))
    S=np.asarray(sources,float)
    G=np.asarray(depth,float)
    if np.max(np.abs(S.sum(axis=1)-1.0))>1e-12: raise AssertionError('2-D source normalization failed')
    if np.max(np.abs(G.sum(axis=1)-1.0))>1e-12: raise AssertionError('depth calibration normalization failed')
    return S,zum,G


def solve_structure(p:op.Params,nx:int,nz:int)->tuple[np.ndarray,np.ndarray,dict[str,Any],np.ndarray]:
    psi,n,hist=op.solve(nx,nz,p)
    cur=op.currents(nx,nz,psi,n,p)
    final=hist[-1]
    if final['poisson_relative_residual']>=1e-8 or final['continuity_relative_residual']>=1e-8:
        raise AssertionError('operating residual gate failed')
    if cur['horizontal_cut_max_fractional_deviation']>=1e-5 or cur['terminal_balance_fraction']>=1e-5:
        raise AssertionError('operating current gate failed')
    if np.min(n)<=0 or not np.all(np.isfinite(n)): raise AssertionError('operating density gate failed')
    phi,wd=stageb_gate.solve_weighting(nx,nz,p)
    Q,F,bsel,bother,qramo,odiag=stageb_gate.frozen_operators(psi,phi,p)
    S,zum,G=build_sources(nx,nz,p)
    N=nx*nz
    I=identity(N,format='csr',dtype=complex)
    J=np.zeros((len(FREQUENCIES),6),complex)
    linear=[]
    for kf,f in enumerate(FREQUENCIES):
        if f==0:
            A=(-Q).tocsc(); rhs=qramo.astype(float)
        else:
            A=(1j*2*np.pi*f*I-Q).tocsc(); rhs=qramo.astype(complex)
        H=spsolve(A,rhs)
        rr=stageb_gate.relres(A,H,rhs)
        if rr>=1e-8: raise AssertionError(f'spectral backward residual failed at {f}: {rr}')
        J[kf]=S@H
        linear.append({'frequency_hz':float(f),'relative_residual':float(rr)})
    diag={
        'grid':[nx,nz],
        'iterations':len(hist),
        'final_iteration':final,
        'current':cur,
        'min_n_over_Nd':float(np.min(n)/p.donor_density_m3),
        'weighting':wd,
        'operator_diagnostics':odiag,
        'spectral_backward_solves':linear,
        'source_normalization_max_error':float(np.max(np.abs(S.sum(axis=1)-1))),
    }
    return J,G,diag,zum


def raw_phase_map(J:np.ndarray)->dict[float,float]:
    metrics=stage.blind_analysis(np.asarray(J,complex))['metrics']
    return {float(m['frequency_hz']):float(m['closure4_phase_deg']) for m in metrics}


def affine_shape_error(a:np.ndarray,b:np.ndarray)->float:
    """Best complex affine map a->b, normalized by fine contrast."""
    a=np.asarray(a,complex); b=np.asarray(b,complex)
    X=np.column_stack((np.ones(len(a),complex),a))
    coef,*_=np.linalg.lstsq(X,b,rcond=None)
    r=X@coef-b
    scale=max(float(np.linalg.norm(b-np.mean(b))),np.finfo(float).tiny)
    return float(np.linalg.norm(r)/scale)


def observable_convergence(Jc:np.ndarray,Jf:np.ndarray)->dict[str,Any]:
    pc,pf=raw_phase_map(Jc),raw_phase_map(Jf)
    rows=[]
    for kf,f in enumerate(FREQUENCIES):
        shape=affine_shape_error(Jc[kf],Jf[kf])
        phase_fraction=None
        phase_change=None
        if f>0:
            phase_change=abs(pf[float(f)]-pc[float(f)])
            phase_fraction=phase_change/abs(float(base.GRADIENT_TARGET_DEG[float(f)]))
        passed=shape<=SHAPE_GATE and (phase_fraction is None or phase_fraction<=PHASE_TARGET_GATE)
        rows.append({'frequency_hz':float(f),'complex_affine_shape_residual':shape,
                     'raw_phase_coarse_deg':pc[float(f)],'raw_phase_fine_deg':pf[float(f)],
                     'raw_phase_absolute_change_deg':phase_change,
                     'raw_phase_change_fraction_of_frozen_target':phase_fraction,
                     'pass':bool(passed)})
    if not all(r['pass'] for r in rows): raise AssertionError('Stage-B six-channel observable convergence failed')
    return {'rows':rows,'shape_gate':SHAPE_GATE,'phase_fraction_gate':PHASE_TARGET_GATE,'pass':True}


def install_discrete_moments(zum:np.ndarray,G:np.ndarray):
    z=np.asarray(zum,float); weights=np.asarray(G,float)
    zref=0.5*(float(z[0])+float(z[-1]))
    def moment(r_per_um:complex,indices:np.ndarray)->np.ndarray:
        expo=np.exp(r_per_um*(z-zref))
        return (weights[np.asarray(indices,dtype=int)]@expo).astype(complex)
    return moment,zref


def blind_grid(J:np.ndarray,zum:np.ndarray,G:np.ndarray,seed_base:int)->dict[str,Any]:
    """Data-only analyzer: J,z,G and frozen frequency/noise coordinates only."""
    moment,zref=install_discrete_moments(zum,G)
    old=one.moment_vector
    one.moment_vector=moment
    try:
        onefits=[]; twofits={}
        for kf,f in enumerate(FREQUENCIES):
            onefits.append(one.kernel_one_mode_fit(J[kf],ALL6))
            if f>0:
                twofits[str(int(f))]=two.fit_two_mode(J[kf],seed=seed_base+kf)
    finally:
        one.moment_vector=old

    analytic=[]
    for kf,f in enumerate(FREQUENCIES):
        if f<=0: continue
        fit=onefits[kf]
        pred=np.asarray(fit['predicted']['real'])+1j*np.asarray(fit['predicted']['imag'])
        y=np.asarray(J[kf],complex)
        residual_norm=float(np.linalg.norm(y-pred))
        step=float(np.mean(np.abs(np.diff(y))))
        _,lam=boot.analytic_lambda_required(6)
        req=np.sqrt(lam)*step/max(residual_norm,np.finfo(float).tiny)
        reqdb=float(20*np.log10(req))
        claim=float(base.GRADIENT_SNR_DB[float(f)])
        analytic.append({'frequency_hz':float(f),'step_amplitude':step,'one_mode_residual_norm':residual_norm,
                         'analytic_required_rejection_snr_db':reqdb,'frozen_false_transport_claim_snr_db':claim,
                         'analytic_warning_margin_db':float(claim-reqdb),
                         'early_warning_analytic':bool(reqdb<claim)})
    return {'input_contract':{
                'currents':array_complex(J),'frequencies_hz':FREQUENCIES.tolist(),
                'z_cell_centers_um':np.asarray(zum,float).tolist(),
                'normalized_calibrated_depth_weights':np.asarray(G,float).tolist(),
                'alpha':boot.ALPHA,'target_power':boot.TARGET_POWER,
                'frozen_false_claim_snr_db':{str(int(f)):float(base.GRADIENT_SNR_DB[float(f)]) for f in FREQUENCIES if f>0}},
            'z_reference_um':zref,'one_mode_fits':onefits,'two_mode_fits_nonzero_rf':twofits,
            'analytic_warning_before_claim':analytic}


def root_summary(coarse:dict[str,Any],fine:dict[str,Any])->dict[str,Any]:
    rows=[]
    sums={}; sumerrs={}
    for f in FREQUENCIES[1:]:
        key=str(int(f)); a=coarse['two_mode_fits_nonzero_rf'][key]; b=fine['two_mode_fits_nonzero_rf'][key]
        dist=two.root_set_distance(a,b)
        sa=complex(a['r1_per_um']['real'],a['r1_per_um']['imag'])+complex(a['r2_per_um']['real'],a['r2_per_um']['imag'])
        sb=complex(b['r1_per_um']['real'],b['r1_per_um']['imag'])+complex(b['r2_per_um']['real'],b['r2_per_um']['imag'])
        err=abs(sb-sa); stable=dist['max_root_change_relative_to_largest_root_magnitude']<=ROOT_STABILITY_GATE
        imag_violation=stable and abs(sb.imag)>ROOT_LAW_NUMERICAL_FACTOR*err
        rows.append({'frequency_hz':float(f),'root_stability':dist,'stable_under_5pct_rule':bool(stable),
                     'coarse_root_sum_per_um':json_complex(sa),'fine_root_sum_per_um':json_complex(sb),
                     'root_sum_grid_change_per_um':float(err),'real_sum_violation':bool(imag_violation)})
        sums[float(f)]=sb; sumerrs[float(f)]=err
    pair=[]
    fs=list(FREQUENCIES[1:])
    stable_by={r['frequency_hz']:r['stable_under_5pct_rule'] for r in rows}
    for i in range(len(fs)):
        for j in range(i+1,len(fs)):
            f1,f2=float(fs[i]),float(fs[j]); delta=abs(sums[f1]-sums[f2]); allow=ROOT_LAW_NUMERICAL_FACTOR*(sumerrs[f1]+sumerrs[f2])
            violation=stable_by[f1] and stable_by[f2] and delta>allow
            pair.append({'frequency_pair_hz':[f1,f2],'root_sum_separation_per_um':float(delta),
                         'five_x_grid_allowance_per_um':float(allow),'rf_independence_violation':bool(violation)})
    return {'per_frequency':rows,'pairwise_rf_independence':pair,'root_stability_gate':ROOT_STABILITY_GATE,
            'numerical_separation_factor':ROOT_LAW_NUMERICAL_FACTOR}


def comparison(finite:np.ndarray,planar:np.ndarray)->dict[str,Any]:
    pf,pp=raw_phase_map(finite),raw_phase_map(planar)
    rows=[]
    for f in FREQUENCIES[1:]:
        f=float(f); excess=pf[f]-pp[f]; mimic=abs(excess)/abs(float(base.GRADIENT_TARGET_DEG[f]))
        rows.append({'frequency_hz':f,'finite_raw_closure_phase_deg':pf[f],'planar_raw_closure_phase_deg':pp[f],
                     'finite_minus_planar_raw_phase_deg':float(excess),'historical_mimic_fraction':float(mimic)})
    return {'warning':'historical raw four-color phase is a comparison coordinate only; calibrated-kernel fit is the physical null',
            'rows':rows,'max_historical_mimic_fraction':float(max(r['historical_mimic_fraction'] for r in rows))}


def classify(comp:dict[str,Any],blind:dict[str,Any],roots:dict[str,Any])->str:
    order_one=comp['max_historical_mimic_fraction']>=ORDER_ONE_MIMIC
    early=all(r['early_warning_analytic'] for r in blind['analytic_warning_before_claim'])
    stable=all(r['stable_under_5pct_rule'] for r in roots['per_frequency'])
    root_violation=any(r['real_sum_violation'] for r in roots['per_frequency']) or any(r['rf_independence_violation'] for r in roots['pairwise_rf_independence'])
    if not order_one: return 'B2-C: small self-consistent confound; generic blind machinery validated if all numerical gates pass'
    if not early and not (stable and root_violation): return 'B2-B: hidden-risk Stage-B point'
    if early and not stable: return 'B2-D: one-mode rejection before false-claim precision; higher-order mechanism unresolved'
    return 'B2-A: order-one self-consistent confound self-announces before false-claim precision'


def main()->None:
    ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path,default=Path(__file__).with_suffix('.json')); args=ap.parse_args()

    # Mandatory upstream validation executes first and enforces the unchanged refined gates.
    p=op.Params()
    validation_cases=[stageb_gate.mesh_case(nx,nz,p) for nx,nz in stageb_gate.MESHES]
    adjacent=[]
    for i in range(len(validation_cases)-1):
        enforce=(tuple(validation_cases[i]['grid'])==stageb_gate.ACCEPTANCE_PAIR[0] and tuple(validation_cases[i+1]['grid'])==stageb_gate.ACCEPTANCE_PAIR[1])
        adjacent.append(stageb_gate.convergence(validation_cases[i],validation_cases[i+1],p,enforce=enforce))
    if not adjacent[-1]['acceptance_pair'] or not adjacent[-1]['pass_all_unchanged_thresholds']:
        raise AssertionError('mandatory refined Stage-B validation did not pass')
    signal_validation=stageb_gate.signal_gate(validation_cases[-1],p)

    finite={}; planar={}
    for nx,nz in MESHES:
        Jf,Gf,df,zf=solve_structure(p,nx,nz)
        Jp,Gp,dp,zp=solve_structure(replace(p,contact_fraction=1.0),nx,nz)
        finite[(nx,nz)]=(Jf,Gf,df,zf); planar[(nx,nz)]=(Jp,Gp,dp,zp)
    Jc,Gc,dfc,zc=finite[MESHES[0]]; Jf,Gf,dff,zf=finite[MESHES[1]]
    Jpc,Gpc,dpc,zpc=planar[MESHES[0]]; Jpf,Gpf,dpf,zpf=planar[MESHES[1]]

    conv=observable_convergence(Jc,Jf)
    # Planar is a numerical/reference diagnostic and is not supplied to blind_grid.
    planar_conv=observable_convergence(Jpc,Jpf)
    bc=blind_grid(Jc,zc,Gc,7300)
    bf=blind_grid(Jf,zf,Gf,8300)
    roots=root_summary(bc,bf)
    comp=comparison(Jf,Jpf)
    outcome=classify(comp,bf,roots)

    if not np.all(np.isfinite(Jf.real)) or not np.all(np.isfinite(Jf.imag)): raise AssertionError('nonfinite blind currents')
    if not all(np.isfinite(r['analytic_warning_margin_db']) for r in bf['analytic_warning_before_claim']): raise AssertionError('nonfinite analytic warning result')

    result={
        'schema':'paper03-stageB-blind-six-channel-v1',
        'status':'PREDECLARED FINAL GENERIC STAGE-B BLIND RESULT / NON-HGCDTE CLAIM',
        'lock':'PAPER03_STAGEB_BLIND_SIX_CHANNEL_LOCK_2026-08-18.md',
        'upstream_validation':{
            'refined_acceptance_pair':[list(stageb_gate.ACCEPTANCE_PAIR[0]),list(stageb_gate.ACCEPTANCE_PAIR[1])],
            'acceptance_pair_result':adjacent[-1],
            'signal_validation':signal_validation,
        },
        'forward_only':{
            'scope':'explicit synthetic single-electron Stage-B structures; not supplied to blind analyzer',
            'finite_grid_diagnostics':[dfc,dff],
            'planar_grid_diagnostics':[dpc,dpf],
        },
        'blind_observable_convergence_finite':conv,
        'reference_observable_convergence_planar':planar_conv,
        'blind_coarse':bc,
        'blind_fine':bf,
        'two_root_cross_mesh_physical_law':roots,
        'finite_vs_planar_comparison_not_used_by_blind_fit':comp,
        'predeclared_outcome':outcome,
        'generic_stageB_minimum_milestone_passed':True,
        'science_interpretation_ready':False,
        'paper03_standalone_go_recorded_here':False,
    }
    args.output.write_text(json.dumps(resolvent.json_safe(result),indent=2,allow_nan=False)+'\n')
    print(outcome)
    for r in bf['analytic_warning_before_claim']:
        print(f"{r['frequency_hz']/1e6:.0f} MHz analytic rejection={r['analytic_required_rejection_snr_db']:.3f} dB claim={r['frozen_false_transport_claim_snr_db']:.3f} margin={r['analytic_warning_margin_db']:.3f} dB")
    print('max historical mimic =',comp['max_historical_mimic_fraction'])
    print('generic_stageB_minimum_milestone_passed = true')


if __name__=='__main__': main()
