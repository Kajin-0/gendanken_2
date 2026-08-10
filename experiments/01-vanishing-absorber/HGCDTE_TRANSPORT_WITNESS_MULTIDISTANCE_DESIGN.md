# Multi-Distance HgCdTe Transport Witness — Facility-Level Observable Design

**Date:** 2026-08-10  
**Status:** conditional measurement-design translation of the witness-posterior requirement; timing, packet-width, and amplitude precisions are regression scales around a synthetic central model, not instrument guarantees; no novelty claim

## 1. Why several propagation distances are preferable to one time-of-flight trace

The relocation inverse primarily needs the **shape** of minority-carrier transport versus electric field and composition.

A multi-distance witness naturally separates transport slopes from common experimental offsets.

For a uniform-composition witness at approximately uniform field:

```math
\boxed{
\langle t\rangle(L)
=t_0+\frac{L}{v}.
}
```

The unknown optical/electrical time zero `t0` is an intercept.

For ordinary one-dimensional drift-diffusion first-passage broadening:

```math
\boxed{
\operatorname{Var}t(L)
=\sigma_{t0}^2
+\frac{2DL}{v^3}.
}
```

The unknown common laser/electronics temporal width is a variance intercept.

For uniform first-order carrier loss:

```math
\boxed{
\ln Q(L)
=\ln Q_0-\frac{L}{v\tau}.
}
```

The unknown injection/collection amplitude scale is an intercept.

Thus the slopes determine

```text
v
D
tau
```

while the largest common calibration nuisances are fitted rather than assumed known.

---

## 2. Central scale used only to convert the equations into timing numbers

Use the same synthetic central witness law as the posterior regression:

```text
T = 300 K
mu = 9000 cm2/Vs
d = 8 kV/cm
r = 2.2
tau = 1 ns
D = mu kT/q only for the synthetic center.
```

The velocity scale is

```math
v(E)=\frac{\mu E}{1+(E/d)^r}.
```

These are **not** claimed material constants.

The actual witness experiment is specifically intended to replace them with measured transport.

---

## 3. Compact six-distance layout

A useful first set is

```math
\boxed{
L=5,\ 10,\ 20,\ 40,\ 70,\ 100\ \mu{\rm m}.
}
```

At each field, use only distances where the measured packet remains above the useful SNR threshold.

The numerical stress uses

```text
Q/Q0 >= 0.05
```

only to keep very strongly attenuated synthetic points from artificially improving the regression.

A real threshold should come from measured noise.

---

## 4. Velocity is the easiest required quantity

For

```math
t=t_0+bL,
\qquad b=1/v,
```

with equal independent centroid uncertainty `sigma_t`,

```math
\sigma_b
=\frac{\sigma_t}
{\sqrt{\sum(L_i-\bar L)^2}}.
```

The current witness posterior needs roughly `20-25%` local velocity precision in the conservative velocity-only route.

For the compact distance set, the most demanding point is the highest field.

### At `3 kV/cm`

The synthetic surviving distance set reaches `100 um`, and the transit-time span is about

```text
0.39 ns.
```

To obtain

```text
25% relative velocity precision
```

requires only approximately

```math
\boxed{87\ {\rm ps}}
```

RMS centroid precision **per distance trace** under the equal-error regression model.

For

```text
10% velocity precision
```

the corresponding scale is about

```math
\boxed{35\ {\rm ps}}.
```

At lower field the transit-time span is longer and the centroid requirement is easier.

Therefore direct velocity calibration should not be the technically limiting witness observable.

---

## 5. Lifetime is also forgiving when fitted as an amplitude slope

For

```math
\ln Q=a-bL,
\qquad b=1/(v\tau),
```

an unknown injection amplitude becomes the intercept `a`.

At `3 kV/cm`, the compact distance set requires only about

```math
\boxed{
\sigma_{\ln Q}\sim0.17
}
```

per point to obtain roughly `50%` relative precision on the lifetime slope, assuming velocity has been measured separately.

This is about a `17%` log-amplitude error scale.

Lower fields generally create stronger attenuation-versus-distance slope and therefore looser amplitude-precision requirements, provided enough distances remain measurable.

---

## 6. Diffusion is the technically demanding witness observable

For the variance law

```math
\operatorname{Var}t
=\sigma_{t0}^2+aL,
\qquad
a=2D/v^3,
```

the desired diffusion information is a small change in packet width on top of the common optical/electrical temporal width.

Use an illustrative

```text
common RMS width sigma_t0 = 30 ps.
```

At `3 kV/cm`, the synthetic packet RMS width over `5-100 um` increases only from approximately

```text
30.3 ps -> 35.0 ps.
```

Under the current weighted variance-line fit, obtaining only

```text
50% relative D precision
```

requires observed RMS packet-width precision of order

```math
\boxed{2.1\ {\rm ps}}
```

per distance point.

This is much more demanding than the velocity-centroid requirement.

---

## 7. Longer drift paths trade voltage for easier diffusion metrology

Consider the extended set

```text
5, 10, 20, 40, 80, 120, 160, 200 um.
```

