# HgCdTe TAT/BTBT Tolerance Allocation — Maximin Placement of an Unavoidable Compensation Voltage

**Date:** 2026-08-09  
**Status:** exact exponent-level allocation inequality for local inverse-field tunneling constraints; nonlocal impact ionization explicitly excluded unless a local-equilibrium reduction is justified; no novelty claim

## 1. Purpose

A graded HgCdTe collection boundary may require a fixed electrostatic compensation voltage for barrier-free minority-carrier extraction. The local gap and defect spectrum determine how much electric field a given location can tolerate before field-assisted tunneling becomes severe.

Question:

> For a fixed required voltage, where should the electric field be placed to maximize the worst local tunneling margin?

## 2. Single local tunneling mechanism

Let

```math
F_T(x)>0
```

be the local characteristic field in a tunneling exponent

```math
\exp[-F_T(x)/F(x)].
```

Assume

```math
F(x)\ge0,
\qquad
V_b=\int_0^wF(x)dx.
```

Define the worst normalized stress

```math
s[F]=\max_x\frac{F(x)}{F_T(x)}.
```

Then

```math
F(x)\le sF_T(x),
```

so

```math
V_b\le s\int_0^wF_T(x)dx.
```

Therefore

```math
\boxed{
s\ge
\frac{V_b}{\int_0^wF_T(x)dx}.
}
```

The bound is tight for

```math
\boxed{
F_{\rm opt}(x)
=
\frac{V_bF_T(x)}
{\int_0^wF_T(x')dx'}.
}
```

Hence the largest achievable minimum tunneling exponent is

```math
\boxed{
\Sigma_*=
\frac{\int_0^wF_T(x)dx}{V_b}.
}
```

At the optimum,

```math
\boxed{
F_{\rm opt}(x)/F_T(x)=1/\Sigma_*
}
```

is spatially constant.

Interpretation:

> place more of the unavoidable field where the local material can tolerate more field.

## 3. Layered form

For layers `i` of width `w_i` and characteristic field `F_{T,i}`,

```math
\sum_iF_iw_i=V_b.
```

The exact maximin allocation is

```math
\boxed{
F_i=
\frac{V_bF_{T,i}}
{\sum_jw_jF_{T,j}},
}
```

with common exponent

```math
\boxed{
\Sigma_*=
\frac{\sum_iw_iF_{T,i}}{V_b}.
}
```

## 4. Several local inverse-field mechanisms

Suppose several **local** mechanisms `m` have exponential margins

```math
\Sigma_m(x)=\frac{F_m(x)}{F(x)}.
```

If each mechanism requires at least a common exponent margin `Sigma`, define

```math
\boxed{
F_*(x)=\min_mF_m(x).
}
```

Then the same theorem applies with `F_T -> F_*`:

```math
\boxed{
\Sigma_{\rm local}^{\rm maximin}
=
\frac{\int_0^wF_*(x)dx}{V_b}.
}
```

For mechanism-specific required margins `Sigma_m^req`, define the local allowable field

```math
\boxed{
F_{\rm allow}(x)
=
\min_m\frac{F_m(x)}{\Sigma_m^{\rm req}}.
}
```

A compensation voltage is feasible under those local exponent requirements iff

```math
\boxed{
V_b\le\int_0^wF_{\rm allow}(x)dx.
}
```

This is both necessary and sufficient within the one-dimensional nonnegative-field model.

For the current HgCdTe boundary branch, appropriate local mechanisms include direct BTBT and TAT when their local WKB forms are valid.

## 5. Barrier-free boundary condition

For a local gap increase `Delta Eg` with conduction-band share `alpha`, minimum barrier-free electron extraction requires

```math
\boxed{
qV_b=\alpha\Delta E_g.
}
```

Therefore the local tunneling feasibility condition becomes

```math
\boxed{
\frac{\alpha\Delta E_g}{q}
\le
\int_0^wF_{\rm allow}(x)dx.
}
```

This turns local gap/trap quality into an integrated **voltage-handling capacity** of the boundary.

## 6. Relation to TAT

For the standard repository TAT exponent scale,

```math
\boxed{
F_{\rm TAT}(x)
=
\frac{4\sqrt{2m^*(x)}\,\Delta_t(x)^{3/2}}
{3q\hbar}.
}
```

Deep traps relative to the receiving band, larger tunneling mass, and wider local gap generally increase the field margin.

The exponent alone is not the full TAT current. Trap density, occupation, capture cross section, and matrix-element prefactors still matter.

## 7. Relation to direct BTBT

In the simplified Kane scaling,

```math
\boxed{
F_K(x)
=\frac{\pi E_g(x)^2}
{4q\hbar v_K}.
}
```

Thus a wide-gap part of the collection boundary can carry disproportionately more electrostatic field before the direct-Zener exponent collapses.

## 8. Important correction — impact ionization is generally nonlocal

The earlier version of this note placed a generic local `F_II(x)` inside `F_tol(x)`.

That is **not** valid in the thin/fast regime unless impact ionization has already been reduced to a trustworthy local-equilibrium field law.

`HGCDTE_GRADED_NONLOCAL_II_PHASE_BOUNDARY.md` shows that the mean carrier energy obeys

```math
\boxed{
\varepsilon(x)
=
\int_0^xS_c(s)
\exp\!\left[-\int_s^x\frac{du}{\ell_E(u)}\right]ds.
}
```

Thus impact-ionization access depends on the upstream conduction-band history.

The current boundary optimization must therefore be split into

```text
local constraints:
TAT + direct BTBT + process field ceilings

nonlocal state constraint:
carrier energy / impact-ionization hazard.
```

Do not hide nonlocal II inside `F_allow(x)` without demonstrating local equilibration.

## 9. Peak-field bound retained

For constant local tolerance,

```math
F_{\rm opt}=V_b/w.
```

This recovers

```math
\boxed{F_{\max}\ge V_b/w.}
```

Delta doping or depletion shaping can move the field into more favorable material but cannot supply the same positive voltage drop across the same width with a smaller peak field than the uniform-field value.

## 10. Prior-art posture

Composition grading, doping modulation, barrier engineering, TAT, and BTBT are established HgCdTe device physics. Equalizing normalized local constraints is elementary minimax mathematics.

No novelty claim is made.

The useful repository interpretation is:

> **the collection boundary has a finite local-tunneling voltage capacity, while nonlocal carrier heating must be tracked separately.**

## 11. Next step

Combine

1. the local boundary voltage-capacity condition above;
2. the nonlocal graded carrier-energy equation;
3. a finite graded absorber + collection-boundary band profile;
4. experimentally anchored trap parameters where available.

The decisive question is whether a realistic profile can simultaneously remain barrier free, keep TAT/BTBT margins acceptable, and keep the carrier-energy trajectory below the unwanted impact-ionization regime.
