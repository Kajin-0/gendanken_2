# Pure RF-Domain Nulls for Uniform Drift-Diffusion Timing

**Date:** 2026-08-10  
**Status:** exact low-frequency derivative form of the inverse-Gaussian first-passage cumulant identities; no time-domain histogram required; no novelty claim for inverse-Gaussian mathematics

## 1. Why rewrite the timing-cumulant theorem in RF language?

The previous result gave parameter-free transit-time relations for ideal uniform drift-diffusion:

```math
\frac{\kappa_3\kappa_1}{\kappa_2^2}=3,
```

```math
\frac{\kappa_4\kappa_2}{\kappa_3^2}=\frac53.
```

A detector experiment does not necessarily measure individual carrier arrival times.

It may instead measure a complex small-signal transfer

```math
H(\omega).
```

The same nulls are encoded directly in low-frequency derivatives of that complex response.

---

## 2. Complex log response

Write

```math
\boxed{
\ln H(\omega)
=m(\omega)+i\phi(\omega),
}
```

where

```text
m(omega)=ln|H(omega)|
phi(omega)=unwrapped phase.
```

For a positive transit-time distribution,

```math
\ln H(\omega)
=
\sum_{n=1}^{\infty}
\frac{(-i\omega)^n}{n!}\kappa_n.
```

Therefore

```math
\phi(\omega)
=-\kappa_1\omega
+\frac{\kappa_3}{6}\omega^3
-\frac{\kappa_5}{120}\omega^5
+\cdots,
```

and

```math
m(\omega)
=-\frac{\kappa_2}{2}\omega^2
+\frac{\kappa_4}{24}\omega^4
-\frac{\kappa_6}{720}\omega^6
+\cdots.
```

Hence exactly at zero frequency,

```math
\boxed{
\phi'(0)=-\kappa_1,
}
\tag{1}
```

```math
\boxed{
m''(0)=-\kappa_2,
}
\tag{2}
```

```math
\boxed{
\phi'''(0)=\kappa_3,
}
\tag{3}
```

```math
\boxed{
m''''(0)=\kappa_4.
}
\tag{4}
```

---

## 3. First parameter-free RF null

Uniform drift-diffusion predicts

```math
\kappa_3\kappa_1=3\kappa_2^2.
```

Using Eqs. (1)-(3),

```math
\boxed{
-\phi'(0)\phi'''(0)
=3[m''(0)]^2.
}
\tag{5}
```

Equivalently,

```math
\boxed{
\frac{-\phi'(0)\phi'''(0)}{[m''(0)]^2}=3.
}
\tag{6}
```

No drift velocity, diffusion coefficient, propagation distance, mobility, or recombination lifetime appears.

---

## 4. Second parameter-free RF null

The next inverse-Gaussian identity is

```math
\kappa_4\kappa_2
=\frac53\kappa_3^2.
```

Therefore

```math
\boxed{
-m''(0)m''''(0)
=\frac53[\phi'''(0)]^2.
}
\tag{7}
```

or

```math
\boxed{
\frac{-m''(0)m''''(0)}{[\phi'''(0)]^2}
=\frac53.
}
\tag{8}
```

Again, the result is parameter free.

---

## 5. Péclet number directly from RF curvature

The coefficient of variation satisfies

```math
CV^2
=\frac{\kappa_2}{\kappa_1^2}.
```

Using the RF derivatives,

```math
\boxed{
CV^2
=
\frac{-m''(0)}{[\phi'(0)]^2}.
}
\tag{9}
```

For uniform drift-diffusion,

```math
CV^2=\frac{2}{Pe},
\qquad
Pe=\frac{wd}{D}.
```

Thus

```math
\boxed{
Pe
=
-\frac{2[\phi'(0)]^2}{m''(0)}.
}
\tag{10}
```

A dimensionless transport number is therefore available from the local phase slope and log-magnitude curvature alone.

---

## 6. Recovering `w` and `D` if the distance is known

If the generation-to-collector propagation distance `d` is independently calibrated,

```math
\kappa_1=d/w.
```

So

```math
\boxed{
w
=\frac{d}{-\phi'(0)}.
}
\tag{11}
```

From

