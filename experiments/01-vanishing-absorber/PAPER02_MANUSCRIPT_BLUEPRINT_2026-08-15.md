# Paper 02 — Manuscript Blueprint

**Date:** 2026-08-15  
**Status:** **BLUEPRINT / DISTINCT COMBINATION SUPPORTED BY FOCUSED AUDIT / NO SUPERLATIVE PRIORITY CLAIM**

## 1. Working paper identity

### Preferred title

**Electrostatic heterogeneity as apparent diffusion in wavelength-resolved photodetector transport**

This is direct, describes the inverse failure, and does not claim chronological priority.

### Strong alternate

**When finite generation depth makes deterministic photodetector transport look diffusive**

More accessible but slightly less formal.

### More technical alternate

**Finite-kernel aliasing of deterministic velocity gradients into homogeneous diffusion in photodetector transport inversion**

Most exact, but probably too dense for the title.

### Recommended venue class

Best initial fit appears to be an applied-physics/detector journal rather than a broad foundational physics journal.

Possible targets after full manuscript assessment:

```text
Physical Review Applied
Applied Physics Letters / APL Photonics
Optics Express
Journal of Applied Physics
```

The final choice should depend on how much of the manuscript is theorem/identifiability versus photodiode-specific modeling.

---

## 2. Central question

The paper should answer one question:

> **Can a wavelength-resolved photodetector measurement return an apparently physical diffusion coefficient even when microscopic diffusion is zero, and if so, what optical/electrical information is required to prevent that false attribution?**

Everything that does not help answer that question should be moved to supplementary material or omitted.

This paper is **not** a general review of spectral-depth transport, not a second exposition of the full Rev. 9 hierarchy, and not a paper about finite-electrode geometry.

---

## 3. Main paper claim

The main result should be stated narrowly:

> Finite calibrated generation-depth distributions can couple deterministic spatial velocity heterogeneity into a wavelength-resolved Shockley-Ramo terminal-current response that is locally consistent with positive homogeneous diffusion even when microscopic diffusion is zero. The alias is controlled by generation-kernel support in the heterogeneous region and by inverse conditioning, rather than by nominal mean generation depth alone. Additional RF frequencies reject the wrong homogeneous model only when the covariance-weighted departure from its dispersion manifold becomes statistically resolvable.

This statement is fully supported by the current theorem/numerical stack and does not depend on claiming any ingredient as first.

---

## 4. Three main results

The paper should be organized around three results, not around the chronological research path.

### Result I — False diffusion from deterministic heterogeneous transport

Show a zero-microscopic-diffusion deterministic device whose calibrated spectral inverse returns

```math
D_{\rm eff}>0.
```

Use the simplest independent one-dimensional prescribed-velocity model as the conceptual demonstration, not the original 2-D geometry sweep.

Core equation:

```math
\frac{dH}{dz}
=-\frac1L+\frac{i\omega}{v(z)}H,
\qquad H(L)=0.
```

Measured channel:

```math
J_m(\omega)=\int g_m(z)H(z,\omega)dz.
```

Then recover one-mode `gamma(omega)` using the exact calibrated kernels and fit

```math
D\gamma^2+w\gamma=-i\omega.
```

Key sign demonstration:

```text
uniform v(z)        -> D_eff ~= 0
accelerating v(z)   -> D_eff > 0
decelerating v(z)   -> D_eff < 0
```

This establishes that the sign is physical/model-structural rather than numerical noise.

### Result II — The alias is caused by remote kernel support, not mean depth

Introduce nuisance region `R` and exact leakage

```math
\boxed{
E_m=\int_Rg_m(z)\delta H(z)dz.
}
```

Then establish zero-overlap invariance:

```math
\boxed{
p_{m,R}=0\ \forall m\Rightarrow E_m=0.}
```

Show the controlled numerical hierarchy:

```text
point sources at 2.0--4.5 um, all outside R:
D_eff = 1.7e-12 m^2/s ~ 0

physical finite kernels with same nominal means:
D_eff = 2.61e-3 m^2/s

zero-overlap kernels with every original mean preserved:
D_eff = -7.7e-8 m^2/s ~ 0
```

