# Paper 02 — Current State Rev. 2

**Date:** 2026-08-15  
**Status:** **SERIOUS STANDALONE THEORY CANDIDATE — PRIORITY UNPROVEN — NO MANUSCRIPT YET**  
**Supersedes for navigation:** `PAPER02_CURRENT_STATE_2026-08-15.md`  
**Preservation rule:** older Paper-02 notes remain provenance and must not be deleted.

## 1. One-sentence result

Finite calibrated optical generation-depth kernels can sample a spatially remote deterministic velocity/electrostatic gradient and cause a zero-microscopic-diffusion photodetector to be inverted as having a positive, apparently admissible homogeneous diffusion coefficient while remaining close to both the calibrated same-frequency one-mode spectral manifold and the low-RF homogeneous drift-diffusion dispersion manifold.

The effect is controlled by **kernel support relative to the nuisance region**, not by nominal mean generation depth alone.

---

## 2. What is now established inside the conditional theoretical program

### A. False positive diffusion exists

For the fine planar-depletion stress:

```text
microscopic D             0
recombination             0
full-width planar contact yes
bias                      0.30 V
depletion width            3.0 um
space-charge drop          0.05 V
```

an exact calibrated finite-kernel one-mode inverse at 100 MHz gives

```math
D_{\rm eff}=2.6098\times10^{-3}\ \mathrm{m^2/s}>0.
```

The same wrong homogeneous law remains within approximately `0.89%` at 1 GHz when parameters are identified at 100 MHz.

### B. Finite-contact geometry is not required

A full-width planar contact already shows the effect. Finite-contact geometry remains a separate nuisance/interaction mechanism but is not the root cause of the strongest result.

### C. The effect is causal to finite-kernel support in the nonuniform region

The collector-side nonuniform region begins at `4.6 um`, whereas the six nominal source means are `2.0--4.5 um`.

Ideal point sources at those same six upstream coordinates give

```math
D_{\rm eff}\simeq1.7\times10^{-12}\ \mathrm{m^2/s}\approx0.
```

Point sources placed inside the gradient region give positive `D_eff`.

Physical finite kernels centered at the upstream means recover the positive false diffusion because their tails overlap the downstream region.

### D. Mean depth is not the causal variable

All support inside the nuisance region was removed and every channel's original mean generation depth was then restored to numerical precision.

Maximum mean error:

```math
9.33\times10^{-15}\ \mu\mathrm m.
```

The result still collapses from

```math
2.6098\times10^{-3}
```

to

```math
-7.68\times10^{-8}\ \mathrm{m^2/s}\approx0.
```

about a `3.4e4`-fold reduction in magnitude.

### E. The mechanism is not specific to the electrostatic solver

With the Poisson solver and finite-electrode geometry removed entirely, independent prescribed one-dimensional velocity profiles satisfy

```text
uniform velocity          -> D_eff ~= 0
linear acceleration       -> D_eff > 0
exponential acceleration  -> D_eff > 0
linear deceleration       -> D_eff < 0
exponential deceleration  -> D_eff < 0
```

with microscopic diffusion fixed to zero throughout.

### F. The parameter-bias law is quantitatively validated

The calibrated-kernel root bias obeys to first order

```math
\delta r
=
\frac{h_\perp^\dagger W E}
{h_\perp^\dagger W h_\perp}.
```

At `|epsilon| <= 0.002` in independent weak velocity-gradient tests:

```text
max complex root-shift relative error = 2.65e-6
max propagated D relative error       = 3.53e-4
```

At `|epsilon| <= 0.01`, the `D` error remains only `1.77e-3`.

Only about `0.34%` of the nuisance-vector amplitude norm lies outside the local calibrated one-mode tangent in the weak-gradient regime, explaining why the fitted parameter can move while the same-frequency residual remains tiny.

### G. A statistical rejection criterion is derived and checked under one explicit noise model

The correct multi-frequency discriminator is the profiled covariance-weighted distance

