# Current Live State — Experiment 02

**Date:** 2026-08-12  
**Status:** exploratory first-principles theory; detector-process / resource-ledger formulation active  
**Priority:** unassessed; no novelty claim

This is the current operational pointer. `CLAIM_LEDGER.md` is the epistemic boundary; `RESEARCH_LOG.md` preserves chronology. Detailed algebra belongs in dedicated derivation files.

## Active derivations

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
11. `RESET_AND_CYCLE_CLOSURE.md`
12. `SOURCE_INCLUSIVE_THERMODYNAMIC_CLOSURE.md`
13. `REFERENCE_FRAME_ACCESS.md`
14. `CRITICAL_MATCHING_CONTROL_PRECISION.md`
15. `PARALLEL_CHANNEL_RESOURCE.md`
16. `DETECTOR_CHANNEL_ORDERING.md`
17. `CORRELATING_CATALYSTS.md`
18. `SINGLE_SHOT_RESOURCE_CLOSURE.md`
19. `CAUSAL_LATENCY_AND_CONTROL_STRENGTH.md`

---

## 1. Current answer

Starting question:

> At what point does a collection of atoms become a photodetector?

Current answer:

> **There is no universal atom-count transition. A material system functions as a detector only relative to a specified optical input family, allowed operations/reference resources, accessible output process, temporal/noise environment, and decision criterion. Under explicit constraints, minimum effective atom numbers, optical depths, interaction actions, rate ratios, control precision, channel counts, one-shot resources, or reset resources can emerge.**

The detector boundary is therefore an **operational detector-channel/process boundary**, not a phase boundary in matter.

---

## 2. Microscopic information criterion

For photon-conditioned accessible detector states,

```math
\mathcal D_D
=\frac12\|\rho_D^{(1)}-\rho_D^{(0)}\|_1,
```

with equal-prior unrestricted optimum

```math
P_{e,\min}=\frac12(1-\mathcal D_D).
```

This established that absorption is neither sufficient nor universally necessary, and that electron-hole generation is a transduction stage rather than a universal detector boundary.

`REFERENCE_FRAME_ACCESS.md` adds the necessary qualification: unrestricted trace distance assumes the optimal measurement is allowed. Under symmetry restrictions without an adequate phase/time reference, operational distinguishability can be smaller or vanish.

---

## 3. Atom count becomes meaningful only after another resource is bounded

In the stated finite-time pure conditional-unitary model,

```math
\mathcal A_\Delta
\ge
\hbar\arcsin(1-2\epsilon).
```

For identical resonant dipoles,

```math
G=g\sqrt N.
```

Perfect transient first-lobe transfer requires

```math
N_{\min}=\left\lceil(\pi/(2g\tau))^2\right\rceil.
```

For unequal couplings,

```math
G^2=\sum_j|g_j|^2,
```

so mode-weighted oscillator strength / optical depth is more invariant than total physical `N`.

---

## 4. Persistent record and external capture are rate-matching problems

For a photon initially inside a lossy mode,

```math
P_R
=\frac{4G^2\Gamma}
{(\kappa+\gamma+\Gamma)[4G^2+\kappa(\gamma+\Gamma)]}.
```

The desired trapping rate has a finite optimum; in the clean internal-mode limit,

```math
\Gamma_{\rm opt}=2G.
```

For a clean one-port incident photon,

```math
\Gamma_{\rm match}=4G^2/\kappa
```

can yield unit monochromatic conversion for any nonzero `G` if arbitrarily slow/narrowband and exactly matched dynamics are allowed.

Thus weak coupling can trade against time/bandwidth.

---

## 5. Control precision is an independent resource

For clean one-port mismatch ratio

```math
x=\Gamma/\Gamma_{\rm match},
```

```math
\eta_R=\frac{4x}{(1+x)^2},
```

and

```math
1-\eta_R=\left(\frac{x-1}{x+1}\right)^2.
```

A nonzero realizable rate floor `Gamma_floor` restores a constrained coupling threshold:

```math
G^2
\ge
\frac{\kappa\Gamma_{\rm floor}}{4}
\frac{1-\sqrt\epsilon}{1+\sqrt\epsilon}
```

for target efficiency `1-epsilon`.

The ideal `G->0` result therefore used arbitrarily slow and arbitrarily precise control as a free resource.

---

## 6. Semiconductor bridge

A minimal semiconductor signal-record chain is

```math
\eta_s
=\eta_{\rm mode}(1-e^{-\alpha L})\eta_{eh}P_{\rm col}P_{\rm read},
```

with benchmark

```math
P_{\rm col}
=\frac{\Gamma_{\rm ext}}
{\Gamma_{\rm ext}+\Gamma_{\rm rec}}.
```

For independent Poisson dark clicks,

```math
\mathcal D_{\rm click}=\eta_s e^{-R_d\tau},
```

so target error requires

```math
R_d\tau\le-\ln(1-2\epsilon).
```

More absorber cannot repair an already-failed downstream/dark-event budget.

---

## 7. Electrical readout is a full output-distribution problem

For common Gaussian covariance,

```math
d^2
=\int\frac{|\tilde s(f)|^2}{S_n^{(2)}(f)}df
=\int\frac{|\tilde p(f)|^2}{\mathrm{NEP}_2^2(f)}df,
```

with

```math
P_e=Q(d/2).
```

For a one-pole white-noise short-pulse benchmark,

```math
d^2=E^2D^{*2}/(A\tau).
```

Thus equal scalar `D*` can coexist with different event performance.

If hypothesis covariance differs, the optimum Gaussian statistic is quadratic; covariance change itself can carry information.

Poisson counting similarly has full distribution geometry rather than one universal SNR.

---

