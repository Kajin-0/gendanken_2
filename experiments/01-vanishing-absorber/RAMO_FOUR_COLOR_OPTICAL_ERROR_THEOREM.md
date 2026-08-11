# Four-Color Shockley-Ramo Closure — Leading Optical-Shape Error

**Date:** 2026-08-10  
**Status:** asymptotic theorem for the planar homogeneous raw-current observable with mean-centered spectral source coordinates; checked against exact Gaussian source transforms; no novelty claim

## 1. Question

The exact four-color terminal-current closure

```math
(J_2-J_1)^2=(J_1-J_0)(J_3-J_2)
```

requires one rigidly translated generation shape.

A real graded absorber changes generation width and higher shape moments with wavelength.

The adversarial question is therefore:

> **How does smooth wavelength-dependent source-shape evolution enter the four-color null?**

The leading answer is more favorable than a generic first-order source-shape error.

---

## 2. Mean-depth coordinate and centered kernels

For spectral channel `m=0,1,2,3`, let the random generation distance from the collector be

```math
D_m=\mu_m+U_m,
```

with

```math
E[U_m]=0.
```

Choose the four wavelengths so their **mean generation distances** are exactly equally spaced:

```math
\boxed{
\mu_m=\mu_0+mh.
}
```

Let

```math
v_m=E[U_m^2]
```

be the centered generation variance.

For homogeneous planar single-carrier propagation with spatial exponent `gamma`, remove the common current prefactor and write

```math
\boxed{
J_m=1-E[e^{-\gamma D_m}].
}
```

The source transform is

```math
E[e^{-\gamma D_m}]
=e^{-\gamma\mu_m}
M_m(-\gamma),
```

where

```math
M_m(-\gamma)
=1+\frac{\gamma^2v_m}{2}
-\frac{\gamma^3\kappa_{3,m}}{6}
+O(\gamma^4).
```

The absence of a linear term follows exactly from mean centering.

---

## 3. First-difference expansion

Define

```math
\Delta J_m=J_{m+1}-J_m.
```

Expanding through the first source-shape-sensitive order gives

```math
\Delta J_m
=K\gamma h
\left[
1
-\gamma
\left(
\mu_m+\frac h2+
\frac{v_{m+1}-v_m}{2h}
\right)
+O(\gamma^2)
\right],
```

where `K` is a common factor irrelevant to the closure.

Use the logarithmic four-color residual

```math
\boxed{
\mathcal C_4
=2\ln\Delta J_1
-\ln\Delta J_0
-\ln\Delta J_2.
}
```

The affine mean-depth terms cancel because the `mu_m` are equally spaced.

The first surviving variance term is

```math
\boxed{
\mathcal C_{4,opt}
=
\frac{\gamma}{2h}
\left(
v_3-3v_2+3v_1-v_0
\right)
+O(\gamma^2).
}
\tag{1}
```

Equivalently,

```math
\boxed{
\mathcal C_{4,opt}
=
\frac{\gamma}{2h}\Delta^3v
+O(\gamma^2).
}
\tag{2}
```

---

## 4. Strong consequence

The forward third difference annihilates every quadratic function of the channel index.

Therefore source-width evolution of the form

```text
constant
linear
quadratic
```

produces **no `O(gamma)` four-color closure error**.

Only cubic-and-higher spatial curvature of the variance contributes at first order.

For a smooth variance field `v(mu)`, since

```math
\Delta^3v
=h^3v'''(\mu)+O(h^4),
```

Eq. (2) becomes

```math
\boxed{
\mathcal C_{4,opt}
\simeq
\frac{\gamma h^2}{2}v'''(\mu)
+O(\gamma h^3,\gamma^2).
}
\tag{3}
```

Thus the combination

```text
mean-depth calibration
+ first spatial difference
+ second log-difference closure
```

suppresses low-order smooth optical-width evolution automatically.

---

## 5. What happens at the next order

When `Delta^3 v=0`, optical corrections do not vanish identically.

They begin at `O(gamma^2)` through combinations of

```text
variance curvature,
centered skewness evolution,
and products of lower centered moments.
```

For example, an exact Gaussian family with quadratically varying variance has zero linear term but a nonzero `O(gamma^2)` closure.

Therefore Eq. (2) is a **leading asymptotic protection**, not permission to ignore optical modeling.

---

## 6. Comparison with the old three-color arrival-flux optical correction

For the ideal arrival observable, mean centering suppresses source-shape error through first order in `gamma`; the leading variance correction enters `O(gamma^2)` directly.

For raw Shockley-Ramo current, the affine particular solution changes the algebra.  After first differencing, smooth variance evolution can enter at `O(gamma)`, but only through its **third discrete difference**.

So the two observables have different error hierarchies.

This is another reason they must not be conflated.

---

## 7. Falsifiable use

A practical theory test should therefore:

1. calibrate each wavelength's mean generation depth;
2. choose four wavelengths with equal mean-depth spacing;
3. calculate the centered variance and higher optical moments from an independent optical model;
4. predict the optical contribution to `C4`;
5. compare the remaining residual with the spatial/RF transport closures.

If the measured `O(gamma)` closure is much larger than the independently predicted

```math
\frac{\gamma}{2h}\Delta^3v,
```

then smooth generation-width evolution alone is insufficient.

---

## 8. Numerical regression

`numerics/ramo_four_color_optical_shape_error.py`

uses exact Gaussian source transforms and verifies:

```text
constant variance -> zero O(gamma) error
linear variance -> zero O(gamma) error
quadratic variance -> zero O(gamma) error, residual starts O(gamma^2)
cubic variance -> predicted gamma Delta^3(v)/(2h) coefficient.
```

This closes one of the largest practical loopholes in the four-color theorem without assuming delta-function optical generation.
