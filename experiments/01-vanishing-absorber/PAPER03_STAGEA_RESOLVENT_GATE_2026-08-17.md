# Paper 03 Stage-A Numerical Gate — Deterministic Backward Resolvent

**Date:** 2026-08-17  
**Status:** **CHECKED NUMERICAL FORMULATION / NON-CLAIM**  
**Decision:** the deterministic backward resolvent is the preferred Stage-A production formulation for small spectral closure observables; brute-force Monte Carlo remains an independent stochastic cross-check.

## 1. Why the formulation was added

The brute-force particle calculation preserved the endpoint Shockley--Ramo identity but failed its predeclared precision gate by orders of magnitude in the nonlinear four-color phase statistic. The fixed-field Stage-A problem nevertheless admits a deterministic backward formulation.

For

```math
dX=v(X)dt+\sqrt{2D}\,dW
```

with independent recombination/killing rate `kappa=1/tau`, the expected selected-electrode response is represented by

```math
(\kappa+i\omega-L)H=L\phi_w,
```

with zero future response on absorbing electrical contacts and reflection on the sidewalls/uncontacted top surface.

Implementation:

```text
numerics/paper03_stageA_resolvent.py
```

The spatial operator is a positive exponentially fitted nearest-neighbor Markov generator. The discrete Ramo source is constructed as `L_h phi_w` using the same jump rates. At dc and infinite lifetime, the implementation therefore has the algebraic committor identity

```math
H(0)=p_{selected}-\phi_w.
```

This is an implementation invariant, not a detector-physics result.

---

## 2. Quick grid gate

Authoritative run:

```text
workflow = Paper 03 Stage A deterministic resolvent
run      = 32062095926
job      = 95485459977
head     = e63edebcf795175b593909f718261c1477f807e9
```

Artifact:

```text
name   = paper03-stageA-resolvent-grid-gate
id     = 9298498677
digest = sha256:14ad44c5cccd130bf927fe6ba18e42b1ac7af5f63f1142dac9ac94ef62b51dc5
```

Configuration:

```text
scenario = finite75_depletion
D        = 2.5e-3 m^2/s
tau      = infinity
lateral quadrature = 9
```

The predeclared deterministic numerical-readiness coordinate was

> finest-grid-pair change of the raw four-color phase <= 2% of the frozen reference transport phase at every nonzero RF.

Quick grids:

```text
61 x 47
81 x 61
121 x 91
```

The 81x61 -> 121x91 pair gave

```text
first-difference relative change = 1.9046e-3
worst phase change / frozen target = 4.0320e-2
```

so the strict 2% phase-scale gate **FAILED** at this resolution. The threshold was not relaxed.

The largest linear residual was below `2.8e-14`, and the dc committor/Ramo error was below `2.4e-15` over the quick sequence.

---

## 3. Refined predeclared gate

The same 2% criterion was retained and the grid was refined rather than the threshold changed.

Authoritative refined run:

```text
run  = 32062211082
job  = 95485832071
head = 6e54853dee03f489732e1046a7511168df551aee
```

Artifact:

```text
name   = paper03-stageA-resolvent-grid-gate-refined
id     = 9298540999
digest = sha256:4f8ba4a6397382edb4bd6716368bc603bfd939a024138202cce50f7de3f0ef40
```

Refined grids:

```text
81 x 61
121 x 91
161 x 121
```

For the decisive 121x91 -> 161x121 pair:

| RF | phase at 121x91 | phase at 161x121 | change / frozen target |
|---:|---:|---:|---:|
| 100 MHz | -0.00559928 deg | -0.00582217 deg | 0.0186082 |
| 500 MHz | -0.0299208 deg | -0.0310554 deg | 0.0193200 |
| 1 GHz | -0.0664625 deg | -0.0686641 deg | 0.0199410 |

Thus

```text
first-difference relative change = 8.5836e-4
worst phase change / frozen target = 1.99410e-2
predeclared 2% gate = PASS
```

The pass was close enough to the threshold that it was not treated as the end of the numerical attack.

