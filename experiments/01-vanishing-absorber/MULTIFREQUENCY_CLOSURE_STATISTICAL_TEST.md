# Multi-Frequency Closure as a Statistical Falsification Test

**Date:** 2026-08-10  
**Status:** linearized Gaussian covariance result built on the exact real-coefficient closure theorem; not a substitute for measured covariance

## 1. Structural theorem to statistical test

At one depth, each RF frequency supplies an apparent real transport pair

```math
\hat\theta_j
=
\begin{pmatrix}
\hat D_j\\
\hat w_j
\end{pmatrix}.
```

The local Markov drift-diffusion null hypothesis is simply

```math
\boxed{
H_0:\quad
\theta_1=\theta_2=\cdots=\theta_N
=\theta
}
```

for one common

```math
\theta=(D,w)^T.
```

This is a particularly clean hypothesis because adding RF frequencies does **not** add local transport parameters under the null.

---

## 2. Stack the estimates

Define

```math
\hat g
=
(\hat D_1,\hat w_1,
 \hat D_2,\hat w_2,
 \ldots,
 \hat D_N,\hat w_N)^T
```

with full covariance

```math
C.
```

The design matrix for one common pair is

```math
X
=
\begin{pmatrix}
I_2\\
I_2\\
\vdots\\
I_2
\end{pmatrix}.
```

The generalized least-squares common coefficient is

```math
\boxed{
\hat\theta
=
(X^TC^{-1}X)^{-1}
X^TC^{-1}\hat g.
}
```

---

## 3. Closure statistic

Define

```math
\boxed{
Q
=
(\hat g-X\hat\theta)^T
C^{-1}
(\hat g-X\hat\theta).
}
```

Under

```text
correct local Markov model
known covariance
approximately Gaussian propagated coefficient errors
and regular nonsingular local inversion,
```

there are

```text
2N measured real coefficients
-
2 fitted common coefficients,
```

so

```math
\boxed{
Q\sim\chi^2_{2N-2}.
}
```

This converts the exact closure theorem into a conventional hypothesis test.

---

## 4. Minimal experiment

For

```math
N=2,
```

there are

```math
\boxed{2N-2=2}
```

closure degrees of freedom.

Thus two RF frequencies are the **mathematical minimum** required to make the one-frequency coefficient inference falsifiable.

This matches the conceptual statement:

```text
frequency 1 -> identify D,w
frequency 2 -> no new transport parameter -> test the law.
```

Three or more frequencies are not required structurally, but they improve rejection power and reveal the shape of any dispersion.

---

## 5. Reference thresholds

Using a two-sided-normal-style cumulative probability

```text
0.9973
```

as a convenient `~3 sigma` reference, the chi-square thresholds are approximately

```text
N=2 -> df=2 -> Q > 11.829
N=3 -> df=4 -> Q > 16.251
N=4 -> df=6 -> Q > 20.062.
```

These are only reference thresholds; an actual experiment should predefine its significance convention and account for any multiple testing across depth.

---

## 6. Power under a real closure violation

If the true mean coefficient vector does not lie in the common-coefficient subspace, then under the same Gaussian linearization

```math
Q
```

follows a noncentral chi-square distribution

```math
\boxed{
Q\sim\chi'^2_{2N-2}(\Lambda),
}
```

where the noncentrality

```math
\boxed{
\Lambda
=
\mu_\perp^T C^{-1}\mu_\perp
}
```

is the squared covariance-whitened size of the true closure violation after removing the best common `D,w`.

This is the correct generalized definition of **how detectable** a non-Markov dispersion is.

It automatically combines

```text
D dispersion
w dispersion
unequal uncertainties
cross-frequency correlations
D-w covariance.
```

---

## 7. Three-frequency reference power

For

```text
N=3
-> df=4
```

and the `0.9973` rejection threshold,

```math
\boxed{Q_{\rm crit}\simeq16.251.}
```

