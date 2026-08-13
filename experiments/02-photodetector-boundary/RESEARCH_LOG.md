# Research Log — Experiment 02: The Photodetector Boundary

Chronological reasoning log. This file records **why the direction changed**, including terminology corrections, failed candidate boundaries, counterexamples, and the current surviving constrained results.

Detailed algebra is preserved in dedicated files; this log records the path.

---

## 2026-08-12 — Experiment opened

Starting question:

> At what point does a simple collection of atoms become a photodetector? If light is absorbed and re-emitted versus absorbed and a charge pair is generated, when does that happen and what is the boundary?

Initial intuitive chain:

```text
few atoms / atomic absorption
-> many atoms / semiconductor bands
-> electron-hole generation
-> photodetector.
```

This chain was treated as a hypothesis, not an assumption.

---

## Terminology split — re-emission is not the alternative to pair generation

Correction:

```text
absorption + later photon re-emission
```

is radiative excitation/relaxation. In a semiconductor, the absorbed photon can create an interband electron-hole excitation that may later recombine radiatively.

Therefore

```text
pair generation
```

and

```text
later photon re-emission
```

can be successive stages of one history.

**Direction change:** separate optical interaction from what makes the event a detector record.

---

## Single-atom counterexample — universal atom-count threshold killed

A single atom can absorb a photon and later return to its original state with no accessible record.

But a single atom can also be ionized:

```math
A+h\nu\rightarrow A^+ + e^-.
```

If the charge state or emitted electron is subsequently read, one atom can encode photon arrival.

**Conclusion:** no universal critical `N` defines photodetection without additional constraints.

**Direction change:** replace atom count with an operational hypothesis-discrimination criterion.

---

## Detector-state distinguishability introduced

Define

```math
H_0:\text{ no photon},
\qquad
H_1:\text{ one photon}.
```

For accessible matter states

```math
\rho_D^{(0)},\qquad\rho_D^{(1)},
```

define

```math
\mathcal D_D
=\frac12\|\rho_D^{(1)}-\rho_D^{(0)}\|_1.
```

For equal priors,

```math
P_{e,\min}
=\frac12(1-\mathcal D_D).
```

This changed the problem from

```text
Is the system a detector?
```

into

```text
How much photon/no-photon information is accessible in the chosen subsystem?
```

---

## Perfect absorber counterexample — absorption not sufficient

Set

```math
P_{\rm abs}=1
```

but suppose the accessible detector state has relaxed so that

```math
\rho_D^{(1)}=\rho_D^{(0)}.
```

Then

```math
\mathcal D_D=0.
```

**Conclusion:** perfect absorption need not leave a useful detector record.

---

## Dispersive counterexample — absorption not necessary

A surviving photon can conditionally rotate/change a matter pointer state:

```math
|1_\gamma\rangle|D_0\rangle
\rightarrow
|1_\gamma\rangle|D_1\rangle.
```

If `|D_0>` and `|D_1>` are distinguishable, the matter contains photon-presence information without photon destruction.

**Conclusion:** absorption is neither sufficient nor universally necessary for the operational detector definition.

No novelty claim was attached to this established measurement-theory idea.

---

## Atomic-to-band crossover separated from detector boundary

For `N` coupled states spread over width `W`, a rough spacing is

```math
\Delta E\sim W/N.
```

Large `N` can make a band/quasi-continuum description useful when spacing is below linewidth/disorder/thermal/measurement scales.

**Conclusion:** "when do atoms become a solid/band?" and "when does matter become a detector?" are distinct questions.

---

## Exciton / mobile-carrier boundary separated

Interband absorption does not guarantee independently mobile carriers. Binding, screening, temperature, fields, interfaces, and scattering determine whether a bound excitation dissociates.

**Conclusion:** bound-to-mobile charge conversion is another physical crossover, not the universal detector boundary.

---

## Pair generation not sufficient — collection race

Minimal illustrative model:

```math
P_{\rm col}
=\frac{\Gamma_{\rm col}}
{\Gamma_{\rm col}+\Gamma_r+\Gamma_{nr}}.
```

Even after a photon creates carriers, recombination or trapping can prevent a readable electrical event.

**Conclusion:**

```text
absorption
!= carrier generation
!= collection
!= readable detector event.
```

---

## Gain reinterpreted

Initial intuition:

```text
1 photon -> 1 electron -> 10^6 electrons -> more information.
```

Corrected interpretation:

```text
photon-conditioned microscopic distinction
-> gain/transduction
-> larger separation relative to downstream noise
-> easier practical readout.
```

