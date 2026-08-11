# Canonical Manuscript Baseline

**Status:** **CANONICAL REV. 4 MANUSCRIPT BASELINE — PRESERVE**  
**Date canonicalized:** 2026-08-11  
**Author metadata:** Anonymous  
**Title:** `Spectral-depth closure tests for falsifying photocarrier transport from Shockley--Ramo current`

This file exists to prevent a future agent from reconstructing the paper from summaries, addenda, or an older checked-in draft.

## Privacy status

The canonical manuscript baseline is intentionally pseudonymous. Author identity is **not** scientific source-of-truth content and must not be restored or inferred from prior files, account metadata, git history, or memory.

Default manuscript and PDF author metadata is:

```text
Anonymous
```

Changing author identity requires explicit user approval for that specific artifact and must follow root `PRIVACY_PROTOCOL.md`.

## Canonical baseline

The authoritative manuscript is the exact anonymous Rev. 4 source:

```text
MANUSCRIPT_REV4_ANON_2026-08-11.tex
```

Rev. 4 was first validated against the established Rev. 3 baseline in PR #4 before these canonical pointers were updated. It surgically incorporates the August 11 hostile-review corrections without deleting established sections, subsections, references, or unrelated derivations.

The exact source is preserved inside this repository as three deterministic base64 text parts containing a gzip-compressed snapshot:

```text
manuscript_history/MANUSCRIPT_REV4_ANON_2026-08-11.tex.gz.b64.part01
manuscript_history/MANUSCRIPT_REV4_ANON_2026-08-11.tex.gz.b64.part02
manuscript_history/MANUSCRIPT_REV4_ANON_2026-08-11.tex.gz.b64.part03
```

Recover it only with:

```bash
python tools/extract_manuscript_baseline.py
```

The extractor concatenates the three parts, verifies the compressed snapshot, decompresses it, verifies the exact source and anonymous author metadata, and writes `MANUSCRIPT_CURRENT.tex`. Do not manually reconstruct the source from the parts.

The decompressed source MUST have:

```text
SHA-256: 9da8c6094a58109873382b6b3c73c519b26f519e327f5ec8058009bc4896df00
bytes: 53896
lines: 817
compiled pages: 19
sections: 12
subsections: 18
bibliography items: 11
\begin{equation} environments: 87
author metadata: Anonymous
PDF author metadata: Anonymous
```

The deterministic gzip snapshot MUST have:

```text
SHA-256: fad3aeee778de42a7c9de278abec5676d6fb3d0effebd4994c7bbdb0950a3f68
bytes: 18851
parts: 3
```

If the snapshot cannot be recovered and verified against these hashes, **do not edit or recreate the manuscript**. Work in a separate addendum until the exact source is restored.

## Rev. 4 corrections now canonical

Rev. 4 retains the central four-color theorem unchanged while adding or tightening:

- spatial-logarithm branch/anti-alias conditions for `q -> gamma -> (D,w,kappa)` inversion;
- candidate-root rather than automatic-uniqueness language for known unequal source spacing;
- the singular `s=kappa=0` weighting-field limit, where a linear field has a quadratic particular solution and requires six colors/third differences for exact polynomial annihilation;
- quantitative independent-error stresses for nonaffine source-coordinate error and irregular complex channel phase;
- the explicit HgCdTe transport prescription and semi-infinite entrance match used by the existing numerical model;
- covariance-aware complex falsification language, `rank at most two` precision, and one conceptual hierarchy figure.

The detailed audit is in:

```text
REV4_ADVERSARIAL_CORRECTIONS_2026-08-11.md
MANUSCRIPT_REV4_PRESERVATION_REPORT_2026-08-11.md
numerics/rev4_critique_regression.py
```

No reported HgCdTe closure values were changed by these corrections.

## Required section spine

The baseline contains these sections, in order:

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

The following established subsections are also part of the preservation baseline:

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

The anonymous Rev. 3 snapshot remains preserved under `manuscript_history/` as provenance. It is no longer the canonical current source and must not override Rev. 4.

`MANUSCRIPT_DRAFT.tex` and `MANUSCRIPT_DRAFT.md` are still older historical repository sources. They are not current manuscript sources.

A handoff summary is navigation only. It is never a substitute for the canonical manuscript source.

## Preservation rule

New science should first be recorded in a theorem/result/addendum file. Manuscript integration must then begin from the exact canonical source and make the smallest scientifically necessary changes.

A shorter or reorganized manuscript can be produced only when the user explicitly requests an editorial compression/rewrite. It must never occur incidentally while integrating a new calculation.

Scientific preservation does not authorize identity disclosure. See root `PRIVACY_PROTOCOL.md`, `MANUSCRIPT_PRESERVATION_PROTOCOL.md`, and `tools/check_manuscript_preservation.py`.
