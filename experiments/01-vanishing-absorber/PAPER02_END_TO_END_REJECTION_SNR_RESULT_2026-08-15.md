# End-to-end RF rejection SNR result

**Date:** 2026-08-15  
**Status:** **CHECKED UNDER EXPLICIT THEORETICAL NOISE MODEL / PRIORITY UNPROVEN**

## 1. Purpose

`PAPER02_RF_REJECTION_PRECISION_CRITERION_2026-08-15.md` derived the covariance-aware criterion for rejecting a wrong homogeneous drift-diffusion model:

```math
T=\min_{\mathbf p}
[\mathbf x-\mathbf m(\mathbf p)]^T
C_\gamma^{-1}
[\mathbf x-\mathbf m(\mathbf p)],
```

with nuisance-alternative noncentrality

```math
\Lambda=\mathbf d^TQ_\perp\mathbf d.
```

The present calculation propagates a fully specified theoretical six-channel noise model through the calibrated finite-kernel root inverse and then through a **joint re-fit of the wrong homogeneous `D,w` model at every cumulative RF bandwidth**.

This is stronger than comparing a fixed wrong model with one later RF point. The homogeneous model is allowed to move to its best covariance-weighted approximation to the nuisance data over each entire band.

---

## 2. Noise model

At each RF frequency, every one of the six complex spectral channels has independent Gaussian noise with

```text
same standard deviation in Re and Im
no cross-channel correlation
no cross-frequency correlation
```

Define the RMS-channel SNR at each RF frequency by

```math
\boxed{
S=\frac{\sqrt{\frac1M\sum_m|J_m|^2}}
{\sigma_{\rm quadrature}}.
}
```

The same value `S` is assumed at every included RF frequency.

This is a transparent theoretical reference model, **not an instrument specification**.

At `S=1`, the full real `12 x 6` Jacobian of the calibrated one-mode channel model with respect to

```text
Re C, Im C, Re K, Im K, Re r, Im r
```

is inverted to obtain the covariance of the recovered complex root after profiling the linear offset/amplitude parameters.

Root covariance then scales exactly as `1/S^2` in the linearized regime.

---

## 3. Device nuisance alternative

The nuisance system is the fine planar-depletion conditional stress used throughout Paper 02:

```text
full-width planar contact
bias                     0.30 V
depletion width           3.0 um
space-charge drop         0.05 V
microscopic diffusion     0
recombination             0
six calibrated HgCdTe generation kernels
field mesh                121 x 91
source quadrature         13 x 41
trajectory step           0.020 um
```

DC is included in the forward solve solely to retain the exact Shockley-Ramo consistency diagnostic.

The RF statistical analysis uses

```text
100, 200, 300, 500, 750 MHz,
1.0, 1.5, 2.0, 3.0 GHz.
```

The corrected run gives

```text
collection fraction = 1.0
DC Ramo error        = 1.11e-16
```

so the forward-model consistency check is at numerical roundoff.

---

## 4. Statistical test

For a band containing `N` complex RF roots, the wrong homogeneous no-recombination model jointly fits

```math
D,w>0
```

under the propagated root covariance.

The real data dimension is `2N`, so after fitting two real material parameters,

```math
\nu=2N-2.
```

The rejection design uses

```text
false-rejection probability alpha = 0.0027
desired power                  = 0.90
```

and solves the corresponding noncentral chi-square requirement exactly.

If `Lambda_1` is the profiled nuisance noncentrality at RMS-channel SNR `S=1`, then

```math
\Lambda(S)=S^2\Lambda_1
```

and

```math
\boxed{
S_{\rm req}
=\sqrt{\Lambda_{\rm req}/\Lambda_1}.
}
```

---

## 5. Reproducibility

Script:

```text
experiments/01-vanishing-absorber/numerics/paper02_end_to_end_rejection_snr.py
```

Corrected GitHub Actions run:

```text
run id       31918459502
artifact     paper02-end-to-end-rejection-snr
artifact id  9255619382
sha256       4cce83783b43cd7efc24dfcfb9624cf44fd3a5a3971542b3ae6dd235146094f6
```

An earlier run `31918362835` produced the same statistical values but omitted DC from the forward frequency array, making its reported `dc_ramo_error` diagnostic meaningless. No statistical quantity depended on that diagnostic. The corrected run above supersedes it.

---

## 6. Required channel SNR versus RF bandwidth

The wrong homogeneous model is independently re-fit over every cumulative band beginning at 100 MHz.

