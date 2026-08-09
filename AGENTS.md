# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gendanken_2`  
**Active experiment:** `experiments/01-vanishing-absorber/`  
**Current mode:** **open theoretical exploration; one-resonance model closed at stated assumptions**  

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

---

## 3. Active thought experiment

**Experiment 01: The vanishing absorber**

Question:

> Can an ideal photodetector be made arbitrarily small, arbitrarily fast, arbitrarily sensitive, and still absorb essentially every incident photon?

The initial one-resonance question has now been answered within its assumptions.

For a passive one-port resonance with external amplitude-decay rate `gamma_e` and active-material absorptive amplitude-decay rate `gamma_a`,

```math
A(\omega)=
\frac{4\gamma_e\gamma_a}
{(\omega-\omega_0)^2+(\gamma_e+\gamma_a)^2},
```

and the resonant small-signal absorbed-power bandwidth is

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

Thus a vanishingly weak absorber can retain unity monochromatic absorption in this model only by becoming proportionally narrow in absorbed-power response.

The broader volume question remains open because `gamma_a proportional to V` is not generally established.

Canonical state:

`experiments/01-vanishing-absorber/CURRENT_STATE.md`

Claim/conjecture boundary:

`experiments/01-vanishing-absorber/CLAIM_LEDGER.md`

Detailed one-port derivation:

`experiments/01-vanishing-absorber/ONE_PORT_RESONATOR_DYNAMICS.md`

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

- absorber volume or thickness tending to zero;
- weak and strong absorption;
- under-coupling, critical coupling, and over-coupling;
- zero dark generation;
- narrowband and broadband limits;
- vanishing optical loss outside the active material;
- long and short carrier lifetimes.

A formula that behaves incorrectly in an obvious limit is not publication-ready.

### Independent derivation

When a numerical coefficient or scaling exponent is load-bearing, seek a conceptually distinct derivation rather than an algebraic rearrangement of the same argument.

### Numerical falsification

Use numerics to try to break the analytic result. A useful numerical test should not merely encode the target formula and reproduce it.

Current one-port time-domain check:

`experiments/01-vanishing-absorber/numerics/one_port_time_domain_check.py`

The time-domain ODE integration is an independent check of the modulation transfer function. The coupling-ratio grid scan in that script is only an algebra regression and must not be described as an independent physical derivation.

### Counterexample search

Actively search architectures or regimes that could evade the proposed statement: multi-resonant structures, traveling-wave absorption, antennas, slow light, nonreciprocal systems, gain, avalanche multiplication, photoconductive gain, nonlocal response, strongly dispersive media, time-varying systems, etc., as relevant.

A counterexample is progress.

---

## 6. Optical and detector quantities must stay distinct

Do not conflate:

- external optical coupling;
- absorption probability in the active semiconductor;
- internal quantum efficiency;
- carrier collection efficiency;
- photoconductive or avalanche gain;
- electrical responsivity;
- optical spectral linewidth;
- absorbed-power modulation bandwidth;
- carrier-response bandwidth;
- readout bandwidth;
- NEP;
- detectivity or specific detectivity.

Define exactly which quantity appears in every bound.

Do not use `bandwidth` without identifying the transfer function and convention: FWHM, `-3 dB`, equivalent noise bandwidth, integrated absorption bandwidth, etc.

The current one-port calculation explicitly established that optical absorptance FWHM and absorbed-power modulation `-3 dB` bandwidth differ by a factor of two at critical coupling.

---

## 7. Noise accounting rules

Never combine a measured responsivity with an inconsistent theoretical noise model and call the result a fundamental detector metric.

For every noise expression state:

- the fluctuating physical process;
- whether the process is Poissonian or has an excess/Fano factor;
- whether the spectrum is one-sided or two-sided;
- current, voltage, power, or event-rate normalization;
- the bandwidth convention;
- whether generation and recombination are both counted;
- whether gain modifies both signal and noise;
- whether optical background fluctuations are excluded or included.

If a factor of two is convention-dependent, say so rather than hiding it.

