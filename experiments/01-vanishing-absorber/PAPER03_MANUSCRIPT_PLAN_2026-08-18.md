# Paper 03 manuscript plan

**Date:** 2026-08-18  
**Status:** **MANUSCRIPT SPINE / NOT A SCIENTIFIC RESULT**

This plan freezes the intended Paper-03 narrative so completion of the remaining numerical gates leads to drafting rather than open-ended extension.

## Working title

**When multidimensional photodetector geometry imitates transport: model-order and cross-frequency falsification before parameter inference**

Alternative shorter title:

**Falsifying transport-like signatures from multidimensional photodetector geometry**

## Core paper question

> Can ordinary multidimensional detector physics generate an order-one spectral/RF signature that looks like microscopic transport while still becoming rejectable through calibrated-kernel model order or physical cross-frequency root laws before the false homogeneous transport parameter becomes statistically defensible?

## Candidate central result

The present checked Stage-A evidence supports the following narrow candidate conclusion:

```text
ordinary finite-contact / electrostatic / diffusion / recombination / beam geometry
can generate order-one transport-like spectral/RF phase signatures;

but across the predeclared first-family regime map and a materially different
coplanar-contact topology, the wrong homogeneous one-mode interpretation
self-announces through calibrated-kernel model-order mismatch and/or
cross-RF physical-root-law failure before the false transport claim reaches
its required measurement precision.
```

This remains subject to closure of the outstanding coplanar 500-MHz optimizer-integrity cell and the generic Stage-B validation layer.

## Explicit non-claims

The paper must not claim as new:

- wavelength-dependent absorption depth producing RF phase/amplitude dispersion;
- optoelectronic chromatic dispersion;
- arbitrary/nonuniform generation-profile effects on small-signal transport inference;
- Shockley-Ramo signal formation;
- generic Prony/Hankel/model-order methods;
- generic frequency-domain consistency testing;
- drift-diffusion inversion itself.

The candidate distinct contribution is the detector-specific **warning-before-false-claim** construction: calibrated spectral kernels are treated as an internal spatial sequence, a restrictive transport interpretation is tested through model order and cross-frequency physical root laws, and the precision required to reject the wrong model is compared directly with the precision required to support the false microscopic transport claim.

## Main-text structure

### I. Introduction

- Problem: realistic detector geometry can bias spectral/RF transport inference.
- Established adjacent literature: spectral-depth transport probing, OED, IMPS/nonuniform generation, model consistency.
- Gap: quantitative question of whether neglected ordinary device physics becomes *detectably inconsistent* before a wrong microscopic parameter claim becomes statistically persuasive.
- State falsification-first objective and predeclared Outcome A/B alternatives.

### II. Observable and inference hierarchy

- Terminal current is Shockley-Ramo weighted, not collection flux alone.
- Six calibrated optical kernels `g_m(z)`.
- Kernel-aware one-mode model `J_m=A+B M_m(r)`.
- Two-mode diagnostic extension.
- Homogeneous scalar physical root law and permutation-invariant root-sum constraint.
- Noise/SNR convention and warning-before-claim definition.

Keep Paper 01 theorem derivations brief; cite Paper 01 and reproduce only the minimum equations needed to make Paper 03 standalone.

### III. First multidimensional geometry family

- 2-D finite selected top contact + full bottom electrode.
- Controlled depletion/electrostatic curvature.
- Drift-diffusion, recombination, beam width/offset.
- Deterministic backward-resolvent production solver and numerical invariants.
- Why Monte Carlo is retained only as an independent coarse cross-check.

### IV. Broad predeclared regime map

- 60 detector coordinates / 180 RF rows.
- 42 order-one RF confounds; zero coarse analytic hidden-risk rows.
- Six mechanically selected S0-S7 refinement points.
- All six refined points preserve at least one order-one confound; no refined analytic hidden-risk point.
- Present max-confound and warning-boundary coordinates rather than every raw row in prose.

### V. Statistical warning-before-claim test

