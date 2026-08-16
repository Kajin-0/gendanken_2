# Paper 02 — Canonical Working Manuscript

**Date:** 2026-08-16  
**Status:** **ANONYMOUS REV. 5 PROMOTED / NUMERICALLY CONVERGED / COMPILED / HOSTILE REVIEW PASSED / NOT SUBMISSION-READY**

## Canonical source

```text
PAPER02_MANUSCRIPT_REV5_ANON_2026-08-16.tex
```

Source blob at promotion:

```text
d61023ee44b7a8b365cf15f6dce579dff4f8a045
```

Canonical supplement:

```text
PAPER02_SUPPLEMENT_REV5_ANON_2026-08-16.tex
```

Supplement blob at promotion:

```text
5b6499c24be70164ea25791e19d143f61197195b
```

Bibliography:

```text
PAPER02_REFERENCES_REV4.bib
```

Rev. 1–Rev. 4 remain frozen provenance. Rev. 4 compiled successfully but was intentionally not promoted after hostile review identified an overly literal interpretation of the planar Poisson-curvature parameter; Rev. 5 is the corrected successor.

## Build identity

GitHub Actions run:

```text
31949546540
```

Artifact:

```text
paper02-manuscript-rev5-package
artifact id 9264292338
```

Compiled PDF fingerprints:

```text
main manuscript: 9 pages
SHA-256 041f818b43f9cd2062690400cd03e69a56c8f7e36663af690c7556ea69a3451e

supplement: 3 pages
SHA-256 eefd607ee9171ce987b3454cf37efac9ca2f03576d032a2410e0a4da94e4ce6a
```

The final build passed numerical-input, figure-regeneration, semantic/privacy/priority/statistical, LaTeX, bibliography/reference-resolution, persistence, and rendered hostile-review gates.

## Scientific identity

Working title:

> **Apparent diffusion from deterministic velocity gradients in wavelength-resolved photodetectors**

Author default:

```text
Anonymous
```

Central claim boundary:

> In deterministic zero-microscopic-diffusion photodetector models, finite wavelength-dependent generation kernels that are treated as known by the inverse and overlap spatial velocity heterogeneity can produce a positive effective diffusion coefficient when the resulting Shockley–Ramo terminal-current response is interpreted through a homogeneous drift–diffusion model. The paper develops causal-support controls, tangent-space/local bias theory, and covariance-aware same- and multi-frequency rejection tests for this attribution failure.

The optical kernels are **theoretical wavelength-dependent generation kernels supplied exactly to the inverse**. No experimental kernel calibration is performed or claimed.

Priority posture:

```text
DISTINCT COMBINATION SUPPORTED BY FOCUSED AUDIT
NO SUPERLATIVE PRIORITY CLAIM
```

Do not introduce `first`, `first-ever`, `fundamental`, `universal`, or equivalent priority language without an explicit later priority upgrade.

## Locked physical interpretation of the planar stress

The collector-side parameter `Delta = 0.05 V` is defined through

```text
V'' = 2 Delta / W_d^2
```

with fixed endpoint potentials. It is a Poisson-curvature parameter, **not** an independently added 0.05-V terminal voltage.

For the canonical stress the exact planar solution gives approximately:

```text
Delta/W_d                         166.7 V/cm  characteristic curvature-field scale
curved-region field magnitude    328.9–662.3 V/cm
curved-region mean field          495.6 V/cm
uniform-bias field                394.7 V/cm
regional mean-field increment     100.9 V/cm
extra regional potential drop     0.030263 V
```

Do not regress to the superseded phrases “adds an electrostatic drop,” “average added field,” or equivalent wording.

## Checked inferential convergence

The inference-level convergence gate independently refined field mesh, source/kernel quadrature, and deterministic trajectory step. It reported `overall_pass=true` under predeclared tolerances.

The field mesh is the limiting tested coordinate. Baseline-to-fine changes in same-frequency inferred `D_eff` are:

```text
100 MHz  1.648%
500 MHz  1.641%
1 GHz    1.633%
```

Source-quadrature and trajectory-step effects are much smaller. The upstream point-source null remains numerical-zero scale and the inside-nonuniform-region positive control remains near `4.87e-3 m^2/s`.

This is a numerical-stability result for the declared surrogate/inverse, not experimental validation.

## Locked same-frequency statistical ordering

```text
100 MHz: one-mode rejection occurs before positive-D detection
500 MHz: positive-D detection occurs before one-mode rejection
1 GHz:  positive-D detection occurs before one-mode rejection
```

Under the explicit reference covariance, there is no same-frequency hidden-risk interval at 100 MHz, while conditional hidden-risk intervals exist at 500 MHz and 1 GHz.

## Current state record

Read next:

```text
PAPER02_CURRENT_STATE_REV5_2026-08-16.md
```

That record contains the Rev. 5 hostile-review disposition, build hashes, convergence scope, and remaining scientific blockers.

## Required reading before future manuscript edits

Follow `PAPER02_MANUSCRIPT_PRESERVATION_PROTOCOL.md`.

At minimum read:

1. root `PRIVACY_PROTOCOL.md`;
2. this file;
3. `PAPER02_CURRENT_STATE_REV5_2026-08-16.md`;
4. `PAPER02_INFERENCE_CONVERGENCE_GATE_2026-08-16.md`;
5. `PAPER02_PRIORITY_CHECKPOINT_2026-08-15.md`;
6. `PAPER02_EXACT_PRIORITY_MATRIX_2026-08-15.md`;
7. exact theorem/result files only as needed.

## Preservation rule

Rev. 5 is frozen as the canonical working manuscript.

Any material scientific correction must create a new numbered source rather than editing Rev. 5 in place. Do not advance the current pointer again until the new source has independently passed its applicable scientific, numerical, compilation, reference-resolution, anonymity, and hostile-review gates.
