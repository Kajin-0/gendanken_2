# Claim Ledger — Experiment 02

**Updated:** 2026-08-12  
**Status:** exploratory; detector-process / resource-ledger formulation active  
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

Mode-weighted coupling `G^2=sum |g_j|^2`, optical depth, and architecture-aware overlaps replace literal `N`.

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

Barrier height/modulation amplitude is a stability-control resource, not by itself irreversible work.

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

### H31 — returning an auxiliary/catalyst to the same local marginal is sufficient for strict cyclic reuse
**Status:** INVALIDATED

The auxiliary can have the same marginal while becoming correlated with source/detector/output history. Strict reusable return requires decoupling or an explicit correlation budget.

### H32 — average entropy/free energy/work determines guaranteed one-event resource cost
**Status:** INVALIDATED IN GENERAL

Rare branches can leave the mean small while dominating a resource quantile or worst-case requirement. Finite-cycle guarantees require one-shot/tail-sensitive accounting.

### H33 — maximum external power alone gives a universal detector speed limit
**Status:** INVALIDATED

Fast distinguishability generation can arise from a strong conditional Hamiltonian with little net detector-energy deposition. Power, interaction strength, stored free energy, and causal propagation are separate resources.

### H34 — detector size alone gives a universal `L/c` response-time lower bound
**Status:** INVALIDATED AS STATED

Latency depends on event locations, required output location(s), local-decision allowance, output-port count, and communication geometry.

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

A phase/time reference can restore otherwise symmetry-hidden information.

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

### B5 — bounded interaction-generator strength gives a conditional latency bound
**Status:** DERIVED / CONDITIONAL

If `Delta V_I(t)<=V_max`,

```math
\tau
\ge
\hbar\arcsin(1-2\epsilon)/V_{\max}.
```

This is an interaction-strength bound, not a power bound.

---

# 4. External capture / optical / control resources

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

```math
\eta_R=\frac{4x}{(1+x)^2},
\qquad
1-\eta_R=\left(\frac{x-1}{x+1}\right)^2,
```

with `x=Gamma/Gamma_match`.

### X7 — nonzero rate floor restores constrained coupling threshold
**Status:** DERIVED / CONDITIONAL

```math
G^2
\ge
\frac{\kappa\Gamma_{\rm floor}}{4}
\frac{1-\sqrt\epsilon}{1+\sqrt\epsilon}.
```

Control range/precision is an independent detector resource.

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

### A3 — clock quality is the timing analogue of optical phase-reference quality
**Status:** DERIVED ORGANIZING STATEMENT

---

# 9. Detector-channel / process ordering

### C1 — classical detector channel
**Status:** DERIVED ORGANIZING DEFINITION

```math
K_D(y|x)=P_D(Y=y|X=x).
```

### C2 — post-processing dominance
**Status:** KNOWN BLACKWELL / GARBLING STRUCTURE APPLIED TO DETECTORS

If

```math
K_B=T\circ K_A,
```

A can simulate every decision strategy available to B.

### C3 — detector comparison is generally a partial order
**Status:** DERIVED / KNOWN CONSEQUENCE

If neither channel is a post-processing of the other, different tasks can legitimately prefer different detectors.

### C4 — quantum detector comparison uses channel post-processing under proper quantum conditions
**Status:** KNOWN / REQUIRES QUANTUM PRIOR-ART AUDIT

```math
\Phi_D:\rho_{\rm opt}\mapsto\rho_{\rm out}.
```

### C5 — current performance hierarchy
**Status:** DERIVED ORGANIZING STATEMENT

```text
scalar metric
-> task-specific decision metric
-> detector-channel partial order
-> resource-constrained achievable-channel set.
```

### C6 — repeated use with hidden correlations is generally a detector process/channel with memory
**Status:** DERIVED ORGANIZING STATEMENT

Use

```math
P(y_1,\ldots,y_n|x_1,\ldots,x_n)
```

