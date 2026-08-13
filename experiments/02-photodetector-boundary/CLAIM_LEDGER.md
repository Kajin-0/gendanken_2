# Claim Ledger — Experiment 02

**Updated:** 2026-08-12  
**Status:** exploratory photodetector-boundary Gedanken experiment; microscopic, external-capture, optical-depth, and semiconductor decision models derived  
**Priority:** unassessed; no novelty claim

This file is the epistemic boundary. `CURRENT_STATE_LIVE.md` is the operational front door; `RESEARCH_LOG.md` preserves chronology.

Detailed derivations:

- `INTERACTION_ACTION_LOWER_BOUND.md`
- `N_DIPOLE_SINGLE_MODE_MODEL.md`
- `COHERENT_CAPTURE_TO_RECORD.md`
- `TRAVELING_WAVE_CAPTURE.md`
- `MODE_WEIGHTED_OPTICAL_DEPTH.md`
- `SEMICONDUCTOR_DECISION_BRIDGE.md`

## Status vocabulary

- **KNOWN** — established result used as input.
- **DERIVED** — exact consequence of stated assumptions.
- **CHECKED** — independently or numerically verified.
- **CONDITIONAL** — valid only inside the stated model/resource envelope.
- **CANDIDATE DISTINCT — PRIORITY UNPROVEN** — potentially unusual formulation; literature boundary incomplete.
- **INVALIDATED** — counterexample or correction kills the statement as posed.
- **SUPERSEDED** — replaced by a stronger/corrected statement.
- **OPEN** — unresolved.
- **NON-CLAIM** — explicitly not asserted.

---

# 1. Permanent invalidations / corrections

### H1 — absorption followed by re-emission is the photoelectric effect
**Status:** INVALIDATED TERMINOLOGY

Absorption followed by later photon emission is radiative excitation/relaxation. External photoelectric emission ejects an electron; semiconductor interband absorption is commonly described as an internal photoelectric process.

### H2 — photon re-emission and electron-hole generation are mutually exclusive alternatives
**Status:** INVALIDATED

Interband absorption can create an electron-hole excitation that later recombines radiatively. These may be successive stages of one event.

### H3 — a universal critical atom count marks the onset of photodetection
**Status:** INVALIDATED AS A GENERAL DEFINITION

One microscopic system can encode photon arrival; a macroscopic absorber can fail to retain an accessible record. Minimum `N` appears only after architecture/resource constraints are imposed.

### H4 — photon absorption is sufficient for photodetection
**Status:** INVALIDATED

If accessible material states conditioned on photon/no-photon input are identical at interrogation, the material provides no discrimination even if absorption was unity.

### H5 — photon absorption is universally necessary for photodetection
**Status:** INVALIDATED

A dispersive/nondestructive interaction can correlate photon presence with distinguishable matter states while the photon survives.

### H6 — creating an electron-hole pair is sufficient for an electrical detection event
**Status:** INVALIDATED GENERALIZATION

The excitation can remain bound, recombine, trap in an inaccessible state, fail separation/collection, or fail readout.

### H7 — gain creates new information about whether the photon arrived
**Status:** INVALIDATED AS STATED

Hypothesis-independent downstream processing cannot create input-hypothesis information absent from its input. Gain can protect/enlarge an existing distinction against later readout noise.

### H8 — microscopic irreversibility occurs at one definite detector atom count
**Status:** INVALIDATED / REFRAMED

Closed photon + detector + environment evolution may remain unitary. Operational irreversibility must be tied to subsystem choice, information dispersal, metastability, loss channels, and practical accessibility.

### H9 — every detected photon dissipates `k_B T ln 2` at acquisition
**Status:** INVALIDATED AS A UNIVERSAL ACQUISITION BOUND

Landauer-type cost belongs to logically irreversible operations such as erasure under stated thermodynamic conditions. Reset must be accounted separately unless the architecture explicitly couples it into acquisition.

### H10 — nonzero final detector-energy change is necessary for distinguishability
**Status:** INVALIDATED

A degenerate pointer can be conditionally rotated into an orthogonal state while the final bare detector-energy change is zero.

