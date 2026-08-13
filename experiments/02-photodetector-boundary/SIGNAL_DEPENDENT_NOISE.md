# Signal-Dependent Noise — Experiment 02

**Date:** 2026-08-12  
**Status:** active conditional derivation  
**Priority:** unassessed; no novelty claim

This file removes the equal-covariance assumption used in `CONTINUOUS_GAUSSIAN_DECISION.md` and then treats the canonical count-noise limit directly with Poisson statistics.

The purpose is to determine what happens to the detector boundary when the optical history changes not only the mean output but also its fluctuations.

---

## 1. General Gaussian hypotheses with different covariance

Let a discretized electrical record `y` obey

```math
H_0:\quad y\sim\mathcal N(\mu_0,C_0),
```

```math
H_1:\quad y\sim\mathcal N(\mu_1,C_1).
```

For equal priors, the log-likelihood ratio is

```math
\boxed{
\ell(y)
=
\frac12(y-\mu_0)^TC_0^{-1}(y-\mu_0)
-
\frac12(y-\mu_1)^TC_1^{-1}(y-\mu_1)
-
\frac12\ln\frac{\det C_1}{\det C_0}.
}
```

Choose `H1` when `ell(y)>0`.

When

```math
C_0=C_1=C,
```

the quadratic terms cancel and the statistic reduces to the linear matched-filter result already derived.

When

```math
C_0\ne C_1,
```

the optimum decision surface is generally quadratic.

This is the first important correction:

```text
signal-dependent noise
-> different output distribution shape
-> optimum detector is not generally a linear matched filter.
```

---

## 2. Covariance itself can carry photon information

Set

```math
\mu_0=\mu_1.
```

If

```math
C_0\ne C_1,
```

the likelihood ratio is still nonconstant.

Therefore a detector can, in principle, discriminate the optical histories from a change in fluctuation statistics even when the mean waveform is unchanged.

This yields a deeper statement:

> **The physical detector output is a probability distribution, not merely a mean signal plus an external nuisance called noise.**

Signal-dependent noise can be detrimental to mean-amplitude readout while simultaneously being part of the information-bearing record.

This does **not** mean more noise is generally beneficial. It means the distinction between `signal` and `noise` depends on the chosen inference task.

---

## 3. Bhattacharyya distance separates mean and covariance evidence

For two multivariate Gaussians define

```math
\Sigma=\frac{C_0+C_1}{2},
\qquad
\Delta\mu=\mu_1-\mu_0.
```

Their Bhattacharyya distance is

```math
\boxed{
D_B
=
\frac18\Delta\mu^T\Sigma^{-1}\Delta\mu
+
\frac12\ln
\frac{\det\Sigma}
{\sqrt{\det C_0\det C_1}}.
}
```

The first term measures mean separation in the averaged noise metric.

The second term is nonzero purely because the covariance structures differ.

For equal priors, the standard Bhattacharyya bound gives

```math
\boxed{
P_e
\le
\frac12 e^{-D_B}.
}
```

The bound need not be tight, but the decomposition is useful:

```text
mean-history information
+
covariance-history information.
```

---

## 4. Scalar variance-only Gedanken experiment

Take

```math
H_0:\quad y\sim\mathcal N(0,\sigma_0^2),
```

```math
H_1:\quad y\sim\mathcal N(0,\sigma_1^2),
\qquad \sigma_1>\sigma_0.
```

The means are identical.

The two probability densities cross at `y=+-y_c`, where

```math
\boxed{
y_c^2
=
\frac{2\ln(\sigma_1/\sigma_0)}
{1/\sigma_0^2-1/\sigma_1^2}.
}
```

The optimum equal-prior rule is

```text
|y| < y_c  -> H0
|y| > y_c  -> H1.
```

Thus a variance change alone is a readable detector record.

The exact equal-prior error is

```math
\boxed{
P_e
=
Q\!\left(\frac{y_c}{\sigma_0}\right)
+
\Phi\!\left(\frac{y_c}{\sigma_1}\right)
-\frac12,
}
```

where `Phi` is the standard normal CDF and `Q=1-Phi`.

This is a clean counterexample to the statement

```text
no mean signal -> no detection information.
```

---

## 5. Why this matters for photodetectors

Several detector processes naturally make the output fluctuations hypothesis dependent:

```text
photon / carrier shot noise
photo-generation-recombination fluctuations
avalanche multiplication noise
signal-dependent trapping / detrapping
state-dependent thermal conductance or Johnson noise
etc.
```

In such regimes a conventional signal-to-noise ratio based only on mean response and a single noise PSD can discard information that an optimum likelihood-ratio detector would use.

Conversely, if the detector task is estimation of mean optical power rather than binary hypothesis testing, the increased variance may remain purely harmful for that estimator.

The task specification therefore matters at the noise-definition level too.

---

## 6. Count statistics should be treated as Poisson before Gaussianizing

For an ideal count channel, let the observed number of elementary events in a window be `K`.

Under the two hypotheses,

```math
H_0:\quad K\sim\operatorname{Poisson}(\mu_0),
```

```math
H_1:\quad K\sim\operatorname{Poisson}(\mu_1),
\qquad \mu_1>\mu_0.
```

The exact log-likelihood ratio is

```math
\boxed{
\ell(K)
=
K\ln\frac{\mu_1}{\mu_0}
-(\mu_1-\mu_0).
}
```

Thus the optimum rule is a count threshold.

For equal priors, the continuous threshold before integer rounding is

```math
\boxed{
K_c
=
\frac{\mu_1-\mu_0}
{\ln(\mu_1/\mu_0)}.
}
```

The exact minimum error is

```math
\boxed{
P_e
=\frac12\sum_{k=0}^{\infty}
\min[P_0(k),P_1(k)].
}
```

