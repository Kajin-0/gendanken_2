# Research Log — Experiment 02: The Photodetector Boundary

Chronological reasoning log. This file records **why the direction changed**, including failed boundaries, counterexamples, and corrected terminology.

---

## 2026-08-12 — Experiment opened

Starting question:

> At what point does a simple collection of atoms become a photodetector? If light is absorbed and re-emitted versus absorbed and a charge pair is generated, when does that happen and what is the boundary?

The rough initial picture was

```text
few atoms / atomic absorption
-> many atoms / semiconductor bands
-> electron-hole generation
-> photodetector.
```

The project did not assume this chain was correct.

---

## Terminology split — re-emission is not the alternative to pair generation

Absorption followed by later photon emission is radiative excitation/relaxation, not by itself the external photoelectric effect.

In a semiconductor, interband absorption can create an electron-hole excitation:

```math
h\nu+e^-_{\rm VB}
\rightarrow
e^-_{\rm CB}+h^+_{\rm VB}.
```

That excitation may later recombine radiatively:

```math
e^-+h^+\rightarrow h\nu'.
```

**Conclusion:** electron-hole generation and later photon re-emission can be stages of the same event.

Direction: separate optical absorption physics from what makes the event a detector record.

---

## Single-atom counterexample — universal atom-count threshold killed

A resonant photon can excite a single atom. If the excitation leaves no accessible lasting record, absorption alone does not establish detection.

But a single atom can in principle encode photon arrival through ionization or another readable state change.

**Conclusion:** there is no universal critical atom number without constraints on coupling, readout, persistence, and noise.

Direction: replace atom count with a discrimination criterion.

---

## Operational detector definition introduced

Define

```math
H_0:\text{ no photon},
\qquad
H_1:\text{ one photon}.
```

For an allowed material readout `Y`, require

```math
P(Y|H_1)\neq P(Y|H_0)
```

for any nonzero discriminating information.

At the quantum-state level, for accessible detector subsystem `D`,

```math
\rho_D^{(0)},\qquad\rho_D^{(1)},
```

with trace distance

```math
\mathcal D_D
=\frac12\|\rho_D^{(1)}-\rho_D^{(0)}\|_1.
```

For equal priors,

```math
P_{e,\min}
=\frac12(1-\mathcal D_D).
```

**Conclusion:** detection becomes a continuous hypothesis-discrimination problem rather than an ontological yes/no atom threshold.

Direction: attack absorption as necessary or sufficient.

---

## Perfect-absorber counterexample — absorption not sufficient

Construct an absorber with

```math
P_{\rm abs}=1
```

but identical accessible material states at interrogation:

```math
\rho_D^{(1)}=\rho_D^{(0)}.
```

Then

```math
\mathcal D_D=0.
```

**Conclusion:** perfect absorption does not imply photodetection under the operational definition.

---

## Dispersive counterexample — absorption not necessary

A photon can survive a dispersive interaction while changing a material pointer state:

```math
|1_\gamma\rangle|D_0\rangle
\rightarrow
|1_\gamma\rangle|D_1\rangle.
```

If the material states are distinguishable, the detector has acquired information without photon destruction.

**Conclusion:** photodetection is more general than absorption.

Direction: return to what increasing atom count actually changes.

---

## Atomic-to-band crossover separated from detector boundary

For many coupled states spread over characteristic width `W`, a rough spacing is

```math
\Delta E\sim W/N.
```

As `N` grows and the spacing becomes small relative to linewidth/disorder/thermal/measurement resolution, a band or quasi-continuum description becomes natural.

**Conclusion:** finite-spectrum -> band-like spectrum is a condensed-matter crossover, not the detector definition.

---

## Exciton/mobile-carrier boundary separated

An absorbed semiconductor photon can create an electron-hole excitation without guaranteeing immediately mobile charge.

Coulomb binding, temperature, electric field, interfaces, screening, and scattering determine whether the excitation remains bound or dissociates.

**Conclusion:** bound-excitation -> mobile-carrier conversion is another physical boundary, but still not the universal detector boundary.

---

## Pair generation not sufficient — collection race

In a minimal competing-rate model,

```math
P_{\rm col}
=\frac{\Gamma_{\rm col}}
{\Gamma_{\rm col}+\Gamma_r+\Gamma_{nr}}.
```

**Conclusion:**

```text
absorption
!= carrier generation
!= charge separation/collection
!= readable event.
```

Direction: distinguish information acquisition from amplification and retention.

---

## Amplification reinterpreted

The naive picture

```text
1 photon -> 1 electron -> 10^6 electrons -> more information
```

was corrected to

