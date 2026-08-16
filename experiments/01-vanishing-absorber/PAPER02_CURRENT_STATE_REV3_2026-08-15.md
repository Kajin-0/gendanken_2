# Paper 02 — Current State Rev. 3

**Date:** 2026-08-15  
**Status:** **MANUSCRIPT DEVELOPMENT AUTHORIZED / DISTINCT COMBINATION SUPPORTED BY FOCUSED AUDIT / NO SUPERLATIVE PRIORITY CLAIM**  
**Supersedes for navigation:** `PAPER02_CURRENT_STATE_REV2_2026-08-15.md`  
**Preservation rule:** older Paper-02 state/result files remain provenance and must not be deleted.

## 1. Canonical paper identity

Working title:

> **Electrostatic heterogeneity as apparent diffusion in wavelength-resolved photodetector transport**

Central question:

> Can a wavelength-resolved photodetector measurement return an apparently physical homogeneous diffusion coefficient even when microscopic diffusion is zero, and what optical/electrical information is required to prevent that false material attribution?

Safe contribution statement:

> We analyze a material-attribution failure mode in wavelength-resolved photodetector transport measurements. Finite calibrated generation-depth kernels can couple spatially remote deterministic velocity heterogeneity into a Shockley-Ramo terminal-current response that is locally consistent with positive homogeneous diffusion even when microscopic diffusion is zero. We derive support- and conditioning-based bias bounds, isolate the mechanism with zero-overlap and mean-preserving controls, and quantify the RF bandwidth/precision required to reject the false homogeneous model.

Do not add `first`, `fundamental`, `universal`, or ingredient-level novelty language.

---

## 2. Scientific status

The Paper-02 research program has passed the following internal gates:

```text
mechanism existence                       PASSED
fine numerical convergence                PASSED
finite-contact versus depletion split     PASSED
exact calibrated-kernel inverse           PASSED
point-source causal control               PASSED
kernel-tail ablation                      PASSED
mean-preserving zero-overlap ablation     PASSED
independent velocity-profile generality   PASSED
analytic tangent/bias theory              PASSED
first-order bias-law numerical validation PASSED
covariance-aware RF rejection criterion   PASSED
end-to-end theoretical SNR example        PASSED
published HgCdTe order-of-magnitude scale PASSED
focused priority audit                    PASSED FOR MANUSCRIPT DEVELOPMENT ONLY
canonical figure/data regeneration        PASSED
```

Submission-level chronological priority is **not** claimed.

The manuscript is justified as a narrow systematic-error / inverse-identifiability theory, not as a newly discovered transport phenomenon.

---

## 3. Core checked numerical counterexample

Conditional planar stress:

```text
absorber thickness             7.6 um
full-width planar contact      yes
bias                           0.30 V
collector-side nonuniform width 3.0 um
space-charge drop              0.05 V
microscopic diffusion          0
recombination                  0
```

Exact calibrated finite-kernel inverse at 100 MHz:

```math
D_{\rm eff}=2.6098\times10^{-3}\ \mathrm{m^2/s},
```

```math
w_{\rm eff}=2.5701\times10^4\ \mathrm{m/s}.
```

The forward trajectory model has `D_micro=0`.

The wrong homogeneous physical law identified at 100 MHz remains within approximately

```text
0.22% at 500 MHz
0.50% at 750 MHz
0.89% at 1 GHz
1.92% at 1.5 GHz
3.23% at 2 GHz
6.35% at 3 GHz.
```

---

## 4. Strongest causal result

The nonuniform region begins at `z=4.6 um`; all six nominal mean source depths are `2.0--4.5 um`.

Ideal point sources at those upstream coordinates give

```math
D_{\rm eff}\simeq1.7\times10^{-12}\ \mathrm{m^2/s}\approx0.
```

Physical finite calibrated kernels with the same nominal means give

```math
D_{\rm eff}=2.6098\times10^{-3}\ \mathrm{m^2/s}.
```

When all kernel support inside the nonuniform region is removed **and every original mean generation depth is restored to numerical precision**, the result collapses to

```math
D_{\rm eff}=-7.68\times10^{-8}\ \mathrm{m^2/s}\approx0.
```

with maximum mean-depth error

```math
9.33\times10^{-15}\ \mu\mathrm m.
```

