# Claim Ledger — Experiment 02

**Updated:** 2026-08-12  
**Status:** exploratory; microscopic-to-electrical detector-boundary chain active  
**Priority:** unassessed; no novelty claim

This file is the epistemic boundary. `CURRENT_STATE_LIVE.md` is the operational front door; `RESEARCH_LOG.md` preserves chronology.

Detailed derivations:

- `INTERACTION_ACTION_LOWER_BOUND.md`
- `N_DIPOLE_SINGLE_MODE_MODEL.md`
- `COHERENT_CAPTURE_TO_RECORD.md`
- `TRAVELING_WAVE_CAPTURE.md`
- `MODE_WEIGHTED_OPTICAL_DEPTH.md`
- `SEMICONDUCTOR_DECISION_BRIDGE.md`
- `CONTINUOUS_GAUSSIAN_DECISION.md`

## Status vocabulary

- **KNOWN** — established result used as input.
- **DERIVED** — exact consequence of stated assumptions.
- **CHECKED** — independently or numerically verified.
- **CONDITIONAL** — valid only in the stated model/resource envelope.
- **CANDIDATE DISTINCT — PRIORITY UNPROVEN** — potentially unusual formulation; literature boundary incomplete.
- **INVALIDATED** — counterexample or correction kills the statement as posed.
- **SUPERSEDED** — replaced by a stronger/corrected statement.
- **OPEN** — unresolved.
- **NON-CLAIM** — explicitly not asserted.

---

# 1. Permanent invalidations / corrections

### H1 — absorption followed by re-emission is the photoelectric effect
**Status:** INVALIDATED TERMINOLOGY

Radiative re-emission and electron-hole generation can be stages of one optical history; they are not mutually exclusive definitions of the detector boundary.

### H2 — a universal critical atom count marks the onset of photodetection
**Status:** INVALIDATED AS A GENERAL DEFINITION

A single microscopic system can encode photon arrival, while a macroscopic absorber can fail to retain an accessible record.

### H3 — absorption is sufficient for detection
**Status:** INVALIDATED

Unity absorption can coexist with identical accessible detector states under photon/no-photon hypotheses.

### H4 — absorption is universally necessary for detection
**Status:** INVALIDATED

Dispersive/nondestructive interactions provide counterexamples.

### H5 — electron-hole generation is a complete electrical detection event
**Status:** INVALIDATED GENERALIZATION

Carrier creation must be separated from binding/dissociation, recombination, extraction, persistent record, and readout.

### H6 — gain creates the original photon-arrival information
**Status:** INVALIDATED AS STATED

Hypothesis-independent downstream processing cannot manufacture information absent from its input. Gain can improve practical robustness.

### H7 — microscopic irreversibility occurs at one definite atom count
**Status:** INVALIDATED / REFRAMED

Operational irreversibility depends on subsystem choice, information dispersal, metastability, and accessibility.

### H8 — every detection event dissipates `k_B T ln 2` at acquisition
**Status:** INVALIDATED AS A UNIVERSAL ACQUISITION BOUND

Reset/erasure must be accounted separately unless explicitly built into acquisition.

### H9 — nonzero final detector-energy change is necessary for distinguishability
**Status:** INVALIDATED

A degenerate pointer can be conditionally rotated into an orthogonal state with zero final bare-energy difference.

### H10 — target discrimination alone implies a universal positive deposited-energy cost
**Status:** INVALIDATED IN GENERAL

Finite interaction action survives in the stated pure/unitary finite-time model, but final deposited energy does not.

### H11 — atom count itself is the fundamental detector resource
**Status:** INVALIDATED / SUPERSEDED

Under nonuniform optical coupling, the microscopic resource is `G^2=sum_j |g_j|^2`; in extended matter, optical depth or other mode-weighted measures are more natural.

### H12 — coherent photon-to-matter transfer is itself a persistent detector record
**Status:** INVALIDATED

The excitation can coherently return to the optical mode.

### H13 — arbitrarily fast desired trapping always improves detection
**Status:** INVALIDATED IN THE CURRENT LOSSY MODELS

Overly fast trapping can overdamp coherent acquisition while optical escape remains available.

### H14 — high monochromatic efficiency implies a positive minimum atom count
**Status:** INVALIDATED IN THE CLEAN ONE-PORT MODEL

