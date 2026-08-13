# Causal Latency, Interaction Strength, and Power — Experiment 02

**Date:** 2026-08-12  
**Status:** active speed-resource correction  
**Priority:** unassessed; no novelty claim

The current resource ledger contains integrated interaction action, bandwidth/time, one-shot work distributions, control precision, and parallel channel count.

A natural next conjecture is:

> perhaps detector latency is universally bounded by available power.

This file attacks that conjecture.

The key correction is that three physically different quantities must be separated:

```text
interaction-generator strength;
net energy/work flow;
causal propagation/communication time.
```

They are not interchangeable.

---

## 1. Finite interaction strength gives a direct state-separation time bound

From `INTERACTION_ACTION_LOWER_BOUND.md`, for the stated pure conditional-unitary detector model,

```math
\int_0^\tau \Delta V_I(t)\,dt
\ge
\hbar\arcsin(1-2\epsilon).
```

Suppose the conditional interaction generator is bounded during the measurement:

```math
\Delta V_I(t)\le V_{\max}.
```

Then immediately

```math
\boxed{
\tau
\ge
\frac{\hbar\arcsin(1-2\epsilon)}{V_{\max}}.
}
```

For perfect binary discrimination,

```math
\boxed{
\tau\ge\frac{\pi\hbar}{2V_{\max}}.
}
```

This is a genuine speed-resource statement within the same conditional-unitary model.

The relevant resource is the **strength of the hypothesis-dependent generator**, not net dissipated energy.

---

## 2. Why power alone does not imply this bound

Consider the degenerate-pointer construction

```math
H_D=0,
```

with conditional interaction

```math
V
=\frac{\hbar\Omega}{2}\sigma_y.
```

The detector branch can rotate by angle `Omega tau/2` even though the pointer's bare energy remains identically zero.

The state-separation rate is controlled by

```math
\hbar\Omega,
```

not by a required increase in the detector's bare energy.

In an idealized static-coupling model there need not be a continuous net energy flow into the detector proportional to `Omega`.

Therefore

```math
\boxed{
P_{\max}\text{ alone does not universally bound detection speed.}
}
```

One must specify how control Hamiltonian strength is physically generated and what energetic cost is charged.

---

## 3. Hamiltonian norm / variance and power are different resources

A large interaction matrix element can produce rapid coherent rotation while exchanging little average energy.

Conversely, a large power flow can dump heat rapidly without producing much hypothesis-dependent state separation.

Thus

```text
large watts
```

and

```text
large distinguishability-generation rate
```

are not equivalent.

The detector resource ledger must retain both when relevant:

```math
V_{\max}
\quad\text{or another interaction-strength norm},
```

and

```math
P_{\max}
\quad\text{for actual energetic throughput}.
```

---

## 4. A power-latency bound becomes valid only after a positive work requirement is established

Suppose an architecture-specific cycle has a guaranteed work requirement

```math
W_{\epsilon}>0
```

that must be supplied through a resource channel whose instantaneous power obeys

```math
P(t)\le P_{\max}.
```

Then

```math
W_{\epsilon}
\le
\int_0^\tau P(t)dt
\le
P_{\max}\tau,
```

so

```math
\boxed{
\tau
\ge
\frac{W_{\epsilon}}{P_{\max}}.
}
```

This is exact but **conditional**.

Experiment 02 already showed that no architecture-independent positive `W_epsilon` per detection event survives when optical/pump free energy, side information, or reversible transduction are unrestricted.

Therefore this power-latency relation cannot be promoted into a universal detector theorem without first closing the work-resource ledger.

---

## 5. Internal free-energy release can bypass an external-power bound

An avalanche/SPAD-like or metastable detector can store free energy before the photon arrives.

The incident photon acts as a trigger; the fast output pulse is powered largely by the precharged bias/metastable resource.

Then a bound on **external power supplied during the event window** need not limit the pulse speed.

The resource was supplied earlier.

Thus latency accounting must specify whether it charges

```text
pre-event stored free energy;
during-event power;
post-event recharge power;
average cycle power.
```

These are different constraints.

---

## 6. Precharging trades average power against storage

Suppose each event consumes stored free energy `E_s` and the detector must support event rate `R` in steady operation.

Ignoring recovery inefficiency, average recharge power must satisfy

```math
\boxed{
P_{\rm avg}\ge R E_s.
}
```

But the **instantaneous event latency** can be much shorter than

```math
E_s/P_{\rm avg}
```

because energy was accumulated before the event.

This gives another serial resource trade:

```text
slow recharge / stored energy
<->
fast triggered response.
```

A throughput theorem must therefore include storage capacity and duty cycle, not just peak event power.

---

## 7. Causality creates a different latency bound

