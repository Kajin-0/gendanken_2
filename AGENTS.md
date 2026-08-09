# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gendanken_2`  
**Active experiment:** `experiments/01-vanishing-absorber/`  
**Current mode:** **open theoretical exploration**  

This is the first operational file a new agent should read.

The repository is intentionally exploratory. Do not assume that the current conjecture is true, novel, important, or destined to become the final paper. Follow the physics.

---

## 1. Mandatory concurrency protocol

Other agents may edit `main` concurrently.

Before every repository write:

1. fetch the latest `main` head;
2. compare it with the last-seen head;
3. inspect relevant intervening commits;
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
- **checked result** — independently verified analytically or numerically;
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

The current intuition is that shrinking active volume can suppress intrinsic carrier-generation noise, while passive resonant or trapping structures can recover optical absorption. The central question is whether the required electromagnetic dwell time, bandwidth, mode coupling, material response, or another physical mechanism necessarily restores a penalty.

This is a question, not a conclusion.

Canonical state:

`experiments/01-vanishing-absorber/CURRENT_STATE.md`

Claim/conjecture boundary:

`experiments/01-vanishing-absorber/CLAIM_LEDGER.md`

Research chronology:

`experiments/01-vanishing-absorber/RESEARCH_LOG.md`

Artifact map:

`experiments/01-vanishing-absorber/ARCHIVE_STATUS.md`

---

## 4. Natural research sequence

Do not mechanically imitate another project. For the current problem, use the shortest sequence demanded by the physics.

A typical progression is:

1. state the simplest physically meaningful thought experiment;
2. strip away nonessential engineering complications;
3. write the smallest model that answers one question exactly;
4. check units, normalization, signs, conservation laws, and limiting cases;
5. identify what assumption creates the apparent tradeoff;
6. search for counterexamples that evade that assumption;
7. generalize only after the simple model is understood;
8. compare with known fundamental bounds and primary literature;
9. add realistic semiconductor physics only when it changes the logical result;
10. specialize to specific materials/devices only after the general structure is clear.

If the logic points somewhere unexpected, change direction.

---

## 5. Required checks for load-bearing results

For any equation that could become central to a paper, perform as many of the following as are applicable:

### Dimensional analysis

Every term must have consistent physical units. Record nontrivial unit checks.

### Limiting cases

Check physically interpretable limits, for example:

- absorber volume or thickness tending to zero;
- weak and strong absorption;
- critical coupling and severe under/over-coupling;
- zero dark generation;
- narrowband and broadband limits;
- vanishing optical loss outside the active material;
- long and short carrier lifetimes.

A formula that behaves incorrectly in an obvious limit is not publication-ready.

### Independent derivation

When a numerical coefficient or scaling exponent is load-bearing, seek a conceptually distinct derivation rather than algebraically rearranging the same argument.

### Numerical falsification

Use numerics to try to break the analytic result. A useful numerical test should not merely encode the target formula and reproduce it.

### Counterexample search

Actively search architectures or regimes that could evade the proposed statement: multi-resonant structures, traveling-wave absorption, antennas, slow light, nonreciprocal systems, gain, avalanche multiplication, photoconductive gain, nonlocal response, strongly dispersive media, etc., as relevant.

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
- optical bandwidth;
- carrier-response bandwidth;
- readout bandwidth;
- NEP;
- detectivity or specific detectivity.

Define exactly which quantity appears in every bound.

Likewise, do not use "bandwidth" without identifying the transfer function and the convention used to measure it (e.g. FWHM, `-3 dB`, equivalent noise bandwidth, integrated absorption bandwidth).

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

---

## 9. Documentation rules

### `CURRENT_STATE.md`

This is the recovery point. It should answer:

- What question are we currently asking?
- What has actually been established?
- What is conjectural?
- What failed?
- What is the next decisive calculation?

Keep it compact enough that a fresh agent can recover quickly.

### `CLAIM_LEDGER.md`

This is the epistemic boundary. Record active claims, conjectures, known ingredients, invalidated claims, and explicit non-claims.

### `RESEARCH_LOG.md`

This is chronological. Preserve meaningful changes of direction, corrections, counterexamples, and why a branch was opened or closed.

### `ARCHIVE_STATUS.md`

This prevents historical files from competing with active work. Never delete useful failed derivations merely to make the repository appear cleaner; mark them historical or stopped.

### Dedicated audit files

Create a dedicated audit only when a calculation becomes substantial enough that keeping it inside `CURRENT_STATE.md` would obscure recovery. Do not generate dozens of ceremonial files before the physics requires them.

---

## 10. Reproducibility

When numerics begin:

- place scripts under `experiments/01-vanishing-absorber/numerics/`;
- state software versions once they matter;
- keep independent checks logically separate from the analytic derivation they test;
- include benchmark parameters and expected tolerances;
- prefer small deterministic regression tests for publication-critical constants or asymptotics.

Do not add continuous-integration machinery merely for appearance. Add it when stable calculations exist that are worth protecting against regression.

---

## 11. Canonical reading order

For a fresh agent:

1. `AGENTS.md`
2. `README.md`
3. `experiments/01-vanishing-absorber/CURRENT_STATE.md`
4. `experiments/01-vanishing-absorber/CLAIM_LEDGER.md`
5. `experiments/01-vanishing-absorber/RESEARCH_LOG.md`
6. `experiments/01-vanishing-absorber/ARCHIVE_STATUS.md`
7. only then read specialized derivations, numerics, or historical branches.

---

## 12. Current next step

Do not jump directly to a geometry-independent theorem.

Start with the simplest one-port passive resonant absorber and establish exactly:

1. its frequency-dependent absorptance;
2. the condition for unity on-resonance absorption;
3. the associated optical energy-decay time;
4. the correct definition of temporal detection bandwidth;
5. how the absorber's material loss/volume enters these quantities.

Then ask whether shrinking the absorbing material necessarily narrows the usable detection bandwidth, and under precisely which assumptions.

Only after that result is secure should the project attempt a general Maxwell/material-response bound.
