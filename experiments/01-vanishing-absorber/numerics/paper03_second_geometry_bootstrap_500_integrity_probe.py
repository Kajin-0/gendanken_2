"""Exact 12-draw integrity probe for the coplanar 500-MHz bootstrap optimizer.

This does not run or alter the bootstrap ensembles. It reproduces only the
predeclared six null + six alternative full-refit spot checks at the analytic
SNR so optimizer branch coverage can be diagnosed cheaply.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
import paper03_second_geometry_gate as cop
import paper03_second_geometry_bootstrap_500_repair as repair
import paper03_stageA_statistical_bootstrap as boot
import paper03_stageA_kernel_blind_gate as kernel

KF=2

def cfit(f,key):
    return np.asarray(f[key]['real'],float)+1j*np.asarray(f[key]['imag'],float)

def draw_rows(mean,sigma,baseline_r,seed):
    rng=np.random.default_rng(seed); rows=[]
    for k in range(6):
        y=mean+sigma*(rng.standard_normal(len(mean))+1j*rng.standard_normal(len(mean)))
        rf,rfast=repair.robust_fast_refit(y,baseline_r)
        ff=kernel.kernel_one_mode_fit(y,boot.ALL6)
        rfull=complex(ff['r_per_um']['real'],ff['r_per_um']['imag'])
        full=cfit(ff,'residual')
        nf=float(np.linalg.norm(rf)); ng=float(np.linalg.norm(full)); ratio=nf/max(ng,np.finfo(float).tiny)
        rows.append({'draw':k,'fast_root':{'real':rfast.real,'imag':rfast.imag},'full_root':{'real':rfull.real,'imag':rfull.imag},
                     'fast_residual_norm':nf,'full_residual_norm':ng,'ratio':float(ratio),
                     'root_distance':float(abs(rfast-rfull))})
    return rows

def main():
    J,_,_,_=cop.solve_grid(161,121,17); y=np.asarray(J[KF],complex)
    fit=kernel.kernel_one_mode_fit(y,boot.ALL6); null=cfit(fit,'predicted')
    r0=complex(fit['r_per_um']['real'],fit['r_per_um']['imag'])
    step=float(np.mean(np.abs(np.diff(y)))); resid=float(np.linalg.norm(y-null))
    _,lam=boot.analytic_lambda_required(2*len(y)-6)
    snr=np.sqrt(lam)*step/resid; snr_db=float(20*np.log10(snr)); sigma=step/10**(snr_db/20)
    null_rows=draw_rows(null,sigma,r0,300000+KF*1000)
    alt_rows=draw_rows(y,sigma,r0,400000+KF*1000)
    allrows=null_rows+alt_rows; worst=max(allrows,key=lambda r:r['ratio'])
    out={'schema':'paper03-coplanar-500-integrity-probe-v1','statistical_contract_changed':False,
         'frequency_hz':500e6,'analytic_snr_db':snr_db,'baseline_root':{'real':r0.real,'imag':r0.imag},
         'null':null_rows,'alternative':alt_rows,'max_ratio':float(worst['ratio']),'worst':worst,
         'frozen_integrity_gate':1.001,'integrity_pass':bool(worst['ratio']<=1.001),
         'science_interpretation_ready':False}
    Path('paper03_second_geometry_bootstrap_500_integrity_probe.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__': main()
