# HgCdTe Spectral Timing Tomography Resolution — Optical, Spectral, and Timing Limits

**Date:** 2026-08-09  
**Status:** analytic experimental-resolution budget for the candidate spectral timing inverse method; order-of-magnitude design relations, not a calibrated detector prediction; no novelty claim

## 1. Purpose

The spectral timing inverse now has a concrete forward model:

```math
\mathbf T
=\mathbf A\mathbf q+c\mathbf1,
\qquad
q(x)=1/v_{\rm eff}(x).
```

A synthetic example shows that a nonuniform profile can be reconstructed in a controlled case.

The next question is experimental:

> **What sets the spatial resolution of this spectral transport tomography?**

There are several independent resolution scales. They should not be collapsed into one vague timing-bandwidth requirement.

---

## 2. Optical generation width

For the analytic edge law

```math
\alpha=C(E_\gamma-E_g)^\beta
```

inside a linear gap gradient `G`, the downstream generation offset from the first allowed position has Weibull scale

```math
\boxed{
\ell_\alpha
=\left[
\frac{\beta+1}
{CG^\beta}
\right]^{1/(\beta+1)}.
}
```

Let

```math
n=\beta+1.
```

Then

```math
\boxed{
\langle z\rangle
=\ell_\alpha
\Gamma\!\left(1+\frac1n\right),
}
```

and

```math
\boxed{
\sigma_{z,\rm opt}
=\ell_\alpha
\sqrt{
\Gamma\!\left(1+\frac2n\right)
-\Gamma^2\!\left(1+\frac1n\right)
}.
}
```

This is a true optical point-spread scale.

Transport features much narrower than `sigma_z,opt` will be strongly smoothed unless the inverse problem has enough signal-to-noise for deconvolution.

---

## 3. Source spectral width maps into spatial width

For a general monotonic gap profile,

```math
E_g[x_g(E_\gamma)]=E_\gamma.
```

Therefore a photon-energy uncertainty `sigma_E` maps to

```math
\boxed{
\sigma_{x,E}
=\frac{\sigma_E}
{|E_g'(x_g)|}.
}
```

For a linear gap with `|E_g'|=G`,

```math
\boxed{
\sigma_{x,E}=\frac{\sigma_E}{G}.
}
```

Since

```math
E_\gamma=hc/\lambda,
```

small wavelength uncertainty gives

```math
\boxed{
\sigma_E
\simeq
\frac{hc}{\lambda^2}\sigma_\lambda,
}
```

hence

```math
\boxed{
\sigma_{x,\lambda}
\simeq
\frac{hc}
{G\lambda^2}
\sigma_\lambda.
}
```

Thus source linewidth / wavelength calibration is an independently calculable spatial blur.

---

## 4. Gap-profile uncertainty also maps directly into position uncertainty

The internal spectral coordinate works only if `E_g(x)` is known.

For a local gap-energy uncertainty `sigma_Eg`, the corresponding first-order position uncertainty is

```math
\boxed{
\sigma_{x,g}
\simeq
\frac{\sigma_{E_g}}
{|E_g'(x)|}.
}
```

For a linear fit with uncertain gradient `G`, there is an additional position-dependent calibration error of order

```math
\boxed{
\sigma_{x,G}
\sim
x\frac{\sigma_G}{G}.
}
```

Therefore composition/profile metrology is part of the transport measurement, not an optional device-description detail.

---

## 5. Timing precision maps into spatial discrimination

In the sharp local-transport limit,

```math
T(x)=\int_x^L\frac{ds}{v_{\rm eff}(s)}.
```

For a small interval `Delta x` over which velocity is approximately constant,

```math
\boxed{
|\Delta T|
\simeq
\frac{\Delta x}{v_{\rm eff}}.
}
```

Therefore a timing uncertainty `sigma_T` corresponds to the scale

```math
\boxed{
\sigma_{x,T}
\sim
v_{\rm eff}\sigma_T.
}
```

If the observable is a difference of two independent timing measurements with equal uncertainty, the differential noise is approximately

```math
\sqrt2\sigma_T.
```

A `k-sigma` local distinction then requires roughly

```math
\boxed{
\Delta x
\gtrsim
k\sqrt2\,
v_{\rm eff}\sigma_T.
}
```

This is only a local order-of-magnitude criterion.

A global regularized inverse uses all wavelengths simultaneously and can outperform a two-point finite difference for smooth profiles.

---

## 6. Common timing offset is not a spatial-resolution limit

A wavelength-independent additive delay

```math
c
```

can be fitted simultaneously in

```math
\mathbf T
=\mathbf A\mathbf q+c\mathbf1.
```

Therefore cable delay, a common amplifier group delay, or another additive constant is not itself a resolution floor.

The dangerous systematic is a **wavelength-dependent** optical or electronic delay unrelated to carrier transport.

That systematic can masquerade as spatial structure in `q(x)`.

---

## 7. Spectral sampling pitch

For linear grading, photon-energy sampling step `Delta E` moves the nominal generation coordinate by

```math
\boxed{
\Delta x_E
=\frac{|\Delta E|}{G}.
}
```

In wavelength coordinates,

