# Paper 03 Stage-A refined selected-regime result

**Date:** 2026-08-17  
**Status:** **CHECKED PREDECLARED REFINEMENT RESULT / NON-CLAIM**

## Provenance

The six unique detector points were selected mechanically from the complete 60-point screen by `PAPER03_STAGEA_REGIME_MAP_PREDECLARATION_2026-08-17.md` and frozen in `PAPER03_STAGEA_REGIME_SELECTION_MANIFEST_2026-08-17.json` before refinement.

Authoritative execution-only refinement-shard run:

```text
run = 32067273524
head = d90483621234fbb107566052778e46d7023fade2
jobs = 6/6 successful
```

Each point was independently recomputed at

```text
161 x 121
201 x 151
17-point lateral quadrature
six calibrated optical kernels
```

with the unchanged numerical readiness rule

```text
201-vs-161 historical raw-phase change <= 2% of the frozen transport target
at 100 MHz, 500 MHz, and 1 GHz.
```

All solver residual, committor, and applicable DC Ramo checks also retained their existing `<1e-8` gates.

## Refinement summary

| Manifest | Predeclared role | Refined max mimic | Minimum analytic warning margin | Worst phase refinement / target | Refined order-one row? | Refined analytic hidden-risk row? |
|---|---|---:|---:|---:|---|---|
| R0_A21 | S0 nominal anchor | 0.875109 | +10.8076 dB | 1.1780% | yes | no |
| R1_B04 | S1 maximum confound; S6 optical-offset stress | 1.685018 | +20.0104 dB | 1.0170% | yes | no |
| R2_A04 | S2 worst warning; S3 closest warning boundary | 0.849562 | +19.0421 dB | 0.3170% | yes | no |
| R3_A07 | S4 strongest early warning | 1.607157 | +20.2074 dB | 0.9488% | yes | no |
| R4_B03 | S5 largest calibrated one-mode mismatch | 2.082612 | +19.5316 dB | 0.9107% | yes | no |
| R5_A03 | S7 weakest still-order-one confound | 0.840804 | +19.2589 dB | 0.3337% | yes | no |

Thus

```text
selected points = 6
numerically passed = 6
selected points retaining >=1 order-one row = 6
selected points retaining analytic hidden-risk row = 0
```

The strongest refined confound in the selected set is `R4_B03`, reaching approximately `2.083 x` the frozen transport target. This does not by itself make `R4_B03` a bootstrap point because bootstrap selection was fixed before refinement output was interpreted.

## Refined RF rows

### R0_A21 — nominal anchor

| RF | mimic fraction | rho1 all-six | analytic warning margin |
|---:|---:|---:|---:|
| 100 MHz | 0.728 | 2.35e-4 | +19.55 dB |
| 500 MHz | 0.774 | 3.49e-4 | +9.16 dB |
| 1 GHz | 0.875 | 6.42e-4 | +10.81 dB |

The already completed nominal bootstrap remains authoritative for S0.

### R1_B04 — S1/S6 maximum-confound optical-offset stress

| RF | mimic fraction | rho1 all-six | analytic warning margin |
|---:|---:|---:|---:|
| 100 MHz | 1.491 | 1.255e-3 | +34.20 dB |
| 500 MHz | 0.271 | 1.602e-3 | +24.38 dB |
| 1 GHz | 1.685 | 1.869e-3 | +20.01 dB |

### R2_A04 — S2/S3 warning-boundary point

| RF | mimic fraction | rho1 all-six | analytic warning margin |
|---:|---:|---:|---:|
| 100 MHz | 0.202 | 1.203e-3 | +35.74 dB |
| 500 MHz | 0.103 | 1.361e-3 | +22.99 dB |
| 1 GHz | 0.850 | 1.659e-3 | +19.04 dB |

### R3_A07 — S4 strongest-early-warning point

| RF | mimic fraction | rho1 all-six | analytic warning margin |
|---:|---:|---:|---:|
| 100 MHz | 1.607 | 1.227e-3 | +35.91 dB |
| 500 MHz | 0.415 | 1.635e-3 | +24.56 dB |
| 1 GHz | 1.509 | 1.911e-3 | +20.21 dB |

### R4_B03 — S5 largest calibrated one-mode mismatch

| RF | mimic fraction | rho1 all-six | analytic warning margin |
|---:|---:|---:|---:|
| 100 MHz | 2.083 | 9.872e-4 | +34.02 dB |
| 500 MHz | 0.965 | 1.441e-3 | +23.46 dB |
| 1 GHz | 1.035 | 1.768e-3 | +19.53 dB |

### R5_A03 — S7 weakest still-order-one confound

| RF | mimic fraction | rho1 all-six | analytic warning margin |
|---:|---:|---:|---:|
| 100 MHz | 0.288 | 1.201e-3 | +35.73 dB |
| 500 MHz | 0.040 | 1.375e-3 | +23.08 dB |
| 1 GHz | 0.841 | 1.701e-3 | +19.26 dB |

## Predeclared bootstrap consequence

Section 12 of the regime-map predeclaration mechanically selects only:

```text
R2_A04  <- S2; S3 is identical and deduplicated
R1_B04  <- distinct S1 with refined max mimic > 1
```

The nominal `R0_A21` bootstrap is reused. No S4/S5/S7 point is promoted after seeing refinement output.

The exact selected-point execution is separately locked in `PAPER03_STAGEA_SELECTED_BOOTSTRAP_EXECUTION_LOCK_2026-08-17.md` before any selected-point bootstrap result is read.

## Interpretation boundary

The refined screen removes the principal numerical concern from the selected extremes and provides broad evidence that order-one geometric confounds are not restricted to the nominal detector coordinate. It does **not** yet establish broad Outcome A because the selected S1/S2 boundary/worst cases still require the predeclared nonlinear bootstrap calibration.

```text
broad refined Stage-A geometry/transport evidence = favorable
broad Outcome A = pending selected-point bootstrap
Stage B self-consistent semiconductor validation = pending
second geometry family = predeclared, unevaluated
focused prior-art audit = pending
science_interpretation_ready = false
Paper 03 standalone GO = false
```
