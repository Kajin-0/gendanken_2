"""Regression for HGCDTE_II_SAFE_TRANSIT_CEILING.md.

Checks the Lambert-W inversion against direct bisection of
A(r)=(1-exp(-r))/r. This is not a calibrated HgCdTe transport model.
"""

import math

try:
    from scipy.special import lambertw
except Exception as exc:  # pragma: no cover
    raise SystemExit("This regression requires scipy.special.lambertw") from exc


def A(r):
    if abs(r) < 1e-10:
        return 1.0 - r / 2.0 + r * r / 6.0
    return -math.expm1(-r) / r


def rmin_lambert(zeta, chi=1.0):
    zeta_ballistic = chi / (1.0 + chi)
    if zeta <= zeta_ballistic:
        return 0.0
    a = chi * (1.0 - zeta) / zeta
    arg = -(1.0 / a) * math.exp(-1.0 / a)
    return 1.0 / a + float(lambertw(arg, 0).real)


def rmin_bisect(zeta, chi=1.0):
    zeta_ballistic = chi / (1.0 + chi)
    if zeta <= zeta_ballistic:
        return 0.0
    a = chi * (1.0 - zeta) / zeta
    lo, hi = 0.0, 1.0
    while A(hi) > a:
        hi *= 2.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if A(mid) > a:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def main():
    expected = {
        0.50: 0.0,
        0.55: 0.415722828005486,
        0.60: 0.874217465798717,
        0.70: 2.02550238894606,
        0.80: 3.92069039487289,
        0.90: 8.99888807607553,
        0.95: 18.9999998935468,
    }

    for zeta, target in expected.items():
        r_w = rmin_lambert(zeta)
        r_b = rmin_bisect(zeta)
        assert abs(r_w - r_b) < 1e-10
        assert abs(r_w - target) < 1e-9
        if r_w > 0.0:
            a = (1.0 - zeta) / zeta
            assert abs(A(r_w) - a) < 1e-11

    # More aggressive grading must require at least as much relaxation distance.
    values = [rmin_lambert(z) for z in (0.51, 0.55, 0.60, 0.70, 0.80, 0.90, 0.95)]
    assert all(b > a for a, b in zip(values, values[1:]))

    print("mean-II-safe transit ceiling regression: PASS")
    print("zeta   r_min")
    for zeta in expected:
        print(f"{zeta:4.2f}   {rmin_lambert(zeta):.9f}")


if __name__ == "__main__":
    main()
