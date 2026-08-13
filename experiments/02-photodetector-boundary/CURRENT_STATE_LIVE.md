# Current Live State — Experiment 02

**Date:** 2026-08-12  
**Status:** exploratory first-principles theory; first constrained lower-bound result  
**Priority:** unassessed; no novelty claim

This file is the current state pointer for Experiment 02. `RESEARCH_LOG.md` preserves chronology; `CLAIM_LEDGER.md` is the epistemic boundary. The detailed first lower-bound derivation is in `INTERACTION_ACTION_LOWER_BOUND.md`.

## 1. Current question

The experiment began with:

> At what point does a simple collection of atoms become a photodetector?

The current formulation separates that into different questions:

```text
A. When does a finite collection of atoms acquire band-like electronic structure?
B. When does an absorbed photon create a bound versus mobile excitation?
C. When does photon arrival become encoded in a material degree of freedom?
D. When does that microscopic encoding become a persistent, readable record?
E. When is that record useful against thermal, quantum, and readout noise?
```

Only C--E define the detector boundary in the present operational approach.

## 2. Minimal binary Gedanken experiment

Prepare the same material system repeatedly. The optical input is either vacuum or one photon:

```math
H_0: |0\rangle_\gamma,
\qquad
H_1: |1\rangle_\gamma.
```

Let the material begin in state `rho_D`. After the joint interaction `U`, trace out everything not granted to the detector observer. The accessible detector states are

```math
\rho_D^{(n)}
=
\operatorname{Tr}_{\overline D}
\left[
U( |n\rangle\langle n|\otimes\rho_D )U^\dagger
\right],
\qquad n\in\{0,1\}.
```

Here `D` is an explicitly chosen detector subsystem and `\overline D` contains outgoing optical modes, inaccessible material modes, environment, etc.

The central distinguishability is

```math
\boxed{
\mathcal D_D
=
\frac12
\left\|
\rho_D^{(1)}-\rho_D^{(0)}
\right\|_1.
}
```

For equal priors,

```math
\boxed{
P_{e,\min}
=
\frac12(1-\mathcal D_D).
}
```

Operational interpretation:

```text
D_D = 0  -> the chosen detector subsystem contains no accessible photon/no-photon distinction;
0 < D_D < 1 -> imperfect but nonzero discrimination is possible;
D_D = 1 -> perfect discrimination is possible in principle.
```

This definition forces the system boundary to be stated. A photon history can remain distinguishable in the environment even if the material subsystem has forgotten it.

## 3. Current strongest counterexample pair

### A. Perfect absorber, useless detector

Assume the material absorbs the photon but, at the time of interrogation, its accessible reduced state is identical for the two input hypotheses:

```math
\rho_D^{(1)}=\rho_D^{(0)}.
```

Then

```math
\mathcal D_D=0,
```

even if the optical absorption probability was unity.

This kills absorption as a sufficient definition of detection.

### B. Nonabsorbing interaction, useful detector

Suppose a photon survives a dispersive interaction while changing a material pointer state:

```math
|1\rangle_\gamma|D_0\rangle
\rightarrow
|1\rangle_\gamma|D_1\rangle.
```

If `|D_0>` and `|D_1>` are distinguishable, the material carries information about photon presence without requiring photon destruction.

This kills absorption as a necessary definition of detection.

Together:

```text
absorption is neither sufficient nor universally necessary for photodetection.
```

This is an organizing deduction, not a novelty claim.

## 4. Current hierarchy of boundaries

### Boundary 1 — finite spectrum to band-like spectrum

For `N` hybridized states spanning a characteristic width `W`, a rough level spacing is

```math
\Delta E\sim W/N.
```

A continuum/band description becomes useful when `Delta E` is small relative to the relevant linewidth, disorder, thermal scale, or measurement resolution. This is a crossover in description, not currently a detector criterion.

### Boundary 2 — bound excitation to mobile carriers

In a semiconductor, photon absorption may create an electron-hole excitation. Coulomb binding can form an exciton; thermal energy, electric field, interfaces, screening, or scattering can dissociate it.

The hydrogenic effective-mass scale is schematically

```math
E_B^*
\approx
13.6\,\mathrm{eV}
\frac{\mu_r}{\epsilon_r^2},
```

