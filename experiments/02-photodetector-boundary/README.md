# Experiment 02 — The Photodetector Boundary

**Opened:** 2026-08-12  
**Status:** exploratory first-principles Gedanken experiment; provisional detector-process framework under adversarial audit  
**Priority / novelty:** unassessed; **no novelty claim**

## Starting question

> At what point does a simple collection of atoms become a photodetector? If light is absorbed and re-emitted versus absorbed and used to generate charge, where is the boundary?

## Current answer

There is **no universal atom-count transition** at which matter becomes a photodetector.

The strongest current formulation is:

> **A photodetector is best characterized by the optical-to-accessible-output process it can realize under an explicit physical resource model. Detector performance is task dependent; universal detector superiority, when it exists, is a channel/process post-processing order rather than a scalar leaderboard.**

This is a provisional organizing principle, not a novelty claim.

## Why the original atom-count intuition failed

The original question mixed several distinct transitions:

```text
atomic -> molecular -> band-like electronic structure;
bound excitation -> mobile carriers;
optical interaction -> encoded information;
encoded information -> persistent record;
record -> accessible output process;
output process -> decision under noise/timing uncertainty.
```

A single microscopic system can encode photon arrival, while a macroscopic absorber can fail to leave an accessible record. Atom count becomes meaningful only after another compensating resource—coupling, time, bandwidth, control precision, channel count, etc.—is bounded.

## Minimal microscopic benchmark

For one binary quantum-state task with unrestricted measurements,

```math
\mathcal D_D
=\frac12\|\rho_D^{(1)}-\rho_D^{(0)}\|_1,
```

with equal-prior optimum error

```math
P_{e,\min}=\frac12(1-\mathcal D_D).
```

This established that absorption is neither sufficient nor universally necessary.

`REFERENCE_FRAME_ACCESS.md` adds the necessary qualification: operational distinguishability also depends on the allowed operations and available phase/time references.

## Microscopic-to-record chain

The experiment derived and documented:

```text
finite-time interaction-action requirement;
collective N-dipole coupling G=g sqrt(N);
coherent transfer versus persistent record;
rate-matched record trapping;
traveling-wave critical coupling;
mode-weighted coupling G^2=sum |g_j|^2;
optical-depth continuum limit;
semiconductor e-h generation/collection bridge.
```

A key correction is that unit **monochromatic** capture can occur for any nonzero coupling in the clean one-port model if arbitrarily slow/narrowband and exactly controlled matching is free. Finite bandwidth or a control-rate floor restores a positive constrained coupling/`N` threshold.

## Electrical-output decision geometry

For common Gaussian covariance,

```math
d^2
=\int\frac{|\tilde s(f)|^2}{S_n^{(2)}(f)}df
=\int\frac{|\tilde p(f)|^2}{\mathrm{NEP}_2^2(f)}df,
```

and

```math
P_e=Q(d/2).
```

For a one-pole white-noise short event,

```math
\boxed{d^2=E^2D^{*2}/(A\tau).}
```

Thus equal conventional `D*` can coexist with different event-detection performance.

Signal-dependent noise, Poisson counting, unknown arrival time, and parallel channels further show that the complete conditional output distribution/process is more fundamental than one fixed-noise SNR.

## Task-specific metrics versus universal comparison

For a fixed normalized waveform `p(t)=Eq(t)`, a useful task-specific scalar is

```math
\mathcal K_D[q]
=\int |\tilde q(f)|^2/\mathrm{NEP}_{2,D}^2(f)df,
```

with

```math
E_{\min}
=2Q^{-1}(\epsilon)/\sqrt{\mathcal K_D[q]}
```

in the known-time Gaussian model.

But crossing detector decision kernels can reverse rankings across tasks. The stronger universal comparison uses the complete detector channel

```math
K_D(y|x)=P_D(Y=y|X=x).
```

If

```math
K_B=T\circ K_A
```

