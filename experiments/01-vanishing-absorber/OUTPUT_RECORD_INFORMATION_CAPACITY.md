# Output-Record Information Capacity — Why Adaptive Branch Information Can Be Exported Instead of Erased

**Date:** 2026-08-08  
**Status:** restricted information/energy corollary built from the adaptive branch-rank theorem and standard bosonic entropy bounds; no novelty claim

## 1. Purpose

`ADAPTIVE_FEEDFORWARD_MODE_CAPACITY.md` shows that compressing many orthogonal possible input modes into a small detector memory by adaptive branching creates a branch/output-record resource.

For a uniform `M`-mode input ensemble with average capture efficiency `eta_bar`, retained detector rank `r`, and successful branch distribution `q_m`, that note gives

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

A naive next step would attach a local Landauer cost to this information.

That is not general because a photodetector can **export** the record as its useful output.

This note asks:

> If the branch information is carried away by a physical bosonic output field rather than erased inside the detector, what resources can carry the required record entropy?

The answer exposes an important trade:

```text
output energy
<->
output mode/time-bandwidth capacity.
```

Energy alone does not bound record dimension.

---

## 2. Output record as distinguishable bosonic states

Suppose successful branch label `m` is exported into mutually distinguishable/orthogonal output states

```math
|R_m\rangle.
```

For branch probabilities `q_m`, the average output-record state is

```math
\rho_R
=
\sum_m q_m |R_m\rangle\langle R_m|.
```

If the states are orthogonal,

```math
\boxed{
S(\rho_R)
=H(q).
}
```

Thus the output physical system must possess enough state entropy to carry at least the branch information required by the adaptive detector.

More generally, if record states are not perfectly orthogonal, the accessible classical information is bounded by their Holevo information and cannot exceed the von Neumann entropy of the average record state.

---

## 3. Finite-mode bosonic entropy ceiling

Assume for a controlled baseline that the record occupies

```math
D_{\rm out}
```

approximately degenerate bosonic modes at carrier frequency `omega_out`, with total mean output excitation number

```math
N_{\rm out}.
```

Among states with fixed mean total boson number, the maximum entropy is achieved by thermal occupation distributed over the available modes.

Define

```math
g(n)
=
(n+1)\ln(n+1)-n\ln n.
```

Then the total output entropy obeys

```math
\boxed{
S(\rho_R)
\le
D_{\rm out}
\,g\!\left(
\frac{N_{\rm out}}
{D_{\rm out}}
\right).
}
```

This is standard bosonic information theory; it is not a repository novelty.

Representative prior theory includes Caves & Drummond, *Reviews of Modern Physics* 66, 481 (1994), and Giovannetti et al., *Physical Review Letters* 92, 027902 (2004).

---

## 4. Record-capacity inequality

Combine

```math
H(M_{\rm branch}|\mathrm{success})
\le
S(\rho_R)
```

for a perfectly exported orthogonal branch record with the adaptive lower bound.

Whenever

```math
M\bar\eta>r,
```

one obtains

```math
\boxed{
D_{\rm out}
\,g\!\left(
\frac{N_{\rm out}}
{D_{\rm out}}
\right)
\ge
\ln\left(
\frac{M\bar\eta}{r}
\right).
}
```

This is a **restricted output-record information-capacity condition**.

It is not a universal detector energy theorem because it assumes

- an explicitly exported distinguishable record;
- approximately degenerate bosonic output modes;
- a mean-excitation constraint;
- no additional nonbosonic record degrees of freedom;
- no pre-shared side information reducing the needed record entropy.

---

## 5. Why output energy alone cannot be the missing universal resource

The most important limit is large output mode count.

Take one output excitation distributed among `D_out` orthogonal temporal modes:

```math
|1_m\rangle,
\qquad
m=1,\ldots,D_{\rm out}.
```

The states are perfectly orthogonal.

For equal probabilities,

```math
N_{\rm out}=1
```

but

```math
\boxed{
H=\ln D_{\rm out}.
}
```

Thus a fixed-energy output event can encode an arbitrarily large branch label if the available output mode/time-bandwidth dimension is allowed to grow.

