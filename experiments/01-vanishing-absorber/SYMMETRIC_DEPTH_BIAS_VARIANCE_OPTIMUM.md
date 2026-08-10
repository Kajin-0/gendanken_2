# Symmetric Depth Bias–Variance Optimum — A Cube-Root Resolution Law

**Date:** 2026-08-10  
**Status:** **DERIVED / CHECKED** for local complex spatial-slope estimation from two symmetric noisy depth coordinates; no novelty/priority claim

## 1. The simplest resolution question

Suppose the transport information is contained in the local complex spatial slope

```math
\gamma(z)=\frac{d}{dz}\ln H(z).
```

The exact local inverse can use continuously differentiated data, but real measurements are noisy.

The simplest gedanken estimator probes two generation coordinates symmetrically around a target depth `z_0`:

```text
z_- = z_0 - Delta z/2
z_+ = z_0 + Delta z/2.
```

Estimate

```math
\boxed{
\widehat\gamma(z_0)
=
\frac{
\ln H(z_+)-\ln H(z_-)
}{\Delta z}.
}
\tag{1}
```

This estimator has an unavoidable tradeoff:

```text
small Delta z -> local but noise amplified
large Delta z -> precise but spatially averaged/curvature biased.
```

The optimum can be derived exactly to leading order.

---

# 2. Central-difference bias

Let

```math
f(z)=\ln H(z),
\qquad
f'(z)=\gamma(z).
```

Taylor expand about `z_0`:

```math
f(z_0\pm h)
=f_0
\pm h f_0'
+\frac{h^2}{2}f_0''
\pm\frac{h^3}{6}f_0'''
+O(h^4),
```

with

```math
h=\Delta z/2.
```

Subtract and divide by `2h`:

```math
\widehat\gamma_{\rm noiseless}
=
\gamma(z_0)
+\frac{h^2}{6}f'''(z_0)
+O(h^4).
```

Since

```math
f'''=\gamma'',
```

```math
\boxed{
\operatorname{bias}\widehat\gamma
=
\frac{\Delta z^2}{24}\gamma''(z_0)
+O(\Delta z^4).
}
\tag{2}
```

Symmetric sampling removes the entire first-order spatial-gradient bias.

The leading bias is quadratic in separation and controlled by the **curvature of the local complex propagation field**, not merely by `gamma'`.

---

# 3. Complex measurement noise

Write

```math
\ln H
=\ln|H|+i\phi.
```

Let one endpoint measurement have independent errors

```math
\operatorname{Var}(\delta\ln|H|)=\sigma_A^2,
```

```math
\operatorname{Var}(\delta\phi)=\sigma_\phi^2.
```

Define the per-endpoint complex mean-square noise

```math
\boxed{
s^2
=\sigma_A^2+\sigma_\phi^2.
}
\tag{3}
```

For independent endpoint measurements, the difference has complex mean-square noise `2s^2`.

Therefore

```math
\boxed{
\mathbb E
\left|
\widehat\gamma-\mathbb E\widehat\gamma
\right|^2
=
\frac{2s^2}{\Delta z^2}.
}
\tag{4}
```

---

# 4. Leading mean-square error

Combine (2) and (4):

```math
\boxed{
\operatorname{MSE}(\Delta z)
\simeq
\frac{2s^2}{\Delta z^2}
+
\frac{|\gamma''(z_0)|^2}{576}
\Delta z^4.
}
\tag{5}
```

The first term decreases with separation.

The second grows with separation.

Hence the optimum is finite.

---

# 5. Universal cube-root optimum

Differentiate (5):

```math
-\frac{4s^2}{\Delta z^3}
+
\frac{|\gamma''|^2}{144}\Delta z^3
=0.
```

Thus

```math
\Delta z^6
=
\frac{576s^2}{|\gamma''|^2}.
```

Therefore

```math
\boxed{
\Delta z_{\rm opt}
=
\left(
\frac{24s}{|\gamma''(z_0)|}
\right)^{1/3}.
}
\tag{6}
```

This is a simple resolution law:

```text
more noise -> use a wider spatial/spectral baseline
more transport curvature -> use a narrower baseline.
```

The scaling is only a cube root, so the optimal spacing is relatively insensitive to moderate errors in either noise or curvature estimates.

---

# 6. Error partition at the optimum

Using Eq. (6),

```math
\frac{|\gamma''|^2\Delta z_{\rm opt}^6}{576}=s^2.
```

Therefore the squared bias is

```math
\operatorname{bias}^2
=
\frac{s^2}{\Delta z_{\rm opt}^2},
```

while the statistical complex variance is

```math
\operatorname{Var}
=
\frac{2s^2}{\Delta z_{\rm opt}^2}.
```

Hence

```math
\boxed{
\operatorname{Var}
=2\,|\operatorname{bias}|^2
}
\tag{7}
```

at the optimum.

The minimum RMS complex-slope error is

```math
\boxed{
\sigma_{\gamma,\rm opt}
=\sqrt{3}\,
\frac{s}{\Delta z_{\rm opt}}.
}
\tag{8}
```

Equivalently,

