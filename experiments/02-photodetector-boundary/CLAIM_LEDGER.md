# Claim Ledger — Experiment 02

**Updated:** 2026-08-12  
**Status:** exploratory; detector-channel / resource-ledger formulation active  
**Priority:** unassessed; no novelty claim

This is the epistemic boundary. `CURRENT_STATE_LIVE.md` is the operational front door; `RESEARCH_LOG.md` preserves chronology; dedicated result files preserve detailed derivations.

## Status vocabulary

- **KNOWN** — established result used as input.
- **DERIVED** — consequence of stated assumptions.
- **CHECKED** — independently/numerically verified.
- **CONDITIONAL** — valid only in the stated model/resource envelope.
- **CANDIDATE DISTINCT — PRIORITY UNPROVEN** — potentially unusual synthesis; literature boundary incomplete.
- **INVALIDATED** — counterexample/correction kills the statement as posed.
- **SUPERSEDED** — replaced by a stronger/corrected statement.
- **OPEN** — unresolved.
- **NON-CLAIM** — explicitly not asserted.

---

# 1. Permanent invalidations / corrections

### H1 — re-emission is the alternative to electron-hole generation
**Status:** INVALIDATED

Interband excitation can later recombine radiatively; these can be stages of one event.

### H2 — a universal critical atom count defines photodetection
**Status:** INVALIDATED

Microscopic systems can encode photon arrival; macroscopic absorbers can fail to retain an accessible record.

### H3 — absorption is sufficient for detection
**Status:** INVALIDATED

Unity absorption can coexist with no accessible photon/no-photon distinction.

### H4 — absorption is universally necessary for detection
**Status:** INVALIDATED

Dispersive/nondestructive interactions provide counterexamples.

### H5 — electron-hole generation is the complete electrical detection event
**Status:** INVALIDATED GENERALIZATION

Generation must be separated from dissociation, recombination, extraction, persistent record, and readout.

### H6 — gain creates the original photon-arrival information
**Status:** INVALIDATED AS STATED

Gain can improve robustness but cannot manufacture missing upstream information under hypothesis-independent downstream processing.

### H7 — microscopic irreversibility occurs at one definite atom count
**Status:** INVALIDATED / REFRAMED

Operational irreversibility depends on subsystem choice, information dispersal, trapping/metastability, and accessibility.

### H8 — every detected photon dissipates `k_B T ln 2` at acquisition
**Status:** INVALIDATED AS A UNIVERSAL ACQUISITION BOUND

Detection and logical erasure are distinct operations.

### H9 — nonzero final detector-energy change is necessary for distinguishability
**Status:** INVALIDATED

A degenerate pointer can become orthogonal with zero final bare-energy difference.

### H10 — target discrimination implies a universal positive deposited-energy cost
**Status:** INVALIDATED IN GENERAL

Interaction action survives conditionally; final deposited energy does not.

### H11 — atom count itself is the fundamental microscopic resource
**Status:** INVALIDATED / SUPERSEDED

Mode-weighted coupling `G^2=sum |g_j|^2`, optical depth, and other architecture-aware quantities replace literal `N`.

### H12 — coherent photon-to-matter transfer is already a persistent record
**Status:** INVALIDATED

The excitation can coherently return to the optical mode.

### H13 — arbitrarily strong desired trapping always improves detection
**Status:** INVALIDATED IN CURRENT LOSSY MODELS

Excessive trapping can overdamp acquisition.

### H14 — high monochromatic efficiency implies a positive minimum atom count
**Status:** INVALIDATED IN CLEAN ONE-PORT MODEL

Any nonzero coupling can reach unit resonant narrowband conversion under ideal matching if arbitrarily slow/narrowband operation is allowed.

### H15 — arbitrarily many atoms always overcome parasitic optical loss
**Status:** INVALIDATED IN CURRENT ONE-PORT MODEL

Optical escape creates an independent ceiling.

### H16 — literal total atom count is the relevant `N` in extended matter
**Status:** INVALIDATED

Only optically participating matter contributes significantly.

### H17 — arbitrarily large optical thickness always repairs detector performance
**Status:** INVALIDATED IN MINIMAL SEMICONDUCTOR DECISION MODEL