The noncentrality required for approximately `90%` rejection probability is

```math
\boxed{\Lambda\simeq24.756.}
```

or

```math
\boxed{\sqrt\Lambda\simeq4.98.}
```

Thus a closure failure should have roughly five units of **covariance-whitened distance from the Markov subspace** to be detected with high power at this stringent threshold.

---

## 8. Simple equal-noise example

Suppose three frequencies have independent equal `D` uncertainty

```math
\sigma_D
```

and `w` is perfectly constant.

Let

```math
D_1=D_0-\Delta,
\qquad
D_2=D_0,
\qquad
D_3=D_0+\Delta.
```

Then

```math
\boxed{
\Lambda
=2\left(\frac{\Delta}{\sigma_D}\right)^2.
}
```

For `90%` power at the above `~3 sigma` threshold,

```math
\boxed{
\frac{\Delta}{\sigma_D}
\simeq3.52.
}
```

The endpoint-to-endpoint coefficient change is `2 Delta`, so it would be about seven single-frequency standard deviations in this deliberately stringent example.

This illustrates why three frequencies are substantially more useful than saying merely that two fitted numbers look different.

---

## 9. From complex-response noise to coefficient covariance

The test should not assume arbitrary `sigma_D,sigma_w`.

They must be propagated from the measured complex response.

For the simple uniform two-depth experiment,

```math
\gamma
=\frac{
\ln F(z_2)-\ln F(z_1)
}{\Delta z}.
```

If each log-response component has independent standard deviation `sigma_y`, then one component of `gamma` has approximately

```math
\boxed{
\sigma_\gamma
=\frac{\sqrt2\,\sigma_y}{\Delta z}.
}
```

At low RF,

```math
\sigma_w
\sim
\frac{w^2}{\omega}
\sigma_{\Im\gamma},
```

```math
\sigma_D
\sim
\frac{w^3}{\omega^2}
\sigma_{\Re\gamma}.
```

Therefore the closure-test power is strongly frequency dependent even when the raw phase/log-magnitude precision is flat.

An exact experiment should propagate the full nonlinear Jacobian of

```math
(\Re\gamma,\Im\gamma)
\mapsto
(D,w)
```

or bootstrap directly in response space.

---

## 10. Multiple depth testing

The arbitrary-profile theorem supplies one local closure test at every resolvable depth.

That creates a multiple-testing issue.

A serious analysis should therefore distinguish

```text
preselected depth test
scan-wise false-discovery control
or a global integrated closure statistic.
```

An especially natural global statistic is the sum/integral of local whitened residual power after accounting for spatial covariance introduced by derivative estimation.

That extension remains open.

---

## 11. Falsification logic

The interpretation should remain asymmetric.

### If the test rejects

Then, within the calibrated measurement model,

> **one real frequency-independent local second-order Markov drift-diffusion generator is insufficient at that depth.**

That is a genuine falsification statement.

### If the test does not reject

Do **not** conclude that drift-diffusion is microscopically proven.

The experiment has only failed to resolve a departure large enough to exceed its covariance and model uncertainty.

Memory mechanisms can also reduce to nearly constant renormalized coefficients over a sufficiently narrow/low-frequency band.

---

## 12. Numerical regression

`numerics/multifrequency_closure_statistical_test.py`

verifies

```text
chi-square closure degrees of freedom = 2N-2
reference ~3-sigma thresholds
noncentral power calculation
and the equal-noise three-frequency closed form.
```

---

## 13. Theory status after this result

The project now has a complete chain:

```text
exact local Markov equation
-> exact real multi-frequency closure theorem
-> concrete non-Markov failure archetypes
-> differentiation-noise spatial resolution law
-> significance and power test.
```

The next high-value theoretical task is not another estimator.

It is to identify a **more surprising parameter-free prediction** of the spectral-depth realization itself—something that a graded photodetector must obey if wavelength truly acts as a passive internal spatial coordinate.
