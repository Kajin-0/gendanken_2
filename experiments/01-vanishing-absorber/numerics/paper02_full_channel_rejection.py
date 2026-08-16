"""Exact-continuum full-channel versus root-space rejection comparison.

Implements PAPER02_FULL_CHANNEL_REJECTION_GATE_2026-08-16.md.
"""
from __future__ import annotations
import argparse,csv,json
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
import realistic_geometry_closure_stress as base
import paper02_exact_planar_continuum_crosscheck as exact
import paper02_kernel_aware_depletion_frequency_law as law
import paper02_end_to_end_rejection_snr as rootspace

FREQ=rootspace.FREQUENCIES.copy()
ALPHA=rootspace.ALPHA; POWER=rootspace.POWER


def channels_exact():
    z=base.OPT_Z_UM*1e-6
    H=exact.exact_point_transfer(z,FREQ)
    return exact.exact_channel_currents(H)


def profile_frequency(J,r):
    F=law.kernel_basis(r)
    X=np.column_stack((np.ones(len(J),complex),F))
    c,*_=np.linalg.lstsq(X,J,rcond=None)
    return X@c,c


def full_fit(Jall,fs):
    sig=np.sqrt(np.mean(np.abs(Jall)**2,axis=1))
    # Initialize from the exact one-root estimate at the lowest frequency.
    r0,*_=law.kernel_aware_root(Jall[0]); D0,w0=law.solve_dw_one_frequency(-r0,float(fs[0]))
    D0=max(float(D0),1e-10);w0=max(float(w0),1.)
    def residual(lp):
        D,w=np.exp(lp); gm=rootspace.gamma_dd(fs,D,w)
        out=[]
        for J,g,s in zip(Jall,gm,sig):
            m,_=profile_frequency(J,-g);e=(m-J)/s
            out.extend(e.real);out.extend(e.imag)
        return np.asarray(out)
    o=least_squares(residual,np.log((D0,w0)),xtol=1e-13,ftol=1e-13,gtol=1e-13,max_nfev=5000)
    D,w=np.exp(o.x);rw=residual(o.x)
    return float(D),float(w),float(rw@rw),bool(o.success)


def root_fit(Jall,fs):
    gs=[];cs=[]
    for J in Jall:
        g,c,_=rootspace.root_covariance_at_snr1(J);gs.append(g);cs.append(c)
    D,w,lam,_=rootspace.fit_homogeneous(np.asarray(fs),np.asarray(gs),cs)
    return D,w,lam


def threshold(lam1,nu):
    q,lamreq=rootspace.lambda_required(nu)
    s=float(np.sqrt(lamreq/lam1)) if lam1>0 else float('inf')
    return q,lamreq,s,float(20*np.log10(s))


def main(args):
    J=channels_exact(); rows=[]
    for n in range(2,len(FREQ)+1):
        fs=FREQ[:n];Js=J[:n]
        Dr,wr,lr=root_fit(Js,fs); qr,lrr,sr,srdb=threshold(lr,2*n-2)
        Df,wf,lf,ok=full_fit(Js,fs); qf,lrf,sf,sfdb=threshold(lf,8*n-2)
        rows.append({
          'max_frequency_hz':float(fs[-1]),'n_frequencies':n,
          'root_dof':2*n-2,'root_best_D':Dr,'root_best_w':wr,'root_lambda_snr1':lr,'root_required_snr':sr,'root_required_snr_db':srdb,
          'full_dof':8*n-2,'full_best_D':Df,'full_best_w':wf,'full_lambda_snr1':lf,'full_required_snr':sf,'full_required_snr_db':sfdb,
          'full_minus_root_snr_db':float(sfdb-srdb),'full_optimizer_success':ok})
    payload={
      'status':'CHECKED exact-continuum root-space versus full-channel rejection comparison',
      'noise_model':{'S':'RMS_m |J_m| / sigma_quadrature','S_dB':'20 log10 S','cross_frequency_correlation':False,'same_S_each_frequency':True},
      'test':{'alpha':ALPHA,'power':POWER,'root_space_dof':'2n-2','full_channel_dof':'8n-2','per_frequency_full_channel_nuisance':'complex C_f,K_f'},
      'rows':rows,
      'through_1ghz':next(r for r in rows if r['max_frequency_hz']==1e9),
      'through_3ghz':rows[-1]}
    p=Path(args.json);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(payload,indent=2,sort_keys=True))
    with open(args.csv,'w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    print(json.dumps(payload,indent=2,sort_keys=True))

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--json',default='results/paper02_full_channel_rejection_summary.json');p.add_argument('--csv',default='results/paper02_full_channel_rejection_rows.csv');main(p.parse_args())