Any nonzero coupling can reach unit resonant narrowband conversion under critical matching if arbitrarily slow/narrowband operation is allowed.

### H15 — arbitrarily many atoms can always overcome parasitic optical loss
**Status:** INVALIDATED IN THE CURRENT ONE-PORT MODEL

The optical escape factor `eta_esc=kappa_in/kappa` sets an independent efficiency ceiling.

### H16 — literal total atom count in the object is the relevant `N`
**Status:** INVALIDATED

Only mode-coupled matter contributes appreciably to the bright-state norm.

### H17 — arbitrarily large optical thickness can always repair detector performance
**Status:** INVALIDATED IN THE MINIMAL SEMICONDUCTOR DECISION MODEL

Downstream collection/readout ceilings and dark events can make the target impossible even as `alpha L -> infinity`.

### H18 — same conventional `D*` implies same event-detection performance
**Status:** INVALIDATED IN THE ONE-POLE WHITE-NOISE BENCHMARK

At equal area and equal low-frequency white-noise `D*`, a short fixed-energy pulse gives `d^2=E^2D*^2/(A tau)`. Different response times therefore yield different optimum discrimination errors.

---

# 2. Operational detector statements

### I1 — accessible detector-state distinguishability is the minimal current criterion
**Status:** DERIVED FROM THE CHOSEN OPERATIONAL DEFINITION

```math
\mathcal D_D
=\frac12\|\rho_D^{(1)}-\rho_D^{(0)}\|_1.
```

### I2 — equal-prior optimum binary quantum-state error
**Status:** KNOWN

```math
P_{e,\min}=\frac12(1-\mathcal D_D).
```

### I3 — detector definition depends on accessible subsystem
**Status:** DERIVED

Information can leave matter and remain in outgoing radiation or environment.

### I4 — persistence is separate from momentary encoding
**Status:** DERIVED ORGANIZING STATEMENT

A useful record requires a time-qualified distinguishability target, not merely `D_D(t)>0` at one instant.

### I5 — detector is a functional relation, not a phase-of-matter label
**Status:** DERIVED ORGANIZING STATEMENT / PRIORITY UNASSESSED

```text
optical hypothesis
-> accessible distinction
-> persistent record
-> decision.
```

---

# 3. Interaction-action and microscopic coupling results

### B1 — finite-time pure-state separation requires interaction action
**Status:** DERIVED FROM ESTABLISHED QUANTUM-SPEED-LIMIT GEOMETRY / CONDITIONAL

```math
\boxed{
\mathcal A_\Delta
\ge
\hbar\arcsin(1-2\epsilon).
}
```

Perfect discrimination requires `A_Delta >= pi hbar/2`.

### B2 — per-constituent action cap produces a conditional atom-count bound
**Status:** DERIVED / CONDITIONAL

```math
N
\ge
\left\lceil
\frac{\hbar\arcsin(1-2\epsilon)}{a_{\max}}
\right\rceil.
```

### D1 — identical resonant dipoles have collective bright-state coupling
**Status:** KNOWN / DERIVED IN THE TAVIS--CUMMINGS SECTOR

```math
\boxed{G=g\sqrt N.}
```

### D2 — matter-only distinguishability in the exact one-excitation benchmark
**Status:** DERIVED / CONDITIONAL

```math
\boxed{\mathcal D_D(t)=\sin^2(g\sqrt Nt).}
```

### D3 — transient constrained atom-count law
**Status:** DERIVED / CONDITIONAL

Perfect first-lobe transfer requires

```math
N_{\min}
=\left\lceil(\pi/(2g\tau))^2\right\rceil.
```

---

# 4. Persistent-record rate matching

### R1 — exact initial-in-mode record probability
**Status:** DERIVED / CHECKED NUMERICALLY

```math
P_R
=
\frac{4G^2\Gamma}
{(\kappa+\gamma+\Gamma)
[4G^2+\kappa(\gamma+\Gamma)]}.
```

### R2 — desired trapping has a finite optimum
**Status:** DERIVED / CHECKED

```math
\Gamma_{\rm opt}
=
\sqrt{
\frac{(\kappa+\gamma)(4G^2+\kappa\gamma)}{\kappa}
}.
```

