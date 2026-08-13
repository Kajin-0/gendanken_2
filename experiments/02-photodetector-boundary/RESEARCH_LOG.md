# Research Log — Experiment 02: The Photodetector Boundary

Chronological reasoning log. This file records **why the direction changed**, including corrected terminology, counterexamples, and discarded definitions.

---

## 2026-08-12 — Experiment opened

Starting question:

> At what point does a simple collection of atoms become a photodetector? If light is absorbed and re-emitted versus absorbed and a charge pair is generated, when does that happen and what is the boundary?

The question was intentionally retained in its rough form because it contains several different physical transitions that are easy to conflate.

Initial candidate boundary:

```text
few atoms / atomic absorption
-> many atoms / semiconductor bands
-> electron-hole generation
-> photodetector.
```

The project did not assume that this chain was correct.

---

## Terminology split — re-emission is not the alternative to pair generation

First correction:

```text
absorption + later photon re-emission
```

is radiative excitation/relaxation, not by itself the external photoelectric effect.

In a semiconductor, the absorbed photon can itself create an interband electron-hole excitation:

```math
h\nu + e^-_{\rm VB}
\rightarrow
 e^-_{\rm CB}+h^+_{\rm VB}.
```

That excitation may later recombine radiatively:

```math
e^-+h^+\rightarrow h\nu'.
```

Conclusion:

> electron-hole generation and later photon re-emission are not mutually exclusive branches. They can be successive stages of the same event.

Direction: separate **optical absorption physics** from **what makes an interaction a detection event**.

---

## Single-atom counterexample — universal atom-count threshold killed

Consider one atom.

A resonant photon may produce

```math
|g\rangle|1_\gamma\rangle
\rightarrow
|e\rangle|0_\gamma\rangle.
```

If the excitation simply reverses or radiatively relaxes and no accessible record remains, absorption alone does not establish useful detection.

But if the photon ionizes the atom,

```math
A+h\nu\rightarrow A^+ + e^-,
```

and the changed charge state or emitted electron is subsequently interrogated, a single atom can in principle encode photon arrival.

Conclusion:

> there is no universal critical atom number that defines photodetection without additional constraints on interaction, readout, persistence, and noise.

Direction: replace atom count with a hypothesis-discrimination criterion.

---

## Operational detector definition introduced

Define two optical hypotheses:

```math
H_0: \text{no photon},
\qquad
H_1: \text{one photon}.
```

Let `Y` be any allowed material readout.

Minimal classical criterion:

```math
P(Y|H_1)\neq P(Y|H_0).
```

Equivalently, photon arrival and material output carry nonzero statistical information.

This immediately separates

```text
interaction / absorption
```

from

```text
accessible evidence that the interaction occurred.
```

Direction: formulate the same question at the quantum-state level.

---

## Reduced-state distinguishability introduced

Let the accessible detector subsystem after the interaction be described by

```math
\rho_D^{(0)},\qquad\rho_D^{(1)}.
```

Define

```math
\mathcal D_D
=
\frac12\|\rho_D^{(1)}-\rho_D^{(0)}\|_1.
```

For equal priors, optimal binary discrimination gives

```math
P_{e,\min}
=
\frac12(1-\mathcal D_D).
```

This produces a continuous detector boundary rather than an ontological yes/no atom count:

```text
D_D = 0 -> no accessible distinction in subsystem D,
D_D > 0 -> some distinction,
D_D -> 1 -> increasingly ideal discrimination.
```

Important correction: the subsystem `D` must be specified. Information can leave the material and remain in the outgoing field or environment.

Direction: test whether absorption is either necessary or sufficient.

---

## Perfect-absorber counterexample — absorption not sufficient

Construct an idealized device with

```math
P_{\rm abs}=1
```

but whose accessible material state at interrogation is identical for the photon and no-photon histories:

```math
\rho_D^{(1)}=\rho_D^{(0)}.
```

Then

```math
\mathcal D_D=0.
```

The photon may have deposited energy and that information may have escaped into inaccessible environmental modes, but the chosen material subsystem is useless for discriminating the incident hypothesis.

Conclusion:

> perfect absorption does not imply perfect photodetection.

Direction: test whether absorption is necessary.

---

## Dispersive counterexample — absorption not necessary

Construct an interaction in which the photon survives but the detector pointer changes:

```math
|1_\gamma\rangle|D_0\rangle
\rightarrow
|1_\gamma\rangle|D_1\rangle.
```

If `|D_0>` and `|D_1>` are distinguishable, information about photon presence has transferred to matter even though the photon was not destroyed.

This is consistent with established nondestructive / quantum-nondemolition measurement concepts.

