# Stochastic Occupation-Time Response Theorem

**Date:** 2026-08-10  
**Status:** exact first-order path-ensemble identity for an ideal local clock perturbation; no deterministic, Markov, or drift-diffusion assumption; no novelty claim pending focused prior-art audit

## 1. Why generalize the translated-feature thought experiment?

The deterministic translation theorem produced unusually sharp identities because every carrier followed one monotonic transit path.

Real carrier motion can include

```text
diffusion,
backtracking,
random scattering,
trapping,
and stochastic transit times.
```

Rather than immediately choosing one stochastic transport equation, ask a more general question:

> **What does a weak local perturbation measure for an arbitrary ensemble of successful carrier trajectories?**

There is an exact answer if the gedanken perturbation changes only the local rate at which the trajectory clock accumulates while leaving the unperturbed path ensemble fixed to first order.

This is an ideal **local clock perturbation**.

---

## 2. Arbitrary successful paths

Let one successful carrier trajectory be

```math
X_t,
\qquad
0\le t\le T,
```

where `T` is its random transit/first-passage time to the collector.

No stochastic differential equation is assumed.

Define the spatial occupation-time density

```math
\boxed{
\ell(z)
=\int_0^T\delta(X_t-z)\,dt.
}
```

It obeys the trajectory-wise identity

```math
\boxed{
\int \ell(z)\,dz=T.
}
\tag{1}
```

`ell(z) dz` is the total time that one trajectory spends in a small neighborhood of `z`.

---

## 3. Local clock perturbation

Let a weak translated perturbation have known shape

```math
h(z-z_0)
```

and area

```math
A_h=\int h(z)dz.
```

Define the perturbed trajectory time to first order by

```math
\boxed{
T_{\epsilon,z_0}
=
T
+
\epsilon
\int_0^T h(X_t-z_0)dt
+O(\epsilon^2).
}
\tag{2}
```

Equivalently,

```math
\delta T
=
\epsilon
\int h(z-z_0)\ell(z)dz.
```

This perturbation is deliberately abstract and clean:

```text
it slows or advances the local trajectory clock,
but does not change which unperturbed path is taken at first order.
```

A real field/composition perturbation can also change path probabilities, drift, diffusion, or recombination. Those additional effects are not included in this theorem and become experimentally falsifiable corrections.

---

## 4. Complex transit-time response

Define the normalized complex timing response of the successful-path ensemble

```math
\boxed{
H(\omega)
=\mathbb E[e^{-i\omega T}].
}
\tag{3}
```

Under the local clock perturbation,

```math
H_{\epsilon,z_0}(\omega)
=\mathbb E[e^{-i\omega T_{\epsilon,z_0}}].
```

Define the first logarithmic sensitivity

```math
\boxed{
S(z_0,\omega)
=
\left.
\partial_\epsilon
\ln H_{\epsilon,z_0}(\omega)
\right|_{\epsilon=0}.
}
\tag{4}
```

Differentiate Eq. (3) using Eq. (2):

```math
\boxed{
S(z_0,\omega)
=
-i\omega
\frac{
\mathbb E\left[
e^{-i\omega T}
\int h(z-z_0)\ell(z)dz
\right]
}{H(\omega)}.
}
\tag{5}
```

This identity is exact to first order in perturbation strength.

---

## 5. Point-feature limit

For an ideal point clock perturbation

```math
h(z-z_0)=A_h\delta(z-z_0),
```

Eq. (5) becomes

```math
\boxed{
S(z,\omega)
=
-i\omega A_h
\frac{
\mathbb E[e^{-i\omega T}\ell(z)]
}{
\mathbb E[e^{-i\omega T}]
}.
}
\tag{6}
```

Define the **frequency-tilted occupation density**

```math
\boxed{
\rho_\omega(z)
=
\frac{
\mathbb E[e^{-i\omega T}\ell(z)]
}{H(\omega)}.
}
\tag{7}
```

Then simply

```math
\boxed{
S(z,\omega)=-i\omega A_h\rho_\omega(z).
}
\tag{8}
```

This is the stochastic analogue of the deterministic local sensitivity field.

Unlike an ordinary probability density, `rho_omega` is generally complex because the trajectory ensemble is tilted by its transit phase.

---

## 6. Exact global sum rule

