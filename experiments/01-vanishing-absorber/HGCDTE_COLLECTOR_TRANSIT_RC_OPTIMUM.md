# HgCdTe Collector Transit–RC Optimum — The Thin-Collector Penalty That Competes with the Tunneling Optimum

**Date:** 2026-08-09  
**Status:** exact timing-variance and stage-feasibility results in a depleted parallel-plate + first-order readout model; standard capacitance/RC physics; no novelty claim

## 1. Purpose

The collector-width branch found a surprisingly robust tunneling optimum:

- interface alignment favors a wider collector;
- transit speed favors a thinner collector;
- simplified TAT and direct BTBT are both minimized at the crossing.

That still leaves an obvious missing thin-layer penalty:

> **junction capacitance increases when the depleted collector becomes thinner.**

This note adds a first-order electrical readout and asks how its RC delay competes with the Shockley–Ramo transit response.

---

## 2. Depletion capacitance

Let the depleted collector have

```math
\boxed{W_d}
```

thickness and electrical area

```math
\boxed{A_d}.
```

Use the parallel-plate depletion approximation

```math
\boxed{
C_j
=\frac{\epsilon_sA_d}{W_d},
}
```

where `epsilon_s` is the semiconductor permittivity.

Let the relevant linear readout resistance be

```math
\boxed{R_{\rm eff}.}
```

Then

```math
\boxed{
\tau_{RC}
=R_{\rm eff}C_j
=\frac{R_{\rm eff}\epsilon_sA_d}{W_d}.
}
```

Thus

```text
thinner depletion
-> larger capacitance
-> longer RC time.
```

---

## 3. Electrical transfer factor

Use a first-order readout pole

```math
\boxed{
H_{RC}(\omega)
=\frac1{1+i\omega\tau_{RC}}.
}
```

The full two-zone response from `HGCDTE_TWO_ZONE_GRADED_DEPLETED_TRANSFER.md` becomes

```math
\boxed{
H_{\rm full}(\omega)
=H_g(\omega)
R_d(\omega)
H_{RC}(\omega),
}
```

where

```math
R_d(\omega)
=e^{-i\omega T_d/2}
\operatorname{sinc}(\omega T_d/2)
```

and

```math
T_d=W_d/v_d.
```

At DC, the RC pole does not change collected QE.

---

## 4. Exact RC timing-kernel interpretation

The first-order low-pass impulse response normalized to unit area is

```math
\boxed{
p_{RC}(t)
=\frac1{\tau_{RC}}
 e^{-t/\tau_{RC}}
\Theta(t).
}
```

This is an exponential delay distribution with

```math
\boxed{
\langle t_{RC}\rangle
=\tau_{RC},
}
```

and

```math
\boxed{
\operatorname{Var}(t_{RC})
=\tau_{RC}^2.
}
```

Because the transfer factors multiply, the normalized impulse responses convolve.

Therefore delay means and variances add.

---

## 5. Exact three-stage timing variance

Let the graded-neutral region have normalized timing variance

```math
\boxed{\sigma_g^2.}
```

The depleted rectangular Ramo pulse contributes

```math
\boxed{
\sigma_d^2
=\frac{T_d^2}{12}
=\frac{W_d^2}{12v_d^2}.
}
```

The RC pole contributes

```math
\boxed{
\sigma_{RC}^2
=\left(
\frac{R_{\rm eff}\epsilon_sA_d}{W_d}
\right)^2.
}
```

Hence

```math
\boxed{
\sigma_{t,\rm full}^2
=
\sigma_g^2
+
\frac{W_d^2}{12v_d^2}
+
\left(
\frac{R_{\rm eff}\epsilon_sA_d}{W_d}
\right)^2.
}
```

This is exact inside the independent linear-kernel model.

---

## 6. Width optimum for fixed drift velocity

Temporarily hold

```math
v_d=\text{constant}
```

and treat the graded-neutral variance `sigma_g^2` as independent of collector width.

Only

```math
\Phi(W_d)
=
\frac{W_d^2}{12v_d^2}
+
\frac{(R_{\rm eff}\epsilon_sA_d)^2}{W_d^2}
```

