# Gedanken 2

First-principles thought experiments in photodetector physics.

The purpose of this repository is to start from physically simple questions and follow the logic wherever it leads. The objective is not to force a predetermined theorem or optimize an existing detector design. A branch is valuable if it clarifies the physics, including when it kills the conjecture that motivated it.

## Current experiment

**Experiment 01: The vanishing absorber**

> Can an ideal photodetector be made arbitrarily small, arbitrarily fast, arbitrarily sensitive, and still absorb essentially every incident photon?

## Where the logic has gone

The original active-volume intuition did **not** survive.

The sequence so far is:

```text
weak absorber
-> unity resonant absorption can be recovered, but gamma_a -> 0 narrows response

active volume
-> not fundamental; ideal field concentration can keep gamma_a finite as V_a -> 0

finite absorber number
-> not sufficient for one photon; the one-excitation sector remains linear

finite transition + passive LDOS
-> finite broadband coupling only after environment/separation are constrained

finite emitter extent
-> regularizes the literal point-dipole ultraviolet divergence

oscillator strength + extent
-> still does not close the perturbative problem when the selected transition strength varies

nonperturbative light-matter coupling
-> deep-strong coupling suppresses dressed access to external reservoirs
```

The current strongest model-level result comes from the last step.

## Current candidate lemma

In a TRK-consistent two-mode Hopfield model, hold the lower dressed mode at a fixed target frequency

```math
\omega_y=\omega_t>0
```

while arbitrarily retuning the bare cavity/material frequencies and sending the internal light-matter coupling

```math
g\to\infty.
```

With fixed positive local optical and detector reservoir coupling resources, the dressed lower-mode rates obey

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

Therefore **peak optical-to-detector transfer and transfer bandwidth cannot both remain bounded away from zero** in this fixed-target infinite-internal-coupling limit.

This is **not** currently claimed as a new or universal photodetector theorem.

A focused first prior-art sweep found extensive deep-strong decoupling/Purcell-collapse literature but no inspected source stating this exact fixed-target retuning result. Current status:

> **candidate distinct supporting lemma; priority unproven.**

## Why this is interesting

The thought experiment has shifted from detector volume to a more general requirement:

```text
useful optical access
+
irreversible detector/material access.
```

A photodetector needs both. In the present nonperturbative model, making internal light-matter coupling arbitrarily large at fixed target frequency forces at least one of those accesses to disappear unless additional reservoir resources are scaled as well.

That is the current form of the original "where does the penalty reappear?" question.

## Canonical files

- [`AGENTS.md`](AGENTS.md) — recovery and scientific-integrity protocol
- [`CURRENT_STATE.md`](experiments/01-vanishing-absorber/CURRENT_STATE.md) — canonical scientific state
- [`CLAIM_LEDGER.md`](experiments/01-vanishing-absorber/CLAIM_LEDGER.md) — exact epistemic/claim boundary
- [`HOPFIELD_RETUNING_NO_GO.md`](experiments/01-vanishing-absorber/HOPFIELD_RETUNING_NO_GO.md) — current strongest model-level derivation
- [`HOPFIELD_RETUNING_PRIOR_ART_SWEEP.md`](experiments/01-vanishing-absorber/HOPFIELD_RETUNING_PRIOR_ART_SWEEP.md) — targeted novelty collision
- [`NONPERTURBATIVE_HOPFIELD_CAPTURE.md`](experiments/01-vanishing-absorber/NONPERTURBATIVE_HOPFIELD_CAPTURE.md) — deep-strong transfer narrowing
- [`RESEARCH_LOG.md`](experiments/01-vanishing-absorber/RESEARCH_LOG.md) — chronological path and failed branches
- [`ARCHIVE_STATUS.md`](experiments/01-vanishing-absorber/ARCHIVE_STATUS.md) — active/stopped artifact map

Earlier supporting derivations remain in `experiments/01-vanishing-absorber/` as the audit trail.

## Current scientific status

This project remains **exploratory**.

No manuscript exists. No novelty claim is made. Several attractive universal bounds have already been invalidated and are preserved explicitly so future agents do not resurrect them.

The next adversarial question is whether a multimode optical environment or deliberately scaled reservoir engineering can evade the fixed-target two-access-channel result.

## Research standard

Any publication-level result must survive, as applicable:

1. explicit assumptions and normalization;
2. dimensional and limiting-case checks;
3. independent analytic/numerical validation where feasible;
4. adversarial counterexample search;
5. primary-source prior-art comparison;
6. explicit accounting of optical, detector-reservoir, and thermodynamic resources;
7. a narrow claim ledger.

Failed or superseded branches are preserved as provenance rather than erased.
