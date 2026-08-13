# Current Live State — Experiment 02

**Date:** 2026-08-12  
**Status:** exploratory first-principles theory; conceptual boundary formulation  
**Priority:** unassessed; no novelty claim

This file is the current state pointer for Experiment 02. `RESEARCH_LOG.md` preserves chronology; `CLAIM_LEDGER.md` is the epistemic boundary.

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

This is enough to kill absorption as a sufficient definition of detection.

### B. Nonabsorbing interaction, useful detector

Suppose a photon survives a dispersive interaction while changing a material pointer state:

```math
|1\rangle_\gamma|D_0\rangle
\rightarrow
|1\rangle_\gamma|D_1\rangle.
```

If `|D_0>` and `|D_1>` are distinguishable, the material carries information about photon presence without requiring photon destruction.

This is enough to kill absorption as a necessary definition of detection.

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

Gain can nevertheless greatly improve *practical* observability by mapping a microscopic distinction onto macroscopically separated output distributions.

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

## 8. Current deepest open problem

The strongest next attack is to impose explicit performance constraints:

```text
binary or photon-number input ensemble
allowed detector Hilbert space / architecture
operating temperature T
observation interval tau_obs
required retention tau_rec
false-positive / false-negative limits
target discrimination error epsilon
reset requirement and cycle time
allowed outgoing optical disturbance
```

Then ask:

> **What is the minimum physical resource required to generate and retain the required distinguishability?**

Candidate resources to test rather than assume include

```text
energy deposition / dissipation
entropy production
measurement back-action
pointer-state separation
metastable barrier height
number of controlled degrees of freedom
bandwidth-time resource
reset work
```

A universal lower bound may fail if the resource accounting is incomplete; counterexamples are expected and must be preserved.

## 9. Immediate next steps

1. Formalize the detector as a quantum channel from the optical hypothesis to an accessible material record and identify which statements follow purely from distinguishability/data processing.
2. Introduce finite temperature and dark-event statistics so the boundary becomes an explicit decision problem rather than `D>0` only.
3. Test candidate thermodynamic lower bounds adversarially, especially any naive `k_B T ln 2` per detected photon assertion.
4. Only after the abstract boundary is stable, map it back onto concrete semiconductor architectures: photoconductor, photovoltaic diode, APD/SPAD, bolometer, and nonabsorptive/dispersive detector.
5. Perform a focused prior-art audit before treating any formulation as a distinct research contribution.

## 10. Current one-line result

> **A photodetector is not a phase of matter reached at a critical atom count; operationally it is a physical system that maps an optical hypothesis into a sufficiently distinguishable, sufficiently persistent, accessible record.**

Status: **DERIVED ORGANIZING STATEMENT / PRIORITY UNASSESSED.**
