# Paper 03 Stage-A Cross-Formulation Check — Predeclaration

**Date:** 2026-08-17  
**Status:** **PREDECLARED / NON-CLAIM**

## 1. Purpose

The brute-force stochastic solver is too noisy to estimate the final nonlinear four-color closure efficiently, while the deterministic backward resolvent passes a stringent grid gate. The two formulations nevertheless represent the same declared fixed-field stopped diffusion process and should agree on coarse observables that Monte Carlo can resolve directly.

This check is deliberately independent of the statistical bootstrap and does not use the kernel-aware closure residual as its comparison quantity.

## 2. Locked physical coordinate

```text
scenario = finite75_depletion
D = 2.5e-3 m^2/s
tau = infinity
selected top contact = absorbing
bottom contact = absorbing
uncontacted top = reflecting
sidewalls = reflecting
```

The continuous stochastic calculation uses the existing Euler--Maruyama path implementation with exact discrete Shockley--Ramo weighting-potential increments.

The deterministic calculation uses the exponentially fitted nearest-neighbor backward Markov generator and the resolvent

```math
(i\omega-L_h)H=L_h\phi_w.
```

## 3. Source points

The following points are fixed before the comparison is run:

```text
(x,z) um = (0.0,2.5)
           (0.0,4.0)
           (2.0,3.0)
           (-2.0,3.0)
           (5.0,3.0)
```

The last point deliberately approaches the finite-contact edge while remaining beneath the selected contact.

## 4. Monte-Carlo discretization and sample count

Per source point:

```text
N paths = 4000
trajectory drift step = 0.020 um
maximum requested diffusion RMS step = 0.040 um
maximum time = 5 ns
fixed independent random seed per source point
```

No particle count is increased after seeing a disagreement and then described as predeclared.

## 5. Deterministic comparison grids

Evaluate the resolvent on

```text
121 x 91
201 x 151
```

grids. The fine result is the deterministic comparison value. The absolute coarse-to-fine difference at each observable is retained as a conservative deterministic discretization allowance.

## 6. Compared observables

At each source point compare:

1. selected-contact hitting probability `p_selected`;
2. dc selected-electrode Shockley--Ramo response `H(0)`;
3. real and imaginary parts of `H(100 MHz)`;
4. real and imaginary parts of `H(500 MHz)`;
5. real and imaginary parts of `H(1 GHz)`.

Monte-Carlo standard errors are computed directly from the path ensemble for each scalar observable.

No nonlinear closure, fitted spatial root, or mechanism label enters this check.

## 7. Acceptance coordinate

For scalar observable `q`, define

```math
Delta=|q_MC-q_fine|,
```

```math
A=4 SE_MC+|q_fine-q_coarse|.
```

The individual comparison passes when

```math
Delta <= A.
```

The factor `4` is fixed before execution. It is a numerical cross-formulation tolerance, not an experimental confidence statement.

The overall cross-formulation check passes only if every declared scalar observable at every declared source point passes.

## 8. Additional invariants

The stochastic calculation must also report:

```text
maximum pathwise dc endpoint-Ramo error;
terminal-fate counts;
time/step-limit counts.
```

Any nonzero unresolved `step_limit` or `time_limit` fraction above `1e-3` at a source point is a validation warning and prevents overall PASS, regardless of observable agreement.

## 9. Interpretation boundary

A PASS establishes only that two numerically independent formulations agree on coarse observables at five source points within the declared Monte-Carlo/discretization tolerance.

It does not validate the final nonlinear closure statistic by Monte Carlo, does not establish self-consistent semiconductor physics, and does not make Paper 03 publication-ready.

A FAIL is to be investigated as a numerical/formulation discrepancy; the tolerance is not to be loosened merely to obtain agreement.