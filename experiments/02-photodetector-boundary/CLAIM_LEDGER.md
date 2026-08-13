# Claim Ledger — Experiment 02

**Updated:** 2026-08-12  
**Status:** exploratory photodetector-boundary Gedanken experiment; first constrained lower-bound result  
**Priority:** unassessed; no novelty claim

This file is the epistemic boundary. `CURRENT_STATE_LIVE.md` is the operational front door; `RESEARCH_LOG.md` preserves chronology; `INTERACTION_ACTION_LOWER_BOUND.md` contains the detailed first resource-bound attack.

## Status vocabulary

- **KNOWN** — established result used as input; attribution may still need to be added.
- **DERIVED** — consequence of explicitly stated assumptions.
- **CHECKED** — independently or numerically verified.
- **CONDITIONAL** — valid only in the stated model or resource envelope.
- **CANDIDATE DISTINCT — PRIORITY UNPROVEN** — potentially unusual formulation; literature boundary incomplete.
- **INVALIDATED** — counterexample or correction kills the statement as posed.
- **SUPERSEDED** — replaced by a stronger or more precise formulation.
- **OPEN** — unresolved.
- **NON-CLAIM** — explicitly not asserted.

---

# 1. Permanent corrections / invalidated starting shortcuts

### H1 — absorption followed by re-emission is the photoelectric effect
**Status:** INVALIDATED TERMINOLOGY

Absorption followed by later photon emission is radiative excitation/relaxation. The external photoelectric effect ejects an electron; semiconductor interband absorption is commonly described as an internal photoelectric process.

### H2 — photon re-emission and electron-hole generation are mutually exclusive alternatives
**Status:** INVALIDATED

Interband absorption can create an electron-hole excitation, which may later recombine radiatively and emit a photon. These can be stages of one history.

### H3 — a universal critical atom count marks the onset of photodetection
**Status:** INVALIDATED AS A GENERAL DEFINITION

Detection can be defined operationally by distinguishability of photon-conditioned material states. A single microscopic system can encode a record, while a macroscopic absorber can fail to retain an accessible record. Atom count instead controls other crossovers such as spectral density and collective-state descriptions.

### H4 — photon absorption is sufficient for photodetection
**Status:** INVALIDATED

If the accessible material states under photon/no-photon hypotheses are identical at interrogation, the material provides no discrimination even if the photon was absorbed.

### H5 — photon absorption is universally necessary for photodetection
**Status:** INVALIDATED

Dispersive / nondestructive measurement provides the conceptual counterexample: the photon can survive while changing an accessible material pointer state.

### H6 — creating an electron-hole pair is sufficient for an electrical detection event
**Status:** INVALIDATED GENERALIZATION

The excitation can recombine, remain bound, become trapped, or otherwise fail to produce a readable electrical record.

### H7 — gain creates new information about whether the photon arrived
**Status:** INVALIDATED AS STATED

Downstream processing can stabilize or enlarge an encoded distinction but cannot create input-hypothesis information that was absent from its input. Gain is therefore separated from initial information acquisition.

### H8 — microscopic irreversibility must occur at one definite detector atom count
**Status:** INVALIDATED / REFRAMED

For a closed photon + detector + environment model, evolution can remain unitary. Operational irreversibility arises through information dispersal, decoherence, inaccessible correlations, and metastable record formation. No universal atom-count transition is assumed.

### H9 — every detected photon must dissipate `k_B T ln 2` at the moment of detection
**Status:** INVALIDATED AS A UNIVERSAL ACQUISITION BOUND / RETAINED AS RESET QUESTION

Landauer-type costs attach to logically irreversible operations such as erasure under stated thermodynamic conditions. A detection interaction can be modeled reversibly/unitarily, so `k_B T ln 2` cannot be imported as a universal acquisition cost per click. Reset remains a separate open accounting problem.

### H10 — a nonzero final detector energy change is necessary for distinguishability
**Status:** INVALIDATED

A degenerate two-state pointer with `H_D=0` can be conditionally rotated from `|0>` to the orthogonal state `|1>` while the final bare detector energy change remains zero.

### H11 — target discrimination alone implies a universal positive deposited/dissipated energy per event
**Status:** INVALIDATED IN GENERAL

