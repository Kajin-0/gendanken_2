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
5. `INTERACTION_ACTION_LOWER_BOUND.md`
6. `N_DIPOLE_SINGLE_MODE_MODEL.md`
7. `COHERENT_CAPTURE_TO_RECORD.md`
8. `TRAVELING_WAVE_CAPTURE.md`
9. `MODE_WEIGHTED_OPTICAL_DEPTH.md`
10. `SEMICONDUCTOR_DECISION_BRIDGE.md`

Do not reconstruct the current frontier from chat summaries when repository files are available.

## 2. Research objective

Follow the strongest surviving consequence of:

> At what point does a collection of atoms become a photodetector?

Do not force the project toward a predetermined semiconductor answer, theorem, or paper.

The current route is

```text
optical hypothesis
-> optical access / mode overlap
-> photon-matter coupling
-> accessible material-state distinguishability
-> competition with optical / matter loss
-> persistent record formation
-> readout under dark/noisy conditions
-> reset / reuse.
```

The strongest current conclusion is that the detector boundary is a **multi-resource dynamical performance surface**, not a universal atom-count transition.

## 3. Semantic locks — do not regress

### Absorption is not the definition

Do not equate photon absorption with photodetection. Absorption is neither sufficient nor universally necessary under the operational definition.

### Re-emission versus carrier generation

Do not describe photon re-emission and electron-hole generation as mutually exclusive alternatives. Interband absorption can create an electron-hole excitation that later recombines radiatively.

### No universal atom-count threshold

Do not claim a critical `N_c` without explicit architecture/resource constraints. Finite-size band formation is not the detector boundary.

### Total atom count is usually not even the correct constrained coordinate

For unequal microscopic couplings,

```math
G^2=\sum_j|g_j|^2.
```

Only matter coupled to the optical mode contributes. In extended absorbers, use mode-weighted oscillator strength, optical depth, or the relevant overlap integral rather than literal total atom number.

### Electron-hole generation is not the complete detection event

Carrier creation must be separated from binding/dissociation, recombination, extraction/collection, record formation, and readout.

### Gain does not create the original hypothesis information

Treat gain as stabilization/enlargement of an existing encoded distinction against later readout limitations unless an explicit additional information-bearing resource is introduced.

### Irreversibility must be qualified and rate matched

Do not invoke irreversibility as a primitive microscopic threshold. In the current coherent-capture models, making the desired trapping rate arbitrarily large can reduce detection by overdamping acquisition. State the relevant subsystem, loss channels, trapping dynamics, and reset model.

### Landauer is not a per-click axiom

Do not assert `k_B T ln 2` as the minimum acquisition energy of every detection event. Separate interaction, retention, readout, logical erasure, and reset.

### Peak monochromatic efficiency does not imply a minimum N

In the clean one-port external-capture model, any nonzero `G` can reach unit resonant narrowband conversion by critical matching,

```math
\Gamma=4G^2/\kappa.
```

Weak coupling is paid for in bandwidth/time. Any `N_min` inferred from efficiency alone must therefore be attacked with this counterexample.

## 4. Mandatory system-boundary discipline

Every information-theoretic statement must specify what is accessible.

For binary optical hypotheses,

```math
\rho_D^{(n)}
=\operatorname{Tr}_{\overline D}
\left[
U(|n\rangle\langle n|\otimes\rho_D)U^\dagger
\right].
```

Use

```math
\mathcal D_D
=\frac12\|\rho_D^{(1)}-\rho_D^{(0)}\|_1.
```

Do not say information is gone merely because it is absent from `D`; it may reside in outgoing light or the environment.

## 5. Separate the boundaries

Always distinguish at least:

```text
(1) finite atomic spectrum -> band-like spectrum
(2) optical access / mode coupling
(3) bound excitation -> mobile carriers
(4) optical interaction -> encoded material information
(5) encoded information -> persistent/metastable record
(6) record -> useful decision under dark/noisy output
(7) reset / reuse.
```

A result about one boundary must not be promoted into another without derivation.

## 6. Current active resource coordinates

Depending on architecture, useful dimensionless coordinates now include

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

and

```math
R_d\tau.
```

Do not assume one scalar metric can replace the full resource ledger.

## 7. Epistemic labels

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

## 8. Counterexample-first procedure

Before accepting a universal detector limit:

1. state the resource and all constraints mathematically;
2. identify excluded systems/degrees of freedom;
3. try single-atom, dispersive, cavity/critical-coupling, reversible-memory, metastable-memory, external-reservoir, active-gain, exported-record, and narrowband/long-time counterexamples where relevant;
4. distinguish theorem failure from a missing resource coordinate;
5. preserve the failed claim and counterexample in `CLAIM_LEDGER.md` and `RESEARCH_LOG.md`;
6. only then narrow the theorem or move to the next resource.

Do not hide a failed universal bound by silently adding assumptions afterward.

## 9. Quantitative performance variables

Prefer explicit constraints:

```text
input ensemble / photon-number distribution
prior probabilities
false-alarm / miss or target P_e
observation time tau
record retention time tau_rec
operating temperature T
incident bandwidth / temporal mode
optical port topology and mode overlap
parasitic optical loss
matter dephasing / recombination
record trapping / extraction rate
dark-event rate
reset requirement and cycle time
available reservoirs / pumps / reference fields.
```

A lower bound without a complete resource ledger is provisional.

## 10. Real-detector mapping rule

Do not specialize to HgCdTe so early that the general boundary is lost. Once an abstract statement survives counterexamples, test representative architectures separately.

For semiconductor mapping, preserve the hierarchy

```text
optical access
-> absorption / alpha L
-> electron-hole excitation
-> carrier survival and separation
-> persistent electrical record
-> discrimination against dark/noisy output.
```

Do not collapse this into `absorption = detection` or `pair generation = detection`.

## 11. Prior-art rule

Before novelty language, audit at minimum:

```text
quantum photodetection / binary state discrimination
quantum speed limits
Dicke / Tavis-Cummings collective coupling
input-output theory and critical coupling
cavity cooperativity / Purcell physics
single-photon absorption and time-reversed emission
Beer-Lambert / optical-depth limits
semiconductor absorption and carrier collection
detector thermodynamics / metastable records
noise and decision theory.
```

The ingredients are largely established. Candidate novelty, if any, is likely to lie only in a narrowly defined detector-boundary synthesis, constrained bound, or cross-architecture result.

## 12. Documentation rule

After every substantive step:

- update `CURRENT_STATE_LIVE.md` when the frontier changes;
- update `CLAIM_LEDGER.md` for new, invalidated, or superseded claims;
- append/revise `RESEARCH_LOG.md` to preserve why the direction changed;
- add a dedicated derivation file when algebra, numerics, or literature detail becomes too large for live state.

Never delete a failed branch merely because a stronger formulation exists.

## 13. Current next attack

The discrete-emitter, traveling-wave, optical-depth, and binary semiconductor-click bridges now exist.

The next strongest attack is:

```text
continuous noisy electrical output
-> likelihood-ratio / Gaussian discrimination
-> integration time and bandwidth
-> responsivity / noise PSD / NEP / D*
-> identify what conventional detector metrics preserve or hide about photon-hypothesis distinguishability.
```

Separately, perform a primary-source prior-art audit before calling any exact matching law or synthesis distinct.
