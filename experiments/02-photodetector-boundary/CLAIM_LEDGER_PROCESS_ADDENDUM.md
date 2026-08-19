# Claim Ledger Addendum — Detector-Process Framework

**Date:** 2026-08-12  
**Status:** active addendum to `CLAIM_LEDGER.md`  
**Priority:** unassessed; no novelty claim

This addendum advances the epistemic boundary beyond the current base `CLAIM_LEDGER.md` without rewriting or deleting the earlier claim history. Read both files together.

## Status vocabulary

Use the same vocabulary as `CLAIM_LEDGER.md`: **KNOWN**, **DERIVED**, **CHECKED**, **CONDITIONAL**, **CANDIDATE DISTINCT — PRIORITY UNPROVEN**, **INVALIDATED**, **SUPERSEDED**, **OPEN**, **NON-CLAIM**.

---

## P1 — marginal catalyst return is sufficient for strict cyclic reuse
**Status:** INVALIDATED

An auxiliary can satisfy

```math
\rho_C'=\rho_C
```

while becoming correlated with the detector/source/output history. Strict reusable return requires decoupling, e.g.

```math
\rho'_{CR}=\rho_C\otimes\rho'_R,
```

or an explicit residual-correlation budget.

Detailed derivation: `CORRELATING_CATALYSTS.md`.

## P2 — repeated detector operation is always a product of one-use channels
**Status:** INVALIDATED GENERALIZATION

Hidden/catalytic memory can require the full process

```math
P(y_1,\ldots,y_n|x_1,\ldots,x_n)
```

rather than

```math
\prod_kK_D(y_k|x_k).
```

## P3 — average work/free energy determines guaranteed one-event resources
**Status:** INVALIDATED

For random cycle resource `W`, define

```math
W_\epsilon
=\inf\{w:\Pr(W>w)\le\epsilon\}.
```

In general `E[W]` does not determine `W_epsilon`. Rare branches can dominate finite-cycle guarantees while barely affecting averages.

Detailed derivation: `SINGLE_SHOT_RESOURCE_CLOSURE.md`.

## P4 — finite-cycle thermodynamics is completely characterized by ordinary Shannon/von-Neumann entropy
**Status:** INVALIDATED GENERALIZATION

Established one-shot information thermodynamics uses smooth/fluctuation-sensitive quantities for finite logical processes; ordinary entropy/free-energy rates emerge in appropriate asymptotic regimes.

## P5 — maximum external power alone gives a universal detector speed limit
**Status:** INVALIDATED

A strong hypothesis-dependent interaction Hamiltonian can generate rapid state separation with little net detector-energy deposition. Interaction strength, net work flow, stored free energy, and power are distinct resources.

## P6 — bounded interaction strength gives a conditional state-separation latency
**Status:** DERIVED / CONDITIONAL

If

```math
\Delta V_I(t)\le V_{\max},
```

then the existing interaction-action result gives

```math
\boxed{
\tau\ge
\frac{\hbar\arcsin(1-2\epsilon)}{V_{\max}}.
}
```

Detailed derivation: `CAUSAL_LATENCY_AND_CONTROL_STRENGTH.md`.

## P7 — positive one-shot work plus bounded power gives a conditional energetic latency
**Status:** DERIVED / CONDITIONAL

If a specified resource channel must supply `W_epsilon>0` and satisfies `P(t)<=P_max`, then

```math
\boxed{\tau\ge W_\epsilon/P_{\max}.}
```

This is not universal because no architecture-independent positive `W_epsilon` per detection event has survived.

## P8 — precharged energy can trade storage/recharge resources against event latency
**Status:** DERIVED ORGANIZING STATEMENT

Fast triggered response can be powered by free energy stored before the event. Event-window power, stored-energy capacity, recharge power, and average event rate must be distinguished.

## P9 — bare detector size gives a universal `L/c` response-time bound
**Status:** INVALIDATED AS STATED

Causal delay depends on event location, required output location(s), allowed local decisions, output-port distribution, and propagation medium. A conditional bound is

```math
\tau_{\rm causal}(\mathbf r)
\ge
|\mathbf r-\mathbf r_o|/v_c.
```

## P10 — adaptivity is a primitive scalar detector resource
**Status:** SUPERSEDED / REFRAMED

Adaptivity is better represented as an allowed strategy class that conditionally allocates underlying resources: controller memory, sequential interaction opportunities, communication latency, control strength/precision, references, pre-shared correlations, and stopping-time freedom.

Detailed derivation: `ADAPTIVE_DISTRIBUTED_MEASUREMENT.md`.

## P11 — adaptive stopping can reduce expected resource use without reducing the same worst-case depth
**Status:** DERIVED / CONDITIONAL

