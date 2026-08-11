# Realistic 2-D Geometry Closure Stress

**Date:** 2026-08-11  
**Status:** **CHECKED / CONDITIONAL geometry hardening stress**; not a calibrated detector simulation and not a novelty claim

## 1. Question

The analytic closure hierarchy was derived most cleanly in one spatial dimension. The most important remaining ordinary-device objection is therefore:

> Can a finite electrode, curved Shockley-Ramo weighting potential, and a depletion-like nonuniform physical field generate a false four-color transport-gradient signal without being exposed by the higher model-order tests?

This file records a direct attempted falsification.

The executable regression is:

`numerics/realistic_geometry_closure_stress.py`

## 2. Geometry and transport stress

The model is intentionally more realistic than the one-dimensional theorem while remaining simple enough to audit.

### Electrostatic domain

```text
absorber thickness = 7.6 um
lateral width       = 16 um
bottom electrode    = 0 V
selected top pixel  = +0.30 V physical potential
```

The selected top electrode occupies either 100%, 75%, or 50% of the top boundary.

The physical potential obeys Poisson's equation on a 2-D finite-difference grid. Sidewalls and the uncontacted part of the top surface have zero normal derivative.

The Shockley-Ramo weighting potential is solved separately:

```text
selected top electrode -> phi_w = 1
bottom electrode       -> phi_w = 0
other boundaries       -> zero normal derivative
```

Thus the weighting field is not assumed to be uniform.

### Depletion stress

For the depletion cases, the upper `3.0 um` contains a controlled constant Poisson curvature

```math
\nabla^2 V = \frac{2V_{\rm sc}}{W_d^2},
\qquad
V_{\rm sc}=0.05\ {\rm V},
\qquad
W_d=3.0\ {\rm \mu m}.
```

This is a **space-charge sensitivity coordinate**, not a claimed HgCdTe doping profile.

### Drift law

An electron-like carrier follows `+grad(V)` with

```math
\mathbf v
=
\frac{\mu\nabla V}
{\left[1+\left(\mu|\nabla V|/v_{\rm sat}\right)^2\right]^{1/2}},
```

using

```text
mu    = 0.90 m^2/V/s
v_sat = 6.0e4 m/s.
```

Diffusion is deliberately omitted in this first geometry stress. The calculation therefore isolates a failure caused by multidimensional signal formation and field geometry rather than adding another stochastic mechanism simultaneously.

## 3. Exact Ramo implementation check

For every trajectory the RF response is accumulated as

```math
H(\omega|\mathbf r_0)
=
\int e^{-i\omega t}\,d\phi_w .
```

Numerically, each trajectory segment contributes its exact discrete weighting-potential increment rather than approximating `v dot grad(phi_w) dt`.

At DC the sum therefore telescopes to

```math
H(0|\mathbf r_0)=1-\phi_w(\mathbf r_0)
```

for a collected carrier.

In the refined runs:

```text
collected trajectory fraction = 1.000000
maximum DC Ramo consistency error = 5.4e-15
```

This is the primary internal validation of the 2-D signal-formation calculation.

## 4. Six-channel optical coordinate

The same Hansen/Moazzami graded-HgCdTe optical construction is extended to six source-depth means:

| mean depth (um) | wavelength (um) | absorbed fraction | sigma_z (um) |
|---:|---:|---:|---:|
| 2.0 | 2.059341983 | 0.999996080 | 0.783254 |
| 2.5 | 2.134650606 | 0.999984721 | 0.787048 |
| 3.0 | 2.215042252 | 0.999943407 | 0.789835 |
| 3.5 | 2.301173401 | 0.999801116 | 0.790930 |
| 4.0 | 2.393906880 | 0.999337640 | 0.788849 |
| 4.5 | 2.494502563 | 0.997909183 | 0.780666 |

The lateral generation profile is a centered Gaussian with `sigma_x=2 um`, integrated over `|x|<=3.5 um`. This keeps the optical support beneath even the 50%-width selected contact so that the deterministic trajectory model does not rely on lateral diffusion to rescue carriers generated outside the active footprint.

## 5. Four-color result: geometry is a serious confound

The central four channels (`2.5, 3.0, 3.5, 4.0 um`) are tested with the ordinary first-difference closure.