```math
T=\min_p(x-m(p))^T C_\gamma^{-1}(x-m(p)),
```

with nuisance-alternative noncentrality

```math
\Lambda=d^TQ_\perp d.
```

An end-to-end theoretical noise calculation propagates six-channel complex noise through the calibrated kernel-aware root inverse and then re-fits the wrong homogeneous `D,w` model over every cumulative RF band.

For independent equal real/imaginary channel noise with common RMS-channel SNR, `alpha=0.0027`, and 90% power, the current nuisance alternative requires approximately

```text
through 1.0 GHz    SNR = 3.31e4   = 90.4 dB
through 1.5 GHz    SNR = 9.91e3   = 79.9 dB
through 2.0 GHz    SNR = 4.58e3   = 73.2 dB
through 3.0 GHz    SNR = 1.63e3   = 64.2 dB
```

The corrected statistical run retains the exact DC Ramo check at `1.11e-16`.

Thus **usable RF bandwidth is a primary nuisance-discrimination resource**, not merely a way to collect additional redundant points.

---

## 3. Theorem spine

### 3.1 Spectral tangent-confound theorem

For rank-one differences `d_m=Aq^m`, normalized nuisance `h_m=g_m/d_m` gives

```math
C'_m=-\Delta^2 h_m,
```

while the inferred multiplier responds as

```math
R'_m=\Delta h_m.
```

A nuisance can therefore bias the root without creating a first-order closure residual.

### 3.2 Low-frequency effective-diffusion equivalence

Any recovered exponent

```math
\delta\gamma=-ia_1\omega+a_2\omega^2+O(\omega^3)
```

with `a1,a2>0` admits a locally matching homogeneous drift-diffusion model

```math
V_{*,\rm eff}=1/a_1,
\qquad
D_{\rm eff}=a_2/a_1^3.
```

The first locally non-adjustable frequency coefficient is cubic.

### 3.3 Deterministic field-gradient apparent diffusion

For planar Ramo readout with deterministic `v(z)`, no diffusion, and no recombination,

```math
\frac{\partial H}{\partial z}
=-\frac1L+\frac{i\omega}{v(z)}H.
```

The local quadratic exponent coefficient is

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

Monotonic downstream acceleration gives positive apparent diffusion.

Weak-gradient point-source limit:

```math
D_{\rm eff}\simeq\frac12(L-z)^2v'(z).
```

### 3.4 Remote-region kernel leakage

For nuisance region `R`, calibrated-channel leakage is exactly

```math
E_m=\int_Rg_m(z)\delta H(z)dz.
```

Zero support gives exact invariance:

```math
\operatorname{supp}(g_m)\cap R=\varnothing\ \forall m
\Rightarrow E_m=0.
```

For normalized nonnegative kernels,

```math
|E_m|\le p_{m,R}H_R.
```

### 3.5 Root and material-parameter attribution bound

After profiling offset/amplitude,

```math
|\delta r|
\le
H_R
\frac{(\sum_m w_mp_{m,R}^2)^{1/2}}
{\|h_\perp\|_W}
```

to first order.

Near pure drift,

```math
D_{\rm app}\simeq\frac{w^3}{\omega^2}\Re\gamma,
```

which exposes the strong low-frequency susceptibility of inferred diffusion to a tiny nuisance-induced real spatial exponent.

### 3.6 RF rejection power

Practical model discrimination is controlled by

```math
\Lambda=d^TQ_\perp d,
```

not by raw residual percentage.

This formalizes the distinction between structural overdetermination and statistically useful falsification.

---

## 4. Physical overlap in the current HgCdTe stress

The six physical kernels overlap the collector-side nonuniform region by approximately

```text
nominal mean     overlap
2.0 um           0.60%
2.5 um           1.65%
3.0 um           4.20%
3.5 um           9.78%
4.0 um          20.60%
4.5 um          38.89%
```

The overlap changes by nearly two orders of magnitude while the nominal source means all remain upstream.

---

