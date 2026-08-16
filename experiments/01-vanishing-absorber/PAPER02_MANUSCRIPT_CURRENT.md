# Paper 02 — Canonical Working Manuscript

**Date:** 2026-08-16  
**Status:** **ANONYMOUS REV. 3 FROZEN REVIEWABLE MANUSCRIPT / FIGURE-BEARING BUILD VALIDATED / NOT SUBMISSION-READY**

## Canonical source

```text
PAPER02_MANUSCRIPT_REV3_ANON_2026-08-15.tex
```

Source blob at this pointer update:

```text
cf9d82b70e858027c038656ffa71f7fed9a2889d
```

Bibliography used by Rev. 3:

```text
PAPER02_REFERENCES_REV2.bib
```

Rev. 1 and Rev. 2 remain frozen provenance. Do not replace, delete, or silently rewrite them.

## Scientific identity

Working title:

> **Apparent diffusion from deterministic velocity gradients in wavelength-resolved photodetectors**

Author default:

```text
Anonymous
```

Central claim boundary:

> In deterministic zero-microscopic-diffusion photodetector models, finite wavelength-dependent generation kernels that are known by the inverse and overlap spatial velocity heterogeneity can produce a positive effective diffusion coefficient when the resulting Shockley-Ramo terminal-current response is interpreted through a homogeneous drift-diffusion model. The paper develops causal support controls, tangent-space bias theory, and covariance-aware same- and multi-frequency rejection tests for this attribution failure.

The optical kernels in the current numerical stress are **theoretical wavelength-dependent generation kernels supplied exactly to the inverse**. Do not shorten this to an empirical claim that they have been experimentally calibrated.

Priority posture:

```text
DISTINCT COMBINATION SUPPORTED BY FOCUSED AUDIT
NO SUPERLATIVE PRIORITY CLAIM
```

Do not introduce `first`, `first-ever`, `fundamental`, `universal`, or equivalent language without an explicit later priority upgrade.

## What Rev. 3 has established

The figure-bearing Rev. 3 build chain regenerated its canonical numerical bundle, compiled without unresolved references, and persisted the source/artifact. Rev. 3 is therefore the frozen source for the next scientific revision.

The same-frequency statistical ordering has also been corrected and must not regress:

```text
100 MHz: one-mode rejection occurs before positive-D detection
500 MHz: positive-D detection occurs before one-mode rejection
1 GHz:  positive-D detection occurs before one-mode rejection
```

Under the branch's explicit reference covariance this means there is no same-frequency hidden-risk window at 100 MHz, but finite hidden-risk windows exist at 500 MHz and 1 GHz.

## New hard gate before Rev. 4

The older geometry calculation's coarse/fine convergence check acted on the four-color closure phase. That is insufficient for the current paper because the headline quantity is the nonlinear inferred `D_eff`.

The stricter gate is now:

```text
PAPER02_INFERENCE_CONVERGENCE_GATE_2026-08-16.md
numerics/paper02_inference_convergence_gate.py
.github/workflows/paper02-inference-convergence.yml
```

It independently refines:

1. the 2-D electrostatic / weighting-potential mesh;
2. the source/kernel quadrature;
3. the trajectory integration step.

It tests the actual inferential chain, including `D_eff` and `w_eff` at 100/500/1000 MHz, the low-band fit, the 1-GHz frequency-law mismatch, upstream and inside-depletion point-source causal controls, collection, and the DC Shockley-Ramo identity.

**Rev. 4 must not be frozen until this executable gate reports `overall_pass=true`.**

## Known Rev. 4 corrections after convergence

If the numerical gate passes, create a new source rather than editing Rev. 3 in place. At minimum the new revision must:

1. replace overbroad uses of "calibrated kernels" with wording that distinguishes exact theoretical-kernel knowledge in the surrogate from experimental calibration;
2. turn the machine-extracted kernel method record into actual submission supplement material rather than saying it "should" become a supplement;
3. incorporate the completed inferential convergence result and declared tolerances;
4. preserve the corrected same-frequency statistical ordering;
5. apply the bibliography metadata corrections found in the publisher-level audit;
6. undergo a new hostile review after compilation.

## Required reading before manuscript edits

Follow `PAPER02_MANUSCRIPT_PRESERVATION_PROTOCOL.md`.

At minimum read:

1. root `PRIVACY_PROTOCOL.md`;
2. this file;
3. `PAPER02_CURRENT_STATE_REV3_2026-08-15.md` plus the newer convergence-gate record;
4. `PAPER02_INFERENCE_CONVERGENCE_GATE_2026-08-16.md`;
5. `PAPER02_PRIORITY_CHECKPOINT_2026-08-15.md`;
6. `PAPER02_EXACT_PRIORITY_MATRIX_2026-08-15.md`;
7. `PAPER02_MANUSCRIPT_BLUEPRINT_2026-08-15.md`;
8. `PAPER02_NOTATION_LOCK_2026-08-15.md`;
9. `PAPER02_FIGURE_BUNDLE_INDEX_2026-08-15.md`;
10. exact theorem/result files only as needed.

## Preservation rule

Rev. 3 is frozen.

Material corrections must create

```text
PAPER02_MANUSCRIPT_REV4_ANON_<date>.tex
```

The pointer must not advance to Rev. 4 until that source has independently passed numerical-input, compilation, unresolved-reference, and hostile scientific-review gates.
