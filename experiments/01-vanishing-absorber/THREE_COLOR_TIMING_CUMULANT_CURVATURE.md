# Three-Color Timing-Cumulant Curvature Theorem

**Date:** 2026-08-10  
**Status:** exact consequence of characteristic-function cumulants; no drift-diffusion assumption; detector spatial interpretation requires a calibrated internal coordinate; no novelty claim

## 1. A model-independent meaning of the three-color residual

Take three de-embedded, DC-normalized detector responses

```math
H_j(\omega),\qquad j=1,2,3,
```

that are each compatible with positive classical transit-time distributions.

Near `omega=0`, choose the analytic logarithm branch and define

```math
\boxed{
\mathcal L(\omega)
=2\ln H_2(\omega)
-\ln H_1(\omega)
-\ln H_3(\omega).
}
\tag{1}
```

No transport equation is needed to interpret this quantity.

---

## 2. Exact cumulant expansion

For channel `j`, let

```math
\kappa_{n,j}
```

be the `n`th cumulant of its successful-carrier transit-time distribution.

Because

```math
H_j(\omega)
=E[e^{-i\omega T_j}],
```

its cumulant expansion is

```math
\ln H_j(\omega)
=
\sum_{n=1}^{\infty}
\frac{(-i\omega)^n}{n!}
\kappa_{n,j}.
```

Therefore Eq. (1) gives exactly

```math
\boxed{
\mathcal L(\omega)
=
\sum_{n=1}^{\infty}
\frac{(-i\omega)^n}{n!}
C_n,
}
\tag{2}
```

where

```math
\boxed{
C_n
=2\kappa_{n,2}
-\kappa_{n,1}
-\kappa_{n,3}.
}
\tag{3}
```

Thus the complex three-color closure is a generating function for **discrete curvature of timing cumulants**.

---

## 3. First three RF orders

Equation (2) begins

```math
\boxed{
\mathcal L
=
-i\omega C_1
-
\frac{\omega^2}{2}C_2
+
\frac{i\omega^3}{6}C_3
+
\frac{\omega^4}{24}C_4
+\cdots.
}
\tag{4}
```

Therefore:

### Linear phase term

```math
\boxed{
\lim_{\omega\to0}
\frac{\Im\mathcal L}{\omega}
=-C_1
}
```

with

```math
C_1
=2E[T_2]-E[T_1]-E[T_3].
```

The low-RF phase closure is exactly the discrete curvature of **mean transit time**.

### Quadratic log-magnitude term

```math
\boxed{
\lim_{\omega\to0}
\frac{\Re\mathcal L}{\omega^2}
=-\frac12C_2
}
```

with

```math
C_2
=2\operatorname{Var}(T_2)
-\operatorname{Var}(T_1)
-\operatorname{Var}(T_3).
```

The leading magnitude closure is the discrete curvature of **timing variance**.

### Cubic phase term

After removing the linear term,

```math
\boxed{
\Im\mathcal L
+
\omega C_1
=
\frac{\omega^3}{6}C_3
+O(\omega^5).
}
```

Thus the next phase term measures discrete curvature of the **third timing cumulant / skewness numerator**.

Higher RF orders continue the hierarchy.

---

## 4. Spatial interpretation with equally spaced internal coordinates

Suppose the three optical channels correspond to equally spaced calibrated internal coordinates

```math
z_1=z_0-h,
\qquad
z_2=z_0,
\qquad
z_3=z_0+h.
```

Let the `n`th timing cumulant vary smoothly with internal coordinate:

```math
\kappa_n=\kappa_n(z).
```

Then the centered second difference is

```math
\begin{aligned}
C_n
&=2\kappa_n(z_0)
-\kappa_n(z_0-h)
-\kappa_n(z_0+h)\\
&=-h^2\kappa_n''(z_0)
-\frac{h^4}{12}\kappa_n''''(z_0)
+O(h^6).
\end{aligned}
```

Hence

```math
\boxed{
\mathcal L(\omega)
\simeq
\sum_{n=1}^{\infty}
\frac{(-i\omega)^n}{n!}
\left[-h^2\kappa_n''(z_0)+O(h^4)\right].
}
\tag{5}
```

So successive RF powers measure the **spatial curvature of successive timing cumulants**.

---

## 5. Physical meaning

This gives the three-color experiment a model-independent interpretation before any drift-diffusion fit.

### `O(omega)` phase

Answers:

> **Is the mean successful-carrier transit time locally linear in the internal coordinate?**

If not, the sign and magnitude of the phase closure measure its curvature.

### `O(omega^2)` magnitude

Answers:

> **Where does the width of the transit-time distribution curve spatially?**

### `O(omega^3)` phase

Answers:

> **Where does asymmetric / non-Gaussian timing begin to develop?**

The hierarchy continues to higher cumulants.

This is a stronger interpretation than treating RF amplitude and phase merely as arbitrary spectral features.

---

## 6. Relation to the spatial-semigroup null

