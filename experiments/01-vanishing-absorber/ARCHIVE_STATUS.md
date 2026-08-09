# Experiment 01 — Artifact Status Map

**Date:** 2026-08-08  
**Purpose:** preserve the research trail without allowing obsolete or speculative files to compete with the active state.

> Live `main`, root `AGENTS.md`, and `CURRENT_STATE.md` are authoritative.

---

## A. Canonical active state

Use these files for current work:

1. `CURRENT_STATE.md`
2. `CLAIM_LEDGER.md`
3. `RESEARCH_LOG.md`
4. `ARCHIVE_STATUS.md`

There is no manuscript yet.

---

## B. Active scientific derivations

None yet.

When a calculation becomes too substantial for `CURRENT_STATE.md`, create a narrowly named derivation or audit file here and add it to this section.

The first likely candidate is an exact one-port resonator dynamical derivation, but do not create that file until the derivation is actually performed.

---

## C. Numerics

No numerical scripts yet.

Create `numerics/` only when an analytic statement exists that benefits from an independent numerical falsification or regression test.

---

## D. Literature audits

No formal prior-art audit yet.

Do not infer novelty from the absence of an audit. Any future literature file should distinguish:

- established ingredients;
- nearest prior bounds/results;
- exact overlap in assumptions and conclusions;
- remaining candidate contribution, if any.

---

## E. Historical or stopped branches

None yet.

When a branch is invalidated or superseded:

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
