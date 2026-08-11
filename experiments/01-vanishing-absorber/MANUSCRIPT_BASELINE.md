# Canonical Manuscript Baseline

**Status:** **CANONICAL REV. 5 MANUSCRIPT BASELINE — PRESERVE**  
**Date canonicalized:** 2026-08-11  
**Author metadata:** Anonymous  
**Title:** `Spectral-depth closure tests for falsifying photocarrier transport from Shockley--Ramo current`

This file prevents reconstruction of the paper from summaries, addenda, older drafts, or historical snapshots.

## Privacy status

The canonical manuscript is intentionally anonymous. Author identity is not scientific source-of-truth content and must not be restored or inferred from prior files, account metadata, git history, public sources, or memory. Default manuscript and PDF author metadata is:

```text
Anonymous
```

Any different author identity requires explicit artifact-specific approval and root `PRIVACY_PROTOCOL.md`.

## Canonical baseline

The authoritative source is:

```text
MANUSCRIPT_REV5_ANON_2026-08-11.tex
```

Rev. 5 was first validated against the established Rev. 4 baseline in PR #6. Only after the preservation and privacy gates passed were these canonical pointers updated. The revision is surgical: only 19 of 817 established Rev. 4 lines were changed or removed (~2.33%); no section, subsection, reference, or unrelated derivation was deleted.

The exact source is preserved as six deterministic base64 text parts containing a gzip-compressed snapshot:

```text
manuscript_history/MANUSCRIPT_REV5_ANON_2026-08-11.tex.gz.b64.part01
manuscript_history/MANUSCRIPT_REV5_ANON_2026-08-11.tex.gz.b64.part02
manuscript_history/MANUSCRIPT_REV5_ANON_2026-08-11.tex.gz.b64.part03
manuscript_history/MANUSCRIPT_REV5_ANON_2026-08-11.tex.gz.b64.part04
manuscript_history/MANUSCRIPT_REV5_ANON_2026-08-11.tex.gz.b64.part05
manuscript_history/MANUSCRIPT_REV5_ANON_2026-08-11.tex.gz.b64.part06
```

Recover it only with:

```bash
python tools/extract_manuscript_baseline.py
```

The recovered source MUST verify as:

```text
SHA-256: 9d9c4686a152dcdbbfebae1db00a22f5cfd743b5948f825e79ba2acd75b812fb
bytes: 59803
lines: 863
compiled pages: 21
sections: 12
subsections: 18
bibliography items: 11
\begin{equation} environments: 92
author metadata: Anonymous
PDF author metadata: Anonymous
```

The deterministic gzip snapshot MUST verify as:

```text
SHA-256: ef1a05707690753bd3affd24909e1bedf6ad0681e409f09f92e479d6c0d22a65
bytes: 20758
parts: 6
```

If recovery or either hash fails, **do not recreate or edit the manuscript from notes**. Work in a separate addendum until the exact source is restored.

## Rev. 5 corrections now canonical

Rev. 5 preserves the central four-color and finite-rank constructions and adds the remaining post-Rev. 4 adversarial hardening:

- low-RF coalescence of the weighting-field multiplier `q_weight=1` with `q_transport -> 1`, including best-case rank-two resolution requirements of approximately 116.2, 88.4, and 76.7 dB at 100, 500, and 1000 MHz;
- the complementary five-color annihilation penalty of approximately 46.3, 32.3, and 26.4 dB at those frequencies;
- a branch-free homogeneous finite-boundary prerequisite `q_+ q_- in R_{>0}` that is RF-independent, followed by explicit two-root branch and permutation discipline;
- accurate description of the inherited HgCdTe velocity expression as an empirical field-rolloff sensitivity law rather than an asymptotic saturation law;
- explicit covariance for the modeled same-optics homogeneous subtraction, whose nominal phase is roughly 20.5--22.4% of the quoted gradient-sensitive excess;
- the confluent `s=kappa=0`, `q->1` limit of the one-carrier current;
- one-log complex closure-ratio notation and `u(z)=1/v(z)` for local slowness;
- explicit language that the few-nanometer coordinate and `~10^-4 degree` phase numbers are derived design requirements, not demonstrated calibration performance.

Detailed records:

```text
REV5_ADVERSARIAL_CORRECTIONS_2026-08-11.md
MANUSCRIPT_REV5_PRESERVATION_REPORT_2026-08-11.md
numerics/rev5_review_regression.py
```

No reported HgCdTe closure value was changed by Rev. 5.

## Priority boundary

The closest-looking 2024 graded-HgCdTe paper is bibliographically verified, but its full text has not yet been lawfully recovered and audited. That audit remains **OPEN** and blocks any priority/novelty claim at submission. Negative searches or related-paper audits are not novelty evidence.

## Required section spine

1. `Introduction`
2. `Observable correction: first-passage flux versus terminal current`
3. `Gedanken experiment I: four colors isolate one spatial mode`
4. `Gedanken experiment II: DC plus one RF identifies; the next RF falsifies`
5. `Gedanken experiment III: six colors when one mode fails`
6. `Observation-operator stress: nonuniform weighting field`
7. `Controlled spatial inhomogeneity`
8. `Optical and calibration corrections`
9. `Independent-noise cost and spacing`
10. `Conditional graded-HgCdTe prediction`
11. `Discussion`
12. `Conclusion`

Required subsections:

```text
First-passage propagation
Shockley--Ramo survival relation
Exact nuisance invariances
No-recombination limit
Complete inversion with recombination
Conditioning of the DC+RF inversion
Noise significance before root fitting
Finite scalar boundary
Two conventional carrier species
Hot-to-cold thermalization as a conventional second mode
Source-shape evolution
Relative amplitude calibration
Known arbitrary source spacing and coordinate uncertainty
Initial excess-energy invariance in an ideal graded gap
Optical coordinate
Transport stress
Prediction and numerical cross-check
Measurement resource
```

## Historical baselines

The anonymous Rev. 4 and Rev. 3 snapshots remain preserved under `manuscript_history/` as provenance. They are not current sources and must not override Rev. 5. `MANUSCRIPT_DRAFT.tex` and `MANUSCRIPT_DRAFT.md` are older historical sources only.

A handoff summary is navigation, never manuscript source-of-truth.

## Preservation rule

New science should first be recorded in a theorem/result/addendum file. Manuscript integration must begin from the exact canonical source and make the smallest scientifically necessary changes. A shorter or reorganized manuscript requires an explicit user request for editorial compression/rewrite; it must never occur incidentally.

Scientific preservation does not authorize identity disclosure. See root `PRIVACY_PROTOCOL.md`, `MANUSCRIPT_PRESERVATION_PROTOCOL.md`, and `tools/check_manuscript_preservation.py`.