Collection/readout ceilings and dark events can make the target impossible even as `alpha L -> infinity`.

### H18 — same scalar `D*` implies same event-detection performance
**Status:** INVALIDATED IN ONE-POLE WHITE-NOISE BENCHMARK

`d^2=E^2D*^2/(A tau)` for a short event, so response time matters.

### H19 — no mean signal means no detector information
**Status:** INVALIDATED

Hypothesis-dependent covariance can carry information even when means coincide.

### H20 — one fixed-noise SNR law spans zero-background and background-dominated counting
**Status:** INVALIDATED

Poisson decision geometry changes qualitatively between those limits.

### H21 — known-time matched-filter performance transfers unchanged to unknown arrival time
**Status:** INVALIDATED

Unknown timing creates a nuisance-parameter search/trials penalty.

### H22 — one scalar detector ranking can represent every waveform task
**Status:** INVALIDATED

Crossing decision kernels produce task-dependent ranking reversal.

### H23 — a reusable local detector necessarily dissipates `k_B T ln 2` locally per click
**Status:** INVALIDATED

Record export and conditional reset provide a counterexample.

### H24 — record barrier height is automatically dissipated each reset
**Status:** INVALIDATED GENERALIZATION

Barrier height / modulation amplitude is a stability-control resource, not by itself irreversible work.

### H25 — resetting detector + controller + record memories and leaving no detector-side record necessarily forces `k_B T h(p)` erasure
**Status:** INVALIDATED / SUPERSEDED

A surviving source/reference variable can enable reversible uncomputation.

### H26 — source-inclusive logical erasure implies positive externally supplied work per event
**Status:** INVALIDATED AS A UNIVERSAL STATEMENT

Optical or pump nonequilibrium free energy can subsidize the information-processing work.

### H27 — a latched binary memory is a necessary thermodynamic stage of detection
**Status:** INVALIDATED

Continuous reversible transduction can carry the record without a binary latch.

### H28 — unrestricted trace distance always equals achievable detector distinguishability
**Status:** INVALIDATED UNDER OPERATION / SYMMETRY RESTRICTIONS

Without the needed reference frame, globally distinct states can become operationally indistinguishable.

### H29 — the `G -> 0` critical-coupling counterexample remains achievable under arbitrary physical control constraints
**Status:** INVALIDATED

A nonzero minimum trapping rate or finite control resolution restores a positive constrained coupling / `N` threshold.

### H30 — a per-channel lower bound automatically gives a system-level detector bound
**Status:** INVALIDATED

Independent evidence can accumulate across arbitrarily many parallel channels unless total channel capacity is bounded.

---

# 2. Core detector statements

### I1 — unrestricted microscopic binary distinguishability
**Status:** DERIVED FROM CHOSEN OPERATIONAL DEFINITION

```math
\mathcal D_D=\frac12\|\rho_D^{(1)}-\rho_D^{(0)}\|_1,
\qquad
P_{e,\min}=\frac12(1-\mathcal D_D)
```

when all POVMs are allowed.

### I2 — allowed operations / reference resources modify operational distinguishability
**Status:** DERIVED / KNOWN SYMMETRY-RESOURCE STRUCTURE

For a symmetry-twirling map `G`, symmetry-invariant measurement access is represented by the corresponding restricted states/measurement class. A phase/time reference can restore otherwise hidden information.

### I3 — persistence is distinct from momentary encoding
**Status:** DERIVED ORGANIZING STATEMENT

### I4 — the general classical detector object is the complete conditional output process
**Status:** DERIVED ORGANIZING STATEMENT

Mean response plus one noise PSD is a special case.

### I5 — detector is a functional relation, not a phase-of-matter label
**Status:** DERIVED ORGANIZING STATEMENT / PRIORITY UNASSESSED

---

# 3. Microscopic coupling / record formation

### B1 — finite-time pure-state separation requires conditional interaction action
**Status:** DERIVED FROM ESTABLISHED QUANTUM-SPEED-LIMIT GEOMETRY / CONDITIONAL

```math
\mathcal A_\Delta\ge\hbar\arcsin(1-2\epsilon).
```

### B2 — per-constituent action cap gives conditional `N_min`
**Status:** DERIVED / CONDITIONAL

