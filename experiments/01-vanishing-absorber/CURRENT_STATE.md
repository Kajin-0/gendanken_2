# Current State — Experiment 01: The Vanishing Absorber

**Date:** 2026-08-10  
**Status:** exploratory theory research; strongest current frontier is an **observable-corrected spectral-depth falsification framework for photocarrier transport**.  The active paper core uses Shockley-Ramo terminal-current formation explicitly; HgCdTe is a worked example, not the source of the general theory.  **No novelty claim.**

There is still **no manuscript**.

---

## 1. Active question

The project should no longer begin with

```text
fit an arbitrary internal velocity profile
```

or

```text
design a special HgCdTe structure.
```

The active theory question is:

> **Can wavelength provide calibrated internal source coordinates that allow a photodetector's measured complex current to falsify progressively richer spatial transport models using exact finite-difference and multi-frequency closure relations?**

The intended logic is

```text
simple gedanken experiment
-> exact observable
-> parameter-free spatial closure
-> recover minimal propagation mode(s)
-> second RF frequency tries to kill the transport law
-> only then add another carrier, boundary, memory state, etc.
```

Fabrication work remains supporting plausibility/provenance only.

---

## 2. Read first

After root `AGENTS.md`:

1. `PAPER_CORE_ADVERSARIAL_CONSOLIDATION.md`
2. `PAPER_CLAIM_LEDGER.md`
3. `SHOCKLEY_RAMO_OBSERVABLE_CORRECTION.md`
4. `SHOCKLEY_RAMO_SURVIVAL_THEOREM.md`
5. `RAMO_FOUR_COLOR_OPTICAL_ERROR_THEOREM.md`
6. `RAMO_FOUR_COLOR_SLOWNESS_GRADIENT_THEOREM.md`
7. `RAMO_FOUR_COLOR_SPACING_OPTIMUM.md`
8. `FIVE_COLOR_BOUNDARY_ROOT_PAIR_CLOSURE.md`
9. `HGCDTE_RAMO_FOUR_COLOR_GRADIENT_PREDICTION.md`
10. `THEORY_FALSIFICATION_LADDER.md`
11. `THEORY_CLAIM_LEDGER.md`
12. `SPATIAL_FIRST_PASSAGE_SEMIGROUP_THEOREM.md`
13. `LOCAL_MARKOV_TRANSPORT_CLOSURE_THEOREM.md`
14. `TRANSLATION_RESPONSE_THEOREM.md`
15. `ARCHIVE_STATUS.md`

The first-passage, occupation-time, Lévy/subordinator, translated-feature, and fabrication-design files remain valuable supporting theory/provenance but should not displace the observable-corrected paper core.

---

## 3. Major observable correction

A generic photodiode terminal RF current is **not automatically**

```math
H(\omega)=E[e^{-i\omega T}]
```

for the carrier first-passage time `T`.

Shockley-Ramo current is induced continuously as charge moves.

For one conserved carrier in the reduced one-dimensional homogeneous planar model,

```math
I(t)=qE_w w S(t),
```

where `S(t)` is first-passage survival probability.

Thus

```math
\boxed{
J(d,s)=qE_ww\frac{1-U(d,s)}{s},
}
```

with

```math
U(d,s)=E[e^{-sT_d}].
```

For a homogeneous scalar first-passage process,

```math
U(d,s)=e^{-\gamma(s)d},
```

so

```math
\boxed{
J(d,s)=C(s)[1-e^{-\gamma(s)d}].
}
```

Consequences:

```text
arrival/collector flux -> pure exponential in depth
raw planar terminal current -> constant + one exponential
DC-normalized terminal current -> generally neither of the above.
```

Therefore the old direct terminal-current three-color geometric-mean law is **invalidated**.

---

## 4. Minimal measurable-current gedanken — four colors

Choose four wavelengths whose calibrated internal **mean generation coordinates** are equally spaced:

```math
z_m=z_0+mh,
\qquad m=0,1,2,3.
```

Under the minimal planar one-carrier homogeneous model, first differences satisfy

```math
\Delta J_m=J_{m+1}-J_m=Bq^m.
```

Hence

```math
\boxed{
(J_2-J_1)^2
=(J_1-J_0)(J_3-J_2).
}
```

This is the active simplest terminal-current null.

Three points estimate the spatial multiplier;

the fourth is a falsification point.

The multiplier and spatial exponent are

```math
\boxed{
q
=\frac{J_2-J_1}{J_1-J_0},
}
```

```math
\boxed{
\gamma
=-\frac1h\log q.
}
```

The logarithm branch must be followed continuously in RF/depth.

The closure is invariant to a wavelength-independent complex gain and wavelength-independent additive complex offset at fixed RF.

