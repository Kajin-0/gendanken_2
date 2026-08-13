# Claim Ledger — Experiment 02

**Updated:** 2026-08-12  
**Status:** exploratory; optical-to-decision-to-reset detector-boundary chain active  
**Priority:** unassessed; no novelty claim

This is the epistemic boundary. `CURRENT_STATE_LIVE.md` is the operational front door; `RESEARCH_LOG.md` preserves chronology. Dedicated result files preserve detailed derivations.

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

Gain can improve practical robustness but cannot manufacture missing upstream information under hypothesis-independent downstream processing.

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

Interaction action survives in the stated pure/unitary finite-time model; final deposited energy does not.

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

Any nonzero coupling can reach unit resonant narrowband conversion under critical matching if arbitrarily slow/narrowband operation is allowed.

### H15 — arbitrarily many atoms always overcome parasitic optical loss
**Status:** INVALIDATED IN CURRENT ONE-PORT MODEL

The optical escape factor `eta_esc` creates an independent ceiling.

### H16 — literal total atom count is the relevant `N` in extended matter
**Status:** INVALIDATED

Only optically participating matter contributes significantly.

### H17 — arbitrarily large optical thickness always repairs detector performance
**Status:** INVALIDATED IN MINIMAL SEMICONDUCTOR DECISION MODEL

Collection/readout ceilings and dark events can make the target impossible even as `alpha L -> infinity`.

### H18 — same scalar `D*` implies same event-detection performance
**Status:** INVALIDATED IN ONE-POLE WHITE-NOISE BENCHMARK

`d^2=E^2D*^2/(A tau)` for a short event, so response time matters at fixed area and low-frequency `D*`.

### H19 — no mean signal means no detector information
**Status:** INVALIDATED

Hypothesis-dependent covariance can carry information even when means coincide.

### H20 — one fixed-noise SNR law spans zero-background and background-dominated counting
**Status:** INVALIDATED

Poisson decision geometry changes qualitatively between those limits.

### H21 — known-time matched-filter performance transfers unchanged to unknown arrival time
**Status:** INVALIDATED

Unknown timing creates a nuisance-parameter search / trials penalty.

### H22 — one scalar detector ranking can represent every waveform task
**Status:** INVALIDATED WHEN GAUSSIAN SPECTRAL DECISION KERNELS CROSS

Crossing kernels imply task-dependent ranking reversal.

### H23 — a reusable local detector necessarily dissipates `k_B T ln 2` locally per click
**Status:** INVALIDATED

A detector can export its record to an external register and use that side information for local reset. The information is moved, not erased.

### H24 — record barrier height is automatically dissipated each reset
**Status:** INVALIDATED GENERALIZATION

Barrier height / modulation amplitude is a stability-control resource, not by itself a lower bound on irreversible work.

---

# 2. Core operational statements

### I1 — accessible quantum-state distinguishability is the minimal current microscopic criterion
**Status:** DERIVED FROM CHOSEN OPERATIONAL DEFINITION

```math
\mathcal D_D=\frac12\|\rho_D^{(1)}-\rho_D^{(0)}\|_1.
```

For equal priors, `P_e,min=(1-D_D)/2`.

### I2 — detector boundary depends on the accessible subsystem
**Status:** DERIVED

Information absent from the chosen detector subsystem may remain in outgoing light or environment.

### I3 — persistence is distinct from momentary encoding
**Status:** DERIVED ORGANIZING STATEMENT

### I4 — the general classical decision object is the complete conditional output distribution/process
**Status:** DERIVED ORGANIZING STATEMENT

Mean response divided by one fixed noise PSD is a special case.

### I5 — detector is a functional relation, not a phase-of-matter label
**Status:** DERIVED ORGANIZING STATEMENT / PRIORITY UNASSESSED

---

# 3. Microscopic interaction and record formation

### B1 — finite-time pure-state separation requires conditional interaction action
**Status:** DERIVED FROM ESTABLISHED QUANTUM-SPEED-LIMIT GEOMETRY / CONDITIONAL

```math
\mathcal A_\Delta\ge\hbar\arcsin(1-2\epsilon).
```

### B2 — per-constituent action cap gives a conditional atom-count law
**Status:** DERIVED / CONDITIONAL

```math
N\ge\left\lceil\hbar\arcsin(1-2\epsilon)/a_{\max}\right\rceil.
```

### B3 — identical resonant dipoles have `G=g sqrt(N)` collective bright-state coupling
**Status:** KNOWN / DERIVED IN STATED TAVIS--CUMMINGS SECTOR

### B4 — coherent excitation alone is not persistent record
**Status:** DERIVED IN BENCHMARK

### B5 — record trapping has a finite matching optimum
**Status:** DERIVED / CHECKED

