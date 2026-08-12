# Canonical Manuscript Baseline

**Status:** **CANONICAL REV. 7 MANUSCRIPT BASELINE — PRESERVE**  
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
MANUSCRIPT_REV7_ANON_2026-08-11.tex
```

Rev. 7 was first validated against the established Rev. 6 baseline in PR #11. Only after the preservation and privacy gates passed were canonical pointers updated. The revision is surgical: 63 of 924 established Rev. 6 lines were changed or removed (~6.82%); no section, subsection, reference, or unrelated derivation was deleted.

The exact source is preserved as six deterministic base64 text parts containing a gzip-compressed snapshot:

```text
manuscript_history/MANUSCRIPT_REV7_ANON_2026-08-11.tex.gz.b64.part01
manuscript_history/MANUSCRIPT_REV7_ANON_2026-08-11.tex.gz.b64.part02
manuscript_history/MANUSCRIPT_REV7_ANON_2026-08-11.tex.gz.b64.part03
manuscript_history/MANUSCRIPT_REV7_ANON_2026-08-11.tex.gz.b64.part04
manuscript_history/MANUSCRIPT_REV7_ANON_2026-08-11.tex.gz.b64.part05
manuscript_history/MANUSCRIPT_REV7_ANON_2026-08-11.tex.gz.b64.part06
```

Recover it only with:

```bash
python tools/extract_manuscript_baseline.py
```

The recovered source MUST verify as:

```text
SHA-256: 9c7fa95eb714b32839760d47f7277aaad795589c44012e2324566b6e6cb9d2f8
bytes: 75182
lines: 963
compiled pages: 24
sections: 12
subsections: 18
bibliography items: 19
\begin{equation} environments: 102
author metadata: Anonymous
PDF author metadata: Anonymous
```

The deterministic gzip snapshot MUST verify as:

```text
SHA-256: 8056b7cf995e1d2985a6c5aaf6d6016c8d2714dcfe3e1e2d391fb0169716038b
bytes: 26026
parts: 6
```

If recovery or either hash fails, **do not recreate or edit the manuscript from notes**. Work in a separate addendum until the exact source is restored.

## Rev. 7 corrections now canonical

Rev. 7 preserves the central four-color theorem, branch-qualified inversion, finite-rank hierarchy, post-detection conditioning, singular weighting-field limit, and earlier nuisance analysis. It changes only points that survived independent checking of the post-Rev. 6 hostile review:

- the one- and two-exponential identities are explicitly placed in the classical **Prony / ESPRIT / matrix-pencil** lineage; neither the geometric identity nor the Hankel/Casoratian minor is claimed as new;
- the candidate contribution is narrowed to the detector-specific chain `calibrated spectral generation depth -> Shockley--Ramo terminal current -> spatial differencing -> classical finite-exponential model-order tests -> cross-RF physical root constraints`;
- the former arbitrary `xi=1` HgCdTe headline force is replaced by the 2025 electron-affinity relation `chi(x)=5.32+0.45x-E_g(x,300 K)` and therefore `E_drive^grad=|(dE_g/dx-0.45) dx/dz|`;
- the corresponding local electron-driving fraction `xi_e=1-0.45/(dE_g/dx)` is about **0.666--0.695** across the worked composition profile;
- the finite-width gradient-sensitive phase becomes approximately **-0.0220167, -0.1064448, -0.1942321 degree** at 100 MHz, 500 MHz, and 1 GHz;
- a deliberately steep spatially varying small-signal recombination stress anchored to a 5-us low-injection scale changes those closures by only about `4e-8` to `4e-7 degree` over 0.1--1 GHz in the stated model; this is a sensitivity result, not a universal Auger claim;
- the one-dimensional polynomial `E_w(z)` remains an exact surrogate theorem but is explicitly not a generic finite-pixel electrostatic solution; finite electrodes can have both axial and lateral weighting structure;
- the hierarchy is explicitly structural model-selection logic, not a globally calibrated sequential hypothesis test; quoted significance levels remain conditional on the rung being tested;
- a concrete common-reference/interleaved-wavelength coherent measurement architecture is stated, while experimental feasibility remains **OPEN**, not demonstrated;
- all HgCdTe conditioning, SNR, coordinate, phase, weighting-field, and baseline-covariance resource numbers are propagated to the literature-anchored transport scale.

Current key resource values include a conditioning optimum near **5.85 GHz**, 3-sigma current-step requirements of **90.9 / 82.9 / 77.1 / 71.4 dB** at 100 / 250 / 500 / 1000 MHz, nonaffine coordinate RMS near **4.5 nm**, and irregular channel-phase RMS of about **1.88e-4 / 9.15e-4 / 1.71e-3 degree** at 100 / 500 / 1000 MHz.

Detailed records:

```text
REV7_ADVERSARIAL_CORRECTIONS_2026-08-11.md
MANUSCRIPT_REV7_PRESERVATION_REPORT_2026-08-11.md
numerics/rev7_review_regression.py
```

The adversarial review itself is not authority. Its objections are retained as attack vectors; each is accepted, narrowed, or rejected only after independent mathematical, physical, numerical, or literature checking.

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

Anonymous Rev. 6, Rev. 5, Rev. 4, and Rev. 3 snapshots remain preserved under `manuscript_history/` as provenance. They are not current sources and must not override Rev. 7. `MANUSCRIPT_DRAFT.tex` and `MANUSCRIPT_DRAFT.md` are older historical sources only.

A handoff summary is navigation, never manuscript source-of-truth.

## Preservation rule

New science should first be recorded in a theorem/result/addendum file. Manuscript integration must begin from the exact canonical source and make the smallest scientifically necessary changes. A shorter or reorganized manuscript requires an explicit user request for editorial compression/rewrite; it must never occur incidentally.

Scientific preservation does not authorize identity disclosure. See root `PRIVACY_PROTOCOL.md`, `MANUSCRIPT_PRESERVATION_PROTOCOL.md`, and `tools/check_manuscript_preservation.py`.
