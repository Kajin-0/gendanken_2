#!/usr/bin/env python3
from __future__ import annotations
import numpy as np
from scipy.integrate import cumulative_trapezoid, solve_ivp
from scipy.optimize import brentq
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import spsolve

HC_EV_UM = 1.2398419843320026
KB = 1.380649e-23
Q = 1.602176634e-19
T = 300.0
L_UM = 7.6
L_M = L_UM*1e-6
X_FRONT, X_BACK = 0.55,0.32
MU=0.90
D=MU*KB*T/Q
E_SCALE=8.0e5
ROLLOFF_EXP=2.2
TARGET_DEPTHS_UM=np.asarray((2.5,3.0,3.5,4.0))
FREQS=(100e6,250e6,500e6,1e9)

def eg(x,t=T):
    return -0.302+1.93*x-0.81*x*x+0.832*x**3+5.35e-4*(1-2*x)*t

def degdx(x,t=T):
    return 1.93-1.62*x+3*0.832*x*x-2*5.35e-4*t

def moazzami_k(x,t=T):
    return -20060+115750*x+32.43*t-64170*x*x+0.43231*t*t-101.92*x*t

def moazzami_n(x,t=T):
    return 0.74487-0.44513*x+(0.000799-0.000757*x)*t

ZF_UM=np.linspace(0,L_UM,10001)
XF=X_FRONT+(X_BACK-X_FRONT)*ZF_UM/L_UM

def optical_kernel_fine(lam_um):
    photon=HC_EV_UM/lam_um
    frac=(photon-eg(XF))/photon
    alpha=np.zeros_like(frac)
    mask=frac>0
    alpha[mask]=moazzami_k(XF[mask])*frac[mask]**moazzami_n(XF[mask])
    alpha=np.maximum(alpha,0)
    tau=np.concatenate(([0.0],cumulative_trapezoid(alpha,ZF_UM*1e-4)))
    density=alpha*1e-4*np.exp(-tau)
    p_abs=1-np.exp(-tau[-1])
    density/=np.trapezoid(density,ZF_UM)
    mean=np.trapezoid(ZF_UM*density,ZF_UM)
    return p_abs,mean,density

def wavelength_for_mean(mean_um):
    return brentq(lambda lam: optical_kernel_fine(lam)[1]-mean_um,1.95,3.20)

N=5000
Z_UM=np.linspace(0,L_UM,N+1)
Z_M=Z_UM*1e-6
DX=Z_M[1]-Z_M[0]
X=X_FRONT+(X_BACK-X_FRONT)*Z_UM/L_UM
DXDZ=(X_BACK-X_FRONT)/L_M


def components(xarr, alpha_dos=1.0, xi_const=None):
    if xi_const is None:
        e_drive=np.abs((degdx(xarr)-0.45)*DXDZ)
    else:
        e_drive=np.abs(xi_const*degdx(xarr)*DXDZ)
    field=MU*e_drive/(1+(e_drive/E_SCALE)**ROLLOFF_EXP)
    dos=1.5*D*(degdx(xarr)*DXDZ/eg(xarr))
    return field,dos,field+alpha_dos*dos

FIELD,DOS,V=components(X)
V_HARM=1/(np.trapezoid(1/V,Z_M)/L_M)

def make_kernels():
    wavelengths=np.asarray([wavelength_for_mean(z) for z in TARGET_DEPTHS_UM])
    kernels=[]; pabs=[]
    for lam in wavelengths:
        p,_,kfine=optical_kernel_fine(lam)
        k=np.interp(Z_UM,ZF_UM,kfine)
        k/=np.trapezoid(k,Z_UM)
        kernels.append(k); pabs.append(p)
    return wavelengths,np.asarray(pabs),kernels
WAVELENGTHS,PABS,KERNELS=make_kernels()