```math
\boxed{
\sigma_{\gamma,\rm opt}
=
\frac{\sqrt3}{24^{1/3}}
s^{2/3}|\gamma''|^{1/3}.
}
\tag{9}
```

So the best achievable local slope precision in this two-point estimator scales as

```math
\boxed{
s^{2/3}|\gamma''|^{1/3}.}
```

---

# 7. Correlated/common-mode noise

The independent-endpoint assumption is not essential.

Let

```math
N_\Delta
\equiv
\mathbb E
|\delta f_+-\delta f_-|^2
```

be the actual complex noise variance of the difference.

Then

```math
\operatorname{MSE}
=
\frac{N_\Delta}{\Delta z^2}
+
\frac{|\gamma''|^2\Delta z^4}{576}.
```

The optimum becomes

```math
\boxed{
\Delta z_{\rm opt}
=
\left(
\frac{288N_\Delta}{|\gamma''|^2}
\right)^{1/6}.
}
\tag{10}
```

For independent endpoints,

```math
N_\Delta=2s^2,
```

and Eq. (10) reduces to Eq. (6).

This form naturally incorporates common-mode rejection and covariance.

---

# 8. Spectral form

If wavelength maps to generation depth `z_g(lambda)`, choose the two wavelengths so that their **generation coordinates**, not necessarily their wavelengths, are symmetric:

```math
z_g(\lambda_-)
=z_0-\Delta z/2,
```

```math
z_g(\lambda_+)
=z_0+\Delta z/2.
```

For a locally linear map,

```math
\Delta z
\simeq
\left|\frac{dz_g}{d\lambda}\right|
\Delta\lambda.
```

Therefore

```math
\boxed{
\Delta\lambda_{\rm opt}
\simeq
\frac{1}{|dz_g/d\lambda|}
\left(
\frac{24s}{|\gamma''|}
\right)^{1/3}.
}
\tag{11}
```

If `z_g(lambda)` is nonlinear, the correct procedure is to choose wavelengths that are symmetric in **depth**, avoiding a separate coordinate-curvature bias.

---

# 9. Connection to exact versus WKB inversion

This result clarifies the hierarchy of estimators.

### Exact local inverse

Uses

```text
c, c', r, r'
```

and is structurally exact in the 1-D local model.

But estimating derivatives such as `r'` requires still finer spatial differentiation and therefore stronger noise amplification.

### Symmetric local-uniform estimator

Uses two separated response measurements to estimate the local complex slope.

It is lower derivative order and has the explicit curvature bias (2).

### WKB/local closure

Then interprets that slope with local algebraic transport formulas, adding a separately calculable model-gradient bias.

Thus there are now two distinct bias sources:

```text
finite-difference curvature bias
and
local-uniform/WKB physical-model bias.
```

They should not be conflated.

---

# 10. A deeper resolution principle

Equation (6) is not an optical diffraction limit.

It is an **information-versus-locality limit** created by estimating a spatial derivative from noisy data.

Even with a perfect wavelength-to-depth encoder,

```text
arbitrarily small spectral/depth spacing
```

is not optimal because the response difference vanishes into measurement noise.

Likewise,

```text
arbitrarily large spacing
```

is not optimal because the result ceases to be local.

The optimal spatial scale is set by the competition

```math
\text{noise}/\Delta z
\quad\leftrightarrow\quad
\text{curvature}\times\Delta z^2.
```

That is a general consequence of local transport tomography, independent of HgCdTe.

---

# 11. Falsifiable predictions

### P1 — cube-root noise scaling

If measurement noise is deliberately changed while the underlying transport field remains fixed,

```math
\boxed{
\Delta z_{\rm opt}\propto s^{1/3}.
}
```

### P2 — cube-root curvature scaling

Across regions with different complex transport curvature,

```math
\boxed{
\Delta z_{\rm opt}\propto|\gamma''|^{-1/3}.
}
```

### P3 — error partition

At the predicted optimum, statistical variance should be twice the squared leading curvature bias.

### P4 — symmetric sampling advantage

Moving from a one-sided difference to a symmetric difference removes the first-order spatial-gradient bias and changes the fundamental optimal-spacing scaling.

### P5 — no universal best wavelength spacing

The best spectral separation must vary with local transport curvature, optical depth mapping, and actual covariance. A single globally optimal wavelength spacing is not predicted.

---

# 12. Numerical regression

`numerics/symmetric_depth_bias_variance_optimum.py`

uses a cubic complex log-transfer for which the leading central-difference bias is exact.

The closed-form optimum agrees with dense numerical minimization, and at that optimum

```text
statistical variance / squared bias = 2
```

to numerical precision.

---

# 13. Next theoretical extension

The exact local inverse requires **second spatial derivatives** of the log response through `c'` and `r'`.

The next derivation should compare:

```text
first-derivative two-point estimator
versus
second-derivative exact inverse
```

under noise.

The central question is whether there is a principled hybrid estimator that uses multiple RF frequencies to reduce derivative order while retaining exact arbitrary-profile identifiability.

That is now a sharper theoretical question than further device optimization.
