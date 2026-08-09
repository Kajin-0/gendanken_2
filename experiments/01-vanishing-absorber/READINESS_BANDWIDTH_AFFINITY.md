# Readiness–Bandwidth–Affinity Relation — A Restricted Capture-to-Click Resource Bound

**Date:** 2026-08-08  
**Status:** derived within a minimal serial/ready-state limit of the unified three-level machine; ingredients are standard rate/detailed-balance physics; no novelty claim  

## 1. Question

A detector can have excellent conditional capture and click probability and still miss an incident photon if it is not in its detection-ready state when the photon arrives.

The autonomous detector back end therefore introduces a resource that the earlier passive capture theorem did not contain:

```text
ready-state occupation.
```

This note asks how the required optical capture bandwidth and the nonequilibrium bias maintaining the ready state combine.

---

## 2. Minimal reset subsystem

Consider the two internal states

```text
|0>  reset/ground
|1>  detection-ready
```

with effective population rates

```math
u:0\to1,
\qquad
d:1\to0.
```

For this isolated reset pair, the stationary ready probability is

```math
\boxed{
p_{\rm r}
=\frac{u}{u+d}.
}
```

Define the dimensionless reset bias / effective affinity

```math
\boxed{
\mathcal A_{\rm r}
\equiv
\ln\frac{u}{d}.
}
```

Then

```math
\boxed{
p_{\rm r}
=\frac{1}{1+e^{-\mathcal A_{\rm r}}}.
}
```

For an ordinary positive-temperature thermal bath coupled to an excited ready state, this affinity would be negative. Achieving `p_r > 1/2` therefore requires a nonequilibrium work source, population inversion, chemical bias, effective negative temperature, or another active preparation resource.

The note treats `A_r` only as an effective rate bias and does not equate it to a universal work cost.

---

## 3. Conditional capture ceiling

Use the restricted one-free-space-channel capture result from

`THERMODYNAMIC_OPTICAL_ACCESS_BRIDGE.md`.

Let

```math
R_C
```

be the aggregate **amplitude-decay** access from the passive optical capture network into the successfully captured/receiving state.

For angular-frequency band width

```math
W,
```

the conditional band-averaged capture probability obeys

```math
\boxed{
\overline\eta_{\rm cap|ready}
\le
C_B
\equiv
\frac{R_C}{R_C+W/(4\pi)}.
}
```

This is a restricted passive optical result with strong prior-art overlap.

---

## 4. Include conditional back-end click efficiency

Let

```math
\eta_D
```

be the conditional probability that a successfully captured excitation produces the desired registered click once the detector is ready.

In the dilute-event limit, where an incident photon samples the stationary ready-state occupation but does not appreciably perturb it before the event, the complete external efficiency satisfies

```math
\boxed{
\overline\eta_{\rm ext}
\le
p_{\rm r}\,\eta_D\,C_B.
}
```

Thus

```math
\boxed{
\overline\eta_{\rm ext}
\le
\frac{\eta_D}{1+e^{-\mathcal A_{\rm r}}}
\frac{R_C}{R_C+W/(4\pi)}.
}
```

This is the central restricted relation.

It separates three conceptually different resources:

```text
capture access       R_C
accepted bandwidth   W
ready-state bias      A_r
```

plus the conditional back-end quality `eta_D`.

---

## 5. Necessary reset affinity for target external efficiency

Demand

```math
\overline\eta_{\rm ext}\ge\eta_*.
```

A necessary feasibility condition is

```math
\boxed{
\eta_D C_B>\eta_*.
}
```

If this is not satisfied, even perfect readiness cannot reach the target.

When the condition holds,

```math
p_{\rm r}
\ge
\frac{\eta_*}{\eta_D C_B}.
```

Using

```math
p_{\rm r}
=\frac1{1+e^{-\mathcal A_{\rm r}}},
```

gives

```math
\boxed{
\mathcal A_{\rm r}
\ge
\ln\!\left[
\frac{\eta_*}
{\eta_D C_B-\eta_*}
\right].
}
```

Substituting

```math
C_B=\frac{R_C}{R_C+W/(4\pi)},
```

yields

```math
\boxed{
\mathcal A_{\rm r}
\ge
\ln\!\left[
\frac{
\eta_*\left(R_C+W/(4\pi)\right)
}{
\eta_D R_C
-\eta_*\left(R_C+W/(4\pi)\right)
}
\right]
}
```

