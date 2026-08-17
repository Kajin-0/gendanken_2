# Paper 02 — Rev. 4 hostile review

**Date:** 2026-08-16  
**Disposition:** **DO NOT PROMOTE / ONE PHYSICS-SEMANTICS BLOCKER / BUILD OTHERWISE CLEAN**  
**Reviewed source:** `PAPER02_MANUSCRIPT_REV4_ANON_2026-08-16.tex`  
**Reviewed supplement:** `PAPER02_SUPPLEMENT_REV4_ANON_2026-08-16.tex`

## Build and reproducibility gates

Rev. 4 successfully passed the controlled source-generation, regenerated-figure, anonymity/priority, LaTeX compilation, and unresolved-reference gates in GitHub Actions run `31949095476`, job `95169650767`.

Compiled package:

```text
main manuscript: 17 pages
supplement:        4 pages

main PDF SHA-256:
673c199b3d6f65c29129edeb2f99c544c7906c16ed43e3df04a6f4b899431819

supplement PDF SHA-256:
62d7f98d7026f15120f60c15df65f2ae9a42cb39ba01e18ff91856eed5660c1d
```

Artifact:

```text
paper02-manuscript-rev4-package
artifact id 9264358263
artifact SHA-256 98bdc5222ac43f3c026ee3d3b0cab6b34bca5a2ff00e984eca62660973261842
```

Rev. 4 also correctly:

- keeps `D_micro=0` distinct from fitted `D_eff>0`;
- describes the finite optical kernels as theoretical/supplied to the inverse rather than experimentally calibrated;
- preserves the corrected same-frequency ordering at 100, 500, and 1000 MHz;
- incorporates the independently passed inferential convergence gate;
- supplies actual Supplemental Material rather than merely promising it;
- adds the load-bearing Hansen band-gap and Moazzami absorption-model citations;
- preserves anonymous authorship and the no-superlative priority posture.

## Blocking defect

The conditional HgCdTe scale section in the main manuscript states that the planar stress

> adds an electrostatic drop of 0.05 V across a 3.0 um collector-side region, corresponding to an average added field of 166.7 V/cm.

The supplement similarly calls `0.05 V` an added space-charge potential scale and `166.7 V/cm` an average added-field scale.

That wording is not the exact semantics of the numerical Poisson model.

In `realistic_geometry_closure_stress.py`, the terminal potentials remain fixed at

```math
V(0)=0,
\qquad
V(L)=V_{\rm bias}=0.30\ \mathrm V,
```

while the collector-side region of width `W_d=3.0 um` receives the Poisson curvature

```math
V''(z)=\frac{2\Delta}{W_d^2},
\qquad
\Delta=0.05\ \mathrm V.
```

Thus `Delta` is a curvature parameter, not an independently added terminal voltage.

For the full-contact planar continuum solution, with `a=L-W_d`,

```math
V(z)=Az,
\qquad 0\le z<a,
```

and

```math
V(z)=Az+\frac{\Delta}{W_d^2}(z-a)^2,
\qquad a\le z\le L,
```

where

```math
A=\frac{V_{\rm bias}-\Delta}{L}.
```

At `L=7.6 um`, `W_d=3.0 um`, `Delta=0.05 V`, and `V_bias=0.30 V`, the corresponding field magnitudes are

```text
upstream edge of curved region: 328.947 V/cm
collecting boundary:            662.281 V/cm
mean over curved region:        495.614 V/cm
uniform-bias field:             394.737 V/cm
mean increment over uniform:    100.877 V/cm
```

The actual increase in potential drop across the last `3 um` relative to the uniform-bias profile is `0.030263 V`, not `0.05 V`.

`Delta/W_d = 166.667 V/cm` is instead a useful **characteristic curvature-field scale**, while `2 Delta/W_d = 333.333 V/cm` is the quadratic-term field swing across the curved region before the fixed-terminal-bias redistribution is accounted for.

## Scientific consequence

This correction does **not** invalidate the counterexample, the inferred `D_eff`, the causal controls, or the numerical convergence result. It changes the physical interpretation of one model parameter in the HgCdTe scale-comparison paragraph.

The plausibility comparison actually becomes cleaner: the exact mean field increment of approximately `100.9 V/cm` remains within the independently reported `~100--200 V/cm` composition-gradient field range used in the manuscript as a scale comparison. But the manuscript must compare like with like and must not call `Delta/W_d` the average added field.

## Required Rev. 5 repair

Rev. 4 is preserved as compiled intermediate provenance and must not be edited in place.

Rev. 5 must:

1. replace the incorrect main-text field-scale sentence with the exact Poisson-curvature semantics;
2. state that `Delta/W_d=166.7 V/cm` is a characteristic curvature-field scale;
3. report the exact planar field span `328.9--662.3 V/cm` and mean increment `100.9 V/cm` relative to the uniform-bias field;
4. make the same correction in Supplemental Material and include the governing piecewise planar solution;
5. add automated guards that reject the phrases `adds an electrostatic drop`, `average added field of`, and `average added-field scale` in the new manuscript package;
6. rerun the full figure-generation, convergence-input, privacy/priority, compilation, and unresolved-reference gates;
7. undergo another hostile scientific review before the current-manuscript pointer advances.

Until those conditions are met, Rev. 3 remains the canonical frozen manuscript pointer and Rev. 4 remains noncanonical provenance.
