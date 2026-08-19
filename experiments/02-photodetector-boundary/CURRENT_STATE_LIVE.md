# Current Live State — Experiment 02

**Date:** 2026-08-12  
**Status:** exploratory first-principles theory; provisional detector-process framework under adversarial audit  
**Priority:** unassessed; no novelty claim

This is the current operational pointer. The epistemic boundary is `CLAIM_LEDGER.md` **plus** `CLAIM_LEDGER_PROCESS_ADDENDUM.md`. `RESEARCH_LOG.md` preserves chronology. Detailed algebra belongs in dedicated derivation files.

## 1. Current answer

Starting question:

> At what point does a collection of atoms become a photodetector?

Current answer:

> **There is no universal atom-count transition. A material system functions as a detector only relative to a specified optical input family, allowed operations/reference resources, accessible output process, temporal/noise environment, and decision criterion. Under explicit physical constraints, minimum effective atom numbers, optical depths, interaction actions, rate ratios, control precision, channel counts, one-shot resources, or reset resources can emerge.**

The detector boundary is therefore an **operational detector-process boundary**, not a phase boundary in matter.

## 2. Strongest provisional framework

For detector implementation `D`, resource model `R`, and allowed strategy `sigma`, let the accessible detector process be represented schematically by

```math
K_{D,\sigma}^{(R)}(dy\,dt\,dc|x),
```

where

```text
x = optical input/hypothesis/process,
y = accessible output/record,
t = decision/completion timing,
c = resource-consumption variables.
```

Define the capability region

```math
\boxed{
\mathfrak C_D(R)
=\{K_{D,\sigma}^{(R)}:\sigma\in\Sigma_D(R)\}.
}
```

For a declared decision problem `Pi`, define optimum risk

```math
\boxed{
R_D^*(\Pi|R)
=\inf_{K\in\mathfrak C_D(R)}
\inf_\delta R(\delta,K;\Pi),
}
```

subject to the task's stated resource and latency constraints.

This is a **provisional organizing framework**, not a proven complete theorem.

## 3. Minimal microscopic information criterion remains useful

For one binary quantum-state task with unrestricted measurements,

```math
\mathcal D_D
=\frac12\|\rho_D^{(1)}-\rho_D^{(0)}\|_1,
```

and

```math
P_{e,\min}=\frac12(1-\mathcal D_D).
```

But `REFERENCE_FRAME_ACCESS.md` shows that unrestricted trace distance can overstate achievable discrimination when allowed measurements lack the necessary phase/time reference. The operational object is therefore distinguishability under the **allowed operations and available reference resources**.

## 4. Atom count is a derived constrained resource, not the definition

A universal deposited-energy-per-event bound failed. In a pure finite-time conditional-unitary benchmark,

```math
\mathcal A_\Delta
\ge
\hbar\arcsin(1-2\epsilon).
```

For identical resonant dipoles,

```math
G=g\sqrt N,
```

with perfect transient first-lobe transfer requiring

```math
N_{\min}=\left\lceil(\pi/(2g\tau))^2\right\rceil.
```

For unequal microscopic couplings,

```math
G^2=\sum_j|g_j|^2,
```

so mode-weighted oscillator strength / optical depth is generally more invariant than total physical `N`.

## 5. Record formation and external capture are rate/resource matching problems

Coherent transfer alone is not persistent record. Adding loss and a record trap yields a finite optimum trapping rate.

For a clean one-port traveling photon,

```math
\Gamma_{\rm match}=4G^2/\kappa
```

can give unit resonant conversion for any nonzero `G` if arbitrarily slow/narrowband and exact matching are allowed.

Thus peak monochromatic efficiency alone gives no positive `N_min`; weak coupling trades against time/bandwidth.

Control precision is a separate resource. With

```math
x=\Gamma/\Gamma_{\rm match},
```

```math
\eta_R=\frac{4x}{(1+x)^2},
```

so a nonzero realizable rate floor restores a positive constrained coupling threshold.

## 6. Semiconductor electron-hole generation sits inside a longer decision chain

A minimal slab is organized as

```math
\eta_s
=\eta_{\rm mode}(1-e^{-\alpha L})\eta_{eh}P_{\rm col}P_{\rm read},
```

with a simple collection benchmark

```math
P_{\rm col}
=\frac{\Gamma_{\rm ext}}
{\Gamma_{\rm ext}+\Gamma_{\rm rec}}.
```

Electron-hole generation is therefore a **microscopic transduction stage**, not the universal detector boundary.

## 7. Electrical-output performance is full-distribution decision geometry

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

For a one-pole white-noise short event,

```math
\boxed{d^2=E^2D^{*2}/(A\tau).}
```

Thus equal conventional `D*` can coexist with different event-detection performance.

If hypothesis covariance/count statistics change with the signal, the full conditional distribution—not one fixed-noise SNR—is the relevant object.

## 8. Timing, parallelism, and adaptive strategies are distinct structural resources

Unknown arrival time creates a search/trials penalty. Known independent channels can add evidence:

```math
d_{\rm tot}^2=\sum_jd_j^2.
```

Unknown active-channel identity creates a spatial search penalty.

