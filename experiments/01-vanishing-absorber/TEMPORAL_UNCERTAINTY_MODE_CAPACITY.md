# Temporal Uncertainty and Storage-Mode Capacity — Known-Time Capture Is Not Always-On Detection

**Date:** 2026-08-08  
**Status:** exact finite-dimensional single-photon linear-algebra bound; interpretation as detector temporal coverage; no novelty claim  

## 1. Purpose

`TIME_DEPENDENT_CAPTURE_AUDIT.md` shows that a detector whose coupling is synchronized to one known photon temporal mode can capture that mode with very high probability, subject to a coupling-strength x loading-time resource.

That is not yet an always-on detector.

A real detector may not know when the photon will arrive. The photon may occupy one of many possible orthogonal temporal modes.

This note asks:

> How many mutually distinguishable possible arrival modes can a finite coherent storage space absorb before an irreversible readout/reset occurs?

The answer is controlled by the dimension of the receiving storage space, independent of the detailed time-dependent modulation protocol.

---

## 2. Abstract single-photon capture map

Let

```math
\mathcal H_{\rm in}
```

be the temporal-mode Hilbert space of the incoming single photon over a chosen observation interval.

Let

```math
\mathcal H_{\rm s}
```

be the coherent detector storage space available at the end of the loading interval, with finite dimension

```math
\boxed{\dim\mathcal H_{\rm s}=r.}
```

Any linear passive capture protocol with a fixed control schedule defines a contraction

```math
\boxed{
K:\mathcal H_{\rm in}
\to
\mathcal H_{\rm s},
}
```

where

```math
K^\dagger K\preceq I.
```

Time-dependent couplings, cavity detunings, coherent mode mixing, etc. may all be included inside `K`.

The only essential assumptions are

- one-photon linear dynamics;
- no measurement-conditioned adaptation based on knowing which input mode arrived;
- no irreversible counted output continuum during the stated loading interval;
- an `r`-dimensional final coherent storage subspace.

---

## 3. Capture probability of one possible input mode

For a normalized incoming temporal mode

```math
|\psi\rangle\in\mathcal H_{\rm in},
```

the total probability stored in the receiving subspace is

```math
\boxed{
\eta_\psi
=\|K|\psi\rangle\|^2
=\langle\psi|K^\dagger K|\psi\rangle.
}
```

Perfect capture of one specially chosen temporal mode is compatible with

```math
\eta_\psi=1.
```

The issue is simultaneous robustness over many *different possible* temporal modes.

---

## 4. Exact orthogonal-mode sum bound

Let

```math
|\psi_1\rangle,\ldots,|\psi_M\rangle
```

be mutually orthonormal possible incoming temporal modes:

```math
\langle\psi_i|\psi_j\rangle=\delta_{ij}.
```

Define their capture efficiencies

```math
\eta_j
=\langle\psi_j|K^\dagger K|\psi_j\rangle.
```

Then

```math
\sum_{j=1}^{M}\eta_j
=
\operatorname{Tr}
(P_M K^\dagger K),
```

where `P_M` projects onto their span.

Because

```math
0\preceq K^\dagger K\preceq I
```

and

```math
\operatorname{rank}(K)\le r,
```

the eigenvalues of `K^dagger K` lie in `[0,1]` and at most `r` are nonzero.

Therefore

```math
\boxed{
\sum_{j=1}^{M}\eta_j
\le
\operatorname{Tr}(K^\dagger K)
\le
r.
}
```

This is the exact temporal-mode capacity bound.

---

## 5. Uniform efficiency requirement

If every possible arrival mode must be captured with efficiency at least

```math
\eta_j\ge\eta,
```

then

```math
M\eta
\le
\sum_j\eta_j
\le r.
```

Hence

```math
\boxed{
r\ge M\eta.}
```

Equivalently,

```math
\boxed{
M
\le
\frac{r}{\eta}.
}
```

Thus one cannot use one finite coherent storage mode to perfectly capture an arbitrarily large set of mutually orthogonal possible arrival modes with one predetermined control protocol.

---

## 6. Equally likely unknown arrival modes

If the `M` orthogonal arrival modes are equally likely, the average capture probability is

```math
\overline\eta
=\frac1M\sum_j\eta_j.
```

Therefore

```math
\boxed{
\overline\eta
\le
\frac{r}{M}.
}
```

For a single storage mode,

```math
r=1,
```

so

```math
\boxed{
\overline\eta\le\frac1M.
}
```

A perfectly mode-matched active trap for one temporal mode is therefore a poor always-on detector for a large unknown temporal-mode ensemble unless another resource is added.

---

## 7. Arrival-time interpretation

Well-separated time bins carrying the same pulse shape are approximately orthogonal temporal modes.

