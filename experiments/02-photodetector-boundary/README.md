# Experiment 02 — The Photodetector Boundary

**Opened:** 2026-08-12  
**Status:** exploratory first-principles Gedanken experiment; optical interaction through channel ordering and source-inclusive resource closure mapped in minimal models  
**Priority / novelty:** unassessed; **no novelty claim**

## Starting question

> At what point does a simple collection of atoms become a photodetector? If light is absorbed and re-emitted versus absorbed and used to generate charge, where is the boundary?

## Current answer

There is **no universal atom-count transition** at which matter becomes a photodetector.

The strongest current formulation is:

> **Matter functions as a detector only relative to a specified optical input family, allowed operations/reference resources, accessible output channel, temporal/noise environment, and decision criterion. The boundary is operational distinguishability of the induced detector channel, not a particular atom count, absorption event, electron-hole pair, or conventional scalar figure of merit.**

Under explicit constraints, minimum effective atom numbers, optical depths, event energies, rate ratios, control precision, channel counts, or reset resources can emerge.

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

This is the unrestricted-POVM benchmark. `REFERENCE_FRAME_ACCESS.md` now makes the operation-set caveat explicit: if measurements obey a symmetry and no phase/time reference is available, globally distinct states can become operationally indistinguishable.

Thus the more precise object is

```text
distinguishability under the allowed operations + reference resources.
```

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

## Traveling-wave capture and control precision

For an incident photon, clean one-port critical matching gives

```math
\Gamma_{\rm match}=4G^2/\kappa.
```

At resonance this can yield unit record conversion for **any nonzero `G`** if sufficiently slow/narrowband operation and arbitrarily good rate control are allowed.

Therefore:

> **Peak monochromatic efficiency does not impose a positive atom-count threshold; weak coupling is paid for in bandwidth/time and control range/precision.**

The exact clean mismatch law is

```math
\eta_R
=\frac{4x}{(1+x)^2},
\qquad
x=\Gamma/\Gamma_{\rm match},
```

so

```math
1-\eta_R
=\left(\frac{x-1}{x+1}\right)^2.
```

If a nonzero minimum trapping rate `Gamma_floor` exists, target efficiency `1-epsilon` restores the constrained matter threshold

```math
G^2
\ge
\frac{\kappa\Gamma_{\rm floor}}{4}
\frac{1-\sqrt\epsilon}{1+\sqrt\epsilon}.
```

For identical dipoles this becomes a positive conditional `N_min`.

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

## Unknown timing and parallel channels

If the event can occur in one of `M` independent candidate temporal modes,

```math
\Lambda(z)
=\frac1M\sum_m e^{dz_m-d^2/2}.
```

The false-alarm threshold grows approximately as `sqrt(2 ln M)` at large `M` for fixed small false-alarm probability.

Parallel spatial/readout channels introduce the complementary resource. For independent Gaussian evidence,

```math
\boxed{d_{\rm tot}^2=\sum_jd_j^2.}
```

Thus many known weak channels can compensate weak per-channel evidence, while an **unknown active channel** creates a search/trials penalty analogous to unknown arrival time.

Detector theorems must therefore state total accessible channel count/capacity and whether channel identity is known.

## Reference frames are a detector resource

Take

```math
|\psi_\pm\rangle
=(|0\rangle\pm|1\rangle)/\sqrt2.
```

They are orthogonal globally.

Without an optical phase reference, `U(1)` phase twirling gives the same mixed state for both:

```math
\mathcal G(\rho_+)
=\mathcal G(\rho_-)
=\frac12(|0\rangle\langle0|+|1\rangle\langle1|).
```

So unrestricted trace distance can say `D=1` while a symmetry-restricted reference-free detector has operational distinguishability zero.

This adds

```text
phase/time reference quality + allowed measurement operations
```

to the detector resource ledger.

## Task-specific sensitivity and no universal scalar ranking

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

Crossing spectral decision kernels give task-dependent ranking reversal.

That led to a stronger organizing framework.

## Detector as a statistical / quantum channel

For a declared input family `X`, write the complete classical detector experiment as

