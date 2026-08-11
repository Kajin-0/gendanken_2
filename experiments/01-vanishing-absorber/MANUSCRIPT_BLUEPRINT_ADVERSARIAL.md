# Manuscript Blueprint — Spectral-Depth Closure Tests for Photocarrier Transport

**Date:** 2026-08-10  
**Status:** planning document after adversarial theory consolidation; **not a manuscript and not a novelty claim**

## 1. Provisional title

### Preferred

**Spectral-depth closure tests for falsifying photocarrier transport from Shockley-Ramo current**

### Alternatives

- **Using wavelength as an internal coordinate for falsifiable photocarrier transport measurements**
- **Four-color and six-color closure tests for photodiode carrier transport**
- **Spectral spatial system identification of photocarrier transport**

Avoid titles that claim

```text
tomography,
first-ever internal imaging,
universal transport theory,
or direct velocity mapping
```

until priority and experimental observability are stronger.

---

# 2. One-sentence thesis

> **If wavelength can be calibrated to move the photocarrier generation distribution through a detector, then spatial finite differences of the complex Shockley-Ramo current isolate a small number of internal propagation modes whose color-count and RF-frequency closure relations can falsify homogeneous drift-diffusion, boundaries, and conventional two-carrier explanations before a flexible transport model is fitted.**

This is the paper.

Everything else must support this sentence or move to an appendix/future paper.

---

# 3. The three gedanken experiments

## Gedanken I — four colors, one RF

Draw the simplest planar detector.

```text
collector                                             optical coordinate
|---------------------------------------------------------------|
          z0       z1       z2       z3
          *--------*--------*--------*
```

The stars are **mean generation coordinates**, not physical laser spots.

Four wavelengths are chosen so

```math
z_m=z_0+mh.
```

Measure the raw complex modulated terminal current per calibrated generated-carrier amplitude

```math
J_m(\omega).
```

For one homogeneous planar signal-carrier mode,

```math
\boxed{
(J_2-J_1)^2
=(J_1-J_0)(J_3-J_2).
}
```

The first three points identify

```math
q_s=\frac{J_2-J_1}{J_1-J_0},
```

and the fourth tries to falsify the model.

Then

```math
\gamma=-\frac1h\log q_s.
```

### Conceptual question

> **Does one homogeneous spatial propagation mode survive the four-color test?**

---

## Gedanken II — repeat at one more RF frequency

For homogeneous real drift-diffusion with uniform recombination,

```math
D\gamma^2+w\gamma=\kappa+i\omega.
```

Use four colors at DC to obtain

```math
\gamma_0.
```

Use the same four colors at one nonzero RF to obtain

```math
\gamma_\omega.
```

DC + one RF then determine

```math
D,
\qquad
w,
\qquad
\kappa
```

algebraically.

A second RF frequency adds **zero transport parameters**.

### Conceptual question

> **Do the same real diffusion, drift, and recombination coefficients survive when the clock frequency changes?**

This should be presented as

```text
one frequency identifies;
the next frequency tries to kill the theory.
```

---

## Gedanken III — if four colors fail, use six

A conventional boundary or a conventional second carrier can invalidate the one-mode theorem.

Do not call this anomalous transport.

Use six source coordinates.

Five first differences are tested for rank two.

Define

```math
W_m
=d_md_{m+2}-d_{m+1}^2.
```

For two modes

```math
\boxed{
W_m
=ab(q_1q_2)^m(q_1-q_2)^2.
}
```

Therefore

```math
\boxed{W_1^2=W_0W_2.}
```

and the second-mode evidence itself vanishes as

```math
|q_1-q_2|^2.
```

Only after the second mode is statistically resolved should `q1,q2` be fitted.

### Conceptual question

> **If one mode fails, are exactly two ordinary propagation modes enough?**

Then use the recovered roots to distinguish mechanisms.

---

# 4. Headline theorem set

