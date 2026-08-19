# Paper 03 standalone GO record

**Date:** 2026-08-19  
**Status:** **STANDALONE MANUSCRIPT GO / GENERIC DETECTOR-PHYSICS CLAIM ONLY**

## Decision

Paper 03 has crossed the predeclared standalone-manuscript GO threshold.

The supported claim is intentionally narrow:

> Ordinary multidimensional detector physics can generate an order-one spectral/RF signature that would support a false homogeneous microscopic transport interpretation, while a calibrated-kernel model-inadequacy hierarchy can reject that interpretation at lower measurement precision than the false parameter claim requires.

This is a generic detector-physics/model-falsification result. It is **not** a material-specific HgCdTe claim and does not require the later bipolar HgCdTe instantiation to begin or freeze the generic manuscript.

## Predeclared GO criteria

The current `PUBLICATION_ROADMAP_CURRENT.md` requires all of the following:

```text
forward recovery and convergence;
blind-analysis boundary preserved;
broad ordinary regime supports a robust early-warning or hidden-confound result;
behavior survives a materially different geometry family;
actionable observable/SNR consequence;
focused prior-art review leaves a defensible contribution.
```

All six are now satisfied for the generic claim.

## 1. Broad first geometry family — PASS / Outcome A

The predeclared 60-point screen contained 180 RF rows.

```text
order-one RF rows = 42 / 180
analytic hidden-risk RF rows = 0 / 180
detector points with max mimic >= 0.5 = 14 / 60
```

Six mechanically selected points under S0--S7 were refined. All six retained at least one order-one confound and no refined analytic hidden-risk row appeared.

The nominal S0 point and the two mechanically selected adversarial points (`R1_B04` maximum confound and `R2_A04` warning-boundary point) were then tested with the locked parametric-bootstrap convention. All nine RF comparisons supported early warning before the frozen false-transport claim threshold.

Smallest conservative tested warning margin anywhere among those nine comparisons:

```text
+9.16 dB
```

No threshold, ensemble size, SNR grid, seed convention, or pass rule was changed after seeing the results.

## 2. Materially different coplanar family — PASS / Outcome A

The second family uses two coplanar top electrodes, an insulating top gap, insulating bottom and sidewalls, and lateral/fringing field and weighting-field topology rather than the first family's selected-top/full-bottom geometry.

Its frozen numerical gate passed.

The calibrated-kernel two-mode diagnostic reduced the one-mode mismatch by approximately 45x--114x, while the fitted root sets were grid-stable and every RF violated the homogeneous scalar finite-boundary root-sum law.

The three locked statistical cells are now all valid:

| RF | lowest tested SNR with >=90% power | frozen false-claim SNR | conservative warning margin |
|---:|---:|---:|---:|
| 100 MHz | 43.238 dB | 96.1 dB | +52.862 dB |
| 500 MHz | 43.100 dB | 82.3 dB | +39.200 dB |
| 1 GHz | 36.146 dB | 76.7 dB | +40.554 dB |

The authoritative 500-MHz repair retained the original statistical experiment and changed only nonlinear optimizer acceleration. The final fast/full multistart residual-norm ratio was

```text
1.0000000000010196
```

well inside the unchanged `<=1.001` implementation-integrity criterion.

The prior failed optimizer attempts remain provenance and are not reclassified as scientific failures.

## 3. Generic self-consistent Stage B — PASS / B2-A

The Stage-B operating state solves coupled finite-volume Poisson plus Scharfetter--Gummel electron continuity with damped Gummel iteration, then uses a separately solved weighting potential and dilute small-signal transport through the converged state.

The refined mesh/weighting/reciprocity gate retained all original convergence thresholds. The accepted pair is

```text
51x39 -> 61x47.
```

On that pair:

```text
terminal-current relative change       = 0.0127287
potential-profile RMS scaled change    = 0.0028590
density-profile RMS / Nd               = 0.0025516
minimum-density relative change        = 0.0283586
weighting-profile RMS change           = 0.00179794
```

The unchanged minimum-density threshold was 0.05, so the previous coarse-mesh failure is genuinely resolved by refinement rather than by threshold relaxation.

Independent signal/operator checks at 500 MHz give

```text
forward/backward operator mismatch     = 1.1259e-16
boundary-rate decomposition error      = 6.3388e-16
DC committor/Ramo max error            = 3.6360e-15
backward linear residual               = 2.4347e-14
forward linear residual                = 2.5778e-14
reciprocity mismatch                   = 3.9432e-16
peak dilute-signal delta_n / Nd        = 1.0e-4
```

