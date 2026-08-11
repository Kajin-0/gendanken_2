# Spatial Lévy Delay Spectroscopy — Reconstructing Random Waiting-Time Increments per Unit Distance

**Date:** 2026-08-10  
**Status:** exact Lévy-Khintchine consequence for homogeneous regenerative first-passage timing; detector application is exploratory; no novelty claim for the stochastic-process mathematics

## 1. Beyond effective drift and diffusion

If successful transit time forms a homogeneous convolution semigroup in propagation distance,

```math
T_{a+b}\overset d=T_a+T_b',
```

then

```math
E[e^{-sT_d}]
=e^{-d\Phi(s)}.
```

Most transport analyses would summarize `Phi` by one drift velocity and one diffusion coefficient.

That is unnecessarily restrictive.

The Lévy-Khintchine theorem says the full exponent itself has a direct physical-statistical decomposition.

---

## 2. The per-distance delay spectrum

For the conditioned successful timing process,

```math
\boxed{
\Phi(s)
=a s
+
\int_0^\infty
(1-e^{-st})\nu(dt).
}
\tag{1}
```

Here

```text
a >= 0
```

is deterministic transit-time accumulation per unit distance, while

```math
\nu(dt)\ge0
```

is the Lévy measure.

Interpret `nu(dt)` as the intensity **per unit propagation distance** of positive random timing increments of scale `t`.

This does not require those increments to correspond literally to isolated trap events.

It is the exact stochastic representation of any homogeneous positive timing subordinator.

---

## 3. The measured RF spatial exponent

At RF frequency `omega`, set

```math
s=i\omega.
```

If a spatial depth experiment determines the complex propagation exponent

```math
\boxed{
\Phi(i\omega)
=-\frac{1}{d}\ln H_d(\omega),
}
\tag{2}
```

then Eq. (1) gives

```math
\boxed{
\Re\Phi(i\omega)
=
\int_0^\infty
[1-\cos(\omega t)]\nu(dt),
}
\tag{3}
```

and

```math
\boxed{
\Im\Phi(i\omega)
=
a\omega
+
\int_0^\infty
\sin(\omega t)\nu(dt).
}
\tag{4}
```

Thus RF attenuation and phase are not merely phenomenological transfer-function components.

Inside the homogeneous regenerative model they are integral transforms of a **positive random-delay spectrum**.

---

## 4. Exact inversion in the ideal infinite-bandwidth limit

Assume the Lévy measure has a density `nu(t)` and sufficient second moment for the following derivatives/transforms.

Differentiate Eq. (3) twice:

```math
\boxed{
\frac{d^2}{d\omega^2}
\Re\Phi(i\omega)
=
\int_0^\infty
t^2\cos(\omega t)\nu(t)dt.
}
\tag{5}
```

The right side is a cosine transform.

Therefore

```math
\boxed{
t^2\nu(t)
=
\frac{2}{\pi}
\int_0^\infty
\frac{d^2}{d\omega^2}
\Re\Phi(i\omega)
\cos(\omega t)d\omega.
}
\tag{6}
```

This is an exact ideal inverse.

So, in principle,

> **complex RF propagation versus internal distance determines the full distribution of stochastic waiting-time increments per unit distance.**

Drift and diffusion become special parameterizations of one particular `nu(t)`.

---

## 5. Cumulants are just moments of the delay spectrum

Whenever finite,

```math
\boxed{
\frac{\kappa_n(T_d)}{d}
=
\int_0^\infty t^n\nu(dt),
\qquad n\ge2.
}
\tag{7}
```

The mean also includes the deterministic component:

```math
\boxed{
\frac{E[T_d]}{d}
=a+
\int_0^\infty t\nu(dt).
}
\tag{8}
```

Thus the cumulant hierarchy is the moment hierarchy of the same positive delay spectrum reconstructed by Eq. (6).

This unifies

```text
RF spatial propagation
transit-time cumulants
cumulant Hankel positivity
and microscopic waiting-time interpretation.
```

---

# 6. Ordinary drift-diffusion predicts a very specific Lévy spectrum

For uniform conditioned drift `w` and diffusion `D`,

```math
\Phi_{DD}(s)
=
\frac{
\sqrt{w^2+4Ds}-w
}{2D}.
```

Its Lévy density is

```math
\boxed{
\nu_{DD}(t)
=
\frac{1}{2\sqrt{\pi D}}
\,t^{-3/2}
\exp\left[-\frac{w^2t}{4D}\right].
}
\tag{9}
```

Substituting Eq. (9) into Eq. (1) exactly reproduces the inverse-Gaussian first-passage exponent.

Thus ordinary drift-diffusion makes a strong stochastic claim:

> **the per-distance random-delay spectrum must have a `t^{-3/2}` short-time form with one exponential cutoff scale `4D/w^2`.**

This is much more specific than saying only that the mean transit time is `d/w`.

---

## 7. Why the inverse-Gaussian cumulant ratios follow

Take moments of Eq. (9):

```math
\int_0^\infty t^n\nu_{DD}(t)dt
=
(2n-3)!!
\frac{(2D)^{n-1}}{w^{2n-1}}.
```

Multiplying by distance gives

```math
\kappa_n
=(2n-3)!!
(2D)^{n-1}
\frac{d}{w^{2n-1}},
```

which yields the previously derived parameter-free relations

```math
\frac{\kappa_{n+1}\kappa_{n-1}}{\kappa_n^2}
=\frac{2n-1}{2n-3}.
```

The universal timing-shape ratios are therefore simply **moment ratios of the drift-diffusion Lévy spectrum**.

---

# 8. A simple regenerative trapping example

