# Claim Ledger — Experiment 02

**Updated:** 2026-08-12  
**Status:** exploratory photodetector-boundary Gedanken experiment; microscopic acquisition and record-formation models derived  
**Priority:** unassessed; no novelty claim

This file is the epistemic boundary. `CURRENT_STATE_LIVE.md` is the operational front door; `RESEARCH_LOG.md` preserves chronology.

Detailed derivations:

- `INTERACTION_ACTION_LOWER_BOUND.md`
- `N_DIPOLE_SINGLE_MODE_MODEL.md`
- `COHERENT_CAPTURE_TO_RECORD.md`

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

One microscopic system can encode photon arrival; a macroscopic absorber can fail to retain any accessible record. Minimum `N` appears only after additional physical constraints are imposed.

### H4 — photon absorption is sufficient for photodetection
**Status:** INVALIDATED

If the accessible material states conditioned on photon/no-photon input are identical at interrogation, the material provides no discrimination even if absorption was unity.

### H5 — photon absorption is universally necessary for photodetection
**Status:** INVALIDATED

A dispersive/nondestructive interaction can correlate photon presence with distinguishable matter pointer states while the photon survives.

### H6 — creating an electron-hole pair is sufficient for an electrical detection event
**Status:** INVALIDATED GENERALIZATION

The excitation can recombine, remain bound, trap in an inaccessible state, or fail collection/readout.

### H7 — gain creates new information about whether the photon arrived
**Status:** INVALIDATED AS STATED

Hypothesis-independent downstream processing cannot create input-hypothesis information that was absent from its input. Gain can protect/enlarge a pre-existing distinction against later readout noise.

### H8 — microscopic irreversibility occurs at one definite detector atom count
**Status:** INVALIDATED / REFRAMED

Closed photon + detector + environment evolution may remain unitary. Operational irreversibility must be tied to subsystem choice, information dispersal, decoherence, metastability, and practical accessibility.

### H9 — every detected photon dissipates `k_B T ln 2` at acquisition
**Status:** INVALIDATED AS A UNIVERSAL ACQUISITION BOUND

Landauer-type cost belongs to logically irreversible operations such as erasure under stated thermodynamic conditions. Reset must be accounted separately unless an architecture explicitly couples it into acquisition.

### H10 — a nonzero final detector-energy change is necessary for distinguishability
**Status:** INVALIDATED

A degenerate two-state pointer can be conditionally rotated into an orthogonal state while `Delta <H_D> = 0`.

### H11 — target discrimination alone implies a universal positive deposited/dissipated energy per event
**Status:** INVALIDATED IN GENERAL

The degenerate-pointer counterexample gives perfect final detector-state distinguishability with zero final bare-energy separation. The interaction still requires finite Hamiltonian action during acquisition.

### H12 — atom count itself is the fundamental detector resource coordinate
**Status:** INVALIDATED / SUPERSEDED

Atom count is a derived constrained resource. Once per-constituent interaction strength/time is bounded, explicit `N_min` laws emerge.

### H13 — coherent photon-to-matter excitation transfer is by itself a persistent detector record
**Status:** INVALIDATED

In the lossless one-mode `N`-dipole model the excitation Rabi-oscillates back into the optical mode. Acquisition and retention are distinct.

### H14 — making the desired irreversible trapping rate arbitrarily large always improves detection
**Status:** INVALIDATED IN THE CURRENT LOSSY MODEL

When optical escape is present, overly fast trapping overdamps coherent photon-to-matter transfer. The exact record probability has a finite optimum trapping rate.

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

Information can leave matter and survive in outgoing radiation/environment. Any statement that the detector has retained or forgotten the photon requires an explicit system boundary.

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
-> distinguishable accessible state
-> persistent record
-> readout decision.
```

---

# 3. Crossovers kept separate from detector definition

### C1 — finite atomic spectra cross over continuously toward band-like descriptions
**Status:** KNOWN / QUALITATIVE

A rough scale is

```math
\Delta E\sim W/N.
```

Band language becomes useful when spacing is small relative to linewidth/disorder/thermal/measurement resolution. This is not the detector boundary.

### C2 — bound excitation versus mobile carriers is material/environment dependent
**Status:** KNOWN / CONDITIONAL MODEL

Wannier-Mott estimates such as

```math
E_B^*\approx13.6\,\mathrm{eV}\,\mu_r/\epsilon_r^2
```

and

```math
a_B^*\approx a_0\epsilon_r/\mu_r
```

organize one regime but do not define photodetection universally.

### C3 — collection may be represented by competing rates only in a minimal hazard model
**Status:** CONDITIONAL

```math
P_{\rm col}
=\frac{\Gamma_{\rm col}}
{\Gamma_{\rm col}+\Gamma_r+\Gamma_{nr}}.
```

Real devices may violate the independent-exponential assumptions.

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
\mathcal D_D=\sin\theta.
```

