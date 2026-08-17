# Paper 03 Stage-A Cross-Formulation Result

**Date:** 2026-08-17  
**Status:** **CHECKED NUMERICAL CROSS-FORMULATION RESULT / FORMAL PREDECLARED FAIL / NON-CLAIM**

## 1. Authoritative workflow

```text
workflow = Paper 03 Stage A cross-formulation check
run      = 32064250152
job      = 95492401382
head     = ee118e65fdc7439386fa4b5fe2c7ca251cae8be6
conclusion = success
```

The green workflow conclusion means the calculation executed and the artifact was preserved. The workflow intentionally did **not** assert that the scientific comparison had to pass.

Artifact:

```text
name   = paper03-stageA-cross-formulation
id     = 9299505079
digest = sha256:608b0feacef2484e082fdb127c6e8aaa34c223756ca138172d06282747d9fac6
```

The comparison used the exact predeclared five source points, 4000 stochastic paths per point, fixed seeds, `D=2.5e-3 m^2/s`, infinite lifetime, `0.020 um` drift step, `0.040 um` maximum requested diffusion RMS step, and 121x91 / 201x151 deterministic grids.

---

## 2. Predeclared acceptance rule

For every scalar observable,

```math
\Delta=|q_{MC}-q_{fine}|,
```

```math
A=4SE_{MC}+|q_{fine}-q_{coarse}|,
```

and the scalar comparison was declared passing only if

```math
\Delta\le A.
```

The overall check was declared passing only if every scalar comparison and unresolved-fate gate passed.

That rule is retained exactly. It is not modified after inspecting the artifact.

---

## 3. Formal result

```text
scalar observables tested = 40
scalar observables passed = 36
source points with every scalar check passed = 1 / 5
maximum endpoint-Ramo error = 1.1102230246251565e-16
maximum unresolved fate fraction = 0
formal overall predeclared pass = FALSE
```

Therefore this file records a **formal predeclared FAIL**.

---

## 4. Location of every failure

All four failed scalar checks are the same observable:

```text
p_selected
```

at four source points.

Every stochastic path at every one of the five source points reached the selected contact:

```text
4000 / 4000 selected-contact fates at each point
0 bottom-contact fates
0 time-limit fates
0 step-limit fates
```

Consequently the empirical Bernoulli sample standard deviation and standard error of `p_selected` are exactly zero.

The deterministic fine-grid selected-contact probabilities at the failed points were nevertheless

```text
(x,z)=(0.0,2.5) um -> 0.999999999992145
(2.0,3.0) um       -> 0.999999999999940
(-2.0,3.0) um      -> 0.999999999999939
(5.0,3.0) um       -> 0.999999999999630
```

so the largest absolute stochastic-versus-fine discrepancy is only approximately

```text
7.86e-12.
```

Because the Monte-Carlo `SE` is exactly zero and the coarse-to-fine deterministic change is even smaller, the literal predeclared formula produces an almost-zero allowance and formally rejects these saturated probability comparisons.

This is a defect in the suitability of the **predeclared probability acceptance statistic at a boundary value**, not evidence of an order-one disagreement between the two physical formulations.

That diagnosis does not retroactively convert the gate to PASS.

---

## 5. Shockley--Ramo signal comparisons

The important independent signal comparison is substantially cleaner.

Each point contains seven direct response checks:

```text
H(0) real;
Re/Im H(100 MHz);
Re/Im H(500 MHz);
Re/Im H(1 GHz).
```

Across five points this gives

```text
35 Shockley--Ramo scalar response comparisons.
```

All **35 / 35 passed** the predeclared tolerance.

The worst signal comparison was

```text
source = (-2.0,3.0) um
observable = Im H(100 MHz)
MC mean = -0.0322076346
MC standard error = 1.25162e-4
121x91 deterministic = -0.0326034113
201x151 deterministic = -0.0325585566
|MC-fine| = 3.50922e-4
allowance = 5.45504e-4
|MC-fine| / allowance = 0.6433
```

Thus even the worst direct signal component remains comfortably inside the frozen cross-formulation tolerance.

The pathwise endpoint-Ramo identity simultaneously remains at machine precision (`1.11e-16`).

---

## 6. What can be concluded

The strict result is:

```text
formal overall predeclared cross-formulation gate -> FAIL
```

because the saturated selected-contact probability made the empirical-SE acceptance rule degenerate.

Separately, the actual signal comparison establishes:

```text
35/35 declared direct Shockley--Ramo coarse observables
agree between the continuous stochastic path formulation
and the deterministic backward resolvent within the
predeclared 4-SE + coarse/fine allowance.
```

This substantially supports the deterministic resolvent as an independent representation of the Stage-A signal process, while preserving the failure of the probability sub-gate exactly as observed.

It does **not** validate the final tiny nonlinear closure statistic by Monte Carlo.

---

## 7. Post-gate treatment of the saturated probability issue

Do not fix the failed gate by adding an arbitrary absolute tolerance after the fact.

If a selected-contact probability cross-check is scientifically needed, run a separately labeled post-gate test using source points chosen to produce a genuinely nondegenerate terminal-fate probability and a binomial interval or exact Bernoulli-tail treatment specified **before** that new execution.

There is no reason to spend additional particles estimating `1-p_selected` at the present points: `4000/4000` successes cannot resolve a failure probability of order `1e-11` implied by the fine deterministic solve.

---

## 8. Remaining boundary

`science_interpretation_ready` remains false.

The immediate primary gate remains the predeclared six-channel nonlinear statistical bootstrap. Beyond that, Paper 03 still requires a broad regime map, a materially different second geometry family, and Stage-B self-consistent semiconductor validation.