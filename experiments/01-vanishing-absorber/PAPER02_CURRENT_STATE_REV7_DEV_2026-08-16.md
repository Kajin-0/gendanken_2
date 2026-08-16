# Paper 02 — Rev. 7 development checkpoint

**Date:** 2026-08-16  
**Status:** **REV. 5 CANONICAL / REV. 6 COMPILE-VALID UNPROMOTED INTERMEDIATE / REV. 7 SCIENTIFIC REVISION AUTHORIZED**  
**Preservation:** Rev. 5 and Rev. 6 sources are frozen. Do not edit either in place.

## Canonical pointer

`PAPER02_MANUSCRIPT_CURRENT.md` remains on anonymous Rev. 5 until a later revision passes all required scientific and compilation gates.

## Rev. 6 disposition

Rev. 6 was built deterministically from frozen Rev. 5 and adds the post-hoc exact planar continuum cross-check plus bounded hostile-review wording corrections.

Frozen Rev. 6 blobs:

```text
PAPER02_MANUSCRIPT_REV6_ANON_2026-08-16.tex
blob 594a38fce4e93cc96df2d45b43c03eb71551ee74

PAPER02_SUPPLEMENT_REV6_ANON_2026-08-16.tex
blob 97ecf3e2b9d8ffd69c227a7c1946d4e7eb544d13
```

Rev. 6 full build workflow:

```text
run      31951656923
artifact paper02-manuscript-rev6-package
id       9264848168
SHA-256 bc1a70ed8fd9f738ecf9743d7e54191afdedff627f9cb79f9b37bbd172f31247
```

The workflow completed successfully, including exact-continuum re-execution, figure regeneration, deterministic source build, anonymity/epistemic guards, source persistence, main/supplement LaTeX compilation, unresolved-reference checks, independent package compilation, and artifact upload.

Rev. 6 was intentionally **not promoted** before the model-uncertainty program completed. It is now preserved as a compile-valid exact-continuum intermediate rather than being retrospectively re-labeled as canonical.

## New checked science requiring Rev. 7

The following records post-date the Rev. 6 scientific scope:

```text
PAPER02_COVARIANCE_GEOMETRY_STRESS_2026-08-16.md
PAPER02_GENERALIZED_NUISANCE_GEOMETRY_2026-08-16.md
PAPER02_KERNEL_MODEL_UNCERTAINTY_STRESS_2026-08-16.md
```

They establish, conditionally within the declared theoretical stress:

1. the 100/500/1000-MHz same-frequency ordering survives a broad family of covariance metrics;
2. the pseudo-true `D_eff` of a misspecified homogeneous inverse can depend materially on the weighting/covariance metric;
3. exact common complex gain and offset directions are absorbed by the profiled one-mode amplitude/offset and do not move the root;
4. a pure affine depth-coordinate error rescales the homogeneous root/drift but cannot create positive `D` from exact `D=0`;
5. fixed non-affine optical-kernel misspecification can create positive apparent diffusion from an exact uniform deterministic `D_micro=0` null;
6. local kernel-nuisance tangent/normal geometry predicts whether parameter bias becomes statistically visible before same-frequency model rejection;
7. in controlled signed wavelength-registration modes, differential linear and curvature errors can reproduce the central `D_eff` while remaining bias-first under the reference covariance;
8. the numerical magnitude `D_eff ~ 2.6e-3 m^2/s` is therefore not a calibration-robust material quantity unless the relevant kernel nuisance subspace is independently constrained.

## Rev. 7 scope lock

Rev. 7 must preserve deterministic velocity heterogeneity as the paper's central physical counterexample. It must **not** silently change the title into a broad generic inverse-problems paper.

Allowed additions:

- a bounded main-text section on covariance and optical-model uncertainty;
- generalized weighted tangent/normal equations explicitly labeled as standard projection/nuisance geometry rather than mathematical novelty;
- the checked covariance-ordering result;
- the exact affine-depth null control;
- one concise signed non-affine kernel-misspecification counterexample in the uniform `D=0` null;
- corresponding Supplemental Material reproducibility details;
- limitations/conclusion wording needed to prevent overinterpretation of the HgCdTe-like `D_eff` magnitude.

Not allowed without a separate later gate:

- claiming experimental kernel calibration;
- converting theoretical wavelength-error amplitudes into instrument specifications;
- claiming that kernel error is the mechanism in any published device;
- claiming arbitrary-covariance robustness;
- claiming novelty for generalized least squares, nuisance projection, Schur complements, or errors-in-variables theory;
- superlative priority language.

## Rev. 7 hard gates

Before promotion, Rev. 7 must:

1. be generated deterministically from the exact frozen Rev. 6 blobs above;
2. re-execute the exact planar continuum check;
3. re-execute covariance geometry stress;
4. re-execute broad kernel misspecification stress;
5. re-execute exact affine depth control;
6. re-execute frequency-corrected local kernel-nuisance tangent projection;
7. re-execute signed kernel-mode thresholds;
8. retain the locked same-frequency canonical ordering for the exact-known-kernel heterogeneous case;
9. compile main and supplement without unresolved citations/references;
10. pass anonymity and no-superlative-priority guards;
11. undergo a new hostile scientific review of the rendered package;
12. undergo a focused priority check on the enlarged nuisance-identifiability framing before the current pointer moves.

Paper 01 / anonymous Rev. 9 remains untouched.
