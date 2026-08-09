# HgCdTe Collector Width and Nonlocal Impact Ionization — Mean-Energy Minimum at the Alignment/Transit Crossing

**Date:** 2026-08-09  
**Status:** exact consequence of the one-relaxation-time mean-energy surrogate combined with the parametric collector-width model; stochastic II hazard remains separate; no novelty claim

## 1. Purpose

The collector branch has accumulated a striking pattern:

- required peak field is minimized at `W_F^*`;
- simplified TAT and direct-BTBT currents are minimized at the same width;
- RC timing can pull the preferred width away from that point.

Impact ionization is different from local tunneling because it depends on carrier energy history and dead space.

This note asks:

> **Does the one-relaxation-time nonlocal mean-energy model also favor the alignment/transit crossing, or can thinning the collector suppress II by reducing interaction length?**

The answer is subtle but clean:

> **At fixed interface-alignment + transit requirements, `W_F^*` also minimizes the mean carrier energy at collector exit.**

Thinning shortens the flight time, but the required alignment field rises enough that the carrier has less time to relax and becomes hotter.

---

## 2. Reference collector point

Let the required electrostatic alignment energy be

```math
\boxed{B>0.}
```

Let the target collector transit time be

```math
\boxed{T^*.}
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

Define normalized width

```math
\boxed{w=W/W_F^*.}
```

The minimum-field operating rule is

```math
\boxed{
F/F_F^*
=\begin{cases}
1/w,&w\le1,\\
w,&w\ge1.
\end{cases}
}
```

---

## 3. Mean-energy transport model

Use the existing nonlocal surrogate

```math
\boxed{
\dot\varepsilon
=qFv-\varepsilon/\tau_E.
}
```

For constant field/velocity and cold injection,

```math
\boxed{
\varepsilon_{\rm exit}
=qF\ell_E
(1-e^{-W/\ell_E}),
}
```

where

```math
\boxed{
\ell_E=v\tau_E.
}
```

Let the impact-ionization mean-energy threshold be

```math
\boxed{E_{\rm th}.}
```

Define

```math
\boxed{
b=B/E_{\rm th}}
```

and

```math
\boxed{
\ell_*
=T^*/\tau_E.
}
```

`b` measures how much electrostatic energy the alignment voltage supplies relative to the II threshold.

`ell_*` measures the target transit time relative to energy relaxation.

---

## 4. Useful dimensionless variables

As in the earlier nonlocal model, define

```math
\boxed{
\theta
=\frac{qF\ell_E}{E_{\rm th}},
}
```

```math
\boxed{
\ell
=\frac{W}{\ell_E}
=\frac{T}{\tau_E}.
}
```

The mean exit energy is

```math
\boxed{
\frac{\varepsilon_{\rm exit}}
{E_{\rm th}}
=\theta(1-e^{-\ell}).
}
```

Also

```math
\boxed{
\theta\ell
=\frac{qFW}{E_{\rm th}},
}
```

which is simply the electrostatic field work across the collector normalized to threshold energy.

---

## 5. Thin alignment-limited branch

For

```math
w\le1,
```

the collector field is

```math
F=F_F^*/w.
```

Ohmic velocity is

```math
v=v^*/w,
```

and the actual transit time is

```math
\boxed{T=w^2T^*.}
```

Therefore

```math
\boxed{
\ell(w)
=w^2\ell_*.
}
```

The collector voltage remains exactly the alignment voltage:

```math
qFW=B.
```

Hence

```math
\boxed{
\theta\ell=b
}
```

throughout the entire thin branch.

Therefore

```math
\boxed{
\theta(w)
=\frac{b}
{w^2\ell_*}.
}
```

The mean exit energy becomes

```math
\boxed{
\frac{\varepsilon_{\rm exit}}
{E_{\rm th}}
=
\frac{b}{w^2\ell_*}
\left[
1-e^{-w^2\ell_*}
\right].
}
```

Equivalently, define

```math
\varphi(\ell)
=\frac{1-e^{-\ell}}{\ell}.
```

Then

```math
\boxed{
\frac{\varepsilon_{\rm exit}}
{E_{\rm th}}
=b\varphi(w^2\ell_*).
}
```

---

## 6. Thinning raises mean exit energy on the alignment branch

For

```math
\ell>0,
```

```math
\varphi(\ell)
=\frac{1-e^{-\ell}}{\ell}
```

is strictly decreasing.

Therefore, when `w` decreases below one,

```math
w^2\ell_*
```

decreases and

```math
\varphi
```

increases.

Hence

```math
\boxed{
\varepsilon_{\rm exit}(w)
\text{ increases as }w\text{ is reduced below }1.
}
```

Physical interpretation:

> **The total electrostatic work stays fixed at `B`, but a thinner collector gives the electron less time to dump that energy into the lattice.**

The ballistic limit is

```math
\boxed{
\lim_{w\to0}
\varepsilon_{\rm exit}
=B.
}
```

---

## 7. Important threshold result for `B <= E_th`

Because

```math
0<\varphi(\ell)\le1,
```

```math
\frac{\varepsilon_{\rm exit}}
{E_{\rm th}}
\le b.
```

Therefore if

```math
\boxed{B\le E_{\rm th},}
```

or

```math
\boxed{b\le1,}
```

the mean trajectory cannot reach the II threshold **anywhere on the thin alignment-limited branch**.

This remains true as

```math
W\to0
```

because the total available electrostatic field work is still only `B`.

This is a mean-energy statement, not a stochastic-tail theorem.

---

## 8. Critical thin width when `B > E_th`

If

```math
b>1,
```

the ballistic limit exceeds the mean threshold.

The threshold boundary is

```math
b\varphi(\ell_c)=1.
```

Thus

```math
\boxed{
\frac{1-e^{-\ell_c}}
{\ell_c}
=\frac1b.
}
```

This is the same Lambert-W equation encountered in the earlier relaxation-length phase boundary.

The nonzero solution is

```math
\boxed{
\ell_c
=b+W_0(-be^{-b}).
}
```

If the field-optimal width has

```math
\ell_*>\ell_c,
```

then the mean energy is below threshold at `w=1`, but thinning crosses the threshold at

```math
\boxed{
w_c
=\sqrt{\ell_c/\ell_*}.}
```

For

```math
w<w_c,
```

the mean exit energy exceeds threshold in the surrogate.

Thus thinning can **reopen** mean II even though collector voltage is unchanged.

---

## 9. Thick speed-limited branch

For

```math
w\ge1,
```

the operating field is

```math
F=wF_F^*.
```

Velocity is

```math
v=wv^*,
```

so the transit time remains exactly

```math
\boxed{T=T^*.}
```

Therefore

```math
\boxed{\ell=\ell_*}
```

is constant.

But the collector voltage grows as

```math
qFW=w^2B.
```

Hence

```math
\boxed{
\theta(w)
=\frac{bw^2}{\ell_*}.
}
```

and

```math
\boxed{
\frac{\varepsilon_{\rm exit}}
{E_{\rm th}}
=
\frac{bw^2}{\ell_*}
(1-e^{-\ell_*}).
}
```

Thus mean exit energy rises exactly as

```math
\boxed{w^2}
```

on the thick branch.

---

## 10. Critical thick width

If the field-optimal point is below the mean threshold,

```math
\frac{b}{\ell_*}
(1-e^{-\ell_*})<1,
```

then the thick branch crosses threshold at

```math
\boxed{
w_{c,+}
=
\left[
\frac{\ell_*}
{b(1-e^{-\ell_*})}
\right]^{1/2}.
}
```

For

```math
w>w_{c,+},
```

the mean exit energy exceeds threshold.

---

## 11. Global mean-energy minimum

On the thin branch, mean exit energy decreases monotonically as `w` increases toward one.

On the thick branch, mean exit energy increases monotonically with `w`.

Therefore

```math
\boxed{
w=1}
```

is the unique global minimum of the mean exit energy under the minimum-field operating rule.

Thus the same collector width simultaneously minimizes, in the stated baseline,

- required electric field;
- simplified local TAT current;
- simplified direct-BTBT current;
- mean carrier exit energy / mean-II accessibility.

RC timing remains the main explicitly derived mechanism that can pull the design away from this point.

---

## 12. Why this does not prove stochastic II is minimized at `w=1`

Impact ionization is a stochastic process.

The previous repository surrogate writes

```math
\boxed{
P_{\rm II}
=1-e^{-aH(\theta,\ell)}
}
```

for a chosen energy-dependent rate model.

On the thin branch,

```math
\theta\ell=b
```

is fixed, but changing width trades

```text
higher carrier energy
against
shorter time available for ionization.
```

The mean-energy monotonicity alone does **not** prove the integrated hazard is monotonic.

The stochastic hazard must be evaluated explicitly.

This is the decisive next numerical attack.

---

## 13. Claim boundary

### DERIVED / CONDITIONAL

Inside the ohmic collector + one-energy-relaxation-time surrogate:

```math
\boxed{
\varepsilon_{\rm exit}/E_{\rm th}
=b\varphi(w^2\ell_*),
\qquad w\le1,
}
```

```math
\boxed{
\varepsilon_{\rm exit}/E_{\rm th}
=
(bw^2/\ell_*)(1-e^{-\ell_*}),
\qquad w\ge1.
}
```

and `w=1` is the unique mean-energy minimum.

If `B<=E_th`, the thin alignment branch never reaches the mean threshold.

### KNOWN / PRIOR

- energy-relaxation transport;
- dead-space / nonlocal II concepts;
- impact ionization as a stochastic energy-dependent process.

### NON-CLAIM

This is not

- a proof that stochastic II probability is minimized at `w=1`;
- a calibrated HgCdTe II model;
- a theorem under velocity saturation;
- a complete avalanche model;
- a novelty claim.

---

## 14. Next decisive attack

Use the repository analytic II hazard test case

```math
\Gamma_{\rm II}(E)
=A(E/E_{\rm th}-1),
\qquad E\ge E_{\rm th},
```

with the collector width map

```math
\theta(w),\quad\ell(w).
```

Then determine whether

```math
P_{\rm II}(w)
```

is also minimized at `w=1` or whether the shorter exposure time on the thin branch creates a distinct stochastic optimum.

That question cannot be answered safely from mean energy alone.