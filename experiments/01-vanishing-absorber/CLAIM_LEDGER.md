# Claim Ledger — Experiment 01

**Updated:** 2026-08-08  
**Status:** exploratory; multiple naive bounds invalidated; exact finite-passive-network harmonic access bound derived; no novelty claim  
**Purpose:** distinguish prior theory, internal derivations, invalidated routes, candidate distinct lemmas, and explicit non-claims.

---

## 1. Active organizing question

The original detector question was

```math
V_a\to0,
\qquad
\eta\to1,
\qquad
B\to\infty,
\qquad
\mathrm{noise}\to0?
```

The active resource is no longer geometric volume.

The strongest current organizing concept is

```text
optical access
+
irreversible detector/material access.
```

---

## 2. Prior ingredients — not repository novelty

Do not claim priority for:

- one-port temporal coupled-mode theory or critical coupling;
- `H_2` norms, Lyapunov Gramians, or passive state-space realizations;
- optical material-response / bandwidth-averaged LDOS bounds;
- deep-strong light-matter decoupling / breakdown of the Purcell effect;
- dark-state quantum photodetector architectures;
- multimode/quasinormal-mode broadband absorption bounds;
- Bose thermal photon bunching.

---

## 3. Derived supporting results

### D1 — One-port detector modulation bandwidth

Canonical file: `ONE_PORT_RESONATOR_DYNAMICS.md`.

```math
\boxed{
B_{3\rm dB}
=\frac{\gamma_e+\gamma_a}{2\pi}.
}
```

At critical coupling,

```math
\gamma_e=\gamma_a,
\qquad
A_0=1,
\qquad
B_{3\rm dB}=\gamma_a/\pi.
```

### D2 — Independent bulk-dark-event toy optimum

Under the stated Poisson bulk-event model,

```math
\gamma_e=2\gamma_a,
\qquad
A_0=8/9
```

optimizes the chosen sensitivity-speed metric.

This is not universal.

### D3 — Thermal input-channel result

Canonical file: `THERMAL_INPUT_CHANNEL.md`.

For one thermal signal/background channel,

```math
\boxed{
\mathcal C_{\rm th,max}^2
=\frac1{\pi\bar n(2+\bar n)}
}
```

at critical coupling.

This is not an internal-dark-count theorem.

---

## 4. Invalidated volume route

Canonical file: `ACTIVE_VOLUME_COUNTEREXAMPLE.md`.

An explicit ideal continuum family has

```math
V_a\to0,
\qquad
\gamma_a=\text{constant},
\qquad
\gamma_a/V_a\to\infty.
```

### H1 — STOPPED

```text
passivity alone bounds gamma_a/V_a
```

is false in the admitted local-linear continuum model with arbitrary ideal field concentration.

### H2 — STOPPED

A universal active-volume-only law of the form

```text
eta^2 B <= C V_a
```

is unsupported and should not be revived without new explicit constraints on the full environment or microscopic material resources.

---

## 5. Invalidated finite-absorber route

Canonical file: `MICROSCOPIC_SINGLE_TRANSITION.md`.

For one photon, a two-level absorber remains linear in the one-excitation sector.

### H3 — STOPPED

Finite absorber number / saturation alone is not the missing one-photon speed limit in the Markov/RWA model.

---

## 6. Weak-coupling microscopic results

Canonical files:

- `FINITE_TRANSITION_LDOS_BANDWIDTH_BOUND.md`
- `FINITE_EMITTER_FORM_FACTOR.md`
- `OSCILLATOR_STRENGTH_EXTENT_STRESS_TEST.md`

### D4 — Conditional LDOS bandwidth ceiling

Finite bandwidth-averaged coupling is bounded when passive material response, allowed environment, finite bandwidth, and nonzero emitter-environment separation are fixed.

### D5 — Finite-emitter regularization

Finite transition density regularizes the literal point-dipole ultraviolet divergence.

### D6 — Insufficiency of oscillator-strength/extent inequalities alone

Those inequalities do not close the perturbative problem before the formal rate reaches `O(omega_0)`, where the Markov/Purcell picture ceases to be controlled.

This is an insufficiency result, not an achievable-divergence claim.

---

## 7. Nonperturbative Hopfield results

Canonical files:

- `NONPERTURBATIVE_HOPFIELD_CAPTURE.md`
- `HOPFIELD_RETUNING_NO_GO.md`

### D7 — Symmetric deep-strong transfer narrowing

Equal local bath scales give matched dressed rates

```math
\Gamma_{\pm,L}
=\Gamma_{\pm,R}
=\frac{\gamma}
{2\sqrt{1+(g/\omega_0)^2}}.
```

Peak transfer may stay at one while transfer linewidth collapses.

This mechanism is established prior deep-strong decoupling physics.

### D8 — Fixed-target retuning theorem

Hold

```math
\omega_y=\omega_t>0
```

while retuning bare frequencies and taking `g -> infinity`.

For fixed local optical and detector bath resources,

```math
\boxed{
\min(\Gamma_L,\Gamma_R)\to0.
}
```

Thus resolved peak transfer and linewidth cannot both stay bounded away from zero.

**Status:** candidate distinct supporting lemma; priority unproven.

No inspected source in the targeted sweep stated the exact fixed-target two-reservoir retuning result. That is a negative search result only.

---

## 8. Reservoir-compensation resource result

Canonical file: `HOPFIELD_RESERVOIR_RESOURCE_COST.md`.

If

```math
T_0\ge\eta_*>0,
\qquad
\Delta\omega_{\rm FWHM}\ge W_*>0,
```

then

```math
\Gamma_*
=\frac{W_*}{4}
\left(1-\sqrt{1-\eta_*}\right)
```