Adaptive stopping can reduce expected resource use while leaving the same worst-case depth. In the exact benchmark from `ADAPTIVE_DISTRIBUTED_MEASUREMENT.md`,

```math
P_e=\frac12(1-q)^n,
```

while

```math
\mathbb E[N]
=\frac{1-(1-q)^n}{q}.
```

Adaptivity is therefore treated as an allowed **strategy class**, enabled by controller memory, communication, control precision, reference resources, pre-shared correlations, and stopping-time freedom.

## 9. Universal detector comparison is a partial order on complete channels/processes

For a memoryless classical detector,

```math
K_D(y|x)=P_D(Y=y|X=x).
```

If detector B is obtainable from A by hypothesis-independent post-processing,

```math
\boxed{K_B=T\circ K_A,}
```

then A can reproduce every decision strategy available from B for the same statistical experiment. This is the classical Blackwell/garbling structure applied to detectors.

If neither detector degrades to the other, they are **incomparable**, so different tasks can legitimately prefer different detectors.

The current hierarchy is

```text
conventional scalar metric
-> task-specific decision metric
-> detector-channel/process partial order
-> resource-constrained achievable detector-process set.
```

## 10. Repeated operation may require a process with memory

A catalyst/helper can return with the same local state while accumulating correlations with source/output history. Therefore

```math
\rho'_C=\rho_C
```

does not imply strict cyclic return.

Repeated detector use may require

```math
P(y_1,\ldots,y_n|x_1,\ldots,x_n)
```

rather than a product of one-use channels.

Strict resource reuse requires decoupling or an explicit residual-correlation budget.

## 11. Average resource accounting is not enough for a single guaranteed event

For random cycle resource `W`, define

```math
W_\epsilon
=\inf\{w:\Pr(W>w)\le\epsilon\}.
```

In general `E[W]` does not determine `W_epsilon`. Rare branches can dominate one-event guarantees while barely affecting averages.

Finite-cycle resource statements must therefore specify average versus quantile/worst-case guarantees and allowed resource-overrun probability.

## 12. Detector speed has several independent resource limits

From the interaction-action result, if

```math
\Delta V_I(t)\le V_{\max},
```

then

```math
\boxed{
\tau\ge
\frac{\hbar\arcsin(1-2\epsilon)}{V_{\max}}.
}
```

This is an interaction-strength bound, **not** a power bound.

A power relation

```math
\tau\ge W_\epsilon/P_{\max}
```

is conditional on a positive one-shot work requirement in that charged power channel.

Precharged energy can produce fast event response while recharge happens outside the event window.

Causal output geometry independently gives

```math
\tau_{\rm causal}(\mathbf r)
\ge |\mathbf r-\mathbf r_o|/v_c.
```

## 13. Thermodynamic cost belongs to the full resource cycle, not to detection itself

A local detector can export its record. Even detector/controller/record-memory closure is not enough if the original source/reference variable survives and enables reversible uncomputation.

A true erasure statement must include all usable side information correlated with the optical variable.

Even source-inclusive logical erasure does not imply positive externally supplied detector work if optical or pump nonequilibrium free energy pays the cost.

No fixed per-click Landauer heat quantum has survived.

## 14. Provisional framework has passed all accumulated Experiment-02 counterexamples at organizing level

`PROVISIONAL_DETECTOR_PROCESS_FRAMEWORK.md` explicitly checks the current synthesis against:

```text
perfect absorber with no record;
nonabsorptive/QND detection;
single atom and collective N-dipole capture;
weak-coupling critical matching;
semiconductor e-h generation/collection;
equal D* with different temporal response;
signal-dependent noise;
unknown timing;
missing phase reference;
parallel channels;
correlated catalyst/detector memory;
one-shot resource tails;
causal latency / precharged energy;
adaptive stopping;
source-inclusive thermodynamics.
```

No known counterexample currently forces another primitive conceptual layer beyond **detector process + explicit resource model + strategy/task specification**.

This is **not proof of completeness**.

## 15. Strongest current candidate principle

> **A photodetector is best characterized not by a universal material threshold or scalar figure of merit, but by the optical-to-accessible-output process it can realize under an explicit physical resource model. Detector performance for a task is the optimum decision performance achievable from that process; universal detector superiority is a process/channel post-processing order; conventional figures of merit are task-specific projections.**

Status: **PROVISIONAL ORGANIZING PRINCIPLE / PRIORITY UNASSESSED.**

## 16. Current frontier

Stop adding resource coordinates by default. The next work is two adversarial audits:

### Mathematical / prior-art audit

Compare the provisional framework directly against

```text
Blackwell statistical experiments;
Le Cam comparison/deficiency;
quantum statistical experiments/channel comparison;
quantum combs/testers/process tensors;
classical/quantum decision theory;
photodetection POVM/instrument theory.
```

Determine whether the detector-process formulation is merely a restatement of established theory or whether the resource-constrained photodetector synthesis has a distinct useful contribution.

### Physical closure attack

Test edge cases including

```text
indefinite causal order;
unbounded-dimensional references/catalysts;
continuous quantum fields;
computationally bounded observers;
nonstationary/adversarial source processes.
```

No manuscript or novelty claim should be attempted before these audits.
