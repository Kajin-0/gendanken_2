# Level-0 Null Tests — Is the RF Response Any Classical Transit-Time Distribution?

**Date:** 2026-08-10  
**Status:** exact probability-theory consequences for a positive classical transit-time distribution; independent of drift-diffusion; no novelty claim

## 1. The question before any transport model

Before fitting drift velocity, diffusion, lifetime, trapping, or a nonlocal transport law, ask a more primitive question.

Suppose the de-embedded, DC-normalized detector response really is the Fourier transform of a positive distribution of successful carrier transit times:

```math
\boxed{
H(\omega)=\mathbb E[e^{-i\omega T}],
\qquad T\ge0.
}
```

Then `H` is a characteristic function.

This assumption is weaker than drift-diffusion.

It does **not** specify

```text
how the carrier moves,
whether the motion is diffusive,
whether the velocity is uniform,
or what material is used.
```

It says only that the measured normalized complex response is an incoherent positive mixture of classical arrival delays.

Therefore it should be tested **before** any more specific transport model.

---

## 2. Immediate exact constraints

Every characteristic function obeys

```math
\boxed{H(0)=1,}
```

```math
\boxed{H(-\omega)=H(\omega)^*,}
```

and

```math
\boxed{|H(\omega)|\le1.}
```

These are necessary but weak.

The stronger structure is positivity.

For any real frequencies

```math
\omega_1,\ldots,\omega_N,
```

the matrix

```math
\boxed{
K_{jk}=H(\omega_j-\omega_k)
}
```

must be positive semidefinite.

Indeed, for arbitrary complex coefficients `c_j`,

```math
\begin{aligned}
\sum_{jk}c_j^*K_{jk}c_k
&=\mathbb E\left[
\left|\sum_jc_je^{i\omega_jT}\right|^2
\right]\\
&\ge0.
\end{aligned}
```

Thus

```math
\boxed{K\succeq0.}
```

This is a parameter-free consistency condition on the measured RF response itself.

---

## 3. A two-harmonic inequality

Take one RF frequency `omega` and define

```math
Z=e^{-i\omega T}.
```

Then

```math
|Z|=1,
```

```math
\mathbb E[Z]=H(\omega),
```

and

```math
\mathbb E[Z^2]=H(2\omega).
```

The centered second complex moment is

```math
\mathbb E[(Z-\mathbb EZ)^2]
=H(2\omega)-H(\omega)^2.
```

Using

```math
|\mathbb E[X]|
\le\mathbb E[|X|]
```

with `X=(Z-EZ)^2`,

```math
\left|
H(2\omega)-H(\omega)^2
\right|
\le
\mathbb E[|Z-\mathbb EZ|^2].
```

But

```math
\mathbb E[|Z-\mathbb EZ|^2]
=1-|H(\omega)|^2.
```

Therefore

```math
\boxed{
\left|
H(2\omega)-H(\omega)^2
\right|
\le
1-|H(\omega)|^2.
}
\tag{1}
```

This uses only two harmonics.

No transport coefficient appears.

---

## 4. Geometric interpretation

For a measured value

```math
h=H(\omega),
```

the second-harmonic response must lie inside the closed disk

```math
\boxed{
H(2\omega)
\in
\left\{
z:\ |z-h^2|\le1-|h|^2
\right\}.
}
```

Thus one complex measurement at `omega` constrains the entire allowed region of the complex response at `2 omega`.

Examples:

### Deterministic transit

If every carrier has one identical transit time `T0`,

```math
|H(\omega)|=1
```

and the disk collapses to a point:

```math
\boxed{
H(2\omega)=H(\omega)^2.
}
```

### Broad transit-time distribution

If `|H(omega)|<1`, the allowed disk acquires finite radius.

Timing dispersion therefore appears geometrically as freedom of the higher harmonic around the deterministic prediction.

---

## 5. Three-frequency positive-semidefinite test

The two-harmonic inequality is one projection of the more general PSD requirement.

For the frequency set

```math
\{0,\omega,2\omega\},
```

define

```math
h=H(\omega),
\qquad
g=H(2\omega).
```

The characteristic matrix is

```math
K=
\begin{pmatrix}
1&h^*&g^*\\
h&1&h^*\\
g&h&1
\end{pmatrix}.
```

Positive semidefiniteness requires every principal minor to be nonnegative, including

```math
\boxed{
\det K
=
1-2|h|^2-|g|^2
+2\Re[g(h^*)^2]
\ge0.
}
\tag{2}
```

