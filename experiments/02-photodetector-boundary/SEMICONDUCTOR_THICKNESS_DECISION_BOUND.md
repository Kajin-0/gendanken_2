# Semiconductor Thickness / Collection / Dark-Event Decision Bound — Experiment 02

**Date:** 2026-08-12  
**Status:** new conditional cross-layer derivation; priority unassessed  
**Priority:** requires direct prior-art audit before any novelty language

The broad detector-process framework has collided strongly with prior art. This file therefore returns to a narrow physical question that can potentially produce a real detector-specific design law.

Question:

> **In the simplest semiconductor slab, what absorber thickness optimizes actual photon/no-photon decision distinguishability when optical absorption, carrier survival to the collecting contact, and volume-scaled dark events all compete?**

The result is an exact finite-thickness optimum and an explicit feasibility ceiling.

---

## 1. Minimal geometry

Take a one-dimensional semiconductor slab

```text
z=0       illuminated surface
z=L       collecting boundary/contact
```

with normal incident light entering at `z=0`.

Assume:

```text
alpha  = optical absorption coefficient [1/length]
ell_c  = effective carrier-survival/collection length
beta   = 1/ell_c
eta_0  = all thickness-independent efficiency factors, 0<=eta_0<=1
```

A photon absorbed at depth `z` has differential absorption probability

```math
\alpha e^{-\alpha z}dz.
```

To reach the collecting boundary at `z=L`, the useful carrier/excitation must survive distance `L-z`:

```math
P_{\rm surv}(z|L)
=e^{-\beta(L-z)}.
```

This is a deliberately minimal exponential-survival model, not a complete drift-diffusion solution.

---

## 2. Signal-record probability

The useful signal-event probability is

```math
\eta_s(L)
=\eta_0
\int_0^L
\alpha e^{-\alpha z}
e^{-\beta(L-z)}dz.
```

For `alpha != beta`,

```math
\boxed{
\eta_s(L)
=\eta_0\frac{\alpha}{\alpha-\beta}
\left(e^{-\beta L}-e^{-\alpha L}\right).
}
```

For `alpha=beta`, the continuous limit is

```math
\boxed{
\eta_s(L)
=\eta_0\alpha L e^{-\alpha L}.
}
```

Already, unlike the ideal Beer-Lambert absorber, useful signal probability is not monotone in thickness when collection occurs at the opposite boundary.

Very thick material absorbs strongly near the illuminated surface but those carriers have poor survival to the far contact.

---

## 3. Add volume-scaled dark events

Let the detector area be `A` and assume independent dark-event rate density

```math
r_d
\quad [\mathrm{s}^{-1}\mathrm{volume}^{-1}].
```

For a decision gate of duration `tau_g`, the mean number of dark events is

```math
\mu_d(L)
=r_d A L\tau_g.
```

Define the dark-exposure coefficient

```math
\boxed{
\delta
=r_dA\tau_g
}
```

with units `[1/length]`, so

```math
\mu_d(L)=\delta L.
```

The probability of no dark event in the gate is

```math
P_{0d}(L)=e^{-\delta L}.
```

---

## 4. Exact binary click distributions

Let a registered output be only

```text
click / no click.
```

Under no incident photon `H0`,

```math
p_0(L)
=P(\mathrm{click}|H_0)
=1-e^{-\delta L}.
```

Under one incident photon `H1`, assume the useful signal event and dark process are independent and either can produce a click:

```math
p_1(L)
=1-[1-\eta_s(L)]e^{-\delta L}.
```

Therefore

```math
p_1-p_0
=\eta_s(L)e^{-\delta L}.
```

For two Bernoulli distributions, total-variation distance is simply `|p_1-p_0|`.

Thus the click/no-click detector distinguishability is

```math
\boxed{
\mathcal D(L)
=\eta_s(L)e^{-\delta L}.
}
```

For equal priors,

```math
\boxed{
P_{e,\min}(L)
=\frac12[1-\mathcal D(L)].
}
```

This is the decision-level quantity to optimize.

---

## 5. Closed form for alpha != beta

Substituting the signal probability,