```math
N\ge\left\lceil\hbar\arcsin(1-2\epsilon)/a_{\max}\right\rceil.
```

### B3 — identical resonant dipoles have `G=g sqrt(N)`
**Status:** KNOWN / DERIVED IN STATED TAVIS--CUMMINGS SECTOR

### B4 — record trapping has a finite matching optimum
**Status:** DERIVED / CHECKED

Clean initial-in-mode limit: `Gamma_opt=2G`.

---

# 4. External capture / optical resources

### X1 — clean one-port critical matching can give unit narrowband capture for any nonzero `G`
**Status:** DERIVED / CONDITIONAL

```math
\Gamma_{\rm match}=4G^2/\kappa.
```

### X2 — optimized external efficiency separates optical escape and cooperativity
**Status:** DERIVED

```math
\eta_{R,\max}=\eta_{\rm esc}C_N/(1+C_N).
```

### X3 — finite photon bandwidth restores a constrained matter threshold
**Status:** DERIVED / CONDITIONAL

### X4 — unequal microscopic coupling reduces to `G^2=sum_j |g_j|^2`
**Status:** DERIVED / KNOWN STRUCTURE

### X5 — dilute single-pass extended matter is naturally controlled by optical depth
**Status:** KNOWN / CONDITIONAL

```math
\mathrm{OD}=n\sigma L,
\qquad
P_{\rm abs}=1-e^{-\mathrm{OD}}.
```

### X6 — exact clean critical-matching mismatch law
**Status:** DERIVED

With `x=Gamma/Gamma_match`,

```math
\eta_R=\frac{4x}{(1+x)^2},
\qquad
1-\eta_R=\left(\frac{x-1}{x+1}\right)^2.
```

### X7 — nonzero rate floor restores constrained coupling threshold
**Status:** DERIVED / CONDITIONAL

For target `eta_R>=1-epsilon`,

```math
G^2
\ge
\frac{\kappa\Gamma_{\rm floor}}{4}
\frac{1-\sqrt\epsilon}{1+\sqrt\epsilon}.
```

Thus control range/precision is an independent detector resource.

---

# 5. Semiconductor / electrical decision bridge

### S1 — minimal signal-record factorization
**Status:** CONDITIONAL

```math
\eta_s=\eta_{\rm mode}(1-e^{-\alpha L})\eta_{eh}P_{\rm col}P_{\rm read}.
```

### S2 — extraction/recombination race
**Status:** CONDITIONAL

```math
P_{\rm col}=\Gamma_{\rm ext}/(\Gamma_{\rm ext}+\Gamma_{\rm rec}).
```

### S3 — electron-hole generation is a microscopic transduction stage, not the complete detector boundary
**Status:** DERIVED ORGANIZING STATEMENT

### S4 — dark-event ceiling
**Status:** DERIVED / CONDITIONAL

```math
\mathcal D_{\rm click}=\eta_s e^{-R_d\tau},
\qquad
R_d\tau\le-\ln(1-2\epsilon).
```

---

# 6. Output-distribution geometry

### G1 — equal-covariance Gaussian decision distance
**Status:** KNOWN / APPLIED HERE

```math
d^2
=\int |\tilde s(f)|^2/S_n^{(2)}(f)\,df
=\int |\tilde p(f)|^2/\mathrm{NEP}_2^2(f)\,df.
```

### G2 — equal-prior Gaussian error
**Status:** KNOWN / CONDITIONAL

```math
P_e=Q(d/2).
```

### G3 — one-pole white-noise short-pulse benchmark
**Status:** DERIVED / CONDITIONAL

```math
d^2=E^2D^{*2}/(A\tau).
```

### G4 — unequal-covariance Gaussian optimum statistic is quadratic
**Status:** KNOWN / APPLIED HERE

### G5 — covariance change alone can carry detection information
**Status:** DERIVED

### G6 — Poisson square-root separation
**Status:** KNOWN / DERIVED

```math
BC=\exp[-(\sqrt{\mu_1}-\sqrt{\mu_0})^2/2].
```

### G7 — zero-background count error
**Status:** DERIVED / CONDITIONAL

```math
P_e=(1/2)e^{-\lambda_sT}.
```

---

