# HgCdTe Collector Dimensionless Pareto Map — Field/Tunneling Optimum versus Transit/RC Timing

**Date:** 2026-08-09  
**Status:** exact nondimensionalization of the parametric band-offset + ohmic transit + first-order RC baseline; no novelty claim

## 1. Purpose

The collector branch now contains two distinct preferred widths:

1. `W_F^*` — minimum field / simplified local TAT-BTBT width from interface alignment versus transit speed;
2. `W_RC^*` — minimum transit+RC timing-variance width at fixed collector velocity.

This note collapses the competition into a dimensionless Pareto map.

The result tells us whether thinning or thickening away from the field-optimal collector can improve timing enough to justify the extra electric-field/tunneling burden.

---

## 2. Field/tunneling reference point

Let the required electrostatic interface-alignment energy be

```math
B>0.
```

Let the target depleted transit time be

```math
T^*.
```

In the ohmic baseline,

```math
\boxed{
W_F^*
=\sqrt{\mu T^*B/q},
}
```

```math
\boxed{
F_F^*
=\sqrt{B/(q\mu T^*)}.
}
```

At this point,

```math
\boxed{
\mu F_F^*
=W_F^*/T^*.
}
```

Define the reference drift velocity

```math
\boxed{
v^*
=\mu F_F^*
=W_F^*/T^*.
}
```

---

## 3. Normalize width

Define

```math
\boxed{
w=W_d/W_F^*.}
```

The minimum required field at each width is

```math
F_{\rm req}
=\max[
B/(qW_d),
W_d/(\mu T^*)
].
```

Therefore

```math
\boxed{
\frac{F_{\rm req}}
{F_F^*}
=\begin{cases}
1/w,&0<w\le1,\\
w,&w\ge1.
\end{cases}
}
```

Thus

```math
\boxed{w=1}
```

is the unique minimum-field point.

---

## 4. Transit time under the minimum-field operating rule

### Thin / alignment-limited branch

For

```math
w\le1,
```

```math
F=F_F^*/w.
```

Ohmic velocity is

```math
v=v^*/w.
```

Therefore

```math
T_d
=\frac{wW_F^*}{v^*/w}
=w^2T^*.
```

So

```math
\boxed{
T_d/T^*=w^2,
\qquad w\le1.
}
```

The interface-alignment requirement forces the thin collector to run **faster than the original transit target**.

### Thick / speed-limited branch

For

```math
w\ge1,
```

```math
F=wF_F^*,
```

```math
v=wv^*,
```

and

```math
\boxed{
T_d/T^*=1.
}
```

The applied field rises exactly enough to maintain the target transit time.

---

## 5. Normalize the RC scale

Define

```math
c
\equiv
R_{\rm eff}\epsilon_sA_d.
```

Then

```math
\tau_{RC}=c/W_d.
```

At fixed reference velocity `v^*`, the transit-RC timing-variance optimum from the previous note is

```math
\boxed{
W_{RC}^*
=12^{1/4}\sqrt{v^*c}.
}
```

Define the single dimensionless readout parameter

```math
\boxed{
\rho
=\frac{W_{RC}^*}
{W_F^*}.
}
```

Using

```math
(W_{RC}^*)^2
=\sqrt{12}\,v^*c
```

and

```math
v^*=W_F^*/T^*,
```

we obtain

```math
\boxed{
\frac{c}{W_F^*}
=\frac{\rho^2T^*}
{\sqrt{12}}.
}
```

Hence

```math
\boxed{
\frac{\tau_{RC}}
{T^*}
=\frac{\rho^2}
{\sqrt{12}\,w}.
}
```

---

## 6. Exact normalized collector timing variance

The collector timing variance is

```math
\sigma_c^2
=\frac{T_d^2}{12}
+\tau_{RC}^2.
```

Define

```math
\boxed{
Z(w;\rho)
\equiv
\frac{12\sigma_c^2}
{(T^*)^2}.
}
```

### Thin branch

Using `T_d/T^*=w^2`,

```math
\boxed{
Z
=w^4+rac{\rho^4}{w^2},
\qquad
0<w\le1.
}
```

### Thick branch

Using `T_d/T^*=1`,

```math
\boxed{
Z
=1+rac{\rho^4}{w^2},
\qquad
w\ge1.
}
```

This is the central timing Pareto map.

---

## 7. Thin-side timing optimum

Differentiate for `w<1`:

```math
\frac{dZ}{dw}
=4w^3
-2\rho^4w^{-3}.
```

Set to zero:

```math
4w^6=2\rho^4.
```

Therefore

```math
\boxed{
w_{\rm timing}
=\frac{\rho^{2/3}}
{2^{1/6}}.
}
```

This lies on the thin branch only if

```math
w_{\rm timing}\le1.
```

Thus

```math
\boxed{
\rho\le2^{1/4}.
}
```

The critical ratio is

```math
\boxed{
\rho_c
=2^{1/4}
\simeq1.1892.
}
```

---

## 8. Minimum thin-side timing variance

At the stationary point,

```math
w^6=\rho^4/2.
```

Therefore

```math
w^4
=\rho^{8/3}/2^{2/3},
```

and

```math
\rho^4/w^2
=2^{1/3}\rho^{8/3}.
```

Hence

```math
\boxed{
Z_{\rm min,thin}
=\frac{3}{2^{2/3}}
\rho^{8/3}.
}
```

Equivalently,

```math
\boxed{
\sigma_{c,\rm min,thin}^2
=\frac{(T^*)^2}{12}
\frac{3}{2^{2/3}}
\rho^{8/3}.
}
```

---

## 9. Physical regime split

