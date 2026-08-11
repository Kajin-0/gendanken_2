# Rev. 3 Geometry Integration Plan - Preserve Prior Manuscript

**Date:** 2026-08-11  
**Status:** repository-integrity correction after manuscript-history audit

## 1. Authoritative pre-geometry manuscript

The user-facing manuscript immediately preceding the two-dimensional geometry stress is the 16-page Rev. 3 build:

```text
Fisher_Spectral_Depth_Closure_Paper_REV3_2026-08-11.pdf
Fisher_Spectral_Depth_Closure_Paper_REV3_2026-08-11.tex
```

That source was generated during the previous review pass but was not committed to `main`. The checked-in `MANUSCRIPT_DRAFT.tex` is older and therefore must not be mistaken for the latest user-facing paper.

The 16-page source already contains the review-driven work that must be preserved, including:

- the full four-color Shockley-Ramo derivation and nuisance invariances;
- no-recombination and recombining DC+RF inversions;
- exact DC+RF conditioning formulas and the `D omega / V_*^2 = sqrt(3)` balanced point;
- six-color Hankel rank-two closure, noise significance, finite-boundary roots, and two-carrier branch;
- hot-to-cold thermalization as a conventional rank-two mechanism, including quantitative thermalization-length stresses;
- nonuniform weighting-field forcing, the `q_weight = 1` signature, polynomial observation annihilation, five-color exact null, low-RF degeneracy, and sub-percent weighting-field sensitivity;
- optical source-shape, relative-amplitude, unequal-spacing, coordinate-uncertainty, and excess-energy corrections;
- four-color independent-noise covariance, spacing optimum, and `h_* proportional to t^(-1/6)` scaling;
- the complete conditional HgCdTe optical/transport example, recombination stresses, independent shooting cross-check, and measurement-resource table;
- conservative discussion and priority language.

## 2. Do not rewrite the paper to add the geometry result

A new agent briefly produced a compressed 12-page reconstruction. The history audit showed that this unnecessarily removed or shortened established material and even replaced the author name with a placeholder. That reconstruction is **not authoritative** and must not be merged.

The geometry result should instead be applied as a surgical revision to the recovered 16-page Rev. 3 source.

## 3. Minimal manuscript changes justified by the new result

When the authoritative 16-page source is imported into the repository, make only these substantive changes unless a separate review independently requires more:

1. Add one abstract sentence stating that a representative 2-D finite-electrode/depletion stress can mimic 74-87% of the current 1-D HgCdTe gradient phase, while its second spatial mode becomes resolvable before the SNR required for the 100-MHz gradient claim.
2. Add a dedicated geometry-hardening section after the existing HgCdTe worked example. The detailed source is `REALISTIC_GEOMETRY_CLOSURE_STRESS.md`.
3. Add one discussion paragraph clarifying that four-color failure is not mechanism-specific; six-color model order and RF root laws are required before assigning a velocity gradient.
4. Amend the limitations paragraph to state that the present 2-D calculation is deterministic/high-Peclet and not yet a self-consistent semiconductor Poisson/drift-diffusion device simulation.
5. Add one conclusion paragraph recording the narrowed geometry claim.

Do **not** delete, rephrase wholesale, or compress unrelated prior sections during this integration.

## 4. New geometry claim boundary

The new checked result is:

```text
four colors -> detect one-mode failure
six colors  -> test whether an additional spatial mode is resolved
RF roots    -> test whether the resolved mode matches an ordinary mechanism
```

A four-color residual alone is not a mechanism label.

The five-color polynomial-observation theorem remains exact for its stated one-dimensional polynomial-forcing hypothesis. The 2-D calculation shows only that it is not a universal cure for curved multidimensional weighting/depletion geometry.

## 5. Repository rule going forward

Before any future manuscript rewrite or compression:

1. recover the latest user-facing source, not merely the latest committed draft;
2. diff section structure and equation/claim inventory against the proposed revision;
3. preserve prior derivations, quantitative stresses, calibration corrections, and validation tables unless a documented scientific reason invalidates them;
4. prefer surgical insertion over wholesale reconstruction.

The geometry calculation itself is new work and is retained. The large manuscript reconstruction is not.