The main paper should contain no more than the following theorem/corollary structure.

## Theorem 1 — Shockley-Ramo survival relation

For one conserved carrier in the reduced homogeneous planar geometry,

```math
\boxed{
J(d,s)
=qE_ww\frac{1-U(d,s)}{s}
}
```

with first-passage transform

```math
U(d,s)=E[e^{-sT_d}].
```

For a homogeneous scalar spatial semigroup,

```math
U=e^{-\gamma d}
```

and hence

```math
J=C(s)[1-e^{-\gamma d}].
```

Purpose: establish the measured observable correctly and explain why one extra color is needed relative to ideal arrival flux.

---

## Theorem 2 — four-color terminal-current closure

For four equally spaced source coordinates,

```math
\boxed{
(J_2-J_1)^2
=(J_1-J_0)(J_3-J_2).
}
```

Purpose: minimal spatial null and propagation-exponent extraction.

Supporting corollaries:

```text
common complex gain cancellation
common additive offset cancellation
rigid finite-width generation-kernel invariance
affine internal-coordinate calibration invariance.
```

Do not overload the theorem statement with every systematic correction.

---

## Theorem 3 — complete uniform DD + recombination inversion

Recover

```math
g_0=\gamma(0),
\qquad
g_\omega=\gamma(i\omega).
```

Define

```math
A=g_\omega^2-g_0^2,
```

```math
B=g_\omega-g_0,
```

```math
\Delta
=\Re A\Im B-\Im A\Re B.
```

Then, for `Delta != 0`,

```math
\boxed{
D=-\frac{\omega\Re B}{\Delta},
}
```

```math
\boxed{
w=\frac{\omega\Re A}{\Delta},
}
```

```math
\boxed{
\kappa=Dg_0^2+wg_0.
}
```

Purpose: one DC + one RF identify; later RF frequencies falsify.

The algebra itself is not the novelty claim.

---

## Theorem 4 — two-mode separation and six-color closure

For

```math
d_m=a q_1^m+b q_2^m,
```

```math
\boxed{
W_m
=d_md_{m+2}-d_{m+1}^2
=ab(q_1q_2)^m(q_1-q_2)^2.
}
```

Hence

```math
\boxed{W_1^2=W_0W_2.}
```

Purpose:

```text
exact rank-two null
+
explicit two-mode identifiability scale.
```

This is stronger for the paper than presenting a generic Hankel determinant alone.

---

## Corollary — mechanism-specific two-root RF closure

### One finite scalar boundary + uniform DD/recombination

```math
r_++r_-=-w/D
```

is real and RF-independent,

```math
r_+r_-=-(\kappa+i\omega)/D.
```

### Two independent homogeneous carrier species

Six colors recover one signed root for each collection direction.  DC + one RF determine

```math
(D_e,w_e,\kappa_e),
```

```math
(D_h,w_h,\kappa_h).
```

Every later RF frequency must reproduce both triples.

Purpose: demonstrate that the hierarchy can absorb ordinary boundary/electron-hole explanations without becoming a free-form fit.

---

# 5. Controlled inhomogeneity result

This should be a corollary/section, not a headline theorem before the homogeneous nulls.

For deterministic/high-Peclet downstream transit with

```math
q(z)=1/v(z),
```

the low-RF logarithmic four-color closure is

```math
\boxed{
\mathcal C_4
=-i\omega h^2
\left[
2q'(z_c)-(L-z_c)q''(z_c)
\right]
+O(\omega h^4,\omega^2).
}
```

For locally linear slowness,

```math
\boxed{
\operatorname{Im}\mathcal C_4/\omega
=-2h^2q'(z_c).
}
```

This is the first simple **positive theoretical prediction after the null fails in a controlled way**.

Do not write

```text
nonzero C4 = velocity gradient.
```

The mode/systematic hierarchy comes first.

---

# 6. Systematic-error section

Keep it short in the main text and push proofs to supplementary material.