is the required minimum dressed access rate.

Across every allowed fixed-target bare-frequency retuning,

```math
\boxed{
\max(\gamma_L,\gamma_R)
\ge
\Gamma_*
\sqrt{1+2g/\omega_t}.
}
```

The `sqrt(g)` asymptotic scaling is sharp within the two-mode model.

This is not a universal strong-reservoir theorem.

---

## 9. Multimode escape audit

Canonical file: `MULTIMODE_ESCAPE_AUDIT.md`.

### H4 — STOPPED naive multimode statement

A theorem based only on

```text
largest internal coupling anywhere in the full system -> infinity
```

is false because a spectator sector can carry that coupling without affecting the useful detector block.

### D9 — Mode density is an explicit resource

A growing bank of narrow matched resonances can preserve finite integrated/broadband response if useful resonance count/density increases sufficiently rapidly.

This motivated replacing individual linewidth by frequency-integrated transfer.

---

## 10. Canonical passive multimode theorem

Canonical file: `PASSIVE_MULTIMODE_TRANSFER_AREA_BOUND.md`.

Consider a finite stable passive linear system

```math
A=-iH-(\Gamma_L+\Gamma_R+\Gamma_I),
\qquad
H=H^\dagger,
```

with

```math
B_LB_L^\dagger=2\Gamma_L,
\qquad
C_R^\dagger C_R=2\Gamma_R,
```

and no direct `L -> R` feedthrough.

Let

```math
L=\operatorname{Tr}\Gamma_L,
\qquad
R=\operatorname{Tr}\Gamma_R.
```

Define

```math
\mathcal I_{L\to R}
=
\int_{-\infty}^{\infty}
\frac{d\omega}{2\pi}
\operatorname{Tr}
\left[G_{RL}^\dagger(i\omega)G_{RL}(i\omega)\right].
```

### D10 — Exact Gramian-basis decomposition

If `Q_L` is the controllability Gramian and `ell_i`, `r_i`, `iota_i` are the diagonal optical/detector/parasitic rates in its eigenbasis, then

```math
\boxed{
q_i
=\frac{\ell_i}
{\ell_i+r_i+\iota_i}
}
```

and

```math
\boxed{
\frac{\mathcal I_{L\to R}}2
=
\sum_i
\frac{\ell_i r_i}
{\ell_i+r_i+\iota_i}.
}
```

The internal Hamiltonian disappears from this diagonal energy-partition identity.

### D11 — Exact harmonic access bound

Cauchy-Schwarz gives

```math
\boxed{
\mathcal I_{L\to R}
\le
\frac{2LR}{L+R}.
}
```

This is stronger than the earlier loose bound

```math
\mathcal I_{L\to R}
\le2\min(L,R),
```

which is now historical only.

The harmonic bound is tight; one passive internal resonance saturates it exactly.

### D12 — Equality structure

Saturation requires no participating parasitic loss and a common access ratio across every transfer-active Gramian direction:

```math
\boxed{
\ell_i/r_i=L/R.
}
```

This is the aggregate multimode analogue of rate matching.

### D13 — Fixed-band access floor

For target angular bandwidth `W`,

```math
\boxed{
\overline T_B
\le
\frac{4\pi LR}{W(L+R)}.
}
```

Thus

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

For matched total budgets `L=R=Gamma_access`,

```math
\boxed{
\Gamma_{\rm access}
\ge
\frac{T_*W}{2\pi}.
}
```

This is an external-access resource law, not an absolute bandwidth limit.

**Status:** exact internally derived passivity corollary. The mathematical ingredients (`H_2`, Lyapunov, scattering passivity) are prior theory. No novelty claim is made.

---

## 11. Verification

### V1

`numerics/one_port_time_domain_check.py` independently checks the one-port modulation response.

### V2

`numerics/passive_multimode_h2_stress.py` checks

- `0 <= Q_L <= I`;
- the exact Gramian-eigenbasis identity;
- the harmonic transfer-area bound;
- exact single-mode saturation;
- direct numerical frequency integration for a representative multimode system.

A private 4,000-network stress test across dimensions `1,2,4,8` found no violation; the diagonal identity agreed to roughly `3e-15` in the sampled networks.

---

## 12. Explicit non-claims

Do **not** claim that:

- active volume fundamentally limits detector bandwidth;
- finite absorber count fundamentally limits one-photon bandwidth;
- the fixed-target Hopfield theorem is novel or universal;
- the harmonic access theorem is novel;
- mode count cannot improve broadband response;
- the harmonic theorem covers direct feedthrough, active gain, time variation, nonlinear/saturating dynamics, or all infinite-dimensional reservoirs;
- the abstract access traces have already been mapped to HgCdTe or another semiconductor material limit;
- the project is ready for a manuscript.

---

## 13. Current organizing statement

Within the finite passive linear class:

> **Internal electromagnetic complexity can redistribute useful detector transfer in frequency, but it cannot replace simultaneous access to the optical input and irreversible detector reservoirs. The full frequency-integrated transfer is bounded by the harmonic mean of their aggregate access budgets.**

This is the strongest surviving model-level structure.

It is not yet a novelty claim.

---

## 14. Next promotion criteria

Before any manuscript decision:

1. search passive network, microwave matching, quantum linear-system, and scattering literature specifically for the harmonic trace inequality;
2. test whether direct finite-band feedthrough admits a clean resource extension;
3. test genuinely infinite-dimensional / strongly structured passive reservoirs;
4. map `L` and `R` onto microscopic detector resources;
5. then add dark-event, thermal reverse-rate, amplification, and reset thermodynamics;
6. only after those attacks reassess publication significance.