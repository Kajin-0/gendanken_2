# Experiment 02 — The Photodetector Boundary

**Opened:** 2026-08-12  
**Status:** exploratory first-principles Gedanken experiment; microscopic acquisition and record-formation models active  
**Priority / novelty:** unassessed; **no novelty claim**

## Starting question

> At what point does a simple collection of atoms become a photodetector? If light is absorbed and re-emitted versus absorbed and used to generate charge, where is the boundary?

The experiment began by separating optical absorption, band formation, carrier generation, information acquisition, record formation, and practical readout rather than assuming they are the same transition.

## Current answer in one paragraph

There is **no universal atom-count transition** at which matter becomes a photodetector. Operationally, the relevant boundary is whether the optical hypothesis creates a sufficiently distinguishable accessible material state and whether that distinction becomes a sufficiently persistent record. Once microscopic constraints are supplied, however, genuine minimum-`N` laws emerge. In the current one-photon / `N`-dipole model, collective coupling grows as `g sqrt(N)`; after competing loss and a persistent record channel are added, detection becomes a **rate-matching problem** among coherent acquisition, optical/matter loss, and trapping into the record.

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
P_{e,\min}=\frac12(1-\mathcal D_D).
}
```

The subsystem boundary is essential: information can leave the material and remain in outgoing radiation or the environment.

## Permanent conceptual corrections

The current reasoning has killed the following shortcuts:

```text
absorption alone = detection                           -> false
absorption is required for every detector              -> false
electron-hole generation = completed electrical event  -> false
macroscopic gain creates the original photon info      -> false
one universal critical atom count exists               -> false
nonzero final detector-energy change is required       -> false
k_B T ln 2 is automatically paid at photon acquisition -> false as a universal claim
coherent excitation transfer = persistent record       -> false
more irreversible trapping is always better            -> false in the current lossy model
```

The counterexamples and exact scope are preserved in `CLAIM_LEDGER.md` and `RESEARCH_LOG.md`.

## Three different meanings of "more atoms"

The original intuition is now decomposed into

```text
SPECTRAL CROSSOVER
more atoms -> denser electronic levels -> molecular/band-like description

ACQUISITION CROSSOVER
more coherently coupled dipoles -> larger collective photon-matter matrix element

RECORD CROSSOVER
additional degrees/dynamics -> trapping, decoherence, metastability, gain, redundancy
```

These are physically distinct.

## Result 1 — finite interaction action is required in the pure/unitary acquisition model

For a conditional detector Hamiltonian

```math
H_0=H_D,
\qquad
H_1=H_D+V,
```

the differential interaction must supply

```math
\boxed{
\mathcal A_\Delta
\equiv
\int_0^\tau\Delta V_I(t)dt
\ge
\hbar\arcsin(1-2\epsilon)
}
```

to reach equal-prior error `epsilon` in the stated pure-state model.

Perfect discrimination requires

```math
\mathcal A_\Delta\ge\pi\hbar/2.
```

A degenerate qubit pointer saturates this while its final bare-energy change is zero. Thus the surviving resource is interaction action, not a universal deposited-energy cost.

This is a detector-specific use of established quantum-speed-limit geometry, not a new speed-limit theorem.

## Result 2 — a general per-constituent action cap recovers minimum atom count

If each microscopic constituent supplies at most integrated differential action `a_max`, then

```math
\boxed{
N
\ge
\left\lceil
\frac{\hbar\arcsin(1-2\epsilon)}{a_{\max}}
\right\rceil.
}
```

This is the first clean answer to the original atom-count intuition:

> `N_min` appears only after a microscopic coupling constraint is stated.

## Result 3 — exact one-photon + N-dipole transfer

For `N` identical resonant two-level dipoles coupled to one quantized mode,

```math
H_I
=\hbar g\sum_j(a\sigma_j^+ + a^\dagger\sigma_j^-),
```

the photon couples to the symmetric bright state with

```math
\boxed{G=g\sqrt N.}
```

The exact matter-only trace distance is

```math
\boxed{
\mathcal D_D(t)=\sin^2(g\sqrt Nt).
}
```

so, on the first transfer lobe,

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

Thus this architecture gives the concrete scaling

```math
N_{\min}\propto(g\tau)^{-2}.
```

The `sqrt(N)` collective enhancement is established Dicke/Tavis--Cummings physics; no novelty claim is attached to it.

## Microscopic optical form of g

For an ideal aligned electric-dipole transition,

```math
\boxed{
g
=|\mathbf d\cdot\mathbf e|
\sqrt{\frac{\omega}{2\hbar\epsilon_0V_{\rm eff}}}.}
```

The atom-count problem therefore maps onto transition dipole strength, optical confinement, and interaction/dwell time.

## Result 4 — coherent acquisition must be converted into a record

The lossless `N`-dipole excitation Rabi-oscillates back into the optical mode. A long-lived detector record therefore requires an additional process.

Minimal record model:

```text
G      = g sqrt(N) coherent photon <-> matter coupling
kappa  = optical-mode population loss
gamma  = unwanted matter-excitation population loss
Gamma  = desired trapping rate into a persistent record state.
```

The exact long-time record probability for a photon initially in the mode is

```math
\boxed{
P_R
=
\frac{4G^2\Gamma}
{(\kappa+\gamma+\Gamma)
[4G^2+\kappa(\gamma+\Gamma)]}.
}
```

This analytic expression was cross-checked against direct numerical integration of the amplitude equations.

## Result 5 — irreversibility must be rate-matched

For `kappa>0`, maximizing the record probability gives

```math
\boxed{
\Gamma_{\rm opt}
=
\sqrt{
\frac{(\kappa+\gamma)(4G^2+\kappa\gamma)}{\kappa}
}.
}
```

For negligible unwanted matter loss,

```math
\boxed{\Gamma_{\rm opt}=2G.}
```

So

```text
trapping too slow -> acquired excitation returns/is lost
trapping too fast -> coherent transfer is overdamped while optical loss continues.
```

The detector therefore has a finite acquisition-to-retention matching condition.

## Result 6 — persistent-record fidelity imposes a stronger N requirement

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
P_{R,\max}
=
\left(\frac{2G}{\kappa+2G}\right)^2.
```

