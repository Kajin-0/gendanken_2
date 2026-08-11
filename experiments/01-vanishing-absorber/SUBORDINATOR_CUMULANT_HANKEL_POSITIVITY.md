# Cumulant Hankel Positivity — A Model-Independent Timing-Shape Null for Regenerative Transport

**Date:** 2026-08-10  
**Status:** classical Stieltjes-moment/subordinator consequence applied as a detector timing null; no novelty claim for the mathematics

## 1. Position in the falsification ladder

The timing hierarchy now has three nested levels:

```text
any positive classical transit-time distribution

superset

homogeneous scalar regenerative first-passage timing

superset

uniform Brownian drift-diffusion first passage.
```

The characteristic-function positivity test checks the first level.

The inverse-Gaussian cumulant ratios check the third.

This file derives exact timing-shape inequalities that characterize the **middle** level more sharply than simple nonnegative cumulants.

---

## 2. Regenerative first passage gives a timing subordinator

For homogeneous scalar regenerative propagation over distance `d`, successful transit time forms a convolution semigroup:

```math
T_{a+b}\overset d=T_a+T_b',
```

with independent stationary spatial increments.

The conditioned timing Laplace transform is

```math
E[e^{-sT_d}]=e^{-d\Phi(s)}
```

with subordinator exponent

```math
\Phi(s)
=a s+
\int_0^\infty(1-e^{-st})\nu(dt).
```

Whenever the moments exist, for every `n>=2`,

```math
\boxed{
\kappa_n(d)
=d\int_0^\infty t^n\nu(dt).
}
\tag{1}
```

Thus the higher cumulants are moments of one positive measure.

---

## 3. Log-convex cumulant sequence

Apply Cauchy-Schwarz to the positive measure `nu`:

```math
\left(
\int t^n\nu(dt)
\right)^2
\le
\left(
\int t^{n-1}\nu(dt)
\right)
\left(
\int t^{n+1}\nu(dt)
\right).
```

Therefore, for `n>=3`,

```math
\boxed{
\kappa_n^2
\le
\kappa_{n-1}\kappa_{n+1}.
}
\tag{2}
```

For `n=2`, deterministic drift contributes only to `kappa_1` and increases it above the Lévy-measure first moment, so the same inequality remains valid:

```math
\boxed{
\kappa_2^2
\le
\kappa_1\kappa_3.
}
\tag{3}
```

Hence the full finite cumulant sequence is constrained to be log-convex in this sense.

---

## 4. First simple observable inequality — skewness cannot be too small

Define

```math
CV
=\frac{\sqrt{\kappa_2}}{\kappa_1},
```

and skewness

```math
\gamma_1
=\frac{\kappa_3}{\kappa_2^{3/2}}.
```

Equation (3) gives

```math
\frac{\kappa_3\kappa_1}{\kappa_2^2}\ge1.
```

But

```math
\frac{\kappa_3\kappa_1}{\kappa_2^2}
=\frac{\gamma_1}{CV}.
```

Therefore

```math
\boxed{
\gamma_1\ge CV.
}
\tag{4}
```

A homogeneous scalar regenerative first-passage distribution with finite moments cannot have positive timing variance but arbitrarily small skewness.

Uniform drift-diffusion is much sharper:

```math
\gamma_1=3CV.
```

---

## 5. Second simple inequality — excess kurtosis bounds skewness

Define excess kurtosis

```math
\gamma_2
=\frac{\kappa_4}{\kappa_2^2}.
```

Equation (2) with `n=3` gives

```math
\kappa_3^2
\le
\kappa_2\kappa_4.
```

Divide by `kappa_2^3`:

```math
\boxed{
\gamma_2
\ge
\gamma_1^2.
}
\tag{5}
```

Thus the allowed `(skewness, excess-kurtosis)` plane has a universal lower boundary for homogeneous regenerative positive timing increments.

Uniform drift-diffusion predicts instead the specific curve

```math
\boxed{
\gamma_2
=\frac53\gamma_1^2.
}
\tag{6}
```

So drift-diffusion occupies a strict subset of the broader regenerative class.

---

## 6. Full Hankel positivity hierarchy

Equation (1) allows a stronger matrix statement.

Define

```math
\boxed{
\mathcal C^{(m)}_{ij}
=\kappa_{i+j+2},
\qquad
i,j=0,\ldots,m.
}
```

Then for any real coefficients `c_i`,

```math
\begin{aligned}
\sum_{ij}c_i\mathcal C_{ij}c_j
&=d\int
\left(
\sum_i c_i t^{i+1}
\right)^2
\nu(dt)\\
&\ge0.
\end{aligned}
```

