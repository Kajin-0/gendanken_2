"""Companion transport-witness design for translated-gradient HgCdTe metrology.

The relocation inverse no longer needs an unconstrained generic high-field
transport law if v(E), D(E), and lifetime are measured independently in p-type
HgCdTe from the same material campaign.

This file translates the current three-depth quasi-neutral design into a simple
calibration envelope. It is NOT a detailed device layout or breakdown model.

Current relocation feature centers:
    2.6, 4.4, 5.6 um.

The programmed 1-um high-gradient regions across those structures span roughly
x=0.34-0.52. A three-composition witness set
    x = 0.35, 0.43, 0.51
therefore brackets the actual high-field carrier path and supplies an interior
model-check point.

A lateral Shockley-Haynes path length of 100 um is used only to put transit
scales on the table. The field range 0.1-3 kV/cm then corresponds to 1-30 V.
Transit-time envelopes are evaluated with

    v = mu E / [1 + (E/d)^r]

using mu=4k,9k,20k cm2/Vs and d=4,8,12 kV/cm with r=2.2. These ranges are scale
stresses informed by published HgCdTe transport/APD measurements; they are not
300 K fitted material parameters.

No novelty claim.
"""

from __future__ import annotations

import numpy as np

from hgcdte_downstream_drift_diffusion_relocation import programmed_profile
from hgcdte_sample_a_constraint_family_joint_iso_kernel import (
    HC_EV_UM,
    eg_hansen,
)

FEATURE_CENTERS_UM = (2.6, 4.4, 5.6)
WITNESS_X = (0.35, 0.43, 0.51)
TRACK_UM = 100.0
FIELDS_V_CM = (100.0, 300.0, 1000.0, 2000.0, 3000.0)
MOBILITY_CM2_VS = (4000.0, 9000.0, 20000.0)
D_KV_CM = (4.0, 8.0, 12.0)
R = 2.2


def empirical_velocity(mu, field_v_cm, d_kv_cm, r=R):
    return mu * field_v_cm / (
        1.0 + (abs(field_v_cm) / (1000.0 * d_kv_cm)) ** r
    )


def transit_ns(track_um, velocity_cm_s):
    return track_um * 1.0e-4 / velocity_cm_s * 1.0e9


def feature_composition_ranges():
    rows = []
    for center in FEATURE_CENTERS_UM:
        z, x, h, _ = programmed_profile(center, 1601)
        mask = h > 1.0e-9
        rows.append(
            (
                center,
                float(np.min(x[mask])),
                float(np.max(x[mask])),
                float(np.interp(center, z, x)),
            )
        )
    return rows


def main():
    ranges = feature_composition_ranges()
    overall_min = min(row[1] for row in ranges)
    overall_max = max(row[2] for row in ranges)

    print("Companion HgCdTe transport-witness calibration design")
    print("programmed high-gradient feature composition spans")
    for center, xmin, xmax, xmid in ranges:
        print(
            f"  z0={center:.1f} um: x={xmin:.4f}-{xmax:.4f}, "
            f"center x={xmid:.4f}"
        )
    print(f"overall feature span: x={overall_min:.4f}-{overall_max:.4f}")
    print()

    print("recommended three uniform-composition witness points")
    for x in WITNESS_X:
        gap = float(eg_hansen(x, 300.0))
        print(
            f"  x={x:.2f}: Eg(300K)={gap:.6f} eV, "
            f"lambda_g={HC_EV_UM/gap:.3f} um"
        )
    print()

    print(
        f"100-um lateral path: field -> voltage = "
        f"E * {TRACK_UM*1e-4:.3f} cm"
    )
    for field in FIELDS_V_CM:
        values = []
        for mu in MOBILITY_CM2_VS:
            for d in D_KV_CM:
                velocity = empirical_velocity(mu, field, d)
                values.append(transit_ns(TRACK_UM, velocity))
        values = np.asarray(values)
        voltage = field * TRACK_UM * 1.0e-4
        print(
            f"  E={field/1000:.1f} kV/cm, V={voltage:.1f} V: "
            f"transit min/median/max="
            f"{values.min():.3f}/{np.median(values):.3f}/{values.max():.3f} ns"
        )

    # Stable scale regressions.
    assert 0.343 < overall_min < 0.345
    assert 0.516 < overall_max < 0.518

    gaps = [float(eg_hansen(x, 300.0)) for x in WITNESS_X]
    cutoffs = [HC_EV_UM / gap for gap in gaps]
    assert 3.45 < cutoffs[0] < 3.48
    assert 2.64 < cutoffs[1] < 2.67
    assert 2.13 < cutoffs[2] < 2.15

    low_field = []
    high_field = []
    for mu in MOBILITY_CM2_VS:
        for d in D_KV_CM:
            low_field.append(
                transit_ns(TRACK_UM, empirical_velocity(mu, 100.0, d))
            )
            high_field.append(
                transit_ns(TRACK_UM, empirical_velocity(mu, 3000.0, d))
            )
    assert 5.0 <= min(low_field) < 5.1
    assert 25.0 < max(low_field) < 25.1
    assert 0.17 < min(high_field) < 0.18
    assert 1.27 < max(high_field) < 1.28

    print()
    print(
        "PASS: three witness compositions x~0.35/0.43/0.51 bracket the actual "
        "high-gradient feature composition range in the current relocation "
        "design. A 100-um Shockley-Haynes path places the 0.1-3 kV/cm calibration "
        "window at only 1-30 V and gives sub-nanosecond to tens-of-nanoseconds "
        "transit times over a deliberately broad mobility/velocity-law envelope. "
        "This is compatible with established HgCdTe impulse/transit metrology and "
        "provides a direct route to measure v(E), D(E), and tau rather than infer "
        "them simultaneously from the relocation experiment."
    )


if __name__ == "__main__":
    main()
