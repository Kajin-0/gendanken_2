# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gendanken_2`  
**Active experiment:** `experiments/01-vanishing-absorber/`  
**Current mode:** **open theoretical exploration; active-volume-only optical bound falsified in the ideal local continuum model**  

This is the first operational file a new agent should read.

The repository is intentionally exploratory. Do not assume that the current conjecture is true, novel, important, or destined to become the final paper. Follow the physics.

---

## 1. Mandatory concurrency protocol

Other agents may edit `main` concurrently.

Before every repository write:

1. fetch the latest `main` head or current target;
2. compare with the last-seen state;
3. inspect relevant intervening changes;
4. fetch the exact current target blob immediately before replacing an existing file;
5. never force a write against a stale blob SHA;
6. if `main` changes during a long task, recheck before writing;
7. preserve concurrent work and prefer narrowly scoped edits.

**Live `main` overrides all snapshots and recovery notes.**

---

## 2. Scientific posture

This project starts from a gedanken experiment, not from a desired conclusion.

Agents must distinguish among:

- **definition** — chosen notation or metric;
- **known result** — established theory used as an input;
- **derived result** — obtained here from stated assumptions;
- **checked result** — independently or numerically verified;
- **conjecture** — plausible but unproved statement;
- **empirical assumption** — material/device behavior imported from experiment or literature;
- **invalidated result** — a claim shown to fail;
- **open question** — unresolved.

Never silently promote a conjecture into a result.

No novelty language (`first`, `new fundamental bound`, `unprecedented`, etc.) is allowed until a focused primary-source prior-art sweep has been completed and recorded.

A negative literature search is evidence, not proof of priority.

When a counterexample kills a hoped-for theorem, preserve it and change direction. Do not add assumptions merely to rescue the original target unless those assumptions are independently physically motivated.

---

## 3. Active thought experiment

**Experiment 01: The vanishing absorber**

Question:

> Can an ideal photodetector be made arbitrarily small, arbitrarily fast, arbitrarily sensitive, and still absorb essentially every incident photon?

Two stages are now closed at their stated assumptions.

### Stage A — one-port resonance

For a passive one-port resonance with external amplitude-decay rate `gamma_e` and active-material absorptive amplitude-decay rate `gamma_a`,

```math
A(\omega)=
\frac{4\gamma_e\gamma_a}
{(\omega-\omega_0)^2+(\gamma_e+\gamma_a)^2},
```

and

```math
B_{3\rm dB}
=
\frac{\gamma_e+\gamma_a}{2\pi}.
```

At critical coupling,

```math
\gamma_e=\gamma_a,
\qquad
A_0=1,
\qquad
B_{3\rm dB}=\frac{\gamma_a}{\pi}.
```

Thus **if `gamma_a -> 0`**, unity monochromatic absorption requires a proportionally narrow absorbed-power response in this architecture.

### Stage B — geometric active volume does not force `gamma_a -> 0`

For a weakly lossy dielectric resonator,

```math
\gamma_a
=
\frac{\omega}{2}p_a\tan\delta,
```

where `p_a` is electric-energy participation.

An explicit shrinking parallel-plate capacitor family can keep capacitance and participation fixed while

```math
V_a\to0,
```

because the local field grows as the gap shrinks. In that ideal local linear continuum model,

```math
\gamma_a=\text{constant},
\qquad
\boxed{\gamma_a/V_a\to\infty.}
```

Therefore geometric active volume alone is not the fundamental optical resource.

Canonical state:

`experiments/01-vanishing-absorber/CURRENT_STATE.md`

Claim/conjecture boundary:

`experiments/01-vanishing-absorber/CLAIM_LEDGER.md`

One-port derivation:

`experiments/01-vanishing-absorber/ONE_PORT_RESONATOR_DYNAMICS.md`

Active-volume counterexample:

`experiments/01-vanishing-absorber/ACTIVE_VOLUME_COUNTEREXAMPLE.md`

Research chronology:

`experiments/01-vanishing-absorber/RESEARCH_LOG.md`

Artifact map:

`experiments/01-vanishing-absorber/ARCHIVE_STATUS.md`

---

## 4. Natural research sequence

Do not mechanically imitate another project. Use the shortest sequence demanded by the physics.

A typical progression is:

1. state the simplest physically meaningful thought experiment;
2. strip away nonessential engineering complications;
3. write the smallest model that answers one question exactly;
4. check units, normalization, signs, conservation laws, and limiting cases;
5. identify the assumption that creates the apparent tradeoff;
6. search for counterexamples that evade that assumption;
7. generalize only after the simple model is understood;
8. compare with known fundamental bounds and primary literature;
9. add realistic semiconductor physics only when it changes the logical result;
10. specialize to specific materials/devices only after the general structure is clear.

