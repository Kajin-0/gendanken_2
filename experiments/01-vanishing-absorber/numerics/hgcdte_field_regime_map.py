"""Deterministic regression for HGCDTE_FIELD_REGIME_MAP.md.

This is a scaling calculation, not a calibrated detector simulator.
All equations use the simplified Kane-substituted direct-BTBT model stated
in the accompanying derivation.
"""

import math

Q = 1.602176634e-19
HBAR = 1.054571817e-34
C0 = 299792458.0
VK = 1.07e6

C_BTBT = Q**3 / (4.0 * math.pi**3 * HBAR**2 * VK)
D_BTBT = math.pi**3 * HBAR * C0**2 / (Q * VK)


def j_btbt_a_cm2(field_v_cm, cutoff_um, length_um=1.0):
    """Direct BTBT current density in A/cm^2 for the simplified model."""
    field_si = field_v_cm * 100.0
    cutoff_si = cutoff_um * 1e-6
    length_si = length_um * 1e-6
    current_si = (
        C_BTBT
        * length_si
        * field_si**2
        * math.exp(-D_BTBT / (field_si * cutoff_si**2))
    )
    return current_si / 1e4


def crossover_um(field_v_cm, current_budget_a_cm2, length_um=1.0):
    """Cutoff where J_BTBT(field) equals the stated current-density budget."""
    field_si = field_v_cm * 100.0
    current_si = current_budget_a_cm2 * 1e4
    length_si = length_um * 1e-6
    prefactor = C_BTBT * length_si * field_si**2
    if prefactor <= current_si:
        raise ValueError("No finite crossover: prefactor <= current budget.")
    cutoff_si = math.sqrt(
        D_BTBT / (field_si * math.log(prefactor / current_si))
    )
    return cutoff_si * 1e6


def transit_hz(velocity_m_s, length_um):
    """Rectangular-Ramo-pulse -3 dB transit convention used in the repo."""
    c_t = 0.44295
    return c_t * velocity_m_s / (length_um * 1e-6)


def main():
    reference_fields = [100, 200, 500, 1000, 1500]
    current_budgets = [1e-12, 1e-8, 1e-6]

    print("Crossover cutoff lambda_x [um], L=1 um")
    print("F[V/cm] " + " ".join(f"J={j:.0e}" for j in current_budgets))
    for field in reference_fields:
        values = [crossover_um(field, j) for j in current_budgets]
        print(f"{field:7.0f} " + " ".join(f"{x:9.3f}" for x in values))

    print("\nDirect BTBT at F=500 V/cm, L=1 um")
    for cutoff in [10, 17, 24, 30, 40]:
        print(
            f"{cutoff:4.0f} um  "
            f"{j_btbt_a_cm2(500, cutoff):.6e} A/cm^2"
        )

    print("\nTransit envelope for v=5e5 m/s")
    for length in [0.2, 0.5, 1, 2, 5, 10]:
        print(
            f"{length:4.1f} um  "
            f"{transit_hz(5e5, length) / 1e9:9.3f} GHz"
        )

    # Regression values recorded in HGCDTE_FIELD_REGIME_MAP.md.
    assert abs(crossover_um(100, 1e-12) - 74.4126684338) < 1e-8
    assert abs(crossover_um(500, 1e-12) - 31.6725072071) < 1e-8
    assert abs(crossover_um(500, 1e-6) - 41.0339402681) < 1e-8
    expected = 2.09608721385e-49
    assert abs(j_btbt_a_cm2(500, 17) - expected) / expected < 1e-10
    assert abs(transit_hz(5e5, 1.0) - 2.21475e11) < 1.0


if __name__ == "__main__":
    main()
