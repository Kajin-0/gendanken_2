# Shockley-Ramo Survival Theorem — Terminal Current Versus First-Passage Flux

**Date:** 2026-08-10  
**Status:** exact reduced theorem for one-dimensional homogeneous drift-diffusion with positive downstream drift, remote upstream boundary, absorbing collector, uniform weighting field, and one conserved signal carrier; classical Shockley-Ramo/transport ingredients; no novelty claim

## 1. Why this theorem matters

The adversarial observable audit showed that two responses had been conflated:

```text
arrival / collection flux
and
terminal Shockley-Ramo induced current.
```

The relation between them can be derived exactly in the simplest homogeneous drift-diffusion geometry.

The result explains why

```text
arrival flux -> pure spatial exponential -> 3-color law
```

while

```text
terminal current -> constant minus exponential -> 4-color difference law.
```

---

## 2. Transport geometry

Let one carrier be generated at `x0<L` and move on

```math
(-\infty,L]
```

with constant downstream drift `w>0` and diffusion coefficient `D>0`.

The collector at `L` is absorbing.

Let

```math
p(x,t|x_0)
```

be the density of carriers still in the transport region.

It obeys

```math
\boxed{
\partial_t p
=-\partial_x j,
\qquad
j=w p-D\partial_x p.
}
```

Use

```math
p(L,t)=0,
```

and assume

```math
p,\partial_xp\to0
```

at the remote upstream end.

---

## 3. Survival and arrival flux

Define the survival probability

```math
\boxed{
S(t)=\int_{-\infty}^{L}p(x,t)dx.
}
```

The first-passage density at the collector is

```math
f_T(t)=-\frac{dS}{dt}.
```

Its Laplace transform is

```math
\boxed{
U(s)
=E[e^{-sT}]
=\int_0^\infty e^{-st}f_T(t)dt.
}
```

Therefore

```math
\boxed{
\widetilde S(s)
=\int_0^\infty e^{-st}S(t)dt
=\frac{1-U(s)}{s}.
}
\tag{1}
```

Equation (1) is the standard survival-density relation.

---

## 4. Uniform planar weighting field

Let the readout electrode have constant one-dimensional weighting field

```math
E_w.
```

In the continuum Shockley-Ramo description, the terminal induced current is

```math
I(t)
=qE_w\int_{-\infty}^{L}j(x,t)dx.
```

Insert

```math
j=w p-Dp_x.
```

Then

```math
\begin{aligned}
\int j dx
&=w\int p dx-D[p(L,t)-p(-\infty,t)]\\
&=wS(t),
\end{aligned}
```

because the density vanishes at both ends of this reduced half-line geometry.

Hence

```math
\boxed{
I(t)=qE_w w S(t).
}
\tag{2}
```

This is the central observable relation.

The ensemble terminal current is proportional to the probability that the carrier has **not yet completed first passage**.

---

## 5. Frequency-domain relation

Laplace-transform Eq. (2) and use Eq. (1):

```math
\boxed{
J(s)
=qE_ww\frac{1-U(s)}{s}.
}
\tag{3}
```

At RF set

```math
s=i\omega
```

by analytic continuation from `Re s>0`.

Thus

```text
arrival transform U
and
terminal current J
```

contain the same first-passage propagator, but through different algebraic observables.

---

## 6. Homogeneous spatial semigroup

For homogeneous scalar first passage over distance

```math
d=L-x_0,
```

```math
\boxed{
U(d,s)=e^{-\gamma(s)d},
}
```

with uniform drift-diffusion dispersion

```math
\boxed{
D\gamma^2+w\gamma=s.
}
```

Equation (3) becomes

```math
\boxed{
J(d,s)
=\frac{qE_ww}{s}
\left[1-e^{-\gamma(s)d}\right].
}
\tag{4}
```

So the terminal current contains

```text
one depth-independent particular term
plus
one exponential propagation mode.
```

---

## 7. Color-count consequence

### Arrival / collector-flux observable

Three equally spaced source distances give

```math
\boxed{
U_1^2=U_0U_2.
}
```

### Raw planar terminal current

First differences remove the constant particular term:

```math
\Delta J_m=J_{m+1}-J_m\propto e^{-\gamma d_m}.
```

Therefore four equally spaced source distances give

```math
\boxed{
(J_2-J_1)^2
=(J_1-J_0)(J_3-J_2).
}
```

The extra color is not an arbitrary statistical choice.

It is the direct consequence of Shockley-Ramo signal formation adding one spatially constant particular mode to the first-passage propagator.

---

## 8. Deterministic limit

As

```math
D\to0,
```

```math
\gamma=s/w.
```

The arrival transform is

```math
U=e^{-sd/w},
```

and Eq. (4) becomes

```math
J
=qE_ww\frac{1-e^{-sd/w}}{s},
```

which is exactly the transform of a rectangular current pulse of duration

```math
d/w.
```

Thus the theorem connects continuously to the simplest Shockley-Ramo picture.

---

## 9. Boundaries of validity

Equation (2) uses several deliberately strong assumptions.

It is not asserted unchanged for

```text
finite upstream boundaries,
spatially varying weighting field,
comparable electron and hole signals,
spatially varying drift/diffusion,
carrier loss/recombination with full two-carrier signal formation,
trapping/internal states,
nonlocal transport,
or time-dependent electrode weighting fields.
```

Those effects can add particular or homogeneous spatial modes and are precisely what the higher color-count / RF closure hierarchy is meant to detect.

The theorem is a **gedanken baseline**, not a universal photodiode transfer formula.

---

## 10. Paper-level interpretation

The first-passage semigroup mathematics remains the underlying transport structure.

Shockley-Ramo theory determines how that propagator appears in the measured electrical signal.

The conceptual chain is therefore

```text
carrier first passage
-> U(d,s)

Shockley-Ramo signal formation
-> J(d,s) proportional to [1-U(d,s)]/s

spatial finite difference
-> remove the Ramo particular term

spectral-depth closure
-> recover U's spatial exponent gamma(s).
```

This is the corrected bridge between the abstract first-passage theory and a measurable planar photodetector current.
