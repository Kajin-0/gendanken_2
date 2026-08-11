"""2-D finite-electrode/depletion stress for the spectral-depth closure hierarchy.

This is a geometry hardening calculation, not a calibrated detector model.
It solves separate 2-D physical and Shockley-Ramo weighting potentials, follows
deterministic saturated-drift trajectories, integrates H(omega)=int exp(-iwt)
d(phi_w), averages over six HgCdTe optical kernels, and applies the existing
four-/five-/six-color diagnostics without first fitting away the geometry.

Requires numpy/scipy and hgcdte_ramo_four_color_gradient_prediction.py.
"""

from __future__ import annotations

from dataclasses import dataclass
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.interpolate import CubicSpline
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve

from hgcdte_ramo_four_color_gradient_prediction import (
    L_UM,
    Z_UM as OPT_Z_UM,
    optical_kernel,
    wavelength_for_mean,
)

WIDTH_UM = 16.0
V_BIAS = 0.30
MU = 0.90
V_SAT = 6.0e4
FREQUENCIES = np.asarray((0.0, 100e6, 500e6, 1e9))
DEPTHS = np.arange(2.0, 4.51, 0.5)
WAVELENGTHS = np.asarray([wavelength_for_mean(z) for z in DEPTHS])
OPTICS = [optical_kernel(wl) for wl in WAVELENGTHS]
X_SIGMA_UM = 2.0
X_EXTENT_UM = 3.5

GRADIENT_TARGET_DEG = {100e6: -0.011978, 500e6: -0.058727, 1e9: -0.110405}
GRADIENT_SNR_DB = {100e6: 96.1, 500e6: 82.3, 1e9: 76.7}


@dataclass(frozen=True)
class Scenario:
    name: str
    contact_fraction: float
    depletion_width_um: float = 0.0
    space_charge_drop_v: float = 0.0


SCENARIOS = (
    Scenario("planar", 1.00),
    Scenario("finite75", 0.75),
    Scenario("finite75_depletion", 0.75, 3.0, 0.05),
    Scenario("finite50_depletion", 0.50, 3.0, 0.05),
)


def solve_potential(s: Scenario, top_value: float, nx: int, nz: int, weighting=False):
    W = WIDTH_UM * 1e-6
    L = L_UM * 1e-6
    xs = np.linspace(-W / 2, W / 2, nx)
    zs = np.linspace(0, L, nz)
    dx, dz = xs[1] - xs[0], zs[1] - zs[0]
    half = s.contact_fraction * W / 2
    A = lil_matrix((nx * nz, nx * nz), dtype=float)
    b = np.zeros(nx * nz)

    def k(j, i):
        return j * nx + i

    for j, z in enumerate(zs):
        for i, x in enumerate(xs):
            r = k(j, i)
            if j == 0:
                A[r, r] = 1.0
            elif j == nz - 1 and abs(x) <= half + 1e-15:
                A[r, r] = 1.0
                b[r] = top_value
            elif j == nz - 1:
                A[r, r], A[r, k(j - 1, i)] = 1.0, -1.0
            elif i == 0:
                A[r, r], A[r, k(j, i + 1)] = 1.0, -1.0
            elif i == nx - 1:
                A[r, r], A[r, k(j, i - 1)] = 1.0, -1.0
            else:
                A[r, r] = -2 / dx**2 - 2 / dz**2
                A[r, k(j, i - 1)] = A[r, k(j, i + 1)] = 1 / dx**2
                A[r, k(j - 1, i)] = A[r, k(j + 1, i)] = 1 / dz**2
                if not weighting and s.depletion_width_um > 0:
                    Wd = s.depletion_width_um * 1e-6
                    if z >= L - Wd:
                        b[r] = 2 * s.space_charge_drop_v / Wd**2

    return xs, zs, spsolve(A.tocsr(), b).reshape(nz, nx)


def geometry(s: Scenario, nx=121, nz=91):
    xs, zs, pw = solve_potential(s, 1.0, nx, nz, weighting=True)
    _, _, V = solve_potential(s, V_BIAS, nx, nz, weighting=False)
    dwdz, dwdx = np.gradient(pw, zs, xs, edge_order=2)
    dVdz, dVdx = np.gradient(V, zs, xs, edge_order=2)
    return dict(s=s, xs=xs, zs=zs, pw=pw, dwdx=dwdx, dwdz=dwdz,
                dVdx=dVdx, dVdz=dVdz)


