# Differentiation Noise and the Spatial Resolution Law

**Date:** 2026-08-10  
**Status:** exact leading bias/variance optimization for centered finite differences under independent equal complex-log-response noise; not a universal information bound

## 1. Why this matters

The local Markov closure theorem is structurally exact.

But the arbitrary-profile version requires

```math
r=\partial_z\ln F,
```

and

```math
A=r'+r^2
=\partial_z^2\ln F+(\partial_z\ln F)^2.
```

Experimental data never provide derivatives directly.

They provide noisy samples of the complex response at finite spatial coordinates, or in the detector realization, finite wavelength-selected generation coordinates.

Thus the exact inverse has a second limitation:

> **spatial differentiation amplifies measurement noise.**

This section derives the simplest quantitative resolution law.

---

## 2. Let the measured field be the complex log response

Define one real component of

```math
y(z)=\ln F(z,\omega).
```

Assume independent equal per-point measurement noise

```math
\operatorname{Var}(\epsilon)=\sigma_y^2.
```

The same derivation applies separately to phase and log-magnitude components, with covariance whitening used in the correlated case.

---

## 3. First derivative — the two-depth gedanken experiment

Using symmetric points

```text
z0-h
z0+h
```

estimate

```math
\widehat{y'}
=\frac{y(z_0+h)-y(z_0-h)}{2h}.
```

Taylor expansion gives

```math
\boxed{
\operatorname{Bias}(\widehat{y'})
=\frac{h^2}{6}y'''(z_0)+O(h^4).
}
```

The independent-point noise variance is

```math
\boxed{
\operatorname{Var}(\widehat{y'})
=\frac{\sigma_y^2}{2h^2}.
}
```

Therefore the leading mean-squared error is

```math
\operatorname{MSE}_1(h)
\simeq
\frac{\sigma_y^2}{2h^2}
+
\frac{|y'''|^2h^4}{36}.
```

Minimizing with respect to `h` gives

```math
\boxed{
h_{1,*}
=\left(\frac{3\sigma_y}{|y'''|}\right)^{1/3}.
}
```

The full separation between the two generation coordinates is

```math
\boxed{
\Delta z_{1,*}=2h_{1,*}.
}
```

This is the natural resolution scale for the simplest two-depth logarithmic-slope experiment under these assumptions.

---

## 4. Second derivative — arbitrary-profile closure

Use

```text
z0-h
z0
z0+h
```

and

```math
\widehat{y''}
=\frac{y(z_0+h)-2y(z_0)+y(z_0-h)}{h^2}.
```

Taylor expansion gives

```math
\boxed{
\operatorname{Bias}(\widehat{y''})
=\frac{h^2}{12}y''''(z_0)+O(h^4).
}
```

The noise variance is

```math
\boxed{
\operatorname{Var}(\widehat{y''})
=\frac{6\sigma_y^2}{h^4}.
}
```

Hence

```math
\operatorname{MSE}_2(h)
\simeq
\frac{6\sigma_y^2}{h^4}
+
\frac{|y''''|^2h^4}{144}.
```

The optimum is

```math
\boxed{
h_{2,*}
=864^{1/8}
\left(
\frac{\sigma_y}{|y''''|}
\right)^{1/4}.
}
```

Numerically

```math
864^{1/8}\simeq2.3284.
```

Thus the three-point span is

```math
\boxed{
\Delta z_{2,*}=2h_{2,*}
\simeq4.6569
\left(
\frac{\sigma_y}{|y''''|}
\right)^{1/4}.
}
```

---

## 5. The important scaling difference

The two-depth slope experiment has

```math
h_{1,*}\propto\sigma_y^{1/3}.
```

The arbitrary-profile curvature experiment has

```math
h_{2,*}\propto\sigma_y^{1/4}.
```

If white-noise averaging gives

```math
\sigma_y\propto t^{-1/2},
```

then

```math
\boxed{
h_{1,*}\propto t^{-1/6},}
```

while

```math
\boxed{
h_{2,*}\propto t^{-1/8}.}
```

Consequences:

```text
64x more coherent averaging time
-> only 2x better optimum first-derivative spatial scale

256x more averaging time
-> only 2x better optimum second-derivative spatial scale.
```

