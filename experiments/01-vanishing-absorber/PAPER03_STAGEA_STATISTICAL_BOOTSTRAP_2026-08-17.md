# Paper 03 Stage-A Statistical Bootstrap Result

**Date:** 2026-08-17  
**Status:** **CHECKED PREDECLARED STATISTICAL RESULT / NON-CLAIM**  
**Decision:** at the tested finite75 + depletion Stage-A coordinate, the calibrated-kernel one-mode mismatch is statistically rejectable at lower raw-current step-amplitude SNR than the frozen transport-claim requirement at 100 MHz, 500 MHz, and 1 GHz. This supports candidate Outcome A for this tested geometry only.

## 1. Predeclaration lock

The complete statistical contract was committed before the bootstrap result was read:

```text
PAPER03_STAGEA_STATISTICAL_PREDECLARATION_2026-08-17.md
```

Locked forward coordinate:

```text
scenario = finite75_depletion
D = 2.5e-3 m^2/s
tau = infinity
spatial grid = 201 x 151
lateral source quadrature = 17
six calibrated HgCdTe optical kernels
```

Locked null model at each RF:

```math
J_m=A+B M_m(r),
```

with

```math
M_m(r)=\int g_m(z)e^{rz}\,dz.
```

Six complex channels minus complex `A,B,r` give the regular local residual dimension

```text
nu = 6 real degrees of freedom.
```

Locked noise convention:

```math
n_m=\sigma(\xi_{m,R}+i\xi_{m,I}),
```

where every real and imaginary quadrature is an independent standard normal variate scaled by the same `sigma`.

Define

```math
s_J=\operatorname{mean}_m |J_{m+1}-J_m|,
```

and

```math
SNR_{dB}=20\log_{10}(s_J/\sigma).
```

Thus `sigma` is the standard deviation of **each current quadrature**. A complex-RMS convention differs by `sqrt(2)` / approximately `3.01 dB`; that convention change is not silently applied here.

Locked statistical coordinates:

```text
alpha = 0.002699796063260207
power target = 0.90
N_null = 4000 per SNR candidate
N_alt  = 2000 per SNR candidate
SNR candidates = analytic threshold + {-4,-2,0,+2,+4} dB
empirical null quantile = method='higher'
```

Every noisy realization is nonlinearly refit to the calibrated-kernel one-mode model. The fast bounded refit is spot-checked against the full multistart fitter.

Frozen current-step transport-claim comparison coordinates:

```text
100 MHz -> 96.1 dB
500 MHz -> 82.3 dB
1 GHz   -> 76.7 dB
```

No alpha, power target, sample count, SNR grid, refit rule, detector coordinate, or pass rule was changed after seeing the bootstrap output.

---

## 2. Authoritative execution

The original serial implementation was computationally expensive. The identical RF gate was therefore executed as three parallel CI shards. This changed execution scheduling only: each shard calls the same `paper03_stageA_statistical_bootstrap.rf_gate()` scientific code with the same fixed seeds, samples, SNR candidates, forward model, and refit.

Authoritative sharded workflow:

```text
workflow = Paper 03 Stage A statistical bootstrap RF shards
run      = 32065068757
head     = ff3be81c695ab872607441b206adc0db47a2bba9
conclusion = success
```

Jobs:

```text
100 MHz -> 95495075570 -> success
500 MHz -> 95495075542 -> success
1 GHz   -> 95495075684 -> success
```

Artifacts:

```text
100 MHz
name   = paper03-stageA-statistical-bootstrap-100MHz
id     = 9299852113
digest = sha256:0f9bbcdf8c238582c4e2e227cf9bde54142ac2f782f5c00465765cbede870b9d

500 MHz
name   = paper03-stageA-statistical-bootstrap-500MHz
id     = 9299791814
digest = sha256:9ea434a1a7b5ac85687a8f5dc43d7c9d6cf05a6fb43de61afe5273801db021e9

1 GHz
name   = paper03-stageA-statistical-bootstrap-1GHz
id     = 9299883661
digest = sha256:b06baed14e0dab9c8c34bc24b8c5361a3b6d662c2394c08d226d8ef4f55fd484
```

---

## 3. 100-MHz result

Analytic local regular approximation:

```text
required SNR = 74.5450781 dB
```

Predeclared candidate results:

| SNR (dB) | empirical power | power MC SE | decision against 0.90 |
|---:|---:|---:|---|
| 70.5451 | 0.3140 | 0.01038 | fail |
| 72.5451 | 0.6080 | 0.01092 | fail |
| 74.5451 | **0.8945** | 0.00687 | **fail** |
| 76.5451 | **0.9965** | 0.00132 | **pass** |
| 78.5451 | 1.0000 | 0 | pass |

The analytic point is not rounded into a pass: `0.8945 < 0.90`.

Lowest tested passing SNR:

```text
76.5450781 dB
```

Frozen transport-claim SNR:

```text
96.1 dB
```

Conservative tested early-warning margin:

```text
96.1 - 76.5450781 = 19.5549219 dB.
```

Predeclared early-warning condition: **SUPPORTED**.

---

## 4. 500-MHz result

Analytic local regular approximation:

```text
required SNR = 71.1365156 dB
```

Predeclared candidate results:

| SNR (dB) | empirical power | decision against 0.90 |
|---:|---:|---|
| 67.1365 | 0.3145 | fail |
| 69.1365 | 0.5735 | fail |
| 71.1365 | **0.8985** | **fail** |
| 73.1365 | **0.9960** | **pass** |
| 75.1365 | 1.0000 | pass |

