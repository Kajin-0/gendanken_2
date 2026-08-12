# Canonical Manuscript Baseline

**Status:** **CANONICAL REV. 8 MANUSCRIPT BASELINE — PRESERVE**  
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
MANUSCRIPT_REV8_ANON_2026-08-11.tex
```

Rev. 8 was first validated against the established Rev. 7 baseline in PR #13. Only after the preservation and privacy gates passed were canonical pointers updated. The revision is surgical: 26 of 826 established nonblank Rev. 7 lines were changed or removed (~3.15%); no section, subsection, reference, or unrelated derivation was deleted.

The exact source is preserved as seven deterministic base64 text parts containing a gzip-compressed snapshot:

```text
manuscript_history/MANUSCRIPT_REV8_ANON_2026-08-11.tex.gz.b64.part01
manuscript_history/MANUSCRIPT_REV8_ANON_2026-08-11.tex.gz.b64.part02
manuscript_history/MANUSCRIPT_REV8_ANON_2026-08-11.tex.gz.b64.part03
manuscript_history/MANUSCRIPT_REV8_ANON_2026-08-11.tex.gz.b64.part04
manuscript_history/MANUSCRIPT_REV8_ANON_2026-08-11.tex.gz.b64.part05
manuscript_history/MANUSCRIPT_REV8_ANON_2026-08-11.tex.gz.b64.part06
manuscript_history/MANUSCRIPT_REV8_ANON_2026-08-11.tex.gz.b64.part07
```

Recover it only with:

```bash
python tools/extract_manuscript_baseline.py
```

The recovered source MUST verify as:

```text
SHA-256: 28eb3de954d50046f177e06e4b54eb1812414c03a1d53a933904f99fb3c49ba9
bytes: 81816
lines: 1023
compiled pages: 26
sections: 12
subsections: 18
bibliography items: 19
\begin{equation} environments: 107
author metadata: Anonymous
PDF author metadata: Anonymous
```

The deterministic gzip snapshot MUST verify as:

```text
SHA-256: 44af67c407d07b6e7d60bbc6760f14cbe0f44cf763a74e972a9b3322a5d8d2f7
bytes: 28082
parts: 7
```

If recovery or either hash fails, **do not recreate or edit the manuscript from notes**. Work in a separate addendum until the exact source is restored.

## Rev. 8 corrections now canonical

Rev. 8 preserves the central four-color theorem, branch-qualified inversion, classical finite-exponential lineage, singular weighting-field treatment, calibration framework, and the literature-anchored HgCdTe composition-band-edge stress. It repairs one genuine algebraic defect in the six-color rung and hardens the associated statistics and material-model boundaries.

The mandatory rank hierarchy is now:

```text
rank one rejected
-> rank-at-most-two Hankel-determinant null tested
-> two-mode recurrence parameters resolved
-> RF physical law tested
-> higher ordinary finite rank if rank two fails
```

The previous unconditional six-color minor closure is **SUPERSEDED** because

```math
W_1^2-W_0W_2=-d_2 det(H).
```

Thus `W1^2=W0W2` contains a spurious `d2=0` acceptance branch. The unconditional rank-at-most-two null is

```math
det [[d0,d1,d2],[d1,d2,d3],[d2,d3,d4]] = 0.
```

The adjacent-minor formula remains valid and useful for mode separation, conditioning, and recurrence recovery when nondegenerate; it is not the general model-order null. Rev. 8 also carries a covariance-aware complex determinant residual before root recovery.

Additional canonical hardening:

- the finite-kernel 1% weighting-field false phases are approximately `0.002947 / 0.012140 / 0.010007 degree` at 100 / 500 / 1000 MHz, with 10%-of-target allowable variations `0.757% / 0.881% / 1.961%`;
- the tiny graded-recombination subtraction is validated by a dedicated differential finite-difference versus adaptive-shooting comparison, conservatively agreeing within about `3e-9 degree` across tested numerical environments; the coarser `1e-5 degree` absolute solver comparison is not used to validate that subtraction;
- the 2025 electron-affinity relation anchors the **composition-induced conduction-band force term**, not the total self-consistent device drift; Poisson/electrostatic fields remain outside the worked one-dimensional stress;
- under the retained reduced `m* proportional to Eg` prescription, `|v_DOS|/v_field` ranges from about **8.8% to 18.3%**, so the DOS/effective-mass term is a substantive uncertainty rather than a negligible correction;
- scaling `v_DOS` by `alpha_DOS=0,0.5,1,1.5` moves the 100-MHz closure from about `-0.01861` to `-0.02349 degree`, exposing that uncertainty directly;
- in the nearly lossless two-carrier limit, total DC Shockley--Ramo response can become depth-degenerate, so species-specific tracking may require two or more nonzero RF frequencies;
- the exact closest 2024 graded-HgCdTe priority audit remains **OPEN / UNPROVEN**; metadata and adjacent papers do not substitute for the exact full-text comparison;
- the blind combined-physics detector challenge remains the next major device-physics validation, not a prerequisite for this localized algebraic repair.

Detailed records:

```text
REV8_ADVERSARIAL_CORRECTIONS_2026-08-11.md
MANUSCRIPT_REV8_PRESERVATION_REPORT_2026-08-11.md
numerics/rev8_review_regression.py
```

Adversarial reviews remain attack vectors rather than authority: accept, narrow, reject, or mark an objection out of scope only after independent checking.

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

Anonymous Rev. 7, Rev. 6, Rev. 5, Rev. 4, and Rev. 3 snapshots remain preserved under `manuscript_history/` as provenance. They are not current sources and must not override Rev. 8. `MANUSCRIPT_DRAFT.tex` and `MANUSCRIPT_DRAFT.md` are older historical sources only.

A handoff summary is navigation, never manuscript source-of-truth.

## Preservation rule

New science should first be recorded in a theorem/result/addendum file. Manuscript integration must begin from the exact canonical source and make the smallest scientifically necessary changes. A shorter or reorganized manuscript requires an explicit user request for editorial compression/rewrite; it must never occur incidentally.

Scientific preservation does not authorize identity disclosure. See root `PRIVACY_PROTOCOL.md`, `MANUSCRIPT_PRESERVATION_PROTOCOL.md`, and `tools/check_manuscript_preservation.py`.