Therefore the causal optical variable is restricted kernel support/shape relative to the device-level nuisance region, not the nominal mean depth.

Physical remote overlap probabilities are approximately

```text
mean 2.0 um   0.60%
mean 2.5 um   1.65%
mean 3.0 um   4.20%
mean 3.5 um   9.78%
mean 4.0 um  20.60%
mean 4.5 um  38.89%.
```

---

## 5. Generality

With the original Poisson solver and finite-electrode geometry removed entirely, prescribed deterministic planar velocity profiles give

```text
uniform velocity          -> D_eff ~= 0
linear acceleration       -> D_eff > 0
exponential acceleration  -> D_eff > 0
linear deceleration       -> D_eff < 0
exponential deceleration  -> D_eff < 0.
```

Examples:

```text
linear endpoint ratio 2.0       D_eff = +3.296e-3 m^2/s
exponential ratio 2.0           D_eff = +2.687e-3 m^2/s
linear ratio 0.5                D_eff = -2.530e-3 m^2/s
exponential ratio 0.5           D_eff = -3.297e-3 m^2/s
uniform                            D_eff = 2.67e-14 m^2/s.
```

The sign follows the deterministic downstream velocity gradient across independent functional families.

---

## 6. Analytic spine

### Planar deterministic source response

With Fourier convention `e^{-i omega t}`:

```math
\frac{\partial H}{\partial z}
=-\frac1L+\frac{i\omega}{v(z)}H,
\qquad H(L)=0.
```

### Low-frequency effective homogeneous diffusion

If

```math
\delta\gamma
=-ia_1\omega+a_2\omega^2+O(\omega^3),
```

then any `a1,a2>0` admit a homogeneous drift-diffusion model matching through quadratic order:

```math
V_{*,\rm eff}=1/a_1,
\qquad
D_{\rm eff}=a_2/a_1^3.
```

### Local deterministic field-gradient contribution

```math
\boxed{
a_2(z)=
\frac{v'(z)}{v(z)^2}
\left[
\frac{(L-z)^2}{v(z)}-
\int_z^L\frac{L-u}{v(u)}du
\right].
}
```

Weak-gradient point-source limit:

```math
D_{\rm eff}\simeq\frac12(L-z)^2v'(z).
```

### Remote-kernel leakage

For nuisance region `R`:

```math
E_m=\int_Rg_m(z)\delta H(z)dz.
```

Zero support gives exact zero leakage.

### First-order profiled root bias

```math
\delta r
=\frac{h_\perp^\dagger W E}
{h_\perp^\dagger W h_\perp}.
```

Remote-overlap bound:

```math
|\delta r|
\le
H_R\frac{(\sum_mw_mp_{m,R}^2)^{1/2}}
{\|h_\perp\|_W}.
```

Near pure drift:

```math
D_{\rm app}\simeq\frac{w^3}{\omega^2}\Re\gamma.
```

### Statistical RF rejection

```math
T=\min_p(x-m(p))^TC_\gamma^{-1}(x-m(p)),
```

with alternative noncentrality

```math
\Lambda=d^TQ_\perp d.
```

This is the practical distinction between structural overdetermination and statistically useful falsification.

---

## 7. Bias-law validation

At the exact uniform zero-diffusion baseline and 100 MHz, weak independent linear/exponential velocity perturbations give:

For `|epsilon|<=0.002`:

```text
maximum complex root-shift relative error  2.65e-6
maximum propagated D relative error        3.53e-4.
```

For `|epsilon|<=0.01`:

```text
maximum propagated D relative error        1.77e-3.
```

Only about `3.44e-3` of the weak-gradient nuisance-vector amplitude norm lies outside the local one-mode tangent, corresponding to a normal residual energy fraction of order `1.18e-5`.

This quantitatively explains why the material parameter can move while the same-frequency fit remains excellent.

---

## 8. End-to-end statistical design result

Explicit theoretical noise model:

```text
six complex channels per RF
independent equal Gaussian Re/Im quadrature noise
RMS-channel SNR = sqrt(mean |J_m|^2) / sigma_quadrature
same SNR at every included RF
no cross-frequency correlation
alpha = 0.0027
desired rejection power = 0.90.
```

After propagating channel covariance through the kernel-aware root inverse and jointly re-fitting the wrong homogeneous `D,w` model over each cumulative RF band:

