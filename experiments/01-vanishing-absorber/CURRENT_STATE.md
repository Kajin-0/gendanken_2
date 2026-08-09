# Current State — Experiment 01: The Vanishing Absorber

**Date:** 2026-08-08  
**Status:** exploratory; passive access-resource structure now connected to an autonomous detector testbed; major 2018/2026 prior-art boundary identified; no novelty claim  

## 1. Guiding question

Can an ideal photodetector be made arbitrarily small, arbitrarily fast, arbitrarily sensitive, and still absorb essentially every incident photon?

The project does not assume that these goals are fundamentally incompatible.

The research has moved away from geometric active volume toward a more durable requirement:

```text
propagating optical access
+
irreversible detector access
+
ready-state / reset free-energy resource
+
correct counting of external background and internal false events.
```

---

## 2. Canonical frontier

Read after root `AGENTS.md`:

1. `PASSIVE_MULTIMODE_TRANSFER_AREA_BOUND.md`
2. `AUTONOMOUS_DETECTOR_CAPTURE_GAP.md`
3. `CAPTURE_TO_CLICK_COMPOSITION.md`
4. `UNIFIED_THREE_LEVEL_CAPTURE_MACHINE.md`
5. `READINESS_BANDWIDTH_AFFINITY.md`
6. `NESS_OPTICAL_RESPONSE_AUDIT.md`
7. `DIRECT_FEEDTHROUGH_AND_BAND_LIMIT.md`
8. `STRUCTURED_RESERVOIR_ACCESS_AUDIT.md`
9. `THERMODYNAMIC_OPTICAL_ACCESS_BRIDGE.md`
10. `THERMAL_IRREVERSIBILITY_COST.md`
11. older Hopfield/LDOS/volume stages only for provenance.

`CLAIM_LEDGER.md` is the epistemic boundary.

---

## 3. Earlier routes that failed

### Geometric active volume

A shrinking ideal dielectric capacitor can retain finite optical participation and finite absorptive decay while

```math
V_a\to0,
\qquad
\gamma_a/V_a\to\infty.
```

Therefore passivity alone does not support a universal active-volume law such as

```text
eta^2 B <= C V_a.
```

### Finite absorber number

For one incident photon, a two-level transition remains linear in the one-excitation sector. Finite absorber number / saturation alone does not impose a one-photon speed ceiling in the Markov/RWA model.

### Weak-coupling oscillator-strength closure

Finite transition extent regularizes the literal point-dipole divergence, but oscillator-strength and extent inequalities do not close the problem before the enhanced rate estimate reaches

```math
\Gamma/\omega_0=O(1),
```

where weak-coupling Purcell/Markov theory fails.

These failures forced the analysis into nonperturbative light-matter coupling and then general passive-network theory.

---

## 4. Supporting nonperturbative Hopfield result

In a TRK-consistent two-mode Hopfield model, hold a lower dressed mode at fixed target frequency

```math
\omega_y=\omega_t>0
```

while retuning the bare frequencies and taking internal coupling

```math
g\to\infty.
```

For fixed local optical and detector bath resources,

```math
\boxed{
\min(\Gamma_L,\Gamma_R)\to0.
}
```

A resolved target resonance therefore cannot retain both finite peak optical-to-detector transfer and finite linewidth.

If the external reservoirs are deliberately strengthened to compensate, preserving target peak transfer `eta_*` and linewidth `W_*` requires at least one bare reservoir resource to grow as

```math
\boxed{
\max(\gamma_L,\gamma_R)
\ge
\Gamma_*
\sqrt{1+2g/\omega_t},
}
```

where

```math
\Gamma_*
=\frac{W_*}{4}
\left(1-\sqrt{1-\eta_*}\right).
```

This is a supporting mechanism with major deep-strong-coupling prior-art overlap. Priority of the fixed-target corollary remains unproven.

---

## 5. Exact finite passive multimode access theorem

For an arbitrary finite stable passive linear network with no direct optical-to-detector feedthrough,

```math
A=-iH-(\Gamma_L+\Gamma_R+\Gamma_I),
\qquad
H=H^\dagger,
```

