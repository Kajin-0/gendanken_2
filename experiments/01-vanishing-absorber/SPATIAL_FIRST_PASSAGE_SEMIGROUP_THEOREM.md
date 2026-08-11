# Spatial First-Passage Semigroup — Why Three Colors Give an Exact Null Test

**Date:** 2026-08-10  
**Status:** classical strong-Markov/translation-invariance consequence applied to detector internal-depth encoding; exact under stated assumptions; no novelty claim for the probability theorem

## 1. The deeper reason behind the three-color law

The three-color spectral closure was first derived using an exponential spatial solution inside a homogeneous drift-diffusion segment.

That made the result look specific to a second-order transport equation.

It is more general.

The exponential law follows from a spatial first-passage **semigroup**.

---

## 2. Scalar homogeneous first-passage process

Consider a one-dimensional carrier coordinate `X_t` with these assumptions:

1. `X_t` is a scalar strong-Markov process over the interval of interest;
2. its law is spatially translation invariant there;
3. paths are continuous, so reaching `a+b` from `0` requires crossing `a` first;
4. after the crossing, no unresolved internal state is required to specify future transport beyond the current coordinate;
5. any local Markov killing/recombination is spatially homogeneous and included in the process.

Let

```math
\tau_d
=\inf\{t\ge0:X_t=d\}
```

be first passage across distance `d`.

With optional killing time `zeta`, define the successful Laplace transform

```math
\boxed{
U_s(d)
=
\mathbb E_0
\left[
e^{-s\tau_d}
\mathbf 1_{\tau_d<\zeta}
\right].
}
\tag{1}
```

For RF response set

```math
s=i\omega.
```

At DC,

```math
U_0(d)=P_0(\tau_d<\zeta)
```

is the collection probability.

---

## 3. Strong-Markov factorization

Take two positive distances `a,b`.

A continuous path reaching `a+b` must first hit `a`.

Apply the strong-Markov property at `tau_a`.

After that stopping time, spatial translation invariance makes the remaining first-passage problem statistically identical to a fresh passage over distance `b`.

Therefore

```math
\boxed{
U_s(a+b)=U_s(a)U_s(b).
}
\tag{2}
```

This includes the survival/killing factor because successful passage over `a+b` requires survival through both successive passages.

Equation (2) is the spatial semigroup law.

---

## 4. Continuity forces an exponential

Assume

```math
U_s(0)=1
```

and continuity in `d`.

The multiplicative Cauchy equation

```math
U_s(a+b)=U_s(a)U_s(b)
```

then gives

```math
\boxed{
U_s(d)=e^{-\gamma_s d}
}
\tag{3}
```

for one generally complex propagation exponent `gamma_s`.

At DC,

```math
U_0(d)=e^{-\gamma_0d}.
```

Hence the DC-normalized successful-carrier response is

```math
\boxed{
F_s(d)
=\frac{U_s(d)}{U_0(d)}
=e^{-\Gamma_s d},
\qquad
\Gamma_s=\gamma_s-\gamma_0.
}
\tag{4}
```

Thus exponential spatial propagation is not unique to ordinary drift-diffusion.

It is the generic scalar homogeneous continuous-path strong-Markov first-passage form.

---

## 5. What ordinary drift-diffusion adds

Uniform conditioned drift-diffusion gives the specific dispersion relation

```math
\boxed{
D\Gamma^2+w\Gamma=i\omega
}
```

in the simple conditioned representation.

Therefore there are two distinct theoretical levels:

### Spatial semigroup level

```math
F(d_1+d_2)=F(d_1)F(d_2)
```

or equivalently

```math
\ln F\propto d.
```

### Drift-diffusion level

The resulting complex exponent must additionally satisfy one real, frequency-independent pair `D,w` over RF frequency.

A detector can therefore pass spatial semigroup closure while failing drift-diffusion frequency closure.

That pattern would indicate homogeneous propagation with additional temporal/internal-state physics rather than simple spatial inhomogeneity.

---

## 6. Three equally spaced internal source coordinates

Suppose an ideal point source can be placed at three equally spaced distances from the collector:

```math
d_1=d_0-\Delta d,
```

```math
d_2=d_0,
```

```math
d_3=d_0+\Delta d.
```

Equation (4) gives

```math
F_2^2=F_1F_3.
```

Thus

```math
\boxed{
F(d_2,\omega)^2
=
F(d_1,\omega)F(d_3,\omega).
}
\tag{5}
```

