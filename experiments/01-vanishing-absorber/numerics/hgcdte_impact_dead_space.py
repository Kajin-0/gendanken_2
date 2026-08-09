"""Regression for HGCDTE_IMPACT_IONIZATION_DEAD_SPACE.md.

Cold-injection field-work estimate plus the simplified HgCdTe Kane/BTBT
normalization used elsewhere in this repository. Not a full APD simulator.
"""

import math

Q = 1.602176634e-19
H = 6.62607015e-34
HBAR = 1.054571817e-34
C0 = 299792458.0
VK = 1.07e6


def eg_j(cutoff_um):
    return H * C0 / (cutoff_um * 1e-6)


def kane_length_m(cutoff_um):
    return HBAR * VK / eg_j(cutoff_um)


def fk_v_cm(cutoff_um):
    eg = eg_j(cutoff_um)
    return (math.pi * eg**2 / (4.0 * Q * HBAR * VK)) / 100.0


def f_dead_v_cm(cutoff_um, length_um, chi=1.0):
    return (chi * eg_j(cutoff_um) / (Q * length_um * 1e-6)) / 100.0


def x_dead(cutoff_um, length_um, chi=1.0):
    return f_dead_v_cm(cutoff_um, length_um, chi) / fk_v_cm(cutoff_um)


def normalized_btbt(x):
    return x * x * math.exp(-1.0 / x)


def j_btbt_a_cm2(field_v_cm, cutoff_um, length_um=1.0):
    field = field_v_cm * 100.0
    length = length_um * 1e-6
    eg = eg_j(cutoff_um)
    fk = math.pi * eg**2 / (4.0 * Q * HBAR * VK)
    pref = Q**3 * length / (4.0 * math.pi**3 * HBAR**2 * VK)
    return pref * field**2 * math.exp(-fk / field) / 1e4


def main():
    cutoffs = [8, 10, 12, 17, 24]
    lengths = [0.5, 1.0, 2.0, 5.0]

    print("Cold-injection field-work threshold F_dead [V/cm], chi=1")
    print("cutoff " + " ".join(f"L={L:g}um" for L in lengths))
    for lam in cutoffs:
        vals = [f_dead_v_cm(lam, L) for L in lengths]
        print(f"{lam:5.0f}um " + " ".join(f"{x:10.3f}" for x in vals))

    print("\nL=1 um: F_dead/F_K, log10(j_dead), J_BTBT(F_dead)")
    for lam in cutoffs:
        x = x_dead(lam, 1.0)
        jn = normalized_btbt(x)
        ja = j_btbt_a_cm2(f_dead_v_cm(lam, 1.0), lam, 1.0)
        print(
            f"{lam:5.0f}um  x={x:.8f}  "
            f"log10(j)={math.log10(jn):9.3f}  J={ja:.6e} A/cm^2"
        )

    # Algebraic identity x_dead = (4 chi/pi) ell_K/L.
    for lam in cutoffs:
        for L in lengths:
            rhs = (4.0 / math.pi) * kane_length_m(lam) / (L * 1e-6)
            assert abs(x_dead(lam, L) - rhs) < 1e-14

    # Recorded table values.
    assert abs(f_dead_v_cm(10, 1.0) - 1239.8419843320) < 1e-9
    assert abs(f_dead_v_cm(17, 1.0) - 729.31881431294) < 1e-9
    expected = 3.8447099038566555e-57
    got = j_btbt_a_cm2(f_dead_v_cm(10, 1.0), 10, 1.0)
    assert abs(got - expected) / expected < 1e-10


if __name__ == "__main__":
    main()
