"""Regression for arbitrary-spacing one-mode closure and quadratic depth distortion.

This verifies that known nonuniform source spacing preserves the one-mode test,
while blindly applying the equal-spacing identity can create a phase bias.
"""

from __future__ import annotations

import numpy as np
from scipy.optimize import brentq, root


L_UM = 7.6
H_UM = 0.5
MU = np.asarray((2.5, 3.0, 3.5, 4.0), dtype=float)
MU_C = 3.25
V = 34473.49237184506

GRADIENT_EXCESS_DEG = {
    100e6: 0.011978,
    500e6: 0.058727,
    1e9: 0.110405,
}


def one_mode_current(z_um: np.ndarray, frequency_hz: float) -> np.ndarray:
    omega = 2.0 * np.pi * frequency_hz
    gamma = 1j * omega / V
    distance_m = (L_UM - z_um) * 1.0e-6
    return (1.0 - np.exp(-gamma * distance_m)) / gamma


def equal_spacing_closure(currents: np.ndarray) -> complex:
    d = np.diff(currents)
    return complex(2.0 * np.log(d[1]) - np.log(d[0]) - np.log(d[2]))


def ratio_prediction(r_per_um: complex, spacings_um: np.ndarray) -> tuple[complex, complex]:
    d0, d1, d2 = spacings_um
    q0 = np.exp(r_per_um * d0)
    q1 = np.exp(r_per_um * d1)
    q2 = np.exp(r_per_um * d2)
    ratio10 = q0 * (q1 - 1.0) / (q0 - 1.0)
    ratio21 = q1 * (q2 - 1.0) / (q1 - 1.0)
    return complex(ratio10), complex(ratio21)


def recover_r_from_first_ratio(
    currents: np.ndarray,
    z_um: np.ndarray,
    initial_r_per_um: complex,
) -> complex:
    differences = np.diff(currents)
    measured = differences[1] / differences[0]
    spacings = np.diff(z_um)

    def residual(x: np.ndarray) -> np.ndarray:
        r_value = x[0] + 1j * x[1]
        predicted, _ = ratio_prediction(r_value, spacings)
        delta = predicted - measured
        return np.asarray((delta.real, delta.imag))

    sol = root(residual, np.asarray((initial_r_per_um.real, initial_r_per_um.imag)))
    assert sol.success
    return complex(sol.x[0] + 1j * sol.x[1])


def quadratic_positions(c_per_um: float) -> np.ndarray:
    return MU + 0.5 * c_per_um * (MU - MU_C) ** 2


def main() -> None:
    print("Arbitrary-spacing and depth-calibration regression")
    print()

    frequency = 500e6
    omega = 2.0 * np.pi * frequency
    true_r_per_um = 1j * omega / V * 1.0e-6

    z_distorted = quadratic_positions(0.02)
    currents = one_mode_current(z_distorted, frequency)
    recovered = recover_r_from_first_ratio(currents, z_distorted, true_r_per_um)
    spacings = np.diff(z_distorted)
    _, predicted_ratio = ratio_prediction(recovered, spacings)
    measured_ratio = np.diff(currents)[2] / np.diff(currents)[1]

    assert abs(recovered - true_r_per_um) < 1.0e-11
    assert abs(predicted_ratio - measured_ratio) < 1.0e-10

    print("known nonuniform spacing:")
    print(f"positions = {z_distorted}")
    print(f"recovered r = {recovered}")
    print(f"prediction error = {abs(predicted_ratio-measured_ratio):.3e}")
    print()

    print("quadratic curvature producing 10% phase contamination if equal spacing is assumed")
    for f_hz, gradient_phase in GRADIENT_EXCESS_DEG.items():
        target = 0.1 * gradient_phase
        c_root = brentq(
            lambda c: abs(
                np.degrees(
                    equal_spacing_closure(one_mode_current(quadratic_positions(c), f_hz)).imag
                )
            )
            - target,
            0.0,
            0.05,
        )
        edge_error_um = 0.5 * c_root * (0.75**2)
        phase = np.degrees(
            equal_spacing_closure(one_mode_current(quadratic_positions(c_root), f_hz)).imag
        )
        print(
            f"{f_hz/1e6:7.1f} MHz: c={c_root:.9f}/um, "
            f"edge nonlinear error={edge_error_um*1e3:.6f} nm, "
            f"phase={phase:+.9f} deg"
        )

        assert 0.0040 < c_root < 0.0048
        assert 1.0 < edge_error_um * 1e3 < 1.5

    print()
    print(
        "PASS: known arbitrary source spacing preserves the one-mode prediction, "
        "while blindly enforcing equal spacing can turn ~nm nonlinear coordinate "
        "distortion into a transport-scale phase bias for the current worked signal."
    )


if __name__ == "__main__":
    main()