```math
\boxed{
\Delta x_\lambda
\simeq
\frac{hc}{G\lambda^2}|\Delta\lambda|.
}
```

To resolve a spatial feature of width `w_f`, the wavelength grid should sample the corresponding coordinate at least several times across the feature.

Dense wavelength sampling cannot overcome a broad optical generation kernel; it only prevents the source grid from becoming the limiting factor.

---

## 8. Approximate geometric blur budget

If independent calibration blurs are approximately Gaussian-like, a useful first diagnostic is

```math
\boxed{
\sigma_{x,\rm geom}^2
\approx
\sigma_{z,\rm opt}^2
+\sigma_{x,\lambda}^2
+\sigma_{x,g}^2
+\sigma_{x,G}^2.
}
```

This is not a theorem about the inverse estimator.

It is a way to identify which physical input dominates the spatial point-spread budget before attempting regularized reconstruction.

Timing noise should normally be treated through the inverse covariance rather than simply added as another geometric blur, but

```math
v_{\rm eff}\sigma_T
```

is still the correct local scale for whether a feature produces a resolvable delay contrast.

---

## 9. Illustrative timing scale

Take only as a transparent example

```math
v_{\rm eff}=10^5\ {\rm m/s}.
```

Then a transport feature of width

```text
1.0 um
0.5 um
0.1 um
```

corresponds to a local transit-delay contrast of approximately

```text
10 ps
5 ps
1 ps
```

respectively.

These numbers are **not** claimed as the velocity of a specific HgCdTe detector.

They show the measurement scale: micron-level internal transport tomography at `10^5 m/s` requires picosecond-class differential timing information.

---

## 10. Illustrative spectral-coordinate scale

Take only as an example a linear gap change

```math
\Delta E_g=0.125\ {\rm eV}
```

over

```math
L=5\ {\rm um}.
```

Then

```math
G=0.025\ {\rm eV/um}.
```

At

```math
\lambda=8\ {\rm um},
```

a wavelength step

```math
\Delta\lambda=0.10\ {\rm um}
```

corresponds to approximately

```math
|\Delta E|
\simeq
\frac{1.23984}{8^2}(0.10)
\approx1.94\times10^{-3}\ {\rm eV},
```

and therefore

```math
\boxed{
\Delta x_\lambda
\approx0.078\ {\rm um}.
}
```

So in this illustrative gradient, ordinary sub-micron wavelength stepping can encode sub-`0.1 um` nominal position increments.

That does **not** mean the transport reconstruction has `0.1 um` resolution; optical generation width and timing precision can be much coarser.

---

## 11. Why the optical kernel is likely central

The spectral coordinate `x_g(E_gamma)` can be sampled extremely finely in principle.

But the carrier is not generated at one mathematical point.

The optical kernel determines how sharply the detector can localize the generation event internally.

Therefore a serious experiment must know or fit

```text
alpha(E_gamma,x)
+
interference / optical-field profile
+
reflection / cavity effects.
```

The tomography should be thought of as an inverse problem with an optical point-spread function, not as an infinitely sharp spectroscopic ruler.

---

## 12. Conditioning and regularization are separate from physical resolution

Even when the physical kernels are narrow, neighboring wavelength kernels may be highly correlated.

The singular values of the forward matrix `A` determine how many independent spatial modes of `q(x)` can be reconstructed above noise.

Therefore a complete resolution analysis should examine

```text
singular-value spectrum of A
+
timing-noise covariance
+
regularization bias
+
physical optical blur.
```

The number of sampled wavelengths is not the number of independently recoverable spatial degrees of freedom.

---

## 13. Connection to localized-excitation prior art

Position-resolved HgCdTe impulse measurements already exist using physically localized excitation.

That supplies a natural benchmark.

For the spectral method to be valuable, its reconstructed spatial resolution should be compared against

```text
localized optical spot size
+
carrier spreading before collection
+
timing precision of the localized experiment.
```

The spectral method may be useful even with poorer raw spatial resolution if it accesses buried/internal generation coordinates without physically scanning the excitation through the device.

---

## 14. Claim boundary

### Derived / calculable scales

```math
\sigma_{x,E}=\sigma_E/|E_g'|,
```

```math
\sigma_{x,\lambda}
\simeq hc\,\sigma_\lambda/(|E_g'|\lambda^2),
```

```math
\sigma_{x,T}\sim v_{\rm eff}\sigma_T,
```

plus the exact Weibull optical-kernel moments for the stated power-law edge model.

### Diagnostic, not theorem

The quadrature blur budget and simple timing-resolution estimates are experimental-design heuristics.

### Open

- calibrated HgCdTe optical kernel;
- achievable differential timing precision;
- realistic singular-value spectrum for a proposed device/profile;
- spatial resolution after regularized inversion;
- comparison against localized-excitation benchmark data.

---

## 15. Next decisive work

The next numerical study should calculate the singular-value / resolution structure of the full forward matrix for several

```text
optical kernel widths
wavelength grids
timing-noise levels
gradient lengths.
```

The output should be the number and spatial scale of transport modes that can be recovered reliably—not only one favorable synthetic profile.