The degenerate-pointer counterexample gives perfect detector-state distinguishability with zero final bare-energy separation. It still requires nonzero interaction Hamiltonian action during acquisition.

### H12 — atom count itself is the fundamental detector resource coordinate
**Status:** INVALIDATED / SUPERSEDED

A minimum `N` appears only after a microscopic per-constituent interaction cap is specified. Atom count is therefore a derived constrained resource count rather than the universal detector boundary.

---

# 2. Core operational statements

### I1 — detector-state distinguishability is a minimal operational detection criterion
**Status:** DERIVED FROM THE CHOSEN OPERATIONAL DEFINITION

For photon hypotheses `H0,H1`, let the accessible material states be `rho_D^(0),rho_D^(1)`. Define

```math
\mathcal D_D
=\frac12\|\rho_D^{(1)}-\rho_D^{(0)}\|_1.
```

If `D_D=0`, no measurement restricted to subsystem `D` can distinguish the hypotheses. If `D_D>0`, some discrimination is possible.

This is a definition of the present Gedanken boundary, not a claim that all communities define "photodetector" this way.

### I2 — equal-prior optimal binary error is fixed by trace distance
**Status:** KNOWN

```math
P_{e,\min}=\frac12(1-\mathcal D_D).
```

This is the Helstrom binary-state discrimination result. A primary-source/textbook citation should be added during the literature phase.

### I3 — perfect absorption does not imply detector distinguishability
**Status:** DERIVED

If

```math
P_{\rm abs}=1
```

but

```math
\rho_D^{(1)}=\rho_D^{(0)},
```

then `D_D=0`. Therefore absorption is not sufficient for the present operational definition.

### I4 — photon destruction is not necessary for detector distinguishability
**Status:** KNOWN / DERIVED COUNTEREXAMPLE

A dispersive interaction can preserve the photon while correlating photon presence with distinguishable detector states. Therefore absorption is not a necessary condition for the present operational definition.

### I5 — detector definition depends on the accessible subsystem
**Status:** DERIVED

The reduced state depends on what is traced out. Information can leave the material and remain in outgoing radiation or the environment. Any statement that a detector "forgot" a photon must specify the allowed measurement boundary.

### I6 — the useful detector boundary can be stated as a decision-performance target
**Status:** DERIVED ORGANIZING FORMULATION

Instead of atom number, impose a target such as

```math
P_e\le\epsilon
```

over a specified observation/retention interval and allowed measurement class.

Real detectors may require asymmetric false-alarm and miss probabilities rather than one equal-prior scalar error.

### I7 — persistence is a separate resource from momentary encoding
**Status:** DERIVED ORGANIZING FORMULATION

A material system can momentarily satisfy `D_D(t)>0` yet lose the distinction before any permitted readout. Define a retention target, e.g.

```math
\mathcal D_D(t)\ge\mathcal D_{\min}
\quad\text{for}\quad 0<t\le\tau_{\rm rec}.
```

The exact persistence metric remains architecture dependent.

### I8 — photodetector is a functional relation, not a phase-of-matter label
**Status:** DERIVED ORGANIZING STATEMENT / PRIORITY UNASSESSED

Current formulation:

```text
optical hypothesis
-> distinguishable accessible material state
-> sufficiently persistent record
-> readout decision.
```

This is not asserted to be novel terminology.

---

# 3. Condensed-matter crossovers kept separate from detection

### C1 — finite atomic systems cross over continuously toward band-like spectra
**Status:** KNOWN / QUALITATIVE

As coupled-state density increases, a band/quasi-continuum description becomes increasingly useful. A rough spacing estimate is

```math
\Delta E\sim W/N.
```

The criterion

```math
\Delta E\ll\Gamma_{\rm eff}
```

is a heuristic observational crossover, not a universal sharp finite-size theorem.

### C2 — exciton versus free-carrier behavior is material and environment dependent
**Status:** KNOWN / CONDITIONAL MODEL

Hydrogenic effective-mass estimates

```math
E_B^*\approx13.6\,\mathrm{eV}\,\mu_r/\epsilon_r^2,
\qquad
a_B^*\approx a_0\epsilon_r/\mu_r
```

