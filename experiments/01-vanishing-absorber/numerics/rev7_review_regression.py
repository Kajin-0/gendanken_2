#!/usr/bin/env python3
"""Independent regression anchors for the Rev. 7 adversarial corrections.

This script reconstructs the electron-affinity-anchored HgCdTe worked stress,
checks the finite-difference prediction against an independent adaptive shooting
solution, and verifies the propagated resource/nuisance numbers introduced in
Rev. 7.  It is a numerical regression for the stated conditional model, not a
material validation.
"""
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
L_M = L_UM * 1e-6
X_FRONT, X_BACK = 0.55, 0.32
MU = 0.90
D = MU * KB * T / Q
E_SCALE = 8.0e5
ROLLOFF_EXP = 2.2
TARGET_DEPTHS_UM = np.asarray((2.5, 3.0, 3.5, 4.0))
FREQS = (100e6, 250e6, 500e6, 1e9)


def eg(x, t=T):
    return -0.302 + 1.93*x - 0.81*x*x + 0.832*x**3 + 5.35e-4*(1 - 2*x)*t


def degdx(x, t=T):
    return 1.93 - 1.62*x + 3*0.832*x*x - 2*5.35e-4*t


def moazzami_k(x, t=T):
    return -20060 + 115750*x + 32.43*t - 64170*x*x + 0.43231*t*t - 101.92*x*t


def moazzami_n(x, t=T):
    return 0.74487 - 0.44513*x + (0.000799 - 0.000757*x)*t


ZF_UM = np.linspace(0.0, L_UM, 10001)
XF = X_FRONT + (X_BACK-X_FRONT)*ZF_UM/L_UM


def optical_kernel_fine(lam_um):
    photon = HC_EV_UM / lam_um
    frac = (photon - eg(XF)) / photon
    alpha = np.zeros_like(frac)
    mask = frac > 0
    alpha[mask] = moazzami_k(XF[mask]) * frac[mask] ** moazzami_n(XF[mask])
    alpha = np.maximum(alpha, 0.0)
    tau = np.concatenate(([0.0], cumulative_trapezoid(alpha, ZF_UM*1e-4)))
    density = alpha*1e-4*np.exp(-tau)
    p_abs = 1.0 - np.exp(-tau[-1])
    density /= np.trapezoid(density, ZF_UM)
    mean_um = np.trapezoid(ZF_UM*density, ZF_UM)
    return p_abs, mean_um, density


def wavelength_for_mean(mean_um):
    return brentq(lambda lam: optical_kernel_fine(lam)[1] - mean_um, 1.95, 3.20)


N = 5000
Z_UM = np.linspace(0.0, L_UM, N+1)
Z_M = Z_UM * 1e-6
DX = Z_M[1] - Z_M[0]
X = X_FRONT + (X_BACK-X_FRONT)*Z_UM/L_UM
DXDZ = (X_BACK-X_FRONT)/L_M


def velocity(xarr):
    # Rhiger & Mustafa (2025), 300 K: chi=5.32+0.45x-Eg.
    # Hence dEc/dz=(dEg/dx-0.45) dx/dz for the electron-driving band edge.
    e_drive = np.abs((degdx(xarr)-0.45)*DXDZ)
    field = MU*e_drive/(1.0 + (e_drive/E_SCALE)**ROLLOFF_EXP)
    dos = 1.5*D*(degdx(xarr)*DXDZ/eg(xarr))
    return field + dos


V = velocity(X)
V_HARM = 1.0/(np.trapezoid(1.0/V, Z_M)/L_M)


def make_kernels():
    wavelengths = np.asarray([wavelength_for_mean(z) for z in TARGET_DEPTHS_UM])
    kernels, pabs = [], []
    for lam in wavelengths:
        p, _, kfine = optical_kernel_fine(lam)
        k = np.interp(Z_UM, ZF_UM, kfine)
        k /= np.trapezoid(k, Z_UM)
        kernels.append(k)
        pabs.append(p)
    return wavelengths, np.asarray(pabs), kernels


WAVELENGTHS, PABS, KERNELS = make_kernels()


