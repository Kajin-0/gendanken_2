# HgCdTe Collector Width–Field Optimum — Match Interface Alignment to Transit Speed

**Date:** 2026-08-09  
**Status:** exact minimax result in the parametric band-offset + ohmic collector model; standard constrained optimization; no novelty claim

## 1. Purpose

A wider-gap depleted collector is attractive because it can keep the strongest electrostatic field out of the narrow-gap optical absorber.

But two opposite width scalings appear:

```text
thin collector
-> short geometric transit distance
-> but large field needed to drop a fixed interface-alignment energy

thick collector
-> smaller alignment field
-> but larger field needed to cross the region within a fixed transit time.
```

This note solves that competition exactly in the ohmic baseline.

---

## 2. Effective interface barrier to be removed

Let

```math
\Delta E_c^{\rm off}
=Q_c(E_{g,c}-E_{g,a})
```

be the conduction-band offset before electrostatic alignment.

Allow a residual positive barrier

```math
\Phi_*
```

consistent with the desired interface transmission.

Define the electrostatic energy drop that must be supplied by the collector as

```math
\boxed{
B
\equiv
\max[
\Delta E_c^{\rm off}-\Phi_*,
0
].
}
```

`B` has units of energy.

For perfectly barrierless transfer,

```math
\Phi_*=0,
```

so

```math
B=Q_c(E_{g,c}-E_{g,a}).
```

---

## 3. Alignment field

Across collector width `W_d`, supplying energy drop `B` requires

```math
qF_{\rm align}W_d=B.
```

Therefore

```math
\boxed{
F_{\rm align}(W_d)
=\frac{B}{qW_d}.
}
```

This decreases as `1/W_d`.

---

## 4. Speed field in the ohmic baseline

Let the target depleted transit time be

```math
\boxed{T_d^*.}
```

For

```math
v_d=\mu_dF_d,
```

meeting

```math
W_d/v_d\le T_d^*
```

requires

```math
\boxed{
F_{\rm speed}(W_d)
=\frac{W_d}
{\mu_dT_d^*}.
}
```

This increases linearly with `W_d`.

---

## 5. Required field at a chosen width

Both constraints must hold, so

```math
\boxed{
F_{\rm req}(W_d)
=\max\left[
\frac{B}{qW_d},
\frac{W_d}{\mu_dT_d^*}
\right].
}
```

The first branch decreases with width and the second increases.

Therefore the global minimax field occurs at their unique intersection.

---

## 6. Exact optimal width

Set

```math
\frac{B}{qW_d}
=
\frac{W_d}{\mu_dT_d^*}.
```

Then

```math
W_d^2
=\frac{\mu_dT_d^*B}{q}.
```

Therefore

```math
\boxed{
W_d^*
=\sqrt{
\frac{\mu_dT_d^*B}{q}
}.
}
```

This is the field-minimizing collector width in the ohmic model.

---

## 7. Exact minimum field

Substitute `W_d^*` into either branch:

```math
\boxed{
F_d^*
=\sqrt{
\frac{B}
{q\mu_dT_d^*}
}.
}
```

Thus

```text
larger mobility
-> lower required field

longer allowed transit time
-> lower required field

larger conduction-band offset to be corrected
-> higher required field.
```

---

## 8. Exact voltage at the optimum

The collector voltage is

```math
V_d=F_dW_d.
```

At the optimum,

```math
V_d^*
=F_d^*W_d^*.
```

Therefore

```math
\boxed{
V_d^*
=\frac{B}{q}.
}
```

This has a simple interpretation:

> **At the field-optimal width, the collector uses exactly the electrostatic voltage required to reduce the interface barrier to the allowed value, and that same voltage is just sufficient to meet the transit-time target.**

No extra voltage is wasted on one constraint while the other dominates.

---

## 9. Equivalent transit identity

At the optimum,

```math
qV_d^*=B.
```

The ohmic transit time is

```math
T_d
=\frac{W_d^2}
{\mu_dV_d}.
```

Therefore

```math
\boxed{
T_d^*
=\frac{q(W_d^*)^2}
{\mu_dB}.
}
```

This is the depleted-collector analogue of the graded-neutral band-edge-drop transport relation

```math
T_g
=qL_g^2/(\mu_n\Delta E_c).
```

Both say that a finite carrier-driving energy drop sets the allowed length squared per unit transit time.

---

## 10. Why this also minimizes monotonic local tunneling

Suppose a local leakage density is monotonically increasing in field:

```math
g'(F)>0.
```

This includes the WKB families used elsewhere in the repository, such as

```math
F^p e^{-K/F}.
```

Because `W_d^*` minimizes the **maximum required field** under the two constraints, it also minimizes every leakage metric that depends monotonically only on that uniform field, provided all other material parameters are held fixed.

Thus in the simplified uniform-collector model:

> **matching the alignment and speed field requirements is simultaneously the field-optimal and local-tunneling-optimal width choice.**

This statement does not include width-dependent trap count, total generation volume, capacitance, or nonlocal processes.

---

## 11. Direct-Zener exponent at the optimum

Use the collector Kane field

```math
F_{K,c}
=\frac{\pi E_{g,c}^2}
{4q\hbar v_K}.
```

Then

```math
\boxed{
\mathcal S_c^*
\equiv
\frac{F_{K,c}}
{F_d^*}
=
\frac{\pi E_{g,c}^2}
{4q\hbar v_K}
\sqrt{
\frac{q\mu_dT_d^*}{B}
}.
}
```