when cycle independence cannot be assumed.

---

# 10. Correlating catalysts / repeated-use closure

### K1 — same catalyst marginal does not imply strict return
**Status:** DERIVED / KNOWN CORRELATED-CATALYSIS STRUCTURE

```math
\rho'_C=\tau_C
```

can coexist with

```math
I(C:R)>0.
```

### K2 — strict uncorrelated reuse requires decoupling or explicit correlation accounting
**Status:** DERIVED ORGANIZING STATEMENT

A strict condition is

```math
\rho'_{CR}=\tau_C\otimes\rho'_R.
```

### K3 — finite catalyst has bounded instantaneous correlation capacity
**Status:** KNOWN INFORMATION-THEORETIC BOUND

For finite `d_C`,

```math
I(C:R)\le2\ln d_C.
```

This does not eliminate correlated-catalysis loopholes; dimension/tolerance/scaling still matter.

### K4 — residual correlation tolerance is a detector resource parameter
**Status:** DERIVED ORGANIZING STATEMENT

A resource theorem must state whether correlated catalyst return is forbidden, bounded, or freely allowed.

---

# 11. One-shot / finite-size resource accounting

### F1 — mean resource cost does not determine an `epsilon`-guaranteed cost
**Status:** DERIVED

Define

```math
W_\epsilon
=\inf\{w:\Pr(W>w)\le\epsilon\}.
```

In general `E[W]` does not determine `W_epsilon`.

### F2 — rare branches can dominate guaranteed single-cycle resources while barely affecting averages
**Status:** DERIVED

### F3 — finite-process information thermodynamics uses one-shot/smooth quantities rather than ordinary entropy alone
**Status:** KNOWN / APPLIED AS RESOURCE WARNING

Faist et al. give a microscopic process work-cost framework in terms of smooth conditional max-entropy under their assumptions; ordinary entropy rates emerge in appropriate many-copy limits.

### F4 — error/overrun tolerance is an independent resource specification
**Status:** DERIVED ORGANIZING STATEMENT

State average versus worst-case input, decision error, reset failure, latency tail, and resource-overrun probability explicitly.

### F5 — asymptotic simplification requires cycle-independence/mixing assumptions
**Status:** DERIVED ORGANIZING STATEMENT

Correlated catalysts / detector memory can invalidate naive i.i.d. concentration.

---

# 12. Causal latency / control-strength / power claims

### L1 — bounded interaction strength gives a state-separation latency
**Status:** DERIVED / CONDITIONAL

```math
\tau
\ge
\hbar\arcsin(1-2\epsilon)/V_{\max}.
```

### L2 — power-latency bound requires a positive one-shot work requirement in the same resource channel
**Status:** DERIVED / CONDITIONAL

If `W_epsilon>0` and `P(t)<=P_max`,

```math
\tau\ge W_\epsilon/P_{\max}.
```

This cannot become universal because `W_epsilon` itself is resource/architecture dependent.

### L3 — precharged stored free energy can decouple event latency from event-window external power
**Status:** DERIVED ORGANIZING STATEMENT

### L4 — steady event rate and storage imply a conditional average recharge requirement
**Status:** DERIVED / CONDITIONAL

If each event consumes stored energy `E_s` at rate `R`, ideal average recharge obeys

```math
P_{\rm avg}\ge R E_s.
```

### L5 — causal output geometry bounds propagation latency
**Status:** DERIVED / CONDITIONAL

For event location `r`, required output `r_o`, and causal propagation speed `v_c`,

```math
\tau_{\rm causal}(r)\ge|r-r_o|/v_c.
```

### L6 — output-port parallelism can trade hardware/channel count against causal latency
**Status:** DERIVED ORGANIZING STATEMENT

### L7 — sequential adaptive rounds incur communication/control latency
**Status:** DERIVED ORGANIZING STATEMENT

---

# 13. Reset / source closure / thermodynamics

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

