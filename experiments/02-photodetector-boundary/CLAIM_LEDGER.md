# Claim Ledger — Experiment 02

**Updated:** 2026-08-12  
**Status:** exploratory photodetector-boundary Gedanken experiment  
**Priority:** unassessed; no novelty claim

This file is the epistemic boundary. `CURRENT_STATE_LIVE.md` is the operational front door; `RESEARCH_LOG.md` preserves chronology.

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
**Status:** NON-CLAIM / TARGET FOR ADVERSARIAL TESTING

Landauer-type reset costs cannot be imported automatically as a per-detection-event lower bound. The memory/reset cycle, logical operation, and resource accounting must be specified.

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

# 5. Open fronts

### O1 — minimum-resource record formation
**Status:** OPEN

Given `epsilon`, `tau_obs`, `tau_rec`, temperature, reset requirements, allowed optical disturbance, and a specified system boundary, determine whether any nontrivial lower bound exists on energy, entropy production, back-action, metastable barrier, controlled dimension, or another resource.

### O2 — finite-temperature false-event boundary
**Status:** OPEN

Introduce dark events and thermal fluctuations explicitly. Determine the minimal record separation required for target false-positive and false-negative rates.

### O3 — persistence versus reversibility
**Status:** OPEN

Quantify when a photon-conditioned microscopic state becomes a robust record rather than a transient coherent correlation.

### O4 — reset accounting
**Status:** OPEN

Separate energy/dissipation needed for interaction, amplification, retention, readout, and reset. Test whether candidate lower bounds attach to one stage rather than to "detection" generically.

### O5 — nondestructive measurement back-action
**Status:** OPEN

If photon absorption is forbidden, quantify what disturbance must remain in conjugate optical observables or other degrees of freedom for a specified amount of acquired information.

### O6 — atom-number scaling under explicit architecture constraints
**Status:** OPEN

A universal `N_c` is rejected, but a meaningful minimum `N` may emerge after fixing interaction strength, temperature, linewidth, retention time, readout access, and error target. This is a constrained engineering/physics question rather than an ontological threshold.

### O7 — mapping to real detector metrics
**Status:** OPEN

Connect the abstract decision variables to quantum efficiency, dark-count probability/rate, NEP, specific detectivity, timing jitter, dead time, gain, and bandwidth without assuming that any one conventional metric captures record distinguishability by itself.

### O8 — prior-art / terminology audit
**Status:** OPEN AND REQUIRED BEFORE NOVELTY LANGUAGE

Audit quantum measurement theory, photodetection theory, quantum nondemolition measurement, detector thermodynamics, metastable measurement records, and finite-system electronic-structure crossover literature.

---

# 6. Explicit non-claims

- **NON-CLAIM:** there is a universal critical number of atoms at which a photodetector appears.
- **NON-CLAIM:** absorption is required for all photodetection.
- **NON-CLAIM:** electron-hole generation alone is a complete detection event.
- **NON-CLAIM:** decoherence by itself guarantees a useful detector.
- **NON-CLAIM:** every detection event costs `k_B T ln 2`.
- **NON-CLAIM:** the trace-distance formulation is novel.
- **NON-CLAIM:** the current experiment has established a publishable new theorem.
