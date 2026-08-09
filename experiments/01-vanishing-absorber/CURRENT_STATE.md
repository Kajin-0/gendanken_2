# Current State — Experiment 01: The Vanishing Absorber

**Date:** 2026-08-08  
**Status:** exploratory; harmonic passive-access theorem derived; direct/continuum loopholes audited; first optical-to-thermal resource chain derived; no novelty claim  

## 1. Guiding question

Can an ideal photodetector be made arbitrarily small, arbitrarily fast, arbitrarily sensitive, and still absorb essentially every incident photon?

The project does not assume the answer is no.

The logic has moved away from geometric active volume toward the more durable requirement

```text
useful optical access
+
irreversible detector/material access.
```

A detector needs both.

---

## 2. Canonical frontier

Read after root `AGENTS.md`:

1. `PASSIVE_MULTIMODE_TRANSFER_AREA_BOUND.md`
2. `DIRECT_FEEDTHROUGH_AND_BAND_LIMIT.md`
3. `STRUCTURED_RESERVOIR_ACCESS_AUDIT.md`
4. `THERMODYNAMIC_OPTICAL_ACCESS_BRIDGE.md`
5. `THERMAL_IRREVERSIBILITY_COST.md`
6. `HOPFIELD_RESERVOIR_RESOURCE_COST.md`
7. `HOPFIELD_RETUNING_NO_GO.md`
8. older stages only for provenance.

`CLAIM_LEDGER.md` defines the epistemic boundary.

---

## 3. Major earlier routes that failed

### Geometric active volume

An explicit shrinking-gap passive continuum model can retain finite optical participation and finite absorptive decay while

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

For one incident photon, a two-level absorber remains linear in the one-excitation sector. Finite absorber count / saturation alone does not impose a single-photon speed ceiling in the Markov/RWA model.

### Weak-coupling oscillator-strength route

Finite transition extent regularizes the literal point-dipole divergence, but oscillator-strength and extent constraints do not close the problem before the enhanced decay estimate reaches

```math
\Gamma/\omega_0=O(1),
```

where the weak-coupling Purcell/Markov picture fails.

These failures forced the analysis into nonperturbative light-matter coupling and then general passive-network theory.

---

## 4. Supporting nonperturbative Hopfield result

For a TRK-consistent two-mode Hopfield model, hold the lower polariton at a fixed target

```math
\omega_y=\omega_t>0
```

while retuning the bare frequencies and sending internal coupling

```math
g\to\infty.
```

For fixed positive local optical and detector bath scales,

```math
\boxed{
\min(\Gamma_L,\Gamma_R)\to0.
}
```

Thus peak transfer and linewidth cannot both remain bounded away from zero for a resolved target polariton.

If reservoir engineering is allowed to compensate, achieving

```math
T_0\ge\eta_*,
\qquad
\Delta\omega_{\rm FWHM}\ge W_*
```

requires each dressed access rate to exceed

```math
\Gamma_*
=
\frac{W_*}{4}
\left(1-\sqrt{1-\eta_*}\right),
```

and at least one bare reservoir resource satisfies

```math
\boxed{
\max(\gamma_L,\gamma_R)
\ge
\Gamma_*
\sqrt{1+2g/\omega_t}.
}
```

This is a model-level supporting lemma with substantial deep-strong-coupling prior-art overlap. Priority is unproven.

---

## 5. Exact finite passive multimode harmonic-access theorem

For an arbitrary finite stable passive linear network with no direct optical-to-detector feedthrough,

```math
A=-iH-(\Gamma_L+\Gamma_R+\Gamma_I),
\qquad
H=H^\dagger,
```

and transfer

```math
G_{RL}(s)=C_R(sI-A)^{-1}B_L,
```

where

```math
B_LB_L^\dagger=2\Gamma_L,
\qquad
C_R^\dagger C_R=2\Gamma_R,
```

define

