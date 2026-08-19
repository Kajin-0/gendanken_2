# Parallel Channel Count as a Detector Resource — Experiment 02

**Date:** 2026-08-12  
**Status:** active hidden-resource derivation  
**Priority:** unassessed; no novelty claim

The resource ledger currently contains coupling, time/bandwidth, mode overlap, noise statistics, timing uncertainty, side information, free energy, reference frames, and control precision.

This file asks whether **parallelism itself** is another independent escape resource.

---

## 1. Independent Gaussian channels

Suppose detector output is divided into `M` statistically independent channels.

For channel `j`, let the signal/noise decision distance be

```math
d_j^2
=\langle s_j,C_j^{-1}s_j\rangle.
```

Because independent Gaussian log-likelihood ratios add, the total distance is

```math
\boxed{
d_{\rm tot}^2
=\sum_{j=1}^M d_j^2.
}
```

For equal priors,

```math
\boxed{
P_e
=Q(d_{\rm tot}/2).
}
```

Thus even if every individual channel is weak,

```math
d_j=d_1\ll1,
```

identical independent channels give

```math
\boxed{
d_{\rm tot}=\sqrt M\,d_1.}
```

Target error `epsilon` requires

```math
\boxed{
M
\ge
\left[
\frac{2Q^{-1}(\epsilon)}{d_1}
\right]^2.
}
```

So unlimited parallel channel count can compensate arbitrarily weak per-channel evidence.

---

## 2. Independent Poisson channels show the same structure

For independent count channels with means

```math
\mu_{0j},\qquad\mu_{1j},
```

the Bhattacharyya coefficient of each channel is

```math
BC_j
=\exp\left[
-\frac12
(\sqrt{\mu_{1j}}-\sqrt{\mu_{0j}})^2
\right].
```

Independence gives

```math
BC_{\rm tot}
=\prod_jBC_j.
```

Therefore

```math
\boxed{
BC_{\rm tot}
=\exp\left[
-\frac12
\sum_j
(\sqrt{\mu_{1j}}-\sqrt{\mu_{0j}})^2
\right].
}
```

The count-distribution separation coordinate is additive across channels.

Again, many weak channels can create strong total discrimination.

---

## 3. Parallelism kills a per-channel universal lower bound

Suppose someone proposes

```text
one detector channel must have at least resource R_min
```

for useful detection.

If `M` independent channels are available and their evidence adds, then each can operate below that proposed threshold while the aggregate detector reaches the decision target.

Therefore

```math
\boxed{
\text{per-channel resource bound}
\not\Rightarrow
\text{system-level detector bound}
}
```

unless total channel count / total resource across channels is constrained.

---

## 4. Relation to atom count

The `N`-dipole model already used collective enhancement

```math
G=g\sqrt N.
```

Parallel channels provide a different route.

One can have

```text
many atoms cooperating coherently in one bright mode
```

or

```text
many weak independent detector modes whose statistical evidence is combined later.
```

Both can improve system-level discrimination, but the scaling and physics differ.

Thus `N` must not silently mix

```text
coherent constituent number
and
independent channel multiplicity.
```

---

## 5. Area and spatial mode count enter through this route

A larger detector area can provide more optical collection area, more independent pixels/channels, or both.

Whether area helps or hurts depends on how signal and noise scale.

This is why area normalization in conventional `D*` cannot by itself capture every task:

```text
area may change signal capture,
noise,
parallel channel count,
spatial localization,
and false-alarm trials.
```

A task-level theorem must specify which of these resources scales with area.

---

## 6. Parallelism also creates a false-alarm cost

Parallel channels are not free in a detection problem with unknown event location.

If the event could occur in any one of `M` channels, searching all channels produces a trials penalty analogous to unknown arrival time.

For independent null statistics with a max threshold,

```math
P_{\rm FA}
=1-[1-p_{\rm FA,1}]^M.
```

At fixed system-level false-alarm probability, the per-channel threshold must rise as `M` grows.

Thus parallelism has two competing roles:

```text
known channel / coherent combination
-> evidence can add constructively;

unknown active channel
-> search complexity / false-alarm burden grows.
```

This is the spatial analogue of the timing-search result.

---

## 7. Known versus unknown channel identity is another hidden assumption

If the signal is present simultaneously in all channels with known weights, the optimum likelihood combines them coherently/statistically and gains `sum d_j^2`.

If exactly one unknown channel contains the event, the alternative hypothesis is a mixture over channel index.

The likelihood becomes a log-sum-exp structure analogous to unknown arrival time.

Therefore

```math
\boxed{
\text{channel count alone is not enough;
channel occupancy knowledge is part of the task.}
}
```

---

## 8. Resource-ledger consequence

Add explicitly:

```text
number of accessible spatial / temporal / polarization / readout channels
and whether the active channel is known.
```

Unlimited channel count can defeat bounds based only on per-channel coupling or information rate.

Conversely, unknown-channel search can make excessive channelization costly.

---

## 9. Emerging duality with time-bandwidth

Earlier:

```text
weak coupling can be compensated by more interaction time.
```

Now:

```text
weak per-channel evidence can be compensated by more parallel channels.
```

These are analogous resource trades:

```math
\boxed{
\text{serial accumulation in time}
\leftrightarrow
\text{parallel accumulation across modes}.
}
```

Any detector throughput theorem that bounds only one while leaving the other free is vulnerable to a counterexample.

---

## 10. Strongest result

For common independent models, the natural information/separation measure is additive across independent channels.

Therefore:

> **A universal detector resource theorem must bound total accessible channel capacity or total additive decision information, not merely the strength of one microscopic channel.**

This is currently another explicit missing coordinate in the Experiment-02 ledger.

---

## 11. Status

The Gaussian and Poisson addition formulas are **DERIVED / KNOWN STATISTICAL STRUCTURE**.

No novelty claim is made for independent-channel likelihood addition.

The detector-specific conclusion is the resource correction:

> **Parallel channel count is an independent resource and can trade against per-channel coupling, time, and noise performance; if channel identity is unknown it also creates a search/false-alarm cost.**