```text
through 1.0 GHz   required SNR 3.31e4 = 90.4 dB
through 1.5 GHz   required SNR 9.91e3 = 79.9 dB
through 2.0 GHz   required SNR 4.58e3 = 73.2 dB
through 3.0 GHz   required SNR 1.63e3 = 64.2 dB.
```

The wrong model continuously re-optimizes its apparent diffusion as bandwidth grows:

```text
through 200 MHz  D_fit = 2.606e-3 m^2/s
through 1 GHz    D_fit = 2.387e-3 m^2/s
through 2 GHz    D_fit = 1.793e-3 m^2/s
through 3 GHz    D_fit = 1.029e-3 m^2/s.
```

Bandwidth is therefore a major nuisance-discrimination resource.

---

## 9. Independent HgCdTe scale context

Published graded-HgCdTe work provides independent order-of-magnitude context:

```text
Paper-02 absorber thickness        7.6 um
published graded-HgCdTe sample    ~7.6 um

Paper-02 added average field       166.7 V/cm
published linear graded field      ~100--200 V/cm
published stronger local field     up to ~2000 V/cm

published high-speed graded HgCdTe ~750 MHz response.
```

This does **not** calibrate the counterexample to a real detector. It establishes only that the theoretical thickness, field, and timing scales are not obviously artificial relative to demonstrated HgCdTe structures.

---

## 10. Priority boundary

Broad ingredient novelty is closed by prior art:

- wavelength-dependent absorption depth and RF phase: established OED/photodiode physics;
- absorption/depletion/field coupling: established PIN/PDA physics;
- field inhomogeneity corrupting transport inference: established TOF literature;
- electrostatic assumptions biasing diffusion-related inference: established transport literature;
- electric-field migration inflating apparent diffusion under a simplified inverse: established generically outside photodetectors;
- tangent-space inverse bias and noncentral chi-square statistics: standard mathematical machinery.

The potentially distinct contribution is the integrated detector-specific package:

```text
finite calibrated generation kernels
+ spatially remote deterministic velocity heterogeneity
+ Shockley-Ramo spectral-depth inverse
+ true microscopic D=0 but positive homogeneous D_eff
+ same-frequency one-mode survival
+ finite-band homogeneous-dispersion survival
+ mean-preserving zero-overlap causality
+ sign-sensitive profile-family generality
+ validated support/conditioning parameter-bias law
+ covariance-aware RF rejection requirement.
```

Focused audit supports manuscript development around this combination.

Do not claim chronological first priority unless a later exact-source audit supports it.

---

## 11. Canonical figure/data bundle

Workflow run:

```text
31918929841
```

Artifact:

```text
paper02-canonical-figure-bundle
artifact id 9255770675
SHA-256 30820eb6564a4fdb827bf6350e83ffaf73454fa9bb414e35335cac255a1b8a3e
```

Index:

```text
PAPER02_FIGURE_BUNDLE_INDEX_2026-08-15.md
```

Seven vector-PDF/PNG working panels plus canonical CSV source tables are included.

Manuscript numerical values and captions should be tied to these datasets or directly regenerated source, not copied from prose notes.

---

## 12. Manuscript development rules

Read before drafting:

1. this file;
2. `PAPER02_PRIORITY_CHECKPOINT_2026-08-15.md`;
3. `PAPER02_EXACT_PRIORITY_MATRIX_2026-08-15.md`;
4. `PAPER02_MANUSCRIPT_BLUEPRINT_2026-08-15.md`;
5. `PAPER02_NOTATION_LOCK_2026-08-15.md`;
6. `PAPER02_FIGURE_BUNDLE_INDEX_2026-08-15.md`;
7. theorem/result files only as needed.

Do not organize the manuscript chronologically around the research process.

Main-text spine:

```text
I. Introduction
II. Measurement model and attribution problem
III. Deterministic heterogeneity produces apparent diffusion
IV. Finite kernels couple remote regions into the inverse
V. Parameter bias and statistical model rejection
VI. HgCdTe scale example and discussion
VII. Conclusion
```

Original finite-contact geometry sweeps, convergence tests, and secondary controls belong in supplementary material.

---

## 13. Next step

The next repository artifact should be the **anonymous Paper-02 manuscript source and bibliography**, created under its own preservation/current-pointer protocol.

Paper 01 / Rev. 9 remains untouched.