Thus

```math
\boxed{
\theta\ge\arcsin(1-2\epsilon).
}
```

### B2 — finite-time pure-state separation requires interaction action
**Status:** DERIVED FROM ESTABLISHED QUANTUM SPEED-LIMIT GEOMETRY / CONDITIONAL

For relative branch generator `V_I(t)`,

```math
\boxed{
\mathcal A_\Delta
\equiv
\int_0^\tau\Delta V_I(t)dt
\ge
\hbar\arcsin(1-2\epsilon).
}
```

Perfect discrimination requires

```math
\mathcal A_\Delta\ge\pi\hbar/2.
```

### B3 — degenerate qubit saturates the perfect-discrimination action bound
**Status:** CHECKED ANALYTICALLY

For

```math
H_D=0,
\qquad
V=(\hbar\Omega/2)\sigma_y,
\qquad
\Omega\tau=\pi,
```

the detector ends orthogonal with

```math
\Delta\langle H_D\rangle=0,
\qquad
\mathcal A_\Delta=\pi\hbar/2.
```

### B4 — per-constituent action cap produces a general conditional atom-count bound
**Status:** DERIVED / CONDITIONAL

If each local term supplies at most `a_max`,

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

### D1 — symmetric bright-state coupling scales as `sqrt(N)`
**Status:** KNOWN / DERIVED IN THE STATED TAVIS--CUMMINGS SECTOR

For

```math
H_I
=\hbar g\sum_j(a\sigma_j^+ + a^\dagger\sigma_j^-),
```

the one-photon state couples to the symmetric `W_N` matter state with

```math
\boxed{G=g\sqrt N.}
```

No novelty claim is attached to this collective enhancement.

### D2 — matter-only trace distance equals excitation-transfer probability in this model
**Status:** DERIVED / CONDITIONAL

Starting from one photon and all dipoles in the ground state,

```math
\boxed{
\mathcal D_D(t)=\sin^2(g\sqrt Nt).
}
```

This equality is model-specific and must not be generalized back to arbitrary absorption/detection.

### D3 — exact transient atom-count law
**Status:** DERIVED / CONDITIONAL

On the first transfer lobe,

```math
\boxed{
N_{\min}
=
\left\lceil
\frac{[\arcsin\sqrt{1-2\epsilon}]^2}
{g^2\tau^2}
\right\rceil.
}
```

For perfect transfer,

```math
N_{\min}
=
\left\lceil
\left(\frac{\pi}{2g\tau}\right)^2
\right\rceil.
```

Thus `N_min proportional to (g tau)^-2` in this architecture.

### D4 — single-emitter coupling can be written in dipole/mode-volume form
**Status:** KNOWN / CONDITIONAL NORMALIZATION

For an aligned ideal electric-dipole transition,

```math
\boxed{
g
=|\mathbf d\cdot\mathbf e|
\sqrt{\frac{\omega}{2\hbar\epsilon_0V_{\rm eff}}}.}
```

This maps the atom-count requirement onto transition dipole, optical confinement, frequency, and interaction time.

---

# 7. Coherent capture -> persistent record model

### R1 — exact record probability with optical loss, matter loss, and desired trapping
**Status:** DERIVED / CHECKED NUMERICALLY

Let

```text
G = g sqrt(N)
kappa = optical-mode population loss
gamma = unwanted matter-excitation population loss
Gamma = desired matter -> record trapping rate.
```

With the photon initially in the optical mode,

```math
\boxed{
P_R
=
\frac{4G^2\Gamma}
{(\kappa+\gamma+\Gamma)
[4G^2+\kappa(\gamma+\Gamma)]}.
}
```

Direct numerical integration of the amplitude equations matched the analytic expression at about `1e-11` absolute level for tested parameter sets.

### R2 — record-trapping rate has an exact finite optimum
**Status:** DERIVED / CHECKED

For `kappa>0`,

```math
\boxed{
\Gamma_{\rm opt}
=
\sqrt{
\frac{(\kappa+\gamma)(4G^2+\kappa\gamma)}{\kappa}
}.
}
```

For `gamma=0`,

```math
\boxed{\Gamma_{\rm opt}=2G.}
```

This is the explicit correction to the shortcut that arbitrarily strong irreversibility is always beneficial.

### R3 — optimized persistent-record probability
**Status:** DERIVED

```math
\boxed{
P_{R,\max}
=
\frac{4G^2}
{[\sqrt{\kappa(\kappa+\gamma)}
+\sqrt{4G^2+\kappa\gamma}]^2}.
}
```

For `gamma=0`,

```math
\boxed{
P_{R,\max}
=
\left(\frac{2G}{\kappa+2G}\right)^2.
}
```

