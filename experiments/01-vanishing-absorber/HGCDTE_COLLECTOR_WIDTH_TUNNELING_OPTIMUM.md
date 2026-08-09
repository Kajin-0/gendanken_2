# HgCdTe Collector Width–Tunneling Optimum — TAT and Direct BTBT Share the Alignment/Transit Crossing in the Uniform Baseline

**Date:** 2026-08-09  
**Status:** exact piecewise monotonicity result inside the uniform-field band-offset + ohmic-transit + local-WKB current models; no novelty claim

## 1. Purpose

`HGCDTE_COLLECTOR_WIDTH_FIELD_OPTIMUM.md` found that the **minimum required collector field** occurs when the interface-alignment and transit-speed field requirements are equal.

It was not obvious that this would remain the optimum once depleted width itself enters the tunneling current prefactor.

A thicker collector contains more tunneling volume/traps, so one might expect the dark-current optimum to shift to a thinner layer.

For the standard simplified TAT and direct-BTBT forms used in this repository, it does not.

The same crossing remains the exact tunneling-current minimum.

---

## 2. Required field versus collector width

Let the required electrostatic alignment energy be

```math
B>0.
```

Let the target transit time be

```math
T^*.
```

In the ohmic collector baseline,

```math
\boxed{
F_{\rm align}(W)
=\frac{B}{qW},
}
```

```math
\boxed{
F_{\rm speed}(W)
=\frac{W}{\mu T^*}.
}
```

Therefore

```math
\boxed{
F_{\rm req}(W)
=\max[
B/(qW),
W/(\mu T^*)
].
}
```

The crossing is

```math
\boxed{
W^*
=\sqrt{\mu T^*B/q}.
}
```

---

## 3. Generic local WKB current family

Consider a uniform-region current density of the form

```math
\boxed{
J_p(W)
=CW F(W)^p
\exp[-K/F(W)],
}
```

where

```text
C > 0
K > 0
p >= 1.
```

The factor `W` represents the region-width factor in the simplified current expression.

This family contains the two relevant repository models:

### Simple TAT form

The standard one-dimensional HgCdTe TAT expression used earlier has

```math
J_{\rm TAT}
\propto
V e^{-F_T/F}
=WF e^{-F_T/F},
```

so

```math
\boxed{p=1.}
```

### Direct BTBT form

The uniform HgCdTe BTBT expression has

```math
J_{\rm BTBT}
\propto
F V e^{-F_K/F}
=WF^2e^{-F_K/F},
```

so

```math
\boxed{p=2.}
```

---

## 4. Alignment-limited side

For

```math
W<W^*,
```

alignment dominates:

```math
F(W)=\frac{B}{qW}.
```

Substitute into the generic current:

```math
J_p(W)
=CW
\left(\frac{B}{qW}\right)^p
\exp\left[-
\frac{KqW}{B}
\right].
```

Therefore

```math
\boxed{
J_p(W)
=C\left(\frac{B}{q}\right)^p
W^{1-p}
e^{-aW},
}
```

with

```math
\boxed{a=Kq/B>0.}
```

Take the logarithmic derivative:

```math
\boxed{
\frac{d\ln J_p}{dW}
=\frac{1-p}{W}-a.
}
```

For

```math
p\ge1,
```

both terms are nonpositive and the `-a` term is strictly negative.

Hence

```math
\boxed{
\frac{dJ_p}{dW}<0
\qquad
(W<W^*).
}
```

The tunneling current strictly **decreases** as the thin alignment-limited collector is made wider.

---

## 5. Speed-limited side

For

```math
W>W^*,
```

speed dominates:

```math
F(W)=\frac{W}{\mu T^*}.
```

Then

```math
J_p(W)
=CW
\left(
\frac{W}{\mu T^*}
\right)^p
\exp\left[-
\frac{K\mu T^*}{W}
\right].
```

Therefore

```math
\boxed{
J_p(W)
=\frac{C}{(\mu T^*)^p}
W^{p+1}
e^{-b/W},
}
```

with

```math
\boxed{b=K\mu T^*>0.}
```

The logarithmic derivative is

```math
\boxed{
\frac{d\ln J_p}{dW}
=\frac{p+1}{W}
+\frac{b}{W^2}>0.
}
```

Hence

```math
\boxed{
\frac{dJ_p}{dW}>0
\qquad
(W>W^*).
}
```

