# HgCdTe Spectral Timing Two-Moment Inverse — Mean Transport and Timing Broadening

**Date:** 2026-08-09  
**Status:** exact law-of-total-variance inverse under additive conditional timing cumulants; collection orientation and common-cumulant identifiability corrected; local drift-diffusion interpretation is conditional; no novelty claim

## 1. Purpose

The full complex timing response contains more information than the mean delay.

For a normalized timing transfer factor,

```math
\ln H_i(\Omega)
=-i\Omega\kappa_{1,i}
-\frac{\Omega^2}{2}\kappa_{2,i}
+O(\Omega^3).
```

Thus phase gives the first timing cumulant and magnitude curvature gives the second.

Question:

> After reconstructing the spatial mean-delay modes, can wavelength-dependent timing variance reconstruct a spatial broadening profile as well?

Under an additive conditional-cumulant model, yes — with the same collection-orientation and common-offset limitations as the first moment.

---

## 2. Orientation-dependent path model

Let

```math
q_1(s)
```

be local mean-delay density and

```math
q_2(s)\ge0
```

local conditional timing-variance density.

### Collection at `L`

For generation at `x`,

```math
m_L(x)=\int_x^Lq_1(s)ds,
```

```math
V_L(x)=\int_x^Lq_2(s)ds.
```

The timing kernel is the generation CDF

```math
K_{L,i}(s)=F_i(s)=P(X_g\le s).
```

### Collection at `0`

For generation at `x`,

```math
m_0(x)=\int_0^xq_1(s)ds,
```

```math
V_0(x)=\int_0^xq_2(s)ds.
```

The timing kernel is the survival function

```math
K_{0,i}(s)=S_i(s)=P(X_g\ge s).
```

Write the correct kernel for the chosen device simply as

```math
K_i(s).
```

---

## 3. First moment

The wavelength-dependent intrinsic mean is

```math
\mu_i=\mathbb E_i[m(X)].
```

For either one-boundary orientation,

```math
\boxed{
\mu_i
=\int_0^L K_i(s)q_1(s)ds.
}
```

Discretely,

```math
\boxed{
\boldsymbol\mu
=\mathbf A\mathbf q_1.
}
```

---

## 4. Total variance

The law of total variance gives

```math
\boxed{
\sigma_i^2
=\mathbb E_i[V(X)]
+\operatorname{Var}_i[m(X)].
}
```

The first term is conditional transport broadening; the second is broadening caused solely by the wavelength-dependent generation-position distribution.

Because the same path geometry applies to `V(x)`,

```math
\boxed{
\mathbb E_i[V(X)]
=\int_0^L K_i(s)q_2(s)ds.
}
```

Once `q_1` has been reconstructed to the available spatial resolution, `m(x)` is known and

```math
\operatorname{Var}_i[m(X)]
```

can be calculated from the optical generation kernel.

---

## 5. Second inverse

Define

```math
\boxed{
y_{2,i}
\equiv
\sigma_i^2
-\operatorname{Var}_i[m(X)].
}
```

Then

```math
\boxed{
y_{2,i}
=\int_0^L K_i(s)q_2(s)ds.
}
```

Discretely,

```math
\boxed{
\mathbf y_2
=\mathbf A\mathbf q_2.
}
```

The **same orientation-correct spatial matrix** appears in both moment inversions.

---

## 6. Common mean and broadening contributions are gauge-like

If a wavelength-independent instrument chain contributes cumulants `c_1` and `c_2`, one may write formally

```math
\boldsymbol\mu^{\rm meas}
=\mathbf A\mathbf q_1+c_1\mathbf1,
```

```math
\mathbf y_2^{\rm meas}
=\mathbf A\mathbf q_2+c_2\mathbf1.
```

However, appending constant nuisance columns does **not** guarantee unique separation from arbitrary boundary-localized `q_1` or `q_2`.

At the collecting boundary the timing kernel tends to unity for every wavelength. Therefore a sufficiently boundary-localized internal contribution is spectrally indistinguishable from a common instrumental cumulant.

