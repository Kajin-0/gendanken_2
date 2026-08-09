# HgCdTe Two-Region Field Allocation — The Smallest Heterostructure That Can Beat the Uniform-Field Bound

**Date:** 2026-08-09  
**Status:** exact constrained optimization for two homogeneous regions with local transport/leakage; standard Lagrange/convexity mathematics; no novelty claim

## 1. Purpose

`HGCDTE_FIELD_PROFILE_VARIATIONAL_BOUND.md` proved that in one homogeneous material, merely redistributing electric field cannot reduce local WKB tunneling exposure at fixed carrier transit time.

Therefore the smallest physically meaningful escape is a two-region structure in which the material or defect parameters differ.

This note asks:

> **How should the field be divided between two different HgCdTe regions if the total carrier transit time is fixed and tunneling leakage is to be minimized?**

The answer is a marginal-cost matching rule.

---

## 2. Two-region model

Let the device contain regions

```math
i=1,2
```

with lengths

```math
L_1,
\qquad
L_2,
\qquad
L_1+L_2=L.
```

Each region has its own local transport and leakage laws

```math
v_i(F_i),
```

```math
g_i(F_i).
```

Assume constant field within each region.

Total transit time:

```math
\boxed{
T
=\sum_{i=1}^2
\frac{L_i}{v_i(F_i)}.
}
```

Total local leakage exposure:

```math
\boxed{
G
=\sum_{i=1}^2
L_i g_i(F_i).
}
```

The bias voltage is **not** fixed independently in this optimization. The field is chosen to meet the transit-time target with minimum leakage.

---

## 3. Exact interior optimality condition

Introduce a Lagrange multiplier `lambda` for the fixed transit time:

```math
\mathcal L
=
\sum_iL_i g_i(F_i)
+\lambda
\left[
\sum_iL_i/v_i(F_i)-T
\right].
```

For an interior optimum,

```math
\frac{\partial\mathcal L}{\partial F_i}=0.
```

The region lengths cancel from the local condition:

```math
\boxed{
\frac{dg_i}{dF_i}
+\lambda
\frac{d(1/v_i)}{dF_i}
=0.
}
```

Therefore every active region must satisfy

```math
\boxed{
-\frac{dg_i/dF_i}
{d(1/v_i)/dF_i}
=\lambda.
}
```

The quantity

```math
\boxed{
\mathcal M_i(F)
\equiv
-\frac{dg_i/dF}
{d(1/v_i)/dF}
}
```

is the **marginal leakage cost per marginal reduction in reciprocal velocity**.

Thus the optimal field distribution obeys

> **Equalize marginal leakage cost per unit transit-time improvement across the regions.**

This is the central result.

---

## 4. Ohmic + local WKB specialization

Take

```math
v_i(F)=\mu_iF
```

and

```math
\boxed{
g_i(F)
=A_iF^p\exp(-K_i/F),
\qquad p>0.
}
```

Then

```math
\frac{d(1/v_i)}{dF}
=-\frac1{\mu_iF^2},
```

and

```math
\frac{dg_i}{dF}
=A_iF^{p-1}e^{-K_i/F}
\left(p+\frac{K_i}{F}\right).
```

Hence

```math
\boxed{
\mathcal M_i(F)
=\mu_iA_iF^{p+1}
\exp(-K_i/F)
\left(p+\frac{K_i}{F}\right).
}
```

The optimum satisfies

```math
\boxed{
\mathcal M_1(F_1)
=\mathcal M_2(F_2).
}
```

Together with

```math
\boxed{
\frac{L_1}{\mu_1F_1}
+\frac{L_2}{\mu_2F_2}
=T,
}
```

this determines the two optimal fields.

---

## 5. Which region receives more field?

The marginal-cost expression makes several trends explicit.

### Larger tunneling barrier `K`

At fixed `F`, write

```math
z=K/F.
```

The `K` dependence of the factor

```math
(p+z)e^{-z}
```

has derivative

```math
\frac{d}{dz}[(p+z)e^{-z}]
=(1-p-z)e^{-z}.
```

For the physically important cases

