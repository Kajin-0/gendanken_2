# Adaptive Feedforward Mode Capacity — Storage Rank Times Branch Rank

**Date:** 2026-08-08  
**Status:** exact finite-dimensional quantum-instrument bound; linear-algebra/information-theory ingredients are standard; detector interpretation only; no novelty claim

## 1. Purpose

`TEMPORAL_UNCERTAINTY_MODE_CAPACITY.md` established that a **fixed** linear capture map into `r` retained detector modes obeys

```math
\sum_{j=1}^M \eta_j \le r
```

for `M` orthogonal possible input modes.

A natural attack is adaptive control:

> Measure or coherently sort which input mode is arriving, then apply branch-dependent feedforward so that many different input modes can be routed into the same small detector memory.

This attack succeeds against the old `r`-only statement.

But the missing rank reappears in the controller/output branch space.

The exact finite-dimensional result is

```math
\boxed{
\sum_{j=1}^{M}\eta_j
\le
r d,
}
```

where `d` is the number of distinguishable successful adaptive branches and each branch terminates in at most `r` retained detector modes.

Thus uniform efficiency `eta_j >= eta` requires

```math
\boxed{
r d \ge M\eta.
}
```

The fixed-protocol theorem is the special case `d=1`.

---

## 2. Quantum-instrument model

Let the relevant input subspace be

```math
\mathcal H_{\rm in}
=\operatorname{span}\{|1\rangle,\ldots,|M\rangle\}.
```

The modes may be temporal, spectral, spatial, polarization, or any orthogonal single-photon modes.

Let the retained detector/storage Hilbert space have dimension at most

```math
r.
```

Model `d` distinguishable **successful** adaptive outcomes by Kraus maps

```math
K_m:
\mathcal H_{\rm in}
\to
\mathcal H_{\rm store},
\qquad
m=1,\ldots,d.
```

All unsuccessful/loss outcomes may be grouped into additional Kraus operators that are not counted as successful capture.

Trace nonincrease of the successful instrument implies

```math
\boxed{
\sum_{m=1}^{d}K_m^\dagger K_m
\preceq I.
}
```

For input mode `|j>`, define successful capture probability

```math
\boxed{
\eta_j
=
\sum_{m=1}^{d}
\langle j|K_m^\dagger K_m|j\rangle.
}
```

No assumption is made that branch `m` perfectly identifies input label `j`.

---

## 3. Exact branch-rank theorem

Sum over the complete orthonormal input set:

```math
\sum_{j=1}^{M}\eta_j
=
\sum_{m=1}^{d}
\operatorname{Tr}(K_m^\dagger K_m).
```

For every branch,

```math
K_m^\dagger K_m\preceq I
```

because it is one positive term in a sum bounded by the identity.

Also,

```math
\operatorname{rank}(K_m^\dagger K_m)
=\operatorname{rank}(K_m)
\le r.
```

Therefore every eigenvalue of `K_m^dagger K_m` lies in `[0,1]`, with at most `r` nonzero eigenvalues, so

```math
\operatorname{Tr}(K_m^\dagger K_m)
\le r.
```

Summing the `d` successful branches gives

```math
\boxed{
\sum_{j=1}^{M}\eta_j
\le rd.
}
```

Together with the trivial probability bound `sum eta_j <= M`,

```math
\boxed{
\sum_j\eta_j
\le
\min(M,rd).
}
```

For a uniform efficiency floor

```math
\eta_j\ge\eta,
```

```math
M\eta
\le
\sum_j\eta_j
\le rd,
```

hence

```math
\boxed{
rd\ge M\eta.
}
```

QED.

---

## 4. Tightness

The bound is exactly achievable as a finite-dimensional linear-algebra statement.

Suppose

```math
M=rd.
```

Partition the `M` input basis states into `d` disjoint groups of size `r`.

For branch `m`, let `K_m` be an isometry from the corresponding `r`-dimensional input group onto the same `r`-dimensional detector-storage space and zero on every other group.

Then

```math
\sum_m K_m^\dagger K_m=I_M
```

and

```math
\eta_j=1
```

for every input mode.

Thus adaptive branching can really replace detector storage dimension one-for-one:

```text
retained detector rank x distinguishable branch rank
```

is the relevant finite-dimensional capacity.

For `r=1`, `d=M`, one storage mode can accept all `M` orthogonal inputs if the controller/output possesses `M` orthogonal branch states.

---

## 5. Coherent controller version

A classical measurement is not required for the rank accounting.

Suppose the controller remains coherent and has an auxiliary Hilbert space of dimension `d`.

A successful contraction maps

```math
\mathcal H_{\rm in}
\to
\mathcal H_{\rm store}\otimes\mathcal H_{\rm ctrl},
```

whose dimension is at most

```math
rd.
```

The same singular-value/rank argument gives the same accepted-mode trace bound.

Therefore replacing measurement-and-feedforward by coherent noncommuting control does not make the branch resource disappear; it moves it into controller Hilbert-space dimension.

An infinite-dimensional external controller or output continuum lies outside this finite-rank theorem and is a genuine escape resource.

---

## 6. Outcome entropy for a uniform input ensemble

There is also a useful information-theoretic corollary.

Assume the `M` orthogonal input modes are equally likely.

The unconditional probability of successful branch `m` is

```math
p_m
=
\frac1M
\operatorname{Tr}(K_m^\dagger K_m).
```

Since each branch trace is at most `r`,

```math
\boxed{
p_m\le\frac rM.}
```

Let average success probability be

```math
\bar\eta
=
\sum_m p_m
=
\frac1M\sum_j\eta_j.
```

