# Paper 02 — Current State

**Date:** 2026-08-15  
**Status:** **SERIOUS STANDALONE CANDIDATE — PRIORITY UNPROVEN — NO MANUSCRIPT YET**  
**Canonical role:** read this file before older `PAPER02_*` development notes. Older notes remain provenance and should not be deleted.

## 1. Current scientific question

The original Paper-02 program began as a test of whether multidimensional finite-electrode Shockley-Ramo geometry could imitate a one-dimensional material-transport signature.

That framing has been superseded by a stronger and more general result.

The active question is now:

> **When can finite optical generation-depth distributions alias deterministic device-level velocity/electrostatic heterogeneity into an apparently physical homogeneous diffusion coefficient in wavelength-resolved Shockley-Ramo transport inversion, and what measurements are required to distinguish the alias from microscopic diffusion?**

Finite-contact geometry is retained as one nuisance mechanism, but it is no longer the central mechanism.

---

## 2. Strongest checked result

A deterministic device with

```text
microscopic diffusion D = 0
recombination           = 0
```

can return

```math
D_{\rm eff}>0
```

when wavelength-dependent finite generation kernels overlap a downstream region of nonuniform deterministic carrier velocity and the measured response is inverted with the homogeneous drift-diffusion law.

The false parameter can survive both of the safeguards that matter for the present spectral-depth hierarchy:

1. the exact calibrated finite-kernel one-mode spectral fit;
2. the overdetermined homogeneous RF dispersion-law test over a finite practical bandwidth.

For the original planar depletion stress, the exact calibrated-kernel one-mode fit gives

```math
\boxed{D_{\rm eff}=2.6098\times10^{-3}\ \mathrm{m^2/s}}
```

at the 100 MHz identification point even though the forward trajectory model has `D=0`.

The wrong homogeneous law remains within approximately

```text
0.22% at 500 MHz
0.50% at 750 MHz
0.89% at 1 GHz
1.92% at 1.5 GHz
3.23% at 2 GHz
6.35% at 3 GHz
```

for that conditional parameter point.

This is not a contradiction of homogeneous-model structural identifiability. It is an omitted-nuisance / practical-attribution problem: a different physical system can lie very close to the assumed model manifold over the measured band.

---

## 3. Causal chain now established

The result has survived a sequence of increasingly restrictive controls.

### 3.1 Initial finite-contact geometry stress

A 75%-contact + depletion case produced transport-sized four-color phase shifts while the higher-rank warning could appear only after the reference transport claim became statistically usable at 500 MHz and 1 GHz.

This established a hidden-risk regime but did not identify its cause.

### 3.2 Contact/depletion factorial decomposition

A full-width planar contact with the same depletion perturbation produced an even stronger hidden confound.

Thus finite-electrode weighting-field geometry is **not required**.

### 3.3 Exact calibrated-kernel test

Replacing the approximate equal-source-spacing reduction by the calibrated arbitrary-kernel one-mode fit did not remove the false diffusion.

Uniform planar truth is recovered by the same inverse to relative residual below `8e-9` over 0--3 GHz, so the effect is not an implementation failure of the kernel-aware fit.

### 3.4 Point-source causal control

The collector-side nonuniform region begins at

```math
z_d=4.6\ \mu\mathrm m.
```

Ideal point sources at the six nominal source coordinates

```text
2.0, 2.5, 3.0, 3.5, 4.0, 4.5 um
```

all lie upstream of that region and give

```math
D_{\rm eff}=1.7\times10^{-12}\ \mathrm{m^2/s}\approx0.
```

Point sources inside the nonuniform region give

```math
D_{\rm eff}=4.87\times10^{-3}\ \mathrm{m^2/s}.
```

Therefore the physical finite-kernel false diffusion is not caused by a local velocity gradient at the nominal source centers.

### 3.5 Tail-support ablation

Removing all generation-kernel support inside the nonuniform region collapses the physical-kernel result from

```math
2.61\times10^{-3}
```

to approximately

```math
-9.65\times10^{-7}\ \mathrm{m^2/s}.
```

