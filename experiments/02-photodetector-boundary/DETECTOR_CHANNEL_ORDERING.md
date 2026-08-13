# Detector Channels and Universal Performance Ordering — Experiment 02

**Date:** 2026-08-12  
**Status:** active organizing theorem / established decision-theory structure applied to detectors  
**Priority:** unassessed; no novelty claim

Earlier Experiment-02 work found that scalar detector rankings fail when spectral decision kernels cross. This file asks the stronger question:

> If no scalar can universally rank detectors, is there still a mathematically precise meaning of `detector A is at least as informative as detector B for every decision task`?

The answer is yes: compare the **entire detector channels / statistical experiments**, not one figure of merit.

The underlying ordering is established classical statistical decision theory (Blackwell comparison of experiments) and has quantum-channel analogues. No novelty is claimed for that mathematics.

---

## 1. Detector as a classical statistical channel

Let `X` denote the optical hypothesis / input class.

Examples:

```text
X = photon absent / present;
X = photon number;
X = wavelength class;
X = arrival-time bin;
X = waveform family;
X = source parameter to be estimated.
```

A classical detector produces output `Y` with conditional law

```math
\boxed{
K_D(y|x)=P_D(Y=y|X=x).
}
```

This conditional distribution includes everything:

```text
quantum efficiency;
dark events;
timing jitter;
waveform distortion;
readout noise;
signal-dependent noise;
gain fluctuations;
saturation;
correlated outputs.
```

Thus `K_D` is the full operational detector object for the chosen input family and output access.

---

## 2. Define detector degradation / garbling

Suppose detectors A and B have outputs `Y_A` and `Y_B` for the same input `X`.

Say that B is a hypothesis-independent post-processing of A if there exists a stochastic channel `T` such that

```math
\boxed{
K_B(z|x)
=\int dy\;T(z|y)K_A(y|x).
}
```

Symbolically,

```math
\boxed{K_B=T\circ K_A.}
```

`T` is not allowed to know the true optical hypothesis `x`.

It may only process A's observed output.

---

## 3. Immediate decision-theory consequence

Assume B is generated from A by `T`.

Take **any** decision rule that uses B's output:

```math
\delta_B:z\to a,
```

where `a` is an action / estimate / declaration.

An observer with detector A can reproduce the same outcome statistics by

```text
A output y
-> simulate z from T(z|y)
-> apply B's decision rule delta_B(z).
```

Therefore any risk achievable with B is also achievable with A.

Hence

```math
\boxed{
K_B=T\circ K_A
\Longrightarrow
R_A^*\le R_B^*
}
```

for every prior and loss function in the same decision problem class.

This is the rigorous meaning of

> **A is never worse than B as an information source.**

---

## 4. Why this is stronger than comparing one SNR or D*

A scalar such as

```text
D*;
NEP at one frequency;
peak responsivity;
quantum efficiency;
bandwidth;
matched-filter d;
```

probes only one aspect / task / projection of the detector channel.

Channel degradation asks whether **all** of B's output information is already contained in A's output.

Therefore it captures

```text
all thresholds;
all priors;
all loss functions;
all downstream algorithms;
```

within the stated input/output model.

No one-dimensional normalization is required.

---

## 5. Classical Blackwell ordering

In classical statistical decision theory, Blackwell's comparison of experiments establishes the connection between

```text
being at least as useful for all decision problems
```

and

```text
one experiment being obtainable from the other by hypothesis-independent randomization / garbling
```

under the theorem's conditions.

For Experiment 02, this means the mathematically natural universal detector ordering is not a number but a **post-processing partial order**.

Primary historical sources include David Blackwell's 1951 `Comparison of Experiments` and 1953 `Equivalent Comparisons of Experiments`.

---

## 6. Partial order, not total order

There need not exist a map

```math
K_B=T\circ K_A
```

or

```math
K_A=S\circ K_B.
```

Then neither detector universally dominates the other.

They are **incomparable**.

This is exactly what the earlier crossing-kernel result suggested in a restricted Gaussian setting.

The channel view generalizes it:

```math
\boxed{
\text{incomparable detector channels}
\to
\text{different decision tasks can prefer different detectors.}
}
```

So task-dependent ranking reversal is not an annoyance. It is the expected signature of incomparable statistical experiments.

---

## 7. Binary trace distance is only one projection

For one fixed binary hypothesis pair with equal priors, total variation distance / trace distance determines optimum binary error.

But knowing one distance

```math
\mathcal D
```

does not generally determine whether one full detector channel is a garbling of another.

Thus

```text
same binary error
```

does not imply

```text
same detector information structure.
```

A may retain timing or amplitude information that B discards even if both have the same yes/no error for one thresholded task.

This explains why collapsing detector output to a click can destroy information relevant to later tasks.

---

## 8. Data processing becomes the central monotonicity law

If

```math
K_B=T\circ K_A,
```

then any valid information/divergence measure obeying data processing cannot increase from A to B.

Examples include, under their relevant assumptions,

```text
total variation / trace distance;
relative entropy;
Chernoff-type distinguishability;
Fisher-information structures under suitable channels;
mutual information for specified priors.
```

This unifies several earlier Experiment-02 statements:

```text
gain cannot create missing upstream information;
coarse thresholding can discard information;
added noise cannot improve unrestricted distinguishability unless it brings another correlated resource;
post-processing cannot make a degraded detector universally superior.
```

---

## 9. Quantum detector channel

At the microscopic level, let the detector be a quantum channel

```math
\boxed{
\Phi_D:\rho_{\rm opt}\mapsto\rho_{\rm out}.
}
```

The output may include material, electrical, photonic, or hybrid degrees of freedom available to the observer.

If there exists a hypothesis-independent quantum channel `Lambda` such that

```math
\boxed{
\Phi_B=\Lambda\circ\Phi_A,
}
```

then B is a degraded/post-processed version of A.

Any measurement performed after B can be simulated after A by first applying `Lambda`.

Therefore A is at least as capable for every downstream measurement/decision problem allowed in this framework.

Quantum statistical comparison has subtleties beyond the classical theorem, especially regarding ancillary systems and exact comparison criteria, so the classical equivalence must not be transplanted naively without its quantum conditions.

---

## 10. Reference resources belong in the channel definition

`REFERENCE_FRAME_ACCESS.md` showed that two states can be orthogonal globally but indistinguishable under symmetry-restricted measurements without a phase reference.

Therefore the detector channel/order must specify

```text
allowed operations;
reference frames;
ancillas;
side information;
output subsystem access.
```

Changing those resources changes the effective statistical experiment.

So a detector channel is not merely the material transfer function. It is the **operational channel under a declared resource model**.

---

## 11. Time and waveform tasks fit naturally

For a time-resolved detector, `Y` can be the full sampled waveform / point process rather than one scalar.

A slower detector might be obtainable by filtering a faster detector output:

```math
Y_B=T[Y_A].
```

If the added filter/noise is hypothesis independent and exact, the faster/full-output detector Blackwell-dominates the degraded one.

But two detectors with different noise spectra and response kernels may not be degradations of one another.

Then their task rankings can reverse.

This gives a broader explanation of the equal-`D*`, unequal-`tau` result.

---

## 12. Detector thresholding is explicitly a garbling operation

Suppose a detector produces analog waveform `Y` but electronics retain only

```text
click / no click.
```

Thresholding is a stochastic/deterministic post-processing map

```math
Z=T(Y).
```

Therefore the click detector cannot be universally more informative than the full waveform record from which it was constructed.

This is obvious physically but becomes exact in the channel-order language.

It also clarifies why

```text
quantum efficiency + dark-count rate
```

cannot capture all information present in a time-resolved analog output.

---

## 13. Universal detector equality

Two detector channels are operationally equivalent for the specified decision class if each can be simulated from the other by allowed hypothesis-independent post-processing.

Symbolically,

```math
K_A\succeq K_B
\quad\text{and}\quad
K_B\succeq K_A.
```

This is much stronger than equality of

```text
D*;
NEP;
responsivity;
quantum efficiency;
one error probability.
```

It says the two detectors contain the same decision-relevant information up to reversible/garbling-equivalent representation.

---

## 14. Strongest conceptual result

The detector-performance problem now has a natural hierarchy:

```text
SCALAR METRIC
useful for a specified conventional task/normalization;

TASK-SPECIFIC DECISION METRIC
minimum event energy / Bayes risk for one waveform/prior/loss;

CHANNEL PARTIAL ORDER
whether one detector is at least as informative for every decision problem;

RESOURCE-CONSTRAINED CHANNEL SET
which detector channels are physically achievable with given coupling,
time, bandwidth, free energy, references, memory, control, and parallelism.
```

This hierarchy may be the cleanest general answer yet to the question

> `What does it mean for one photodetector to be fundamentally better than another?`

---

## 15. Relation to the original `when does matter become a detector?` question

The original material-boundary question can now be stated as a channel question:

> **When does the physical interaction between an optical input and a material system generate a nontrivial accessible channel from optical hypotheses to observer-accessible outputs?**

A system is operationally useless for the task if the channel is constant:

```math
K_D(y|x)=K_D(y)
```

for all relevant `x`.

It becomes increasingly detector-like as the induced channel becomes more informative under the allowed resource/measurement model.

There is no required atom-count phase transition in this formulation.

---

## 16. Current research consequence

The search for one generalized detector scalar should be deprioritized.

A stronger program is:

```text
1. characterize detector channels;
2. identify channel partial order / incomparability;
3. derive resource constraints on achievable channels;
4. recover D*, NEP, quantum efficiency, bandwidth, jitter, etc. as task-specific projections.
```

This is a more general performance principle than scalar detectivity.

---

## 17. Status / literature boundary

**KNOWN mathematical framework / DERIVED detector-specific organization.**

No novelty claim is made for Blackwell comparison of experiments, statistical sufficiency, channel degradation, data processing, or quantum statistical comparison.

Historical primary references to audit directly before manuscript use:

```text
D. Blackwell, Comparison of Experiments (1951).
D. Blackwell, Equivalent Comparisons of Experiments (1953), DOI 10.1214/aoms/1177729032.
```

Quantum channel/statistical-experiment comparison also has established literature and requires a dedicated primary-source audit before any formal quantum theorem is stated.
