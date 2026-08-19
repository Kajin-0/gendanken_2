# Paper 03 Stage-B blind v3 aligned-mesh lock

**Date:** 2026-08-18  
**Status:** **PREDECLARED GEOMETRY-DISCRETIZATION REPAIR / NON-CLAIM**

## 1. Preserved v1/v2 dispositions

B2-v1 is preserved as a numerical REFINE/failure because the 51x39 -> 61x47 six-current observable did not meet the frozen 2% spectral-shape criterion. Its auxiliary raw four-color phase coordinate was additionally found ill-conditioned and was retired only from the separate v2 acceptance design, not relabeled as passed.

B2-v2 froze 91x71 -> 101x79 before the 101x79 result. A pre-CI local diagnostic then showed a strong non-monotonic regression of the finite-contact six-current shape despite an apparently converged 81x63 -> 91x71 pilot pair. Therefore v2 is also preserved as **failed numerical confirmation** and no B2 A/B/C/D interpretation is permitted from it.

## 2. Identified numerical geometry defect

The synthetic finite structure has device width 16 um and selected top-contact fraction 0.75, so the physical contact occupies

```text
-6 um <= x <= +6 um.
```

The finite-volume contact mask classifies top boundary cells by cell-center position. If `nx` is arbitrary, the represented contact edge moves by a fraction of a cell as the mesh changes. The B2 spectral observable is sufficiently geometry-sensitive that this contact-width snapping can dominate the apparent coarse/fine difference.

For a uniform lateral grid with faces

```text
x_face = -8 um + m * (16 um / nx),
```

the physical edges x=+/-6 um coincide exactly with grid faces when `nx` is divisible by 8.

The production B2 convergence pair must therefore preserve the physical contact boundary exactly rather than comparing two slightly different discretized devices.

## 3. Frozen aligned production pair

Before either aligned-mesh result is generated, freeze

```text
coarse: 96 x 75
fine:   112 x 87
```

for both the finite 75%-contact structure and the same-physics full-top reference.

Both lateral counts are divisible by 8, so the finite selected-contact edges x=+/-6 um lie exactly on cell faces at both resolutions.

No result from the earlier arbitrary-nx pilot meshes may be substituted for this pair.

## 4. Acceptance rule

Use the unchanged v2 direct-observable rule at each of

```text
0, 100 MHz, 500 MHz, 1 GHz:

best complex-affine coarse->fine six-current shape residual
/ fine six-current contrast <= 0.02
```

and require it separately for the finite and full-top reference structures.

The historical raw four-color principal-log phase remains diagnostic only under v3, for the mathematical reasons recorded in the v2 lock. It is reported but is not an acceptance coordinate and cannot strengthen the scientific claim.

If any six-current shape row exceeds 2%, v3 fails and B2 remains numerically unresolved. No mesh may be selected post hoc from a sweep as the final passing pair.

## 5. All scientific blind-analysis rules remain frozen

Unchanged:

- synthetic Stage-B semiconductor parameters;
- Poisson + SG operating-state equations and boundary conditions;
- separate selected-electrode weighting solve;
- independently assembled backward generator;
- six actual calibrated discrete depth kernels;
- common centered 2-um lateral beam and support;
- dc / 100 MHz / 500 MHz / 1 GHz coordinates;
- blind input whitelist;
- one-mode and two-mode calibrated-kernel models;
- root stability <=5%;
- analytic warning-before-claim convention;
- frozen false-claim SNR coordinates;
- conservative B2 A/B/C/D classification.

## 6. Claim boundary

This v3 repair changes only the numerical representation of a boundary whose physical coordinate was already fixed. It does not change the physical contact width, forward equations, statistical threshold, or scientific interpretation rule.

No aligned 96x75 or 112x87 B2 result is known when this lock is committed.
