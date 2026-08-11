"""Regression for nonuniform weighting-field contamination of the four-color closure.

Uses the existing HgCdTe four-color optical kernels and homogeneous path-harmonic
transport.  The weighting field is a deliberately simple linear stress across
the quartet.  This is not a device electrostatic simulation.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.optimize import brentq

from hgcdte_ramo_four_color_gradient_prediction import (
    L_UM,
    TARGET_MEAN_DEPTHS_UM,
    V_HARMONIC,
    Z_M,
    Z_UM,
    optical_kernel,
    wavelength_for_mean,
)


QUARTET_SPAN_UM = float(TARGET_MEAN_DEPTHS_UM[-1] - TARGET_MEAN_DEPTHS_UM[0])
QUARTET_CENTER_UM = 0.5 * float(
    TARGET_MEAN_DEPTHS_UM[0] + TARGET_MEAN_DEPTHS_UM[-1]
)

# Main-manuscript stochastic gradient-sensitive phase magnitudes.
GRADIENT_EXCESS_DEG = {
    100e6: 0.011978,
    500e6: 0.058727,
    1e9: 0.110405,
}


def remaining_integral(y: np.ndarray) -> np.ndarray:
    cumulative = np.concatenate(([0.0], cumulative_trapezoid(y, Z_M)))
    return cumulative[-1] - cumulative


def point_current_linear_weighting(
    frequency_hz: float,
    fractional_change_across_quartet: float,
) -> np.ndarray:
    """Homogeneous deterministic current with a linear weighting-field stress."""

    omega = 2.0 * np.pi * frequency_hz
    beta_per_um = fractional_change_across_quartet / QUARTET_SPAN_UM
    weighting = 1.0 + beta_per_um * (Z_UM - QUARTET_CENTER_UM)

    phase = np.exp(-1j * omega * Z_M / V_HARMONIC)
    inner = remaining_integral(weighting * phase)
    return np.exp(1j * omega * Z_M / V_HARMONIC) * inner


def channel_currents(point_current: np.ndarray, kernels: list[np.ndarray]) -> np.ndarray:
    return np.asarray(
        [np.trapezoid(kernel * point_current, Z_UM) for kernel in kernels]
    )


def closure(currents: np.ndarray) -> complex:
    differences = np.diff(currents)
    return complex(
        2.0 * np.log(differences[1])
        - np.log(differences[0])
        - np.log(differences[2])
    )


def weighting_excess_phase_deg(
    frequency_hz: float,
    fractional_change_across_quartet: float,
    kernels: list[np.ndarray],
) -> float:
    stressed = closure(
        channel_currents(
            point_current_linear_weighting(
                frequency_hz, fractional_change_across_quartet
            ),
            kernels,
        )
    )
    uniform = closure(
        channel_currents(point_current_linear_weighting(frequency_hz, 0.0), kernels)
    )
    return float(np.degrees((stressed - uniform).imag))


def main() -> None:
    wavelengths = np.asarray(
        [wavelength_for_mean(depth) for depth in TARGET_MEAN_DEPTHS_UM]
    )
    kernels = [optical_kernel(wavelength)[3] for wavelength in wavelengths]

    print("Nonuniform weighting-field four-color regression")
    print(f"quartet span = {QUARTET_SPAN_UM:.3f} um")
    print(f"homogeneous velocity = {V_HARMONIC:.6f} m/s")
    print()

    anchors = {
        (100e6, 0.005): (0.0008, 0.0011),
        (100e6, 0.010): (0.0017, 0.0021),
        (500e6, 0.005): (0.0040, 0.0047),
        (500e6, 0.010): (0.0083, 0.0094),
        (1e9, 0.005): (0.0060, 0.0072),
        (1e9, 0.010): (0.0125, 0.0145),
    }

    for frequency in (100e6, 500e6, 1e9):
        for span_change in (0.005, 0.010):
            phase = weighting_excess_phase_deg(frequency, span_change, kernels)
            lo, hi = anchors[(frequency, span_change)]
            assert lo < phase < hi
            print(
                f"{frequency/1e6:7.1f} MHz, "
                f"weighting change={100*span_change:4.1f}% -> "
                f"phase contamination={phase:+.9f} deg"
            )

    print()
    print("10% contamination thresholds relative to manuscript gradient signal")
    thresholds = {}
    for frequency, gradient_phase in GRADIENT_EXCESS_DEG.items():
        target = 0.1 * gradient_phase
        root = brentq(
            lambda span: abs(weighting_excess_phase_deg(frequency, span, kernels))
            - target,
            0.0,
            0.03,
        )
        thresholds[frequency] = root
        print(
            f"{frequency/1e6:7.1f} MHz -> "
            f"{100*root:.6f}% weighting-field change across quartet"
        )

    assert 0.0060 < thresholds[100e6] < 0.0068
    assert 0.0063 < thresholds[500e6] < 0.0072
    assert 0.0077 < thresholds[1e9] < 0.0088

    print()
    print(
        "PASS: a linear weighting-field gradient gives a finite O(omega) phase "
        "closure and sub-percent uniformity is required for <10% contamination "
        "of the current worked HgCdTe gradient signal if the field is not modeled."
    )


if __name__ == "__main__":
    main()
