# Occupation-Time Cumulant Hierarchy — Spatially Resolving Every Transit-Time Cumulant

**Date:** 2026-08-10  
**Status:** exact consequence of the stochastic occupation-time response theorem; arbitrary successful path ensemble; no Markov or drift-diffusion assumption; no novelty claim pending prior-art audit

## 1. Starting point

For an arbitrary successful carrier trajectory with transit time `T` and occupation-time density

```math
\ell(z)=\int_0^T\delta(X_t-z)dt,
```

the point-like local-clock theorem defines

```math
\rho_\omega(z)
=
\frac{
\mathbb E[e^{-i\omega T}\ell(z)]
}{
\mathbb E[e^{-i\omega T}]
}.
```

The local logarithmic perturbation response is

```math
S(z,\omega)
=-i\omega A_h\rho_\omega(z).
```

The previous result showed

```math
\rho_\omega(z)
=
\mathbb E[\ell(z)]
-i\omega\operatorname{Cov}(T,\ell(z))
+O(\omega^2).
```

That expansion continues exactly to all orders.

---

## 2. Joint cumulant generating function

Introduce two auxiliary variables

```math
s,
\qquad
\eta,
```

and define

```math
\boxed{
K_z(s,\eta)
=
\ln
\mathbb E[
e^{sT+\eta\ell(z)}
].
}
```

Then

```math
\left.
\partial_\eta K_z(s,\eta)
\right|_{\eta=0}
=
\frac{
\mathbb E[e^{sT}\ell(z)]
}{
\mathbb E[e^{sT}]
}.
```

Setting

```math
s=-i\omega
```

gives precisely `rho_omega(z)`.