This is likely the most visually convincing causal result in the paper.

Then show physical remote overlaps:

```text
0.60%, 1.65%, 4.20%, 9.78%, 20.60%, 38.89%.
```

The central conceptual sentence:

> Mean generation depth is not a sufficient optical coordinate for material attribution when a finite kernel overlaps a spatially localized device-level nuisance.

### Result III — Quantitative attribution and falsification criteria

First-order root bias:

```math
\boxed{
\delta r
=
\frac{h_\perp^\dagger W E}
{h_\perp^\dagger W h_\perp}.
}
```

Remote-region bound:

```math
\boxed{
|\delta r|
\le
H_R
\frac{(\sum_mw_mp_{m,R}^2)^{1/2}}
{\|h_\perp\|_W}.
}
```

Near-pure-drift diffusion susceptibility:

```math
\boxed{
D_{\rm app}
\simeq
\frac{w^3}{\omega^2}\Re\gamma.
}
```

Validate the linearized bias law against the nonlinear inverse.

Then formulate multi-RF rejection:

```math
\boxed{
T=\min_p(x-m(p))^TC_\gamma^{-1}(x-m(p)),
}
```

with noncentrality

```math
\boxed{
\Lambda=d^TQ_\perp d.
}
```

Use the end-to-end theoretical noise example to show the bandwidth dependence of practical discrimination.

---

## 5. Recommended manuscript structure

### I. Introduction

Approximately 1.5–2 pages.

Narrative:

1. photodiode temporal response depends on where carriers are generated and how they travel to the contacts;
2. wavelength-dependent absorption depth therefore produces wavelength-dependent RF response — explicitly acknowledge OED and high-speed/PDA literature;
3. spectral-depth measurements can in principle use this dependence to probe transport;
4. material attribution becomes nontrivial when finite optical kernels overlap device-level regions with different electric field/velocity;
5. existing work establishes the forward physics and broad risks from nonuniform fields, but the present question is whether the wrong homogeneous model can remain statistically credible while returning a false diffusion coefficient;
6. state the contribution without `first` language.

Suggested final introduction paragraph:

```text
Here we study this attribution problem in a deliberately controlled setting. We construct deterministic zero-diffusion photodetector responses with calibrated wavelength-dependent generation kernels, invert them with a homogeneous drift-diffusion model, and determine when the resulting apparent diffusion is detectable as model error. We derive an exact remote-kernel leakage relation, a local parameter-bias law, and a covariance-aware multi-frequency rejection criterion. Numerical controls isolate generation-kernel support rather than mean depth as the causal optical variable and show that downstream acceleration and deceleration produce opposite signs of the inferred diffusion coefficient. A published-HgCdTe scale comparison is used only to establish that the field and thickness ranges required by the theoretical stress are not obviously artificial.
```

### II. Measurement model and false-attribution problem

Keep the formalism minimal.

Define:

- point-source terminal response `H(z,omega)`;
- calibrated optical kernels `g_m(z)`;
- channel measurements `J_m`;
- homogeneous one-mode model;
- homogeneous drift-diffusion root law.

State clearly:

```text
forward truth used for the counterexample:
D_micro = 0, kappa = 0, deterministic v(z)

inverse model:
homogeneous D,w model
```

This distinction must never be ambiguous.

### III. Deterministic heterogeneity produces apparent diffusion

Derive the planar Ramo ODE.

Present independent prescribed velocity families first.

Then derive the local low-frequency theorem:

```math
\delta\gamma
=-ia_1\omega+a_2\omega^2+O(\omega^3)
```

and

```math
D_{\rm eff}=a_2/a_1^3.
```

Follow with the deterministic field-gradient expression

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

Weak-gradient interpretation:

```math
D_{\rm eff}\simeq\frac12(L-z)^2v'(z).
```

Do not oversell this as a new universal transport coefficient. It is an apparent parameter produced by a specified inverse model.

