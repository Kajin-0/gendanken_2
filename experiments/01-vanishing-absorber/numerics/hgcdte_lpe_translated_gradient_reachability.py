"""Reachability stress for the purpose-built translated-gradient design under LPE.

Primary empirical boundary
--------------------------
Huo et al., J. Infrared Millim. Waves 43 (2024) 307-315,
DOI 10.11972/j.issn.1001-9014.2024.03.003, established a slider-LPE growth
model and validated control of the *linear* longitudinal HgCdTe composition
gradient through mercury-loss rate and cooling rate.

At cooling rate 0.2 C/min they report/model average composition gradients
[cm^-1] for mercury-loss rates [%/min]

    fg = -0.01, 0, 0.01, 0.02, 0.03, 0.04
    g  = -12.4,-9,-4.9, 0.2, 6.9,16.7.

At fg=0.035 %/min, positive-gradient values for cooling rates
0.15, 0.20, 0.30, 0.40 C/min are 18.8, 11.3, 5.5, 2.8 cm^-1.
The experimentally grown positive-gradient sample used fg=0.035 %/min,
0.2 C/min, 50 min and was ~9 um thick.

The same paper separately states that ordinary LPE material contains a steep
3-5 um substrate interdiffusion region plus a much more slowly varying linear
growth-controlled region. The compact translated feature proposed in this
repository must be an *internal* feature, not a substrate-pinned interdiffusion
zone.

This script does NOT extrapolate the Huo model as a fabrication prediction.
It only compares scales and computes one deliberately naive high-end secant
extrapolation to show how far outside the validated control range the current
1-um programmed feature lies.

Repository target
-----------------
The current programmed matched-control profile has representative coordinates
x ~0.5166 at one edge and x ~0.3917 one micron later, giving Delta x ~0.1249
across the full feature. Its background slope is ~0.01593 /um and its local
high-gradient plateau is ~0.13698 /um. Those correspond to ~159 and ~1370 cm^-1.

No claim is made that the real transport perturbation scales linearly with this
composition gradient or field.
"""

from __future__ import annotations

import numpy as np

# Huo et al. 2024: Fig. 2 / text, alpha = 0.2 C/min.
FG_PCT_PER_MIN = np.asarray((-0.01, 0.0, 0.01, 0.02, 0.03, 0.04))
GRADIENT_CM_INV = np.asarray((-12.4, -9.0, -4.9, 0.2, 6.9, 16.7))

# Huo et al. 2024: positive-gradient cooling-rate sweep, fg=0.035 %/min.
COOLING_C_PER_MIN = np.asarray((0.15, 0.20, 0.30, 0.40))
POSITIVE_GRADIENT_CM_INV = np.asarray((18.8, 11.3, 5.5, 2.8))

DEMONSTRATED_FG_PCT_PER_MIN = 0.035
DEMONSTRATED_COOLING_C_PER_MIN = 0.20
DEMONSTRATED_GROWTH_MIN = 50.0
DEMONSTRATED_THICKNESS_UM = 9.0

# Current repository programmed-profile scale.
TARGET_BACKGROUND_PER_UM = 0.01593
TARGET_HIGH_PER_UM = 0.13698
TARGET_FEATURE_DELTA_X = 0.5166 - 0.3917
TARGET_FEATURE_WIDTH_UM = 1.0


def per_um_to_cm_inv(value_per_um: float) -> float:
    return value_per_um * 1.0e4


def hansen_deg_dx(x: float, T: float = 300.0) -> float:
    """dEg/dx [eV per composition fraction] for the canonical Hansen relation."""
    return 1.93 - 2.0 * 0.81 * x + 3.0 * 0.832 * x**2 - 2.0 * 5.35e-4 * T


def field_from_gradient(gradient_cm_inv: float, x: float = 0.45) -> float:
    """Composition-gradient band-edge scale [V/cm]."""
    return abs(hansen_deg_dx(x) * gradient_cm_inv)