At `3 kV/cm`, the longest path requires approximately

```text
60 V
```

and the synthetic collected fraction remains substantial in the central `tau=1 ns` stress.

The larger diffusion accumulation relaxes the `50% D` packet-width requirement to approximately

```math
\boxed{4.5\ {\rm ps}}.
```

Thus the witness has a clear experimental trade:

```text
shorter path
-> lower voltage / easier device layout
-> harder high-field D extraction

longer path
-> larger voltage and more loss
-> easier diffusion broadening measurement.
```

The final geometry should be chosen after the actual room-temperature lifetime and breakdown/contact behavior are measured.

---

## 8. Adaptive distance use is better than forcing every field through every bar

If lifetime is short at low field, the longest-distance packets may vanish before collection.

That is not a reason to discard the distance-series architecture.

Use

```text
short distances at low field
longer distances at high field
```

while retaining enough common distances to cross-check the transport model.

The slope fit already handles a different number of usable distances at different fields.

A real experiment should use measured packet SNR, not the current synthetic `5%` survival cutoff, to decide which traces enter the posterior.

---

## 9. Why packet variance should be fitted, not deconvolved one trace at a time

Trying to infer diffusion from a single measured pulse width would require subtracting

```text
laser pulse width
detector/electronics impulse width
contact response
```

in quadrature.

The multi-distance regression is stronger:

```math
\operatorname{Var}t(L)
=\text{common intercept}
+\text{transport slope}\times L.
```

Any stable common width becomes the fitted intercept.

The experiment therefore needs **stability across the distance series** more than it needs perfect knowledge of the absolute impulse response.

This is directly analogous to using several transport distances to remove `t0` from the velocity fit.

---

## 10. Same logic for charge amplitude

Absolute pulse amplitude can vary with

```text
laser coupling
absorption
contact gain
collection efficiency
and detector responsivity.
```

For a given witness composition/field series, use the **distance dependence** of integrated collected charge or a properly normalized packet amplitude.

The intercept absorbs a common injection scale.

The slope constrains transport loss/lifetime.

Any distance-dependent optical coupling or contact-area change must be independently controlled or modeled.

---

## 11. Recommended first witness mask concept

For each witness composition, fabricate several nominally identical lateral transport structures with propagation distances approximately

```text
5
10
20
40
70
100 um.
```

If layout and breakdown margins permit, add one or more long high-field structures near

```text
150-200 um
```

specifically to improve `D(E)` extraction.

Use common

```text
contact metallurgy
passivation
doping target
crystal orientation
optical injection geometry
and readout chain
```

across the distance set.

The exact Shockley-Haynes contact layout should follow the chosen HgCdTe facility's proven process.

---

## 12. Field sequence

The current witness posterior uses

```text
0.1
0.3
0.5
1.0
1.5
2.0
2.5
3.0 kV/cm.
```

For a `100 um` path these correspond to

```text
1
3
5
10
15
20
25
30 V.
```

For a `200 um` high-field witness, `3 kV/cm` corresponds to about `60 V`.

Use pulse duty cycle / thermal checks as needed.

Do not assume the field is uniform until contact and space-charge effects are validated.

---

## 13. What precision should the facility target?

The witness-posterior propagation now suggests two operating levels.

### Velocity-only fallback

If diffusion and lifetime remain essentially uncalibrated, target approximately

```text
20-25% local v(E,x) precision.
```

The multi-distance timing regression shows this is a modest centroid-timing requirement.

### Preferred whole-packet calibration

If the witness extracts even coarse

```text
D(E,x) to factor ~1.6
tau(E,x) to factor ~1.6,
```

then the relocation posterior tolerates velocity uncertainty far larger than `25%` in the current linearized model.

Therefore the experiment should prioritize **complete packet characterization**, even if `D` and `tau` are much less precise than `v`.

---

## 14. Important limitations

The slope formulas above assume approximately

```text
uniform composition
uniform lateral electric field
constant v,D,tau along one witness path
and simple first-order loss.
```

A real witness can violate these through

```text
contact fields
surface fields
carrier heating
space charge
nonuniform doping
and density-dependent recombination.
```

Those effects should be diagnosed by

```text
field reversal / contact controls
multiple injection levels
multiple propagation distances
and full packet-shape residuals.
```

If the simple slope laws fail, use a direct forward transit model rather than forcing a straight-line fit.

---

## 15. Current facility-ready measurement request

For each of approximately

```math
x=0.35,\ 0.43,\ 0.51,
```

request a p-type transport-witness distance series capable of measuring, over `0.1-3 kV/cm`:

```text
packet centroid versus distance
packet temporal variance versus distance
integrated packet charge/amplitude versus distance
Hall/doping state
and electrical impulse response.
```

The desired first precision targets are approximately

```text
v: <=20-25% locally if used without D/tau support
D: factor ~1.6 is already useful
tau: factor ~1.6 is already useful.
```

The high-field `D` measurement is the only part that presently looks close to an instrument-resolution challenge in the synthetic scale study.

---

## 16. Numerical implementation

`numerics/hgcdte_transport_witness_multidistance_design.py`
