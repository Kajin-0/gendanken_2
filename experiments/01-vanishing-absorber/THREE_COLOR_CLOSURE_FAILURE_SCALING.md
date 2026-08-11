# Three-Color Closure Failure Scaling — Separating Optical Shape Evolution from Transport Inhomogeneity

**Date:** 2026-08-10  
**Status:** asymptotically exact low-RF discriminator under explicitly stated smoothness assumptions; numerically checked; no novelty claim

## 1. Why a failed three-color law is not enough

The exact homogeneous/rigid-translation prediction is

```math
H_2^2=H_1H_3.
```

Define the complex logarithmic closure residual

```math
\boxed{
\mathcal L
=2\ln H_2-\ln H_1-\ln H_3.
}
\tag{1}
```

Perfect closure gives

```math
\mathcal L=0.
```

But a nonzero residual can come from at least two qualitatively different sources:

1. the optical generation kernel changes shape with wavelength;
2. the transport law varies with depth.

The next question is whether those two failure channels have different **RF scaling**.

They do.

---

## 2. Use mean generation depth as the spectral coordinate

For wavelength `j`, define

```math
\mu_j=E_j[z]
```

and centered coordinate

```math
U_j=z-\mu_j.
```

Suppose the transport segment is homogeneous with complex spatial propagation constant `Gamma(omega)`.

Then

```math
H_j
=e^{\Gamma\mu_j}
M_j(\Gamma),
```

where

```math
\boxed{
M_j(\Gamma)=E_j[e^{\Gamma U_j}]
}
```

is the centered moment-generating transform of the optical kernel.

Choose three wavelengths with equally spaced **mean** depths:

```math
\mu_2-\mu_1
=\mu_3-\mu_2
=h.
```

Then the pure mean-depth propagation term cancels exactly from Eq. (1):

```math
\boxed{
\mathcal L_{opt}
=2K_2(\Gamma)-K_1(\Gamma)-K_3(\Gamma),
}
\tag{2}
```

where

```math
K_j(\Gamma)=\ln M_j(\Gamma).
```

---

## 3. Centering removes the first-order optical error exactly

The cumulant expansion of the centered kernel is

```math
K_j(\Gamma)
=
\sum_{n=2}^{\infty}
\frac{\kappa_{n,j}}{n!}\Gamma^n.
```

There is no `n=1` term because

```math
E[U_j]=0.
```

Therefore

```math
\boxed{
\mathcal L_{opt}
=
\frac{\Gamma^2}{2}
\left(
2\sigma_2^2-\sigma_1^2-\sigma_3^2
\right)
+
\frac{\Gamma^3}{6}
\left(
2\kappa_{3,2}-\kappa_{3,1}-\kappa_{3,3}
\right)
+O(\Gamma^4).
}
\tag{3}
```

This is the central optical-robustness result:

> **When the spectral coordinate is the mean generation depth, wavelength-dependent kernel-shape evolution cannot contaminate three-color closure at first order in the spatial propagation constant.**

Finite width is not the issue.

Even changing width only enters through second and higher centered cumulants.

---

## 4. Low-RF optical signature

For ordinary downstream drift-diffusion in a uniform region,

```math
\Gamma(\omega)
=
\frac{i\omega}{w}
+
\frac{D\omega^2}{w^3}
+O(\omega^3).
```

Hence

```math
\Gamma^2
=-\frac{\omega^2}{w^2}
+O(i\omega^3).
```

Equation (3) therefore gives

```math
\boxed{
\Re\mathcal L_{opt}
=O(\omega^2),
}
```

while

```math
\boxed{
\Im\mathcal L_{opt}
=O(\omega^3)
}
```

for smooth kernel-shape evolution.

Thus the leading optical contamination is **quadratic in RF and log-magnitude-like**.

---

## 5. Spatially varying transport gives a different leading order

Now take point-like generation for clarity, but allow the local propagation exponent to vary with depth:

```math
\Gamma=\Gamma(z,\omega).
```

Define

```math
G(z,\omega)=\int^z\Gamma(u,\omega)du,
```

so

```math
\ln H(z,\omega)=G(z,\omega)+\mathrm{constant}.
```

For equally spaced coordinates `z-h,z,z+h`,

```math
\begin{aligned}
\mathcal L_{tr}
&=2G(z)-G(z-h)-G(z+h)\\
&=-h^2G''(z)-\frac{h^4}{12}G''''(z)+\cdots.
\end{aligned}
```

Since

```math
G''=\partial_z\Gamma,
```

```math
\boxed{
\mathcal L_{tr}
=-h^2\partial_z\Gamma
+O(h^4).
}
\tag{4}
```

At low RF,

```math
\Gamma(z,\omega)
=\frac{i\omega}{w(z)}+O(\omega^2),
```

