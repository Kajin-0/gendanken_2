# Current State — Experiment 01: The Vanishing Absorber

**Date:** 2026-08-08  
**Status:** one-resonance model derived; active-volume-only optical bound falsified in the ideal local continuum model; no novelty claim  

## 1. Active question

Can an ideal photodetector be made arbitrarily small, arbitrarily fast, arbitrarily sensitive, and still absorb essentially every incident photon?

The research has now passed through two distinct stages:

1. a weak absorber in a one-port resonance can retain unity monochromatic absorption only by becoming temporally narrow if its absorptive decay rate `gamma_a` tends to zero;
2. geometric active volume does **not** force `gamma_a` to tend to zero when the electromagnetic field is allowed to concentrate more strongly as the absorber shrinks.

The second result invalidates the simplest active-volume-based route to a general detector bound.

---

## 2. Canonical detailed notes

### One-port dynamics

`ONE_PORT_RESONATOR_DYNAMICS.md`

For a passive one-port resonance,

```math
A(\omega)=
\frac{4\gamma_e\gamma_a}
{(\omega-\omega_0)^2+(\gamma_e+\gamma_a)^2},
```

and the resonant small-signal absorbed-power bandwidth is

```math
\boxed{
B_{3\rm dB}
=
\frac{\gamma_e+\gamma_a}{2\pi}.
}
```

At critical coupling,

```math
\gamma_e=\gamma_a,
\qquad
A_0=1,
\qquad
B_{3\rm dB}=\frac{\gamma_a}{\pi}.
```

Thus, **if `gamma_a -> 0`**, maintaining unity absorption forces the one-resonance detector response to narrow.

### Active-volume counterexample

`ACTIVE_VOLUME_COUNTEREXAMPLE.md`

This note shows that `gamma_a -> 0` does not follow from `V_a -> 0` in a general ideal local-linear passive model.

---

## 3. Explicit counterexample to bounded `gamma_a/V_a`

For weak dielectric loss,

```math
\gamma_a
=
\frac{\omega}{2}p_a\tan\delta,
```

where `p_a` is the active dielectric's electric-energy participation fraction.

Now take an ideal parallel-plate capacitor filled with the active dielectric and scale

```math
d=s d_0,
\qquad
A=s A_0,
\qquad
s\to0.
```

The capacitance remains fixed because

```math
C=\frac{\epsilon_0\epsilon' A}{d}=C_0,
```

while the active volume obeys

```math
\boxed{V_a=Ad\propto s^2\to0.}
```

For fixed modal energy, the capacitor voltage remains fixed but

```math
|E|^2\propto\frac{1}{d^2}\propto\frac{1}{s^2}.
```

Hence

```math
|E|^2V_a=\text{constant},
```

so the active dielectric can retain fixed participation `p_a` and therefore fixed `gamma_a` while its geometric volume vanishes.

Thus

```math
\boxed{
\frac{\gamma_a}{V_a}\to\infty.
}
```

This is an explicit counterexample to the conjecture that passivity alone bounds `gamma_a/V_a` by geometric active volume.

---

## 4. Consequence for the toy detector metric

The earlier idealized bulk dark-event model was

```math
D=g_dV_a.
```

The one-port optimization gave

```math
\boxed{
\mathcal C_{\max}^2
=
\frac{16\gamma_a}{27\pi D},
}
```

where

```math
\mathcal C
=
\frac{h\nu\sqrt{B_{3\rm dB}}}{\mathrm{NEP}}.
```

In the capacitor counterexample,

```math
\gamma_a=\text{constant},
\qquad
D\propto V_a.
```

Therefore the same toy model predicts

```math
\boxed{
\mathcal C_{\max}^2\propto\frac{1}{V_a},
\qquad
\mathcal C_{\max}\propto\frac{1}{\sqrt{V_a}}.
}
```

So the previous conditional volume cancellation is not a universal passive-electromagnetic result.

This divergence should **not** be interpreted as a prediction that a real detector can achieve infinite performance. It shows that at least one assumption must fail before the physical microscopic limit is reached.

---

## 5. Why established per-volume absorption bounds do not contradict this

Known passivity/material-response theory bounds absorption for a specified susceptibility and specified background excitation. For a homogeneous local absorber, a representative bound is

