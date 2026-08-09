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
4. `RESEARCH_LOG.md`
5. `ARCHIVE_STATUS.md`

There is no manuscript yet.

---

## B. Active scientific derivations

### `ONE_PORT_RESONATOR_DYNAMICS.md`

Status: **active supporting derivation**.

Role:

- fixes the one-port temporal coupled-mode normalization;
- derives absorptance, critical coupling, energy lifetime, optical linewidth, and absorbed-power modulation bandwidth;
- derives the toy dark-event-limited sensitivity-speed metric;
- shows that this metric is optimized at `gamma_e/gamma_a = 2` rather than exact critical coupling;
- isolates `gamma_a/V` as the next unresolved electromagnetic quantity.

Do not treat this file as a geometry-independent theorem.

The note also preserves two convention corrections caught before canonical-state promotion.

---

## C. Numerics

Active directory:

`numerics/`

Current check:

### `numerics/one_port_time_domain_check.py`

Status: **active deterministic validation**.

Role:

- integrates the resonant cavity envelope directly under small incident-power modulation;
- Fourier-extracts the absorbed-power response;
- checks the analytic first-order modulation transfer function at representative normalized frequencies;
- performs a grid regression on the coupling-objective algebra.

Important distinction: the time-domain integration is an independent numerical check of the modulation response. The coupling-ratio scan is only a regression on the derived objective and is not an independent physical derivation.

No continuous-integration workflow is justified yet.

---

## D. Literature audits

No formal novelty/prior-art audit yet.

Primary resonator-theory sources are listed in `ONE_PORT_RESONATOR_DYNAMICS.md` only to anchor known temporal coupled-mode theory.

Do not infer novelty from the absence of a formal audit.

The next literature work should focus on the active electromagnetic question:

- bounds on absorption per material amount;
- local-field concentration and susceptibility bounds;
- frequency-integrated absorption or power-bandwidth limits;
- whether any such bound constrains `gamma_a/V` under explicit material and input-channel assumptions.

Any future literature file should distinguish established ingredients, nearest prior bounds, exact overlap in assumptions/conclusions, and the remaining candidate contribution if one survives.

---

## E. Historical or stopped branches

None yet.

No scientific branch has been stopped; the initial one-port problem has instead been **closed at its stated model assumptions** and remains active supporting material.

When a future branch is invalidated or superseded:

1. retain scientifically useful derivations;
2. mark their status here;
3. record the reason in `RESEARCH_LOG.md`;
4. update `CLAIM_LEDGER.md` so obsolete statements cannot be accidentally revived.

Do not delete a failed branch merely because it failed.

---

## F. Rule for future artifact growth

Documentation should grow because the physics demands separation, not because a mature repository is being imitated.

Prefer one compact canonical state over many overlapping summaries. Split out a new file only when it has a clear role such as:

- substantial derivation;
- independent normalization audit;
- approximation/error budget;
- numerical validation;
- counterexample analysis;
- primary-source prior-art comparison;
- manuscript snapshot.