For `gamma=0`, `Gamma_opt=2G`.

### R3 — acquisition and record formation are a rate-matching problem
**Status:** DERIVED ORGANIZING STATEMENT

Increasing irreversibility without regard to coherent acquisition can reduce record probability.

---

# 5. Traveling-wave external capture

### X1 — exact external spectral record-conversion kernel
**Status:** DERIVED / CONDITIONAL

```math
\eta_R(\delta)
=
\frac{\kappa_{\rm in}\Gamma G^2}
{\left|
(\kappa/2-i\delta_c)
((\gamma+\Gamma)/2-i\delta_m)
+G^2
\right|^2}.
```

### X2 — clean one-port critical matching gives perfect narrowband capture
**Status:** DERIVED / CONDITIONAL

For `kappa_loss=gamma=0`,

```math
\boxed{\Gamma_{\rm match}=4G^2/\kappa.}
```

Then `r(0)=0` and `eta_R(0)=1`.

### X3 — optimized external efficiency factorizes into optical escape and cooperativity
**Status:** DERIVED

```math
\boxed{
\eta_{R,\max}
=\eta_{\rm esc}\frac{C_N}{1+C_N},
}
```

with

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
\Gamma=4Ng^2/\kappa.
```

Thus

```math
N
\ge
\frac{\kappa B}{8g^2}
\frac{1-2\epsilon}{\epsilon}.
```

---

# 6. Mode-weighted coupling and optical depth

### M1 — unequal microscopic couplings reduce to one bright-state norm
**Status:** DERIVED / KNOWN STRUCTURE

```math
\boxed{G^2=\sum_j|g_j|^2.}
```

### M2 — dilute single-pass absorber is controlled by optical depth
**Status:** KNOWN / CONDITIONAL

```math
\mathrm{OD}=n\sigma L
=\frac{N_{\rm col}\sigma}{A},
\qquad
P_{\rm abs}=1-e^{-\mathrm{OD}}.
```

### M3 — ideal high-efficiency single-pass optical-depth requirement
**Status:** DERIVED / CONDITIONAL

```math
\boxed{\mathrm{OD}_{\min}=-\ln(2\epsilon).}
```

### M4 — architecture changes apparent atom-count scaling
**Status:** DERIVED ORGANIZING STATEMENT

Single-pass absorption and resonant critical coupling trade matter amount against optical dwell time/bandwidth differently.

---

# 7. Semiconductor decision bridge

### S1 — minimal signal-record probability
**Status:** CONDITIONAL ORGANIZING MODEL

```math
\eta_s
=\eta_{\rm mode}
(1-e^{-\alpha L})
\eta_{eh}
P_{\rm col}
P_{\rm read}.
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

The excitation must still survive, collect, form a record, and remain distinguishable from dark output.

### S4 — binary click distinguishability with independent Poisson dark events
**Status:** DERIVED / CONDITIONAL

```math
\boxed{
\mathcal D_{\rm click}
=\eta_s e^{-R_d\tau}.
}
```

Thus

```math
P_e
=\frac12(1-\eta_s e^{-R_d\tau}).
```

### S5 — dark-event impossibility condition
**Status:** DERIVED / CONDITIONAL

```math
\boxed{
R_d\tau
\le
-\ln(1-2\epsilon).
}
```

---

# 8. Continuous Gaussian electrical-output results

### G1 — optimum decision coordinate is Mahalanobis / matched-filter distance
**Status:** KNOWN DETECTION-THEORY STRUCTURE / APPLIED HERE

For

```math
H_0:y=n,
\qquad
H_1:y=s+n,
```

with common Gaussian covariance `C`,

```math
\boxed{
d^2=\langle s,C^{-1}s\rangle.
}
```

For stationary noise,

```math
\boxed{
d^2
=\int_{-\infty}^{\infty}
\frac{|\tilde s(f)|^2}
{S_n^{(2)}(f)}df.
}
```

### G2 — equal-prior Gaussian waveform error
**Status:** KNOWN / DERIVED IN THE STATED MODEL

```math
\boxed{P_e=Q(d/2).}
```

### G3 — input-referred noise gives a task-weighted NEP integral
**Status:** DERIVED

If `s_tilde=R(f)p_tilde`, then

