# AGENTS.md — Experiment 02 Research Protocol

**Experiment:** `02-photodetector-boundary`  
**Mode:** exploratory first-principles Gedanken experiment  
**Priority:** unassessed; no novelty claim

Root `AGENTS.md` remains authoritative for repository privacy/preservation. This file adds Experiment-02-specific scientific locks.

## 1. Canonical reading order

1. `CURRENT_STATE_LIVE.md`
2. `CLAIM_LEDGER.md`
3. `RESEARCH_LOG.md`
4. `README.md`
5. `INTERACTION_ACTION_LOWER_BOUND.md`
6. `N_DIPOLE_SINGLE_MODE_MODEL.md`
7. `COHERENT_CAPTURE_TO_RECORD.md`
8. `TRAVELING_WAVE_CAPTURE.md`
9. `MODE_WEIGHTED_OPTICAL_DEPTH.md`
10. `SEMICONDUCTOR_DECISION_BRIDGE.md`
11. `CONTINUOUS_GAUSSIAN_DECISION.md`
12. `SIGNAL_DEPENDENT_NOISE.md`
13. `UNKNOWN_ARRIVAL_TIME.md`
14. `TASK_SPECIFIC_DETECTIVITY.md`
15. `RESET_AND_CYCLE_CLOSURE.md`
16. `SOURCE_INCLUSIVE_THERMODYNAMIC_CLOSURE.md`
17. `REFERENCE_FRAME_ACCESS.md`
18. `CRITICAL_MATCHING_CONTROL_PRECISION.md`
19. `PARALLEL_CHANNEL_RESOURCE.md`
20. `DETECTOR_CHANNEL_ORDERING.md`
21. `CORRELATING_CATALYSTS.md`
22. `SINGLE_SHOT_RESOURCE_CLOSURE.md`
23. `CAUSAL_LATENCY_AND_CONTROL_STRENGTH.md`

Do not reconstruct the frontier from chat summaries when repository files are available.

## 2. Current research objective

The original question was:

> At what point does a collection of atoms become a photodetector?

The live formulation is now:

> **What detector channels/processes are physically achievable under a closed, explicitly stated resource model, and when does one detector process universally dominate another for the declared optical task family?**

Current chain:

```text
optical input family / task
-> allowed operations + phase/time references
-> optical access / mode overlap
-> microscopic coupling / interaction action
-> interaction time / bandwidth
-> control range / precision
-> acquisition/extraction versus loss
-> persistent record
-> complete conditional output process
-> timing / parallel-channel structure
-> optimum decision
-> detector-channel / process ordering
-> record export / local reset
-> source-inclusive information accounting
-> correlation/catalyst accounting
-> one-shot resource guarantees
-> causal/control/power accounting for finite latency.
```

The strongest current conclusion is that detection is a **task- and resource-dependent channel/process relation**, not a universal atom-count transition, one scalar score, or one fixed thermodynamic cost.

## 3. Permanent semantic locks

### Absorption is not the definition

Absorption is neither sufficient nor universally necessary for the operational detector criterion.

### Re-emission and electron-hole generation are not mutually exclusive

An interband electron-hole excitation can later recombine radiatively.

### No universal atom-count threshold

Do not claim `N_c` without explicit architecture/resource constraints.

### Literal total N is usually the wrong constrained coordinate

For unequal couplings,

```math
G^2=\sum_j|g_j|^2.
```

Use mode-weighted oscillator strength, optical depth, or the appropriate overlap functional.

### Electron-hole generation is not a complete detector event

Separate generation from dissociation, recombination, extraction/collection, persistent record, and readout.

### Gain does not create missing upstream information

Treat gain as practical stabilization/enlargement unless an explicit additional information-bearing resource enters.

### Irreversibility must be qualified and rate matched

Do not use irreversibility as a primitive detector threshold. Overly strong trapping can reduce coherent acquisition in current models.

### Peak monochromatic efficiency does not imply minimum N without time/control constraints

Critical matching can give unit narrowband capture for arbitrarily weak nonzero coupling only if arbitrarily slow and sufficiently precise matched dynamics are allowed.

A nonzero `Gamma_floor`, finite bandwidth, or finite control resolution can restore a positive constrained `N_min`.

### Scalar D* is not the detector boundary

In the one-pole white-noise benchmark,

```math
d^2=E^2D^{*2}/(A\tau).
```

Equal scalar `D*` can hide different event performance.

### Mean signal is not the complete output information

If the optical history changes covariance or count statistics, the full conditional distribution matters.

### Known timing is a resource assumption

Unknown arrival time creates a search/trials penalty.

### Unlimited parallelism is not free

Independent evidence can add across channels, while unknown active-channel identity creates a trials penalty. Bound total channel capacity explicitly.

### Unrestricted trace distance assumes unrestricted measurement access

Symmetry-restricted measurements without an adequate phase/time reference can make globally distinct states operationally indistinguishable.

### No universal scalar detector ranking

Use complete detector statistical/quantum channels. Universal dominance is a hypothesis-independent post-processing / degradation partial order.

### Marginal catalyst return is not strict cyclic return

A catalyst can return with the same local state while becoming correlated with source/detector/output systems. If strict reuse is required, demand decoupling or explicitly bound/charge residual correlations.

### One-shot guarantees are not determined by averages

Mean entropy, free energy, work, latency, or power do not determine finite-cycle tails. State resource-overrun/error tolerance and whether the claim is average, quantile, or worst case.

### Power is not interaction strength

A strong hypothesis-dependent Hamiltonian can generate fast state separation with little net energy deposition. Do not infer a universal speed limit from watts alone.

### Precharged energy must be accounted separately

Fast triggered output can be powered by energy stored before the event. Distinguish event-window power, stored free energy, recharge power, and average cycle power.

