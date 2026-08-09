"""Regression for HGCDTE_NONLOCAL_IONIZATION_SURROGATE.md.

Mean-energy relaxation model plus the alpha=1, beta=0 energy-dependent
impact-ionization rate. This is not a calibrated HgCdTe APD simulator.
"""

import math


def threshold_reached(theta, ell):
    """Mean trajectory reaches threshold before device exit."""
    return theta * (1.0 - math.exp(-ell)) > 1.0


def normalized_threshold_time(theta):
    """t_dead/tau_E for theta=q F ell_E / E_th > 1."""
    if theta <= 1.0:
        return math.inf
    return math.log(theta / (theta - 1.0))


def hazard_shape(theta, ell):
    """Dimensionless hazard H for alpha=1, beta=0.

    Xi = (A tau_E) * H.
    """
    s_d = normalized_threshold_time(theta)
    if not math.isfinite(s_d) or ell <= s_d:
        return 0.0
    return (
        (theta - 1.0) * (ell - s_d)
        + theta * (math.exp(-ell) - math.exp(-s_d))
    )


def probability(theta, ell, a):
    """Poisson-event probability with a=A tau_E."""
    h = hazard_shape(theta, ell)
    return 1.0 - math.exp(-a * h)


def dimensional_hazard(field, velocity, tau_e, e_th, length, A, q=1.0):
    """Closed-form dimensional hazard for E0=0, alpha=1, beta=0.

    Arguments may use any internally consistent unit system.
    """
    e_ss = q * field * velocity * tau_e
    T = length / velocity
    if e_ss <= e_th:
        return 0.0
    t_d = tau_e * math.log(e_ss / (e_ss - e_th))
    if T <= t_d:
        return 0.0
    return A / e_th * (
        (e_ss - e_th) * (T - t_d)
        + e_ss * tau_e * (math.exp(-T / tau_e) - math.exp(-t_d / tau_e))
    )


def numeric_midpoint_hazard(field, velocity, tau_e, e_th, length, A, q=1.0, n=200000):
    """Independent midpoint integration of the same rate trajectory."""
    T = length / velocity
    dt = T / n
    total = 0.0
    e_ss = q * field * velocity * tau_e
    for k in range(n):
        t = (k + 0.5) * dt
        energy = e_ss * (1.0 - math.exp(-t / tau_e))
        if energy >= e_th:
            total += A * (energy / e_th - 1.0) * dt
    return total


def main():
    # Dimensionless threshold limits.
    assert not threshold_reached(0.9, 10.0)
    assert threshold_reached(2.0, 1.0)

    # One dimensional example; q=1 defines arbitrary consistent units.
    args = dict(
        field=1.0,
        velocity=1.0,
        tau_e=2.0,
        e_th=0.8,
        length=3.0,
        A=5.0,
        q=1.0,
    )
    closed = dimensional_hazard(**args)
    numeric = numeric_midpoint_hazard(**args)
    assert abs(closed - numeric) < 1e-9

    theta = args["field"] * args["velocity"] * args["tau_e"] / args["e_th"]
    ell = args["length"] / (args["velocity"] * args["tau_e"])
    a = args["A"] * args["tau_e"]
    assert abs(closed - a * hazard_shape(theta, ell)) < 1e-12

    print(f"theta={theta:.6f}")
    print(f"ell={ell:.6f}")
    print(f"a={a:.6f}")
    print(f"H={hazard_shape(theta, ell):.12f}")
    print(f"Xi={closed:.12f}")
    print(f"P_II={probability(theta, ell, a):.12f}")


if __name__ == "__main__":
    main()