The current toy `NEP` result uses independent bulk dark events, one collected charge per event, unity post-absorption collection, no internal gain, and a one-sided shot-noise convention. Do not generalize it silently.

---

## 8. Literature protocol

Prefer primary sources for technical claims.

For each potentially novelty-bearing idea:

1. search the exact mathematical/physical statement, not merely similar detector keywords;
2. identify the closest prior theorem, bound, or device result;
3. record what is identical, what assumptions differ, and what remains unaddressed;
4. distinguish a known ingredient from a potentially new synthesis;
5. update the claim ledger immediately if prior art narrows or kills a branch.

Do not cite a review as evidence of priority when the original source is available.

The temporal coupled-mode equations themselves are prior theory and must never be presented as novel.

---

## 9. Documentation rules

### `CURRENT_STATE.md`

This is the recovery point. It should answer:

- What question are we currently asking?
- What has actually been established?
- What is conjectural?
- What failed or was corrected?
- What is the next decisive calculation?

Keep it compact enough that a fresh agent can recover quickly.

### `CLAIM_LEDGER.md`

This is the epistemic boundary. Record active claims, conjectures, known ingredients, invalidated claims, explicit non-claims, and material corrections.

### `RESEARCH_LOG.md`

This is chronological. Preserve meaningful changes of direction, corrections, counterexamples, and why a branch was opened or closed.

### `ARCHIVE_STATUS.md`

This prevents historical files from competing with active work. Never delete useful failed derivations merely to make the repository appear cleaner; mark them historical or stopped.

### Dedicated audit files

Create a dedicated audit only when a calculation becomes substantial enough that keeping it inside `CURRENT_STATE.md` would obscure recovery. Do not generate ceremonial files before the physics requires them.

---

## 10. Reproducibility

Numerical work belongs under

`experiments/01-vanishing-absorber/numerics/`.

Rules:

- state software dependencies once they matter;
- keep independent checks logically separate from the analytic derivation they test;
- include benchmark parameters and expected tolerances;
- prefer small deterministic regression tests for publication-critical constants or asymptotics;
- do not add continuous-integration machinery merely for appearance.

Current numerical state requires only the Python standard library for the one-port time-domain check.

---

## 11. Canonical reading order

For a fresh agent:

1. `AGENTS.md`
2. `README.md`
3. `experiments/01-vanishing-absorber/CURRENT_STATE.md`
4. `experiments/01-vanishing-absorber/CLAIM_LEDGER.md`
5. `experiments/01-vanishing-absorber/ONE_PORT_RESONATOR_DYNAMICS.md`
6. `experiments/01-vanishing-absorber/RESEARCH_LOG.md`
7. `experiments/01-vanishing-absorber/ARCHIVE_STATUS.md`
8. only then read specialized numerics, future literature audits, or historical branches.

---

## 12. Current next step

Do **not** restart the one-port cavity derivation unless a concrete contradiction is found.

The load-bearing open assumption is now the relation between active material amount and absorptive decay rate.

For weak dielectric loss,

```math
\gamma_a
=
\frac{\omega\epsilon_0}{4U}
\int_{V_a}
\epsilon''(\mathbf r,\omega)|\mathbf E|^2\,dV.
```

The next question is:

> **Can passive electromagnetic design make `gamma_a/V` grow without bound as active volume tends to zero while preserving a physically meaningful incident channel and material model?**

Proceed in this order:

1. identify the weakest assumptions under which `gamma_a/V` could be bounded;
2. search primary electromagnetic-limit literature for bounds on absorption, local field concentration, material susceptibility, and frequency-integrated response;
3. construct explicit counterexample candidates before trying to prove a theorem;
4. distinguish fixed-frequency field enhancement from frequency-integrated or time-domain capability;
5. determine whether any bound concerns geometric material volume, oscillator strength, susceptibility integral, or another more physical resource;
6. only if a bounded quantity survives those attacks should it be combined with the dark-event model.

Do not add HgCdTe-specific carrier transport yet. The next bottleneck is electromagnetic, not semiconductor-specific.