Integrate Eq. (5) over all perturbation positions `z0`.

Because

```math
\int h(z-z_0)dz_0=A_h,
```

and Eq. (1) gives

```math
\int \ell(z)dz=T,
```

we obtain

```math
\int S(z_0,\omega)dz_0
=
-i\omega A_h
\frac{\mathbb E[Te^{-i\omega T}]}{H(\omega)}.
```

But

```math
\partial_\omega H
=-i\mathbb E[Te^{-i\omega T}],
```

so

```math
\boxed{
\int S(z,\omega)dz
=
A_h\omega\partial_\omega\ln H(\omega).
}
\tag{9}
```

This is exact for the arbitrary path ensemble.

### Interpretation

The total response obtained by scanning the local clock perturbation through all space is fixed by the **frequency derivative of the unperturbed global response**.

The local scan and the global RF transfer are therefore not independent datasets.

They must satisfy Eq. (9).

A reproducible violation falsifies at least one assumption of the local-clock linear-response construction.

---

## 7. Low-frequency expansion — mean occupation and timing dispersion

Expand Eq. (7) around `omega=0`.

The numerator is

```math
\mathbb E[e^{-i\omega T}\ell(z)]
=
\mathbb E[\ell(z)]
-i\omega\mathbb E[T\ell(z)]
+O(\omega^2).
```

Also

```math
H(\omega)
=1-i\omega\mathbb E[T]+O(\omega^2).
```

Therefore

```math
\boxed{
\rho_\omega(z)
=
\mathbb E[\ell(z)]
-i\omega\operatorname{Cov}(T,\ell(z))
+O(\omega^2).
}
\tag{10}
```

and

```math
\boxed{
\frac{S(z,\omega)}{-i\omega A_h}
=
\mathbb E[\ell(z)]
-i\omega\operatorname{Cov}(T,\ell(z))
+O(\omega^2).
}
\tag{11}
```

This has a direct physical interpretation.

### Leading term

```math
\boxed{
\mathbb E[\ell(z)]
}
```

is the mean time successful carriers spend near depth `z`.

### Next term

```math
\boxed{
\operatorname{Cov}(T,\ell(z))
}
```

measures whether trajectories that linger near `z` tend to have longer or shorter total transit times.

Thus the first frequency correction localizes the spatial origin of transit-time dispersion.

---

## 8. Two exact moment sum rules

Integrating Eq. (10) over space gives two immediate identities.

First,

```math
\boxed{
\int\mathbb E[\ell(z)]dz
=\mathbb E[T].
}
\tag{12}
```

Second,

```math
\begin{aligned}
\int\operatorname{Cov}(T,\ell(z))dz
&=\operatorname{Cov}\left(T,\int\ell(z)dz\right)\\
&=\operatorname{Cov}(T,T).
\end{aligned}
```

Therefore

```math
\boxed{
\int\operatorname{Cov}(T,\ell(z))dz
=\operatorname{Var}(T).
}
\tag{13}
```

This is a strong spatial decomposition:

> **the global mean transit time is the integral of the local mean occupation field, while the global transit-time variance is the integral of the local occupation/transit covariance field.**

The latter gives a rigorous meaning to the phrase “where the timing dispersion comes from.”

---

## 9. A normalized residence-time distribution

Because Eq. (12) is positive at zero frequency, define

```math
\boxed{
\pi_{\rm occ}(z)
=
\frac{\mathbb E[\ell(z)]}{\mathbb E[T]}.
}
\tag{14}
```

Then

```math
\pi_{\rm occ}(z)\ge0,
\qquad
\int\pi_{\rm occ}(z)dz=1.
```

This is not the generation-position distribution.

It is the distribution of **where successful trajectories spend their mean transit time**.

A region can have small generation probability yet dominate `pi_occ` if carriers repeatedly revisit or linger there.

This sharply distinguishes the stochastic theorem from the deterministic generation-density factorization.

---

## 10. Deterministic monotonic path as a special case

Suppose a carrier generated at position `x` moves monotonically to `L` with local slowness

```math
q(z)=1/v(z).
```

For that trajectory,

```math
\ell_x(z)=q(z)\,\mathbf 1_{x\le z\le L}.
```

Averaging over generation position `X` gives