At 161x121:

```text
maximum cell Peclet number = 2.3299
maximum RF linear relative residual = 4.995e-14
committor relative residual = 3.439e-15
dc committor/Ramo max error = 2.887e-15
```

---

## 4. Post-gate adversarial refinement

Because the predeclared pass occurred at 1.9941%, one finer grid was run after the gate. This extra check is explicitly **post-gate**; it does not alter or retroactively redefine the predeclared criterion.

Implementation:

```text
numerics/paper03_stageA_resolvent_extended_check.py
```

Authoritative run:

```text
workflow = Paper 03 Stage A resolvent post-gate refinement
run      = 32062334204
job      = 95486232276
head     = f4627e1d69451014e6d50a6f3bdc8c40477214a1
```

Artifact:

```text
name   = paper03-stageA-resolvent-postgate
id     = 9298586484
digest = sha256:d56cfe19ea53c1e88b6181db839eeede66836be36e03b2d9254b2e5469dbaeaf
```

Grid sequence:

```text
121 x 91
161 x 121
201 x 151
```

For 161x121 -> 201x151:

| RF | phase at 161x121 | phase at 201x151 | change / frozen target |
|---:|---:|---:|---:|
| 100 MHz | -0.00582217 deg | -0.00595446 deg | 0.0110451 |
| 500 MHz | -0.0310554 deg | -0.0317266 deg | 0.0114300 |
| 1 GHz | -0.0686641 deg | -0.0699593 deg | 0.0117317 |

and

```text
first-difference relative change = 4.8896e-4
worst phase change / frozen target = 1.17317e-2
```

The finer check therefore remains below the original 2% threshold and shows continued refinement rather than a threshold-crossing oscillation.

At 201x151:

```text
maximum cell Peclet number = 1.87386
maximum RF linear relative residual = 7.968e-14
committor relative residual = 4.565e-15
dc committor/Ramo max error = 4.108e-15
transient nodes = 29999
```

---

## 5. What is and is not established

Established numerically for this Stage-A fixed-field formulation:

```text
positive exponentially fitted backward generator works;
sparse RF solves are internally precise;
dc committor/Ramo identity is satisfied to floating-point-scale error;
the predeclared 2%-of-target grid gate passes on 121x91 -> 161x121;
an additional 201x151 grid strengthens the convergence trend;
small spectral observables can be evaluated without Monte-Carlo variance dominating them.
```

Not established:

```text
that the raw four-color phase is itself the correct final blind statistic for evolving optical kernels;
that the 201x151 phase values are a mechanism-specific detector prediction;
that Stage A is a self-consistent semiconductor Poisson/drift-diffusion solution;
that the stochastic and deterministic formulations have yet passed a quantitative cross-formulation comparison;
that recombination/contact/multicarrier extensions are converged;
that a Paper-03 standalone claim exists.
```

In particular, the current raw closure/Hankel/root diagnostics are inherited geometry diagnostics. Paper 01 Rev. 9 explicitly requires the calibrated arbitrary-kernel model

```math
M_m(r)=\int g_m(z)e^{rz}\,dz,
```

```math
J_m=A+B M_m(r),
```

when wavelength changes the kernel shape. That kernel-aware nonlinear consistency test must be implemented before the Stage-A result is used to judge the Paper-01 one-mode null.

---

## 6. Next numerical/scientific gates

```text
1. check lateral/source quadrature convergence at the refined deterministic grid;
2. compute a same-physics planar/same-optics reference rather than interpreting the raw closure directly;
3. implement the calibrated arbitrary-kernel one-mode blind consistency fit;
4. compare deterministic and stochastic formulations on coarse observables that Monte Carlo can actually resolve (dc current / selected-contact probability / broad RF response), rather than asking Monte Carlo to resolve the final tiny closure phase;
5. add finite recombination through the deterministic resolvent and converge it;
6. only then advance to Stage-B charge-coupled semiconductor Poisson/drift-diffusion.
```

`science_interpretation_ready` remains false.