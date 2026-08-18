"""Generic Stage-B mesh, weighting, Ramo, and reciprocity gate; non-claim."""
from __future__ import annotations
import argparse, json
from pathlib import Path
import numpy as np
from scipy.sparse import csr_matrix, identity, lil_matrix
from scipy.sparse.linalg import spsolve
import paper03_stageB_operating_state as op

MESHES=((21,15),(31,23),(41,31))
FREQ_HZ=500e6


def relres(A,x,b):
    return float(np.linalg.norm(A@x-b)/max(np.linalg.norm(b),np.finfo(float).tiny))


def common_profile(a,n=101):
    z=np.linspace(0.,1.,a.size)
    zz=np.linspace(0.,1.,n)
    return np.interp(zz,z,np.asarray(a,float))


def solve_weighting(nx,nz,p):
    dx,dz=p.width_m/nx,p.thickness_m/nz
    xx=op.xs(nx,p)
    A=lil_matrix((nx*nz,nx*nz),dtype=float); b=np.zeros(nx*nz)
    for j in range(nz):
      for i,x in enumerate(xx):
        r=op.k(j,i,nx)
        if i>0:
            g=dz/dx; A[r,r]+=g; A[r,op.k(j,i-1,nx)]-=g
        if i+1<nx:
            g=dz/dx; A[r,r]+=g; A[r,op.k(j,i+1,nx)]-=g
        if j>0:
            g=dx/dz; A[r,r]+=g; A[r,op.k(j-1,i,nx)]-=g
        else:
            g=dx/(.5*dz); A[r,r]+=g
        if j+1<nz:
            g=dx/dz; A[r,r]+=g; A[r,op.k(j+1,i,nx)]-=g
        elif op.contacted(float(x),p):
            g=dx/(.5*dz); A[r,r]+=g; b[r]+=g
    A=A.tocsr(); phi=spsolve(A,b)
    rr=relres(A,phi,b)
    if rr>=1e-10: raise AssertionError(f'weighting residual failed: {rr}')
    if np.min(phi)<-1e-10 or np.max(phi)>1+1e-10: raise AssertionError('weighting bounds failed')
    return phi.reshape(nz,nx),dict(linear_relative_residual=rr,min_phi=float(np.min(phi)),max_phi=float(np.max(phi)))


def mesh_case(nx,nz,p):
    psi,n,h=op.solve(nx,nz,p)
    c=op.currents(nx,nz,psi,n,p); f=h[-1]
    if f['poisson_relative_residual']>=1e-8 or f['continuity_relative_residual']>=1e-8: raise AssertionError('operating residual gate failed')
    if c['horizontal_cut_max_fractional_deviation']>=1e-5 or c['terminal_balance_fraction']>=1e-5: raise AssertionError('operating current gate failed')
    if np.any(~np.isfinite(n)) or np.min(n)<=0: raise AssertionError('density positivity failed')
    phi,wd=solve_weighting(nx,nz,p)
    ic=nx//2
    return dict(grid=[nx,nz],psi=psi,n=n,phi=phi,current=c,final=f,iterations=len(h),weighting=wd,
                psi_center=psi[:,ic].copy(),n_center=n[:,ic].copy(),phi_center=phi[:,ic].copy(),min_n_over_Nd=float(np.min(n)/p.donor_density_m3))


def convergence(a,b,p):
    ja=float(a['current']['horizontal_cut_mean_A_per_m_depth']); jb=float(b['current']['horizontal_cut_mean_A_per_m_depth'])
    jrel=abs(jb-ja)/max(abs(jb),np.finfo(float).tiny)
    pa,pb=common_profile(a['psi_center']),common_profile(b['psi_center'])
    na,nb=common_profile(a['n_center']),common_profile(b['n_center'])
    wa,wb=common_profile(a['phi_center']),common_profile(b['phi_center'])
    pscale=max(p.vt,abs(p.top_V),np.finfo(float).tiny)
    psi_rms=float(np.sqrt(np.mean((pb-pa)**2))/pscale)
    n_rms=float(np.sqrt(np.mean((nb-na)**2))/p.donor_density_m3)
    w_rms=float(np.sqrt(np.mean((wb-wa)**2)))
    mnrel=abs(float(b['min_n_over_Nd'])-float(a['min_n_over_Nd']))/max(abs(float(b['min_n_over_Nd'])),np.finfo(float).tiny)
    out=dict(terminal_current_relative_change=float(jrel),centerline_potential_rms_scaled=psi_rms,centerline_density_rms_over_Nd=n_rms,
             min_n_over_Nd_relative_change=float(mnrel),centerline_weighting_rms_change=w_rms)
    if jrel>0.03: raise AssertionError(f'mesh current convergence failed: {jrel}')
    if psi_rms>0.02: raise AssertionError(f'mesh potential convergence failed: {psi_rms}')
    if n_rms>0.03: raise AssertionError(f'mesh density convergence failed: {n_rms}')
    if mnrel>0.05: raise AssertionError(f'mesh minimum-density convergence failed: {mnrel}')
    if w_rms>0.02: raise AssertionError(f'weighting convergence failed: {w_rms}')
    return out