```math
\boxed{
\mathbb E[\ell(z)]
=q(z)F_X(z),
}
\tag{15}
```

where

```math
F_X(z)=P(X\le z).
```

Thus the stochastic occupation theorem reduces to the familiar downstream cumulative timing kernel at low RF.

Backtracking/diffusion modifies the occupation field away from this one-pass expression.

---

## 11. New falsifiable contrast with deterministic transit

For deterministic monotonic transport, each generation point has one transit time and one-pass occupation.

Then the earlier translated-delay theorem predicts a much stronger optical/transport factorization.

For stochastic paths, the point clock response instead contains

```math
\rho_\omega(z)
=\frac{\mathbb E[e^{-i\omega T}\ell(z)]}{H}.
```

Therefore departures from the deterministic factorization have a precise interpretation:

```text
revisiting/backtracking
path-to-path transit dispersion
or correlations between local residence and total transit time.
```

At low RF the first such correction is exactly the covariance field in Eq. (11).

---

## 12. Finite-width perturbation

For a general known `h`, Eq. (5) is a convolution of the point occupation field:

```math
\boxed{
S(z_0,\omega)
=
-i\omega
\int h(z-z_0)\rho_\omega(z)dz.
}
\tag{16}
```

Thus finite feature width again acts as a known spatial point-spread function.

In noiseless data it can be deconvolved over spatial frequencies where the feature transfer function is nonzero.

In noisy data, width imposes a practical bandwidth/noise tradeoff rather than changing the exact underlying identity.

---

## 13. What kind of real perturbation approximates the clock gedanken?

Equation (2) is an idealization.

A physical perturbation approximates it when, to first order, it changes the local residence-time accumulation while negligibly changing

```text
path branching probabilities,
spatial diffusion statistics,
recombination probability,
and the optical generation kernel.
```

A real composition-gradient or electric-field perturbation generally does **not** satisfy this exactly because it changes the transport generator itself.

Therefore the occupation theorem should be used in two ways:

1. as an exact conceptual baseline;
2. as a null prediction whose failure quantifies how strongly the perturbation reshapes the path ensemble rather than merely changing its local clock.

This is preferable to silently assuming a real device feature is a pure clock perturbation.

---

## 14. Relation to Feynman-Kac / occupation-time mathematics

Occupation-time generating functionals and their relation to local perturbations are established tools in stochastic-process theory.

Therefore the mathematical machinery itself should not be presented as new probability theory.

The candidate detector contribution, if any, would be the use of a controlled translated internal perturbation plus complex RF response to spatially resolve

```text
mean successful-carrier occupation time
and local contributions to transit-time dispersion,
```

followed by exact sum-rule consistency tests.

A focused prior-art audit is still required before any priority language.

---

## 15. Numerical verification

`numerics/stochastic_occupation_time_response_theorem.py`

uses an arbitrary finite ensemble of successful trajectories specified only by

```text
trajectory probabilities,
random transit times,
and occupation times in spatial bins.
```

No drift-diffusion law is imposed.

The regression verifies to numerical precision that

```math
\int S dz
=A_h\omega\partial_\omega\ln H
```

and that the small-RF expansion approaches

```math
\mathbb E[\ell(z)]
-i\omega\operatorname{Cov}(T,\ell(z)).
```

It also verifies the integrated covariance identity

```math
\int\operatorname{Cov}(T,\ell(z))dz
=\operatorname{Var}(T).
```

---

## 16. Why this result matters to the paper structure

The project now has three nested descriptions with exact boundaries:

```text
ANY positive timing distribution
-> characteristic-function positivity tests

ANY stochastic successful paths + pure local clock perturbation
-> occupation-time response and sum rules

LOCAL second-order Markov conditioned transport
-> frequency-independent real D_app,w_app closure

DETERMINISTIC monotonic transit
-> strongest optical-generation / local-slowness factorization.
```

Each stronger model predicts additional identities.

That creates a natural **falsification ladder** rather than one monolithic transport fit.

---

## 17. Next question

The next theoretical target is now very specific:

> **Can the hierarchy be expressed as a compact set of nested experimentally measurable invariants whose pattern of failure distinguishes deterministic transit, stochastic local Markov transport, and genuinely memory/nonlocal transport?**

That would provide the conceptual spine for a full paper.