with effective Bohr radius

```math
a_B^*
\approx
a_0\frac{\epsilon_r}{\mu_r}.
```

These formulas are model dependent and are not a universal detector boundary.

### Boundary 3 — interaction to encoded information

Photon arrival becomes encoded in the chosen material subsystem when

```math
\mathcal D_D>0.
```

This is the present minimal detector criterion.

### Boundary 4 — encoded information to persistent record

Define a required retention interval `tau_rec`. A practical record must preserve sufficient distinguishability over that interval:

```math
\mathcal D_D(t)\ge \mathcal D_{\min}
\qquad
0<t\le\tau_{\rm rec}.
```

This introduces time explicitly. A transient microscopic distinction that disappears before any allowed readout may satisfy momentary encoding but fail as a useful record.

### Boundary 5 — record to usable detector

Real discrimination must include dark events, thermal fluctuations, readout noise, finite efficiency, timing constraints, and decision thresholds.

The useful boundary can therefore be parameterized by an error target rather than by atom count:

```math
P_e\le\epsilon.
```

Other architectures require asymmetric false-positive / false-negative costs rather than equal-prior Helstrom error.

## 5. Semiconductor specialization: rate competition

For a created excitation with independent effective rates

```math
\Gamma_{\rm col},\quad
\Gamma_r,\quad
\Gamma_{nr},
```

the simple competing-hazard collection probability is

```math
P_{\rm col}
=
\frac{\Gamma_{\rm col}}
{\Gamma_{\rm col}+\Gamma_r+\Gamma_{nr}}.
```

This illustrates why optical absorption and useful electrical detection are different resources.

It is **CONDITIONAL**: real detectors can have trapping, re-emission, gain, field-dependent transport, correlated pathways, nonlinear recombination, and multiple carrier species.

## 6. Amplification interpretation

Working distinction:

```text
interaction acquires/encodes information;
gain makes the encoded distinction robust to later noise and readout limitations.
```

A deterministic downstream channel cannot create information about the input variable that was absent from its input state. This is consistent with data-processing logic.

Gain can nevertheless greatly improve practical observability by mapping a microscopic distinction onto macroscopically separated output distributions.

## 7. Irreversibility / decoherence boundary

No fundamental nonunitary step is assumed for the closed photon + detector + environment system.

The current interpretation is:

```text
microscopic interaction
-> correlations spread into detector/environment degrees of freedom
-> local coherence becomes inaccessible
-> a metastable pointer-like record can emerge
-> downstream readout accesses that record.
```

The word "irreversible" is therefore operational unless a more specific open-system model is stated.

## 8. First lower-bound attack — deposited energy fails

A universal lower bound on **final detector energy change** does not follow from distinguishability alone.

A two-state pointer can have degenerate bare states,

```math
H_D=0,
```

while a photon-conditioned unitary rotates

```math
|0\rangle\rightarrow|1\rangle.
```

The two final detector states are orthogonal although

```math
\Delta\langle H_D\rangle=0.
```

Thus target discrimination does not by itself imply a nonzero final energy separation or a universal deposited/dissipated energy per detection event.

The interaction still requires a finite Hamiltonian action. This motivates the surviving bound below.

## 9. First surviving bound — interaction action

Restrict first to a pure detector state and conditional unitary evolution. Write

```math
H_0(t)=H_D(t),
\qquad
H_1(t)=H_D(t)+V(t).
```

After removing the common `H_D` evolution, the relative detector state is generated by `V_I(t)`.

Define the branch angle

```math
\theta
=
\arccos
\left|
\langle D^{(0)}|D^{(1)}\rangle
\right|.
```

For pure states,

```math
\mathcal D_D=\sin\theta.
```

Therefore `P_e<=epsilon` requires

```math
\theta\ge\arcsin(1-2\epsilon).
```

The pure-state geometric speed limit gives

```math
\theta(\tau)
\le
\frac{1}{\hbar}
\int_0^\tau
\Delta V_I(t)\,dt.
```

Define

```math
\mathcal A_\Delta
\equiv
\int_0^\tau \Delta V_I(t)dt.
```

Then

```math
\boxed{
\mathcal A_\Delta
\ge
\hbar\arcsin(1-2\epsilon).
}
```

For perfect discrimination,

