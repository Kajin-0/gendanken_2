# Gedanken 2

First-principles thought experiments in photodetector physics.

The purpose of this repository is to start from physically simple questions and follow the logic wherever it leads. The objective is not to force a predetermined theorem, reproduce the path of another project, or optimize an existing detector design. A branch is valuable if it clarifies the physics, including when it kills the conjecture that motivated it.

## Current experiment

**Experiment 01: The vanishing absorber**

Start with the question:

> Can an ideal photodetector be made arbitrarily small, arbitrarily fast, arbitrarily sensitive, and still absorb essentially every incident photon?

## What has happened so far

The first one-port resonator calculation established a clean local tradeoff:

> if the active optical loss rate `gamma_a` tends to zero while unity resonant absorption is maintained by critical coupling, the absorbed-power modulation bandwidth also tends to zero.

But the next counterexample changed the direction.

A shrinking lossy dielectric capacitor can keep its electromagnetic energy participation and `gamma_a` finite while its geometric active volume tends to zero. In the ideal local linear continuum model,

```math
V_a\to0
```

can coexist with

```math
\gamma_a=\text{constant},
\qquad
\gamma_a/V_a\to\infty.
```

Therefore **geometric active volume alone is not the fundamental optical resource**.

The apparent `V_a -> 0` divergence then runs into microscopic physics: finite oscillator number and strength, saturation, nonlocality, atomic granularity, thermal reverse processes, and the resources required for irreversible detection/amplification.

That is the active frontier of the thought experiment.

## Canonical files

Active state:

[`experiments/01-vanishing-absorber/CURRENT_STATE.md`](experiments/01-vanishing-absorber/CURRENT_STATE.md)

Claim/conjecture boundary:

[`experiments/01-vanishing-absorber/CLAIM_LEDGER.md`](experiments/01-vanishing-absorber/CLAIM_LEDGER.md)

One-port dynamics:

[`experiments/01-vanishing-absorber/ONE_PORT_RESONATOR_DYNAMICS.md`](experiments/01-vanishing-absorber/ONE_PORT_RESONATOR_DYNAMICS.md)

Active-volume counterexample:

[`experiments/01-vanishing-absorber/ACTIVE_VOLUME_COUNTEREXAMPLE.md`](experiments/01-vanishing-absorber/ACTIVE_VOLUME_COUNTEREXAMPLE.md)

Research history:

[`experiments/01-vanishing-absorber/RESEARCH_LOG.md`](experiments/01-vanishing-absorber/RESEARCH_LOG.md)

Artifact status:

[`experiments/01-vanishing-absorber/ARCHIVE_STATUS.md`](experiments/01-vanishing-absorber/ARCHIVE_STATUS.md)

## Current scientific status

This project is **exploratory** and makes no novelty claim.

The active-volume-only route to a universal passive optical bound has been explicitly invalidated within the ideal local linear continuum model. The next stage is to determine what microscopic or thermodynamic resource, if any, cannot be concentrated away.

A relevant prior-art collision already warns against assuming a universal quantum efficiency-dark-count-jitter tradeoff: fully quantum dark-state detector models can evade that tradeoff under idealized nonequilibrium assumptions. Therefore future claims must account explicitly for architecture, reservoirs, thermal reverse rates, amplification, and reset/free-energy resources.

## Research standard

A publication-level result should eventually survive, as applicable:

1. explicit assumptions and normalization;
2. units and dimensional checks;
3. exact limiting cases;
4. independent derivation for load-bearing results when feasible;
5. numerical checks that do not merely restate the analytic formula;
6. adversarial counterexample search;
7. primary-source prior-art comparison;
8. explicit thermodynamic/resource accounting;
9. a narrow claim ledger distinguishing known ingredients from any genuinely new result.

Failed or superseded branches are preserved as provenance rather than erased.

## Start here

New agents should read [`AGENTS.md`](AGENTS.md) first.
