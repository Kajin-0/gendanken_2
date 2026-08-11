# Paper Claim Ledger — Adversarially Reduced Core

**Updated:** 2026-08-10  
**Purpose:** epistemic boundary for the shortest defensible theory paper after the Shockley-Ramo observable correction and ordinary counterexample attacks.  This does not replace the broader `THEORY_CLAIM_LEDGER.md`; it records only claims that should currently be considered for the main paper.

## Status vocabulary

- **KNOWN** — established physics/mathematics used as input.
- **DERIVED** — exact consequence of stated assumptions.
- **CHECKED** — numerically/independently verified in repository regressions.
- **CONDITIONAL** — valid only under explicitly stated reduced assumptions.
- **CANDIDATE DISTINCT APPLICATION — PRIORITY UNPROVEN** — current search has not established priority; no novelty claim.
- **INVALIDATED** — explicit counterexample/correction found.
- **SUPERSEDED** — replaced by a stronger/corrected statement.
- **NON-CLAIM** — explicitly not asserted.

---

# 1. Observable boundary

### O1 — generic terminal RF current is the first-passage characteristic function

**Status:** **INVALIDATED AS A GENERAL PHOTODIODE STATEMENT**

Shockley-Ramo current is induced continuously while a carrier moves.  Even deterministic uniform transit gives

```math
U(d,i\omega)=e^{-i\omega d/w}
```

for arrival flux but

```math
J(d,i\omega)
\propto
1-e^{-i\omega d/w}
```

for raw planar induced current.

Therefore arrival flux and terminal current must be treated as distinct observables.

### O2 — raw terminal-current three-color geometric-mean law

**Status:** **INVALIDATED**

A deterministic rectangular Ramo pulse is an explicit counterexample.

### O3 — arrival-flux three-color law

**Status:** **DERIVED / CHECKED / CONDITIONAL**

For a homogeneous scalar first-passage semigroup and a rigidly translated source kernel,

```math
U_2^2=U_1U_3
```

for three equally spaced internal source coordinates.

This remains an ideal first-passage theorem, not a generic terminal-current theorem.

---

# 2. Corrected planar terminal-current core

### R1 — Shockley-Ramo survival relation

**Status:** **DERIVED / CONDITIONAL**

For one conserved carrier in one-dimensional homogeneous drift-diffusion on a half-line with positive downstream drift, absorbing collector, remote upstream boundary, and uniform planar weighting field,

```math
I(t)=qE_w w S(t),
```

where `S(t)` is first-passage survival probability.

Hence

```math
\boxed{
J(d,s)=qE_ww\frac{1-U(d,s)}{s}.
}
```

For homogeneous scalar first passage,

```math
U=e^{-\gamma d},
```

so raw terminal current has one constant particular term plus one exponential spatial mode.

### R2 — four-color first-difference closure

**Status:** **DERIVED / CHECKED / CONDITIONAL**

For four equally spaced internal source coordinates in the stated planar one-carrier homogeneous model,

```math
\boxed{
(J_2-J_1)^2
=(J_1-J_0)(J_3-J_2).
}
```

Equivalently, the first differences form one geometric spatial mode.

### R3 — propagation multiplier/exponent recovery

**Status:** **DERIVED / CHECKED**

```math
q_s
=\frac{J_2-J_1}{J_1-J_0}
=\frac{J_3-J_2}{J_2-J_1},
```

and

```math
\boxed{
\gamma(s)=-\frac1{\Delta d}\log q_s.
}
```

The log branch must be tracked continuously in RF/depth.

### R4 — common-chain invariance

**Status:** **DERIVED / CHECKED**

The four-color closure is invariant to

```math
J_m^{meas}=G(\omega)J_m+C(\omega)
```

when `G,C` are common across the four spectral channels at fixed RF.

Wavelength-dependent chain factors do not cancel.

### R5 — rigid finite-width source invariance

**Status:** **DERIVED / CHECKED**

Any fixed translated generation-kernel shape changes only the exponential mode amplitude.  Source width/asymmetry do not break R2 by themselves.

---

# 3. Optical source-shape error

### OP1 — leading mean-centered optical-width correction

**Status:** **DERIVED / CHECKED / CONDITIONAL ASYMPTOTIC**