```math
\boxed{
\mathcal D(L)
=\eta_0\frac{\alpha}{\alpha-\beta}
\left[
e^{-(\beta+\delta)L}
-e^{-(\alpha+\delta)L}
\right].
}
```

This exposes three independent inverse-length scales:

```text
alpha = optical absorption
beta  = carrier-survival loss
 delta = dark-event exposure per thickness.
```

The detector boundary is now controlled by their competition, not by atom count.

---

## 6. Exact optimum thickness

Differentiate:

```math
\frac{d\mathcal D}{dL}
\propto
-(\beta+\delta)e^{-(\beta+\delta)L}
+(\alpha+\delta)e^{-(\alpha+\delta)L}.
```

Setting the derivative to zero gives

```math
(\alpha+\delta)e^{-(\alpha+\delta)L_*}
=(\beta+\delta)e^{-(\beta+\delta)L_*}.
```

Therefore, for `alpha != beta`,

```math
\boxed{
L_*
=
\frac{
\ln[(\alpha+\delta)/(\beta+\delta)]
}{\alpha-\beta}.
}
```

This expression is positive for all positive `alpha,beta,delta` because numerator and denominator always share the same sign.

For `alpha=beta`,

```math
\mathcal D(L)
=\eta_0\alpha L e^{-(\alpha+\delta)L},
```

so

```math
\boxed{
L_*
=\frac{1}{\alpha+\delta}.
}
```

The general formula tends continuously to this limit.

---

## 7. Maximum achievable distinguishability

Using the optimum condition,

```math
\boxed{
\mathcal D_{\max}
=
\eta_0
\frac{\alpha}{\alpha+\delta}
\left(
\frac{\beta+\delta}{\alpha+\delta}
\right)^{\frac{\beta+\delta}{\alpha-\beta}}
}
```

for `alpha != beta`.

For `alpha=beta`,

```math
\boxed{
\mathcal D_{\max}
=
\eta_0
\frac{\alpha}{\alpha+\delta}
e^{-1}.
}
```

This is the key cross-layer ceiling.

---

## 8. Exact feasibility condition for target decision error

Equal-prior error target

```math
P_e\le\epsilon
```

requires

```math
\mathcal D\ge1-2\epsilon.
```

Since `D(L)<=D_max` for every thickness,

```math
\boxed{
\mathcal D_{\max}
\ge1-2\epsilon
}
```

is a **necessary and sufficient thickness-feasibility condition inside this model**.

If

```math
\boxed{
\mathcal D_{\max}<1-2\epsilon,
}
```

then

> **no absorber thickness can meet the requested binary decision error.**

Changing thickness alone cannot repair the detector.

One must change at least one of

```text
alpha;
ell_c = 1/beta;
eta_0;
dark-event density r_d;
area A;
gate duration tau_g;
collection geometry.
```

This is the strongest result of the model.

---

## 9. Dimensionless form

Scale length by the collection length

```math
\ell_c=1/\beta.
```

Define

```math
\boxed{
a=\alpha\ell_c,
\qquad
d=\delta\ell_c.
}
```

Then

```math
\boxed{
\frac{L_*}{\ell_c}
=
\frac{\ln[(a+d)/(1+d)]}{a-1}
}
```

for `a != 1`, with

```math
\boxed{
L_*/\ell_c=1/(1+d)
}
```

at `a=1`.

The maximum normalized distinguishability is

```math
\boxed{
\frac{\mathcal D_{\max}}{\eta_0}
=
\frac{a}{a+d}
\left(
\frac{1+d}{a+d}
\right)^{\frac{1+d}{a-1}}.
}
```

At `a=1`,

```math
\boxed{
\frac{\mathcal D_{\max}}{\eta_0}
=\frac{e^{-1}}{1+d}.
}
```

Thus this entire minimal detector family collapses to two nontrivial dimensionless coordinates:

```text
a = absorption length / collection-length competition;
d = dark-event exposure over one collection length.
```

---

## 10. Physically informative limits

### Infinite collection length

As

```math
\beta\to0,
```

and with `delta=0`, useful collection no longer penalizes thickness and