The tunneling current strictly **increases** as the speed-limited collector is made wider.

---

## 6. Exact global minimum

The current decreases up to the crossing and increases after it.

Therefore

```math
\boxed{
W_{\rm tunnel,opt}
=W^*
=\sqrt{\mu T^*B/q}
}
```

for every member of this local-WKB family with

```math
p\ge1.
```

Thus the collector width that minimizes required peak field also minimizes the simplified TAT and direct-BTBT current densities.

This is the central result.

---

## 7. TAT specialization

For

```math
p=1,
```

the alignment-limited TAT current is especially simple:

```math
\boxed{
J_{\rm TAT}
\propto
\exp[-aW].
}
```

The explicit width prefactor cancels the `1/W` alignment field prefactor.

The reduction with width comes entirely from the improved tunneling exponent.

On the speed-limited side,

```math
\boxed{
J_{\rm TAT}
\propto
W^2 e^{-b/W}.
}
```

Both factors increase with `W`.

---

## 8. Direct-BTBT specialization

For

```math
p=2,
```

alignment-limited direct BTBT is

```math
\boxed{
J_{\rm BTBT}
\propto
W^{-1}e^{-aW}.
}
```

It decreases even more strongly with width.

On the speed-limited side,

```math
\boxed{
J_{\rm BTBT}
\propto
W^3 e^{-b/W},
}
```

which increases monotonically.

Again the unique minimum is at `W^*`.

---

## 9. Why the trap-count intuition did not shift the optimum

The TAT current carries an explicit factor of depleted width because more width means more trap-containing material.

But in the alignment-limited branch, increasing width lowers the required field as `1/W`, and the WKB exponential improves as

```math
e^{-aW}.
```

That exponential suppression dominates the linear increase in available trap volume.

In the speed-limited branch, both the width and the required field increase, so every factor moves in the same unfavorable direction.

Hence the crossing remains the optimum.

---

## 10. Scope of the theorem

The result is stronger than a field-only argument, but still model specific.

It assumes

- uniform field in the collector;
- one width-independent trap density;
- width-independent defect matrix element;
- a local WKB current with `p>=1`;
- ohmic velocity for the closed-form `W^*`;
- no interface-state sheet current independent of depleted volume;
- no capacitance / RC cost;
- no stochastic nonlocal II;
- no Poisson change of field shape with width;
- no width-dependent mobility or composition.

Any of those can shift the true device optimum.

---

## 11. What kind of mechanism can move the optimum?

A new width cost must have a scaling that is not already captured by `W F^p e^{-K/F}`.

Candidates include

### Junction capacitance

For a parallel-plate-like depletion region,

```math
C_j\propto1/W.
```

Making the collector thinner increases capacitance and can add RC delay.

### Interface-state leakage

A sheet-like interface current need not scale with depleted width.

### Nonlocal impact ionization

Event probability depends on energy history and dead space, not a local `W F^p e^{-K/F}` density.

### Velocity saturation

Changes the speed branch from `F~W` to the inverse of a nonlinear `v(F)` law.

### Self-consistent electrostatics

Changes the local field profile and may introduce peak fields not represented by the average `F`.

These are the correct next attacks.

---

## 12. Claim boundary

### DERIVED / CONDITIONAL

For

```math
J_p
=CWF^p e^{-K/F},
\qquad p\ge1,
```

with

```math
F(W)
=\max[
B/(qW),
W/(\mu T^*)
],
```

```math
\boxed{
J_p(W)
\text{ decreases for }W<W^*,
}
```

```math
\boxed{
J_p(W)
\text{ increases for }W>W^*,
}
```

and therefore

```math
\boxed{
W_{\rm tunnel,opt}=W^*.
}
```

### KNOWN / PRIOR

- WKB TAT/BTBT field dependences;
- width dependence of uniform-region generation models;
- elementary monotonic optimization.

### NON-CLAIM

This is not

- a universal collector-width theorem;
- a theorem including RC;
- a theorem for interface sheet traps;
- a theorem for nonlocal II;
- a calibrated HgCdTe device optimum;
- a novelty claim.

---

## 13. Next decisive attack

Add the **junction capacitance / RC response** because it provides a qualitatively different thin-width penalty.

Then ask:

> **When the collector is made thin enough that interface alignment dominates, does the rising capacitance move the total speed/dark-current optimum away from `W^*`?**

Keep the readout resistance explicit rather than assuming a universal RC constant.