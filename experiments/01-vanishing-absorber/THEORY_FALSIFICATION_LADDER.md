# Theory Falsification Ladder — From Any Transit-Time Distribution to Spatially Resolved Stochastic Transport

**Date:** 2026-08-10  
**Status:** canonical theory synthesis; combines exact results with explicit model boundaries; prior-art priority unresolved; no novelty claim

## 1. The new organizing question

The project should no longer begin by asking

> Can we fit an internal velocity profile?

That question is too model-dependent and invites poorly conditioned inverse fits.

The stronger approach is:

> **What exact relations must the measured response satisfy before a particular transport model is even allowed?**

Each level below adds one assumption and therefore one new falsifiable prediction.

A stronger model is considered only after the weaker model has survived its own null tests.

---

# Level 0 — Is the response any positive classical transit-time distribution?

Assumption:

```math
H(\omega)=\mathbb E[e^{-i\omega T}],
\qquad T\ge0.
```

No transport law is assumed.

Exact predictions:

```math
H(0)=1,
```

```math
H(-\omega)=H(\omega)^*,
```

```math
|H(\omega)|\le1.
```

For every set of RF frequencies,

```math
\boxed{
K_{jk}=H(\omega_j-\omega_k)\succeq0.
}
```

A particularly simple two-harmonic null is

```math
\boxed{
|H(2\omega)-H(\omega)^2|
\le1-|H(\omega)|^2.
}
```

### If Level 0 fails

Do not fit carrier drift/diffusion.

The supposedly de-embedded transfer is not even compatible with a positive classical delay mixture.

First investigate

```text
electrical/optical de-embedding
signed or interfering current components
nonlinear response
coherent effects
or an incorrect timing interpretation.
```

Canonical file:

`TRANSIT_TIME_CHARACTERISTIC_FUNCTION_NULL_TESTS.md`

---

# Level 1 — Does wavelength behave as one homogeneous internal spatial coordinate?

Assumptions:

```text
scalar spatially homogeneous first-passage process
continuous paths / no skipping of the intermediate coordinate
strong-Markov regeneration in the spatial coordinate
rigid translation of the optical generation kernel with wavelength.
```

The successful first-passage transform obeys the spatial semigroup

```math
\boxed{
U_s(a+b)=U_s(a)U_s(b),
}
```

so

```math
\boxed{
U_s(d)=e^{-\gamma_s d}.
}
```

DC normalization preserves the exponential form.

For three wavelengths whose calibrated generation centers are equally spaced,

```math
\boxed{
H_2(\omega)^2
=H_1(\omega)H_3(\omega).
}
```

Equivalently,

```math
\boxed{
\partial_{z_g}^2\ln H=0.
}
```

Remarkably, this remains exact for an arbitrarily broad/asymmetric fixed generation profile if wavelength only translates its shape.

### If Level 1 fails

Possible causes include

```text
generation-kernel shape evolution
spatially varying transport
boundary/interface influence
hidden carrier populations/internal states
non-Markov spatial memory
jump/overshoot transport
or bad spectral-to-depth calibration.
```

Do not immediately interpret failure as a diffusion coefficient changing with RF.

Canonical files:

`SPATIAL_FIRST_PASSAGE_SEMIGROUP_THEOREM.md`

`THREE_COLOR_SPECTRAL_CLOSURE_THEOREM.md`

---

# Level 2 — Is the homogeneous/local response specifically real Markov drift-diffusion?

Assumption:

```math
D(z)F''+w(z)F'-i\omega F=0,
```

with real, frequency-independent

```text
D(z)>0
w(z).
```

Define

```math
r_\omega=\partial_z\ln F,
```

```math
A_\omega=r_\omega'+r_\omega^2.
```

Then

```math
D A_\omega+w r_\omega=i\omega.
```

At every nonsingular frequency define

```math
\delta_\omega
=\Re A_\omega\Im r_\omega
-\Im A_\omega\Re r_\omega,
```

```math
\boxed{
D_{\rm app}(\omega)
=-\frac{\omega\Re r_\omega}{\delta_\omega},
}
```

```math
\boxed{
w_{\rm app}(\omega)
=\frac{\omega\Re A_\omega}{\delta_\omega}.
}
```

Exact closure theorem:

```math
\boxed{
D_{\rm app}(\omega)=\mathrm{constant},
\qquad
w_{\rm app}(\omega)=\mathrm{constant}
}
```

across RF frequency **if and only if** one real frequency-independent local second-order generator exists at that depth.

For `N` RF frequencies this produces

```math
\boxed{2(N-1)}
```

real closure conditions.

The older three-frequency complex determinant is only necessary, not sufficient, because common complex coefficients can also satisfy it.

Canonical file:

`LOCAL_MARKOV_TRANSPORT_CLOSURE_THEOREM.md`

---

# Level 2A — Minimal two-depth / two-frequency version

Inside a uniform segment,

```math
\gamma(\omega)
=\frac{
\sqrt{w^2+4iD\omega}-w
}{2D}.
```

Two source depths give

```math
\gamma
=\frac{\ln[H(z_2)/H(z_1)]}{z_2-z_1}.
```