Suppose an independent random waiting mechanism adds events along propagation distance at rate

```math
\lambda
```

per unit length, and each event has an exponential wait-time distribution

```math
f(t)=\beta e^{-\beta t}.
```

Its Lévy density is

```math
\boxed{
\nu_{trap}(t)
=\lambda\beta e^{-\beta t}.
}
\tag{10}
```

The corresponding Laplace exponent is

```math
\boxed{
\Phi_{trap}(s)
=\lambda\frac{s}{\beta+s}.
}
\tag{11}
```

If this mechanism is statistically independent of the drift-diffusion timing increments,

```math
\boxed{
\Phi_{total}(s)
=
\Phi_{DD}(s)+\Phi_{trap}(s),
}
\tag{12}
```

or equivalently

```math
\boxed{
\nu_{total}(t)
=
\nu_{DD}(t)+\nu_{trap}(t).
}
\tag{13}
```

This additive structure is important.

A trapping-like delay channel does not have to be represented by an arbitrary frequency-dependent 'effective diffusion coefficient.'

It can appear as **extra positive spectral weight in the random-delay measure**.

---

## 9. Different mechanisms correspond to different delay spectra

Within the homogeneous regenerative class:

### Deterministic transit

```math
\nu(t)=0,
```

with all delay carried by the deterministic coefficient `a`.

### Brownian drift-diffusion first passage

```math
\nu(t)\propto
t^{-3/2}e^{-t/t_c}.
```

### Poisson exponential waiting events

```math
\nu(t)\propto e^{-\beta t}.
```

### Distributed trapping / broad memory

May produce a broad superposition of positive waiting-time scales in `nu(t)`.

Thus the theoretical target shifts from

> fit one effective lifetime

toward

> **infer the positive spectrum of delay increments that the data require.**

---

## 10. Positivity itself becomes a null test

The reconstructed Lévy measure must satisfy

```math
\boxed{\nu(t)\ge0.}
```

A deconvolution that robustly requires negative Lévy weight means the homogeneous scalar regenerative subordinator model is insufficient or the reconstruction/calibration is wrong.

This is analogous to the characteristic-function PSD test at Level 0, but now applied after imposing the stronger spatial-regeneration assumption.

---

## 11. Practical inverse is ill-conditioned

Equation (6) is an ideal infinite-bandwidth theorem.

A real experiment has

```text
finite RF bandwidth
noise
spatial-coordinate uncertainty
electrical transfer corrections
and numerical differentiation error.
```

Recovering `nu(t)` therefore becomes a regularized positive inverse-transform problem.

The exact theorem should not be confused with a claim of arbitrary practical time-scale resolution.

A sensible experimental program would first test low-order robust consequences:

```text
cumulant positivity
cumulant Hankel positivity
inverse-Gaussian ratio nulls
simple one-pole extra spectral weight
```

before attempting full Lévy-density reconstruction.

---

## 12. Connection to spectral depth encoding

A graded absorber can provide the distance coordinate without physically moving a source.

If wavelength produces calibrated internal source coordinates `z_g(lambda)`, then pairwise complex response ratios estimate

```math
\Phi(i\omega)
\simeq
-\frac{
\ln H(z_2,\omega)-\ln H(z_1,\omega)
}{z_2-z_1}
```

inside a homogeneous region, after optical-kernel shape correction.

Repeating this over RF frequency provides the data needed for Eqs. (3)-(6).

Thus wavelength × RF response becomes, in the ideal theory,

> **spectroscopy of the stochastic delay increments accumulated per unit internal propagation distance.**

---

## 13. Relation to the local Markov closure theorem

If the reconstructed `nu(t)` has exactly the drift-diffusion form Eq. (9), then the spatial exponent must satisfy

```math
D\Phi^2+w\Phi=s.
```

That is the same quadratic closure tested by the `D_app,w_app` theorem.

The two views are complementary:

```text
quadratic D,w closure
-> compact parametric null

Levy delay spectrum
-> general positive stochastic representation.
```

If quadratic closure fails but the Lévy spectrum remains positive, the data can still be consistent with homogeneous scalar regenerative transport—just not ordinary drift-diffusion.

This is a particularly clean theoretical classification.

---

## 14. Numerical regression

`numerics/spatial_levy_delay_spectrum.py`

verifies numerically that

```math
\int_0^\infty
(1-e^{-st})\nu_{DD}(t)dt
=
\frac{\sqrt{w^2+4Ds}-w}{2D}
```

over several positive Laplace frequencies.

It verifies that moments of `nu_DD` reproduce the inverse-Gaussian cumulants.

It then adds the exponential trap-wait spectrum Eq. (10) and confirms both in real Laplace and complex RF form that the total exponent is the sum of the two mechanisms.

---

## 15. Mathematical prior-art boundary

Lévy-Khintchine representations, subordinators, inverse-Gaussian processes, and inversion of characteristic/Laplace exponents are classical stochastic-process theory.

None of that mathematics is claimed as new.

The candidate detector contribution is the proposed physical correspondence

```text
wavelength-selected internal distance
+
complex RF spatial exponent
->
per-distance positive delay spectrum
->
transport-law falsification / mechanism discrimination.
```

A dedicated literature audit is required before any novelty language.

---

## 16. One-line conceptual result

The most compact statement is:

> **In a homogeneous regenerative detector, the complex RF phase and attenuation accumulated per micron are the transform of a positive spectrum of random time delays accumulated per micron. Ordinary drift-diffusion predicts one specific `t^{-3/2}` exponential-cutoff spectrum; extra transport physics must change that spectrum or break regeneration entirely.**

This gives a rigorous stochastic meaning to what the wavelength × RF experiment is actually measuring.