```math
L=\operatorname{Tr}\Gamma_L,
\qquad
R=\operatorname{Tr}\Gamma_R.
```

Then

```math
\boxed{
\mathcal I_{L\to R}
\equiv
\int_{-\infty}^{\infty}
\frac{d\omega}{2\pi}
\operatorname{Tr}
[G_{RL}^\dagger(i\omega)G_{RL}(i\omega)]
\le
\frac{2LR}{L+R}.
}
```

The bound is independent of finite internal mode count, modal overlap, coherent Hermitian topology, Fano interference, and passive parasitic loss.

A single passive resonance saturates it exactly.

In the controllability-Gramian eigenbasis,

```math
\boxed{
\frac{\mathcal I_{L\to R}}2
=
\sum_i
\frac{\ell_i r_i}
{\ell_i+r_i+\iota_i}.
}
```

Equality requires no participating parasitic loss and a common optical-to-detector access ratio

```math
\ell_i/r_i=L/R.
```

This is the aggregate multimode analogue of rate matching.

Mathematical ingredients are standard `H2`/Lyapunov/passive-systems theory; novelty is not claimed.

---

## 6. Fixed-band access requirement

For angular-frequency band width `W`, define

```math
\overline T_B
=
\frac1W
\int_B
\operatorname{Tr}(G_{RL}^\dagger G_{RL})\,d\omega.
```

Then

```math
\boxed{
\overline T_B
\le
\frac{4\pi LR}{W(L+R)}.
}
```

Demanding

```math
\overline T_B\ge T_*
```

requires

```math
\boxed{
\frac{LR}{L+R}
\ge
\frac{T_*W}{4\pi}.
}
```

Thus broadband transfer requires aggregate external access proportional to bandwidth. Internal mode proliferation can redistribute transfer but cannot create unlimited integrated transfer at fixed `L,R`.

---

## 7. Direct feedthrough is a genuine new resource

Allow

```math
G_{RL}(i\omega)
=D_{RL}+G_{\rm res}(i\omega).
```

If `D_RL != 0` is frequency independent, the total all-frequency `H2` area diverges because an ideal feedthrough has no high-frequency rolloff.

Therefore the no-feedthrough assumption is essential to a finite all-frequency theorem.

Over a finite band of angular width `W`, however,

```math
\boxed{
\sqrt{\mathcal I_B}
\le
\sqrt{\frac{W}{2\pi}}\,\|D_{RL}\|_F
+
\sqrt{\frac{2LR}{L+R}}.
}
```

The resonant excess

```math
G_{\rm res}=G_{RL}-D_{RL}
```

still obeys the harmonic theorem.

Interpretation: direct transfer does not defeat the resource picture for free; it introduces a new resource—prompt channel strength and usable bandwidth.

---

## 8. Structured/non-Markovian reservoirs

A structured reservoir can often be represented by moving collective environmental modes into an enlarged system and leaving a simpler residual bath.

For every finite passive embedding,

```math
\|G_n\|_{H2}^2
\le
\frac{2L_nR_n}{L_n+R_n}.
```

If

```math
G_n\to G \quad\text{in }H2,
```

and

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

Thus spectral complexity alone is not an escape under finite passive embedding assumptions.

A continuum escape must involve at least one of

- direct/high-frequency feedthrough;
- divergent terminal access budget;
- failure of `H2` convergence;
- a residual bath that cannot be reduced to bounded passive terminal access;
- active, nonlinear, or time-varying physics.

This is a conditional limit argument, not a universal continuum theorem.

---

## 9. Restricted thermodynamic optical-access bridge

Yu, Raman & Fan's prior thermodynamic light-coupling result bounds, for one free-space radiation channel and modes in angular-frequency interval `W`, the sum of **energy-decay** rates by

```math
\sum_m\gamma_{m,n}
\le
\frac{W}{2\pi}.
```

The repository uses amplitude-decay rates,