If the logic points somewhere unexpected, change direction.

---

## 5. Required checks for load-bearing results

For any equation that could become central to a paper, perform as many of the following as apply.

### Dimensional analysis

Every term must have consistent physical units. Record nontrivial checks.

### Limiting cases

Check physically interpretable limits, including where applicable:

- absorber volume or absorber number tending to zero;
- weak and strong optical coupling;
- under-coupling, critical coupling, and over-coupling;
- zero and finite thermal occupation;
- narrowband and broadband limits;
- linear-response and saturation limits;
- vanishing and finite irreversible relaxation;
- equilibrium and explicitly driven nonequilibrium operation.

A formula that behaves incorrectly in an obvious limit is not publication-ready.

### Independent derivation

When a numerical coefficient or scaling exponent is load-bearing, seek a conceptually distinct derivation rather than an algebraic rearrangement of the same argument.

### Numerical falsification

Use numerics to try to break the analytic result. A useful numerical test should not merely encode the target formula and reproduce it.

Current one-port time-domain check:

`experiments/01-vanishing-absorber/numerics/one_port_time_domain_check.py`

The time-domain ODE integration independently checks the modulation transfer function. The coupling-ratio grid scan is only an algebra regression and must not be described as an independent physical derivation.

### Counterexample search

Actively search architectures or regimes that could evade the proposed statement: field concentrators, multi-resonant structures, traveling waves, dark-state transfer, nonequilibrium reservoirs, gain, avalanche multiplication, photoconductive gain, nonlocal response, time-varying systems, etc., as relevant.

A counterexample is progress.

---

## 6. Invalidated routes — do not restart casually

### Active-volume-only bound

Do not attempt to prove a universal law based only on geometric active volume such as

```text
eta^2 B <= C V_a
```

or

```text
gamma_a / V_a <= constant
```

without adding explicit constraints that defeat the documented constant-capacitance counterexample.

`ACTIVE_VOLUME_COUNTEREXAMPLE.md` shows that arbitrary ideal field concentration can keep active participation finite while `V_a -> 0`.

Any new volume theorem must state what is fixed about:

- the full concentrating structure;
- its materials and losses;
- the bounding region / spatial scale;
- the input channel;
- material nonlocality or microscopic degrees of freedom.

### Universal efficiency-dark-count-jitter tradeoff

Do not assume quantum mechanics alone imposes such a tradeoff.

Young, Sarovar & Léonard, *Phys. Rev. A* 97, 033836 (2018), explicitly constructed a fully quantum detector architecture with rapid incoherent transfer to a monitored optically dark state that approaches unit efficiency, negligible dark counts, and minimal jitter under their ideal assumptions.

Their model assumes thermally activated return from the dark state to the optically active state is negligible.

Therefore thermodynamic and architectural resources must be stated before claiming a universal detector tradeoff.

---

## 7. Optical, microscopic, and detector quantities must stay distinct

Do not conflate:

- external optical coupling;
- active-material energy participation;
- absorption probability;
- transition/oscillator strength;
- internal quantum efficiency;
- carrier collection efficiency;
- irreversible localization rate;
- amplification gain;
- optical spectral linewidth;
- absorbed-power modulation bandwidth;
- carrier-response bandwidth;
- readout bandwidth;
- background count rate;
- internal dark count rate;
- NEP;
- detectivity or specific detectivity.

Define exactly which quantity appears in every bound.

Do not use `bandwidth` without identifying the transfer function and convention: FWHM, `-3 dB`, equivalent noise bandwidth, integrated absorption bandwidth, etc.

The one-port calculation established that optical absorptance FWHM and absorbed-power modulation `-3 dB` bandwidth differ by a factor of two at critical coupling.

---

## 8. Noise and thermodynamic accounting rules

For every noise expression state:

- the fluctuating physical process;
- whether it is internal detector noise or photons entering through an optical channel;
- photon/event statistics (Poisson, thermal/bunched, sub-Poisson, etc.);
- one-sided or two-sided spectral normalization;
- current, voltage, power, or event-rate normalization;
- whether correlations between spectral/temporal modes are included;
- whether the detector is in thermal equilibrium, driven steady state, or a reset cycle;
- what reservoir/free-energy resource makes an irreversible transition possible;
- whether gain modifies both signal and noise.

Never call thermal background photons `dark counts` without qualification. They are real input photons even when they are indistinguishable from the desired signal.

Never extrapolate `D = g_d V_a` into the few-absorber regime without a microscopic derivation.

If a factor of two is convention-dependent, state the convention rather than hiding it.

