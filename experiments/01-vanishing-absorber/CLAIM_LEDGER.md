# Claim Ledger — Experiment 01

**Updated:** 2026-08-08  
**Status:** exploratory; multiple naive bounds invalidated; finite-passive-network transfer-area bound derived; no novelty claim  
**Purpose:** separate known theory, internal derivations, invalidated claims, candidate distinct lemmas, and explicit non-claims.

---

## 1. Active question

The original question remains:

```math
V_a\to0,
\qquad
\eta\to1,
\qquad
B\to\infty,
\qquad
\mathrm{noise}\to0?
```

But geometric active volume is no longer the active theoretical resource.

The current candidate organizing principle is **two-access resource accounting**:

```text
optical access
+
irreversible detector/material access.
```

---

## 2. Established prior ingredients — not repository novelty

### K1 — Temporal coupled-mode / critical-coupling theory

One-port resonant absorption, critical coupling, modal decay rates, and input-output normalization are established resonator theory.

### K2 — `H_2` norm and Lyapunov Gramians

For stable strictly proper linear systems, frequency-integrated squared transfer is the squared `H_2` norm and can be computed from controllability/observability Gramians satisfying continuous Lyapunov equations.

### K3 — Scattering-passive linear systems

Passive linear-system energy balance and passive realizations, including Maxwell and passive quantum linear systems, are established systems theory.

### K4 — Material-response and LDOS bounds

Passivity/causality impose optical-response and bandwidth-averaged LDOS bounds when the material response, admissible region, emitter separation, and excitation are specified.

### K5 — Deep-strong light-matter decoupling

Gauge-consistent ultrastrong/deep-strong coupling can suppress ordinary Purcell enhancement and external transport/decay. This is established prior physics.

### K6 — Multiresonant broadband absorption

Broadband response from overlapping resonances and spectral mode density is established contemporary absorption theory.

---

## 3. Derived one-port results

Canonical file: `ONE_PORT_RESONATOR_DYNAMICS.md`.

### D1 — Absorptance

```math
\boxed{
A(\omega)
=
\frac{4\gamma_e\gamma_a}
{(\omega-\omega_0)^2+(\gamma_e+\gamma_a)^2}.
}
```

### D2 — Absorbed-power modulation bandwidth

```math
\boxed{
B_{3\rm dB}
=
\frac{\gamma_e+\gamma_a}{2\pi}.
}
```

At critical coupling,

```math
\gamma_e=\gamma_a,
\qquad
A_0=1,
\qquad
B_{3\rm dB}=\frac{\gamma_a}{\pi}.
```

### D3 — Toy independent bulk-dark-event optimum

Under the stated Poisson bulk-event model,

```math
\mathcal C
=\frac{h\nu\sqrt{B_{3\rm dB}}}{\mathrm{NEP}}
```

is optimized at

```math
\boxed{
\gamma_e=2\gamma_a,
\qquad
A_0=\frac89.
}
```

This is model-specific, not universal.

---

## 4. Derived active-volume counterexample

Canonical file: `ACTIVE_VOLUME_COUNTEREXAMPLE.md`.

An ideal shrinking dielectric capacitor can satisfy

```math
V_a\to0,
\qquad
\gamma_a=\mathrm{constant},
```

so

```math
\boxed{
\gamma_a/V_a\to\infty.
}
```

### H1 — Invalidated claim

```text
passivity alone bounds gamma_a/V_a
```

**INVALIDATED** inside ideal local linear continuum electrodynamics when arbitrary lossless field concentration is allowed.

### H2 — Invalidated general target

```text
eta^2 B <= C V_a
```

**STOPPED** as a universal active-volume-only law.

Any future volume theorem must explicitly constrain the full concentrating environment or microscopic material resources.

---

## 5. Restricted thermal input-channel result

Canonical file: `THERMAL_INPUT_CHANNEL.md`.

For one thermal optical channel with Bose occupation `n_bar`, exact counting including bunching gives

```math
\boxed{
\mathcal C_{\rm th,max}^2
=
\frac1{\pi\bar n(2+\bar n)}
}
```

at critical coupling.

This is a **thermal input/background relation**, not an internal-dark-count theorem.

---

## 6. Microscopic absorber result and prior-art collision

Canonical file: `MICROSCOPIC_SINGLE_TRANSITION.md`.

For one incoming photon, a two-level absorber with irreversible localization remains linear in the one-excitation sector:

```math
\boxed{
A_d(\omega)
=
\frac{4\gamma_o\gamma_d}
{(\omega-\omega_0)^2+(\gamma_o+\gamma_d)^2}.
}
```

### H3 — Invalidated route

Finite absorber number / two-level saturation alone does **not** impose a single-photon speed ceiling in the Markov/RWA model.

Strong prior-art overlap with quantum dark-state detector architectures means no novelty may be claimed for rate matching or dark-state protection.

---

## 7. Finite-transition / LDOS / emitter-extent results

Canonical files:

- `FINITE_TRANSITION_LDOS_BANDWIDTH_BOUND.md`
- `FINITE_EMITTER_FORM_FACTOR.md`
- `OSCILLATOR_STRENGTH_EXTENT_STRESS_TEST.md`

### D4 — Conditional LDOS bandwidth ceiling

A finite bandwidth-averaged coupling ceiling exists when passive material response, allowed environment, and a nonzero emitter-environment separation are fixed.

This is prior-theory-based and conditional.

### D5 — Finite emitter regularization

For a finite transition density, the literal point-dipole ultraviolet divergence is regularized; a Gaussian form factor gives finite contact scaling proportional to `a^{-3}`.

### D6 — Oscillator-strength/extent insufficiency

TRK/oscillator-strength and finite-extent inequalities alone do not algebraically close the perturbative problem when the selected transition strength may vary. The formal envelope reaches `Gamma/omega = O(1)`, where weak-coupling rate theory ceases to be controlled.

This is an insufficiency result, not an achievable-divergence theorem.

---

## 8. Nonperturbative Hopfield results

Canonical files:

- `NONPERTURBATIVE_HOPFIELD_CAPTURE.md`
- `HOPFIELD_RETUNING_NO_GO.md`

### D7 — Symmetric deep-strong transfer narrowing

For equal bare frequencies and equal weak local bath scales,

```math
\boxed{
\Gamma_{\pm,L}
=\Gamma_{\pm,R}
=
\frac{\gamma}
{2\sqrt{1+(g/\omega_0)^2}}.
}
```

A resolved polariton can retain unit peak transfer while its linewidth collapses as `1/g`.

The decoupling mechanism is established prior physics.

### D8 — Fixed-target retuning theorem

Hold the lower polariton at

```math
\omega_y=\omega_t>0
```

while allowing bare-frequency retuning and taking `g -> infinity`.

For fixed local optical and detector bath scales,

```math
\boxed{
\min(\Gamma_L,\Gamma_R)\to0.
}
```

Therefore resolved peak transfer and transfer linewidth cannot both stay bounded away from zero.

**Status:** candidate distinct supporting lemma; priority unproven.

A targeted search found no inspected source stating the exact fixed-target two-reservoir retuning result, but that negative search is not a novelty claim.

---

## 9. Reservoir-compensation resource theorem

Canonical file: `HOPFIELD_RESERVOIR_RESOURCE_COST.md`.

Demand

```math
T_0\ge\eta_*>0,
\qquad
\Delta\omega_{\rm FWHM}\ge W_*>0.
```

Then each dressed access rate must satisfy

```math
\boxed{
\min(\Gamma_L,\Gamma_R)
\ge
\Gamma_*
}
```

with

```math
\boxed{
\Gamma_*
=
\frac{W_*}{4}
\left(1-\sqrt{1-\eta_*}\right).
}
```

Optimizing over every allowed fixed-target bare-frequency retuning gives

```math
\boxed{
\max(\gamma_L,\gamma_R)
\ge
\Gamma_*
\sqrt{1+2g/\omega_t}.
}
```

Thus defeating the fixed-bath no-go while retaining fixed performance requires at least one bare external reservoir coupling resource to grow as `sqrt(g)` in deep strong coupling.

The symmetric retuning family asymptotically saturates this scaling.

This is a two-mode model theorem, not a universal reservoir theorem.

---

## 10. Multimode escape audit

Canonical file: `MULTIMODE_ESCAPE_AUDIT.md`.

### H4 — Invalidated naive multimode theorem

A claim based only on

```text
largest internal coupling anywhere in the whole multimode system -> infinity
```

is false because a disconnected spectator sector can carry the divergent coupling while the useful detector block remains unchanged.

### D9 — Mode proliferation as an explicit resource

A growing bank of narrow matched resonances can preserve finite integrated response if useful mode count/density grows sufficiently rapidly.

For sparse comparable matched resonances,

```math
N(g)\Gamma(g)=O(1)
```

