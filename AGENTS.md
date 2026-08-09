# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gendanken_2`  
**Active experiment:** `experiments/01-vanishing-absorber/`  
**Current mode:** **open theoretical exploration; fixed-target Hopfield transfer no-go derived as a model-level candidate lemma; novelty unproven**  

This is the first operational file a new agent should read.

The repository is intentionally exploratory. Do not assume the current result is true beyond its stated model, novel, important, or destined to become the final paper. Follow the physics.

---

## 1. Mandatory concurrency protocol

Other agents may edit `main` concurrently.

Before every repository write:

1. fetch the latest current target;
2. compare with the last-seen state;
3. inspect relevant intervening changes;
4. fetch the exact target blob immediately before replacing an existing file;
5. never force a write against a stale blob SHA;
6. if `main` changes during a long task, recheck before writing;
7. preserve concurrent work and prefer narrowly scoped edits.

**Live `main` overrides every snapshot and recovery note.**

---

## 2. Scientific posture

Distinguish explicitly among

- **definition**;
- **known prior result**;
- **derived result**;
- **checked result**;
- **conjecture**;
- **empirical assumption**;
- **invalidated result**;
- **candidate publication claim**;
- **open question**.

Never silently promote one category into another.

No priority language (`first`, `new fundamental bound`, `unprecedented`, `universal`, etc.) is allowed without a focused primary-source prior-art record supporting the exact mathematical statement.

A negative literature search is not proof of novelty.

When a counterexample kills a desired theorem, preserve it and change direction. Do not invent assumptions solely to rescue the original target.

---

## 3. Experiment 01 — current scientific hierarchy

Guiding question:

> Can an ideal photodetector be made arbitrarily small, arbitrarily fast, arbitrarily sensitive, and still absorb essentially every incident photon?

The current logic is:

```text
weak one-port absorber
-> if gamma_a -> 0, unity absorption becomes narrow

geometric volume
-> not fundamental; field concentration can keep gamma_a finite as V_a -> 0

finite absorber number
-> not sufficient; one-photon two-level dynamics is linear

finite-transition LDOS
-> bounded over bandwidth only after environment and separation are constrained

finite emitter extent
-> removes literal point-dipole ultraviolet divergence

oscillator strength + extent
-> still insufficient to close perturbative rate bound when selected f varies

nonperturbative Hopfield model
-> deep-strong coupling suppresses dressed access to reservoirs

fixed target frequency + arbitrary bare retuning + g -> infinity
-> at least one required dressed reservoir coupling vanishes
```

The last line is the current strongest internally derived model-level statement.

---

## 4. Current candidate lemma

Canonical derivation:

`experiments/01-vanishing-absorber/HOPFIELD_RETUNING_NO_GO.md`

Use a TRK-consistent two-mode Hopfield model. Hold the lower polariton at

```math
\omega_y=\omega_t>0
```

while allowing `omega_c(g)`, `omega_b(g)` to retune and sending

```math
g\to\infty.
```

The fixed-target branch obeys

```math
(\omega_c^2-\omega_t^2)
(\omega_b^2-\omega_t^2)
=4g^2\frac{\omega_c}{\omega_b}\omega_t^2.
```

For fixed positive local optical and detector reservoir coupling scales, the dressed lower-polariton rates satisfy

```math
\boxed{
\min(\Gamma_L,\Gamma_R)\to0.
}
```

For a resolved transfer resonance,

```math
T_0
=\frac{4\Gamma_L\Gamma_R}
{(\Gamma_L+\Gamma_R)^2},
```

```math
\Delta\omega_{\rm FWHM}
=2(\Gamma_L+\Gamma_R).
```

Therefore peak transfer and linewidth cannot both remain bounded away from zero in this fixed-target infinite-internal-coupling limit.

**Status:** candidate distinct supporting lemma; priority unproven.

Targeted prior-art note:

`experiments/01-vanishing-absorber/HOPFIELD_RETUNING_PRIOR_ART_SWEEP.md`

Do not present this as a universal photodetector theorem.

---

## 5. Invalidated routes — do not reopen casually

### Active-volume-only bound — STOP

The shrinking-capacitor counterexample invalidates general claims such as

```text
gamma_a/V_a <= constant
```

or

```text
eta^2 B <= C V_a
```

from passivity alone.

### Finite absorber number / saturation — STOP as missing one-photon bound

The one-excitation sector is linear. Prior dark-state detector models already exploit this.

### TRK + finite emitter extent automatically closes weak-coupling enhancement — STOP as sufficient argument

The oscillator-strength/extent stress test shows that the retained inequalities do not close when the selected transition strength varies.

### Infinite weak-coupling Purcell rate -> infinite detector speed — STOP

The perturbative rate picture loses validity and the gauge-consistent Hopfield model exhibits deep-strong decoupling / transfer-line narrowing.

### Universal efficiency-dark-count-jitter tradeoff from quantum mechanics alone — STOP

Prior nonequilibrium dark-state detector models provide counterexamples under their resource assumptions.

---

## 6. Quantity-separation rules

Do not conflate

- geometric active volume;
- energy participation;
- transition/oscillator strength;
- projected LDOS;
- bare internal light-matter coupling `g`;
- local optical-reservoir coupling;
- local detector-reservoir coupling;
- dressed polariton reservoir rates;
- peak transfer probability;
- optical spectral linewidth;
- absorbed-power modulation bandwidth;
- carrier/readout bandwidth;
- thermal background counts;
- internal dark counts;
- NEP / detectivity.