Restoring the remote tail continuously produces a monotonic recovery of positive `D_eff` over the tested tail-weight range.

### 3.6 Mean-preserving zero-overlap ablation

To eliminate the objection that truncation merely changed the nominal source coordinate, every channel's original mean depth was restored to numerical precision after all nonuniform-region support was removed.

Maximum mean error:

```math
9.33\times10^{-15}\ \mu\mathrm m.
```

The result still collapses to

```math
\boxed{D_{\rm eff}=-7.68\times10^{-8}\ \mathrm{m^2/s}\approx0,}
```

approximately a `3.4e4`-fold reduction in magnitude relative to the physical kernels.

Thus **support relative to the remote electrostatic region, not the mean generation-depth coordinate, is causal in the current stress.**

### 3.7 Independent deterministic velocity families

The Poisson solver and finite-contact geometry were then removed entirely.

The exact one-dimensional planar Shockley-Ramo ODE

```math
\frac{dH}{dz}=-\frac1L+\frac{i\omega}{v(z)}H,
\qquad H(L)=0
```

was solved for prescribed velocity profiles with the same six finite optical kernels.

Two unrelated downstream profile families were tested:

- linear;
- exponential.

The sign-sensitive gate passed exactly:

```text
uniform velocity          -> D_eff ~= 0
all acceleration profiles -> D_eff > 0
all deceleration profiles -> D_eff < 0
```

Examples:

```text
linear endpoint ratio 2.0       D_eff = +3.296e-3 m^2/s
exponential ratio 2.0           D_eff = +2.687e-3 m^2/s
linear ratio 0.5                D_eff = -2.530e-3 m^2/s
exponential ratio 0.5           D_eff = -3.297e-3 m^2/s
uniform                            D_eff = 2.67e-14 m^2/s
```

The positive acceleration cases remain close to the calibrated one-mode spectral manifold and to the wrong homogeneous RF law at 1 GHz.

This establishes generality beyond the original electrostatic discretization.

---

## 4. Theorem stack

The active result is supported by four analytical layers.

### 4.1 Spectral tangent-confound theorem

For rank-one differences

```math
d_m=Aq^m
```

and normalized nuisance `h_m=g_m/d_m`, the first-order closure responds to discrete curvature,

```math
C'_m=-\Delta^2h_m,
```

while the inferred multiplier responds to discrete slope,

```math
R'_m=\Delta h_m.
```

An affine normalized nuisance is tangent to the rank-one manifold and can bias the inferred root with zero first-order closure residual.

### 4.2 Low-frequency effective-diffusion equivalence

For any recovered exponent

```math
\delta\gamma=-ia_1\omega+a_2\omega^2+O(\omega^3)
```

with `a1,a2>0`, the homogeneous drift-diffusion model matches through quadratic order with

```math
V_{*,\rm eff}=1/a_1,
```

```math
\boxed{D_{\rm eff}=a_2/a_1^3.}
```

The first locally non-adjustable coefficient appears at cubic order.

Thus the next-RF test remains structurally valid, but a wrong mechanism can be tangent to the homogeneous dispersion family through `O(omega^2)`.

### 4.3 Deterministic field-gradient theorem

For local point-source probing in a deterministic planar device,

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

Monotonic downstream acceleration gives positive `a2` and therefore positive apparent homogeneous diffusion even though microscopic diffusion is zero.

Weak-gradient limit:

```math
\boxed{D_{\rm eff}\simeq\frac12(L-z)^2v'(z).}
```

### 4.4 Remote-region finite-kernel leakage theorem

For true point response

```math
H(z)=A+Be^{rz}+\delta H(z)
```

with nuisance `delta H` supported only in region `R`, calibrated channel measurements obey

```math
J_m=A+B M_m(r)+E_m,
```

where

```math
\boxed{E_m=\int_Rg_m(z)\delta H(z)dz.}
```

If every generation kernel has zero support in `R`, then `E_m=0` exactly regardless of nuisance complexity inside `R`.

For normalized nonnegative kernels,

```math
|E_m|\le p_{m,R}\|\delta H\|_{\infty,R},
```

