# Nonuniform Shockley-Ramo Weighting Field — Exact Observation Forcing and Closure Signatures

**Date:** 2026-08-11  
**Status:** **DERIVED / CHECKED / CONDITIONAL**; direct response to adversarial review; clarifies that weighting-field nonuniformity changes the observation operator rather than the transport law

## 1. Why this is a first-order paper risk

The headline four-color theorem assumes a uniform planar Shockley-Ramo weighting field.

A real detector can have spatially varying weighting field near contacts, depletion edges, mesas, guard structures, or non-planar electrodes.

A skeptical reviewer can therefore ask:

> **Can a nonuniform weighting field create the same four-color phase residual that the paper attributes to spatially varying transport?**

Yes, at leading low RF it can.

But its spatial-mode signature is also constrained and can be tested.

---

## 2. Exact terminal-current functional for nonuniform weighting field

Let

```math
E_w(z)
```

be the scalar weighting field in a one-dimensional transport coordinate.

For homogeneous drift-diffusion

```math
j(z,t)=w p-D\partial_zp,
```

Shockley-Ramo gives

```math
I(t)
=q\int E_w(z)j(z,t)dz.
```

Integrate the diffusive term by parts. If the carrier density vanishes at the absorbing collector and remote upstream boundary,

```math
\boxed{
I(t)
=q\int
\left[
wE_w(z)+D E_w'(z)
\right]
p(z,t)dz.
}
\tag{1}
```

Thus a nonuniform weighting field changes the **observation forcing**.

It is not equivalent to changing `D`, `w`, or `kappa`.

---

## 3. Exact backward equation

Let `J(z,s)` be the expected discounted raw induced current for a carrier starting at `z`, with uniform Markov recombination/killing `kappa`.

Feynman-Kac / backward transport gives

```math
\boxed{
D J''+wJ'-(\kappa+s)J
=-\left[wE_w(z)+D E_w'(z)\right].
}
\tag{2}
```

For constant `E_w`, the right-hand side is constant. The solution is one constant particular term plus one admissible homogeneous exponential, which is the origin of the one-mode four-color theorem.

For variable `E_w`, extra spatial structure is forced directly into the measured current even when the physical transport coefficients are perfectly homogeneous.

This is why weighting-field nonuniformity must be classified as an **observable-model failure**, not automatically as anomalous transport.

---

## 4. Linear weighting-field gradient gives exactly one extra first-difference mode

Take

```math
E_w(z)=E_0(a+bz)
```

locally, and define

```math
\lambda=\kappa+s.
```

At nonzero `lambda`, a linear particular solution

```math
J_p(z)=c_0+c_1z
```

exists because Eq. (2) has linear forcing.

The complete one-boundary solution is therefore

```math
J(z)=c_0+c_1z+B e^{rz},
```

where `r` is the admissible root of

```math
D r^2+w r-\lambda=0.
```

Sample at equally spaced internal coordinates

```math
z_m=z_0+mh.
```

Then the first differences are

```math
\boxed{
\Delta J_m
=C+B_1q^m,
\qquad
q=e^{rh}.
}
\tag{3}
```

Thus a linear weighting-field gradient converts the first-difference sequence from rank one to **rank two**, with one spatial multiplier fixed exactly at

```math
\boxed{q_{weight}=1.}
\tag{4}
```

That multiplier is RF-independent.

This is a strong diagnostic:

```text
four-color one-mode closure fails
+
six-color rank-two closure passes
+
one recovered first-difference multiplier is ~1 at every RF
```

is precisely the pattern expected from a local linear weighting-field gradient in otherwise homogeneous transport.

A generic hidden carrier state or finite boundary need not produce this fixed unit multiplier.

---

## 5. DC limit

When

```math
s=0,
\qquad
\kappa=0,
```

the total induced charge is path independent:

```math
J(z,0)
\propto
\int_z^L E_w(x)dx.
```

For linear `E_w`, `J(z,0)` is quadratic in `z`, so its first differences are linear in the color index.

That is a rank-two Jordan sequence with a repeated multiplier

```math
q=1.
```

Thus the DC spectral sequence itself can reveal a smooth weighting-field gradient before the RF transport law is interpreted.

---

## 6. General small-spacing closure for a smooth measured current

For any smooth complex current function `J(z)`, let

```math
d_m=J(z_{m+1})-J(z_m)
```

for four equally spaced coordinates.

At quartet midpoint `z_c`,

```math
\boxed{
\mathcal C_4
=2\ln d_1-\ln d_0-\ln d_2
=-h^2\partial_z^2\ln J'(z_c)+O(h^4).
}
\tag{5}
```

