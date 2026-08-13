# Research Log — Experiment 02: The Photodetector Boundary

Chronological reasoning log. This file records **why the direction changed**, including failed boundaries, counterexamples, and corrections. Detailed algebra is retained in dedicated derivation files.

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

The project did not assume this chain was correct.

---

## Re-emission versus pair generation — first correction

Interband absorption can create an electron-hole excitation which later recombines radiatively.

**Conclusion:** re-emission and electron-hole generation are not mutually exclusive alternatives; they can be stages of one history.

**Direction:** separate optical absorption physics from detector-record physics.

---

## Universal atom-count threshold attacked — failed

A single microscopic system can in principle encode photon arrival through excitation, ionization, or another readable state change.

A macroscopic absorber can absorb and then leave no accessible material record.

**Conclusion:** no universal `N_c` exists without specifying interaction, readout, persistence, and noise.

**Direction:** replace atom count with hypothesis discrimination.

---

## Operational detector definition introduced

For no-photon and one-photon hypotheses, define accessible detector states

```math
\rho_D^{(0)},\qquad\rho_D^{(1)}.
```

Use trace distance

```math
\mathcal D_D
=\frac12\|\rho_D^{(1)}-\rho_D^{(0)}\|_1.
```

For equal priors,

```math
P_{e,\min}=\frac12(1-\mathcal D_D).
```

**Conclusion:** detection becomes a quantitative distinguishability problem rather than a phase-of-matter label.

---

## Absorption as detector boundary attacked — failed twice

A perfect absorber can have

```math
\rho_D^{(1)}=\rho_D^{(0)},
```

so the accessible material contains no photon/no-photon evidence.

Conversely, a dispersive interaction can leave the photon intact while changing a material pointer state.

**Conclusion:** absorption is neither sufficient nor universally necessary for the operational detector definition.

---

## Atomic-to-band crossover separated

Increasing `N` can make the electronic spectrum increasingly dense and band-like.

**Conclusion:** finite-spectrum -> band-like spectrum is a condensed-matter crossover, not the detector boundary.

**Direction:** locate semiconductor electron-hole generation separately.

---

## Electron-hole generation separated from useful detection

An absorbed photon can create a bound or mobile excitation. In a minimal collection-race model,

```math
P_{\rm col}
=\frac{\Gamma_{\rm col}}
{\Gamma_{\rm col}+\Gamma_r+\Gamma_{nr}}.
```

**Conclusion:**

```text
absorption
!= pair generation
!= collection
!= readable record.
```

---

## Gain reinterpreted

Naive chain:

```text
1 photon -> 1 electron -> 10^6 electrons -> more information.
```

Corrected chain:

```text
microscopic photon-conditioned distinction
-> gain/transduction
-> larger practical output separation.
```

**Conclusion:** gain can stabilize/enlarge an existing distinction against later readout limitations; it cannot create missing upstream photon-arrival information under a hypothesis-independent downstream channel.

---

## Irreversibility moved from axiom to dynamical question

Closed photon + detector + environment evolution can remain unitary while local information becomes inaccessible and a metastable pointer record emerges.

**Conclusion:** operational irreversibility must be tied to subsystem choice, information dispersal, metastability, and accessibility.

**Direction:** explicitly separate momentary encoding from persistent record.

---

## Momentary encoding versus retention

A detector can satisfy `D_D(t)>0` only briefly and lose the distinction before any allowed readout.

**Conclusion:** acquisition and retention are independent detector resources.

---

## Universal deposited-energy lower bound attacked — failed

A degenerate two-state pointer can be conditionally rotated into an orthogonal state with zero final bare detector-energy difference.

Finite-time pure-state separation nevertheless requires interaction action:

```math
\mathcal A_\Delta
\ge
\hbar\arcsin(1-2\epsilon).
```

Perfect discrimination requires

```math
\mathcal A_\Delta\ge\pi\hbar/2.
```

**Conclusion:** final deposited energy is not universal; interaction action survives in the stated pure/unitary finite-time model.

Detailed derivation: `INTERACTION_ACTION_LOWER_BOUND.md`.

---

## Original N question recovered conditionally

If each constituent supplies at most interaction action `a_max`,

```math
N
\ge
\left\lceil
\frac{\hbar\arcsin(1-2\epsilon)}{a_{\max}}
\right\rceil.
```

**Conclusion:** a minimum atom count can emerge only after a microscopic resource cap is stated.

