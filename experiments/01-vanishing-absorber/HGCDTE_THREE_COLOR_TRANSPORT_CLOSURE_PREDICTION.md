# HgCdTe Three-Color Closure — First Material-Level Falsifiable Prediction

**Date:** 2026-08-10  
**Status:** conditional theoretical worked example using Hansen/Moazzami optics plus a reduced quasi-neutral HgCdTe transport model; no calibrated device prediction and no novelty claim

## 1. Purpose

The general theory predicts that three wavelengths whose internal generation coordinates are equally spaced obey

```math
H_2^2=H_1H_3
```

inside a homogeneous scalar first-passage segment.

The leading closure failures separate asymptotically:

```text
transport inhomogeneity -> O(omega) phase
centered optical shape evolution -> O(omega^2) magnitude, O(omega^3) phase.
```

The first material-level question is therefore:

> **In a realistic graded-HgCdTe optical model, is the optical shape-evolution floor small enough that a physically modest transport gradient produces a clearly larger phase closure signal?**

For one explicit theory stress, the answer is yes by a large margin.

---

## 2. Deliberately simple graded-HgCdTe profile

Use a monotonic linear composition profile

```text
T = 300 K
L = 7.6 um
x(0) = 0.55
x(L) = 0.32.
```

The high-Cd side is the optical entrance and the low-Cd side is the downstream collecting end, matching the corrected transport orientation used in the theory branch.

This is a **simple gedanken material profile**, not a claimed existing device.

The bandgap is Hansen-Schmit-Casselman:

```math
E_g(x,T)
=-0.302+1.93x-0.81x^2+0.832x^3
+5.35\times10^{-4}T(1-2x).
```

Absorption uses the repository Moazzami above-gap model

```math
\alpha(E,x,T)
=K(x,T)
\left(\frac{E-E_g}{E}\right)^{n(x,T)},
\qquad E>E_g.
```

Beer-Lambert absorption then gives the conditional carrier-generation density

```math
p_\lambda(z).
```

---

## 3. Choose the colors by physics, not equal wavelength spacing

The three-color theorem requires equally spaced **internal generation coordinates**, not equally spaced wavelengths.

Choose target mean depths

```math
\boxed{
\mu_1=2.0\ \mu m,
\qquad
\mu_2=4.0\ \mu m,
\qquad
\mu_3=6.0\ \mu m.
}
```

Solving the real HgCdTe optical kernels gives approximately

```text
mean depth 2.0 um -> lambda1 = 2.05934 um
mean depth 4.0 um -> lambda2 = 2.39391 um
mean depth 6.0 um -> lambda3 = 2.87456 um.
```

Modeled absorbed fractions are approximately

```text
lambda1 -> Pabs = 0.999996
lambda2 -> Pabs = 0.999338
lambda3 -> Pabs = 0.94953.
```

Thus all three coordinates remain strongly absorbing in this example.

The conditional generation widths are approximately

```text
mu=2 um -> sigma_z ~0.783 um
mu=4 um -> sigma_z ~0.789 um
mu=6 um -> sigma_z ~0.652 um.
```

The kernels are therefore **not** rigid copies. This makes the test useful: the real optical shape-evolution error is included rather than artificially removed.

---

## 4. Conditional transport model

Use the central scale already developed in the repository:

```text
electron mobility mu = 9000 cm^2/Vs
T = 300 K
Einstein diffusion D = mu kT/q ~0.02327 m^2/s.
```

The force-equivalent field is the quasi-neutral full bandgap gradient

```math
F(z)=\left|\frac{dE_g}{dz}\right|/q.
```

The velocity field uses the broad empirical saturation stress

```math
v_F(z)
=
\frac{\mu F(z)}
{1+[F(z)/d]^r},
```

with

```text
d = 8 kV/cm
r = 2.2.
```

These are sensitivity coordinates, not calibrated 300 K constants for a particular sample.

Include the reduced conduction-density-of-states term

```math
v_{DOS}
=D\frac{d\ln N_c}{dz}
\simeq
\frac{3D}{2}\frac{d\ln E_g}{dz}.
```

The resulting downstream drift varies only from approximately

```math
\boxed{
3.76\times10^4
\rightarrow
3.21\times10^4\ \mathrm{m/s}
}
```

across the full absorber.

That is only about a `15%` spatial variation.

No bulk recombination is included in this first worked closure prediction so the transport-vs-optics comparison is transparent.

---

## 5. Finite-RF first-passage calculation

For each RF frequency solve

```math
\boxed{
D u''(z)+v(z)u'(z)-i\omega u(z)=0.
}
```

Use

```math
u'(0)=0
```

at the optical entrance and

```math
u(L)=1
```

at the collector.

The wavelength-dependent complex response is

```math
\boxed{
H_j(\omega)
=\int p_j(z)u(z,\omega)dz.
}
```

Define the logarithmic three-color closure residual

```math
\boxed{
\mathcal L(\omega)
=2\ln H_2-\ln H_1-\ln H_3.
}
```

Perfect homogeneous spectral closure gives

```math
\mathcal L=0.
```

---

## 6. Optical false-positive reference

To isolate the scale of **optical kernel-shape evolution**, propagate the exact same three HgCdTe kernels through one homogeneous transport law using

```text
same D
spatially averaged drift velocity.
```

This homogeneous reference has no transport inhomogeneity.

Any remaining closure error therefore comes only from the fact that the three real Beer-Lambert generation distributions change shape with wavelength.

