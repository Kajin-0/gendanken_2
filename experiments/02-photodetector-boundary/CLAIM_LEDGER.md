# Claim Ledger — Experiment 02

**Updated:** 2026-08-12  
**Status:** exploratory; full optical-to-decision detector-boundary chain active  
**Priority:** unassessed; no novelty claim

This is the epistemic boundary. `CURRENT_STATE_LIVE.md` is the operational front door; `RESEARCH_LOG.md` preserves chronology.

Detailed derivations:

- `INTERACTION_ACTION_LOWER_BOUND.md`
- `N_DIPOLE_SINGLE_MODE_MODEL.md`
- `COHERENT_CAPTURE_TO_RECORD.md`
- `TRAVELING_WAVE_CAPTURE.md`
- `MODE_WEIGHTED_OPTICAL_DEPTH.md`
- `SEMICONDUCTOR_DECISION_BRIDGE.md`
- `CONTINUOUS_GAUSSIAN_DECISION.md`
- `SIGNAL_DEPENDENT_NOISE.md`
- `UNKNOWN_ARRIVAL_TIME.md`
- `TASK_SPECIFIC_DETECTIVITY.md`

## Status vocabulary

- **KNOWN** — established result used as input.
- **DERIVED** — consequence of stated assumptions.
- **CHECKED** — independently or numerically verified.
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

Interband absorption can create an electron-hole excitation that later recombines radiatively. Re-emission and pair generation can be stages of one event.

### H2 — a universal critical atom count defines photodetection
**Status:** INVALIDATED

A single microscopic system can encode photon arrival, while a macroscopic absorber can fail to retain an accessible record.

### H3 — absorption is sufficient for detection
**Status:** INVALIDATED

Unity absorption can coexist with identical accessible detector states under the two optical hypotheses.

### H4 — absorption is universally necessary for detection
**Status:** INVALIDATED

Dispersive/nondestructive interactions provide counterexamples.

### H5 — electron-hole generation is a complete electrical detection event
**Status:** INVALIDATED GENERALIZATION

Excitation creation must be separated from binding/dissociation, recombination, extraction/collection, persistent record, and readout.

### H6 — gain creates the original photon-arrival information
**Status:** INVALIDATED AS STATED

Hypothesis-independent downstream processing cannot manufacture absent upstream information; gain can improve practical robustness.

### H7 — microscopic irreversibility occurs at one definite atom count
**Status:** INVALIDATED / REFRAMED

Operational irreversibility depends on subsystem choice, information dispersal, trapping/metastability, and accessibility.

### H8 — every detector click costs `k_B T ln 2` at acquisition
**Status:** INVALIDATED AS A UNIVERSAL ACQUISITION BOUND

Logical erasure/reset must be accounted separately unless explicitly built into acquisition.

### H9 — nonzero final detector-energy change is necessary for distinguishability
**Status:** INVALIDATED

A degenerate pointer can be conditionally rotated into an orthogonal state with zero final bare-energy difference.

### H10 — target discrimination implies a universal positive deposited-energy cost
**Status:** INVALIDATED IN GENERAL

Finite interaction action survives in the stated pure/unitary finite-time model; final deposited energy does not.

### H11 — atom count itself is the fundamental microscopic resource
**Status:** INVALIDATED / SUPERSEDED

Under nonuniform optical coupling, `G^2=sum_j |g_j|^2`; in extended matter, optical depth or other mode-weighted quantities are more natural.

### H12 — coherent photon-to-matter transfer is already a persistent record
**Status:** INVALIDATED

The excitation can coherently return to the optical mode.

### H13 — arbitrarily strong desired trapping always improves detection
**Status:** INVALIDATED IN CURRENT LOSSY MODELS

Excessive trapping can overdamp acquisition while optical escape remains available.

### H14 — high monochromatic efficiency implies a positive minimum atom count
**Status:** INVALIDATED IN CLEAN ONE-PORT MODEL

Any nonzero coupling can reach unit resonant narrowband conversion under critical matching if arbitrarily slow/narrowband operation is allowed.

### H15 — arbitrarily many atoms can always overcome parasitic optical loss
**Status:** INVALIDATED IN CURRENT ONE-PORT MODEL

`eta_esc=kappa_in/kappa` sets an independent optical-access ceiling.

