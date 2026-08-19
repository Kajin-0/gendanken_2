"""Generic coupled Poisson/electron-continuity Stage-B validation; not HgCdTe."""
from __future__ import annotations
import argparse, json, math
from dataclasses import asdict, dataclass, replace
from pathlib import Path
import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve

Q=1.602176634e-19; EPS0=8.8541878128e-12; KB=1.380649e-23

@dataclass(frozen=True)
class Params:
    width_m: float=16e-6
    thickness_m: float=7.6e-6
    eps_r: float=12.0
    temperature_K: float=100.0
    mobility_m2_Vs: float=0.50
    donor_density_m3: float=1e19
    built_in_top_V: float=-0.010
    applied_bias_V: float=0.030
    contact_fraction: float=0.75
    @property
    def eps(self): return self.eps_r*EPS0
    @property
    def vt(self): return KB*self.temperature_K/Q
    @property
    def D(self): return self.mobility_m2_Vs*self.vt
    @property
    def top_V(self): return self.built_in_top_V+self.applied_bias_V
    @property
    def top_n(self): return self.donor_density_m3*math.exp(self.built_in_top_V/self.vt)

def B(x: float)->float:
    a=abs(x)
    if a<1e-6:
        x2=x*x; return 1-.5*x+x2/12-x2*x2/720
    if x>50: return x*math.exp(-x)
    if x<-50: return -x
    return x/math.expm1(x)

def k(j,i,nx): return j*nx+i

def xs(nx,p):
    dx=p.width_m/nx
    return -.5*p.width_m+(np.arange(nx)+.5)*dx

def contacted(x,p,full=False):
    return full or abs(x)<=.5*p.contact_fraction*p.width_m

def poisson(nx,nz,n,p,full_top=False,top_V=None,rho_const=None):
    dx,dz=p.width_m/nx,p.thickness_m/nz; xx=xs(nx,p)
    A=lil_matrix((nx*nz,nx*nz)); b=np.zeros(nx*nz)
    tv=p.top_V if top_V is None else top_V
    for j in range(nz):
      for i,x in enumerate(xx):
        r=k(j,i,nx)
        if i>0:
            g=p.eps*dz/dx; A[r,r]+=g; A[r,k(j,i-1,nx)]-=g
        if i+1<nx:
            g=p.eps*dz/dx; A[r,r]+=g; A[r,k(j,i+1,nx)]-=g
        if j>0:
            g=p.eps*dx/dz; A[r,r]+=g; A[r,k(j-1,i,nx)]-=g
        else:
            g=p.eps*dx/(.5*dz); A[r,r]+=g
        if j+1<nz:
            g=p.eps*dx/dz; A[r,r]+=g; A[r,k(j+1,i,nx)]-=g
        elif contacted(float(x),p,full_top):
            g=p.eps*dx/(.5*dz); A[r,r]+=g; b[r]+=g*tv
        rho=rho_const if rho_const is not None else Q*(p.donor_density_m3-float(n[j,i]))
        b[r]+=rho*dx*dz
    return A.tocsr(),b

def continuity(nx,nz,psi,p,full_top=False,top_V=None,top_n=None):
    dx,dz=p.width_m/nx,p.thickness_m/nz; xx=xs(nx,p)
    A=lil_matrix((nx*nz,nx*nz)); b=np.zeros(nx*nz)
    tv=p.top_V if top_V is None else top_V; tn=p.top_n if top_n is None else top_n
    def edge(r,rn,delta,area,dist):
        g=Q*p.D*area/dist; A[r,r]+=g*B(-delta); A[r,rn]-=g*B(delta)
    def contact(r,pi,pb,nb,area,dist):
        d=(pb-pi)/p.vt; g=Q*p.D*area/dist; A[r,r]+=g*B(-d); b[r]+=g*B(d)*nb
    for j in range(nz):
      for i,x in enumerate(xx):
        r=k(j,i,nx); pi=float(psi[j,i])
        if i>0: edge(r,k(j,i-1,nx),(float(psi[j,i-1])-pi)/p.vt,dz,dx)
        if i+1<nx: edge(r,k(j,i+1,nx),(float(psi[j,i+1])-pi)/p.vt,dz,dx)
        if j>0: edge(r,k(j-1,i,nx),(float(psi[j-1,i])-pi)/p.vt,dx,dz)
        else: contact(r,pi,0.,p.donor_density_m3,dx,.5*dz)
        if j+1<nz: edge(r,k(j+1,i,nx),(float(psi[j+1,i])-pi)/p.vt,dx,dz)
        elif contacted(float(x),p,full_top): contact(r,pi,tv,tn,dx,.5*dz)
    return A.tocsr(),b