This is the relevant false-positive floor for the three-color test in this explicit model.

---

## 7. Main result

The calculated phase closure is approximately

| RF | Full graded transport | Homogeneous optical-shape floor |
|---:|---:|---:|
| 10 MHz | `-0.01235 deg` | `+0.00000003 deg` |
| 50 MHz | `-0.06170 deg` | `+0.0000038 deg` |
| 100 MHz | `-0.12319 deg` | `+0.000030 deg` |
| 250 MHz | `-0.30432 deg` | `+0.000472 deg` |
| 500 MHz | `-0.58331 deg` | `+0.00370 deg` |
| 1 GHz | `-0.98549 deg` | `+0.02769 deg` |

The corresponding log-magnitude closure values are approximately

| RF | Full graded transport | Homogeneous optical floor |
|---:|---:|---:|
| 100 MHz | `-1.41e-4` | `-3.40e-5` |
| 500 MHz | `-3.42e-3` | `-8.40e-4` |
| 1 GHz | `-1.25e-2` | `-3.26e-3` |

---

## 8. The low-RF phase channel is exceptionally clean

At `100 MHz`,

```text
transport-gradient phase closure ~0.123 deg
optical shape-evolution phase floor ~0.000030 deg.
```

The ratio is roughly

```math
\boxed{4\times10^3.}
```

At `500 MHz`, the ratio remains approximately

```math
\boxed{1.6\times10^2.}
```

Even at `1 GHz`, where optical higher-order effects are no longer negligible, the transport phase closure remains about

```math
\boxed{36\times}
```

larger in this explicit stress.

This is the key prediction.

---

## 9. Why the signal is so different in phase

The general asymptotic theorem already predicted the separation.

### Spatial transport variation

At low RF,

```math
\mathcal L_{tr}
\simeq
-i\omega h^2
\partial_z(1/w)
+O(\omega^2).
```

So phase closure begins **linearly** with RF frequency.

### Mean-centered optical shape evolution

Because every generation kernel is centered at its own mean depth, the first optical cumulant vanishes.

Therefore

```math
\mathcal L_{opt}
\sim
\Gamma^2\Delta\sigma_z^2/2
+O(\Gamma^3)
```

and

```text
log-magnitude closure begins ~omega^2
phase closure begins ~omega^3.
```

The HgCdTe numerical result follows exactly this hierarchy.

---

## 10. A simple falsifiable prediction

For this class of monotonic graded HgCdTe absorber, conventional quasi-neutral local drift-diffusion predicts:

> **Three colors selected by equal mean generation depth should show a low-frequency complex closure residual whose leading transport contribution is phase-like and approximately linear in RF frequency.**

For the explicit `x=0.55 -> 0.32`, `7.6 um` stress, the predicted scale is about

```text
~0.12 deg at 100 MHz
~0.58 deg at 500 MHz
~0.99 deg at 1 GHz.
```

The real wavelength-dependent absorption-shape correction is much smaller in phase over the same range.

This is a direct prediction that could be falsified without reconstructing a pointwise velocity profile.

---

## 11. What different outcomes would mean

### Outcome A — near-zero phase closure

If measured closure remains at the optical floor despite a known composition-driven transport gradient, the assumed quasi-neutral drift model is too strong or some other transport physics cancels it.

### Outcome B — approximately linear low-RF phase closure at the predicted scale/sign

This is consistent with a spatially varying local transit law.

It does not by itself prove the microscopic band-edge force model.

### Outcome C — strong RF dispersion inconsistent with the local model

If the inferred local `D_app,w_app` also vary with frequency, ordinary Markov drift-diffusion fails and the trapping/relaxation/nonlocal hierarchy becomes relevant.

### Outcome D — closure dominated by `omega^2` magnitude with little linear phase

This points first toward optical-kernel shape evolution or another non-transport spectral correction rather than spatial drift variation.

---

## 12. Numerical convergence

The finite-difference first-passage solve uses

```text
3200 spatial intervals over 7.6 um
centered interior derivatives
second-order reflecting entrance condition.
```

A convergence stress over `400-6400` intervals changes the `1 GHz` closure phase by less than roughly `0.001 deg` once the grid is in the `~1600-6400` range.

Thus the order-one-degree prediction is not a spatial-grid artifact.

---

## 13. What is conditional

This result depends on

```text
the chosen linear x(z) profile
Hansen gap
Moazzami absorption
mu = 9000 cm2/Vs
Einstein diffusion
the reduced DOS correction
the broad empirical saturation stress
reflecting entrance boundary
no bulk recombination in this first example.
```

It is therefore **not** a prediction for a named existing HgCdTe detector.

The important theoretical result is the scale separation:

> **a modest realistic transport inhomogeneity can create an O(0.1-1 deg) low-RF phase closure while the same real optical kernels produce a much smaller phase false-positive floor.**

---

## 14. Next calculation

The next high-value step is to add one controlled alternative at a time while keeping the same optical kernels:

```text
ordinary local drift-diffusion
vs
reversible trapping
vs
finite transport relaxation
vs
leading spatial nonlocal correction.
```

Then calculate the multi-frequency apparent

```math
D_{app}(\omega),
\qquad
w_{app}(\omega)
```

and the exact closure-test noncentrality.

That would turn this first material prediction into a direct **model discrimination forecast**.

Numerical implementation:

`numerics/hgcdte_three_color_transport_closure_prediction.py`
