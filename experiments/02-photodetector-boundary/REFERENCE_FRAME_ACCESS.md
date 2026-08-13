# Reference-Frame Access as a Detector Resource — Experiment 02

**Date:** 2026-08-12  
**Status:** active hidden-resource counterexample  
**Priority:** unassessed; no novelty claim

The current operational detector criterion uses trace distance between photon-conditioned states. That assumes access to the measurement needed to attain the trace-distance optimum.

This file asks what happens when allowed detector operations obey a symmetry because the apparatus lacks an external reference frame.

---

## 1. Unrestricted distinguishability is not always operationally accessible

For two states `rho_0,rho_1`, unrestricted binary discrimination uses

```math
\mathcal D
=\frac12\|\rho_1-\rho_0\|_1.
```

But suppose all allowed detector operations must be invariant under a symmetry group `G`.

Then the detector cannot access degrees of freedom that transform nontrivially under that symmetry unless an appropriate reference resource is supplied.

A useful representation is the group-twirled state

```math
\boxed{
\mathcal G(\rho)
=\int_G dg\;U_g\rho U_g^\dagger.
}
```

For symmetry-invariant measurements, the effective distinguishability is bounded by / represented through

```math
\boxed{
\mathcal D_G
=\frac12
\|\mathcal G(\rho_1)-\mathcal G(\rho_0)\|_1.
}
```

Thus

```math
\mathcal D_G\le\mathcal D.
```

The difference is a hidden **reference-frame resource**.

---

## 2. Exact optical phase example

Take

```math
|\psi_+\rangle
=\frac{|0\rangle+|1\rangle}{\sqrt2},
```

```math
|\psi_-\rangle
=\frac{|0\rangle-|1\rangle}{\sqrt2}.
```

These states are orthogonal:

```math
\langle\psi_+|\psi_-\rangle=0.
```

Therefore unrestricted trace distance is

```math
\boxed{\mathcal D=1.}
```

Now suppose the detector has no optical phase reference and allowed operations are invariant under

```math
U_\phi=e^{-i\phi \hat N}.
```

Phase twirling gives

```math
\mathcal G(\rho_+)
=\mathcal G(\rho_-)
=\frac12
\left(
|0\rangle\langle0|
+|1\rangle\langle1|
\right).
```

Hence

```math
\boxed{\mathcal D_{U(1)}=0.}
```

So two globally orthogonal optical states can be completely indistinguishable to a detector lacking the needed phase reference.

---

## 3. Add a reference and distinguishability returns

Supply a phase-reference system `R`, for example a coherent reference field or another state that breaks the `U(1)` symmetry operationally.

The joint detector can now compare relative phase between signal and reference.

The exact recovered distinguishability depends on the reference state and allowed interaction.

In the ideal large-reference limit the originally hidden phase distinction can become operationally accessible.

Therefore

```math
\boxed{
\text{same signal states}
+\text{different reference resources}
\to
\text{different achievable detection performance}.
}
```

This is a direct counterexample to a resource ledger containing only the signal state, detector material, and energy budget.

---

## 4. Why reference-frame resource is not identical to energy

Two auxiliary states can have similar or even identical mean energy while providing different coherence / phase-reference quality.

The useful resource is not simply

```text
more joules.
```

It is asymmetry/coherence relative to the symmetry that constrains the allowed detector operations.

Thus nonequilibrium free energy alone need not specify the operational measurement capability when control operations obey symmetry restrictions.

This is an established resource-theory lesson; no novelty is claimed.

---

## 5. Relation to homodyne/interferometric detection

A strong local oscillator is often described as `amplifying` a weak optical field.

For the present Gedanken experiment, its deeper role is twofold:

```text
energy / amplitude resource
+
phase-reference resource.
```

A detector-performance bound that counts the signal photon but treats the reference field as free can therefore be badly incomplete.

This is structurally analogous to earlier failures:

```text
weak absorber + free cavity dwell time;
weak coupling + free bandwidth/time;
local reset + free external memory;
thermodynamic closure + free optical/pump free energy;
phase-sensitive detection + free phase reference.
```

---

## 6. Clock / time reference is the temporal analogue

Unknown-arrival-time analysis already introduced a search penalty.

But a deeper issue appears if the detector lacks a clock or synchronization reference entirely.

Time translations are another symmetry. A sufficiently good clock breaks that symmetry operationally and permits measurements of arrival time / phase relative to that clock.

Therefore timing performance depends on both

```text
intrinsic detector dynamics
and
external clock/reference quality.
```

A future timing theorem must not treat the clock as a free resource.

---

## 7. Corrected operational definition

The most precise current detector statement is no longer simply

```text
trace distance between output states.
```

It is

> **distinguishability under the allowed measurement operations and available reference resources.**

Symbolically, one can write an operational distinguishability

```math
\mathcal D_{\mathsf A}(\rho_0,\rho_1),
```

where `A` denotes the allowed measurement set/resources.

Unrestricted trace distance is the special case where all POVMs are allowed.

---

## 8. Consequence for the resource ledger

Add explicitly:

```text
reference-frame / coherence / asymmetry resource
```

to any candidate universal detector resource ledger.

Otherwise states that are mathematically distinct but operationally symmetry-hidden produce counterexamples.

---

## 9. Relation to the original atom-count question

An ensemble with enormous `N` does not necessarily solve a missing-reference problem.

Conversely a small detector plus a strong external phase/clock reference can access information unavailable to a larger reference-free apparatus.

Therefore

```math
\boxed{
N\text{ is not a substitute for measurement-reference access.}
}
```

This adds another independent axis to the detector boundary.

---

## 10. Current status

**DERIVED / KNOWN SYMMETRY-RESOURCE STRUCTURE.**

No novelty claim is attached to group twirling, reference-frame resource theories, phase references, or symmetry-restricted discrimination.

The Experiment-02-specific result is the resource-ledger correction:

> **A detector-performance boundary must specify not only the signal state and detector physics, but also the measurement operations and reference frames that make the relevant state distinction accessible.**
