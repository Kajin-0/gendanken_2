# Gedanken 2

First-principles thought experiments in photodetector physics.

This repository starts from simple physical questions and follows the logic wherever it leads. Failed conjectures and counterexamples are retained because they define the real claim boundary.

## Experiment 01 — The vanishing absorber

> Can an ideal photodetector be made arbitrarily small, arbitrarily fast, arbitrarily sensitive, and still absorb essentially every incident photon?

The original active-volume intuition did **not** survive.

The path has been:

```text
weak resonant absorber
-> high peak absorption can cost temporal bandwidth

active volume
-> not fundamental; field concentration defeats simple V scaling

finite absorber number
-> not enough; one-photon sector remains linear

finite transition / LDOS / emitter extent
-> conditional weak-coupling bounds, then perturbative closure fails

nonperturbative light-matter coupling
-> dressed optical/detector access can collapse

multimode internal structure
-> integrated transfer becomes the robust quantity

finite passive network
-> exact harmonic two-access transfer-area bound

direct prompt path
-> genuine additional broadband boundary resource

structured continuum
-> no escape under finite-budget H2-convergent passive embeddings

thermodynamic free-space coupling bound
-> target broadband efficiency requires minimum detector-reservoir access

thermal detector bath
-> stronger forward access also strengthens reverse thermal activation unless energy bias/cooling increases

NEXT
-> explicit readout/reset cycle and observable dark counts.
```

## Current strongest general finite-network result

For a finite stable passive linear network with no direct optical-to-detector feedthrough, let

```math
L=\operatorname{Tr}\Gamma_L,
\qquad
R=\operatorname{Tr}\Gamma_R.
```

Define

```math
\mathcal I_{L\to R}
=
\int_{-\infty}^{\infty}
\frac{d\omega}{2\pi}
\operatorname{Tr}
[G_{RL}^\dagger(i\omega)G_{RL}(i\omega)].
```

Then

```math
\boxed{
\mathcal I_{L\to R}
\le
\frac{2LR}{L+R}.
}
```

The right side is the harmonic mean of the aggregate optical and irreversible detector access budgets. A single passive resonance saturates the bound.

For angular-frequency band width `W`,

```math
\boxed{
\overline T_B
\le
\frac{4\pi LR}{W(L+R)}.
}
```

This is an **external-access resource law**, not an absolute bandwidth limit.

The mathematical ingredients—`H2` norms, Lyapunov Gramians, and scattering-passive linear systems—are established theory. No novelty claim is made.

## Scope attacks

### Direct feedthrough

A nonzero frequency-independent prompt optical-to-detector path makes the total all-frequency `H2` area divergent because it inserts infinite Markov bandwidth by assumption.

Over finite band width `W`,

```math
\boxed{
\sqrt{\mathcal I_B}
\le
\sqrt{\frac{W}{2\pi}}\,\|D_{RL}\|_F
+
\sqrt{\frac{2LR}{L+R}}.
}
```

So prompt transfer is another resource, not a free internal-mode bypass.

### Structured reservoirs

If passive finite augmented models converge in `H2` with finite limiting terminal access budgets, the harmonic bound survives the continuum limit.

Spectral complexity alone is therefore not enough to evade the access picture under those assumptions.

## First optical-to-thermodynamic chain

Established thermodynamic light-coupling theory bounds the aggregate **amplitude-decay** access from modes in angular band `W` into one free-space channel by

```math
\boxed{
L_B\le\frac{W}{4\pi}.
}
```

Combining this prior optical ceiling with the harmonic theorem gives the restricted necessary condition

```math
\boxed{
R_B
\ge
\frac{\eta}{1-\eta}
\frac{W}{4\pi}
}
```

to achieve band-averaged transfer at least `eta` in the stated one-channel/modal setting.

Now model the irreversible localization step as a thermal transition with energy release `Delta`:

```math
\frac{k_\uparrow}{k_\downarrow}
=e^{-\Delta/(k_BT)}.
```

