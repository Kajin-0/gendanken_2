# Adaptive and Distributed Detector Strategies — Experiment 02

**Date:** 2026-08-12  
**Status:** active strategy/process-level resource correction  
**Priority:** unassessed; no novelty claim

The current detector framework progressed from

```text
one scalar
-> one task-specific decision metric
-> one detector channel
-> a detector process with memory.
```

The next question is whether **adaptivity** is another independent physical resource, or whether it is better treated as a class of allowed strategies acting on the detector process.

The strongest current answer is:

> **Adaptivity is not a new information source by itself. It is an outcome-conditioned strategy for allocating existing interactions, channels, references, time, memory, and control. Its advantage disappears from a universal resource theorem only when those enabling resources and their worst-case/average costs are explicitly charged.**

Established quantum-comb / quantum-network theory already provides a general framework for multi-round memory-assisted strategies. No novelty is claimed for that formalism.

---

## 1. Fixed detector channel is not enough for an interactive protocol

For a one-use memoryless detector,

```math
K_D(y|x)=P(Y=y|X=x).
```

For a controlled multi-round detector, introduce control/action `a_k` at round `k` and outcome `y_k`.

The physical process is described by conditional laws such as

```math
P(y_k|x,a_{1:k},y_{1:k-1}),
```

or jointly

```math
\boxed{
P(y_{1:n}|x,a_{1:n}).
}
```

An adaptive controller chooses

```math
\boxed{
a_k\sim\pi_k(a_k|y_{1:k-1}).}
```

Thus the final experiment depends on both

```text
the detector process
and
the strategy policy pi.
```

---

## 2. Simple exact stopping-time example

Construct one observation with three possible outcomes

```text
- : conclusive evidence for H0
+ : conclusive evidence for H1
? : ambiguous
```

and symmetric laws

```math
H_0:
P(-)=q,\quad P(?)=1-q,\quad P(+)=0,
```

```math
H_1:
P(+)=q,\quad P(?)=1-q,\quad P(-)=0.
```

Each conclusive outcome is error free.

A fixed protocol that always takes `n` observations spends exactly `n` samples.

An adaptive stopping protocol does:

```text
measure;
if + or - appears -> stop and decide;
if ? appears -> continue;
after n ambiguous outcomes -> guess.
```

The two protocols can be arranged to have the same final decision error.

---

## 3. Exact error probability

The adaptive protocol makes an error only if all `n` observations are ambiguous and the final guess is wrong.

For equal priors,

```math
\boxed{
P_e
=\frac12(1-q)^n.
}
```

Therefore target error `epsilon` requires

```math
\boxed{
n
\ge
\frac{\ln(2\epsilon)}{\ln(1-q)}
}
```

with the appropriate ceiling, since both logarithms are negative for `0<q<1` and `epsilon<1/2`.

The worst-case number of observations remains `n`.

---

## 4. Expected resource use is reduced by adaptivity

The adaptive protocol reaches observation `k` only if the previous `k-1` outcomes were all ambiguous.

Hence

```math
\Pr(N\ge k)=(1-q)^{k-1}.
```

The expected number of observations is

```math
\boxed{
\mathbb E[N]
=\sum_{k=1}^n(1-q)^{k-1}
=\frac{1-(1-q)^n}{q}.
}
```

For large `n`,

```math
\boxed{
\mathbb E[N]\to\frac1q,
}
```

while the fixed protocol always pays `n`.

Therefore adaptivity can produce an arbitrarily large ratio between

```text
fixed worst-case resource
and
average resource consumed
```

as the demanded error is made very small.

---

## 5. But worst-case resource has not disappeared

The adaptive protocol still requires capacity for `n` rounds in the all-ambiguous branch.

Thus

```math
\boxed{
\text{adaptivity can reduce expected cost without reducing the same worst-case cost.}
}
```

This links directly to `SINGLE_SHOT_RESOURCE_CLOSURE.md`.

A detector specification must say whether its resource budget is

```text
mean;
quantile;
worst case;
maximum latency;
average latency.
```

Otherwise adaptive gains can be misreported as fundamental reductions.

---

## 6. Adaptivity reallocates resources conditional on evidence

In a real detector, later actions might be

```text
increase bias;
change integration time;
change optical local-oscillator phase;
open/close a gate;
change bandwidth;
switch gain stage;
route the event to another pixel/channel;
request another measurement;
change threshold;
stop early.
```

The strategy uses early information to decide where to spend later resources.

So the useful interpretation is

```text
adaptivity = conditional resource allocation.
```

It does not create information ex nihilo.

---

## 7. Controller memory is a required physical resource

An adaptive policy must remember enough of the measurement history to choose future actions.

At minimum the controller carries some state `M_k` satisfying

```math
M_{k+1}=F(M_k,y_k)
```

for an appropriate update rule.

Thus adaptive performance depends on

```text
controller state-space dimension;
precision;
retention time;
reset cost;
correlations with detector history.
```

A theorem that grants arbitrary history-dependent control with zero controller memory is incomplete.

---

## 8. Causal feedback latency is another cost

If action `a_{k+1}` depends on outcome `y_k`, information must propagate from the measurement location to the controller and then back to the controlled detector degree of freedom.

Therefore sequential adaptive rounds consume causal/control time.

With `n_round` mandatory sequential rounds and round-trip delay `tau_round`,

