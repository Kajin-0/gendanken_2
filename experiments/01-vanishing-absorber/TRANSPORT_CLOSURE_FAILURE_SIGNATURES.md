# Falsification Hierarchy Beyond Local Markov Drift-Diffusion

**Date:** 2026-08-10  
**Status:** exact/archetypal theory results inside explicitly stated reduced models; mechanisms are diagnostic examples, not unique microscopic identifications; no novelty claim

## 1. Purpose

The exact closure theorem says that a real, frequency-independent local second-order Markov generator exists at depth `z` if and only if

```math
D_{\rm app}(z,\omega)
```

and

```math
w_{\rm app}(z,\omega)
```

are independent of RF frequency.

That gives a null test, but closure failure alone does not identify the cause.

The next question is:

> **What kinds of frequency dispersion should simple departures from local Markov drift-diffusion produce?**

The goal is a hierarchy of falsifiable signatures, not an ever-larger fit model.

---

## 2. A general temporal-memory form

For a uniform conditioned transport segment, ordinary local drift-diffusion gives

```math
D r^2+w r=s,
\qquad s=i\omega.
```

A broad class of temporal-memory models can instead be written

```math
\boxed{
D r^2+w r=\Psi(s).
}
```

Suppose near `s=0`

```math
\Psi(s)
=c_1s+c_2s^2+c_3s^3+\cdots.
```

If the resulting response is *incorrectly* forced into ordinary drift-diffusion, then its low-frequency apparent coefficients approach

```math
\boxed{
w_{\rm app}(0)=\frac{w}{c_1},
}
```

and

```math
\boxed{
D_{\rm app}(0)
=\frac{D}{c_1}
-\frac{c_2w^2}{c_1^3}.
}
```

### Consequence

> **Low-frequency agreement with an ordinary drift-diffusion fit does not establish Markov transport. Memory can hide inside renormalized apparent drift and diffusion coefficients.**

The falsifiable prediction of the Markov model is not merely that one frequency can be fitted.

It is

```math
\boxed{
\partial_\omega D_{\rm app}=0,
\qquad
\partial_\omega w_{\rm app}=0
}
```

through the frequency range where the reduced model is supposed to apply.

---

## 3. Archetype A — reversible trapping

Consider a mobile state that can be immobilized at rate `k_t` and released at rate `k_d`.

Eliminating the trapped population in frequency/Laplace space gives the simple memory factor

```math
\boxed{
\Psi_{\rm trap}(s)
=s\left(1+\frac{k_t}{k_d+s}\right).
}
```

This is a one-pole Debye-like memory kernel.

Its low-frequency expansion is

```math
\Psi_{\rm trap}(s)
=
\left(1+\frac{k_t}{k_d}\right)s
-
\frac{k_t}{k_d^2}s^2
+
\frac{k_t}{k_d^3}s^3
+\cdots.
```

Therefore ordinary drift-diffusion inferred at very low RF approaches

```math
\boxed{
w_{\rm app}(0)
=
\frac{w}{1+k_t/k_d},
}
```

and

```math
\boxed{
D_{\rm app}(0)
=
\frac{D}{1+k_t/k_d}
+
\frac{(k_t/k_d^2)w^2}
{(1+k_t/k_d)^3}.
}
```

Thus trapping can masquerade simultaneously as

```text
slower apparent drift
+
a strongly modified apparent diffusion coefficient.
```

The disguise fails as `omega` approaches the release rate `k_d`; both apparent coefficients develop a characteristic turnover.

At very high frequency the trap population cannot follow the modulation in the same way, so the response moves away from the low-frequency renormalized coefficients.

### Prediction

A reproducible coefficient turnover centered around one characteristic RF scale is consistent with a finite release-time memory mode.

It is **not unique evidence for trapping**, but it is incompatible with one frequency-independent second-order Markov generator.

---

## 4. Archetype B — finite flux / momentum-relaxation time

A minimal hyperbolic or telegraph-like correction writes

```math
\boxed{
\Psi_{\rm rel}(s)=s(1+\tau_J s).
}
```

Here `tau_J` is a flux-relaxation time.

The ordinary low-RF apparent coefficients become

```math
\boxed{
w_{\rm app}(0)=w,
}
```

```math
\boxed{
D_{\rm app}(0)=D-\tau_Jw^2.
}
```

Thus a finite transport-relaxation time can hide at low RF as a shifted diffusion coefficient even when the apparent drift remains correct.

For sufficiently small `tau_J`, the next dispersion is quadratic in frequency.

Using the exact series from the uniform-channel inverse,

```math
D_{\rm app}(\omega)
=
D-\tau_Jw^2
+
O(\omega^2),
```

```math
w_{\rm app}(\omega)
=
w+O(\omega^2).
```

### Prediction

A low-frequency plateau followed by even-in-frequency dispersion is a natural signature of a finite relaxation-time correction.

Again, the signature is model-class evidence, not unique microscopic identification.

---

## 5. Archetype C — leading spatially nonlocal correction

A spatially nonlocal transport generator can be expanded formally in higher spatial derivatives when the nonlocal length is short but not negligible.

The first asymmetric correction may be represented by

