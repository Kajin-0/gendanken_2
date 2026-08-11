"""Regression checks for the Rev. 4 adversarial-review corrections.

Checks only algebraic/numerical statements introduced in the surgical revision:
1. spatial-log aliasing leaves q unchanged and can yield another positive inverse;
2. unequal spacing can admit multiple attenuating q candidates;
3. linear weighting at s=kappa=0 has a quadratic particular solution and
   requires third differences (six colors) for exact polynomial annihilation;
4. independent-error coordinate and phase-calibration stress values.
"""
from __future__ import annotations
import cmath
import math
import numpy as np

D = 0.02327
W_ALIAS = 3.5e4
W_STRESS = 3.45e4
H = 0.5e-6


def gamma_rf(D: float, w: float, f: float) -> complex:
    s = 1j * 2.0 * math.pi * f
    return (-w + cmath.sqrt(w * w + 4.0 * D * s)) / (2.0 * D)


def inverse_no_recombination(gamma: complex, f: float) -> tuple[float, float]:
    a, b = gamma.real, gamma.imag
    omega = 2.0 * math.pi * f
    D_fit = omega * a / (b * (a * a + b * b))
    w_fit = omega * (b * b - a * a) / (b * (a * a + b * b))
    return D_fit, w_fit


def alias_check() -> None:
    f = 100e6
    g0 = gamma_rf(D, W_ALIAS, f)
    q0 = cmath.exp(-g0 * H)
    g1 = g0 + 2j * math.pi / H
    q1 = cmath.exp(-g1 * H)
    D1, w1 = inverse_no_recombination(g1, f)
    assert abs(q1 - q0) < 2e-14
    assert D1 > 0 and w1 > 0
    assert 6.5e-11 < D1 < 7.1e-11
    assert 45.0 < w1 < 55.0
    print(f"alias: gamma0={g0.real:.3f}+i{g0.imag:.3f} 1/m")
    print(f"alias inverse: D'={D1:.6e} m^2/s, w'={w1:.3f} m/s")


def arbitrary_spacing_check() -> None:
    R = -0.16
    roots = np.roots([1.0, 1.0, -R])
    roots = np.sort(roots)
    assert np.allclose(roots, [-0.8, -0.2], atol=1e-12)
    assert all(abs(q) < 1 for q in roots)
    print(f"unequal-spacing candidates for R={R}: {roots.tolist()}")


def weighting_singular_check() -> None:
    D0, w0, E0, E1 = 0.03, 3.0, 2.0, 0.4
    for z in np.linspace(-2.0, 2.0, 11):
        lhs = D0 * (-E1) + w0 * (-E0 - E1 * z)
        rhs = -(w0 * (E0 + E1 * z) + D0 * E1)
        assert abs(lhs - rhs) < 1e-13

    q = 0.73 + 0.08j
    m = np.arange(6)
    J = 1.2 - 0.4 * m + 0.17 * m**2 + (0.9 - 0.2j) * q**m
    d3 = np.diff(J, n=3)
    assert len(d3) == 3
    assert abs(d3[1] ** 2 - d3[0] * d3[2]) < 1e-12
    d2 = np.diff(J, n=2)
    assert abs(d2[1] ** 2 - d2[0] * d2[2]) > 1e-5
    print("weighting singular: quadratic particular verified; six-color third-difference closure PASS")


def nuisance_checks() -> None:
    target_deg = {100e6: 0.01198, 500e6: 0.05873, 1e9: 0.11041}
    expected_nm = {100e6: 3.8, 500e6: 3.8, 1e9: 3.6}
    for f, target in target_deg.items():
        g = gamma_rf(D, W_STRESS, f)
        q = cmath.exp(g * H)
        base = g / (q - 1.0)
        c = np.asarray([1.0, -(q + 2.0), 2.0 * q + 1.0, -q], dtype=complex) * base
        im_norm = float(np.linalg.norm(c.imag))
        sigma_m = math.radians(target) / 3.0 / im_norm
        sigma_nm = sigma_m * 1e9
        assert abs(sigma_nm - expected_nm[f]) < 0.15
        print(f"coordinate RMS @ {f/1e6:g} MHz: {sigma_nm:.3f} nm")

    L_um = 7.6
    z_um = np.asarray([2.5, 3.0, 3.5, 4.0])
    J = L_um - z_um
    h_um = 0.5
    phase_coeff = np.asarray([-J[0], 3*J[1], -3*J[2], J[3]]) / h_um
    phase_norm = float(np.linalg.norm(phase_coeff))
    assert abs(phase_norm - 39.0231) < 1e-3
    for f, target in target_deg.items():
        sigma_deg = target / 3.0 / phase_norm
        dt_fs = sigma_deg / 360.0 / f * 1e15
        print(f"phase RMS @ {f/1e6:g} MHz: {sigma_deg:.3e} deg ({dt_fs:.3f} fs)")
    assert 9.5e-5 < target_deg[100e6] / 3 / phase_norm < 1.1e-4


def main() -> None:
    alias_check()
    arbitrary_spacing_check()
    weighting_singular_check()
    nuisance_checks()
    print("PASS: Rev. 4 critique regression checks")


if __name__ == "__main__":
    main()