```text
1 photon
-> microscopic photon-conditioned distinction
-> gain/transduction
-> macroscopically separated output distributions
-> improved robustness against downstream readout noise.
```

**Conclusion:** gain stabilizes/enlarges an existing distinction; it does not manufacture photon-arrival information that was absent from its input.

---

## Irreversibility moved from axiom to open-system question

A naive detector story says absorption becomes detection when the process becomes irreversible.

That is too loose. Closed photon + detector + environment dynamics can remain unitary while local coherence becomes inaccessible and a pointer-like record emerges.

**Conclusion:** operational irreversibility must be tied to subsystem choice, information dispersal, metastability, and record persistence.

Direction: explicitly separate momentary encoding from persistent record.

---

## Momentary encoding versus retention

A microscopic state can have

```math
\mathcal D_D(t)>0
```

for a short interval and then relax so that the distinction disappears before any allowed readout.

A record requirement must therefore include time, e.g.

```math
\mathcal D_D(t)\ge\mathcal D_{\min}
\quad
0<t\le\tau_{\rm rec}.
```

**Conclusion:** acquisition and retention are separate resources.

Direction: attack candidate lower bounds.

---

## Energy-per-detection lower bound attacked — failed

Candidate conjecture:

> target detector distinguishability requires a nonzero final deposited energy.

Counterexample: a degenerate two-state pointer can be conditionally rotated into an orthogonal state while its final bare-energy change is zero.

Therefore final energy separation or deposited energy is not a universal detection resource.

However, finite-time pure-state separation still requires finite Hamiltonian action.

For relative generator `V_I(t)`, the state-space angle obeys

```math
\theta(\tau)
\le
\frac{1}{\hbar}
\int_0^\tau\Delta V_I(t)dt.
```

Target error `epsilon` therefore gives

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

The degenerate qubit example saturates the perfect-discrimination value.

**Conclusion:** final detector energy fails as a universal bound; interaction action survives in the stated finite-time pure/unitary model.

Detailed derivation: `INTERACTION_ACTION_LOWER_BOUND.md`.

---

## Original N question recovered conditionally

If the interaction is a sum of constituent terms and each constituent supplies at most action `a_max`, then

```math
N
\ge
\left\lceil
\frac{\hbar\arcsin(1-2\epsilon)}{a_{\max}}
\right\rceil.
```

**Conclusion:** a minimum atom number can emerge after the microscopic per-constituent resource is capped.

This is a constrained engineering/physics threshold, not an ontological material boundary.

Direction: replace the abstract local-action cap with an explicit optical interaction.

---

## Exact one-photon + N-dipole model

For identical resonant two-level dipoles in one mode,

```math
H_I
=\hbar g\sum_j(a\sigma_j^+ + a^\dagger\sigma_j^-).
```

The photon couples only to the symmetric bright `W_N` state with

```math
G=g\sqrt N.
```

Starting from one photon,

```math
\mathcal D_D(t)=\sin^2(g\sqrt Nt).
```

Thus on the first transfer lobe,

```math
N_{\min}
=
\left\lceil
\frac{[\arcsin\sqrt{1-2\epsilon}]^2}
{g^2\tau^2}
\right\rceil.
```

For perfect transient transfer,

```math
N_{\min}
=
\left\lceil
\left(\frac{\pi}{2g\tau}\right)^2
\right\rceil.
```

**Conclusion:** in this explicit coherent architecture, the atom threshold comes from collective optical matrix element and finite interaction time, not band formation.

Detailed derivation: `N_DIPOLE_SINGLE_MODE_MODEL.md`.

---

## Coherent transfer attacked as a detector record — failed

The matter excitation Rabi-oscillates back into the optical mode.

So even perfect transient transfer does not guarantee a persistent record.

**Conclusion:** coherent acquisition is not yet detection in the practical record sense.

Direction: add an irreversible record state and competing loss.

---

## Coherent capture -> persistent record model

Use

```text
|P> = photon in optical mode
|M> = collective matter excitation
|R> = persistent record
```

with

```text
G      = g sqrt(N)
kappa  = optical loss
gamma  = unwanted matter loss
Gamma  = desired M -> R trapping.
```

The exact long-time record probability is

```math
\boxed{
P_R
=
\frac{4G^2\Gamma}
{(\kappa+\gamma+\Gamma)
[4G^2+\kappa(\gamma+\Gamma)]}.
}
```

Direct numerical integration agreed with the analytic expression at about `1e-11` absolute level in tested cases.

Detailed derivation: `COHERENT_CAPTURE_TO_RECORD.md`.

---

## "More irreversibility is always better" attacked — failed

Naive expectation:

```text
larger Gamma -> faster freezing -> better detector.
```

The exact model contradicts this for `kappa>0`.

