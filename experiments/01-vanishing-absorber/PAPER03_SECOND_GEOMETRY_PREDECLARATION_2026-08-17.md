# Paper 03 — Second Geometry Family Predeclaration

**Date:** 2026-08-17  
**Status:** **PREDECLARED MODEL FAMILY / NO RESULT / NON-CLAIM**

## 1. Purpose

The current Stage-A program uses a vertical selected-top-contact / full-bottom-contact geometry. Standalone Paper-03 GO requires the decisive behavior to survive a materially different geometry family rather than a parameter variation of the same finite pixel.

The second family is fixed here **before its output is calculated**.

## 2. Geometry family: coplanar lateral contacts

Use the same 2-D absorber cross-section dimensions as the existing stress unless numerical aspect-ratio refinement requires an explicitly documented extension:

```text
absorber thickness L = 7.6 um
lateral width W = 16 um
```

Replace the top-versus-bottom electrode topology with two **coplanar top contacts**:

```text
left top contact  -> physical potential 0
right top contact -> physical potential +V_bias
central top gap   -> insulating
bottom surface    -> insulating
sidewalls         -> insulating
```

The right top electrode is the selected terminal.

The initial declared contact layout is symmetric:

```text
left contact  : x in [-8,-2] um
central gap   : x in (-2,+2) um
right contact : x in [+2,+8] um
```

so each electrode occupies `6 um` and the insulating gap is `4 um`.

This is not a small perturbation of the original geometry. The dominant physical drift and weighting fields are lateral/fringing rather than approximately vertical.

## 3. Physical electrostatics

First second-family Stage-A calculation:

```text
Laplace physical potential only
no imposed depletion/Poisson curvature
V_bias = 0.30 V
```

This isolates geometry/topology before a later controlled space-charge coordinate is added.

If the Laplace-only family already produces a relevant spectral-depth confound, do not add space charge merely to amplify it before that result is recorded.

## 4. Independent weighting potential

Solve separately

```text
right selected contact -> phi_w = 1
left contact           -> phi_w = 0
central top gap        -> zero normal derivative
bottom                 -> zero normal derivative
sidewalls              -> zero normal derivative
```

The physical potential and weighting potential remain distinct solves.

For every collected stochastic/deterministic trajectory, the same selected-electrode Shockley--Ramo observable applies.

## 5. Carrier model

For direct comparison with the checked nominal Stage-A result, first use

```text
D = 2.5e-3 m^2/s
tau = infinity
same velocity-field law as current Stage A
same six calibrated HgCdTe optical kernels
```

Then add `tau=5 ns` only as a declared sensitivity coordinate after the infinite-lifetime result is recorded.

This remains a fixed-field Stage-A calculation, not Stage-B self-consistent semiconductor physics.

## 6. Optical coordinates

The spectral kernels remain vertical depth kernels `g_m(z)`.

The first beam is centered over the gap:

```text
x0 = 0
sigma_x = 1.0 um
```

This choice is fixed before execution because it probes the strongest vertical variation of the lateral/fringing-field topology without centering the source directly under one metal contact.

A second beam coordinate may be tested later at

```text
x0 = +2.5 um
```

only as a separately recorded positional sensitivity, not as a replacement if the centered result is unfavorable.

## 7. Same-physics control

The control for the second family is **not** the vertical planar detector.

Construct the appropriate one-dimensional/laterally homogeneous transport reference only if such a reference is mathematically meaningful for the lateral-contact topology. Otherwise the primary diagnostics are:

```text
calibrated-kernel one-mode residual;
model-order extension;
physical root-law consistency;
statistical rejection SNR.
```

Do not manufacture a misleading vertical-planar subtraction simply to reuse the first-family mimic metric.

A direct raw phase relative to the frozen Paper-01 transport target may be reported only as a scale coordinate, clearly labeled as cross-architecture rather than a same-physics baseline subtraction.

## 8. Numerical gates

Before model-order interpretation require:

```text
three spatial grids, initially 81x61 / 121x91 / 161x121 or finer;
all sparse linear residuals <1e-8;
DC endpoint/committor Shockley--Ramo identity <1e-8 for infinite lifetime;
source quadrature convergence;
finest-pair change of the calibrated one-mode residual and direct RF response quantified explicitly.
```

Because this topology is new, the first-family `2% of frozen raw phase` criterion is not automatically transplanted as the sole acceptance metric. Before the first second-family result is read, the implementation must predeclare a topology-appropriate convergence coordinate based on both direct current response and kernel-aware residual.

## 9. Blind analysis

The same blind boundary applies:

```text
forward side knows geometry and fields;
blind side receives calibrated complex channel currents, kernels, RF/noise coordinates;
blind side does not receive contact topology or hidden field labels when running the hierarchy.
```

The analysis order remains

```text
kernel-aware one mode
-> model-order diagnostic if needed
-> physical cross-RF laws
-> statistical detectability.
```

## 10. Second-family decision

The family supports the standalone geometry-independence requirement if a numerically converged ordinary region shows either:

```text
Outcome A:
transport-scale spectral confound is rejected by model-order / physical-law diagnostics before mechanism-specific claim precision;

or

Outcome B:
transport-scale spectral confound remains hidden through the hierarchy at claim precision.
```

If the coplanar family produces negligible spectral-depth structure, that is a valid negative result; do not tune contact positions after inspection and call the tuned version predeclared.

## 11. Scope lock

At creation of this file:

```text
second geometry family -> specified
solver implementation -> not yet completed
numerical result -> none
scientific outcome -> unknown
```

The current finite-pixel Stage-A refinement remains the immediate primary gate.