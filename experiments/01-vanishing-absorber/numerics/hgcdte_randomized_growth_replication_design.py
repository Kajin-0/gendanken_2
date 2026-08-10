"""Replicate-anchor design for the randomized translated-gradient MBE series.

The six-depth randomized growth-order calculation suppresses smooth chronological
process drift, but real MBE runs also contain genuinely random variation. A real
validation series should therefore repeat selected feature depths.

This script keeps the previously optimized six-run relative order

    4.6, 2.0, 2.4, 5.6, 2.8, 5.2 um

and asks which TWO of the six depths should each be repeated once. For every
candidate anchor pair, the two replicate runs are inserted in all distinct slots
while preserving the relative order of the original six runs.

Two drift stresses are compared:
- every modeled bulk/front/back-interface nuisance amplitude may drift
  quadratically with chronological run number;
- the same amplitudes may drift cubically.

The score is inherited from hgcdte_same_wafer_translation_series.py and is
proportional to fixed-total-measurement-time nuisance-orthogonal complex-response
SNR under the current statistics-like optical weighting.

Replication does not itself model or remove random run-to-run error. Its purpose
is to create same-depth observations from which that random variance can be
measured empirically in the eventual experiment.

No novelty claim.
"""

from __future__ import annotations

import itertools

from hgcdte_same_wafer_translation_series import response_at_depth, series_score

BASE_DEPTHS = (2.0, 2.4, 2.8, 4.6, 5.2, 5.6)
BASE_ORDER = (4.6, 2.0, 2.4, 5.6, 2.8, 5.2)
IDEAL_PAIR = (4.1, 5.6)


def insertion_schedules(base, first, second):
    schedules = set()
    for first_slot in range(len(base) + 1):
        sequence = list(base)
        sequence.insert(first_slot, first)
        for second_slot in range(len(sequence) + 1):
            candidate = list(sequence)
            candidate.insert(second_slot, second)
            schedules.add(tuple(float(z) for z in candidate))
    return schedules


def build_cache():
    depths = set(BASE_DEPTHS) | set(IDEAL_PAIR)
    return {round(float(z), 6): response_at_depth(float(z)) for z in depths}


def best_for_anchor_pair(anchor_pair, drift_order, cache):
    best = None
    for schedule in insertion_schedules(BASE_ORDER, *anchor_pair):
        result = series_score(schedule, cache, drift_order)
        if best is None or result[0] > best[1][0]:
            best = (schedule, result)
    return best


def main() -> None:
    cache = build_cache()
    ideal = series_score(IDEAL_PAIR, cache, drift_order=0)

    stored = {}
    for drift_order in (2, 3):
        rows = []
        for anchor_pair in itertools.combinations(BASE_DEPTHS, 2):
            best = best_for_anchor_pair(anchor_pair, drift_order, cache)
            rows.append((best[1][0], anchor_pair, best[0], best[1]))
        rows.sort(reverse=True, key=lambda row: row[0])
        stored[drift_order] = rows

        print(
            f"eight-run replicate design; chronological nuisance polynomial "
            f"order={drift_order}"
        )
        for row in rows[:5]:
            print(
                "  anchors "
                f"{row[1][0]:.1f}/{row[1][1]:.1f} um -> "
                f"score={row[0]:.9f}, "
                f"score/ideal={row[0] / ideal[0]:.6f}"
            )
            print(
                "    order = "
                + ", ".join(f"{z:.1f}" for z in row[2])
            )
        print()

    best2 = stored[2][0]
    best3 = stored[3][0]

    assert best2[1] == (2.8, 4.6)
    assert best2[2] == (2.8, 4.6, 2.0, 2.4, 5.6, 2.8, 4.6, 5.2)
    assert 0.00219 < best2[0] < 0.00220
    assert 1.34 < best2[0] / ideal[0] < 1.36

    assert best3[1] == (2.8, 5.2)
    assert best3[2] == (5.2, 2.8, 4.6, 2.0, 2.4, 5.6, 2.8, 5.2)
    assert 0.00187 < best3[0] < 0.00189
    assert 1.14 < best3[0] / ideal[0] < 1.16

    print(
        "PASS: replicate runs are most valuable at high-leverage interior "
        "feature depths, not automatically at the shallow/deep extremes. Within "
        "the present insertion search, repeats at 2.8/4.6 um give an eight-run "
        "quadratic-drift score ~1.35x the ideal perfectly matched two-device "
        "reference, while repeats at 2.8/5.2 um give ~1.15x under cubic drift. "
        "The repeated depths also provide the empirical same-structure run-to-run "
        "variance that the polynomial-drift model alone cannot estimate."
    )


if __name__ == "__main__":
    main()
