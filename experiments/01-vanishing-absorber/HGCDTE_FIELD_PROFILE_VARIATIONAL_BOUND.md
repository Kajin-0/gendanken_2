# HgCdTe Field-Profile Variational Bound — When Electric-Field Shaping Cannot Beat Uniform Field

**Date:** 2026-08-09  
**Status:** exact variational/Jensen result inside a homogeneous local-transport + local-WKB-leakage model; standard convexity mathematics; no novelty claim

## 1. Question

Real HgCdTe detector structures have nonuniform electric fields.

That creates an obvious adversarial escape from every uniform-field speed/leakage calculation:

> Can the same carrier transit time be obtained with a cleverly shaped field `F(x)` while reducing the total tunneling exposure?

For a broad homogeneous-material model, the answer is **no**.

The result is useful precisely because it identifies what a real field-engineered heterostructure must change in order to improve performance: not merely the spatial distribution of the field, but the material/defect/transport parameters experienced by that field.

---

## 2. Distributed model

Let the carrier cross

```math
0\le x\le L
```

through a homogeneous material with local field

```math
F(x)>0.
```

Define the transit time

```math
\boxed{
T[F]
=\int_0^L\frac{dx}{v[F(x)]}.
}
```

Represent a local tunneling-generation/leakage exposure by

```math
\boxed{
G[F]
=\int_0^L g[F(x)]\,dx.
}
```

The local WKB family considered here is

```math
\boxed{
g(F)
=A F^p\exp(-K/F),
\qquad A>0,\ K>0,\ p>0.
}
```

Important examples are

```text
p = 2
-> direct-BTBT-like local field dependence

p = 1
-> simple TAT-like local field dependence.
```

This is a **local generation/exposure surrogate**. It is not valid when the leakage mechanism is intrinsically nonlocal, series-limited, strongly space-charge coupled, or when trap occupation/material parameters vary with position.

---

## 3. Low-field result first

For ohmic drift

```math
v(F)=\mu F,
```

the transit constraint is

```math
T
=\frac1\mu
\int_0^L\frac{dx}{F(x)}.
```

Define

```math
\boxed{y=1/F.}
```

Then fixed transit time fixes the spatial average of `y`:

```math
\frac1L\int_0^L y(x)dx
=\frac{\mu T}{L}.
```

The leakage density becomes

```math
\boxed{
h_p(y)
=A y^{-p}e^{-Ky}.
}
```

Differentiate twice:

```math
\boxed{
\frac{d^2h_p}{dy^2}
=A e^{-Ky}y^{-p-2}
\left[
K^2y^2+2pKy+p(p+1)
\right].
}
```

Every factor is positive for

```math
y>0,
\qquad p>0,
\qquad K>0.
```

Therefore

```math
\boxed{h_p''(y)>0.}
```

The leakage density is strictly convex in reciprocal field.

---

## 4. Jensen theorem — uniform field is optimal in the ohmic model

By Jensen's inequality,

```math
\frac1L\int_0^L h_p[y(x)]dx
\ge
h_p\left[
\frac1L\int_0^L y(x)dx
\right].
```

Thus, for fixed transit time `T`,

```math
\boxed{
G[F]
\ge
L g(F_0),
}
```

where the uniform field is fixed by

```math
\boxed{
F_0
=\frac{L}{\mu T}.
}
```

Equality holds only when

```math
F(x)=F_0
```

almost everywhere.

Therefore:

> **Within homogeneous ohmic drift plus local WKB leakage `A F^p e^{-K/F}`, electric-field concentration cannot reduce tunneling exposure at fixed transit time. Uniform field is the unique minimizer.**

This covers both the `p=2` direct-BTBT-like and `p=1` TAT-like field dependences used in the present simplified models.

---

## 5. Attack with high-field velocity turnover

The low-field theorem might fail once drift velocity saturates or decreases.

Use the empirical peaked transport family already audited for HgCdTe APDs:

```math
\boxed{
v(F)
=\frac{\mu F}
{1+(F/d)^r},
\qquad r>1.
}
```

Define dimensionless field and tunneling exponent

```math
\boxed{
f=F/d,
\qquad
k=K/d.
}
```

Up to positive scale factors,

