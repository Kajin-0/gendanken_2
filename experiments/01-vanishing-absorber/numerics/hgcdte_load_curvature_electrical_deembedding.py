"""Electrical-pole de-embedding requirement for optical-load phase curvature.

Strong illumination is known to change HgCdTe zero-bias impedance. A load-
dependent electrical RF pole can therefore mimic transport phase curvature.

Use a first-order electrical transfer

    H_e = 1 / (1 + i Omega tau_e),
    phi_e = -atan(Omega tau_e),

with x = Omega tau_e.  For a small residual fractional time-constant error
eta = delta tau_e / tau_e,

    delta phi_e ~= - x/(1+x^2) * eta.

The load-curvature/wavelength-difference observable has coefficients
[1,-2,1,-1,2,-1], whose squared sum is 12.  If the six residual fractional
errors are independent with equal RMS sigma_eta and have similar x, the RMS
residual electrical phase is

    sigma_C,e ~= sqrt(12) * x/(1+x^2) * sigma_eta  [rad].

This is a conservative local linear diagnostic, not a full readout model.
"""

from __future__ import annotations

import numpy as np

COEFFICIENTS = np.asarray([1.0, -2.0, 1.0, -1.0, 2.0, -1.0])
SUM_SQUARES = float(np.sum(COEFFICIENTS**2))
X_VALUES = (0.01, 0.03, 0.10, 0.30, 1.0, 3.0, 10.0)
PHASE_BUDGETS_DEG = (0.10, 0.04, 0.01, 0.005)


def phase_logtau_sensitivity(x: float) -> float:
    """Absolute |d phi / d ln tau| in rad per unit fractional tau error."""
    return x / (1.0 + x**2)


def fractional_tau_requirement(x: float, phase_budget_deg: float) -> float:
    """Equal independent per-state RMS fractional tau residual."""
    sensitivity = phase_logtau_sensitivity(x)
    return (
        np.deg2rad(phase_budget_deg)
        / (np.sqrt(SUM_SQUARES) * sensitivity)
    )


def single_state_phase_from_fractional_tau(x: float, fractional_change: float) -> float:
    """First-order single-state phase shift in degrees."""
    return float(
        np.degrees(phase_logtau_sensitivity(x) * fractional_change)
    )


def exact_single_state_phase_change(x: float, fractional_change: float) -> float:
    """Exact phase change for tau -> tau*(1+fractional_change), degrees."""
    return float(
        np.degrees(
            np.arctan(x * (1.0 + fractional_change)) - np.arctan(x)
        )
    )


def main() -> None:
    print("Electrical de-embedding requirement for load-curvature phase")
    print(f"curvature/wavelength coefficients = {COEFFICIENTS.astype(int).tolist()}")
    print(f"sum a_i^2 = {SUM_SQUARES:.0f}")
    print()

    print("equal independent per-state fractional tau_e RMS requirement")
    for budget in PHASE_BUDGETS_DEG:
        print(f"phase-curvature budget = {budget:.3f} deg")
        for x in X_VALUES:
            requirement = fractional_tau_requirement(x, budget)
            print(
                f"  x=Omega*tau={x:>5.2f}: "
                f"sigma_tau/tau <= {100*requirement:.5f}%"
            )
        print()

    print("single-state phase produced by an uncorrected 1% tau_e change")
    for x in X_VALUES:
        linear = single_state_phase_from_fractional_tau(x, 0.01)
        exact = exact_single_state_phase_change(x, 0.01)
        print(
            f"  x={x:>5.2f}: linear={linear:.6f} deg, "
            f"exact={exact:.6f} deg"
        )

    # Frequency interpretation: x = f/f_pole for a first-order pole.
    print()
    print("at measurement f=1 GHz, representative pole frequencies")
    for x in (0.01, 0.03, 0.10, 0.30, 1.0):
        print(f"  x={x:.2f} -> f_pole={1.0/x:.2f} GHz")

    # Stable regression anchors.
    assert SUM_SQUARES == 12.0

    assert 0.00203 < fractional_tau_requirement(0.1, 0.04) < 0.00204
    assert 0.000402 < fractional_tau_requirement(1.0, 0.04) < 0.000404
    assert 0.000508 < fractional_tau_requirement(0.1, 0.01) < 0.000510
    assert 0.000100 < fractional_tau_requirement(1.0, 0.01) < 0.000102

    assert 0.000732 < fractional_tau_requirement(0.3, 0.04) < 0.000733
    assert 0.00672 < fractional_tau_requirement(0.03, 0.04) < 0.00673
    assert 0.0201 < fractional_tau_requirement(0.01, 0.04) < 0.0202

    # Small-error linearization is accurate for a 1% perturbation.
    for x in X_VALUES:
        linear = single_state_phase_from_fractional_tau(x, 0.01)
        exact = exact_single_state_phase_change(x, 0.01)
        assert abs(linear - exact) < 0.003

    print()
    print(
        "PASS: illumination-dependent electrical phase can readily live on the "
        "same 0.01-0.1 degree scale as the proposed transport-curvature signal. "
        "For independent de-embedding residuals, a 0.04-degree six-state "
        "curvature budget requires per-state effective RF time-constant errors "
        "below ~0.20% at Omega*tau=0.1 and ~0.040% near the electrical pole. "
        "Operating well below the pole relaxes this requirement, while direct "
        "complex-transfer de-embedding can remove a larger absolute load-induced "
        "impedance change if its residual uncertainty meets the same phase budget."
    )


if __name__ == "__main__":
    main()