### Regime A — `rho >= 2^(1/4)`

The formal thin-side timing optimum lies at or beyond `w=1`.

For every

```math
0<w<1,
```

the thinner collector has

- higher required field than the field optimum;
- no timing-variance advantage over `w=1` once the minimum is excluded from the branch.

Therefore thinning below the field optimum is **Pareto dominated**.

The useful timing-improvement direction is toward

```math
w>1,
```

where capacitance falls, but the required field rises as `w`.

### Regime B — `rho < 2^(1/4)`

A genuine thin-side timing optimum exists:

```math
0<w_{\rm timing}<1.
```

Moving from `w=1` toward this point

- raises the field as `1/w`;
- shortens depletion transit faster than RC worsens initially;
- reduces total timing variance.

So thinning is a real speed-for-field/tunneling trade in this regime.

---

## 10. Field penalty at the thin timing optimum

On the thin branch,

```math
F/F_F^*=1/w.
```

Therefore at `w_timing`,

```math
\boxed{
\frac{F_{\rm timing}}
{F_F^*}
=2^{1/6}
\rho^{-2/3}.
}
```

Thus very small `rho` allows a much thinner timing-optimal collector, but the field penalty rises correspondingly.

---

## 11. Exact normalized tunneling penalty

Use the generic local-WKB current family

```math
J_p
=CWF^p e^{-K/F},
\qquad p\ge1.
```

Define the reference exponent parameter

```math
\boxed{
\kappa
=K/F_F^*.
}
```

Let

```math
\boxed{j_p(w)=J_p(w)/J_p(1).}
```

### Thin branch

For `F/F_F^*=1/w`,

```math
\boxed{
j_p(w)
=w^{1-p}
\exp[\kappa(1-w)],
\qquad
w\le1.
}
```

### Thick branch

For `F/F_F^*=w`,

```math
\boxed{
j_p(w)
=w^{p+1}
\exp\left[
\kappa\left(1-\frac1w\right)
\right],
\qquad
w\ge1.
}
```

Both are at least one away from the minimum point.

For simple TAT use `p=1` and `K=F_T`.

For direct BTBT use `p=2` and `K=F_K`.

This gives a full dimensionless timing-versus-tunneling Pareto curve using only

```math
\boxed{w,\rho,\kappa,p.}
```

---

## 12. Voltage ratio

The collector voltage is

```math
V=FW.
```

Relative to the field-optimal voltage

```math
V_F^*=F_F^*W_F^*=B/q,
```

### Thin alignment-limited branch

```math
\boxed{
V/V_F^*=1,
\qquad w\le1.
}
```

The same alignment voltage is simply dropped over a smaller width.

### Thick speed-limited branch

```math
\boxed{
V/V_F^*=w^2,
\qquad w\ge1.
}
```

Thus thick-side capacitance reduction is paid for with a quadratic voltage increase in the ohmic target-time baseline.

---

## 13. Why this map is more useful than one optimal width

There is no universal single collector optimum because device priorities differ.

The map separates three quantities:

```text
field / tunneling burden
-> minimum at w=1

timing variance
-> depends on rho

bias voltage
-> constant on thin branch, quadratic on thick branch.
```

A detector designer can therefore choose a point on the Pareto frontier rather than pretending one geometry optimizes all objectives.

---

## 14. Add the neutral graded absorber

The full timing variance is

```math
\boxed{
\sigma_{\rm full}^2
=
\sigma_g^2
+\frac{(T^*)^2}{12}Z(w;\rho).
}
```

The neutral grading branch can reduce `sigma_g` and raise external collected QE by moving near-cutoff absorption closer to the collector.

Once

```math
\sigma_g^2
\ll
\frac{(T^*)^2}{12}Z,
```

further grading yields diminishing timing return because the depleted collector/readout dominates.

This gives an exact stopping criterion for the benefit of neutral-region transport engineering inside the model.

---

## 15. Claim boundary

### DERIVED / CONDITIONAL

Under the parametric interface-alignment, ohmic speed, uniform-collector and first-order RC model:

```math
\boxed{
F/F_F^*
=1/w\ (w\le1),
\qquad
=w\ (w\ge1),
}
```

```math
\boxed{
Z(w;\rho)
=\begin{cases}
w^4+\rho^4/w^2,&w\le1,\\
1+\rho^4/w^2,&w\ge1,
\end{cases}
}
```

```math
\boxed{
\rho_c=2^{1/4},
}
```

and for `rho<rho_c`,

```math
\boxed{
w_{\rm timing}=\rho^{2/3}/2^{1/6}.}
```

The normalized local-WKB current penalties are also derived exactly.

### KNOWN / PRIOR

- RC/depletion-capacitance scaling;
- Shockley–Ramo transit;
- minimax field allocation;
- WKB field dependence;
- nondimensional Pareto analysis.

### NON-CLAIM

This is not

- a universal HgCdTe collector design map;
- a full impedance/noise model;
- a high-field calibrated velocity model;
- a Poisson solution;
- a theorem including interface sheet leakage or nonlocal II;
- a novelty claim.

---

## 16. Next decisive step

The collector-side baseline is now sufficiently reduced.

The next physically meaningful attack is **nonlocal impact ionization in the collector**, because it depends on width and energy history in a way that cannot be represented by the local WKB Pareto penalty.

Use the existing nonlocal II surrogate with

```math
L=W_d,
```

and the width-dependent minimum field `F_req(W_d)`.

Then ask:

> **Does finite dead space favor a thinner collector strongly enough to shift the dark-current/avalanche optimum away from `w=1`, even when local TAT/BTBT are minimized there?**

That is the first remaining collector mechanism with genuinely different width physics.