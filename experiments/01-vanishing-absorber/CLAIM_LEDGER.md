# Claim Ledger — Experiment 01

**Updated:** 2026-08-08  
**Status:** exploratory; passive access theorem connected to an autonomous detector testbed; major 2018/2026 prior-art boundary identified; no novelty claim  
**Purpose:** distinguish established prior theory, internal derivations, invalidated routes, conditional compositions, and open claims.

---

## 1. Active organizing question

The original target was

```math
V_a\to0,
\qquad
\eta\to1,
\qquad
B\to\infty,
\qquad
\mathrm{noise}\to0.
```

The surviving organizing variables are instead

```text
propagating optical access
+
irreversible detector access
+
ready-state/reset resource
+
external background admission
+
internal detector false events.
```

---

## 2. Prior ingredients — never claim as repository novelty

Established ingredients include

- temporal coupled-mode theory / critical coupling;
- quantum input-output photodetector modeling with incoming few-photon fields, absorption, amplification, dark counts and timing (Young, Sarovar & Leonard 2018);
- autonomous nonequilibrium detector thermodynamics with efficiency, gain, jitter, dead time, dark counts and entropy production (Schwarzhans et al. 2026);
- `H2` norms, Lyapunov Gramians and passive state-space theory;
- optical material-response, LDOS and power-bandwidth bounds;
- broadband thermodynamic external-coupling bounds and radiative/internal rate matching;
- multiresonant absorption bounds;
- Bode-Fano matching theory;
- reaction-coordinate / pseudomode structured-reservoir embeddings;
- deep-strong light-matter decoupling;
- Bose photon bunching;
- optical Bloch population-difference susceptibility;
- local/KMS detailed balance and unicyclic stochastic thermodynamics.

---

## 3. Invalidated general routes

### H1 — active-volume-only bound — STOPPED

`ACTIVE_VOLUME_COUNTEREXAMPLE.md` gives

```math
V_a\to0,
\qquad
\gamma_a=\mathrm{constant},
\qquad
\gamma_a/V_a\to\infty
```

under admitted ideal field concentration.

Therefore generic

```text
eta^2 B <= C V_a
```

or passivity-only bounded `gamma_a/V_a` are stopped.

### H2 — finite absorber count as missing one-photon speed limit — STOPPED

One-photon dynamics stays linear in the accessible one-excitation sector.

### H3 — largest multimode coupling as universal control parameter — STOPPED

A disconnected/spectator strong-coupling sector is a counterexample.

### H4 — all-frequency harmonic theorem with arbitrary ideal feedthrough — INVALID EXTENSION

A constant prompt transfer path has infinite Markov bandwidth and makes total all-frequency `H2` area diverge.

### H5 — generic autonomous three-state detector as novelty target — STOPPED

Schwarzhans et al. (2026) already provide a richer autonomous detector thermodynamics framework.

### H6 — generic incoming-field capture + amplification as novelty target — STOPPED

Young, Sarovar & Leonard (2018) already treat the quantized photon field, absorption and amplification as one coupled detector system.

---

## 4. Supporting one-port / thermal-input results

### D1 — one-port absorbed-power bandwidth

```math
\boxed{
B_{3\rm dB}
=\frac{\gamma_e+\gamma_a}{2\pi}.
}
```

At critical coupling, `B_3dB = gamma_a/pi`.

### D2 — toy bulk-dark-event optimum

For the stated Poisson bulk-event metric,

```math
\gamma_e=2\gamma_a,
\qquad
A_0=8/9
```

maximizes the chosen sensitivity-speed metric. Not universal.

### D3 — one thermal optical channel

Exact Bose counting gives

```math
\boxed{
\mathcal C_{\rm th,max}^2
=\frac1{\pi\bar n(2+\bar n)}
}
```

at critical coupling. This is external thermal-background physics, not internal dark counts.

---

## 5. Supporting microscopic/nonperturbative results

### D4 — finite transition / LDOS conditional ceiling

Finite bandwidth-averaged coupling is bounded when passive material response, finite bandwidth, admissible environment and nonzero emitter-environment separation are fixed.

### D5 — finite emitter form factor

Finite transition density regularizes the point-dipole ultraviolet divergence.

### D6 — oscillator-strength/extent insufficiency

Those weak-coupling inequalities do not close the problem before the formal enhanced rate reaches `O(omega_0)`.

### D7 — deep-strong Hopfield narrowing

A dressed resonance can remain rate matched while its useful transfer linewidth collapses as internal coupling increases. Mechanism strongly overlaps established deep-strong decoupling.

### D8 — fixed-target Hopfield retuning theorem

For fixed lower dressed target frequency and fixed local reservoir resources,

