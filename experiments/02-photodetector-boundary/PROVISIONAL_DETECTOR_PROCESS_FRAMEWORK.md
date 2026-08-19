# Provisional Detector-Process Framework — Experiment 02

**Date:** 2026-08-12  
**Status:** provisional synthesis / adversarial integration target  
**Priority:** unassessed; no novelty claim

This file is the first attempt to synthesize the entire Gedanken path into one framework.

It is deliberately called **provisional**.

The objective is not to declare a theorem prematurely. It is to construct the weakest structure that can reproduce every counterexample and special case already derived, then attack the structure itself.

---

## 1. The starting question after all corrections

The original question

> At what point does a collection of atoms become a photodetector?

has transformed into three distinct questions:

```text
DETECTION
Does the physical system generate accessible information about the optical input?

PERFORMANCE
How well can that information support a specified decision task?

PHYSICAL ACHIEVABILITY
What detector processes/channels can be realized under specified physical resources?
```

These questions must not be collapsed back into one material threshold.

---

## 2. Optical input process

Let `X` denote the optical input hypothesis / parameter / process of interest.

Examples include

```text
photon absent / present;
photon number;
wavelength;
arrival time;
waveform;
spatial location;
polarization;
phase;
source class;
a time sequence of optical events.
```

The prior/input law is part of the task:

```math
\pi(x)
```

for a single-use problem, or a stochastic/quantum input process for repeated operation.

There is no detector performance statement without declaring what optical alternatives must be distinguished or estimated.

---

## 3. Resource model

Define a resource specification `R` containing all physical assumptions that are not to be treated as free.

Current Experiment-02 ledger includes, where relevant,

```text
allowed measurement/control operations;
phase/time reference resources;
optical mode access / overlap;
microscopic interaction strength/action;
interaction time / bandwidth;
optical escape / parasitic loss;
record trapping / retention;
control range / precision;
parallel channel count / geometry;
noise / dark-event statistics;
timing prior / synchronization;
controller memory;
feedback/communication latency;
side information / exported records;
catalyst dimensions / correlation tolerance;
one-shot versus average resource guarantee;
stored free-energy capacity;
peak / average power;
output locations and causal propagation;
optical/pump nonequilibrium free energy;
reset / source-inclusive cycle-closure requirement.
```

The resource model is not assumed complete merely because it is long.

---

## 4. Detector implementation as a physical process

Let `D` denote the detector hardware/physical implementation.

For a fixed input `X=x`, resource model `R`, and allowed control strategy `sigma`, the detector produces accessible outputs.

The output should be broad enough to include

```text
waveforms;
clicks;
timestamps;
spatial channel labels;
controller state;
final material record;
resource use;
decision latency;
reset state.
```

Represent a classical accessible process schematically by

```math
\boxed{
K_{D,\sigma}^{(R)}
(dy\,dt\,dc|x),
}
```

where

```text
y = accessible detector record/output;
t = decision / completion time information;
c = resource-consumption vector.
```

For repeated operation, `K` is generally a process over histories rather than a one-use product channel.

---

## 5. Quantum form

At the microscopic level, the corresponding object is a quantum process/network mapping optical inputs and allowed controls into accessible output systems.

For a one-use memoryless special case,

```math
\boxed{
\Phi_D^{(R)}:
\rho_{\rm opt}
\mapsto
\rho_{\rm out}.
}
```

For multi-round adaptive/memory operation, use a higher-order process / quantum-comb-type object rather than forcing the experiment into one CPTP map.

The exact quantum process formalism is established literature and requires a dedicated primary-source audit before any theorem is stated.

---

## 6. Allowed strategy set

Let

```math
\Sigma_D(R)
```

be the set of physically allowed strategies for detector `D` under resource model `R`.

A strategy may include

```text
fixed measurement;
adaptive stopping;
feedback;
spatial fusion;
reference-field use;
pre-shared correlations;
controller updates;
post-processing;
reset/recycle protocol.
```

This absorbs `adaptivity` into the strategy class rather than treating it as a primitive scalar resource.

---

## 7. Detector capability region

Define the detector capability region as the set of all accessible input-output/resource processes achievable with allowed strategies:

```math
\boxed{
\mathfrak C_D(R)
=
\left\{
K_{D,\sigma}^{(R)}:
\sigma\in\Sigma_D(R)
\right\}.
}
```

This is the central provisional object.

It is generally not a number.

It may be high dimensional or infinite dimensional.

---

## 8. Decision problem

A decision problem `Pi` specifies at least

```text
input prior / uncertainty set;
action space;
loss function;
false-alarm/miss asymmetry;
allowed observation horizon;
latency constraint;
resource-cost constraint;
worst-case versus average requirement.
```

Let a decision rule be

```math
\delta:y\mapsto a.
```

For one classical formulation, risk is