def relres(A,x,b):
    return float(np.linalg.norm(A@x.ravel()-b)/max(np.linalg.norm(b),np.finfo(float).tiny))

def solve(nx,nz,p,tol=1e-8,relax=.20,maxit=300):
    n=np.full((nz,nx),p.donor_density_m3); A,b=poisson(nx,nz,n,p); psi=spsolve(A,b).reshape(nz,nx); hist=[]
    for it in range(1,maxit+1):
        A,b=continuity(nx,nz,psi,p); ns=spsolve(A,b).reshape(nz,nx)
        if not np.all(np.isfinite(ns)) or np.any(ns<=0): raise AssertionError('carrier positivity/finite-density failure')
        nn=(1-relax)*n+relax*ns
        A,b=poisson(nx,nz,nn,p); ps=spsolve(A,b).reshape(nz,nx); pp=(1-relax)*psi+relax*ps
        dn=float(np.max(np.abs(nn-n))/p.donor_density_m3); dp=float(np.max(np.abs(pp-psi))/max(p.vt,abs(p.top_V),1e-15)); n,psi=nn,pp
        Ap,bp=poisson(nx,nz,n,p); Ac,bc=continuity(nx,nz,psi,p); rp,rc=relres(Ap,psi,bp),relres(Ac,n,bc)
        hist.append(dict(iteration=it,max_density_update_over_Nd=dn,max_potential_update_scaled=dp,poisson_relative_residual=rp,continuity_relative_residual=rc))
        if max(dn,dp,rp,rc)<tol: return psi,n,hist
    raise AssertionError('Gummel iteration did not converge')

def jedge(ni,nj,pi,pj,area,dist,p):
    d=(pj-pi)/p.vt
    return float(Q*p.D*area/dist*(nj*B(d)-ni*B(-d)))

def currents(nx,nz,psi,n,p):
    dx,dz=p.width_m/nx,p.thickness_m/nz; xx=xs(nx,p); cuts=[]
    for j in range(nz-1):
        cuts.append(sum(jedge(float(n[j,i]),float(n[j+1,i]),float(psi[j,i]),float(psi[j+1,i]),dx,dz,p) for i in range(nx)))
    bottom=sum(jedge(float(n[0,i]),p.donor_density_m3,float(psi[0,i]),0.,dx,.5*dz,p) for i in range(nx))
    top=sum(jedge(float(n[-1,i]),p.top_n,float(psi[-1,i]),p.top_V,dx,.5*dz,p) for i,x in enumerate(xx) if contacted(float(x),p))
    c=np.asarray(cuts); m=float(np.mean(c)); s=max(abs(m),np.finfo(float).tiny)
    return dict(bottom_outward_A_per_m_depth=float(bottom),top_outward_A_per_m_depth=float(top),horizontal_cut_mean_A_per_m_depth=m,horizontal_cut_max_fractional_deviation=float(np.max(np.abs(c-m))/s),terminal_balance_fraction=float(abs(bottom+top)/max(abs(bottom),abs(top),np.finfo(float).tiny)),max_abs_horizontal_cut_A_per_m_depth=float(np.max(np.abs(c))))

def analytic_poisson(p):
    rho=Q*1e18; tv=.020; rows=[]
    for nx,nz in ((9,16),(9,31),(9,61)):
        n=np.full((nz,nx),p.donor_density_m3); A,b=poisson(nx,nz,n,p,True,tv,rho); psi=spsolve(A,b).reshape(nz,nx)
        z=(np.arange(nz)+.5)*p.thickness_m/nz
        exact=-rho*z*z/(2*p.eps)+(tv+rho*p.thickness_m**2/(2*p.eps))*z/p.thickness_m
        rows.append(dict(grid=[nx,nz],max_abs_error_V=float(np.max(np.abs(psi-exact[:,None])))))
    ratio=rows[-2]['max_abs_error_V']/rows[-1]['max_abs_error_V']
    if rows[-1]['max_abs_error_V']>=5e-6 or ratio<=3: raise AssertionError('analytic Poisson gate failed')
    return dict(rho_C_m3=rho,top_V=tv,rows=rows,last_refinement_error_ratio=ratio)