```math
L_*\to\infty,
\qquad
\mathcal D_{\max}\to\eta_0.
```

The ordinary monotone Beer-Lambert result is recovered.

### No dark events but finite collection length

For `delta=0`,

```math
\frac{\mathcal D_{\max}}{\eta_0}
=
\left(\frac{\beta}{\alpha}
\right)^{\frac{\beta}{\alpha-\beta}}.
```

Equivalently in dimensionless form,

```math
\boxed{
\mathcal D_{\max}/\eta_0
=a^{-1/(a-1)}.
}
```

At matched optical and collection inverse lengths `a=1`,

```math
\mathcal D_{\max}=\eta_0/e.
```

Even with **zero dark noise**, opposite-side collection can impose a strong finite-thickness efficiency ceiling.

### Strong absorption relative to collection loss

For

```math
a\gg1,
```

absorption occurs over a short depth relative to `ell_c`. In the present back-collection geometry this does **not** automatically guarantee good collection, because most carriers are generated far from the collecting boundary unless `L` is correspondingly thin.

### Dark exposure

Increasing `d` always shifts the useful thickness downward and lowers the maximum achievable distinguishability.

The dark process therefore acts not merely as an additive noise penalty but as a geometry-selection pressure.

---

## 11. Why this is more interesting than a bare optimum-thickness calculation

Photodiode/photovoltaic literature already contains extensive optimization of absorber thickness from absorption and diffusion/collection physics.

The potentially useful Experiment-02 step is to place **decision distinguishability** at the top of the optimization and include dark-event exposure explicitly:

```text
optical generation profile
x carrier survival
x no-dark-event probability
-> Bernoulli hypothesis distance
-> optimum geometry
-> target-error feasibility ceiling.
```

Whether this exact decision-level formulation is novel is **OPEN** and requires direct prior-art audit.

The algebra alone is not novelty evidence.

---

## 12. Counterexample value even if prior art exists

Even if the exact optimum is already known in some detector/solar-cell form, the model gives a clean Gedanken answer:

> **Adding more detector material can make a photodetector worse.**

The reason is not merely capacitance or electronics. In the minimal model, thickness simultaneously changes

```text
where the photon is absorbed;
how far the generated carrier must survive;
how much dark-active material exists.
```

Thus `more atoms` can decrease photon/no-photon distinguishability.

This directly reinforces the original conclusion that photodetector-ness is not monotone in atom count.

---

## 13. Strongest candidate cross-layer theorem from this branch

Inside the stated model:

```math
\boxed{
\sup_{L\ge0}\mathcal D(L)
=\mathcal D_{\max}(\alpha,\beta,\delta,\eta_0)
}
```

with the closed form above.

Therefore target error `epsilon` is achievable by **some** thickness if and only if

```math
\boxed{
1-2\epsilon
\le
\eta_0
\frac{\alpha}{\alpha+\delta}
\left(
\frac{\beta+\delta}{\alpha+\delta}
\right)^{\frac{\beta+\delta}{\alpha-\beta}}
}
```

for `alpha != beta`, with the continuous `alpha=beta` limit.

This is the result to attack in the prior-art literature.

---

## 14. Mandatory caveats

- One-dimensional planar geometry.
- Front illumination, collection at the opposite boundary.
- Beer-Lambert absorption with constant `alpha`.
- Exponential carrier survival with one effective length `ell_c`.
- Thickness-independent prefactor `eta_0`.
- Independent Poisson dark events with rate proportional to volume.
- Fixed decision-gate duration `tau_g` independent of thickness.
- Binary click/no-click readout only.
- No capacitance, transit-time distribution, field profile, surface recombination, reflection, gain noise, or saturation.

The result is exact only inside these assumptions.

---

## 15. Current status

**DERIVED / ALGEBRAICALLY CHECKED / CONDITIONAL / PRIORITY UNASSESSED.**

This branch is now a higher-priority novelty target than the broad detector-process framework because it produces one explicit cross-layer physical feasibility law.

Next action:

> perform a direct prior-art audit of absorber-thickness optimization including absorption length, diffusion/collection length, dark current/counts, and optimum photon/event decision performance before expanding the model further.
