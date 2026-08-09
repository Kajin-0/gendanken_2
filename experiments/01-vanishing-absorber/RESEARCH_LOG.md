# Research Log — Experiment 01: The Vanishing Absorber

This file is chronological. It records why the research direction changed, including failed conjectures and superseded intermediate results.

---

## 2026-08-08 — Experiment opened

Question:

> Can an ideal photodetector be made arbitrarily small, arbitrarily fast, arbitrarily sensitive, and still absorb essentially every incident photon?

Initial idea:

```text
smaller active volume
-> fewer bulk dark events

passive optical confinement
-> recover absorption

possible penalty
-> longer photon dwell time / less bandwidth.
```

The schematic relation

```text
eta^2 B <= C V
```

was treated only as a conjectural target.

Decision: derive the simplest one-port resonator exactly before generalizing.

---

## 2026-08-08 — One-port resonator closed at stated assumptions

Derived

```math
A(\omega)
=
\frac{4\gamma_e\gamma_a}
{(\omega-\omega_0)^2+(\gamma_e+\gamma_a)^2},
```

and the absorbed-power modulation bandwidth

```math
\boxed{
B_{3\rm dB}
=\frac{\gamma_e+\gamma_a}{2\pi}.
}
```

At critical coupling,

```math
A_0=1,
\qquad
B_{3\rm dB}=\gamma_a/\pi.
```

Thus the dwell-time intuition survives in terms of the **absorptive decay rate**, not yet volume.

The optical absorptance FWHM was found to be twice the absorbed-power modulation `-3 dB` bandwidth at critical coupling.

A toy independent bulk-dark-event metric was unexpectedly optimized at

```math
\gamma_e=2\gamma_a,
\qquad
A_0=8/9,
```

rather than critical coupling.

If `gamma_a proportional to V` and bulk dark events also scale with `V`, the toy metric becomes volume independent. The next branch attacked that premise.

Two convention errors were found and corrected before state promotion; neither affected the central decay-rate or coupling-optimization result.

---

## 2026-08-08 — Active-volume-only route falsified

A shrinking dielectric capacitor family was constructed with fixed capacitance and finite electric-energy participation while

```math
V_a\to0.
```

Because the field grows as the gap shrinks,

```math
\gamma_a=\text{constant}
```

can coexist with

```math
\boxed{
\gamma_a/V_a\to\infty.
}
```

Therefore passivity alone does not bound `gamma_a/V_a` when arbitrary ideal field concentration is allowed.

Direction change:

> geometric active volume is not the fundamental optical resource.

The general active-volume law was stopped.

---

## 2026-08-08 — Restricted thermal signal-channel branch

For one thermal spatial/polarization input channel, exact Bose counting including bunching gave

```math
\boxed{
\mathcal C_{\rm th,max}^2
=\frac1{\pi\bar n(2+\bar n)}
}
```

at critical coupling.

This showed that when signal and thermal background enter through the same optical channel, the absorber rate and cavity `Q` cancel from this restricted ratio.

It is a background-channel result, not an internal-dark-count theorem.

---

## 2026-08-08 — Single microscopic transition did not restore a speed limit

A two-level optical transition plus an irreversible dark detection state was analyzed.

With at most one input photon, the accessible sector remains linear. Finite absorber number / saturation therefore does not impose the hoped-for single-photon speed ceiling in the Markov/RWA model.

Prior-art collision with quantum dark-state photodetector models reinforced that no universal efficiency-dark-count-jitter tradeoff should be assumed without explicit architectural and thermodynamic resources.

Direction change: constrain the optical coupling of a finite transition.

---

## 2026-08-08 — LDOS, finite emitter extent, and oscillator-strength stress tests

Established bandwidth-averaged LDOS theory provides finite coupling enhancement when the passive environment, material response, finite bandwidth, and nonzero emitter-environment separation are fixed.

The bound still diverges as the separation tends to zero.