def neutral_linear(p):
    nx,nz,tv=9,31,.020; n=np.full((nz,nx),p.donor_density_m3); A,b=poisson(nx,nz,n,p,True,tv); psi=spsolve(A,b).reshape(nz,nx)
    z=(np.arange(nz)+.5)*p.thickness_m/nz; err=float(np.max(np.abs(psi-tv*z[:,None]/p.thickness_m)))
    if err>=1e-12: raise AssertionError('neutral linear-potential gate failed')
    return dict(grid=[nx,nz],max_abs_error_V=err)

def opcase(p,label):
    nx,nz=31,23; psi,n,h=solve(nx,nz,p); c=currents(nx,nz,psi,n,p); f=h[-1]
    if f['poisson_relative_residual']>=1e-8 or f['continuity_relative_residual']>=1e-8: raise AssertionError(label+' residual gate failed')
    if np.min(n)<=0: raise AssertionError(label+' nonpositive density')
    return dict(label=label,grid=[nx,nz],iterations=len(h),final_iteration=f,min_n_over_Nd=float(np.min(n)/p.donor_density_m3),max_n_over_Nd=float(np.max(n)/p.donor_density_m3),min_psi_V=float(np.min(psi)),max_psi_V=float(np.max(psi)),current=c)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path,default=Path(__file__).with_suffix('.json')); a=ap.parse_args(); p=Params()
    pa=analytic_poisson(p); nl=neutral_linear(p); eq=opcase(replace(p,applied_bias_V=0.),'equilibrium-built-in')
    if max(abs(eq['current']['bottom_outward_A_per_m_depth']),abs(eq['current']['top_outward_A_per_m_depth']),eq['current']['max_abs_horizontal_cut_A_per_m_depth'])>=1e-8: raise AssertionError('equilibrium zero-current gate failed')
    bi=opcase(p,'finite-bias-nontrivial')
    if bi['current']['horizontal_cut_max_fractional_deviation']>=1e-5: raise AssertionError('current-conservation gate failed')
    if bi['current']['terminal_balance_fraction']>=1e-5: raise AssertionError('terminal-balance gate failed')
    if bi['min_n_over_Nd']>=.80: raise AssertionError('nontrivial coupling gate failed')
    out=dict(schema='paper03-stageB-operating-state-validation-v1',status='GENERIC SELF-CONSISTENT OPERATING-STATE VALIDATION / NON-CLAIM',model_scope='Synthetic single-electron semiconductor; not HgCdTe-specific. Coupled dark/bias Poisson + steady continuity only.',sign_convention=dict(poisson='-div(eps grad psi)=q(Nd-n)',electric_field='E=-grad(psi)',electron_current='Jn=-q mu n grad(psi)+q D grad(n)',einstein_relation='D=mu kT/q'),parameters={**asdict(p),'eps_F_m':p.eps,'thermal_voltage_V':p.vt,'diffusion_m2_s':p.D,'top_potential_V':p.top_V,'top_density_m3':p.top_n,'parameter_status':'explicit synthetic validation values; not literature-derived material claims'},poisson_analytic_validation=pa,neutral_linear_validation=nl,equilibrium_validation=eq,finite_bias_validation=bi,stageB_numerically_established=False,science_interpretation_ready=False,remaining_before_stageB_numerically_established=['three-mesh convergence of terminal and internal operating-state observables','independent weighting-potential validation in Stage-B geometry','dilute small-signal transport through converged operating state','backward-resolvent versus independent forward/reciprocity signal check','blind six-channel spectral/RF analysis without hidden-field leakage','material-specific parameter ledger before any HgCdTe instantiation'])
    a.output.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2))
if __name__=='__main__': main()