```math
\boxed{
\mathcal A_\Delta\ge\frac{\pi\hbar}{2}.
}
```

A degenerate qubit pointer driven by

```math
V=(\hbar\Omega/2)\sigma_y,
\qquad
\Omega\tau=\pi
```

saturates the bound while its final bare-energy change remains zero.

**Interpretation:** distinguishability need not cost final-state energy separation, but finite-time branch separation requires finite differential interaction action in this model.

This result is a direct specialization of established quantum-state geometry / speed-limit physics, not a novelty claim.

## 10. Conditional atom-count bound recovered

Now impose the missing microscopic constraint that the original question lacked.

Let

```math
V_I(t)=\sum_{j=1}^{N}v_j(t)
```

and define each local term's half spectral range

```math
g_j(t)
=
\frac{\lambda_{\max}[v_j(t)]-\lambda_{\min}[v_j(t)]}{2}.
```

If

```math
a_j\equiv\int_0^\tau g_j(t)dt
```

is the maximum action supplied by atom/local degree `j`, then

```math
\boxed{
\sum_{j=1}^{N}a_j
\ge
\hbar\arcsin(1-2\epsilon).
}
```

If every local constituent satisfies

```math
a_j\le a_{\max},
```

then

```math
\boxed{
N
\ge
\left\lceil
\frac{\hbar\arcsin(1-2\epsilon)}{a_{\max}}
\right\rceil.
}
```

This is the first mathematically clean recovery of an atom-count threshold in the experiment.

Crucially, it is **conditional**, not ontological:

> atom count becomes a lower-bound coordinate only after the maximum photon-conditioned action available from each atom is bounded.

One strongly coupled atom can satisfy the requirement; many weakly coupled atoms can collectively satisfy the same action budget.

## 11. Acquisition and retention separate

The action bound constrains record **creation**, not record lifetime.

For an activated bistable pointer with

```math
\Gamma_d
=\nu_0e^{-E_b/k_BT},
```

requiring dark-switch probability `p_d` during `tau_rec` gives

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

For `p_d<<1`,

```math
E_b
\gtrsim
k_BT\ln(\nu_0\tau_{\rm rec}/p_d).
```

This is **CONDITIONAL** on activated Arrhenius escape. It is not a universal thermodynamic detector bound.

The emerging decomposition is therefore

```text
ACQUISITION -> interaction action
RETENTION   -> architecture-specific stability / dark-event suppression
RESET       -> separate logical/thermodynamic accounting
```

This is currently a stronger organizing structure than `energy per detected photon`.

## 12. Current deepest open problem

The immediate frontier has sharpened from a generic minimum-resource question to a microscopic optical-coupling test:

> **Can the interaction-action bound be rewritten in measurable photon--matter quantities such as dipole matrix element, oscillator strength, cross section, optical depth, mode volume, dwell time, or cooperativity?**

The natural next model is

```text
one photon
-> N identical two-level absorbers/dipoles
-> per-dipole coupling g
-> finite interaction/dwell time
-> collective state separation
-> target trace distance / error epsilon
-> conditional minimum N.
```

This should reveal whether the abstract action bound becomes a physically useful optical detector bound or collapses into a restatement of known coupling/cooperativity limits.

## 13. Immediate next steps

1. Solve the one-photon + `N` identical dipole model in the simplest single-mode / wavepacket geometry and express the action budget in `g tau`.
2. Compare independent versus collectively enhanced coupling and identify the physically permitted `N` scaling.
3. Replace abstract `g` with dipole matrix element / mode-volume quantities, then ask whether free-space cross-section or optical-depth constraints produce a more experimental form.
4. Generalize the acquisition bound to mixed detector states and open-system dynamics using Bures-angle / generator speed limits.
5. Keep retention and reset separate; do not fold Arrhenius or Landauer costs into the acquisition theorem.
6. Perform the focused prior-art audit before any novelty language.

## 14. Current one-line result

> **There is no universal atom-count threshold for photodetection, but finite-time photon/no-photon discrimination requires finite interaction action; once per-atom interaction action is capped, an explicit minimum atom count follows.**

Status: **DERIVED CONDITIONAL RESULT / ESTABLISHED SPEED-LIMIT FOUNDATION / PRIORITY UNASSESSED.**