The exact homogeneous uniform-weighting model has `J'(z)` exponential, so the second derivative of `ln J'` vanishes.

Equation (5) is useful for perturbation analysis because it separates the null from the mechanism that breaks it.

---

## 7. First-order weighting-field perturbation in deterministic homogeneous transport

Take constant velocity `v` and

```math
E_w(z)=E_0[1+\epsilon f(z)].
```

For a carrier generated at `z` and collected at `L`, the raw-current transform is

```math
J(z,s)
=\int_z^L
E_w(x)
\exp[-\gamma(x-z)]dx,
```

with

```math
\gamma=s/v.
```

Expand

```math
J=J_0+\epsilon J_1.
```

Using Eq. (5) and the exact first-order forced solution gives

```math
\boxed{
\mathcal C_{4,w}
=-\epsilon h^2
 e^{\gamma(L-z_c)}
\left[
f''(z_c)-\gamma f'(z_c)
\right]
+O(\epsilon h^4,\epsilon^2).
}
\tag{6}
```

At DC, `gamma=0`, so a locally linear weighting field produces no first-order closure error; curvature of the weighting field is required.

At nonzero RF, however, a locally linear weighting field does contribute at first order.

Define the local fractional weighting-field slope

```math
\beta
=\partial_z\ln E_w
\simeq\epsilon f'.
```

For low RF and locally linear `E_w`,

```math
\boxed{
\mathcal C_{4,w}
\simeq
+i\omega h^2\frac{\beta}{v}
}
\tag{7}
```

under the manuscript's `e^{-i omega t}` convention and coordinate orientation.

---

## 8. Important degeneracy with the slowness-gradient signal

The manuscript's deterministic transport-gradient theorem gives

```math
\mathcal C_{4,tr}
=-i\omega h^2
\left[
2q'(z_c)-(L-z_c)q''(z_c)
\right]
+O(\omega h^4,\omega^2),
```

where

```math
q=1/v.
```

Both the transport-gradient term and a linear weighting-field gradient are therefore

```text
phase-like
and
linear in RF at low frequency.
```

This means RF scaling alone cannot separate them.

The weighting-field gradient must instead be

```text
independently calculated from device electrostatics,
constrained by geometry,
or identified through its extra q=1 spatial mode.
```

This is a substantive limitation, not a cosmetic correction.

---

## 9. Quantitative tolerance for the current HgCdTe quartet

Use the same four real HgCdTe optical kernels as the manuscript, the same quartet

```text
2.5, 3.0, 3.5, 4.0 um,
```

and homogeneous transport at the path-harmonic velocity.

Impose a linear weighting field whose fractional value changes by a specified amount across the `1.5 um` quartet span.

The exact finite-width deterministic calculation gives the following weighting-field-only phase closure relative to the uniform-weighting control:

| fractional weighting-field change across quartet | 100 MHz | 500 MHz | 1 GHz |
|---:|---:|---:|---:|
| 0.5% | +0.00093 deg | +0.00431 deg | +0.00661 deg |
| 1.0% | +0.00191 deg | +0.00883 deg | +0.01346 deg |

Compare with the manuscript's stochastic gradient-sensitive excess magnitudes

```text
0.01198 deg @ 100 MHz
0.05873 deg @ 500 MHz
0.11041 deg @ 1 GHz.
```

A linear weighting-field variation therefore stays below approximately **10%** of the worked transport-gradient signal only if its fractional change across the quartet is roughly below

| RF | maximum linear weighting-field change across 1.5 um for 10% contamination |
|---:|---:|
| 100 MHz | ~0.64% |
| 500 MHz | ~0.68% |
| 1 GHz | ~0.83% |

These are not universal device tolerances. They are quantitative requirements for the explicit worked quartet under this simple linear-weighting stress.

They show that the reviewer concern is real: sub-percent weighting-field uniformity over the sampled internal region may be required if the weighting contribution is not independently modeled.

---

## 10. Scientific consequence

The paper should no longer treat nonuniform weighting field merely as one item in a generic limitations list.

The correct hierarchy is:

```text
four-color closure failure
-> test whether a second mode is statistically resolved

if a second mode exists:
-> is one multiplier pinned near q=1 across RF?
   yes: weighting-field gradient is a conventional candidate

-> do two roots satisfy finite-boundary DD root algebra?
   yes: boundary candidate

-> do signed roots satisfy two-carrier transport closure?
   yes: electron-hole candidate

-> none of the above:
   richer observation/transport model required.
```

Thus the nonuniform weighting field does weaken the naive one-mode interpretation, but it does not destroy the falsification philosophy. It becomes another ordinary, overdetermined rung of the model hierarchy.

Numerical regression:

`numerics/nonuniform_weighting_field_closure.py`
