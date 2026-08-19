# Collection-Weighted Dark Transport — Experiment 02

**Date:** 2026-08-12  
**Status:** adversarial physical refinement of the strong-dark semiconductor branch  
**Priority:** unassessed; no novelty claim

The earlier bulk-dark model counted every thermally generated carrier pair in the active volume as a detected dark event.

That is physically inconsistent if a dark-generated carrier must traverse the same material and can recombine before reaching the collecting boundary.

This file corrects that asymmetry.

---

## 1. Same geometry and collection survival

Use the one-dimensional slab

```text
z=0       illuminated face
z=L       collecting boundary
```

with carrier survival probability

```math
P_{\rm col}(z|L)
=e^{-\beta(L-z)}.
```

For the photo-signal, the useful-event probability remains

```math
\eta_s(L)
=\eta_0
\int_0^L
\alpha e^{-\alpha z}
e^{-\beta(L-z)}dz.
```

For `alpha != beta`,

```math
\eta_s(L)
=\eta_0\frac{\alpha}{\alpha-\beta}
(e^{-\beta L}-e^{-\alpha L}).
```

---

## 2. Bulk dark generation should also be collection weighted

Let

```math
r_d
```

be the uniform generation rate of potentially detectable dark excitations per unit volume per unit time.

A dark excitation generated at `z` contributes a detected dark event only with probability

```math
P_{\rm col}(z|L)=e^{-\beta(L-z)}.
```

Therefore the **collected dark-event rate** is

```math
\lambda_d^{\rm col}(L)
=r_dA
\int_0^L e^{-\beta(L-z)}dz.
```

Hence

```math
\boxed{
\lambda_d^{\rm col}(L)
=
\frac{r_dA}{\beta}
(1-e^{-\beta L}).
}
```

This replaces the earlier raw-volume rate

```math
r_dAL.
```

---

## 3. Thin-limit expansion

For

```math
\beta L\ll1,
```

```math
1-e^{-\beta L}
=\beta L-rac{\beta^2L^2}{2}+O(L^3).
```

Therefore

```math
\boxed{
\lambda_d^{\rm col}(L)
=r_dA
\left[
L-rac{\beta L^2}{2}+O(L^3)
\right].
}
```

Thus the leading collected dark rate is still linear in thickness.

The collection correction first enters at higher order.

---

## 4. Transit-linked gate

Retain the minimal transport gate

```math
T(L)=\frac Lv
```

for the thickness-dependent part of the observation interval.

Then the mean collected dark count is

```math
\mu_d^{\rm col}(L)
=\lambda_d^{\rm col}(L)\frac Lv.
```

Exactly,

```math
\boxed{
\mu_d^{\rm col}(L)
=
\frac{r_dA}{\beta v}
L(1-e^{-\beta L}).
}
```

In the thin limit,

```math
\boxed{
\mu_d^{\rm col}(L)
=
\frac{r_dA}{v}L^2
-
\frac{r_dA\beta}{2v}L^3
+O(L^4).
}
```

Therefore the leading dark-exposure exponent remains

```math
\boxed{p=2}
```

with

```math
\boxed{K=r_dA/v.}
```

---

## 5. Strong-dark optimum therefore survives to leading order

In the strong-dark regime the optimum is forced to

```math
L=O(K^{-1/2}).
```

If that also satisfies

```math
\alpha L\ll1,
\qquad
\beta L\ll1,
```

then

```math
\eta_s(L)
\sim\eta_0\alpha L,
```

and

```math
\mu_d^{\rm col}(L)
\sim K L^2.
```

Hence the same leading optimization applies:

```math
\boxed{
L_*
\sim
\frac1{\sqrt{2K}}
=
\sqrt{\frac{v}{2r_dA}},
}
```

```math
\boxed{
\mu_*
\sim\frac12,
}
```

and

```math
\boxed{
\mathcal D_{\max}
\sim
\eta_0\alpha
\sqrt{\frac{v}{2e\,r_dA}}.
}
```

Thus the strong-dark bulk-transit scaling is **not an artifact of assuming 100% dark-carrier collection**.

---

