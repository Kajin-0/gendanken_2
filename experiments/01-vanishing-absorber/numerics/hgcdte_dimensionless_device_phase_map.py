"""Dimensionless phase-map regression for the graded HgCdTe device branch.

No material relaxation length is guessed here. The script checks the analytic
mean-II margin, the r_min inversion, the boundary voltage-margin definition,
and the normalized transit-floor bookkeeping.
"""

import math


def A(r):
    if abs(r) < 1e-10:
        return 1.0 - r / 2.0 + r * r / 6.0
    return -math.expm1(-r) / r


def ii_margin(zeta, r, chi=1.0):
    if not (0.0 < zeta < 1.0):
        raise ValueError("zeta must lie between 0 and 1")
    return chi * (1.0 - zeta) / (zeta * A(r))


def rmin(zeta, chi=1.0):
    zeta_ballistic = chi / (1.0 + chi)
    if zeta <= zeta_ballistic:
        return 0.0
    target = chi * (1.0 - zeta) / zeta
    lo, hi = 0.0, 1.0
    while A(hi) > target:
        hi *= 2.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if A(mid) > target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def boundary_margin(vcap, vb):
    if vb <= 0.0:
        raise ValueError("vb must be positive")
    return vcap / vb


def normalized_transit_floor(zeta, chi, rho_e, cooling_fraction, nu_tat, nu_z):
    if not (0.0 < cooling_fraction < 1.0):
        raise ValueError("cooling_fraction must lie between 0 and 1")
    absorber = rmin(zeta, chi)
    boundary = max(
        rho_e * math.log(1.0 / cooling_fraction),
        nu_tat,
        nu_z,
    )
    return absorber + boundary


def classify(m_ii, m_b):
    if m_ii >= 1.0 and m_b >= 1.0:
        return "jointly feasible"
    if m_ii < 1.0 and m_b >= 1.0:
        return "hot-electron limited"
    if m_ii >= 1.0 and m_b < 1.0:
        return "boundary-tunneling limited"
    return "jointly infeasible"


def main():
    # The analytic phase boundary must give unit margin.
    for chi in (0.8, 1.0, 1.2):
        for r in (0.0, 0.1, 0.5, 1.0, 3.0, 10.0):
            rr = 1e-12 if r == 0.0 else r
            zc = chi / (chi + A(rr))
            assert abs(ii_margin(zc, rr, chi) - 1.0) < 1e-12

    # More relaxation distance improves the mean-II margin at fixed grading.
    zeta = 0.7
    margins = [ii_margin(zeta, r, 1.0) for r in (0.01, 0.1, 0.5, 1.0, 3.0, 10.0)]
    assert all(b > a for a, b in zip(margins, margins[1:]))

    # r_min must land on the unit-margin boundary when nonzero.
    for zeta in (0.55, 0.60, 0.70, 0.80, 0.90):
        rm = rmin(zeta)
        assert rm > 0.0
        assert abs(ii_margin(zeta, rm) - 1.0) < 1e-11

    # Boundary margin is exactly the voltage-capacity ratio.
    assert boundary_margin(0.12, 0.10) == 1.2
    assert classify(1.1, 1.2) == "jointly feasible"
    assert classify(0.9, 1.2) == "hot-electron limited"
    assert classify(1.1, 0.8) == "boundary-tunneling limited"
    assert classify(0.9, 0.8) == "jointly infeasible"

    # Transit floor must be governed by the largest boundary requirement.
    theta = normalized_transit_floor(
        zeta=0.70,
        chi=1.0,
        rho_e=0.5,
        cooling_fraction=0.10,
        nu_tat=0.8,
        nu_z=0.2,
    )
    expected = rmin(0.70) + max(0.5 * math.log(10.0), 0.8, 0.2)
    assert abs(theta - expected) < 1e-13

    print("dimensionless HgCdTe device phase-map regression: PASS")
    print()
    print("Mean-II margin for chi=1")
    print("zeta  r=0.1   r=0.5   r=1     r=2     r=5")
    for zeta in (0.40, 0.50, 0.60, 0.70, 0.80):
        vals = [ii_margin(zeta, r) for r in (0.1, 0.5, 1.0, 2.0, 5.0)]
        print(f"{zeta:4.2f}  " + "  ".join(f"{v:7.3f}" for v in vals))

    print()
    print("Minimum L/ell_E for mean-II safety, chi=1")
    for zeta in (0.50, 0.55, 0.60, 0.70, 0.80, 0.90):
        print(f"zeta={zeta:4.2f}  r_min={rmin(zeta):.6f}")


if __name__ == "__main__":
    main()