```math
u(f)
\equiv
\frac1{v(F)}
\propto
U(f)
=\frac1f+f^{r-1},
```

and

```math
g(F)
\propto
G(f)
=f^p e^{-k/f}.
```

The velocity maximum occurs when

```math
\boxed{
q\equiv(r-1)f^r=1.
}
```

The rising-velocity branch therefore has

```math
\boxed{0<q<1.}
```

On this branch `U'(f)<0`, so `f` is a single-valued function of reciprocal velocity.

---

## 6. Exact convexity on the entire rising-velocity branch

Let

```math
\Phi(U)=G[f(U)].
```

Direct differentiation gives

```math
\frac{d^2\Phi}{dU^2}
=
\frac{f^p e^{-k/f}}
{(1-q)^3}
\,\mathcal P,
```

with

```math
\boxed{
\mathcal P
=
(1-q)k^2
+fk\,[2p-q(2p-r)]
+f^2p\,[p+1-q(p-r+1)].
}
```

Every term is strictly positive for

```math
p>0,
\qquad k>0,
\qquad 0<q<1.
```

To see this:

### First coefficient

```math
1-q>0.
```

### Second coefficient

If `2p-r >= 0`,

```math
2p-q(2p-r)
>
2p-(2p-r)
=r>0.
```

If `2p-r < 0`, the subtraction of a negative term makes it larger than `2p>0`.

### Third coefficient

If `p-r+1 >= 0`,

```math
p+1-q(p-r+1)
>
p+1-(p-r+1)=r>0.
```

If `p-r+1 < 0`, it is larger than `p+1>0`.

Hence

```math
\boxed{
\frac{d^2\Phi}{dU^2}>0
}
```

throughout the entire rising-velocity branch.

Thus local WKB leakage is strictly convex as a function of reciprocal drift velocity, not merely reciprocal field.

---

## 7. The falling-velocity branch is automatically dominated

For any field

```math
F>F_{\rm pk}
```

above the velocity maximum, there exists a lower field

```math
F_-<F_{\rm pk}
```

with the same local drift velocity:

```math
v(F_-)=v(F).
```

But

```math
g'(F)>0
```

for every `p>0`, `K>0` because

```math
\frac{d\ln g}{dF}
=\frac{p}{F}+\frac{K}{F^2}>0.
```

Therefore

```math
\boxed{
g(F_-)<g(F).}
```

Replacing the high-field point by `F_-` preserves its local transit-time contribution and lowers leakage.

Hence no leakage-minimizing profile contains fields above the velocity maximum under the stated model.

---

## 8. High-field theorem

After eliminating the dominated falling branch, reciprocal velocity `u=1/v` is monotonic and the leakage function `g[F(u)]` is strictly convex.

Jensen therefore applies again.

For any field profile with fixed total transit time

```math
T
=\int_0^L\frac{dx}{v[F(x)]},
```

there is a unique uniform field `F_0` on the rising branch satisfying

```math
\boxed{
v(F_0)=L/T.}
```

Then

```math
\boxed{
G[F]
\ge
L g(F_0).
}
```

Equality holds only for uniform field almost everywhere.

Therefore:

> **For homogeneous transport obeying `v=mu F/[1+(F/d)^r]`, `r>1`, and local leakage `g=A F^p exp(-K/F)`, `p>0`, a uniform field is the unique leakage-minimizing profile at fixed transit time. Field shaping alone cannot improve the speed–local-tunneling tradeoff.**

This result includes velocity saturation/negative differential velocity rather than relying on `v=mu F`.

---

## 9. General convex-envelope statement

The proof suggests a more general formulation.

For any monotonic transport branch define

```math
\boxed{
u(F)=1/v(F)}
```

and

```math
\boxed{
\phi(u)=g[F(u)].
}
```

The relaxed field-profile problem is

```math
\min
\frac1L\int_0^L\phi[u(x)]dx
```

subject to

```math
\frac1L\int_0^L u(x)dx
=T/L.
```

Then:

### If `phi(u)` is convex

Uniform field is optimal.

### If `phi(u)` is nonconvex

The minimum is the **lower convex envelope** of `phi`.

