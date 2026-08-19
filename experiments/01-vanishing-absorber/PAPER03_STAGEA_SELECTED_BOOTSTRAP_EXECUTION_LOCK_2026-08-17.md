# Paper 03 Stage-A selected-point bootstrap execution lock

**Date:** 2026-08-17  
**Status:** **LOCKED AFTER PREDECLARED REFINEMENT / BEFORE SELECTED-POINT BOOTSTRAP OUTPUT / NON-CLAIM**

## Purpose

This file instantiates Section 12 of `PAPER03_STAGEA_REGIME_MAP_PREDECLARATION_2026-08-17.md` after the six predeclared selected points completed the unchanged 161x121 -> 201x151 refinement gate.

Authoritative refinement-shard run:

```text
run = 32067273524
head = d90483621234fbb107566052778e46d7023fade2
six of six selected points passed the unchanged <=2%-of-frozen-target phase-refinement criterion
```

No bootstrap result from the selected points has been read at the time this lock is committed.

## Mechanically selected new bootstrap points

The committed Section-12 rule gives exactly two new detector coordinates.

### R2_A04 — S2/S3 boundary point

```text
selection reasons:
  S2_worst_warning_margin_order_one
  S3_closest_analytic_warning_boundary

contact fraction = 0.50
Wd = 0.0 um
Vsc = 0.000 V
D = 2.5e-3 m^2/s
tau = infinity
beam sigma = 2.0 um
beam center = 0.0 um
```

Its refined calculation contains an order-one row, so S2 requires bootstrap. S3 is the same detector point and is therefore deduplicated.

### R1_B04 — S1/S6 maximum-confound point

```text
selection reasons:
  S1_maximum_confound
  S6_optical_offset_stress

contact fraction = 0.50
Wd = 3.0 um
Vsc = 0.050 V
D = 2.5e-3 m^2/s
tau = infinity
beam sigma = 1.0 um
beam center = 1.5 um
```

Its refined maximum mimic fraction exceeds 1.0, so the distinct S1 rule requires bootstrap.

The already completed nominal S0 bootstrap is reused unchanged. No S4, S5, or S7 point is promoted to a predeclared bootstrap coordinate.

## Statistical contract reused without modification

The selected-point execution imports the already checked `paper03_stageA_statistical_bootstrap.rf_gate()` implementation directly. Therefore the following remain unchanged:

```text
alpha = 0.002699796063260207
target power = 0.90
N_null = 4000 per SNR candidate
N_alt = 2000 per SNR candidate
SNR offsets = analytic threshold + {-4,-2,0,+2,+4} dB
empirical null quantile method = higher
noise = sigma*(xi_R + i xi_I), with iid unit-normal quadratures
SNR_dB = 20 log10(mean adjacent deterministic current step / sigma)
nonlinear one-mode null is refit for every realization
fast bounded refit is spot-checked against the full multistart fitter
```

The existing deterministic seed schedule inside `rf_gate()` is also reused verbatim. This intentionally supplies common random numbers across the selected detector points; it is an execution choice for reproducibility and does not change the statistical threshold or sample count.

## Forward calculation

For each selected point and each RF in

```text
100 MHz
500 MHz
1 GHz
```

the forward current is recomputed independently on

```text
201 x 151 spatial grid
17-point lateral source quadrature
six calibrated optical kernels
```

using the same Stage-A fixed-field backward resolvent and selected-point beam integration used by the accepted refinement calculation.

## Decision rule

For each RF retain the existing definition

```text
predeclared early warning supported
  iff the lowest tested SNR with empirical power >= 0.90
  is <= the frozen transport-claim SNR.
```

No interpolation between the five fixed SNR candidates is used to manufacture a pass.

For broad Stage-A Outcome-A evidence, the selected boundary/worst points must preserve positive **tested** warning margin after bootstrap calibration. A failure is retained as a failure and is not repaired by changing the SNR grid, alpha, power target, sample counts, or noise convention.

## Claim boundary

```text
Stage A fixed-field only
selected-point bootstrap output not yet known
science_interpretation_ready = false
Paper 03 standalone GO = false
```