If the arrival uncertainty spans

```math
M
```

nonoverlapping possible time bins before readout/reset, the bound becomes a temporal-coverage statement:

```math
\boxed{
r\ge M\eta.}
```

Thus high-efficiency acceptance over many possible arrival times requires at least one of

1. many independent coherent storage modes;
2. real-time measurement/adaptation that changes the control after learning something about the arrival;
3. repeated reset/reuse between possible arrival intervals;
4. an irreversible detector output continuum that removes and records the excitation instead of storing all possibilities coherently.

Each option introduces a distinct detector resource.

---

## 8. Why an ordinary always-on detector can evade the storage-rank bound

A photodetector is normally not a finite coherent quantum memory.

An irreversible detector reservoir contains a continuum of output temporal modes. A click at time `t_1` and a click at time `t_2` can leave distinguishable environmental records.

Therefore the receiving Hilbert space for an always-on detector is effectively much larger than a single cavity-storage mode.

That does **not** contradict the bound.

It means that continuous temporal coverage is purchased by coupling to a large irreversible output space—the same detector-side access resource that appeared earlier in the harmonic passive-network theorem.

So the two branches fit together:

```text
finite coherent trap
-> temporal-mode capacity limited by storage rank

continuous irreversible detector
-> many temporal output modes available
-> requires detector-reservoir access / reset / thermodynamic resources.
```

---

## 9. Known-time versus unknown-time detector gedanken

The thought experiment can now be stated sharply.

### Known temporal mode

If the complete temporal wavepacket is known and synchronized, time-dependent impedance matching can tailor the detector to that one mode.

The relevant resource is coupling strength integrated over the loading window.

### Unknown temporal mode / arrival time

If the photon can occupy many orthogonal temporal modes and the control protocol is fixed in advance, a finite storage space cannot capture all of them efficiently.

The relevant resource becomes temporal-mode capacity or irreversible output dimensionality.

Therefore active modulation does not simply erase the passive bandwidth problem. It changes the question from

```text
frequency-domain matching
```

to

```text
how many spatiotemporal input modes can the detector accept and irreversibly record?
```

---

## 10. Relation to quantum-memory literature

Multimode capacity and time-bandwidth product are established central resources in quantum-memory theory.

Dynamic single-photon absorption also has extensive prior work.

This repository therefore does **not** claim novelty for the fact that finite memories have finite multimode capacity.

The value here is organizational: it identifies why a known-time dynamically matched absorber is not a counterexample to an always-on detector access-resource picture.

---

## 11. Weighted arrival prior

For nonuniform prior probabilities

```math
p_j,
\qquad
\sum_jp_j=1,
```

the average efficiency is

```math
\overline\eta
=\sum_jp_j\eta_j.
```

The optimal `r`-dimensional storage subspace can preferentially accept the most likely modes.

For mutually orthogonal arrival modes, the largest possible average capture probability is bounded by the sum of the `r` largest prior probabilities:

```math
\boxed{
\overline\eta_{\max}
\le
\sum_{j=1}^{r}p_j^{\downarrow},
}
```

where `p_j^downarrow` denotes the probabilities sorted from largest to smallest.

This shows explicitly that **arrival-time prior information is a resource**.

If the prior is sharply concentrated, a low-dimensional dynamically controlled detector can cover the likely arrival times efficiently.

If the prior is uniform over many orthogonal possibilities, it cannot.

---

## 12. Claim boundary

### Derived exactly

For a fixed linear capture map into `r` coherent storage dimensions and `M` orthogonal possible input temporal modes,

```math
\boxed{
\sum_j\eta_j\le r.
}
```

Hence uniform target efficiency requires

```math
\boxed{r\ge M\eta.}
```

and equal-prior average efficiency obeys

```math
\boxed{\overline\eta\le r/M.}
```

### Not established

- novelty of this linear-algebra capacity statement;
- a universal mapping between spectral bandwidth and `M`;
- limits with adaptive measurement/feedback;
- limits when irreversible readout occurs continuously during capture;
- a universal thermodynamic cost per storage/output temporal mode;
- a complete always-on detector theorem.

---

## 13. Next decisive direction

The active time-modulation escape has now split into two physically distinct cases:

```text
scheduled/known-mode capture
-> dynamic impedance matching can be nearly perfect
-> finite coupling x loading-time resource

unscheduled/unknown-mode detection
-> finite coherent storage cannot cover arbitrarily many temporal modes
-> requires storage capacity or irreversible output continuum.
```

The next useful step is to connect the temporal-mode count to the autonomous detector output/reset rate and external thermal-background admission.

That would test whether an **always-on time-bandwidth-coverage-dark-count** resource relation exists, rather than another pulse-specific capture formula.