def frozen_operators(psi,phi,p):
    nz,nx=psi.shape; dx,dz=p.width_m/nx,p.thickness_m/nz; xx=op.xs(nx,p); vol=dx*dz
    Ac,_=op.continuity(nx,nz,psi,p)
    F=(-Ac/(op.Q*vol)).tocsr()
    Q=F.transpose().tocsr()
    bsel=np.zeros(nx*nz); bother=np.zeros(nx*nz)
    for j in range(nz):
      for i,x in enumerate(xx):
        r=op.k(j,i,nx); pi=float(psi[j,i])
        if j==0:
            d=(0.-pi)/p.vt
            bother[r]+=p.D/(.5*dz*dz)*op.B(-d)
        if j==nz-1 and op.contacted(float(x),p):
            d=(p.top_V-pi)/p.vt
            bsel[r]+=p.D/(.5*dz*dz)*op.B(-d)
    row_loss=np.asarray(-Q.sum(axis=1)).ravel()
    boundary_rate=bsel+bother
    deficit=float(np.linalg.norm(row_loss-boundary_rate)/max(np.linalg.norm(boundary_rate),np.finfo(float).tiny))
    if deficit>=1e-12: raise AssertionError(f'boundary-rate decomposition failed: {deficit}')
    ph=phi.ravel(); qramo=Q@ph+bsel
    return Q,F,bsel,bother,qramo,dict(forward_backward_operator_relative_mismatch=float(np.linalg.norm((F-Q.transpose()).data) if (F-Q.transpose()).nnz else 0.0),boundary_rate_decomposition_relative_error=deficit)


def signal_gate(case,p):
    psi=case['psi']; phi=case['phi']; nz,nx=psi.shape
    Q,F,bsel,bother,qramo,diag=frozen_operators(psi,phi,p)
    nstate=nx*nz
    psel=spsolve((-Q).tocsc(),bsel)
    rp=relres((-Q).tocsr(),psel,bsel)
    h0=spsolve((-Q).tocsc(),qramo)
    rh0=relres((-Q).tocsr(),h0,qramo)
    dcerr=float(np.max(np.abs(h0-(psel-phi.ravel()))))
    if rp>=1e-8 or rh0>=1e-8 or dcerr>=1e-8: raise AssertionError('DC committor/Ramo gate failed')

    omega=2*np.pi*FREQ_HZ; I=identity(nstate,format='csr',dtype=complex)
    Ab=(1j*omega*I-Q).tocsc(); H=spsolve(Ab,qramo.astype(complex)); rb=relres(Ab,H,qramo.astype(complex))
    Af=(1j*omega*I-F).tocsc()
    x=op.xs(nx,p); z=(np.arange(nz)+.5)*p.thickness_m/nz
    X,Z=np.meshgrid(x,z)
    s=np.exp(-.5*(X/(.20*p.width_m))**2-.5*((Z-.55*p.thickness_m)/(.18*p.thickness_m))**2).ravel()
    u=spsolve(Af,s.astype(complex)); rf=relres(Af,u,s.astype(complex))
    left=complex(np.dot(s.astype(complex),H)); right=complex(np.dot(qramo.astype(complex),u))
    rec=abs(left-right)/max(abs(left),abs(right),np.finfo(float).tiny)
    if rb>=1e-8 or rf>=1e-8 or rec>=1e-9: raise AssertionError(f'reciprocity gate failed: {rb}, {rf}, {rec}')
    peak=float(np.max(np.abs(u))); scale=1e-4*p.donor_density_m3/max(peak,np.finfo(float).tiny)
    inj=float(np.max(np.abs(scale*u))/p.donor_density_m3)
    return dict(frequency_hz=FREQ_HZ,committor_relative_residual=rp,ramo_dc_relative_residual=rh0,dc_committor_ramo_max_abs_error=dcerr,
                backward_relative_residual=rb,forward_relative_residual=rf,reciprocity_relative_mismatch=float(rec),
                bilinear_backward={'real':left.real,'imag':left.imag},bilinear_forward={'real':right.real,'imag':right.imag},
                low_injection_peak_delta_n_over_Nd=inj,operator_diagnostics=diag)


def serializable(c):
    return dict(grid=c['grid'],iterations=c['iterations'],final_iteration=c['final'],min_n_over_Nd=c['min_n_over_Nd'],current=c['current'],weighting=c['weighting'])


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path,default=Path(__file__).with_suffix('.json')); a=ap.parse_args()
    p=op.Params(); cases=[mesh_case(nx,nz,p) for nx,nz in MESHES]
    conv12=convergence(cases[0],cases[1],p); conv23=convergence(cases[1],cases[2],p)
    sig=signal_gate(cases[-1],p)
    out=dict(schema='paper03-stageB-mesh-weighting-reciprocity-v1',status='GENERIC STAGE-B MESH/WEIGHTING/RECIPROCITY VALIDATION / NON-CLAIM',
             lock='PAPER03_STAGEB_MESH_WEIGHTING_RECIPROCITY_LOCK_2026-08-17.md',parameters='unchanged synthetic Params from paper03_stageB_operating_state.py',
             meshes=[serializable(c) for c in cases],coarse_to_middle=conv12,middle_to_fine=conv23,signal_validation=sig,
             stageB_numerically_established=False,science_interpretation_ready=False,
             remaining=['blind six-channel spectral/RF Stage-B response','material-specific bipolar HgCdTe implementation and closed parameter ledger before material claim'])
    a.output.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n'); print(json.dumps(out,indent=2))
if __name__=='__main__': main()
