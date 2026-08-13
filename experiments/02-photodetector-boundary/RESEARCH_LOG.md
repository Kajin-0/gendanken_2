# Research Log — Experiment 02: The Photodetector Boundary

Chronological reasoning log. This file records **why the direction changed**, especially failed universal boundaries and the missing resource that killed them. Detailed algebra is preserved in dedicated derivation files.

---

## 2026-08-12 — Experiment opened

Starting question:

> At what point does a simple collection of atoms become a photodetector? If light is absorbed and re-emitted versus absorbed and a charge pair is generated, when does that happen and what is the boundary?

Initial intuition:

```text
few atoms
-> bands
-> electron-hole generation
-> photodetector.
```

The project explicitly refused to assume this chain.

---

## Re-emission versus electron-hole generation — corrected

Interband absorption can create an electron-hole excitation which later recombines radiatively.

**Conclusion:** re-emission and pair generation can be stages of one event.

**Direction:** separate absorption physics from detector-record physics.

---

## Universal atom-count threshold — killed

A single microscopic system can encode photon arrival; a macroscopic absorber can fail to retain an accessible record.

**Conclusion:** no universal `N_c` without interaction/readout/persistence/noise constraints.

**Missing coordinate:** operational distinguishability.

---

## Detector defined as hypothesis discrimination

For accessible material states

```math
\rho_D^{(0)},\qquad\rho_D^{(1)},
```

use

```math
\mathcal D_D
=\frac12\|\rho_D^{(1)}-\rho_D^{(0)}\|_1,
```

with equal-prior optimum error

```math
P_{e,\min}=\frac12(1-\mathcal D_D).
```

**Conclusion:** detection is a functional information relation, not a phase-of-matter label.

---

## Absorption as detector boundary — killed twice

A perfect absorber can leave identical accessible detector states.

A dispersive interaction can leave the photon intact while changing a material pointer.

**Conclusion:** absorption is neither sufficient nor universally necessary.

---

## Band formation separated

Increasing atom count can produce a dense, band-like electronic spectrum.

**Conclusion:** atomic-to-band crossover is condensed-matter structure, not detector definition.

---

## Electron-hole generation separated

A semiconductor photon can create an excitation that remains bound, recombines, traps, or fails extraction.

Minimal collection benchmark:

```math
P_{\rm col}
=\frac{\Gamma_{\rm ext}}
{\Gamma_{\rm ext}+\Gamma_{\rm rec}}.
```

**Conclusion:** electron-hole generation is transduction, not a complete detector event.

---

## Gain reinterpreted

Gain enlarges/stabilizes an upstream distinction against later readout limitations.

**Conclusion:** gain does not create photon-arrival information that was absent before the gain stage.

---

## Irreversibility reframed

Closed-system evolution may remain unitary while local coherence becomes inaccessible and a metastable record forms.

**Conclusion:** practical irreversibility must be tied to subsystem choice, information dispersal, and record persistence.

---

## Momentary encoding versus retention

A transient `D_D(t)>0` can disappear before allowed readout.

**Conclusion:** acquisition and retention are distinct resources.

---

## Universal deposited-energy lower bound — killed

A degenerate two-state pointer can become orthogonal with zero final bare-energy change.

Finite-time pure-state separation still requires interaction action:

```math
\mathcal A_\Delta
\ge
\hbar\arcsin(1-2\epsilon).
```

Perfect discrimination requires `pi hbar/2`.

**Conclusion:** final deposited energy fails; interaction action survives conditionally.

Detailed derivation: `INTERACTION_ACTION_LOWER_BOUND.md`.

---

## Constrained atom count recovered

If each constituent supplies at most action `a_max`, then

```math
N
\ge
\left\lceil
\hbar\arcsin(1-2\epsilon)/a_{\max}
\right\rceil.
```

**Conclusion:** `N_min` can emerge only after a microscopic resource cap is stated.

---

## Exact one-photon + N-dipole benchmark

For identical resonant dipoles,

```math
G=g\sqrt N,
```

and

```math
\mathcal D_D(t)=\sin^2(g\sqrt Nt).
```

Perfect transient first-lobe transfer requires

```math
N_{\min}=\left\lceil(\pi/(2g\tau))^2\right\rceil.
```

**Conclusion:** a many-atom threshold can arise from collective coupling and finite interaction time without band formation.

Detailed derivation: `N_DIPOLE_SINGLE_MODE_MODEL.md`.

---

## Coherent transfer as persistent detection — killed

The excitation Rabi-oscillates back into the optical mode.

**Conclusion:** acquisition is not yet persistent record.

---

## Record trapping introduced

For collective coupling `G`, optical loss `kappa`, unwanted matter loss `gamma`, and desired trapping `Gamma`,

```math
P_R
=\frac{4G^2\Gamma}
{(\kappa+\gamma+\Gamma)[4G^2+\kappa(\gamma+\Gamma)]}.
```

The formula was cross-checked numerically at about `1e-11` absolute agreement in tested cases.

Detailed derivation: `COHERENT_CAPTURE_TO_RECORD.md`.

---