## 8. Timing and parallelism are separate resources

Unknown arrival time produces a mixture over shifted templates; in the independent-bin benchmark,

```math
\Lambda
=\frac1M\sum_m e^{dz_m-d^2/2},
```

with large-`M` search thresholds scaling roughly as `sqrt(2 ln M)` at fixed small false-alarm probability.

For known independent Gaussian channels,

```math
d_{\rm tot}^2=\sum_jd_j^2.
```

Thus parallelism can compensate weak per-channel evidence, while unknown active-channel identity creates a spatial search penalty.

---

## 9. Detector-channel ordering replaces a universal scalar leaderboard

For a declared input family `X`, represent the complete classical detector by

```math
K_D(y|x)=P_D(Y=y|X=x).
```

If

```math
K_B=T\circ K_A
```

for hypothesis-independent post-processing `T`, then A can simulate every decision strategy available to B.

This is the classical Blackwell/garbling ordering applied to detectors.

If neither detector degrades to the other, they are incomparable and different tasks can legitimately prefer different detectors.

At the microscopic level, the analogous object is a quantum detector channel

```math
\Phi_D:\rho_{\rm opt}\mapsto\rho_{\rm out},
```

under the proper quantum comparison conditions.

Current performance hierarchy:

```text
scalar conventional metric
-> task-specific decision metric
-> detector-channel partial order
-> resource-constrained achievable detector-channel set.
```

---

## 10. Repeated operation can require a detector process, not a memoryless channel

A catalyst or hidden detector state can return to the same local marginal while becoming correlated with source/output/history systems.

Therefore

```math
\rho'_C=\rho_C
```

does not imply strict cyclic return.

A strict reusable auxiliary requires decoupling such as

```math
\rho'_{CR}=\rho_C\otimes\rho'_R
```

or an explicit residual-correlation budget.

For repeated detector use, the full object may be

```math
P(y_1,\ldots,y_n|x_1,\ldots,x_n)
```

rather than a product of one-use channels.

This connects abstract correlated catalysis to practical detector memory/history effects.

---

## 11. Average resources do not determine one-shot guarantees

For a random cycle resource `W`, define an `epsilon`-guaranteed quantile

```math
W_\epsilon
=\inf\{w:\Pr(W>w)\le\epsilon\}.
```

In general,

```math
\langle W\rangle
```

does not determine `W_epsilon`.

One-shot information thermodynamics likewise uses fluctuation-sensitive smooth quantities in finite processes; ordinary entropy/free-energy rates emerge in appropriate many-copy limits.

Detector resource claims must therefore state whether they concern

```text
mean cost;
resource quantile;
worst-case cost;
allowed resource-overrun probability;
independent or correlated repeated cycles.
```

---

## 12. Power is not interaction strength

Combining the interaction-action result with

```math
\Delta V_I(t)\le V_{\max}
```

gives

```math
\boxed{
\tau
\ge
\frac{\hbar\arcsin(1-2\epsilon)}{V_{\max}}.
}
```

This is a conditional interaction-strength speed bound.

But a degenerate pointer can be rotated rapidly with little net energy deposition, so maximum watts alone do not universally bound detection speed.

A power-latency relation

```math
\tau\ge W_\epsilon/P_{\max}
```

is valid only after a positive one-shot work requirement `W_epsilon` is established for the same charged resource channel.

Precharged free energy can also produce a fast event response while recharge occurs slowly before/after the event.

---

## 13. Causality adds a geometry/output-location latency

If an event at `r` must influence an output at `r_o`, then

```math
\tau_{\rm causal}(r)
\ge
|\mathbf r-\mathbf r_o|/v_c.
```

A size-only `L/c` statement is incomplete because local decisions, multiple output ports, restricted illuminated regions, and spatial parallelism can alter the relevant distance.

Therefore decision latency depends separately on

```text
interaction/state-separation time;
causal propagation to required output;
noise-limited observation/readout;
sequential feedback/control latency.
```

---

## 14. Thermodynamics remains source/resource inclusive

A local detector can export its record; detector-memory reset is not logical erasure if source/reference side information survives and permits reversible uncomputation.

Even source-inclusive logical erasure does not imply positive externally supplied detector work if optical or pump nonequilibrium free energy pays the cost.

The robust thermodynamic endpoint is therefore

```text
identify actually discarded information
+ retained side information/correlations
+ all consumed nonequilibrium free-energy resources
+ one-shot reliability requirement
-> apply the appropriate second-law/work-cost relation.
```

There is no surviving fixed per-click Landauer heat quantum.

---

## 15. Current resource ledger

Current independent coordinates/resources include

```text
optical input family / priors / task
allowed operations
phase/time reference resources
mode overlap / optical access
interaction action / microscopic coupling
maximum interaction strength
interaction time / bandwidth
optical escape / competing loss
record trapping / retention
control rate floor / precision
parallel channel count / occupancy knowledge
complete output/noise statistics and dark events
timing prior / synchronization
side information / exported-record capacity
catalyst correlation / decoupling tolerance
mean versus one-shot resource guarantee
stored free-energy capacity
peak versus average power
output geometry / causal communication constraints
nonequilibrium optical/pump free energy
reset / source-inclusive cycle-closure requirements.
```

Every attempted universal detector bound has failed when a compensating coordinate was left free.

---

## 16. Current frontier

The next attack is **adaptive distributed measurement**:

> Does adaptivity add a genuinely new detector resource coordinate, or is it fully captured by a detector-process framework once controller memory, communication latency, references, pre-shared correlations, and feedback operations are charged?

Only after that attack should a detector-process resource-conversion theorem be attempted.

A focused primary-source prior-art audit remains mandatory before novelty language.
