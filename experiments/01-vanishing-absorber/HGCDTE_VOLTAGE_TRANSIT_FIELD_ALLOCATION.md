# HgCdTe Voltage–Transit Field Allocation — Bias Cost of Protecting a Fragile Region

**Date:** 2026-08-09  
**Status:** exact Cauchy/Jensen allocation result in the ohmic local-transport model; standard inequality mathematics; no novelty claim

## 1. Purpose

`HGCDTE_FIELD_PROFILE_VARIATIONAL_BOUND.md` showed that a homogeneous material cannot reduce local WKB tunneling exposure at fixed transit time by shaping the electric field.

`HGCDTE_TWO_REGION_FIELD_ALLOCATION.md` then showed that a heterogeneous two-region structure **can** lower leakage by putting more field into the region with the lower marginal leakage cost.

A real device, however, pays for that redistribution with bias voltage.

This note asks:

> **What minimum voltage is required to achieve a target transit time, and how much extra voltage is consumed by heterostructure field redistribution?**

---

## 2. General ohmic transport with spatially varying mobility

Take

```math
v(x)=\mu(x)F(x)
```

with

```math
F(x)>0.
```

Total voltage drop:

```math
\boxed{
V
=\int_0^L F(x)\,dx.
}
```

Carrier transit time:

```math
\boxed{
T
=\int_0^L
\frac{dx}{\mu(x)F(x)}.
}
```

Define

```math
S_\mu
\equiv
\int_0^L
\frac{dx}{\sqrt{\mu(x)}}.
```

---

## 3. Exact voltage–transit inequality

Apply Cauchy-Schwarz to

```math
\sqrt{F(x)}
```

and

```math
\frac1{\sqrt{\mu(x)F(x)}}.
```

Their product is

```math
1/\sqrt{\mu(x)}.
```

Therefore

```math
\left(\int_0^L Fdx\right)
\left(\int_0^L\frac{dx}{\mu F}\right)
\ge
\left(\int_0^L\frac{dx}{\sqrt\mu}\right)^2.
```

Hence

```math
\boxed{
VT
\ge
S_\mu^2.
}
```

Equivalently,

```math
\boxed{
V_{\min}(T)
=\frac{S_\mu^2}{T},
}
```

or

```math
\boxed{
T_{\min}(V)
=\frac{S_\mu^2}{V}.
}
```

This is purely a kinematic ohmic-transport result. It contains no tunneling or dark-current model.

---

## 4. Equality field profile

Cauchy equality requires

```math
\sqrt F
=C
\frac1{\sqrt{\mu F}},
```

so

```math
\boxed{
F(x)
=\frac{C}{\sqrt{\mu(x)}}.
}
```

Using the transit constraint,

```math
C=\frac{S_\mu}{T}.
```

Therefore the minimum-bias field profile for a target transit time is

```math
\boxed{
F_{\min V}(x)
=
\frac{S_\mu}
{T\sqrt{\mu(x)}}.
}
```

Thus a lower-mobility region receives more field in the minimum-voltage solution.

This differs from the leakage-optimal allocation, which also depends on bandgap, trap burden and tunneling exponent.

---

## 5. Homogeneous special case

For constant mobility `mu`,

```math
S_\mu=L/\sqrt\mu.
```

Therefore

```math
\boxed{
VT\ge\frac{L^2}{\mu}.
}
```

At equality,

```math
\boxed{F=V/L=\text{uniform}.}
```

So in one homogeneous ohmic material, the uniform field simultaneously

- minimizes voltage for a target transit time; and
- minimizes local WKB tunneling exposure for that transit time.

There is no field-shaping freedom at the kinematic optimum.

---

## 6. Two equal-length, equal-mobility regions — exact bias contrast

Now consider the heterogeneous leakage example with

```math
L_1=L_2=L/2,
```

```math
\mu_1=\mu_2=\mu.
```

Fix the transit time and define the corresponding minimum-bias uniform field

```math
\boxed{
F_{\rm bar}
=\frac{L}{\mu T}.
}
```

Let

```math
y_i=1/F_i.
```

The fixed transit-time condition is

```math
\boxed{
\frac12(y_1+y_2)
=\frac1{F_{\rm bar}}.
}
```

Define the bias ratio

```math
\boxed{
\beta
\equiv
\frac{V}{V_{\min}}
=
\frac{(F_1+F_2)/2}
{F_{\rm bar}}.
}
```

Cauchy requires

```math
\boxed{\beta\ge1.}
```

---

## 7. Exact field contrast for a stated extra-bias ratio

Write

```math
\frac{y_1}{1/F_{\rm bar}}=1+s,
```

```math
\frac{y_2}{1/F_{\rm bar}}=1-s.
```

The transit constraint is then automatic.

The bias ratio is

```math
\beta
=\frac12\left[
\frac1{1+s}
+\frac1{1-s}
\right]
=\frac1{1-s^2}.
```

Therefore

```math
\boxed{
s
=\sqrt{1-\frac1\beta}.
}
```

The two fields are

```math
\boxed{
F_{\rm low}
=\frac{F_{\rm bar}}
{1+s},
}
```

```math
\boxed{
F_{\rm high}
=\frac{F_{\rm bar}}
{1-s}.
}
```

This is an exact speed/bias relation.

For a given bias overhead `beta`, the device can only generate this amount of two-region field contrast while preserving the target transit time.

The safer region should receive `F_high`; the more fragile region receives `F_low`.

---

## 8. Small bias overhead can produce appreciable field contrast

For