This is the point-source form of the three-color geometric-mean law.

---

## 7. Why a rigid finite-width optical source preserves the law

Let the wavelength-selected generation distribution be one translated shape

```math
p_\lambda(z)=g[z-z_g(\lambda)].
```

Averaging the exponential `U_s` over the translated shape multiplies it by one transform factor depending on `s` and `g`, but not on `z_g`.

The same is true at DC.

Therefore the DC-normalized distributed response remains

```math
\boxed{
H(z_g,s)=B(s)e^{\pm\Gamma_s z_g},
}
```

with sign set by the coordinate orientation.

Hence equally spaced generation centers still satisfy

```math
\boxed{H_2^2=H_1H_3.}
```

The optical width cancels exactly as long as the shape translates rigidly within the homogeneous segment.

---

## 8. A hidden-state counterexample

The scalar semigroup assumption can fail even if each unresolved carrier population separately propagates homogeneously.

Suppose the measured response is a fixed mixture

```math
\boxed{
F(d)
=p e^{-\Gamma_1d}
+(1-p)e^{-\Gamma_2d}.
}
\tag{6}
```

This can represent two unresolved propagation populations or internal states.

Generically

```math
F(a+b)\ne F(a)F(b)
```

and

```math
F(d_2)^2\ne F(d_1)F(d_3).
```

Therefore three-color closure can detect a failure of the **scalar regenerative coordinate description** even when every hidden component is individually simple.

This is conceptually important.

A closure failure need not mean the material is spatially inhomogeneous; it may mean the carrier carries hidden dynamical state that is not reset by specifying position alone.

---

## 9. What else can break the semigroup law?

Within a real detector, failure can arise from

```text
spatially varying transport coefficients,
proximity to boundaries or interfaces,
non-rigid wavelength-dependent generation shape,
hidden carrier populations/internal states,
non-Markov memory,
jump/overshoot transport that bypasses the intermediate coordinate,
frequency-dependent contact/electrical contamination,
or incorrect spectral-to-depth calibration.
```

Thus semigroup failure is a broad null-test result.

It does not uniquely diagnose its cause.

---

## 10. A nested failure pattern

The combination with the real drift-diffusion closure gives a useful hierarchy.

### Pattern A

```text
three-color spatial semigroup passes
multi-frequency D_app,w_app closure passes
```

Consistent with homogeneous local Markov drift-diffusion over the tested region/band.

### Pattern B

```text
three-color semigroup passes
D_app,w_app disperse with RF
```

Spatial propagation remains scalar/exponential, but ordinary Markov drift-diffusion is insufficient.

Temporal memory or a more complicated homogeneous propagation law becomes a natural target.

### Pattern C

```text
three-color semigroup fails
```

The failure occurs at a more basic spatial-coordinate level.

Before interpreting RF coefficient dispersion, test optical-kernel evolution, inhomogeneity, boundaries, and hidden-state/multichannel transport.

This hierarchy prevents one kind of model failure from being misdiagnosed as another.

---

## 11. Relation to optoelectronic chromatic dispersion prior art

Photodiode optoelectronic chromatic dispersion is established: wavelength-dependent absorption depth can create measurable RF phase/amplitude changes, and those changes have already been used for wavelength monitoring and computational spectroscopy.

Therefore the use of wavelength-dependent carrier dynamics as an optical information channel is **not** a novelty candidate.

The narrower candidate here is

```text
calibrated spectral generation coordinate
+
parameter-free spatial semigroup closure
+
subsequent multi-frequency real transport closure.
```

A focused literature audit is still required before any priority claim.

---

## 12. Numerical regression

`numerics/spatial_semigroup_three_color_test.py`

checks

```math
U(a+b)=U(a)U(b)
```

and the corresponding equally spaced three-point closure for one scalar exponential propagation law.

It then constructs an unresolved mixture of two exponential propagation populations and confirms that the three-point closure is violated.

---

## 13. Paper-level significance

The simplest detector-specific experiment is now more fundamental than originally thought.

> **Three colors test whether the carrier transport is compatible with one scalar homogeneous spatial first-passage semigroup. Two RF frequencies then test whether that semigroup is specifically ordinary real drift-diffusion.**

The first test is about the existence of a clean internal spatial coordinate.

The second is about the transport law along that coordinate.

Keeping those questions separate is one of the strongest conceptual advances of the present theory branch.