Now consider a spatially extended detector.

Suppose an optical event may occur at position `r`, but the final decision must be available at a specified output location `r_o`.

No local physical influence can propagate faster than the relevant causal speed `v_c` of the theory/medium, with relativistic vacuum upper bound `c`.

Therefore an event at `r` cannot influence the output earlier than

```math
\boxed{
\tau_{\rm causal}(r)
\ge
\frac{|\mathbf r-\mathbf r_o|}{v_c}.
}
```

For worst-case event location over active region `Omega`,

```math
\boxed{
\tau_{\rm causal}^{\rm worst}
\ge
\frac{1}{v_c}
\sup_{\mathbf r\in\Omega}
|\mathbf r-\mathbf r_o|.
}
```

This is a geometry/output-location bound, not an energetic bound.

---

## 8. Why detector size alone still does not give a universal latency

A claim such as

```math
\tau\ge L/c
```

for a detector of size `L` is too crude.

Counterexamples:

```text
each pixel can make a local decision;
output may be distributed rather than centralized;
event location may already be known;
only a small illuminated subregion may matter;
parallel readout ports can shorten maximum communication distance.
```

Thus causality requires specifying

```text
where the event can occur;
where the decision must appear;
how many output ports exist;
whether local decisions count;
what communication medium/speed is allowed.
```

Again, an apparent size limit becomes a task/architecture limit.

---

## 9. Parallel outputs trade hardware against causal latency

Suppose an active area is divided among `M` spatial output nodes.

Increasing `M` can reduce the maximum distance from an event to its nearest output.

Thus

```text
more spatial channels / readout ports
<->
smaller causal collection latency.
```

This directly couples `PARALLEL_CHANNEL_RESOURCE.md` to the causality problem.

A theorem bounding latency while leaving output-port count free is vulnerable to spatial parallelism.

---

## 10. Adaptive feedforward also consumes causal time

An adaptive detector may perform

```text
weak measurement
-> classical/quantum communication
-> control update
-> further interaction.
```

Every feedback round has a causal/control latency.

If `n_round` sequential adaptive rounds are required and each has minimum round-trip delay `tau_round`, then trivially

```math
\boxed{
\tau_{\rm adapt}\ge n_{\rm round}\tau_{\rm round}.
}
```

The benefit of adaptive measurement must therefore be compared with its communication/control-time resource.

Parallel preprogrammed measurements can avoid this sequential latency at the cost of more hardware/resources.

---

## 11. Decision latency has at least four distinct contributions

A useful decomposition is

```math
\boxed{
\tau_{\rm decision}
\gtrsim
\max\{
\tau_{\rm interaction},
\tau_{\rm propagation},
\tau_{\rm readout}
\}
+\tau_{\rm sequential\ control},
}
```

where the exact combination is architecture dependent.

The terms represent

```text
interaction / distinguishability generation;
causal transport to accessible output;
noise-limited observation/integration;
sequential feedback/control rounds.
```

They should not be collapsed into a single material `time constant` without derivation.

---

## 12. Relation to conventional detector response time

A measured detector time constant may reflect one or several of

```text
carrier lifetime;
transit time;
RC filtering;
thermal relaxation;
trap dynamics;
avalanche buildup;
readout bandwidth;
communication latency.
```

Experiment 02 therefore interprets temporal response operationally:

> **how quickly does the complete detector channel produce enough accessible distinguishability at the required output location to meet the decision target?**

This is broader than one intrinsic lifetime.

---

## 13. Strongest correction

The conjecture

```text
finite power alone imposes a universal detector speed limit
```

fails.

The surviving structure is

```text
interaction-strength bound
-> quantum/state-separation latency;

positive one-shot work + power bound
-> energetic latency;

finite propagation speed + output geometry
-> causal latency;

sequential adaptive control
-> feedback latency.
```

These are independent resource axes.

---

## 14. Resource-ledger update

Add explicitly:

```text
maximum hypothesis-dependent interaction strength;
precharged/stored free-energy capacity;
peak versus average power;
required decision-output location(s);
causal propagation speed;
number/distribution of output ports;
number of sequential adaptive rounds;
control/communication latency.
```

A detector speed theorem must bound the compensating resources rather than quoting one intrinsic time constant.

---

## 15. Current next attack

The next adversarial direction is **adaptive distributed measurement**.

Ask whether a fixed detector channel/resource model misses protocols in which

```text
measurements are interleaved with feedback;
spatial nodes share partial results;
reference resources are dynamically redistributed;
future interactions depend on earlier outcomes.
```

The goal is to decide whether adaptivity creates a genuinely new resource coordinate or can be absorbed cleanly into the general detector-process/channel formalism once causal/control resources are included.