```math
\beta=1+\epsilon,
\qquad
\epsilon\ll1,
```

```math
s
=\sqrt{1-1/(1+\epsilon)}
\simeq\sqrt\epsilon.
```

Thus the first useful field contrast grows as the **square root** of the fractional extra bias:

```math
\boxed{
F_{\rm high}/F_{\rm bar}
\simeq
1+\sqrt\epsilon,
}
```

```math
\boxed{
F_{\rm low}/F_{\rm bar}
\simeq
1-\sqrt\epsilon.
}
```

So a few percent additional voltage can create a much larger percentage field redistribution.

This explains why heterostructure field engineering can have strong leakage leverage even when the additional total bias is modest.

---

## 9. Revisit the two-region tunneling example

The previous example used

```text
L1 = L2
mu1 = mu2
A1 = A2
p = 2
K1/F_bar = 2
K2/F_bar = 4.
```

The leakage-only optimum was

```math
F_1\simeq0.872F_{\rm bar},
```

```math
F_2\simeq1.172F_{\rm bar},
```

with the higher field placed in the larger-`K` region.

Its bias ratio is

```math
\boxed{
\beta
=\frac{0.872+1.172}{2}
\simeq1.0220.
}
```

So the modeled leakage reduction

```math
G_{\rm opt}/G_{\rm uniform}
\simeq0.794
```

corresponds to only about

```math
\boxed{2.2\%}
```

additional voltage above the minimum required for that transit time.

Thus in this dimensionless example:

```text
~2.2% extra bias
-> ~17% field reduction in fragile region
-> ~17% field increase in safe region
-> ~20.6% lower modeled tunneling exposure.
```

This is an illustration, not an HgCdTe device prediction.

---

## 10. Exact leakage–bias curve for two equal regions

For equal lengths and mobilities, the field pair at a chosen `beta` is fixed up to interchange.

If region 2 is safer, assign

```math
F_1
=\frac{F_{\rm bar}}
{1+s},
```

```math
F_2
=\frac{F_{\rm bar}}
{1-s},
```

where

```math
s=\sqrt{1-1/\beta}.
```

For local leakage laws

```math
g_i(F)
=A_iF^p e^{-K_i/F},
```

the exact two-region Pareto curve is

```math
\boxed{
G(\beta)
=\frac L2
\left[
g_1\left(
\frac{F_{\rm bar}}{1+s}
\right)
+
g_2\left(
\frac{F_{\rm bar}}{1-s}
\right)
\right].
}
```

This makes bias an explicit third resource alongside transit time and leakage.

The leakage-only optimum occurs at the minimum of this function over `beta >= 1`.

---

## 11. Why this matters for real HgCdTe heterostructures

A graded or layered HgCdTe device can exploit extra bias to move field away from

```text
narrow-gap regions
high-trap regions
surface-sensitive regions
```

and toward

```text
wider-gap regions
cleaner low-trap regions
regions designed for multiplication or fast transport.
```

Published HgCdTe APD work explicitly changes layer thickness, doping and composition to alter internal field distributions and suppress BBT while retaining useful gain. This is therefore a physically real design axis, not a purely mathematical counterexample.

However, real devices also have

- built-in fields;
- band offsets;
- Poisson constraints;
- spatially varying depletion;
- nonlocal impact ionization;
- capacitance and RC penalties.

The present result is the simplest bias accounting beneath those complications.

---

## 12. General fixed-voltage / fixed-transit optimization

If both

```math
\int Fdx=V
```

and

```math
\int dx/v(F,x)=T
```

are fixed while leakage is minimized, introduce two multipliers:

```math
\boxed{
\frac{\partial g}{\partial F}
+\lambda_T
\frac{\partial(1/v)}{\partial F}
+\lambda_V
=0.
}
```

This replaces the one-constraint marginal-cost rule.

In a continuous heterostructure the solution need not be uniform even if each local leakage curve is convex, because `g` and `v` themselves vary with `x`.

---

## 13. Claim boundary

### DERIVED

For ohmic spatial transport,

```math
\boxed{
VT
\ge
\left[
\int_0^L\frac{dx}{\sqrt{\mu(x)}}
\right]^2.
}
```

Equality field:

```math
\boxed{
F(x)
\propto\mu(x)^{-1/2}.
}
```

For two equal-length/equal-mobility regions at fixed transit time and bias ratio `beta`,

```math
\boxed{
s=\sqrt{1-1/\beta},}
```

```math
\boxed{
F_{\rm low,high}
=F_{\rm bar}/(1\pm s).
}
```

### CHECKED

The previous two-region leakage optimum has

```text
beta ~ 1.0220
G_opt/G_uniform ~ 0.794.
```

### KNOWN / PRIOR

Cauchy-Schwarz / constrained transport optimization and heterostructure field engineering are established mathematics/device physics.

### NON-CLAIM

This is not

- a high-field velocity theorem;
- a complete fixed-bias HgCdTe device model;
- a Poisson/self-consistent electrostatics solution;
- a full APD optimization;
- a novelty claim.

---

## 14. Next decisive step

The next model should stop treating `F_1` and `F_2` as freely assignable knobs.

For a two-region HgCdTe heterostructure, enforce

1. band offsets / continuity of electrochemical potential;
2. Poisson/depletion electrostatics;
3. fixed applied bias;
4. region-specific `E_g`, mobility and trap parameters;
5. then evaluate transit, TAT, BTBT and nonlocal II.

That is the minimum model in which a quantitative field-engineering recommendation would be physically credible.