```math
\gamma_{\rm energy}=2\Gamma_{\rm amplitude},
```

so the optical access budget satisfies

```math
\boxed{
L_B\le\frac{W}{4\pi}.
}
```

Combining this prior one-sided optical ceiling with the harmonic two-access theorem gives, under the stated modal/band assumptions,

```math
\boxed{
\overline T_B
\le
\frac{R_B}
{R_B+W/(4\pi)}.
}
```

Therefore achieving

```math
\overline T_B\ge\eta
```

requires

```math
\boxed{
R_B
\ge
\frac{\eta}{1-\eta}
\frac{W}{4\pi}.
}
```

This is a restricted necessary detector-reservoir access requirement, not a universal photodetector theorem.

There is strong prior-art overlap: thermodynamic external-coupling bounds and radiative/internal rate matching in broadband absorption are established theory, including modern overlapping-resonance generalizations.

---

## 10. Thermal irreversibility is not a free one-way sink

Model the detector localization transition

```text
|e> -> |d>
```

with energy release

```math
\Delta=E_e-E_d>0
```

into a thermal reservoir at temperature `T`.

Local detailed balance gives

```math
\boxed{
\frac{k_\uparrow}{k_\downarrow}
=e^{-\Delta/(k_BT)}.
}
```

For the minimal convention

```math
k_\downarrow=2R_B,
```

the broadband access requirement implies

```math
\boxed{
k_\downarrow
\ge
\frac{\eta}{1-\eta}
\frac{W}{2\pi}.
}
```

Hence

```math
\boxed{
k_\uparrow
\ge
\frac{\eta}{1-\eta}
\frac{W}{2\pi}
\exp[-\Delta/(k_BT)].
}
```

If the allowed reverse thermal-activation rate is

```math
k_\uparrow\le D_{\rm rev},
```

then necessarily

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

`D_rev` is **not automatically a dark-count rate**. A cyclic detector model is required to decide whether reverse activation produces a recorded false event.

---

## 11. What is now established versus open

### Established within explicit models

1. Geometric active volume alone is not a universal optical resource.
2. Finite absorber count alone does not impose a one-photon speed ceiling in the linear one-excitation regime.
3. The exact finite-passive-network transfer area is bounded by the harmonic mean `2LR/(L+R)`.
4. Ideal direct feedthrough defeats an all-frequency finite `H2` bound by inserting infinite bandwidth; its finite-band contribution must be counted separately.
5. Passive structured reservoirs inherit the harmonic theorem under finite-budget `H2`-convergent embeddings.
6. In the restricted one-free-space-channel model, a thermodynamic optical-coupling ceiling converts desired broadband transfer into a minimum detector-reservoir access.
7. In a minimal thermal detector transition, detailed balance converts that access requirement into a reverse-activation / energy-bias constraint.

### Explicitly not established

- a universal sensitivity-speed-dark-count theorem;
- a universal Maxwell bound on direct detector feedthrough;
- a universal bound on `R_B` for arbitrary materials/reservoirs;
- equivalence of reverse activation and observable dark counts;
- a minimum reset work;
- a theorem for active/time-varying/nonlinear detectors;
- publication novelty of the combined access-resource chain.

---

## 12. Current frontier — complete minimal detector cycle

The next decisive model is

```text
|g> -- photon --> |e>
|e> -- detector bath --> |d>
|d> -- readout/reset --> |g>.
```

It must define

1. forward and reverse `e <-> d` thermal rates;
2. what physical transition constitutes a recorded count;
3. explicit reset dynamics and its reservoir/work source;
4. false-count pathways without an input photon;
5. steady-state count statistics and dead time;
6. the connection between optical access `L`, detector access `R`, efficiency, bandwidth, and observable dark counts.

Only after this cycle is solved should the project decide whether the current chain can support a detector-specific theoretical paper.

Do not add HgCdTe-specific transport yet.