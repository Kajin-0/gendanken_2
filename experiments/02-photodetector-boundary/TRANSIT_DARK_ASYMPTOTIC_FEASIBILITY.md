# Strong Dark-Time Semiconductor Feasibility Asymptote — Experiment 02

**Date:** 2026-08-12  
**Status:** conditional asymptotic cross-layer derivation; priority unassessed  
**Priority:** requires prior-art and full-model validation

This file extracts the strong transport-linked dark-exposure limit of `TRANSIT_LINKED_THICKNESS_BOUND.md`.

The purpose is to obtain a simple design-feasibility relation coupling

```text
absorption coefficient;
carrier transport speed;
dark-event density;
detector area;
required decision error.
```

---

## 1. Starting model

The exact binary distinguishability is

```math
\mathcal D(L)
=\eta_s(L)
\exp[-\delta_1L-\zeta L^2],
```

with

```math
\zeta=\frac{r_dA}{v}.
```

Here

```text
r_d = bulk dark-event rate density per volume;
A   = detector area;
v   = effective carrier transport speed.
```

The signal probability for front illumination and opposite-side collection is

```math
\eta_s(L)
=\eta_0\frac{\alpha}{\alpha-\beta}
(e^{-\beta L}-e^{-\alpha L}).
```

---

## 2. Thin-device expansion

For sufficiently small `L`,

```math
\eta_s(L)
=\eta_0\alpha L
\left[
1-\frac{\alpha+\beta}{2}L+O(L^2)
\right].
```

Therefore

```math
\mathcal D(L)
\approx
\eta_0\alpha L
\exp[-cL-\zeta L^2],
```

where

```math
\boxed{
c
=\delta_1+\frac{\alpha+\beta}{2}.}
```

This approximation is valid when the optimum lies at lengths satisfying

```text
alpha L << 1;
beta L << 1;
delta_1 L << 1.
```

---

## 3. Approximate optimum thickness

For

```math
\mathcal D_{\rm thin}(L)
=\eta_0\alpha L e^{-cL-\zeta L^2},
```

the stationarity condition is

```math
\frac1L-c-2\zeta L=0.
```

Thus

```math
\boxed{
L_*^{\rm thin}
=\frac{2}
{c+\sqrt{c^2+8\zeta}}.
}
```

This is the same leading result obtained from the log-slope expansion in `TRANSIT_LINKED_THICKNESS_BOUND.md`.

---

## 4. Strong dark-time regime

If

```math
\boxed{\zeta\gg c^2,}
```

then

```math
\boxed{
L_*
\sim
\frac1{\sqrt{2\zeta}}
=
\sqrt{\frac{v}{2r_dA}}.
}
```

The optimum thickness is set primarily by a competition between

```text
more signal probability ~ L
and
dark-time penalty ~ exp[-(r_dA/v)L^2].
```

Optical and collection inverse lengths enter only at higher order in this limit because the optimum has already been forced into the thin-device regime.

---

## 5. Maximum distinguishability asymptote

At

```math
L_*=1/\sqrt{2\zeta},
```

the quadratic dark exponent is

```math
\zeta L_*^2=1/2.
```

Neglecting the subleading `cL_*` term,

```math
\boxed{
\mathcal D_{\max}
\sim
\frac{\eta_0\alpha}
{\sqrt{2e\zeta}}.
}
```

Substituting

```math
\zeta=r_dA/v,
```

gives

```math
\boxed{
\mathcal D_{\max}
\sim
\eta_0\alpha
\sqrt{
\frac{v}{2e\,r_dA}
}.
}
```

This is the strongest simple cross-layer scaling produced by the thickness branch so far.

---

## 6. Decision-feasibility condition

Let

```math
D_{\rm req}=1-2\epsilon
```

for target equal-prior binary error `epsilon`.

Requiring

```math
\mathcal D_{\max}\gtrsim D_{\rm req}
```

gives

```math
\boxed{
\frac{r_dA}{v}
\lesssim
\frac{\eta_0^2\alpha^2}
{2eD_{\rm req}^2}.
}
```

Equivalently,

```math
\boxed{
v
\gtrsim
\frac{2e\,r_dA\,D_{\rm req}^2}
{\eta_0^2\alpha^2}.
}
```

Or, as an area ceiling,

```math
\boxed{
A
\lesssim
\frac{
\eta_0^2\alpha^2v
}{
2e\,r_dD_{\rm req}^2
}.
}
```

These are **asymptotic conditional feasibility relations**, not universal detector bounds.

---

## 7. Interpretation

The combination

```math
\boxed{
\eta_0\alpha
\sqrt{\frac{v}{r_dA}}
}
```

acts as the leading strong-dark-time decision resource.

Improvement can come from

```text
larger absorption coefficient alpha;
higher carrier speed v;
lower dark-event density r_d;
smaller active area A;
higher thickness-independent efficiency eta_0.
```

The trade is explicitly cross-layer:

```text
optics x transport x noise x geometry x decision target.
```

---

## 8. Why this scaling is more informative than `make L thinner`

The asymptote does not merely say that dark noise favors thin devices.

It identifies the thickness scale

```math
L_*\sim\sqrt{v/(2r_dA)}
```

and the maximum achievable binary distinction

```math
D_{\max}\sim\eta_0\alpha\sqrt{v/(2er_dA)}.
```

Thus the model predicts when **no choice of thickness can compensate** a poor combination of carrier speed, area, dark-event density, and absorption strength.

---

## 9. Regime-of-validity warning

The asymptote requires more than `zeta` being numerically large.

The optimum must satisfy

```math
\alpha L_*\ll1,
\qquad
\beta L_*\ll1,
\qquad
\delta_1L_*\ll1.
```

Using

```math
L_*\sim1/\sqrt{2\zeta},
```

sufficient conditions are schematically

```math
\zeta\gg\alpha^2,
\qquad
\zeta\gg\beta^2,
\qquad
\zeta\gg\delta_1^2.
```

The exact numerical boundary depends on the accuracy required.

Outside this regime, solve the exact unique-root equation from `TRANSIT_LINKED_THICKNESS_BOUND.md`.

---

## 10. Numerical sanity check performed

The exact one-dimensional optimization and the asymptotic formulas were compared numerically over increasing `zeta` for representative positive `alpha,beta,delta_1`.

The optimum thickness and maximum distinguishability approach

```math
L_*\to1/\sqrt{2\zeta},
```

and

```math
\mathcal D_{\max}
\to\eta_0\alpha/\sqrt{2e\zeta}
```

as the dark-time parameter is increased, consistent with the analytic expansion.

This is a sanity check of the asymptote, not physical validation of the model.

---

## 11. Current novelty disposition

No novelty claim is made.

The broad ingredients

```text
absorption-thickness tradeoff;
transit-time / bandwidth tradeoff;
dark-current scaling;
area scaling
```

are established detector engineering.

The exact cross-layer decision scaling above may be useful, but because it follows from a deliberately minimal model its novelty expectation should remain **modest** until direct source comparison and a more realistic transport/noise model are completed.

---

## 12. Next test

The most important physical weakness is that the gate uses the worst-case thickness transit time `L/v` rather than the actual absorption-depth-dependent signal arrival time.

A stronger model should treat

```text
absorption depth z
-> survival probability
-> signal arrival time (L-z)/v
-> competing dark-event point process
-> timestamped output likelihood.
```

That would replace the binary fixed-window detector with a proper time-tagged decision process.

If the same feasibility scaling survives that refinement, it becomes substantially more physically meaningful.