The final predeclared blind six-channel Stage-B gate then passed on independently converged spectral observables while withholding the self-consistent field, carrier density, contact labels, forward generator, true mobility/diffusion, and generating mechanism from the analyzer.

Predeclared Stage-B outcome:

```text
B2-A: order-one self-consistent confound self-announces before false-claim precision.
```

The analytic one-mode rejection thresholds and warning margins were

| RF | analytic rejection SNR | frozen false-claim SNR | analytic warning margin |
|---:|---:|---:|---:|
| 100 MHz | 11.708 dB | 96.1 dB | +84.392 dB |
| 500 MHz | 11.286 dB | 82.3 dB | +71.014 dB |
| 1 GHz | 10.741 dB | 76.7 dB | +65.959 dB |

These Stage-B margins are analytic validation coordinates, not replacements for the finite-sample bootstrap claims above.

The stable Stage-B two-root fits also reject the homogeneous scalar root-sum law at all three RFs and across every RF pair under the frozen numerical-separation rule.

## 4. Blind-analysis boundary — PASS

The final Stage-B blind analyzer received only

```text
six complex terminal currents;
RF coordinates;
cell-center depth coordinates;
actual calibrated discrete depth kernels;
frozen measurement-noise / false-claim comparison convention.
```

It did not receive hidden forward fields, carrier density, contact fraction/labels, true mobility or diffusion coefficient, forward generator, or generating-mechanism labels.

The successful result therefore does not depend on revealing the mechanism to the inverse.

## 5. Actionable measurement consequence — PASS

The paper's experimentally actionable object is the precision ordering itself:

```text
precision required to reject an inadequate low-dimensional transport interpretation
<
precision required to defend the corresponding false microscopic transport claim.
```

This ordering was demonstrated with finite-sample bootstrap tests in the broad first family and materially different coplanar family, and with an independent self-consistent Stage-B analytic validation.

The result therefore says more than "geometry matters": it provides a measurable warning-before-claim criterion.

## 6. Focused prior-art boundary — PASS under narrow framing

The audit found close established precedent for

```text
wavelength/absorption-depth dependent RF photodiode phase (optoelectronic chromatic dispersion);
nonuniform/arbitrary optical-generation profiles altering inferred small-signal transport;
frequency-domain transfer-function consistency/model diagnostics;
classical finite-exponential / Prony-Hankel model identification.
```

Those ingredients must not be claimed as new.

The defensible candidate contribution is narrower:

> a mechanism-blind calibrated spectral-kernel hierarchy that compares the precision at which neglected multidimensional detector physics becomes statistically rejectable with the precision at which a false homogeneous microscopic transport parameter would otherwise become claim-worthy, validated over a broad ordinary geometry family, a materially different topology, and a self-consistent semiconductor forward model.

Priority remains non-superlative. The manuscript must not claim first-ever wavelength-dependent timing, first-ever spectral-depth transport inference, first-ever model-consistency testing, or first-ever Hankel/Prony detector analysis.

## 7. Material-specific boundary

A material-specific HgCdTe instantiation remains future work.

The preliminary material ledger indicates that a low-doped `x ~ 0.30`, elevated-temperature HgCdTe operating point should not be forced into the generic electron-only Stage-B solver; a material claim would require a bipolar implementation and a closed parameter ledger.

That work is **not a blocker for the generic Paper-03 manuscript** because the final Stage-B predeclaration explicitly defines the generic self-consistent milestone separately and makes no HgCdTe material claim.

## 8. Standalone disposition

```text
broad first-family Outcome A                   PASS
selected-point finite-sample bootstrap          PASS
materially different coplanar numerical gate   PASS
coplanar root-law/model-order gate              PASS
coplanar 100/500/1000 MHz statistics            PASS
self-consistent Stage-B refined numerical gate PASS
Stage-B blind six-channel gate / B2-A          PASS
blind-information boundary                      PASS
focused prior-art boundary                      PASS under narrow framing
actionable SNR consequence                      PASS
```

Therefore:

```text
Paper 03 standalone GO = TRUE
generic science interpretation ready for manuscript drafting = TRUE
HgCdTe-specific material claim ready = FALSE
```

## 9. Execution rule after GO

Stop expanding the generic Paper-03 research domain merely to accumulate more tests.

Next work is manuscript production:

```text
1. freeze the evidence table and exact claim boundary;
2. draft anonymous Paper-03 Rev. 1;
3. generate only figures that directly support the claim;
4. run an adversarial manuscript review against the frozen research record;
5. repair material defects only;
6. compile and package a manuscript candidate;
7. then merge the Paper-03 research/manuscript branch after CI and preservation checks.
```

New HgCdTe bipolar work belongs to a separate material-validation extension unless the manuscript review exposes a genuine dependence on it.
