"""Randomized growth-order design for translated-gradient HgCdTe validation.

A same-wafer depth series would suppress run-to-run mismatch, but a HgCdTe-
specific selective-growth implementation remains unproven. This script asks
whether ordinary sequential MBE growths can recover most of the causal power by
DELIBERATELY scrambling feature depth versus chronological run number.

The physical / optical model is inherited from
hgcdte_same_wafer_translation_series.py:
- programmed 1-um gradient feature;
- lambda = 2.00-2.40 um;
- f = 0.25,0.5,1,2,3 GHz;
- common bulk + front/back interface nuisance basis;
- statistics-like Pabs weighting;
- fixed total measurement resource.

For a given run sequence, each nuisance amplitude may drift as a polynomial in
chronological run coordinate xi. The feature depth is permuted relative to xi.
Thus smooth chamber/process drift no longer has to be monotonic in feature depth.

Two explicit cases are exhausted:
1. six chosen depths with arbitrary QUADRATIC chronological nuisance drift;
2. seven chosen depths with arbitrary CUBIC chronological nuisance drift.

No claim is made that real run-to-run variation is exactly polynomial. Replicate
runs and measured process covariates remain necessary for a real experiment.
No novelty claim.
"""

from __future__ import annotations

import itertools
import numpy as np

from hgcdte_same_wafer_translation_series import (
    CANDIDATE_DEPTHS_UM,
    response_at_depth,
    series_score,
)

IDEAL_PAIR = (4.1, 5.6)
SIX_DEPTH_SET = (2.0, 2.4, 2.8, 4.6, 5.2, 5.6)
SEVEN_DEPTH_SET = (2.0, 2.4, 2.8, 4.4, 4.8, 5.2, 5.6)


def build_cache(depths: tuple[float, ...]):
    unique = sorted(set(depths) | set(IDEAL_PAIR))
    return {round(float(z), 6): response_at_depth(float(z)) for z in unique}


def optimize_order(
    depths: tuple[float, ...],
    drift_order: int,
    cache,
):
    values = []
    best = None
    for order in itertools.permutations(depths):
        result = series_score(tuple(float(z) for z in order), cache, drift_order)
        values.append(result[0])
        if best is None or result[0] > best[1][0]:
            best = (tuple(float(z) for z in order), result)
    return best, np.asarray(values)


def main() -> None:
    cache6 = build_cache(SIX_DEPTH_SET)
    ideal = series_score(IDEAL_PAIR, cache6, drift_order=0)

    monotonic6 = series_score(SIX_DEPTH_SET, cache6, drift_order=2)
    best6, values6 = optimize_order(SIX_DEPTH_SET, 2, cache6)

    cache7 = build_cache(SEVEN_DEPTH_SET)
    monotonic7 = series_score(SEVEN_DEPTH_SET, cache7, drift_order=3)
    best7, values7 = optimize_order(SEVEN_DEPTH_SET, 3, cache7)

    print("Randomized translated-gradient growth-order design")
    print(
        f"ideal perfectly matched 4.1/5.6-um pair score = {ideal[0]:.9f}"
    )
    print()

    print("six depths, quadratic chronological nuisance drift")
    print(
        "  monotonic depth order = "
        + ", ".join(f"{z:.1f}" for z in SIX_DEPTH_SET)
    )
    print(f"  monotonic score = {monotonic6[0]:.9f}")
    print(
        "  best chronological order = "
        + ", ".join(f"{z:.1f}" for z in best6[0])
    )
    print(f"  best score = {best6[1][0]:.9f}")
    print(f"  best / ideal pair = {best6[1][0] / ideal[0]:.6f}")
    print(
        f"  permutation score min/median/max = {values6.min():.9f}/"
        f"{np.median(values6):.9f}/{values6.max():.9f}"
    )
    print(
        "  fraction of all 6! orders exceeding 90% of ideal = "
        f"{np.mean(values6 > 0.90 * ideal[0]):.6f}"
    )
    print()

    print("seven depths, cubic chronological nuisance drift")
    print(
        "  monotonic depth order = "
        + ", ".join(f"{z:.1f}" for z in SEVEN_DEPTH_SET)
    )
    print(f"  monotonic score = {monotonic7[0]:.9f}")
    print(
        "  best chronological order = "
        + ", ".join(f"{z:.1f}" for z in best7[0])
    )
    print(f"  best score = {best7[1][0]:.9f}")
    print(f"  best / ideal pair = {best7[1][0] / ideal[0]:.6f}")
    print(
        f"  permutation score min/median/max = {values7.min():.9f}/"
        f"{np.median(values7):.9f}/{values7.max():.9f}"
    )
    print(
        "  fraction of all 7! orders exceeding 80% of ideal = "
        f"{np.mean(values7 > 0.80 * ideal[0]):.6f}"
    )

    # Regression anchors from exhaustive 6! and 7! searches.
    assert 0.00162 < ideal[0] < 0.00164

    assert best6[0] == (4.6, 2.0, 2.4, 5.6, 2.8, 5.2)
    assert 0.00160 < best6[1][0] < 0.00161
    assert 0.984 < best6[1][0] / ideal[0] < 0.986
    assert 0.00123 < np.median(values6) < 0.00124
    assert 0.07 < np.mean(values6 > 0.90 * ideal[0]) < 0.08

    assert best7[0] == (4.8, 2.4, 2.0, 5.2, 2.8, 5.6, 4.4)
    assert 0.00141 < best7[1][0] < 0.00143
    assert 0.870 < best7[1][0] / ideal[0] < 0.873
    assert 0.00100 < np.median(values7) < 0.00102
    assert 0.05 < np.mean(values7 > 0.80 * ideal[0]) < 0.06

    print()
    print(
        "PASS: chronological randomization is a major experimental-design "
        "resource. For the chosen six-depth set, an optimized nonmonotonic run "
        "order retains ~98.5% of the ideal perfectly matched two-device fixed-"
        "time information score while allowing every modeled bulk/front/back "
        "nuisance amplitude to drift quadratically with run number. A seven-run "
        "sequence retains ~87% while allowing cubic drift. This does not remove "
        "truly random run-to-run errors; replicate depths and measured process "
        "covariates are still required."
    )


if __name__ == "__main__":
    main()