For the exact three-outcome benchmark in `ADAPTIVE_DISTRIBUTED_MEASUREMENT.md`,

```math
P_e=\frac12(1-q)^n,
```

while

```math
\mathbb E[N]
=\frac{1-(1-q)^n}{q}.
```

As `n` grows, expected samples approach `1/q` while worst-case samples remain `n`.

## P12 — one-use detector channel is sufficient for all adaptive/repeated detector comparisons
**Status:** INVALIDATED GENERALIZATION

Multi-round memory-assisted operation requires a detector process / higher-order strategy description rather than one CPTP/stochastic map alone.

## P13 — provisional detector capability region
**Status:** DERIVED ORGANIZING DEFINITION / PROVISIONAL

For detector implementation `D`, resource model `R`, and allowed strategy set `Sigma_D(R)`, define

```math
\boxed{
\mathfrak C_D(R)
=\{K_{D,\sigma}^{(R)}:\sigma\in\Sigma_D(R)\}.
}
```

A representative accessible process can include output record, completion time, and resource-use variables:

```math
K_{D,\sigma}^{(R)}(dy\,dt\,dc|x).
```

Detailed synthesis: `PROVISIONAL_DETECTOR_PROCESS_FRAMEWORK.md`.

## P14 — task-specific detector performance is optimum decision risk over the capability region
**Status:** DERIVED ORGANIZING DEFINITION / PROVISIONAL

For decision problem `Pi`,

```math
\boxed{
R_D^*(\Pi|R)
=
\inf_{K\in\mathfrak C_D(R)}
\inf_\delta R(\delta,K;\Pi),
}
```

subject to the task's declared latency/resource constraints.

Useful detection at target `epsilon` can then be expressed as

```math
R_D^*(\Pi|R)\le\epsilon.
```

## P15 — universal detector superiority is a process/channel partial order, not generally a scalar total order
**Status:** DERIVED ORGANIZING STATEMENT / ESTABLISHED DECISION-THEORY STRUCTURE

For a memoryless classical special case, if

```math
K_B=T\circ K_A
```

for hypothesis-independent post-processing `T`, detector A can simulate every decision strategy available from B. This is the Blackwell/garbling order applied to detector outputs.

For multi-round processes, the comparison must be lifted to the corresponding process/strategy class.

## P16 — a complete universal scalar detector ranking generally cannot exist on an incomparable detector class
**Status:** DERIVED DECISION-THEORY CONSEQUENCE

If task `Pi_1` prefers A but task `Pi_2` prefers B,

```math
R_A^*(\Pi_1)<R_B^*(\Pi_1),
```

```math
R_B^*(\Pi_2)<R_A^*(\Pi_2),
```

then a scalar that insists on strict total ranking must misrepresent at least one task; scalar equality hides a real operational difference.

## P17 — conventional detector metrics are projections of a richer detector process
**Status:** DERIVED ORGANIZING STATEMENT

Quantum efficiency, dark-count rate, NEP, `D*`, bandwidth, jitter, etc. remain useful under their declared conventions/tasks but do not uniquely determine the full detector process.

## P18 — provisional detector-process framework reproduces all Experiment-02 counterexamples so far
**Status:** CHECKED AT ORGANIZING LEVEL / NOT A COMPLETENESS PROOF

The framework was explicitly checked against the accumulated cases: perfect absorber/no record, QND detection, collective coupling, critical matching, semiconductor carrier collection, equal-`D*` temporal differences, signal-dependent noise, unknown timing, missing references, parallelism, catalyst memory, one-shot tails, causal latency/precharged energy, adaptive stopping, and source-inclusive thermodynamics.

No current counterexample forces an additional primitive conceptual layer beyond detector process + resource model + strategy/task specification.

## P19 — strongest current candidate principle
**Status:** PROVISIONAL ORGANIZING PRINCIPLE / PRIORITY UNASSESSED

> **A photodetector is best characterized not by a universal material threshold or scalar figure of merit, but by the optical-to-accessible-output process it can realize under an explicit physical resource model. Detector performance for a task is the optimum decision performance achievable from that process; universal detector superiority is a process/channel post-processing order; conventional figures of merit are task-specific projections.**

This is not claimed novel.

## P20 — novelty/publication status
**Status:** NON-CLAIM

No manuscript or novelty claim is justified yet. The next required work is a direct mathematical/prior-art audit against statistical experiments, Le Cam comparison/deficiency, quantum statistical experiments/channel comparison, quantum combs/testers/process tensors, photodetection instrument/POVM theory, and related resource-constrained decision frameworks, followed by remaining physical edge-case attacks.
