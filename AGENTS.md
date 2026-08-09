# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gendanken_2`  
**Active experiment:** `experiments/01-vanishing-absorber/`  
**Current mode:** **open theoretical exploration; harmonic external-access theorem is the current frontier; no novelty claim**  

This is the first operational file a new agent should read.

The repository starts from thought experiments and follows the physics. Do not assume the current result is true beyond its stated model, novel, important, or destined to become a paper.

---

## 1. Mandatory concurrency protocol

Other agents may edit `main` concurrently.

Before every repository write:

1. fetch the latest `main` state;
2. compare with the last-seen head/state;
3. inspect relevant intervening changes;
4. fetch the exact current target blob immediately before replacing an existing file;
5. never overwrite a stale blob SHA;
6. if `main` changes during a long task, recheck before writing;
7. preserve concurrent work and make narrowly scoped edits.

**Live `main` overrides every snapshot and recovery note.**

---

## 2. Epistemic labels are mandatory

Distinguish explicitly among:

- **definition** — chosen notation or metric;
- **known result** — established prior theory used as an input;
- **derived result** — obtained in this repository from stated assumptions;
- **checked result** — independently/numerically verified;
- **candidate distinct lemma** — internally derived and not found in a targeted search, but priority unproven;
- **conjecture** — plausible but unproved;
- **empirical assumption** — material/device behavior imported from experiment/literature;
- **invalidated result** — explicit counterexample or contradiction found;
- **superseded result** — still true or useful but replaced by a stronger/correcter statement;
- **open question** — unresolved.

Never silently promote a conjecture, negative literature search, or numerical observation into a theorem or novelty claim.

Do not use `first`, `new fundamental`, `unprecedented`, `universal`, etc. without a focused primary-source audit and a claim-ledger update.

---

## 3. Active thought experiment

**Experiment 01: The vanishing absorber**

> Can an ideal photodetector be made arbitrarily small, arbitrarily fast, arbitrarily sensitive, and still absorb essentially every incident photon?

The original active-volume route failed.

The research path is now roughly

```text
one-port weak absorber
-> dwell-time penalty in gamma_a

active volume
-> counterexample: field concentration defeats V_a scaling

finite absorber
-> one-photon sector remains linear

finite transition + LDOS
-> conditional finite-band bounds

finite emitter extent
-> point-dipole divergence regularized

oscillator strength + extent
-> perturbative closure still fails

nonperturbative Hopfield coupling
-> dressed access collapses at deep strong coupling

multimode / reservoir escape
-> additional access resources can compensate

finite passive network
-> integrated transfer bounded by aggregate two-sided access.
```

---

## 4. Current strongest model-level theorem

Canonical derivation:

`experiments/01-vanishing-absorber/PASSIVE_MULTIMODE_TRANSFER_AREA_BOUND.md`

For a finite stable passive linear network

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

and no direct optical-to-detector feedthrough, define

```math
G_{RL}(s)=C_R(sI-A)^{-1}B_L.
```

