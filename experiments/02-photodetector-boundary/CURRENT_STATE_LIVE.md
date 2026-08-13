# Current Live State — Experiment 02

**Date:** 2026-08-12  
**Status:** exploratory first-principles theory; detector boundary now formulated from microscopic interaction through full output-distribution decision  
**Priority:** unassessed; no novelty claim

This is the current state pointer. `CLAIM_LEDGER.md` is the epistemic boundary; `RESEARCH_LOG.md` preserves chronology and failed routes.

Detailed derivations:

1. `INTERACTION_ACTION_LOWER_BOUND.md`
2. `N_DIPOLE_SINGLE_MODE_MODEL.md`
3. `COHERENT_CAPTURE_TO_RECORD.md`
4. `TRAVELING_WAVE_CAPTURE.md`
5. `MODE_WEIGHTED_OPTICAL_DEPTH.md`
6. `SEMICONDUCTOR_DECISION_BRIDGE.md`
7. `CONTINUOUS_GAUSSIAN_DECISION.md`
8. `SIGNAL_DEPENDENT_NOISE.md`
9. `UNKNOWN_ARRIVAL_TIME.md`
10. `TASK_SPECIFIC_DETECTIVITY.md`

---

## 1. Starting question and strongest current answer

Starting question:

> At what point does a simple collection of atoms become a photodetector?

Strongest current answer:

> **There is no universal atom-count transition. Matter functions as a detector only relative to a specified optical task, accessible subsystem, interaction architecture, temporal/bandwidth constraints, loss and dark processes, persistent-record mechanism, and decision criterion. The most general boundary found so far is statistical distinguishability of the complete photon-conditioned output processes.**

The experiment has therefore moved from

```text
How many atoms?
```

to

```text
How distinguishable are the complete accessible outputs
under the competing optical hypotheses,
under the allowed observation and decision rules?
```

---

## 2. Quantum-state operational spine

For accessible detector states conditioned on no photon and one photon,

```math
\rho_D^{(0)},\qquad\rho_D^{(1)},
```

define

```math
\boxed{
\mathcal D_D
=\frac12\|\rho_D^{(1)}-\rho_D^{(0)}\|_1.
}
```

For equal priors,

```math
\boxed{
P_{e,\min}=\frac12(1-\mathcal D_D).
}
```

Consequences preserved:

```text
perfect absorption can coexist with no accessible detector record;
nonabsorptive/dispersive coupling can encode photon presence;
therefore absorption is neither sufficient nor universally necessary.
```

Electron-hole creation, gain, atom count, and decoherence are likewise not complete detector definitions by themselves.

---

## 3. Atom count reappears only after a resource constraint

A universal positive final deposited-energy cost failed: a degenerate pointer can become orthogonal with zero final bare-energy difference.

For a pure conditional-unitary detector, finite-time state separation instead obeys the conditional interaction-action requirement

```math
\boxed{
\mathcal A_\Delta
\ge
\hbar\arcsin(1-2\epsilon).
}
```

Perfect discrimination requires

```math
\mathcal A_\Delta\ge\pi\hbar/2.
```

If each constituent can supply at most action `a_max`, then

```math
N
\ge
\left\lceil
\frac{\hbar\arcsin(1-2\epsilon)}{a_{\max}}
\right\rceil.
```

Thus a minimum `N` is a constrained resource result, not a detector phase transition.

---

## 4. Explicit collective-coupling benchmark

For identical resonant dipoles in one optical mode,

```math
\boxed{G=g\sqrt N.}
```

The matter-only trace distance in the one-excitation model is

```math
\boxed{
\mathcal D_D(t)=\sin^2(g\sqrt Nt).
}
```

Perfect transient first-lobe transfer requires

```math
N_{\min}
=\left\lceil\left(\frac{\pi}{2g\tau}\right)^2\right\rceil.
```

This is standard Dicke/Tavis--Cummings collective physics used as a detector-boundary benchmark, not claimed new.

Coherent transfer is still not a persistent record because the excitation can return to the optical mode.

---

## 5. Persistent record formation is dynamically matched

With optical loss `kappa`, unwanted matter loss `gamma`, and desired matter-to-record trapping `Gamma`, for a photon initially inside the optical mode,

```math
\boxed{
P_R
=\frac{4G^2\Gamma}
{(\kappa+\gamma+\Gamma)
[4G^2+\kappa(\gamma+\Gamma)]}.
}
```

The trapping optimum is finite:

```math
\boxed{
\Gamma_{\rm opt}
=\sqrt{\frac{(\kappa+\gamma)(4G^2+\kappa\gamma)}{\kappa}}.
}
```

For `gamma=0`, `Gamma_opt=2G`.

Therefore

```text
more irreversibility != monotonically better detection.
```

Record formation must be matched to acquisition and competing loss.

---

## 6. Traveling-wave capture removes the apparent peak-efficiency N threshold

For an actual incident photon, the resonant narrowband record efficiency is

```math
\boxed{
\eta_R(0)
=\frac{16\kappa_{\rm in}\Gamma G^2}
{[\kappa(\gamma+\Gamma)+4G^2]^2}.
}
```