### Planar same-optics baseline

| RF | four-color phase |
|---:|---:|
| 100 MHz | +0.002769 deg |
| 500 MHz | +0.013682 deg |
| 1 GHz | +0.026346 deg |

This is the finite optical-kernel floor for the present deterministic homogeneous transport.

### 75% finite contact, no depletion curvature

| RF | total phase | excess over planar |
|---:|---:|---:|
| 100 MHz | +0.003885 deg | +0.001116 deg |
| 500 MHz | +0.017265 deg | +0.003583 deg |
| 1 GHz | +0.022395 deg | -0.003951 deg |

Finite weighting geometry by itself creates a strong **DC amplitude/model-order** signature but only a small RF phase confound in this centered-source stress.

### 75% finite contact + 3 um depletion stress

| RF | total phase | geometry/depletion excess | fraction of current HgCdTe gradient target |
|---:|---:|---:|---:|
| 100 MHz | -0.006072 deg | **-0.008841 deg** | **0.738** |
| 500 MHz | -0.032145 deg | **-0.045827 deg** | **0.780** |
| 1 GHz | -0.069168 deg | **-0.095513 deg** | **0.865** |

The current one-dimensional graded-transport targets are `-0.011978`, `-0.058727`, and `-0.110405 deg`, respectively.

Therefore:

```math
\boxed{
\text{realistic weighting/depletion geometry can mimic an }O(1)
\text{ fraction of the proposed gradient signal.}
}
```

This is not a small caveat. A four-color phase residual by itself is not mechanism-specific.

The 50%-contact depletion stress is even more severe and changes sign with RF:

```text
100 MHz -> +0.019067 deg excess over planar
500 MHz -> +0.024754 deg
1 GHz   -> -0.161243 deg
```

That behavior is qualitatively unlike a clean one-dimensional low-RF gradient law.

## 6. The important rescue: geometry exposes model order before interpretation

For six colors, form the `3 x 3` Hankel matrix of the five first differences and inspect its singular spectrum.

For a strict one-mode sequence:

```text
sigma_2 / sigma_1 -> 0.
```

For an approximate rank-two sequence:

```text
sigma_2 / sigma_1 is finite,
sigma_3 / sigma_2 << 1.
```

### Refined 75%-contact + depletion case

| RF | sigma2/sigma1 | sigma3/sigma2 |
|---:|---:|---:|
| DC | 4.771e-4 | 8.202e-3 |
| 100 MHz | 4.804e-4 | 8.611e-3 |
| 500 MHz | 5.635e-4 | 1.352e-2 |
| 1 GHz | 8.581e-4 | 1.531e-2 |

### Refined 50%-contact + depletion case

| RF | sigma2/sigma1 | sigma3/sigma2 |
|---:|---:|---:|
| DC | 2.418e-3 | 3.266e-3 |
| 100 MHz | 2.490e-3 | 3.025e-3 |
| 500 MHz | 3.518e-3 | 6.378e-3 |
| 1 GHz | 4.095e-3 | 1.429e-2 |

The multidimensional response is therefore **not rank one**, but over this six-channel window it is surprisingly close to rank two.

That is favorable for the hierarchy: the geometry tends to appear as an extra spatial mode instead of silently masquerading as a clean one-mode gradient.

## 7. Is the second mode statistically visible soon enough?

Using the manuscript's exact linearized noise for the first adjacent Hankel minor,

```math
W_0=d_0d_2-d_1^2,
```

the raw-current noise level required for a `3 sigma` second-mode witness can be solved directly.

At 100 MHz:

```text
75% contact + depletion:
3-sigma second-mode threshold = 84.61 dB current-step amplitude SNR

50% contact + depletion:
3-sigma second-mode threshold = 71.49 dB current-step amplitude SNR
```

The existing 100-MHz worked example requires approximately

```text
96.1 dB
```

current-step amplitude SNR to claim the present four-color transport-gradient signal at `3 sigma`.

Hence the 75%-contact geometry mode becomes statistically resolvable about

```math
96.1-84.6 \simeq 11.5\ {\rm dB}
```

**before** the experiment reaches the SNR needed for the proposed gradient claim.

For the 50%-contact stress the margin is about `24.6 dB`.

This is the strongest result of the geometry study:

> **At the measurement precision needed to interpret the present HgCdTe four-color gradient target, these representative finite-geometry confounds should already announce themselves as an additional spatial mode.**

That statement is conditional on this geometry family; it is not yet a theorem for arbitrary devices.

## 8. Six-color roots do not become a false ordinary mechanism

The first-difference sequence is close enough to rank two that a two-root recurrence can be fit. However, the effective roots do not satisfy the simple finite-boundary scalar root constraint.

For a homogeneous scalar drift-diffusion operator with a finite boundary,

```math
r_1+r_2=-w/D
```

must be **real and RF-independent**.

For the refined 75%-contact depletion stress, the fitted effective spatial-root sum has imaginary part approximately

```text
DC       -> 0.000 1/um
100 MHz  -> +0.141 1/um
500 MHz  -> +0.568 1/um
1 GHz    -> +0.680 1/um.
```

Thus the geometry-generated second mode does not survive the next rung as a valid homogeneous finite-boundary transport model.

The correct interpretation is:

```text
four-color failure
+ resolved second mode
+ RF root-law failure
-> lower-dimensional homogeneous transport model rejected;
   geometry/nonuniform transport remains required.
```

## 9. Five-color observation annihilation is not a universal geometry cure

The exact five-color theorem remains valid when the observation forcing is affine in the sampled one-dimensional coordinate.

The present finite-pixel problem violates that hypothesis. The 2-D weighting potential is curved and the carrier trajectories themselves bend laterally.

For the 75%-contact depletion stress, the five-color second-difference phase closure is

```text
100 MHz -> -0.370431 deg
500 MHz -> -0.088599 deg
1 GHz   -> -0.095796 deg.
```

The five-color construction therefore does **not** magically remove a general multidimensional weighting/depletion geometry.

This sharpens the experimental rule:

```text
known approximately linear 1-D observation trend
-> five-color annihilation is legitimate;

unknown curved / multidimensional geometry
-> use model-order + RF-root falsification,
   or model the electrostatics explicitly.
```

## 10. Numerical refinement

For the 75%-contact depletion stress, the main run uses

```text
electrostatic grid: 121 x 91
lateral source quadrature: 13 points
depth trajectory grid: 41 points
trajectory step: 0.020 um
```

A coarser run uses

```text
81 x 61
9 lateral points
31 depth points
0.035 um trajectory step.
```

The four-color phase changes under simultaneous refinement by

| RF | coarse | refined | relative change |
|---:|---:|---:|---:|
| 100 MHz | -0.005769 deg | -0.006072 deg | 4.99% |
| 500 MHz | -0.030544 deg | -0.032145 deg | 4.98% |
| 1 GHz | -0.065817 deg | -0.069168 deg | 4.84% |

This is adequate for the present classification result, but not for claiming device-specific precision at the percent level.

## 11. Scientific consequence

The realistic-geometry stress produces both bad news and good news.

### Bad news

The one-dimensional four-color gradient phase is **not geometry-proof**. A finite weighting potential plus depletion-field curvature can create a residual of the same order as the target transport signal.

### Good news

In the tested geometries the confound does not remain hidden at the same model order. It generates a much larger second-mode witness, and the current experiment's own SNR requirement is stringent enough that this second mode should become statistically visible before a gradient-specific claim is justified.

The hierarchy therefore survives this first multidimensional attack in a weaker but more defensible form:

```math
\boxed{
\text{four colors detect failure;}
\quad
\text{six colors classify model order;}
\quad
\text{RF root laws prevent premature mechanism assignment.}
}
```

The five-color polynomial-annihilation route remains a targeted tool for known smooth one-dimensional observation trends, not a replacement for electrostatic validation.

## 12. Remaining limitation

This calculation is still a deterministic high-Peclet stress.

It does not yet include:

- lateral/longitudinal diffusion in the 2-D field,
- electron-hole coupling,
- trapping or hot-carrier state dynamics,
- a self-consistent semiconductor Poisson/drift-diffusion solution,
- contact transfer kinetics,
- measured pixel geometry or doping.

The next geometry step, if needed for submission, should therefore be a self-consistent 2-D drift-diffusion/Poisson simulation for one plausible detector structure, with the synthetic measurement analyzed blind by exactly the same hierarchy.
