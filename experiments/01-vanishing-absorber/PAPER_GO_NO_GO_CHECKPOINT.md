# Theory Paper Go/No-Go Checkpoint

**Date:** 2026-08-10  
**Decision:** **GO for manuscript drafting as a falsifiable theory/method paper; NO-GO for novelty/priority language.**

This checkpoint is intentionally stricter than asking whether the mathematics is interesting.

The question is:

> **Has the reduced spectral-depth / Shockley-Ramo closure program survived enough ordinary counterexamples, observable corrections, numerical checks, and measurement-resource analysis to justify writing a full theory manuscript?**

Current answer: **yes, conditionally**.

Priority remains open.

---

# 1. Observable correctness

## Risk

The original theory treated

```math
H(\omega)=E[e^{-i\omega T}]
```

as if it were generic measured photodiode terminal current.

## Result

**PASS AFTER MAJOR CORRECTION.**

Shockley-Ramo signal formation was derived explicitly.

For the minimal homogeneous planar one-carrier geometry,

```math
J(d,s)=C(s)[1-U(d,s)],
```

with

```math
U(d,s)=e^{-\gamma d}.
```

This invalidated the old terminal-current three-color law and produced the correct **four-color first-difference closure**.

The arrival-flux theory remains valid as supporting first-passage mathematics but is no longer conflated with terminal current.

Relevant files:

```text
SHOCKLEY_RAMO_OBSERVABLE_CORRECTION.md
SHOCKLEY_RAMO_SURVIVAL_THEOREM.md
```

---

# 2. Minimal one-mode closure

## Result

**PASS.**

For four equally spaced internal source coordinates,

```math
\boxed{
(J_2-J_1)^2
=(J_1-J_0)(J_3-J_2).
}
```

The spatial multiplier and exponent follow from current first differences.

The closure survives

```text
common complex RF gain,
common additive offset,
rigid finite-width generation kernels,
and unknown affine internal-depth calibration.
```

It is therefore not a fragile delta-source identity.

---

# 3. Physical transport closure

## Result

**PASS.**

Uniform drift-diffusion with uniform Markov recombination satisfies

```math
D\gamma^2+w\gamma=\kappa+s.
```

Four colors at DC plus four colors at one RF recover

```math
D,w,\kappa
```

algebraically in nonsingular noiseless data.

Every additional RF frequency introduces no transport parameter and is therefore a pure falsification measurement.

This is the cleanest physical null in the paper.

Relevant file:

```text
RAMO_DC_RF_RECOMBINATION_INVERSION.md
```

---

# 4. Ordinary two-carrier objection

## Risk

A real photodiode can have both electron and hole Shockley-Ramo contributions.

## Result

**PASS AS NEXT HIERARCHY RUNG.**

A conventional electron-hole pair breaks the one-mode four-color closure but produces a rank-two first-difference sequence.

Six colors recover the two spatial roots in generic noiseless data.

At DC their signs label opposite collection directions; DC plus one RF then recover

```math
(D_e,w_e,\kappa_e),
```

```math
(D_h,w_h,\kappa_h).
```

Every additional RF overdetermines both species simultaneously.

Thus the obvious two-carrier complication does not turn the theory into a free-form fit.

Relevant file:

```text
RAMO_SIX_COLOR_TWO_CARRIER_INVERSION.md
```

---

# 5. Finite-boundary objection

## Risk

A finite entrance/contact boundary can add a second spatial mode and previously produced a serious false interpretation in the HgCdTe branch.

## Result

**PASS AS A DISTINCT RANK-TWO MODEL.**

For uniform scalar drift-diffusion/recombination with arbitrary linear finite-boundary amplitudes, six colors recover two roots satisfying

```math
r_++r_-=-w/D,
```

```math
r_+r_-=-(\kappa+i\omega)/D.
```

The boundary amplitudes are nuisance quantities that do not enter the coefficient recovery.

Boundary and electron-hole rank-two models have different RF root structure.

Relevant file:

```text
RAMO_SIX_COLOR_BOUNDARY_RECOMBINATION.md
```

---

# 6. Rank-two identifiability

## Risk

Exact rank-two recovery may be numerically meaningless when the roots merge or one mode is weak.

## Result

**PASS WITH AN EXPLICIT RESOLUTION BOUNDARY.**

For

```math
d_m=a q_1^m+b q_2^m,
```

the exact Hankel-minor witness is

```math
\boxed{
W_m
=ab(q_1q_2)^m(q_1-q_2)^2.
}
```

