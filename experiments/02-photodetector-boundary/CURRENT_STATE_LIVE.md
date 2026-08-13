# Current Live State — Experiment 02

**Date:** 2026-08-12  
**Status:** exploratory first-principles theory; detector-channel / resource-ledger formulation active  
**Priority:** unassessed; no novelty claim

This is the current operational pointer. Use `CLAIM_LEDGER.md` for epistemic status and `RESEARCH_LOG.md` for chronology. Detailed algebra belongs in the dedicated derivation files.

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

---

## 1. Current answer to the starting question

Starting question:

> At what point does a collection of atoms become a photodetector?

Current answer:

> **There is no universal atom-count transition. A material system functions as a detector only relative to a specified optical input family, allowed operations/reference resources, accessible output channel, temporal/noise environment, and decision criterion. Under explicit constraints, minimum effective atom numbers, optical depths, interaction actions, rate ratios, control precision, channel counts, or reset resources can emerge.**

The detector boundary is therefore not a phase boundary in matter. It is an **operational channel / decision-performance boundary**.

---

## 2. Minimal quantum criterion

For photon-conditioned accessible detector states,

```math
\rho_D^{(0)},\qquad\rho_D^{(1)},
```

define unrestricted trace distance

```math
\boxed{
\mathcal D_D
=\frac12\|\rho_D^{(1)}-\rho_D^{(0)}\|_1.
}
```

For equal priors,

```math
\boxed{P_{e,\min}=\frac12(1-\mathcal D_D).}
```

This already established:

```text
absorption is not sufficient;
absorption is not universally necessary;
electron-hole generation is not a complete detection event.
```

But `REFERENCE_FRAME_ACCESS.md` adds an important qualification: unrestricted trace distance assumes access to the optimal measurement. Under symmetry-restricted operations without the needed phase/time reference, operational distinguishability can be smaller.

The most precise current statement is therefore:

> **detector performance is distinguishability under the allowed operations and available reference resources.**

---

## 3. Atom count becomes meaningful only after another resource is bounded

A universal positive deposited-energy cost failed. In the stated pure finite-time conditional-unitary model,

```math
\boxed{
\mathcal A_\Delta
\ge
\hbar\arcsin(1-2\epsilon).
}
```

For identical resonant dipoles,

```math
\boxed{G=g\sqrt N.}
```

Perfect transient first-lobe transfer requires

```math
N_{\min}=\left\lceil(\pi/(2g\tau))^2\right\rceil.
```

For unequal couplings,

```math
\boxed{G^2=\sum_j|g_j|^2,}
```

so literal total atom count is not the invariant microscopic resource.

In extended dilute matter this becomes optical depth / column density rather than total `N`.

---

## 4. Persistent record is a rate-matching problem

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

Thus more irreversible trapping is not monotonically better.

---

## 5. Traveling-wave capture: weak coupling can trade against time

For a clean one-port incident photon,

```math
\boxed{\Gamma_{\rm match}=4G^2/\kappa.}
```

Unit monochromatic record conversion is possible for any nonzero `G` if sufficiently slow/narrowband operation and exact matching are allowed.

Therefore peak narrowband efficiency alone imposes no positive `N_min`.

Weak coupling costs bandwidth / interaction time.

---

## 6. Control precision restores a constrained threshold

The clean resonant efficiency versus mismatch ratio

```math
x=\Gamma/\Gamma_{\rm match}
```

is

```math
\boxed{\eta_R=\frac{4x}{(1+x)^2},}
```

so

```math
\boxed{1-\eta_R=\left(\frac{x-1}{x+1}\right)^2.}
```

If the architecture imposes a minimum realizable trapping rate `Gamma_floor`, target efficiency `1-epsilon` requires

```math
\boxed{
G^2
\ge
\frac{\kappa\Gamma_{\rm floor}}{4}
\frac{1-\sqrt\epsilon}{1+\sqrt\epsilon}.
}
```

For identical dipoles this restores a positive constrained `N_min`.

Thus the ideal `G->0` counterexample was using **arbitrarily slow and arbitrarily well-controlled matching dynamics as a free resource**.

---

## 7. Semiconductor bridge

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

Electron-hole generation is the microscopic transduction stage, not the detector boundary.

For independent Poisson dark clicks,

```math
\mathcal D_{\rm click}=\eta_s e^{-R_d\tau},
```

so target error requires

```math
R_d\tau\le-\ln(1-2\epsilon).
```

---

## 8. Electrical output: complete distribution, not one SNR

For common Gaussian covariance,

```math
\boxed{
d^2
=\int\frac{|\tilde s(f)|^2}{S_n^{(2)}(f)}df
=\int\frac{|\tilde p(f)|^2}{\mathrm{NEP}_2^2(f)}df,
}
```

with

```math
P_e=Q(d/2).
```

For a one-pole white-noise short-pulse benchmark,

```math
\boxed{d^2=E^2D^{*2}/(A\tau).}
```

Thus equal scalar `D*` does not imply equal event performance when temporal response differs.

If `C_0 != C_1`, the optimum Gaussian statistic is quadratic and covariance change itself can carry information.

For Poisson counts,

```math
BC
=\exp[-(\sqrt{\mu_1}-\sqrt{\mu_0})^2/2],
```