---

## 5. Broad generation is not automatically a resolution failure

If wavelength rigidly translates one finite generation shape, source width/asymmetry only changes the exponential mode amplitude.

The four-color closure remains exact.

The relevant optical correction is **wavelength-dependent source-shape evolution**.

When the channels are selected by equally spaced **mean generation depth**, the leading variance contribution to the logarithmic closure

```math
\mathcal C_4
=2\ln\Delta J_1
-\ln\Delta J_0
-\ln\Delta J_2
```

is

```math
\boxed{
\mathcal C_{4,opt}
=\frac{\gamma}{2h}
(\sigma_3^2-3\sigma_2^2+3\sigma_1^2-\sigma_0^2)
+O(\gamma^2).
}
```

Thus constant, linear, and quadratic evolution of generation variance produces **no first-order optical-width closure error**.

Optical modeling is still required for higher moments and higher orders.

---

## 6. One RF identifies; the second RF falsifies

For uniform real drift-diffusion,

```math
D\gamma^2+w\gamma=i\omega.
```

Write

```math
\gamma=a+ib.
```

One RF frequency gives

```math
\boxed{
D=\frac{\omega a}{b(a^2+b^2)},
}
```

```math
\boxed{
w=\frac{\omega(b^2-a^2)}{b(a^2+b^2)}.
}
```

For positive downstream transport,

```math
\boxed{0<a<b.}
```

The second RF frequency adds no new `D,w` parameter.

The null prediction is therefore

```math
\boxed{
D(\omega_2)=D(\omega_1),
\qquad
w(\omega_2)=w(\omega_1).
}
```

This is the strongest compact transport gedanken experiment in the current paper core:

```text
first frequency -> identify
second frequency -> try to kill the model.
```

---

## 7. Failure does not imply anomalous transport

A conventional electron-hole pair already breaks the one-mode four-color law.

For deterministic planar electron-hole current,

```math
J(z)=C_0+C_e e^{r_ez}+C_h e^{r_hz}.
```

First differences have rank at most two.

Six source coordinates provide five first differences and allow the rank-two Hankel test

```math
\boxed{
\det
\begin{pmatrix}
\Delta J_0&\Delta J_1&\Delta J_2\\
\Delta J_1&\Delta J_2&\Delta J_3\\
\Delta J_2&\Delta J_3&\Delta J_4
\end{pmatrix}=0.
}
```

Therefore a failed four-color test should first trigger **mode counting**, not a claim of nonlocal or exotic physics.

---

## 8. Rank two can distinguish ordinary mechanisms through RF root geometry

Two spatial modes are not enough to identify a mechanism.

### Finite scalar boundary

For one uniform scalar second-order drift-diffusion equation,

```math
D r^2+w r-i\omega=0.
```

The two roots satisfy

```math
\boxed{r_++r_-=-w/D}
```

(real and RF-independent) and

```math
\boxed{r_+r_-=-i\omega/D}
```

(purely imaginary and linear in RF).

### Conventional deterministic electron-hole pair

```math
\boxed{
r_e+r_h
=i\omega(1/v_e-1/v_h),
}
```

```math
\boxed{
r_er_h=\omega^2/(v_ev_h).
}
```

Thus

```text
finite scalar boundary:
root sum -> real constant
root product -> imaginary ~ omega

electron-hole pair:
root sum -> imaginary ~ omega
root product -> real ~ omega^2.
```

This is the current clearest example of the program's philosophy:

> **count modes first; then use their RF algebra to falsify physical explanations.**

---

## 9. Controlled departure from homogeneous transport

In the deterministic/high-Peclet limit with local slowness

```math
q(z)=1/v(z),
```

the low-RF four-color closure at quartet midpoint `z_c` is

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

If slowness is locally linear,

```math
\boxed{
\frac{\operatorname{Im}\mathcal C_4}{\omega}
=-2h^2q'(z_c).
}
```

So after the lower-level one-mode/optical hypotheses have been controlled, the low-RF phase closure has a direct inverse-velocity-gradient interpretation in this limiting model.

Do not apply this interpretation automatically to every nonzero closure residual.

---

## 10. Noise and spacing

For independent equal circular complex sample noise and approximately equal first-difference magnitude `|d|`, high-SNR propagation gives

```math
\boxed{
\sigma_{\mathcal C_4}
\simeq
\sqrt{20}\frac{\sigma_J}{|d|}.
}
```

The equal-difference linearized coefficients are the third-difference stencil

```text
(1,-3,3,-1)/d.
```

This is why smooth low-order systematics are rejected strongly but uncorrelated noise is amplified.

If the dominant smooth systematic scales as `A h^2` and closure noise as `B/h`,