Using `k_down = 2R_B`, the same restricted chain implies

```math
\boxed{
k_\uparrow
\ge
\frac{\eta}{1-\eta}
\frac{W}{2\pi}
 e^{-\Delta/(k_BT)}.
}
```

For allowed reverse thermal activation `D_rev`,

```math
\boxed{
\Delta
\ge
k_BT
\ln\!\left[
\frac{\eta W}
{2\pi(1-\eta)D_{\rm rev}}
\right]
}
```

when the logarithm argument exceeds unity.

**`D_rev` is not yet a dark-count rate.** Whether reverse activation becomes an observable false count depends on readout and reset topology.

## Supporting nonperturbative result

In a TRK-consistent two-mode Hopfield model, holding a lower dressed mode at fixed target frequency while `g -> infinity` with fixed local optical/detector bath resources forces

```math
\min(\Gamma_L,\Gamma_R)\to0.
```

If the bare reservoirs are scaled to compensate while maintaining fixed peak transfer and linewidth, at least one must grow asymptotically as `sqrt(g)`.

This is a supporting mechanism, not the current general theorem.

## Canonical files

- [`AGENTS.md`](AGENTS.md) — recovery and scientific-integrity protocol
- [`CURRENT_STATE.md`](experiments/01-vanishing-absorber/CURRENT_STATE.md) — canonical scientific state
- [`CLAIM_LEDGER.md`](experiments/01-vanishing-absorber/CLAIM_LEDGER.md) — exact claim boundary
- [`PASSIVE_MULTIMODE_TRANSFER_AREA_BOUND.md`](experiments/01-vanishing-absorber/PASSIVE_MULTIMODE_TRANSFER_AREA_BOUND.md) — harmonic finite-network theorem
- [`DIRECT_FEEDTHROUGH_AND_BAND_LIMIT.md`](experiments/01-vanishing-absorber/DIRECT_FEEDTHROUGH_AND_BAND_LIMIT.md) — prompt-path scope audit
- [`STRUCTURED_RESERVOIR_ACCESS_AUDIT.md`](experiments/01-vanishing-absorber/STRUCTURED_RESERVOIR_ACCESS_AUDIT.md) — structured-continuum audit
- [`THERMODYNAMIC_OPTICAL_ACCESS_BRIDGE.md`](experiments/01-vanishing-absorber/THERMODYNAMIC_OPTICAL_ACCESS_BRIDGE.md) — optical coupling ceiling to detector-access requirement
- [`THERMAL_IRREVERSIBILITY_COST.md`](experiments/01-vanishing-absorber/THERMAL_IRREVERSIBILITY_COST.md) — reverse thermal activation / energy-bias result
- [`HOPFIELD_RESERVOIR_RESOURCE_COST.md`](experiments/01-vanishing-absorber/HOPFIELD_RESERVOIR_RESOURCE_COST.md) — nonperturbative reservoir-scaling cost
- [`HOPFIELD_RETUNING_NO_GO.md`](experiments/01-vanishing-absorber/HOPFIELD_RETUNING_NO_GO.md) — fixed-target supporting lemma
- [`RESEARCH_LOG.md`](experiments/01-vanishing-absorber/RESEARCH_LOG.md) — chronological research path
- [`ARCHIVE_STATUS.md`](experiments/01-vanishing-absorber/ARCHIVE_STATUS.md) — active/stopped/superseded artifact map

## Current scientific status

The project remains **exploratory**. No manuscript exists and no result is presented as a new universal photodetector limit.

The next model is the complete minimal detector cycle:

```text
|g> -- photon --> |e>
|e> <-> |d>       thermal detector bath
|d> -- readout/reset --> |g>.
```

It must define the recorded transition, spontaneous false-count pathways, reset/free-energy resource, dead time, steady-state counts, and net thermodynamic cycle current.

Only then can reverse thermal activation be connected honestly to an observable dark-count rate.

New agents should read [`AGENTS.md`](AGENTS.md) first.