Conclusion:

> photodetection is more generally an information-transfer problem than an absorption problem.

No novelty claim was attached to this statement.

Direction: return to the original many-atom intuition and ask what atom count actually changes.

---

## Atomic-to-band crossover separated from detector boundary

For `N` coupled states spread over characteristic width `W`, use the rough scale

```math
\Delta E\sim W/N.
```

As `N` grows, the discrete spectrum becomes increasingly dense. When level spacing is much smaller than the relevant linewidth / disorder / thermal / measurement resolution,

```math
\Delta E\ll\Gamma_{\rm eff},
```

band or quasi-continuum language becomes operationally natural.

Conclusion:

> "when do atoms become a solid/band system?" is a finite-size condensed-matter crossover; it is not the same question as "when does matter become a detector?"

Direction: separate optical excitation from free-carrier production.

---

## Exciton / mobile-charge boundary separated

An absorbed semiconductor photon can create an electron-hole excitation without immediately guaranteeing independently mobile carriers.

Weakly bound Wannier-Mott exciton scales can be organized by

```math
E_B^*\approx13.6\,\mathrm{eV}\frac{\mu_r}{\epsilon_r^2},
\qquad
a_B^*\approx a_0\frac{\epsilon_r}{\mu_r}.
```

Temperature, fields, interfaces, screening, confinement, and scattering determine whether bound excitation survives or dissociates.

Conclusion:

> bound-excitation -> mobile-carrier conversion is another physical boundary, but not the universal definition of detection.

Direction: ask when mobile charge actually becomes a signal.

---

## Collection race — pair generation not sufficient

Minimal competing-rate model:

```math
\Gamma_{\rm tot}
=
\Gamma_{\rm col}+\Gamma_r+\Gamma_{nr},
```

with

```math
P_{\rm col}
=
\frac{\Gamma_{\rm col}}
{\Gamma_{\rm col}+\Gamma_r+\Gamma_{nr}}.
```

Thus even after absorption and carrier generation, the useful event can be lost to recombination or other pathways.

Conclusion:

```text
absorption
!= carrier generation
!= charge separation/collection
!= readable detector event.
```

Direction: distinguish microscopic information from macroscopic readout robustness.

---

## Amplification reinterpreted

Initial intuitive chain:

```text
1 photon -> 1 electron -> 10^6 electrons -> more information.
```

Corrected chain:

```text
1 photon
-> microscopic photon-conditioned distinction
-> gain / transduction
-> macroscopically separated output distributions
-> improved robustness against downstream noise and finite readout resolution.
```

A hypothesis-independent downstream channel cannot manufacture information about photon arrival that was absent from its input state.

Conclusion:

> amplification is best treated as information stabilization / accessible signal enlargement, not creation of the original photon-arrival information.

Direction: ask what makes the record persistent and effectively classical.

---

## Irreversibility moved from axiom to open-system question

A naive detector narrative says that absorption becomes detection when the microscopic process is "irreversible."

That wording is too loose.

For a closed photon + detector + environment system, microscopic evolution can remain unitary while correlations spread into an enormous number of degrees of freedom. The detector subsystem can then decohere and retain a metastable pointer-like record even though the global description is reversible in principle.

Conclusion:

> operational irreversibility must be tied to subsystem choice, inaccessible correlations, decoherence, and record persistence rather than asserted as a primitive atom-count threshold.

Direction: introduce an explicit retention requirement.

---

## Momentary encoding versus record formation

A microscopic state can satisfy

```math
\mathcal D_D(t)>0
```

for an arbitrarily short interval and then relax so that

```math
\mathcal D_D(t)\rightarrow0.
```

This suggests adding a record requirement such as

```math
\mathcal D_D(t)\ge\mathcal D_{\min}
\quad
0<t\le\tau_{\rm rec}.
```

Conclusion:

> information acquisition and information retention are separate detector resources.

Direction: include thermal false events and a target decision error.

---

## Current frontier — constrained minimum-resource record

The original question has now transformed from

```text
How many atoms make a photodetector?
```

into

```text
Given:
- an optical input ensemble,
- a defined accessible detector subsystem,
- temperature,
- observation and retention times,
- false-positive / false-negative requirements,
- allowed disturbance of the optical field,
- reset and cycle-time requirements,

what minimum physical resource is required to generate a sufficiently distinguishable and sufficiently persistent record?
```

Candidate resources include energy deposition, entropy production, back-action, metastable barrier height, controlled state-space dimension, bandwidth-time product, and reset work.

None is assumed to be universal.

The next phase should try to **kill candidate lower bounds with counterexamples before attempting to build a theorem**.
