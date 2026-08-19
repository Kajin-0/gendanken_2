# Transit-Linked Thickness / Dark-Exposure Decision Bound — Experiment 02

**Date:** 2026-08-12  
**Status:** new conditional cross-layer derivation; priority unassessed  
**Priority:** requires direct prior-art audit before novelty language

`SEMICONDUCTOR_THICKNESS_DECISION_BOUND.md` assumed a fixed decision gate independent of absorber thickness. This file couples the gate to carrier transport time.

The physical question becomes:

> **When a thicker absorber simultaneously changes photon absorption, carrier survival distance, dark-active volume, and the time for which dark events can accumulate, is there still a unique optimum thickness and an explicit decision-feasibility boundary?**

Yes inside the stated model.

---

## 1. Keep the same optical/collection model

Slab:

```text
z=0       illuminated face
z=L       collecting boundary
```

Parameters:

```text
alpha = absorption coefficient
beta  = inverse effective carrier-survival length = 1/ell_c
eta_0 = thickness-independent efficiency factor
```

Useful signal probability:

for `alpha != beta`,

```math
\boxed{
\eta_s(L)
=\eta_0\frac{\alpha}{\alpha-\beta}
\left(e^{-\beta L}-e^{-\alpha L}\right).
}
```

For `alpha=beta`,

```math
\boxed{
\eta_s(L)=\eta_0\alpha L e^{-\alpha L}.
}
```

---

## 2. Link decision gate to transport time

Take the minimal timing model

```math
\boxed{
\tau_g(L)=\tau_0+\frac{L}{v},
}
```

where

```text
tau_0 = fixed electronics / declaration overhead
v     = effective carrier transport speed.
```

This is intentionally simple. It says that a useful gate must remain open long enough for a carrier generated near the farthest relevant location to traverse an order-`L` distance.

---

## 3. Bulk dark-event exposure becomes linear + quadratic in thickness

Let `r_d` be independent dark-event rate density per unit volume and `A` detector area.

Then

```math
\mu_d(L)
=r_dAL\tau_g(L).
```

Therefore

```math
\boxed{
\mu_d(L)
=\delta_1L+\zeta L^2,
}
```

with

```math
\boxed{
\delta_1=r_dA\tau_0,
\qquad
\zeta=\frac{r_dA}{v}.
}
```

This is the first explicit cross-layer coupling of

```text
geometry
x dark-active volume
x carrier transit time.
```

---

## 4. Binary click distinguishability

As before, with independent signal and dark clicks,

```math
\mathcal D(L)
=\eta_s(L)e^{-\mu_d(L)}.
```

Thus

```math
\boxed{
\mathcal D(L)
=\eta_s(L)
\exp[-\delta_1L-\zeta L^2].
}
```

For equal priors,

```math
\boxed{
P_{e,\min}(L)
=\frac12[1-\mathcal D(L)].
}
```

---

## 5. Exact stationarity equation for alpha != beta

Write

```math
\Delta=\alpha-\beta.
```

For `alpha != beta`, the signal can be written as

```math
\eta_s(L)
\propto
e^{-\beta L}(1-e^{-\Delta L}).
```

Its logarithmic derivative is

```math
\boxed{
\frac{d}{dL}\ln\eta_s(L)
=-\beta+
\frac{\Delta}{e^{\Delta L}-1}.
}
```

The optimum of `D(L)` satisfies

```math
\frac{d}{dL}\ln\mathcal D(L)=0,
```

so

```math
\boxed{
-\beta+
\frac{\alpha-\beta}
{e^{(\alpha-\beta)L_*}-1}
=\delta_1+2\zeta L_*.
}
```

Equivalently,

```math
\boxed{
\frac{\alpha-\beta}
{e^{(\alpha-\beta)L_*}-1}
=\beta+\delta_1+2\zeta L_*.
}
```

This implicit equation is the exact optimum-thickness condition in the stated transit-linked model.

---

## 6. The positive optimum is unique

Define

```math
F(L)
=-\beta+
\frac{\Delta}{e^{\Delta L}-1}.
```

Then

```math
\boxed{
F'(L)
=-\frac{\Delta^2e^{\Delta L}}
{(e^{\Delta L}-1)^2}<0
}
```

for every `L>0` and `Delta != 0`.

Therefore the signal logarithmic slope is strictly decreasing.

The dark/time slope

```math
G(L)=\delta_1+2\zeta L
```

is nondecreasing and strictly increasing if `zeta>0`.

As `L -> 0+`,

```math
F(L)\sim\frac1L-\frac{\alpha+\beta}{2}\to+\infty.
```

As `L -> infinity`,

```math
F(L)\to-\min(\alpha,\beta)<0,
```

while `G(L)>=0`.

Hence the equation

```math
F(L_*)=G(L_*)
```

has exactly one positive solution.

Therefore:

```math
\boxed{
\text{the transit-linked model has one and only one physically relevant optimum thickness.}
}
```

---

## 7. Transit-linked dark exposure always shifts the optimum thinner

Set `zeta=0`. The stationarity equation reduces to the fixed-gate result

```math
L_0
=\frac{
\ln[(\alpha+\delta_1)/(\beta+\delta_1)]
}{\alpha-\beta}.
```

For `zeta>0`, the right-hand side of

```math
F(L)=\delta_1+2\zeta L
```

is strictly larger than the fixed-gate value `delta_1` for every `L>0`.

Because `F(L)` is strictly decreasing, the crossing must occur earlier:

