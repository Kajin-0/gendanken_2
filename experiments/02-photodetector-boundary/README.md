# Experiment 02 — The Photodetector Boundary

**Opened:** 2026-08-12  
**Status:** exploratory first-principles Gedanken experiment; optical interaction through decision and cyclic reset mapped in minimal models  
**Priority / novelty:** unassessed; **no novelty claim**

## Starting question

> At what point does a simple collection of atoms become a photodetector? If light is absorbed and re-emitted versus absorbed and used to generate charge, where is the boundary?

## Current answer

There is **no universal atom-count transition** at which matter becomes a photodetector.

The strongest current formulation is:

> **Matter functions as a detector only relative to a specified optical task, accessible output, temporal/noise environment, and decision criterion. The boundary is statistical distinguishability of the complete photon-conditioned output process, not a particular atom count, absorption event, electron-hole pair, or conventional scalar figure of merit.**

Under explicit constraints, minimum effective atom numbers, optical depths, event energies, rate ratios, or reset resources can emerge.

## Operational spine

For accessible detector states conditioned on no photon and one photon,

```math
\mathcal D_D
=\frac12\|\rho_D^{(1)}-\rho_D^{(0)}\|_1,
```

with equal-prior optimum error

```math
P_{e,\min}=\frac12(1-\mathcal D_D).
```

This immediately kills absorption as the universal definition: perfect absorption can leave no accessible record, while dispersive nonabsorptive coupling can create one.

## What increasing atom count actually changes

Atom count participates in several different crossovers that must not be conflated:

```text
spectral/band crossover
collective optical coupling
optical depth / column density
record redundancy / stability.
```

In a resonant identical-dipole benchmark,

```math
G=g\sqrt N.
```

But for unequal microscopic couplings,

```math
G^2=\sum_j|g_j|^2,
```

so literal total `N` is not the invariant microscopic resource.

In extended dilute matter the natural coordinate becomes optical depth,

```math
\mathrm{OD}=n\sigma L.
```

## Interaction and record formation

A universal deposited-energy-per-detection bound failed. In a pure finite-time conditional-unitary model, a surviving conditional resource is interaction action:

```math
\mathcal A_\Delta
\ge
\hbar\arcsin(1-2\epsilon).
```

Coherent photon-to-matter transfer is still not a persistent record because the excitation can return.

Adding desired trapping and competing loss shows that record formation is rate matched: arbitrarily strong trapping can overdamp acquisition.

## Traveling-wave capture

For an incident photon, clean one-port critical matching gives

```math
\Gamma_{\rm match}=4G^2/\kappa.
```

At resonance this can yield unit record conversion for **any nonzero `G`** if sufficiently slow/narrowband operation is allowed.

Therefore:

> **Peak monochromatic efficiency does not impose a positive atom-count threshold; weak coupling is paid for in bandwidth/time.**

Optimized external efficiency separates optical escape and collective cooperativity:

```math
\eta_{R,\max}
=\eta_{\rm esc}\frac{C_N}{1+C_N}.
```

## Semiconductor bridge

For a minimal semiconductor slab,

```math
\eta_s
=\eta_{\rm mode}(1-e^{-\alpha L})\eta_{eh}P_{\rm col}P_{\rm read},
```

with

```math
P_{\rm col}
=\frac{\Gamma_{\rm ext}}
{\Gamma_{\rm ext}+\Gamma_{\rm rec}}.
```

Thus electron-hole generation is the **microscopic transduction stage**, not the complete detector event.

A dark-event ceiling appears naturally. For independent Poisson dark clicks,

```math
\mathcal D_{\rm click}=\eta_s e^{-R_d\tau},
```

so target error requires

```math
R_d\tau\le-\ln(1-2\epsilon).
```

## Continuous electrical readout

For common Gaussian covariance,

```math
H_0:y=n,
\qquad
H_1:y=s+n,
```

the optimum decision distance is

```math
\boxed{
d^2
=\int\frac{|\tilde s(f)|^2}{S_n^{(2)}(f)}df
=\int\frac{|\tilde p(f)|^2}{\mathrm{NEP}_2^2(f)}df.
}
```

with

```math
P_e=Q(d/2).
```

For a one-pole white-noise short-pulse benchmark,

```math
\boxed{
d^2
=\frac{E^2D^{*2}}{A\tau}.}
```

Thus equal conventional `D*` does not imply equal event performance when temporal response differs.

## Signal-dependent noise

If noise statistics depend on the optical history, the matched-filter picture is no longer sufficient.

For unequal Gaussian covariances, the optimum statistic is quadratic and covariance change itself can carry information.