Write

```math
\gamma=a+ib.
```

Then one RF frequency gives exactly

```math
\boxed{
D
=\frac{\omega a}{b(a^2+b^2)},
}
```

```math
\boxed{
w
=\frac{\omega(b^2-a^2)}{b(a^2+b^2)}.
}
```

For positive downstream transport,

```math
\boxed{0<a<b.}
```

The **second RF frequency has no new transport parameter**.

It is a pure model test:

```math
D(\omega_2)=D(\omega_1),
```

```math
w(\omega_2)=w(\omega_1).
```

This is the simplest exact transport gedanken experiment in the project.

Canonical file:

`MINIMAL_TWO_DEPTH_TWO_FREQUENCY_GEDANKEN.md`

---

# Level 3 — What does DC normalization hide?

Let

```math
h(z)=U(z,0)
```

be the probability of successful collection before local Markov recombination/killing.

The normalized RF field

```math
F(z,\omega)=U(z,i\omega)/h(z)
```

obeys an exact conditioned equation

```math
D F''
+
\left[v+2D\partial_z\ln h\right]F'
-i\omega F=0.
```

Thus RF of successfully collected carriers measures

```math
\boxed{
w_{\rm cond}
=v+2D\partial_z\ln h,
}
```

not necessarily the unconditioned physical drift `v`.

This is a Doob-conditioning transformation.

Therefore RF alone cannot generally separate physical drift from recombination.

The DC collection field supplies exactly the missing information.

In the simple uniform exponential case,

```math
c=\partial_z\ln h,
```

```math
\boxed{v=w-2Dc,}
```

```math
\boxed{\kappa=Dc^2+vc,}
```

```math
\boxed{\tau=1/\kappa.}
```

This explains structurally why lifetime/drift calibration repeatedly appeared as a bottleneck in earlier branches.

---

# Level 4 — If Markov drift-diffusion fails, what is the smallest missing physics?

Do not immediately fit an arbitrary frequency-dependent `D(omega)`.

Examine the **shape** of closure failure.

### Reversible trapping archetype

```math
\Psi(s)
=s\left(1+\frac{k_t}{k_d+s}\right).
```

Low RF can masquerade as renormalized constant drift/diffusion, followed by a turnover near the release scale.

### Finite flux/momentum-relaxation archetype

```math
\Psi(s)=s(1+\tau_Js).
```

Low RF shifts the apparent diffusion while leaving drift correct to leading order, followed by even-in-frequency dispersion.

### Leading spatial nonlocal correction

```math
C F'''+D F''+wF'-sF=0.
```

At low RF,

```math
D_{\rm app}-D\propto+\omega^2,
```

```math
w_{\rm app}-w\propto-\omega^2.
```

The goal is a nested model hierarchy:

```text
smallest model
-> exact closure test
-> fail
-> add one physically interpretable state/operator
-> new closure test.
```

Canonical file:

`TRANSPORT_CLOSURE_FAILURE_SIGNATURES.md`

---

# Level 5 — What can a controlled internal perturbation reveal for arbitrary stochastic paths?

Now relax the transport law completely again.

For a successful trajectory `X_t` with random transit time `T`, define local occupation time

```math
\ell(z)=\int_0^T\delta(X_t-z)dt.
```

Apply an ideal weak local clock perturbation.

For a point perturbation of area `A_h`, the exact logarithmic response is

```math
\boxed{
S(z,\omega)
=-i\omega A_h
\frac{
\mathbb E[e^{-i\omega T}\ell(z)]
}{H(\omega)}.
}
```

No Markov or drift-diffusion assumption appears.

The global sum rule is

```math
\boxed{
\int S(z,\omega)dz
=A_h\omega\partial_\omega\ln H(\omega).
}
```

Low RF gives

```math
\boxed{
\frac{S}{-i\omega A_h}
=
\mathbb E[\ell(z)]
-i\omega\operatorname{Cov}(T,\ell(z))
+O(\omega^2).
}
```

Thus local perturbation spectroscopy can resolve

```text
where successful carriers spend their mean transit time
and which regions are statistically responsible for timing dispersion.
```

Canonical file:

`STOCHASTIC_OCCUPATION_TIME_RESPONSE_THEOREM.md`

---

# Level 6 — The full timing-cumulant spatial decomposition

The frequency-tilted occupation field has the exact joint-cumulant expansion

```math
\boxed{
\rho_\omega(z)
=
\sum_{n=0}^{\infty}
\frac{(-i\omega)^n}{n!}
\kappa
\left(
\ell(z),
\underbrace{T,\ldots,T}_{n}
\right).
}
```

Trajectory-wise

```math
\int\ell(z)dz=T.
```

Therefore every local mixed cumulant integrates to the next global timing cumulant:

```math
\boxed{
\int dz\,
\kappa(
\ell(z),T,\ldots,T
)
=
\kappa_{n+1}(T).
}
```

Examples:

```math
\int E[\ell(z)]dz=E[T],
```

```math
\int Cov[\ell(z),T]dz=Var(T),
```