needs optimization.

Differentiate:

```math
\frac{d\Phi}{dW_d}
=
\frac{W_d}{6v_d^2}
-
\frac{2(R_{\rm eff}\epsilon_sA_d)^2}{W_d^3}.
```

Set equal to zero:

```math
W_d^4
=12v_d^2
(R_{\rm eff}\epsilon_sA_d)^2.
```

Therefore

```math
\boxed{
W_{RC}^*
=12^{1/4}
\sqrt{
v_dR_{\rm eff}\epsilon_sA_d
}.
}
```

This is the exact timing-variance-optimal depletion width for the stated fixed-velocity model.

---

## 7. Equal timing-variance contributions at the optimum

Substitute the stationarity condition:

```math
\boxed{
\frac{(W_{RC}^*)^2}
{12v_d^2}
=
\frac{(R_{\rm eff}\epsilon_sA_d)^2}
{(W_{RC}^*)^2}.
}
```

Hence

```math
\boxed{
\frac{T_d^2}{12}
=
\tau_{RC}^2
}
```

at the optimum.

Equivalently,

```math
\boxed{
T_d
=\sqrt{12}\,\tau_{RC}.
}
```

The optimum therefore balances the **variance**, not the raw time constants.

---

## 8. Minimum added timing variance

At the optimum the two terms are equal, so

```math
\Phi_{\min}
=2\tau_{RC,*}^2.
```

Using the optimal width,

```math
\tau_{RC,*}^2
=
\frac{R_{\rm eff}\epsilon_sA_d}
{\sqrt{12}\,v_d}.
```

Therefore

```math
\boxed{
\Phi_{\min}
=
\frac{R_{\rm eff}\epsilon_sA_d}
{\sqrt3\,v_d}.
}
```

Thus

```math
\boxed{
\sigma_{t,\rm full,min}^2
=
\sigma_g^2
+
\frac{R_{\rm eff}\epsilon_sA_d}
{\sqrt3\,v_d}.
}
```

This is the minimum timing variance available from collector transit + first-order RC at fixed drift velocity.

---

## 9. Separate stage bandwidths

The depleted transit response has

```math
\boxed{
f_{3\rm dB,d}
=0.44294647\frac{v_d}{W_d}.
}
```

The RC pole has

```math
\boxed{
f_{3\rm dB,RC}
=\frac{W_d}
{2\pi R_{\rm eff}\epsilon_sA_d}.
}
```

Therefore the full detector obeys the necessary bound

```math
\boxed{
f_{3\rm dB,full}
\le
\min(
f_{3\rm dB,g},
f_{3\rm dB,d},
f_{3\rm dB,RC}
).
}
```

The actual product response is lower whenever two or more stages roll off comparably.

---

## 10. Fixed-velocity bandwidth-feasibility window

To require both collector stages individually to exceed a target bandwidth

```math
f_* ,
```

we need

```math
0.44294647\frac{v_d}{W_d}
\ge f_*
```

and

```math
\frac{W_d}
{2\pi R_{\rm eff}\epsilon_sA_d}
\ge f_*.
```

Thus

```math
\boxed{
2\pi R_{\rm eff}\epsilon_sA_d f_*
\le
W_d
\le
0.44294647\frac{v_d}{f_*}.
}
```

A feasible width exists only if

```math
\boxed{
f_*^2
\le
\frac{0.44294647\,v_d}
{2\pi R_{\rm eff}\epsilon_sA_d}.
}
```

Therefore the individual-stage feasibility ceiling is

```math
\boxed{
f_*
\le
\sqrt{
\frac{0.44294647\,v_d}
{2\pi R_{\rm eff}\epsilon_sA_d}
}.
}
```

This is a necessary condition, not the exact full-product `-3 dB` optimum.

---

## 11. Relation to the alignment/tunneling width `W^*`

The previous collector optimum was

```math
\boxed{
W_{F}^*
=\sqrt{
\frac{\mu_dT_d^*B}{q}
}.
}
```