## 6.1 Optical source shape

Using equally spaced **mean generation depth**,

```math
\boxed{
\mathcal C_{4,opt}
=\frac{\gamma}{2h}\Delta^3\sigma_z^2
+O(\gamma^2).
}
```

Key sentence:

> Smooth source-width evolution through quadratic order cannot contaminate the closure at first order in the propagation exponent.

---

## 6.2 Spectral amplitude/chain calibration

At low RF with locally affine current,

```math
\boxed{
\delta\mathcal C_4
=-\frac{\Delta^3(\epsilon J)}{B}.
}
```

Common and linearly varying fractional complex calibration error cancel at first order.

The dangerous part is irregular/high-curvature channel error.

---

## 6.3 Internal-coordinate calibration

Any affine map

```math
z=a+b\mu
```

preserves exact closure.

Only nonlinear coordinate curvature creates a false model-order failure.

This is a useful practical robustness statement.

---

## 6.4 Independent noise

Equal-step high-SNR limit:

```math
\boxed{
\sigma_{\mathcal C_4}
\simeq\sqrt{20}\frac{\sigma_J}{|d|}.
}
```

The stencil is

```text
(1,-3,3,-1).
```

The same high-order cancellation that rejects smooth systematics amplifies uncorrelated noise.

---

# 7. Rank-two statistical boundary

This is worth one main-text equation because it prevents overclaiming six-color inversion.

The second-mode witness is

```math
W_0=ab(q_1-q_2)^2.
```

Its independent-current noise is

```math
\boxed{
\sigma_{W_0}^2
=\sigma_J^2
\left[
|d_2|^2
+|d_2+2d_1|^2
+|d_0+2d_1|^2
+|d_0|^2
\right].
}
```

Near equal current steps,

```math
\sigma_{W_0}
\simeq\sqrt{20}|d|\sigma_J.
```

Therefore second-mode detectability collapses as

```math
|q_1-q_2|^2.
```

Only statistically resolved modes should be given physical root interpretations.

---

# 8. HgCdTe worked example

Use one deliberately simple example only.

```text
T = 300 K
L = 7.6 um
linear x = 0.55 -> 0.32
Hansen gap
Moazzami absorption
mean generation depths = 2.5,3.0,3.5,4.0 um.
```

Corresponding wavelengths:

```text
2.134651
2.215042
2.301173
2.393907 um.
```

All modeled absorbed fractions exceed `0.9993`.

Use the reduced graded-velocity stress already documented.

### Correct stochastic result

Finite Einstein diffusion, no finite entrance boundary, no recombination:

```text
100 MHz:
graded raw-current closure phase ~ -0.00952 deg
homogeneous same-optics floor ~ +0.00246 deg
gradient-sensitive excess ~ -0.01198 deg

500 MHz:
excess ~ -0.05873 deg

1 GHz:
excess ~ -0.11041 deg.
```

Uniform lifetime stresses around `10 ns` and `1 ns` do not erase the signal in the explicit model.

The deterministic low-RF theorem predicts approximately

```text
-0.01254 deg @100 MHz,
```

close to the finite-diffusion result.

This is the only material calculation needed in the main paper unless a reviewer-level reason demands more.

---

# 9. Experimental resource prediction

For the same stochastic quartet and independent equal complex current noise, `3 sigma` gradient-closure detection requires approximately

```text
100 MHz -> 96.1 dB amplitude SNR on spatial current step
250 MHz -> 88.2 dB
500 MHz -> 82.3 dB
1 GHz   -> 76.7 dB.
```

This should be stated as a **theoretical measurement target**, not proof that a particular laboratory setup can achieve it.

The scientific point is the RF tradeoff:

```text
low RF -> cleaner asymptotic interpretation but harder statistics
higher RF -> stronger closure signal but more exposure to parasitics / extra modes.
```

---

# 10. Figure plan

## Figure 1 — the entire idea in one picture

