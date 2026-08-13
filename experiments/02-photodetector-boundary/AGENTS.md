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

Do not reconstruct the frontier from chat summaries when repository files are available.

## 2. Current research objective

Follow the strongest surviving consequence of:

> At what point does a collection of atoms become a photodetector?

The live chain is

```text
optical task / hypothesis family
-> allowed operations + reference resources
-> optical access / mode overlap
-> mode-weighted interaction resource
-> microscopic transduction
-> acquisition/extraction versus loss
-> persistent record
-> complete conditional output process
-> timing / nuisance parameters
-> optimum decision
-> detector-channel / statistical-experiment ordering
-> record export / local reset
-> source-inclusive information accounting
-> nonequilibrium free-energy accounting when cyclic thermodynamics is imposed.
```

The strongest current conclusion is that detection is a **task- and resource-dependent channel relation**, not a universal atom-count transition, one scalar detector score, or one fixed thermodynamic cost.

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

Only optically participating matter contributes appreciably. Use mode-weighted oscillator strength, optical depth, or the appropriate overlap functional.

### Electron-hole generation is not a complete detector event

Separate generation from dissociation, recombination, extraction/collection, persistent record, and readout.

### Gain does not create missing upstream information

Treat gain as practical stabilization/enlargement unless an explicit additional information-bearing resource enters.

### Irreversibility must be qualified and rate matched

Do not use irreversibility as a primitive detector threshold. Overly strong trapping can reduce coherent acquisition in the current models.

### Peak monochromatic efficiency does not imply minimum N without control/time constraints

Critical matching can give unit narrowband capture for arbitrarily weak nonzero coupling only if arbitrarily slow and sufficiently precise matched dynamics are allowed.

A nonzero `Gamma_floor` or finite control resolution can restore a positive constrained `N_min`.

### Scalar D* is not the detector boundary

In the one-pole white-noise benchmark,

```math
d^2=E^2D^{*2}/(A\tau).
```

Equal scalar `D*` can therefore hide different event performance.

### Mean signal is not the complete output information

If the photon history changes covariance or count statistics, the full conditional distribution matters. A fixed-noise matched filter is only a special case.

### Known timing is a resource assumption

Unknown arrival time creates a search/trials penalty. Never quote known-time `d` as a full event metric without stating timing knowledge.

### Unlimited parallel channel count is not free

Independent evidence can add across channels, but unknown active-channel identity creates a trials penalty. Any per-channel theorem must state whether total channel count/capacity is bounded.

### Unrestricted trace distance assumes unrestricted measurement access

If allowed operations obey a symmetry and no phase/time reference is available, globally distinct optical states can become operationally indistinguishable.

State detector performance as distinguishability under the **allowed measurement operations and available reference frames**.

### No universal scalar detector ranking

Within the Gaussian waveform class, crossing spectral decision kernels already cause task-dependent ranking reversal.

More generally, treat the detector as a statistical/quantum channel. Universal dominance is a **channel post-processing / degradation partial order**, not a scalar leaderboard.

### Landauer is not a per-click acquisition or local-reset axiom

A local detector can export its record. `k_B T ln2` applies only under stronger logical-erasure conditions and for an unbiased bit.

### Detector-memory closure is not source-inclusive closure

A surviving source/reference variable can allow reversible uncomputation of the detector memory. Include all usable side information before claiming erasure.

### Source-inclusive erasure does not imply positive external detector work

Optical or pump nonequilibrium free energy can pay the information-processing cost. Account available free-energy decrease before asserting a positive work bound.

### Barrier height is not automatically dissipated work

Activated retention/reset formulas produce conditional stability/control-range requirements, not universal heat bounds.

## 4. Mandatory system-boundary and operation-set discipline

At the quantum level, specify

```text
accessible subsystem;
allowed POVMs / channels;
reference frames / clocks;
ancillas / side information.
```

Unrestricted trace distance

```math
\mathcal D_D
=\frac12\|\rho_D^{(1)}-\rho_D^{(0)}\|_1
```

is the all-POVM benchmark, not automatically the achievable distance under symmetry/control restrictions.

At the classical output level, specify the complete conditional output distributions/processes and observation interval.

At the thermodynamic level, specify whether the accounting boundary includes

```text
detector memory
controller
readout register
external record store
optical source/reference
outgoing optical/environmental degrees of freedom
work reservoirs / bias / pumps
bath
correlation / coherence resources.
```

Never claim information or entropy has disappeared merely because it left one chosen subsystem.