so conventional shot-noise SNR is only a local approximation to full count-distribution geometry.

The general classical object is the **complete conditional output process**.

---

## 9. Timing and parallelism are independent resources

Unknown arrival time creates a mixture over shifted templates. In the independent-bin benchmark,

```math
\Lambda
=\frac1M\sum_m e^{dz_m-d^2/2}.
```

At fixed small false-alarm probability, the search threshold grows approximately as `sqrt(2 ln M)`.

Parallel known channels behave differently. For independent Gaussian outputs,

```math
\boxed{d_{\rm tot}^2=\sum_jd_j^2.}
```

Many weak channels can therefore compensate weak per-channel evidence.

If the active channel is unknown, channel search introduces a spatial trials penalty analogous to unknown arrival time.

Therefore a detector theorem must state

```text
total accessible channel count / capacity
and
whether active channel identity is known.
```

---

## 10. Reference frames can change accessible information

Consider

```math
|\psi_\pm\rangle
=(|0\rangle\pm|1\rangle)/\sqrt2.
```

Globally they are orthogonal, so unrestricted trace distance is one.

Without an optical phase reference, `U(1)` twirling gives

```math
\mathcal G(\rho_+)
=\mathcal G(\rho_-)
=\frac12(|0\rangle\langle0|+|1\rangle\langle1|),
```

making them indistinguishable to symmetry-invariant measurements.

Hence

```text
same optical states
+ different phase/time-reference resources
-> different achievable detector performance.
```

Reference-frame/coherence resources are therefore independent ledger coordinates, not merely energy.

---

## 11. Task-specific scalar versus universal detector ordering

For a fixed normalized waveform `p(t)=Eq(t)`, define

```math
\mathcal K_D[q]
=\int |\tilde q(f)|^2/\mathrm{NEP}_{2,D}^2(f)\,df,
```

so

```math
E_{\min}
=2Q^{-1}(\epsilon)/\sqrt{\mathcal K_D[q]}
```

in the known-time Gaussian model.

This is useful after the task is fixed.

But crossing detector decision kernels can reverse rankings across waveform tasks, so no universal scalar ordering exists in general.

---

## 12. Detector-channel partial order is the stronger universal comparison

For a declared optical input family `X`, represent a classical detector by

```math
\boxed{K_D(y|x)=P_D(Y=y|X=x).}
```

If detector B can be generated from A by hypothesis-independent post-processing,

```math
\boxed{K_B=T\circ K_A,}
```

then every decision rule available with B can be simulated using A.

So A is universally at least as informative as B for the declared statistical experiment.

If neither detector is a post-processing of the other, they are **incomparable** and task-dependent ranking is expected.

This is the classical Blackwell/garbling structure applied to photodetectors.

At the microscopic level, use quantum detector channels

```math
\Phi_D:\rho_{\rm opt}\mapsto\rho_{\rm out}
```

and the corresponding post-processing comparison under proper quantum conditions.

The current performance hierarchy is therefore

```text
scalar conventional metric
-> task-specific decision metric
-> detector-channel partial order
-> resource-constrained set of physically achievable detector channels.
```

This is currently the cleanest general answer to `which detector is fundamentally better?`

---

## 13. Thermodynamics: source-inclusive closure, not detector-local Landauer

The fixed per-click `k_B T ln2` statement remains rejected.

A local detector can export its record. Even detector/controller/all-record-memory closure is not enough if the original optical/source variable survives as side information:

```math
|x\rangle_S|0\rangle_M
\to
|x\rangle_S|x\rangle_M
\to
|x\rangle_S|0\rangle_M.
```

A true erasure statement must include every usable degree of freedom correlated with `X`.

Even under source-inclusive logical erasure, optical or pump nonequilibrium free energy can pay the information-processing cost.

Therefore no architecture-independent positive heat or externally supplied work per detector event has survived.

The robust endpoint is

```text
identify discarded information
+ retained side information
+ all consumed free-energy resources
-> apply the appropriate second-law/work-cost relation.
```

Thermodynamic irreversibility is a property of the complete resource cycle, not the definition of photodetection.

---

## 14. Current resource ledger

Current known independent coordinates/resources include

```text
optical input family / prior / task
allowed operations
phase/time reference resources
mode overlap / optical access
interaction action / microscopic coupling
interaction time / bandwidth
optical escape / competing loss
record trapping / retention
control rate floor / precision
parallel channel count / occupancy knowledge
complete noise statistics / dark events
timing prior / synchronization
side information / exported-record capacity
nonequilibrium optical/pump free energy
reset / cycle-closure requirements.
```

Every attempted universal bound has failed when one of these was left free.

---

## 15. Current frontier

Do not propose another scalar metric or simple thermodynamic lower bound.

The live question is:

> **Can the set of physically achievable detector channels be bounded by a resource ledger that remains closed under adversarial counterexamples?**

Attack next with

```text
correlating catalysts;
finite-size / single-shot fluctuations;
causal latency / maximum power;
spatially distributed adaptive measurements;
resource states that return locally unchanged but accumulate correlations.
```

Only after those attacks should a resource-conversion theorem be attempted.

A focused primary-source prior-art audit remains mandatory before novelty language.