```math
\boxed{
d^2
=\int
\frac{|\tilde p(f)|^2}
{\mathrm{NEP}_2^2(f)}df.
}
```

Thus the complete practical decision coordinate depends on the whole signal/noise spectrum, not one quoted frequency.

### G4 — one-pole white-noise pulse benchmark
**Status:** DERIVED / CONDITIONAL

For impulse response `h(t)=exp(-t/tau)/tau`, short optical energy `E`, and flat one-sided output-noise PSD,

```math
\boxed{
d^2
=\frac{E^2}{\tau\,\mathrm{NEP}^2}.
}
```

### G5 — equal-area equal-D* pulse discrimination depends on response time
**Status:** DERIVED / CONDITIONAL

Using `NEP=sqrt(A)/D*`,

```math
\boxed{
d^2
=\frac{E^2D^{*2}}{A\tau}.
}
```

Hence `d proportional to tau^-1/2` at fixed `E`, `A`, and low-frequency white-noise `D*`.

### G6 — finite observation time adds an additional slow-detector penalty
**Status:** DERIVED / CONDITIONAL

```math
\boxed{
d^2(T)
=\frac{E^2}{\tau\,\mathrm{NEP}^2}
(1-e^{-2T/\tau}).
}
```

For `T<<tau`, `d^2 ~ 2E^2T/(tau^2 NEP^2)`.

### G7 — scalar D* is not a complete task-independent detector coordinate
**Status:** DERIVED ORGANIZING STATEMENT

A scalar `D*` does not retain the full temporal/spectral response and noise structure needed to compute optimum waveform discrimination.

---

# 9. Current organizing statement

### O1 — detector boundary is a multi-resource performance surface
**Status:** DERIVED ORGANIZING STATEMENT / PRIORITY UNASSESSED

The strongest current chain is

```text
optical task
-> optical access / mode overlap
-> mode-weighted coupling or optical depth
-> microscopic transduction
-> competition with loss/recombination
-> persistent record
-> electrical transfer + noise spectrum
-> noise-weighted hypothesis distance
-> decision error.
```

There may be no architecture-independent scalar detector quality unless the optical task class is specified first.

---

# 10. Open fronts

### F1 — signal-dependent noise
**Status:** OPEN / CURRENT FRONTIER

Allow covariance to differ under `H0` and `H1`, including shot noise, generation-recombination noise, and gain noise.

### F2 — unknown photon arrival time / timing jitter
**Status:** OPEN

Derive the penalty for searching over arrival time and for stochastic detector latency.

### F3 — task-specific detectivity
**Status:** OPEN

Determine whether an optimal scalar quantity can be defined for a specified class of optical waveforms and decision constraints.

### F4 — continuum semiconductor derivation from susceptibility
**Status:** OPEN

Bridge oscillator-strength density to susceptibility, absorption coefficient, carrier generation, and transport without relying only on dilute Beer-Lambert intuition.

### F5 — architecture-independent lower bounds
**Status:** OPEN

Continue attacking candidate universal resources after allowing optical topology, bandwidth/time, reservoirs, and record channels.

### F6 — prior-art audit
**Status:** OPEN AND REQUIRED BEFORE NOVELTY LANGUAGE

Audit quantum photodetection, speed limits, collective coupling, input-output/critical coupling, cooperativity, optical depth, semiconductor collection, Gaussian detection theory, matched filtering, detector figures of merit, and measurement thermodynamics.

---

# 11. Explicit non-claims

- **NON-CLAIM:** there is a universal critical number of atoms at which a photodetector appears.
- **NON-CLAIM:** total physical atom count is the correct coupling resource in extended matter.
- **NON-CLAIM:** absorption is required for all photodetection.
- **NON-CLAIM:** electron-hole generation alone is a complete detection event.
- **NON-CLAIM:** every detection event costs `k_B T ln 2` at acquisition.
- **NON-CLAIM:** high monochromatic efficiency implies large oscillator count.
- **NON-CLAIM:** scalar `D*` is useless; it is simply incomplete for general time-dependent decision tasks.
- **NON-CLAIM:** trace distance, Helstrom, quantum-speed-limit, Tavis--Cummings, cooperativity, critical coupling, optical depth, Gaussian detection theory, or matched filtering are novel.
- **NON-CLAIM:** the current experiment has established a publishable new theorem.
