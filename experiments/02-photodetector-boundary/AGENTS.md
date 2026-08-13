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

Do not reconstruct the frontier from chat summaries when repository files are available.

## 2. Current research objective

Follow the strongest surviving consequence of:

> At what point does a collection of atoms become a photodetector?

The current chain is

```text
optical task
-> optical access / mode overlap
-> mode-weighted interaction resource
-> microscopic transduction
-> acquisition/extraction versus loss
-> persistent record
-> complete conditional output process
-> timing / nuisance parameters
-> optimum decision
-> local reset / record export
-> optional global cycle closure.
```

The strongest current conclusion is that detection is a **task-dependent multi-resource relation**, not a universal atom-count transition or one scalar detector score.

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

### Peak monochromatic efficiency does not imply minimum N

Critical matching can give unit narrowband capture for arbitrarily weak nonzero coupling if arbitrarily long interaction time/narrow bandwidth is allowed.

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

### No universal scalar detector ranking when spectral decision kernels cross

Within the linear Gaussian waveform class, if

```math
W_A(f)-W_B(f)
```

changes sign, task waveforms can reverse the detector ranking.

### Landauer is not a per-click acquisition or local-reset axiom

A local detector can export its record. `k_B T ln2` applies only under much stronger logical-erasure conditions and for an unbiased bit. Distinguish local reset from global cycle closure.

### Barrier height is not automatically dissipated work

Activated retention/reset formulas produce conditional stability/control-range requirements, not universal heat bounds.

## 4. Mandatory system-boundary discipline

At the quantum level, specify the accessible subsystem `D` and use

```math
\mathcal D_D
=\frac12\|\rho_D^{(1)}-\rho_D^{(0)}\|_1.
```

At the classical output level, specify the complete conditional output distributions/processes and the allowed observation interval.

At the thermodynamic level, specify whether the accounting boundary includes

```text
detector memory
controller
readout register
external record store
optical/environmental degrees of freedom
work reservoirs
pumps
bath.
```

Never claim information or entropy has disappeared merely because it left one chosen subsystem.

## 5. Keep these boundaries distinct

```text
(1) finite atomic spectrum -> band-like spectrum
(2) optical access / mode coupling
(3) bound excitation -> mobile carriers
(4) optical interaction -> encoded information
(5) encoded information -> persistent record
(6) record -> electrical/output process
(7) output process -> decision under noise/timing uncertainty
(8) local reset / record export
(9) global cycle closure.
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

and for cyclic reset

```math
h(p),\quad H(M|R),\quad \tau_{\rm rec}/\tau_r,\quad p_d,\quad \epsilon_r.
```

Do not assume one scalar can replace the full resource ledger.

## 7. Counterexample-first procedure

Before accepting a universal lower bound:

1. state the resource and all constraints mathematically;
2. identify excluded degrees of freedom and reservoirs;
3. attack with single-atom, dispersive, cavity/critical-coupling, narrowband/long-time, reversible-memory, exported-record, side-information, active-pump, external-reservoir, and task-change counterexamples where relevant;
4. distinguish theorem failure from a missing resource coordinate;
5. preserve the failed claim in `CLAIM_LEDGER.md` and `RESEARCH_LOG.md`;
6. only then narrow the statement.

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
Landauer erasure with side information
measurement thermodynamics / reversible measurement.
```

Most ingredients are established. Candidate distinction, if any, is likely only in a narrowly constrained synthesis or cross-architecture statement.

## 10. Documentation rule

After every substantive step:

- update `CURRENT_STATE_LIVE.md` when the frontier changes;
- update `CLAIM_LEDGER.md` for new/invalidated/superseded claims;
- update `RESEARCH_LOG.md` with why the direction changed;
- add a dedicated derivation file when algebra/numerics/literature become too large for live state.

Never delete a failed route merely because a stronger formulation exists.

## 11. Current next attack

Attack **global cycle closure** itself.

Allow, one at a time:

```text
side information correlated with optical/environmental input;
work extraction from the detected field;
nonequilibrium reservoirs and active pumps;
continuous reversible transduction with no explicit binary memory;
external records retained indefinitely outside the accounting horizon.
```

Goal:

> identify the weakest precise assumptions under which any nontrivial architecture-independent detector-cycle thermodynamic bound survives.

Do not defend Landauer by assumption; try to break the bound first.