### H11 — target discrimination alone implies a universal positive deposited/dissipated energy per event
**Status:** INVALIDATED IN GENERAL

The degenerate-pointer counterexample gives perfect final detector-state distinguishability with zero final bare-energy separation. Finite interaction action is still required in the stated pure/unitary finite-time model.

### H12 — atom count itself is the fundamental detector resource coordinate
**Status:** INVALIDATED / SUPERSEDED

Atom count is a derived constrained resource. Under nonuniform optical coupling, the relevant microscopic quantity is `sum_j |g_j|^2`; in extended matter, optical depth or other mode-weighted measures are more natural.

### H13 — coherent photon-to-matter excitation transfer is by itself a persistent detector record
**Status:** INVALIDATED

In the lossless one-mode model the excitation Rabi-oscillates back into the optical mode. Acquisition and retention are distinct.

### H14 — making the desired irreversible trapping rate arbitrarily large always improves detection
**Status:** INVALIDATED IN THE CURRENT LOSSY MODELS

When optical escape competes, overly fast trapping overdamps coherent transfer. Both the initial-in-mode and external-capture formulations have finite matching conditions.

### H15 — high monochromatic external efficiency by itself implies a minimum atom count
**Status:** INVALIDATED IN THE CLEAN ONE-PORT MODEL

For any nonzero `G`, unit resonant narrowband conversion is possible by choosing `Gamma=4G^2/kappa`. Weak coupling is paid for in bandwidth/time rather than peak efficiency.

### H16 — arbitrarily many atoms can always compensate parasitic optical loss
**Status:** INVALIDATED IN THE CURRENT ONE-PORT MODEL

Optimized external efficiency is bounded by `eta_esc=kappa_in/kappa`. Increasing collective coupling cannot exceed an optical-access ceiling created by inaccessible optical channels.

### H17 — literal total atom count in the object is the relevant `N`
**Status:** INVALIDATED

Atoms outside the optical mode, at field nodes, or with poor transition-dipole overlap can contribute negligibly. The bright-state resource is `G^2=sum_j|g_j|^2`.

### H18 — arbitrarily large optical thickness can always repair detector performance
**Status:** INVALIDATED IN THE MINIMAL SEMICONDUCTOR DECISION MODEL

If downstream collection/readout is too poor or dark-event probability too high, `alpha L -> infinity` still cannot satisfy the target decision error.

---

# 2. Operational detector statements

### I1 — accessible detector-state distinguishability is the minimal current criterion
**Status:** DERIVED FROM THE CHOSEN OPERATIONAL DEFINITION

```math
\mathcal D_D
=\frac12\|\rho_D^{(1)}-\rho_D^{(0)}\|_1.
```

`D_D=0` means no measurement restricted to `D` can discriminate the hypotheses; `D_D>0` means some discrimination is possible.

### I2 — equal-prior optimum binary error is fixed by trace distance
**Status:** KNOWN

```math
P_{e,\min}=\frac12(1-\mathcal D_D).
```

### I3 — detector definition depends on accessible subsystem
**Status:** DERIVED

Information can leave matter and survive in outgoing radiation/environment. Any statement that the detector retained or forgot the photon requires an explicit system boundary.

### I4 — persistence is separate from momentary encoding
**Status:** DERIVED ORGANIZING STATEMENT

A useful record may require

```math
\mathcal D_D(t)\ge\mathcal D_{\min}
\quad
0<t\le\tau_{\rm rec}.
```

### I5 — photodetector is a functional relation, not a phase-of-matter label
**Status:** DERIVED ORGANIZING STATEMENT / PRIORITY UNASSESSED

```text
optical hypothesis
-> accessible distinction
-> persistent record
-> readout decision.
```

---

# 3. Crossovers kept separate from detector definition

### C1 — finite atomic spectra cross over continuously toward band-like descriptions
**Status:** KNOWN / QUALITATIVE

A rough scale is `Delta E ~ W/N`. Band language becomes useful when spacing is small relative to linewidth/disorder/thermal/measurement resolution. This is not the detector boundary.