Equivalently, since

```math
B=qF_d^*W_d^*,
```

and

```math
\ell_{K,c}=\hbar v_K/E_{g,c},
```

```math
\boxed{
\mathcal S_c^*
=
\frac{\pi}{4}
\frac{E_{g,c}}{B}
\frac{W_d^*}{\ell_{K,c}}.
}
```

For barrierless alignment

```math
B=Q_c(E_{g,c}-E_{g,a}),
```

this reduces to

```math
\boxed{
\mathcal S_c^*
=
\frac{\pi}
{4Q_c\rho}
\frac{W_d^*}{\ell_{K,c}},
}
```

with

```math
\rho=(E_{g,c}-E_{g,a})/E_{g,c}.
```

---

## 12. If the collector is thinner than `W_d^*`

For

```math
W_d<W_d^*,
```

alignment dominates:

```math
F_{\rm req}
=\frac{B}{qW_d}.
```

Shrinking the collector further **increases** the required field even though the geometric distance is shorter.

Thus

> “make depletion thinner for speed” fails once the fixed interface-alignment drop becomes the active constraint.

---

## 13. If the collector is thicker than `W_d^*`

For

```math
W_d>W_d^*,
```

speed dominates:

```math
F_{\rm req}
=\frac{W_d}{\mu_dT_d^*}.
```

Making the collector thicker reduces the field needed for interface alignment but forces a larger field to meet the same transit time.

---

## 14. Allow high-field nonlinear velocity

The exact square-root formulas use

```math
v=\mu F.
```

The minimax structure survives more generally if the useful rising-branch velocity law is monotonic.

Let

```math
F_v(u)
```

be the minimum field required to obtain velocity `u` on the useful branch.

For width `W_d` and transit target `T_d^*`, the speed field is

```math
\boxed{
F_{\rm speed}(W_d)
=F_v(W_d/T_d^*).
}
```

The required field is

```math
\boxed{
F_{\rm req}(W_d)
=\max[
B/(qW_d),
F_v(W_d/T_d^*)
].
}
```

The alignment term decreases with `W_d`; the speed term increases as long as the required velocity lies on a monotonic rising branch.

Therefore the optimum remains the unique crossing

```math
\boxed{
\frac{B}{qW_d^*}
=F_v(W_d^*/T_d^*).
}
```

unless the target velocity exceeds the physically available branch.

The closed square-root formula is simply the ohmic special case.

---

## 15. Feasibility under a velocity ceiling

If the collector has a maximum usable drift velocity

```math
v_{\max},
```

then

```math
\boxed{
W_d
\le
v_{\max}T_d^*
}
```

is necessary for the transit target.

If the alignment/speed crossing lies beyond this width, the ideal square-root optimum is not physically reachable and the solution sits at the velocity-limited boundary.

Do not substitute an arbitrary universal HgCdTe saturation velocity.

---

## 16. TAT and total trap volume are separate width penalties

The field optimum does not automatically minimize realistic TAT current.

For example, a local TAT generation density may scale with

```text
trap density
x
collector volume/width
x
field-dependent exponential.
```

Then increasing `W_d` both changes field and changes the number of active traps.

Likewise, capacitance scales with geometry.

Therefore the exact `W_d^*` is best interpreted as

```text
minimum-field width under interface + transit constraints,
```

not a complete device optimum.

It is the correct baseline around which TAT/RC/Poisson corrections should be added.

---

## 17. Claim boundary

### DERIVED / CONDITIONAL

For positive required alignment energy `B` and ohmic collector transport:

```math
\boxed{
F_{\rm req}(W_d)
=\max[
B/(qW_d),
W_d/(\mu_dT_d^*)
],
}
```

```math
\boxed{
W_d^*
=\sqrt{\mu_dT_d^*B/q},
}
```

```math
\boxed{
F_d^*
=\sqrt{B/(q\mu_dT_d^*)},
}
```

```math
\boxed{V_d^*=B/q.}
```

### GENERALIZED STRUCTURE

For any monotonic rising velocity law,

```math
\boxed{
B/(qW_d^*)
=F_v(W_d^*/T_d^*)
}
```

at the field-minimizing interior solution.

### KNOWN / PRIOR

- heterojunction band-offset alignment;
- drift transit;
- minimax intersection of decreasing/increasing constraints.

### OPEN

- target HgCdTe `Q_c`;
- high-field `v_d(F)` in the intended collector composition;
- width-dependent TAT and trap statistics;
- Poisson electrostatics;
- RC/capacitance cost.

### NON-CLAIM

This file does not establish

- a universal optimal HgCdTe collector width;
- a universal conduction-band offset;
- that the minimum-field width minimizes total dark current;
- a full APD collector design;
- novelty of the optimization.

---

## 18. Next decisive attack

The next correction should be **TAT + width**, because it is the first mechanism that can shift the optimum away from the minimum-field crossing even when direct BTBT remains negligible.

Use a model of the form

```math
J_{\rm TAT,tot}(W_d)
\propto
N_T W_d
\,\mathcal F[F_{\rm req}(W_d),\Delta_t]
```

and ask:

> **Does the field-minimizing collector width remain close to the dark-current-minimizing width once the number of active traps grows with depleted width?**

Keep the trap parameters explicit rather than inserting a universal `N_T`.