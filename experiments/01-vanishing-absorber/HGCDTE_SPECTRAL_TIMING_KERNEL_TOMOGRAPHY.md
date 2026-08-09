# HgCdTe Spectral Timing Kernel Tomography — Finite Absorption Depth as a Spatial Point-Spread Function

**Date:** 2026-08-09  
**Status:** exact asymptotic kernel result for a linear gap and local power-law absorption edge, combined with path-additive transport; generalizes the pointwise velocity inversion; no novelty claim

## 1. Purpose

`HGCDTE_SPECTRAL_TIMING_VELOCITY_INVERSION.md` derived the sharp-generation relation

```math
v_{\rm eff}[x_g(E_\gamma)]
=\frac1{G\,dT/dE_\gamma}.
```

A real absorber has a finite spatial generation distribution.

The first question is therefore not whether the inversion fails, but what quantity the timing derivative measures once the optical generation region has finite width.

For a linear graded gap and a local power-law absorption edge, the answer is unusually clean:

> **the finite optical absorption width acts as a stationary spatial point-spread kernel, and the spectral timing derivative measures a kernel-averaged inverse carrier velocity.**

---

## 2. Linear gap and local absorption edge

Use

```math
E_g(x)=E_{g,\rm in}-Gx,
\qquad G>0.
```

For

```math
E_{g,\rm out}<E_\gamma<E_{g,\rm in},
```

define the earliest allowed generation point

```math
\boxed{
x_g=\frac{E_{g,\rm in}-E_\gamma}{G}.
}
```

Measure downstream distance from this point:

```math
\boxed{z=x-x_g\ge0.}
```

Then

```math
E_\gamma-E_g(x)=Gz.
```

Take the local absorption law

```math
\boxed{
\alpha(z)=C(Gz)^\beta,
\qquad \beta>-1.
}
```

Crucially, when written in the relative coordinate `z`, `alpha(z)` no longer contains `E_gamma`.

---

## 3. Stationary generation-offset kernel

The survival probability to offset `z` is

```math
S(z)
=\exp\!\left[-\int_0^z\alpha(s)ds\right].
```

Hence

```math
\boxed{
S(z)
=\exp\!\left[
-\frac{CG^\beta}{\beta+1}
z^{\beta+1}
\right].
}
```

The untruncated absorption-position density is

```math
p(z)=\alpha(z)S(z).
```

Therefore

```math
\boxed{
p(z)
=CG^\beta z^\beta
\exp\!\left[
-\frac{CG^\beta}{\beta+1}
z^{\beta+1}
\right],
\qquad z\ge0.
}
```

This is a Weibull density.

Define

```math
n=\beta+1,
```

and the optical spatial scale

```math
\boxed{
\ell_\alpha
=\left(
\frac{n}{CG^\beta}
\right)^{1/n}.
}
```

Then

```math
\boxed{
p(z)
=\frac{n}{\ell_\alpha}
\left(\frac{z}{\ell_\alpha}\right)^{n-1}
\exp\!\left[-(z/\ell_\alpha)^n\right].
}
```

The kernel shape and length scale depend on the local absorption physics and gap slope, but **not on photon energy** as long as downstream truncation is negligible.

---

## 4. Mean optical offset

The mean generation offset is

```math
\boxed{
\langle z\rangle
=\ell_\alpha
\Gamma\!\left(1+\frac1n\right).
}
```

The variance is

```math
\boxed{
\operatorname{Var}(z)
=\ell_\alpha^2
\left[
\Gamma\!\left(1+\frac2n\right)
-\Gamma^2\!\left(1+\frac1n\right)
\right].
}
```

Thus finite absorption depth introduces a calculable spatial resolution scale.

---

## 5. Path-additive transport

Let

```math
q(x)=\frac1{v_{\rm eff}(x)}.
```

For a carrier generated at `x`, take

```math
\boxed{
T(x)=\int_x^L q(s)ds.
}
```

When the absorber is sufficiently long downstream that the Weibull generation kernel is effectively untruncated, the mean measured intrinsic delay is

```math
\boxed{
\bar T(x_g)
=\int_0^\infty p(z)T(x_g+z)dz.
}
```

Because `p(z)` is stationary with respect to `x_g`, differentiation is simple:

```math
\frac{d\bar T}{dx_g}
=\int_0^\infty p(z)T'(x_g+z)dz.
```

Since

```math
T'(x)=-q(x),
```

```math
\boxed{
\frac{d\bar T}{dx_g}
=-\int_0^\infty p(z)q(x_g+z)dz.
}
```

Using

```math
dx_g/dE_\gamma=-1/G,
```

we obtain

```math
\boxed{
G\frac{d\bar T}{dE_\gamma}
=\int_0^\infty
p(z)
\frac{dz}{v_{\rm eff}(x_g+z)}.
}
```

This is the central finite-depth result.

---

## 6. Interpretation: harmonic-type spatial averaging

Define the kernel-averaged inverse velocity

```math
\boxed{
\langle v^{-1}\rangle_p(x_g)
=\int_0^\infty
p(z)
\frac{dz}{v_{\rm eff}(x_g+z)}.
}
```

Then

```math
\boxed{
G\frac{d\bar T}{dE_\gamma}
=\langle v^{-1}\rangle_p(x_g).
}
```

Therefore the direct spectral inversion gives

```math
\boxed{
v_{\rm spec}(x_g)
\equiv
\left[
G\frac{d\bar T}{dE_\gamma}
\right]^{-1}
=
\frac1{\langle v^{-1}\rangle_p}.
}
```