Every use of `bandwidth` must identify the transfer function and convention.

Every use of `dark count` must identify the physical process and distinguish it from real thermal photons entering through the signal channel.

---

## 7. Noise and thermodynamic accounting

For every noise or irreversibility expression state

- the fluctuating process;
- whether noise is internal or enters through the optical channel;
- photon/event statistics;
- one-sided/two-sided normalization;
- the detector operating state: equilibrium, driven steady state, or reset cycle;
- the reservoir or free-energy source making a transition effectively irreversible;
- whether gain changes signal and noise together.

Do not extrapolate `D = g_d V_a` into the few-absorber regime without microscopic justification.

The thermodynamic cost of dark-state localization/reset remains an independent open resource axis.

---

## 8. Required checks for load-bearing results

As applicable, require

1. dimensional analysis;
2. exact limiting cases;
3. normalization/sign checks;
4. conceptually independent derivation when feasible;
5. numerical or symbolic falsification attempts;
6. adversarial architecture/counterexample search;
7. primary-source prior-art collision;
8. explicit domain of validity.

For the fixed-target Hopfield lemma specifically, every extension must preserve the distinction between

```text
internal light-matter coupling g
```

and

```text
external optical/detector reservoir resources.
```

Scaling reservoir coupling with `g` is not a refutation unless the required resource is counted explicitly.

---

## 9. Literature protocol

Prefer primary sources.

Important current anchors include

- Miller et al., *Optics Express* 24, 3329-3364 (2016): material-response limits;
- Zmuidzinas, *Applied Optics* 42, 4989-5008 (2003): thermal photon noise;
- Young, Sarovar & Leonard, *Physical Review A* 97, 033836 (2018): dark-state quantum detector architecture;
- Shim et al., *Physical Review X* 9, 011043 (2019): bandwidth-averaged near-field/LDOS limits;
- Scala et al., *New Journal of Physics* 22, 123047 (2020): finite-wavefunction regularization;
- De Liberato, *Physical Review Letters* 112, 016401 (2014): deep-strong light-matter decoupling;
- De Bernardis et al. (2018): gauge-consistent nonperturbative cavity QED;
- Palafox et al., *Journal of Physics: Photonics* 7, 04LT02 (2025): Hopfield dressed decay/heat-current suppression in deep strong coupling.

The exact fixed-target retuning statement still requires a broader older-literature search before publication positioning.

---

## 10. Documentation roles

### `CURRENT_STATE.md`

Canonical recovery point: what is established, what failed, what remains.

### `CLAIM_LEDGER.md`

Epistemic boundary: prior ingredients, derived results, invalidated claims, candidate claims, non-claims.

### `RESEARCH_LOG.md`

Chronology and reasons for direction changes.

### `ARCHIVE_STATUS.md`

Which artifacts are active, supporting, stopped, or historical.

### Dedicated derivation/audit files

Create only when the physics requires separation.

---

## 11. Canonical reading order

For a fresh agent:

1. `AGENTS.md`
2. `README.md`
3. `experiments/01-vanishing-absorber/CURRENT_STATE.md`
4. `experiments/01-vanishing-absorber/CLAIM_LEDGER.md`
5. `experiments/01-vanishing-absorber/HOPFIELD_RETUNING_NO_GO.md`
6. `experiments/01-vanishing-absorber/HOPFIELD_RETUNING_PRIOR_ART_SWEEP.md`
7. `experiments/01-vanishing-absorber/NONPERTURBATIVE_HOPFIELD_CAPTURE.md`
8. `experiments/01-vanishing-absorber/OSCILLATOR_STRENGTH_EXTENT_STRESS_TEST.md`
9. `experiments/01-vanishing-absorber/FINITE_EMITTER_FORM_FACTOR.md`
10. `experiments/01-vanishing-absorber/FINITE_TRANSITION_LDOS_BANDWIDTH_BOUND.md`
11. `experiments/01-vanishing-absorber/MICROSCOPIC_SINGLE_TRANSITION.md`
12. `experiments/01-vanishing-absorber/THERMAL_INPUT_CHANNEL.md`
13. `experiments/01-vanishing-absorber/ACTIVE_VOLUME_COUNTEREXAMPLE.md`
14. `experiments/01-vanishing-absorber/ONE_PORT_RESONATOR_DYNAMICS.md`
15. `experiments/01-vanishing-absorber/RESEARCH_LOG.md`
16. `experiments/01-vanishing-absorber/ARCHIVE_STATUS.md`

Read older stages in reverse only when auditing provenance.

---

## 12. Current next step

Do **not** restart the volume, single-transition, or weak-coupling-LDOS branches without a concrete new contradiction.

The next adversarial problem is:

> **Can a multimode optical environment or deliberately scaled reservoir engineering maintain both finite optical-to-detector peak transfer and finite bandwidth at a fixed target frequency as the internal light-matter coupling becomes arbitrarily large?**

Proceed in this order:

1. test a passive multimode Hopfield/star environment while keeping the target dressed frequency fixed;
2. identify whether the two-access-channel proof has a linear-algebraic generalization or a clear multimode counterexample;
3. separately test scaling `gamma_L(g)` or `gamma_R(g)` and quantify what resource scaling is required to defeat the two-mode result;
4. only if the result survives, broaden the prior-art search and add symbolic/numerical regression;
5. do not add HgCdTe-specific transport until the general optical constraint has either survived or failed.
