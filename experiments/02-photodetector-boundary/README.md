# Experiment 02 — The Photodetector Boundary

**Opened:** 2026-08-12  
**Status:** exploratory first-principles Gedanken experiment; external capture and semiconductor decision bridge active  
**Priority / novelty:** unassessed; **no novelty claim**

## Starting question

> At what point does a simple collection of atoms become a photodetector? If light is absorbed and re-emitted versus absorbed and used to generate charge, where is the boundary?

The experiment began by separating optical absorption, band formation, carrier generation, information acquisition, record formation, and practical readout rather than assuming they are one transition.

## Current answer in one paragraph

There is **no universal atom-count transition** at which matter becomes a photodetector. A useful detector regime appears only relative to an optical mode, coupling strength, interaction time/bandwidth, competing loss, persistent-record mechanism, dark-event budget, and decision target. Under explicit constraints, minimum effective atom numbers, collective cooperativities, or optical depths do emerge. Total atom count itself is generally not the invariant resource: only matter that actually overlaps and couples to the optical field contributes.

## Operational spine

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
P_{e,\min}
=\frac12(1-\mathcal D_D).
}
```

This immediately gives the first central correction:

```text
absorption != detection.
```

A perfect absorber can leave no accessible material record, while a dispersive interaction can encode photon presence without destroying the photon.

## Separate boundaries

The project keeps distinct:

```text
1. finite atomic spectrum -> band-like spectrum
2. optical access / mode overlap
3. bound excitation -> mobile carriers
4. optical interaction -> encoded information
5. encoded information -> persistent/metastable record
6. record -> useful decision against dark/readout noise
7. reset / reuse.
```

A result about one boundary must not be promoted into another without derivation.

## First resource result — energy fails, interaction action survives conditionally

Target discrimination alone does not require a universal positive final detector-energy change. A degenerate two-state pointer can end in an orthogonal state with zero final bare-energy separation.

For a pure conditional-unitary detector, finite-time state separation instead requires interaction action

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

This is an application of established quantum-speed-limit geometry, not a novelty claim.

If each constituent can supply at most action `a_max`, then

```math
N
\ge
\left\lceil
\frac{\hbar\arcsin(1-2\epsilon)}{a_{\max}}
\right\rceil.
```

So `N_min` appears only after a microscopic resource cap is stated.

## Exact one-photon / N-dipole benchmark

For identical resonant dipoles in one optical mode,

```math
\boxed{G=g\sqrt N.}
```

The matter-only distinguishability is

```math
\boxed{
\mathcal D_D(t)=\sin^2(g\sqrt Nt).
}
```

and perfect transient transfer requires

```math
\boxed{
N_{\min}
=
\left\lceil
\left(\frac{\pi}{2g\tau}\right)^2
\right\rceil.
}
```

This is standard collective-coupling physics used here to show how a constrained many-atom threshold can arise without band formation.

## Coherent transfer is still not a detector record

In the lossless model the matter excitation oscillates back into the optical mode.

Therefore

```text
photon -> matter excitation
```

is still not equivalent to

```text
photon -> persistent detector record.
```

Adding optical loss, unwanted matter loss, and desired record trapping produces the exact initial-in-mode record probability

```math
\boxed{
P_R
=
\frac{4G^2\Gamma}
{(\kappa+\gamma+\Gamma)
[4G^2+\kappa(\gamma+\Gamma)]}.
}
```

The desired trapping rate has a finite optimum; for `gamma=0`,

```math
\boxed{\Gamma_{\rm opt}=2G.}
```

Thus **more irreversibility is not monotonically better** when coherent acquisition still has to occur.

## Traveling-wave external capture

The photon is next treated as an incident traveling wavepacket rather than an excitation already inside the optical mode.

For input coupling `kappa_in`, parasitic optical loss `kappa_loss`, collective matter coupling `G`, matter loss `gamma`, and record rate `Gamma`, the resonant narrowband record efficiency is

```math
\boxed{
\eta_R(0)
=
\frac{16\kappa_{\rm in}\Gamma G^2}
{[\kappa(\gamma+\Gamma)+4G^2]^2}.
}
```

Equivalently,

```math
\eta_R(0)
=
\beta_R
\frac{4\kappa_{\rm in}\kappa_m}
{(\kappa+\kappa_m)^2},
```

with

```math
\kappa_m=4G^2/(\gamma+\Gamma),
\qquad
\beta_R=\Gamma/(\gamma+\Gamma).
```

This exposes an optical critical-coupling structure.

## Major counterexample — peak efficiency does not require large N

In the clean one-port limit,

```text
kappa_loss=0,
gamma=0,
```

critical matching is

```math
\boxed{
\Gamma_{\rm match}=4G^2/\kappa.
}
```

At resonance,

```math
r=0,
\qquad
\eta_R=1.
```

This can occur for **any nonzero `G`** if correspondingly slow/narrowband operation is allowed.

Therefore

> **unit monochromatic efficiency by itself does not imply a minimum atom count. Weak coupling is paid for in bandwidth/time.**

This is one of the strongest conceptual corrections in the experiment.

## External-capture optimum and collective cooperativity

Optimizing the traveling-wave record rate gives

```math
\boxed{
\Gamma_{\rm opt}
=\gamma+\frac{4G^2}{\kappa}.
}
```

The maximum resonant efficiency is

```math
\boxed{
\eta_{R,\max}
=\eta_{\rm esc}\frac{C_N}{1+C_N},
}
```

with

```math
\eta_{\rm esc}=\kappa_{\rm in}/\kappa,
```

and

```math
\boxed{
C_N=\frac{4G^2}{\kappa\gamma}.
}
```

This separates two ceilings:

```text
optical access / parasitic loss
and
collective coupling / matter loss.
```

Increasing atom number cannot repair inaccessible optical escape without changing the architecture.

## Bandwidth restores a finite threshold

In the clean critically matched bad-cavity benchmark,

```math
\eta_R(\delta)
\simeq
\frac{\Gamma^2}{\delta^2+\Gamma^2},
\qquad
\Gamma=4Ng^2/\kappa.
```

For a Lorentzian incident photon spectrum of HWHM `B`,

```math
\boxed{
P_R=\frac{\Gamma}{\Gamma+B}.
}
```

Thus target error `epsilon` requires

```math
\boxed{
N
\ge
\frac{\kappa B}{8g^2}
\frac{1-2\epsilon}{\epsilon}.
}
```

The missing resource behind the weak-coupling perfect-efficiency construction is therefore **bandwidth / response time**.

## Total N is replaced by mode-weighted coupling

For nonuniform couplings,

```math
\boxed{
G^2=\sum_j|g_j|^2.
}
```

Only the bright superposition proportional to

```math
\sum_jg_j|e_j\rangle
```

couples to the optical mode.

Atoms outside the mode, at field nodes, or poorly aligned with the field contribute little.

Thus the natural microscopic resource is **mode-weighted oscillator strength**, not literal atom count.

## Continuum limit — optical depth

For a dilute single-pass absorber,

```math
\boxed{
\mathrm{OD}=n\sigma L
=\frac{N_{\rm col}\sigma}{A},
}
```

and

```math
\boxed{
P_{\rm abs}=1-e^{-\mathrm{OD}}.
}
```

In the ideal single-pass high-efficiency limit,

```math
\boxed{
\mathrm{OD}_{\min}=-\ln(2\epsilon).
}
```

This shows explicitly why total atom number is poor: what matters is the optically sampled column density / oscillator strength.

## Semiconductor decision bridge

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

A simple extraction/recombination race gives

```math
\boxed{
P_{\rm col}
=\frac{\Gamma_{\rm ext}}
{\Gamma_{\rm ext}+\Gamma_{\rm rec}}.
}
```

This answers the original pair-generation question cleanly:

> **electron-hole generation is a microscopic transduction event. It becomes useful detection only if the excitation survives, separates/collects, becomes an accessible record, and remains distinguishable from dark output.**

## Add dark events

For independent Poisson dark clicks of rate `R_d` in a decision window `tau`, binary click/no-click distinguishability becomes

```math
\boxed{
\mathcal D_{\rm click}
=\eta_s e^{-R_d\tau}.
}
```

Hence

```math
\boxed{
P_e
=\frac12(1-\eta_s e^{-R_d\tau}).
}
```

A necessary dark-event condition for target `P_e<=epsilon` is

```math
\boxed{
R_d\tau
\le
-\ln(1-2\epsilon).
}
```

For small `epsilon`,

```math
R_d\tau\lesssim2\epsilon.
```

No amount of absorber thickness or atom number can repair a dark-event budget that already destroys the required evidential contrast.

## Strongest current organizing picture

The experiment now reads

```text
atomic/material constitution
-> optical access / mode overlap
-> mode-weighted oscillator strength or optical depth
-> microscopic excitation / electron-hole generation
-> acquisition/extraction versus loss/recombination
-> rate-matched persistent record
-> discrimination against dark/readout noise
-> reset/reuse.
```

Useful coordinates include

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

The strongest answer to the starting question is:

> **A collection of atoms does not become a photodetector at a universal `N`. It enters a useful detector regime when the complete optical–matter–record–decision dynamics cross the required performance surface.**

## Current frontier

The next attack is to replace binary click/no-click output with a continuous noisy electrical waveform:

```text
photon/no-photon hypotheses
-> current or voltage waveform
-> Gaussian / colored noise
-> optimum likelihood-ratio / matched-filter statistic
-> finite integration time and bandwidth
-> responsivity / noise PSD / NEP / D*
-> determine what conventional metrics preserve or hide about detector distinguishability.
```

This is the natural route back to practical photodetector figures of merit without allowing conventional metrics to define the detector boundary by assumption.

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

## Research rule

Follow the physics rather than a desired paper result. Preserve counterexamples and failed boundaries. Before any novelty claim, perform a focused primary-source audit; negative search results are not novelty evidence.