Conditioned on successful capture, the branch distribution is

```math
q_m=\frac{p_m}{\bar\eta},
```

so

```math
q_m
\le
\frac{r}{M\bar\eta}.
```

The Shannon entropy is at least the min-entropy. Using natural logarithms,

```math
\boxed{
H(M_{\rm branch}|\mathrm{success})
\ge
\max\left[
0,
\ln\left(\frac{M\bar\eta}{r}\right)
\right].
}
```

For perfect capture with `M` divisible by `r`, the partition construction above gives exactly `M/r` equiprobable branches and saturates

```math
H=\ln(M/r).
```

Thus adaptive compression of many orthogonal input modes into a small retained detector space necessarily creates branch information somewhere in the successful instrument.

---

## 7. Restricted Landauer baseline — not a universal detector work bound

If the successful branch label is stored in a symmetric/degenerate classical controller memory, the controller is operated cyclically, the record is reset to a standard state in contact with a bath at temperature `T_c`, and no side information or reversible export is used, the usual Landauer baseline gives

```math
W_{\rm erase|success}
\ge
k_B T_c
H(M_{\rm branch}|\mathrm{success}).
```

Under those assumptions,

```math
\boxed{
W_{\rm erase|success}
\ge
k_BT_c
\max\left[
0,
\ln\left(\frac{M\bar\eta}{r}\right)
\right].
}
```

This is **not** an intrinsic photodetector dissipation theorem.

Why not:

- the branch record may be exported as the useful detector output rather than erased locally;
- a continuous output field can carry the record away irreversibly;
- memory energetics need not be symmetric/degenerate;
- side information can reduce erasure cost;
- a coherent controller need not decohere into a classical branch record until later.

The safe conclusion is therefore about **information/output capacity**, not mandatory local work.

Primary thermodynamic background includes Sagawa & Ueda, *Physical Review Letters* 102, 250602 (2009), and standard Landauer erasure theory.

---

## 8. Space-time form

For one propagating spatial/polarization channel restricted to an angular-frequency band `W` and a long observation window `T_obs`, the effective number of orthogonal temporal degrees of freedom scales as the usual time-bandwidth/Shannon number

```math
M
\simeq
\frac{W T_{\rm obs}}{2\pi}
```

up to edge/basis-convention corrections.

The finite-branch theorem then becomes approximately

```math
\boxed{
r d
\gtrsim
\eta
\frac{W T_{\rm obs}}{2\pi}.
}
```

Equivalently, defining branch-information capacity

```math
I_{\rm branch}^{\max}=\ln d,
```

```math
\boxed{
I_{\rm branch}^{\max}
\gtrsim
\ln\left(
\frac{\eta W T_{\rm obs}}
{2\pi r}
\right)
}
```

whenever the logarithm is positive.

This is a **finite-dimensional adaptive space-time mode-capacity statement**, not a universal always-on detector theorem.

Quantum memories already use time-bandwidth product and explicit multimode capacity as distinct physical resources, so this scaling language has strong prior-art overlap.

---

## 9. Physical adaptive counterexample

Temporal-mode sorting is physically meaningful, not merely abstract.

Established quantum-frequency-conversion / quantum-pulse-gate work can separate orthogonal temporal modes into different output channels.

Representative prior work includes

- Reddy, Raymer & McKinstrie, *Optics Letters* 39, 2924 (2014), DOI `10.1364/OL.39.002924`;
- Serino, Eigner, Brecht & Silberhorn, *Optics Express* 33, 5577 (2025), DOI `10.1364/OE.544206`.

A mode sorter followed by branch-dependent routing is therefore a concrete implementation of the resource counted by `d`.

No novelty is claimed for temporal-mode sorting.

---

## 10. What actually happened to the old rank bound

The fixed-map result

```math
\sum_j\eta_j\le r
```

was not universal once adaptive input-dependent branching was admitted.

It generalizes to

```math
\boxed{
\sum_j\eta_j\le rd.
}
```

The resource migration is

```text
storage-mode rank
        |
        | adaptive sorting/feedforward
        v
storage-mode rank x controller/output branch rank.
```

So adaptive control is a genuine escape, but not a free one.

---

## 11. Most important counterexample to overinterpretation

A normal continuously operating photodetector already couples to an effectively enormous output/environmental record space.

Different arrival times can produce orthogonal or macroscopically distinguishable records in that output continuum.

In the ideal continuum limit,

```math
d\to\infty,
```

and the finite-branch theorem becomes nonrestrictive.

Therefore this result **does not** prove a universal finite mode capacity for always-on photodetection.

Instead it identifies the resource that the finite-storage theorem had omitted:

> an always-on detector needs sufficient retained storage **or** sufficient controller/output/environment record dimension to accommodate the accepted orthogonal input modes.

---

## 12. Current conclusion

Adaptive measurement/feedforward kills any universal theorem based only on detector storage rank.

A correct finite-dimensional statement is

```math
\boxed{
\text{accepted-mode trace}
\le
\text{retained detector rank}
\times
\text{successful branch rank}.
}
```

For a cyclic controller that must erase its own branch record, information thermodynamics can attach a work cost under additional assumptions. But a detector can export that information into its output record, so local Landauer cost is not fundamental.

The next adversarial question is therefore not whether adaptive feedback works—it does.

It is:

> **Can the branch/output record itself be given a physically meaningful rate/energy capacity that combines with passive access, active pump strength, background occupation, and reset/dead-time into a nontrivial always-on detector law?**

Do not promote this finite-rank identity as a novel quantum-information theorem.