So the robust objects are

```text
wavelength-dependent / differential q1 modes
+
wavelength-dependent / differential q2 modes.
```

Absolute common delay and absolute common broadening require external calibration, a gauge constraint, or a physical boundary prior.

Earlier synthetic recovery of fitted common constants was regularization-dependent and is **not** proof of structural identifiability.

---

## 7. Frequency-domain extraction

At low frequency,

```math
\boxed{
\mu_i
=-\left.
\frac{d}{d\Omega}\arg H_i(\Omega)
\right|_{0},
}
```

and

```math
\boxed{
\sigma_i^2
=-\left.
\frac{d^2}{d\Omega^2}\ln|H_i(\Omega)|
\right|_{0}.
}
```

Equivalently,

```math
\arg H_i\approx-\Omega\mu_i,
```

```math
\ln|H_i|
\approx-\frac{\Omega^2}{2}\sigma_i^2.
```

Using several RF frequencies is preferable to estimating either cumulant from a single point.

Differential phase removes the common first cumulant. Differential log-magnitude curvature removes a wavelength-independent second cumulant.

---

## 8. Conditional drift-diffusion interpretation

For a local constant-coefficient advection-diffusion segment,

```math
\mathbb E[dT]=\frac{dx}{v},
```

```math
\operatorname{Var}(dT)=\frac{2D}{v^3}dx.
```

Thus in the local additive high-Peclet approximation,

```math
\boxed{q_1(x)=1/v(x),}
```

```math
\boxed{q_2(x)\simeq2D(x)/v^3(x).}
```

If both are known on an identifiable differential/gauge-fixed basis,

```math
\boxed{
D(x)\simeq\frac{q_2(x)}{2q_1^3(x)}.
}
```

This is **not** a general theorem for strongly nonlocal or strongly position-dependent HgCdTe transport. A full drift-diffusion or Monte Carlo model must validate the local interpretation.

---

## 9. What the second moment adds

Mean timing alone cannot distinguish

```text
slow but narrow timing
```

from

```text
slow and strongly broadened timing.
```

The second moment can separate a spatial mean-delay anomaly from a spatial timing-broadening anomaly, provided the optical generation broadening is first accounted for.

This is why the two-moment method is potentially more useful than a single wavelength-dependent bandwidth curve.

---

## 10. Existing synthetic result

The deterministic regression

`numerics/hgcdte_spectral_timing_two_moment_inverse.py`

uses separate synthetic slow-transport and high-broadening regions.

It shows that, in a controlled normalized problem, the two profiles can be numerically separated.

Its common-offset recovery should now be interpreted only as one **regularized gauge choice**, not an independently verified absolute calibration.

A future regression should use the published sample-B matrix and differential phase/magnitude observables.

---

## 11. Claim boundary

### DERIVED under additive conditional cumulants

```math
\boxed{
\mu_i=\int K_iq_1,
}
```

```math
\boxed{
\sigma_i^2
=\int K_iq_2
+\operatorname{Var}_{p_i}[m(X)].
}
```

with `K_i=F_i` or `S_i` according to the collection boundary.

### DERIVED IDENTIFIABILITY LIMIT

Wavelength-independent first- and second-cumulant contributions are not generically separable from arbitrary boundary-localized internal transport without extra information.

### CONDITIONAL

```math
q_1=1/v,
\qquad
q_2\simeq2D/v^3.
```

### NOT ESTABLISHED

- real sample-B `q_2(z)`;
- experimental second-cumulant precision;
- local diffusion recovery in nonlocal HgCdTe transport;
- novelty / priority.

---

## 12. Next decisive work

Do not add another formal moment.

The high-value next experiment/model is a **multi-frequency complex-response inversion** on the published-sample-B optical matrix:

```text
phase slope -> differential q1 modes
magnitude curvature -> differential q2 modes
```

with realistic wavelength-dependent SNR and covariance.

Only after that should the project claim any practical ability to separate internal mean transport from timing broadening.