- Exact bootstrap convention: per-quadrature Gaussian noise, current-step SNR, 3-sigma alpha, 90% power, fixed SNR grid, no interpolation.
- Nominal S0 plus selected max-confound and warning-boundary points.
- Nine first-family RF comparisons all support early warning.
- Smallest conservative tested first-family warning margin: +9.16 dB.

### VI. Materially different coplanar topology

- Two top coplanar electrodes, insulating bottom, lateral/fringing physical and weighting fields.
- Numerical convergence gate.
- One-mode mismatch approximately 1-2% of contrast.
- Two-mode reduction and root-set grid stability.
- Strong violation of homogeneous scalar root-sum law.
- Valid 100-MHz and 1-GHz statistical warning results.
- Insert 500-MHz result only after optimizer-integrity rerun is authoritative.

### VII. Self-consistent semiconductor validation

Purpose: show that the self-announcement logic is not an artifact of prescribing a fixed physical field.

- Generic coupled Poisson + Scharfetter-Gummel dark operating state.
- Equilibrium/current-conservation/positivity regressions.
- Mesh refinement under the predeclared thresholds.
- Separate weighting potential.
- Discrete DC Ramo/committor identity.
- Independently assembled forward/backward small-signal reciprocity.
- Final blind six-channel Stage-B response if/when completed.

Keep generic synthetic Stage B distinct from any HgCdTe-specific claim.

### VIII. Discussion and experimental implications

- Outcome A versus Outcome B interpretation.
- Geometry can be large without being silent.
- Measurement-design consequence: acquire enough calibrated spectral channels to test model order before fitting microscopic transport.
- Report both rejection precision and parameter-claim precision.
- Mechanism unresolved is an acceptable scientific outcome.
- Limits: generic synthetic Stage B, no experimental data, no claim of universal topology independence, no complete material-specific bipolar HgCdTe device simulation unless separately validated.

### IX. Conclusion

One paragraph: ordinary geometry can imitate transport; the tested hierarchy detects the model inadequacy earlier than the wrong parameter becomes claim-worthy over the declared domains; therefore model falsification should precede microscopic interpretation.

## Planned main figures

1. **Falsification hierarchy and two geometry families.** Compact schematic: spectral kernels -> terminal currents -> one-mode test -> model order -> physical root law -> parameter claim; show vertical-contact and coplanar topologies.
2. **First-family regime map.** Geometry-mimic fraction and warning margin over the predeclared parameter lattice; selected S0-S7 coordinates marked.
3. **Refined adversarial coordinates.** Max-confound, warning-boundary, and nominal response; one-mode residual versus RF.
4. **Warning-before-claim statistics.** Required rejection SNR versus frozen false-transport claim SNR for nominal/max-confound/boundary coordinates, with conservative tested bootstrap points.
5. **Coplanar topology self-announcement.** Geometry, one-mode versus two-mode residual, and cross-RF root sums.
6. **Stage-B self-consistency validation.** Mesh convergence + independent forward/backward/Ramo diagnostics; include only after the refined gate is authoritative.

## Planned main tables

1. Forward-model coordinates and predeclared parameter ranges.
2. Mechanically selected refined first-family points and reasons S0-S7.
3. Bootstrap rejection thresholds, frozen claim thresholds, and warning margins.
4. Second-family model-order/root-law diagnostics.
5. Stage-B numerical validation summary if passed.

Full 60-point screen, all bootstrap calibration rows, solver residuals, and material-ledger provenance belong in the supplement/data package rather than the main text.

## Manuscript freeze rule

Do not add another broad Stage-A geometry sweep after the current two-family program.

Begin the full manuscript immediately when:

1. the coplanar 500-MHz statistical cell has an authoritative optimizer-integrity-passing result; and
2. the generic Stage-B mesh/weighting/reciprocity continuation is resolved.

If Stage B requires further refinement, preserve that outcome and decide whether the paper can honestly delimit Stage B as a validation boundary; do not relax a frozen numerical threshold merely to reach manuscript status.