Planar detector schematic.

Four wavelengths map to four equally spaced internal mean-generation coordinates.

Below the device show

```text
J0, J1, J2, J3
-> Delta J0, Delta J1, Delta J2
-> (Delta J1)^2 ?= Delta J0 Delta J2.
```

This figure should make the paper understandable before any PDE appears.

---

## Figure 2 — one RF identifies, next RF falsifies

Complex `gamma` plane.

One RF point maps algebraically to `D,w,kappa` after DC.

Second/third RF points either collapse to the same coefficients or visibly disperse.

Include the physical root cone / allowed region only if it helps visually.

---

## Figure 3 — failure hierarchy

Flow diagram:

```text
4-color closure passes
-> one spatial mode
-> RF DD/recombination closure

4-color fails
-> second-mode witness W0

W0 insignificant
-> cannot resolve second mode

W0 significant
-> 6-color rank-two closure
-> recover roots
-> boundary root law?
-> two-carrier law?
-> neither -> richer model required.
```

This may be the conceptual centerpiece.

---

## Figure 4 — corrected HgCdTe worked prediction

Plot versus RF frequency:

```text
variable-transport C4 phase
homogeneous same-optics phase
corrected gradient-sensitive excess.
```

Use the stochastic finite-diffusion calculation.

Optionally overlay the low-RF analytic slope.

Do not show the superseded boundary-confounded three-color calculation except perhaps in supplementary provenance.

---

## Figure 5 — statistical/systematic design

Compact plot or table showing

```text
four-color closure noise versus RF
optical correction scale
3-sigma SNR target.
```

Avoid overcrowding the main paper with all calibration formulas.

---

# 11. Main-text section order

## I. Introduction

One conceptual problem:

> A photodiode RF response can be fitted by many transport models; can the device be made to **falsify** simple transport hypotheses before fitting richer ones?

Introduce wavelength as an internal source coordinate, but explicitly acknowledge that absorption-depth-dependent photodiode phase/OED is established prior art.

State that the contribution sought is closure/model-order logic, not wavelength-dependent timing itself.

---

## II. Observable correction and minimal four-color theorem

Shockley-Ramo survival theorem.

Derive raw-current affine exponential.

Derive four-color closure.

This is where the paper distinguishes itself from an arrival-time-only treatment.

---

## III. From one spatial mode to a physical transport generator

Recover `gamma`.

DC + one RF inversion of `D,w,kappa`.

Additional RF frequencies as null tests.

---

## IV. What a failed four-color law means

Ordinary electron-hole counterexample.

Six-color rank-two closure.

Exact second-mode witness.

Finite-boundary and two-carrier RF root laws.

This section demonstrates that the framework is conservative rather than anomaly-seeking.

---

## V. Controlled spatial inhomogeneity

Low-RF slowness-gradient theorem.

Only now discuss what a nonzero closure can measure after lower-level explanations are excluded or modeled.

---

## VI. Optical/calibration/noise robustness

Short main-text summary of

```text
rigid-source invariance
Delta^3 variance correction
affine coordinate invariance
smooth calibration rejection
sqrt(20) noise law
mode-separation witness significance.
```

Full derivations to supplement.

---

## VII. HgCdTe worked prediction

One conditional calculation.

Emphasize falsifiable scale and measurement resource, not fabrication.

---

## VIII. Discussion

What a failure at each rung means.

What is established prior art.

What the framework does **not** identify uniquely.

Why richer models should enter only after lower-order closures fail.

---

# 12. Supplement structure

### S1
Full Shockley-Ramo / backward-equation derivations.

### S2
Rigid-source and optical-shape expansions.

### S3
Amplitude and coordinate calibration errors.

### S4
Noise covariance and spacing optimization.

### S5
Rank-two recurrence/Hankel proofs and conditioning.

### S6
Boundary + recombination root proof.

### S7
Two-carrier complete inversion.

