# Paper 02 — Current State after Rev. 8

**Date:** 2026-08-16  
**Status:** **ANONYMOUS REV. 8 / CANONICAL / FULL SCIENCE-COMPILE-RENDER GATE PASSED / SCIENTIFICALLY SUBMISSION-READY**

## Canonical package

```text
PAPER02_MANUSCRIPT_REV8_ANON_2026-08-16.tex
PAPER02_SUPPLEMENT_REV8_ANON_2026-08-16.tex
PAPER02_REFERENCES_REV7.bib
```

Rev. 7 remains frozen provenance and is superseded for submission by Rev. 8. Paper 01 / anonymous Rev. 9 is untouched.

## Final scientific scope

The central result is explicitly restricted to a **single-mobile-carrier / unipolar planar Shockley–Ramo observable**. It is not claimed for the complete electron–hole transient of a generic photodiode.

The exact pair-aware audit motivated this restriction rather than being tuned to preserve the original sign:

- pair dc full-collection identity error: `1.11e-16`;
- the uniform two-carrier null recovers numerical-zero diffusion;
- with the simple countercarrier propagation root fixed to its correct value and its complex amplitude profiled, only `1/21` core heterogeneous speed/frequency cases retains positive downstream inferred diffusion.

Therefore no generic two-carrier extension is claimed.

## Central exact-continuum result

For the checked unipolar deterministic surrogate with microscopic diffusion and recombination both zero:

```text
D_eff(100 MHz) = 2.618164535e-3 m^2/s
D_eff(500 MHz) = 2.550830551e-3 m^2/s
D_eff(1 GHz)   = 2.350617904e-3 m^2/s
```

The exact upstream point-source control remains at numerical-zero diffusion scale, while an inside-heterogeneity point-source control remains positive. The exact planar continuum is now the primary full-contact calculation; the independent two-dimensional field/trajectory solver is retained as a numerical reproduction/generalization path.

## Adversarial-review closure

The claim-affecting Rev. 8 issues are closed as follows:

1. **Carrier species:** resolved by explicit unipolar scope plus exact two-carrier stress.
2. **`remote` wording:** narrowed to finite-support coupling with mean generation depths upstream; no stronger weak-tail claim is required.
3. **Upstream logical bridge:** exact affine-plus-one-exponential solution added for a uniform upstream interval; downstream heterogeneity enters the matching constant.
4. **Primary numerical calculation:** exact planar continuum promoted; mesh calculation is secondary reproduction/generalization.
5. **Multi-frequency rejection:** root-space and direct full-channel tests are both reported and treated as complementary.
6. **Submission-facing cleanup:** SNR dB convention is explicit; internal review/run-history prose is removed from the PDFs; anonymity is preserved.
7. **HgCdTe realism:** remains a conditional optical/field/timing scale example, not a claimed calibrated or fully self-consistent detector simulation.

## Full-channel versus root-space rejection

Under the declared equal-quadrature noise model, `S_dB = 20 log10 S`, false-rejection probability `alpha=0.0027`, and 90% power:

```text
through 1 GHz: root-space 90.37 dB; full-channel 81.51 dB
through 2 GHz: root-space 73.20 dB; full-channel 72.28 dB
through 3 GHz: root-space 64.21 dB; full-channel 65.00 dB
```

The full-channel statistic is stronger at intermediate bandwidth because it retains same-frequency normal residuals; by 3 GHz the lower-dimensional root-space statistic is slightly stronger after its smaller residual degrees-of-freedom penalty. Neither is claimed globally optimal outside the declared model/covariance family.

## Final build and rendered-QA identity

```text
GitHub Actions run: 31983951996
job:               95255579031
artifact:          paper02-manuscript-rev8-package
artifact id:       9273251646
artifact SHA-256:  653c996b3166211cb465efceee5ba64944b7e92eab14c0ae38046e7fc89f2b60

main PDF:          11 pages
main SHA-256:      97a0916bcc83f94221f78e3315cf21e9b3c593a2a40601470cbf0dcdc685df75

supplement PDF:    5 pages
supp SHA-256:      a7dadfe7289a715f53c09456a315e81d83393a4dd3fc90aee9b683d0d1e717db
```

The final PDFs were rendered page-by-page after compilation. No clipping, figure/text collisions, malformed equations, unresolved reference markers, anonymity leakage, or internal workflow-ID prose remained. The final CI-rendered main PDF is pixel-identical to the reviewed main render; the final CI-rendered supplement is pixel-identical to the independently compiled and reviewed cleaned supplement.

## Priority posture

```text
DISTINCT DETECTOR-SPECIFIC COMBINATION PLAUSIBLE AFTER FOCUSED COLLISION AUDIT
BROAD INGREDIENTS ARE ESTABLISHED PRIOR ART
PRIORITY UNPROVEN
NO SUPERLATIVE PRIORITY CLAIM
```

No novelty is claimed for generalized least squares, nuisance projection, Schur complements, generic optical-model sensitivity, wavelength-dependent photodiode RF phase, inhomogeneous-field transport bias, or the general fact that absorption-model errors can bias transport inference.

## Remaining work

There is no known unresolved scientific blocker in the present manuscript. Remaining work is target-journal submission preparation: journal-specific formatting/length/metadata, author identity after explicit authorization, cover letter, and any repository/archive DOI chosen for submission. Any later material scientific correction requires a new numbered revision under the preservation protocol.
