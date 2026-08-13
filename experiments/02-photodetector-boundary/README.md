# Experiment 02 — The Photodetector Boundary

**Opened:** 2026-08-12  
**Status:** exploratory first-principles Gedanken experiment; microscopic-to-electrical decision chain active  
**Priority / novelty:** unassessed; **no novelty claim**

## Starting question

> At what point does a simple collection of atoms become a photodetector? If light is absorbed and re-emitted versus absorbed and used to generate charge, where is the boundary?

The experiment has progressively separated band formation, optical absorption, excitation/carrier generation, information acquisition, persistent record formation, and practical readout rather than assuming they are one transition.

## Current answer

There is **no universal atom-count transition** at which matter becomes a photodetector.

The strongest current formulation is task dependent:

> **Matter functions as a photodetector when the photon-conditioned accessible output distribution is sufficiently distinguishable from the no-photon distribution over the allowed observation interval.**

The physical path to that distinction depends on

```text
optical access / mode overlap
mode-weighted oscillator strength or optical depth
interaction time / bandwidth
microscopic excitation / electron-hole generation
competition with recombination and other loss
persistent record formation
electrical transfer function and noise statistics
dark events / timing constraints
reset and reuse.
```

Under explicit constraints, minimum effective atom numbers, optical depths, cooperativities, or rate ratios emerge. Literal total atom count is generally not the invariant resource.

## Operational quantum-state spine

For accessible detector states

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
P_{e,\min}
=\frac12(1-\mathcal D_D).
}
```

This immediately shows that absorption is neither sufficient nor universally necessary for detection.

## Main results so far

### Interaction-action boundary

Target discrimination alone does not require a universal positive final detector-energy change. In the stated pure/unitary finite-time model,

```math
\boxed{
\mathcal A_\Delta
\ge
\hbar\arcsin(1-2\epsilon).
}
```

Perfect discrimination requires `A_Delta >= pi hbar/2`.

### Collective microscopic coupling

For identical resonant dipoles,

```math
\boxed{G=g\sqrt N.}
```

and perfect transient first-lobe transfer requires

```math
N_{\min}
=\left\lceil(\pi/(2g\tau))^2\right\rceil.
```

This is a constrained coupling/time threshold, not a band-formation threshold.

### Persistent record requires rate matching

For a photon initially inside a lossy optical mode,

```math
P_R
=
\frac{4G^2\Gamma}
{(\kappa+\gamma+\Gamma)
[4G^2+\kappa(\gamma+\Gamma)]}.
```

The desired trapping rate has a finite optimum; making the event arbitrarily irreversible is not always beneficial.

### Traveling-wave critical coupling

For an actual incident photon, clean one-port matching gives

```math
\boxed{\Gamma_{\rm match}=4G^2/\kappa.}
```

At resonance this can yield unit record conversion for **any nonzero `G`** if sufficiently slow/narrowband operation is permitted.

Thus

> **peak monochromatic efficiency does not impose a minimum atom count; weak coupling is paid for in bandwidth/time.**

Optimized external efficiency has the structure

```math
\boxed{
\eta_{R,\max}
=\eta_{\rm esc}\frac{C_N}{1+C_N},
}
```

with optical escape factor `eta_esc` and collective cooperativity `C_N`.

### Mode-weighted atom number -> optical depth

For unequal microscopic couplings,

```math
\boxed{G^2=\sum_j|g_j|^2.}
```

Only mode-coupled matter counts.

In a dilute traveling-wave continuum,

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

Thus column density / oscillator-strength overlap is more natural than literal total atom count.

### Semiconductor electron-hole bridge

For a minimal slab,

```math
\eta_s
=\eta_{\rm mode}
(1-e^{-\alpha L})
\eta_{eh}
P_{\rm col}
P_{\rm read},
```

with

```math
P_{\rm col}
=\frac{\Gamma_{\rm ext}}
{\Gamma_{\rm ext}+\Gamma_{\rm rec}}.
```

Therefore electron-hole generation is a **microscopic transduction stage**, not the complete detection event.

### Dark-event decision boundary

For independent Poisson dark clicks,

```math
\boxed{
\mathcal D_{\rm click}
=\eta_s e^{-R_d\tau}.
}
```

A necessary target condition is

```math
\boxed{
R_d\tau
\le
-\ln(1-2\epsilon).
}
```

No amount of absorber thickness or atom number can repair a dark-event budget that already violates the target.

## Continuous electrical readout — current strongest engineering bridge

For

```math
H_0:y(t)=n(t),
\qquad
H_1:y(t)=s(t)+n(t),
```

with common Gaussian covariance, the complete decision coordinate is

```math
\boxed{
d^2
=\langle s,C^{-1}s\rangle.
}
```

For stationary noise,

```math
\boxed{
d^2
=\int_{-\infty}^{\infty}
\frac{|\tilde s(f)|^2}
{S_n^{(2)}(f)}df.
}
```

The optimum equal-prior error is

```math
\boxed{P_e=Q(d/2).}
```

If the optical waveform is `p(t)`,

```math
\boxed{
d^2
=\int
\frac{|\tilde p(f)|^2}
{\mathrm{NEP}_2^2(f)}df.
}
```

This makes the full frequency-dependent signal/noise structure the natural practical detector coordinate.

## Equal D* does not imply equal event performance

For a one-pole detector with response time `tau`, white output noise, a short optical pulse of energy `E`, and matched filtering,

```math
\boxed{
d^2
=\frac{E^2}{\tau\,\mathrm{NEP}^2}.
}
```

Using

```math
\mathrm{NEP}=\sqrt A/D^*,
```

```math
\boxed{
d^2
=\frac{E^2D^{*2}}{A\tau}.
}
```

Thus at equal area and equal low-frequency `D*`,

```math
\boxed{d\propto\tau^{-1/2}.}
```

A faster detector has better optimum discrimination of a short fixed-energy event in this conditional benchmark.

So a scalar `D*` is useful but incomplete: it discards temporal/spectral information needed for general decision tasks.

## Strongest organizing picture

```text
material constitution
-> optical access / mode overlap
-> mode-weighted coupling or optical depth
-> microscopic excitation / electron-hole generation
-> extraction/acquisition versus loss
-> persistent record
-> electrical transfer + noise spectrum
-> noise-weighted photon/no-photon distance
-> decision error
-> reset/reuse.
```

Every attempted universal scalar threshold has so far exposed a missing resource coordinate:

```text
atom count       -> coupling/time and mode overlap
peak efficiency  -> bandwidth
more atoms       -> optical escape ceiling
more absorber    -> downstream loss and dark events
D*               -> temporal/spectral task structure.
```

## Current frontier

Next attacks:

```text
signal-dependent noise
-> shot / generation-recombination / gain noise
-> H0 and H1 have different covariances

unknown photon arrival time / timing jitter
-> temporal search / alignment penalty

then
-> test whether a task-specific scalar detectivity can be defined
   from optimum decision distance.
```

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

## Research rule

Follow the physics rather than a desired paper result. Preserve counterexamples and failed boundaries. Before any novelty claim, perform a focused primary-source audit; negative search results are not novelty evidence.