**Conclusion:** gain stabilizes/enlarges accessible signal but does not manufacture photon information that was absent upstream.

---

## Irreversibility moved from axiom to open-system question

A closed photon + detector + environment description can remain unitary. Local irreversibility can emerge because information disperses into inaccessible correlations and a pointer-like state becomes metastable.

**Conclusion:** "irreversible" is not a primitive atom-count criterion.

**Direction change:** separate momentary information encoding from persistent record formation.

---

## Retention introduced explicitly

A microscopic detector state may satisfy

```math
\mathcal D_D(t)>0
```

for a short time and then relax back toward

```math
\mathcal D_D(t)=0.
```

A practical record may require

```math
\mathcal D_D(t)\ge\mathcal D_{\min}
\quad
0<t\le\tau_{\rm rec}.
```

**Conclusion:** information acquisition and retention are separate resources.

---

## Candidate universal deposited-energy bound attacked — failed

A tempting next claim was that creating a detector record must leave a nonzero final detector-energy change.

Counterexample: choose a degenerate pointer

```math
H_D=0
```

and photon-conditioned rotation

```math
V=(\hbar\Omega/2)\sigma_y.
```

At

```math
\Omega\tau=\pi,
```

the detector rotates from `|0>` to orthogonal `|1>` while

```math
\Delta\langle H_D\rangle=0.
```

**Failure reason:** state distinguishability is not equivalent to final energy separation.

**Direction change:** identify what resource the counterexample did use.

---

## Interaction action survives

For

```math
H_0=H_D,
\qquad
H_1=H_D+V,
```

remove common detector evolution and let `V_I(t)` generate the relative branch.

Pure-state geometry gives

```math
\theta(\tau)
\le
\frac{1}{\hbar}
\int_0^\tau\Delta V_I(t)dt.
```

Since target equal-prior error `epsilon` requires

```math
\theta\ge\arcsin(1-2\epsilon),
```

one obtains

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

The degenerate qubit counterexample exactly saturates this value.

**Conclusion:** the failed energy bound was not resource-free; it used finite differential Hamiltonian action.

**Important boundary:** this is established quantum-speed-limit geometry specialized to the detector question, not a new theorem claim.

---

## Original atom-count question recovered conditionally

Let

```math
V_I(t)=\sum_{j=1}^{N}v_j(t)
```

and bound each constituent's available action by `a_max`.

Then

```math
\boxed{
N
\ge
\left\lceil
\frac{\hbar\arcsin(1-2\epsilon)}{a_{\max}}
\right\rceil.
}
```

**Conceptual reversal:** there is no magic atom count, but once microscopic coupling per constituent is bounded, a minimum atom count follows automatically.

This was the first clean recovery of the user's original intuition in constrained form.

Detailed derivation: `INTERACTION_ACTION_LOWER_BOUND.md`.

---

## One photon + N dipoles — microscopic specialization

Next, use the resonant Tavis--Cummings interaction

```math
H_I
=\hbar g\sum_{j=1}^{N}
(a\sigma_j^+ + a^\dagger\sigma_j^-).
```

In the one-excitation manifold, the photon couples only to the symmetric bright matter state

```math
|W_N\rangle
=\frac{1}{\sqrt N}\sum_j|g\cdots e_j\cdots g\rangle
```

with

```math
G=g\sqrt N.
```

Exact evolution gives

```math
|\Psi_1(t)\rangle
=
\cos(Gt)|1,G\rangle
-i\sin(Gt)|0,W_N\rangle.
```

Tracing out the optical mode yields

```math
\boxed{
\mathcal D_D(t)=\sin^2(g\sqrt Nt).
}
```

and

```math
\boxed{
P_{e,\min}(t)=\frac12\cos^2(g\sqrt Nt).
}
```

Therefore, on the first transfer lobe,

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

For perfect transient transfer,

```math
N_{\min}
=
\left\lceil
\left(\frac{\pi}{2g\tau}\right)^2
\right\rceil.
```

**New conceptual split:** more atoms can matter for at least two unrelated reasons:

```text
band formation / dense spectrum
versus
collective light-matter coupling.
```

The second requires no semiconductor band at all.

Detailed derivation: `N_DIPOLE_SINGLE_MODE_MODEL.md`.

---

## Microscopic coupling mapped to optical parameters

For an ideal aligned electric dipole,

```math
E_{\rm zpf}
=\sqrt{\frac{\hbar\omega}{2\epsilon_0V_{\rm eff}}},
```