In the clean initial-in-mode limit, `Gamma_opt=2G`.

---

# 4. External capture and optical resources

### X1 — clean one-port critical matching can give unit narrowband capture for any nonzero `G`
**Status:** DERIVED / CONDITIONAL

```math
\Gamma_{\rm match}=4G^2/\kappa.
```

### X2 — optimized external efficiency separates optical escape and collective cooperativity
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
\qquad P_{\rm abs}=1-e^{-\mathrm{OD}}.
```

---

# 5. Semiconductor decision bridge

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

### S4 — binary click distinguishability with independent Poisson dark events
**Status:** DERIVED / CONDITIONAL

```math
\mathcal D_{\rm click}=\eta_s e^{-R_d\tau}.
```

### S5 — dark-event impossibility condition
**Status:** DERIVED / CONDITIONAL

```math
R_d\tau\le-\ln(1-2\epsilon).
```

---

# 6. Electrical-output decision geometry

### G1 — equal-covariance Gaussian optimum coordinate is Mahalanobis / matched-filter distance
**Status:** KNOWN DETECTION-THEORY STRUCTURE / APPLIED HERE

```math
d^2=\langle s,C^{-1}s\rangle
=\int |\tilde s(f)|^2/S_n^{(2)}(f)\,df.
```

### G2 — equal-prior Gaussian error is `P_e=Q(d/2)`
**Status:** KNOWN / DERIVED IN STATED MODEL

### G3 — input-referred decision distance is an NEP-weighted waveform integral
**Status:** DERIVED

```math
d^2=\int |\tilde p(f)|^2/\mathrm{NEP}_2^2(f)\,df.
```

### G4 — one-pole white-noise short-pulse benchmark gives `d^2=E^2D*^2/(A tau)`
**Status:** DERIVED / CONDITIONAL

### G5 — unequal-covariance Gaussian optimum statistic is quadratic
**Status:** KNOWN LIKELIHOOD STRUCTURE / APPLIED HERE

### G6 — covariance change alone can carry detection information
**Status:** DERIVED / KNOWN STATISTICAL CONSEQUENCE

### G7 — Poisson overlap is controlled by square-root count separation
**Status:** DERIVED / KNOWN STATISTICAL STRUCTURE

```math
BC=\exp[-(\sqrt{\mu_1}-\sqrt{\mu_0})^2/2].
```

### G8 — zero-background count error is `P_e=(1/2)e^{-lambda_s T}`
**Status:** DERIVED / CONDITIONAL

---

# 7. Timing and task dependence

### T1 — unknown arrival time makes the event hypothesis a mixture over shifted templates
**Status:** DERIVED / KNOWN NUISANCE-PARAMETER STRUCTURE

### T2 — independent-bin benchmark likelihood is a log-sum-exp over matched filters
**Status:** DERIVED / CONDITIONAL

```math
\Lambda=(1/M)\sum_m e^{dz_m-d^2/2}.
```

### T3 — max-threshold false-alarm and miss probabilities
**Status:** DERIVED / CONDITIONAL

```math
P_{\rm FA}=1-\Phi(\eta)^M,
```

```math
P_{\rm miss}=\Phi(\eta-d)\Phi(\eta)^{M-1}.
```

### T4 — temporal-search threshold scales approximately as `sqrt(2 ln M)` for large independent trial count
**Status:** DERIVED ASYMPTOTIC / CONDITIONAL

### T5 — `M_eff ~ T_search B_eff` is a heuristic time-bandwidth organizing coordinate
**Status:** HEURISTIC / CONDITIONAL

---

# 8. Task-specific sensitivity and detector ordering

### Q1 — Gaussian task functional
**Status:** DERIVED

```math
\mathcal K_D[q]
=\int |\tilde q(f)|^2/\mathrm{NEP}_{2,D}^2(f)\,df.
```

### Q2 — known-time decision-equivalent minimum event energy
**Status:** DERIVED / CONDITIONAL

```math
E_{\min}(q,\epsilon)
=2Q^{-1}(\epsilon)/\sqrt{\mathcal K_D[q]}.
```

### Q3 — task-specific `E_min` is not detector-only
**Status:** DERIVED ORGANIZING STATEMENT

### Q4 — pointwise spectral decision-kernel dominance gives universal ordering within the Gaussian waveform class
**Status:** DERIVED

### Q5 — crossing spectral kernels imply task-dependent ranking reversal
**Status:** DERIVED / CONDITIONAL

### Q6 — detector comparison is naturally a partial order for unrestricted waveform classes
**Status:** DERIVED ORGANIZING STATEMENT

---

# 9. Reset and cycle-closure thermodynamics

### R1 — binary record entropy depends on event prior
**Status:** KNOWN

```math
h(p)=-p\ln p-(1-p)\ln(1-p).
```

`ln2` occurs only for an unbiased record.

### R2 — ideal exact erasure of a degenerate binary memory with no retained side information has scale `k_B T h(p)`
**Status:** KNOWN / CONDITIONAL INFORMATION-THERMODYNAMIC RESULT

Applies under the stated quasistatic isothermal/degenerate-memory assumptions.

### R3 — imperfect reset changes the entropy-reduction scale
**Status:** DERIVED / CONDITIONAL

For final logical error `delta`, the entropy term is `k_B T[h(p)-h(delta)]` when positive and when other free-energy changes vanish.

### R4 — exported side information can remove a universal local reset cost
**Status:** KNOWN PRINCIPLE / DERIVED COUNTEREXAMPLE

Local erasure cost can depend on conditional entropy `H(M|R)`. A perfect external copy can make `H(M|R)=0` while the record remains in `R`.

### R5 — global cycle closure restores an eventual record-erasure problem
**Status:** CONDITIONAL ORGANIZING STATEMENT

If detector + controller + record stores must all return to standard states and no record copy may remain outside the accounting boundary, the stored record entropy must eventually be removed somewhere under standard thermodynamic assumptions.

### R6 — rare-event records do not carry a universal `k_B T ln2` average cycle cost
**Status:** DERIVED / CONDITIONAL

For `p<<1`, `h(p)~p ln(1/p)+p`.

### R7 — activated record retention gives a conditional barrier requirement
**Status:** DERIVED / CONDITIONAL

```math
E_b
\ge
k_BT\ln[\nu_0\tau_{\rm rec}/(-\ln(1-p_d))].
```

### R8 — retention plus fast reset gives a conditional landscape-modulation requirement
**Status:** DERIVED / CONDITIONAL

```math
\Delta E
\ge
k_BT\ln\left[
\frac{\tau_{\rm rec}\ln(1/\epsilon_r)}
{\tau_r[-\ln(1-p_d)]}
\right]
```

when positive and within the common activated-rate model.

### R9 — the stability/reset relation is a control-range bound, not a universal heat bound
**Status:** DERIVED ORGANIZING STATEMENT

### R10 — external record capacity is a resource that can trade against local reset dissipation
**Status:** DERIVED ORGANIZING STATEMENT

---

# 10. Current organizing statement

### O1 — detector boundary is a task-dependent multi-resource performance surface
**Status:** DERIVED ORGANIZING STATEMENT / PRIORITY UNASSESSED

```text
optical task
-> optical access / mode overlap
-> microscopic interaction resource
-> transduction
-> acquisition/extraction versus loss
-> persistent record
-> complete conditional output statistics
-> timing / nuisance parameters
-> optimum decision
-> local reset / record export
-> optional global cycle closure.
```

There is generally no architecture-independent scalar detector boundary or total detector ranking.

---

# 11. Open fronts

### F1 — global cycle-closure lower bound under broader resources
**Status:** OPEN / CURRENT FRONTIER

Test correlations with input/environment, work extraction from detected fields, nonequilibrium reservoirs, active pumps, continuous reversible transduction, and records retained outside the accounting horizon.

### F2 — information acquisition rate under bounded interaction resource
**Status:** OPEN

Seek a rate form that survives open-system and cyclic architectures.

### F3 — stability versus reuse in non-activated memories
**Status:** OPEN

Determine which parts of the current barrier/reset tradeoff survive beyond simple Arrhenius dynamics.

### F4 — prior-art audit
**Status:** OPEN AND REQUIRED BEFORE NOVELTY LANGUAGE

Audit measurement/photodetection theory, quantum speed limits, collective coupling, critical coupling, optical depth, semiconductor collection, Gaussian/Poisson decision theory, timing search, detector figures of merit, and information thermodynamics.

---

# 12. Explicit non-claims

- **NON-CLAIM:** there is a universal atom count at which a detector appears.
- **NON-CLAIM:** total physical atom count is the correct resource in extended matter.
- **NON-CLAIM:** absorption is required for all photodetection.
- **NON-CLAIM:** electron-hole generation alone is a complete detection event.
- **NON-CLAIM:** every click dissipates `k_B T ln2` at acquisition or locally during reset.
- **NON-CLAIM:** record barrier height equals dissipated reset work.
- **NON-CLAIM:** high monochromatic efficiency implies large oscillator count.
- **NON-CLAIM:** scalar `D*` is useless; it is incomplete for general time-dependent decision tasks.
- **NON-CLAIM:** one matched-filter SNR applies to signal-dependent/non-Gaussian noise.
- **NON-CLAIM:** the task-specific energy threshold or partial-order framing is novel.
- **NON-CLAIM:** the current experiment has established a publishable new theorem.