```math
\int \kappa[\ell(z),T,T]dz=\kappa_3(T).
```

So the theory predicts a spatial decomposition of

```text
mean timing
variance
skewness
and every higher transit-time cumulant.
```

Canonical file:

`OCCUPATION_TIME_CUMULANT_HIERARCHY.md`

---

# Level 7 — Deterministic monotonic transit is an even stronger limiting theory

If each generated carrier follows one monotonic deterministic path with local slowness `q(z)`, the translated-feature theorem factorizes the local complex response.

For a point perturbation,

```math
R_{\lambda,\omega}(z)
\propto
p_\lambda(z)e^{-i\omega T(z)}.
```

Therefore

```text
normalized magnitude -> optical generation PDF
spatial phase slope / omega -> local transit slowness q(z).
```

It also predicts the exact relocation sum rule

```math
\int R dz=-i\omega A_h.
```

These strong identities should be treated as **falsifiable deterministic limits**, not imposed on stochastic detector data.

Canonical file:

`TRANSLATION_RESPONSE_THEOREM.md`

---

# Statistical layer — when is a failure significant?

For `N` RF frequencies producing apparent coefficient vectors

```math
\hat\theta_j=(\hat D_j,\hat w_j),
```

with full covariance `C`, the Markov null is one common two-component vector.

The generalized least-squares closure statistic is

```math
\boxed{
Q
=
(\hat g-X\hat\theta)^TC^{-1}(\hat g-X\hat\theta).
}
```

Under the linearized Gaussian null,

```math
\boxed{Q\sim\chi^2_{2N-2}.}
```

Under an alternative the noncentrality

```math
\boxed{
\Lambda=\mu_\perp^TC^{-1}\mu_\perp
}
```

sets detection power.

Canonical file:

`MULTIFREQUENCY_CLOSURE_STATISTICAL_TEST.md`

---

# Spatial-noise layer — exact structure does not mean infinite resolution

A centered two-depth first derivative of `y=ln F` has

```text
noise ~ h^-1
bias ~ h^2
```

and optimum

```math
\boxed{
h_{1,*}
=(3\sigma_y/|y'''|)^{1/3}.}
```

A second derivative needed for arbitrary-profile closure has

```text
noise ~ h^-2
bias ~ h^2
```

and optimum

```math
\boxed{
h_{2,*}
=864^{1/8}
(\sigma_y/|y''''|)^{1/4}.}
```

With white averaging noise,

```math
h_{1,*}\propto t^{-1/6},
```

```math
h_{2,*}\propto t^{-1/8}.
```

Thus brute-force averaging improves spatial resolution extremely slowly.

This mathematically favors simple piecewise-uniform gedanken geometries over arbitrary-profile differentiation.

Canonical file:

`SPATIAL_DERIVATIVE_NOISE_RESOLUTION.md`

---

# The simplest full experimental story

The current theory can be communicated without beginning with a complicated device.

## Gedanken experiment A — three colors

Choose three wavelengths that translate generation to three equally spaced internal coordinates.

Test

```math
\boxed{H_2^2=H_1H_3.}
```

This tests the spatial-coordinate/semigroup picture.

## Gedanken experiment B — second RF frequency

Infer `D,w` from the complex slope at one frequency.

Repeat at another frequency.

Test

```math
D_1=D_2,
\qquad
w_1=w_2.
```

This tests ordinary local Markov drift-diffusion.

## Gedanken experiment C — DC depth dependence

Use collection probability versus depth to undo conditioning and recover physical drift/recombination.

## Gedanken experiment D — move one weak local clock feature

Measure the local occupation response and test whether its spatial integral reproduces the independently measured global RF derivative/cumulants.

This decomposes timing statistics spatially.

---

# Prior-art boundary

Several ingredients are established:

```text
photodiode transit-time frequency response
wavelength-dependent absorption depth and RF phase
optoelectronic chromatic dispersion
multi-frequency photodiode response characterization
algebraic convection-diffusion inverse methods
Doob conditioning / h-transforms
occupation-time / Feynman-Kac mathematics
characteristic-function positivity.
```

Therefore the manuscript must **not** claim novelty for those ingredients.

The candidate research contribution is the integrated detector-theory framework:

```text
spectral depth coordinate
+
nested exact null tests
+
real multi-frequency local closure
+
DC conditioning correction
+
controlled perturbation occupation/cumulant tomography
+
explicit falsification signatures and statistical thresholds.
```

Whether that integrated framework or any of its detector-specific theorems has priority remains OPEN.

---

# Current research frontier

The strongest next tasks are now:

1. audit the detector-specific null laws against primary prior art, especially optoelectronic chromatic-dispersion and modulated-transport literature;
2. derive the finite-generation-shape correction and covariance for the three-color law in a realistic graded absorber;
3. map the hierarchy onto one clean HgCdTe example using a measured/credible `x(z)` and absorption law;
4. calculate predicted closure residuals for conventional drift-diffusion versus trapping/nonlocal alternatives;
5. only then decide whether the theory is sufficiently distinct and complete to begin a manuscript.

Fabrication optimization is supporting context, not the active theoretical frontier.