---

## 9. Literature protocol

Prefer primary sources for technical claims.

For each potentially novelty-bearing idea:

1. search the exact mathematical/physical statement, not merely similar detector keywords;
2. identify the closest prior theorem, bound, or detector model;
3. record what is identical, what assumptions differ, and what remains unaddressed;
4. distinguish a known ingredient from a potentially new synthesis;
5. update the claim ledger immediately if prior art narrows or kills a branch.

Important current anchors:

- Miller et al., *Optics Express* 24, 3329-3364 (2016): material-response optical bounds;
- Raman, Shin & Fan, *Phys. Rev. Lett.* 110, 183901 (2013): modal material-loss bounds;
- Young, Sarovar & Léonard, *Phys. Rev. A* 97, 033836 (2018): quantum coherence/backaction and dark-state detector architecture;
- Young, Sarovar & Léonard, *Phys. Rev. A* 98, 063835 (2018): general coupled quantum photodetector framework;
- Zmuidzinas, *Applied Optics* 42, 4989-5008 (2003): thermal photon noise and bunching correlations.

These are prior theory, not repository novelty.

---

## 10. Documentation rules

### `CURRENT_STATE.md`

This is the recovery point. It should answer:

- What question are we currently asking?
- What has actually been established?
- What is conjectural?
- What failed or was corrected?
- What is the next decisive calculation?

### `CLAIM_LEDGER.md`

This is the epistemic boundary. Record active claims, conjectures, known ingredients, invalidated claims, explicit non-claims, and material corrections.

### `RESEARCH_LOG.md`

This is chronological. Preserve meaningful changes of direction, corrections, counterexamples, and why a branch was opened or closed.

### `ARCHIVE_STATUS.md`

This prevents historical files from competing with active work. Never delete useful failed derivations merely to make the repository appear cleaner; mark them historical or stopped.

### Dedicated audit files

Create a dedicated audit only when a calculation becomes substantial enough that keeping it inside `CURRENT_STATE.md` would obscure recovery.

---

## 11. Reproducibility

Numerical work belongs under

`experiments/01-vanishing-absorber/numerics/`.

Rules:

- state software dependencies once they matter;
- keep independent checks logically separate from the analytic derivation they test;
- include benchmark parameters and expected tolerances;
- prefer small deterministic regression tests for publication-critical constants or asymptotics;
- do not add continuous-integration machinery merely for appearance.

---

## 12. Canonical reading order

For a fresh agent:

1. `AGENTS.md`
2. `README.md`
3. `experiments/01-vanishing-absorber/CURRENT_STATE.md`
4. `experiments/01-vanishing-absorber/CLAIM_LEDGER.md`
5. `experiments/01-vanishing-absorber/ONE_PORT_RESONATOR_DYNAMICS.md`
6. `experiments/01-vanishing-absorber/ACTIVE_VOLUME_COUNTEREXAMPLE.md`
7. `experiments/01-vanishing-absorber/RESEARCH_LOG.md`
8. `experiments/01-vanishing-absorber/ARCHIVE_STATUS.md`
9. only then read numerics or future microscopic/thermal branches.

---

## 13. Current next step

Do **not** restart the one-port cavity derivation or the active-volume-only bound unless a concrete contradiction is found.

The continuum model has run out of physical content in the `V_a -> 0` limit. The next bottleneck is the transition to microscopic light-matter coupling and thermodynamic resource accounting.

Proceed along two tightly controlled tests rather than trying to announce a universal theorem:

### A. Microscopic absorber

Use the smallest explicit absorber model needed to replace bulk susceptibility:

1. finite transition/oscillator strength;
2. field normalized to a single photon;
3. explicit radiative coupling to the incident mode;
4. explicit irreversible localization/detection channel;
5. saturation and finite-state effects;
6. thermal reverse rates where relevant.

Ask whether increasing field concentration can compensate indefinitely for reducing absorber number.

### B. Restricted thermal-input problem

Before attempting a full equilibrium detector theorem, analyze one passive optical input channel in a thermal state:

1. use Bose occupation `n_bar(omega,T)`;
2. fold it through the exact one-port absorptance `A(omega)`;
3. retain thermal photon bunching, not a Poisson approximation unless `n_bar << 1` is explicitly invoked;
4. derive mean background count rate and zero-frequency count noise;
5. combine with the already-defined absorbed-power modulation bandwidth;
6. optimize the coupling ratio without assuming critical coupling in advance.

This result must be labeled a **thermal input-channel/background limit**, not a universal internal dark-count bound.

Only after these two tests should the project decide whether a genuine fundamental detector statement remains.

Do not add HgCdTe-specific transport yet.
