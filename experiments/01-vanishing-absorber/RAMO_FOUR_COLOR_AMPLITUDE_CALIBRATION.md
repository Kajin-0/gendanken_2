# Four-Color Shockley-Ramo Closure — Spectral Amplitude Calibration Error

**Date:** 2026-08-10  
**Status:** **DERIVED / CHECKED / CONDITIONAL** low-RF/high-SNR result for multiplicative channel-calibration error; no novelty claim

## 1. Why relative channel amplitude matters

The raw-current four-color theorem assumes the response is compared **per calibrated generated-carrier modulation amplitude**.

If different wavelengths create different modulated carrier populations or see different external gains, an uncorrected multiplicative factor can break the closure even when transport is perfectly homogeneous.

At first sight this appears to require extremely accurate absolute calibration because the raw current is much larger than the spatial current difference.

The finite-difference structure gives a more favorable result for smooth calibration error.

---

## 2. Low-RF affine-current limit

For one conserved carrier in the minimal planar geometry, the DC / sufficiently low-RF raw current is locally affine in internal source coordinate.

For four equally spaced channels write

```math
\boxed{
J_m=A+Bm,
\qquad m=0,1,2,3.
}
```

The exact ideal closure is zero.

Suppose imperfect amplitude calibration leaves a small fractional channel error

```math
\widetilde J_m
=(1+\epsilon_m)J_m.
```

Define

```math
\mathcal C_4
=2\ln\Delta J_1
-\ln\Delta J_0
-\ln\Delta J_2.
```

---

## 3. Exact first variation

Let

```math
\delta J_m=\epsilon_mJ_m.
```

Linearizing the log closure gives

```math
\delta\mathcal C_4
=\frac{2(\delta J_2-\delta J_1)
-(\delta J_1-\delta J_0)
-(\delta J_3-\delta J_2)}{B}.
```

Therefore

```math
\boxed{
\delta\mathcal C_4
=-\frac{\Delta^3(\epsilon_mJ_m)}{B},
}
\tag{1}
```

where

```math
\Delta^3 f_0
=f_3-3f_2+3f_1-f_0.
```

Thus amplitude-calibration error enters through a **third spatial difference** of the calibration-weighted current.

---

## 4. Constant and linear fractional calibration drift cancel

Because `J_m` is affine in `m`:

### Constant fractional error

```math
\epsilon_m=\epsilon_0
```

makes

```math
\epsilon_mJ_m
```

a linear sequence, so

```math
\boxed{
\delta\mathcal C_4=0.
}
```

### Linear fractional error

```math
\epsilon_m=\epsilon_0+\epsilon_1m
```

makes

```math
\epsilon_mJ_m
```

quadratic, so again

```math
\boxed{
\delta\mathcal C_4=0
}
```

to first order.

Therefore the four-color null does **not** require tiny absolute gain error or zero spectral gain slope.

It is sensitive first to spectral **curvature** in the relative amplitude calibration.

---

## 5. Quadratic calibration curvature

If

```math
\epsilon_m=c_2m^2,
```

then

```math
\boxed{
\delta\mathcal C_4=-6c_2.
}
\tag{2}
```

at first order.

This result is independent of the affine-current intercept `A` and slope `B`.

So the natural calibration quantity is not

```text
absolute gain accuracy
```

but rather

```text
unmodeled channel-to-channel curvature after mapping wavelength to the internal source coordinate.
```

---

## 6. Smooth-coordinate form

Let the four internal coordinates be

```math
z_m=z_0+mh
```

and let

```math
J(z)\simeq J_c+G(z-z_c)
```

be locally affine.

For a smooth fractional calibration field `epsilon(z)`, Eq. (1) gives asymptotically

```math
\boxed{
\delta\mathcal C_4
\simeq
-h^2
\left[
3\epsilon''(z_c)
+\frac{J(z_c)}{G}\epsilon'''(z_c)
\right]
+O(h^3).
}
\tag{3}
```

Thus smooth calibration error follows the same general design principle as the optical-source-shape error:

> **low-order smooth variation is rejected; higher spatial curvature is the dangerous component.**

---

## 7. Independent calibration error is still dangerous

The cancellation above does **not** protect against uncorrelated channel errors.

For arbitrary small `epsilon_m`, the first-order coefficients are

```math
\delta\mathcal C_4
=
\frac{J_0}{d_0}\epsilon_0
-J_1\left(\frac1{d_0}+\frac2{d_1}\right)\epsilon_1
+J_2\left(\frac2{d_1}+\frac1{d_2}\right)\epsilon_2
-\frac{J_3}{d_2}\epsilon_3,
```

where

```math
d_m=J_{m+1}-J_m.
```

When `|J| >> |d|`, irregular relative-calibration errors can be strongly amplified.

A practical experiment should therefore aim for

```text
smooth/common optical power control,
relative generated-pair calibration,
and correlated channel metrology,
```

rather than interpreting this theorem as permission for arbitrary wavelength-dependent gain error.

---

## 8. Relation to the optical-shape theorem

Two superficially different systematic errors now have closely related finite-difference structure.

### Generation-kernel shape evolution

Leading variance error:

```math
\mathcal C_{4,opt}
\propto
\Delta^3\sigma_z^2.
```

### Multiplicative spectral amplitude calibration

Low-RF first-order error:

```math
\delta\mathcal C_4
\propto
\Delta^3(\epsilon J).
```

This is not accidental.

The four-color observable is fundamentally a third-difference-like closure after one spatial difference has isolated the propagator.

That gives it strong rejection of low-order smooth structure while amplifying high-spatial-frequency noise/error.

---

## 9. Numerical regression

`numerics/ramo_four_color_amplitude_calibration.py`

verifies:

```text
constant fractional error -> zero first-order closure
linear fractional error -> zero first-order closure
quadratic fractional error -> -6 c2
smooth-coordinate asymptotic formula
```

against the exact logarithmic closure.

---

## 10. Paper-level consequence

The calibration requirement can now be stated more precisely:

> **The four-color null is insensitive to common relative amplitude and, in the low-RF affine-current limit, to a linear spectral calibration drift at first order.  The leading concern is unmodeled spectral curvature or channel-to-channel irregularity after converting wavelength to internal generation coordinate.**

This is substantially less restrictive—and more experimentally meaningful—than demanding identical absolute optical amplitude at all four wavelengths.
