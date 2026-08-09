"""Regression for HGCDTE_SPECTRAL_DELAY_RELAXATION_ROBUSTNESS.md.

Deterministic mean-energy + Kane-velocity model. Not a calibrated HgCdTe
transport simulation.
"""

import math

try:
    from scipy.integrate import quad
except Exception as exc:  # pragma: no cover
    raise SystemExit("This regression requires scipy.integrate.quad") from exc


def vnorm(e, g):
    if e <= 0.0:
        return 0.0
    return 2.0 * math.sqrt(e * (e + g)) / (2.0 * e + g)


def theta_relax(h, R, r, xi_e=1.0):
    """Dimensionless transit Theta=G vK T / Eg,out.

    r=L/ell_E for the full graded region. r=0 is ballistic.
    """
    if h <= 1.0:
        return 0.0

    if h <= R:
        g_s = h
        e_s = 0.0
    else:
        g_s = R
        e_s = xi_e * (h - R)

    D = g_s - 1.0
    if D <= 0.0:
        return 0.0

    kappa = math.inf if r == 0.0 else (R - 1.0) / r

    def e_of_z(z):
        if math.isinf(kappa):
            return e_s + z
        return kappa + (e_s - kappa) * math.exp(-z / kappa)

    if e_s == 0.0:
        # Substitute z=t^2 to remove the integrable 1/sqrt(z) start singularity.
        def transformed(t):
            if t == 0.0:
                return math.sqrt(g_s)
            z = t * t
            return 2.0 * t / vnorm(e_of_z(z), g_s - z)

        return quad(transformed, 0.0, math.sqrt(D), epsabs=1e-11, limit=300)[0]

    return quad(
        lambda z: 1.0 / vnorm(e_of_z(z), g_s - z),
        0.0,
        D,
        epsabs=1e-11,
        limit=300,
    )[0]


def main():
    # Peak remains at h=R in the sampled relaxation range.
    for R in (1.5, 2.0, 3.0):
        for r in (0.0, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0):
            peak = theta_relax(R, R, r, xi_e=1.0)

            # Dense samples on the long-wave side must stay below the peak.
            for i in range(1, 101):
                h = 1.0 + (R - 1.0) * i / 101.0
                assert theta_relax(h, R, r, xi_e=1.0) < peak

            # Short-wave side must decrease for xi_e>0.
            prev = peak
            for delta in (0.05, 0.1, 0.25, 0.5, 1.0, 2.0, 5.0):
                val = theta_relax(R + delta, R, r, xi_e=1.0)
                assert val < prev
                prev = val

    # Relaxation increases the entrance-gap transit time in this mean-energy model.
    vals = [theta_relax(2.0, 2.0, r, xi_e=1.0) for r in (0.0, 0.5, 1.0, 2.0, 5.0, 10.0)]
    assert all(b > a for a, b in zip(vals, vals[1:]))

    print("spectral delay relaxation robustness regression: PASS")
    print()
    print("R=2 entrance-gap peak")
    print("L/ell_E   Theta_peak")
    for r in (0.0, 0.5, 1.0, 2.0, 5.0, 10.0):
        print(f"{r:7.2f}   {theta_relax(2.0, 2.0, r):.9f}")


if __name__ == "__main__":
    main()
