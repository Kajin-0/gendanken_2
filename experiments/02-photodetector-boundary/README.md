# Experiment 02 — The Photodetector Boundary

**Opened:** 2026-08-12  
**Status:** exploratory first-principles Gedanken experiment  
**Priority / novelty:** unassessed; **no novelty claim**

## Starting question

> At what point does a simple collection of atoms become a photodetector? If light is absorbed and re-emitted, versus absorbed and used to generate charge, where is the boundary?

The question initially mixes several distinct boundaries. The purpose of this experiment is to separate them and then follow the strongest surviving chain of logic without assuming in advance that the answer is a semiconductor-specific atom count, a band-gap criterion, or even photon absorption.

## First terminology correction

Absorption followed by photon re-emission is fluorescence / spontaneous emission (or related radiative relaxation), not the external photoelectric effect. In a semiconductor, interband photon absorption itself can create an electron-hole excitation:

```math
h\nu + e^-_{\mathrm{VB}} \rightarrow e^-_{\mathrm{CB}} + h^+_{\mathrm{VB}}.
```

Radiative recombination can occur later:

```math
e^-+h^+\rightarrow h\nu'.
```

Therefore

```text
"photon absorbed and re-emitted"
```

and

```text
"photon absorbed and electron-hole pair generated"
```

are not generally mutually exclusive alternatives. They can be successive stages of the same event.

## Central operational question

Strip away semiconductor architecture. Send either zero photons or one photon toward a material system initially in the same state.

Let

```math
H_0: n_\gamma=0,
\qquad
H_1: n_\gamma=1.
```

After the interaction, interrogate the material. If its observable statistics depend on which hypothesis occurred, the material contains information about photon arrival:

```math
P(Y|H_1)\neq P(Y|H_0).
```

Equivalently, for the detector's reduced quantum states

```math
\rho_D^{(0)},\qquad \rho_D^{(1)},
```

define the trace distance

```math
\boxed{
\mathcal D
=\frac12\left\|\rho_D^{(1)}-\rho_D^{(0)}\right\|_1.
}
```

Then

```text
D = 0  -> no measurement on the chosen detector subsystem can distinguish photon/no-photon,
D > 0  -> some information about photon arrival is encoded in that subsystem,
D = 1  -> the two detector states are perfectly distinguishable in principle.
```

For equal prior probabilities, the optimal binary discrimination error is

```math
\boxed{
P_{e,\min}=\frac{1-\mathcal D}{2}.
}
```

This converts the original qualitative question into a quantitative one:

> **How distinguishable are the physical states produced by zero and one incident photons, and how long does that distinguishability remain accessible?**

## Strongest current conceptual result

The working boundary is **not photon absorption itself**.

A hypothetical perfect absorber can be a useless detector if, after the interaction, the chosen detector subsystem returns to exactly the same accessible state for photon and no-photon histories:

```math
\rho_D^{(1)}=\rho_D^{(0)}.
```

Conversely, a photon can in principle survive while a dispersive interaction maps the material into distinguishable states:

```math
|1_\gamma\rangle|D_0\rangle
\rightarrow
|1_\gamma\rangle|D_1\rangle,
\qquad
\langle D_0|D_1\rangle\neq 1.
```

Therefore the current organizing statement is

> **Photodetection is fundamentally an information-transfer / record-formation process. Absorption is one important implementation, not the definition.**

This statement is not a novelty claim; quantum nondemolition and dispersive measurements already establish that measurement need not always destroy the measured quantum.

## Why there is probably no universal atom-count boundary

The original intuition suggested a critical number of atoms

```math
N_c
```

at which matter changes from "not a detector" to "detector."

That universal boundary does not survive the operational definition. A single atom can, in principle, encode photon arrival through excitation or ionization if the resulting state is subsequently readable. A macroscopic absorber can, conversely, fail to provide a useful accessible record.

Atom count does matter for a different question: when isolated atomic levels become well described as molecular manifolds and eventually bands. If a manifold of width `W` contains `N` states, a rough characteristic spacing is