### IV. Finite generation kernels couple remote device regions into the inverse

Introduce exact leakage identity.

Show:

- point-source outside-region control;
- physical finite kernels;
- zero-tail ablation;
- mean-preserving zero-tail ablation;
- continuous tail-weight dependence.

This section supplies causality.

### V. Parameter bias and model rejection

Derive `delta r` after profiling amplitude/offset.

Show numerical validation:

```text
|epsilon|<=0.002:
root prediction error <=2.65e-6 relative
D prediction error <=3.53e-4 relative
```

Then derive RF rejection statistic and show SNR-vs-bandwidth table.

This is the section that converts the work from a cautionary simulation into a reusable inference framework.

### VI. HgCdTe scale example and discussion

Use the existing conditional HgCdTe kernel set and planar-depletion surrogate.

State plainly that it is a scale/stress example, not a calibrated device simulation.

Compare:

```text
Paper-02 L = 7.6 um
published graded-HgCdTe sample ~7.6 um

Paper-02 added field average = 166.7 V/cm
published composition-gradient field ~100--200 V/cm
```

Mention published local fields up to ~2000 V/cm only as an upper context, not as a direct model parameter.

Mention published ~750 MHz graded-HgCdTe response to establish the timescale, while emphasizing that the present six-channel experiment is different.

Then discuss implications:

- kernel support needs to be calibrated relative to junction/depletion/graded regions;
- positive best-fit `D` is not enough for material attribution;
- additional RF information must be judged in covariance-weighted normal distance;
- independent electrostatic characterization may be more valuable than extreme low-RF precision.

### VII. Conclusion

Four concise conclusions:

1. deterministic velocity heterogeneity can produce positive apparent homogeneous diffusion;
2. finite optical support can transmit a remote field gradient into channels whose mean source depths lie outside that region;
3. parameter bias and fit residual are orthogonal projections and need not track one another;
4. bandwidth/covariance determine whether the wrong model can actually be rejected.

No broad novelty or universality language.

---

## 6. Figure plan

Keep the main text to approximately five or six figures.

### Figure 1 — Problem geometry and inverse mismatch

Four-panel conceptual/quantitative figure:

A. planar absorber, six generation kernels, downstream heterogeneous velocity region;
B. representative `v(z)` uniform versus acceleration;
C. calibrated kernel overlap with region `R`;
D. flow diagram:

```text
true D=0 heterogeneous device
-> J_m(omega)
-> homogeneous inverse
-> D_eff > 0
```

No decorative illustration; use actual computed kernels and profiles.

### Figure 2 — Sign-controlled apparent diffusion

Plot `D_eff` versus endpoint velocity ratio for

- linear family;
- exponential family.

Mark `R=1` and `D_eff=0`.

This should show the clean sign reversal:

```text
R<1 -> D_eff<0
R=1 -> 0
R>1 -> D_eff>0.
```

Secondary panel: one-mode fit residual versus `R` to show that substantial parameter bias coexists with tiny residual.

### Figure 3 — Remote kernel-support causality

Best central figure.

A. six physical kernels with shaded depletion/nuisance region;
B. overlap probability `p_m` versus nominal mean depth;
C. `D_eff` versus tail-scale factor;
D. three bars or points:

```text
physical full kernels        +2.61e-3
zero-overlap renormalized    -9.65e-7
zero-overlap mean-preserved  -7.68e-8
```

The mean-preserving ablation should be visually emphasized.

### Figure 4 — Tangent bias versus model residual

For small velocity-gradient `epsilon`:

A. actual versus predicted `delta r`;
B. actual versus predicted `delta D`;
C. tangent and normal nuisance fractions.

Use a unity line and residual inset.

This validates the analytic bias law.

### Figure 5 — Frequency-domain survival and rejection

A. fixed-100-MHz homogeneous-law residual versus frequency;
B. best-fit homogeneous `D` versus maximum fit bandwidth;
C. required RMS-channel SNR versus maximum RF bandwidth.