### C2 — bound excitation versus mobile carriers is material/environment dependent
**Status:** KNOWN / CONDITIONAL MODEL

Wannier-Mott estimates can organize one regime but do not define photodetection universally.

### C3 — carrier collection can be represented by competing rates only in a minimal hazard model
**Status:** CONDITIONAL

```math
P_{\rm col}
=\frac{\Gamma_{\rm ext}}
{\Gamma_{\rm ext}+\Gamma_{\rm rec}}.
```

Real devices can violate the independent-exponential assumptions.

---

# 4. Information / amplification statements

### A1 — downstream gain can improve practical readout without increasing ideal input distinguishability
**Status:** KNOWN PRINCIPLE / WORKING INTERPRETATION

Trace-distance contractivity/data processing prevents a hypothesis-independent downstream channel from manufacturing absent input information. Gain can nevertheless protect a microscopic distinction from later added noise and finite resolution.

### A2 — microscopic-to-macroscopic conversion is a record-stabilization problem
**Status:** DERIVED ORGANIZING STATEMENT

```text
microscopic correlation
-> pointer-state separation
-> trapping/decoherence/metastability
-> accessible macroscopic record.
```

---

# 5. Interaction-action lower bound

### B1 — pure detector branch angle required by target error
**Status:** DERIVED / KNOWN GEOMETRY

For pure detector branches,

```math
\theta
=\arccos|\langle D^{(0)}|D^{(1)}\rangle|,
\qquad
\mathcal D_D=\sin\theta,
```

so

```math
\theta\ge\arcsin(1-2\epsilon).
```

### B2 — finite-time pure-state separation requires interaction action
**Status:** DERIVED FROM ESTABLISHED QUANTUM SPEED-LIMIT GEOMETRY / CONDITIONAL

```math
\boxed{
\mathcal A_\Delta
\equiv
\int_0^\tau\Delta V_I(t)dt
\ge
\hbar\arcsin(1-2\epsilon).
}
```

Perfect discrimination requires `A_Delta >= pi hbar/2`.

### B3 — degenerate qubit saturates the perfect-discrimination action bound
**Status:** CHECKED ANALYTICALLY

A conditional `sigma_y` rotation with a degenerate bare pointer reaches an orthogonal detector state with zero final bare-energy change and `A_Delta=pi hbar/2`.

### B4 — per-constituent action cap produces a conditional atom-count bound
**Status:** DERIVED / CONDITIONAL

```math
\boxed{
N
\ge
\left\lceil
\frac{\hbar\arcsin(1-2\epsilon)}{a_{\max}}
\right\rceil.
}
```

---

# 6. Exact one-photon + N-dipole model

### D1 — symmetric bright-state coupling scales as `sqrt(N)` for identical couplings
**Status:** KNOWN / DERIVED IN THE STATED TAVIS--CUMMINGS SECTOR

```math
\boxed{G=g\sqrt N.}
```

### D2 — matter-only trace distance equals excitation-transfer probability in this model
**Status:** DERIVED / CONDITIONAL

```math
\boxed{
\mathcal D_D(t)=\sin^2(g\sqrt Nt).
}
```

### D3 — exact transient atom-count law
**Status:** DERIVED / CONDITIONAL

```math
\boxed{
N_{\min}
=
\left\lceil
\frac{[\arcsin\sqrt{1-2\epsilon}]^2}{g^2\tau^2}
\right\rceil.
}
```

Perfect transfer gives `N_min = ceil[(pi/(2g tau))^2]`.

### D4 — single-emitter coupling can be written in dipole/mode-volume form
**Status:** KNOWN / CONDITIONAL NORMALIZATION

```math
\boxed{
g
=|\mathbf d\cdot\mathbf e|
\sqrt{\frac{\omega}{2\hbar\epsilon_0V_{\rm eff}}}.}
```

---

# 7. Initial-in-mode coherent capture -> persistent record

### R1 — exact record probability
**Status:** DERIVED / CHECKED NUMERICALLY