### Causal latency requires output geometry

A size-only `L/c` claim is incomplete unless event locations, output locations/ports, and allowed local decisions are specified.

### Landauer is not a per-click acquisition or local-reset axiom

Record export, source side information, reversible uncomputation, and optical/pump free energy all matter.

### Source-inclusive erasure does not imply positive external detector work

Account all consumed nonequilibrium free-energy resources before asserting a positive work bound.

### Barrier height is not automatically dissipated work

Activated retention/reset formulas give stability/control-range requirements, not universal heat costs.

## 4. Mandatory system/resource boundary discipline

Every theorem must state:

```text
input hypothesis/state family and priors;
accessible detector/output subsystem;
allowed measurements / channels / feedback operations;
phase/time reference resources and ancillas;
spatial modes / channel count / output locations;
interaction-strength and time/bandwidth limits;
control range / precision;
noise and dark-event process;
record-retention/reset requirements;
side information / exported records;
catalysts and whether correlated return is allowed;
mean versus one-shot/worst-case resource guarantee;
stored free energy, work reservoirs, pumps, and bath;
causal communication constraints.
```

Never claim information, entropy, or resource state is restored merely because one local marginal returned to its initial value.

## 5. Keep these boundaries distinct

```text
(1) finite atomic spectrum -> band-like spectrum
(2) allowed-operation / reference access
(3) optical access / mode coupling
(4) bound excitation -> mobile carriers
(5) optical interaction -> encoded information
(6) encoded information -> persistent record
(7) record -> electrical/output process
(8) output process -> decision under noise/timing uncertainty
(9) detector-channel / detector-process comparison
(10) local reset / record export
(11) source-inclusive information/free-energy closure
(12) repeated-use correlation / catalyst closure
(13) one-shot resource guarantee
(14) finite-latency causal/control closure.
```

A result at one boundary must not be promoted to another without derivation.

## 6. Detector-channel / process ordering rule

For a memoryless classical detector,

```math
K_D(y|x)=P_D(Y=y|X=x).
```

If

```math
K_B=T\circ K_A
```

for hypothesis-independent post-processing `T`, A can reproduce every decision strategy available to B.

If neither channel is a post-processing of the other, expect task-dependent incomparability rather than forcing a scalar score.

For repeated operation with hidden/catalytic memory, use the full process

```math
P(y_1,\ldots,y_n|x_1,\ldots,x_n)
```

rather than assuming

```math
\prod_kK_D(y_k|x_k).
```

At the quantum level use the proper quantum channel/process comparison framework and ancillary-resource discipline.

## 7. Counterexample-first procedure

Before accepting a universal lower bound:

1. state the resource and all constraints mathematically;
2. identify excluded degrees of freedom, references, channels, controls, memories, and reservoirs;
3. attack with single-atom, dispersive, cavity/critical-coupling, narrowband/long-time, reference-frame, parallel-channel, correlated-catalyst, reversible-memory, exported-record, source-side-information, active-pump, precharged-energy, and task-change counterexamples where relevant;
4. test average-resource claims against rare-event/single-shot tails;
5. test latency claims against stored energy, local outputs, and spatial parallelism;
6. distinguish theorem failure from a missing resource coordinate;
7. preserve the failed claim in `CLAIM_LEDGER.md` and `RESEARCH_LOG.md`;
8. only then narrow the statement.

Do not silently add assumptions after a counterexample appears.

## 8. Epistemic labels

Use explicitly:

- **KNOWN**
- **DERIVED**
- **CHECKED**
- **CONDITIONAL**
- **CANDIDATE DISTINCT — PRIORITY UNPROVEN**
- **INVALIDATED**
- **SUPERSEDED**
- **OPEN**
- **NON-CLAIM**

A negative literature search is not novelty evidence.

## 9. Prior-art rule

Before novelty language, audit at minimum:

```text
quantum photodetection / state discrimination
quantum speed limits
Dicke / Tavis-Cummings collective coupling
input-output theory / critical coupling / cooperativity
single-photon absorption / optical depth
semiconductor carrier collection
detection theory / matched filtering / Poisson decisions
timing-search statistics
NEP / D* conventions
Blackwell comparison / statistical experiments
quantum channel/process comparison
reference-frame / asymmetry resource theory
correlated catalytic transformations / channel memory
reversible information processing
Landauer erasure with classical/quantum side information
one-shot / finite-size information thermodynamics
nonequilibrium work/free-energy resource theories.
```

Most ingredients are established. Candidate distinction, if any, is likely a narrowly constrained detector-specific synthesis or resource theorem.

## 10. Documentation rule

After every substantive batch:

- update `CURRENT_STATE_LIVE.md` when the frontier changes;
- update `CLAIM_LEDGER.md` for new/invalidated/superseded claims;
- update `RESEARCH_LOG.md` with why the direction changed;
- add a dedicated derivation file when algebra/numerics/literature become too large for live state;
- keep `README.md`, root README, and draft PR summary aligned at major frontier changes.

`CURRENT_STATE_LIVE.md` should remain concise; detailed derivations and failed routes belong in their dedicated files and chronology/ledger.

Never delete a failed route merely because a stronger formulation exists.

## 11. Current next attack

The live next question is **adaptive distributed measurement**:

> Does adaptivity create a genuinely new detector resource coordinate, or is it fully captured by the general detector-process framework once communication latency, controller memory, references, and feedback operations are charged?

Attack protocols with

```text
sequential measurement + feedback;
spatially distributed partial measurements;
dynamic reallocation of reference resources;
measurement-dependent stopping times;
pre-shared correlations / entanglement;
local versus centralized decisions.
```

After that, reassess whether the resource ledger is sufficiently closed to attempt a detector-process resource-conversion theorem.
