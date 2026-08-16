"""Post-hoc two-carrier follow-up with the countercarrier root fixed to truth.

See PAPER02_TWO_CARRIER_FOLLOWUP_2026-08-16.md.  The countercarrier is present
in the forward terminal transient and its complex amplitude is still profiled,
but its deliberately simple uniform-velocity propagation root is treated as
known.  Only the downstream root is nonlinear.
"""
from __future__ import annotations
import argparse,csv,json
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
import realistic_geometry_closure_stress as base
import paper02_exact_planar_continuum_crosscheck as exact
import paper02_kernel_aware_depletion_frequency_law as law
import paper02_two_carrier_exact_continuum as pair


def linear_fit(J, rd, ru):
    X=np.column_stack((np.ones(len(J),complex),law.kernel_basis(rd),law.kernel_basis(ru)))
    c,*_=np.linalg.lstsq(X,J,rcond=None)
    m=X@c; e=m-J
    sc=max(float(np.linalg.norm(J-np.mean(J))),1e-30)
    return c,m,float(np.linalg.norm(e)/sc),float(np.linalg.cond(X))


def fit_down(J, rd_seed, ru):
    rho=rd_seed*1e-6
    seeds=[np.array((rho.real,max(rho.imag*s,1e-8))) for s in (0.8,0.9,1.0,1.1,1.2)]
    lo=np.array((-20.,1e-10)); hi=np.array((20.,20.))
    cand=[]
    for x0 in seeds:
        x0=np.minimum(np.maximum(x0,lo+1e-12),hi-1e-12)
        def res(x):
            rd=(x[0]+1j*x[1])/1e-6
            _,m,_,_=linear_fit(J,rd,ru)
            e=(m-J)/max(float(np.linalg.norm(J-np.mean(J))),1e-30)
            return np.r_[e.real,e.imag]
        o=least_squares(res,x0,bounds=(lo,hi),xtol=1e-13,ftol=1e-13,gtol=1e-13,max_nfev=5000)
        rd=(o.x[0]+1j*o.x[1])/1e-6
        c,m,rel,cond=linear_fit(J,rd,ru)
        s=np.linalg.svd(o.jac,compute_uv=False); jc=float(s[0]/s[-1]) if s[-1]>0 else float('inf')
        cand.append((rel,o.cost,rd,cond,jc,o))
    rel,cost,rd,cond,jc,o=min(cand,key=lambda q:(q[0],q[1]))
    return rd,rel,cond,jc,bool(o.success)


def main(args):
    z=base.OPT_Z_UM*1e-6
    freqs=pair.PROBE_FREQUENCIES
    vd=float(exact.exact_speed_m_per_s(np.array([0.]))[0])
    Hd_h=exact.exact_point_transfer(z,freqs)
    Hd_u=pair.uniform_down_transfer(z,freqs,vd)
    Jd=pair.channel_currents(Hd_h)
    single=[]
    for jf,f in enumerate(freqs):
        r,*_=law.kernel_aware_root(Jd[jf]); single.append(r)
    rows=[]
    core_pass=True
    for ratio in pair.SPEED_RATIOS:
        vu=float(ratio*vd)
        Hu=pair.uniform_up_transfer(z,freqs,vu)
        Ju=pair.channel_currents(Hd_u+Hu)
        Jh=pair.channel_currents(Hd_h+Hu)
        for jf,f in enumerate(freqs):
            om=2*np.pi*f; rd0=1j*om/vd; ru=-1j*om/vu
            rdu,urelu,ucond,ujc,us=fit_down(Ju[jf],rd0,ru)
            Du,wu=law.solve_dw_one_frequency(-rdu,float(f))
            uniform_ok=bool(us and urelu<=1e-8 and abs(Du)<=1e-7)
            if 0.1<=ratio<=10: core_pass &= uniform_ok
            rdh,hrel,hcond,hjc,hs=fit_down(Jh[jf],single[jf],ru)
            Dh,wh=law.solve_dw_one_frequency(-rdh,float(f))
            Dref,_=law.solve_dw_one_frequency(-single[jf],float(f))
            rows.append({
              'ratio':float(ratio),'frequency_hz':float(f),'core':bool(0.1<=ratio<=10),
              'uniform_ok':uniform_ok,'uniform_D':float(Du),'uniform_centered_rel':urelu,
              'heterogeneous_D':float(Dh),'heterogeneous_w':float(wh),'heterogeneous_centered_rel':hrel,
              'heterogeneous_positive_D':bool(Dh>0),'relative_D_shift_from_single':float(abs(Dh-Dref)/abs(Dref)),
              'single_D_reference':float(Dref),'downstream_r_real':float(rdh.real),'downstream_r_imag':float(rdh.imag),
              'known_up_r_imag':float(ru.imag),'heterogeneous_design_condition':hcond,
              'heterogeneous_jacobian_condition':hjc,'optimizer_success':hs})
    core=[r for r in rows if r['core'] and r['uniform_ok'] and r['optimizer_success']]
    pos=[r for r in core if r['heterogeneous_positive_D']]
    payload={
      'status':'CHECKED post-hoc known-countercarrier pair stress' if core_pass else 'CONTROL_FAIL',
      'interpretation_boundary':'countercarrier root fixed to its known uniform-velocity value; amplitude profiled; not a generic free two-carrier identifiability claim',
      'uniform_core_gate_pass':bool(core_pass),'core_rows':len(core),'positive_D_core_rows':len(pos),
      'all_identifiable_core_positive_D':bool(core and len(pos)==len(core)),
      'min_core_D':float(min(r['heterogeneous_D'] for r in core)) if core else None,
      'max_core_D':float(max(r['heterogeneous_D'] for r in core)) if core else None,
      'max_core_relative_D_shift_from_single':float(max(r['relative_D_shift_from_single'] for r in core)) if core else None,
      'max_core_heterogeneous_centered_rel':float(max(r['heterogeneous_centered_rel'] for r in core)) if core else None,
      'rows':rows}
    Path(args.json).parent.mkdir(parents=True,exist_ok=True)
    Path(args.json).write_text(json.dumps(payload,indent=2,sort_keys=True))
    with open(args.csv,'w',newline='') as f:
      w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    print(json.dumps(payload,indent=2,sort_keys=True))

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--json',default='results/paper02_two_carrier_known_countercarrier_summary.json');p.add_argument('--csv',default='results/paper02_two_carrier_known_countercarrier_rows.csv');main(p.parse_args())