So `v_spec` is a **kernel-weighted harmonic-type effective velocity**, not necessarily the point value `v_eff(x_g)`.

The sharp-generation inversion is recovered when

```math
p(z)\to\delta(z).
```

---

## 7. Slowly varying velocity limit

If

```math
q(x)=1/v_{\rm eff}(x)
```

varies slowly over `ell_alpha`, expand around `x_g`:

```math
q(x_g+z)
=q(x_g)+zq'(x_g)+\frac{z^2}{2}q''(x_g)+\cdots.
```

Then

```math
\boxed{
G\frac{d\bar T}{dE_\gamma}
=q(x_g)
+\langle z\rangle q'(x_g)
+\frac{\langle z^2\rangle}{2}q''(x_g)
+\cdots.
}
```

To first order, the measurement behaves approximately like a point measurement shifted downstream by the mean optical offset:

```math
\boxed{
G\frac{d\bar T}{dE_\gamma}
\approx
q(x_g+\langle z\rangle).
}
```

Thus finite absorption depth produces both

```text
spatial smoothing
+
a downstream registration offset.
```

---

## 8. Resolution criterion

The pointwise inversion is accurate only if the transport profile changes slowly over the optical kernel.

A natural criterion is

```math
\boxed{
\ell_\alpha
\left|\frac{d\ln q}{dx}\right|
\ll1.
}
```

Equivalently,

```math
\boxed{
\ell_\alpha
\left|\frac{d\ln v_{\rm eff}}{dx}\right|
\ll1.
}
```

If this fails, the wavelength sweep still carries spatial information, but deconvolution is required.

---

## 9. Downstream truncation near the long-wave cutoff

The eligible region has finite remaining length

```math
\boxed{
d_\gamma=L-x_g.}
```

Its total optical depth is

```math
\boxed{
\tau_\gamma
=\left(
\frac{d_\gamma}{\ell_\alpha}
\right)^n.
}
```

When

```math
\tau_\gamma\gg1,
```

the infinite-kernel approximation is exponentially accurate.

Near the long-wave cutoff,

```math
\tau_\gamma\lesssim1,
```

the kernel is strongly truncated and normalized conditionally on absorption:

```math
\boxed{
p_T(z|\mathrm{abs})
=\frac{p(z)}{1-e^{-\tau_\gamma}},
\qquad
0<z<d_\gamma.
}
```

Now both the upper limit and normalization depend on photon energy.

The simple convolution identity no longer holds exactly.

Therefore the direct tomography should avoid the extreme cutoff region unless the full truncated kernel is included in the inversion.

---

## 10. Finite-depth inverse problem

In the general case,

```math
\boxed{
\bar T(E_\gamma)
=\int_{x_g(E_\gamma)}^L
p(x|E_\gamma,\mathrm{abs})
\left[
\int_x^L q(s)ds
\right]dx.
}
```

This is a linear integral map from

```math
q(x)=1/v_{\rm eff}(x)
```

to measured delay.

Once `E_g(x)` and `alpha(E_gamma,x)` are known, reconstructing `q(x)` becomes a regularized linear inverse problem.

The physical quantity inferred most naturally is **inverse velocity / local delay density**, not velocity itself.

This is important because the measured delay is linear in `q`.

---

## 11. Why this is experimentally attractive

A compositionally graded absorber supplies three things at once:

1. a known wavelength-to-position map from `E_g(x)`;
2. a calculable optical spatial point-spread function from `alpha(E_gamma,x)`;
3. a timing observable that integrates local carrier delay downstream from the generation point.

Thus a wavelength sweep can potentially recover the spatial distribution of carrier delay without a scanned optical spot inside the device.

The band-gap gradient acts as an **internal spectral coordinate encoder**.

---

## 12. Relation to ordinary wavelength-dependent photodiode bandwidth

Wavelength-dependent photodiode response caused by different absorption depths is established semiconductor-detector physics.

The present result is narrower:

> use a known monotonic band-gap profile to turn photon energy into an internal spatial coordinate and invert the derivative of timing to recover a local or kernel-averaged transport quantity.

Whether this exact inversion/tomographic interpretation is already present in prior detector literature remains to be assessed separately.

No novelty claim is made here.

---

## 13. Claim boundary

### Derived under stated assumptions

- stationary Weibull generation-offset kernel for a linear gap plus local power-law absorption edge;
- kernel-averaged inverse-velocity identity
  ```math
  Gd\bar T/dE_\gamma
  =\int p(z)/v(x_g+z)dz;
  ```
- optical spatial-resolution scale `ell_alpha`;
- pointwise inversion as the narrow-kernel limit.

### Conditional

- monotonic linear gap;
- local absorption coefficient depending only on `E_gamma-E_g` with fixed `C,beta`;
- path-additive mean transport delay;
- negligible downstream truncation for the stationary-kernel identity.

### Open

- realistic HgCdTe `alpha(E,x,T)` and its composition dependence;
- uniqueness/stability of deconvolution with experimental noise;
- transport nonlocality beyond a local delay density;
- priority / novelty.

---

## 14. Next decisive work

1. collision-test the tomography interpretation against high-speed photodiode literature on wavelength-dependent absorption depth and transit time;
2. build a synthetic inversion using a known nonuniform `v_eff(x)` and finite optical depth;
3. quantify spatial resolution and reconstruction bias versus `tau_gamma` and `ell_alpha`;
4. only then consider using a real HgCdTe absorption model.