```math
\boxed{K_D(y|x)=P_D(Y=y|X=x).}
```

Detector A universally dominates detector B if B can be generated from A by hypothesis-independent post-processing:

```math
\boxed{K_B=T\circ K_A.}
```

Then every decision strategy available with B can be simulated from A.

This is the classical Blackwell/garbling order applied to detector outputs.

If neither detector is a post-processing of the other, they are **incomparable**, and different tasks may legitimately prefer different detectors.

At the microscopic quantum level, the analogous object is

```math
\Phi_D:\rho_{\rm opt}\mapsto\rho_{\rm out},
```

with post-processing order

```math
\Phi_B=\Lambda\circ\Phi_A
```

under the proper quantum comparison conditions.

This gives the current hierarchy:

```text
scalar metric
-> task-specific decision metric
-> detector-channel partial order
-> resource-constrained set of physically achievable channels.
```

## Reset and source-inclusive thermodynamic closure

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

But detector/controller/record-memory closure is **not yet source-inclusive closure**.

A surviving source variable can enable reversible uncomputation:

```math
|x\rangle_S|0\rangle_M
\to
|x\rangle_S|x\rangle_M
\to
|x\rangle_S|0\rangle_M.
```

So a genuine erasure statement must account for all usable side information correlated with `X`, including source/reference degrees of freedom.

Even then, optical or pump nonequilibrium free energy can pay the information-processing cost. The surviving statement is a generalized discarded-information/free-energy resource balance, **not a universal positive heat or external-work quantum per detector event**.

For a simple activated record, long retention plus fast reliable reset still implies a conditional energy-landscape control range,

```math
\Delta E
\ge
k_BT\ln\left[
\frac{\tau_{\rm rec}\ln(1/\epsilon_r)}
{\tau_r[-\ln(1-p_d)]}
\right],
```

when positive. This is a control-range bound, not automatically dissipated work.

## Strongest organizing picture

```text
optical input family / task
-> allowed operations + reference frames
-> optical access / mode overlap
-> mode-weighted interaction resource
-> microscopic transduction
-> acquisition/extraction versus loss
-> persistent record
-> complete conditional output process
-> timing / parallel-channel nuisance structure
-> optimum decision
-> detector-channel partial order
-> record export / local reset
-> source-inclusive information accounting
-> nonequilibrium free-energy accounting for cyclic operation.
```

Every attempted universal scalar/bound has exposed an omitted resource:

```text
atom count             -> coupling/time and mode overlap
peak efficiency        -> bandwidth
weak-coupling matching -> control range / precision
more atoms             -> optical escape
more absorber          -> downstream loss and dark events
fixed-noise SNR        -> hypothesis-dependent statistics
D*                     -> temporal/spectral task structure
known-time score       -> timing-search complexity
per-channel bound      -> parallel channel count
unrestricted D         -> reference-frame / operation access
local reset heat       -> exported record capacity
memory-global erasure  -> surviving source/side information
positive cycle work    -> optical/pump nonequilibrium free energy.
```

## Current frontier

The project should now **deprioritize inventing another universal detector scalar**.

The live question is:

> Can the physically achievable detector channels be characterized by a resource ledger that remains closed under counterexamples?

Attack next with

```text
correlating catalysts;
finite-size / single-shot work fluctuations;
causal latency / maximum power;
spatially distributed adaptive measurement;
resource states that return locally unchanged but accumulate correlations.
```

Only after those attacks should a resource-conversion theorem be attempted.

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
16. `SOURCE_INCLUSIVE_THERMODYNAMIC_CLOSURE.md`
17. `REFERENCE_FRAME_ACCESS.md`
18. `CRITICAL_MATCHING_CONTROL_PRECISION.md`
19. `PARALLEL_CHANNEL_RESOURCE.md`
20. `DETECTOR_CHANNEL_ORDERING.md`

## Research rule

Follow the physics rather than a desired paper result. Preserve failed conjectures and counterexamples. Before novelty language, perform a focused primary-source audit; negative search results are not novelty evidence.
