"""Regression for HGCDTE_RELAXATION_LENGTH_PHASE_BOUNDARY.md.

This script compares the mean-energy ionization threshold against the
simplified direct-BTBT current-budget field. It is not a calibrated HgCdTe
impact-ionization simulator.
"""

import math

try:
    from scipy.special import lambertw
except Exception as exc:  # pragma: no cover
    raise SystemExit("This regression requires scipy.special.lambertw") from exc

Q = 1.602176634e-19
H = 6.62607015e-34
HBAR = 1.054571817e-34
C0 = 299792458.0
VK = 1.07e6


def eg_j(cutoff_um):
    return H * C0 / (cutoff_um * 1e-6)


def fk_v_m(cutoff_um):
    eg = eg_j(cutoff_um)
    return math.pi * eg**2 / (4.0 * Q * HBAR * VK)


def jk_a_m2(cutoff_um, length_um):
    lam = cutoff_um * 1e-6
    length = length_um * 1e-6
    return Q * math.pi**3 * C0**4 * length / (4.0 * VK**3 * lam**4)


def x_from_j(j):
    return 1.0 / (2.0 * lambertw(1.0 / (2.0 * math.sqrt(j)), 0).real)


def fj_v_cm(cutoff_um, length_um, current_a_cm2):
    j = current_a_cm2 * 1e4 / jk_a_m2(cutoff_um, length_um)
    return x_from_j(j) * fk_v_m(cutoff_um) / 100.0


def fdead_v_cm(cutoff_um, length_um, chi=1.0):
    return chi * eg_j(cutoff_um) / (Q * length_um * 1e-6) / 100.0


def critical_ell_um(cutoff_um, length_um, current_a_cm2, chi=1.0):
    f_dead = fdead_v_cm(cutoff_um, length_um, chi)
    f_j = fj_v_cm(cutoff_um, length_um, current_a_cm2)
    r = f_dead / f_j
    if r >= 1.0:
        return None, r, f_j, f_dead
    z = -(1.0 / r) * math.exp(-1.0 / r)
    y = 1.0 / r + lambertw(z, 0).real
    return length_um / y, r, f_j, f_dead


def residual(length_um, ell_um, r):
    return ell_um * (1.0 - math.exp(-length_um / ell_um)) - r * length_um


def main():
    cutoffs = [8, 10, 12, 17, 24]
    budgets = [1e-12, 1e-8, 1e-6]

    for budget in budgets:
        print(f"J*={budget:.0e} A/cm^2, L=1 um")
        for lam in cutoffs:
            ell, r, f_j, f_dead = critical_ell_um(lam, 1.0, budget)
            assert ell is not None
            assert abs(residual(1.0, ell, r)) < 1e-12
            print(
                f"{lam:2d} um: F_J={f_j:9.3f} V/cm, "
                f"F_dead={f_dead:8.3f} V/cm, "
                f"r={r:.6f}, ell_E*={ell:.6f} um"
            )
        print()

    # Representative values recorded in the derivation.
    ell10, _, _, _ = critical_ell_um(10, 1.0, 1e-12)
    ell17, _, _, _ = critical_ell_um(17, 1.0, 1e-12)
    assert abs(ell10 - 0.28770285213035807) < 1e-12
    assert abs(ell17 - 0.5291336429478135) < 1e-12

    # Critical tau_E range for representative high-field velocities.
    for lam, ell in [(10, ell10), (17, ell17)]:
        print(f"{lam} um critical relaxation time:")
        for velocity in [2.5e5, 5.0e5]:
            tau_ps = ell * 1e-6 / velocity * 1e12
            print(f"  v={velocity:.2e} m/s -> tau_E*={tau_ps:.6f} ps")


if __name__ == "__main__":
    main()
