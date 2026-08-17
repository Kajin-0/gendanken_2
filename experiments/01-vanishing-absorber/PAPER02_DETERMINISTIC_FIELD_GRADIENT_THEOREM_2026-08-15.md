# Deterministic field-gradient apparent diffusion in the planar Shockley-Ramo observable

**Date:** 2026-08-15  
**Status:** **DERIVED / CANDIDATE DISTINCT APPLICATION — PRIORITY UNPROVEN**  
**Purpose:** explain analytically why the Paper-02 depletion calculation returns a positive drift-diffusion coefficient even though every carrier trajectory is deterministic and the microscopic diffusion coefficient is exactly zero.

## 1. Setup

Consider the simplest possible geometry in which the numerical effect already occurs.

- one spatial coordinate `z`;
- collecting electrode at `z=L`;
- planar Shockley-Ramo weighting potential

```math
\phi_w(z)=\frac{z}{L};
```

- a carrier launched at `z=z_0`;
- deterministic downstream velocity

```math
v(z)>0;
```

- no microscopic diffusion;
- no recombination.

Define the deterministic travel time from the launch point to an intermediate position `x` by

```math
\tau(x;z_0)=\int_{z_0}^{x}\frac{du}{v(u)}.
```

For Fourier convention `e^{-i\omega t}`, the terminal-current transfer integrated over the Ramo path is

```math
\boxed{
H(z_0,\omega)
=\frac{1}{L}\int_{z_0}^{L}
\exp[-i\omega\tau(x;z_0)]\,dx.
}
```

This is an exact deterministic path functional. No stochastic broadening has been introduced.

---

## 2. Exact source-coordinate differential equation

Differentiate with respect to launch coordinate `z=z_0`.

Because

```math
\frac{\partial\tau(x;z)}{\partial z}=-\frac{1}{v(z)},
```

Leibniz differentiation gives

```math
\boxed{
\frac{\partial H}{\partial z}
=-\frac{1}{L}
+\frac{i\omega}{v(z)}H.
}
```

Define the infinitesimal spectral-depth difference response

```math
P(z,\omega)=\frac{\partial H}{\partial z}.
```

For constant velocity `v(z)=v_0`, the exact solution is

```math
P(z,\omega)
=-\frac{1}{L}
\exp\left[-i\omega\frac{L-z}{v_0}\right],
```

so the source-depth differences are exactly one spatial exponential and contain no attenuation curvature associated with diffusion.

A velocity gradient changes this conclusion even though each trajectory remains deterministic.

---

## 3. Low-frequency expansion

Expand the path integral:

```math
H(z,\omega)
=\frac{L-z}{L}
-\frac{i\omega}{L}I(z)
+O(\omega^2),
```

where

```math
\boxed{
I(z)=\int_z^L\frac{L-u}{v(u)}\,du.
}
```

Using the exact differential equation,

```math
P(z,\omega)
=-\frac{1}{L}
\left[
1-i\omega F(z)-\omega^2\frac{I(z)}{v(z)}+O(\omega^3)
\right],
```

with

```math
\boxed{
F(z)=\frac{L-z}{v(z)}.
}
```

Therefore

```math
\boxed{
\log[-LP(z,\omega)]
=-i\omega F(z)
+\omega^2K(z)
+O(\omega^3),
}
```

where

```math
\boxed{
K(z)=\frac{F(z)^2}{2}-\frac{I(z)}{v(z)}.
}
```

---

## 4. Finite source-spacing effective exponent

For two neighboring point-source coordinates separated by `h`, define the local spatial multiplier

```math
q_h(z,\omega)
=\frac{P(z+h,\omega)}{P(z,\omega)}
```

and the apparent one-mode exponent

```math
\gamma_h(z,\omega)
=-\frac{1}{h}\log q_h(z,\omega).
```

Then

```math
\gamma_h(z,\omega)
=-i a_{1,h}\omega+a_{2,h}\omega^2+O(\omega^3),
```

with the **exact finite-difference low-frequency coefficients**

```math
\boxed{
a_{1,h}
=-\frac{F(z+h)-F(z)}{h},
}
```

```math
\boxed{
a_{2,h}
=-\frac{K(z+h)-K(z)}{h}.
}
```

Thus even a completely deterministic variable-velocity device can produce a positive real quadratic term in the apparent spatial exponent.

By the low-frequency effective-diffusion theorem, if `a_{1,h}>0` and `a_{2,h}>0`, a homogeneous drift-diffusion inversion returns

```math
\boxed{
V_{*,\mathrm{eff}}=\frac{1}{a_{1,h}},
\qquad
D_{\mathrm{eff}}=\frac{a_{2,h}}{a_{1,h}^3},
}
```

although the microscopic model used to generate the data has `D=0`.

---

## 5. Infinitesimal-spacing theorem

Take `h -> 0`.

The first coefficient is

```math
\boxed{
a_1(z)
=-F'(z)
=\frac{1}{v(z)}
+\frac{(L-z)v'(z)}{v(z)^2}.
}
```

For the quadratic coefficient, direct differentiation gives

```math
\boxed{
a_2(z)
=\frac{v'(z)}{v(z)^2}
\left[
\frac{(L-z)^2}{v(z)}
-\int_z^L\frac{L-u}{v(u)}\,du
\right].
}
```

This is the deterministic field-gradient source of the apparent diffusion term.

No stochastic process appears anywhere in the derivation.

---

## 6. Monotone acceleration implies positive apparent diffusion