It minimizes required field and the simplified local TAT/direct-BTBT currents under the interface-alignment + transit-time target.

The RC timing optimum is

```math
\boxed{
W_{RC}^*
=12^{1/4}
\sqrt{
v_dR_{\rm eff}\epsilon_sA_d
}.
}
```

These depend on different resources.

There is no reason for them to coincide.

Therefore a real collector can have a genuine Pareto conflict:

```text
W near W_F*
-> minimum field / simplified tunneling

W near W_RC*
-> minimum transit+RC timing variance.
```

This is the first width trade in the collector branch that cannot be removed simply by matching the two field constraints.

---

## 12. If `W_RC^* < W_F^*`

The timing-optimal collector is thinner than the field/tunneling optimum.

Moving toward the timing optimum

- reduces transit distance;
- increases capacitance;
- enters the alignment-dominated field branch;
- raises the required electrostatic field;
- worsens local tunneling exposure.

This is a direct speed–dark-current compromise.

---

## 13. If `W_RC^* > W_F^*`

The timing-optimal collector is thicker than the field/tunneling optimum.

Moving toward it

- lowers capacitance;
- increases geometric transit distance;
- enters the speed-dominated field branch;
- raises the field required to maintain the target carrier velocity/time.

Again field-driven leakage increases away from `W_F^*`.

---

## 14. Area becomes an explicit speed resource

Because

```math
W_{RC}^*
\propto\sqrt{A_d}
```

and

```math
\Phi_{\min}
\propto A_d,
```

reducing detector electrical area directly reduces RC timing burden.

This reconnects to the original “small detector” intuition, but in a much narrower and defensible form:

> **small electrical junction area is useful because it reduces capacitance, not because geometric active volume is a universal detector resource.**

Optical concentration / coupling may allow optical collection area and electrical junction area to differ, which is a separate architecture resource already encountered earlier in the project.

---

## 15. High-field velocity and nonuniform capacitance caveats

The fixed-velocity optimum is a baseline only.

In a real depleted collector,

```math
v_d=v_d[F(W_d)]
```

and the field required for interface alignment / transit changes with width.

The capacitance may also deviate from

```math
\epsilon A/W
```

because of

- nonuniform depletion;
- heterojunction permittivity changes;
- fringing fields;
- contact geometry;
- parasitic capacitance external to the depletion region.

Those effects should be added only after the simple competing width scales are understood.

---

## 16. Claim boundary

### DERIVED / CONDITIONAL

For fixed collector drift velocity, parallel-plate depletion capacitance, and first-order readout:

```math
\boxed{
\sigma_t^2
=\sigma_g^2
+W_d^2/(12v_d^2)
+(R_{\rm eff}\epsilon_sA_d/W_d)^2,
}
```

```math
\boxed{
W_{RC}^*
=12^{1/4}
\sqrt{v_dR_{\rm eff}\epsilon_sA_d},
}
```

and at the optimum

```math
\boxed{T_d^2/12=\tau_{RC}^2.}
```

The individual-stage bandwidth-feasibility condition is also derived.

### KNOWN / PRIOR

- depletion capacitance;
- first-order RC filtering;
- Shockley–Ramo transit response;
- convolution/timing-variance addition.

### NON-CLAIM

This is not

- a universal detector bandwidth theorem;
- a calibrated HgCdTe readout model;
- a full impedance/noise optimization;
- a theorem including parasitic capacitance;
- a novelty claim.

---

## 17. Next decisive attack

The collector now has a real three-way geometry problem:

```text
interface alignment / tunneling optimum
+
transit timing
+
RC capacitance.
```

The next clean step is to combine them into a **dimensionless Pareto map** rather than adding another arbitrary physical parameter.

Use normalized width

```math
w=W_d/W_F^*
```

and one ratio

```math
\rho_{RC}=W_{RC}^*/W_F^*.
```

Then plot / derive how

- required field / tunneling burden;
- timing variance;
- RC pole;

change as functions of `w`.

This will show whether a given device is intrinsically field-limited or readout-limited without fixing a particular HgCdTe band-offset model.