# Four-Color Shockley-Ramo Closure — Bias/Noise Spacing Law

**Date:** 2026-08-10  
**Status:** **DERIVED / CHECKED / CONDITIONAL** design law for the stated high-SNR noise and smooth-source-error model; not a universal information bound

## 1. Why spacing cannot be arbitrarily small

The four-color closure uses four equally spaced internal mean-generation coordinates separated by `h`.

Reducing `h` improves locality and suppresses smooth optical-shape evolution, but it also shrinks the current differences on which the closure is built.

For independent current noise, the two effects scale in opposite directions.

This produces an analytic optimal spacing.

---

## 2. Leading smooth optical systematic

The optical-shape theorem gives

```math
\mathcal C_{4,opt}
\simeq
\frac{\gamma h^2}{2}
\frac{d^3\sigma_z^2}{d\mu^3}
```

for smooth variance evolution in the mean-generation coordinate `mu`.

Write the magnitude of the leading systematic as

```math
\boxed{
|b(h)|=A h^2,
}
```

with

```math
A
=\frac12
\left|\gamma
\frac{d^3\sigma_z^2}{d\mu^3}
\right|
```

for this particular leading optical term.

Higher moments and other calibrated systematics can change `A`; the `h^2` scaling is the ingredient used below.

---

## 3. Independent current noise

For equal complex sample noise with

```math
E|\epsilon_m|^2=\sigma_J^2,
```

the high-SNR four-color closure has, in the equal-difference limit,

```math
\sigma_{\mathcal C_4}
\simeq
\sqrt{20}\frac{\sigma_J}{|\Delta J|}.
```

At sufficiently small spacing,

```math
|\Delta J|
\simeq G_J h,
```

where

```math
G_J
=\left|\frac{\partial J}{\partial\mu}\right|
```

is the local current change per unit internal source displacement.

Therefore

```math
\boxed{
\sigma_{\mathcal C_4}
=\frac{B}{h},
\qquad
B=\sqrt{20}\frac{\sigma_J}{G_J}.
}
```

---

## 4. Mean-square optimum

Approximate the closure mean-square error by

```math
\boxed{
MSE(h)
=A^2h^4+\frac{B^2}{h^2}.
}
```

Differentiate:

```math
\frac{dMSE}{dh}
=4A^2h^3-2B^2h^{-3}.
```

The unique positive optimum is

```math
\boxed{
h_*
=\left(\frac{B}{\sqrt2 A}\right)^{1/3}.
}
\tag{1}
```

For the leading optical-variance term,

```math
\boxed{
h_*
=
\left[
\frac{\sqrt{40}\,\sigma_J}
{G_J
\left|\gamma\,d^3\sigma_z^2/d\mu^3\right|}
\right]^{1/3}.
}
\tag{2}
```

This is the four-color cube-root spacing law.

---

## 5. Balance at the optimum

At `h=h_*`,

```math
\boxed{
\frac{B^2}{h_*^2}
=2A^2h_*^4.
}
```

So the statistical variance is twice the squared leading systematic bias at the MSE optimum.

The optimum is not the point where bias and standard deviation are equal.

---

## 6. Slow improvement with averaging

If white averaging gives

```math
\sigma_J\propto t^{-1/2},
```

then

```math
\boxed{
h_*\propto t^{-1/6}.}
```

Thus a `64x` increase in integration time reduces the optimum spatial spacing by only a factor of `2`.

This is another indication that experimental geometry and systematic cancellation matter more than brute-force averaging.

---

## 7. Relation to transport signal

In the locally linear high-Peclet slowness limit,

```math
|\mathcal C_{4,tr}|
\simeq
2\omega h^2|q'|.
```

Meanwhile independent-noise standard deviation scales as

```math
h^{-1}.
```

Therefore transport-closure SNR initially grows approximately as

```math
\boxed{SNR\propto h^3}
```

while the quartet remains local.

Larger spacing is therefore statistically favorable until

```text
optical-shape curvature,
transport curvature,
boundary exposure,
or failure of the local model
```

becomes important.

The optimum is inherently a bias-versus-noise decision.

---

## 8. Scope

Equation (1) is not a universal resolution bound.

It assumes

```text
one dominant h^2 systematic,
independent equal complex current noise,
high-SNR log linearization,
locally linear current difference in h,
and a fixed total per-channel noise level.
```

Correlated noise, optimized unequal dwell time, full covariance, or higher-order source-shape errors alter the numerical optimum.

The useful general result is the scaling structure:

```text
smooth closure bias ~ h^2
independent closure noise ~ h^-1
-> cube-root optimum.
```

Numerical regression:

`numerics/ramo_four_color_spacing_optimum.py`
