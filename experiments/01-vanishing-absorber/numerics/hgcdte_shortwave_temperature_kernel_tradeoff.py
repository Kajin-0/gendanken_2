"""Temperature-kernel tradeoff between sample-A localization and iso-kernel control.

The short-wave branch uses ~2.0-2.8 um to move generation through sample A's
near-junction nonlinear region. The mid/deep branch showed that a 3.632 um
reference can be retuned with temperature while preserving A/B optical timing
kernels closely.

This script asks whether the same temperature-control idea can be used for the
short-wave A-localized measurement.

For each 300 K reference wavelength, and for every member of the 72-profile A
sensitivity family, find the common lower-temperature wavelength that minimizes

    epsilon_A^2 + epsilon_B^2

with epsilon the normalized full front-collection kernel mismatch. The search
is constrained to lambda >= 2.0 um, the current lower boundary of the optical
model used in this repository.

No transport-temperature model or novelty claim.
"""

from __future__ import annotations

import numpy as np
from scipy.optimize import brentq, minimize_scalar

from hgcdte_sample_a_constraint_family_joint_iso_kernel import (
    HC_EV_UM,
    eg_hansen,
    optical_kernel,
    relative_error,
    sample_a_profiles,
    sample_b_profile,
)

REFERENCE_WAVELENGTHS_UM = (
    2.00,
    2.10,
    2.20,
    2.40,
    2.69,
    2.80,
    3.20,
    3.30,
    3.40,
    3.42,
    3.50,
    3.55,
    3.60,
    3.632,
)
TARGET_T_K = (215.0, 115.0)
SEARCH_BOUNDS_UM = (2.0, 4.8)


def joint_match(
    a_z: np.ndarray,
    a_x: np.ndarray,
    b_z: np.ndarray,
    b_x: np.ndarray,
    reference_lambda_um: float,
    T: float,
):
    p_a0, a0 = optical_kernel(a_z, a_x, reference_lambda_um, 300.0)
    p_b0, b0 = optical_kernel(b_z, b_x, reference_lambda_um, 300.0)
    if p_a0 <= 1.0e-14 or p_b0 <= 1.0e-14:
        raise RuntimeError("Reference wavelength has zero modeled absorption")

    def objective(wavelength_um: float) -> float:
        p_a, a = optical_kernel(a_z, a_x, wavelength_um, T)
        p_b, b = optical_kernel(b_z, b_x, wavelength_um, T)
        if p_a <= 1.0e-14 or p_b <= 1.0e-14:
            return 1.0e6
        return relative_error(a, a0) ** 2 + relative_error(b, b0) ** 2

    result = minimize_scalar(
        objective,
        bounds=SEARCH_BOUNDS_UM,
        method="bounded",
        options={"xatol": 1.0e-9},
    )
    wavelength = float(result.x)
    _, a = optical_kernel(a_z, a_x, wavelength, T)
    _, b = optical_kernel(b_z, b_x, wavelength, T)
    return wavelength, relative_error(a, a0), relative_error(b, b0)


def band_edge_composition(wavelength_um: float, T: float = 300.0) -> float:
    E = HC_EV_UM / wavelength_um
    return float(brentq(lambda xx: eg_hansen(xx, T) - E, 0.2, 0.8))


def main() -> None:
    profiles = sample_a_profiles()
    b_z, b_x = sample_b_profile()

    stored = {}
    print("Short-wave / temperature full-kernel tradeoff")
    print(f"A profile family = {len(profiles)}")
    print(f"lower wavelength bound = {SEARCH_BOUNDS_UM[0]:.2f} um")
    print()

    for reference in REFERENCE_WAVELENGTHS_UM:
        print(
            f"300 K reference {reference:.3f} um: "
            f"x_edge={band_edge_composition(reference):.6f}"
        )
        for T in TARGET_T_K:
            values = np.asarray(
                [
                    joint_match(z, x, b_z, b_x, reference, T)
                    for z, x, _ in profiles
                ]
            )
            stored[(reference, T)] = values
            print(
                f"  {T:.0f} K lambda*="
                f"{values[:,0].min():.6f}-{values[:,0].max():.6f} um; "
                f"A mismatch={100*values[:,1].min():.2f}-"
                f"{100*values[:,1].max():.2f}%; "
                f"B mismatch={100*values[:,2].min():.2f}-"
                f"{100*values[:,2].max():.2f}%"
            )
        print()

    # Key short-wave failures.
    r269_215 = stored[(2.69, 215.0)]
    r269_115 = stored[(2.69, 115.0)]
    assert np.max(r269_215[:, 1]) > 0.09
    assert np.max(r269_215[:, 2]) > 0.18
    assert np.max(r269_115[:, 1]) > 0.24
    assert np.max(r269_115[:, 2]) > 0.43

    # 2.0 um is boundary-limited and cannot be made remotely iso-kernel at 115 K.
    r200_115 = stored[(2.00, 115.0)]
    assert np.all(r200_115[:, 0] < 2.000001)
    assert np.max(r200_115[:, 1]) > 0.57
    assert np.max(r200_115[:, 2]) > 0.71

    # Empirical crossover at 115 K within the current reference grid.
    r342 = stored[(3.42, 115.0)]
    assert np.max(r342[:, 1]) < 0.025
    assert np.max(r342[:, 2]) < 0.050

    r340 = stored[(3.40, 115.0)]
    assert np.max(r340[:, 2]) > 0.050

    r355 = stored[(3.55, 115.0)]
    assert np.max(r355[:, 1]) < 0.010
    assert np.max(r355[:, 2]) < 0.020

    print(
        "PASS: temperature iso-kernel control and near-junction short-wave "
        "localization pull in opposite spectral directions. Within the current "
        "model, references near 2.0-2.8 um cannot be retuned at 115 K without "
        "large A/B kernel changes; worst A/B mismatch falls below 5% only near "
        "a 300 K reference of ~3.42 um and below 2% near ~3.55 um. Temperature "
        "therefore remains a mid/deep causal control, not the preferred "
        "perturbation for the short-wave nonlinear-region localization test."
    )


if __name__ == "__main__":
    main()