can organize weakly bound Wannier-Mott excitons. They are not universal across all materials or confinement regimes.

### C3 — collection can be represented as competing effective hazards in a minimal model
**Status:** CONDITIONAL

If collection, radiative recombination, and nonradiative recombination are independent exponential hazards,

```math
P_{\rm col}
=\frac{\Gamma_{\rm col}}
{\Gamma_{\rm col}+\Gamma_r+\Gamma_{nr}}.
```

This is illustrative only; real detectors can violate the independent-rate assumptions.

---

# 4. Information / amplification statements

### A1 — downstream gain can improve practical discrimination without increasing fundamental input information
**Status:** KNOWN PRINCIPLE / WORKING INTERPRETATION

Under a hypothesis-independent downstream physical channel, distinguishability cannot increase beyond the information already present at its input in the unrestricted ideal-measurement sense. Practical electronics can nevertheless benefit enormously because gain protects the signal from later added noise and finite readout resolution.

A precise treatment should use trace-distance contractivity / data-processing inequalities and must include noise introduced by the gain mechanism.

### A2 — microscopic-to-macroscopic mapping is a record-stabilization problem
**Status:** DERIVED ORGANIZING STATEMENT

The current conceptual chain is

```text
microscopic correlation
-> pointer-state separation
-> metastability / decoherence
-> macroscopic accessible record.
```

No claim is made that this chain has one universal quantitative threshold.

---

# 5. First constrained lower-bound results

### B1 — pure-state discrimination target fixes a minimum branch angle
**Status:** DERIVED / KNOWN GEOMETRY

For pure detector branch states define

```math
\theta
=\arccos|\langle D^{(0)}|D^{(1)}\rangle|.
```

Since

```math
\mathcal D_D=\sin\theta,
```

the equal-prior error target `P_e<=epsilon` requires

```math
\boxed{
\theta\ge\arcsin(1-2\epsilon).
}
```

### B2 — finite-time pure-state branch separation requires interaction action
**Status:** DERIVED FROM ESTABLISHED QUANTUM SPEED-LIMIT GEOMETRY / CONDITIONAL

For

```math
H_0=H_D,
\qquad
H_1=H_D+V,
```

remove the common detector evolution and let `V_I(t)` generate the relative branch state. Then

```math
\theta(\tau)
\le
\frac{1}{\hbar}
\int_0^\tau\Delta V_I(t)dt.
```

Therefore

```math
\boxed{
\mathcal A_\Delta
\equiv
\int_0^\tau\Delta V_I(t)dt
\ge
\hbar\arcsin(1-2\epsilon).
}
```

For perfect discrimination,

```math
\boxed{
\mathcal A_\Delta\ge\pi\hbar/2.
}
```

This is not claimed as a new quantum speed-limit theorem. The Experiment-02 content is the detector-specific resource interpretation.

### B3 — degenerate conditional qubit saturates the perfect-discrimination action bound
**Status:** CHECKED ANALYTICALLY

For

```math
H_D=0,
\qquad
V=(\hbar\Omega/2)\sigma_y,
```

with initial `|0>` and pulse area `Omega tau=pi`, the photon branch ends in the orthogonal state `|1>`. Meanwhile

```math
\Delta\langle H_D\rangle=0
```

and

```math
\mathcal A_\Delta=\pi\hbar/2.
```

Thus the action bound is saturated while the final bare detector energy change vanishes.

### B4 — a per-constituent action cap induces an explicit minimum atom count
**Status:** DERIVED / CONDITIONAL

Let

```math
V_I(t)=\sum_{j=1}^{N}v_j(t),
```

and define

```math
g_j(t)
=\frac{\lambda_{\max}[v_j]-\lambda_{\min}[v_j]}{2},
\qquad
a_j=\int_0^\tau g_j(t)dt.
```

Then

```math
\sum_j a_j
\ge
\hbar\arcsin(1-2\epsilon).
```

If `a_j<=a_max` for every constituent,

```math
\boxed{
N
\ge
\left\lceil
\frac{\hbar\arcsin(1-2\epsilon)}{a_{\max}}
\right\rceil.
}
```

This is the first recovered atom-count threshold in the experiment, but it exists only after a per-atom physical coupling/action constraint is supplied.

