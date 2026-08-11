# Canonical Manuscript Baseline

**Status:** **CANONICAL PRE-GEOMETRY MANUSCRIPT BASELINE — PRESERVE**  
**Date recovered/audited:** 2026-08-11  
**Author:** Anonymous  
**Title:** `Spectral-depth closure tests for falsifying photocarrier transport from Shockley--Ramo current`

This file exists to prevent a future agent from reconstructing the paper from summaries, addenda, or an older checked-in draft.

## Canonical baseline

The authoritative manuscript immediately before the realistic-geometry hardening study is the exact source previously generated as:

```text
MANUSCRIPT_REV3_ANON_2026-08-11.tex
```

The exact source is preserved inside this repository as six deterministic base64 text parts containing a gzip-compressed snapshot:

```text
manuscript_history/MANUSCRIPT_REV3_ANON_2026-08-11.tex.gz.b64.part01
...
manuscript_history/MANUSCRIPT_REV3_ANON_2026-08-11.tex.gz.b64.part06
```

Recover it only with:

```bash
python tools/extract_manuscript_baseline.py
```

The extractor concatenates the six parts, verifies the compressed snapshot, decompresses it, verifies the exact source, and writes `MANUSCRIPT_CURRENT.tex`. Do not manually reconstruct the source from the parts.

The decompressed source MUST have:

```text
SHA-256: 3ba57ed7c7bbe264038ffa4e6eabfc1ea90c1075d4989d4075d2589352cf6d8c
bytes: 43554
lines: 696
compiled pages: 16
sections: 12
subsections: 18
bibliography items: 11
\begin{equation} environments: 75
```

The deterministic gzip snapshot MUST have:

```text
SHA-256: e413c1be218f4f3d33611381b6407137169abafb6fc22a6087f33f77b3c2ae3e
bytes: 15362
parts: 6
```

If the snapshot cannot be recovered and verified against these hashes, **do not edit or recreate the manuscript**. Work in a separate addendum until the exact source is restored.

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

## Important distinction

`MANUSCRIPT_DRAFT.tex` and `MANUSCRIPT_DRAFT.md` are historical repository sources. They are **not** allowed to override this recovered 16-page Rev. 3 baseline merely because they are older files on `main`.

A handoff summary is navigation only. It is never a substitute for the canonical manuscript source.

## Preservation rule

New science should first be recorded in a theorem/result/addendum file. Manuscript integration must then begin from the exact canonical source and make the smallest scientifically necessary changes.

A shorter or reorganized manuscript can be produced only when the user explicitly requests an editorial compression/rewrite. It must never occur incidentally while integrating a new calculation.

See `MANUSCRIPT_PRESERVATION_PROTOCOL.md` and `tools/check_manuscript_preservation.py`.