```math
\boxed{
g
=|\mathbf d\cdot\mathbf e|
\sqrt{\frac{\omega}{2\hbar\epsilon_0V_{\rm eff}}}.}
```

Thus weak transition dipole, large mode volume, or short interaction time can force a large `N` even though no universal atom-count threshold exists.

**Direction change:** the abstract action bound can be translated into measurable photon-matter quantities.

---

## Coherent transfer still failed as a detector record

At the perfect transfer time,

```math
|1,G\rangle\rightarrow-i|0,W_N\rangle.
```

But if the coherent interaction remains, the excitation returns to the optical mode.

**Failure reason:** strong acquisition is not the same as persistence.

This provided a concrete realization of the earlier abstract acquisition/retention split.

**Direction change:** add the smallest possible long-lived record channel.

---

## Minimal lossy capture-to-record model

Use

```text
|P> : photon in optical mode
|M> : collective matter excitation
|R> : persistent record
```

with

```text
G      = g sqrt(N)
kappa  = optical-mode loss
gamma  = unwanted matter loss
Gamma  = desired M -> R trapping.
```

Effective amplitudes:

```math
\dot c_P
=-\frac{\kappa}{2}c_P-iGc_M,
```

```math
\dot c_M
=-\frac{\gamma+\Gamma}{2}c_M-iGc_P.
```

Record probability:

```math
P_R
=\Gamma\int_0^\infty|c_M(t)|^2dt.
```

Solving the integrated two-state problem gives

```math
\boxed{
P_R
=
\frac{4G^2\Gamma}
{(\kappa+\gamma+\Gamma)
[4G^2+\kappa(\gamma+\Gamma)]}.
}
```

The expression was independently tested against numerical integration for multiple parameter sets; tested absolute disagreement was about `1e-11` or smaller.

Detailed derivation: `COHERENT_CAPTURE_TO_RECORD.md`.

---

## "More irreversibility is always better" attacked — failed

The naive expectation was

```text
larger Gamma -> faster freezing -> better detector.
```

The exact expression contradicts this when `kappa>0`.

If `Gamma` is too small, the excitation returns/is lost before being trapped.

If `Gamma` is too large, coherent transfer into `|M>` is overdamped while the photon remains exposed to optical loss.

Maximization gives

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

**Conclusion:** irreversible record formation must be dynamically matched to information acquisition; it is not simply maximized.

This resembles established critical-coupling/overdamping/quantum-Zeno physics, so novelty is explicitly unclaimed pending direct prior-art audit.

---

## Maximum persistent-record probability

At optimal trapping,

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

Thus a persistent high-fidelity record requires collective acquisition to beat competing optical escape, not merely high absorptance or strong trapping.

---

## Loss-constrained atom-count law

For `gamma=0`, optimized trapping, no false records, and a perfectly distinguishable record state,

```math
\mathcal D_R=P_{R,\max}.
```

Target equal-prior error `epsilon` yields

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
N_{\min}
\sim
\left(\frac{\kappa}{2g\epsilon}\right)^2.
```

**Interpretation:** the original atom-count question has now become a quantitative rate-competition question.

---

## Current strongest organizing picture

The Gedanken path now reads

```text
few/many atoms
        |
        +-> spectral-density / band crossover
        |
        +-> total available light-matter coupling
                    |
                    v
            photon-conditioned state separation
                    |
              compete with loss
                    |
                    v
          rate-matched record trapping
                    |
                    v
             persistent readout
                    |
                    v
                  reset
```

Natural dimensionless coordinates are becoming

```math
\frac{g\sqrt N}{\kappa},
\qquad
\frac{g\sqrt N}{\gamma},
\qquad
\frac{\Gamma}{g\sqrt N}.
```

The detector boundary therefore looks increasingly like a **dynamical rate-ratio / impedance-matching problem**, not a static phase transition in matter.

---

## Current frontier — traveling photon rather than photon already in the mode

The latest model starts with the photon already inside the optical mode. That avoids the actual external capture problem.

Next model:

```text
traveling one-photon wavepacket
-> input coupling kappa_in
-> parasitic optical loss kappa_loss
-> collective matter coupling g sqrt(N)
-> record trapping Gamma
-> reflection/transmission/loss/record probabilities.
```

The next question is:

> Does near-unity conversion of an **incident** photon into a persistent record reduce to a precise impedance-matching or critical-coupling condition, and can that condition be written in cross section, optical depth, oscillator strength, mode volume, and bandwidth?

That is the current live frontier.