and

```math
L=\operatorname{Tr}\Gamma_L,
\qquad
R=\operatorname{Tr}\Gamma_R,
```

define

```math
\mathcal I_{L\to R}
=
\int_{-\infty}^{\infty}
\frac{d\omega}{2\pi}
\operatorname{Tr}
[G_{RL}^\dagger(i\omega)G_{RL}(i\omega)].
```

Then

```math
\boxed{
\mathcal I_{L\to R}
\le
\frac{2LR}{L+R}.
}
```

In the left controllability-Gramian eigenbasis,

```math
\boxed{
\frac{\mathcal I_{L\to R}}2
=
\sum_i
\frac{\ell_i r_i}
{\ell_i+r_i+\iota_i}.
}
```

A single passive resonance saturates the bound. Multimode equality requires no participating parasitic loss and a common optical-to-detector access ratio

```math
\ell_i/r_i=L/R.
```

For angular-frequency band width `W`,

```math
\boxed{
\overline T_B
\le
\frac{4\pi LR}{W(L+R)}.
}
```

Thus internal modal complexity can redistribute transfer but cannot create unlimited integrated useful transfer at fixed aggregate boundary access.

The mathematical ingredients are standard `H2`, Lyapunov, and passivity theory. No novelty claim is made.

---

## 6. Scope audits that survived

### Direct feedthrough

A nonzero frequency-independent prompt optical-to-detector block makes the total all-frequency `H2` area divergent. It is a genuine additional broadband boundary resource.

For finite angular-frequency band `W`,

```math
\boxed{
\sqrt{\mathcal I_B}
\le
\sqrt{\frac{W}{2\pi}}\,\|D_{RL}\|_F
+
\sqrt{\frac{2LR}{L+R}}.
}
```

The strictly proper resonant excess remains subject to the harmonic theorem.

### Structured/non-Markovian reservoirs

If passive finite augmented realizations satisfy

```math
G_n\to G \quad\text{in }H2,
```

with finite limiting terminal access budgets

```math
L_n\to L<\infty,
\qquad
R_n\to R<\infty,
```

then

```math
\boxed{
\|G\|_{H2}^2
\le
\frac{2LR}{L+R}.
}
```

Spectral complexity alone is therefore not an escape under finite passive embedding assumptions.

---

## 7. Restricted thermodynamic optical-access bridge

Established thermodynamic broadband-coupling theory bounds the sum of **energy-decay** rates from optical modes in an angular-frequency interval `W` into one free-space channel:

```math
\sum_m\gamma_{m,n}
\le
\frac{W}{2\pi}.
```

The repository uses amplitude-decay rates, giving

```math
\boxed{
L_B\le\frac{W}{4\pi}.
}
```

Combining this prior optical ceiling with the harmonic theorem gives, under the stated one-channel/modal assumptions,

```math
\boxed{
\overline T_B
\le
\frac{R_B}{R_B+W/(4\pi)}.
}
```

Hence target band-averaged transfer `eta` requires

```math
\boxed{
R_B
\ge
\frac{\eta}{1-\eta}
\frac{W}{4\pi}.
}
```

This has strong prior-art overlap with broadband absorption/rate-matching theory and is retained only as a detector-facing composition corollary.

---

## 8. Thermal irreversibility result

For detector localization

```text
|e> <-> |d>
```

with energy release `Delta` into a thermal reservoir,

```math
\boxed{
\frac{k_\uparrow}{k_\downarrow}
=e^{-\Delta/(k_BT)}.
}
```

With the minimal population/amplitude convention

```math
k_\downarrow=2R_B,
```

the restricted optical-access requirement implies

```math
\boxed{
k_\uparrow
\ge
\frac{\eta}{1-\eta}
\frac{W}{2\pi}
 e^{-\Delta/(k_BT)}.
}
```

If the allowed reverse thermal-activation rate is `D_rev`,

```math
\boxed{
\Delta
\ge
k_BT
\ln\!\left[
\frac{\eta W}
{2\pi(1-\eta)D_{\rm rev}}
\right]
}
```