By the definition of joint cumulants,

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
\tag{1}
```

This is the full local timing-cumulant expansion.

---

## 3. First terms

Equation (1) begins

```math
\boxed{
\rho_\omega(z)
=
\mathbb E[\ell(z)]
-i\omega\operatorname{Cov}[\ell(z),T]
-
\frac{\omega^2}{2}
\kappa[\ell(z),T,T]
+
\frac{i\omega^3}{6}
\kappa[\ell(z),T,T,T]
+\cdots.
}
\tag{2}
```

Therefore the local clock response contains a hierarchy:

```text
omega^1 response -> mean local residence time
omega^2 correction -> local contribution to timing variance
omega^3 correction -> local contribution to timing skewness
omega^4 correction -> local contribution to fourth timing cumulant
etc.
```

The alternating real/imaginary structure follows directly from `s=-i omega`.

---

## 4. Exact spatial sum rule at every order

Every trajectory obeys

```math
\int\ell(z)dz=T.
```

Cumulants are linear in each argument separately.

Therefore

```math
\begin{aligned}
\int dz\,
\kappa(
\ell(z),T,\ldots,T
)
&=
\kappa
\left(
\int\ell(z)dz,
T,\ldots,T
\right)\\
&=\kappa(T,T,\ldots,T).
\end{aligned}
```

Hence

```math
\boxed{
\int dz\,
\kappa
\left(
\ell(z),
\underbrace{T,\ldots,T}_{n}
\right)
=
\kappa_{n+1}(T).
}
\tag{3}
```

This is exact for every order for which the cumulant exists.

---

## 5. Explicit first three global identities

For `n=0`,

```math
\boxed{
\int dz\,\mathbb E[\ell(z)]
=\mathbb E[T].
}
```

For `n=1`,

```math
\boxed{
\int dz\,\operatorname{Cov}[\ell(z),T]
=\operatorname{Var}(T).
}
```

For `n=2`,

```math
\boxed{
\int dz\,\kappa[\ell(z),T,T]
=\kappa_3(T)
=
\mathbb E[(T-\mathbb E T)^3].
}
```

Thus the global timing skewness numerator has an exact spatial decomposition just as the mean and variance do.

Higher cumulants follow identically.

---

## 6. Interpretation — 'where does the non-Gaussian timing come from?'

Ordinary detector timing descriptions often compress the response into

```text
mean delay
rise time
bandwidth
or one effective lifetime.
```

The occupation hierarchy asks a more detailed but still rigorous question:

> **Which regions of the device are statistically associated with the mean, variance, skewness, and higher cumulants of successful transit time?**

The answers are the local mixed-cumulant fields

```math
c_n(z)
=
\kappa(
\ell(z),T,\ldots,T
).
```

These fields need not be positive for `n>=1`.

A region can

```text
increase global timing variance,
reduce it through anticorrelation,
or dominate asymmetric long-tail timing
```

according to the sign and magnitude of its mixed cumulants.

---

## 7. This is stronger than a local 'lifetime' map

A local lifetime or velocity map assigns one scalar material parameter to each depth.

The cumulant hierarchy instead characterizes the **statistics of successful paths**.

For example two regions may have the same mean occupation time but very different

```math
\operatorname{Cov}[\ell(z),T].
```

One region may be visited similarly by nearly every trajectory, while the other is visited mainly by the rare trajectories that form the long-time tail.

The mean map alone cannot distinguish them.

The frequency dependence of the local-clock response can.

---

## 8. Relation to the global RF transfer

The exact occupation sum rule is

```math
\int S(z,\omega)dz
=A_h\omega\partial_\omega\ln H(\omega).
```

Expanding

```math
\ln H(\omega)
=
\sum_{m=1}^{\infty}
\frac{(-i\omega)^m}{m!}
\kappa_m(T)
```

and differentiating gives

```math
A_h\omega\partial_\omega\ln H
=
A_h
\sum_{m=1}^{\infty}
\frac{(-i)^m\omega^m}{(m-1)!}
\kappa_m(T).
```

This is exactly the spatial integral of

```math
S(z,\omega)
=-i\omega A_h\rho_\omega(z)
```

using Eq. (3).

Thus the local and global cumulant descriptions are mathematically locked together at every order.

---

## 9. Falsifiable predictions

If an experimental perturbation is a sufficiently good local-clock perturbation, then the following must hold.

### P1 — mean sum rule

The spatial integral of the zero-frequency occupation field equals the measured mean transit time.

### P2 — variance sum rule

The integral of the first frequency-derivative field equals the global transit-time variance.

### P3 — skewness sum rule

The integral of the second frequency-derivative field equals the global third timing cumulant.

### P4 — full generating-function sum rule

All orders are simultaneously summarized by

```math
\int S dz=A_h\omega\partial_\omega\ln H.
```

A measured local response that cannot reproduce the independently measured global timing cumulants violates the pure local-clock model.

---

## 10. What a violation means

A failed cumulant sum rule does **not** imply exotic transport automatically.

The physical perturbation may have changed more than the local clock, for example

```text
the drift field,
diffusion coefficient,
path probabilities,
recombination,
optical generation,
or boundary conditions.
```

The theorem is useful precisely because those effects can no longer hide inside an undefined 'local timing perturbation.'

They become explicit departures from an exact baseline.

---

## 11. Mathematical prior-art boundary

Joint cumulant-generating functions, occupation times, and Feynman-Kac-type perturbation identities are established stochastic-process mathematics.

Do not claim Eq. (1) as new probability theory without a dedicated literature review.

The potential detector contribution is the proposed **spatial perturbation spectroscopy interpretation**:

```text
frequency-resolved local clock response
-> mixed occupation/transit cumulants
-> spatial decomposition of detector timing statistics
-> exact global consistency sum rules.
```

Priority remains unproven.

---

## 12. Numerical regression

`numerics/occupation_time_cumulant_hierarchy.py`

uses an arbitrary discrete path ensemble and verifies

```math
\int \kappa(\ell)dz=\kappa_1(T),
```

```math
\int \kappa(\ell,T)dz=\kappa_2(T),
```

```math
\int \kappa(\ell,T,T)dz=\kappa_3(T),
```

plus the second-order expansion of `rho_omega(z)`.

---

## 13. Paper-level role

This result suggests a broader target than reconstructing a spatial velocity profile:

> **Use controlled internal perturbations and complex frequency response to spatially decompose the statistical structure of carrier transit itself.**

The mean is only the first member of an exact hierarchy.

That gives a natural bridge from simple deterministic detector timing to stochastic, trapping-dominated, or non-Gaussian transport without committing prematurely to one microscopic model.
