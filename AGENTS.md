# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gendanken_2`  
**Active experiment:** `experiments/01-vanishing-absorber/`  
**Current mode:** **open theoretical exploration; access-resource chain now reaches thermal irreversibility; next model is the complete detector cycle; no novelty claim**  

This is the first operational file a new agent should read.

The repository starts from thought experiments and follows the physics. Do not assume the current result is true beyond its stated model, novel, important, or destined to become a paper.

---

## 1. Mandatory concurrency protocol

Other agents may edit `main` concurrently.

Before every repository write:

1. fetch the latest `main` state;
2. compare with the last-seen state;
3. inspect relevant intervening changes;
4. fetch the exact current target blob immediately before replacing an existing file;
5. never overwrite a stale blob SHA;
6. preserve concurrent work and make narrowly scoped edits.

**Live `main` overrides every snapshot and recovery note.**

---

## 2. Epistemic labels are mandatory

Distinguish explicitly among

- **definition**;
- **known result**;
- **derived result**;
- **checked result**;
- **candidate distinct lemma** — internally derived, not found in a targeted search, but priority unproven;
- **conjecture**;
- **empirical/model assumption**;
- **invalidated result**;
- **superseded result**;
- **open question**.

Never promote a negative literature search, numerical observation, or restricted corollary into a novelty or universality claim.

No `first`, `new fundamental`, `unprecedented`, or `universal` language without a focused primary-source audit and claim-ledger update.

---

## 3. Current research path

**Experiment 01: The vanishing absorber**

> Can an ideal photodetector be made arbitrarily small, arbitrarily fast, arbitrarily sensitive, and still absorb essentially every incident photon?

The path has been forced by counterexamples:

```text
one-port weak absorber
-> dwell-time penalty in absorptive decay rate

active volume
-> killed: field concentration can defeat volume scaling

finite absorber count
-> killed: one-photon sector remains linear

finite transition / LDOS / emitter extent
-> conditional weak-coupling bounds, then perturbation theory fails

nonperturbative Hopfield coupling
-> dressed optical/detector access can collapse

multimode internal structure
-> integrated transfer, not individual linewidth, is the robust object

finite passive network
-> harmonic two-access transfer-area theorem

direct prompt path
-> genuine new broadband boundary resource

structured continuum
-> still obeys harmonic theorem under finite-budget H2-convergent passive embeddings

free-space thermodynamic optical coupling ceiling
-> converts target bandwidth/efficiency into minimum detector-reservoir access

thermal detector bath
-> detailed balance converts that access into a reverse-activation / energy-bias requirement

NEXT
-> complete cyclic detector with explicit readout/reset and actual dark-count definition.
```

---

## 4. Canonical strongest general finite-network result

Read:

`experiments/01-vanishing-absorber/PASSIVE_MULTIMODE_TRANSFER_AREA_BOUND.md`

For a finite stable passive strictly proper network,

```math
A=-iH-(\Gamma_L+\Gamma_R+\Gamma_I),
\qquad H=H^\dagger,
```

with

```math
L=\operatorname{Tr}\Gamma_L,
\qquad
R=\operatorname{Tr}\Gamma_R,
```

the integrated optical-to-detector transfer obeys

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

A single passive resonance saturates the bound. Equality in multimode form requires no participating parasitic loss and a common access ratio `ell_i/r_i = L/R`.

For target angular-frequency width `W`,

```math
\boxed{
\overline T_B
\le
\frac{4\pi LR}{W(L+R)}.
}
```

Interpret this as an **external-access resource law**, not an absolute detector bandwidth limit.

The mathematical ingredients are standard `H2`, Lyapunov, and passivity theory. Novelty is not claimed.

---

## 5. Scope attacks already completed

### Direct feedthrough

Read `DIRECT_FEEDTHROUGH_AND_BAND_LIMIT.md`.

An ideal nonzero frequency-independent prompt block makes the total all-frequency `H2` area divergent. This is a real counterexample to overextending the harmonic theorem.

For finite band width `W`,

```math
\boxed{
\sqrt{\mathcal I_B}
\le
\sqrt{\frac{W}{2\pi}}\,\|D_{RL}\|_F
+
\sqrt{\frac{2LR}{L+R}}.
}
```

Prompt channel strength/bandwidth is a new resource; do not call it a free bypass.

### Structured reservoirs

Read `STRUCTURED_RESERVOIR_ACCESS_AUDIT.md`.

If finite passive augmented realizations satisfy