In the clean one-port limit,

```math
\boxed{
\Gamma_{\rm match}=\frac{4G^2}{\kappa}
}
```

gives

```math
r(0)=0,\qquad \eta_R(0)=1.
```

This can occur for any nonzero `G` if sufficiently slow/narrowband operation is permitted.

Hence:

> **Peak monochromatic efficiency by itself imposes no positive atom-count threshold. Weak coupling is paid for in bandwidth/time.**

Optimized external efficiency is

```math
\boxed{
\eta_{R,\max}
=\eta_{\rm esc}\frac{C_N}{1+C_N},
}
```

with

```math
\eta_{\rm esc}=\kappa_{\rm in}/\kappa,
\qquad
C_N=4G^2/(\kappa\gamma).
```

Optical escape and matter-loss/cooperativity are independent ceilings.

Finite photon bandwidth restores a constrained threshold; in the clean matched Lorentzian benchmark,

```math
N
\ge
\frac{\kappa B}{8g^2}
\frac{1-2\epsilon}{\epsilon}.
```

---

## 7. Literal total atom count is not the microscopic invariant

For unequal couplings,

```math
\boxed{
G^2=\sum_j|g_j|^2.
}
```

Only the optically bright superposition contributes directly.

In a dilute traveling-wave continuum this becomes optical depth,

```math
\boxed{
\mathrm{OD}=n\sigma L
=\frac{N_{\rm col}\sigma}{A},
}
```

with

```math
P_{\rm abs}=1-e^{-\mathrm{OD}}.
```

Thus mode-weighted oscillator strength / optical depth is more physical than total `N` in extended matter.

---

## 8. Semiconductor bridge — where electron-hole generation belongs

For a minimal semiconductor slab,

```math
\boxed{
\eta_s
=\eta_{\rm mode}
(1-e^{-\alpha L})
\eta_{eh}
P_{\rm col}
P_{\rm read}.
}
```

With independent extraction/recombination hazards,

```math
\boxed{
P_{\rm col}
=\frac{\Gamma_{\rm ext}}
{\Gamma_{\rm ext}+\Gamma_{\rm rec}}.
}
```

Therefore electron-hole generation is the semiconductor-specific **microscopic transduction/encoding stage**. It is not the full detection event.

For independent Poisson dark clicks of rate `R_d` in window `tau`, binary click distinguishability is

```math
\boxed{
\mathcal D_{\rm click}=\eta_s e^{-R_d\tau}.
}
```

Target `P_e<=epsilon` requires the necessary dark condition

```math
\boxed{
R_d\tau\le-\ln(1-2\epsilon).
}
```

No amount of absorber thickness or atom count repairs a dark-event budget that already violates this condition.

---

## 9. Equal-covariance Gaussian electrical readout

For

```math
H_0:y(t)=n(t),
\qquad
H_1:y(t)=s(t)+n(t),
```

with common Gaussian covariance `C`, the complete decision coordinate is

```math
\boxed{
d^2=\langle s,C^{-1}s\rangle.
}
```

For stationary noise,

```math
\boxed{
d^2
=\int_{-\infty}^{\infty}
\frac{|\tilde s(f)|^2}{S_n^{(2)}(f)}df.
}
```

and

```math
\boxed{P_e=Q(d/2).}
```

Input referring gives

```math
\boxed{
d^2
=\int
\frac{|\tilde p(f)|^2}{\mathrm{NEP}_2^2(f)}df.
}
```

Thus the practical detector coordinate is the full noise-weighted waveform distance, not one scalar `D*`.

For a one-pole detector, white noise, and a short optical energy `E`,

```math
\boxed{
d^2
=\frac{E^2}{\tau\,\mathrm{NEP}^2}
=\frac{E^2D^{*2}}{A\tau}.
}
```

Hence two equal-area detectors with identical low-frequency `D*` can have different event-detection error solely because their response times differ.

---

## 10. Signal-dependent noise strengthens the full-distribution formulation

For Gaussian hypotheses

```math
H_i:y\sim\mathcal N(\mu_i,C_i),
```

with `C_0 != C_1`, the exact equal-prior likelihood ratio is quadratic:

```math
\boxed{
\ell(y)
=
\frac12(y-\mu_0)^TC_0^{-1}(y-\mu_0)
-
\frac12(y-\mu_1)^TC_1^{-1}(y-\mu_1)
-
\frac12\ln\frac{\det C_1}{\det C_0}.
}
```

Covariance changes can therefore carry photon-history information even if the mean is unchanged.

For Poisson count hypotheses

```math
K\sim\operatorname{Poisson}(\mu_i),
```

the exact log-likelihood ratio is

```math
\boxed{
\ell(K)
=K\ln\frac{\mu_1}{\mu_0}
-(\mu_1-\mu_0).
}
```

The Poisson Bhattacharyya coefficient is

```math
\boxed{
BC
=\exp\left[-\frac12
(\sqrt{\mu_1}-\sqrt{\mu_0})^2\right].
}
```

Thus the natural count-statistics separation is built from square-root rates. Conventional background-shot-noise SNR is only the weak-signal expansion of this distribution geometry.