Again, the analytic point is retained as a fail because `0.8985 < 0.90`.

Lowest tested passing SNR:

```text
73.1365156 dB
```

Frozen transport-claim SNR:

```text
82.3 dB
```

Conservative tested early-warning margin:

```text
82.3 - 73.1365156 = 9.1634844 dB.
```

Predeclared early-warning condition: **SUPPORTED**.

---

## 5. 1-GHz result

Analytic local regular approximation:

```text
required SNR = 65.8923604 dB
```

Predeclared candidate results:

| SNR (dB) | empirical power | power MC SE | decision against 0.90 |
|---:|---:|---:|---|
| 61.8924 | 0.2590 | 0.00980 | fail |
| 63.8924 | 0.6635 | 0.01057 | fail |
| 65.8924 | **0.9000** | **0.00671** | **pass by locked >=0.90 rule** |
| 67.8924 | **0.9975** | 0.00112 | pass |
| 69.8924 | 1.0000 | 0 | pass |

The primary predeclared rule was `power >= 0.90`, so the 65.8924-dB point counts as the lowest tested pass. Its finite-bootstrap proximity to the boundary is retained explicitly rather than hidden.

Lowest tested passing SNR under the locked rule:

```text
65.8923604 dB
```

Frozen transport-claim SNR:

```text
76.7 dB
```

Primary conservative tested warning margin:

```text
76.7 - 65.8923604 = 10.8076396 dB.
```

For a visibly stronger finite-bootstrap power margin, the next **already predeclared** tested point gives

```text
67.8923604 dB -> power 0.9975,
```

which remains

```text
76.7 - 67.8923604 = 8.8076396 dB
```

below the frozen transport-claim requirement. This second number is a robustness observation, not a redefinition of the primary pass rule.

Predeclared early-warning condition: **SUPPORTED**.

---

## 6. Nonlinear refit integrity

At the analytic SNR coordinate, the fast local bootstrap refit was compared against the full multistart kernel fitter on fixed subsets.

Maximum fast/full residual-norm ratios were approximately

```text
100 MHz: null 1.000000000122; alternative 1.000000000070
500 MHz: null 1.000000000061; alternative 1.000000000007
1 GHz:   null 1.000000000145; alternative 1.000000000002
```

Thus the computationally efficient bootstrap refit does not produce a material residual inflation relative to the full multistart implementation in the tested high-SNR regime.

---

## 7. Analytic versus bootstrap calibration

The local regular noncentral-chi-square approximation was useful but slightly optimistic at 100 and 500 MHz:

```text
100 MHz analytic-threshold power -> 0.8945
500 MHz analytic-threshold power -> 0.8985
1 GHz   analytic-threshold power -> 0.9000
```

The empirical null critical values remained close to the regular chi-square reference, and the empirical null exceedance around the analytic critical value stayed of the same order as the declared false-alarm probability.

The practical conclusion is not that the analytic approximation failed. It is that the bootstrap was justified: a few tenths of a percent in power matter when the predeclared boundary is exactly 0.90.

---

## 8. Combined Stage-A hierarchy at the nominal geometry

For the tested finite75 + depletion coordinate with `D=2.5e-3 m^2/s` and infinite lifetime:

```text
same-physics finite-minus-planar raw phase
-> 0.728, 0.774, 0.875 x frozen transport target

calibrated-kernel one-mode model
-> numerically resolved failure

calibrated-kernel two-mode diagnostic
-> residual reduced by ~100x--273x to approximately planar floor
-> fitted root set stable under grid refinement

homogeneous scalar root law
-> fails strongly across RF

predeclared nonlinear bootstrap
-> one-mode failure detectable before transport-claim SNR
   at 100 MHz, 500 MHz, and 1 GHz
```

Conservative tested warning margins are therefore

```text
100 MHz -> 19.55 dB
500 MHz ->  9.16 dB
1 GHz   -> 10.81 dB under the locked >=0.90 rule
```

This is the strongest current evidence for candidate **Outcome A: geometry self-announces**.

---

## 9. What this result does not establish

Do **not** promote Paper 03 to standalone-GO from this single geometry coordinate.

Still open:

```text
broad physically ordinary geometry/diffusion/lifetime regime map;
a materially different second geometry family;
Stage-B self-consistent semiconductor operating-state validation;
focused primary-source prior-art audit;
robust treatment of the formally failed saturated-probability sub-gate in the stochastic cross-formulation test, if that probability observable is needed.
```

The independent cross-formulation result should be stated accurately:

```text
35/35 direct Shockley--Ramo response components passed the frozen stochastic/resolvent tolerance;
formal overall cross-formulation gate failed because four saturated p_selected checks had empirical Bernoulli SE=0.
```

The failed predeclared probability sub-gate is preserved as a failure and is not relabeled post hoc.

---

## 10. Current decision

For this Stage-A coordinate only:

```text
candidate Outcome A -> SUPPORTED
Paper 03 standalone GO -> NOT YET
science_interpretation_ready -> false
```

The next scientific step is a predeclared broad Stage-A regime map, using the deterministic resolvent and calibrated-kernel diagnostics for screening, with explicit rules for which points are refined and bootstrap-calibrated. A materially different second geometry family remains a separate mandatory gate.