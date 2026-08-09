# Nonequilibrium Optical-Response Audit — Readiness Pumping Does Not Beat the Fully Ready Passive Transition

**Date:** 2026-08-08  
**Status:** derived weak-probe result for the unified three-level rate/Lindblad model; standard optical-Bloch physics; no novelty claim  

## 1. Question

The finite passive capture theorem does not apply to an optically active gain medium.

The unified three-level detector is maintained out of equilibrium by a reset/work source, so the obvious adversarial question is:

> Can that nonequilibrium resource make the signal transition absorb more strongly than the fully ready passive transition and thereby evade the capture/access bound?

For the minimal incoherently pumped three-level machine, the answer is no as long as the signal transition remains absorptive rather than inverted.

---

## 2. Dark steady-state populations

Use the notation from `UNIFIED_THREE_LEVEL_CAPTURE_MACHINE.md`:

```text
u : 0 -> 1   reset/preparation
 d : 1 -> 0  reverse reset
 a : 1 -> 2  incoherent optical upward rate
 b : 2 -> 1  optical downward rate
 c : 2 -> 0  detector-channel downward rate
 e : 0 -> 2  detector-channel reverse rate.
```

The exact stationary probabilities are

```math
p_1
=
\frac{be+bu+cu}{Z},
```

```math
p_2
=
\frac{ae+au+de}{Z},
```

with

```math
Z
=
ac+ae+au
+bd+be+bu
+cd+cu+de.
```

Therefore the signal-transition population difference is

```math
\boxed{
w
\equiv
p_1-p_2
=
\frac{
be+bu+cu-ae-au-de
}{Z}.
}
```

Equivalently,

```math
\boxed{
w
=
\frac{
e(b-a-d)+u(b+c-a)
}{Z}.
}
```

---

## 3. Add a weak coherent optical probe

Let the signal field drive the transition

```text
|1> <-> |2>
```

with carrier detuning

```math
\Delta=\omega-\omega_{21}.
```

Write the weak coherent drive in the usual rotating-wave form with Rabi frequency `Omega`.

To first order in the probe amplitude, the populations remain at their dark steady-state values while the optical coherence obeys

```math
\boxed{
\dot\rho_{21}^{(1)}
=
-(\gamma_\perp+i\Delta)\rho_{21}^{(1)}
+
\frac{i\Omega}{2}(p_1-p_2).
}
```

The transverse decay rate for the incoherent rate model is

```math
\boxed{
\gamma_\perp
=
\frac12(a+d+b+c)+\gamma_\phi,
}
```

where `gamma_phi >= 0` is any additional pure dephasing.

The rates `u` and `e`, which feed population **into** the two optical levels from `|0>`, do not directly appear in the anticommutator dephasing of the `1-2` coherence in this minimal Lindblad representation; they affect the response through the steady-state populations.

---

## 4. Exact weak-probe coherence

At steady state,

```math
\boxed{
\rho_{21}^{(1)}
=
\frac{i\Omega}{2}
\frac{p_1-p_2}
{\gamma_\perp+i\Delta}.
}
```

Thus the linear optical susceptibility has the standard form

```math
\boxed{
\chi_{\rm opt}(\omega)
\propto
\frac{p_1-p_2}
{\gamma_\perp-i\Delta}.
}
```

The entire nonequilibrium-state dependence of the oscillator's weak-probe sign and amplitude enters through

```math
\boxed{w=p_1-p_2.}
```

This is established optical-Bloch physics, used here only to test the detector-resource argument.

---

## 5. Absorption, bleaching, and gain

### Absorbing detector state

If

```math
p_1>p_2,
```

then

```math
w>0
```

and the signal transition has ordinary positive absorption.

### Saturated / transparent state

If

```math
p_1=p_2,
```

then

```math
w=0
```

and the net linear absorption vanishes.

### Inverted state

If

```math
p_2>p_1,
```

then

```math
w<0
```

and the signal sees stimulated emission / gain rather than passive absorption.

---

## 6. Fully ready state is the maximum absorptive population factor

For any physical populations,

```math
0\le p_1\le1,
\qquad
0\le p_2\le1.
```

In the non-inverted absorbing regime,

```math
0\le p_1-p_2\le1.
```

The upper limit