In the zero-background case with signal count rate `lambda_s`,

```math
\boxed{
P_e=\frac12e^{-\lambda_sT}.
}
```

So one universal SNR law does not span both zero-background and background-dominated regimes.

---

## 11. Unknown arrival time creates a temporal-search resource

If an event can occupy one of `M` independent temporal cells, with normalized matched-filter outputs `z_m`, the exact mixture likelihood is

```math
\boxed{
\Lambda(z)
=\frac1M\sum_{m=1}^M
\exp(dz_m-d^2/2).
}
```

For a max-threshold benchmark,

```math
\boxed{
P_{\rm FA}=1-\Phi(\eta)^M,
}
```

```math
\boxed{
P_{\rm miss}
=\Phi(\eta-d)\Phi(\eta)^{M-1}.
}
```

At fixed small false-alarm probability, the required threshold grows approximately as

```math
\sqrt{2\ln M}.
```

Real shifted templates are correlated; a rough effective-trial coordinate is

```math
M_{\rm eff}\sim T_{\rm search}B_{\rm eff}
```

up to order-unity/task-specific factors.

Thus response bandwidth, search-window duration, and false-alarm budget are separate temporal resources.

---

## 12. Task-specific minimum event energy

For a normalized known-time optical waveform

```math
p(t)=Eq(t),\qquad \int q(t)dt=1,
```

define

```math
\boxed{
\mathcal K_D[q]
=\int
\frac{|\tilde q(f)|^2}
{\mathrm{NEP}_{2,D}^2(f)}df.
}
```

Then

```math
d^2=E^2\mathcal K_D[q].
```

For known timing and equal priors,

```math
\boxed{
E_{\min}(q,\epsilon)
=\frac{2Q^{-1}(\epsilon)}
{\sqrt{\mathcal K_D[q]}}.
}
```

This is an operational scalar **only after the task and decision target are fixed**.

Trying to force `D*`-like units introduces another arbitrary time-scale convention for general waveforms, so `E_min` is the cleaner task-specific quantity.

---

## 13. No-universal-scalar-ranking result inside the Gaussian task class

Define the detector spectral decision kernel

```math
\boxed{
W_D(f)
=\frac1{\mathrm{NEP}_{2,D}^2(f)}.
}
```

Then

```math
\mathcal K_D[q]
=\int |\tilde q(f)|^2W_D(f)df.
```

If

```math
W_A(f)\ge W_B(f)
```

for every allowed frequency, detector A is never worse than B for any known-time Gaussian waveform in that task class.

But if `W_A-W_B` changes sign with frequency, there exist tasks concentrated in the A-favored region and tasks concentrated in the B-favored region. Therefore the ranking reverses.

Hence

```math
\boxed{
W_A-W_B\text{ changes sign}
\Rightarrow
\text{no task-independent scalar ranking can represent all waveform tasks.}
}
```

This is a simple functional-ordering consequence, not claimed as a new theorem.

The natural detector comparison is therefore often a **partial order**, not one universal score.

---

## 14. Strongest organizing result so far

The complete chain is now

```text
material constitution
-> optical access / mode overlap
-> mode-weighted coupling or optical depth
-> microscopic excitation / electron-hole generation
-> acquisition/extraction versus loss/recombination
-> persistent record
-> complete conditional electrical/output statistics
-> nuisance parameters such as unknown timing
-> optimum likelihood discrimination
-> decision error
-> reset/reuse.
```

Every attempted universal scalar has exposed a missing resource coordinate:

```text
atom count       -> interaction strength/time and mode overlap
peak efficiency  -> bandwidth
more atoms       -> optical escape ceiling
more absorber    -> downstream collection and dark events
fixed-noise SNR  -> signal-dependent distribution shape
D*               -> temporal/spectral task structure
known-time score -> arrival-time search complexity.
```

The strongest current conceptual statement is:

> **Detection is a relation among the optical task, matter, accessible output process, and observer's decision problem. There is generally no architecture-independent scalar boundary or total ordering of detectors.**

---

## 15. Current frontier

The next phase should return to fundamental lower-bound attacks rather than add conventional metrics indefinitely.

Candidate fronts:

```text
minimum reset/erasure cost for a reusable detector at fixed error and cycle time;
record-stability versus reset-speed tradeoff;
finite information acquisition rate per bounded interaction resource;
which bounds survive exported records, reversible measurement, active reservoirs, and narrowband/long-time counterexamples.
```

A focused primary-source prior-art audit remains mandatory before any novelty language.

---

## 16. Mandatory caveats

- Trace distance / Helstrom discrimination are established.
- Quantum-speed-limit geometry is established.
- Dicke/Tavis--Cummings coupling, critical coupling, cooperativity, Beer-Lambert optical depth, Gaussian/Poisson detection theory, likelihood ratios, matched filtering, and extreme-value/trials effects are established structures.
- The detector-boundary synthesis and conditional cross-stage formulas have not yet undergone a focused prior-art audit.
- Current models remain idealized and omit many realistic complications.
- Experiment 01 remains separate and untouched.