A finite transition-density form factor then regularized the literal point-dipole ultraviolet divergence and replaced it by a microscopic finite-size scale.

However, allowing selected oscillator strength itself to vary showed that oscillator-strength plus finite-extent inequalities do not algebraically close the weak-coupling problem. The formal enhanced rate can reach

```math
\Gamma/\omega_0=O(1),
```

exactly where the Purcell/Markov decay-rate description ceases to be controlled.

Direction change: treat light and matter nonperturbatively.

---

## 2026-08-08 — Nonperturbative Hopfield capture

A TRK-consistent two-mode Hopfield model with weak local optical and detector reservoirs was used.

For equal bare frequencies and equal local bath scales,

```math
\Gamma_{\pm,L}
=\Gamma_{\pm,R}
=\frac{\gamma}
{2\sqrt{1+(g/\omega_0)^2}}.
```

A resolved polariton can retain unit peak transfer while its linewidth collapses as

```math
\Delta\omega_{\rm FWHM}
\sim2\gamma\omega_0/g.
```

This is consistent with established deep-strong decoupling / Purcell-breakdown physics.

Counterexample proposed: retune the bare frequencies with `g` so the useful dressed pole remains at a fixed detector frequency.

---

## 2026-08-08 — Fixed-target Hopfield retuning theorem

Hold the lower polariton at

```math
\omega_y=\omega_t>0
```

while retuning bare frequencies and taking `g -> infinity`.

The exact fixed-target branch satisfies

```math
(\omega_c^2-\omega_t^2)
(\omega_b^2-\omega_t^2)
=4g^2\frac{\omega_c}{\omega_b}\omega_t^2.
```

For fixed local optical and detector bath resources, a contradiction proof gives

```math
\boxed{
\min(\Gamma_L,\Gamma_R)\to0.
}
```

Therefore resolved peak transfer and linewidth cannot both stay finite in that limit.

The symmetric retuning family keeps peak transfer at one but narrows as `g^{-1/2}`.

Interpretation:

```text
optical access
+
irreversible detector/material access
```

must both survive; infinite internal hybridization cannot substitute for both.

---

## 2026-08-08 — Fixed-target prior-art collision

The search target was the exact fixed-dressed-frequency retuning + two-reservoir statement, not generic deep-strong decoupling.

Closest inspected work establishes Purcell collapse, dressed decay suppression, heat-current suppression, and multimode decoupling.

No inspected source stated the exact theorem.

Verdict:

> **candidate distinct supporting lemma; priority unproven.**

No novelty language is allowed.

---

## 2026-08-08 — Reservoir-engineering escape quantified

The next attack allowed the bare external reservoir couplings themselves to scale with `g`.

Demand

```math
T_0\ge\eta_*,
\qquad
\Delta\omega_{\rm FWHM}\ge W_*.
```

This requires

```math
\Gamma_*
=\frac{W_*}{4}
\left(1-\sqrt{1-\eta_*}\right)
```

as a minimum dressed access rate.

Optimizing over every fixed-target retuning gives

```math
\boxed{
\max(\gamma_L,\gamma_R)
\ge
\Gamma_*
\sqrt{1+2g/\omega_t}.
}
```

Thus a reservoir-engineering escape spends an external-access resource that grows asymptotically as `sqrt(g)`.

The symmetric retuning family asymptotically saturates this scaling.

Direction change:

> stronger reservoirs are a genuine escape resource, not a free counterexample.

---

## 2026-08-08 — Multimode escape audit

A disconnected spectator sector showed that no theorem can depend only on the largest coupling anywhere in a multimode Hamiltonian.

A bank of narrow matched resonances can also recover broadband response if useful mode count/density grows as the individual widths shrink.

Thus mode density is another real resource.

This suggested replacing individual linewidth by **frequency-integrated optical-to-detector transfer**.

---

## 2026-08-08 — Preliminary passive multimode trace bound

For a finite passive Markov/LTI network with optical access matrix `Gamma_L` and detector access matrix `Gamma_R`, the transfer area was identified as an `H_2` norm.