Too little trapping lets the excitation return or escape.

Too much trapping overdamps coherent transfer while the photon remains exposed to optical loss.

The optimum is

```math
\Gamma_{\rm opt}
=
\sqrt{
\frac{(\kappa+\gamma)(4G^2+\kappa\gamma)}{\kappa}
}.
```

For `gamma=0`,

```math
\Gamma_{\rm opt}=2G.
```

**Conclusion:** record formation must be dynamically rate matched.

Direction: remove the artificial assumption that the photon begins inside the optical mode.

---

## Traveling-wave photon capture introduced

Use one external input/output channel with coupling `kappa_in`, parasitic optical loss `kappa_loss`, collective matter coupling `G`, unwanted matter loss `gamma`, and record trapping `Gamma`.

For a spectral component, the exact record conversion kernel is

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

At resonance,

```math
\eta_R(0)
=
\frac{16\kappa_{\rm in}\Gamma G^2}
{[\kappa(\gamma+\Gamma)+4G^2]^2}.
```

Define

```math
\kappa_m=4G^2/(\gamma+\Gamma),
\qquad
\beta_R=\Gamma/(\gamma+\Gamma).
```

Then

```math
\eta_R(0)
=
\beta_R
\frac{4\kappa_{\rm in}\kappa_m}
{(\kappa+\kappa_m)^2}.
```

**Conclusion:** external detection factorizes naturally into optical matching and record branching.

Detailed derivation: `TRAVELING_WAVE_CAPTURE.md`.

---

## Peak-efficiency atom threshold attacked — failed

In the clean one-port limit,

```text
kappa_loss=0,
gamma=0,
```

critical matching occurs at

```math
\Gamma_{\rm match}=4G^2/\kappa.
```

Then

```math
r(0)=0,
\qquad
\eta_R(0)=1.
```

This holds for any nonzero `G` if arbitrarily slow/narrowband operation is permitted.

**Conclusion:** unit monochromatic efficiency does not impose a positive `N_min`; weak coupling is paid for in bandwidth/time.

This is a major counterexample to any atom-count bound built from peak efficiency alone.

Direction: identify the resource that restores a threshold.

---

## External-capture optimum -> collective cooperativity

For fixed `G`, `kappa`, and `gamma`, optimization over `Gamma` gives

```math
\Gamma_{\rm opt}
=\gamma+4G^2/\kappa.
```

The maximum resonant record probability is

```math
\eta_{R,\max}
=\frac{\kappa_{\rm in}}{\kappa}
\frac{4G^2}{4G^2+\kappa\gamma}.
```

Define

```math
\eta_{\rm esc}=\kappa_{\rm in}/\kappa,
```

and

```math
C_N=4G^2/(\kappa\gamma).
```

Then

```math
\eta_{R,\max}
=\eta_{\rm esc}\frac{C_N}{1+C_N}.
```

**Conclusion:** two independent ceilings appear:

```text
optical-access / parasitic-loss ceiling
and
collective-coupling / matter-loss ceiling.
```

No increase in atom number can overcome an optical-access ceiling without changing the architecture.

---

## Bandwidth restores a finite resource threshold

In the clean critically matched bad-cavity limit,

```math
\eta_R(\delta)
\simeq
\frac{\Gamma^2}{\delta^2+\Gamma^2},
\qquad
\Gamma=4Ng^2/\kappa.
```

For a Lorentzian incident photon spectrum of HWHM `B`,

```math
P_R=\frac{\Gamma}{\Gamma+B}.
```

Target error `epsilon` gives

```math
N
\ge
\frac{\kappa B}{8g^2}
\frac{1-2\epsilon}{\epsilon}.
```

**Conclusion:** weak coupling can preserve peak efficiency only by narrowing the detector's useful spectral/temporal acceptance.

The atom threshold has become a bandwidth/resource statement.

---

## Literal total atom count attacked — failed

For nonuniform microscopic couplings,

```math
G^2=\sum_j|g_j|^2.
```

The photon couples only to one bright superposition proportional to

```math
\sum_jg_j|e_j\rangle.
```

Atoms outside the optical mode, at field nodes, or poorly aligned with the field contribute little.

**Conclusion:** total physical atom count is not even the correct constrained microscopic coordinate.

A useful effective atom number is mode weighted.

Direction: take the continuum limit.

---

## Optical depth emerges in the traveling-wave continuum

For independent dilute absorbers,

```math
\mathrm{OD}=n\sigma L
=\frac{N_{\rm col}\sigma}{A},
```

with

```math
P_{\rm abs}=1-e^{-\mathrm{OD}}.
```

A minimal single-pass record model gives