when the logarithm argument exceeds unity.

`D_rev` is **not automatically an observable dark-count rate**.

---

## 9. Major prior-art boundary: 2018 incoming-field framework and 2026 autonomous detector

Two primary papers now define what the repository may not claim.

### Young, Sarovar & Léonard (2018)

Their general quantum photodetector framework already treats

```text
incoming quantized photon field
+
absorption
+
amplification / monitored detector dynamics
```

as one coupled system and defines efficiency, dark counts, timing metrics, etc.

Therefore simply unifying propagating photon capture and detector amplification is not new.

### Schwarzhans et al. (2026)

Their autonomous quantum detector already treats

```text
captured target excitation
+
nonequilibrium work source
+
amplification / reset
+
entropy production
+
internal dark counts / jitter / dead time.
```

Their thermodynamic analysis conditions on the target excitation being present and explicitly leaves capture as a possible additional source of cost/inefficiency.

Therefore simply building a generic thermodynamic detector cycle is also not new.

### Narrowed candidate junction

A targeted search has not yet found a primary source combining

```text
externally normalized propagating-field capture bandwidth/access constraints
+
autonomous thermodynamic detector work/reset/dark-count accounting
```

in one detector model.

This is only a negative search result, not proof of novelty.

---

## 10. Serial capture-to-click diagnostic

For a serial architecture with conditional back-end click efficiency `eta_D`,

```math
\eta_{\rm ext}(\omega)
=\eta_{\rm cap}(\omega)\eta_D.
```

Under the restricted one-channel capture ceiling,

```math
\boxed{
\overline\eta_{\rm ext}
\le
\eta_D
\frac{R_C}{R_C+W/(4\pi)}.
}
```

Thus target external efficiency `eta_*` requires

```math
\boxed{
R_C
\ge
\frac{\eta_*}{\eta_D-\eta_*}
\frac{W}{4\pi},
\qquad
\eta_D>\eta_*.
}
```

For one flat thermal input channel with mean occupation `n_B`,

```math
\boxed{
R_{\rm bg}
=
\bar n_B
\frac{W}{2\pi}
\overline\eta_{\rm ext}.
}
```

These are real admitted background photons, not internal dark events.

The serial factorization is a reference limit, not the final unified detector theory.

---

## 11. Unified three-level capture machine

The minimal analytic testbed is

```text
|0>  reset/ground
|1>  metastable detection-ready
|2>  optically activated.

|0> <-> |1>  work/reset source
|1> <-> |2>  propagating optical signal channel
|2> <-> |0>  counted detector output channel.
```

For a detector conditioned on being ready in `|1>`, single-photon conversion is

```math
\boxed{
T_{L\to R}(\omega)
=
\frac{4\Gamma_L\Gamma_R}
{(\omega-\omega_L)^2
+(\Gamma_L+\Gamma_R+\Gamma_I)^2}.
}
```

The output quantum has energy

```math
\boxed{
\hbar\omega_R
=
\hbar\omega_L+(E_1-E_0),
}
```

so the metastable ready-state free energy supplies output energy gain but does not remove the capture rate-matching structure.

After a click the detector is in `|0>` and must be reset to `|1>`.

---

## 12. Exact reversible dark-cycle solution

Let population rates be

```text
u : 0 -> 1
 d : 1 -> 0
 a : 1 -> 2
 b : 2 -> 1
 c : 2 -> 0
 e : 0 -> 2.
```

Define

```math
Z
=ac+ae+au+bd+be+bu+cd+cu+de.
```

Then

```math
p_0=\frac{ac+bd+cd}{Z},
```

```math
p_1=\frac{be+bu+cu}{Z},
```

```math
p_2=\frac{ae+au+de}{Z}.
```

If every forward `2 -> 0` event is a registered click, the gross forward click rate is

```math
\boxed{
R_+
=cp_2
=\frac{c(ae+au+de)}{Z}.
}
```

The net detector-channel / cycle current is

```math
\boxed{
J_D
=cp_2-ep_0
=\frac{uac-dbe}{Z}.
}
```

Thus