# 7. Timing / parallelism / task dependence

### T1 — unknown arrival time is a mixture over shifted templates
**Status:** DERIVED / KNOWN NUISANCE-PARAMETER STRUCTURE

### T2 — independent-bin benchmark
**Status:** DERIVED / CONDITIONAL

```math
\Lambda=(1/M)\sum_m e^{dz_m-d^2/2}.
```

### T3 — temporal-search threshold scales approximately as `sqrt(2 ln M)`
**Status:** DERIVED ASYMPTOTIC / CONDITIONAL

### T4 — task-specific Gaussian sensitivity functional
**Status:** DERIVED

```math
\mathcal K_D[q]=\int |\tilde q(f)|^2/\mathrm{NEP}_{2,D}^2(f)\,df.
```

### T5 — known-time minimum event energy
**Status:** DERIVED / CONDITIONAL

```math
E_{\min}=2Q^{-1}(\epsilon)/\sqrt{\mathcal K_D[q]}.
```

### T6 — independent Gaussian evidence adds across channels
**Status:** DERIVED / KNOWN

```math
d_{\rm tot}^2=\sum_jd_j^2.
```

### T7 — independent Poisson separation exponents add across channels
**Status:** DERIVED / KNOWN

The total Bhattacharyya exponent is the sum of channel square-root-count separations.

### T8 — unknown active channel creates a spatial trials penalty
**Status:** DERIVED ORGANIZING STATEMENT

### T9 — parallel channel count is an independent resource
**Status:** DERIVED ORGANIZING STATEMENT

---

# 8. Reference-frame / allowed-operation claims

### A1 — globally orthogonal optical states can be reference-free indistinguishable
**Status:** DERIVED / KNOWN SYMMETRY STRUCTURE

For

```math
|\psi_\pm\rangle=(|0\rangle\pm|1\rangle)/\sqrt2,
```

`U(1)` twirling without a phase reference gives identical mixed states.

### A2 — reference-frame quality is not reducible to mean energy alone
**Status:** KNOWN RESOURCE-THEORY PRINCIPLE / ORGANIZING STATEMENT

Coherence/asymmetry relative to the constrained symmetry is an independent operational resource.

### A3 — clock quality is the timing analogue of optical phase-reference quality
**Status:** DERIVED ORGANIZING STATEMENT

---

# 9. Detector-channel ordering

### C1 — classical detector channel
**Status:** DERIVED ORGANIZING DEFINITION

```math
K_D(y|x)=P_D(Y=y|X=x).
```

### C2 — post-processing dominance
**Status:** KNOWN BLACKWELL / GARBLING STRUCTURE APPLIED TO DETECTORS

If

```math
K_B=T\circ K_A
```

with hypothesis-independent `T`, every decision rule achievable with B can be simulated from A.

### C3 — detector comparison is generally a partial order
**Status:** DERIVED / KNOWN CONSEQUENCE

If neither channel is a post-processing of the other, different tasks can legitimately prefer different detectors.

### C4 — one binary error probability or one scalar metric does not determine channel equivalence
**Status:** DERIVED ORGANIZING STATEMENT

### C5 — quantum detector comparison uses channel post-processing under proper quantum conditions
**Status:** KNOWN / REQUIRES DEDICATED QUANTUM PRIOR-ART AUDIT

```math
\Phi_D:\rho_{\rm opt}\mapsto\rho_{\rm out}.
```

If `Phi_B=Lambda o Phi_A`, A can simulate B's downstream measurements.

### C6 — current performance hierarchy
**Status:** DERIVED ORGANIZING STATEMENT

```text
scalar metric
-> task-specific decision metric
-> detector-channel partial order
-> resource-constrained achievable-channel set.
```

---

# 10. Reset / source closure / thermodynamics

### R1 — binary record entropy depends on prior
**Status:** KNOWN

```math
h(p)=-p\ln p-(1-p)\ln(1-p).
```

### R2 — ideal degenerate-memory erasure with no side information has scale `k_B T h(p)`
**Status:** KNOWN / CONDITIONAL

### R3 — exported side information can remove universal local reset cost
**Status:** KNOWN / DERIVED COUNTEREXAMPLE

### R4 — detector-memory closure is not source-inclusive informational closure
**Status:** DERIVED COUNTEREXAMPLE

