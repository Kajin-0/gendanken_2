"""White-noise resource for a short-wave optical-load curvature observable.

The static short-wave A-localized inverse is strongly degenerate with smooth A/B
baselines. A causal alternative is to hold temperature and wavelength fixed,
measure paired A-B phase at three equally spaced optical-load states, and take a
second finite difference in load. This cancels static and linear-in-load phase.
A subsequent difference between two wavelengths also cancels a wavelength-
independent nonlinear differential-chain curvature.

For the six raw phase measurements the linear-combination coefficients are

    [1, -2, 1] at lambda_1
  - [1, -2, 1] at lambda_2.

With white phase variance sigma0^2/t_i and fixed total time, the minimum-variance
allocation is t_i proportional to |a_i|, giving a 1:2:1 load-state ratio at each
wavelength and equal total time between wavelengths.

The illustrative transport-curvature spatial amplitude is set equal to the same
25% sample-A support-shaped perturbation used in the earlier short-wave
visibility calculation. This is only a measurement-resource scale; it is NOT a
prediction of real load curvature.
"""

from __future__ import annotations

import numpy as np

from hgcdte_sample_a_shortwave_calibration_prior import (
    LAMBDA_GRID,
    NOMINAL_SIGMA_PHASE_DEG,
)
from hgcdte_sample_a_shortwave_two_band_design import (
    TOTAL_TIME_UNITS,
    build_family,
)

TARGET_SIGMA = 3.0


def anomaly_phase_family():
    """Return physical anomaly phase over wavelength for each A profile."""
    designs, physical_rms = build_family()
    # Column zero is the anomaly shape normalized to RMS one over the short-wave
    # grid, so multiply by the physical RMS amplitude to restore phase degrees.
    phase = designs[:, :, 0] * physical_rms[:, None]
    return phase


def robust_best_pair(phase: np.ndarray):
    """Pair maximizing the minimum absolute anomaly phase difference."""
    best = None
    for j in range(len(LAMBDA_GRID) - 1):
        for k in range(j + 1, len(LAMBDA_GRID)):
            signal = np.abs(phase[:, j] - phase[:, k])
            record = (
                float(np.min(signal)),
                float(np.median(signal)),
                float(np.max(signal)),
                j,
                k,
            )
            if best is None or record[0] > best[0]:
                best = record
    return best


def optimum_linear_combination_variance(
    coefficients: np.ndarray,
    sigma0_deg: float,
    total_time_units: float,
) -> tuple[np.ndarray, float]:
    """Optimal white-noise time split for a fixed linear combination.

    Minimize sum a_i^2 sigma0^2/t_i subject to sum t_i=T.
    The solution is t_i = T |a_i| / sum |a| and

        Var_min = sigma0^2 (sum |a_i|)^2 / T.
    """
    magnitude = np.abs(coefficients)
    times = total_time_units * magnitude / np.sum(magnitude)
    variance = sigma0_deg**2 * np.sum(magnitude) ** 2 / total_time_units
    return times, float(variance)


def main() -> None:
    phase = anomaly_phase_family()
    best = robust_best_pair(phase)
    signal_min, signal_med, signal_max, j, k = best

    # Ordinary two-wavelength phase difference.
    pair_coeff = np.asarray([1.0, -1.0])
    pair_times, pair_var = optimum_linear_combination_variance(
        pair_coeff,
        NOMINAL_SIGMA_PHASE_DEG,
        TOTAL_TIME_UNITS,
    )
    pair_sigma = np.sqrt(pair_var)

    # Load curvature at lambda_1 minus load curvature at lambda_2.
    curvature_coeff = np.asarray([1.0, -2.0, 1.0, -1.0, 2.0, -1.0])
    curvature_times, curvature_var = optimum_linear_combination_variance(
        curvature_coeff,
        NOMINAL_SIGMA_PHASE_DEG,
        TOTAL_TIME_UNITS,
    )
    curvature_sigma = np.sqrt(curvature_var)

    pair_snr = signal_min / pair_sigma
    curvature_snr = signal_min / curvature_sigma

    required_total_time = (
        TARGET_SIGMA
        * NOMINAL_SIGMA_PHASE_DEG
        * np.sum(np.abs(curvature_coeff))
        / signal_min
    ) ** 2
    time_multiplier = required_total_time / TOTAL_TIME_UNITS

    equivalent_sigma0 = (
        NOMINAL_SIGMA_PHASE_DEG
        * curvature_snr
        / TARGET_SIGMA
    )

    print("Short-wave optical-load curvature resource")
    print(
        f"robust no-smooth-nuisance spectral pair = "
        f"{LAMBDA_GRID[j]:.2f}/{LAMBDA_GRID[k]:.2f} um"
    )
    print(
        f"illustrative curvature-equivalent phase-difference signal "
        f"min/median/max = {signal_min:.6f}/{signal_med:.6f}/"
        f"{signal_max:.6f} deg"
    )
    print()

    print("ordinary two-wavelength difference")
    print(f"  optimal time fractions = {pair_times/TOTAL_TIME_UNITS}")
    print(f"  sigma = {pair_sigma:.6f} deg")
    print(f"  worst SNR = {pair_snr:.6f}")
    print()

    print("load second-difference, then wavelength difference")
    print(
        f"  coefficients = {curvature_coeff.astype(int).tolist()}"
    )
    print(
        f"  optimal time fractions = "
        f"{np.round(curvature_times/TOTAL_TIME_UNITS,6).tolist()}"
    )
    print(f"  sigma = {curvature_sigma:.6f} deg")
    print(f"  worst SNR at T={TOTAL_TIME_UNITS:.0f} = {curvature_snr:.6f}")
    print(
        f"  total-time units for worst-profile 3 sigma = "
        f"{required_total_time:.3f}"
    )
    print(f"  time multiplier vs 81-unit reference = {time_multiplier:.3f}")
    print(
        f"  equivalent one-unit phase sigma for 3 sigma at T=81 = "
        f"{equivalent_sigma0:.6f} deg"
    )

    # Stable regression anchors.
    assert LAMBDA_GRID[j] == 2.00
    assert LAMBDA_GRID[k] == 2.80
    assert 0.1080 < signal_min < 0.1082

    assert np.allclose(pair_times / TOTAL_TIME_UNITS, [0.5, 0.5])
    assert np.allclose(
        curvature_times / TOTAL_TIME_UNITS,
        [0.125, 0.25, 0.125, 0.125, 0.25, 0.125],
    )

    assert abs(curvature_sigma / pair_sigma - 4.0) < 1.0e-12
    assert 1.21 < curvature_snr < 1.22
    assert 6.08 < time_multiplier < 6.10
    assert 0.040 < equivalent_sigma0 < 0.041

    print()
    print(
        "PASS: a second finite difference in optical load removes static and "
        "linear load terms at the price of a 4x white-noise phase standard "
        "deviation relative to a two-wavelength difference for fixed total "
        "time. If the nonlinear load-curvature transport amplitude were equal "
        "to the repository's illustrative 25% A-localized perturbation, ~6.1x "
        "more white-noise integration than the 81-unit reference would give a "
        "worst-profile 3-sigma curvature signal without requiring the static "
        "A smooth baseline to be known."
    )


if __name__ == "__main__":
    main()