### H16 — literal total atom count in the object is the relevant `N`
**Status:** INVALIDATED

Only mode-coupled matter contributes significantly to the bright-state norm.

### H17 — arbitrarily large optical thickness can always repair detector performance
**Status:** INVALIDATED IN MINIMAL SEMICONDUCTOR DECISION MODEL

Downstream collection/readout ceilings and dark events can make the target impossible even for `alpha L -> infinity`.

### H18 — same conventional scalar `D*` implies same event-detection performance
**Status:** INVALIDATED IN ONE-POLE WHITE-NOISE BENCHMARK

At equal area and low-frequency `D*`, `d^2=E^2D*^2/(A tau)` for a short fixed-energy pulse, so response time changes optimum decision error.

### H19 — no mean signal implies no detection information
**Status:** INVALIDATED

If `C_0 != C_1`, Gaussian hypotheses with identical means can still be distinguished from their covariance difference.

### H20 — one fixed-noise SNR law describes both zero-background and background-dominated counting
**Status:** INVALIDATED

Poisson discrimination changes qualitatively between finite-background and zero-background limits.

### H21 — known-time matched-filter performance transfers unchanged to unknown arrival time
**Status:** INVALIDATED

Arrival-time uncertainty creates a nuisance-parameter search / trials penalty tied to the number of effectively distinguishable temporal modes.

### H22 — one scalar detector ranking can represent every optical waveform task
**Status:** INVALIDATED IN THE LINEAR EQUAL-COVARIANCE GAUSSIAN TASK CLASS WHEN KERNELS CROSS

If two detectors' spectral decision kernels cross, their ranking reverses for appropriately chosen waveform spectra.

---

# 2. Operational detector statements

### I1 — accessible state distinguishability is the minimal current quantum criterion
**Status:** DERIVED FROM CHOSEN OPERATIONAL DEFINITION

```math
\mathcal D_D
=\frac12\|\rho_D^{(1)}-\rho_D^{(0)}\|_1.
```

### I2 — equal-prior optimum binary quantum-state error
**Status:** KNOWN

```math
P_{e,\min}=\frac12(1-\mathcal D_D).
```

### I3 — detector definition depends on the accessible subsystem
**Status:** DERIVED

Information can leave matter and remain in outgoing radiation or the environment.

### I4 — persistence is separate from momentary encoding
**Status:** DERIVED ORGANIZING STATEMENT

A practical record requires time-qualified distinguishability, not merely `D_D(t)>0` at one instant.

### I5 — detector is a functional relation, not a phase-of-matter label
**Status:** DERIVED ORGANIZING STATEMENT / PRIORITY UNASSESSED

```text
optical hypothesis
-> accessible distinction
-> persistent record
-> decision.
```

### I6 — the general classical boundary is full conditional-output distinguishability
**Status:** DERIVED ORGANIZING STATEMENT

Once noise can depend on the hypothesis, the complete conditional output distributions/processes are the invariant inference objects; mean signal divided by one PSD is only a special case.

---

# 3. Interaction-action and microscopic coupling

### B1 — finite-time pure-state separation requires interaction action
**Status:** DERIVED FROM ESTABLISHED QUANTUM-SPEED-LIMIT GEOMETRY / CONDITIONAL

```math
\mathcal A_\Delta
\ge
\hbar\arcsin(1-2\epsilon).
```

Perfect discrimination requires `A_Delta >= pi hbar/2`.

### B2 — per-constituent action cap yields a conditional atom-count law
**Status:** DERIVED / CONDITIONAL

```math
N
\ge
\left\lceil
\frac{\hbar\arcsin(1-2\epsilon)}{a_{\max}}
\right\rceil.
```

### B3 — identical resonant dipoles have collective bright-state coupling
**Status:** KNOWN / DERIVED IN STATED TAVIS--CUMMINGS SECTOR

```math
G=g\sqrt N.
```

### B4 — exact transient matter distinguishability in that benchmark
**Status:** DERIVED / CONDITIONAL

```math
\mathcal D_D(t)=\sin^2(g\sqrt Nt).
```

Perfect first-lobe transfer requires `N_min=ceil[(pi/(2g tau))^2]`.

---

# 4. Persistent-record rate matching

### R1 — exact initial-in-mode record probability
**Status:** DERIVED / CHECKED NUMERICALLY

