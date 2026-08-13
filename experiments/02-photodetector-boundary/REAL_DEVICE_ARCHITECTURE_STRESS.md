# Real-Device Architecture Stress — Experiment 02

**Date:** 2026-08-12  
**Status:** adversarial architecture test; generic SPAD interpretation rejected  
**Priority:** no novelty claim

The semiconductor scaling branch produced a clean asymptotic class

```math
\eta_s\sim S L^s,
\qquad
\mu_d\sim K L^p,
```

with, in the first Poisson-mode regime,

```math
L_*\sim(s/pK)^{1/p},
\qquad
\mu_*=s/p.
```

The bulk-dark + transit-gate specialization gave `s=1,p=2` and therefore

```math
L_*\sim\sqrt{v/(2r_dA)}.
```

This file asks whether that `p=2` model is actually a defensible generic model of a practical single-photon avalanche detector.

The answer is **no**.

---

## 1. Architecture selected for the stress

Use a separate-absorption / multiplication photodiode architecture as the adversarial target.

Conceptually:

```text
incident photon
-> absorption region
-> field-assisted carrier transport
-> multiplication region
-> avalanche / macroscopic output
-> threshold/timing electronics.
```

This is already enough to expose several assumptions hidden in the minimal slab model.

The point is not to reproduce one commercial device. It is to test whether the scaling class survives a realistic architecture decomposition.

---

## 2. Hidden assumption A — collection was modeled as exponential survival to a far contact

The Gedanken slab used

```math
P_{\rm col}(z|L)=e^{-\beta(L-z)}.
```

That makes thicker absorption layers intrinsically penalize carriers generated farther from the collecting boundary.

A field-engineered absorption/charge region can instead be operated so that useful carriers drift toward the multiplication region with collection probability much closer to unity over the relevant layer, until trapping/recombination or field nonuniformity becomes important.

Then the signal model is closer to

```math
\eta_s(L)
\approx
\eta_0(1-e^{-\alpha L})
```

than to

```math
\eta_0\frac{\alpha}{\alpha-\beta}
(e^{-\beta L}-e^{-\alpha L}).
```

### Consequence

The finite optimum caused by `absorption versus far-contact survival` is **architecture dependent**.

It cannot be promoted into a generic semiconductor-photodetector thickness law.

---

## 3. Hidden assumption B — dark-event rate was proportional to absorber volume

The `p=2` class assumed, to leading order,

```math
\lambda_d(L)\propto A L.
```

That corresponds to a bulk generation mechanism distributed throughout the thickness being optimized.

A real avalanche detector can have important dark contributions from different regions/mechanisms, schematically

```text
bulk generation in absorption region;
field-assisted/tunneling generation;
multiplication-region generation;
surface/perimeter generation;
trap-related afterpulsing/history;
readout/threshold false events.
```

Those terms need not scale as `L` when the absorption thickness changes.

A more honest decomposition is

```math
\boxed{
\lambda_d(L)
=
\lambda_0
+\lambda_1 L
+\lambda_{\rm field}(L,V,T)
+\lambda_{\rm hist}[\text{past events}]
+\cdots
}
```

where `lambda_0` represents thickness-independent contributions and the remaining terms can have different geometry/field dependence.

### Consequence

The exponent `m=1` is a mechanism assumption, not a detector universal.

---

## 4. Hidden assumption C — the observation time was forced to scale as L/v

The strong-dark law used

```math
T(L)=L/v.
```

A real event decision window may instead be determined by a maximum of several times:

```math
\boxed{
T_{\rm obs}(L)
\sim
\max\{
T_{\rm transport}(L),
T_{\rm avalanche},
T_{\rm electronics},
T_{\rm timing\ gate}
\}.
}
```

If electronics or an externally imposed gate dominates,

```math
T_{\rm obs}\approx\text{constant},
```

so bulk dark rate `~L` gives `p=1`, not `p=2`.

If transit dominates,

```math
T_{\rm obs}\propto L,
```

then the `p=2` class can reappear.

### Consequence

The scaling exponent `p` depends on **which latency actually controls the decision window**.

---

## 5. Realistic reduced model should contain multiple dark/timing terms

Keep an optically thin signal for the moment:

```math
\eta_s(L)\sim S L.
```

Let

```math
\lambda_d(L)=\lambda_0+\lambda_1L
```

and

```math
T(L)=T_0+L/v.
```

Then

```math
\boxed{
\mu_d(L)
=
(\lambda_0+\lambda_1L)(T_0+L/v).
}
```