is the natural compensation scaling.

This is a model/resource-counting result, not a general overlapping-mode theorem.

---

## 11. Passive multimode transfer-area theorem

Canonical file: `PASSIVE_MULTIMODE_TRANSFER_AREA_BOUND.md`.

Consider a finite stable passive linear network

```math
A
=-iH-(\Gamma_L+\Gamma_R+\Gamma_I),
\qquad
H=H^\dagger,
```

with

```math
B_LB_L^\dagger=2\Gamma_L,
\qquad
C_R^\dagger C_R=2\Gamma_R,
```

and no direct left-to-detector feedthrough.

Define

```math
G_{RL}(s)=C_R(sI-A)^{-1}B_L
```

and

```math
\mathcal I_{L\to R}
=
\int_{-\infty}^{\infty}
\frac{d\omega}{2\pi}
\operatorname{Tr}
\left[G_{RL}^\dagger G_{RL}\right].
```

### D10 — Passivity Gramian inequality

The left controllability Gramian satisfies

```math
\boxed{
0\preceq Q_L\preceq I.
}
```

The dual detector observability Gramian obeys the analogous inequality.

### D11 — Integrated transfer-area bound

```math
\boxed{
\mathcal I_{L\to R}
\le
2\min\!\left(
\operatorname{Tr}\Gamma_L,
\operatorname{Tr}\Gamma_R
\right).
}
```

This holds for arbitrary finite mode count, resonance overlap, coherent Hermitian internal coupling, and additional passive loss within the stated finite Markov/LTI model.

### D12 — Fixed-band access floor

For target angular bandwidth `W` and average transfer `T_bar`,

```math
\boxed{
\overline T_B
\le
\frac{4\pi}{W}
\min\!\left(
\operatorname{Tr}\Gamma_L,
\operatorname{Tr}\Gamma_R
\right).
}
```

Thus demanding

```math
\overline T_B\ge T_*
```

requires

```math
\boxed{
\min\!\left(
\operatorname{Tr}\Gamma_L,
\operatorname{Tr}\Gamma_R
\right)
\ge
\frac{T_*W}{4\pi}.
}
```

**Status:** exact internally derived passivity corollary. `H_2`, Lyapunov, and scattering-passive ingredients are standard prior mathematics. No novelty claim is made for the exact detector-facing trace inequality.

---

## 12. Verification state

### V1 — One-port time-domain check

`numerics/one_port_time_domain_check.py` independently integrates the cavity envelope and reproduces the derived modulation response.

### V2 — Passive multimode stress test

`numerics/passive_multimode_h2_stress.py` generates deterministic random passive networks, verifies

```math
0\preceq Q_L\preceq I
```

and the transfer-area inequality, and directly integrates one multimode transfer spectrum for comparison with the Gramian/H2 value.

No CI workflow is currently justified.

---

## 13. Explicit non-claims

Do **not** claim that:

- active volume fundamentally limits detector bandwidth;
- finite absorber number alone creates a single-photon speed limit;
- the fixed-target Hopfield lemma is novel or universal;
- the passive multimode trace inequality is novel;
- mode count cannot improve broadband response;
- the finite-network theorem covers direct feedthrough, active gain, time-varying systems, nonlinear detection, or genuinely infinite-dimensional non-Markovian baths;
- external reservoir coupling can be increased without physical cost;
- any current result is yet a publication-ready universal photodetector theorem.

---

## 14. Current candidate organizing statement

Within the finite passive linear class studied so far:

> **Internal electromagnetic complexity can redistribute useful detector transfer in frequency, but cannot replace the need for access to both the optical input side and the irreversible detector side. The full frequency-integrated transfer is bounded by the smaller aggregate external-access budget.**

This is presently the most robust theoretical structure produced by the thought experiment.

It is not yet a novelty claim.

---

## 15. Next promotion criteria

Before considering a manuscript or publication claim:

1. search passive network, microwave matching, quantum linear-system, and scattering literature more deeply for an equivalent integrated two-access bound;
2. test whether the trace inequality can be sharpened without extra assumptions;
3. treat direct finite-band feedthrough explicitly;
4. test strong/non-Markovian reservoir realizations by enlarging the passive system where possible;
5. map `Tr Gamma_L` and `Tr Gamma_R` onto microscopic detector resources;
6. bring thermal/dark/reset thermodynamics back only after that mapping is clear;
7. then reassess whether the surviving contribution is detector-specific and publication-worthy.