This is exactly how arrival time itself can serve as the detector record.

Therefore

```text
more possible arrival times
```

does **not** require proportionally more click energy.

It can instead require

```text
more distinguishable output temporal modes.
```

---

## 6. Why output mode count alone is also insufficient

At fixed small `D_out`, increasing bosonic excitation number increases the entropy/coding capacity of the output system.

For large `n`,

```math
g(n)
\simeq
\ln(en).
```

So amplification energy can partially substitute for output-mode dimension.

Conversely, large time-bandwidth can substitute for amplification energy.

The record resource is therefore at least two-dimensional:

```text
output energy / excitation number
+
output mode (space-time-bandwidth) capacity.
```

A theorem depending on either alone is vulnerable to the other.

---

## 7. Long-time output time-bandwidth interpretation

For one output spatial/polarization channel over angular bandwidth `W_out` and long record window `T_obs`, an effective one-excitation temporal-mode count scales as

```math
D_{\rm out}
\sim
\frac{W_{\rm out}T_{\rm obs}}{2\pi}
```

up to basis/edge corrections.

Likewise, an incident one-channel band `W_in` over the same observation window has

```math
M_{\rm in}
\sim
\frac{W_{\rm in}T_{\rm obs}}{2\pi}.
```

The output record can therefore scale its state dimension with observation time just as the incident field does.

This is why an ideal continuous record/output continuum defeats any finite-`d` adaptive mode-capacity theorem as `T_obs -> infinity` unless output bandwidth, channel count, energy, or information flux is also constrained.

---

## 8. Local erasure versus exported record

The adaptive branch information has two limiting fates.

### A. Local cyclic erasure

If the detector/controller stores the branch internally and must reset that record to a standard state, information thermodynamics can impose a Landauer-type free-energy cost under the usual memory/bath assumptions.

### B. Exported useful record

If the branch is emitted as the click time, pulse mode, digital word, or another outgoing record, the local detector need not erase that information.

Instead, the resource appears as output record capacity.

Thus the safe general statement is not

```text
adaptive detection costs kBT ln M locally.
```

It is

> **Adaptive compression of many possible input modes into a small retained detector state requires the missing distinguishability to live somewhere — in controller memory, an output record, or an environment. Whether that distinguishability incurs local thermodynamic work depends on how it is stored, exported, and reset.**

---

## 9. Connection to detector amplification

A macroscopic detector click uses both axes naturally.

- **Amplification** creates a robust/high-energy record.
- **Timing/readout bandwidth** creates many distinguishable temporal output states.

The 2026 autonomous-detector literature already analyzes thermodynamic amplification/reset costs after capture.

The present repository should therefore not claim generic novelty for the statement that reliable amplification costs nonequilibrium resources.

The narrower unresolved question is whether the optical-input access constraints, active-control resources, and output-record capacity can be combined into a useful detector-specific rate theorem.

---

## 10. Current result of the output-continuum attack

The infinite-output-continuum counterexample is genuine.

It invalidates any common space-time detector theorem based only on

```text
finite internal storage rank
+
local controller branch count.
```

A normal detector can continuously export orthogonal records.

To recover a nontrivial always-on law, one must constrain at least one property of that output channel, for example

- output bandwidth / number of channels;
- output energy or power;
- accessible information rate;
- finite reset/dead-time throughput;
- entropy/free-energy flux into the record reservoir.

No single preferred scalar has yet been justified.

---

## 11. Next adversarial target

The candidate common resource law has therefore narrowed again.

The next useful question is:

> **For a cyclic always-on detector with finite input bandwidth, finite output record bandwidth/power, and finite reset throughput, can one derive a nontrivial bound on accepted spatiotemporal-mode rate that survives adaptive/coherent control?**

A natural starting point is not another storage-rank theorem, but a rate balance among

```text
accepted input mode flux
-> output information/entropy flux
-> reset or exported-record flux.
```

Any such result must be collision-tested against standard bosonic communication capacity and quantum-memory multimode-capacity theory before novelty claims.