def fd_solution(freq_hz, kappa=0.0):
    s = 1j*2*np.pi*freq_hz
    kp = np.full_like(X, float(kappa)) if np.isscalar(kappa) else np.asarray(kappa, float)
    lam = kp + s
    v0, lam0 = V[0], kp[0] + s
    rp = (-v0 + np.sqrt(v0*v0 + 4*D*lam0))/(2*D)
    jp = v0/lam0
    rows, cols, vals = [], [], []
    rhs = np.zeros(N+1, complex)
    rows += [0,0,0]; cols += [0,1,2]
    vals += [-3/(2*DX)-rp, 4/(2*DX), -1/(2*DX)]
    rhs[0] = -rp*jp
    for i in range(1, N):
        rows += [i,i,i]; cols += [i-1,i,i+1]
        vals += [D/DX**2 - V[i]/(2*DX), -2*D/DX**2 - lam[i], D/DX**2 + V[i]/(2*DX)]
        rhs[i] = -V[i]
    rows.append(N); cols.append(N); vals.append(1.0)
    A = csr_matrix((np.asarray(vals,complex),(rows,cols)),shape=(N+1,N+1))
    return spsolve(A,rhs)


def shoot_solution(freq_hz):
    s = 1j*2*np.pi*freq_hz
    v0 = V[0]
    rp = (-v0 + np.sqrt(v0*v0 + 4j*D*2*np.pi*freq_hz))/(2*D)
    jp = v0/s

    def v_at(z):
        x = X_FRONT + (X_BACK-X_FRONT)*z/L_M
        return float(velocity(np.asarray([x]))[0])

    def rhs(z, y, forced=True):
        j, p = y
        vv = v_at(z)
        source = -vv if forced else 0.0
        return np.asarray([p, (source - vv*p + s*j)/D], complex)

    base0 = np.asarray([0.0+0j, -rp*jp], complex)
    sens0 = np.asarray([1.0+0j, rp], complex)
    opts = dict(method='DOP853', rtol=2e-11, atol=2e-13, dense_output=True, max_step=L_M/300)
    b = solve_ivp(lambda z,y: rhs(z,y,True), (0,L_M), base0, **opts)
    h = solve_ivp(lambda z,y: rhs(z,y,False), (0,L_M), sens0, **opts)
    coeff = -b.y[0,-1]/h.y[0,-1]
    return b.sol(Z_M)[0] + coeff*h.sol(Z_M)[0]


def homogeneous_solution(freq_hz, kappa=0.0):
    s = 1j*2*np.pi*freq_hz
    gam = (np.sqrt(V_HARM**2 + 4*D*(kappa+s))-V_HARM)/(2*D)
    return 1.0 - np.exp(-gam*(L_UM-Z_UM)*1e-6)


def currents(point_response):
    return np.asarray([np.trapezoid(k*point_response,Z_UM) for k in KERNELS])


def closure(js):
    d = np.diff(js)
    return 2*np.log(d[1])-np.log(d[0])-np.log(d[2])


def excess_from(point, freq):
    return closure(currents(point))-closure(currents(homogeneous_solution(freq)))


def graded_kappa_profile():
    # Deliberately steep activated sensitivity profile, anchored to the lower
    # end (5 us) of Kopytko et al.'s reported 300 K ~4-um-cutoff lifetime range.
    tau = 5e-6*np.exp((eg(X)-eg(0.325))/(KB*T/Q))
    return 1.0/tau, tau


def remaining_integral(y):
    c = np.concatenate(([0.0], cumulative_trapezoid(y,Z_M)))
    return c[-1]-c


def weighting_point_current(freq_hz, frac_change):
    span = TARGET_DEPTHS_UM[-1]-TARGET_DEPTHS_UM[0]
    center = 0.5*(TARGET_DEPTHS_UM[-1]+TARGET_DEPTHS_UM[0])
    weighting = 1.0 + (frac_change/span)*(Z_UM-center)
    omega = 2*np.pi*freq_hz
    phase = np.exp(-1j*omega*Z_M/V_HARM)
    inner = remaining_integral(weighting*phase)
    return np.exp(1j*omega*Z_M/V_HARM)*inner