```math
|x\rangle_S|0\rangle_M
\to|x\rangle_S|x\rangle_M
\to|x\rangle_S|0\rangle_M.
```

### R5 — erasure cost depends on discarded information conditional on retained side information
**Status:** KNOWN INFORMATION-THERMODYNAMIC PRINCIPLE / CONDITIONAL

Quantum conditional entropy can be negative; correlation restoration closes the cycle.

### R6 — optical/pump free energy can subsidize cycle closure
**Status:** DERIVED ORGANIZING RESOURCE BALANCE / CONDITIONAL

No positive externally supplied detector work is universal when other nonequilibrium resources may be consumed.

### R7 — raw `h nu` is not automatically usable reset work
**Status:** DERIVED ORGANIZING STATEMENT

Available nonequilibrium free-energy decrease is the disciplined resource.

### R8 — continuous reversible transduction need not contain a binary erasure stage
**Status:** DERIVED COUNTEREXAMPLE

### R9 — activated retention/reset relation is a control-range bound, not a universal heat bound
**Status:** DERIVED / CONDITIONAL

---

# 11. Current organizing statement

### O1 — detector boundary is a resource-dependent channel-performance surface
**Status:** DERIVED ORGANIZING STATEMENT / PRIORITY UNASSESSED

```text
optical input family / task
-> allowed operations + phase/time references
-> optical access / mode overlap
-> microscopic coupling / interaction action
-> time / bandwidth
-> loss / trapping / retention
-> control range / precision
-> parallel channel capacity
-> complete output statistics
-> timing / nuisance structure
-> optimum decision
-> detector-channel ordering
-> side information / record export
-> source-inclusive free-energy accounting if cyclic thermodynamics is imposed.
```

No architecture-independent scalar detector boundary or fixed thermodynamic cost per event has survived.

---

# 12. Open fronts

### F1 — correlating catalysts
**Status:** OPEN / CURRENT FRONTIER

Test resources that return with the same local marginal but accumulate correlations with detector/source degrees of freedom.

### F2 — finite-size / single-shot thermodynamics
**Status:** OPEN

Average Shannon/von-Neumann entropy need not characterize worst-case or finite-copy work fluctuations.

### F3 — causal latency / maximum power
**Status:** OPEN

Test whether finite power/control-speed limits restore stronger detector resource bounds than integrated action/free energy alone.

### F4 — adaptive distributed measurements
**Status:** OPEN

Test whether spatially distributed feedforward/adaptive control defeats channel/resource bounds that assume fixed parallel processing.

### F5 — resource-constrained detector-channel theorem
**Status:** OPEN

Only after F1-F4 should an achievable-channel/resource-conversion theorem be attempted.

### F6 — prior-art audit
**Status:** OPEN AND REQUIRED BEFORE NOVELTY LANGUAGE

Audit photodetection theory, quantum/statistical channel comparison, reference-frame resource theory, critical coupling/control sensitivity, detection theory, and information thermodynamics.

---

# 13. Explicit non-claims

- **NON-CLAIM:** there is a universal atom count at which a detector appears.
- **NON-CLAIM:** total physical atom count is the correct resource in extended matter.
- **NON-CLAIM:** absorption is required for all photodetection.
- **NON-CLAIM:** electron-hole generation alone is a complete detection event.
- **NON-CLAIM:** unrestricted trace distance is always operationally attainable without reference resources.
- **NON-CLAIM:** arbitrary weak coupling can attain perfect efficiency under finite control constraints.
- **NON-CLAIM:** per-channel bounds automatically extend to systems with unbounded parallelism.
- **NON-CLAIM:** every click dissipates `k_B T ln2`.
- **NON-CLAIM:** detector/controller/memory closure alone forces `k_B T h(p)` if source side information remains.
- **NON-CLAIM:** source-inclusive erasure requires positive external work when optical/pump free energy may be consumed.
- **NON-CLAIM:** scalar `D*` is useless; it remains useful for its stated conventional task/normalization but is incomplete generally.
- **NON-CLAIM:** Blackwell ordering or quantum channel comparison is novel.
- **NON-CLAIM:** the current experiment has established a publishable new theorem.
