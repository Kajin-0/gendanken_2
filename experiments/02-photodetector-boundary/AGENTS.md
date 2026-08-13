# AGENTS.md — Experiment 02 Research Protocol

**Experiment:** `02-photodetector-boundary`  
**Mode:** exploratory first-principles Gedanken experiment  
**Priority:** unassessed; no novelty claim

Read this file before extending Experiment 02.

Root `AGENTS.md` remains authoritative for repository privacy, preservation, and general scientific-integrity rules. This file adds Experiment-02-specific locks.

## 1. Canonical reading order

1. `CURRENT_STATE_LIVE.md`
2. `CLAIM_LEDGER.md`
3. `RESEARCH_LOG.md`
4. `README.md`
5. specialized derivations/results added later

Do not reconstruct the current frontier from chat summaries when the repository files are available.

## 2. Research objective

Follow the strongest surviving consequence of the question:

> At what point does a collection of atoms become a photodetector?

Do not force the project toward a predetermined semiconductor answer, theorem, or paper.

The current operational route is

```text
optical hypothesis
-> photon-matter interaction
-> accessible material-state distinguishability
-> persistence / metastability
-> readout under noise
-> reset / reuse.
```

The current deepest open problem is to determine whether explicit performance constraints imply a nontrivial minimum physical resource for a robust photon-arrival record.

## 3. Semantic locks — do not regress

### Absorption is not the definition

Do not equate

```text
photon absorbed
```

with

```text
photon detected.
```

Absorption is neither sufficient nor universally necessary under the current operational definition.

### Re-emission versus carrier generation

Do not describe photon re-emission and electron-hole generation as mutually exclusive alternatives. Interband absorption can create an electron-hole excitation that later recombines radiatively.

### No universal atom-count threshold

Do not claim a critical `N_c` without first imposing explicit architecture/resource constraints. A finite-size electronic-structure crossover is not automatically a detector boundary.

### Electron-hole generation is not the complete detection event

Carrier creation must be separated from exciton dissociation, transport, collection, gain, retention, and readout.

### Gain does not create the original hypothesis information

Treat gain as a mapping that can make an existing distinction robust against subsequent noise/readout limitations. If claiming an information increase, specify the system boundary and what additional correlated resource entered.

### Irreversibility must be qualified

Do not invoke "irreversibility" as a primitive microscopic threshold. State whether the claim concerns a reduced subsystem, decoherence, environmental information dispersal, metastability, thermodynamic entropy production, or logical reset.

### Landauer is not a per-click axiom

Do not assert `k_B T ln 2` as the minimum energy dissipated by every photon-detection event. Separate measurement interaction, memory stabilization, logical erasure/reset, and cycle requirements.

## 4. Mandatory system-boundary discipline

Every information-theoretic statement must specify what is accessible.

For the binary optical hypotheses, use

```math
\rho_D^{(n)}
=
\operatorname{Tr}_{\overline D}
\left[
U( |n\rangle\langle n|\otimes\rho_D )U^\dagger
\right].
```

The trace distance

```math
\mathcal D_D
=\frac12\|\rho_D^{(1)}-\rho_D^{(0)}\|_1
```

is meaningful only relative to the chosen subsystem `D` and allowed measurement class.

Do not say "the information is gone" merely because it is absent from `D`; it may reside in the outgoing optical field or environment.

## 5. Separate the five boundaries

Always distinguish:

```text
(1) finite atomic spectrum -> band-like spectrum
(2) bound excitation -> mobile carriers
(3) optical interaction -> encoded material information
(4) encoded information -> persistent/metastable record
(5) record -> useful decision under noise
```

A result about one boundary must not be promoted into a statement about another without derivation.

## 6. Epistemic labels

Use the root vocabulary explicitly:

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

## 7. Counterexample-first procedure

Before accepting a proposed universal detector limit:

1. state the resource and all constraints mathematically;
2. identify what systems/degrees of freedom are excluded;
3. try a single atom, cavity/dispersive interaction, reversible memory, metastable memory, external reservoir, active gain, and exported record as adversarial counterexamples where relevant;
4. distinguish a failure of the theorem from a missing resource coordinate;
5. preserve the failed claim and the counterexample in `CLAIM_LEDGER.md` and `RESEARCH_LOG.md`;
6. only then narrow the theorem or move to the next resource.

Do not hide a failed universal bound by silently adding assumptions after the fact.

## 8. Quantitative performance variables for the next phase

Prefer explicit constraints such as

```text
input ensemble / photon-number distribution
prior probabilities
P_false / P_miss or target P_e
observation time tau_obs
record retention time tau_rec
operating temperature T
bandwidth
allowed optical disturbance
reset requirement
cycle time
system dimension / number of controlled degrees of freedom
available reservoirs / pumps / reference fields
```

A lower bound without a complete resource ledger should be treated as provisional.

## 9. Real-detector mapping rule

Do not specialize to HgCdTe or another semiconductor too early.

Once an abstract statement survives counterexamples, test it separately against representative architectures:

```text
photoconductor
photovoltaic photodiode
APD / SPAD
photomultiplier-like gain chain
bolometer / calorimetric detector
superconducting single-photon detector
nonabsorptive / dispersive photon-number measurement.
```

The purpose is to find the true scope of the statement, not to force all architectures into semiconductor carrier language.

## 10. Prior-art rule

Before novelty language, audit at minimum:

```text
quantum photodetection theory
binary quantum-state discrimination
POVM / measurement-channel formulations
quantum nondemolition photon measurement
data-processing / trace-distance contractivity
decoherence and pointer-state formation
metastable detector models
measurement thermodynamics and Landauer reset
finite-system atomic-to-band crossover
semiconductor exciton/free-carrier physics.
```

Established mathematical or conceptual results must be attributed. Candidate novelty, if any, will likely lie in a narrowly constrained detector-specific synthesis or bound, not in trace distance, Helstrom discrimination, QND measurement, decoherence, or semiconductor band formation themselves.

## 11. Documentation rule

After every substantive step:

- update `CURRENT_STATE_LIVE.md` if the frontier changed;
- update `CLAIM_LEDGER.md` for new/invalidated/superseded claims;
- append `RESEARCH_LOG.md` with the reasoning path and why direction changed;
- add a dedicated result file when algebra, numerics, or literature detail becomes too large for the live-state file.

Never delete a failed branch merely because a better formulation exists.

## 12. Current next attack

Formalize a constrained record-formation problem:

```text
Given target discrimination performance epsilon
and retention interval tau_rec
at temperature T,
with specified allowed optical disturbance and reset requirements,
what resources are unavoidable?
```

Start with the weakest possible assumptions. Try to kill proposed bounds before strengthening them.