```math
\boxed{
\min(\Gamma_L,\Gamma_R)\to0
\quad(g\to\infty).
}
```

Peak transfer and linewidth cannot both stay bounded away from zero for the resolved target mode.

**Status:** candidate distinct supporting lemma; priority unproven.

### D9 — reservoir compensation cost

For target peak transfer `eta_*` and linewidth `W_*`, with

```math
\Gamma_*
=\frac{W_*}{4}
\left(1-\sqrt{1-\eta_*}\right),
```

one needs

```math
\boxed{
\max(\gamma_L,\gamma_R)
\ge
\Gamma_*\sqrt{1+2g/\omega_t}.
}
```

---

## 6. Canonical finite passive multimode theorem

For a stable finite passive strictly proper network,

```math
L=\operatorname{Tr}\Gamma_L,
\qquad
R=\operatorname{Tr}\Gamma_R,
```

and

```math
\mathcal I_{L\to R}
=
\int\frac{d\omega}{2\pi}
\operatorname{Tr}[G_{RL}^\dagger G_{RL}],
```

### D10 — exact Gramian decomposition

```math
\boxed{
\frac{\mathcal I_{L\to R}}2
=
\sum_i
\frac{\ell_i r_i}
{\ell_i+r_i+\iota_i}.
}
```

### D11 — harmonic access bound

```math
\boxed{
\mathcal I_{L\to R}
\le
\frac{2LR}{L+R}.
}
```

A single passive resonance saturates it.

### D12 — equality condition

Saturation requires no participating parasitic loss and

```math
\ell_i/r_i=L/R
```

for every transfer-active Gramian direction.

### D13 — finite-band access floor

```math
\boxed{
\overline T_B
\le
\frac{4\pi LR}{W(L+R)}.
}
```

Therefore `Tbar_B >= T_*` requires

```math
\boxed{
\frac{LR}{L+R}
\ge
\frac{T_*W}{4\pi}.
}
```

**Status:** exact internally derived detector-facing passivity corollary; mathematical ingredients prior; novelty unassessed and not claimed.

---

## 7. Feedthrough and continuum scope results

### D14 — ideal direct feedthrough defeats all-frequency finite `H2`

For

```math
G_{RL}=D_{RL}+G_{\rm res}
```

with nonzero constant `D_RL`, total all-frequency transfer area diverges.

### D15 — finite-band prompt + resonant accounting

```math
\boxed{
\sqrt{\mathcal I_B}
\le
\sqrt{\frac{W}{2\pi}}\,\|D_{RL}\|_F
+
\sqrt{\frac{2LR}{L+R}}.
}
```

### D16 — conditional structured-reservoir extension

If finite passive augmented realizations converge in `H2` and terminal access budgets converge to finite `L,R`, then

```math
\boxed{
\|G\|_{H2}^2
\le
\frac{2LR}{L+R}.
}
```

---

## 8. Restricted optical-to-thermal bridge

Prior one-free-space-channel thermodynamic coupling theory gives, in repository amplitude-rate convention,

```math
\boxed{
L_B\le\frac{W}{4\pi}.
}
```

### D17 — receiving-side access requirement

```math
\boxed{
\overline T_B
\le
\frac{R_B}{R_B+W/(4\pi)}
}
```

and target `Tbar_B >= eta` requires

```math
\boxed{
R_B
\ge
\frac{\eta}{1-\eta}
\frac{W}{4\pi}.
}
```

Strong prior-art overlap; not claimed as new rate matching.

### D18 — thermal irreversibility

For localization energy release `Delta`,

```math
\frac{k_\uparrow}{k_\downarrow}
=e^{-\Delta/(k_BT)}.
```

With `k_down=2R_B`,

```math
\boxed{
k_\uparrow
\ge
\frac{\eta}{1-\eta}
\frac{W}{2\pi}
e^{-\Delta/(k_BT)}.
}
```

For `k_up <= D_rev`,

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

when applicable.

`D_rev` is reverse activation, not automatically a measured dark-count rate.

---

## 9. Prior-art boundary at the current frontier

### K1 — Young, Sarovar & Leonard (2018)

Already covers incoming quantized few-photon fields, absorption, amplification, detector configurations, efficiency, dark counts and timing in one quantum framework.

### K2 — Schwarzhans et al. (2026)

Already covers autonomous nonequilibrium detector preparation/amplification/reset, entropy production, internal dark counts, efficiency, jitter and dead time.

Their transient event model treats the target excitation as present in a target system rather than deriving a propagating optical capture spectrum, and their discussion identifies capture as outside the thermodynamic stage analyzed.

### C1 — narrowed candidate junction