## More irreversibility is always better — killed

The trapping rate has a finite optimum; for `gamma=0`,

```math
\Gamma_{\rm opt}=2G.
```

Too little trapping fails to freeze the event; too much overdamps acquisition.

**Conclusion:** record formation is a rate-matching problem.

---

## Traveling-wave capture introduced

The photon was no longer placed inside the mode by assumption.

Clean one-port matching gives

```math
\Gamma_{\rm match}=4G^2/\kappa
```

and unit resonant record conversion.

Detailed derivation: `TRAVELING_WAVE_CAPTURE.md`.

---

## Peak-efficiency atom threshold — killed

The critical-coupling condition works for any nonzero `G` if arbitrarily slow/narrowband operation is allowed.

**Conclusion:** peak monochromatic efficiency does not impose positive `N_min`.

**Missing resource:** bandwidth / interaction time.

---

## Optical escape and cooperativity separated

Optimized external efficiency becomes

```math
\eta_{R,\max}
=\eta_{\rm esc}\frac{C_N}{1+C_N}.
```

**Conclusion:** more atoms cannot repair inaccessible optical escape.

---

## Finite bandwidth restored a constrained matter threshold

In a clean matched Lorentzian benchmark,

```math
P_R=\Gamma/(\Gamma+B),
\qquad
\Gamma=4Ng^2/\kappa.
```

**Conclusion:** weak coupling trades against bandwidth.

---

## Literal total atom count — killed

For unequal microscopic couplings,

```math
G^2=\sum_j|g_j|^2.
```

Only the bright mode-weighted combination participates.

**Conclusion:** the relevant microscopic resource is mode-weighted oscillator strength, not total physical `N`.

Detailed derivation: `MODE_WEIGHTED_OPTICAL_DEPTH.md`.

---

## Continuum limit -> optical depth

For dilute single-pass matter,

```math
\mathrm{OD}=n\sigma L,
\qquad
P_{\rm abs}=1-e^{-\mathrm{OD}}.
```

**Conclusion:** column density / optical depth replaces total atom count in extended matter.

Resonant critical coupling showed that architecture can trade absorber strength against dwell time/bandwidth.

---

## Semiconductor chain reconstructed

Minimal signal-record probability:

```math
\eta_s
=\eta_{\rm mode}(1-e^{-\alpha L})\eta_{eh}P_{\rm col}P_{\rm read}.
```

**Conclusion:** electron-hole generation occupies the microscopic transduction stage inside a longer optical-to-record chain.

Detailed derivation: `SEMICONDUCTOR_DECISION_BRIDGE.md`.

---

## Dark-event ceiling derived

For Poisson dark clicks,

```math
\mathcal D_{\rm click}=\eta_s e^{-R_d\tau}.
```

Target error requires

```math
R_d\tau\le-\ln(1-2\epsilon).
```

**Conclusion:** more absorber/gain cannot overcome a dark-event budget that already destroys the evidential contrast.

---

## Continuous Gaussian electrical output introduced

For

```math
H_0:y=n,
\qquad
H_1:y=s+n,
```

with common Gaussian covariance,

```math
d^2
=\langle s,C^{-1}s\rangle
=\int |\tilde s(f)|^2/S_n^{(2)}(f)\,df,
```

and

```math
P_e=Q(d/2).
```

Input referring gives the NEP-weighted waveform integral.

**Conclusion:** the practical detector coordinate is the full noise-weighted waveform distance.

Detailed derivation: `CONTINUOUS_GAUSSIAN_DECISION.md`.

---

## Same D* -> same event performance — killed

For a one-pole white-noise short-pulse benchmark,

```math
d^2
=\frac{E^2D^{*2}}{A\tau}.
```

**Conclusion:** equal scalar low-frequency `D*` can coexist with different event-detection performance because temporal response differs.

**Missing coordinate:** task spectrum / response time.

---

## Equal-covariance noise model generalized

For Gaussian hypotheses with `C_0 != C_1`, the optimum statistic becomes quadratic. Covariance change alone can carry information.

**Conclusion:** the detector output is the complete conditional distribution, not just a mean signal plus nuisance noise.

Detailed derivation: `SIGNAL_DEPENDENT_NOISE.md`.

---

## Poisson count geometry exposed the local nature of SNR

For Poisson means `mu_0,mu_1`,

```math
BC
=\exp[-(\sqrt{\mu_1}-\sqrt{\mu_0})^2/2].
```

Weak-signal finite-background expansion recovers familiar shot-noise scaling.

Zero background instead gives

```math
P_e=\frac12e^{-\lambda_sT}.
```

**Conclusion:** one fixed-noise SNR law cannot cover all count regimes.

---

## Unknown arrival time introduced

For `M` independent candidate temporal modes,

```math
\Lambda(z)=\frac1M\sum_m e^{dz_m-d^2/2}.
```

A max-threshold benchmark gives

```math
P_{\rm FA}=1-\Phi(\eta)^M,
```

```math
P_{\rm miss}=\Phi(\eta-d)\Phi(\eta)^{M-1}.
```