with

```math
p_{m,R}=\int_Rg_m(z)dz.
```

The tangent component of the leakage vector biases fitted transport parameters; the normal component drives model-rejection residual.

---

## 5. Physical kernel overlap in the current HgCdTe stress

Although all nominal source means are upstream of the nonuniform region, the calibrated kernels have depletion-region probabilities approximately

```text
mean depth     remote overlap
2.0 um          0.60%
2.5 um          1.65%
3.0 um          4.20%
3.5 um          9.78%
4.0 um         20.60%
4.5 um         38.89%
```

The overlap changes by almost two orders of magnitude across the sequence.

This is why mean source depth is not a sufficient optical coordinate for material-parameter attribution.

---

## 6. Current novelty boundary

### Established prior-art territory — do not claim

The following broad ideas are already established in semiconductor/photodiode literature:

1. nonuniform electric fields can corrupt time-of-flight transport inference;
2. space-charge assumptions can bias inferred transport quantities such as diffusion length;
3. planar terminal-current transients contain electrode/displacement-current and internal-space-charge effects;
4. wavelength-dependent absorption depth changes photodiode transit/diffusion response and bandwidth;
5. partially depleted absorber photodiodes require coupled optical-generation/electric-field transport modeling;
6. photodiode optoelectronic chromatic dispersion uses wavelength-dependent internal carrier transport to produce measurable RF phase signatures and has already been used for wavelength monitoring/spectroscopy.

### Candidate distinct contribution — priority still unproven

The current candidate is much narrower:

> **A calibrated spectral-depth inverse can return a positive, apparently physical homogeneous diffusion coefficient from a zero-diffusion deterministic velocity gradient because finite optical generation kernels overlap a remote nonuniform-transport region; the alias can remain close to both the same-frequency one-mode spectral manifold and the low-frequency homogeneous drift-diffusion dispersion manifold.**

The supporting package includes:

- exact source-coordinate/tangent analysis;
- low-frequency two-coefficient equivalence;
- zero-overlap theorem;
- point-source control;
- direct tail ablation;
- mean-preserving tail ablation;
- independent profile-family sign reversal;
- explicit finite-band physical-law residuals.

No direct collision with this full inverse-identifiability statement has yet been located in the targeted audit.

**That is not novelty evidence. Priority remains OPEN until the closest full texts are compared claim-by-claim.**

---

## 7. Closest literature that must be treated as boundary conditions

At minimum, the eventual claim ledger must explicitly compare against:

- E. V. Emelianova, V. I. Arkhipov, and G. J. Adriaenssens, “Time-of-flight measurements in inhomogeneous electric fields,” *Journal of Non-Crystalline Solids* 352, 1122–1125 (2006), DOI: 10.1016/j.jnoncrysol.2005.12.045.
- K. Hattori, H. Okamoto, and Y. Hamakawa, “Theory of the steady-state-photocarrier-grating technique for obtaining accurate diffusion-length measurements in amorphous silicon,” *Physical Review B* 45, 1126 (1992), DOI: 10.1103/PhysRevB.45.1126.
- S. A. Hawks, B. Y. Finck, and B. J. Schwartz, “Theory of Current Transients in Planar Semiconductor Devices: Insights and Applications to Organic Solar Cells,” *Physical Review Applied* 3, 044014 (2015), DOI: 10.1103/PhysRevApplied.3.044014.
- Y. Hu et al., “Simulation of a partially depleted absorber (PDA) photodetector,” *Optics Express* 23, 20402–20417 (2015), DOI: 10.1364/OE.23.020402.
- “Transient response of high-speed p-i-n photodiodes including diffusion effects,” *Solid-State Electronics* 37, 1841–1847 (1994), DOI: 10.1016/0038-1101(94)90175-9.
- E. Liokumovitch, Z. Glasser, and S. Sternklar, “Optoelectronic chromatic dispersion in germanium PN photodiodes: wavelength monitoring and FBG interrogation,” *Optics Letters* 46, 4061–4064 (2021).
- E. Liokumovitch, Z. Glasser, and S. Sternklar, “Femtometer-resolved wavelength monitor based on photodiode optoelectronic chromatic dispersion with RF phase-shift amplification,” *Optics Letters* 47, 2622–2625 (2022), DOI: 10.1364/OL.462018.
- S. Mudgal et al., “Large optoelectronic chromatic dispersion in PN-type silicon photodiodes and photovoltaic cells,” *Optics Letters* 49, 2185–2188 (2024), DOI: 10.1364/OL.514906.
- A. Dutta et al., “Large and tunable optoelectronic chromatic dispersion in PIN-type photodiodes,” *Optics Letters* 49, 2057–2060 (2024), DOI: 10.1364/OL.519164.
- E. E. Kassa et al., “Optoelectronic Chromatic Dispersion in a Single Photodiode for Machine-Learning-Based Computational Spectroscopy,” arXiv:2605.18014 (2026).