```math
R(\delta,K;\Pi)
=
\mathbb E_{\pi,K}
[\ell(X,\delta(Y))].
```

The optimum detector risk under the resource model is

```math
\boxed{
R_D^*(\Pi|R)
=
\inf_{K\in\mathfrak C_D(R)}
\inf_{\delta\in\Delta(\Pi,R)}
R(\delta,K;\Pi),
}
```

subject to the task's latency/resource constraints.

This reduces detector comparison to ordinary decision theory once the physically achievable process set is known.

---

## 9. Detection boundary becomes task relative

For a specified task `Pi` with target risk `epsilon`, define useful detection as

```math
\boxed{
R_D^*(\Pi|R)\le\epsilon.
}
```

The minimal nontrivial information boundary is weaker:

```text
the accessible output process depends on X
```

under the allowed operations/resources.

Thus there are two distinct notions:

```text
NONTRIVIAL DETECTOR
some optical information is accessible;

USEFUL DETECTOR FOR Pi
specified decision target is achievable.
```

Neither is an atom-count phase transition.

---

## 10. Universal detector dominance

For two detectors A and B under the same declared resource/task universe, define

```math
\boxed{
A\succeq_R B
}
```

if A can do at least as well as B for every admissible decision problem.

Operationally,

```math
R_A^*(\Pi|R)
\le
R_B^*(\Pi|R)
```

for all admissible `Pi`.

In the simple memoryless classical fixed-channel case, established Blackwell theory connects this ordering to hypothesis-independent garbling/post-processing:

```math
K_B=T\circ K_A.
```

For detector processes with memory/adaptivity, the analogous comparison must be defined at the process/strategy level.

---

## 11. No-universal-scalar corollary

Suppose there exist detectors A and B and two admissible tasks `Pi_1,Pi_2` such that

```math
R_A^*(\Pi_1)<R_B^*(\Pi_1),
```

but

```math
R_B^*(\Pi_2)<R_A^*(\Pi_2).
```

Then A and B are task-incomparable.

Any real-valued scalar that insists on a strict total ranking

```text
A better than B
or
B better than A
```

must contradict at least one task.

If it assigns equality, it hides a real operational difference because the detectors are not equivalent.

Therefore:

```math
\boxed{
\text{a complete universal detector ranking cannot generally be represented by one real scalar}
}
```

unless the relevant detector class happens to be totally ordered under the universal decision relation.

This is the general version of the earlier crossing-`NEP(f)` result.

It is a decision-theory consequence, not claimed as new mathematics.

---

## 12. Conventional metrics become projections

The framework should recover conventional detector figures of merit as restricted projections.

Examples:

### Quantum efficiency

For a binary click task with negligible dark counts, quantum efficiency approximates one transition probability inside a highly coarse-grained detector channel.

### Dark-count rate

Specifies part of the null output process and becomes decisive for a thresholded rare-event task.

### NEP

In linear Gaussian stationary readout, NEP enters the noise-weighted waveform distance

```math
d^2
=\int|\tilde p(f)|^2/\mathrm{NEP}_2^2(f)df.
```

### `D*`

Adds conventional area normalization to NEP for a specified frequency/bandwidth convention.

It is therefore a useful task-specific projection, not the full detector channel.

### Bandwidth / response time

Constrains which waveform information reaches the accessible output and affects latency/search resources.

### Timing jitter

Is part of the conditional timestamp distribution rather than an independent universal quality scalar.

---

## 13. Test 1 — perfect absorber with no record

Previous counterexample:

```text
P_abs=1
but
accessible output distribution independent of photon history.
```

In the framework,

```math
K_D(y|H_0)=K_D(y|H_1).
```

The detector process is constant with respect to the task input.

Therefore no nontrivial decision information exists.

**PASS.**

---

## 14. Test 2 — nonabsorptive / QND detector

A dispersive interaction can correlate the surviving photon with an accessible material pointer.

The induced output channel depends on the optical input even though photon destruction does not occur.

**PASS.**

Absorption is implementation-specific, not definitional.

---

## 15. Test 3 — single atom versus many atoms

A single atom can induce a nontrivial channel if coupling/readout resources permit.

Many weak atoms can improve collective coupling.

The framework places atom count inside the physical resource/implementation map that determines `C_D(R)`, not inside the definition of detection.

**PASS.**

---

## 16. Test 4 — weak coupling + arbitrarily long narrowband time

Clean critical matching allows perfect monochromatic conversion for arbitrarily weak nonzero coupling if time/bandwidth and control precision are free.

In the framework, enlarging allowed time/control resources enlarges `C_D(R)` and makes the perfect-conversion process achievable.

Bounding bandwidth/control removes that point.

**PASS.**

---

## 17. Test 5 — semiconductor electron-hole generation

The semiconductor chain

```text
mode access
-> absorption/e-h generation
-> collection versus recombination
-> readout
```