With one average constraint, the relaxed optimum can be represented by at most two field values whose reciprocal velocities bracket the required average.

Thus a genuinely beneficial field-shaped solution requires a nonconvex leakage-versus-reciprocal-velocity curve or spatially varying material parameters.

This convexification principle is standard variational mathematics; no novelty claim is made.

---

## 10. What the theorem does not cover

The result deliberately assumes a homogeneous local problem.

It does **not** cover

- spatially varying bandgap / Cd composition;
- spatially varying trap density or trap energy;
- spatially varying mobility/velocity parameters;
- heterojunction band offsets;
- field-dependent ionization history/dead space;
- nonlocal BTBT or coherent tunneling across multiple spatial regions;
- self-consistent space charge that couples generation back into `F(x)`;
- simultaneous fixed-bias/voltage constraint unless treated explicitly;
- RC/capacitance effects of the field-shaping architecture;
- avalanche multiplication as a desired rather than parasitic process.

These exclusions are not minor. They are precisely how real HgCdTe field engineering can improve devices.

---

## 11. Why this does not contradict successful HgCdTe APD field engineering

Published HgCdTe APD design work shows that doping, layer thickness and heterostructure design can redistribute electric field and suppress BBT while retaining useful multiplication/gain.

That does not contradict the theorem because those designs change more than `F(x)` in one homogeneous material:

```text
composition / bandgap
+
doping / depletion geometry
+
where multiplication occurs
+
field profile
+
carrier history.
```

For example, Chen et al. (npj Quantum Materials 6, 103, 2021) explicitly optimize multiplication-layer thickness and doping, changing the internal field distribution and the competition between BBT and avalanche generation.

The theorem says only:

> **If the material, trap population, local leakage law and transport law are fixed everywhere, redistributing field alone cannot beat uniform field for a fixed transit time in the stated model.**

The escape is therefore heterogeneous resource allocation, not mere field concentration.

---

## 12. A useful direction for heterostructures

Let material parameters vary with position:

```math
v=v(F,x),
```

```math
g=g(F,x).
```

The constrained local optimum satisfies the Euler/Lagrange pointwise condition

```math
\boxed{
\frac{\partial g}{\partial F}
+\lambda
\frac{\partial(1/v)}{\partial F}
=0
}
```

where `lambda` enforces the transit-time constraint.

Equivalently,

```math
\boxed{
-\frac{\partial g/\partial F}
{\partial(1/v)/\partial F}
=\lambda
}
```

wherever the optimum is interior.

This says the optimized structure equalizes the **marginal leakage cost of reducing reciprocal velocity** across space.

A region with larger gap, lower trap density, or more favorable transport can rationally receive more electric field than a fragile region.

This is the natural next heterostructure problem.

---

## 13. Claim boundary

### DERIVED

For homogeneous

```math
v(F)=\mu F/[1+(F/d)^r],
\qquad r>1,
```

and

```math
g(F)=A F^p e^{-K/F},
\qquad p>0,
```

local leakage is strictly convex as a function of reciprocal velocity on the rising branch, the falling branch is dominated, and therefore

```math
\boxed{
G[F]\ge Lg(F_0)
}
```

at fixed transit time, with equality only for uniform `F_0`.

### CHECKED

The symbolic factorization of `d^2g/d(1/v)^2` has been independently algebraically checked and should be protected by a deterministic regression.

### KNOWN / PRIOR

- Jensen/convex-envelope variational mathematics;
- high-field HgCdTe field engineering by doping/thickness/heterostructure design;
- local WKB-like BTBT/TAT field dependence.

### NON-CLAIM

This is not

- a universal electric-field theorem;
- a theorem for heterostructures;
- a theorem for nonlocal impact ionization;
- a proof that real HgCdTe devices should have uniform fields;
- a novelty claim.

---

## 14. Next decisive attack

The homogeneous escape is closed under the stated model.

The next problem is therefore genuinely different:

> **If `E_g(x)`, trap parameters and transport coefficients can vary spatially, where should the electric field be placed to minimize total leakage for a fixed carrier transit time?**

Start with a two-region heterostructure, because it is the smallest model that can beat the homogeneous uniform-field theorem.

Do not jump immediately to a continuous bandgap profile.