The OED lineage is particularly important because it already treats wavelength-dependent photodiode RF phase as useful information rather than a nuisance.

---

## 8. Reproducible numerical record

Key GitHub Actions artifacts:

```text
quick geometry sweep
run 31916800184
artifact 9255131125

fine geometry sweep
run 31916853136
artifact 9255160359

contact/depletion factorial
run 31917052026
artifact 9255227347

simple-root dense frequency law
run 31917263235
artifact 9255275424

kernel-aware dense frequency law
run 31917357402
artifact 9255304855

point-source vs finite-kernel causal test
run 31917583825
artifact 9255370581

kernel-tail ablation
run 31917697296
artifact 9255419176

mean-preserving tail ablation
run 31917802506
artifact 9255439098

independent prescribed-velocity profiles
run 31917901867
artifact 9255463448
```

The scripts and workflows that produced these outputs are retained on the Paper-02 branch.

---

## 9. Relation to Paper 01 / Rev. 9

No canonical Rev. 9 manuscript source has been modified by this program.

The present result does **not** make the Rev. 9 homogeneous algebra wrong.

It does show that a later RF point is a structural falsification measurement only relative to the assumed model family; practical rejection of an omitted deterministic nuisance depends on frequency, precision, kernel overlap, and inverse conditioning.

This is sufficiently consequential that, if Paper 02 survives the priority audit, Paper 01 should eventually receive a carefully bounded adversarial qualification or cross-reference. That integration must occur only through the manuscript-preservation protocol after the current Paper-02 claim is stable.

---

## 10. Remaining gates before manuscript drafting

### Gate A — exact closest-prior-art comparison

Read the closest OED, PDA, TOF-field-inhomogeneity, and transient-current papers in full where accessible. Compare exact observables, inferred parameters, nuisance structure, and identifiability claims.

### Gate B — first-order parameter-bias law

Go beyond the channel leakage bound and derive the noise-weighted transport-parameter bias

```math
\delta\theta=(\mathcal J^\dagger W\mathcal J)^{-1}\mathcal J^\dagger W\mathbf E,
```

then propagate to `delta D`.

The desired result is a bound/design law in terms of restricted kernel overlap, nuisance-response magnitude, and inverse conditioning.

### Gate C — rejection precision / bandwidth

Translate the higher-order RF-law mismatch into the complex-response precision and bandwidth required to reject the wrong homogeneous model at a stated significance.

### Gate D — realistic scale without new experiments

Use independently published device/material parameters or a clearly labeled theoretical parameter envelope. No new physical experiment is required or assumed.

---

## 11. Manuscript decision rule

Do **not** draft a standalone manuscript merely because the numerical effect is strong.

Proceed to a Paper-02 manuscript only if:

1. the exact inverse-identifiability claim survives the focused priority audit;
2. the parameter-bias/bound formalism becomes sufficiently compact to provide a reusable design rule;
3. the required RF precision/bandwidth is quantified;
4. the distinction from existing photodiode OED and partial-depletion response literature is explicit.

At the present checkpoint, the branch has moved from **possible paper** to **serious standalone paper candidate**, but publication priority remains deliberately unclaimed.
