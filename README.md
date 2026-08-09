# Gedanken 2

First-principles thought experiments in photodetector physics.

This repository starts from simple physical questions and follows the logic wherever it leads. Failed conjectures and counterexamples are retained because they define the real claim boundary.

## Experiment 01 — The vanishing absorber

> Can an ideal photodetector be made arbitrarily small, arbitrarily fast, arbitrarily sensitive, and still absorb essentially every incident photon?

The original active-volume intuition did **not** survive.

The path has been:

```text
weak absorber
-> unity resonant absorption can become temporally narrow

active volume
-> not fundamental; ideal field concentration defeats simple V scaling

finite absorber number
-> not enough; one-photon sector remains linear

finite transition / LDOS / emitter extent
-> conditional weak-coupling bounds, but no full closure

nonperturbative light-matter coupling
-> deep-strong dressed access can collapse

retuning / reservoir scaling / multimode escapes
-> each spends additional external access resources

finite passive multimode network
-> exact harmonic bound on integrated optical-to-detector transfer.
```

## Current strongest result

For an arbitrary finite stable passive linear network with no direct optical-to-detector feedthrough, let

```math
L=\operatorname{Tr}\Gamma_L
```

be the aggregate optical access budget and

```math
R=\operatorname{Tr}\Gamma_R
```

the aggregate irreversible detector access budget.

Define

```math
\mathcal I_{L\to R}
=
\int_{-\infty}^{\infty}
\frac{d\omega}{2\pi}
\operatorname{Tr}
\left[
G_{RL}^\dagger(i\omega)
G_{RL}(i\omega)
\right].
```

Then

```math
\boxed{
\mathcal I_{L\to R}
\le
\frac{2LR}{L+R}.
}
```

The right side is the harmonic mean of the two total access budgets.

The theorem allows arbitrary finite internal mode count, resonance overlap, coherent coupling topology, and passive internal interference. A single passive resonance saturates the bound exactly.

The physical interpretation is:

> **Internal electromagnetic sophistication can redistribute detector transfer in frequency, but it cannot replace simultaneous access to both the optical input and irreversible detector sides.**

For a target angular-frequency band of width `W`,

```math
\boxed{
\overline T_B
\le
\frac{4\pi LR}{W(L+R)}.
}
```

So broadband efficient transfer requires proportionally sufficient aggregate access on both sides.

This is an **access-resource law**, not an absolute bandwidth limit.

## Important status warning

The mathematical ingredients—`H_2` norms, Lyapunov Gramians, and scattering-passive linear systems—are established theory.

An initial targeted search has not found this exact harmonic two-access trace inequality stated in photodetector language, but that is only a negative search result.

**No novelty or priority claim is currently made.**

## Supporting nonperturbative result

In a TRK-consistent two-mode Hopfield model, if a lower polariton is held at a fixed target frequency while internal light-matter coupling `g -> infinity`, fixed local optical/detector bath resources force

```math
\min(\Gamma_L,\Gamma_R)\to0.
```

If the bare reservoirs are scaled to compensate while maintaining fixed peak transfer and linewidth, at least one must grow asymptotically as `sqrt(g)`.

This gives one concrete mechanism behind the broader access-resource picture.

## Canonical files

- [`AGENTS.md`](AGENTS.md) — recovery and scientific-integrity protocol
- [`CURRENT_STATE.md`](experiments/01-vanishing-absorber/CURRENT_STATE.md) — canonical scientific state
- [`CLAIM_LEDGER.md`](experiments/01-vanishing-absorber/CLAIM_LEDGER.md) — exact claim boundary
- [`PASSIVE_MULTIMODE_TRANSFER_AREA_BOUND.md`](experiments/01-vanishing-absorber/PASSIVE_MULTIMODE_TRANSFER_AREA_BOUND.md) — current strongest model-level derivation
- [`HOPFIELD_RESERVOIR_RESOURCE_COST.md`](experiments/01-vanishing-absorber/HOPFIELD_RESERVOIR_RESOURCE_COST.md) — cost of scaling external reservoirs
- [`MULTIMODE_ESCAPE_AUDIT.md`](experiments/01-vanishing-absorber/MULTIMODE_ESCAPE_AUDIT.md) — multimode counterexample/resource audit
- [`HOPFIELD_RETUNING_NO_GO.md`](experiments/01-vanishing-absorber/HOPFIELD_RETUNING_NO_GO.md) — fixed-target nonperturbative lemma
- [`RESEARCH_LOG.md`](experiments/01-vanishing-absorber/RESEARCH_LOG.md) — chronological research path
- [`ARCHIVE_STATUS.md`](experiments/01-vanishing-absorber/ARCHIVE_STATUS.md) — active/stopped/superseded artifact map

## Current scientific status

The project remains **exploratory**.

No manuscript exists. No theorem is currently presented as a new universal photodetector limit.

The next attacks are direct-path/feedthrough accounting, infinite or strongly structured passive reservoirs, deeper prior-art collision, and eventually a microscopic mapping from the abstract access budgets to semiconductor detector physics.

New agents should read [`AGENTS.md`](AGENTS.md) first.