```math
\boxed{
C F'''
+D F''
+w F'
-sF=0.
}
```

Define

```math
B=\frac{F'''}{F}
=r''+3rr'+r^3.
```

Then the ordinary second-order closure residual is

```math
\boxed{
\mathcal R
=D A+w r-s
=-CB.
}
```

In a uniform drift-dominated low-frequency limit,

```math
r\sim\frac{s}{w},
```

so

```math
\boxed{
\mathcal R
\sim
-C\left(\frac{s}{w}\right)^3.
}
```

For `s=i omega`, the leading violation is therefore cubic in RF frequency and approximately quadrature-like.

More directly, forcing this model into ordinary drift-diffusion gives

```math
\boxed{
D_{\rm app}(\omega)
=D+\frac{2CD}{w^3}\omega^2+O(\omega^4),
}
```

```math
\boxed{
w_{\rm app}(\omega)
=w-\frac{C}{w^2}\omega^2+O(\omega^4).
}
```

Unlike the temporal-memory examples above, the zero-frequency apparent coefficients return to the actual local `D,w`; the violation grows away from zero frequency.

A symmetric nonlocal kernel whose first new term is fourth order would instead begin at still higher order.

---

## 6. What does *not* break the closure

Several effects that look complicated experimentally are **not** by themselves closure violations.

### Arbitrary spatial grading

`D(z)` and `w(z)` may vary rapidly with depth.

The exact relation

```math
D(z)A_\omega(z)+w(z)r_\omega(z)=i\omega
```

still holds pointwise.

Therefore

> **inhomogeneity alone is not evidence for nonlocal transport.**

### Ordinary recombination after DC conditioning

If killing/recombination is local and Markovian, DC normalization performs the previously derived conditioning transformation.

The normalized RF field still obeys a second-order local equation with

```math
w_{\rm cond}
=v+2D\partial_z\ln h.
```

Thus ordinary local recombination changes the conditioned drift but does not create RF-frequency dispersion in the conditioned local coefficients.

### A static contact or boundary condition

A boundary condition can strongly alter the global response field.

But if the interior dynamics remain one local Markov second-order process, the pointwise interior closure still holds away from singular/boundary regions.

A genuinely frequency-dependent interface can, however, break the closure near the boundary and must be treated separately.

---

## 7. Falsification hierarchy

The theory suggests the following order of questions.

### Level 1 — local Markov closure

Measure

```math
D_{\rm app}(z,\omega),
\qquad
w_{\rm app}(z,\omega).
```

If both are frequency independent within uncertainty, the local second-order Markov description survives.

If not, it is falsified at that depth.

### Level 2 — dispersion shape

If closure fails, ask whether the frequency dependence resembles

```text
one-pole turnover -> finite-state trapping / exchange archetype
low-frequency renormalization + quadratic dispersion -> relaxation archetype
zero-frequency recovery + growing even-power dispersion -> short-range spatial nonlocal correction
power-law dispersion -> broad/distributed memory candidate
```

These are hypotheses to test, not labels to assign automatically.

### Level 3 — extended closure

Each mechanism adds a specific extra state or operator.

For example a third-spatial-derivative model predicts

```math
D A+w r+C B=i\omega.
```

With enough RF frequencies, that **extended** model is again overdetermined and can itself be falsified.

This creates a nested sequence:

```text
2-coefficient local Markov model
-> fail
3-coefficient spatial correction
-> pass/fail
explicit trap-state model
-> pass/fail
etc.
```

The objective is not unlimited flexibility.

The objective is to add the **smallest new physical state needed to restore closure**.

---

## 8. Connection to semiconductor transport physics

The reduced archetypes correspond to known reasons ordinary semiconductor drift-diffusion can fail or become incomplete:

```text
trapping and detrapping
finite carrier momentum/energy relaxation
hot-carrier transport
quasi-ballistic or nonlocal transport
higher-moment transport physics.
```

Primary semiconductor literature already treats frequency-dependent/trapped-carrier response and extensions beyond ordinary drift-diffusion. Therefore none of those mechanisms is claimed as new.

The candidate contribution is the **parameter-free local closure/falsification protocol when internal generation depth is supplied spectrally**.

---

## 9. Numerical stress

`numerics/transport_closure_failure_archetypes.py`

constructs

```text
ordinary Markov drift-diffusion
reversible one-pole trapping
finite flux relaxation
leading third-order spatial correction
```

and forces all four into the ordinary real `D_app,w_app` inference.

The baseline remains frequency independent to numerical precision.

All three departures develop measurable coefficient dispersion on the chosen dimensionless frequency range, while several of them appear as perfectly plausible **renormalized constants** as `omega -> 0`.

That is the central warning:

> **one-frequency agreement is not a model test. Multi-frequency closure is.**

---

## 10. Next limitation — differentiation noise

For arbitrary spatially varying transport, evaluating

```math
A=r'+r^2
```

requires a second spatial derivative of `ln F`.

The theory is structurally exact but experimental inference is therefore differentiation-noise limited.

The next calculation is to derive the bias-variance optimum and the scaling of achievable depth resolution with complex-response precision.
