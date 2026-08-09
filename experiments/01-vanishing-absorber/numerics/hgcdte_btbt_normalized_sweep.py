"""Normalized HgCdTe direct-BTBT scaling audit.

Standard-library only.

This script implements the simplified scaling model documented in
HGCDTE_NORMALIZED_BTBT_FRONTIER.md.  It is not a device simulator.

It computes:
- Eg = h c / lambda_c;
- simplified Kane field F_K;
- normalized current scale J_K;
- j(x) = x^2 exp(-1/x);
- F_max for a specified absolute J target using monotonic bisection;
- optimistic c_t v_K / L transit envelope.

Units:
- SI internally;
- wavelength input in micrometres;
- thickness input in micrometres;
- current-density targets/output in A/cm^2;
- fields output in V/cm.
"""

from __future__ import annotations

import math


Q = 1.602176634e-19
HBAR = 1.054571817e-34
H = 2.0 * math.pi * HBAR
C = 299_792_458.0
V_K = 1.07e6
C_T = 0.44295


def scales(lambda_um: float, L_um: float, v_k: float = V_K):
    lam = lambda_um * 1e-6
    L = L_um * 1e-6

    E_g = H * C / lam
    F_K = math.pi * E_g * E_g / (4.0 * Q * HBAR * v_k)
    J_K = Q * math.pi**3 * C**4 * L / (4.0 * v_k**3 * lam**4)
    ell_K = HBAR * v_k / E_g
    B_kin = C_T * v_k / L

    return {
        "Eg_eV": E_g / Q,
        "F_K_V_per_m": F_K,
        "J_K_A_per_m2": J_K,
        "ell_K_m": ell_K,
        "B_kin_Hz": B_kin,
    }


def normalized_current(x: float) -> float:
    if x <= 0.0:
        return 0.0
    return x * x * math.exp(-1.0 / x)


def invert_normalized_current(j_target: float) -> float:
    """Solve x^2 exp(-1/x) = j_target by monotonic bisection."""
    if j_target <= 0.0:
        return 0.0

    lo = 0.0
    hi = 1.0
    while normalized_current(hi) < j_target:
        hi *= 2.0

    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if normalized_current(mid) < j_target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def field_for_current(lambda_um: float, L_um: float, J_A_per_cm2: float):
    s = scales(lambda_um, L_um)
    J_target_si = J_A_per_cm2 * 1e4
    j = J_target_si / s["J_K_A_per_m2"]
    x = invert_normalized_current(j)
    return x, x * s["F_K_V_per_m"]


def check_algebraic_scale_identity():
    for lambda_um in (3, 5, 8, 10, 12, 17, 24):
        for L_um in (0.25, 1.0, 2.0):
            s = scales(lambda_um, L_um)
            lam = lambda_um * 1e-6
            L = L_um * 1e-6
            E_g = H * C / lam
            J_alt = Q * L * E_g**4 / (64.0 * math.pi * HBAR**4 * V_K**3)
            rel = abs(J_alt - s["J_K_A_per_m2"]) / s["J_K_A_per_m2"]
            assert rel < 5e-14, rel


def check_inversion():
    for j in (1e-30, 1e-20, 1e-12, 1e-6, 1e-2, 1.0, 10.0):
        x = invert_normalized_current(j)
        recovered = normalized_current(x)
        rel = abs(recovered - j) / j
        assert rel < 2e-13, (j, x, recovered, rel)


def print_scale_table(L_um: float = 1.0):
    print(f"HgCdTe simplified Kane scaling; L = {L_um:g} um")
    print(
        "lambda_um  Eg_eV    F_K[V/cm]    J_K[A/cm2]     ell_K[nm]   B_kin[GHz]"
    )
    for lam in (3, 5, 8, 10, 12, 17, 24):
        s = scales(lam, L_um)
        print(
            f"{lam:8.1f}  "
            f"{s['Eg_eV']:6.4f}  "
            f"{s['F_K_V_per_m']/100:11.3e}  "
            f"{s['J_K_A_per_m2']/1e4:12.3e}  "
            f"{s['ell_K_m']*1e9:10.3f}  "
            f"{s['B_kin_Hz']/1e9:10.3f}"
        )


def print_field_table(L_um: float = 1.0):
    J_targets = (1e-6, 1e-4, 1e-2, 1.0)
    header = "lambda_um" + "".join(f"   F@{J:g}[V/cm]" for J in J_targets)
    print("\nDirect-BTBT-only field ceilings")
    print(f"L = {L_um:g} um")
    print(header)
    for lam in (5, 8, 10, 12, 17):
        fields = []
        for J in J_targets:
            _, F_si = field_for_current(lam, L_um, J)
            fields.append(F_si / 100.0)
        print(f"{lam:8.1f}" + "".join(f"   {F:13.3e}" for F in fields))


def print_normalized_curve():
    print("\nUniversal normalized curve j=x^2 exp(-1/x)")
    print("x=F/F_K       j=J/J_K")
    for x in (0.02, 0.03, 0.04, 0.05, 0.075, 0.1, 0.2, 0.5, 1.0):
        print(f"{x:9.3f}       {normalized_current(x):.6e}")


if __name__ == "__main__":
    check_algebraic_scale_identity()
    check_inversion()
    print_scale_table(L_um=1.0)
    print_field_table(L_um=1.0)
    print_normalized_curve()