### B5 — activated thermal retention produces a conditional barrier bound
**Status:** DERIVED / CONDITIONAL

For

```math
\Gamma_d=\nu_0e^{-E_b/k_BT},
```

and dark-switch probability over `tau_rec`

```math
p_d=1-e^{-\Gamma_d\tau_{\rm rec}},
```

requiring `p_d<=p_d,max` gives

```math
\boxed{
E_b
\ge
k_BT
\ln\left[
\frac{\nu_0\tau_{\rm rec}}
{-\ln(1-p_{d,\max})}
\right].
}
```

This is an Arrhenius bistable-pointer result, not a universal detector bound.

### B6 — acquisition, retention, and reset are distinct resource stages
**Status:** DERIVED ORGANIZING STATEMENT

Current decomposition:

```text
acquisition -> differential interaction action
retention   -> architecture-specific stability / dark-event suppression
reset       -> separate thermodynamic/logical cost
```

A single scalar `energy per detected photon` generally conflates these stages.

---

# 6. Open fronts

### O1 — microscopic optical realization of the action bound
**Status:** OPEN / CURRENT FRONTIER

For one photon interacting with `N` identical absorbers/dipoles, express the required action in physical optical quantities: coupling `g`, dwell time, dipole matrix element, oscillator strength, mode volume, cross section, optical depth, or cooperativity. Determine whether the result is useful or merely restates known strong-coupling/cooperativity conditions.

### O2 — finite-temperature false-event boundary beyond activated bistability
**Status:** OPEN

Introduce thermal initial mixtures and dark dynamics explicitly. Determine whether any architecture-independent stability coordinate survives beyond model-specific barriers/rates.

### O3 — persistence versus reversibility
**Status:** OPEN

Quantify when a photon-conditioned microscopic state becomes a robust record rather than a transient coherent correlation.

### O4 — reset accounting
**Status:** OPEN

Separate energy/dissipation needed for interaction, amplification, retention, readout, and reset. Test whether candidate lower bounds attach to one stage rather than to "detection" generically.

### O5 — nondestructive measurement back-action
**Status:** OPEN

If photon absorption is forbidden, quantify what disturbance must remain in conjugate optical observables or other degrees of freedom for a specified amount of acquired information.

### O6 — mixed-state / open-system acquisition bound
**Status:** OPEN

Generalize the pure conditional-unitary action result using Bures-angle / quantum-Fisher-information or generator-norm speed limits. Track which subsystem contains the acquired information.

### O7 — many-body scaling
**Status:** OPEN

Determine how independent, collective, correlated, and entangled matter states change achievable detector-state separation for fixed local interaction resources. Do not assume `sqrt(N)` or `N` enhancement without a specified Hamiltonian and state family.

### O8 — mapping to real detector metrics
**Status:** OPEN

Connect the abstract decision variables to quantum efficiency, dark-count probability/rate, NEP, specific detectivity, timing jitter, dead time, gain, and bandwidth without assuming that any one conventional metric captures record distinguishability by itself.

### O9 — prior-art / terminology audit
**Status:** OPEN AND REQUIRED BEFORE NOVELTY LANGUAGE

Audit quantum measurement theory, photodetection theory, quantum nondemolition measurement, detector thermodynamics, quantum speed limits, metastable measurement records, finite-system electronic-structure crossover literature, and optical cooperativity/absorption bounds.

---

# 7. Explicit non-claims

- **NON-CLAIM:** there is a universal critical number of atoms at which a photodetector appears.
- **NON-CLAIM:** absorption is required for all photodetection.
- **NON-CLAIM:** electron-hole generation alone is a complete detection event.
- **NON-CLAIM:** decoherence by itself guarantees a useful detector.
- **NON-CLAIM:** every detection event costs `k_B T ln 2` during acquisition.
- **NON-CLAIM:** a nonzero final detector energy change is required for detection.
- **NON-CLAIM:** the interaction-action inequality is a new quantum speed-limit theorem.
- **NON-CLAIM:** the current conditional atom-count bound is universal across unconstrained matter-light interactions.
- **NON-CLAIM:** the trace-distance formulation is novel.
- **NON-CLAIM:** the current experiment has established a publishable new theorem.
