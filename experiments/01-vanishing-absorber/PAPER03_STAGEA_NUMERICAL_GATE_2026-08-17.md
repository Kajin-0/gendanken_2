# Paper 03 Stage-A Numerical Gate — Particle Sampling

**Date:** 2026-08-17  
**Status:** **CHECKED NUMERICAL RESULT / NON-CLAIM**  
**Decision:** brute-force Monte Carlo is retained as an independent stochastic cross-check but rejected as the production solver for the small closure observable.

## 1. Provenance

Workflow:

```text
Paper 03 Stage A particle convergence
```

Authoritative pull-request run:

```text
run  = 32061188941
job  = 95482613674
head = 463d85c8f58e5cba9625e0228c18b52e865650b3
```

Artifact:

```text
name   = paper03-stageA-particle-convergence
id     = 9298420109
digest = sha256:d7192ad18d8b2e23bf2bf1f4505b3f683877a96ea7e176bffcbaf5d2f95bf320
```

The workflow completed the numerical sweep, non-claim assertion, DC-invariant check, and artifact upload successfully.

Forward coordinate:

```text
scenario = finite75_depletion
D        = 2.5e-3 m^2/s
tau      = infinity
field grid = 81 x 61
lateral source quadrature = 5
source-depth transfer grid = 17
trajectory drift step = 0.05 um
maximum requested diffusion RMS step = 0.08 um
```

Two independent random seeds were used at each particle count.

---

## 2. Predeclared particle precision gate

Before reading the convergence result, the initial readiness coordinate was fixed as

> independent-replica four-color phase half-spread no larger than 5% of the frozen reference transport phase at every nonzero RF.

This is a numerical readiness coordinate, not a physical significance threshold.

Frozen comparison phases:

```text
100 MHz -> |target| = 0.011978 deg
500 MHz -> |target| = 0.058727 deg
1 GHz   -> |target| = 0.110405 deg
```

---

## 3. Result

| particles/source | first-difference replica disagreement | worst phase half-spread / frozen target | initial 5% gate |
|---:|---:|---:|---:|
| 24  | 1.9496e-2 | 7.6528 | FAIL |
| 96  | 2.3409e-2 | 16.7994 | FAIL |
| 384 | 9.4308e-3 | 7.7625 | FAIL |

The first-difference replica disagreement did not decrease monotonically over this three-point seed comparison. A log-log fit across the three particle counts gave

```text
observed slope = -0.26193
independent-sampling reference slope = -0.5
```

The fit is only a compact diagnostic across three noisy points; it is not a new asymptotic theorem. Its significance here is practical: the present brute-force calculation is nowhere near the precision required for the phase observable.

### N = 384 phase replica disagreement

| RF | replica A phase | replica B phase | half-spread | half-spread / frozen target |
|---:|---:|---:|---:|---:|
| 100 MHz | +0.027311 deg | -0.158646 deg | 0.092979 deg | 7.7625 |
| 500 MHz | +0.117884 deg | -0.775499 deg | 0.446692 deg | 7.6062 |
| 1 GHz | +0.137267 deg | -1.448918 deg | 0.793092 deg | 7.1835 |

Thus even at the largest tested ensemble the independent-replica uncertainty in the raw four-color phase is several times larger than the entire frozen transport target, whereas the predeclared readiness requirement was 0.05 times the target.

These phase values therefore **must not** be interpreted as detector physics.

---

## 4. Strong invariant that did pass

Across the stochastic paths, the maximum discrete endpoint Shockley--Ramo consistency error remained

```text
1.1102230246251565e-16
```

for the particle-convergence runs.

The earlier smoke run also showed physically sensible explicit path fates: diffusion allowed a small fraction of trajectories to reach the bottom contact, and adding finite recombination produced selected-contact, bottom-contact, and recombined fates without forcing every path to selected-contact unit collection.

Therefore the failure is not an endpoint-Ramo bookkeeping failure. It is a precision/variance problem in estimating a small nonlinear spectral phase from a finite stochastic ensemble.

---

## 5. Decision

Do **not** respond by weakening the 5% gate or by reporting the mean Monte-Carlo closure phase as a physical result.

Instead:

```text
brute-force stochastic path solver
-> retain as independent validation / distributional cross-check
-> not the production estimator of the small closure signal
```

The Stage-A production route is now a deterministic backward-resolvent formulation of the same fixed-field stopped diffusion/recombination problem:

```math
(\kappa+i\omega-L)H=L\phi_w,
```

with absorbing selected/bottom contacts and reflecting side/uncontacted-top boundaries.

A positive exponentially fitted nearest-neighbour Markov generator is used so the discrete source is exactly `L_h phi_w`. At dc and infinite lifetime this gives the internal algebraic check

```math
H(0)=p_{selected}-\phi_w,
```

where `p_selected` is the selected-contact committor under the same discrete generator.

Implementation:

```text
numerics/paper03_stageA_resolvent.py
```

The deterministic solver is a second numerical formulation, not a reinterpretation of the failed particle gate.

---

## 6. Remaining Stage-A numerical gates

Before any combined-physics scientific interpretation:

1. run the deterministic resolvent on a declared grid sequence;
2. require sparse-solver and dc committor/Ramo invariants;
3. test deterministic grid convergence against a predeclared phase-scale tolerance;
4. compare deterministic currents against stochastic sampling at a precision the Monte-Carlo calculation can actually resolve, rather than requiring Monte Carlo to resolve the final tiny closure phase directly;
5. implement the calibrated arbitrary-kernel blind consistency inverse rather than treating the inherited raw geometric closure/root diagnostics as the final Paper-01 test;
6. keep `science_interpretation_ready = false` until these numerical gates and the separately required Stage-B self-consistent semiconductor forward-model validation are complete.

No Paper 03 physics claim is made by this record.