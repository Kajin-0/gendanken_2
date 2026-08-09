# Experiment 01 — Artifact Status Map

**Date:** 2026-08-08  
**Purpose:** preserve the research trail without allowing obsolete or speculative files to compete with the active state.

> Live `main`, root `AGENTS.md`, and `CURRENT_STATE.md` are authoritative.

---

## A. Canonical active state

Use these files for current work:

1. `CURRENT_STATE.md`
2. `CLAIM_LEDGER.md`
3. `ONE_PORT_RESONATOR_DYNAMICS.md`
4. `ACTIVE_VOLUME_COUNTEREXAMPLE.md`
5. `RESEARCH_LOG.md`
6. `ARCHIVE_STATUS.md`

There is no manuscript yet.

---

## B. Active scientific derivations

### `ONE_PORT_RESONATOR_DYNAMICS.md`

Status: **active supporting derivation; closed at stated one-mode assumptions**.

Role:

- fixes the one-port temporal coupled-mode normalization;
- derives absorptance, critical coupling, energy lifetime, optical linewidth, and absorbed-power modulation bandwidth;
- derives the toy dark-event-limited sensitivity-speed metric;
- shows that this metric is optimized at `gamma_e/gamma_a = 2` rather than exact critical coupling;
- establishes a bandwidth penalty in terms of `gamma_a`, not geometric volume.

Do not treat this file as a geometry-independent theorem.

### `ACTIVE_VOLUME_COUNTEREXAMPLE.md`

Status: **active counterexample / direction-changing derivation**.

Role:

- rewrites weak dielectric loss in terms of electric-energy participation;
- constructs a constant-capacitance shrinking-gap family with `V_a -> 0` but fixed participation and fixed `gamma_a`;
- explicitly gives `gamma_a/V_a -> infinity` inside the ideal local linear continuum model;
- invalidates the conjecture that passivity alone bounds `gamma_a/V_a` by active geometric volume;
- explains why established per-material-volume absorption bounds do not become active-volume-only detector bounds when arbitrary ideal field concentration is allowed;
- identifies microscopic light-matter physics and thermodynamic resource accounting as the next bottleneck.

Do not interpret the continuum `V_a -> 0` divergence as a prediction of infinite real detector performance.

---

## C. Numerics

Active directory:

`numerics/`

### `numerics/one_port_time_domain_check.py`

Status: **active deterministic validation**.

Role:

- integrates the resonant cavity envelope directly under small incident-power modulation;
- Fourier-extracts the absorbed-power response;
- checks the analytic first-order modulation transfer function at representative normalized frequencies;
- performs a grid regression on the coupling-objective algebra.

Important distinction: the time-domain integration is an independent numerical check of the modulation response. The coupling-ratio scan is only a regression on the derived objective and is not an independent physical derivation.

No numerical script is needed for the capacitor scaling because the counterexample is algebraic and exact within its idealized model.

No continuous-integration workflow is justified yet.

---

## D. Literature / prior-art state

No integrated novelty audit exists yet, and none is justified while the scientific target is still moving.

Primary sources already important to interpretation include:

- Miller et al., *Optics Express* 24, 3329-3364 (2016): geometry-independent optical-response bounds for specified material susceptibility and specified excitation;
- Raman, Shin & Fan, *Physical Review Letters* 110, 183901 (2013): material-defined upper bounds on modal material loss in plasmonic/metamaterial systems;
- Young, Sarovar & Léonard, *Physical Review A* 97, 033836 (2018): fully quantum photodetector model showing that a dark-state architecture can evade an assumed universal efficiency-dark-count-jitter tradeoff under its ideal assumptions;
- Young, Sarovar & Léonard, *Physical Review A* 98, 063835 (2018): general modeling framework treating field, absorption, and amplification as one coupled quantum system;
- Zmuidzinas, *Applied Optics* 42, 4989-5008 (2003): rigorous thermal photon-noise treatment including bunching correlations.

These are prior ingredients and constraints on the research direction, not evidence of novelty.

The next literature work should be attached to a concrete microscopic or thermodynamic statement, not a broad keyword sweep.

---

## E. Invalidated / narrowed branches

### Active-volume-only electromagnetic bound

Status: **STOPPED as a general claim**.

Invalidated statements include:

```text
passivity alone keeps gamma_a/V_a bounded
```

and any general active-volume-only law of the schematic form

```text
eta^2 B <= C V_a.
```

The conditional result obtained when `gamma_a proportional to V_a` remains mathematically valid for regular scaling families, but is not universal.

Do not restart an active-volume-only theorem without introducing additional explicit constraints on the full electromagnetic environment or microscopic material resources.

---

## F. Current forward branch

The next stage is the transition from continuum electromagnetic volume to microscopic and thermodynamic resources.

Candidate questions:

1. For a finite number of optical oscillators or transitions, what quantity replaces bulk susceptibility/volume?
2. Can increasing single-photon field strength compensate indefinitely for decreasing oscillator number?
3. How do oscillator-strength sum rules, saturation, nonlocality, and atomic granularity enter?
4. Under a **restricted passive thermal-input problem**, does detailed balance / thermal photon statistics impose a clean sensitivity-speed relation?
5. Which apparent tradeoffs disappear once nonequilibrium dark-state or amplification resources are allowed?

Do not add HgCdTe-specific transport until at least one of these microscopic statements is understood.

---

## G. Rule for future artifact growth

Documentation should grow because the physics demands separation, not because a mature repository is being imitated.

Prefer one compact canonical state over many overlapping summaries. Split out a new file only when it has a clear role such as:

- substantial derivation;
- independent normalization audit;
- approximation/error budget;
- numerical validation;
- counterexample analysis;
- primary-source prior-art comparison;
- manuscript snapshot.