The threshold grows roughly as `sqrt(2 ln M)` at large `M` for fixed small false-alarm probability.

**Conclusion:** timing uncertainty / search complexity is a separate detector resource.

Detailed derivation: `UNKNOWN_ARRIVAL_TIME.md`.

---

## Faster is always better — narrowed

Higher bandwidth can increase known-time waveform information but also increase the number of distinguishable candidate arrival cells in a fixed search window.

**Conclusion:** speed must be interpreted relative to timing uncertainty and false-alarm constraints.

---

## Task-specific scalar constructed

For `p(t)=E q(t)`,

```math
\mathcal K_D[q]
=\int |\tilde q(f)|^2/\mathrm{NEP}_{2,D}^2(f)\,df,
```

with

```math
E_{\min}
=2Q^{-1}(\epsilon)/\sqrt{\mathcal K_D[q]}
```

for known-time equal-prior Gaussian readout.

**Conclusion:** an operational scalar exists after the task and decision target are fixed, but it is not detector-only.

Detailed derivation: `TASK_SPECIFIC_DETECTIVITY.md`.

---

## Universal scalar detector ranking — killed when kernels cross

Define

```math
W_D(f)=1/\mathrm{NEP}_{2,D}^2(f).
```

Pointwise dominance `W_A>=W_B` guarantees A is never worse for any waveform in the task class.

If `W_A-W_B` changes sign, appropriately chosen waveforms reverse the ranking.

**Conclusion:** detector comparison is generally a partial order, not a universal one-dimensional leaderboard.

---

## Returned to thermodynamic lower bounds

The original per-click Landauer claim had already failed at acquisition.

The new question became:

> Does thermodynamics re-enter when the detector must be reused cyclically?

Detailed derivation: `RESET_AND_CYCLE_CLOSURE.md`.

---

## Fixed `k_B T ln2` reset cost — narrowed to the actual record entropy

For a binary event record with event prior `p`, logical entropy is

```math
h(p)=-p\ln p-(1-p)\ln(1-p).
```

Under ideal degenerate-memory quasistatic isothermal erasure with no retained side information,

```math
W_{\rm erase,min}\ge k_BT h(p).
```

`k_BT ln2` is only the unbiased `p=1/2` case.

**Conclusion:** even cyclic erasure does not carry a universal fixed `ln2` cost independent of record statistics.

---

## Local reusable detector -> local Landauer cost — killed by record export

Copy/export the detector record into an external register `R`, then reset the local detector conditionally using `R`.

The local uncertainty becomes `H(M|R)`; for a perfect external copy it can vanish.

**Conclusion:** a detector can be locally reusable without a mandatory local `k_BT ln2` heat packet per click.

**Missing resource:** external record memory / entropy capacity.

---

## Global cycle closure restores an erasure problem

Strengthen the requirement:

```text
detector + controller + all record memories
must return to standard states,
and no event copy may remain outside the accounting boundary.
```

Then the record entropy cannot be exported indefinitely.

**Conclusion:** a Landauer-like bound can reappear at the global cycle level under standard thermodynamic assumptions, with scale `k_BT h(p)` for an ideal binary record rather than universally `k_BT ln2`.

This is a cycle-closure statement, not a photon-absorption statement.

---

## Stability versus reset speed derived conditionally

Activated retention gives

```math
E_b
\ge
k_BT\ln[\nu_0\tau_{\rm rec}/(-\ln(1-p_d))].
```

If reset lowers the barrier by `Delta E`, rapid reliable reset gives

```math
\Delta E
\ge
k_BT\ln\left[
\frac{\tau_{\rm rec}\ln(1/\epsilon_r)}
{\tau_r[-\ln(1-p_d)]}
\right]
```

when positive in the common activated-rate model.

**Conclusion:** long retention + tiny false switching + fast reset requires large control of the energy landscape.

**Important correction:** this is a control-range requirement, not a proof that the barrier modulation energy must be dissipated.

---

## Current strongest organizing picture

```text
material constitution
-> optical access / mode overlap
-> mode-weighted interaction resource
-> microscopic transduction
-> acquisition/extraction versus loss
-> persistent record
-> complete conditional output process
-> timing / nuisance parameters
-> optimum decision
-> local reset / record export
-> optional global cycle closure.
```

Every attempted universal scalar has exposed a missing coordinate:

```text
atom count       -> interaction strength/time + mode overlap
peak efficiency  -> bandwidth
more atoms       -> optical escape
more absorber    -> downstream loss + dark events
fixed-noise SNR  -> hypothesis-dependent statistics
D*               -> task spectrum / temporal response
known-time score -> timing-search complexity
local reset heat -> external record capacity.
```

---

## Current frontier

Attack the global cycle-closure bound itself.

Allow:

```text
side information correlated with the incident optical/environmental state;
work extraction from the detected field;
nonequilibrium reservoirs / active pumps;
continuous reversible transduction with no explicit binary memory;
external records retained indefinitely outside the chosen horizon.
```

The goal is to identify the weakest precise assumptions under which any universal detector-cycle thermodynamic bound actually survives.

A focused prior-art audit remains mandatory before novelty language.