## 6. Full time-dependent collected dark intensity

The refinement can also be made at the timestamp-process level.

A dark excitation generated at depth `z` survives with factor

```math
e^{-\beta(L-z)}.
```

Using deterministic drift time

```math
t=\frac{L-z}{v},
```

so

```math
z=L-vt,
\qquad
0\le t\le L/v,
```

the detected dark-event intensity in arrival time is

```math
\boxed{
\lambda_0(t)
=
r_dAv
e^{-\beta vt},
\qquad
0\le t\le L/v.
}
```

Integrating gives

```math
\int_0^{L/v}\lambda_0(t)dt
=
\frac{r_dA}{\beta}(1-e^{-\beta L}),
```

as required.

---

## 7. Signal/dark likelihood weight

The photo-signal event density is

```math
q_L(t)
=\eta_0\alpha v
e^{-\alpha L}
e^{(\alpha-\beta)vt}.
```

Therefore the point-process likelihood weight is

```math
\boxed{
\frac{q_L(t)}{\lambda_0(t)}
=
\frac{\eta_0\alpha}{r_dA}
e^{-\alpha L}e^{\alpha vt}.
}
```

Equivalently, because `z=L-vt`,

```math
\boxed{
\frac{q_L}{\lambda_0}
=
\frac{\eta_0\alpha}{r_dA}
e^{-\alpha z}.
}
```

The common collection-survival factor cancels from the **local likelihood ratio**.

This is physically interesting:

> when signal and bulk-dark carriers experience the same collection survival law, collection loss suppresses both processes locally in the same way; the timestamp/depth evidence that distinguishes them is then controlled by the optical generation profile relative to spatially uniform dark generation.

---

## 8. Thin-limit time shapes again become indistinguishable

For a sufficiently thin device,

```math
\alpha L\ll1,
\qquad
\beta L\ll1,
```

both

```math
q_L(t)
```

and

```math
\lambda_0(t)
```

are approximately constant over the gate.

Thus signal and dark timestamps again become shape-indistinguishable to leading order.

The full timestamp observer reduces to the same leading count-shift problem analyzed in `TIMETAGGED_POINT_PROCESS_DECISION.md`.

Therefore the strong-dark optimum

```math
\mu_*=1/2
```

for the `p=2,s=1` bulk-transit class and the corresponding feasibility scaling survive the collection-consistent point-process refinement.

---

## 9. Important finite-thickness correction

Away from the thin limit, signal and dark timestamp shapes differ:

```math
q_L(t)\propto e^{(\alpha-\beta)vt},
```

```math
\lambda_0(t)\propto e^{-\beta vt}.
```

Their likelihood ratio scales as

```math
e^{\alpha vt},
```

so later arrivals (corresponding to shallower optical absorption) can carry systematically different evidence than earlier arrivals.

Thus full timestamp processing can outperform simple count/click processing outside the asymptotic thin regime.

---

## 10. What this refinement does and does not establish

It establishes, inside the same minimal drift/survival model, that

```text
collection-weighting the bulk dark process
does not change the leading p=2 strong-dark class.
```

It does **not** establish universality across dark mechanisms.

`DARK_SCALING_UNIVERSALITY_CLASSES.md` already showed that surface-dominated or fixed-gate dark processes belong to different scaling classes.

Therefore the robust statement is conditional:

> **For a bulk-generated dark process whose detected rate is locally linear in thickness in the thin limit, combined with a transit-linked gate linear in thickness, the leading strong-dark decision class has `p=2`, regardless of whether dark carriers are collected perfectly or through the same finite survival law as signal carriers.**

---

## 11. Current status

**DERIVED / PHYSICALLY MORE CONSISTENT / STRONG-DARK SCALING SURVIVES / PRIORITY UNASSESSED.**

This increases confidence that the bulk-transit scaling

```math
\mathcal D_{\max}
\sim
\eta_0\alpha
\sqrt{\frac{v}{2e\,r_dA}}
```

is not merely a bookkeeping artifact of the first dark model.

However, it remains a conditional asymptotic result and still requires direct prior-art comparison against semiconductor photon-counting/dark-current optimization literature.