Expanding,

```math
\boxed{
\mu_d(L)
=
\underbrace{\lambda_0T_0}_{\mu_0}
+
\underbrace{\left(\frac{\lambda_0}{v}+\lambda_1T_0\right)}_{K_1}L
+
\underbrace{\frac{\lambda_1}{v}}_{K_2}L^2.
}
```

Thus a more realistic architecture naturally produces

```text
constant dark exposure + linear thickness penalty + quadratic thickness penalty.
```

The pure `p=2` asymptote is only one limiting regime.

---

## 6. Decision optimum in the mixed-exponent thin model

Ignoring the constant `mu_0`, which multiplies all signal distinctions by the same factor, the leading thin-device objective is

```math
\mathcal D(L)
\propto
L\exp[-K_1L-K_2L^2].
```

The optimum satisfies

```math
\frac1L-K_1-2K_2L=0.
```

Therefore

```math
\boxed{
L_*
=
\frac{2}
{K_1+\sqrt{K_1^2+8K_2}}.
}
```

This interpolates continuously between the two scaling classes:

### Linear-penalty dominated

If

```math
K_1^2\gg K_2,
```

then

```math
\boxed{L_*\approx1/K_1.}
```

### Quadratic-penalty dominated

If

```math
K_2\gg K_1^2,
```

then

```math
\boxed{L_*\approx1/\sqrt{2K_2}.}
```

The apparent `p=1` and `p=2` universality classes are therefore **limits of one mixed architecture model**, not competing fundamental laws.

---

## 7. Constant dark background creates a separate feasibility ceiling

The thickness-independent term

```math
\mu_0=\lambda_0T_0
```

multiplies the maximum binary distinction by

```math
e^{-\mu_0}
```

in the low-count click/no-click limit.

No choice of absorption thickness can eliminate that penalty.

Thus an architecture with a large thickness-independent dark/background component can fail the target even if the absorption-layer geometry itself is optimally chosen.

This recovers an earlier Experiment-02 lesson in a more realistic geometry model:

```text
an upstream geometry optimization cannot repair an independent downstream/background ceiling.
```

---

## 8. Dimensionless crossover coordinate

The mixed model is controlled by

```math
\boxed{
\chi
=\frac{K_2}{K_1^2}.
}
```

Then

```text
chi << 1 -> linear-penalty / p=1-like regime;
chi >> 1 -> quadratic-penalty / p=2-like regime;
chi ~ 1 -> crossover.
```

This is a better architecture descriptor than asserting one universal exponent in advance.

---

## 9. What survives the real-architecture stress

### Survives

The general principle

```text
signal-growth scaling
versus
dark-exposure / timing scaling
sets the decision-optimal geometry.
```

The scaling-class formalism remains useful.

### Does not survive as generic SPAD law

```math
L_*\sim\sqrt{v/(2r_dA)}.
```

That law requires the specific bulk-dark + transit-dominated assumptions.

### Stronger surviving formulation

```math
\boxed{
\text{identify the actual thickness dependence of }
\eta_s(L),\lambda_d(L),T_{\rm obs}(L),
\text{ then optimize the complete output decision process.}
}
```

This is physically honest but less likely to be novel.

---

## 10. Consequence for the original Gedanken question

The real-device stress reinforces the deepest recurring lesson:

> **There is no detector boundary controlled by atom count alone because adding matter changes several architecture-dependent resource channels at once, and those channels need not scale with matter in the same way.**

The relevant question is not

```text
How many atoms?
```

but

```text
How does adding/removing matter change the complete optical-to-decision channel under the actual architecture?
```

---

## 11. Current disposition

**ADVERSARIAL RESULT:** the pure `p=2` square-root law is **not** a defensible generic SPAD/APD law.

**SURVIVING VALUE:** the scaling-class method and mixed-exponent optimum remain useful as reduced architecture models.

**NOVELTY:** none claimed; expectation remains low without a real experimentally consequential constraint.

---

## 12. Direction

Do not insert arbitrary literature numbers into the pure `p=2` law.

A meaningful device specialization must first identify, for one actual architecture:

```text
which dark terms scale with absorption thickness;
which timing term sets the observation window;
whether collection probability changes materially with thickness;
which output information is actually retained;
which parameters are independently measurable.
```

If those inputs reduce to ordinary established device optimization, close the semiconductor branch as a rigorous conceptual demonstration rather than forcing novelty.