This is the discrete analogue of the full-distribution viewpoint.

---

## 7. Exact Poisson Bhattacharyya coefficient

For Poisson means `mu_0` and `mu_1`,

```math
\sum_{k=0}^{\infty}
\sqrt{P_0(k)P_1(k)}
=
\exp\left[
-\frac12
(\sqrt{\mu_1}-\sqrt{\mu_0})^2
\right].
```

Therefore the equal-prior Bhattacharyya error bound is

```math
\boxed{
P_e
\le
\frac12
\exp\left[
-\frac12
(\sqrt{\mu_1}-\sqrt{\mu_0})^2
\right].
}
```

This exposes a natural count-noise distance:

```math
\boxed{
\mathcal J_P
=(\sqrt{\mu_1}-\sqrt{\mu_0})^2.
}
```

The square-root count coordinate is not an arbitrary transform; it appears directly in the overlap of the two Poisson distributions.

---

## 8. Background + signal count-rate model

Let

```text
lambda_d = background / dark event rate
lambda_s = additional signal event rate
T        = observation time.
```

Then

```math
\mu_0=\lambda_dT,
```

```math
\mu_1=(\lambda_d+\lambda_s)T.
```

The Poisson overlap exponent becomes

```math
\boxed{
-\ln BC
=
\frac{T}{2}
\left(
\sqrt{\lambda_d+\lambda_s}
-
\sqrt{\lambda_d}
\right)^2.
}
```

Thus evidence accumulates linearly with observation time in the exponent.

Define the Bhattacharyya information rate

```math
\boxed{
\mathcal R_B
=
\frac12
\left(
\sqrt{\lambda_d+\lambda_s}
-
\sqrt{\lambda_d}
\right)^2.
}
```

Then

```math
BC=e^{-\mathcal R_BT}.
```

This gives a rate-domain version of the detector boundary for ideal count statistics.

---

## 9. Weak-signal limit recovers conventional shot-noise scaling

For

```math
\lambda_s\ll\lambda_d,
```

expand

```math
\sqrt{\lambda_d+\lambda_s}
-
\sqrt{\lambda_d}
\simeq
\frac{\lambda_s}{2\sqrt{\lambda_d}}.
```

Therefore

```math
\boxed{
\mathcal R_B
\simeq
\frac{\lambda_s^2}{8\lambda_d}.
}
```

The exponent after time `T` scales as

```math
\frac{\lambda_s^2T}{\lambda_d},
```

which is the familiar background-shot-noise signal-to-noise scaling up to the convention-dependent numerical factor associated with the chosen error bound.

Thus the ordinary Gaussian SNR picture emerges as a local approximation to the full Poisson distribution geometry.

---

## 10. Zero-background limit behaves qualitatively differently

If

```math
\lambda_d=0,
```

then under `H0`

```math
K=0
```

with certainty, while under `H1`

```math
K\sim\operatorname{Poisson}(\lambda_sT).
```

The optimum equal-prior rule is simply

```text
K=0 -> H0
K>=1 -> H1.
```

The exact error is then

```math
\boxed{
P_e
=\frac12e^{-\lambda_sT}.
}
```

This is not the quadratic weak-signal scaling of the background-dominated limit.

It shows that the detector resource law changes qualitatively when the background channel vanishes.

Another attempted universal scalar therefore fails:

```text
one SNR formula
```

cannot describe both zero-background event detection and background-dominated detection.

---

## 11. Signal-dependent noise can be information and cost simultaneously

The results force a more precise statement.

Suppose the photon history increases both the mean and the variance of the electrical output.

Relative to a fixed-noise matched filter:

```text
larger variance broadens the H1 distribution
-> can increase overlap and hurt mean-based discrimination;
```

but simultaneously

```text
variance/covariance differs from H0
-> the shape change itself is evidence available to the optimum detector.
```

Therefore there is no architecture-independent rule

```text
more signal-dependent noise -> exactly this much worse detection.
```

The correct quantity is the overlap / likelihood ratio of the complete conditional output distributions.

---

## 12. New unifying statement

The previous Gaussian result suggested

```math
\text{detector quality for a task}
\leftrightarrow
\text{noise-weighted mean-waveform distance}.
```

The present extension is stronger:

> **The general detector boundary is set by the statistical distance between the complete photon-conditioned output processes, not merely by mean-waveform separation divided by a noise PSD.**

The equal-covariance Gaussian matched-filter distance is one important special case.

Poisson count discrimination is another.

A real photodetector can interpolate between or combine them.

---

## 13. Implication for conventional detector metrics

A conventional scalar such as NEP or `D*` is normally built from small-signal mean response and a noise spectrum measured about an operating state.

That can be sufficient when

```text
noise is approximately stationary,
noise covariance is effectively hypothesis independent,
the optical task is narrow enough,
and linear response applies.
```

It can become incomplete when

```text
noise changes materially with signal,
output statistics are non-Gaussian,
gain fluctuations matter,
rare dark events dominate,
or the decision is event based.
```

This does not invalidate NEP or `D*`; it identifies their scope.

---

## 14. Current frontier

The strongest next attack is now **unknown event time**.

So far the matched-filter derivations assume the signal waveform is aligned in time.

A real detector may need to decide whether an event occurred somewhere inside a search window.

That introduces

```text
unknown arrival time
matched-filter bank / temporal search
false-alarm trials penalty
timing jitter / stochastic detector latency
bandwidth versus localization tradeoff.
```

The key question is whether temporal uncertainty creates another unavoidable resource coordinate analogous to optical bandwidth and dark-event window.

After that, ask whether a task-specific scalar detectivity can be defined from the full likelihood geometry.