so

```math
\boxed{
\mathcal L_{tr}
=
-i\omega h^2
\partial_z\left(\frac{1}{w}\right)
+O(\omega^2,h^4).
}
\tag{5}
```

Therefore

```math
\boxed{
\Im\mathcal L_{tr}=O(\omega),
}
```

with a leading phase-like signal.

---

## 6. Leading-order discriminator

The two common failure channels therefore have parametrically different signatures:

### Optical kernel-shape evolution

```math
\boxed{
\Re\mathcal L\sim\omega^2,
\qquad
\Im\mathcal L\sim\omega^3.
}
```

### Transport inhomogeneity

```math
\boxed{
\Im\mathcal L\sim\omega,
}
```

with real corrections beginning at higher order.

Conceptually:

```text
linear-in-RF phase curvature
-> transport inhomogeneity is the natural leading candidate

quadratic-in-RF magnitude curvature with little linear phase term
-> optical shape evolution is the natural leading candidate.
```

This is not unique microscopic mechanism identification, but it prevents the two most obvious closure failures from being automatically conflated.

---

## 7. Smooth spectral limit

If the centered optical cumulants vary smoothly with mean depth, then

```math
2\kappa_n(z)-\kappa_n(z-h)-\kappa_n(z+h)
=-h^2\kappa_n''(z)+O(h^4).
```

Equation (3) becomes

```math
\boxed{
\mathcal L_{opt}
=-h^2
\left[
\frac{\Gamma^2}{2}(\sigma^2)''
+
\frac{\Gamma^3}{6}\kappa_3''
+\cdots
\right]
+O(h^4).
}
\tag{6}
```

So both optical and transport curvature scale as `h^2` for small depth spacing, but they separate by RF order and complex quadrature.

---

## 8. Practical implication for a graded detector

The three-color experiment should not merely ask whether

```math
H_2^2=H_1H_3
```

within error.

It should measure the closure residual over several RF frequencies and fit the low-frequency expansion

```math
\boxed{
\mathcal L(\omega)
=c_1(i\omega)
+c_2\omega^2
+c_3(i\omega^3)
+\cdots.
}
```

The coefficients can then be compared with independent optical-kernel calculations.

A realistic analysis can proceed in this order:

1. calculate `p_lambda(z)` from the known optical profile;
2. choose wavelengths by equal **mean generation depth**;
3. predict the optical `O(omega^2)` closure residual from the kernel cumulants;
4. subtract/propagate that calibrated term;
5. test for an unexplained `O(omega)` phase residual indicating transport variation.

This makes the three-color law useful even when rigid translation is only approximate.

---

## 9. Relation to the local drift-diffusion closure

The three-color residual tests **spatial homogeneity / spectral-coordinate validity**.

The multi-frequency `D_app,w_app` test asks a different question:

> once a local propagation slope has been established, does its RF dispersion match one real Markov drift-diffusion generator?

Thus the intended hierarchy is

```text
three-color closure versus RF
-> separate optical shape evolution from spatial transport curvature

then

pairwise complex spatial slope versus RF
-> real D_app,w_app frequency closure

then

DC collection
-> physical drift/recombination unconditioning.
```

---

## 10. Numerical verification

`numerics/three_color_closure_failure_scaling.py`

checks two deliberately separate synthetic cases.

### Optical-only failure

Uniform transport with Gaussian generation kernels whose mean depths are equally spaced but whose variances have smooth depth curvature.

Numerically,

```text
Re(L)/omega^2 -> constant
Im(L)/omega^3 -> constant
```

over the low-RF stress interval.

### Transport-only failure

Point generation with smoothly depth-varying conditioned drift.

Numerically,

```text
Im(L)/omega -> constant
```

while the leading real correction scales as `omega^2`.

The expected asymptotic laws are recovered to the numerical tolerance.

---

## 11. Falsifiability

A measured low-frequency closure residual with

```text
large O(omega) phase curvature
```

cannot be explained by **centered optical kernel width/shape evolution alone** under the homogeneous propagation assumptions above.

Conversely, an `O(omega^2)` magnitude residual consistent with independently calculated generation-variance curvature should not be misidentified as anomalous carrier transport.

This is a sharper prediction than simply saying that optics must be modeled.

It specifies **which RF power and quadrature the leading optical error is allowed to occupy.**

---

## 12. Next worked-example calculation

The obvious next step is now quantitative rather than conceptual:

> **Use the actual Hansen/Moazzami graded-HgCdTe optical kernels to calculate the three-color mean-depth triplets and the expected optical `O(omega^2)` false-closure floor.**

Then compare that floor with the predicted `O(omega)` phase residual from plausible spatial transport gradients.

That will be the first direct material-level falsifiable prediction from the new theory ladder.
