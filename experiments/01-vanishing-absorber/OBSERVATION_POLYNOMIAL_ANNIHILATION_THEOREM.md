# Polynomial Observation-Forcing Annihilation — Higher-Order Spectral Closure

**Date:** 2026-08-11  
**Status:** **DERIVED / CHECKED / CONDITIONAL** for homogeneous constant-coefficient transport with polynomial observation forcing over the sampled region; no novelty claim for finite-difference annihilation

## 1. Motivation

The nonuniform-weighting-field stress showed that a locally linear weighting field changes the raw-current particular solution from a constant to a linear function of source depth.

That breaks the four-color first-difference one-mode law.

But the failure has algebraic structure and can be removed exactly.

---

## 2. General homogeneous forced transport equation

Let the homogeneous spatial transport operator at one `s` be

```math
\mathcal L_s
=D\partial_z^2+w\partial_z-(\kappa+s).
```

Suppose the raw-current observable satisfies

```math
\mathcal L_s J(z)=-F_p(z),
```

where `F_p(z)` is a polynomial of degree at most `p` across the sampled region.

For `kappa+s != 0`, a polynomial particular solution of degree at most `p` exists.

In the one-admissible-spatial-root geometry used by the headline theorem,

```math
\boxed{
J(z)=P_p(z)+B e^{rz},
}
\tag{1}
```

where `P_p` is a polynomial of degree at most `p`.

A polynomial weighting field `E_w(z)` of degree `p` generates precisely this structure because

```math
F_p=wE_w+D E_w'
```

has degree at most `p`.

---

## 3. Finite differences annihilate the observation particular solution

Sample equally spaced internal coordinates

```math
z_m=z_0+mh.
```

The `(p+1)`-th forward spatial difference annihilates any degree-`p` polynomial:

```math
\Delta^{p+1}P_p(z_m)=0.
```

For the exponential mode,

```math
\Delta^{p+1}e^{rz_m}
=(e^{rh}-1)^{p+1}e^{rz_m}.
```

Therefore

```math
\boxed{
Y_m
\equiv\Delta^{p+1}J_m
=B(q-1)^{p+1}q^m,
\qquad
q=e^{rh}.
}
\tag{2}
```

The filtered sequence is exactly geometric.

Hence

```math
\boxed{
Y_1^2=Y_0Y_2.
}
\tag{3}
```

To obtain the three consecutive filtered samples `Y_0,Y_1,Y_2`, the minimum number of raw spectral channels is

```math
\boxed{N_{color}=p+4.}
\tag{4}
```

---

## 4. Familiar cases

### Uniform weighting field / constant forcing

`p=0`.

Use first differences and four colors:

```math
\boxed{
(\Delta J_1)^2=(\Delta J_0)(\Delta J_2).
}
```

This is the headline four-color theorem.

### Linear weighting field / affine forcing

`p=1`.

Use second differences and five colors:

```math
\boxed{
(\Delta^2J_1)^2
=(\Delta^2J_0)(\Delta^2J_2).
}
\tag{5}
```

Explicitly,

```math
\boxed{
(J_3-2J_2+J_1)^2
=(J_2-2J_1+J_0)
(J_4-2J_3+J_2).
}
\tag{6}
```

A linear weighting-field gradient is therefore **exactly annihilated** under the homogeneous one-mode transport hypothesis.

### Quadratic observation forcing

`p=2`.

Use third differences and six colors.

This is distinct from using six colors to identify two transport modes: here the additional colors are spent annihilating a known low-order observation polynomial while retaining one transport exponential.

---

## 5. Noise price

Exact nuisance annihilation is not free.

Let

```math
n=p+1
```

be the spatial-difference order and assume independent equal complex raw-current noise `sigma_J`.

In the near-equal filtered-sample limit, linearization of the log geometric closure gives a raw-noise stencil equal to the `(n+2)`-th finite difference.

Using

```math
\sum_{k=0}^{m}\binom{m}{k}^2
=\binom{2m}{m},
```

with `m=n+2`,

```math
\boxed{
\sigma_C
\simeq
\sqrt{\binom{2n+4}{n+2}}
\frac{\sigma_J}{|\Delta^n J|}.
}
\tag{7}
```

Examples:

| observation degree `p` | difference order `n` | colors | raw-noise coefficient |
|---:|---:|---:|---:|
| 0 | 1 | 4 | `sqrt(20)=4.472` |
| 1 | 2 | 5 | `sqrt(70)=8.367` |
| 2 | 3 | 6 | `sqrt(252)=15.875` |
| 3 | 4 | 7 | `sqrt(924)=30.397` |

There is an additional low-RF penalty because

```math
\Delta^n J
\propto(q-1)^n.
```

For `|rh| << 1`, every extra nuisance-annihilating difference costs approximately another factor `|rh|` in signal amplitude.

Relative to the ordinary four-color first-difference null, the five-color linear-weighting-immune construction has an approximate raw-current SNR penalty

```math
\boxed{
\frac{\mathrm{SNR\ cost}_{5}}
{\mathrm{SNR\ cost}_{4}}
\sim
\sqrt{70/20}\,|q-1|^{-1}
\simeq
1.87\,|rh|^{-1}.
}
\tag{8}
```

Thus exact observation immunity can be statistically very expensive at low RF.

---

## 6. Numerical sanity check

For a homogeneous deterministic transport stress with

```text
v = 3.45e4 m/s
RF = 100 MHz
h = 0.5 um
```

and a linear weighting field changing by 1% across 1.5 um, the ordinary four-color closure gives approximately

```text
+0.00184 deg
```

phase failure in a point-source stress.

The five-color second-difference closure is zero to numerical quadrature precision (`~1e-12` in complex log-closure magnitude).

This confirms the analytic annihilation theorem.

---

## 7. Experimental interpretation

There are now two legitimate ways to handle a simple weighting-field gradient:

### Route A — identify it

Use the ordinary six-color first-difference rank-two hierarchy.

A linear weighting field contributes one root

```math
q_{weight}=1.
```

This preserves more low-RF signal but requires the second mode to be statistically resolved.

### Route B — annihilate it

Use five colors and second differences.

This removes the linear observation particular term exactly without root fitting, but incurs a severe noise penalty when `|rh|` is small.

The choice is therefore an explicit statistics-versus-systematics tradeoff rather than an unquantified device-geometry assumption.

---

## 8. Paper consequence

The paper no longer needs to frame sub-percent weighting-field uniformity as the only route to a clean transport test.

A stronger statement is available:

> **Low-order observation nonuniformity can either be identified as extra spatial rank or annihilated by raising the finite-difference order.**

The minimal four-color law remains the most statistically efficient lowest-rung test. Higher-order color closures are robustness options when the observation operator is known to vary smoothly but cannot be made sufficiently uniform.