def interp(g, key, x, z):
    xs, zs, a = g["xs"], g["zs"], g[key]
    dx, dz = xs[1] - xs[0], zs[1] - zs[0]
    x, z = np.clip(x, xs[0], xs[-1]), np.clip(z, zs[0], zs[-1])
    i, j = int((x - xs[0]) / dx), int((z - zs[0]) / dz)
    i, j = min(i, len(xs) - 2), min(j, len(zs) - 2)
    tx, tz = (x - xs[i]) / dx, (z - zs[j]) / dz
    return float((1-tx)*(1-tz)*a[j,i] + tx*(1-tz)*a[j,i+1]
                 + (1-tx)*tz*a[j+1,i] + tx*tz*a[j+1,i+1])


def velocity(gx, gz):
    E = float(np.hypot(gx, gz))
    if E < 1e-12:
        return 0.0, 0.0, 0.0
    v0 = MU * E
    speed = v0 / np.sqrt(1 + (v0 / V_SAT)**2)
    return speed * gx / E, speed * gz / E, speed


def trajectory(g, x0_um, z0_um, ds_um=0.020, max_steps=8000):
    xs, zs = g["xs"], g["zs"]
    x, z = x0_um * 1e-6, z0_um * 1e-6
    L, W = zs[-1], xs[-1] - xs[0]
    half = g["s"].contact_fraction * W / 2
    omega = 2 * np.pi * FREQUENCIES
    H = np.zeros(len(FREQUENCIES), complex)
    t, ds = 0.0, ds_um * 1e-6
    phi0 = phi = interp(g, "pw", x, z)
    reached = False

    for _ in range(max_steps):
        if z >= L - 0.002e-6 and abs(x) <= half + 0.005e-6:
            reached = True
            break
        gx, gz = interp(g, "dVdx", x, z), interp(g, "dVdz", x, z)
        vx, vz, speed = velocity(gx, gz)
        if speed < 1:
            break
        ux, uz = vx / speed, vz / speed
        step = ds
        if uz > 1e-10:
            step = min(step, max(1e-12, (L-z)/uz))
        xm, zm = x + 0.5*step*ux, z + 0.5*step*uz
        vx, vz, speed = velocity(interp(g, "dVdx", xm, zm),
                                 interp(g, "dVdz", xm, zm))
        ux, uz = vx / speed, vz / speed
        xn = float(np.clip(x + step*ux, xs[0], xs[-1]))
        zn = float(np.clip(z + step*uz, zs[0], zs[-1]))
        phin = interp(g, "pw", xn, zn)
        dt = step / speed
        H += (phin - phi) * np.exp(-1j * omega * (t + 0.5*dt))
        x, z, phi, t = xn, zn, phin, t + dt

    if reached:
        H += (1 - phi) * np.exp(-1j * omega * t)
    return H, t, reached, phi0


def gauss(a, b, n):
    u, w = leggauss(n)
    return 0.5*(b-a)*u + 0.5*(a+b), 0.5*(b-a)*w


def currents(s: Scenario, nx=121, nz=91, nx_src=13, nz_src=41, ds_um=0.020):
    g = geometry(s, nx, nz)
    x, wx = gauss(-X_EXTENT_UM, X_EXTENT_UM, nx_src)
    beam = np.exp(-0.5*(x/X_SIGMA_UM)**2)
    beam /= np.sum(wx*beam)
    zsrc = np.linspace(0.01, L_UM-0.01, nz_src)
    transfer = np.zeros((nx_src, nz_src, len(FREQUENCIES)), complex)
    collected, dc_error, tmax = 0, 0.0, 0.0

    for ix, x0 in enumerate(x):
        for iz, z0 in enumerate(zsrc):
            H, t, ok, phi0 = trajectory(g, x0, z0, ds_um)
            transfer[ix, iz] = H
            collected += int(ok)
            dc_error = max(dc_error, abs(H[0].real - (1-phi0)))
            tmax = max(tmax, t)

    mask = (OPT_Z_UM >= zsrc[0]) & (OPT_Z_UM <= zsrc[-1])
    zd = OPT_Z_UM[mask]
    J = np.zeros((len(FREQUENCIES), len(DEPTHS)), complex)
    for ix in range(nx_src):
        for jf in range(len(FREQUENCIES)):
            Hz = CubicSpline(zsrc, transfer[ix, :, jf])(zd)
            for m, row in enumerate(OPTICS):
                J[jf, m] += wx[ix]*beam[ix]*np.trapezoid(row[3][mask]*Hz, zd)

    return J, dict(collected=collected/(nx_src*nz_src),
                   dc_error=dc_error, tmax=tmax)


def closure(y):
    return complex(2*np.log(y[1]) - np.log(y[0]) - np.log(y[2]))