**Direction:** replace the abstract resource cap by an explicit optical model.

---

## Exact one-photon + N-dipole model

For identical resonant two-level dipoles,

```math
G=g\sqrt N.
```

The matter-only distinguishability is

```math
\mathcal D_D(t)=\sin^2(g\sqrt Nt).
```

Perfect transient first-lobe transfer requires

```math
N_{\min}
=\left\lceil(\pi/(2g\tau))^2\right\rceil.
```

**Conclusion:** a many-atom threshold can arise from collective coupling and finite time without band formation.

Detailed derivation: `N_DIPOLE_SINGLE_MODE_MODEL.md`.

---

## Coherent transfer as persistent detection attacked — failed

The matter excitation Rabi-oscillates back into the optical mode.

**Conclusion:** strong acquisition is not yet a persistent detector record.

**Direction:** add a long-lived record state and competing loss.

---

## Initial-in-mode coherent capture -> record

With collective coupling `G`, optical loss `kappa`, unwanted matter loss `gamma`, and desired trapping `Gamma`,

```math
P_R
=\frac{4G^2\Gamma}
{(\kappa+\gamma+\Gamma)[4G^2+\kappa(\gamma+\Gamma)]}.
```

The analytic expression was checked against direct numerical integration at about `1e-11` absolute agreement in tested cases.

Detailed derivation: `COHERENT_CAPTURE_TO_RECORD.md`.

---

## More irreversibility is always better — attacked and failed

The exact trapping optimum is

```math
\Gamma_{\rm opt}
=\sqrt{\frac{(\kappa+\gamma)(4G^2+\kappa\gamma)}{\kappa}}.
```

For `gamma=0`,

```math
\Gamma_{\rm opt}=2G.
```

Too little trapping fails to freeze the excitation; too much overdamps acquisition while optical escape remains available.

**Conclusion:** persistent record formation must be dynamically matched.

---

## Traveling-wave capture introduced

The photon was no longer placed inside the optical mode by assumption.

The frequency-resolved record kernel became

```math
\eta_R(\delta)
=\frac{\kappa_{\rm in}\Gamma G^2}
{|(\kappa/2-i\delta_c)((\gamma+\Gamma)/2-i\delta_m)+G^2|^2}.
```

**Conclusion:** external detection separates optical matching from matter-to-record branching.

Detailed derivation: `TRAVELING_WAVE_CAPTURE.md`.

---

## Peak-efficiency atom threshold attacked — failed

In the clean one-port limit,

```math
\Gamma_{\rm match}=4G^2/\kappa
```

gives zero resonant reflection and unit record conversion.

This works for any nonzero `G` if arbitrarily slow/narrowband operation is allowed.

**Conclusion:** unit monochromatic efficiency does not imply positive `N_min`.

**Hidden resource found:** bandwidth/time.

---

## Optical escape and collective cooperativity emerged as independent ceilings

Optimized external efficiency is

```math
\eta_{R,\max}
=\eta_{\rm esc}\frac{C_N}{1+C_N},
```

where

```math
\eta_{\rm esc}=\kappa_{\rm in}/\kappa,
\qquad
C_N=4G^2/(\kappa\gamma).
```

**Conclusion:** more atoms cannot repair an inaccessible optical port.

---

## Finite bandwidth restored a constrained N threshold

For a clean matched Lorentzian benchmark,

```math
P_R=\frac{\Gamma}{\Gamma+B},
\qquad
\Gamma=4Ng^2/\kappa.
```

Hence

```math
N
\ge
\frac{\kappa B}{8g^2}
\frac{1-2\epsilon}{\epsilon}.
```

**Conclusion:** weak coupling can preserve peak efficiency only by narrowing useful spectral/temporal acceptance.

---

## Literal total atom count attacked — failed

For nonuniform microscopic couplings,

```math
G^2=\sum_j|g_j|^2.
```

Only one bright superposition couples directly to the ideal optical mode.

**Conclusion:** the microscopic resource is mode-weighted oscillator strength, not literal total atom count.

Detailed derivation: `MODE_WEIGHTED_OPTICAL_DEPTH.md`.

---

## Continuum limit -> optical depth

For a dilute single-pass absorber,

```math
\mathrm{OD}=n\sigma L
=\frac{N_{\rm col}\sigma}{A},
```

and

```math
P_{\rm abs}=1-e^{-\mathrm{OD}}.
```

