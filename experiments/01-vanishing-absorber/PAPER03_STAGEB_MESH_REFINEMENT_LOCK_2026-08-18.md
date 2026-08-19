# Paper 03 Stage-B mesh refinement lock

**Date:** 2026-08-18  
**Status:** **PREDECLARED CONTINUATION OF FAILED GENERIC NUMERICAL GATE / NON-CLAIM**

This file extends, but does not relax, `PAPER03_STAGEB_MESH_WEIGHTING_RECIPROCITY_LOCK_2026-08-17.md` after its first execution failed the minimum-density convergence coordinate.

## 1. Preserved failure

The original workflow is retained as a failed gate. Its implementation stopped first on the coarse `21x15 -> 31x23` minimum-density change because the script inadvertently enforced the convergence thresholds on that diagnostic pair as well as the predeclared finest pair. The original lock, however, explicitly designated `31x23 -> 41x31` as the acceptance pair.

Independent diagnostic evaluation of the intended `31x23 -> 41x31` pair also gives a minimum-density relative change above the unchanged 5% threshold (about 7%), so the scientific disposition is still **REFINE**, not pass.

No original threshold is changed and the failed execution is not relabeled.

## 2. Frozen refinement meshes

Append two meshes to the existing ladder:

```text
21 x 15   historical diagnostic
31 x 23   historical diagnostic
41 x 31   prior finest mesh
51 x 39   refinement mesh 1
61 x 47   refinement mesh 2 / new finest mesh
```

The same synthetic operating-state physics and parameters remain fixed.

## 3. Refined convergence gate

The new acceptance pair is fixed before execution as

```text
51 x 39 -> 61 x 47.
```

Require the same thresholds from the original lock:

```text
absolute relative change of mean terminal/cut current <= 0.03
centerline potential RMS change / max(V_T, |V_top|) <= 0.02
centerline density RMS change / N_D <= 0.03
relative change of min(n/N_D) <= 0.05
centerline weighting-potential RMS change <= 0.02
```

All earlier adjacent-pair changes are recorded as diagnostics but are not substituted for the frozen refined acceptance pair.

Every mesh must independently retain:

```text
positive finite carrier density
Poisson residual < 1e-8
continuity residual < 1e-8
horizontal-cut current nonconservation < 1e-5
terminal imbalance < 1e-5
weighting linear residual < 1e-10
weighting potential within [0,1] to 1e-10 tolerance.
```

If the `51x39 -> 61x47` pair fails any unchanged threshold, the result remains a formal mesh-convergence failure and no tolerance may be relaxed post hoc.

## 4. Signal validation on the new finest mesh

Only if the operating-state/weighting solves exist on the new finest mesh, repeat the unchanged frozen-field signal validation at `61x47`:

```text
f = 500 MHz
max |delta n| / N_D = 1e-4
DC committor residual < 1e-8
DC Ramo residual < 1e-8
max |H_0-(p_sel-phi_w)| < 1e-8
backward residual < 1e-8
forward residual < 1e-8
relative reciprocity mismatch < 1e-9
relative ||F-Q^T|| < 1e-12
```

`F` and `Q` remain independently assembled as required by the corrected implementation.

## 5. Claim boundary

Passing this continuation establishes only the generic numerical Stage-B mesh/weighting/reciprocity layer. It does not establish HgCdTe material realism, bipolar operation, the six-channel Stage-B blind result, or Paper-03 standalone GO.

`science_interpretation_ready = false` until the remaining locked gates are resolved.
