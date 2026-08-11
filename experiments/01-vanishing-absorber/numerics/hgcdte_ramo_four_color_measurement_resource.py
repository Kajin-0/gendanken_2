"""Measurement-resource calculation for the corrected HgCdTe four-color stress.

Uses the stochastic no-recombination calculation from
hgcdte_ramo_four_color_diffusion_recombination.py.

For the logarithmic closure

    C4 = 2 log d1 - log d0 - log d2,

linearized independent circular complex current noise has coefficients

    [1/d0,
     -(1/d0+2/d1),
      (2/d1+1/d2),
     -1/d2].

If sigma_J is the complex RMS noise of each spectral current sample, then

    sigma_C4 = sigma_J ||c||.

The 3-sigma condition for the gradient-sensitive excess is

    sigma_J <= |C_excess|/(3 ||c||).

Results are reported relative to the mean magnitude of the three spatial current
differences.  This is a conditional coherent-measurement resource, not an
instrument specification.
"""

from __future__ import annotations

import numpy as np

import hgcdte_ramo_four_color_diffusion_recombination as model


FREQUENCIES_HZ = (100e6, 250e6, 500e6, 1e9)


def closure(currents: np.ndarray) -> complex:
    d = np.diff(currents)
    return complex(2.0 * np.log(d[1]) - np.log(d[0]) - np.log(d[2]))


def noise_coefficients(currents: np.ndarray) -> np.ndarray:
    d0, d1, d2 = np.diff(currents)
    return np.asarray(
        (
            1.0 / d0,
            -(1.0 / d0 + 2.0 / d1),
            2.0 / d1 + 1.0 / d2,
            -1.0 / d2,
        ),
        dtype=complex,
    )


def main() -> None:
    _, _, kernels = model.kernels_on_bvp_grid()
    kappa = 0.0

    print("HgCdTe four-color 3-sigma measurement resource")
    print("RF, |C_excess|, sigma_J/<|Delta J|>, amplitude SNR")

    stored = {}
    for frequency in FREQUENCIES_HZ:
        variable_currents = model.channel_currents(
            model.solve_variable(frequency, kappa), kernels
        )
        homogeneous_currents = model.channel_currents(
            model.homogeneous_point_current(frequency, kappa), kernels
        )

        Cvar = closure(variable_currents)
        Chom = closure(homogeneous_currents)
        excess = Cvar - Chom

        c = noise_coefficients(variable_currents)
        sigma_max = abs(excess) / (3.0 * np.sqrt(np.sum(np.abs(c) ** 2)))
        mean_step = float(np.mean(np.abs(np.diff(variable_currents))))
        relative = sigma_max / mean_step
        snr_db = 20.0 * np.log10(1.0 / relative)

        stored[int(frequency)] = (excess, relative, snr_db, Chom)
        print(
            f"{frequency/1e6:7.1f} MHz: "
            f"|C|={abs(excess):.9e}, "
            f"sigma/step={relative:.9e}, SNR={snr_db:.3f} dB, "
            f"phase excess={np.degrees(excess.imag):+.6f} deg"
        )

    assert 1.5e-5 < stored[int(100e6)][1] < 1.7e-5
    assert 95.5 < stored[int(100e6)][2] < 96.7
    assert 7.3e-5 < stored[int(500e6)][1] < 8.1e-5
    assert 81.5 < stored[int(500e6)][2] < 83.0
    assert 1.40e-4 < stored[int(1e9)][1] < 1.55e-4
    assert 76.0 < stored[int(1e9)][2] < 77.5

    # Optical closure is a calibrated bias, not random noise.  Report phase-size
    # ratio only as a scale diagnostic.
    for frequency in (100e6, 500e6, 1e9):
        excess, _, _, Chom = stored[int(frequency)]
        ratio = abs(Chom.imag / excess.imag)
        print(
            f"optical-phase-floor / gradient-phase-excess @ {frequency/1e6:.0f} MHz "
            f"= {ratio:.4f}"
        )
        assert 0.18 < ratio < 0.25

    print()
    print(
        "PASS: the corrected quartet is testable in principle but demands high "
        "coherent current-step SNR.  Increasing RF substantially relaxes the "
        "independent-noise requirement in this explicit model, at the cost of "
        "greater exposure to high-frequency nonidealities."
    )


if __name__ == "__main__":
    main()