In the ideal high-efficiency single-pass limit,

```math
\mathrm{OD}_{\min}=-\ln(2\epsilon).
```

**Conclusion:** in extended matter, column density / optical depth is more meaningful than total atom count.

The contrast with resonant critical coupling showed that detector architecture trades absorber strength against optical dwell time/bandwidth.

---

## Returned to semiconductor electron-hole physics

For a minimal slab,

```math
\eta_s
=\eta_{\rm mode}
(1-e^{-\alpha L})
\eta_{eh}P_{\rm col}P_{\rm read},
```

with

```math
P_{\rm col}
=\frac{\Gamma_{\rm ext}}
{\Gamma_{\rm ext}+\Gamma_{\rm rec}}.
```

**Conclusion:** electron-hole generation is the semiconductor-specific transduction stage. It becomes useful detection only after survival/separation, record formation, and readout.

Detailed derivation: `SEMICONDUCTOR_DECISION_BRIDGE.md`.

---

## Dark-event decision boundary derived

For independent Poisson dark clicks of rate `R_d` over window `tau`,

```math
\mathcal D_{\rm click}
=\eta_s e^{-R_d\tau},
```

so

```math
P_e
=\frac12(1-\eta_s e^{-R_d\tau}).
```

A necessary target condition is

```math
R_d\tau\le-\ln(1-2\epsilon).
```

**Conclusion:** no amount of atom number, absorptance, or gain can overcome a dark-event budget that already destroys the needed evidential contrast.

---

## Continuous Gaussian electrical readout introduced

Binary click output was replaced by

```math
H_0:y(t)=n(t),
\qquad
H_1:y(t)=s(t)+n(t),
```

with common Gaussian covariance.

The decision coordinate is

```math
d^2
=\langle s,C^{-1}s\rangle
=\int\frac{|\tilde s(f)|^2}{S_n^{(2)}(f)}df,
```

and

```math
P_e=Q(d/2).
```

Input referring gives

```math
d^2
=\int\frac{|\tilde p(f)|^2}{\mathrm{NEP}_2^2(f)}df.
```

**Conclusion:** at the electrical-output level, detector performance for a task is the noise-weighted separation of the full photon/no-photon waveforms.

Detailed derivation: `CONTINUOUS_GAUSSIAN_DECISION.md`.

---

## Same D* -> same event performance attacked — failed

For a one-pole detector, white output noise, and a short optical energy `E`,

```math
d^2
=\frac{E^2}{\tau\,\mathrm{NEP}^2}
=\frac{E^2D^{*2}}{A\tau}.
```

Thus at equal area and equal low-frequency `D*`,

```math
d\propto\tau^{-1/2}.
```

**Conclusion:** equal scalar `D*` does not imply equal event-discrimination performance.

Finite decision deadlines make the slow-response penalty still stronger.

---

## Equal-covariance Gaussian noise attacked — generalized

Real photodetector noise can depend on the optical history.

For

```math
H_i:y\sim\mathcal N(\mu_i,C_i),
```

with `C_0 != C_1`, the optimum likelihood statistic is quadratic rather than a linear matched filter.

Even with

```math
\mu_0=\mu_1,
```

a covariance change can carry hypothesis information.

**Conclusion:** the detector output is fundamentally a conditional probability distribution, not merely a mean signal plus an external nuisance called noise.

Detailed derivation: `SIGNAL_DEPENDENT_NOISE.md`.

---

## Poisson count geometry exposed the limits of one SNR law

For

```math
K\sim\operatorname{Poisson}(\mu_i),
```

the likelihood ratio is

```math
\ell(K)
=K\ln(\mu_1/\mu_0)-(\mu_1-\mu_0).
```

The exact Bhattacharyya coefficient is

```math
BC
=\exp[-(\sqrt{\mu_1}-\sqrt{\mu_0})^2/2].
```

So the natural count-space separation is based on square-root rates.

In the weak-signal, finite-background limit this reduces to conventional shot-noise scaling.

In the zero-background limit,

```math
P_e=\frac12e^{-\lambda_sT}.
```

**Conclusion:** one fixed Gaussian SNR expression cannot describe both regimes.

---

## Unknown arrival time introduced

Known-time matched filtering silently assumes temporal alignment.

For unknown arrival time with prior `p(tau)`, the exact Gaussian likelihood becomes a mixture over shifted templates.

For `M` independent equal-norm candidate times,