def solve_fd(freq_hz, var_v=V, kappa=0.0):
    s=1j*2*np.pi*freq_hz
    kp=np.full_like(X,float(kappa)) if np.isscalar(kappa) else np.asarray(kappa,float)
    lam=kp+s
    v0=var_v[0]; lam0=kp[0]+s
    rp=(-v0+np.sqrt(v0*v0+4*D*lam0))/(2*D)
    jp=v0/lam0
    rows=[];cols=[];vals=[]
    rhs=np.zeros(N+1,complex)
    rows += [0,0,0]; cols += [0,1,2]; vals += [-3/(2*DX)-rp,4/(2*DX),-1/(2*DX)]
    rhs[0]=-rp*jp
    for i in range(1,N):
        rows += [i,i,i]; cols += [i-1,i,i+1]
        vals += [D/DX**2-var_v[i]/(2*DX), -2*D/DX**2-lam[i], D/DX**2+var_v[i]/(2*DX)]
        rhs[i]=-var_v[i]
    rows.append(N);cols.append(N);vals.append(1.0)
    A=csr_matrix((np.asarray(vals,complex),(rows,cols)),shape=(N+1,N+1))
    return spsolve(A,rhs)

def solve_shoot(freq_hz, var_v=V, kappa_profile=None):
    s=1j*2*np.pi*freq_hz
    kp=np.zeros_like(X) if kappa_profile is None else np.asarray(kappa_profile,float)
    def vat(z): return float(np.interp(z,Z_M,var_v))
    def kat(z): return float(np.interp(z,Z_M,kp))
    v0=var_v[0]; lam0=kp[0]+s
    rp=(-v0+np.sqrt(v0*v0+4*D*lam0))/(2*D)
    jp=v0/lam0
    def rhs(z,y,forced=True):
        j,p=y; vv=vat(z); kk=kat(z)
        src=-vv if forced else 0.0
        return np.asarray([p,(src-vv*p+(kk+s)*j)/D],complex)
    base0=np.asarray([0+0j,-rp*jp],complex)
    sens0=np.asarray([1+0j,rp],complex)
    opts=dict(method='DOP853',rtol=2e-12,atol=2e-14,dense_output=True,max_step=L_M/500)
    b=solve_ivp(lambda z,y: rhs(z,y,True),(0,L_M),base0,**opts)
    h=solve_ivp(lambda z,y: rhs(z,y,False),(0,L_M),sens0,**opts)
    coeff=-b.y[0,-1]/h.y[0,-1]
    return b.sol(Z_M)[0]+coeff*h.sol(Z_M)[0]

def v_harm(var_v):
    return 1/(np.trapezoid(1/var_v,Z_M)/L_M)

def homogeneous(freq,var_v=V,kappa=0.0):
    vh=v_harm(var_v); s=1j*2*np.pi*freq
    gam=(np.sqrt(vh**2+4*D*(kappa+s))-vh)/(2*D)
    return 1-np.exp(-gam*(L_UM-Z_UM)*1e-6)

def currents(point):
    return np.asarray([np.trapezoid(k*point,Z_UM) for k in KERNELS])

def closure(js):
    d=np.diff(js)
    return 2*np.log(d[1])-np.log(d[0])-np.log(d[2])

def excess(point,f,var_v=V,kappa_hom=0.0):
    return closure(currents(point))-closure(currents(homogeneous(f,var_v,kappa_hom)))

def remaining_integral(y):
    c=np.concatenate(([0.0],cumulative_trapezoid(y,Z_M)))
    return c[-1]-c

def weighting_point_current(freq_hz,frac_change):
    span=TARGET_DEPTHS_UM[-1]-TARGET_DEPTHS_UM[0]
    center=.5*(TARGET_DEPTHS_UM[-1]+TARGET_DEPTHS_UM[0])
    weighting=1+(frac_change/span)*(Z_UM-center)
    omega=2*np.pi*freq_hz
    phase=np.exp(-1j*omega*Z_M/V_HARM)
    inner=remaining_integral(weighting*phase)
    return np.exp(1j*omega*Z_M/V_HARM)*inner

def graded_kappa_profile():
    tau=5e-6*np.exp((eg(X)-eg(.325))/(KB*T/Q))
    return 1/tau,tau

def hankel_det(d):
    return np.linalg.det(np.asarray([[d[0],d[1],d[2]],
                                     [d[1],d[2],d[3]],
                                     [d[2],d[3],d[4]]], complex))


def adjacent_minors(d):
    return np.asarray([d[m]*d[m+2]-d[m+1]**2 for m in range(3)], complex)