```math
P_{\rm abs}
\le
\frac{\omega\epsilon_0}{2}
\frac{|\chi|^2}{\operatorname{Im}\chi}
\int_{V_a}|\mathbf E_{\rm bg}|^2\,dV.
```

For a uniform plane wave this gives the familiar per-volume scaling

```math
\frac{\sigma_{\rm abs}}{V_a}
\le
k\frac{|\chi|^2}{\operatorname{Im}\chi}.
```

However, if a separate ideal lossless antenna, resonator, transformer, or other field concentrator is admitted as part of the electromagnetic environment, the background field at the active material need not remain fixed as `V_a` shrinks.

The capacitor family has

```math
|E_{\rm bg}|^2\propto\frac{1}{V_a},
```

so `V_a |E_bg|^2` remains finite.

Therefore a material-per-volume bound does not automatically become an **active-volume-only detector bound**. The allowed optical environment must also be constrained.

Primary context includes Miller et al., *Optics Express* 24, 3329-3364 (2016), and Raman, Shin & Fan, *Physical Review Letters* 110, 183901 (2013). These are prior electromagnetic results, not novelty claims of this repository.

---

## 6. What the counterexample teaches

The optical resource is not geometric active volume by itself.

A better variable is electromagnetic participation, but even participation is not yet fundamental: the ideal capacitor keeps participation finite by driving the field amplitude toward infinity as the physical volume shrinks.

The mathematical limit therefore runs directly into microscopic physics.

For fixed modal energy,

```math
|E|\propto\frac{1}{d}.
```

For a single photon, the stored energy is not arbitrarily scalable:

```math
U\sim\hbar\omega.
```

Thus the single-photon field grows without bound in the continuum model as the relevant electromagnetic volume vanishes.

Real matter cannot preserve a fixed bulk susceptibility and linear response indefinitely in that limit.

---

## 7. Physical assumptions expected to fail next

At sufficiently small scale, at least some of the following become unavoidable:

- nonlinear response or saturation;
- dielectric breakdown, tunneling, or ionization;
- spatial nonlocality;
- atomic granularity / finite absorber count;
- finite oscillator strength;
- quantum rather than classical field normalization;
- failure of the extensive dark-event law `D = g_d V_a` once the active degrees of freedom are discrete;
- loss and finite bandwidth in the concentrating structure itself.

The first four are not optional engineering imperfections in the `V_a -> 0` limit. They mark the breakdown of the continuum model that generated the apparent divergence.

---

## 8. Current claim boundary

### Established within stated models

1. The one-port absorbed-power modulation bandwidth is `B_3dB = (gamma_e + gamma_a)/(2 pi)`.
2. Critical coupling with `gamma_a -> 0` becomes temporally narrow.
3. A shrinking active dielectric can nevertheless retain finite `gamma_a` if its energy participation is held fixed by increasing field concentration.
4. The explicit constant-capacitance family has `V_a -> 0`, fixed `gamma_a`, and therefore `gamma_a/V_a -> infinity` within ideal local linear continuum electrodynamics.
5. Geometric active volume alone cannot support the proposed general passive optical bound.

### Not established

- that a real detector can make performance diverge as `V_a -> 0`;
- that lossless field concentration can remain ideal at arbitrarily small scales;
- that the toy dark-event law remains valid to microscopic absorber counts;
- that oscillator strength, nonlocality, quantum saturation, or fluctuation-dissipation produces a particular universal detector bound;
- that any current detector-level result is novel.

---

## 9. Next decisive question

The research question has moved from classical geometric volume to microscopic physical resources:

> **What is the smallest physical resource that cannot be concentrated away: absorber number, oscillator strength, single-photon saturation field, material sum rule, or a fluctuation-dissipation/detailed-balance quantity?**

The next stage should begin with the simplest microscopic absorber model rather than immediately invoking a broad theorem.

A natural test is a finite set of resonant two-level or Lorentz oscillators coupled to one optical mode:

1. replace bulk susceptibility by explicit oscillator strength;
2. normalize the field to one photon;
3. determine how absorption/coupling bandwidth scales as oscillator number decreases;
4. include the minimal irreversible detection or relaxation channel;
5. determine whether thermal/dark excitation scales independently of optical coupling;
6. only then ask whether a geometry-independent detector capability bound survives.

Do not add HgCdTe-specific transport yet. The next bottleneck is the transition from continuum electromagnetism to microscopic light-matter coupling.