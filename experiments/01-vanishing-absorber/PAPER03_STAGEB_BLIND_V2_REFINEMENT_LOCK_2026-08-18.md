# Paper 03 Stage-B blind v2 refinement lock

**Date:** 2026-08-18  
**Status:** **PREDECLARED REPLACEMENT NUMERICAL GATE / NON-CLAIM**

## 1. Why a v2 numerical gate is required

The original B2 lock (`PAPER03_STAGEB_BLIND_SIX_CHANNEL_LOCK_2026-08-18.md`) added two numerical acceptance coordinates for the 51x39 -> 61x47 six-channel response:

1. best complex-affine coarse-to-fine six-current shape residual / fine contrast <= 0.02;
2. change of the historical raw four-color closure phase / frozen microscopic target phase <= 0.02.

A pre-CI local reconstruction of the exact committed Stage-B equations shows that the first pair is not sufficiently resolved for the RF observable: the direct six-current shape residual is above 2% at the nonzero RFs. Therefore v1 is **REFINE**, not pass.

The same pilot also shows that the auxiliary raw four-color log-phase is a poor numerical convergence coordinate for this self-consistent point. Its principal-log phase changes by degrees while the underlying six complex currents converge smoothly. This is consistent with the original lock's explicit statement that raw four-color closure is only a historical comparison coordinate because the optical kernels are not exact translations; the calibrated-kernel fit is the physical null.

The v1 raw-phase criterion is not relabeled as passed and its threshold is not relaxed. It is retired from the v2 acceptance rule as an ill-conditioned derived diagnostic and will continue to be reported. The production convergence gate is moved to the actual six complex terminal-current observable that is supplied to the blind analyzer.

## 2. Mesh pilot and frozen production pair

A mesh-refinement pilot through 91x71 was used only to locate a production resolution. The direct complex-affine six-channel mismatch decreases normally with refinement and is already below 2% for the 81x63 -> 91x71 pair at every RF.

Before any 101x79 result is generated, freeze the independent production confirmation pair as

```text
91 x 71 -> 101 x 79.
```

No B2 A/B/C/D scientific classification may use the pilot meshes as its final convergence pair.

## 3. v2 observable convergence rule

For both the finite 75%-top-contact structure and same-physics full-top reference, independently generate the six complex selected-terminal currents at

```text
0, 100 MHz, 500 MHz, 1 GHz
```

on 91x71 and 101x79.

At each RF, fit the best complex affine map from the 91x71 six-current vector to the 101x79 vector,

```math
J^{101}_m \approx a+b J^{91}_m,
```

and require

```text
||a + b J_91 - J_101||_2 / ||J_101 - mean(J_101)||_2 <= 0.02.
```

This criterion is invariant to an overall complex gain and offset and directly tests convergence of the spectral shape used by the blind hierarchy.

Require the 2% bound separately at all four RF coordinates for both structures. If any row fails, B2 remains numerically unresolved and no A/B/C/D interpretation may be promoted.

## 4. Historical raw four-color diagnostic

Continue to record the principal-branch raw four-color closure phase and its coarse/fine change at every RF, but do not use it as a v2 pass/fail coordinate. It is explicitly labeled an ill-conditioned historical diagnostic for this Stage-B point and may not be used to strengthen the scientific claim.

## 5. Blind-analysis and precision rules remain unchanged

All other B2 rules remain exactly as previously frozen:

- actual discrete calibrated depth kernels;
- same centered 2-um lateral source envelope and support;
- unit source normalization;
- data-only blind input whitelist;
- all-six calibrated-kernel one-mode fit;
- two-mode diagnostic at nonzero RF;
- root stability <= 5% between the final production meshes;
- analytic one-mode warning SNR in the established per-quadrature convention;
- frozen false-claim SNRs 96.1 / 82.3 / 76.7 dB;
- conservative B2 classification clarification: an uncalibrated deterministic root-law violation cannot substitute for a missing precision-calibrated one-mode warning.

## 6. Claim boundary

B2-v1 remains a preserved numerical failure/refinement trigger. Passing B2-v2 establishes convergence of the actual six-channel self-consistent terminal-current observable; it does not retroactively make the v1 raw-phase criterion pass.

No scientific A/B/C/D outcome is known at the time this 91x71 -> 101x79 production pair is frozen.