Thus the evidence for two observable modes collapses quadratically as the roots merge and linearly as either mode amplitude vanishes.

The pre-fit current-noise covariance is explicit.

For comparable visible modes near equal current steps,

```math
Z_2
\simeq
\frac{|q_1-q_2|^2}
{4\sqrt{20}\,\eta},
\qquad
\eta=\sigma_J/|d|.
```

At `3 sigma`,

```math
|q_1-q_2|
\gtrsim7.33\sqrt{\eta}.
```

Examples:

```text
eta=1e-4 -> root-multiplier split ~0.073
eta=1e-5 -> ~0.023.
```

So the two-mode extension has a finite resolvable region rather than being a formal exact-arithmetic construction.

Relevant files:

```text
RAMO_SIX_COLOR_MODE_SEPARATION.md
RAMO_SIX_COLOR_MODE_SEPARATION_NOISE.md
RAMO_TWO_MODE_RESOLUTION_SCALING.md
```

---

# 7. Optical generation width and shape

## Result

**PASS CONDITIONALLY.**

Rigid finite-width source kernels preserve the exact one-mode closure.

For wavelength-dependent shape evolution, choosing the four channels by equally spaced **mean generation depth** gives the leading variance correction

```math
\mathcal C_{4,opt}
=\frac{\gamma}{2h}\Delta^3\sigma_z^2
+O(\gamma^2).
```

Constant, linear, and quadratic evolution of generation variance therefore produces no first-order width contamination.

Optical modeling remains necessary at higher order.

Relevant file:

```text
RAMO_FOUR_COLOR_OPTICAL_ERROR_THEOREM.md
```

---

# 8. Initial carrier-energy objection

## Risk

Changing wavelength changes both generation depth and photon energy.

## Result

**PASS CONDITIONALLY / STRONG IDEAL THEOREM.**

For an affine graded gap

```math
E_g(z)=E_{g0}-Gz
```

and absorption depending only on local photon excess energy

```math
u=E_\gamma-E_g(z),
```

the complete generation distribution expressed in `nu` is independent of photon energy:

```math
p_\nu(\nu)
=\frac{\alpha(\nu)}{G}
\exp\left[-\frac1G\int_0^\nu\alpha(u)du\right].
```

Thus wavelength translates the generation position while preserving the total initial excess-energy distribution exactly in the ideal limit.

For the real Hansen/Moazzami HgCdTe quartet, the generation-weighted mean total excess energy changes by only about `0.24%`, and its standard deviation by about `1.6%`.

Electron/hole partition and thermalization-memory effects remain open ordinary corrections, not assumed absent.

Relevant file:

```text
SPECTRAL_DEPTH_EXCESS_ENERGY_INVARIANCE.md
```

---

# 9. Spectral amplitude and depth calibration

## Result

**PASS CONDITIONALLY.**

The four-color null rejects low-order smooth calibration structure.

### Multiplicative spectral calibration

At low RF with locally affine current,

```math
\delta\mathcal C_4
=-\Delta^3(\epsilon J)/B.
```

Constant and linear fractional calibration drift cancel to first order.

### Internal-depth calibration

Any affine map

```math
z=a+b\mu
```

preserves exact model-order closure.

Only nonlinear coordinate curvature creates false closure failure.

Relevant files:

```text
RAMO_FOUR_COLOR_AMPLITUDE_CALIBRATION.md
RAMO_FOUR_COLOR_COORDINATE_CALIBRATION.md
```

---

# 10. Corrected HgCdTe prediction

## Result

**PASS CONDITIONALLY AND INDEPENDENTLY CROSS-CHECKED.**

Use the explicit `300 K`, `7.6 um`, linear `x=0.55 -> 0.32` graded-HgCdTe theory stress with Hansen/Moazzami optics.

Mean generation depths

```text
2.5, 3.0, 3.5, 4.0 um
```

correspond to approximately

```text
2.134651, 2.215042, 2.301173, 2.393907 um.
```

All modeled absorbed fractions exceed `0.9993`.

With finite Einstein diffusion and no finite entrance boundary, the gradient-sensitive four-color phase excess is approximately

```text
100 MHz -> -0.01198 deg
500 MHz -> -0.05873 deg
1 GHz   -> -0.11041 deg.
```

Uniform recombination stresses do not erase the effect in the tested range.

The `100 MHz` stochastic result is close to the independent deterministic low-RF slowness-gradient theorem.

### Independent numerical implementation

**PASS.**

