# Published Sample B — RF Phase Precision Required for Spectral Transport Tomography

**Date:** 2026-08-09  
**Status:** deterministic Monte Carlo conditioning study using the literature-constrained 2023 sample-B optical matrix; illustrative transport anomaly; no novelty claim

## 1. Purpose

The dimensional sample-B forward matrix shows that the published `3.7 um` graded HgCdTe structure contains several recoverable smooth spatial modes.

That does not yet say what RF phase precision is needed to use them.

This note asks:

> **For a modest internal transport anomaly, how does wavelength-dependent phase noise limit the number of recoverable transport modes?**

The calculation uses the real Moazzami optical kernels from the sample-B dimensional model but an explicitly illustrative carrier-velocity profile.

---

## 2. Forward operator

For front collection,

```math
\bar T_i
=\int_0^W S_i(s)q(s)ds,
```

where

```math
S_i(s)=P(Z_g\ge s|\lambda_i,{\rm abs}).
```

The dimensional matrix is calculated for the central literature bracket

```math
F_g=150\ {\rm V/cm},
```

with

```text
W = 3.7 um
T = 300 K
nominal x_low = 0.316
Moazzami above-gap alpha(lambda,x,T)
Pabs >= 0.05.
```

This retains `110` wavelengths from approximately

```text
2.80 to 3.89 um.
```

---

## 3. Remove the common-phase mode

The wavelength-independent delay is not structurally identifiable from arbitrary boundary-localized transport.

Therefore the phase-noise test first projects out the wavelength-independent timing mode:

```math
\boxed{
\mathbf A_\Delta
=\mathbf A
-\mathbf1\,\overline{\mathbf A}.
}
```

At RF frequency `f`, if `q` is expressed in `ps/um`, the differential phase operator is

```math
\boxed{
\boldsymbol\phi_\Delta
=-360f\times10^{-12}
\,\mathbf A_\Delta\mathbf q
}
```

in degrees.

At

```math
f=1\ {\rm GHz},
```

one picosecond of differential delay gives

```math
0.36^\circ
```

of phase.

---

## 4. Synthetic transport defect

Use only as a transparent stress test a baseline

```math
v_0=10^5\ {\rm m/s}
```

with a smooth local slowdown

```math
\boxed{
v(z)
=v_0
\left[
1-0.25
\exp\!\left(
-\frac{(z-2.30\ {\rm um})^2}
{2(0.35\ {\rm um})^2}
\right)
\right].
}
```

Thus the imposed anomaly is

```text
25% peak slowdown
center = 2.30 um
Gaussian sigma = 0.35 um.
```

This is not a model of an actual defect in sample B.

It is a known target used to ask whether the optical/phase measurement can localize smooth internal transport structure.

---

## 5. Phase signal size

For this synthetic anomaly, the wavelength-dependent differential phase at `1 GHz` has peak-to-peak amplitude

```math
\boxed{
\Delta\phi_{\rm pp}
\approx0.935^\circ.
}
```

This is substantially smaller than the approximately `10 degree` total phase span produced by the full wavelength-induced mean-depth scan for a constant `10^5 m/s` transport scale.

The reason is important:

```text
full phase span
-> mostly gross generation-depth shift

anomaly phase
-> small residual spatial structure after the smooth baseline is removed.
```

Tomography therefore requires substantially better phase precision than merely detecting wavelength-dependent transit delay.

---

## 6. Truncated spatial modes

Use a truncated singular-value reconstruction after projecting out common phase.

### First three modes

The noiseless three-mode projection of the imposed anomaly has

```text
peak position ≈ 2.336 um
peak amplitude ≈ 66% of true anomaly
full-profile truncation error ≈ 40%.
```

The location is recovered well, but the shape and amplitude are strongly smoothed by the optical kernel.

### First five modes

The noiseless five-mode projection gives

```text
peak position ≈ 2.336 um
peak amplitude ≈ 86% of true anomaly
full-profile truncation error ≈ 17%.
```

Thus the fifth mode contains useful submicron shape information, but its singular value is much smaller and it is correspondingly noise sensitive.

---

## 7. Monte Carlo phase-noise result

For each phase-noise level, `1000` independent Gaussian phase-noise realizations were generated and the common phase was removed.

### Rank-3 reconstruction

