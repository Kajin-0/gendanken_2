"""Temperature-matched optical-kernel design for graded-HgCdTe sample B.

The goal is to compare carrier transport versus temperature without confusing
that change with the temperature dependence of the optical generation profile.

A fixed composition profile is taken from the current literature-constrained
sample-B envelope: x_low=0.316 and x_high chosen so the 300 K gap slope
corresponds to 150 V/cm across W=3.7 um.

For each selected 300 K reference wavelength, the code finds the wavelength at
lower temperature that minimizes the relative L2 distance between the full
cell-integrated front-collection timing kernels.

The Moazzami above-gap absorption fit was established over approximately
600-5000 cm^-1.  The primary constrained search therefore uses lambda >= 2 um.
An unconstrained diagnostic is also reported when the mathematical optimum
leaves that spectral range; it must not be treated as a validated prediction.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.optimize import brentq, minimize_scalar

HC_EV_UM = 1.2398419843320026
W_UM = 3.7
W_CM = W_UM * 1.0e-4
X_LOW = 0.316
REFERENCE_T_K = 300.0
REFERENCE_FIELD_V_CM = 150.0
TARGET_TEMPERATURES_K = (215.0, 115.0)

# Statistics-like D-optimal support bands from the current 300 K design.
REFERENCE_WAVELENGTHS_UM = (2.800, 3.410, 3.632, 3.840)

# Approximate spectral range used to establish the current above-gap fit.
VALID_LAMBDA_MIN_UM = 2.0
VALID_LAMBDA_MAX_UM = 10.0
UNCONSTRAINED_LAMBDA_MIN_UM = 0.8

N_FINE = 4001
N_CELL = 80


def eg_hansen(x: np.ndarray | float, T: float) -> np.ndarray | float:
    return (
        -0.302
        + 1.93 * x
        + 5.35e-4 * T * (1.0 - 2.0 * x)
        - 0.81 * x**2
        + 0.832 * x**3
    )


def k_moazzami(x: np.ndarray | float, T: float) -> np.ndarray | float:
    return (
        -20060.0
        + 115750.0 * x
        + 32.43 * T
        - 64170.0 * x**2
        + 0.43231 * T**2
        - 101.92 * x * T
    )


def n_moazzami(x: np.ndarray | float, T: float) -> np.ndarray | float:
    return 0.74487 - 0.44513 * x + (0.000799 - 0.000757 * x) * T


def alpha_moazzami(E: float, x: np.ndarray, T: float) -> np.ndarray:
    eg = eg_hansen(x, T)
    fraction = (E - eg) / E
    alpha = np.zeros_like(x)
    mask = fraction > 0.0
    alpha[mask] = k_moazzami(x[mask], T) * fraction[mask] ** n_moazzami(
        x[mask], T
    )
    return np.maximum(alpha, 0.0)


def reference_x_high() -> float:
    target_gap = eg_hansen(X_LOW, REFERENCE_T_K) + REFERENCE_FIELD_V_CM * W_CM
    return float(
        brentq(
            lambda xx: eg_hansen(xx, REFERENCE_T_K) - target_gap,
            X_LOW,
            0.60,
        )
    )


X_HIGH = reference_x_high()
Z_UM = np.linspace(0.0, W_UM, N_FINE)
Z_CM = Z_UM * 1.0e-4
X_PROFILE = X_HIGH + (X_LOW - X_HIGH) * Z_UM / W_UM
CELL_EDGES_UM = np.linspace(0.0, W_UM, N_CELL + 1)


def optical_kernel(wavelength_um: float, T: float) -> tuple[float, float, float, np.ndarray]:
    E = HC_EV_UM / wavelength_um
    alpha = alpha_moazzami(E, X_PROFILE, T)
    tau = np.concatenate(([0.0], cumulative_trapezoid(alpha, Z_CM)))
    p_abs = float(1.0 - np.exp(-tau[-1]))
    if p_abs <= 1.0e-14:
        return p_abs, np.nan, np.nan, np.zeros(N_CELL)

    cdf = (1.0 - np.exp(-tau)) / p_abs
    survival = 1.0 - cdf

    density_cm = alpha * np.exp(-tau) / p_abs
    density_cm /= np.trapezoid(density_cm, Z_CM)
    mean_cm = float(np.trapezoid(Z_CM * density_cm, Z_CM))
    var_cm2 = float(np.trapezoid((Z_CM - mean_cm) ** 2 * density_cm, Z_CM))

    survival_integral = np.concatenate(([0.0], cumulative_trapezoid(survival, Z_UM)))
    integral_edges = np.interp(CELL_EDGES_UM, Z_UM, survival_integral)
    timing_row_um = np.diff(integral_edges)

    return (
        p_abs,
        mean_cm * 1.0e4,
        np.sqrt(max(var_cm2, 0.0)) * 1.0e4,
        timing_row_um,
    )


def relative_kernel_error(row: np.ndarray, reference: np.ndarray) -> float:
    return float(np.linalg.norm(row - reference) / np.linalg.norm(reference))


def match_kernel(
    reference_row: np.ndarray,
    T: float,
    lower_um: float,
    upper_um: float,
) -> tuple[float, float, float, float, float]:
    def objective(wavelength_um: float) -> float:
        p_abs, _, _, row = optical_kernel(wavelength_um, T)
        if p_abs <= 1.0e-12:
            return 1.0e6
        return relative_kernel_error(row, reference_row)

    result = minimize_scalar(
        objective,
        bounds=(lower_um, upper_um),
        method="bounded",
        options={"xatol": 1.0e-10},
    )
    p_abs, mean_um, std_um, row = optical_kernel(float(result.x), T)
    return float(result.x), float(result.fun), p_abs, mean_um, std_um


def main() -> None:
    print("Sample-B temperature iso-kernel wavelength schedule")
    print(
        f"fixed composition envelope: x_high={X_HIGH:.6f}, "
        f"x_low={X_LOW:.3f}, W={W_UM:.2f} um"
    )
    print()

    stored = {}

    for reference_lambda in REFERENCE_WAVELENGTHS_UM:
        p0, mean0, std0, reference_row = optical_kernel(reference_lambda, REFERENCE_T_K)
        print(
            f"reference: T={REFERENCE_T_K:.0f} K, lambda={reference_lambda:.3f} um, "
            f"Pabs={p0:.3f}, <z>={mean0:.3f} um, sigma_z={std0:.3f} um"
        )

        for T in TARGET_TEMPERATURES_K:
            constrained = match_kernel(
                reference_row,
                T,
                VALID_LAMBDA_MIN_UM,
                VALID_LAMBDA_MAX_UM,
            )
            unconstrained = match_kernel(
                reference_row,
                T,
                UNCONSTRAINED_LAMBDA_MIN_UM,
                VALID_LAMBDA_MAX_UM,
            )
            stored[(reference_lambda, T)] = (constrained, unconstrained)

            print(
                f"  {T:.0f} K constrained: lambda={constrained[0]:.6f} um, "
                f"kernel error={100*constrained[1]:.3f}%, "
                f"Pabs={constrained[2]:.3f}, <z>={constrained[3]:.3f} um"
            )
            if abs(unconstrained[0] - constrained[0]) > 1.0e-3:
                print(
                    f"    unconstrained mathematical optimum: "
                    f"lambda={unconstrained[0]:.6f} um, "
                    f"kernel error={100*unconstrained[1]:.3f}% "
                    f"[outside validated spectral range]"
                )
        print()

    # Stable regressions for the three practically useful deeper kernels.
    expected = {
        (3.410, 215.0): (3.52095, 0.02454),
        (3.410, 115.0): (3.65954, 0.05081),
        (3.632, 215.0): (3.79272, 0.00439),
        (3.632, 115.0): (4.00268, 0.00843),
        (3.840, 215.0): (4.04232, 0.000434),
        (3.840, 115.0): (4.31011, 0.001121),
    }
    for key, (lambda_expected, error_expected) in expected.items():
        result = stored[key][0]
        assert abs(result[0] - lambda_expected) < 2.0e-4
        assert abs(result[1] - error_expected) < 2.0e-4

    shallow_115_constrained = stored[(2.800, 115.0)][0]
    shallow_115_unconstrained = stored[(2.800, 115.0)][1]
    assert shallow_115_constrained[0] < 2.001
    assert 0.16 < shallow_115_constrained[1] < 0.19
    assert 1.14 < shallow_115_unconstrained[0] < 1.16
    assert shallow_115_unconstrained[1] < 0.03

    print(
        "PASS: mid/deep optical timing kernels can be held nearly invariant "
        "by temperature-dependent wavelength retuning; the shallow 300 K "
        "anchor leaves the validated absorption-fit range by 115 K"
    )


if __name__ == "__main__":
    main()