The first Gramian/passivity proof gave

```math
\mathcal I_{L\to R}
\le
2\min(
\operatorname{Tr}\Gamma_L,
\operatorname{Tr}\Gamma_R
).
```

This was already sufficient to show that arbitrary finite internal mode count cannot create unlimited integrated transfer at fixed total boundary access.

**Status:** superseded immediately below by a sharper exact harmonic bound.

The preliminary result is retained here because it records how the stronger theorem was found.

---

## 2026-08-08 — Harmonic multimode access bound derived

The Lyapunov equation was then examined in the eigenbasis of the left controllability Gramian `Q_L`.

In that basis, the diagonal of `[H,Q_L]` vanishes exactly. If

```math
\ell_i,
\qquad
r_i,
\qquad
\iota_i
```

are the diagonal optical, detector, and parasitic-loss rates, then

```math
\boxed{
q_i
=\frac{\ell_i}
{\ell_i+r_i+\iota_i}.
}
```

Therefore the full transfer area decomposes exactly as

```math
\boxed{
\frac{\mathcal I_{L\to R}}2
=
\sum_i
\frac{\ell_i r_i}
{\ell_i+r_i+\iota_i}.
}
```

Dropping parasitic loss and applying Cauchy-Schwarz gives, with

```math
L=\operatorname{Tr}\Gamma_L,
\qquad
R=\operatorname{Tr}\Gamma_R,
```

the sharper theorem

```math
\boxed{
\mathcal I_{L\to R}
\le
\frac{2LR}{L+R}.
}
```

This is the harmonic mean of the aggregate optical and detector access budgets.

A single passive resonance saturates it exactly.

Equality in the multimode case requires no participating parasitic loss and the same optical-to-detector access ratio in every transfer-active Gramian direction:

```math
\ell_i/r_i=L/R.
```

This is the aggregate multimode analogue of critical/rate matching.

For a target angular-frequency band `W`,

```math
\boxed{
\overline T_B
\le
\frac{4\pi LR}{W(L+R)}.
}
```

For equal total access budgets,

```math
L=R=\Gamma_{\rm access},
```

a required average transfer `T_*` implies

```math
\boxed{
\Gamma_{\rm access}
\ge
\frac{T_*W}{2\pi}.
}
```

Interpretation:

> internal electromagnetic complexity can reshape the spectrum but cannot replace simultaneous access to both external sides of a finite passive detector network.

### Numerical stress test

A deterministic NumPy regression now checks

- `0 <= Q_L <= I`;
- the Gramian-basis identity above;
- the harmonic transfer bound;
- exact single-mode saturation;
- direct frequency integration for a representative multimode network.

A private 4,000-network stress test over dimensions `1,2,4,8` found no violation; the diagonal identity agreed to approximately `3e-15` in the sampled cases.

### Prior-art posture

`H_2` norms, Lyapunov Gramians, scattering-passive systems, and broadband multiresonant bounds are established mathematics/physics.

An initial targeted search has not located the exact harmonic two-access trace inequality in photodetector language.

This is **not** treated as evidence of novelty.

Current status:

> exact detector-facing passivity corollary; priority unassessed; no novelty claim.

---

## Current direction

The original active-volume question has transformed into an access-resource problem.

The strongest surviving structure is:

> **In a finite passive linear detector network, internal mode complexity can redistribute useful transfer in frequency, but the total frequency-integrated optical-to-detector transfer is bounded by the harmonic mean of the aggregate optical and irreversible detector access budgets.**

Next attacks:

1. deeper systems/network/scattering prior-art search for the harmonic trace inequality;
2. direct finite-band feedthrough/bypass accounting;
3. strongly structured and genuinely infinite-dimensional passive reservoirs;
4. microscopic mapping of the two access traces onto semiconductor detector resources;
5. only then reintegrate dark-event, reverse-rate, amplification, and reset thermodynamics;
6. manuscript decision only after those tests.