```math
\kappa_2=\frac{2Dd}{w^3},
```

```math
\boxed{
D
=
\frac{[-m''(0)]d^2}
{2[-\phi'(0)]^3}.
}
\tag{12}
```

These parameter estimates are secondary.

The stronger theory test is that the higher derivatives must then satisfy Eqs. (5) and (7) **without additional fitted parameters**.

---

## 7. Uniform recombination robustness

For uniform Markov recombination/killing, DC normalization changes the physical drift `v` into conditioned drift

```math
w=\sqrt{v^2+4D\kappa}.
```

But the successful-carrier timing distribution remains inverse Gaussian in the ideal homogeneous geometry.

Therefore Eqs. (5)-(10) survive exactly.

This is useful because it means a failure of the parameter-free derivative nulls cannot be repaired merely by adding one uniform lifetime parameter.

---

## 8. Experimental interpretation

A low-frequency complex-response measurement can be fitted locally as

```math
\phi(\omega)
=a_1\omega+a_3\omega^3+a_5\omega^5+\cdots,
```

```math
m(\omega)
=b_2\omega^2+b_4\omega^4+b_6\omega^6+\cdots.
```

Then

```math
\phi'(0)=a_1,
```

```math
\phi'''(0)=6a_3,
```

```math
m''(0)=2b_2,
```

```math
m''''(0)=24b_4.
```

Uniform drift-diffusion predicts

```math
\boxed{
-6a_1a_3=12b_2^2,
}
```

or

```math
\boxed{-a_1a_3=2b_2^2,}
```

and

```math
\boxed{
-(2b_2)(24b_4)
=\frac53(6a_3)^2.
}
```

These forms may be convenient when fitting RF data directly.

---

## 9. Why the first null is much easier than the second

Equation (5) requires estimating

```text
linear phase
quadratic log magnitude
cubic phase.
```

Equation (7) additionally requires a fourth-order magnitude term.

Higher derivatives are progressively more noise sensitive and require a broader valid low-frequency band.

Therefore the practical hierarchy should be

```text
first test Eq. (5)
then, only with sufficient SNR/bandwidth, test Eq. (7)
and higher cumulant ratios.
```

This mirrors the project's general principle of testing the smallest overdetermined prediction first.

---

## 10. Relation to the two-frequency spatial closure

The RF-derivative null and the two-depth/two-frequency coefficient closure are complementary.

### Cumulant derivative test

Uses the **frequency shape at one propagation distance**.

It asks whether the transit-time distribution has the inverse-Gaussian shape required by uniform drift-diffusion.

### Spatial propagation closure

Uses **multiple generation depths**.

It asks whether one common real `D,w` explains spatial propagation across RF frequency.

A strong theory test would apply both.

They fail for different reasons and therefore provide cross-validation.

---

## 11. Falsification logic

If Eq. (5) fails beyond covariance/model uncertainty, then the ideal uniform one-dimensional drift-diffusion first-passage model is falsified for that timing response.

Possible causes include

```text
spatially varying drift or diffusion,
finite boundaries,
trapping / temporal memory,
multiple transport populations,
nonlocal transport,
frequency-dependent electronics not fully removed,
or failure of the positive first-passage timing interpretation itself.
```

The broader falsification ladder is then used to localize the failure.

---

## 12. Prior-art boundary

The inverse-Gaussian first-passage distribution and its moments/cumulants are classical results.

Photodetector frequency-response and carrier-transit-time theory are also established.

The current literature search has **not** established priority for using the parameter-free derivative identities Eqs. (5) and (7) as photocarrier drift-diffusion null tests.

Do not interpret that negative search as novelty evidence.

---

## 13. Numerical regression

`numerics/rf_derivative_drift_diffusion_nulls.py`

checks the exact derivative ratios over multiple arbitrary values of

```text
D
w
d
```

and verifies direct RF extraction of the transit Péclet number.

---

## 14. Conceptual one-line prediction

The first null can be stated compactly:

> **For ideal uniform drift-diffusion, the cubic curvature of RF phase is not free; once the linear phase delay and quadratic magnitude roll-off are known, it is fixed exactly.**

That is a strong frequency-domain prediction with no material parameter fitting.