| Maximum RF | Complex frequencies | Best-fit `D` [m^2/s] | Best-fit `w` [m/s] | Required RMS-channel SNR | SNR [dB] |
|---:|---:|---:|---:|---:|---:|
| 200 MHz | 2 | 2.6063e-3 | 2.5707e4 | 4.391e6 | 132.85 |
| 300 MHz | 3 | 2.5954e-3 | 2.5715e4 | 1.230e6 | 121.80 |
| 500 MHz | 4 | 2.5558e-3 | 2.5743e4 | 2.470e5 | 107.86 |
| 750 MHz | 5 | 2.4821e-3 | 2.5795e4 | 7.564e4 | 97.58 |
| 1.0 GHz | 6 | 2.3872e-3 | 2.5863e4 | 3.307e4 | 90.39 |
| 1.5 GHz | 7 | 2.1177e-3 | 2.6041e4 | 9.911e3 | 79.92 |
| 2.0 GHz | 8 | 1.7933e-3 | 2.6270e4 | 4.582e3 | 73.22 |
| 3.0 GHz | 9 | 1.0288e-3 | 2.6752e4 | 1.626e3 | 64.22 |

These SNR values are referenced to the RMS **full channel response**, according to the explicit definition above. They are high because the transport root is extracted from subtle differential structure among six large complex channel signals after offset/amplitude freedom is profiled out.

---

## 7. Approximate phase-scale interpretation

For orientation only, an SNR `S` corresponds to an approximate small-angle per-quadrature phase scale

```math
\sigma_\phi\sim1/S
```

radians when amplitude and phase are locally well behaved.

The corresponding rough scales are

| Maximum RF | Required SNR | `1/S` phase scale |
|---:|---:|---:|
| 1.0 GHz | 3.307e4 | 0.00173 deg |
| 1.5 GHz | 9.911e3 | 0.00578 deg |
| 2.0 GHz | 4.582e3 | 0.0125 deg |
| 3.0 GHz | 1.626e3 | 0.0352 deg |

These are **not** direct instrument requirements because the actual experiment will have unequal channel amplitudes, frequency-dependent noise, correlations, calibration uncertainty, and potentially different optimal weighting.

---

## 8. Central result: bandwidth dominates discrimination

The required channel SNR falls from

```text
132.9 dB through 200 MHz
```

to

```text
90.4 dB through 1 GHz
64.2 dB through 3 GHz.
```

Thus, for the current nuisance alternative, extending usable RF bandwidth is far more effective than attempting extreme precision over only the low-frequency regime where the heterogeneous response is tangent to the homogeneous model through quadratic order.

This is the quantitative counterpart of the low-frequency equivalence theorem.

---

## 9. The wrong model continuously re-optimizes

An important feature is that the best-fit homogeneous diffusion coefficient is not constant as the bandwidth grows:

```text
through 200 MHz   D_fit = 2.606e-3 m^2/s
through 500 MHz   D_fit = 2.556e-3 m^2/s
through 1 GHz     D_fit = 2.387e-3 m^2/s
through 2 GHz     D_fit = 1.793e-3 m^2/s
through 3 GHz     D_fit = 1.029e-3 m^2/s
```

The nuisance does not abruptly fail at a particular RF point. Instead, the wrong homogeneous model progressively sacrifices parameter consistency to remain near the data.

This is why the correct rejection statistic is the **profiled covariance-weighted distance to the entire homogeneous model manifold**, not the residual relative to parameters fixed at one identification frequency.

---

## 10. Comparison with the fixed-100-MHz law residual

The earlier fixed-parameter calculation found a normalized homogeneous-law mismatch of approximately

```text
0.22% at 500 MHz
0.89% at 1 GHz
1.92% at 1.5 GHz
3.23% at 2 GHz
6.35% at 3 GHz.
```

Those numbers correctly show that the nuisance departs increasingly from the 100-MHz-identified homogeneous law.

However, they overstate practical discrimination if interpreted as direct required measurement precision because the homogeneous parameters should be allowed to re-fit and because root uncertainty is strongly amplified by the six-channel inverse.

The end-to-end SNR calculation incorporates both effects.

---

## 11. Experimental design implication

For this theoretical nuisance model, a spectral-depth RF experiment intended to distinguish microscopic diffusion from deterministic electrostatic/velocity heterogeneity should prioritize:

1. **usable RF bandwidth** extending into the regime where cubic/higher dispersion becomes appreciable;
2. channel selection and optical kernels that improve the profiled root sensitivity `||h_perp||`;
3. covariance-aware joint fitting rather than pointwise parameter extraction;
4. independent constraints on electrostatic nuisance regions so the systematic bias bound can be tightened before RF rejection is invoked.

The result also suggests a nontrivial optimization problem: the best wavelength/RF design should maximize both material-parameter Fisher information and nuisance-model normal distance.

---

## 12. Status of the statistical gate

**Gate C is now checked under one explicit theoretical noise model.**

What is not yet established:

- actual achievable SNR/phase precision in a specific experimental platform;
- effects of correlated calibration errors;
- frequency-dependent electronics noise and parasitics;
- optimal nonuniform allocation of measurement time across channels/frequencies;
- discrimination against a fully parameterized nuisance family rather than the present fixed depletion alternative.

Those are refinements, not prerequisites for the current theoretical identifiability result.

The remaining publication gates are now dominated by

1. exact closest-prior-art comparison;
2. realistic parameter-scale validation using independent published device/material data.
