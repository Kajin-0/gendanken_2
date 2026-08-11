# HgCdTe Four-Color Shockley-Ramo Closure — Measurement Resource

**Date:** 2026-08-10  
**Status:** **DERIVED / CHECKED / CONDITIONAL** high-SNR covariance calculation for the corrected stochastic HgCdTe theory stress; not an instrument specification

## 1. Question

The corrected four-color HgCdTe model produces a nonzero gradient-sensitive complex closure.

That is not sufficient for an experimentally meaningful prediction.

The next question is:

> **How accurately must the four complex current samples be measured for the predicted closure to reach `3 sigma` under independent equal per-channel noise?**

The answer is demanding but finite, and it improves rapidly with RF frequency in the present model.

---

## 2. Closure noise propagation

For spectral currents

```math
J_0,J_1,J_2,J_3
```

define

```math
d_m=J_{m+1}-J_m
```

and

```math
\mathcal C_4
=2\ln d_1-
\ln d_0-
\ln d_2.
```

For small independent circular complex current errors `epsilon_m`, the linearized coefficients are

```math
\delta\mathcal C_4
=\frac{\epsilon_0}{d_0}
-\left(\frac1{d_0}+\frac2{d_1}\right)\epsilon_1
+\left(\frac2{d_1}+\frac1{d_2}\right)\epsilon_2
-\frac{\epsilon_3}{d_2}.
```

Let

```math
E|\epsilon_m|^2=\sigma_J^2.
```

Then

```math
\boxed{
\sigma_{\mathcal C_4}^2
=\sigma_J^2\sum_m|c_m|^2.
}
```

The exact complex `d_m` from the stochastic HgCdTe model are used below rather than replacing them by the equal-difference approximation.

---

## 3. Three-sigma condition

Let

```math
\mathcal C_{grad}
=\mathcal C_{variable}
-\mathcal C_{homogeneous\ same-optics}
```

be the gradient-sensitive excess.

Require

```math
|\mathcal C_{grad}|
\ge3\sigma_{\mathcal C_4}.
```

Therefore

```math
\boxed{
\sigma_{J,max}
=\frac{|\mathcal C_{grad}|}
{3\sqrt{\sum|c_m|^2}}.
}
\tag{1}
```

Report the requirement relative to the mean magnitude of the three spatial current steps

```math
\langle|\Delta J|\rangle.
```

That quantity is more natural than referencing the much larger absolute raw current.

---

## 4. Corrected stochastic HgCdTe quartet

Use the same no-recombination finite-diffusion stress documented in

`HGCDTE_RAMO_FOUR_COLOR_DIFFUSION_RECOMBINATION.md`:

```text
mean generation depths = 2.5,3.0,3.5,4.0 um
D = 0.02327 m2/s
same graded velocity profile
same real Hansen/Moazzami kernels
semi-infinite upstream bulk matching
no finite entrance boundary.
```

The `3 sigma` independent-noise requirements are approximately

| RF | Gradient-sensitive phase | allowed `sigma_J/<|Delta J|>` | amplitude SNR on spatial current step |
|---:|---:|---:|---:|
| 100 MHz | `-0.01198 deg` | `1.56e-5` | `96.1 dB` |
| 250 MHz | `-0.02982 deg` | `3.88e-5` | `88.2 dB` |
| 500 MHz | `-0.05873 deg` | `7.68e-5` | `82.3 dB` |
| 1 GHz | `-0.11041 deg` | `1.47e-4` | `76.7 dB` |

Here

```math
SNR_{dB}=20\log_{10}
\frac{\langle|\Delta J|\rangle}{\sigma_J}.
```

These are amplitude-SNR conventions for the complex RMS noise definition above.

---

## 5. Interpretation

The low-RF analytic regime is the cleanest theoretically but the hardest statistically.

At `100 MHz`, the closure is only about

```math
2.1\times10^{-4}
```

in dimensionless complex-log magnitude.

The third-difference-like four-color observable strongly amplifies independent sample noise.

Moving upward in RF increases the gradient-sensitive closure much faster than it changes the current-step scale in this particular model, so the required current-step SNR relaxes from roughly

```text
96 dB -> 77 dB
```

between `100 MHz` and `1 GHz`.

That improvement is not free: higher RF also increases sensitivity to

```text
parasitic electrical phase,
nonlocal transport,
multiple carrier modes,
boundary modes,
and optical higher-order corrections.
```

The correct experiment therefore has an RF design tradeoff rather than a universal optimum frequency.

---

## 6. Optical model accuracy

The homogeneous same-optics phase closure is approximately

```text
~20-22% of the gradient-sensitive phase excess
```

across `100 MHz-1 GHz` for this quartet.

That optical term is a **calibrated/modelled bias**, not random measurement noise.

If its model uncertainty were, for example, `10%` of the correction itself, the corresponding uncertainty would be only a few percent of the predicted gradient-sensitive phase in this explicit stress.

No specific optical-model accuracy is asserted here; the statement is only a scale comparison.

---

## 7. Relation to spacing optimization

The chosen `h=0.5 um` quartet is not globally optimized.

The general theory gives

```text
transport closure signal ~ h^2
independent closure noise ~ h^-1
```

in the local low-RF regime, so statistical SNR initially grows as

```math
h^3.
```

Larger spacing therefore helps until

```text
optical source-shape curvature,
transport nonlocality over the quartet,
or boundary exposure
```

becomes too large.

The separate cube-root spacing theorem gives the conditional MSE optimum once the dominant systematic coefficient and noise are specified.

---

## 8. What this result does and does not establish

It establishes that the corrected four-color prediction has a concrete coherent-measurement resource rather than merely being nonzero.

It does **not** establish that a particular laboratory can achieve the required covariance.

No instrument noise floor, optical power, detector responsivity, or electronics chain has been assumed here.

The result should therefore be read as

> **If the per-channel complex-current uncertainty reaches the stated fraction of the spatial current step, the explicit HgCdTe gradient stress becomes a 3-sigma four-color closure effect under independent noise.**

That is a falsifiable measurement target suitable for a theory paper.

Numerical implementation:

`numerics/hgcdte_ramo_four_color_measurement_resource.py`