For four channels selected by equally spaced **mean generation depth**, with centered variances `v_m=sigma_m^2`, the logarithmic closure

```math
\mathcal C_4
=2\ln\Delta J_1-
\ln\Delta J_0-
\ln\Delta J_2
```

obeys

```math
\boxed{
\mathcal C_{4,opt}
=\frac{\gamma}{2h}
(v_3-3v_2+3v_1-v_0)
+O(\gamma^2).
}
```

Thus constant, linear, and quadratic variance evolution produce no `O(gamma)` contamination.

### OP2 — optical modeling is unnecessary

**Status:** **NON-CLAIM / FALSE IN GENERAL**

Higher source moments and wavelength-dependent shape evolution remain real corrections.  The theorem suppresses low-order smooth errors; it does not eliminate optical calibration.

---

# 4. Uniform drift-diffusion RF closure

### D1 — one-frequency inversion from recovered spatial exponent

**Status:** **DERIVED / CHECKED**

If

```math
D\gamma^2+w\gamma=i\omega,
```

with real `D>0,w>0` and

```math
\gamma=a+ib,
```

then

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

### D2 — positive downstream root cone

**Status:** **DERIVED**

```math
\boxed{0<a<b}
```

for `D>0,w>0,omega>0` under the adopted branch convention.

### D3 — second RF frequency is a pure null test

**Status:** **DERIVED / CHECKED**

A homogeneous real Markov drift-diffusion model predicts

```math
\boxed{
D(\omega_1)=D(\omega_2),
\qquad
w(\omega_1)=w(\omega_2).
}
```

The second RF point introduces no new material parameter.

### D4 — algebraic drift-diffusion inversion itself is novel

**Status:** **NON-CLAIM / HARD PRIOR-ART BOUNDARY**

Local/frequency-domain convection-diffusion inversion and related mathematics are established.  Candidate value lies in the spectral-depth/Ramo-aware falsification construction, not Eq. D1 alone.

---

# 5. Failure does not imply exotic transport

### M1 — conventional electron-hole pair breaks the one-mode four-color law

**Status:** **DERIVED / CHECKED COUNTEREXAMPLE**

Ordinary deterministic planar electron-hole signal formation gives

```math
J(z)=C_0+C_e e^{r_ez}+C_h e^{r_hz},
```

so the one-mode first-difference closure generically fails.

### M2 — six colors test two first-difference spatial modes

**Status:** **DERIVED / CHECKED / KNOWN HANKEL MATHEMATICS**

Six source coordinates give five first differences.  If two modes suffice,

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

Hankel/Prony/system-identification mathematics is not a novelty claim.

### M3 — finite scalar boundary root signature

**Status:** **DERIVED / CHECKED / CONDITIONAL**

For the two roots of one finite-boundary scalar drift-diffusion equation,

```math
\boxed{r_++r_-=-w/D}
```

is real and RF-independent, while

```math
\boxed{r_+r_-=-i\omega/D}
```

is imaginary and linear in RF.

### M4 — conventional deterministic electron-hole root signature

**Status:** **DERIVED / CHECKED / CONDITIONAL**

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

Thus its root sum is imaginary/linear and its root product real/quadratic, qualitatively distinct from M3.

### M5 — rank-two alone identifies a boundary

**Status:** **INVALIDATED GENERALIZATION**

An ordinary electron-hole pair is already a rank-two counterexample.  Mechanism claims require root/RF closure after mode counting.

---

# 6. Controlled nonuniform-transport prediction

### G1 — low-RF four-color slowness-gradient theorem

**Status:** **DERIVED / CHECKED / CONDITIONAL HIGH-PECLET LIMIT**

For deterministic downstream transit with local slowness `q(z)=1/v(z)`, uniform planar weighting field, quartet spacing `h`, and midpoint `z_c`,

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

If `q` is locally linear,

```math
\boxed{
\frac{\operatorname{Im}\mathcal C_4}{\omega}
=-2h^2q'(z_c).
}
```

### G2 — any nonzero C4 directly proves a velocity gradient

**Status:** **INVALIDATED GENERALIZATION / NON-CLAIM**

Optical source-shape evolution, a second carrier, a boundary, hidden states, and wavelength-dependent external response can also break the minimal closure.  The hierarchy must be followed in order.

