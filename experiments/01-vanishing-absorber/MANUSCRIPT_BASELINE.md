# Canonical Manuscript Baseline

**Status:** **CANONICAL REV. 6 MANUSCRIPT BASELINE — PRESERVE**  
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
MANUSCRIPT_REV6_ANON_2026-08-11.tex
```

Rev. 6 was first validated against the established Rev. 5 baseline in PR #8. Only after the preservation and privacy gates passed were canonical pointers updated. The revision is surgical: 21 of 863 established Rev. 5 lines were changed or removed (~2.43%); no section, subsection, reference, or unrelated derivation was deleted.

The exact source is preserved as six deterministic base64 text parts containing a gzip-compressed snapshot:

```text
manuscript_history/MANUSCRIPT_REV6_ANON_2026-08-11.tex.gz.b64.part01
manuscript_history/MANUSCRIPT_REV6_ANON_2026-08-11.tex.gz.b64.part02
manuscript_history/MANUSCRIPT_REV6_ANON_2026-08-11.tex.gz.b64.part03
manuscript_history/MANUSCRIPT_REV6_ANON_2026-08-11.tex.gz.b64.part04
manuscript_history/MANUSCRIPT_REV6_ANON_2026-08-11.tex.gz.b64.part05
manuscript_history/MANUSCRIPT_REV6_ANON_2026-08-11.tex.gz.b64.part06
```

Recover it only with:

```bash
python tools/extract_manuscript_baseline.py
```

The recovered source MUST verify as:

```text
SHA-256: 2f8f6c22b64d89f7237a3053663fc500f97574c75a0c60489bb7f19925f112b4
bytes: 67837
lines: 924
compiled pages: 22
sections: 12
subsections: 18
bibliography items: 13
\begin{equation} environments: 99
author metadata: Anonymous
PDF author metadata: Anonymous
```

The deterministic gzip snapshot MUST verify as:

```text
SHA-256: aa7ab9e3271599bf9cdaa5ef37618cb2b9757ee0e08c867303a83e06e61adb8e
bytes: 23386
parts: 6
```

If recovery or either hash fails, **do not recreate or edit the manuscript from notes**. Work in a separate addendum until the exact source is restored.

## Rev. 6 corrections now canonical

Rev. 6 preserves the central four-color theorem and the established branch/finite-rank hierarchy while adding the post-Rev. 5 adversarial hardening:

- a separate **post-detection conditioning rung**: rank-two detection is necessary but not sufficient for useful root-law inference;
- for `P=q_1q_2=W_1/W_0`, full first-order covariance including the shared-minor covariance, with the deliberately optimistic independent equal-significance limit `sigma_P/|P| ~ sqrt(2)/Z`; thus a `3 sigma` minor detection can still imply about 47.1% relative product uncertainty and about `14.1 sigma` is needed for 10% product precision in that simplified limit;
- the recurrence sum `S=q_1+q_2`, its first-order differential, and explicit ill-conditioning as `S^2-4P -> 0`;
- explicit distinction between algebraic branch immunity and statistical robustness for the finite-boundary product test;
- explicit interpretation of prescribed one-dimensional `E_w(z)` as an **effective observation-operator surrogate**, not a generic finite-electrode electrostatic solution;
- a graded-HgCdTe force-partition sensitivity coordinate `xi`, with the existing finite-width benchmark and resource table explicitly normalized to the conditional `xi=1` stress;
- a 100-MHz point-source finite-diffusion `xi` sweep showing that the benchmark magnitude is not a robust material constant;
- two additional adjacent OED primary references (2021 Ge PN and 2024 Ge PIN) and a sharper prior-art boundary;
- two-carrier labeling only after both modes are statistically resolved and continuously tracked;
- covariance `chi^2` language explicitly treated as per-rung/conditional, with sequential model-order/root-law error control left to a full experimental implementation;
- one self-consistent **combined-physics blind synthetic detector challenge** named as the decisive next device-physics validation rather than added as another large theory section.

Detailed records:

```text
REV6_ADVERSARIAL_CORRECTIONS_2026-08-11.md
MANUSCRIPT_REV6_PRESERVATION_REPORT_2026-08-11.md
numerics/rev6_review_regression.py
```

The previously reported finite-width HgCdTe closure values remain the `xi=1` baseline; Rev. 6 does not relabel them as generic material predictions.

## Priority and feasibility boundary

Priority remains **OPEN / UNPROVEN**. The exact closest 2024 graded-HgCdTe paper still requires a full-text audit before submission-level priority/novelty language. Negative searches or related-paper audits are not novelty evidence.

The manuscript also does not claim demonstrated experimental feasibility. The derived few-nanometer nonaffine-coordinate, approximately `10^-4 degree` irregular-phase, and baseline-model covariance requirements remain design/resource scales that require an eventual calibration architecture.

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

Anonymous Rev. 5, Rev. 4, and Rev. 3 snapshots remain preserved under `manuscript_history/` as provenance. They are not current sources and must not override Rev. 6. `MANUSCRIPT_DRAFT.tex` and `MANUSCRIPT_DRAFT.md` are older historical sources only.

A handoff summary is navigation, never manuscript source-of-truth.

## Preservation rule

New science should first be recorded in a theorem/result/addendum file. Manuscript integration must begin from the exact canonical source and make the smallest scientifically necessary changes. A shorter or reorganized manuscript requires an explicit user request for editorial compression/rewrite; it must never occur incidentally.

Scientific preservation does not authorize identity disclosure. See root `PRIVACY_PROTOCOL.md`, `MANUSCRIPT_PRESERVATION_PROTOCOL.md`, and `tools/check_manuscript_preservation.py`.