### R4 — loss-constrained atom-count law at optimized trapping
**Status:** DERIVED / CONDITIONAL

For `gamma=0`, no dark records, and perfectly distinguishable `|R>`, target equal-prior error `epsilon` requires

```math
\boxed{
N
\ge
\left[
\frac{\kappa}{2g}
\frac{\sqrt{1-2\epsilon}}
{1-\sqrt{1-2\epsilon}}
\right]^2.
}
```

For `epsilon<<1`,

```math
\boxed{
N_{\min}
\sim
\left(\frac{\kappa}{2g\epsilon}\right)^2.
}
```

### R5 — acquisition and record formation are a rate-matching problem
**Status:** DERIVED ORGANIZING STATEMENT

The current model is controlled by ratios such as

```math
\frac{g\sqrt N}{\kappa},
\qquad
\frac{g\sqrt N}{\gamma},
\qquad
\frac{\Gamma}{g\sqrt N}.
```

This suggests the detector boundary is better represented as a dynamical phase/rate diagram than as a static atom-count transition.

---

# 8. Retention and reset remain separate

### T1 — activated bistable retention gives a conditional barrier bound
**Status:** DERIVED / CONDITIONAL

For

```math
\Gamma_d=\nu_0e^{-E_b/k_BT},
```

requiring false-switch probability `p_d` over `tau_rec` gives

```math
\boxed{
E_b
\ge
k_BT
\ln\left[
\frac{\nu_0\tau_{\rm rec}}
{-\ln(1-p_d)}
\right].
}
```

This is not universal beyond the Arrhenius pointer model.

### T2 — acquisition, retention, and reset are distinct resource stages
**Status:** DERIVED ORGANIZING STATEMENT

```text
acquisition -> interaction action / coherent coupling
competition -> loss versus state transfer
retention   -> trapping/metastability/dark-event suppression
reset       -> separate logical/thermodynamic recycling.
```

---

# 9. Open fronts

### O1 — traveling-wave photon capture / external quantum efficiency
**Status:** OPEN / CURRENT FRONTIER

Replace the initial-in-mode photon with an incident one-photon wavepacket and include input coupling, output/reflection/transmission, parasitic optical loss, collective matter coupling, and record trapping. Determine the actual impedance-matching condition for near-unity conversion into a persistent record.

### O2 — prior-art boundary for the finite trapping optimum
**Status:** OPEN AND REQUIRED

Audit critical coupling, impedance matching, quantum-Zeno/overdamped transfer, cavity-assisted absorption, quantum memories, and irreversible photon detection. The finite optimum is not to be called novel before this audit.

### O3 — mixed-state / finite-temperature acquisition
**Status:** OPEN

Generalize the pure/unitary action bound and microscopic models to thermal mixtures and open-system dynamics using appropriate Bures-angle/generator methods.

### O4 — many-body scaling beyond the symmetric bright state
**Status:** OPEN

Test inhomogeneous couplings, disorder, finite spatial phase, correlated/entangled initial matter states, dark states, and whether practical scaling can differ from `sqrt(N)`.

### O5 — nondestructive information-disturbance boundary
**Status:** OPEN

If absorption is forbidden, determine the disturbance/back-action necessary for specified acquired information.

### O6 — semiconductor specialization
**Status:** OPEN

Map the acquisition/loss/record framework onto interband absorption, excitons, carrier separation, trapping, photoconductive gain, photovoltaic collection, APD/SPAD avalanche, and bolometric response.

### O7 — mapping to conventional detector metrics
**Status:** OPEN

Connect the abstract discrimination/record probabilities to quantum efficiency, dark counts, NEP, `D*`, jitter, dead time, gain, and bandwidth.

### O8 — reset accounting
**Status:** OPEN

Determine when and where logically irreversible reset occurs and what thermodynamic cost attaches to it under a specified detector cycle.

---

# 10. Explicit non-claims

- **NON-CLAIM:** a universal critical atom count exists.
- **NON-CLAIM:** absorption is universally necessary or sufficient for photodetection.
- **NON-CLAIM:** electron-hole generation alone is a complete detection event.
- **NON-CLAIM:** every click costs `k_B T ln 2` during acquisition.
- **NON-CLAIM:** a nonzero final detector-energy change is required.
- **NON-CLAIM:** the interaction-action inequality is a new quantum speed-limit theorem.
- **NON-CLAIM:** `sqrt(N)` collective coupling is new.
- **NON-CLAIM:** `Gamma_opt=2G` is universal outside the stated clean model.
- **NON-CLAIM:** the finite trapping optimum is novel before a direct prior-art audit.
- **NON-CLAIM:** the current idealized models already describe a practical semiconductor detector.
- **NON-CLAIM:** Experiment 02 has yet established a submission-ready new theorem.
