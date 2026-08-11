#!/usr/bin/env python3
"""Regression checks for the Rev. 6 adversarial-review corrections."""
from __future__ import annotations

import cmath
import math
import numpy as np

# --- Post-detection rank-two conditioning ---
Z = 3.0
rel_p = math.sqrt(2.0) / Z
assert abs(rel_p - 0.4714045207910317) < 1e-14
assert abs(math.sqrt(2.0) / 0.10 - 14.142135623730951) < 1e-12

# --- HgCdTe force-partition point-source finite-diffusion sweep ---
L = 7.6e-6
T = 300.0
X_FRONT, X_BACK = 0.55, 0.32
MU = 0.90
KB = 1.380649e-23
QE = 1.602176634e-19
D = MU * KB * T / QE
E_ROLLOFF = 8.0e5
R_S = 2.2
DEPTHS = np.array([2.5, 3.0, 3.5, 4.0]) * 1e-6
DX_DZ = (X_BACK - X_FRONT) / L


def eg(x: float) -> float:
    return -0.302 + 1.93*x - 0.81*x*x + 0.832*x**3 + 5.35e-4*(1.0 - 2.0*x)*T


def degdx(x: float) -> float:
    return 1.93 - 1.62*x + 2.496*x*x - 2.0*5.35e-4*T


def velocity(z: float, xi: float) -> float:
    x = X_FRONT + (X_BACK - X_FRONT) * z / L
    gap = eg(x)
    dg = degdx(x)
    e_drive = xi * abs(dg * DX_DZ)
    v_field = MU * e_drive / (1.0 + (e_drive / E_ROLLOFF)**R_S)
    v_dos = (3.0 * D / 2.0) * (dg * DX_DZ / gap)
    return v_field + v_dos


def closure(values: np.ndarray) -> complex:
    d = np.diff(values)
    return np.log(d[1]**2 / (d[0] * d[2]))


def point_source_phase_deg(xi: float, f_hz: float = 100e6, dz_target: float = 2e-9) -> float:
    s = 1j * 2.0 * math.pi * f_hz
    n = int(round(L / dz_target))
    dz = L / n
    depth_indices = [int(round(z / dz)) for z in DEPTHS]
    v0 = velocity(0.0, xi)
    j_part = v0 / s
    r_plus = (-v0 + cmath.sqrt(v0*v0 + 4.0*D*s)) / (2.0*D)

    def rhs(z: float, y: np.ndarray) -> np.ndarray:
        j, jp = y
        v = velocity(z, xi)
        return np.array([jp, (-v - v*jp + s*j) / D], dtype=complex)

    def integrate(j0: complex, collect: bool = False):
        y = np.array([j0, r_plus*(j0 - j_part)], dtype=complex)
        vals: dict[int, complex] = {}
        for i in range(n):
            z = i * dz
            k1 = rhs(z, y)
            k2 = rhs(z + 0.5*dz, y + 0.5*dz*k1)
            k3 = rhs(z + 0.5*dz, y + 0.5*dz*k2)
            k4 = rhs(z + dz, y + dz*k3)
            y = y + dz*(k1 + 2*k2 + 2*k3 + k4)/6.0
            if collect and i + 1 in depth_indices:
                vals[i + 1] = y[0]
        return y, vals

    y0, _ = integrate(0j)
    y1, _ = integrate(1.0 + 0j)
    sensitivity = y1[0] - y0[0]
    j0 = -y0[0] / sensitivity
    y, vals = integrate(j0, collect=True)
    assert abs(y[0]) < 1e-14
    js = np.array([vals[i] for i in depth_indices])
    return closure(js).imag * 180.0 / math.pi


expected = {
    0.3: -0.0074085719346,
    0.6: -0.0182242824894,
    1.0: -0.0124582993362,
}
for xi, target in expected.items():
    got = point_source_phase_deg(xi)
    assert abs(got - target) < 2e-9, (xi, got, target)

# Baseline midpoint drift used in the manuscript table.
zc = 3.25e-6
expected_v = {0.3: 8.37905715294e3, 0.6: 1.96980267957e4, 1.0: 3.47570371931e4}
for xi, target in expected_v.items():
    got = velocity(zc, xi)
    assert abs(got - target) / target < 1e-10, (xi, got, target)

print("Rev6 regression: PASS")
print(f"simplified 3sigma product relative uncertainty = {rel_p:.6f}")
for xi in (0.3, 0.6, 1.0):
    print(f"xi={xi:.1f}: v(zc)={velocity(zc,xi):.6e} m/s, phase={point_source_phase_deg(xi):.9f} deg")
