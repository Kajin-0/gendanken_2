# Paper 02 — Current State Rev. 7

**Date:** 2026-08-16  
**Status:** **ANONYMOUS REV. 7 PROMOTED / SCIENTIFICALLY SUBMISSION-READY / TARGET-JOURNAL FORMATTING ONLY**  
**Supersedes for navigation:** `PAPER02_CURRENT_STATE_REV5_2026-08-16.md` and the Rev. 7 development checkpoint.  
**Preservation:** all earlier manuscript/state/result revisions remain provenance and must not be deleted or silently rewritten.

## 1. Canonical manuscript package

Main source:

```text
PAPER02_MANUSCRIPT_REV7_ANON_2026-08-16.tex
blob 85e56d36d320e0012b28a6742f2b48d8c268af91
```

Supplement source:

```text
PAPER02_SUPPLEMENT_REV7_ANON_2026-08-16.tex
blob 947641ca95bcda1319b6b5ef322404ee14fba027
```

Bibliography:

```text
PAPER02_REFERENCES_REV7.bib
blob 3aef882d23cf81973b4091b7d5964d90ec4e53e2
```

Full-gate workflow:

```text
run      31955139692
job      95184522376
artifact paper02-manuscript-rev7-v2-package
id       9265784989
artifact SHA-256 b9f1087918e34e8b644f7c4039abf351ef08337a1381a7523d8f771566bac813
```

Compiled PDFs:

```text
main manuscript: 10 pages
SHA-256 622ef57e9c0f1a542fbe85215d0188f787c80f11f60081cd71401ef8fcf4d555

supplement: 5 pages
SHA-256 7791d4d639af311ba08b4f5c413ac05b4928ea4535878ad06f7991fec190f86b
```

The gate independently compiled a minimal packaged copy after the branch-tree compile, checked unresolved references/citations, persisted the deterministic sources, and uploaded the final package.

## 2. Revision provenance

Rev. 5 was the previous promoted canonical manuscript.

Rev. 6 is a compile-valid but intentionally unpromoted exact-continuum intermediate. It remains frozen provenance and must not be retroactively labeled canonical.

The first Rev. 7 builder/workflow attempted a material model-uncertainty revision but failed only in brittle source transformation after every scientific rerun had passed. That failure is preserved. Rev. 7 v2 replaced the brittle whole-paragraph transformation with exact frozen-blob guards and stable section anchors, then reran the full science and compilation gate from a clean branch checkout.

No Paper-01 source was modified.

## 3. Central scientific result

The central physical counterexample remains deterministic velocity heterogeneity, not optical-model error:

> In a zero-microscopic-diffusion Shockley–Ramo photodetector model, finite wavelength-dependent generation kernels that overlap deterministic spatial velocity heterogeneity can produce a positive effective diffusion coefficient when an exact-known-kernel terminal-current response is interpreted through a homogeneous drift–diffusion inverse.

The post-hoc exact planar continuum calculation gives approximately

```text
D_eff(100 MHz) = 2.618164535e-3 m^2/s
D_eff(500 MHz) = 2.550830551e-3 m^2/s
D_eff(1 GHz)   = 2.350617904e-3 m^2/s
```

with the upstream point-source sequence at numerical-zero diffusion scale and the inside-nonuniform-region point-source control positive.

The finite-support/mean-preserving causal ablations, independent velocity-profile signs, analytical local exponent, bias law, exact continuum cross-check, and RF dispersion-rejection calculation remain controlling evidence.

## 4. Measurement-covariance robustness

The exact-known-kernel heterogeneous response was re-fit under twelve normalized structured covariance shapes.

The qualitative same-frequency ordering survives every tested case:

```text
100 MHz: one-mode rejection first       12/12
500 MHz: positive-D detection first     12/12
1 GHz:   positive-D detection first     12/12
```

The numerical pseudo-true coefficient is nevertheless metric-dependent. At 100 MHz the same deterministic response yields approximately

```text
D_eff = 1.66e-3 to 2.61e-3 m^2/s
```

across the tested weighting metrics.

Cross-frequency AR(1)/equicorrelated root errors change the 3-GHz rejection requirement by at most about +1.1 dB in the tested family; the bandwidth-discrimination result therefore survives those correlations.

This is robustness over a declared structured family, not arbitrary-covariance proof.

## 5. Optical-kernel/model-uncertainty boundary

The exact-known-kernel assumption is now explicitly identified as load-bearing for interpreting the **magnitude** of the recovered effective diffusion as a material quantity.

General local nuisance geometry is recorded separately and used without claiming novelty for generalized least squares, nuisance projection, Fisher information, or Schur complements.

A fixed kernel nuisance can decompose into a transport-tangent bias plus a normal model-rejection signal. A zero-mean random kernel nuisance can contribute to effective covariance at first order, whereas a fixed biased nuisance retains deterministic parameter bias.

### Exact affine null

A global affine depth-coordinate rescaling obeys

```text
gamma_eff = b gamma
D_eff     = D / b^2
w_eff     = w / b
```

and therefore cannot create positive diffusion from exact `D=0`.

