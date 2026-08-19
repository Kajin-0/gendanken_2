# Experiment 02 — Final Current Disposition

**Date:** 2026-08-12  
**Status:** original Gedanken question conceptually resolved; no novelty claim; retain as rigorous synthesis  
**Manuscript status:** no manuscript recommended from the broad framework

## 1. Original question

> At what point does a simple collection of atoms become a photodetector?

The experiment intentionally began without assuming that the answer would be band formation, electron-hole generation, absorption, irreversibility, or a critical number of atoms.

## 2. Final current answer

> **There is no observer-independent atom-count or condensed-matter boundary at which matter suddenly becomes a photodetector. A physical subsystem functions as a detector only relative to a declared measurement architecture: optical alternatives must induce distinguishable accessible output processes, and the architecture must terminate in a usable measurement outcome under the allowed operations/resources. Band formation, electron-hole generation, absorption, amplification, carrier collection, and persistent local memory are implementation mechanisms, not the universal definition.**

This is an organizing conclusion, not a novelty claim.

## 3. Formal transducer/detector distinction once the boundary is fixed

A coherent transducer can be represented schematically as

```math
\Phi:\rho_{\rm opt}\mapsto\rho_Q.
```

It maps optical information into another quantum degree of freedom.

A detector endpoint instead supplies a classical outcome through a measurement channel / instrument, e.g.

```math
\mathcal M(\rho)
=
\sum_y\operatorname{Tr}(E_y\rho)
|y\rangle\langle y|.
```

A full instrument can additionally preserve a conditional residual quantum state.

Thus the distinction is objective **after** the input/output partition and classical readout are declared, but no atom count determines where that partition must be drawn.

## 4. Main universal-bound candidates that failed

The experiment explicitly invalidated or narrowed all of the following as universal detector boundaries:

```text
critical atom count;
band formation;
photon absorption;
electron-hole generation;
persistent local material memory;
microscopic irreversibility;
gain;
final deposited energy;
fixed Landauer cost per click;
scalar D*;
absorber thickness;
peak monochromatic efficiency;
literal total atom number;
one fixed-noise SNR;
one universal detector ranking.
```

Each failure exposed a missing system/resource/task coordinate rather than a new universal scalar.

## 5. What atom count actually changes

Atom count matters indirectly because it can change

```text
spectral density / band-like structure;
collective light-matter coupling;
mode overlap / oscillator strength;
optical depth;
thermalization pathways;
transport mechanisms;
dark-active volume;
geometry and timing;
number of available output channels.
```

Under explicit constraints, these dependencies can produce real `N_min` laws. Those are architecture/resource-specific thresholds, not an ontological transition to `detector matter`.

## 6. Main quantitative examples retained

Useful conditional examples include:

### Interaction-action benchmark

```math
\mathcal A_\Delta
\ge
\hbar\arcsin(1-2\epsilon).
```

### Collective dipoles

```math
G=g\sqrt N.
```

### One-port critical matching

```math
\Gamma_{\rm match}=4G^2/\kappa.
```

### Gaussian waveform decision distance

```math
d^2
=\int|\tilde p(f)|^2/\mathrm{NEP}_2^2(f)df.
```

For the explicit one-sided one-pole benchmark,

```math
d^2=E^2D^{*2}/(A\tau).
```

### Semiconductor scaling class

```math
\eta_s\sim SL^s,
\qquad
\mu_d\sim KL^p
```

implies, in the stated asymptotic decision regime,

```math
L_*\sim(s/pK)^{1/p},
\qquad
\mu_*=s/p.
```

These illustrate the main lesson: detector thresholds appear only after specific compensating resources are bounded.

## 7. Broad-framework novelty disposition

Primary-source audit found direct or close prior art for the broad formal layers:

```text
statistical-experiment comparison / Blackwell ordering;
approximate comparison / deficiency;
quantum statistical/channel comparison;
quantum combs / multi-round processes;
photodetector POVM-based figures of merit;
general microscopic quantum photodetector modeling;
coherence/backaction limits;
optimum-filter / full-NEP event-energy detection.
```

Therefore the provisional detector-process framework is retained as a **useful synthesis/bookkeeping language**, not a new foundational theory.

## 8. Semiconductor-branch disposition

The semiconductor thickness/dark-event branch produced a robust reduced scaling family and survived stronger observers/refinements, but realistic SPAD/APD architecture stress showed that the exponent and coefficients are mechanism dependent.

It is therefore closed as a primary novelty route and retained as a rigorous conceptual/device-modeling demonstration.

## 9. Strongest scientific value of Experiment 02

The experiment has produced a transparent chain showing why the original question has no material-threshold answer:

```text
atoms
-> available microscopic interactions
-> transduction pathways
-> accessible output channel/process
-> allowed readout/measurement
-> decision task.
```

The boundary is architectural and operational.

This resolves the original conceptual confusion between

```text
absorption/re-emission;
electron-hole generation;
and photodetection.
```

## 10. Documentation status

The repository preserves:

```text
live-state files;
claim ledgers and addenda;
chronological research log;
agent handoff/protocol;
all detailed derivations;
all failed routes;
all prior-art audits;
semiconductor/device stress tests;
provisional synthesis framework.
```

Failed statements remain visible because they define the path by which the final answer was reached.

## 11. Recommendation

Do **not** continue adding abstract resource coordinates to Experiment 02 merely to force novelty.

Do **not** draft a paper claiming a new general photodetector framework.

Keep Experiment 02 as a rigorous conceptual synthesis unless a separately identified narrow physical theorem emerges from future work.

If new research is desired, open a new Gedanken experiment with a new sharply posed physical question rather than disguising a new topic as unfinished work here.

## 12. Natural next research question, if a new experiment is opened

A productive next question should begin from one unresolved physical constraint rather than from `what is a detector?`.

One candidate suggested by this work is:

> **Given a physically fixed photodetector architecture and a fixed total resource budget, what transformations of bandwidth, dark-event statistics, gain, timing, and readout preserve the complete decision experiment—and which tradeoffs are fundamentally impossible?**

That would be a different experiment and should receive a separate directory/claim ledger rather than being appended to Experiment 02.