| per-wavelength phase noise | median noise error vs rank-3 recoverable target | median full-profile error | 90% peak-location error |
|---:|---:|---:|---:|
| 0.03 deg | 0.050 | 0.404 | 0.036 um |
| 0.05 deg | 0.089 | 0.410 | 0.082 um |
| 0.10 deg | 0.175 | 0.432 | 0.128 um |
| 0.25 deg | 0.420 | 0.556 | 0.729 um |

At `0.1 degree`, the **coarse three-mode anomaly** remains identifiable and localized, although the optical truncation already prevents accurate recovery of the full narrow profile.

At `0.25 degree`, localization becomes unreliable for this specific anomaly.

### Rank-5 reconstruction

| per-wavelength phase noise | median noise error vs rank-5 recoverable target | median full-profile error | 90% peak-location error |
|---:|---:|---:|---:|
| 0.03 deg | 0.255 | 0.305 | 0.174 um |
| 0.05 deg | 0.432 | 0.459 | 0.452 um |
| 0.10 deg | 0.910 | 0.913 | 0.591 um |
| 0.25 deg | 2.187 | 2.160 | 1.099 um |

Five-mode reconstruction requires substantially better phase precision.

For this anomaly, even `0.03 degree` noise materially affects the fifth mode.

---

## 8. Main experimental implication

The published optical structure may support roughly five strongly conditioned modes in a noiseless singular-value sense, but that does **not** mean five modes are experimentally accessible.

The usable rank is set by both

```text
optical singular spectrum
+
phase-noise floor.
```

For the present illustrative anomaly:

```math
\boxed{
\text{3 coarse modes}
\quad\text{are plausible near}\quad
\sigma_\phi\sim0.1^\circ
}
```

at `1 GHz`, whereas

```math
\boxed{
\text{5 modes require phase precision well below }0.1^\circ.
}
```

This is not an instrument specification.

The requirement scales with anomaly strength, RF frequency, wavelength count, optical power/SNR, and the validity range of the low-frequency phase expansion.

---

## 9. Frequency scaling

For the same mean-delay anomaly,

```math
\Delta\phi
\propto f.
```

Therefore increasing usable modulation frequency improves phase leverage linearly.

However, the low-frequency cumulant approximation requires the timing distribution to remain sufficiently unresolved:

```math
\Omega\sigma_T\ll1.
```

At higher frequency, the correct strategy is not to keep applying the linear phase formula indefinitely.

Instead fit the full complex transfer function.

Thus the likely best experiment is a **multi-frequency complex-response fit**, not a single-frequency phase measurement.

---

## 10. What the phase-noise study changes

The project should no longer describe the goal as a pointwise velocity reconstruction.

For a few-micron published graded layer, the more credible target is

> **recover a small number of smooth internal transport modes and test whether a slow/broadening region is present and where it lies.**

That is both better conditioned and closer to what the optical physics actually supports.

---

## 11. Claim boundary

### CHECKED NUMERICALLY / CONDITIONAL

For the stated 2023 sample-B optical envelope and the stated synthetic anomaly:

- anomaly differential phase is approximately `0.94 degree peak-to-peak` at `1 GHz`;
- three-mode localization remains useful around `0.1 degree` phase noise;
- five-mode reconstruction becomes noise dominated well before `0.1 degree` for this anomaly.

### NOT A DEVICE CLAIM

The calculation does not establish

- actual sample-B carrier velocity;
- actual internal transport defects;
- achievable experimental phase precision;
- exact phase-noise independence across wavelength;
- calibrated reconstruction performance.

### OPEN

Need an experimentally realistic covariance model including

```text
wavelength-dependent optical power
phase-reference drift
source tuning repeatability
readout SNR
frequency correlation
uncertainty in x(z) and alpha.
```

---

## 12. Next decisive work

The theoretical inverse is now sufficiently constrained.

The highest-value next steps are

1. recover the actual sample-B `x(z)` fit parameters or digitized profile;
2. determine whether a tunable MWIR source plus VNA/LCA-type measurement can deliver the required **differential phase covariance**;
3. fit multiple RF frequencies simultaneously rather than relying on one phase point;
4. compare the spectral inverse against an independent spatially localized timing measurement or calibrated drift-diffusion/Monte-Carlo calculation.

Further generic inverse algebra has lower value than these experimental collisions.

---

## 13. Reproducibility

Deterministic Monte Carlo regression:

`numerics/hgcdte_published_sample_b_phase_noise.py`