provided the denominator is positive.

---

## 6. Optical resource condition reappears automatically

The denominator positivity condition is

```math
\eta_D R_C
>
\eta_*\left(R_C+W/(4\pi)\right).
```

Equivalently,

```math
\boxed{
R_C
>
\frac{\eta_*}
{\eta_D-\eta_*}
\frac{W}{4\pi},
\qquad
\eta_D>\eta_*.
}
```

This is exactly the capture-resource feasibility condition obtained earlier in `CAPTURE_TO_CLICK_COMPOSITION.md`.

Thus the readiness calculation is consistent with the previous serial composition rather than introducing a contradictory resource condition.

---

## 7. Useful limits

### Infinite capture access

If

```math
R_C\to\infty,
```

then `C_B -> 1` and

```math
\boxed{
\mathcal A_{\rm r}
\ge
\ln\!\left[
\frac{\eta_*}{\eta_D-\eta_*}
\right].
}
```

Even a perfect optical front end cannot overcome insufficient detector readiness.

### Perfect conditional back end

If

```math
\eta_D=1,
```

and `R_C -> infinity`,

```math
\boxed{
\mathcal A_{\rm r}
\ge
\ln\frac{\eta_*}{1-\eta_*}.
}
```

For example, making the ready probability arbitrarily close to one requires a logarithmically diverging rate bias.

### Infinite reset bias

If

```math
\mathcal A_{\rm r}\to\infty,
```

then `p_r -> 1` and the result reduces to the earlier capture-to-click ceiling

```math
\overline\eta_{\rm ext}
\le
\eta_D C_B.
```

### Increasing bandwidth

At fixed `R_C`, `eta_D`, and reset affinity, increasing `W` lowers the maximum external efficiency.

Thus bandwidth cannot be widened indefinitely at fixed capture access and fixed readiness resource even before internal dark-count or dead-time constraints are added.

---

## 8. Relation to dead time

The stationary readiness factor and the transient dead time are distinct.

If the detector enters `|0>` after every registered event and the dominant recovery is the forward reset rate `u`, a simple low-noise estimate is

```math
D\sim\frac1u.
```

But `p_r` depends on the **ratio** `u/d`, whereas recovery time depends primarily on the **absolute scale** of the reset rates.

Therefore two independent aspects of the reset resource appear:

```text
bias / directionality     u/d
speed                      u+d  (or the Liouvillian gap in a full model).
```

This is consistent with autonomous-detector thermodynamics, where state preparation, dead time, and dissipation cannot generally be reduced to one parameter.

No universal dead-time relation is claimed here.

---

## 9. Relation to optical gain

The detection-ready state `|1>` stores free energy, but the signal transition is still an **absorbing** transition so long as the dark operating point has more population in `|1>` than in the activated state `|2>`.

The ready-state resource therefore does not automatically turn the optical capture front end into an active gain medium.

If an autonomous work source instead produces population inversion on the signal transition itself,

```math
p_2>p_1,
```

then the small-signal optical response can become active and the passive capture theorem no longer applies without counting the pump resource.

That is the next adversarial direction.

---

## 10. Claim boundary

### Derived within the restricted ready-state model

```math
\boxed{
\overline\eta_{\rm ext}
\le
\frac{\eta_D}{1+e^{-\mathcal A_{\rm r}}}
\frac{R_C}{R_C+W/(4\pi)}
}
```

and, when feasible,

```math
\boxed{
\mathcal A_{\rm r}
\ge
\ln\!\left[
\frac{\eta_*}
{\eta_D C_B-\eta_*}
\right].
}
```

### Not established

- novelty of this composition;
- a universal relation between `A_r` and entropy production/work;
- validity outside the dilute-event stationary-readiness limit;
- validity when capture and reset dynamics overlap coherently;
- validity for an optically inverted/gain-assisted front end;
- a universal efficiency-bandwidth-dead-time-dark-count theorem.

---

## 11. Next decisive calculation

Use the full three-level dark steady state from `UNIFIED_THREE_LEVEL_CAPTURE_MACHINE.md` and compute the weak optical susceptibility about that nonequilibrium operating point.

The key quantity is the population difference

```math
p_1-p_2.
```

Determine whether the work/reset source can increase capture beyond the passive bound without creating optical gain, and if gain appears, identify exactly which pump/free-energy resource has replaced the passive-access limitation.