For Poisson counts,

```math
BC
=\exp[-(\sqrt{\mu_1}-\sqrt{\mu_0})^2/2].
```

This shows that ordinary shot-noise SNR is a local approximation to the full count-distribution geometry.

## Unknown timing

If the event can occur in one of `M` independent candidate temporal modes,

```math
\Lambda(z)
=\frac1M\sum_m e^{dz_m-d^2/2}.
```

The false-alarm threshold grows approximately as `sqrt(2 ln M)` at large `M` for fixed small false-alarm probability.

Thus intrinsic bandwidth, search-window duration, and timing knowledge are separate resources.

## Task-specific sensitivity and no universal ranking

For a normalized optical waveform `p(t)=E q(t)`, define

```math
\mathcal K_D[q]
=\int |\tilde q(f)|^2/\mathrm{NEP}_{2,D}^2(f)\,df.
```

Then a known-time Gaussian target has

```math
E_{\min}
=2Q^{-1}(\epsilon)/\sqrt{\mathcal K_D[q]}.
```

This is a useful scalar **only after the task is fixed**.

Define the detector decision kernel

```math
W_D(f)=1/\mathrm{NEP}_{2,D}^2(f).
```

If `W_A>=W_B` pointwise, A dominates B for every waveform in the allowed class.

If the kernels cross, there exist tasks that reverse the ranking.

Therefore detector comparison is generally a **partial order**, not a universal one-dimensional leaderboard.

## Reset and thermodynamic closure

The statement

```text
every detected photon dissipates k_B T ln2
```

remains rejected.

For a binary record with event prior `p`, record entropy is

```math
h(p)=-p\ln p-(1-p)\ln(1-p).
```

Under ideal degenerate-memory quasistatic isothermal erasure with no retained side information, exact reset has information-thermodynamic scale

```math
W_{\rm erase,min}\ge k_BT h(p).
```

`k_BT ln2` is only the unbiased case.

A local detector can export its record to another register and use that side information for local reset, so no universal local per-click Landauer heat survives.

A nontrivial erasure problem reappears only after imposing **global cycle closure**: detector, controller, and all record memories return to standard states and no event copy remains outside the accounting boundary.

For a simple activated record, long retention plus fast reliable reset implies a conditional energy-landscape control range,

```math
\Delta E
\ge
k_BT\ln\left[
\frac{\tau_{\rm rec}\ln(1/\epsilon_r)}
{\tau_r[-\ln(1-p_d)]}
\right],
```

when positive. This is a control-range bound, **not** automatically dissipated work.

## Strongest organizing picture

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

Every attempted universal scalar has exposed an omitted resource:

```text
atom count       -> coupling/time and mode overlap
peak efficiency  -> bandwidth
more atoms       -> optical escape
more absorber    -> downstream loss and dark events
fixed-noise SNR  -> hypothesis-dependent statistics
D*               -> temporal/spectral task structure
known-time score -> timing-search complexity
local reset heat -> exported record capacity.
```

## Current frontier

Attack **global cycle closure** itself by allowing, one at a time:

```text
side information correlated with the optical/environmental input;
work extraction from the detected field;
nonequilibrium reservoirs and active pumps;
continuous reversible transduction with no explicit binary memory;
external records retained indefinitely outside the accounting horizon.
```

The goal is to find the weakest assumptions under which any genuinely architecture-independent detector-cycle thermodynamic bound survives.

## Reading order

1. `AGENTS.md`
2. `CURRENT_STATE_LIVE.md`
3. `CLAIM_LEDGER.md`
4. `RESEARCH_LOG.md`
5. `INTERACTION_ACTION_LOWER_BOUND.md`
6. `N_DIPOLE_SINGLE_MODE_MODEL.md`
7. `COHERENT_CAPTURE_TO_RECORD.md`
8. `TRAVELING_WAVE_CAPTURE.md`
9. `MODE_WEIGHTED_OPTICAL_DEPTH.md`
10. `SEMICONDUCTOR_DECISION_BRIDGE.md`
11. `CONTINUOUS_GAUSSIAN_DECISION.md`
12. `SIGNAL_DEPENDENT_NOISE.md`
13. `UNKNOWN_ARRIVAL_TIME.md`
14. `TASK_SPECIFIC_DETECTIVITY.md`
15. `RESET_AND_CYCLE_CLOSURE.md`

## Research rule

Follow the physics rather than a desired paper result. Preserve failed conjectures and counterexamples. Before novelty language, perform a focused primary-source audit; negative search results are not novelty evidence.