```math
\Delta E\sim\frac{W}{N}.
```

A band / quasi-continuum description becomes operationally natural when individual spacings are small relative to the relevant broadening or experimental resolution, schematically

```math
\Delta E \ll \Gamma_{\mathrm{eff}}.
```

That is a finite-size spectroscopic crossover. It is **not identified here with the definition of a photodetector**.

## Separate physical boundaries

The experiment currently distinguishes at least five different transitions that must not be conflated:

```text
1. atomic -> molecular -> band-like electronic spectrum
2. bound optical excitation -> mobile charge carriers
3. photon interaction -> information encoded in matter
4. microscopic encoded information -> robust/metastable record
5. physical record -> useful detector output against noise and false events
```

The first two concern condensed-matter excitation and transport. The last three concern detection.

## Semiconductor specialization

For an ordinary semiconductor absorber, the optical event can create an electron-hole excitation. Whether that excitation becomes an electrical detection event depends on subsequent dynamics.

In a simple competing-rate picture,

```math
\Gamma_{\rm tot}
=\Gamma_{\rm col}+\Gamma_r+\Gamma_{nr},
```

so the conditional probability that an existing excitation is collected is approximately

```math
P_{\rm col}
=\frac{\Gamma_{\rm col}}
{\Gamma_{\rm col}+\Gamma_r+\Gamma_{nr}}.
```

A useful device efficiency therefore factors conceptually into distinct stages, for example

```math
\eta
\sim
P_{\rm abs}
P_{\rm useful\ excitation}
P_{\rm col}
P_{\rm read}.
```

The exact factorization is architecture dependent. Its purpose here is to prevent the false equivalence

```text
high absorptivity = good photodetection.
```

## Amplification reinterpretation

If one microscopic event is mapped to a macroscopic output,

```text
1 photon
-> microscopic material-state difference
-> gain / avalanche / transduction
-> macroscopic current or voltage record,
```

the amplification stage should not be described as creating fundamental information about whether the photon arrived. It makes an already encoded distinction more robust against downstream noise and imperfect readout.

This suggests a useful conceptual separation:

```text
information acquisition
!=
information amplification / stabilization.
```

## Irreversibility boundary

For a closed photon + detector + environment system, microscopic evolution can remain unitary while information becomes distributed over many degrees of freedom. Operational irreversibility emerges when recovering the original coherence would require control of inaccessible environmental correlations.

Therefore the detector boundary may be more naturally connected to

```text
record formation
+
metastability
+
decoherence / information dispersal
+
readout accessibility
```

than to absorption alone.

The exact relation between these concepts remains **OPEN** and must be stated with a precise system partition. Information absent from the reduced detector state can still reside in outgoing light or the environment.

## Current frontier

The strongest next question is no longer

> How many atoms make a photodetector?

It is

> **Given a required discrimination error, observation time, thermal environment, allowed measurement access, and reset requirement, what minimum physical disturbance or resource is required to create a robust photon-arrival record?**

That frontier naturally connects photodetection to quantum measurement back-action, detector noise, metastability, energy dissipation, reset costs, dark events, and information theory.

No universal energy-per-detection or Landauer-per-event result is assumed. Those are hypotheses to test, not conclusions.

## Reading order

1. [`AGENTS.md`](AGENTS.md) — experiment-specific reasoning and documentation locks.
2. [`CURRENT_STATE_LIVE.md`](CURRENT_STATE_LIVE.md) — current frontier and definitions.
3. [`CLAIM_LEDGER.md`](CLAIM_LEDGER.md) — what is known, derived, invalidated, conditional, or open.
4. [`RESEARCH_LOG.md`](RESEARCH_LOG.md) — chronological path, including discarded formulations.

## Research rule

Follow the physics rather than a desired paper result. Preserve counterexamples and failed boundaries. Before any novelty claim, perform a focused primary-source audit; negative search results are not novelty evidence.