```math
\boxed{p_1-p_2=1}
```

occurs only for the ideal fully ready operating point

```math
p_1=1,
\qquad
p_2=0.
```

Therefore an incoherent nonequilibrium pump that merely restores population to the lower signal state cannot increase the weak absorptive oscillator response above the fully ready passive transition.

It can only

- restore the lost oscillator weight caused by imperfect readiness;
- broaden/dephase the transition through additional rates;
- or, if it overpopulates the upper signal state, turn the transition into gain.

---

## 7. Consequence for the passive capture bound

The earlier passive capture theorem was derived for the detector conditioned on being in its ready state.

The present calculation shows that, in this minimal incoherently pumped detector,

```text
non-inverted NESS optical response
<=
fully ready passive optical response
```

at the level of the transition population factor.

Thus the nonequilibrium reset source does **not** provide a hidden enhancement that invalidates the ready-state capture ceiling in the ordinary absorbing regime.

A conservative resource statement is

```math
\boxed{
\text{absorptive response in NESS}
\le
\text{fully ready response}
}
```

with equality only at `p_1=1, p_2=0` when other linewidth changes are held fixed.

This is not a new optical sum rule. It is the direct consequence of the population-difference factor in linear response.

---

## 8. Why optical gain is a different problem

If the autonomous work source produces

```math
p_2>p_1,
```

then the signal transition is active.

The passive harmonic capture theorem no longer applies because the optical subsystem can now deliver energy into the propagating field.

But this is not a free counterexample:

```text
optical gain
-> population inversion
-> continuous nonequilibrium pump/free-energy resource.
```

Moreover, stimulated emission on the `2 -> 1` signal transition is not the same task as irreversible photon capture into the counted `2 -> 0` channel. Depending on the architecture, inversion may actually compete with the desired click pathway.

Therefore any gain-assisted escape must be analyzed as an explicitly active detector with pump resource included in the input-output accounting.

---

## 9. Dark-state inversion condition

Using the exact stationary populations, the signal transition is inverted when

```math
\boxed{
ae+au+de
>
be+bu+cu.
}
```

Equivalently,

```math
\boxed{
e(a+d-b)+u(a-b-c)>0.
}
```

A detector designed to sit predominantly in the ready state `|1>` normally operates on the opposite side of this inequality.

This exposes a useful design distinction:

```text
ready-state pumping
!=
optical-transition inversion.
```

The former prepares the detector to absorb; the latter turns the front end into an amplifier.

---

## 10. Relation to the 2018 and 2026 frameworks

Young, Sarovar & Léonard already provide the general incoming-field quantum machinery needed to compute such nonequilibrium optical responses in more complex detector architectures.

Schwarzhans et al. provide an explicit autonomous thermal machine that maintains a metastable detection-ready state and quantify its thermodynamic performance.

The present calculation only isolates the missing interface in the simplest analytic form:

> a work source that maintains readiness does not automatically evade passive spectral capture bounds unless it also makes the optical transition active.

---

## 11. Claim boundary

### Derived within the minimal weak-probe model

```math
\boxed{
\rho_{21}^{(1)}
=
\frac{i\Omega}{2}
\frac{p_1-p_2}
{\gamma_\perp+i\Delta}
}
```

with

```math
\boxed{
\gamma_\perp
=\frac12(a+d+b+c)+\gamma_\phi.
}
```

For a non-inverted operating point,

```math
\boxed{0\le p_1-p_2\le1.}
```

Therefore incoherent readiness pumping cannot make the absorptive population factor exceed the fully ready passive value.

### Not established

- a general theorem for coherently pumped or parametrically driven detectors;
- a passive-bound extension to optical gain media;
- a universal relation between optical gain and entropy production;
- that every autonomous photodetector remains non-inverted on its signal transition;
- publication novelty.

---

## 12. Next decisive attack

The natural remaining escape is now **coherent active capture** rather than simple readiness pumping.

Ask:

> Can a coherently driven/time-dependent/parametric front end use pump work to broaden the incident-photon acceptance while preserving high irreversible click probability, and what work/entropy resource scales with that bandwidth?

Before opening that active branch, the current passive-plus-autonomous results should be consolidated and subjected to a focused publication-level prior-art assessment.