def main():
    xi = 1.0-0.45/degdx(X)
    assert 0.665 < xi.min() < 0.667
    assert 0.694 < xi.max() < 0.696
    assert 2.21e4 < V_HARM < 2.23e4
    assert np.max(np.abs(WAVELENGTHS-np.asarray([2.13465049,2.21504239,2.30117342,2.39390681]))) < 2e-7
    assert PABS.min() > 0.9993

    target_deg = {}
    resource_db = {}
    for f in FREQS:
        jf = fd_solution(f)
        ex = excess_from(jf,f)
        target_deg[f] = np.degrees(ex.imag)
        d = np.diff(currents(jf))
        coeff = np.asarray([1/d[0],-(1/d[0]+2/d[1]),2/d[1]+1/d[2],-1/d[2]])
        sigma = abs(ex)/(3*np.linalg.norm(coeff))
        eta = sigma/np.mean(np.abs(d))
        resource_db[f] = 20*np.log10(1/eta)

    expected = {100e6:-0.0220167193,250e6:-0.0546243847,500e6:-0.1064448211,1e9:-0.1942321472}
    for f,val in expected.items(): assert abs(target_deg[f]-val) < 2e-7
    expected_snr = {100e6:90.8569,250e6:82.9466,500e6:77.0778,1e9:71.3939}
    for f,val in expected_snr.items(): assert abs(resource_db[f]-val) < 0.02

    for f in (100e6,500e6,1e9):
        es = excess_from(shoot_solution(f),f)
        assert abs(np.degrees(es.imag)-target_deg[f]) < 1e-5

    kp,tau = graded_kappa_profile()
    assert 3.8e-6 < tau.min() < 3.9e-6
    assert 0.88 < tau.max() < 0.90
    keff = np.trapezoid(kp/V,Z_M)/np.trapezoid(1/V,Z_M)
    for f,limit in ((100e6,5e-8),(500e6,2.5e-7),(1e9,4e-7)):
        ex = closure(currents(fd_solution(f,kp))) - closure(currents(homogeneous_solution(f,keff)))
        delta = abs(np.degrees(ex.imag)-target_deg[f])
        assert delta < limit

    phase_deg, coord_nm = {}, {}
    for f in (100e6,500e6,1e9):
        js = currents(fd_solution(f)); c0 = closure(js); eps=1e-7
        g=[]
        for m in range(4):
            j2=js.copy(); j2[m]*=np.exp(1j*eps)
            g.append((closure(j2).imag-c0.imag)/eps)
        sigma_rad = abs(np.radians(target_deg[f]))/(3*np.linalg.norm(g))
        phase_deg[f]=np.degrees(sigma_rad)
        omega=2*np.pi*f
        gam=(np.sqrt(V_HARM**2+4j*D*omega)-V_HARM)/(2*D)
        q=np.exp(-gam*0.5e-6)
        a=(gam/(q-1))*np.asarray([1,-(q+2),2*q+1,-q])
        coord_nm[f]=abs(np.radians(target_deg[f]))/(3*np.linalg.norm(np.imag(a)))*1e9
    assert abs(phase_deg[100e6]-1.88108e-4) < 2e-7
    assert abs(phase_deg[500e6]-9.14686e-4) < 2e-7
    assert abs(phase_deg[1e9]-1.70636e-3) < 3e-7
    for f in coord_nm: assert 4.45 < coord_nm[f] < 4.60

    wt={}
    for f in (100e6,500e6,1e9):
        c0=closure(currents(weighting_point_current(f,0)))
        def contam(a): return abs(np.degrees((closure(currents(weighting_point_current(f,a)))-c0).imag))
        wt[f]=brentq(lambda a: contam(a)-0.1*abs(target_deg[f]),0,0.05)
    assert abs(100*wt[100e6]-0.75683)<0.01
    assert abs(100*wt[500e6]-0.88129)<0.01
    assert abs(100*wt[1e9]-1.96060)<0.02

    fstar=np.sqrt(3)*V_HARM**2/D/(2*np.pi)
    assert abs(fstar/1e9-5.84986)<0.01

    print('PASS Rev7 regression')
    print('xi range:',xi.min(),xi.max())
    print('V_harm:',V_HARM,'m/s; f*:',fstar/1e9,'GHz')
    for f in FREQS:
        print(f'{f/1e6:7.1f} MHz excess={target_deg[f]:+.9f} deg SNR={resource_db[f]:.3f} dB')
    print('phase RMS [deg]:',phase_deg)
    print('coordinate RMS [nm]:',coord_nm)
    print('weighting 10% thresholds:',{f:100*v for f,v in wt.items()})


if __name__ == '__main__':
    main()