```math
P_R
=\frac{4G^2\Gamma}
{(\kappa+\gamma+\Gamma)[4G^2+\kappa(\gamma+\Gamma)]}.
```

### R2 — desired trapping has a finite optimum
**Status:** DERIVED / CHECKED

```math
\Gamma_{\rm opt}
=\sqrt{\frac{(\kappa+\gamma)(4G^2+\kappa\gamma)}{\kappa}}.
```

For `gamma=0`, `Gamma_opt=2G`.

### R3 — acquisition and persistent record formation are a matching problem
**Status:** DERIVED ORGANIZING STATEMENT

Irreversibility/trapping is not an independent monotonic good.

---

# 5. Traveling-wave external capture

### X1 — exact spectral record-conversion kernel
**Status:** DERIVED / CONDITIONAL

```math
\eta_R(\delta)
=\frac{\kappa_{\rm in}\Gamma G^2}
{|(\kappa/2-i\delta_c)((\gamma+\Gamma)/2-i\delta_m)+G^2|^2}.
```

### X2 — clean one-port critical matching gives perfect narrowband capture
**Status:** DERIVED / CONDITIONAL

```math
\Gamma_{\rm match}=4G^2/\kappa,
```

with `r(0)=0` and `eta_R(0)=1`.

### X3 — optimized external efficiency factorizes into escape and cooperativity ceilings
**Status:** DERIVED

```math
\eta_{R,\max}
=\eta_{\rm esc}\frac{C_N}{1+C_N},
```

where

```math
\eta_{\rm esc}=\kappa_{\rm in}/\kappa,
\qquad
C_N=4G^2/(\kappa\gamma).
```

### X4 — finite bandwidth restores a constrained atom threshold
**Status:** DERIVED / CONDITIONAL BAD-CAVITY BENCHMARK

For Lorentzian incident HWHM `B`,

```math
P_R=\Gamma/(\Gamma+B),
\qquad
\Gamma=4Ng^2/\kappa,
```

so

```math
N
\ge
\frac{\kappa B}{8g^2}
\frac{1-2\epsilon}{\epsilon}.
```

---

# 6. Mode-weighted coupling and optical depth

### M1 — unequal microscopic couplings reduce to a bright-state norm
**Status:** DERIVED / KNOWN STRUCTURE

```math
G^2=\sum_j|g_j|^2.
```

### M2 — dilute single-pass absorber is controlled by optical depth
**Status:** KNOWN / CONDITIONAL

```math
\mathrm{OD}=n\sigma L
=\frac{N_{\rm col}\sigma}{A},
\qquad
P_{\rm abs}=1-e^{-\mathrm{OD}}.
```

### M3 — ideal high-efficiency single-pass requirement
**Status:** DERIVED / CONDITIONAL

```math
\mathrm{OD}_{\min}=-\ln(2\epsilon).
```

### M4 — architecture changes apparent matter-count requirements
**Status:** DERIVED ORGANIZING STATEMENT

Single-pass absorption and resonant critical coupling trade oscillator strength against optical dwell time/bandwidth differently.

---

# 7. Semiconductor decision bridge

### S1 — minimal signal-record factorization
**Status:** CONDITIONAL ORGANIZING MODEL

```math
\eta_s
=\eta_{\rm mode}
(1-e^{-\alpha L})
\eta_{eh}P_{\rm col}P_{\rm read}.
```

### S2 — extraction/recombination race
**Status:** CONDITIONAL

```math
P_{\rm col}
=\frac{\Gamma_{\rm ext}}
{\Gamma_{\rm ext}+\Gamma_{\rm rec}}.
```

### S3 — electron-hole generation is a transduction stage, not the complete detector boundary
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

# 8. Equal-covariance Gaussian electrical output

### G1 — optimum decision coordinate is Mahalanobis / matched-filter distance
**Status:** KNOWN DETECTION-THEORY STRUCTURE / APPLIED HERE

```math
d^2=\langle s,C^{-1}s\rangle
=\int\frac{|\tilde s(f)|^2}{S_n^{(2)}(f)}df.
```

### G2 — equal-prior error
**Status:** KNOWN / DERIVED IN STATED MODEL

```math
P_e=Q(d/2).
```

