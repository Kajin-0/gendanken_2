# Four-Color Shockley-Ramo Closure — Low-RF Slowness-Gradient Theorem

**Date:** 2026-08-10  
**Status:** **DERIVED / CHECKED / CONDITIONAL** for one-dimensional deterministic downstream transit with uniform planar weighting field; high-Peclet limiting theorem, not a generic photodiode identity; no novelty claim

## 1. Question

After the Shockley-Ramo observable correction, the homogeneous single-carrier terminal-current null is

```math
\boxed{
(J_2-J_1)^2=(J_1-J_0)(J_3-J_2).
}
```

A failed closure can indicate nonuniform transport, but that statement alone is qualitative.

The sharper question is:

> **If the carrier velocity varies slowly with depth, what physical quantity does the leading low-RF four-color phase closure measure?**

In the deterministic/high-Peclet limit, the answer is an explicit local combination of the first and second spatial derivatives of the transit slowness.

For locally linear slowness, the result becomes a direct measurement of the inverse-velocity gradient.

---

## 2. Deterministic downstream transit

Let `z` increase toward a collector at `L`.

Define the positive local transit slowness

```math
\boxed{
q(z)=\frac{1}{v(z)}.
}
```

A carrier generated at `z` reaches position `x>z` after

```math
\boxed{
\tau(z,x)=\int_z^x q(u)du.
}
```

With a uniform planar weighting field, the induced current is proportional to the carrier velocity while it traverses the device.

Changing integration variable from time to position cancels that velocity factor, giving the frequency-domain point-source current, up to one depth-independent complex prefactor,

```math
\boxed{
J(z,s)
=K\int_z^L
\exp\!\left[-s\int_z^xq(u)du\right]dx.
}
\tag{1}
```

For RF response,

```math
s=i\omega.
```

Equation (1) is exact for the stated deterministic planar model.

---

## 3. Low-frequency expansion

Expand the exponential in `s`:

```math
J(z,s)
=K\left[
(L-z)-sA(z)+O(s^2)
\right],
```

where

```math
\boxed{
A(z)
=\int_z^L(L-u)q(u)du.
}
\tag{2}
```

The first derivative is

```math
A'(z)=-(L-z)q(z).
```

Therefore

```math
A'''(z)
=2q'(z)-(L-z)q''(z).
\tag{3}
```

This derivative will control the four-color closure.

---

## 4. Four equally spaced internal generation coordinates

Take

```math
z_m=z_0+mh,
\qquad m=0,1,2,3,
```

and define first differences

```math
\Delta J_m=J(z_{m+1})-J(z_m).
```

Use the logarithmic closure

```math
\boxed{
\mathcal C_4
=2\ln\Delta J_1
-\ln\Delta J_0
-\ln\Delta J_2.
}
\tag{4}
```

The depth-independent current prefactor and the common sign of the low-RF differences cancel from Eq. (4).

Let the quartet midpoint be

```math
\boxed{
z_c=z_0+\frac{3h}{2}.
}
```

A centered finite-difference expansion gives

```math
\boxed{
\mathcal C_4
=-s h^2
\left[
2q'(z_c)
-(L-z_c)q''(z_c)
\right]
+O(sh^4,s^2).
}
\tag{5}
```

This is the low-RF four-color slowness-gradient theorem.

---

## 5. Locally linear slowness — direct inverse-velocity-gradient measurement

If `q(z)` is locally linear across the quartet,

```math
q''(z_c)=0,
```

so Eq. (5) reduces to

```math
\boxed{
\mathcal C_4
=-2s h^2 q'(z_c)
+O(sh^4,s^2).
}
\tag{6}
```

At RF,

```math
s=i\omega,
```

therefore

```math
\boxed{
\frac{\operatorname{Im}\mathcal C_4}{\omega}
=-2h^2\frac{d}{dz}\left(\frac1v\right)_{z_c}
}
\tag{7}
```

at leading order.