def main() -> None:
    target_background = per_um_to_cm_inv(TARGET_BACKGROUND_PER_UM)
    target_high = per_um_to_cm_inv(TARGET_HIGH_PER_UM)
    target_average_feature = (
        TARGET_FEATURE_DELTA_X / (TARGET_FEATURE_WIDTH_UM * 1.0e-4)
    )

    max_validated_positive = float(
        max(np.max(GRADIENT_CM_INV), np.max(POSITIVE_GRADIENT_CM_INV))
    )

    print("LPE reachability stress for the compact translated-gradient feature")
    print(f"max Huo-2024 positive linear gradient = {max_validated_positive:.3f} cm^-1")
    print(f"target background gradient = {target_background:.3f} cm^-1")
    print(f"target full-feature average gradient = {target_average_feature:.3f} cm^-1")
    print(f"target local high-gradient plateau = {target_high:.3f} cm^-1")
    print()

    print("ratios to strongest Huo-2024 positive linear-gradient point")
    print(f"  background / validated = {target_background / max_validated_positive:.3f}x")
    print(f"  feature-average / validated = {target_average_feature / max_validated_positive:.3f}x")
    print(f"  local-high / validated = {target_high / max_validated_positive:.3f}x")
    print()

    # How thick a layer would be required to accumulate the same Delta x if the
    # strongest validated broad linear gradient were sustained?
    required_thickness_cm = TARGET_FEATURE_DELTA_X / max_validated_positive
    required_thickness_um = required_thickness_cm * 1.0e4
    print(
        "thickness needed to accumulate target Delta x at strongest validated "
        f"linear gradient = {required_thickness_um:.3f} um"
    )
    print()

    x_ref = 0.45
    print(f"Hansen field scales at x={x_ref:.2f}, T=300 K")
    print(
        f"  validated 18.8 cm^-1 -> {field_from_gradient(max_validated_positive, x_ref):.2f} V/cm"
    )
    print(
        f"  target background -> {field_from_gradient(target_background, x_ref):.2f} V/cm"
    )
    print(
        f"  target local high -> {field_from_gradient(target_high, x_ref):.2f} V/cm"
    )
    print()

    # Diagnostic only: extend the *last measured secant* of the fg sweep.
    # This is intentionally NOT a physical prediction outside 0.03-0.04 %/min.
    high_end_secant = (
        GRADIENT_CM_INV[-1] - GRADIENT_CM_INV[-2]
    ) / (FG_PCT_PER_MIN[-1] - FG_PCT_PER_MIN[-2])
    fg_naive = FG_PCT_PER_MIN[-1] + (
        target_high - GRADIENT_CM_INV[-1]
    ) / high_end_secant

    average_growth_rate_um_min = (
        DEMONSTRATED_THICKNESS_UM / DEMONSTRATED_GROWTH_MIN
    )
    feature_time_min = TARGET_FEATURE_WIDTH_UM / average_growth_rate_um_min
    equivalent_feature_hg_loss_percent = fg_naive * feature_time_min

    print("deliberately naive high-end-sec ant extrapolation (diagnostic only)")
    print(f"  last measured dg/dfg = {high_end_secant:.1f} cm^-1 per (%/min)")
    print(f"  fg needed for target local slope = {fg_naive:.3f} %/min")
    print(
        f"  ratio to largest Huo fg point (0.04 %/min) = {fg_naive / 0.04:.1f}x"
    )
    print(
        f"  at 9 um / 50 min average growth, 1 um takes {feature_time_min:.3f} min"
    )
    print(
        "  equivalent Hg-loss fraction over that interval = "
        f"{equivalent_feature_hg_loss_percent:.2f}% of the paper's mother-liquor-mass reference"
    )
    print()

    # Stable scale checks.
    assert 8.4 < target_background / max_validated_positive < 8.6
    assert 66.3 < target_average_feature / max_validated_positive < 66.6
    assert 72.8 < target_high / max_validated_positive < 73.0
    assert 66.3 < required_thickness_um < 66.6
    assert 25.9 < field_from_gradient(max_validated_positive, x_ref) < 26.2
    assert 220.0 < field_from_gradient(target_background, x_ref) < 221.5
    assert 1890.0 < field_from_gradient(target_high, x_ref) < 1910.0
    assert 1.41 < fg_naive < 1.43
    assert 35.0 < fg_naive / 0.04 < 36.0
    assert 7.8 < equivalent_feature_hg_loss_percent < 8.0

    print(
        "PASS: the current compact translated-gradient target lies far outside "
        "the empirically validated single-run LPE linear-gradient regime. The "
        "same ~0.125 composition change would require ~66 um at the strongest "
        "reported broad positive gradient, versus 1 um in the current design. "
        "The natural LPE route to steep gradients is the substrate-pinned 3-5 um "
        "interdiffusion region, which conflicts with the interface-safe relocation "
        "logic. Single-run slider LPE is therefore not the preferred fabrication "
        "route for this compact matched-relocation experiment without new evidence "
        "of much stronger time-programmed melt control."
    )


if __name__ == "__main__":
    main()