### G3 — input-referred noise gives task-weighted NEP integral
**Status:** DERIVED

```math
d^2
=\int\frac{|\tilde p(f)|^2}{\mathrm{NEP}_2^2(f)}df.
```

### G4 — one-pole white-noise pulse benchmark
**Status:** DERIVED / CONDITIONAL

```math
d^2
=\frac{E^2}{\tau\,\mathrm{NEP}^2}
=\frac{E^2D^{*2}}{A\tau}.
```

### G5 — finite observation time further penalizes slow response
**Status:** DERIVED / CONDITIONAL

```math
d^2(T)
=\frac{E^2}{\tau\,\mathrm{NEP}^2}(1-e^{-2T/\tau}).
```

---

# 9. Signal-dependent and Poisson noise

### N1 — unequal-covariance Gaussian optimum statistic is quadratic
**Status:** KNOWN LIKELIHOOD STRUCTURE / APPLIED HERE

```math
\ell(y)
=\frac12(y-\mu_0)^TC_0^{-1}(y-\mu_0)
-\frac12(y-\mu_1)^TC_1^{-1}(y-\mu_1)
-\frac12\ln\frac{\det C_1}{\det C_0}.
```

### N2 — covariance change alone can carry detection information
**Status:** DERIVED / KNOWN STATISTICAL CONSEQUENCE

If `mu_0=mu_1` but `C_0 != C_1`, the hypotheses remain distinguishable.

### N3 — exact Poisson count likelihood ratio
**Status:** KNOWN / DERIVED

```math
\ell(K)
=K\ln(\mu_1/\mu_0)-(\mu_1-\mu_0).
```

### N4 — Poisson Bhattacharyya overlap is controlled by square-root count separation
**Status:** DERIVED / KNOWN STATISTICAL STRUCTURE

```math
BC
=\exp[-(\sqrt{\mu_1}-\sqrt{\mu_0})^2/2].
```

### N5 — weak-signal finite-background limit recovers shot-noise scaling
**Status:** DERIVED / CONDITIONAL EXPANSION

For `lambda_s << lambda_d`, the overlap exponent rate scales as `lambda_s^2/(8 lambda_d)`.

### N6 — zero-background event error is exponential in expected signal counts
**Status:** DERIVED / CONDITIONAL

```math
P_e=\frac12e^{-\lambda_sT}.
```

---

# 10. Unknown arrival time

### T1 — unknown arrival time makes `H1` a mixture over shifted templates
**Status:** DERIVED / KNOWN NUISANCE-PARAMETER STRUCTURE

```math
\Lambda(y)
=\int p(\tau)
\exp[\langle y,C^{-1}s_\tau\rangle
-\tfrac12\langle s_\tau,C^{-1}s_\tau\rangle]d\tau.
```

### T2 — independent-bin mixture likelihood
**Status:** DERIVED / CONDITIONAL BENCHMARK

For `M` orthogonal equal-norm candidate times,

```math
\Lambda(z)
=\frac1M\sum_{m=1}^M e^{dz_m-d^2/2}.
```

### T3 — exact false-alarm and miss probabilities for max-threshold benchmark
**Status:** DERIVED / CONDITIONAL

```math
P_{\rm FA}=1-\Phi(\eta)^M,
```

```math
P_{\rm miss}=\Phi(\eta-d)\Phi(\eta)^{M-1}.
```

### T4 — timing-search threshold grows logarithmically in effective trial count
**Status:** DERIVED ASYMPTOTIC / CONDITIONAL

For large `M`, small false-alarm target, `eta` scales approximately as `sqrt(2 ln M)` up to logarithmic corrections and the false-alarm factor.

### T5 — effective temporal trial count is tied to time-bandwidth complexity
**Status:** HEURISTIC / CONDITIONAL

`M_eff ~ T_search B_eff` is an order-of-magnitude organizing coordinate, not a universal exact formula.

---

# 11. Task-specific sensitivity and detector ordering

### Q1 — known-time Gaussian task functional
**Status:** DERIVED

For `p(t)=E q(t)` with unit-energy-shape normalization,

```math
\mathcal K_D[q]
=\int\frac{|\tilde q(f)|^2}{\mathrm{NEP}_{2,D}^2(f)}df,
\qquad
d^2=E^2\mathcal K_D[q].
```