```math
\boxed{
P_R
=
\frac{4G^2\Gamma}
{(\kappa+\gamma+\Gamma)
[4G^2+\kappa(\gamma+\Gamma)]}.
}
```

Direct numerical integration matched the analytic result at about `1e-11` absolute level for tested parameter sets.

### R2 — record-trapping rate has a finite optimum
**Status:** DERIVED / CHECKED

```math
\boxed{
\Gamma_{\rm opt}
=
\sqrt{
\frac{(\kappa+\gamma)(4G^2+\kappa\gamma)}{\kappa}
}.
}
```

For `gamma=0`, `Gamma_opt=2G`.

### R3 — optimized persistent-record probability
**Status:** DERIVED

```math
\boxed{
P_{R,\max}
=
\frac{4G^2}
{[\sqrt{\kappa(\kappa+\gamma)}+\sqrt{4G^2+\kappa\gamma}]^2}.
}
```

### R4 — loss-constrained atom-count law
**Status:** DERIVED / CONDITIONAL

For `gamma=0`, optimized trapping, no dark records, and a perfectly distinguishable record state,

```math
N
\ge
\left[
\frac{\kappa}{2g}
\frac{\sqrt{1-2\epsilon}}
{1-\sqrt{1-2\epsilon}}
\right]^2.
```

### R5 — acquisition and record formation form a rate-matching problem
**Status:** DERIVED ORGANIZING STATEMENT

The internal-mode model is controlled by ratios such as `g sqrt(N)/kappa`, `g sqrt(N)/gamma`, and `Gamma/(g sqrt(N))`.

---

# 8. Traveling-wave external capture

### X1 — exact spectral record-conversion kernel
**Status:** DERIVED / CONDITIONAL

For one input/output optical port plus parasitic optical loss,

```math
\boxed{
\eta_R(\delta)
=
\frac{\kappa_{\rm in}\Gamma G^2}
{\left|
\left(\frac{\kappa}{2}-i\delta_c\right)
\left(\frac{\gamma+\Gamma}{2}-i\delta_m\right)
+G^2
\right|^2}.
}
```

### X2 — resonant narrowband conversion factorizes into optical matching and record branching
**Status:** DERIVED

Define

```math
\kappa_m=4G^2/(\gamma+\Gamma),
\qquad
\beta_R=\Gamma/(\gamma+\Gamma).
```

Then

```math
\boxed{
\eta_R(0)
=
\beta_R
\frac{4\kappa_{\rm in}\kappa_m}
{(\kappa+\kappa_m)^2}.
}
```

### X3 — clean one-port perfect capture occurs at critical matching
**Status:** DERIVED / CONDITIONAL

For `kappa_loss=gamma=0`,

```math
\boxed{
\Gamma_{\rm match}=4G^2/\kappa.
}
```

At resonance, `r=0` and `eta_R=1`.

### X4 — peak narrowband efficiency alone gives no positive `N_min` in the clean one-port model
**Status:** DERIVED COUNTEREXAMPLE

Any nonzero `G` can satisfy the matching condition if correspondingly small bandwidth / slow record formation is allowed.

### X5 — optimized external efficiency has escape and cooperativity ceilings
**Status:** DERIVED

```math
\boxed{
\Gamma_{\rm opt}
=\gamma+\frac{4G^2}{\kappa}
}
```

and

```math
\boxed{
\eta_{R,\max}(0)
=\eta_{\rm esc}\frac{C_N}{1+C_N},
}
```

where

```math
\eta_{\rm esc}=\kappa_{\rm in}/\kappa,
\qquad
C_N=4G^2/(\kappa\gamma).
```

The cooperativity structure is established cavity-QED physics.

### X6 — cooperativity-based constrained atom-count law
**Status:** DERIVED / CONDITIONAL

For `eta_req<eta_esc`,

```math
\boxed{
N
\ge
\frac{\kappa\gamma}{4g^2}
\frac{\eta_{\rm req}}
{\eta_{\rm esc}-\eta_{\rm req}}.
}
```

### X7 — finite bandwidth restores a threshold in the lossless matched case
**Status:** DERIVED / CONDITIONAL BAD-CAVITY BENCHMARK

