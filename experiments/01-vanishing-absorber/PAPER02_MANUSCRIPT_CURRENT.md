# Paper 02 — Canonical Manuscript

**Date:** 2026-08-16  
**Status:** **ANONYMOUS REV. 7 PROMOTED / SCIENTIFICALLY SUBMISSION-READY / TARGET-JOURNAL FORMATTING ONLY**

## Canonical package

```text
PAPER02_MANUSCRIPT_REV7_ANON_2026-08-16.tex
blob 85e56d36d320e0012b28a6742f2b48d8c268af91

PAPER02_SUPPLEMENT_REV7_ANON_2026-08-16.tex
blob 947641ca95bcda1319b6b5ef322404ee14fba027

PAPER02_REFERENCES_REV7.bib
blob 3aef882d23cf81973b4091b7d5964d90ec4e53e2
```

Build identity:

```text
GitHub Actions run 31955139692
job 95184522376
artifact paper02-manuscript-rev7-v2-package
artifact id 9265784989
artifact SHA-256 b9f1087918e34e8b644f7c4039abf351ef08337a1381a7523d8f771566bac813
```

Compiled PDFs:

```text
main: 10 pages
SHA-256 622ef57e9c0f1a542fbe85215d0188f787c80f11f60081cd71401ef8fcf4d555

supplement: 5 pages
SHA-256 7791d4d639af311ba08b4f5c413ac05b4928ea4535878ad06f7991fec190f86b
```

A convenience delivery copy joining main plus supplement is not a canonical repository artifact; its local delivery SHA-256 is

```text
6fe059741d3c2546820e075a7aa51d4ee9a8bb4958f8f6faff31c8a31e161aa1
```

## Scientific identity

Working title:

> **Apparent diffusion from deterministic velocity gradients in wavelength-resolved photodetectors**

Author default:

```text
Anonymous
```

Central physical counterexample:

> In deterministic zero-microscopic-diffusion photodetector models, finite wavelength-dependent generation kernels that overlap spatial velocity heterogeneity can produce a positive effective diffusion coefficient when the resulting Shockley–Ramo terminal-current response is interpreted through a homogeneous drift–diffusion model.

The central velocity-heterogeneity counterexample uses **theoretical wavelength-dependent generation kernels supplied exactly to the inverse**. Rev. 7 separately relaxes the exact-kernel assumption as an attribution/model-uncertainty stress; do not conflate that stress with experimental calibration.

The exact planar continuum central result is approximately:

```text
D_eff(100 MHz) = 2.618164535e-3 m^2/s
D_eff(500 MHz) = 2.550830551e-3 m^2/s
D_eff(1 GHz)   = 2.350617904e-3 m^2/s
```

## Locked attribution boundaries

### Exact-known-kernel statistical ordering

```text
100 MHz: one-mode rejection occurs before positive-D detection
500 MHz: positive-D detection occurs before one-mode rejection
1 GHz:  positive-D detection occurs before one-mode rejection
```

The same qualitative ordering survives all twelve tested structured covariance metrics, but this is not an arbitrary-covariance theorem.

### Metric dependence

Under model misspecification the pseudo-true effective coefficient can depend on the weighting/covariance metric. In the tested covariance family the same 100-MHz deterministic response gives roughly

```text
D_eff = 1.66e-3 to 2.61e-3 m^2/s.
```

Do not describe the effective coefficient as a metric-independent material observable when the inverse family is misspecified.

### Optical-kernel uncertainty

A pure affine depth-coordinate error cannot create positive diffusion from exact `D=0`; the exact continuum affine control retains `|D_eff| < 4.7e-14 m^2/s` even with kernel-mean shifts up to 18 nm.

Non-affine, channel-dependent optical-model error can project onto the transport-root tangent. The signed wavelength-to-kernel nuisance tests demonstrate positive apparent diffusion in an exact uniform-velocity `D_micro=0` null.

The sub-nanometer nuisance amplitudes in Rev. 7 are **theoretical sensitivity coordinates**, not wavelength-meter specifications, measured calibration errors, or empirical detector error bars.

Thus exact kernel knowledge is a load-bearing condition for interpreting the fitted `D_eff` magnitude as a material parameter. It is not required for the logical existence of the separately established deterministic velocity-heterogeneity mechanism under its declared exact-kernel conditions.

## Locked physical interpretation of the planar stress

The collector-side parameter `Delta = 0.05 V` is defined by

```text
V'' = 2 Delta / W_d^2
```

with fixed endpoint potentials. It is a Poisson-curvature parameter, not an independently added terminal voltage.

Canonical exact planar field interpretation:

```text
Delta/W_d                         166.7 V/cm  characteristic curvature-field scale
curved-region field magnitude    328.9–662.3 V/cm
curved-region mean field          495.6 V/cm
uniform-bias field                394.7 V/cm
regional mean-field increment     100.9 V/cm
extra regional potential drop     0.030263 V
```

Do not regress to superseded “added 0.05-V drop” or equivalent language.

## Priority posture

Rev. 7 explicitly cites direct prior art showing that optical-model inputs can bias diffusion extraction from wavelength-dependent photodiode response. Generic optical-model sensitivity, inhomogeneous-field transport bias, wavelength-dependent RF photodiode phase, generalized least squares, nuisance projection, covariance propagation, and Schur complements are not claimed as new.

Current posture:

```text
DISTINCT DETECTOR-SPECIFIC COMBINATION PLAUSIBLE AFTER FOCUSED COLLISION AUDIT
BROAD INGREDIENTS ARE ESTABLISHED PRIOR ART
PRIORITY UNPROVEN
NO SUPERLATIVE PRIORITY CLAIM
```

Do not introduce `first`, `first-ever`, `fundamental`, `universal`, or equivalent priority language without a new explicit priority gate.

## Preservation history

- Rev. 5: previous promoted canonical manuscript; frozen.
- Rev. 6: compile-valid exact-continuum intermediate; intentionally never promoted; frozen.
- Rev. 7 v1 builder/workflow: scientific reruns passed, source transformation failed due brittle text anchoring; preserved as failed development provenance.
- Rev. 7 v2: full science, source, reference, independent compile, and rendered hostile-review gates passed; current canonical manuscript.

No earlier source should be deleted or silently rewritten.

## Current state record

Read next:

```text
PAPER02_CURRENT_STATE_REV7_2026-08-16.md
```

That record contains build hashes, convergence/covariance/model-uncertainty scope, priority boundary, hostile-review disposition, and submission-readiness decision.

## Future edits

Follow `PAPER02_MANUSCRIPT_PRESERVATION_PROTOCOL.md` and root `PRIVACY_PROTOCOL.md`.

Rev. 7 is frozen. Any material scientific correction must create a new numbered revision and pass applicable numerical, compilation, reference, anonymity, priority, and hostile-review gates.

Editorial target-journal formatting may be developed separately, but do not add author identity without explicit user authorization.