```math
\tau_{\rm adapt}
\ge
n_{\rm round}\tau_{\rm round}.
```

This was already identified in `CAUSAL_LATENCY_AND_CONTROL_STRENGTH.md`.

Adaptive information efficiency can therefore trade against latency.

---

## 9. Spatially distributed detection introduces communication architecture

Consider detector nodes

```text
D_1,...,D_M
```

that each observe part of the optical field or part of the detector output.

Possible strategies include

```text
independent local decisions;
centralized fusion;
one-way feedforward;
multiple interactive rounds;
pre-shared random variables;
pre-shared entanglement/correlations;
dynamic routing.
```

These strategies need not have the same achievable decision region under finite communication/time constraints.

Therefore the resource ledger must include the **communication architecture**, not just the number of detector pixels.

---

## 10. Pre-shared correlation can reduce online communication

If distributed nodes share correlated resources before the event, some coordination burden can be shifted from event time to preparation time.

This is the same structural trade already seen with precharged energy:

```text
resource prepared before event
<->
reduced online latency/resource demand.
```

Thus any event-window communication bound must charge

```text
pre-shared randomness;
pre-shared entanglement;
shared reference frames;
precomputed control state.
```

Otherwise the theorem leaves an offline resource free.

---

## 11. Quantum multi-round strategies are naturally process objects

Established quantum-network theory represents sequential memory-assisted transformations using quantum combs / testers and related higher-order channel formalisms.

This supports the current detector move from

```text
one-shot quantum channel
```

into

```text
multi-time detector process / strategy.
```

Primary references for later full audit:

```text
G. Chiribella, G. M. D'Ariano, and P. Perinotti,
Memory Effects in Quantum Channel Discrimination,
Phys. Rev. Lett. 101, 180501 (2008).

G. Chiribella, G. M. D'Ariano, and P. Perinotti,
Theoretical framework for quantum networks,
Phys. Rev. A 80, 022339 (2009).
```

The established theory shows that memory-assisted protocols are relevant for discrimination of channels with memory and provides a general framework for admissible multi-round networks.

No novelty claim is attached to quantum combs/testers.

---

## 12. Adaptivity is strategy, not necessarily primitive resource

Suppose the resource model already specifies

```text
allowed multi-round operations;
controller memory;
communication links and latency;
control strength/precision;
references;
pre-shared correlations;
worst-case/average round count.
```

Then `adaptivity` itself need not be added as another scalar resource.

It is part of the optimization over allowed strategies.

This is conceptually cleaner:

```math
\boxed{
\text{physical resource constraints}
\to
\text{allowed strategy set}
\to
\text{achievable detector processes/channels}.
}
```

---

## 13. Stopping time becomes part of the detector output/resource pair

For adaptive detection the final decision time `T_dec` is random and correlated with the observed evidence.

Therefore a full detector performance description may require the joint distribution

```math
\boxed{
P(\hat X,T_{\rm dec},R_{\rm used}|X),
}
```

where `R_used` denotes resources actually consumed.

This is substantially richer than

```text
one response time + one D* + one error rate.
```

It also reveals a new Pareto structure:

```text
error
versus
latency distribution
versus
resource-consumption distribution.
```

---

## 14. Universal comparison of adaptive detectors

The Blackwell/channel-order idea must be lifted from one-use output distributions to complete interactive processes.

A process A universally dominates process B only if every admissible strategy/output experiment obtainable from B can be simulated from A within the same allowed-resource class.

In quantum theory this enters higher-order channel / comb comparison rather than ordinary state trace distance alone.

The exact mathematical comparison theorem depends on the declared strategy class and is **OPEN** for the detector-specific program.

---

## 15. Strongest conclusion

The adaptive attack does **not** require adding a mysterious `adaptivity resource` scalar.

Instead it forces a structural upgrade:

```text
memoryless detector channel
-> detector process with memory
-> allowed adaptive strategy class
-> joint error/latency/resource performance region.
```

Physical resources that enable adaptive advantages are

```text
controller memory;
sequential interaction opportunities;
causal communication;
control precision/strength;
reference resources;
pre-shared correlations;
stopping-time freedom.
```

Therefore:

> **Adaptivity is best understood as a strategy that converts these underlying resources into a different point on the detector error–latency–resource frontier.**

---

## 16. Current program consequence

The candidate final abstract object is no longer simply a detector channel.

It is closer to

```text
RESOURCE-CONSTRAINED DETECTOR PROCESS
=
input optical process
+ allowed interaction network
+ memories/references/controls
-> joint accessible output process.
```

Conventional detector metrics become projections of this process onto particular tasks and operating assumptions.

---

## 17. Current next question

The major planned loopholes have now been attacked individually.

The natural next move is **not** to add another resource immediately.

Instead:

> **Attempt a provisional detector-process resource theorem / definition, then adversarially test whether it reproduces every previously derived counterexample and special case without hiding a free resource.**

If the provisional framework cannot simultaneously contain

```text
single atom / QND detection;
collective N-dipole capture;
critical coupling;
semiconductor e-h collection;
D* / matched-filter limits;
signal-dependent noise;
unknown timing;
reference-frame restrictions;
parallel channels;
correlated memory/catalysts;
one-shot resource tails;
causal/adaptive strategies;
source-inclusive thermodynamics,
```

then the framework is still incomplete.
