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
11. `CONTINUOUS_GAUSSIAN_DECISION.md`

Do not reconstruct the frontier from chat summaries when these files are available.

## 2. Current research objective

Follow the strongest surviving consequence of:

> At what point does a collection of atoms become a photodetector?

Do not force a predetermined semiconductor answer, theorem, or paper.

The current route is

```text
optical task
-> optical access / mode overlap
-> mode-weighted photon-matter coupling
-> microscopic transduction
-> competition with loss / recombination
-> persistent record
-> electrical signal transfer + noise statistics
-> optimum hypothesis discrimination
-> reset / reuse.
```

The strongest current conclusion is that the detector boundary is a **task-dependent multi-resource performance surface**, not a universal atom-count transition or one conventional scalar figure of merit.

## 3. Semantic locks — do not regress

### Absorption is not the definition

Absorption is neither sufficient nor universally necessary under the operational definition.

### Re-emission and electron-hole generation are not mutually exclusive branches

Interband absorption can create an electron-hole excitation that later recombines radiatively.

### No universal atom-count threshold

Do not claim a critical `N_c` without explicit architecture/resource constraints.

### Literal total N is usually not even the right constrained coordinate

For unequal microscopic couplings,

```math
G^2=\sum_j|g_j|^2.
```

Only mode-coupled matter contributes appreciably. In extended absorbers, prefer mode-weighted oscillator strength, column density, or optical depth.

### Electron-hole generation is not a complete detection event

Separate excitation generation from binding/dissociation, recombination, extraction/collection, record formation, and readout.

### Gain does not create the original hypothesis information

Treat gain as stabilization/enlargement of an existing distinction unless an explicit additional information-bearing resource enters.

### Irreversibility must be qualified and rate matched

Do not invoke irreversibility as a primitive threshold. In the current coherent models, overly strong trapping can reduce record probability by overdamping acquisition.

### Landauer is not a per-click acquisition axiom

Separate interaction, retention, readout, logical erasure, and reset.

### Peak monochromatic efficiency does not imply minimum N

In the clean one-port external-capture model,

```math
\Gamma=4G^2/\kappa
```

can give unit resonant narrowband capture for any nonzero `G`. Weak coupling is paid for in bandwidth/time.

### Same D* does not imply same event-detection performance

In the one-pole white-noise benchmark,

```math
d^2=E^2D^{*2}/(A\tau).
```

At equal area and equal low-frequency `D*`, different response times give different optimum pulse-discrimination error.

Do not treat scalar `D*` as the detector boundary.

## 4. Mandatory system-boundary discipline

For binary optical hypotheses, use an explicit accessible subsystem `D` and

```math
\mathcal D_D
=\frac12\|\rho_D^{(1)}-\rho_D^{(0)}\|_1.
```

Do not say information is gone merely because it left `D`; it may remain in outgoing radiation or environment.

At the classical electrical-output level, specify the complete output distributions and allowed observation interval.

## 5. Keep the boundaries separate

Always distinguish at least:

```text
(1) finite atomic spectrum -> band-like spectrum
(2) optical access / mode coupling
(3) bound excitation -> mobile carriers
(4) optical interaction -> encoded material information
(5) encoded information -> persistent/metastable record
(6) record -> electrical waveform
(7) waveform -> useful decision under dark/readout noise
(8) reset / reuse.
```

A result about one boundary must not be promoted into another without derivation.

## 6. Current resource coordinates

Depending on architecture, useful coordinates include

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

and for Gaussian waveform decisions

```math
\boxed{
d^2
=\int
\frac{|\tilde s(f)|^2}
{S_n^{(2)}(f)}df.
}
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
3. try single-atom, dispersive, cavity/critical-coupling, narrowband/long-time, reversible-memory, metastable-memory, external-reservoir, active-gain, exported-record, mode-overlap, and task-change counterexamples where relevant;
4. distinguish theorem failure from a missing resource coordinate;
5. preserve the failed claim and counterexample in `CLAIM_LEDGER.md` and `RESEARCH_LOG.md`;
6. only then narrow the theorem or move to the next resource.

Do not hide a failed universal bound by silently adding assumptions afterward.

## 9. Quantitative performance variables

Prefer explicit constraints:

```text
input ensemble / optical waveform
prior probabilities
false-alarm / miss or target P_e
observation time / decision deadline
record retention time
operating temperature
incident bandwidth / temporal mode
optical port topology and mode overlap
parasitic optical loss
matter dephasing / recombination
record trapping / extraction rate
dark-event rate
signal-dependent noise
timing uncertainty / jitter
reset requirement and cycle time
available reservoirs / pumps / reference fields.
```

A lower bound without a complete resource ledger is provisional.

## 10. Real-detector mapping rule

For semiconductor mapping, preserve

```text
optical access
-> absorption / alpha L
-> electron-hole excitation
-> carrier survival/separation
-> persistent electrical record
-> waveform transfer R(f)
-> noise PSD / statistics
-> decision error.
```

Do not collapse this to `absorption = detection`, `pair generation = detection`, or `D* = detector quality`.

## 11. Prior-art rule

Before novelty language, audit at minimum:

```text
quantum photodetection / binary state discrimination
quantum speed limits
Dicke / Tavis-Cummings collective coupling
input-output theory / critical coupling
cavity cooperativity / Purcell physics
single-photon absorption / time-reversed emission
Beer-Lambert / optical-depth physics
semiconductor carrier collection
Gaussian detection theory / matched filtering
NEP / D* conventions
signal-dependent detector noise
measurement thermodynamics.
```

The ingredients are largely established. Candidate novelty, if any, is likely only in a narrowly constrained synthesis, bound, or cross-architecture result.

## 12. Documentation rule

After every substantive step:

- update `CURRENT_STATE_LIVE.md` when the frontier changes;
- update `CLAIM_LEDGER.md` for new/invalidated/superseded claims;
- update `RESEARCH_LOG.md` with why the direction changed;
- add a dedicated result file when algebra/numerics/literature become too large for live state.

Never delete a failed branch merely because a stronger formulation exists.

## 13. Current next attack

The strongest next attack is

```text
signal-dependent noise
-> H0 and H1 have different covariances
-> shot / generation-recombination / avalanche-gain noise
-> optimum likelihood ratio beyond equal-covariance matched filtering.
```

Then treat unknown photon arrival time / timing jitter and ask whether a **task-specific detectivity** can be defined from optimum decision distance.

Separately, perform a focused primary-source prior-art audit before any novelty claim.