---

# 7. Statistics/design

### N1 — four-color independent-noise propagation

**Status:** **DERIVED / CHECKED / HIGH-SNR**

For independent equal circular complex current noise and equal first-difference magnitude `|d|`,

```math
\boxed{
\sigma_{\mathcal C_4}
\simeq
\sqrt{20}\frac{\sigma_J}{|d|}.
}
```

The linearized sample coefficients become the third-difference stencil

```text
(1,-3,3,-1)/d.
```

### N2 — cube-root spacing optimum

**Status:** **DERIVED / CHECKED / CONDITIONAL DESIGN LAW**

If the leading systematic bias is `A h^2` and statistical closure noise is `B/h`,

```math
\boxed{
h_*=(B/\sqrt2 A)^{1/3}.}
```

For the leading optical-variance error,

```math
\boxed{
h_*
=\left[
\frac{\sqrt{40}\sigma_J}
{G_J|\gamma\,d^3\sigma_z^2/d\mu^3|}
\right]^{1/3}.
}
```

With white averaging, `h_* proportional to t^-1/6`.

### N3 — N2 is a universal information bound

**Status:** **NON-CLAIM**

It depends on the stated estimator, dominant systematic, and noise assumptions.

---

# 8. Corrected HgCdTe worked example

### H1 — earlier `~0.1-1 deg` three-color phase was mainly bulk-gradient transport

**Status:** **INVALIDATED / SUPERSEDED**

A matched finite-boundary control showed that the reflecting entrance produced almost all of the original phase curvature.

### H2 — boundary-free raw-Ramo four-color HgCdTe high-Peclet stress

**Status:** **CHECKED / CONDITIONAL**

For the explicit `L=7.6 um`, `x=0.55->0.32`, 300 K Hansen/Moazzami optical model and reduced graded-velocity stress, choose mean generation depths

```text
2.5, 3.0, 3.5, 4.0 um
```

corresponding to approximately

```text
2.134651, 2.215042, 2.301173, 2.393907 um.
```

All modeled absorbed fractions exceed `0.9993`.

At 100 MHz:

```text
variable-transport C4 phase ~ -0.00993 deg
homogeneous same-optics floor ~ +0.00246 deg
gradient-sensitive excess ~ -0.01238 deg.
```

The independent point-source low-RF theorem predicts approximately

```text
-0.01254 deg
```

for the same slowness profile/spacing.

This is a theory consistency check, not a calibrated detector forecast.

---

# 9. Candidate contribution

### A1 — integrated spectral-depth/Ramo-aware falsification protocol

**Status:** **CANDIDATE DISTINCT APPLICATION — PRIORITY UNPROVEN**

The current candidate contribution is the sequence

```text
wavelength -> calibrated internal source coordinate

Shockley-Ramo-aware spatial first differences
-> isolate propagation modes

4 colors
-> test one dominant mode / recover gamma

second RF
-> falsify or retain one real DD generator

if one-mode test fails:
6 colors
-> test rank two
-> recover roots
-> use RF root geometry to discriminate ordinary boundary / electron-hole / richer models.
```

No individual mathematical ingredient is asserted novel.

### A2 — surrounding physics that is not claimed novel

**Status:** **HARD BOUNDARY**

Do not claim novelty for

```text
Shockley-Ramo signal formation
wavelength-dependent absorption depth
wavelength-dependent photodiode RF phase/bandwidth
frequency-domain drift-diffusion modeling
Hankel/Prony model-order tests
first-passage semigroups
algebraic convection-diffusion inversion.
```

### A3 — priority

**Status:** **OPEN**

Targeted searches have not yet recovered the exact equal-internal-depth four-/six-color finite-difference closure protocol in photodiode transport characterization.  Negative search is not novelty evidence.  A focused primary-source audit remains mandatory before novelty language.

---

# 10. Material demoted from the headline paper

The following remain useful repository theory but should not currently be headline claims:

```text
arbitrary-profile second-spatial-derivative inversion
ideal local-clock occupation-time spectroscopy
full Levy delay-spectrum reconstruction
fabrication optimization of translated gradient structures
published sample-A/B rescue calculations.
```

They can become appendices/follow-up work if they materially support the reduced paper.