Suppose velocity increases monotonically downstream on `[z,L]`:

```math
v'(z)>0,
\qquad
v(u)\ge v(z)\quad (u\ge z).
```

Then

```math
I(z)
=\int_z^L\frac{L-u}{v(u)}\,du
\le
\frac{1}{v(z)}\int_z^L(L-u)\,du
=\frac{(L-z)^2}{2v(z)}.
```

Hence

```math
\frac{(L-z)^2}{v(z)}-I(z)
\ge
\frac{(L-z)^2}{2v(z)}>0.
```

Since `v'(z)>0`, it follows that

```math
\boxed{a_2(z)>0.}
```

Therefore:

> **A deterministic carrier that accelerates monotonically toward a planar collecting electrode generically acquires a positive apparent diffusion coefficient when its low-frequency spectral-depth response is forced onto the homogeneous drift-diffusion manifold.**

The apparent `D` is produced by velocity-gradient timing dispersion in the terminal-current observable, not by microscopic random walk.

---

## 7. Weak-gradient limit

Let the velocity gradient be small over the remaining collection distance, so that `v(u)` can be replaced by `v(z)` inside `I(z)` to zeroth order while retaining `v'(z)` in the prefactor.

Then

```math
I(z)
\simeq\frac{(L-z)^2}{2v(z)},
```

and

```math
\boxed{
a_2(z)
\simeq
\frac{v'(z)(L-z)^2}{2v(z)^3}.
}
```

At the same order

```math
a_1\simeq\frac{1}{v(z)}.
```

Therefore

```math
\boxed{
D_{\rm eff}(z)
\simeq
\frac{1}{2}(L-z)^2v'(z).
}
```

This compact expression is physically transparent:

- no velocity gradient -> no false diffusion;
- the effect grows linearly with the local downstream acceleration gradient;
- the effect grows quadratically with remaining collection distance.

The dimensions are correct because `v'(z)` has units `s^{-1}`.

---

## 8. Why deterministic heterogeneity creates frequency attenuation

For a single launch depth and a single deterministic path there is only one trajectory, but the measured terminal-current transfer is not an arrival-time delta function.

Shockley-Ramo current integrates the entire path:

```math
H(\omega)=\int e^{-i\omega t}\,d\phi_w.
```

Different pieces of that deterministic path contribute at different times. A nonuniform velocity changes the distribution of Ramo weight over time. When source depth is varied, the corresponding path-weighted delay distribution changes non-affinely.

The quadratic frequency attenuation that a homogeneous model interprets as diffusion can therefore arise from **deterministic intrapath timing structure**, before any ensemble stochasticity is added.

This is distinct from ordinary carrier-packet diffusion, although both mechanisms enter the low-frequency recovered exponent through the same quadratic coefficient.

---

## 9. Relation to the current numerical depletion model

The planar-depletion calculation solves a one-dimensional field profile embedded in the same 2-D solver. In the space-charge region the electrostatic potential has nonzero curvature, so the downstream field and saturated-drift velocity vary with depth.

The full-width contact eliminates lateral weighting-field structure. Thus the false diffusion observed in the `planar_depletion` scenario does not require finite-electrode geometry.

The numerical truth contains:

```text
microscopic diffusion       = 0
recombination               = 0
finite-contact perturbation = 0
space-charge drop           = 0.05 V
space-charge width          = 3.0 um
total bias                  = 0.30 V
```

Yet the calibrated-kernel one-mode inversion at 100 MHz gives

```math
D_{\rm eff}=2.6098\times10^{-3}\ {\rm m^2/s}>0.
```

The theorem above supplies a direct deterministic mechanism for the sign and existence of that result.

A quantitative point-by-point comparison between the analytic `a_1,a_2` formulas and the finite-kernel fitted root remains a separate validation task because the latter averages over six finite generation kernels and a finite source-depth interval rather than taking `h->0` at a point.

---

## 10. Prior-art boundary after initial audit

The broad phenomenon that nonuniform electric fields corrupt semiconductor transport extraction is established prior art and must not be claimed as new.

Relevant known examples include:

- inhomogeneous-field TOF transients producing incorrect mobility and apparent DOS structure;
- space-charge assumptions causing severe overestimation of diffusion length in photocarrier-grating analysis;
- exact current-transient formalisms showing that internal space charge and electrode/displacement current alter the relationship between internal carrier dynamics and measured terminal current;
- conventional TOF fitting of transient broadening to drift velocity and diffusion coefficient.

The candidate distinct contribution is therefore narrower:

> the exact Shockley-Ramo source-coordinate derivation above, its positive `D_eff` theorem for deterministic downstream acceleration, and its role as a hidden confound in wavelength-programmed spectral-depth / RF model-falsification measurements.

**Priority remains unproven.** A focused full-text audit is still required before manuscript drafting.

---

## 11. Next tests

1. Evaluate the finite-spacing formulas directly on the numerical velocity profile and compare their `D_eff` with the fitted calibrated-kernel value.
2. Sweep depletion width and space-charge drop and test the weak-gradient scaling

```math
D_{\rm eff}\propto (L-z)^2v'(z).
```

3. Repeat with an independent analytic field profile to show that the effect is not specific to the quadratic Poisson surrogate.
4. Derive the cubic coefficient for deterministic `v(z)` and predict the RF scale at which the wrong homogeneous diffusion law becomes rejectable.
5. Convert the residual-vs-frequency curve into required experimental complex-response precision.

Until those tests and the priority audit are complete, this theorem is a research result, not a publication-priority claim.