```math
G_n\to G \text{ in }H2,
\qquad
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

A continuum escape must violate one of those assumptions or use active/nonlinear/time-dependent physics.

---

## 6. Current optical-to-thermal resource chain

### Optical access

Read `THERMODYNAMIC_OPTICAL_ACCESS_BRIDGE.md`.

Prior thermodynamic theory bounds the sum of **energy-decay** coupling rates from modes in angular band `W` into one free-space channel by

```math
\sum_m\gamma_{m,n}\le\frac{W}{2\pi}.
```

Repository rates are amplitude-decay rates, so

```math
\boxed{
L_B\le\frac{W}{4\pi}.
}
```

Combining with the harmonic theorem gives the restricted necessary condition

```math
\boxed{
R_B
\ge
\frac{\eta}{1-\eta}
\frac{W}{4\pi}
}
```

for band-averaged transfer `>= eta` in the stated one-free-space-channel/modal setting.

This has strong prior-art overlap with broadband absorption/rate-matching theory. Do not claim the matching structure as new.

### Thermal irreversibility

Read `THERMAL_IRREVERSIBILITY_COST.md`.

For detector localization `|e> <-> |d>` with energy release `Delta` into a thermal bath,

```math
\boxed{
\frac{k_\uparrow}{k_\downarrow}
=e^{-\Delta/(k_BT)}.
}
```

With the minimal convention `k_down = 2R_B`, the restricted optical requirement gives

```math
\boxed{
k_\downarrow
\ge
\frac{\eta}{1-\eta}
\frac{W}{2\pi}
}
```

and

```math
\boxed{
k_\uparrow
\ge
\frac{\eta}{1-\eta}
\frac{W}{2\pi}
e^{-\Delta/(k_BT)}.
}
```

If `k_up <= D_rev`, then

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

when the logarithm argument exceeds one.

**Critical:** `D_rev` is a reverse thermal-activation rate, not automatically a detector dark-count rate.

---

## 7. Supporting nonperturbative branch

Keep for mechanism/provenance:

- `HOPFIELD_RETUNING_NO_GO.md`
- `HOPFIELD_RESERVOIR_RESOURCE_COST.md`
- `HOPFIELD_RETUNING_PRIOR_ART_SWEEP.md`
- `NONPERTURBATIVE_HOPFIELD_CAPTURE.md`

The fixed-target two-mode lemma has status **candidate distinct supporting lemma; priority unproven**. Deep-strong decoupling itself is established prior physics.

Do not elevate the Hopfield branch above the more general access theorem.

---

## 8. Invalidated routes — do not restart casually

### Active-volume-only theorem — STOPPED

`ACTIVE_VOLUME_COUNTEREXAMPLE.md` defeats universal `eta^2 B <= C V_a` and `gamma_a/V_a <= constant` under admitted ideal field concentration.

### Finite absorber count as missing one-photon speed limit — STOPPED

The one-excitation sector remains linear.

### Largest internal coupling as universal multimode control parameter — STOPPED

Spectator-sector counterexample.

### `2 min(L,R)` bound — SUPERSEDED

Use the harmonic bound.

### Harmonic all-frequency theorem with arbitrary ideal feedthrough — INVALID EXTENSION

A constant prompt path is an explicit counterexample because it carries infinite bandwidth by assumption.

---

## 9. Noise/thermodynamic discipline

Never conflate

- thermal input photons;
- reverse thermal activation;
- observable dark counts;
- reset events;
- net thermodynamic current;
- raw monitored transitions;
- amplification/readout noise.

A transition is a dark count only after the detector's monitored output and cycle topology say it is.

For every rate/noise formula state

- physical process;
- counting convention;
- equilibrium vs driven operation;
- reservoir temperature/chemical potential where relevant;
- whether the quantity is a forward rate, reverse rate, net current, or observed event rate;
- reset/dead-time assumptions.

---

## 10. Required checks

For load-bearing results apply, as relevant:

1. explicit assumptions and normalization;
2. dimensional checks;
3. limiting cases;
4. independent derivation;
5. numerical falsification;
6. adversarial counterexamples;
7. primary-source prior-art collision;
8. exact domain of validity;
9. claim-ledger and research-log update.

A counterexample is progress.

---

## 11. Canonical reading order

For a fresh agent:

1. `AGENTS.md`
2. `README.md`
3. `experiments/01-vanishing-absorber/CURRENT_STATE.md`
4. `experiments/01-vanishing-absorber/CLAIM_LEDGER.md`
5. `experiments/01-vanishing-absorber/PASSIVE_MULTIMODE_TRANSFER_AREA_BOUND.md`
6. `experiments/01-vanishing-absorber/DIRECT_FEEDTHROUGH_AND_BAND_LIMIT.md`
7. `experiments/01-vanishing-absorber/STRUCTURED_RESERVOIR_ACCESS_AUDIT.md`
8. `experiments/01-vanishing-absorber/THERMODYNAMIC_OPTICAL_ACCESS_BRIDGE.md`
9. `experiments/01-vanishing-absorber/THERMAL_IRREVERSIBILITY_COST.md`
10. `experiments/01-vanishing-absorber/HOPFIELD_RESERVOIR_RESOURCE_COST.md`
11. `experiments/01-vanishing-absorber/HOPFIELD_RETUNING_NO_GO.md`
12. `experiments/01-vanishing-absorber/RESEARCH_LOG.md`
13. `experiments/01-vanishing-absorber/ARCHIVE_STATUS.md`
14. older files only for provenance.

---

## 12. Current next step — complete minimal detector cycle

Do **not** call reverse activation a dark count yet.

Build

```text
|g> -- photon --> |e>
|e> <-> |d>       thermal detector bath
|d> -- readout/reset --> |g>.
```

The model must explicitly determine

1. what physical jump produces a registered count;
2. what transitions can produce a count with no signal photon;
3. forward/reverse thermal rates;
4. reset/readout forward and reverse rates or explicit nonequilibrium bias;
5. steady-state state probabilities;
6. raw count rate versus net cycle current;
7. dead time / maximum count throughput;
8. entropy/free-energy affinity of a directional detector cycle.

A useful minimal mathematical language is a three-state continuous-time Markov cycle, but do not assume a one-way reset unless the work/reservoir resource producing it is stated.

Only after this cycle is solved should the project decide whether a genuine efficiency-bandwidth-dark-count thermodynamic statement survives.

Do not add HgCdTe-specific transport yet.