# Canonical Manuscript Baseline

**Status:** **CANONICAL REV. 9 MANUSCRIPT BASELINE — PRESERVE**  
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
MANUSCRIPT_REV9_ANON_2026-08-11.tex
```

Rev. 9 was first validated against the established Rev. 8 baseline in PR #15. Only after the preservation and privacy gates passed were canonical pointers updated. The revision is surgical: 34 of 883 established nonblank Rev. 8 lines were changed or removed (~3.85%); no prior section, subsection, reference, or unrelated derivation was deleted.

The exact source is preserved as seven deterministic base64 text parts containing a gzip-compressed snapshot:

```text
manuscript_history/MANUSCRIPT_REV9_ANON_2026-08-11.tex.gz.b64.part01
manuscript_history/MANUSCRIPT_REV9_ANON_2026-08-11.tex.gz.b64.part02
manuscript_history/MANUSCRIPT_REV9_ANON_2026-08-11.tex.gz.b64.part03
manuscript_history/MANUSCRIPT_REV9_ANON_2026-08-11.tex.gz.b64.part04
manuscript_history/MANUSCRIPT_REV9_ANON_2026-08-11.tex.gz.b64.part05
manuscript_history/MANUSCRIPT_REV9_ANON_2026-08-11.tex.gz.b64.part06
manuscript_history/MANUSCRIPT_REV9_ANON_2026-08-11.tex.gz.b64.part07
```

Recover it only with:

```bash
python tools/extract_manuscript_baseline.py
```

The recovered source MUST verify as:

```text
SHA-256: df62813f764f051684ec52162095a5103296b71da1549b4c96829b0168fa1ce4
bytes: 92749
lines: 1086
compiled pages: 28
sections: 12
subsections: 19
bibliography items: 21
\begin{equation} environments: 116
author metadata: Anonymous
PDF author metadata: Anonymous
```

The deterministic gzip snapshot MUST verify as:

```text
SHA-256: 15b434edbd72a5217f6183e45a537350683755fd98ec7f39716a21e5f601cdb9
bytes: 31390
parts: 7
```

If recovery or either hash fails, **do not recreate or edit the manuscript from notes**. Work in a separate addendum until the exact source is restored.

## Rev. 9 corrections now canonical

Rev. 9 preserves the central translated-kernel four-color theorem, branch-qualified DC/RF inversion, conditioning analysis, corrected Rev. 8 Hankel rank-at-most-two null, singular weighting-field treatment, nuisance/calibration framework, and the conditional graded-HgCdTe stress.

The mandatory rank hierarchy is now:

```text
rank one rejected
-> rank-at-most-two Hankel determinant tested
-> rank-two recurrence parameters resolved
-> distinct-root versus confluent/repeated-root rank two classified
-> multiplicity-aware RF physical law tested
-> higher ordinary finite rank if rank two fails
```

For a confluent rank-two sequence,

```math
d_m=(A+Bm)q^m,
```

one has nonzero adjacent minors while the recurrence discriminant satisfies

```math
Delta_q=S^2-4P=0.
```

Thus Hankel rank two does not imply two distinct exponentials. The distinct-root adjacent-minor identity is not evaluated by naively setting `q1=q2`; repeated roots use the multiplicity-aware confluent basis. A physical second-order transport model can itself become confluent.

Additional canonical hardening:

- near exact rank one the determinant statistic is nonregular because its first derivative vanishes; null-constrained Monte Carlo / parametric-bootstrap calibration is preferred when linearization is inadequate;
- a common depth-scale error `h_cal=c h` leaves the model-order null unchanged but transforms dimensional parameters as `D_cal=c^2D`, `w_cal=cw`, `kappa_cal=kappa`;
- independently calibrated arbitrary generation kernels obey the homogeneous one-mode relation `J_m=A+B M_m(r)`, giving a kernel-aware nonlinear consistency test; the simple geometric four-color identity is the rigid-translation special case;
- raw geometric-closure failure with wavelength-evolving kernels rejects the combined homogeneous-transport + assumed-optics idealization unless the optical kernels are independently constrained;
- the composition profile `x(z)` is a shared nuisance because it controls both spectral generation depth/kernels and the modeled composition-induced transport force;
- the cited electron-affinity source's quoted `67.1%` average conduction-band partition / approximately `±1%` two-thirds comparison is tied to its stated `0.15<x<0.45` interval; the explicit affinity relation is evaluated to the worked `x=0.55` without extending that quoted validation range by assumption;
- the worked local Peclet numbers are only about `0.48` per source step and `0.75` over the optical-kernel width, so the high-Peclet relation is asymptotic intuition rather than the quantitative HgCdTe result;
- the inherited hot-to-cold stress is an independent deliberately strong two-state benchmark, not the same Rev. 9 HgCdTe realization;
- wavelength-dependent absorption/generation depth as a carrier-transport probe is acknowledged as established prior art from classical surface-photovoltage/diffusion-length and photodiode spectral-response work;
- the stated one-carrier model has free DC admissibility nulls `q(0) in (0,1]`, `D>0`, `kappa>=0`, plus the assumed drift-direction sign;
- the exact closest 2024 graded-HgCdTe technical comparison remains **OPEN / UNPROVEN**;
- the blind combined-physics detector challenge remains the next major device-physics validation.

Detailed records:

```text
REV9_ADVERSARIAL_CORRECTIONS_2026-08-11.md
MANUSCRIPT_REV9_PRESERVATION_REPORT_2026-08-11.md
PAPER_CLAIM_LEDGER_REV9_ADVERSARIAL_ADDENDUM_2026-08-11.md
numerics/rev9_review_regression.py
```

Adversarial reviews remain attack vectors rather than authority: accept, narrow, reject, or mark an objection out of scope only after independent checking.

## Priority and feasibility boundary

Priority remains **OPEN / UNPROVEN**. Spectral-depth probing of carrier transport, wavelength-dependent RF response, and finite-exponential/Hankel identification are all established lineages. The candidate distinction is the specific observable-corrected spectral-depth closure hierarchy plus cross-RF physical-law falsification.

The exact closest 2024 graded-HgCdTe paper still requires a direct technical full-text comparison before submission-level priority/novelty language. Negative searches, metadata, or related-paper audits are not novelty evidence.

The manuscript also does not claim demonstrated experimental feasibility. The derived nonaffine-depth, irregular-phase, absolute common depth-scale, optical-kernel, composition-profile, and baseline-model covariance requirements remain calibration/modeling resources that require an eventual experimental demonstration.

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
Known arbitrary generation kernels
Initial excess-energy invariance in an ideal graded gap
Optical coordinate
Transport stress
Prediction and numerical cross-check
Measurement resource
```

## Historical baselines

Anonymous Rev. 8, Rev. 7, Rev. 6, Rev. 5, Rev. 4, and Rev. 3 snapshots remain preserved under `manuscript_history/` as provenance. They are not current sources and must not override Rev. 9. `MANUSCRIPT_DRAFT.tex` and `MANUSCRIPT_DRAFT.md` are older historical sources only.

A handoff summary is navigation, never manuscript source-of-truth.

## Preservation rule

New science should first be recorded in a theorem/result/addendum file. Manuscript integration must begin from the exact canonical source and make the smallest scientifically necessary changes. A shorter or reorganized manuscript requires an explicit user request for editorial compression/rewrite; it must never occur incidentally.

Scientific preservation does not authorize identity disclosure. See root `PRIVACY_PROTOCOL.md`, `MANUSCRIPT_PRESERVATION_PROTOCOL.md`, and `tools/check_manuscript_preservation.py`.