```math
p\ge1,
```

this is strictly negative for `z>0`.

Therefore a region with larger `K` has **smaller marginal leakage cost at the same field**.

To restore the common optimum `lambda`, it receives a larger field.

So, all else equal:

```math
\boxed{
K_2>K_1
\quad\Rightarrow\quad
F_2>F_1
}
```

at the optimum.

This is the mathematical version of

> put more field into the region with the stronger tunneling barrier.

### Smaller leakage prefactor `A`

At fixed field,

```math
\mathcal M\propto A.
```

A cleaner / lower-trap / lower-generation region therefore receives more field.

### Higher mobility `mu`

At fixed field,

```math
\mathcal M\propto\mu.
```

A high-mobility region needs less field to contribute to the required transit-time reduction, so the optimum tends to operate it at a lower field, all else equal.

This is a useful reminder that

```text
best place for field
```

and

```text
highest mobility region
```

are not automatically the same thing.

---

## 6. Reciprocal-field form

For ohmic transport define

```math
y_i=1/F_i.
```

Then

```math
T
=\sum_i\frac{L_i}{\mu_i}y_i
```

and

```math
g_i
=A_i y_i^{-p}e^{-K_iy_i}.
```

The stationarity condition becomes

```math
\boxed{
\mu_iA_i
 e^{-K_i y_i}
 y_i^{-p-1}
(p+K_i y_i)
=\lambda.
}
```

Each regional leakage function is strictly convex in `y_i`, so the two-region problem has a unique interior solution whenever no field bound becomes active.

---

## 7. Deep-WKB approximation

If

```math
K_i/F_i\gg p,
```

then

```math
p+K_i/F_i
\simeq K_i/F_i.
```

The marginal condition simplifies to

```math
\boxed{
\lambda
\simeq
\mu_iA_iK_iF_i^p
\exp(-K_i/F_i).
}
```

Let

```math
z_i=K_i/F_i.
```

Then

```math
\lambda
\simeq
\mu_iA_iK_i^{p+1}
 z_i^{-p}e^{-z_i}.
```

This can be inverted approximately:

```math
\boxed{
z_i
\simeq
pW_0\!\left[
\frac1p
\left(
\frac{\mu_iA_iK_i^{p+1}}
{\lambda}
\right)^{1/p}
\right],
}
```

so

```math
\boxed{
F_i
\simeq
\frac{K_i}
{pW_0\left[
\frac1p
(\mu_iA_iK_i^{p+1}/\lambda)^{1/p}
\right]}.
}
```

Thus the optimal field grows almost proportionally with the barrier scale `K_i`, modified only logarithmically through the Lambert function in the deep-WKB regime.

---

## 8. Dimensionless example

Take two equal-length regions with

```text
mu_1 = mu_2
A_1  = A_2
p    = 2.
```

Set the target transit time equal to the one produced by a reference uniform field `F_bar`, so

```math
\frac12\left(
\frac{F_{\rm bar}}{F_1}
+
\frac{F_{\rm bar}}{F_2}
\right)=1.
```

Let

```math
K_1/F_{\rm bar}=2,
\qquad
K_2/F_{\rm bar}=4.
```

Numerical minimization gives

```math
\boxed{
F_1\simeq0.872F_{\rm bar},
\qquad
F_2\simeq1.172F_{\rm bar}.
}
```

The average leakage exposure becomes

```math
G_{\rm opt}
\simeq0.794\,G_{\rm uniform}.
```

So the heterogeneous field allocation reduces the modeled tunneling exposure by about

```math
\boxed{20.6\%}
```

at the same transit time.

The gain comes entirely from the difference in material barrier scale. If `K_1=K_2` and all other local parameters are equal, the result collapses back to the uniform-field theorem.

---

## 9. Why heterostructure field engineering works

The homogeneous theorem and two-region escape fit existing detector engineering cleanly.

Published HgCdTe APD work changes

- composition / bandgap;
- doping;
- multiplication-layer thickness;
- depletion profile;
- spatial field distribution;
- where impact ionization is allowed.