Therefore

```math
\boxed{
\mathcal C^{(m)}\succeq0
}
\tag{7}
```

for every finite block for which the required cumulants exist.

Thus all principal minors satisfy exact nonnegative inequalities.

The first `2x2` determinant gives Eq. (5):

```math
\boxed{
\kappa_2\kappa_4-\kappa_3^2\ge0.
}
```

The next blocks constrain combinations of

```text
kappa2 through kappa6,
then kappa2 through kappa8,
etc.
```

This is the cumulant analogue of characteristic-function positive definiteness.

---

## 7. Why this is stronger than saying 'all cumulants are positive'

Positivity alone gives

```math
\kappa_n\ge0.
```

Hankel positivity constrains their **relative sizes**.

For example a hypothetical timing distribution might have

```text
positive variance
positive skewness
positive excess kurtosis
```

but still violate

```math
\kappa_2\kappa_4\ge\kappa_3^2.
```

Such a distribution can be perfectly valid as a positive random variable while being incompatible with a homogeneous scalar regenerative first-passage convolution semigroup.

That distinction is important.

---

## 8. Nested timing-shape tests

The resulting hierarchy can be stated without transport equations.

### Any positive transit-time distribution

Must satisfy characteristic-function positive definiteness.

It may have a broad range of cumulant shapes.

### Homogeneous scalar regenerative first passage

Additionally requires

```math
\kappa_n\propto d,
```

```math
\kappa_n\ge0,
```

and the cumulant Hankel matrices Eq. (7) to be positive semidefinite.

Simple consequences:

```math
\boxed{\text{skewness}\ge CV,}
```

```math
\boxed{\text{excess}\ge\text{skewness}^2.}
```

### Uniform drift-diffusion

Sharpen those to

```math
\boxed{\text{skewness}=3CV,}
```

```math
\boxed{\text{excess}=\frac53\text{skewness}^2.}
```

This is a clean model-selection ladder based purely on the shape of transit-time statistics.

---

## 9. What failure means

### Characteristic-function test fails

The observable is not even any positive classical transit-time distribution.

### Characteristic-function passes but cumulant Hankel positivity fails

A positive timing distribution exists, but it cannot be generated by the stated homogeneous scalar regenerative first-passage process.

Possible causes include

```text
hidden state carried between spatial increments,
spatial inhomogeneity,
non-regenerative memory,
boundaries,
or a source coordinate that does not define equivalent spatial increments.
```

### Regenerative inequalities pass but inverse-Gaussian ratios fail

The timing may still form a homogeneous convolution semigroup, but ordinary Brownian drift-diffusion is too restrictive.

That is exactly where trapping/relaxation or another homogeneous memory law becomes interesting.

---

## 10. RF-domain accessibility

The required cumulants are available from derivatives of

```math
\ln H(\omega)
```

at zero RF:

```text
phase slope -> kappa1
log-magnitude curvature -> kappa2
cubic phase -> kappa3
quartic log magnitude -> kappa4
etc.
```

Therefore the inequalities can, in principle, be tested from complex frequency response without constructing a time-domain arrival histogram.

The practical limitation is derivative noise, especially for fourth and higher cumulants.

---

## 11. Numerical example

`numerics/subordinator_cumulant_hankel_positivity.py`

constructs a generic compound-Poisson waiting-time subordinator plus deterministic transit accumulation.

It verifies

```text
skewness/CV > 1
excess/skewness^2 > 1
all tested adjacent cumulant log-convexity margins >=0
2x2, 3x3, and 4x4 cumulant Hankel matrices PSD.
```

It then checks uniform drift-diffusion and recovers the stronger exact values

```text
skewness/CV = 3
excess/skewness^2 = 5/3.
```

---

## 12. Mathematical prior-art boundary

Stieltjes moment sequences, Hankel positivity, subordinators, and infinite-divisibility cumulant properties are established probability theory.

Do not claim this as new mathematics.

The potential detector contribution is using these classical constraints as an explicit **transport falsification ladder** for photocarrier timing.

A dedicated semiconductor prior-art audit remains necessary.

---

## 13. Conceptual one-line result

The middle-level null can be summarized very simply:

> **If each added micron of a homogeneous detector contributes an independent positive random transit-time increment, the timing skewness cannot be smaller than the coefficient of variation, and the excess kurtosis cannot be smaller than skewness squared.**

Ordinary drift-diffusion predicts still more specific ratios.