## 5. Keep these boundaries distinct

```text
(1) finite atomic spectrum -> band-like spectrum
(2) reference/operation access
(3) optical access / mode coupling
(4) bound excitation -> mobile carriers
(5) optical interaction -> encoded information
(6) encoded information -> persistent record
(7) record -> electrical/output process
(8) output process -> decision under noise/timing uncertainty
(9) detector-channel comparison / task ordering
(10) local reset / record export
(11) source-inclusive resource closure.
```

A result at one boundary must not be promoted to another without derivation.

## 6. Active resource coordinates

Depending on architecture, useful quantities include

```math
\eta_{\rm esc}=\kappa_{\rm in}/\kappa,
```

```math
C_N=4G^2/(\kappa\gamma),
```

```math
\Gamma/(4G^2/\kappa),
```

```math
B/(4G^2/\kappa),
```

```math
\alpha L,
```

```math
\Gamma_{\rm ext}/\Gamma_{\rm rec},
```

```math
R_d\tau,
```

```math
d^2=\int |\tilde s(f)|^2/S_n^{(2)}(f)\,df,
```

```math
M_{\rm eff}\text{ or the full timing prior},
```

and for cyclic/resource accounting

```math
h(p),\quad H(M|R),\quad \Delta F_{\rm opt}^{\rm avail},\quad \Delta F_{\rm pump}^{\rm avail}.
```

Also state explicitly

```text
reference-frame quality;
control-rate floor / precision;
parallel channel count and occupancy knowledge;
exported-record capacity.
```

Do not assume one scalar can replace the full resource ledger.

## 7. Detector-channel ordering rule

For a declared input family `X`, treat a classical detector as

```math
K_D(y|x)=P_D(Y=y|X=x).
```

If

```math
K_B=T\circ K_A
```

for hypothesis-independent post-processing `T`, then A can reproduce every decision strategy available to B.

Use this as the strongest current meaning of

```text
A is universally at least as informative as B.
```

If neither channel is a post-processing of the other, expect task-dependent ranking/incomparability rather than forcing a scalar score.

At the quantum level, analogous post-processing/channel-comparison statements require their proper quantum conditions and ancillary-resource discipline.

## 8. Counterexample-first procedure

Before accepting a universal lower bound:

1. state the resource and all constraints mathematically;
2. identify excluded degrees of freedom, references, channels, controls, and reservoirs;
3. attack with single-atom, dispersive, cavity/critical-coupling, narrowband/long-time, reference-frame, parallel-channel, reversible-memory, exported-record, source-side-information, active-pump, external-reservoir, and task-change counterexamples where relevant;
4. distinguish theorem failure from a missing resource coordinate;
5. preserve the failed claim in `CLAIM_LEDGER.md` and `RESEARCH_LOG.md`;
6. only then narrow the statement.

Do not silently add assumptions after a counterexample appears.

## 9. Epistemic labels

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

## 10. Prior-art rule

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
quantum channel comparison / deficiency
reference-frame / asymmetry resource theory
reversible information processing
Landauer erasure with classical/quantum side information
nonequilibrium work/free-energy resource theories.
```

Most ingredients are established. Candidate distinction, if any, is likely only in a narrowly constrained detector-specific synthesis or resource theorem.

## 11. Documentation rule

After every substantive step:

- update `CURRENT_STATE_LIVE.md` when the frontier changes;
- update `CLAIM_LEDGER.md` for new/invalidated/superseded claims;
- update `RESEARCH_LOG.md` with why the direction changed;
- add a dedicated derivation file when algebra/numerics/literature become too large for live state;
- keep `README.md` and the draft PR summary aligned at major frontier changes.

Never delete a failed route merely because a stronger formulation exists.

## 12. Current next attack

Do **not** return to a universal scalar or simple Landauer bound.

The live question is:

> Can the physically achievable detector channels be characterized by a resource ledger that remains closed under counterexamples?

The current candidate resources are

```text
optical-state input family / distinguishability
allowed operations + phase/time references
mode overlap / optical access
interaction action / coupling
interaction time / bandwidth
control range / precision
parallel channel count
noise / dark-event statistics
timing prior / synchronization
side information / exported-record capacity
nonequilibrium free energy / pumps
retention / reset requirements.
```

Attack this ledger next with

```text
correlating catalysts;
finite-size / single-shot fluctuations;
causal latency / maximum power;
spatially distributed adaptive measurement;
resource states that return locally unchanged but degrade through correlations.
```

Only after those attacks should a resource-conversion theorem be attempted.