For one scalar homogeneous spatial first-passage semigroup with a rigidly translated generation kernel,

```math
H(z,\omega)=B(\omega)e^{\Gamma(\omega)z}.
```

Then

```math
\ln H
```

is exactly linear in `z` at **every RF frequency**.

Equivalently, every timing cumulant is affine in `z`:

```math
\boxed{
\kappa_n(z)
=a_n+b_nz.
}
```

Therefore

```math
\boxed{C_n=0}
```

for every cumulant and

```math
\boxed{\mathcal L(\omega)=0}
```

identically.

The geometric-mean law is therefore equivalent to the simultaneous vanishing of the discrete spatial curvature of **all timing cumulants**.

---

## 7. Why low RF is especially interpretable

At sufficiently low RF the hierarchy separates by powers of `omega`:

```text
phase / omega
-> mean-delay curvature

log-magnitude / omega^2
-> timing-variance curvature

residual phase / omega^3
-> timing-skewness curvature
```

This means a frequency sweep can test progressively richer timing statistics without first choosing a microscopic transport model.

A drift-diffusion, trapping, or nonlocal model is only introduced afterward to explain the observed cumulant-curvature pattern.

---

## 8. Connection to the HgCdTe prediction

The existing HgCdTe worked example found, for three colors selected by mean generation depths `2,4,6 um`, approximately

```text
100 MHz -> phase closure ~ -0.123 deg
500 MHz -> ~ -0.583 deg
1 GHz -> ~ -0.985 deg
```

under a modest spatially varying local transport model.

At low RF this should now be interpreted first as a prediction for **mean-transit-time curvature**, not merely as a fitted drift-gradient signature.

The model-specific step is then to ask whether the predicted mean-time curvature follows from the quasi-neutral HgCdTe drift law.

This separation improves falsifiability:

```text
measurement -> timing-cumulant curvature
then
transport model -> explanation of that curvature.
```

---

## 9. Distinction from optical shape evolution

If the internal coordinate is chosen as **mean generation depth**, homogeneous propagation plus centered optical kernel shape evolution has no first-order propagation term in the centered kernel transform.

Therefore smooth optical shape evolution contributes to closure only at higher order in the spatial propagation constant, giving the previously derived low-RF hierarchy

```text
optical-shape log-magnitude closure ~ O(omega^2)
optical-shape phase closure ~ O(omega^3)
```

while a genuine curvature of mean transit time gives an `O(omega)` phase term.

Thus the timing-cumulant theorem and the optical-correction theorem are mutually consistent.

---

## 10. A direct experimental estimator

For sufficiently low RF, define

```math
\boxed{
\widehat C_1
=-\frac{\Im\mathcal L(\omega)}{\omega}.
}
```

With several low frequencies, fit the phase closure to

```math
\Im\mathcal L
=-C_1\omega
+\frac{C_3}{6}\omega^3
+\cdots.
```

Likewise fit the real closure to

```math
\Re\mathcal L
=-\frac{C_2}{2}\omega^2
+\frac{C_4}{24}\omega^4
+\cdots.
```

This returns timing-cumulant curvature directly from response data without solving a transport inverse problem.

---

## 11. What failure means

A nonzero `C_1` does **not** uniquely prove a spatial drift gradient.

It proves that the three channels have non-affine mean successful-carrier transit times in the chosen internal coordinate after all calibrated optical/electrical corrections.

Possible explanations include

```text
spatial transport inhomogeneity,
boundary influence,
hidden carrier populations,
generation-kernel shape effects if the coordinate/correction is inadequate,
frequency-dependent measurement contamination,
or another violation of the spatial-semigroup assumptions.
```

The subsequent closure hierarchy discriminates among these possibilities.

---

## 12. Prior-art boundary

Cumulant expansions of characteristic functions are classical mathematics.

Wavelength-dependent photodiode RF phase/amplitude and absorption-depth-dependent carrier dynamics are also established.

Therefore the mathematical series itself is not a novelty claim.

The candidate detector contribution is narrower:

> **Use three spectrally selected, equally spaced internal generation coordinates so the complex RF closure directly measures discrete spatial curvature of the full transit-time cumulant hierarchy, then apply nested semigroup and transport-law null tests.**

A focused prior-art audit is still required before priority language.

---

## 13. Numerical verification

`numerics/three_color_timing_cumulant_curvature.py`

uses three arbitrary discrete timing distributions and verifies the first four cumulant coefficients of Eq. (2).

It also verifies the centered spatial second-difference expansion for smooth synthetic cumulant fields.

---

## 14. Why this may be a central paper result

The simplest version can be stated without transport jargon:

> **Three colors sample three internal depths. The linear RF phase curvature measures curvature of the mean carrier transit time; the quadratic magnitude curvature measures curvature of timing variance; higher RF orders measure curvature of higher timing cumulants.**

That is simple, rigorous, falsifiable, and does not require a large numerical inversion.

The drift-diffusion closure theorem then becomes a second-stage explanation/test rather than the opening assumption.
