"""Regression for HGCDTE_SPECTRAL_TRANSIT_STATISTICS.md.

Checks the ballistic transit integral with nonzero photoexcitation excess and
its optical-depth averages. This is not a calibrated HgCdTe transport model.
"""

import math

try:
    from scipy.integrate import quad
except Exception as exc:  # pragma: no cover
    raise SystemExit("This regression requires scipy.integrate.quad") from exc


def phi(z, e):
    if z <= 0.0:
        return 0.0
    return math.sqrt(e * z) + z ** 1.5 / (3.0 * math.sqrt(e))


def theta(q, s, xi_e):
    """Dimensionless ballistic transit G vK T / Eg,out."""
    e = 1.0 + s * (1.0 - (1.0 - xi_e) * q)
    z_s = xi_e * s * q
    z_0 = s * (1.0 - (1.0 - xi_e) * q)
    return phi(z_0, e) - phi(z_s, e)


def theta_early(s):
    return math.sqrt(s) / math.sqrt(1.0 + s) * (1.0 + 4.0 * s / 3.0)


def moments(s, tau, beta=0.5, xi_e=0.5):
    n = beta + 1.0
    den = 1.0 - math.exp(-tau)

    def q_of_y(y):
        return (y / tau) ** (1.0 / n)

    mean = quad(
        lambda y: math.exp(-y) * theta(q_of_y(y), s, xi_e),
        0.0,
        tau,
        epsabs=1e-12,
    )[0] / den

    second = quad(
        lambda y: math.exp(-y) * theta(q_of_y(y), s, xi_e) ** 2,
        0.0,
        tau,
        epsabs=1e-12,
    )[0] / den

    sigma = math.sqrt(max(0.0, second - mean * mean))
    return mean, sigma


def main():
    # Earliest generation is independent of photon-excess partition.
    for s in (0.05, 0.1, 0.5, 1.0, 2.0):
        target = theta_early(s)
        for xi in (0.0, 0.5, 1.0):
            assert abs(theta(0.0, s, xi) - target) < 1e-13

    # Generation at the output has zero geometric transit time.
    for s in (0.1, 0.5, 1.0):
        for xi in (0.0, 0.5, 1.0):
            assert abs(theta(1.0, s, xi)) < 1e-13

    # More electron photon-excess share shortens downstream transit.
    for s in (0.1, 0.5, 1.0):
        for q in (0.2, 0.5, 0.8):
            vals = [theta(q, s, xi) for xi in (0.0, 0.5, 1.0)]
            assert vals[2] <= vals[1] <= vals[0]

    # Increasing optical depth drives the mean toward the earliest-generation limit.
    for xi in (0.0, 0.5, 1.0):
        for s in (0.1, 0.5, 1.0):
            vals = [moments(s, tau, xi_e=xi)[0] for tau in (0.1, 1.0, 2.302585093, 5.0, 20.0)]
            assert all(b > a for a, b in zip(vals, vals[1:]))
            assert vals[-1] < theta_early(s)

    # Jitter need not be monotonic with optical depth.
    sigmas = [moments(0.5, tau, xi_e=0.5)[1] for tau in (0.1, 1.0, 5.0)]
    assert sigmas[1] > sigmas[0]
    assert sigmas[2] < sigmas[1]

    print("corrected spectral transit regression: PASS")
    print()
    print("lambda/lambda_c  theta_infty")
    for ratio in (0.95, 0.90, 0.80, 0.70, 0.60, 0.50):
        s = 1.0 / ratio - 1.0
        print(f"{ratio:6.2f}          {theta_early(s):.9f}")

    print()
    print("beta=0.5, xi_e=0.5, s=0.5")
    print("tau       mean_theta   sigma_theta")
    for tau in (0.1, 1.0, 2.302585093, 5.0):
        mean, sigma = moments(0.5, tau, beta=0.5, xi_e=0.5)
        print(f"{tau:8.4f}  {mean:10.6f}  {sigma:11.6f}")


if __name__ == "__main__":
    main()