Let

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
\left[G_{RL}^\dagger(i\omega)G_{RL}(i\omega)\right]
\le
\frac{2LR}{L+R}.
}
```

The right side is the harmonic mean of the aggregate optical and detector access budgets.

The result is tight; a single passive resonance saturates it.

### Proof mechanism

If `Q_L` is the left controllability Gramian and

```math
\ell_i,
\quad r_i,
\quad \iota_i
```

are the diagonal optical/detector/parasitic rates in its eigenbasis, the diagonal Lyapunov equation gives exactly

```math
q_i
=\frac{\ell_i}{\ell_i+r_i+\iota_i}.
```

Therefore

```math
\frac{\mathcal I_{L\to R}}2
=
\sum_i
\frac{\ell_i r_i}
{\ell_i+r_i+\iota_i}.
```

Cauchy-Schwarz then yields the harmonic bound.

This is the canonical form. The earlier bound

```math
\mathcal I\le2\min(L,R)
```

is **superseded** and should not be quoted as the final result.

---

## 5. Fixed-band corollary

For target angular bandwidth `W` and average transfer

```math
\overline T_B
=\frac1W\int_B
\operatorname{Tr}(G_{RL}^\dagger G_{RL})\,d\omega,
```

```math
\boxed{
\overline T_B
\le
\frac{4\pi LR}{W(L+R)}.
}
```

Thus a required

```math
\overline T_B\ge T_*
```

implies

```math
\boxed{
\frac{LR}{L+R}
\ge
\frac{T_*W}{4\pi}.
}
```

For matched budgets `L=R=Gamma_access`,

```math
\boxed{
\Gamma_{\rm access}
\ge
\frac{T_*W}{2\pi}.
}
```

Interpret this as an **external-access resource floor**, not an absolute detector bandwidth limit.

---

## 6. Current nonperturbative supporting results

### Fixed-target Hopfield retuning lemma

Canonical:

`experiments/01-vanishing-absorber/HOPFIELD_RETUNING_NO_GO.md`

At fixed lower dressed frequency `omega_t` and `g -> infinity`, fixed local optical/detector bath resources imply

```math
\min(\Gamma_L,\Gamma_R)\to0.
```

So resolved peak transfer and linewidth cannot both remain finite.

**Status:** candidate distinct supporting lemma; priority unproven.

Do not claim deep-strong decoupling itself as new.

### Reservoir compensation cost

Canonical:

`experiments/01-vanishing-absorber/HOPFIELD_RESERVOIR_RESOURCE_COST.md`

For fixed peak-transfer and linewidth targets, at least one bare reservoir coupling must scale as

```math
\sqrt{g/\omega_t}
```

in deep strong coupling.

This quantifies the resource spent by the `"just increase the external coupling"` escape.

---

## 7. Invalidated or stopped routes — do not restart casually

### Active-volume-only theorem — STOPPED

`ACTIVE_VOLUME_COUNTEREXAMPLE.md` explicitly permits

```math
V_a\to0,
\qquad
\gamma_a/V_a\to\infty
```

inside the admitted ideal continuum model.

Do not restart

```text
eta^2 B <= C V_a
```

or `gamma_a/V_a <= constant` without new explicit constraints defeating that counterexample.

### Finite absorber count as the missing one-photon speed limit — STOPPED

The one-excitation sector remains linear.

### Largest coupling anywhere in a multimode Hamiltonian as a universal control parameter — STOPPED

A disconnected spectator sector is a direct counterexample.

### Preliminary `2 min(L,R)` transfer-area theorem — SUPERSEDED

Use the exact harmonic bound instead.

---

## 8. What the harmonic theorem does not cover

Do not silently extend it to

- direct `L -> R` feedthrough/bypass;
- active gain;
- explicit time modulation;
- nonlinear/saturating detector dynamics;
- strong boundary coupling if the local Markov representation fails;
- genuinely infinite-dimensional non-Markovian reservoirs without a finite passive realization;
- arbitrary fermionic many-body semiconductor physics.

Finite structured reservoirs may be promoted to reaction-coordinate/pseudomode degrees of freedom and then included in an enlarged finite passive model when that representation is valid.

---

## 9. Noise and thermodynamic accounting rules

Keep distinct:

- thermal photons entering the optical channel;
- internal dark events;
- irreversible localization/relaxation;
- amplification noise;
- readout noise;
- reset/free-energy cost.

Never call thermal input photons `dark counts` without qualification.

Do not extrapolate the old continuum law

```math
D=g_dV_a
```

into a few-absorber regime without a microscopic derivation.

For every noise formula state

- physical fluctuating process;
- statistics;
- one-sided/two-sided convention;
- bandwidth convention;
- equilibrium vs driven operation;
- what reservoir makes a transition irreversible;
- whether gain changes signal and noise together.

---

## 10. Required checks for load-bearing results

Before promotion, apply as relevant:

1. explicit assumptions and normalization;
2. units/dimensional analysis;
3. limiting cases;
4. independent derivation where feasible;
5. deterministic numerical falsification;
6. adversarial architecture/counterexample search;
7. primary-source prior-art collision;
8. explicit domain of validity;
9. update `CLAIM_LEDGER.md` and `RESEARCH_LOG.md`.

A counterexample is progress.

---

## 11. Numerical state

Active scripts:

### `experiments/01-vanishing-absorber/numerics/one_port_time_domain_check.py`

Independent time-domain validation of the one-port modulation response.

### `experiments/01-vanishing-absorber/numerics/passive_multimode_h2_stress.py`

NumPy deterministic stress/regression test for

- `0 <= Q_L <= I`;
- the exact Gramian-eigenbasis identity;
- the harmonic access theorem;
- single-mode tightness;
- direct frequency integration versus the Gramian/H2 value.

Do not add CI merely for appearance. Add it when the result set is stable enough that regression protection is valuable.

---

## 12. Literature posture

Important established anchors include

- passive/scattering linear-system theory;
- Maxwell formulated as a scattering-passive system;
- passive quantum linear-system realizations;
- material-response and LDOS limits;
- dark-state quantum photodetector models;
- deep-strong light-matter decoupling;
- multiresonant broadband absorption/emission bounds.

The `H_2`/Lyapunov/passivity ingredients of the harmonic theorem are standard.

An initial targeted search has not located the exact harmonic two-access trace inequality in photodetector language.

This is **not** evidence of novelty.

Before publication positioning, search older control, microwave matching, network synthesis, scattering, cavity transport, and quantum linear-system literature for mathematically equivalent results.

---

## 13. Documentation roles

### `CURRENT_STATE.md`

Compact canonical recovery point.

### `CLAIM_LEDGER.md`

Exact epistemic boundary.

### `RESEARCH_LOG.md`

Chronological record of why the project changed direction.

### `ARCHIVE_STATUS.md`

Active/supporting/stopped/superseded artifact map.

### Dedicated derivation/audit files

Create only when a calculation needs separation to preserve recovery clarity.

---

## 14. Canonical reading order

For a fresh agent:

1. `AGENTS.md`
2. `README.md`
3. `experiments/01-vanishing-absorber/CURRENT_STATE.md`
4. `experiments/01-vanishing-absorber/CLAIM_LEDGER.md`
5. `experiments/01-vanishing-absorber/PASSIVE_MULTIMODE_TRANSFER_AREA_BOUND.md`
6. `experiments/01-vanishing-absorber/HOPFIELD_RESERVOIR_RESOURCE_COST.md`
7. `experiments/01-vanishing-absorber/MULTIMODE_ESCAPE_AUDIT.md`
8. `experiments/01-vanishing-absorber/HOPFIELD_RETUNING_NO_GO.md`
9. `experiments/01-vanishing-absorber/HOPFIELD_RETUNING_PRIOR_ART_SWEEP.md`
10. `experiments/01-vanishing-absorber/RESEARCH_LOG.md`
11. `experiments/01-vanishing-absorber/ARCHIVE_STATUS.md`
12. older stages only when tracing provenance.

---

## 15. Current next step

Do **not** return to active volume or one-port cavity optimization without a concrete contradiction.

The next adversarial questions are:

1. **Prior art:** does the harmonic `H_2` trace inequality already exist in equivalent passive-network notation?
2. **Direct path:** can a finite-band feedthrough contribution be included in a clean total access budget?
3. **Continuum reservoirs:** what survives for genuinely infinite-dimensional or strongly structured passive environments?
4. **Microscopic mapping:** what physical semiconductor quantities determine `Tr Gamma_L` and `Tr Gamma_R`?
5. **Thermodynamics:** once that mapping exists, how do reverse rates, dark events, amplification, and reset cost constrain the useful access budgets?

Only after these attacks should the project decide whether it has earned a manuscript.

Do not add HgCdTe-specific transport yet.