simply generates one particular family of output channels.

Electron-hole generation alone need not make the final channel informative enough for the task.

**PASS.**

---

## 18. Test 6 — equal D*, different response time

The one-pole Gaussian benchmark has

```math
d^2=E^2D^{*2}/(A\tau).
```

Two detectors can share conventional `D*` while inducing different waveform channels and therefore different risks for short events.

The framework predicts no contradiction because equality of one projection does not imply channel equivalence.

**PASS.**

---

## 19. Test 7 — signal-dependent noise

If the optical input changes output covariance/count statistics, the complete conditional distribution changes even if the mean does not.

The framework uses the complete output process, so covariance information is retained.

**PASS.**

---

## 20. Test 8 — unknown arrival time

Arrival time is part of `X` or a nuisance parameter in `Pi`.

Searching many possible times changes optimum risk and latency.

Known-time and unknown-time experiments are different tasks.

**PASS.**

---

## 21. Test 9 — missing phase reference

The resource model `R` specifies allowed operations/reference frames.

Removing the phase reference shrinks the strategy set and can collapse otherwise orthogonal optical inputs into the same operational experiment.

**PASS.**

---

## 22. Test 10 — parallel channels

Channel count/geometry is in `R`.

Known independent evidence can add across channels; unknown active channel modifies the task and creates search cost.

**PASS.**

---

## 23. Test 11 — correlated catalyst / detector memory

Repeated use need not factorize into identical one-use channels.

The framework permits a process over histories and requires the resource model to state correlation/decoupling constraints.

**PASS.**

---

## 24. Test 12 — one-shot resource tails

The resource-consumption vector `c` is part of the joint output/process rather than being represented only by its mean.

A decision/resource problem can constrain a quantile or worst case.

**PASS.**

---

## 25. Test 13 — causal latency / precharged energy

Decision time `t` and stored-energy/power resources are explicitly separate coordinates.

A precharged detector can have small event latency despite low event-window external power; a centralized output remains causally limited by geometry.

**PASS.**

---

## 26. Test 14 — adaptive stopping

Adaptive strategy `sigma` belongs to `Sigma_D(R)`.

The capability process tracks both decision result and random stopping/resource use.

Expected-resource gains without worst-case gains therefore appear naturally.

**PASS.**

---

## 27. Test 15 — source-inclusive thermodynamics

Local reset, source-side information, exported records, catalysts, and free-energy reservoirs live inside the resource/accounting model.

A Landauer-like cost arises only under the corresponding closure assumptions, not from `detection` itself.

**PASS at the organizing level.**

A rigorous thermodynamic process theorem still requires exact one-shot free-energy formalism.

---

## 28. What the framework has not yet proven

Passing known counterexamples does **not** establish completeness.

Open risks include

```text
hidden resource states not represented by R;
indefinite/quantum causal order;
field-theoretic continuum subtleties;
unbounded-dimensional reference/catalyst limits;
non-Markovian baths not captured by declared process boundary;
resource embezzlement / approximate catalysis;
measurement disturbance constraints for unknown quantum states;
computational complexity of optimal decision/control;
physical implementability of abstract post-processing maps.
```

The framework remains provisional.

---

## 29. Strongest current principle

The entire Gedanken experiment now points to the following candidate principle:

> **A photodetector is best characterized not by a universal material threshold or scalar figure of merit, but by the optical-to-accessible-output process it can realize under an explicit physical resource model. Detector performance for a task is the optimum decision performance achievable from that process; universal detector superiority is a process/channel post-processing order; conventional figures of merit are task-specific projections.**

This is an organizing principle, not yet a novelty claim.

---

## 30. Why this is deeper than `photodetection is information transfer`

The earlier statement

```text
photodetection = information transfer / record formation
```

was conceptually useful but incomplete.

It did not specify

```text
which information;
which measurements are allowed;
how timing/noise affects accessibility;
what resource enables the mapping;
how repeated uses correlate;
what downstream task matters;
how to compare two detectors universally.
```

The detector-process framework supplies those missing layers.

---

## 31. Immediate next attack

Before promoting this framework, perform two separate adversarial audits:

### A. mathematical/prior-art audit

Compare directly against

```text
Blackwell statistical experiments;
Le Cam deficiency/comparison;
quantum statistical experiments/channel comparison;
quantum combs/testers/process tensors;
classical/quantum decision theory;
photodetection POVM/instrument theory.
```

Determine whether the proposed detector language is merely a straightforward restatement or whether the resource-constrained detector synthesis has a distinct useful contribution.

### B. physical closure attack

Try edge cases that may still break the resource ledger:

```text
indefinite causal order;
unbounded-dimensional reference/catalyst resources;
continuous quantum fields;
computationally bounded observers;
nonstationary/adversarial source processes.
```

No manuscript or novelty statement should be attempted before those audits.