This is a severe diminishing return.

---

## 6. Why the simplest gedanken experiment matters

The uniform-segment test needs only

```math
r_\omega=\partial_z\ln F.
```

The arbitrary-profile exact closure needs

```math
r_\omega'
```

as well.

Therefore the conceptual hierarchy is also a statistical hierarchy:

```text
uniform / piecewise-uniform two-depth experiment
-> first spatial derivative
-> cube-root noise-resolution law

arbitrary rapidly varying transport
-> second spatial derivative
-> fourth-root noise-resolution law.
```

This is a strong reason to formulate the paper around the **simplest falsifiable gedanken experiment first**, then present the arbitrary-profile theorem as the exact generalization.

---

## 7. Low-frequency uncertainty in drift and diffusion

In a uniform segment write

```math
r_\omega=a+ib.
```

At low RF,

```math
b\simeq\frac{\omega}{w},
```

```math
a\simeq\frac{D\omega^2}{w^3}.
```

The exact uniform inverse is

```math
D=\frac{\omega a}{b(a^2+b^2)},
```

```math
w=\frac{\omega(b^2-a^2)}{b(a^2+b^2)}.
```

To leading order, uncertainty in the measured spatial log-slope therefore propagates as

```math
\boxed{
\sigma_w
\sim
\frac{w^2}{\omega}\,\sigma_b,
}
```

and

```math
\boxed{
\sigma_D
\sim
\frac{w^3}{\omega^2}\,\sigma_a.
}
```

Thus increasing RF frequency initially improves

```text
drift precision ~ omega

diffusion precision ~ omega^2.
```

This reproduces the earlier qualitative observation from a much simpler exact asymptotic argument:

> **diffusion is much harder to measure than drift in the low-frequency limit.**

The benefit of increasing RF eventually stops when higher-order/nonlocal transport, electrical bandwidth, or poor signal invalidates the simple local model.

---

## 8. Mapping depth spacing to wavelength spacing

In the detector realization the generation coordinate is supplied by wavelength.

If a calibrated spectral generation coordinate

```math
z_g(\lambda)
```

is locally monotonic, then a small depth offset maps to

```math
\boxed{
\Delta\lambda
\simeq
\frac{\Delta z}
{|dz_g/d\lambda|}.
}
```

The previous finite-width theorem is important here:

- a broad generation kernel that translates rigidly does **not** bias the uniform transport slope;
- wavelength-dependent shape evolution contributes a calculable correction and must be propagated into `sigma_y` / model bias.

So the depth-resolution law is not simply an optical absorption-length limit.

It is a bias-variance problem combining

```text
complex-response precision
spectral-to-depth leverage
transport-profile curvature
and optical-kernel shape calibration.
```

---

## 9. This is not claimed as a universal information bound

The constants and exponents above follow from

```text
centered finite differences
independent equal point noise
known local derivative bounds
and leading Taylor truncation.
```

Multi-point local polynomial fits, correlated covariance, regularization, optimal experimental design, or stronger physical priors can change constants and sometimes rates under additional smoothness assumptions.

Therefore call this

> **the local finite-difference bias-variance resolution law**

rather than a fundamental quantum or universal resolution limit.

What is robust is the qualitative conclusion that arbitrary-profile exact inversion pays a severe statistical price for spatial differentiation.

---

## 10. Numerical verification

`numerics/spatial_derivative_bias_variance_resolution.py`

uses a quartic response field for which the central-difference bias terms are exact.

The numerically minimized MSE agrees with

```math
h_{1,*}
=\left(3\sigma_y/|y'''|\right)^{1/3}
```

and

```math
h_{2,*}
=864^{1/8}
(\sigma_y/|y''''|)^{1/4}
```

to the search-grid precision.

---

## 11. Next theory target

We now have

```text
exact structural closure
specific closure-failure archetypes
and the first statistical resolution law.
```

The next useful calculation is a **minimal three-frequency detection threshold**:

> for a specified response precision and spatial sampling, how large must the frequency dispersion of `D_app,w_app` be before local Markov drift-diffusion can be rejected at a chosen significance?

That would convert the exact null theorem into a complete falsifiable prediction with a metrology requirement.