For a Lorentzian incident spectrum of HWHM `B`,

```math
\boxed{
P_R=\frac{\Gamma}{\Gamma+B},
\qquad
\Gamma=4Ng^2/\kappa.
}
```

Thus target error `epsilon` requires

```math
\boxed{
N
\ge
\frac{\kappa B}{8g^2}
\frac{1-2\epsilon}{\epsilon}.
}
```

---

# 9. Mode-weighted coupling and optical depth

### M1 — unequal microscopic couplings reduce to one bright-state norm
**Status:** DERIVED / KNOWN STRUCTURE

```math
\boxed{
G^2=\sum_j|g_j|^2.
}
```

The directly coupled bright state is proportional to `sum_j g_j |e_j>`.

### M2 — effective atom number is mode weighted
**Status:** DERIVED ORGANIZING DEFINITION

```math
N_{\rm eff}
=\frac{1}{|g_{\rm ref}|^2}
\sum_j|g_j|^2.
```

This need not equal literal atom count.

### M3 — dilute single-pass absorber is controlled by optical depth
**Status:** KNOWN / CONDITIONAL

```math
\boxed{
\mathrm{OD}=n\sigma L
=\frac{N_{\rm col}\sigma}{A},
\qquad
P_{\rm abs}=1-e^{-\mathrm{OD}}.
}
```

### M4 — single-pass record target gives an optical-depth bound
**Status:** DERIVED / CONDITIONAL

For `P_R=eta_mode eta_rec(1-e^-OD)`,

```math
\boxed{
\mathrm{OD}
\ge
-\ln\left[
1-\frac{\eta_{\rm req}}
{\eta_{\rm mode}\eta_{\rm rec}}
\right].
}
```

In the ideal high-efficiency case, `OD_min=-ln(2 epsilon)`.

### M5 — architecture changes apparent atom-count scaling
**Status:** DERIVED ORGANIZING STATEMENT

Single-pass optical depth and resonant critical coupling can produce different `N`/bandwidth tradeoffs from the same microscopic absorber. No architecture-independent `N -> detector` map exists.

---

# 10. Semiconductor decision bridge

### S1 — minimal signal-record probability factorization
**Status:** CONDITIONAL ORGANIZING MODEL

```math
\boxed{
\eta_s
=\eta_{\rm mode}
(1-e^{-\alpha L})
\eta_{eh}
P_{\rm col}
P_{\rm read}.
}
```

### S2 — extraction/recombination race
**Status:** CONDITIONAL

```math
\boxed{
P_{\rm col}
=\frac{\Gamma_{\rm ext}}
{\Gamma_{\rm ext}+\Gamma_{\rm rec}}
=\frac{1}{1+\tau_{\rm ext}/\tau_{\rm rec}}.
}
```

### S3 — electron-hole generation is a transduction stage, not the complete detector boundary
**Status:** DERIVED ORGANIZING STATEMENT

The pair must survive subsequent loss, separation/collection, record, and decision stages.

### S4 — exact binary click distinguishability with independent Poisson dark events
**Status:** DERIVED / CONDITIONAL

With signal click probability `eta_s`, dark rate `R_d`, and window `tau`,

```math
\boxed{
\mathcal D_{\rm click}
=\eta_s e^{-R_d\tau}.
}
```

Hence

```math
\boxed{
P_e
=\frac12(1-\eta_s e^{-R_d\tau}).
}
```

### S5 — dark-event impossibility condition
**Status:** DERIVED / CONDITIONAL

Target `P_e<=epsilon` requires

```math
\boxed{
R_d\tau
\le
-\ln(1-2\epsilon).
}
```

For small `epsilon`, `R_d tau` is at most approximately `2 epsilon`.

No increase in absorption or atom count can overcome violation of this condition in the stated binary-click model.

### S6 — optical-depth requirement including downstream inefficiency and dark events
**Status:** DERIVED / CONDITIONAL

Define `eta_int=eta_eh P_col P_read`. If feasible,