The exact continuum control moves kernel means by as much as 18 nm for a 1% depth-scale compression while retaining

```text
max |D_eff| < 4.7e-14 m^2/s.
```

### Non-affine signed nuisance control

In an exact uniform-velocity `D_micro=0` null, while the inverse uses the nominal theoretical kernels, the signed channel-linear wavelength-to-kernel nuisance

```text
delta_lambda_m = A[-1,-0.6,-0.2,+0.2,+0.6,+1]
```

reproduces the central heterogeneous 100-MHz apparent diffusion at

```text
A = +0.0299713 nm
max kernel-mean shift = 0.205754 nm
D_eff = 2.618164535e-3 m^2/s
one-mode fit residual = 3.09e-8
positive-D threshold = 115.22 dB
one-mode rejection threshold = 156.81 dB.
```

A signed curvature nuisance reaches the same target at

```text
A = -0.00294205 nm
max kernel-mean shift = 0.020041 nm
positive-D threshold = 115.23 dB
one-mode rejection threshold = 138.14 dB.
```

These amplitudes are **theoretical nuisance coordinates**, not wavelength-meter specifications, measured calibration errors, or empirical detector error bars.

The scientific consequence is not that velocity heterogeneity has been replaced as the mechanism. It is that a fitted diffusion magnitude is material-like only to the extent that optical nuisance directions overlapping the transport-root tangent are independently constrained.

## 6. Prior-art boundary after Rev. 7

The enlarged model-uncertainty framing was subjected to a focused closest-collision audit.

Direct boundary sources include:

- Ashry and Fares (2003): wavelength-dependent photodiode response used to infer diffusion length; absorption-coefficient error can bias the extracted diffusion quantity;
- Hattori et al. (1992): transport-model assumptions can bias diffusion-length extraction;
- Emelianova et al. (2006): inhomogeneous fields can bias apparent transport parameters under homogeneous-field interpretation;
- Hawks et al. (2015): terminal current is an observation functional and can be misinterpreted as microscopic carrier motion;
- the OED literature: wavelength-dependent photodiode RF phase and inverse spectroscopy are established.

Ashry--Fares is cited directly in Rev. 7. The manuscript explicitly does **not** claim novelty for generic optical-model sensitivity, wavelength-calibration sensitivity, generalized least squares, nuisance projection, or Schur-complement geometry.

Current priority posture:

```text
DISTINCT DETECTOR-SPECIFIC COMBINATION PLAUSIBLE AFTER FOCUSED COLLISION AUDIT
BROAD INGREDIENTS ARE ESTABLISHED PRIOR ART
PRIORITY UNPROVEN
NO SUPERLATIVE PRIORITY CLAIM
```

No direct collision containing the integrated zero-`D_micro`, finite spectral-kernel, Shockley–Ramo, deterministic-velocity-heterogeneity, causal-support, signed-kernel-null, tangent/normal, and covariance-aware RF attribution construction was found in the focused search. Absence in a focused search is not a first-priority proof.

## 7. Hostile review disposition

The compiled 10-page manuscript and 5-page supplement were rendered page-by-page after the full gate.

Passed checks:

- no identity leakage; both documents remain `Anonymous`;
- no superlative priority language;
- no unresolved references or citations;
- no clipped text, figure collisions, broken equations, malformed glyphs, or corrupted pages;
- new covariance/kernel-uncertainty section is legible in the two-column layout;
- Ashry--Fares precedent is acknowledged before the new optical-model sensitivity result;
- deterministic velocity heterogeneity remains the paper's central physical counterexample;
- exact-known theoretical kernels are separated from the separately labeled perturbed-kernel stress;
- sub-nanometer nuisance coordinates are explicitly barred from interpretation as instrument specifications;
- exact affine-depth control and non-affine false-diffusion control are logically consistent;
- locked 100/500/1000-MHz exact-known-kernel statistical ordering is preserved;
- covariance conclusions are limited to the tested structured families;
- HgCdTe comparison remains a scale/plausibility check, not a calibrated-device prediction;
- Rev. 6 and failed Rev. 7-v1 paths remain provenance rather than being erased.

**Disposition: PASS. No substantive Rev. 8 is warranted.**

## 8. Submission readiness

The earlier scientific blockers have now been dispositioned:

```text
exact-continuum independent implementation   PASS
inferential numerical convergence            PASS
same-frequency statistical semantics         PASS
multi-frequency rejection calculation        PASS
structured covariance stress                  PASS
optical-kernel/model-uncertainty stress       PASS
exact affine null control                     PASS
signed non-affine nuisance control             PASS
publisher/closest-collision prior-art boundary PASS
rendered hostile scientific review             PASS
```

A public experimental-data confrontation would be valuable if a genuinely matched dataset becomes available, but it is not required for the validity of this theoretical counterexample and is not treated as an artificial blocker.

**Paper 02 Rev. 7 is scientifically submission-ready.** Remaining work should be editorial only: choose the target journal, adjust format/length/style to that journal, add author identity only when explicitly authorized, and prepare submission metadata/cover letter. Material scientific changes must create a new numbered revision.

Paper 01 / anonymous Rev. 9 remains untouched.