Chen et al. (npj Quantum Materials **6**, 103, 2021) show directly that changing multiplication-layer doping and thickness changes the electric-field distribution and the competition between BBT and avalanche generation.

More recent composition-graded HgCdTe APD work explicitly uses different-gap regions and built-in quasi-electric fields to redistribute carrier transport and dark-current burden.

Therefore the useful design principle is not

```text
make F(x) nonuniform.
```

It is

> **place field where the local material can buy the most transit/multiplication benefit per unit leakage cost.**

---

## 10. Important APD caveat

For a simple photodiode whose objective is fast collection with low leakage, a wide-gap / low-trap region is naturally a safer place to put field.

An APD has a different objective because impact ionization is **desired** in the multiplication region.

Narrower-gap HgCdTe can provide efficient electron ionization but also increases tunneling vulnerability.

Therefore an APD optimization should not minimize leakage at fixed transit time alone. It must include a required multiplication/gain functional.

This is exactly why real APD layer design can choose a multiplication region that is deliberately more ionization-active than the absorber while controlling its thickness and field.

The present two-region theorem is therefore a collection/leakage baseline, not a complete APD design theorem.

---

## 11. General continuous heterostructure

For spatially varying parameters,

```math
v=v(F,x),
```

```math
g=g(F,x),
```

the local interior optimum obeys

```math
\boxed{
-\frac{\partial g/\partial F}
{\partial(1/v)/\partial F}
=\lambda
}
```

at every position where the field is not constrained by a boundary.

This is the continuous marginal-cost equalization principle.

It gives a direct interpretation for graded HgCdTe:

```text
larger local tunneling barrier / lower trap burden
-> lower marginal leakage cost
-> receive more field

fragile narrow-gap / high-trap region
-> receive less field
```

subject to the required transport, absorption, depletion and multiplication functions.

---

## 12. Fixed total voltage is a separate problem

The present optimization fixes transit time but allows whatever total voltage is needed.

If one also imposes

```math
\int_0^L F(x)dx=V,
```

there are **two independent integral constraints**.

The local condition gains another multiplier:

```math
\boxed{
\frac{\partial g}{\partial F}
+\lambda_T
\frac{\partial(1/v)}{\partial F}
+\lambda_V
=0.
}
```

The resulting optimum need not coincide with the transit-only solution.

Do not silently apply the one-constraint theorem to a fixed-bias design problem.

---

## 13. Claim boundary

### DERIVED

For two local homogeneous regions, fixed transit time and no independent voltage constraint, the interior optimum satisfies

```math
\boxed{
\mathcal M_1(F_1)
=\mathcal M_2(F_2),
\qquad
\mathcal M_i
=-\frac{g_i'}{(1/v_i)'}.
}
```

For ohmic `v_i=mu_iF_i` and local WKB `g_i=A_iF_i^p e^{-K_i/F_i}`,

```math
\boxed{
\mathcal M_i
=\mu_iA_iF_i^{p+1}e^{-K_i/F_i}
(p+K_i/F_i).
}
```

### CHECKED

The equal-length example with `K_1/F_bar=2`, `K_2/F_bar=4`, `p=2` gives

```text
F1/F_bar ~ 0.872
F2/F_bar ~ 1.172
G_opt/G_uniform ~ 0.794.
```

### KNOWN / PRIOR

- Lagrange multiplier / convex optimization;
- field-profile engineering in HgCdTe APDs;
- graded-gap / heterostructure detector design.

### NON-CLAIM

This is not

- a universal heterostructure optimum;
- a complete APD design law;
- a theorem including self-consistent Poisson electrostatics;
- a theorem for nonlocal II/TAT;
- a novelty claim.

---

## 14. Next decisive step

The smallest useful detector-design question is now:

> **For a two-region HgCdTe collection structure with one narrow-gap absorber and one wider-gap transport region, how much field redistribution is actually worth pursuing once the voltage constraint and realistic band offsets are included?**

Before solving a continuous graded structure, add

1. fixed total bias;
2. band-offset / carrier-transfer condition;
3. region-specific TAT/BTBT parameters;
4. then, only if needed, nonlocal impact ionization.