def main():
    d_bad=np.asarray([0,1,0,1,100],complex)
    w_bad=adjacent_minors(d_bad)
    f_bad=hankel_det(d_bad)
    assert abs(w_bad[1]**2-w_bad[0]*w_bad[2]) < 1e-14
    assert abs(f_bad+100) < 1e-10

    rng=np.random.default_rng(20260812)
    for _ in range(20):
        d=rng.normal(size=5)+1j*rng.normal(size=5)
        w=adjacent_minors(d)
        assert abs((w[1]**2-w[0]*w[2]) + d[2]*hankel_det(d)) < 1e-10

    target={}
    expected_target={100e6:-0.0220167193,250e6:-0.0546243847,
                     500e6:-0.1064448211,1e9:-0.1942321472}
    for f in FREQS:
        target[f]=np.degrees(excess(solve_fd(f),f).imag)
        assert abs(target[f]-expected_target[f]) < 2e-7

    weight_1p={}; weight_thresh={}
    expected_false={100e6:0.00294725169,500e6:0.01214000828,1e9:0.01000743531}
    expected_thresh={100e6:0.00756826705,500e6:0.00881288481,1e9:0.0196059800}
    for f in (100e6,500e6,1e9):
        c0=closure(currents(weighting_point_current(f,0)))
        def contam(a):
            return abs(np.degrees((closure(currents(weighting_point_current(f,a)))-c0).imag))
        weight_1p[f]=contam(.01)
        weight_thresh[f]=brentq(lambda a: contam(a)-.1*abs(target[f]),0,.05)
        assert abs(weight_1p[f]-expected_false[f]) < 2e-9
        assert abs(weight_thresh[f]-expected_thresh[f]) < 2e-8

    dos_frac=np.abs(DOS/FIELD)
    assert 0.087 < dos_frac.min() < 0.089
    assert 0.183 < dos_frac.max() < 0.184

    alpha={}
    expected_alpha={
        0.0:{100e6:-0.0186109,500e6:-0.0902584,1e9:-0.1651311},
        0.5:{100e6:-0.0203546,500e6:-0.0985193,1e9:-0.1796356},
        1.0:{100e6:-0.0220167,500e6:-0.1064448,1e9:-0.1942321},
        1.5:{100e6:-0.0234871,500e6:-0.1136000,1e9:-0.2088509},
    }
    for a in expected_alpha:
        _,_,vv=components(X,alpha_dos=a)
        alpha[a]={}
        for f in (100e6,500e6,1e9):
            alpha[a][f]=np.degrees(excess(solve_fd(f,vv),f,vv).imag)
            assert abs(alpha[a][f]-expected_alpha[a][f]) < 3e-7

    kp,tau=graded_kappa_profile()
    keff=np.trapezoid(kp/V,Z_M)/np.trapezoid(1/V,Z_M)
    recomb={}
    expected_recomb={100e6:3.78e-8,500e6:1.85e-7,1e9:3.45e-7}
    for f in (100e6,500e6,1e9):
        no_fd=excess(solve_fd(f),f)
        yes_fd=excess(solve_fd(f,V,kp),f,V,keff)
        no_sh=excess(solve_shoot(f,V,None),f)
        yes_sh=excess(solve_shoot(f,V,kp),f,V,keff)
        d_fd=np.degrees((yes_fd-no_fd).imag)
        d_sh=np.degrees((yes_sh-no_sh).imag)
        recomb[f]=(d_fd,d_sh,abs(d_sh-d_fd))
        assert abs(d_fd-expected_recomb[f]) < 1.5e-9
        assert abs(d_sh-d_fd) < 2e-9

    assert 3.8e-6 < tau.min() < 3.9e-6
    assert 0.88 < tau.max() < 0.90

    print("PASS: Rev. 8 adversarial regression")
    print(f"spurious minor closure: residual={w_bad[1]**2-w_bad[0]*w_bad[2]:.3g}, detH={f_bad:.6g}")
    print("weighting 1% false phase [deg]:",weight_1p)
    print("weighting 10% thresholds [%]:",{f:100*v for f,v in weight_thresh.items()})
    print(f"|v_DOS|/v_field range: {dos_frac.min():.5f} .. {dos_frac.max():.5f}")
    print("DOS alpha sensitivity [deg]:",alpha)
    print("graded recombination FD/shoot/difference [deg]:",recomb)


if __name__=="__main__":
    main()