This figure makes the practical lesson immediate: the wrong model gradually re-optimizes rather than suddenly failing.

### Figure 6 — HgCdTe scale context

Prefer a compact non-decorative scale comparison rather than another full numerical plot.

Options:

- field/thickness parameter-space diagram showing theoretical stress and published graded-HgCdTe ranges;
- or a table-like plot with `L`, internal field, and response bandwidth.

If space is tight, move this to the discussion without a separate figure.

---

## 7. Supplementary material

Move the following out of the main narrative:

1. original finite-contact geometry sweep;
2. contact/depletion factorial decomposition;
3. coarse-to-fine mesh convergence;
4. beam-offset sweep;
5. full kernel-tail scaling table;
6. complete independent velocity-profile tables;
7. numerical details of complex kernel fitting;
8. all GitHub Actions reproduction hashes;
9. derivation details for finite-spacing field-gradient formulas;
10. extended covariance derivation;
11. alternative SNR/power/alpha choices;
12. possible rank-two diagnostics.

The main paper should feel like one argument, not a research log.

---

## 8. Abstract skeleton

Do not finalize wording until the main figures are generated, but the abstract should have this structure:

### Sentence 1 — problem

Wavelength-dependent photogeneration can encode internal carrier transport in a photodetector response, but material-parameter extraction can be contaminated by device-level field heterogeneity sampled by finite generation profiles.

### Sentence 2 — controlled result

We show in deterministic zero-diffusion models that finite calibrated generation-depth kernels overlapping a spatially nonuniform velocity region can yield a positive diffusion coefficient when the resulting Shockley-Ramo response is fit with a homogeneous drift-diffusion model.

### Sentence 3 — causal theorem

The effect vanishes when kernel support in the heterogeneous region is removed, even when every channel's original mean generation depth is preserved, and its first-order root bias is determined by the projection of the channel discrepancy onto the calibrated model tangent.

### Sentence 4 — practical falsification

Low-frequency dispersion can remain close to the wrong homogeneous model through quadratic order, so additional RF frequencies become useful only when their covariance-weighted normal mismatch is statistically resolved.

### Sentence 5 — scale/result

A conditional HgCdTe stress using independently demonstrated thickness and internal-field scales illustrates the size of the effect and the bandwidth/precision tradeoff required for rejection.

### Sentence 6 — implication

The result provides an attribution criterion for separating microscopic diffusion from finite-kernel coupling to deterministic device heterogeneity in wavelength-resolved transport measurements.

---

## 9. Claim discipline inside the manuscript

Use:

```text
we show
we derive
we identify in the present model
we find
our results demonstrate within the stated assumptions
candidate material attribution
```

Avoid:

```text
for the first time
fundamental new mechanism
universal
previously unknown
proves that all...
```

When discussing general inverse theory, distinguish generic mathematics from the detector-specific instantiation.

Example:

```text
The tangent-space decomposition itself is standard local inverse-problem geometry. Its role here is to quantify how a physically specific finite-generation-kernel leakage can bias the photodetector transport root while producing little same-frequency model residual.
```

---

## 10. Target manuscript length

Main text target:

```text
~5000–6500 words
5–6 main figures
~45–65 references
```

Supplement:

```text
full derivations
numerical convergence
secondary geometry cases
reproducibility tables
```

Do not turn the main paper into another 25–30 page theorem compendium unless the selected journal format requires it.

---

## 11. Remaining pre-draft tasks

Before writing polished prose:

1. generate the five central figure datasets from the existing checked scripts in a standardized format;
2. produce publication-quality plots with consistent axes/units;
3. build a reference file containing the exact closest literature;
4. perform the final five exact source questions listed in `PAPER02_PRIORITY_CHECKPOINT_2026-08-15.md` while drafting the introduction/discussion;
5. freeze notation (`r` versus `gamma`, Fourier sign, coordinate orientation) so it never changes between theorem and numerics;
6. decide whether the HgCdTe example remains in the main paper or moves to a dedicated final section.

After those tasks, a full manuscript draft is justified.
