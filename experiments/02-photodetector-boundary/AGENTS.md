# AGENTS.md — Experiment 02 Research Protocol

**Experiment:** `02-photodetector-boundary`  
**Mode:** exploratory first-principles Gedanken experiment  
**Priority:** unassessed; no novelty claim

Root `AGENTS.md` remains authoritative for repository privacy/preservation. This file adds Experiment-02 scientific and documentation locks.

## 1. Canonical reading order

Read in this order:

1. `CURRENT_STATE_LIVE.md`
2. `CLAIM_LEDGER.md`
3. `CLAIM_LEDGER_PROCESS_ADDENDUM.md`
4. `RESEARCH_LOG.md`
5. `README.md`
6. specialized derivation files as cited by the live state/log
7. `PROVISIONAL_DETECTOR_PROCESS_FRAMEWORK.md` for the current synthesis

Do not reconstruct the frontier from chat summaries when repository files are available.

## 2. Current research objective

The original question was:

> At what point does a collection of atoms become a photodetector?

The live question is now:

> **What optical-to-accessible-output detector processes are physically achievable under an explicit resource model, and when does one detector process universally dominate another for the declared task family?**

The current organizing chain is

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
-> adaptive strategy / controller memory / communication
-> optimum decision
-> detector-channel / process ordering
-> record export / local reset
-> source-inclusive information accounting
-> catalyst/correlation accounting
-> one-shot resource guarantees
-> causal/control/power accounting for finite latency.
```

## 3. Permanent semantic locks

- **Absorption is not the definition.** It is neither sufficient nor universally necessary under the operational criterion.
- **Electron-hole generation is not a complete detector event.** Separate generation from collection, recombination, persistent record, and readout.
- **No universal atom-count threshold.** `N_min` can emerge only after another compensating resource is bounded.
- **Literal total N is usually not the invariant microscopic resource.** Use mode-weighted coupling, optical depth, oscillator strength, etc.
- **Gain does not create missing upstream information.** Treat it as transduction/stabilization unless an additional correlated resource enters.
- **Irreversibility must be qualified and rate matched.** More trapping is not automatically better.
- **Peak monochromatic efficiency does not imply a minimum N when arbitrarily long/narrowband and exact control are free.** Finite bandwidth/control range restores constrained thresholds.
- **Scalar `D*` is not the detector boundary.** Equal `D*` can coexist with different event performance.
- **Mean signal is not the complete output information.** Hypothesis-dependent covariance/count statistics can carry information.
- **Known timing is a resource assumption.** Unknown timing creates a search/trials penalty.
- **Unlimited parallelism is not free.** Evidence can add across channels; unknown active-channel identity adds a search penalty.
- **Unrestricted trace distance assumes unrestricted measurement/reference access.** Phase/time references are explicit resources.
- **No universal scalar detector ranking.** Use complete detector channels/processes and task-relative risk.
- **Marginal catalyst return is not strict cyclic return.** Residual correlations must be forbidden, bounded, or charged.
- **Average resources do not determine one-shot guarantees.** State mean versus quantile/worst-case and the allowed overrun probability.
- **Power is not interaction strength.** Strong conditional Hamiltonians can generate fast distinguishability without large net energy deposition.
- **Precharged energy is a separate resource.** Distinguish event-window power, stored free energy, recharge power, and average rate.
- **Causal latency requires geometry/output locations.** A bare detector-size `L/c` statement is incomplete.
- **Adaptivity is a strategy class, not a primitive scalar resource.** Charge controller memory, sequential opportunities, communication, references, pre-shared correlations, and stopping-time freedom.
- **Landauer is not a per-click axiom.** Record export, source side information, reversible uncomputation, and optical/pump free energy matter.

## 4. Mandatory boundary/resource discipline

Every proposed theorem must state, as relevant:

```text
input state/hypothesis family and priors;
accessible output subsystem/process;
allowed measurements / controls / feedback;
phase/time references and ancillas;
mode overlap and spatial channels;
interaction strength/action and duration/bandwidth;
loss/trapping/retention;
control range/precision;
noise and dark-event process;
timing prior and synchronization;
controller memory and communication latency;
side information / exported records;
catalyst dimension and correlation tolerance;
mean versus one-shot/worst-case guarantee;
stored free energy, pumps, work reservoirs, bath;
required output locations and causal constraints;
reset/source-inclusive cycle-closure requirements.
```

Never say information/resource state is restored merely because one local marginal returned to its initial value.

## 5. Detector channel/process rule

For a memoryless classical detector,

```math
K_D(y|x)=P_D(Y=y|X=x).
```

If

```math
K_B=T\circ K_A
```

for hypothesis-independent post-processing `T`, A can simulate every decision strategy available from B for the same experiment. This is the classical Blackwell/garbling structure.

For repeated/adaptive operation with memory, use the full process

```math
P(y_1,\ldots,y_n|x_1,\ldots,x_n)
```

or the appropriate quantum higher-order process rather than assuming a product of one-use channels.

## 6. Provisional capability framework

For detector hardware `D`, resource model `R`, and allowed strategy set `Sigma_D(R)`, the current provisional object is

```math
\mathfrak C_D(R)
=\{K_{D,\sigma}^{(R)}:\sigma\in\Sigma_D(R)\}.
```

A representative process may include accessible record `y`, completion time `t`, and resource-consumption vector `c`:

```math
K_{D,\sigma}^{(R)}(dy\,dt\,dc|x).
```

For decision problem `Pi`,

```math
R_D^*(\Pi|R)
=\inf_{K\in\mathfrak C_D(R)}\inf_\delta R(\delta,K;\Pi)
```

subject to the declared resource/latency constraints.

This is **provisional**, not a theorem of completeness.

## 7. Counterexample-first procedure

Before accepting a universal limit:

1. State the resource and constraints mathematically.
2. Identify excluded degrees of freedom, references, memories, controls, channels, and reservoirs.
3. Attack with relevant counterexamples: single atom, dispersive/QND, cavity/critical coupling, long-time/narrowband, reference frame, parallel channels, adaptive stopping, correlated catalyst, reversible memory, record export, source side information, active pump, precharged energy, and task changes.
4. Attack average claims with one-shot tails.
5. Attack latency claims with local outputs, spatial parallelism, stored energy, and communication geometry.
6. Distinguish theorem failure from a missing resource coordinate.
7. Preserve the failed statement in the ledger/log rather than silently adding assumptions.

## 8. Epistemic vocabulary

Use explicitly: **KNOWN**, **DERIVED**, **CHECKED**, **CONDITIONAL**, **CANDIDATE DISTINCT — PRIORITY UNPROVEN**, **INVALIDATED**, **SUPERSEDED**, **OPEN**, **NON-CLAIM**.

A negative literature search is not novelty evidence.

## 9. Prior-art rule

Before novelty language, audit primary literature for at least:

```text
photodetection POVM/instrument theory;
classical statistical experiments / Blackwell / Le Cam comparison;
quantum statistical experiments and channel comparison;
quantum combs/testers/process tensors;
quantum speed limits;
Dicke/Tavis-Cummings collective coupling;
critical coupling/cooperativity;
reference-frame/asymmetry resource theory;
correlated catalysis;
one-shot information thermodynamics;
reversible information processing / Landauer with side information;
semiconductor carrier collection;
Gaussian/Poisson detection theory;
NEP / D* conventions.
```

Most ingredients are established. Any candidate distinction is likely only in a narrowly defined photodetector-specific synthesis or resource theorem.

## 10. Documentation rule

After every substantive batch:

- update `CURRENT_STATE_LIVE.md` when the frontier changes;
- update `CLAIM_LEDGER.md` or an explicit addendum for new/invalidated/superseded claims;
- update `RESEARCH_LOG.md` with why the direction changed;
- add a dedicated derivation file for substantial algebra/numerics/literature;
- keep Experiment 02 `README.md`, root navigation, and draft PR summary aligned at major frontier changes.

`CURRENT_STATE_LIVE.md` should stay concise. Do not duplicate every derivation into it.

Never delete a failed route merely because a stronger formulation exists.

## 11. Current frontier

Do **not** add more resource coordinates by default and do **not** invent another generalized scalar.

The next work is two adversarial audits of `PROVISIONAL_DETECTOR_PROCESS_FRAMEWORK.md`:

### Mathematical/prior-art audit

Compare directly against Blackwell/Le Cam statistical experiments, quantum statistical experiments/channel comparison, quantum combs/testers/process tensors, classical/quantum decision theory, and photodetection POVM/instrument theory.

### Physical closure attack

Try edge cases including indefinite causal order, unbounded-dimensional references/catalysts, continuous quantum fields, computationally bounded observers, and nonstationary/adversarial source processes.

No manuscript or novelty claim should be attempted before these audits.