Equation (2) is algebraically equivalent to Eq. (1) after squaring the disk inequality:

```math
|g-h^2|^2\le(1-|h|^2)^2.
```

Larger frequency sets provide strictly richer consistency tests through the eigenvalues of `K`.

---

## 6. Why this is a useful detector null test

Suppose an experiment reports a normalized complex response `H(omega)` and interprets it as carrier timing.

If the characteristic-function constraints fail beyond uncertainty, then the response cannot be represented as

```math
H(\omega)=\int_0^\infty p_T(t)e^{-i\omega t}\,dt
```

with

```math
p_T(t)\ge0,
\qquad
\int p_T(t)dt=1.
```

That means the problem occurs **before** choosing a drift-diffusion law.

Possible explanations include

```text
incomplete electrical/optical de-embedding,
signed current components,
multiple interfering signal pathways,
coherent response not reducible to a positive delay mixture,
nonlinear measurement response,
or an incorrect identification of the measured transfer with a first-passage timing characteristic function.
```

A violation does not uniquely identify which explanation is correct.

---

## 7. Important asymmetry of interpretation

### If the Level-0 test fails

Then ordinary classical first-passage timing models, including the local drift-diffusion model used later in this project, cannot be applied directly to that de-embedded observable.

### If the Level-0 test passes

Do **not** conclude that drift-diffusion is correct.

Passing only establishes consistency with *some* positive classical transit-time distribution over the tested RF set.

The hierarchy must continue:

```text
Level 0:
positive transit-time distribution?

Level 1:
real frequency-independent local second-order Markov drift-diffusion?

Level 2:
if not, what minimal memory/nonlocal extension restores closure?
```

---

## 8. Statistical implementation

With noisy measurements, do not test the raw inequality by eye.

For Eq. (1), define the signed margin

```math
\boxed{
M(\omega)
=
1-|H(\omega)|^2
-
|H(2\omega)-H(\omega)^2|.
}
```

The classical timing null requires

```math
M(\omega)\ge0.
```

Measurement covariance for

```text
Re H(omega), Im H(omega),
Re H(2omega), Im H(2omega)
```

can be propagated through `M` by the delta method away from the modulus cusp, or more robustly by Monte Carlo/bootstrap from the complex-response covariance.

For the general PSD test, propagate the covariance to the smallest eigenvalue

```math
\lambda_{\min}(K).
```

The null requires

```math
\lambda_{\min}\ge0.
```

Finite-sample uncertainty and multiple-frequency scanning must be included before declaring a violation.

---

## 9. Numerical regression

`numerics/transit_time_characteristic_function_null_tests.py`

checks the theorem on arbitrary discrete timing distributions.

For every tested valid distribution:

```text
the two-harmonic margin remains nonnegative
the characteristic matrix remains positive semidefinite.
```

It also constructs an intentionally impossible harmonic pair

```math
H(\omega)=0.9,
\qquad
H(2\omega)=-0.9,
```

for which

```text
left side of Eq. (1) = 1.71
right side             = 0.19.
```

Such a response cannot be the characteristic function of any positive classical transit-time distribution.

---

## 10. Prior-art boundary

These characteristic-function positivity properties are classical probability theory, closely related to the standard positive-definiteness characterization of characteristic functions.

Therefore **none of the mathematics in this Level-0 section is claimed as new probability theory**.

Its role is different:

> use exact characteristic-function positivity as the first, model-independent validation layer for interpreting a photodetector's de-embedded RF response as a carrier transit-time distribution.

Whether this specific detector diagnostic has been used systematically in prior photodetector literature remains to be audited.

---

## 11. Strongest conceptual hierarchy so far

A very simple experimental logic now exists:

```text
measure complex H(omega)
        |
        v
Level 0: characteristic-function positivity
        |
        | pass
        v
infer spatial complex slope from two generation depths
        |
        v
Level 1: real D_app,w_app independent of frequency
        |
        | fail
        v
Level 2: examine trapping / relaxation / nonlocal dispersion signatures
```

This is substantially stronger than beginning with a large multiparameter transport fit.

Every level contains an exact null prediction that can fail.

---

## 12. Next theorem

The deterministic translated-feature theorem gave unusually strong local optical/transport identities.

The next question is:

> **Which relocation identities survive for completely stochastic carrier trajectories without assuming drift-diffusion?**

The natural object is the carrier's spatial occupation time before collection.

That provides the next generalization.