Thus the four-color phase closure is not merely sensitive to velocity variation.

> **In the deterministic/high-Peclet locally linear limit, its low-RF slope directly measures the spatial gradient of inverse carrier velocity.**

No absolute RF gain or common phase is required.

---

## 6. Sign prediction

For downstream transport becoming slower with depth,

```math
q'(z_c)>0,
```

Eq. (7) predicts

```math
\operatorname{Im}\mathcal C_4<0
```

for the `e^{-i\omega t}` convention.

If transport becomes faster with depth,

```math
q'(z_c)<0,
```

the low-RF phase-closure sign reverses.

This is a direct falsifiable sign prediction under the stated assumptions.

---

## 7. Why the `q''` term matters

For a curved slowness profile, the leading closure is not purely local `q'`:

```math
\mathcal C_4/( -s h^2)
=2q'-(L-z_c)q''.
```

The factor

```math
L-z_c
```

appears because Shockley-Ramo current accumulates continuously over the **remaining path to the collector**.

This is physically different from an ideal point-arrival observable.

A paper should therefore not claim arbitrary pointwise velocity-gradient tomography from one quartet.

Instead:

```text
locally linear q -> direct q' measurement
curved q -> known q',q'' combination
multiple translated quartets -> additional spatial information.
```

---

## 8. Relation to homogeneous closure

If

```math
q'(z)=q''(z)=0,
```

Eq. (5) gives

```math
\mathcal C_4=O(s^2)
```

and the exact homogeneous theorem gives

```math
\mathcal C_4=0
```

at every RF frequency.

Thus Eq. (5) is the perturbative departure from the exact four-color homogeneous null.

---

## 9. Optical-shape correction must be kept separate

Real wavelength-selected generation kernels have finite width and can change shape with wavelength.

The independent optical-error theorem gives, for four channels selected by equally spaced **mean generation depth**,

```math
\mathcal C_{4,opt}
=\frac{\gamma}{2h}\Delta^3\sigma_z^2
+O(\gamma^2).
```

Therefore a measured low-RF phase closure contains at least two conceptually distinct contributions:

```text
transport slowness curvature
and
wavelength-dependent generation-shape evolution.
```

The optical term is calculable from an independently specified absorption model.

The transport theorem should be tested only after that correction/error budget is propagated.

---

## 10. Noise tradeoff

The same spatial differencing that removes common signal terms amplifies uncorrelated sample noise.

For equal first differences `|Delta J|=|d|`, the independent-complex-noise result is

```math
\boxed{
\sigma_{\mathcal C_4}
\simeq
\sqrt{20}\frac{\sigma_J}{|d|}.
}
```

At low RF, `|d|` scales approximately with the spatial spacing `h`, while the locally linear transport signal in Eq. (6) scales as `h^2`.

So increasing spacing initially improves transport-closure SNR strongly, but eventually worsens locality, source-shape evolution, and boundary exposure.

This creates a genuine optimization problem rather than a reason to take `h` arbitrarily small.

---

## 11. Numerical regression

`numerics/ramo_four_color_slowness_gradient.py`

uses a smooth nonlinear positive `q(z)`, evaluates the full RF integral in Eq. (1), and verifies that

```math
\frac{\mathcal C_4}{i\omega}
\to
-h^2[2q'-(L-z_c)q'']
```

as `omega -> 0`.

The direct numerical response converges to the analytic coefficient to the regression tolerance.

---

## 12. Paper-level role

This theorem supplies the clearest **prediction after a controlled failure of the homogeneous four-color null**.

The manuscript logic can be:

```text
homogeneous one-carrier model
-> exact C4=0

observe C4 != 0
-> first rule out source-shape / extra-mode explanations

if one spatial mode remains adequate and high-Peclet deterministic transport is appropriate
-> low-RF Im(C4)/omega predicts the local slowness-gradient combination.
```

That keeps the falsification hierarchy logically ordered and avoids interpreting every closure residual as a velocity gradient by default.
