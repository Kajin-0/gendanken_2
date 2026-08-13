# Single-Shot Resource Closure — Experiment 02

**Date:** 2026-08-12  
**Status:** active finite-size resource-ledger correction  
**Priority:** unassessed; no novelty claim

The current detector resource ledger includes information, side information, free energy, interaction time, bandwidth, control precision, channel count, reference frames, and correlation budgets.

This file attacks a remaining hidden assumption:

> are **average** entropy, free energy, work, and noise resources sufficient to guarantee a single detector cycle?

The answer is generally no in microscopic / finite-copy regimes.

Established one-shot thermodynamics and information processing use fluctuation-sensitive quantities such as smooth entropies / coherent relative entropy rather than ordinary average entropy alone. No novelty is claimed for that mathematics.

---

## 1. Average cost and guaranteed cost are different questions

Let a complete detector cycle require a random work amount `W` because different microscopic event histories demand different resources.

The mean is

```math
\langle W\rangle.
```

But a single-cycle guarantee with tolerated failure probability `epsilon` is naturally described by a work quantile

```math
\boxed{
W_{\epsilon}
=\inf\{w:\Pr(W>w)\le\epsilon\}.
}
```

These quantities can differ arbitrarily.

Therefore

```math
\boxed{
\langle W\rangle
\text{ does not determine }
W_{\epsilon}.
}
```

The same distinction applies to

```text
reset energy;
latency;
peak current;
gain excursion;
dark-event burst size;
required memory;
heat dumped in one cycle.
```

---

## 2. Exact rare-branch example

Take a detector cycle with

```math
W=
\begin{cases}
0,&\text{probability }1-p,\\
W_h,&\text{probability }p.
\end{cases}
```

The average work is

```math
\boxed{\langle W\rangle=pW_h.}
```

For small `p`, this can be tiny even when `W_h` is extremely large.

But the `epsilon`-guaranteed work cap is

```math
\boxed{
W_{\epsilon}
=\begin{cases}
W_h,&\epsilon<p,\\
0,&\epsilon\ge p,
\end{cases}
}
```

for this two-point idealization.

Thus a rare branch can be negligible in the average resource ledger and still completely determine the guaranteed single-cycle requirement.

---

## 3. Detector interpretation

Possible rare branches include

```text
rare high-gain avalanche;
afterpulse burst;
rare long trap-release event;
large reset-energy excursion;
rare source waveform with poor mode overlap;
background fluctuation crossing a nonlinear threshold;
controller branch requiring unusually long correction;
rare high-energy optical input.
```

A detector specified only by average power / average noise / average reset work can therefore be operationally incomplete for a strict reliability target.

---

## 4. Information-processing work cost is one-shot in the microscopic regime

Faist, Dupuis, Oppenheim, and Renner derived a finite-process work-cost result in which the irreversibility of a logical process is quantified by the **smooth max-entropy of discarded information conditioned on the retained output** under their framework.

The ordinary von Neumann/Shannon entropy difference emerges in an appropriate many-copy / macroscopic limit.

This directly supports the present correction:

```math
\boxed{
\text{finite-cycle work requirement}
\ne
\text{ordinary average entropy difference in general}.
}
```

Primary source for later full audit:

```text
P. Faist, F. Dupuis, J. Oppenheim, and R. Renner,
The minimal work cost of information processing,
Nature Communications 6, 7669 (2015),
DOI 10.1038/ncomms8669.
```

Related later work formulates more general microscopic process work costs using coherent relative entropy.

---

## 5. Error tolerance is itself a resource coordinate

One-shot quantities are typically **smoothed** by an allowed approximation/error parameter.

Operationally this means that a detector may ignore sufficiently rare costly branches if the permitted failure budget allows it.

Therefore the resource specification must include not merely

```text
average error probability
```

but which guarantees are required:

```text
Bayes-average decision error;
worst-case input error;
conditional miss probability;
false-alarm probability;
reset failure probability;
resource-overrun probability;
maximum tolerated latency tail.
```

Two detectors with the same average `P_e` can have radically different tail guarantees.

---

## 6. Average free energy does not close a finite-cycle theorem

Suppose two resource states have the same mean nonequilibrium free energy.

They can nevertheless have different distributions over energy/information branches and therefore different one-shot work requirements.

Likewise, two detector cycles can have identical

```text
mean optical energy consumed;
mean pump energy;
mean reset work;
mean information discarded
```

while differing strongly in the probability of large excursions.

Hence a resource theorem stated only in terms of expectation values is vulnerable to fluctuation counterexamples.

---

## 7. Asymptotic averaging recovers simpler thermodynamics

For many independent repeated cycles, typicality can make resource consumption concentrate around an entropy/free-energy rate.

Then conventional average thermodynamic quantities become increasingly predictive per cycle.

This gives a hierarchy analogous to the detector-performance hierarchy:

```text
single-cycle / finite-copy
-> smooth / fluctuation-sensitive resource quantities;

many independent cycles
-> asymptotic entropy / free-energy rates.
```

Thus one must not use an asymptotic rate theorem as a worst-case single-photon detector theorem without an explicit concentration argument.

---

## 8. Repeated cycles may not be independent

`CORRELATING_CATALYSTS.md` showed that hidden correlations can produce memory across cycles.

If detector cycles are correlated,

```text
law-of-large-numbers concentration
```

may fail or converge differently.

Therefore the asymptotic simplification itself requires assumptions such as

```text
independence / mixing;
finite correlation time;
ergodicity;
bounded tails;
controlled catalyst/output correlations.
```

This couples the catalyst-memory problem directly to one-shot thermodynamics.

---

## 9. Single-shot work and detector power are still distinct

Even a bound on one-shot total work

```math
W_{\epsilon}
```

does not specify how quickly that work must be delivered.

If the cycle must complete within time `tau`, a power/latency resource enters separately.

Thus

```math
\boxed{
\text{energy/work budget}
\ne
\text{power/latency budget}.
}
```

This sets up the next attack.

---

## 10. Strongest detector-specific conclusion

The current resource ledger must distinguish at least

```text
mean resource consumption;
finite-cycle distribution/tails;
allowed overrun probability;
worst-case or conditional guarantees;
number of repeated uses;
correlation/memory between uses.
```

Therefore:

> **A detector resource theorem based only on average entropy, free energy, power, or information can fail at the single-event level. The physically relevant resource is a distribution or one-shot guarantee conditioned on an explicit error budget.**

This is especially important for single-photon / rare-event detectors, where the target task is intrinsically finite-event rather than thermodynamic-limit operation.

---

## 11. Resource-ledger update

Add explicitly:

```text
single-shot / finite-copy resource quantiles;
smoothing / allowed resource-overrun probability;
worst-case versus average input specification;
cycle-to-cycle correlation assumptions.
```

Do not compress these into average free energy without proving an asymptotic/concentration regime.

---

## 12. Current next attack

The next missing coordinate is **causal latency / maximum power**.

The existing interaction-action bound and one-shot work/free-energy bounds are integrated quantities.

Ask:

> **If the detector must deliver a decision and reset within finite time while interaction strength and available power are bounded, does a stronger speed-resource bound emerge that cannot be evaded by simply storing the same total action or free energy over a longer process?**

This should be attacked before attempting a final detector-channel resource theorem.