```math
P_R
=\eta_{\rm mode}\eta_{\rm rec}
(1-e^{-\mathrm{OD}}).
```

Thus

```math
\mathrm{OD}_{\min}
=-\ln\left[
1-\frac{\eta_{\rm req}}
{\eta_{\rm mode}\eta_{\rm rec}}
\right].
```

In the ideal high-efficiency case,

```math
\mathrm{OD}_{\min}=-\ln(2\epsilon).
```

**Conclusion:** in extended matter the relevant variable is closer to column density / optical depth / oscillator-strength overlap than total `N`.

Detailed derivation: `MODE_WEIGHTED_OPTICAL_DEPTH.md`.

---

## Why single-pass and resonant detectors have different apparent N laws

Single-pass Beer-Lambert absorption gives one traversal.

A one-port matched resonator can build up the field and give weak matter repeated coherent interaction before escape.

Therefore

```text
single pass:
weak optical depth -> weak absorption;

matched resonator:
weak absorption per pass can -> unity narrowband capture.
```

The hidden cost is lifetime/bandwidth/detuning sensitivity.

**Conclusion:** detector architecture changes the projection of microscopic matter resources into apparent atom-count thresholds.

---

## Returned to the semiconductor question

For a minimal semiconductor slab, define

```math
\eta_s
=\eta_{\rm mode}
(1-e^{-\alpha L})
\eta_{eh}
P_{\rm col}
P_{\rm read}.
```

With independent extraction and recombination hazards,

```math
P_{\rm col}
=\frac{\Gamma_{\rm ext}}
{\Gamma_{\rm ext}+\Gamma_{\rm rec}}.
```

This gives a precise location for electron-hole generation:

```text
optical access
-> absorption
-> electron-hole excitation
-> survival/separation
-> persistent record
-> decision.
```

**Conclusion:** electron-hole generation is the semiconductor-specific transduction stage, not the detector boundary itself.

Detailed derivation: `SEMICONDUCTOR_DECISION_BRIDGE.md`.

---

## Dark-event decision boundary derived

Let dark clicks be an independent Poisson process of rate `R_d` over observation window `tau`.

No-photon click probability:

```math
p_0=1-e^{-R_d\tau}.
```

One-photon click probability:

```math
p_1
=1-(1-\eta_s)e^{-R_d\tau}.
```

For the binary output, the exact distribution distance is

```math
\boxed{
\mathcal D_{\rm click}
=\eta_s e^{-R_d\tau}.
}
```

Thus

```math
\boxed{
P_e
=\frac12(1-\eta_s e^{-R_d\tau}).
}
```

Target `P_e<=epsilon` requires

```math
\boxed{
R_d\tau
\le
-\ln(1-2\epsilon)
}
```

as a necessary condition because `eta_s<=1`.

For small `epsilon`,

```math
R_d\tau\lesssim2\epsilon.
```

**Conclusion:** no amount of absorption, atom number, or gain can overcome a dark-event budget that already destroys the required evidential contrast.

This is structurally analogous to the optical-access ceiling from the traveling-wave model.

---

## Current strongest organizing picture

The experiment now reads

```text
ATOMIC / MATERIAL CONSTITUTION
        |
        +-> spectral/band crossover
        |
        v
OPTICAL ACCESS / MODE OVERLAP
        |
        v
MODE-WEIGHTED OPTICAL RESOURCE
G^2 = sum |g_j|^2
or optical depth alpha L
        |
        v
MICROSCOPIC TRANSDUCTION
exciton / electron-hole / other excitation
        |
        v
DYNAMICAL COMPETITION
acquisition or extraction versus loss/recombination
        |
        v
RATE-MATCHED PERSISTENT RECORD
        |
        v
DECISION AGAINST DARK/READOUT NOISE
        |
        v
RESET / REUSE
```

Natural coordinates now include

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

The strongest answer to the original question is now:

> **A collection of atoms does not become a photodetector at a universal N. It enters a useful detector regime when the complete optical–matter–record–decision dynamics cross the required performance surface.**

Atom count survives only through mode-weighted coupling, optical depth, or other explicitly constrained physical resources.

---

## Current frontier — continuous noisy electrical output

The next attack is to replace binary click/no-click output with a continuous electrical waveform:

```text
H0 / H1
-> current or voltage waveform
-> Gaussian / colored noise
-> optimum likelihood-ratio / matched-filter statistic
-> integration time and bandwidth
-> responsivity / noise PSD / NEP / D*
-> determine what conventional metrics preserve or hide about detector distinguishability.
```

This is the strongest route back to practical photodetector figures of merit without allowing those conventional metrics to define the detector boundary by assumption.

A focused primary-source prior-art audit remains required before novelty language.