### R5 — erasure cost depends on discarded information conditional on retained side information
**Status:** KNOWN INFORMATION-THERMODYNAMIC PRINCIPLE / CONDITIONAL

### R6 — optical/pump free energy can subsidize cycle closure
**Status:** DERIVED ORGANIZING RESOURCE BALANCE / CONDITIONAL

No positive externally supplied detector work is universal when other nonequilibrium resources may be consumed.

### R7 — raw `h nu` is not automatically usable reset work
**Status:** DERIVED ORGANIZING STATEMENT

### R8 — continuous reversible transduction need not contain a binary erasure stage
**Status:** DERIVED COUNTEREXAMPLE

### R9 — activated retention/reset relation is a control-range bound, not a universal heat bound
**Status:** DERIVED / CONDITIONAL

---

# 14. Current organizing statement

### O1 — detector boundary is a resource-dependent detector-process performance surface
**Status:** DERIVED ORGANIZING STATEMENT / PRIORITY UNASSESSED

```text
optical input family / task
-> allowed operations + phase/time references
-> optical access / mode overlap
-> microscopic coupling / interaction action
-> maximum interaction strength
-> time / bandwidth
-> loss / trapping / retention
-> control range / precision
-> parallel channel capacity
-> complete output statistics
-> timing / nuisance structure
-> optimum decision
-> detector-channel/process ordering
-> catalyst correlation / cycle memory
-> side information / record export
-> one-shot reliability specification
-> stored energy / power / causal geometry
-> source-inclusive free-energy accounting if cyclic thermodynamics is imposed.
```

No architecture-independent scalar detector boundary or fixed thermodynamic cost per event has survived.

---

# 15. Open fronts

### O2 — adaptive distributed measurement
**Status:** OPEN / CURRENT FRONTIER

Determine whether adaptivity is a genuinely new resource coordinate or can be absorbed into the detector-process formalism once controller memory, communication latency, references, pre-shared correlations, and feedback operations are charged.

### O3 — resource-constrained detector-process theorem
**Status:** OPEN

Only after the adaptive attack should an achievable-process/resource-conversion theorem be attempted.

### O4 — prior-art audit
**Status:** OPEN AND REQUIRED BEFORE NOVELTY LANGUAGE

Audit photodetection theory, statistical/quantum channel comparison, quantum combs/process tensors, reference-frame theory, correlated catalysis, one-shot thermodynamics, detection theory, and critical-coupling/control literature.

---

# 16. Explicit non-claims

- **NON-CLAIM:** there is a universal atom count at which a detector appears.
- **NON-CLAIM:** total physical atom count is the correct resource in extended matter.
- **NON-CLAIM:** absorption is required for all photodetection.
- **NON-CLAIM:** electron-hole generation alone is a complete detection event.
- **NON-CLAIM:** unrestricted trace distance is always operationally attainable without reference resources.
- **NON-CLAIM:** arbitrary weak coupling can attain perfect efficiency under finite control constraints.
- **NON-CLAIM:** per-channel bounds automatically extend to systems with unbounded parallelism.
- **NON-CLAIM:** same local catalyst state means the global resource is restored.
- **NON-CLAIM:** average work/free energy determines single-event guaranteed cost.
- **NON-CLAIM:** finite external watts alone impose a universal detector response-time limit.
- **NON-CLAIM:** every click dissipates `k_B T ln2`.
- **NON-CLAIM:** detector/controller/memory closure alone forces `k_B T h(p)` if source side information remains.
- **NON-CLAIM:** source-inclusive erasure requires positive external work when optical/pump free energy may be consumed.
- **NON-CLAIM:** scalar `D*` is useless; it remains useful for its conventional task/normalization but is incomplete generally.
- **NON-CLAIM:** Blackwell ordering, correlated catalysis, one-shot thermodynamics, or quantum channel comparison is novel.
- **NON-CLAIM:** the current experiment has established a publishable new theorem.
