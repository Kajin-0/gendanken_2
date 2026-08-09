"""Independent time-domain checks for Experiment 01 one-port resonator.

The analytic target is NOT used inside the ODE integration.  The script
integrates the resonant cavity envelope under small incident-power modulation,
extracts the absorbed-power modulation amplitude by Fourier projection, and
compares it with the separately derived first-order transfer function.

Only the Python standard library is required.
"""

from math import cos, sin, sqrt, pi


def rk4_step(a, t, dt, gamma_e, gamma_a, omega_mod, modulation):
    """Advance the real resonant envelope by one RK4 step."""
    gamma_tot = gamma_e + gamma_a
    coupling = sqrt(2.0 * gamma_e)

    def rhs(tt, aa):
        # Input *power* is sinusoidally modulated.  The coupled-mode drive is
        # a field amplitude, hence the square root.
        p_in = 1.0 + modulation * cos(omega_mod * tt)
        s_in = sqrt(p_in)
        return -gamma_tot * aa + coupling * s_in

    k1 = rhs(t, a)
    k2 = rhs(t + 0.5 * dt, a + 0.5 * dt * k1)
    k3 = rhs(t + 0.5 * dt, a + 0.5 * dt * k2)
    k4 = rhs(t + dt, a + dt * k3)

    return a + dt * (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0


def numerical_fractional_response(
    gamma_e,
    gamma_a,
    omega_over_gamma,
    modulation=1.0e-4,
    steps_per_period=600,
    measure_periods=30,
):
    """Return |delta P_abs/P_abs| / |delta P_in/P_in| from time integration."""
    gamma_tot = gamma_e + gamma_a
    omega_mod = omega_over_gamma * gamma_tot
    period = 2.0 * pi / omega_mod
    dt = period / steps_per_period

    # Start at the unmodulated resonant steady state for unit incident power.
    a = sqrt(2.0 * gamma_e) / gamma_tot
    t = 0.0

    # Remove the turn-on transient after the modulation is applied.
    settle_steps = max(
        int((20.0 / gamma_tot) / dt),
        5 * steps_per_period,
    )
    for _ in range(settle_steps):
        a = rk4_step(
            a,
            t,
            dt,
            gamma_e,
            gamma_a,
            omega_mod,
            modulation,
        )
        t += dt

    samples = []
    sample_count = steps_per_period * measure_periods

    for _ in range(sample_count):
        a = rk4_step(
            a,
            t,
            dt,
            gamma_e,
            gamma_a,
            omega_mod,
            modulation,
        )
        t += dt
        p_abs = 2.0 * gamma_a * a * a
        samples.append((t, p_abs))

    mean_abs = sum(value for _, value in samples) / sample_count

    cosine_component = (
        2.0
        * sum(
            (value - mean_abs) * cos(omega_mod * tt)
            for tt, value in samples
        )
        / sample_count
    )
    sine_component = (
        2.0
        * sum(
            (value - mean_abs) * sin(omega_mod * tt)
            for tt, value in samples
        )
        / sample_count
    )

    fractional_absorbed_modulation = (
        sqrt(cosine_component**2 + sine_component**2) / mean_abs
    )

    # The imposed incident-power fractional modulation amplitude is exactly m.
    return fractional_absorbed_modulation / modulation


def analytic_fractional_response(omega_over_gamma):
    """Separately derived small-signal prediction for comparison only."""
    return 1.0 / sqrt(1.0 + omega_over_gamma**2)


def coupling_metric_shape(x):
    """Dimensionless x-dependent part of C^2: x^2/(1+x)^3."""
    return x * x / (1.0 + x) ** 3


def main():
    gamma_e = 1.0
    gamma_a = 1.0

    print("Time-domain absorbed-power modulation check")
    print("omega/Gamma   numerical          analytic           abs error")

    tolerance = 2.0e-6

    for ratio in (0.5, 1.0, 2.0):
        numerical = numerical_fractional_response(
            gamma_e,
            gamma_a,
            ratio,
        )
        analytic = analytic_fractional_response(ratio)
        error = abs(numerical - analytic)
        print(
            f"{ratio:10.3f}   {numerical: .12f}   "
            f"{analytic: .12f}   {error:.3e}"
        )
        if error > tolerance:
            raise AssertionError(
                f"modulation response failed at omega/Gamma={ratio}: {error}"
            )

    # Numerical scan of the already-derived coupling objective.  This is a
    # regression on the optimization algebra, not an independent physical model.
    best_x = None
    best_value = -1.0

    for index in range(1, 200001):
        x = 0.00005 * index  # scans 5e-5 through 10
        value = coupling_metric_shape(x)
        if value > best_value:
            best_value = value
            best_x = x

    expected_x = 2.0
    if abs(best_x - expected_x) > 1.0e-4:
        raise AssertionError(
            f"coupling optimum moved: numerical x={best_x}, expected 2"
        )

    a0 = 4.0 * best_x / (1.0 + best_x) ** 2

    print()
    print("Coupling-objective scan")
    print(f"best gamma_e/gamma_a = {best_x:.6f}")
    print(f"on-resonance absorptance = {a0:.12f}")
    print("expected exact values: x = 2, A0 = 8/9")
    print()
    print("PASS")


if __name__ == "__main__":
    main()
