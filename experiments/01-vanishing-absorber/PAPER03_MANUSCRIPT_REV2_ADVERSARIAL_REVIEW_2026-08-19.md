# Paper 03 Rev. 2 adversarial manuscript review

**Date:** 2026-08-19  
**Status:** **INTERNAL ADVERSARIAL REVIEW / MANUSCRIPT REPAIR INPUT**

## Overall disposition

The frozen research record supports a standalone generic Paper-03 manuscript. No fatal defect in the central warning-before-claim result was found in this pass. Several manuscript-level vulnerabilities must remain explicit before submission.

## 1. Stage-B raw-phase convergence — repaired in Rev. 2

The first manuscript draft could be read as though the final self-consistent Stage-B result inherited a clean raw four-color phase-convergence claim. That is not correct.

Preserved numerical history:

```text
B2-v1 -> REFINE/failure
B2-v2 -> failed numerical confirmation
B2-v3 -> predeclared aligned-boundary repair
```

The defect was lateral contact-edge snapping: the 75%-contact physical edge lies at x=+/-6 um, while arbitrary lateral cell counts move the represented edge between meshes.

The final production pair was frozen before output as

```text
96x75 -> 112x87
```

with both lateral counts divisible by 8, placing the physical edge on a cell face at both resolutions.

The accepted convergence statistic is the best complex-affine coarse-to-fine six-current shape residual divided by fine-grid contrast. The nonzero-RF finite-structure values are

```text
100 MHz -> 0.0024767
500 MHz -> 0.0028103
1 GHz   -> 0.0031425
```

and the same-physics full-top values are

```text
100 MHz -> 0.0035328
500 MHz -> 0.0036969
1 GHz   -> 0.0037916
```

all below the frozen 0.02 gate.

The historical principal-log raw four-color phase is ill-conditioned in this case and remains diagnostic only. Its earlier failed convergence tests are not relabeled as passes. Rev. 2 now states this explicitly and does not use the enormous Stage-B historical raw-phase mimic ratio as quantitative evidence.

## 2. False-claim benchmark must be self-contained — repaired in Rev. 2

Rev. 1 assumed the reader knew the frozen comparison coordinates. Rev. 2 now defines them explicitly:

```text
RF        reference transport phase    frozen claim SNR
100 MHz   -0.011978 deg                 96.1 dB
500 MHz   -0.058727 deg                 82.3 dB
1 GHz     -0.110405 deg                 76.7 dB
```

These coordinates remain fixed throughout the Paper-03 program and are not refit to each geometry.

## 3. Statistical symmetry caveat — MUST BE ADDED IN NEXT REVISION

The two sides of the warning margin are deliberately not identical hypothesis-test calibrations.

The frozen transport-claim SNR is the pre-existing **3-sigma current-step amplitude threshold** for the mechanism-specific transport signal.

The Paper-03 warning threshold uses

```text
alpha = 0.002699796063260207
power = 0.90
```

and, for the first-family/coplanar claims, finite-sample parametric bootstrap with nonlinear refitting.

Therefore the manuscript must not imply that both SNR coordinates are 90%-power thresholds. The comparison is conservative in the direction relevant to the paper: the warning side is required to reach 90% power while the historical claim side is only the frozen 3-sigma claim coordinate.

Required wording for the next revision:

> The claim SNRs are the pre-existing 3-sigma current-step thresholds, not independently recalibrated 90%-power thresholds. The warning test is held to the stronger requirement of 90% power at the same nominal 3-sigma false-alarm probability. The reported positive margins are therefore conditional, deliberately asymmetric warning-before-claim comparisons rather than differences between two identically powered tests.

No claim threshold is to be recomputed after seeing Paper-03 results.

## 4. Full nine-cell first-family table — repaired in Rev. 2

Rev. 1 compressed the adversarial bootstrap evidence too aggressively. Rev. 2 gives all nine cells:

```text
S0 nominal:
100 MHz  76.545 vs 96.1 -> +19.555 dB
500 MHz  73.137 vs 82.3 -> +9.163 dB
1 GHz    65.892 vs 76.7 -> +10.808 dB

R1_B04 maximum confound:
100 MHz  62.273 vs 96.1 -> +33.827 dB
500 MHz  59.923 vs 82.3 -> +22.377 dB
1 GHz    56.690 vs 76.7 -> +20.010 dB

R2_A04 warning boundary:
100 MHz  62.360 vs 96.1 -> +33.740 dB
500 MHz  61.313 vs 82.3 -> +20.987 dB
1 GHz    57.658 vs 76.7 -> +19.042 dB
```

The minimum finite-sample margin remains +9.163 dB.

## 5. Stage-B evidence hierarchy — acceptable with current limits

At the aligned fine grid, the Stage-B calibrated-kernel one-mode residuals are

```text
100 MHz -> 0.5337
500 MHz -> 0.5742
1 GHz   -> 0.6123
```

and the two-mode diagnostic reduces them to approximately

```text
6.99e-5
3.63e-4
9.23e-4.
```

Matched roots are stable across the aligned grids and violate both the real-sum and RF-independent homogeneous scalar root law.

This is strong evidence of low-dimensional model inadequacy in the declared synthetic Stage-B model. It is not a material-specific semiconductor validation.

## 6. Prior-art boundary — acceptable, retain conservative wording

The manuscript correctly acknowledges established precedent for:

- wavelength/absorption-depth dependent photodiode RF phase / OED;
- spectral-response transport inference;
- arbitrary/nonuniform optical generation affecting small-signal transport interpretation;
- finite-exponential / Prony / Hankel / subspace model identification;
- Gummel iteration and Scharfetter-Gummel semiconductor discretization.

The manuscript must continue to claim only the narrower calibrated-kernel, mechanism-blind precision ordering and its validation stack. No first-ever, universal, or superlative priority language is justified.

## 7. Scope limitations that must remain

The following are not defects if stated clearly:

```text
Stage B is generic and single-electron, not HgCdTe-specific;
HgCdTe-specific elevated-temperature work likely needs bipolar transport and a closed material ledger;
no laboratory calibration/SNR feasibility has been demonstrated;
Stage-B warning coordinates are analytic, not a third finite-sample bootstrap campaign;
the arbitrary-kernel two-mode fit is diagnostic, not a universal theorem;
the tested detector domain is broad but not exhaustive.
```

## Current recommendation

Proceed to compilation of Rev. 2, then create a targeted next revision that adds the statistical-asymmetry paragraph above plus any genuine compile/PDF defects. Do not reopen the generic research domain unless manuscript review uncovers a material scientific dependency.