### S8
HgCdTe material relations, numerical convergence, and parameter stresses.

### S9
Prior-art search protocol / claim table.

Do not bury a central conceptual assumption only in the supplement.

---

# 13. Results that should stay out of the main paper

Unless the story later requires them:

```text
occupation-time local-clock theorem
full cumulant hierarchy
Levy delay-spectrum reconstruction
arbitrary-profile second-derivative inverse
translated-gradient fabrication optimization
sample-A/B rescue/calibration history.
```

They are good theory but make this paper less clear.

The paper should feel like one idea, not a repository dump.

---

# 14. Prior-art boundary for the manuscript

The introduction/discussion must explicitly acknowledge at least these surrounding areas:

```text
Shockley-Ramo signal formation
classical photodiode drift/diffusion impulse-response theory
wavelength-dependent absorption-depth / RF phase and optoelectronic chromatic dispersion
multi-frequency photodiode characterization
Hankel / Prony model-order identification
time-domain Hankel identification of photodetector impulse response
first-passage drift-diffusion mathematics.
```

Specific close methodological neighbor:

```text
Y. Sun et al.,
"Complete model identification for measuring photodetector's data age in high-speed and high-precision interferometry,"
Optics Express 33, 15125-15140 (2025),
DOI 10.1364/OE.550721.
```

That work uses a Hankel matrix on a **time-sampled photodetector impulse response** to identify system order.

The candidate distinction here is spatial:

```text
spectral channel -> calibrated internal generation coordinate
-> spatial first-difference sequence
-> mode-order closure
-> transport-specific RF root algebra.
```

Also acknowledge

```text
Z. Glasser et al.,
"Optoelectronic chromatic dispersion and wavelength monitoring in a photodiode,"
Optics Express 29, 19839-19852 (2021),
DOI 10.1364/OE.424157,
```

because wavelength-dependent absorption depth producing RF phase is established and central surrounding prior art.

Priority of the exact four-/six-color spectral-depth construction remains **OPEN**.

---

# 15. Reviewer attacks that the manuscript must pre-answer

### "You confused transit time with terminal photocurrent."

Pre-answered by Shockley-Ramo survival theorem and four-color correction.

### "A second carrier trivially breaks your closure."

Pre-answered by six-color two-carrier inversion.

### "A boundary trivially breaks your closure."

Pre-answered by rank-two boundary root law and boundary-amplitude cancellation.

### "Your optical kernels are broad."

Rigid width is exactly harmless; real shape evolution is explicitly expanded and calculated.

### "Your depth calibration is uncertain."

Affine coordinate error does not affect model-order closure; nonlinear curvature does and has an explicit correction.

### "This is just Hankel system identification."

Hankel model-order mathematics is acknowledged as known.  The candidate application is the spectrally generated **internal spatial sequence** plus Shockley-Ramo/transport root constraints.

### "Your exact inversion is unusably ill-conditioned."

Second-mode witness/noise significance and root-coalescence boundary are explicit.

### "Your material example is too idealized."

It is presented as one falsifiable conditional stress, not a fitted real device.  Finite diffusion and uniform recombination are already included in the corrected robustness calculation.

---

# 16. Go/no-go criteria before writing the manuscript itself

Proceed to full manuscript drafting only if the following remain true after one final focused audit:

1. no primary source is found that already states the same equal-internal-depth four-color terminal-current closure or equivalent spatial finite-difference construction;
2. no primary source is found that already uses six spectral-depth channels to recover photocarrier spatial modes and then applies RF root algebra to falsify boundary/two-carrier transport;
3. the corrected stochastic HgCdTe example remains numerically stable under independent implementation/convergence checks;
4. rank-two mode recovery retains a plausible significance region rather than being formally exact but universally ill-conditioned;
5. all main-text claims can be stated without relying on the superseded three-color boundary-confounded result.

If a close priority collision appears, narrow the paper rather than defend a broad novelty claim.