for hypothesis-independent post-processing `T`, detector A can simulate every decision strategy available from B for the same statistical experiment. If neither detector degrades to the other, they are incomparable and task-dependent ranking is expected.

## Repeated/adaptive detection requires a process description

A detector may retain hidden memory between cycles. A catalyst/helper can return to the same local marginal while becoming correlated with previous source/output histories. Therefore repeated operation need not factorize into identical one-use channels.

Adaptive stopping similarly changes expected resource/latency without necessarily changing the same worst-case depth.

The current framework therefore treats multi-round detection as a **detector process + allowed strategy class**, not merely one transfer function or one-use stochastic map.

## One-shot, causal, and thermodynamic resources

Average work/free energy does not determine a guaranteed one-event resource budget. Finite-cycle resource quantiles and failure/overrun tolerances must be specified.

Interaction strength and power are distinct. With bounded conditional generator strength,

```math
\tau
\ge
\hbar\arcsin(1-2\epsilon)/V_{\max},
```

whereas a power-latency bound requires a separate positive one-shot work requirement.

Precharged energy can trade storage/recharge resources against event latency. Causal propagation additionally depends on event/output geometry and parallel output ports.

Thermodynamic erasure is not the definition of detection. Local reset can export information; surviving source side information can permit reversible uncomputation; optical/pump nonequilibrium free energy can pay cycle costs. No fixed per-click Landauer heat quantum has survived.

## Provisional detector-process framework

For detector implementation `D`, explicit resource model `R`, and allowed strategy `sigma`, represent the accessible process schematically as

```math
K_{D,\sigma}^{(R)}(dy\,dt\,dc|x),
```

where `y` is accessible output, `t` completion/decision timing, and `c` resource use.

Define

```math
\boxed{
\mathfrak C_D(R)
=\{K_{D,\sigma}^{(R)}:\sigma\in\Sigma_D(R)\}.
}
```

For decision problem `Pi`,

```math
\boxed{
R_D^*(\Pi|R)
=\inf_{K\in\mathfrak C_D(R)}\inf_\delta R(\delta,K;\Pi),
}
```

subject to the declared resource/latency constraints.

This framework currently reproduces every Experiment-02 counterexample at the organizing level, but that is **not proof of completeness**.

## Current performance hierarchy

```text
conventional scalar metric
-> task-specific decision metric
-> detector-channel/process partial order
-> resource-constrained achievable detector-process set.
```

Conventional figures such as quantum efficiency, dark-count rate, NEP, `D*`, bandwidth, and jitter remain useful projections under declared tasks/conventions; they are not claimed useless.

## Current frontier

Stop adding resource coordinates by default. Two adversarial audits are now required.

### Mathematical / prior-art audit

Compare directly against

```text
Blackwell statistical experiments;
Le Cam comparison/deficiency;
quantum statistical experiments/channel comparison;
quantum combs/testers/process tensors;
classical/quantum decision theory;
photodetection POVM/instrument theory.
```

Determine whether the current detector-process language is merely a restatement of established theory or whether the resource-constrained photodetector synthesis has a distinct useful contribution.

### Physical closure attack

Test

```text
indefinite causal order;
unbounded-dimensional references/catalysts;
continuous quantum fields;
computationally bounded observers;
nonstationary/adversarial source processes.
```

No manuscript or novelty claim should be attempted before these audits.

## Canonical reading order

1. `AGENTS.md`
2. `CURRENT_STATE_LIVE.md`
3. `CLAIM_LEDGER.md`
4. `CLAIM_LEDGER_PROCESS_ADDENDUM.md`
5. `RESEARCH_LOG.md`
6. `PROVISIONAL_DETECTOR_PROCESS_FRAMEWORK.md`
7. dedicated derivation files cited in those documents

## Research rule

Follow the physics rather than a desired paper result. Preserve failed conjectures, counterexamples, and superseded statements. Before novelty language, perform a focused primary-source audit; negative search results are not novelty evidence.