def metrics(J):
    out = []
    for f, j in zip(FREQUENCIES, J):
        d = np.diff(j)
        c4 = closure(d[1:4])
        c5 = closure(np.diff(j[:5], n=2))
        H = np.array([[d[0],d[1],d[2]],[d[1],d[2],d[3]],[d[2],d[3],d[4]]])
        sv = np.linalg.svd(H, compute_uv=False)
        W0 = d[0]*d[2] - d[1]**2
        coeff = np.sqrt(abs(d[2])**2 + abs(d[2]+2*d[1])**2
                        + abs(d[0]+2*d[1])**2 + abs(d[0])**2)
        step = np.mean(np.abs(d))
        eta3 = abs(W0)/(3*step*coeff)
        snr3 = 20*np.log10(1/eta3)

        A = np.column_stack((d[1:4], -d[0:3]))
        S, P = np.linalg.lstsq(A, d[2:5], rcond=None)[0]
        roots = np.roots([1, -S, P])
        rsum = np.sum(np.log(roots)/(0.5e-6))
        recur = np.linalg.norm(A @ np.array([S,P]) - d[2:5]) / np.linalg.norm(d[2:5])

        out.append(dict(f=f, c4=c4, c5=c5, s21=sv[1]/sv[0],
                        s32=sv[2]/sv[1], snr3=snr3, rsum=rsum,
                        recurrence=recur))
    return out


def main():
    print("Six-color HgCdTe coordinate")
    for d, wl, row in zip(DEPTHS, WAVELENGTHS, OPTICS):
        print(f"{d:3.1f} um -> {wl:.9f} um, Pabs={row[0]:.9f}, "
              f"sigma={np.sqrt(row[2]):.6f} um")
    print()

    result = {}
    for s in SCENARIOS:
        J, diag = currents(s)
        M = metrics(J)
        result[s.name] = (J, diag, M)
        print(f"[{s.name}] collected={diag['collected']:.6f}, "
              f"DC_Ramo_error={diag['dc_error']:.3e}, "
              f"tmax={1e12*diag['tmax']:.2f} ps")
        for m in M:
            print(f"{m['f']/1e6:7.1f} MHz  "
                  f"C4phi={np.degrees(m['c4'].imag):+.6f} deg  "
                  f"|C4|={abs(m['c4']):.3e}  "
                  f"C5phi={np.degrees(m['c5'].imag):+.6f} deg  "
                  f"s2/s1={m['s21']:.3e}  s3/s2={m['s32']:.3e}  "
                  f"rank2@3sigma={m['snr3']:.2f} dB  "
                  f"Im(sum_r)={m['rsum'].imag/1e6:+.3f} 1/um")
        print()

    P = result["planar"][2]
    F75 = result["finite75"][2]
    D75 = result["finite75_depletion"][2]
    D50 = result["finite50_depletion"][2]

    print("Geometry excess over planar same-optics baseline")
    for k in (1,2,3):
        f = FREQUENCIES[k]
        p = np.degrees(P[k]["c4"].imag)
        e75 = np.degrees(F75[k]["c4"].imag)-p
        ed75 = np.degrees(D75[k]["c4"].imag)-p
        ed50 = np.degrees(D50[k]["c4"].imag)-p
        print(f"{f/1e6:7.1f} MHz: finite75={e75:+.6f} deg; "
              f"finite75+dep={ed75:+.6f} deg "
              f"({abs(ed75/GRADIENT_TARGET_DEG[f]):.3f} x target); "
              f"finite50+dep={ed50:+.6f} deg")

    Jc, dc = currents(SCENARIOS[2], nx=81, nz=61, nx_src=9, nz_src=31, ds_um=0.035)
    Mc = metrics(Jc)
    print("\nFinite75+depletion convergence")
    for k in (1,2,3):
        coarse = np.degrees(Mc[k]["c4"].imag)
        fine = np.degrees(D75[k]["c4"].imag)
        rel = abs((fine-coarse)/fine)
        print(f"{FREQUENCIES[k]/1e6:7.1f} MHz: {coarse:+.6f} -> "
              f"{fine:+.6f} deg ({100*rel:.2f}%)")
        assert rel < 0.07

    assert result["finite75_depletion"][1]["collected"] == 1.0
    assert result["finite75_depletion"][1]["dc_error"] < 1e-12
    assert 83 < D75[1]["snr3"] < 86
    assert 70 < D50[1]["snr3"] < 73
    assert GRADIENT_SNR_DB[100e6] > D75[1]["snr3"]
    assert D75[1]["s32"] < 0.02 and D50[1]["s32"] < 0.02

    excess100 = np.degrees(D75[1]["c4"].imag - P[1]["c4"].imag)
    assert -0.0095 < excess100 < -0.0080

    print("\nPASS: 2-D finite-electrode/depletion geometry can mimic an O(1) "
          "fraction of the four-color gradient phase, but it produces a "
          "lower-SNR second-mode witness and fails the simple RF root law. "
          "The five-color linear-observation annihilator is not universal "
          "for curved multidimensional geometry.")


if __name__ == "__main__":
    main()