```math
\boxed{R_+\neq J_D}
```

when the reverse detector-channel rate is appreciable.

At zero cycle affinity, `J_D=0` but microscopic forward and reverse jump activity can remain nonzero.

Therefore **gross click counts and net thermodynamic current are different observables**. The correct dark-count definition depends on what the physical readout monitors.

---

## 13. Readiness is a thermodynamic resource

In the simplest dark reset pair

```math
u:0\to1,
\qquad
d:1\to0,
```

define

```math
\mathcal A_r=\ln(u/d).
```

Then

```math
\boxed{
p_{\rm ready}
=\frac{1}{1+e^{-\mathcal A_r}}.
}
```

In the dilute-event serial limit,

```math
\boxed{
\overline\eta_{\rm ext}
\le
\frac{\eta_D}{1+e^{-\mathcal A_r}}
\frac{R_C}{R_C+W/(4\pi)}.
}
```

So target external efficiency requires not only optical access but sufficient ready-state bias.

This is a restricted composition result, not a universal work/entropy theorem.

---

## 14. Nonequilibrium readiness pumping does not beat passive absorptive capture

For the full dark steady state, define

```math
w=p_1-p_2.
```

A weak coherent probe on the signal transition gives

```math
\boxed{
\rho_{21}^{(1)}
=
\frac{i\Omega}{2}
\frac{p_1-p_2}
{\gamma_\perp+i\Delta},
}
```

with

```math
\boxed{
\gamma_\perp
=\frac12(a+d+b+c)+\gamma_\phi.
}
```

In the non-inverted absorbing regime,

```math
\boxed{0\le p_1-p_2\le1.}
```

The fully ready state `p_1=1,p_2=0` is therefore the maximum absorptive population factor.

An incoherent reset/work source can restore readiness but cannot make the weak absorptive transition stronger than the fully ready passive case.

To leave this passive envelope the detector must produce signal-transition inversion or another coherent/parametric active process. Then the pump/free-energy source becomes part of the optical resource and the passive theorem no longer applies by itself.

---

## 15. Current claim boundary

### Established within explicit stated models

1. Geometric active volume alone is not a universal optical resource.
2. Finite absorber count alone does not impose a one-photon speed ceiling.
3. Finite passive-network integrated optical-to-detector transfer obeys the exact harmonic access bound.
4. Ideal direct feedthrough is an additional broadband boundary resource.
5. Structured passive reservoirs inherit the harmonic bound under finite-budget `H2`-convergent embeddings.
6. A restricted one-free-space-channel optical ceiling converts desired capture bandwidth/efficiency into minimum receiving-side access.
7. Thermal detailed balance converts finite forward detector access into reverse-activation / energy-bias constraints.
8. In the unified three-level testbed, stored ready-state energy can amplify click energy without increasing conditional capture beyond rate matching.
9. Gross forward click rate and net thermodynamic detector current are distinct when reverse jumps exist.
10. Incoherent readiness pumping does not increase a non-inverted signal transition beyond the fully ready absorptive population factor.

### Explicitly not established

- a universal efficiency-bandwidth-dark-count-entropy theorem;
- novelty of the harmonic access theorem;
- novelty of the capture-to-click compositions;
- a universal mapping from net detector current to gross click counts;
- a universal thermodynamic work cost for `A_r`;
- a theorem for coherent/parametric/gain-assisted capture;
- a material-specific infrared limit;
- publication priority of the narrowed capture-plus-thermodynamics junction.

---

## 16. Current frontier

The passive/absorbing capture + autonomous readiness branch is sufficiently mapped for now.

Before opening a coherent active-capture branch, perform a focused publication-level prior-art assessment of the **combined** structure:

```text
propagating spectral capture
+
passive access/bandwidth resource
+
autonomous detector readiness/amplification/reset
+
internal dark current
+
external background counts
+
gross click versus net-current observables.
```

If the junction remains distinct enough to justify further development, the next technical calculation is an explicitly active/coherently pumped input-output detector and the work/entropy resource required to broaden capture beyond the passive envelope.

Do not add HgCdTe-specific transport yet.