## 5. Current prior-art boundary

### Established — do not claim

The literature already establishes the broad ingredients:

- nonuniform semiconductor fields can corrupt transit/transport inference;
- space-charge assumptions can bias diffusion-related quantities;
- terminal-current measurements contain device/electrode observation physics;
- partially depleted absorbers require coupled optical/electrical transport models;
- wavelength-dependent absorption depth changes photodiode RF amplitude/phase;
- optoelectronic chromatic dispersion has already been used for wavelength sensing and, by 2026, multi-frequency single-photodiode computational spectroscopy.

### Candidate distinct contribution — still unproven

The possible standalone contribution is the **inverse-attribution failure and its quantitative bounds**:

```text
calibrated finite generation kernels
+ spatially remote deterministic velocity heterogeneity
+ Shockley-Ramo spectral-depth inverse
+ false positive homogeneous D with microscopic D=0
+ survival of calibrated same-frequency one-mode fit
+ finite-band survival of homogeneous RF dispersion
+ mean-preserving zero-overlap causality
+ sign-sensitive independent-profile generality
+ validated tangent-space parameter-bias law
+ covariance-aware RF rejection requirement
```

No direct source matching this entire package has yet been located.

That statement is **not novelty evidence**. Priority remains OPEN until the closest full texts are compared claim-by-claim.

The closest currently identified neighboring lineages are recorded in `PAPER02_PRIOR_ART_BOUNDARY_2026-08-15.md`.

---

## 6. Reproducibility index

Key checked GitHub Actions results:

```text
quick geometry sweep                 run 31916800184
fine geometry sweep                  run 31916853136
contact/depletion factorial          run 31917052026
simple-root dense RF law             run 31917263235
kernel-aware dense RF law            run 31917357402
point-source vs finite-kernel        run 31917583825
kernel-tail ablation                 run 31917697296
mean-preserving tail ablation        run 31917802506
independent velocity profiles        run 31917901867
bias-law linearization               run 31918166467
corrected end-to-end rejection SNR   run 31918459502
```

See the dated result files for artifact IDs, SHA-256 digests, exact assumptions, and numerical tables.

---

## 7. Relation to Paper 01 / Rev. 9

The canonical Rev. 9 manuscript remains untouched.

The current Paper-02 result does not invalidate its exact homogeneous-model algebra or rank hierarchy.

It sharpens the interpretation:

> structural model overdetermination does not guarantee that an omitted physical nuisance will generate a statistically useful normal residual over the experimentally accessible band.

A deterministic nuisance can be tangent in both channel space and low-frequency dispersion space.

If Paper 02 survives the remaining publication gates, Paper 01 should eventually receive a bounded qualification or cross-reference through the manuscript-preservation protocol. Do not edit Paper 01 before the Paper-02 claim boundary is stable.

---

## 8. Remaining gates

The internal theoretical mechanism, causal controls, first-order bias law, and one explicit statistical-design example are now substantially complete.

The remaining high-value work is no longer arbitrary theorem generation.

### Gate A — exact priority

Complete full-text, claim-by-claim comparison against the closest:

- photodiode optoelectronic chromatic-dispersion lineage;
- partially depleted absorber response models;
- inhomogeneous-field TOF analyses;
- transient-current / weighting-field treatments;
- any papers fitting deterministic heterogeneity with effective diffusion.

### Gate B — independent realistic scale

Use published device/material parameters or defensible theoretical parameter envelopes to determine whether the required kernel-overlap/electrostatic-gradient regime is realistic for a plausible photodiode or HgCdTe structure.

No new physical experiment is assumed.

### Gate C — manuscript decision

Only after Gates A and B:

```text
if exact inverse-identifiability claim survives
and realistic magnitude is nontrivial
    -> draft standalone Paper 02
else
    -> retain as a major adversarial/systematic qualification to Paper 01
```

At this checkpoint, the science is strong enough to justify the priority and realistic-scale work, but not a novelty claim or manuscript draft.