If the persistent record is perfectly distinguishable and there are no false records, equal-prior error target `epsilon` requires

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

Near-perfect **persistent** detection is therefore much more demanding than merely creating a transient coherent excitation.

## Current detector-resource hierarchy

The strongest organizing structure is now

```text
ACQUISITION
photon-conditioned coupling / interaction action

LOSS COMPETITION
coherent acquisition versus optical/matter escape

RETENTION
rate-matched trapping / metastability / dark-event suppression

READOUT / GAIN
make the stored distinction robust to downstream electronics/noise

RESET
separate logical/thermodynamic recycling problem.
```

For a thermally activated bistable record, a separate conditional retention requirement is

```math
E_b
\ge
k_BT
\ln\left[
\frac{\nu_0\tau_{\rm rec}}
{-\ln(1-p_d)}
\right].
```

It is not a universal bound outside the Arrhenius model.

## Current strongest insight

The detector boundary increasingly looks like a **dynamical rate-ratio / impedance-matching problem**, not a static transition in matter.

Candidate coordinates are

```math
\frac{g\sqrt N}{\kappa},
\qquad
\frac{g\sqrt N}{\gamma},
\qquad
\frac{\Gamma}{g\sqrt N}.
```

The chain is now

```text
microscopic constituents
-> available photon-matter coupling
-> state-separation speed
-> competition with loss
-> rate-matched persistent record
-> readout/reset.
```

## Current frontier

The latest exact record model begins with the photon already occupying the optical mode. It therefore sidesteps the real external capture problem.

Next:

```text
traveling one-photon wavepacket
-> input coupling kappa_in
-> parasitic optical loss kappa_loss
-> collective matter coupling g sqrt(N)
-> record trapping Gamma
-> reflection / transmission / loss / record probability.
```

The target question is:

> **What impedance-matching / critical-coupling condition converts an incident photon into a persistent detector record with near-unity probability, and how does that condition map onto cross section, optical depth, oscillator strength, mode volume, and bandwidth?**

That is the current live frontier.

## Reading order

1. [`AGENTS.md`](AGENTS.md) — experiment-specific reasoning/documentation rules.
2. [`CURRENT_STATE_LIVE.md`](CURRENT_STATE_LIVE.md) — authoritative live state.
3. [`CLAIM_LEDGER.md`](CLAIM_LEDGER.md) — epistemic boundary.
4. [`RESEARCH_LOG.md`](RESEARCH_LOG.md) — chronological path and failures.
5. [`INTERACTION_ACTION_LOWER_BOUND.md`](INTERACTION_ACTION_LOWER_BOUND.md) — first resource-bound attack.
6. [`N_DIPOLE_SINGLE_MODE_MODEL.md`](N_DIPOLE_SINGLE_MODE_MODEL.md) — exact collective single-mode specialization.
7. [`COHERENT_CAPTURE_TO_RECORD.md`](COHERENT_CAPTURE_TO_RECORD.md) — exact loss/trapping record model.

## Research rule

Follow the physics rather than a desired paper result. Preserve failed bounds and counterexamples. Quantum-speed-limit, Dicke/Tavis--Cummings, critical-coupling, quantum-Zeno, and detector-theory prior art must be audited directly before any novelty language.