```math
\Lambda(z)
=\frac1M\sum_{m=1}^M e^{dz_m-d^2/2}.
```

A max-threshold benchmark gives

```math
P_{\rm FA}=1-\Phi(\eta)^M,
```

```math
P_{\rm miss}=\Phi(\eta-d)\Phi(\eta)^{M-1}.
```

At fixed small false-alarm probability the threshold grows approximately as

```math
\sqrt{2\ln M}
```

up to extreme-value corrections.

Real shifted templates are correlated; `M_eff ~ T_search B_eff` is only a heuristic organizing estimate.

**Conclusion:** arrival-time uncertainty introduces a distinct temporal-search resource coordinate.

Detailed derivation: `UNKNOWN_ARRIVAL_TIME.md`.

---

## Faster is always better — narrowed

More bandwidth can increase known-time waveform distinguishability and sharpen temporal localization.

But with unknown arrival time it can also increase the number of effectively distinguishable search cells within a fixed window.

**Conclusion:** intrinsic speed is not a universally monotonic detector-quality coordinate once timing uncertainty and false alarms are included. The task must specify search window and timing model.

---

## Task-specific scalar constructed

For known-time Gaussian tasks, normalize an incident event as

```math
p(t)=Eq(t),
\qquad \int q(t)dt=1.
```

Define

```math
\mathcal K_D[q]
=\int\frac{|\tilde q(f)|^2}{\mathrm{NEP}_{2,D}^2(f)}df.
```

Then

```math
d^2=E^2\mathcal K_D[q],
```

and the equal-prior target energy is

```math
E_{\min}(q,\epsilon)
=\frac{2Q^{-1}(\epsilon)}{\sqrt{\mathcal K_D[q]}}.
```

**Conclusion:** a useful scalar exists once the waveform task and decision target are fixed, but it is not detector-only.

Detailed derivation: `TASK_SPECIFIC_DETECTIVITY.md`.

---

## Universal scalar detector ranking attacked — failed when kernels cross

Define the Gaussian spectral decision kernel

```math
W_D(f)=1/\mathrm{NEP}_{2,D}^2(f).
```

Then

```math
\mathcal K_D[q]
=\int|\tilde q(f)|^2W_D(f)df.
```

If

```math
W_A(f)\ge W_B(f)
```

for all allowed frequencies, A dominates B for every waveform in the task class.

But if `W_A-W_B` changes sign, choose one waveform concentrated where A is stronger and another where B is stronger. The ranking reverses.

**Conclusion:** no one-dimensional task-independent scalar ranking can preserve all Gaussian waveform tasks for crossing detector kernels.

The physically natural comparison is often a **partial order**, not a universal leaderboard.

This is an elementary functional-ordering consequence, not claimed new.

---

## Current strongest organizing picture

The experiment now reads

```text
material constitution
-> optical access / mode overlap
-> mode-weighted coupling or optical depth
-> microscopic excitation / electron-hole generation
-> acquisition/extraction versus loss/recombination
-> persistent record
-> complete conditional output statistics
-> nuisance parameters such as unknown timing
-> optimum likelihood decision
-> error probability
-> reset/reuse.
```

Every attempted universal scalar boundary has exposed a missing coordinate:

```text
atom count       -> interaction strength/time and mode overlap
peak efficiency  -> bandwidth
more atoms       -> optical escape ceiling
more absorber    -> downstream collection and dark events
fixed-noise SNR  -> signal-dependent distribution shape
D*               -> temporal/spectral task structure
known-time score -> arrival-time search complexity
universal ranking -> crossing spectral decision kernels.
```

Strongest current statement:

> **Detection is a relation among the optical task, matter, accessible output process, and observer's decision problem. There is generally no architecture-independent scalar detector boundary or total detector ranking.**

---

## Current direction — return to fundamental lower bounds

The project should now stop adding conventional metrics and return to the original deeper question:

> After the resource ledger has been made this explicit, does any architecture-independent lower bound survive?

Next candidates to attack:

```text
reusable-detector reset / erasure cost at fixed error and cycle time;
record-stability versus reset-speed tradeoff;
finite information-acquisition rate under bounded interaction action;
minimum entropy export when the detector must return to a standard ready state.
```

Counterexamples must again include reversible measurement, exported records, active reservoirs, QND-like interactions, and arbitrarily narrowband/long-time operation.

A focused prior-art audit remains mandatory before novelty language.
