# HgCdTe TAT-Tolerance Field Allocation — Maximin Placement of an Unavoidable Compensation Voltage

**Date:** 2026-08-09  
**Status:** exact exponent-level allocation inequality for a one-dimensional heterostructure; no novelty claim

## 1. Purpose

The graded-interior and boundary-layer analyses now agree on one point:

> some electrostatic potential drop may remain unavoidable at the collection boundary, but heterogeneous HgCdTe gives freedom to choose **where** that field is concentrated.

The local trap spectrum and band gap determine how strongly a given field activates trap-assisted tunneling.

Question:

> For a fixed required compensation voltage, what field profile maximizes the worst local TAT exponent when the local tunneling-tolerance scale varies spatially?

The answer is closed form.

---

## 2. Local exponent scale

Let

```math
F_T(x)>0
```

be the local characteristic field entering a TAT exponent

```math
\exp[-F_T(x)/F(x)].
```

`F_T(x)` may vary because of

- local band gap;
- local tunneling mass;
- trap energy relative to a band edge;
- composition;
- defect species.

The present note concerns the exponent only. It does not include local trap-density or capture-cross-section prefactors.

Assume a nonnegative field magnitude `F(x)` over a boundary region `0 <= x <= w` and a required potential drop

```math
\boxed{
V_b=\int_0^wF(x)dx.
}
```

---

## 3. Maximin problem

The worst local TAT exponent is

```math
\Sigma_{\min}[F]
=\min_x\frac{F_T(x)}{F(x)}.
```

Equivalently define the worst normalized electrical stress

```math
s[F]
=\max_x\frac{F(x)}{F_T(x)}.
```

Then

```math
\Sigma_{\min}=1/s.
```

We seek the field profile that minimizes `s` subject to the fixed voltage `V_b`.

---

## 4. Exact lower bound on the worst normalized stress

If

```math
s=\max_x\frac{F(x)}{F_T(x)},
```

then pointwise

```math
F(x)\le sF_T(x).
```

Integrating,

```math
V_b
=\int_0^wF(x)dx
\le
s\int_0^wF_T(x)dx.
```

Therefore

```math
\boxed{
s
\ge
\frac{V_b}
{\int_0^wF_T(x)dx}.
}
```

---

## 5. The bound is tight

Choose

```math
\boxed{
F_{\rm opt}(x)
=\frac{V_bF_T(x)}
{\int_0^wF_T(x')dx'}.
}
```

Then

```math
\int_0^wF_{\rm opt}(x)dx
=V_b,
```

and

```math
\frac{F_{\rm opt}(x)}{F_T(x)}
=\frac{V_b}
{\int_0^wF_T(x')dx'}
```

is constant everywhere.

Hence the exact optimum is

```math
\boxed{
\min_F\max_x\frac{F}{F_T}
=
\frac{V_b}
{\int_0^wF_T(x)dx}.
}
```

Equivalently, the largest achievable minimum exponent is

```math
\boxed{
\Sigma_{\rm TAT}^{\rm maximin}
=
\frac{\int_0^wF_T(x)dx}
{V_b}.
}
```

---

## 6. Physical interpretation

At the optimum,

```math
\boxed{
F_{\rm opt}(x)\propto F_T(x).
}
```

So more field should be placed where the local TAT characteristic field is larger.

In the simple HgCdTe TAT model,

```math
F_T
=\frac{4\sqrt{2m^*}\Delta_t^{3/2}}
{3q\hbar}.
```

Therefore, all else equal, high-field burden should preferentially be placed in regions with

```text
larger local gap / tunneling mass
+
deeper traps relative to the receiving band
+
cleaner defect spectrum if prefactors are later included.
```

This is exactly what a wide-gap collection transition can provide.

---

## 7. Discrete layered form

For layers `i` of widths `w_i` and local exponent fields `F_{T,i}`, require

```math
\sum_iF_iw_i=V_b.
```

The maximin solution is

```math
\boxed{
F_i
=\frac{V_bF_{T,i}}
{\sum_jw_jF_{T,j}}.
}
```

The common optimized exponent is

```math
\boxed{
\Sigma_*
=\frac{\sum_iw_iF_{T,i}}
{V_b}.
}
```

Thus each layer carries the same normalized TAT stress:

```math
\boxed{
F_i/F_{T,i}=1/\Sigma_*.
}
```

This is a useful design diagnostic for a graded boundary represented as piecewise uniform layers.

---

## 8. Relation to the peak-field bound

If `F_T(x)` is constant,

```math
F_T(x)=F_T,
```

then

```math
F_{\rm opt}=V_b/w,
```

and

```math
\Sigma_*=F_Tw/V_b.
```

This exactly recovers the uniform-field result and the peak-field width floor in

`HGCDTE_ELECTROSTATIC_COMPENSATION_PEAK_FIELD_BOUND.md`.

Thus the new result is the heterogeneous generalization of that boundary condition.

---

## 9. A more practical generalized tolerance field

Real leakage is not controlled by TAT alone.

Define a local allowed field scale

```math
F_{\rm tol}(x)
```

that may be chosen conservatively from several constraints, for example

```math
F_{\rm tol}(x)
=\min\left[
\frac{F_{\rm TAT}(x)}{\Sigma_t},
\frac{F_K(x)}{\Sigma_Z},
F_{\rm II}(x),
F_{\rm process}(x)
\right].
```

Then the same proof gives the feasibility condition

```math
\boxed{
V_b
\le
\int_0^wF_{\rm tol}(x)dx.
}
```

If this inequality fails, **no one-dimensional electrostatic field profile can supply the required compensation voltage without violating at least one local field ceiling.**

If it holds, the equalized normalized-stress profile gives a constructive reference allocation.

This may be the most useful form for later numerical device design.

---

## 10. Why defect density is still missing

Two locations can have the same `F_T` but radically different TAT currents if their trap densities or capture cross sections differ.

A more complete optimization should replace exponent-only stress with a local leakage functional

```math
g(x,F)
```

containing

- trap density;
- occupation;
- capture cross sections;
- field-dependent tunneling matrix element;
- local carrier densities.

The repository's earlier variational rule

```math
-\frac{\partial g/\partial F}
{\partial(1/v)/\partial F}
=\lambda
```

is the appropriate general framework once a trustworthy `g(x,F)` is available.

The present maximin rule is a simpler robust-design limit when only exponent scales are trusted.

---

## 11. Prior-art posture

Field and band engineering in HgCdTe APDs and barrier detectors are established prior physics.

Equalizing a normalized local constraint is elementary minimax mathematics.

No novelty claim is made for the allocation rule.

Its value in this repository is conceptual:

> **the unavoidable electrostatic field should be treated as a resource to allocate according to local leakage tolerance, not as a scalar bias that must be uniform across the detector.**

---

## 12. Next decisive model

The next step should replace the abstract `F_T(x)` with an experimentally anchored defect profile.

Primary HgCdTe studies report

- LWIR trap levels that can make TAT important around `10^14 cm^-3` trap density;
- DLTS-resolved electron/hole traps and capture cross sections in multilayer HgCdTe heterostructures;
- wide-gap layers with distinct defect spectra.

The next calculation should therefore build a two- or three-region boundary with measured/fitted `E_t`, `N_t`, and capture-cross-section scales and compare

```text
exponent-equalized field allocation
versus
uniform field
versus
delta-doped / sharply localized field.
```

The goal is to determine whether realistic defect heterogeneity materially changes the optimum.