A targeted search has not found a primary source that simultaneously imposes

```text
propagating spectral capture/access constraints
+
autonomous thermodynamic detector work/reset/dark-count accounting.
```

**Status:** candidate gap; negative search result only; priority unproven.

---

## 10. Capture-to-click composition results

Let `eta_D` be conditional click efficiency after successful capture.

### D19 — serial external efficiency ceiling

```math
\boxed{
\overline\eta_{\rm ext}
\le
\eta_D
\frac{R_C}{R_C+W/(4\pi)}.
}
```

Thus target `eta_*` requires

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

### D20 — admitted external background mean rate

For one flat thermal channel,

```math
\boxed{
R_{\rm bg}
=
\bar n_B
\frac{W}{2\pi}
\overline\eta_{\rm ext}.
}
```

These are real input photons, not internal dark counts.

Serial factorization is a reference limit, not a general dynamically coupled detector theorem.

---

## 11. Unified three-level capture-machine results

Use states

```text
|0> reset/ground
|1> detection-ready
|2> optically activated.
```

### D21 — ready-state frequency-converting single-photon capture

```math
\boxed{
T_{L\to R}(\omega)
=
\frac{4\Gamma_L\Gamma_R}
{(\omega-\omega_L)^2
+(\Gamma_L+\Gamma_R+\Gamma_I)^2}.
}
```

Output energy obeys

```math
\boxed{
\hbar\omega_R
=\hbar\omega_L+(E_1-E_0).
}
```

Stored ready-state free energy can amplify click energy without removing optical/detector rate matching.

### D22 — exact reversible steady state

For rates `u,d,a,b,c,e`,

```math
Z=ac+ae+au+bd+be+bu+cd+cu+de,
```

```math
p_0=(ac+bd+cd)/Z,
```

```math
p_1=(be+bu+cu)/Z,
```

```math
p_2=(ae+au+de)/Z.
```

### D23 — gross forward click versus net current

```math
\boxed{
R_+
=\frac{c(ae+au+de)}{Z}
}
```

while

```math
\boxed{
J_D
=\frac{uac-dbe}{Z}.
}
```

Thus `R_+ != J_D` when reverse detector jumps are non-negligible.

At zero cycle affinity, net current can vanish while forward/reverse jump activity remains finite.

**Interpretation:** an event-resolved click observable and a net thermodynamic current are not interchangeable without a readout definition.

### D24 — minimal internal gross-dark-click rate

With no signal/background upward optical events (`a=0`),

```math
\boxed{
R_{\rm dc,int}^{(+)}
=
\frac{cde}
{bd+be+bu+cd+cu+de}.
}
```

This is specific to the gross-forward-jump readout definition of this minimal cycle.

---

## 12. Readiness and NESS optical response

### D25 — ready-state occupation from reset bias

For isolated reset pair `u:0->1`, `d:1->0`,

```math
\boxed{
p_{\rm r}
=\frac{1}{1+e^{-\mathcal A_r}},
\qquad
\mathcal A_r=\ln(u/d).
}
```

### D26 — readiness-bandwidth composition

In the dilute serial limit,

```math
\boxed{
\overline\eta_{\rm ext}
\le
\frac{\eta_D}{1+e^{-\mathcal A_r}}
\frac{R_C}{R_C+W/(4\pi)}.
}
```

This is a restricted rate-bias relation, not a universal entropy/work bound.

### D27 — weak optical susceptibility about NESS

For the signal transition,

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

Thus incoherent readiness pumping cannot make the absorptive population factor exceed the fully ready passive state.

To leave the passive envelope requires optical inversion/coherent active capture, at which point pump/free-energy resources must enter the optical accounting.

---

## 13. Explicit non-claims

Do not claim

- a universal sensitivity-speed-dark-count-entropy theorem;
- novelty of the harmonic access theorem;
- novelty of serial capture-to-click factorization;
- that gross forward clicks are always the correct detector observable;
- that net thermodynamic current is always the correct click observable;
- a universal work cost for reset affinity `A_r`;
- that every autonomous detector has a passive/non-inverted signal transition;
- a theorem for coherent/parametric/gain-assisted capture;
- a material-specific IR limit;
- publication priority of the capture-plus-thermodynamics junction.

---

## 14. Current frontier

Before opening the explicitly active/coherent capture branch, perform a publication-level prior-art assessment of the combined passive/autonomous structure.

If the junction remains scientifically distinct, the next technical target is:

> **Can coherent or parametric pump work broaden propagating-photon capture beyond the passive harmonic envelope while preserving irreversible click probability, and what work/entropy resource must scale with that gain-assisted bandwidth?**