```math
\boxed{
L_*(\zeta>0)<L_0.
}
```

Thus:

> **when the observation gate grows with carrier transit time, the decision-optimal absorber is always thinner than in the otherwise identical fixed-gate model.**

This is exact inside the model.

---

## 8. Equal optical and collection inverse lengths

For

```math
\alpha=\beta,
```

```math
\mathcal D(L)
=\eta_0\alpha L
\exp[-(\alpha+\delta_1)L-\zeta L^2].
```

The stationarity condition is

```math
\frac1L
-(\alpha+\delta_1)
-2\zeta L
=0.
```

Therefore

```math
2\zeta L^2
+(\alpha+\delta_1)L
-1=0.
```

For `zeta>0`, the exact positive root is

```math
\boxed{
L_*
=
\frac{
\sqrt{(\alpha+\delta_1)^2+8\zeta}
-(\alpha+\delta_1)
}{4\zeta}.
}
```

The numerically stable equivalent form is

```math
\boxed{
L_*
=
\frac{2}
{(\alpha+\delta_1)+
\sqrt{(\alpha+\delta_1)^2+8\zeta}}.
}
```

As `zeta -> 0`,

```math
L_*\to\frac1{\alpha+\delta_1},
```

recovering the fixed-gate limit.

---

## 9. Strong dark-time coupling asymptote

When `zeta` is large enough that the optimum is thin, use

```math
\frac{d}{dL}\ln\eta_s(L)
\approx
\frac1L-rac{\alpha+\beta}{2}.
```

Then the stationarity condition becomes

```math
2\zeta L^2
+cL
-1\approx0,
```

with

```math
\boxed{
c=\delta_1+\frac{\alpha+\beta}{2}.}
```

Hence

```math
\boxed{
L_*
\approx
\frac{2}
{c+\sqrt{c^2+8\zeta}}.
}
```

For very large `zeta`,

```math
\boxed{
L_*
\sim
\frac1{\sqrt{2\zeta}}.
}
```

So under strong volume-times-transit dark exposure, the optimum thickness acquires the scaling

```math
\boxed{
L_*
\propto
\sqrt{
\frac{v}{r_dA}
}.
}
```

This explicitly links optimum geometry to carrier speed and dark-event density.

---

## 10. Dimensionless form

Scale length by collection length

```math
\ell_c=1/\beta.
```

Define

```math
\boxed{
a=\alpha\ell_c,
\qquad
d_1=\delta_1\ell_c,
\qquad
q=\zeta\ell_c^2.
}
```

Let

```math
x=L/\ell_c.
```

Then the optimum for `a != 1` satisfies

```math
\boxed{
\frac{a-1}{e^{(a-1)x_*}-1}
=1+d_1+2qx_*.
}
```

The entire minimal problem therefore collapses to three dimensionless resources:

```text
a   = absorption/collection-length ratio;
d_1 = fixed-overhead dark exposure per collection length;
q   = transport-linked dark exposure over one collection length squared.
```

---

## 11. Decision-feasibility ceiling still exists

Because `D(L)` is continuous,

```math
\mathcal D(0)=0,
```

and

```math
\mathcal D(L)\to0
```

as `L -> infinity` when `zeta>0`, the unique stationary point is the global maximum.

Define

```math
\boxed{
\mathcal D_{\max}
=\mathcal D(L_*).
}
```

Then target equal-prior error `epsilon` is achievable by some thickness if and only if

```math
\boxed{
\mathcal D_{\max}
\ge1-2\epsilon.
}
```

If this fails, no thickness can satisfy the requested decision performance inside the model.

The difference from the fixed-gate case is that `D_max` is now determined by the unique implicit root rather than a simple elementary closed form.

---

## 12. A stronger geometry-time-dark coupling

The physical chain is now

```text
increase L
-> more optical interaction / shifted generation distribution
-> longer carrier survival distance
-> more dark-active volume
-> longer required observation gate
-> still more accumulated dark probability
-> altered binary decision distance.
```

This is a genuine cross-layer coupling that the fixed-gate model only partially represented.

---

## 13. Important interpretation

The result does **not** say `thin is always better`.

At `L -> 0`, useful absorption tends to zero.

At large `L`, collection survival and dark exposure dominate.

The finite optimum arises because neither extreme is acceptable.

---

## 14. What remains simplified

The timing law

```math
\tau_g=\tau_0+L/v
```

is a crude upper-envelope transport model.

Real collection time depends on

```text
where the photon is absorbed;
field profile;
drift versus diffusion;
velocity saturation;
trapping;
carrier species;
weighting field;
thresholding strategy.
```

A more exact model should average or optimize over the joint distribution of

```text
absorption depth
and
collection time.
```

That is a likely next physical refinement if this branch survives prior-art audit.

---

## 15. Current status

**DERIVED / ANALYTICALLY CHECKED / CONDITIONAL / PRIORITY UNASSESSED.**

The most interesting statements are:

```math
\frac{\alpha-\beta}
{e^{(\alpha-\beta)L_*}-1}
=\beta+\delta_1+2\zeta L_*,
```

```math
L_*(\zeta>0)<L_*(\zeta=0),
```

and, in the strong dark-time regime,

```math
L_*\sim1/\sqrt{2\zeta}
=\sqrt{v/(2r_dA)}.
```

These are the next equations to audit directly against semiconductor photodetector / solar-cell / radiation-detector optimization literature.
