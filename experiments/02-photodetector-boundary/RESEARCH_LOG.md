# Research Log — Experiment 02: The Photodetector Boundary

Chronological reasoning log. This file records **why the direction changed**, including corrected terminology, counterexamples, discarded definitions, and surviving constrained results.

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

## Constrained minimum-resource program introduced

The original question transformed from

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

Candidate resources included energy deposition, entropy production, back-action, metastable barrier height, controlled state-space dimension, bandwidth-time product, and reset work.

None was assumed to be universal.

Direction: try to kill candidate lower bounds with explicit counterexamples before building any theorem.

---

## First lower-bound attack — final/deposited energy killed

The first candidate was a universal positive energy cost associated directly with acquiring the photon record.

Construct a two-state detector pointer with degenerate bare Hamiltonian

```math
H_D=0.
```

Under the no-photon branch nothing happens. Under the photon branch use

```math
V=(\hbar\Omega/2)\sigma_y.
```

Starting from `|0>`, a pulse satisfying

```math
\Omega\tau=\pi
```

produces the orthogonal state `|1>`.

The detector branches are therefore perfectly distinguishable while

```math
\Delta\langle H_D\rangle=0.
```

Conclusion:

> target detector-state distinguishability does not by itself require a nonzero final bare-energy separation or a universal positive deposited-energy cost.

This does **not** imply a realistic detector has zero energetic overhead. The interaction Hamiltonian was nonzero during acquisition.

Direction: identify the resource used by the counterexample rather than discarding it.

---

## Interaction action survives the energy counterexample

Write the photon-conditioned branches as

```math
H_0(t)=H_D(t),
\qquad
H_1(t)=H_D(t)+V(t).
```

Remove the common evolution with

```math
W(t)=U_0^\dagger(t)U_1(t).
```

The relative branch state is generated by `V_I(t)`. Define

```math
\theta(t)
=
\arccos|\langle D^{(0)}(t)|D^{(1)}(t)\rangle|.
```

For pure detector branches,

```math
\mathcal D_D=\sin\theta.
```

Thus target error `epsilon` requires

```math
\theta\ge\arcsin(1-2\epsilon).
```

Established Fubini--Study / quantum-speed-limit geometry gives

```math
\theta(\tau)
\le
\frac{1}{\hbar}
\int_0^\tau\Delta V_I(t)dt.
```

Define

```math
\mathcal A_\Delta
=\int_0^\tau\Delta V_I(t)dt.
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
\mathcal A_\Delta\ge\pi\hbar/2.
}
```

The same degenerate qubit counterexample has

```math
\Delta V=\hbar\Omega/2
```

and at `Omega tau=pi`

```math
\mathcal A_\Delta=\pi\hbar/2,
```

so it exactly saturates the bound.

Conclusion:

> the energy counterexample does not make record acquisition resource-free. It replaces a failed deposited-energy bound with a finite **interaction-action** requirement.

Important scope correction: this is not a new speed-limit theorem. The new content of the Gedanken path is the detector-specific resource interpretation and what it does to the original atom-count question.

Direction: return to atom count with a physical per-atom interaction cap.

---

## Original atom-count question recovered conditionally

Let the differential photon-conditioned interaction decompose into local terms:

```math
V_I(t)=\sum_{j=1}^{N}v_j(t).
```

For each term define half its spectral range

```math
g_j(t)
=
\frac{\lambda_{\max}[v_j(t)]-\lambda_{\min}[v_j(t)]}{2}.
```

Since the state-dependent uncertainty is bounded by the available spectral range, define

```math
a_j=\int_0^\tau g_j(t)dt.
```

The required action then implies

```math
\boxed{
\sum_{j=1}^{N}a_j
\ge
\hbar\arcsin(1-2\epsilon).
}
```

If every constituent is bounded by

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

For perfect discrimination this becomes

```math
N
\ge
\left\lceil
\frac{\pi\hbar}{2a_{\max}}
\right\rceil.
```

This is the first clean atom-count threshold recovered by the experiment.

But its meaning is the opposite of the original naive intuition:

> there is no magic `N` at which matter becomes a detector; `N_min` emerges only after the strength/time action available from each microscopic constituent is bounded.

One strongly coupled atom and many weakly coupled atoms can lie on the same total-action contour.

Direction: determine whether `a_max` can be replaced by measurable optical quantities rather than left as an abstract Hamiltonian constraint.

---

## Retention barrier separated from acquisition action

The action bound creates distinguishability but does not keep the record alive.

For a thermally activated bistable pointer,

```math
\Gamma_d=\nu_0e^{-E_b/k_BT}.
```

Over retention interval `tau_rec`,

```math
p_d=1-e^{-\Gamma_d\tau_{\rm rec}}.
```

Demanding `p_d<=p_d,max` yields

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

For small `p_d`, the requirement is approximately

```math
E_b
\gtrsim
k_BT\ln(\nu_0\tau_{\rm rec}/p_d).
```

Conclusion:

> acquisition and retention have different natural resources: interaction action versus stability against unwanted evolution.

The Arrhenius barrier expression is not universal; it is a model-specific example. Other architectures can gain stability through different mechanisms.

Direction: keep reset thermodynamics separate as a third stage.

---

## Acquisition–retention–reset decomposition

The current resource hierarchy is now

```text
ACQUISITION
create photon-conditioned state separation
-> constrained by interaction action in the current pure/unitary model

RETENTION
preserve that separation against dark/thermal/environmental dynamics
-> architecture-specific stability resource

RESET
return/recycle the memory state for another event
-> separate logical/thermodynamic accounting
```

This kills the tendency to compress all detector cost into one quantity called `energy per photon`.

Landauer-type reasoning belongs naturally in the reset/logical-irreversibility branch unless a specific detector architecture couples erasure directly into another stage.

Direction: specialize the abstract action bound to an actual photon--matter coupling model.

---

## Current frontier — one photon coupled to N dipoles

The strongest next question is now concrete:

```text
one photon
-> N identical two-level absorbers/dipoles
-> per-dipole coupling g
-> finite interaction or dwell time
-> collective state separation
-> target error epsilon
-> minimum N.
```

The goal is to determine whether the abstract interaction action can be rewritten in experimentally meaningful optical quantities such as

```text
dipole matrix element
oscillator strength
mode volume
cross section
optical depth
cooperativity
photon dwell time.
```

A successful reduction would connect the Gedanken experiment back to real photodetector physics.

A failure would also be informative: if the action bound merely collapses to a standard cooperativity or optical-depth requirement, that defines the prior-art boundary and prevents false novelty.

The next phase should therefore derive the simplest one-photon / `N`-dipole model before adding thermal/open-system complexity.