```math
\boxed{
\alpha L
\ge
-\ln\left[
1-
\frac{(1-2\epsilon)e^{R_d\tau}}
{\eta_{\rm mode}\eta_{\rm int}}
\right].
}
```

If the required fraction is at least unity, arbitrarily large `alpha L` cannot meet the target.

---

# 11. Retention and reset remain separate

### T1 — activated bistable retention gives a conditional barrier bound
**Status:** DERIVED / CONDITIONAL

For `Gamma_d=nu_0 exp(-E_b/k_B T)`, a false-switch constraint over `tau_rec` gives

```math
E_b
\ge
k_BT
\ln\left[
\frac{\nu_0\tau_{\rm rec}}
{-\ln(1-p_d)}
\right].
```

### T2 — acquisition, retention, decision, and reset are distinct resource stages
**Status:** DERIVED ORGANIZING STATEMENT

```text
acquisition -> optical coupling / interaction action
competition -> optical/matter/recombination loss
retention   -> trapping/metastability
decision    -> signal distribution versus dark/noise distribution
reset       -> separate logical/thermodynamic recycling.
```

---

# 12. Current organizing statement

### G1 — the detector boundary is a multi-resource performance surface
**Status:** DERIVED ORGANIZING STATEMENT / PRIORITY UNASSESSED

Current useful coordinates include

```math
\eta_{\rm esc},
\quad
C_N,
\quad
\Gamma/(4G^2/\kappa),
\quad
B/(4G^2/\kappa),
\quad
\alpha L,
\quad
\Gamma_{\rm ext}/\Gamma_{\rm rec},
\quad
R_d\tau.
```

The detector is not a phase of matter reached at critical `N`; it is a performance region of the complete optical-matter-record-decision dynamics.

---

# 13. Open fronts

### O1 — continuous noisy electrical output
**Status:** OPEN / CURRENT FRONTIER

Replace the binary click record with current/voltage waveforms under Gaussian or colored noise. Derive optimum hypothesis discrimination, matched filtering, integration-time dependence, and bandwidth dependence.

### O2 — relation to conventional detector metrics
**Status:** OPEN

Map responsivity, noise PSD, NEP, `D*`, bandwidth, timing jitter, and integration time onto the same decision problem. Determine what information conventional metrics discard.

### O3 — finite-temperature / gain / dark-noise generalization
**Status:** OPEN

Include thermal initial mixtures, dark generation, gain statistics, avalanche excess noise, trapping, and reset.

### O4 — continuum semiconductor derivation from susceptibility
**Status:** OPEN

Bridge `sum |g_j|^2` to oscillator-strength density, susceptibility, `Im chi`, absorption coefficient, electron-hole generation, and transport without relying only on dilute independent-absorber intuition.

### O5 — architecture-independent lower bounds
**Status:** OPEN

Test whether any bound survives after optical topology, bandwidth/time, reservoirs, and record channels are included. Counterexamples remain mandatory.

### O6 — prior-art / terminology audit
**Status:** OPEN AND REQUIRED BEFORE NOVELTY LANGUAGE

Audit quantum photodetection, quantum speed limits, collective coupling, input-output/critical coupling, cavity cooperativity, single-photon absorption, optical depth, semiconductor collection, detector decision theory, and measurement thermodynamics.

---

# 14. Explicit non-claims

- **NON-CLAIM:** there is a universal critical number of atoms at which a photodetector appears.
- **NON-CLAIM:** total physical atom count is the relevant coupling resource in extended matter.
- **NON-CLAIM:** absorption is required for all photodetection.
- **NON-CLAIM:** electron-hole generation alone is a complete detection event.
- **NON-CLAIM:** decoherence by itself guarantees a useful detector.
- **NON-CLAIM:** every detection event costs `k_B T ln 2` at acquisition.
- **NON-CLAIM:** high monochromatic efficiency implies large oscillator count.
- **NON-CLAIM:** critical-coupling, cooperativity, optical-depth, trace-distance, Helstrom, quantum-speed-limit, or Tavis--Cummings structures are novel.
- **NON-CLAIM:** the current experiment has established a publishable new theorem.
