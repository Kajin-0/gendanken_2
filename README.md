# Gedanken 2

First-principles thought experiments in photodetector physics.

The purpose of this repository is to start from physically simple questions and follow the logic wherever it leads. The objective is not to force a predetermined theorem, reproduce the path of another project, or optimize an existing detector design. A branch is valuable if it clarifies the physics, even when it ends by showing that an apparent novelty is already known or that a conjecture is false.

## Current experiment

**Experiment 01: The vanishing absorber**

Start with the question:

> Can an ideal photodetector be made arbitrarily small, arbitrarily fast, arbitrarily sensitive, and still absorb essentially every incident photon?

The initial tension is simple:

- reducing active semiconductor volume can reduce intrinsic carrier-generation noise and carrier transit distance;
- passive optical confinement can restore high absorption in a weak absorber;
- restoring absorption by increasing photon dwell time may reintroduce a temporal-bandwidth penalty.

The current task is to determine exactly what follows from these statements and what does not.

Active state:

[`experiments/01-vanishing-absorber/CURRENT_STATE.md`](experiments/01-vanishing-absorber/CURRENT_STATE.md)

Claim/conjecture boundary:

[`experiments/01-vanishing-absorber/CLAIM_LEDGER.md`](experiments/01-vanishing-absorber/CLAIM_LEDGER.md)

Research history:

[`experiments/01-vanishing-absorber/RESEARCH_LOG.md`](experiments/01-vanishing-absorber/RESEARCH_LOG.md)

Artifact status:

[`experiments/01-vanishing-absorber/ARCHIVE_STATUS.md`](experiments/01-vanishing-absorber/ARCHIVE_STATUS.md)

## Current scientific status

This project is **exploratory**.

No novelty claim is currently made. In particular, no general sensitivity-bandwidth bound has been established. The proposed relations in the active notes are conjectures or targets until explicitly marked otherwise in the claim ledger.

## Research standard

A publication-level result should eventually survive, as applicable:

1. explicit assumptions and normalization;
2. units and dimensional checks;
3. exact limiting cases;
4. at least one independent analytic route for load-bearing results when feasible;
5. numerical checks that do not merely restate the analytic formula;
6. adversarial counterexample search;
7. primary-source prior-art comparison;
8. a narrow claim ledger distinguishing known ingredients from any genuinely new result.

Failed or superseded branches should normally be preserved as provenance rather than erased.

## Start here

New agents should read [`AGENTS.md`](AGENTS.md) first.