```math
\boxed{
h_*=(B/\sqrt2A)^{1/3}.}
```

With white averaging,

```math
h_*\propto t^{-1/6}.
```

Thus brute-force averaging improves the useful spatial spacing only slowly.

---

## 11. Corrected HgCdTe worked example

Use the explicit theory stress

```text
T = 300 K
L = 7.6 um
linear x=0.55 -> 0.32
Hansen gap
Moazzami above-gap absorption
reduced quasi-neutral graded-velocity sensitivity model
high-Peclet deterministic propagation
no reflecting upstream boundary.
```

Choose mean generation depths

```text
2.5, 3.0, 3.5, 4.0 um,
```

which give approximately

```text
lambda = 2.134651, 2.215042, 2.301173, 2.393907 um.
```

All modeled absorbed fractions exceed `0.9993`.

At `100 MHz`:

```text
variable-transport C4 phase ~ -0.00993 deg
same-optics homogeneous floor ~ +0.00246 deg
gradient-sensitive excess ~ -0.01238 deg.
```

The independent point-source low-RF slowness-gradient theorem predicts

```text
~ -0.01254 deg
```

for the same profile/spacing.

The close agreement is an internal theory check, not a calibrated device forecast.

At higher RF the explicit gradient-sensitive excess reaches about

```text
-0.060 deg at 500 MHz
-0.110 deg at 1 GHz
```

inside this stated stress.

This replaces the earlier boundary-confounded three-color HgCdTe phase interpretation.

---

## 12. Major invalidations to remember

Do **not** resurrect the following statements:

### Generic terminal current is the first-passage characteristic function

**INVALIDATED.**

### Generic terminal-current three-color geometric-mean law

**INVALIDATED.**

### Inverse-Gaussian first-passage skewness/kurtosis identities apply directly to any measured photocurrent waveform

**INVALIDATED AS A GENERIC OBSERVABLE CLAIM.**

The first-passage mathematics remains valid for the arrival propagator/recovered spatial exponent, not arbitrary induced-current signal-time distributions.

### Earlier `~0.1-1 deg` HgCdTe three-color phase was mainly the bulk gradient

**INVALIDATED / SUPERSEDED.**

The reflecting entrance boundary produced almost all of that curvature.

### Rank two identifies a boundary

**INVALIDATED GENERALIZATION.**

A conventional electron-hole pair is already a rank-two counterexample.

---

## 13. What is not claimed novel

Hard prior-art boundary includes

```text
Shockley-Ramo signal formation
wavelength-dependent absorption depth
wavelength-dependent photodiode RF phase/bandwidth
optoelectronic chromatic dispersion
frequency-domain photodiode drift-diffusion models
Prony/Hankel/system-identification mathematics
first-passage semigroups
inverse-Gaussian first-passage theory
algebraic convection-diffusion inversion.
```

The candidate contribution, if it survives priority audit, is the **integrated detector protocol**:

```text
wavelength -> calibrated internal source coordinate

Shockley-Ramo-aware finite differences
-> isolate spatial propagation modes

minimal color count
-> falsify model order

RF root algebra
-> falsify the physical transport law

only then
-> add a boundary, second carrier, memory state, etc.
```

**Status:** CANDIDATE DISTINCT APPLICATION — PRIORITY UNPROVEN.

Targeted searches have not yet recovered this exact four-/six-color equal-internal-depth closure protocol, but a negative search is not novelty evidence.

---

## 14. Supporting theory demoted from the headline paper

The following remain useful but should not presently dominate the manuscript:

```text
arbitrary-profile second-spatial-derivative inversion
ideal local-clock occupation-time spectroscopy
full Levy delay-spectrum reconstruction
translated-gradient fabrication optimization
published sample-A/B rescue calculations.
```

They remain available as appendices, follow-up work, or provenance if needed.

---

## 15. Next decisive work

Do **not** add another unrelated general theorem.

Priority now:

1. complete the narrow primary-source audit for the exact spectral-depth finite-difference / Hankel closure construction;
2. derive the full stochastic Shockley-Ramo four-color relation beyond the half-line uniform model and identify exactly which assumptions preserve the affine-exponential spatial form;
3. add calibrated source-amplitude and wavelength-dependent external-chain errors to the covariance/systematic model;
4. stress the corrected HgCdTe quartet with finite diffusion, recombination, electron-hole contribution, and a realistic finite boundary one at a time;
5. determine whether the four-/six-color hierarchy remains experimentally discriminating after those ordinary effects;
6. only then outline the manuscript and reassess publication strength.

The project is now **theory-first and adversarially falsification-driven**.  A smaller result that survives these attacks is preferred over a larger but fragile claim.