The canonical sparse finite-difference BVP result was independently reproduced by an adaptive DOP853 shooting method using a forced solution plus homogeneous boundary sensitivity.

The cross-check reproduces the three quoted phase excesses to about `1e-6` degree or better.

Relevant files:

```text
HGCDTE_RAMO_FOUR_COLOR_GRADIENT_PREDICTION.md
HGCDTE_RAMO_FOUR_COLOR_DIFFUSION_RECOMBINATION.md
numerics/hgcdte_ramo_four_color_shooting_crosscheck.py
```

---

# 11. Measurement resource

## Result

**PASS AS A CONDITIONAL TARGET; DEMANDING.**

For the corrected stochastic HgCdTe quartet and independent equal complex current noise, `3 sigma` detection requires approximate amplitude SNR on the spatial current step of

```text
100 MHz -> 96.1 dB
250 MHz -> 88.2 dB
500 MHz -> 82.3 dB
1 GHz   -> 76.7 dB.
```

Thus the effect is not merely mathematically nonzero, but the low-RF regime is metrologically demanding.

The paper must present this honestly.

Relevant file:

```text
HGCDTE_RAMO_FOUR_COLOR_MEASUREMENT_RESOURCE.md
```

---

# 12. Prior-art status

## Surrounding physics definitely known

Do not claim novelty for

```text
Shockley-Ramo signal formation
photodiode drift/diffusion impulse-response theory
wavelength-dependent absorption depth and RF phase
optoelectronic chromatic dispersion
multi-frequency photodiode characterization
Hankel/Prony model-order identification
Hankel identification of photodetector time-domain impulse responses
first-passage drift-diffusion mathematics.
```

Important methodological neighbor:

```text
Y. Sun et al.,
"Complete model identification for measuring photodetector's data age in high-speed and high-precision interferometry,"
Optics Express 33, 15125-15140 (2025),
DOI 10.1364/OE.550721.
```

That work uses a Hankel matrix on a **time-sampled photodetector impulse-response sequence**.

Important spectral-depth neighbor:

```text
Z. Glasser et al.,
"Optoelectronic chromatic dispersion and wavelength monitoring in a photodiode,"
Optics Express 29, 19839-19852 (2021),
DOI 10.1364/OE.424157.
```

That work establishes wavelength-dependent absorption depth as a source of photodiode RF phase.

## Exact surviving candidate

Targeted searches have not yet recovered a primary source using the complete sequence

```text
wavelength -> calibrated internal spatial source coordinate
-> raw Shockley-Ramo spatial first differences
-> four-color one-mode closure
-> six-color rank-two mode closure
-> RF root algebra to falsify boundary/two-carrier drift-diffusion models.
```

This is **not evidence of priority**.

Status remains

```text
CANDIDATE DISTINCT APPLICATION — PRIORITY UNPROVEN.
```

---

# 13. Unresolved 2024 HgCdTe source

The paper

```text
"Potential application of HgCdTe detector with composition gradient in laser measurement"
Journal of Applied Optics 45(3), 549-556 (2024)
DOI 10.5768/JAO202445.0310009
```

is bibliographically confirmed, but full technical text remains unavailable in the sources recovered here.

Accessible surrounding publications from the same group place this branch strongly in

```text
laser strong-illumination response,
saturation,
and graded-HgCdTe photoelectric performance.
```

That makes a direct four-/six-color closure collision less likely, but does **not** clear priority.

The manuscript should cite/acknowledge the source if relevant and avoid claiming it has been fully audited.

---

# 14. Final disposition

## GO

Proceed to a full theorem/method manuscript draft based on

```text
four-color Shockley-Ramo closure
DC + RF complete homogeneous inversion
six-color model-order hierarchy
boundary/two-carrier root closure
controlled slowness-gradient prediction
systematic/noise bounds
corrected HgCdTe worked example.
```

The internal mathematical story is now coherent enough to write.

## NO-GO

Do **not** write

```text
"first"
"novel"
"new fundamental"
"unprecedented"
```

or equivalent priority language.

Do not present the HgCdTe numerical stress as a calibrated detector forecast.

Do not resurrect the superseded three-color boundary-confounded result.

Do not apply first-passage timing-distribution identities directly to generic terminal current.

---

# 15. Next action

The next work should be **manuscript drafting**, not another broad branch of mathematics.

Use

```text
MANUSCRIPT_BLUEPRINT_ADVERSARIAL.md
```

as the spine.

During drafting, any theorem whose assumptions cannot be stated in one concise paragraph should be moved to the supplement rather than expanded in the main text.
