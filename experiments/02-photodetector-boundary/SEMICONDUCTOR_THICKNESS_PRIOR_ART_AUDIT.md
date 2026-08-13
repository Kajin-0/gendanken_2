# Semiconductor Thickness Decision-Bound Prior-Art Audit — Experiment 02

**Date:** 2026-08-12  
**Status:** initial source-level audit; physical ingredients strongly prior-art aligned; exact decision corollary priority unproven  
**Priority:** low-to-moderate novelty expectation; no novelty claim

This file audits `SEMICONDUCTOR_THICKNESS_DECISION_BOUND.md`.

The derived model combines

```text
Beer-Lambert absorption;
finite carrier-survival / collection length;
volume-scaled Poisson dark events;
binary click/no-click decision theory.
```

The central question is whether the resulting optimum thickness and decision-feasibility ceiling represent new detector physics or a transparent recombination of established ingredients.

---

## 1. Classical absorption/collection competition is established semiconductor device physics

A long-standing semiconductor photoresponse lineage, including W. W. Gartner's depletion-layer photoresponse treatment and later solar-cell/photodiode spectral-response models, combines

```text
wavelength-dependent absorption depth
with
minority-carrier transport / diffusion / collection probability.
```

The general physical fact that useful quantum efficiency can depend non-monotonically on absorber geometry when carriers generated far from the collecting region are lost is therefore **not new**.

The Experiment-02 exponential survival kernel

```math
P_{\rm surv}(z|L)=e^{-\beta(L-z)}
```

is a deliberately simplified collection model, not a new microscopic transport law.

### Claim boundary

Do not claim novelty for

```text
absorption depth competing with diffusion/collection length;
finite optimum absorber thickness from optical generation plus carrier loss;
collection probability depending on generation depth.
```

These are classical semiconductor detector/solar-cell structures.

---

## 2. Bulk dark-generation scaling with active volume is conditional but standard in spirit

The model assumes a uniform independent dark-event rate density

```math
r_d
```

so that, for area `A`, thickness `L`, and fixed decision gate `tau_g`,

```math
\mu_d=r_dAL\tau_g.
```

This is a valid minimal model for a spatially uniform bulk-generation process.

Real detector dark current/count rate can instead be dominated by

```text
surface generation;
depletion-region generation;
tunneling;
contacts;
trap-assisted processes;
avalanche afterpulsing;
readout threshold statistics;
spatially nonuniform defects.
```

Therefore linear volume scaling is **not universal**, but it is not a new physical concept either.

### Claim boundary

The dark-volume term is a **conditional modeling assumption**, not a candidate novelty.

---

## 3. Binary click distinguishability is elementary decision theory

For Bernoulli click probabilities `p0,p1`, total-variation distance is

```math
\mathcal D=|p_1-p_0|.
```

In the stated independent signal/dark model,

```math
\mathcal D(L)=\eta_s(L)e^{-\delta L}.
```

This is mathematically immediate once the signal and dark probabilities are specified.

Therefore the conversion

```text
quantum efficiency + no-dark probability
-> binary decision distance
```

is not new statistical theory.

---

## 4. Exact finite-thickness optimum remains a useful closed-form corollary

For `alpha != beta`,

```math
\mathcal D(L)
=\eta_0\frac{\alpha}{\alpha-\beta}
\left[
e^{-(\beta+\delta)L}
-e^{-(\alpha+\delta)L}
\right].
```

The exact optimum is

```math
\boxed{
L_*
=\frac{
\ln[(\alpha+\delta)/(\beta+\delta)]
}{\alpha-\beta}.
}
```

The maximum is

```math
\boxed{
\mathcal D_{\max}
=\eta_0
\frac{\alpha}{\alpha+\delta}
\left(
\frac{\beta+\delta}{\alpha+\delta}
\right)^{\frac{\beta+\delta}{\alpha-\beta}}.
}
```

This closed form is useful because it places

```text
optical absorption;
carrier-survival length;
dark-active volume;
decision error
```

in one expression.

However, its ingredients and optimization method are elementary enough that **absence of an exact identical published formula would not by itself establish novelty**.

Current status:

**DERIVED CROSS-LAYER COROLLARY / PRIORITY UNPROVEN / LOW-TO-MODERATE NOVELTY EXPECTATION.**

---

## 5. Decision-feasibility ceiling is the most useful interpretation

The target error condition

```math
\mathcal D_{\max}\ge1-2\epsilon
```

says that, inside the model,

> if the maximum achievable signal/dark distinction is below the target, no absorber thickness can satisfy the decision requirement.

This is a clean design-feasibility statement.

But it follows directly from optimizing the Bernoulli distance, so the novelty burden would have to come from the **physical model/constraint**, not from the optimization logic.

---

## 6. Why the fixed-gate assumption is the weakest part of the cross-layer coupling

The current dark exposure is

```math
\mu_d= r_d A L\tau_g
```

with `tau_g` assumed independent of thickness.

That leaves the temporal response partially external to the geometry.

But in many detector architectures the required observation gate must cover a carrier-transport or collection time that itself grows with thickness.

Then thickness influences dark events twice:

```text
more dark-active volume
and
longer time during which dark events can occur.
```

This creates a stronger cross-layer coupling between

```text
optics;
transport distance;
timing;
dark statistics;
decision error.
```

That is the next model to derive.

---

## 7. Audit disposition

| Element | Disposition |
|---|---|
| Beer-Lambert absorption | **PRIOR ART / STANDARD** |
| generation-depth-dependent carrier collection | **CLASSICAL SEMICONDUCTOR PRIOR ART** |
| finite optimum thickness from absorption + collection | **PRIOR-ART-ALIGNED** |
| bulk dark rate proportional to active volume | **STANDARD CONDITIONAL MODEL** |
| Bernoulli total-variation decision distance | **ELEMENTARY DECISION THEORY** |
| exact fixed-gate `L_*` formula | **DERIVED COROLLARY / PRIORITY UNPROVEN** |
| `D_max >= 1-2epsilon` feasibility statement | **DERIVED DECISION COROLLARY** |
| broad novelty claim | **NOT JUSTIFIED** |

---

## 8. Strongest safe value of the result

Even if fully prior-art-equivalent in content, the model gives a transparent answer to the original Gedanken question:

> **Adding more detector material can reduce detection performance because thickness changes not only photon absorption but also where carriers are generated, how far they must survive, and how much dark-active material participates.**

This is a strong conceptual result, not yet a novel theorem.

---

## 9. Next attack

Replace the externally fixed gate by a transport-linked gate.

For a minimal drift-limited model,

```math
\tau_g(L)=\tau_0+L/v,
```

with carrier speed `v` and fixed electronics/declaration overhead `tau_0`.

Then the bulk dark mean becomes

```math
\mu_d(L)
=r_d A L(\tau_0+L/v)
=\delta_1L+\zeta L^2.
```

This yields

```math
\mathcal D(L)
=\eta_s(L)e^{-\delta_1L-\zeta L^2}.
```

The next question is whether this more physical **geometry–transport-time–dark-noise–decision** coupling yields a new analytic bound or merely another standard device-optimization result.