### Q2 — decision-equivalent minimum event energy
**Status:** DERIVED / CONDITIONAL

```math
E_{\min}(q,\epsilon)
=\frac{2Q^{-1}(\epsilon)}{\sqrt{\mathcal K_D[q]}}
```

for known timing, equal priors, and equal-covariance Gaussian readout.

### Q3 — task-specific energy threshold is not detector-only
**Status:** DERIVED ORGANIZING STATEMENT

Changing waveform, timing uncertainty, false-alarm target, or noise class changes the threshold functional.

### Q4 — pointwise spectral decision-kernel dominance gives universal ordering within the Gaussian waveform class
**Status:** DERIVED

Define

```math
W_D(f)=1/\mathrm{NEP}_{2,D}^2(f).
```

If `W_A(f)>=W_B(f)` throughout the allowed band, then `K_A[q]>=K_B[q]` for every allowed waveform.

### Q5 — crossing kernels imply task-dependent ranking reversal
**Status:** DERIVED / CONDITIONAL

If `W_A-W_B` changes sign, there exist waveform tasks for which A is better and others for which B is better.

Therefore no task-independent scalar total ranking can preserve all waveform decisions for that detector pair.

### Q6 — detector comparison is naturally a partial order
**Status:** DERIVED ORGANIZING STATEMENT

Pointwise spectral dominance compares some detector pairs; crossing kernels leave others incomparable until the task is specified.

---

# 12. Current organizing statement

### O1 — detector boundary is a task-dependent multi-resource performance surface
**Status:** DERIVED ORGANIZING STATEMENT / PRIORITY UNASSESSED

Current chain:

```text
optical task
-> optical access / mode overlap
-> mode-weighted coupling / optical depth
-> microscopic transduction
-> competition with loss/recombination
-> persistent record
-> complete conditional output statistics
-> timing / nuisance parameters
-> optimum likelihood decision
-> decision error
-> reset/reuse.
```

There is generally no architecture-independent scalar detector boundary or total detector ranking.

---

# 13. Open fronts

### F1 — reusable detector reset thermodynamics
**Status:** OPEN / CURRENT FRONTIER

Determine whether fixed decision error, record stability, cycle time, and reset requirements imply a nontrivial thermodynamic lower bound after reversible measurement/exported-record counterexamples are allowed.

### F2 — record stability versus reset speed
**Status:** OPEN

Test whether metastable record retention and rapid reuse enforce a barrier/rate tradeoff.

### F3 — bounded interaction resource versus information acquisition rate
**Status:** OPEN

Ask whether a rate version of the interaction-action bound survives open-system/cyclic detector architectures.

### F4 — architecture-independent lower bounds
**Status:** OPEN

Continue counterexample-first testing with narrowband/long-time operation, external reservoirs, active pumps, exported records, reversible memories, and QND-like schemes.

### F5 — prior-art audit
**Status:** OPEN AND REQUIRED BEFORE NOVELTY LANGUAGE

Audit quantum measurement/photodetection, speed limits, collective coupling, input-output critical coupling, optical depth, semiconductor collection, Gaussian/Poisson detection theory, timing-search statistics, detector figures of merit, and measurement thermodynamics.

---

# 14. Explicit non-claims

- **NON-CLAIM:** there is a universal atom count at which a detector appears.
- **NON-CLAIM:** total physical atom count is the correct resource in extended matter.
- **NON-CLAIM:** absorption is required for all photodetection.
- **NON-CLAIM:** electron-hole generation alone is a complete detection event.
- **NON-CLAIM:** every click costs `k_B T ln 2` at acquisition.
- **NON-CLAIM:** high monochromatic efficiency implies large oscillator count.
- **NON-CLAIM:** scalar `D*` is useless; it is incomplete for general time-dependent decision tasks.
- **NON-CLAIM:** one matched-filter SNR applies when noise is hypothesis dependent or non-Gaussian.
- **NON-CLAIM:** the task-specific `E_min` formulation is novel.
- **NON-CLAIM:** trace distance, Helstrom, speed limits, Tavis--Cummings, critical coupling, cooperativity, Beer-Lambert, Gaussian/Poisson likelihood theory, matched filtering, or trials-factor results are novel.
- **NON-CLAIM:** the current experiment has established a publishable new theorem.
