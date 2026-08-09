# Active-Volume Counterexample — Fixed Participation with Vanishing Geometric Volume

**Date:** 2026-08-08  
**Status:** explicit counterexample within an ideal local linear passive model; no novelty claim  

## 1. Purpose

The previous one-port calculation showed that detector capability can depend on the ratio

```math
\frac{\gamma_a}{D},
```

where `gamma_a` is the active-material optical amplitude-decay rate and `D` is the dark-event rate.

If both scale linearly with active volume,

```math
\gamma_a\propto V_a,
\qquad
D\propto V_a,
```

the volume cancels from the toy sensitivity-speed metric.

That raised the question:

> Is `gamma_a / V_a` necessarily bounded as `V_a -> 0` in passive electromagnetic systems?

This note gives a direct counterexample to any such statement based on geometric active volume alone.

The counterexample is intentionally idealized. Its purpose is not to propose a practical detector, but to identify which assumption fails.

---

## 2. Loss rate in terms of electric-energy participation

Take a weakly lossy, approximately nondispersive dielectric with

```math
\epsilon_r=\epsilon'+i\epsilon'',
\qquad
\tan\delta=\frac{\epsilon''}{\epsilon'}.
```

For phasor fields with the `exp(-i omega t)` convention, the time-averaged dielectric dissipation is

```math
P_{\rm abs}
=
\frac{\omega\epsilon_0}{2}
\int_{V_a}\epsilon''|\mathbf E|^2\,dV.
```

Define the time-averaged electric energy in the active dielectric by

```math
U_{e,a}
=
\frac{\epsilon_0}{4}
\int_{V_a}\epsilon'|\mathbf E|^2\,dV.
```

Then

```math
\boxed{
P_{\rm abs}=2\omega\tan\delta\,U_{e,a}.
}
```

For a weakly damped resonance, the time-averaged electric and magnetic energies are equal, so if `U` is the total modal energy and

```math
p_a
\equiv
\frac{U_{e,a}}{U_e}
```

is the fraction of electric energy stored in the active dielectric, then

```math
U_e=\frac{U}{2}
```

and therefore

```math
P_{\rm abs}
=
\omega p_a\tan\delta\,U.
```

Using the one-port convention

```math
P_{\rm abs}=2\gamma_a U,
```

gives

```math
\boxed{
\gamma_a
=
\frac{\omega}{2}p_a\tan\delta.
}
```

Equivalently, the material-loss-limited intrinsic quality factor is

```math
\boxed{
Q_a
=
\frac{\omega}{2\gamma_a}
=
\frac{1}{p_a\tan\delta}.
}
```

The important variable is the **energy participation** `p_a`, not geometric volume by itself.

---

## 3. Explicit vanishing-volume capacitor family

Consider an ideal parallel-plate capacitor completely filled by the active dielectric.

Let its plate spacing be `d` and its plate area be `A`.

Its capacitance is

```math
C
=
\frac{\epsilon_0\epsilon' A}{d}.
```

Construct a one-parameter family in which

```math
d=s d_0,
\qquad
A=s A_0,
\qquad
s\to0.
```

Then

```math
\frac{A}{d}
=
\frac{A_0}{d_0},
```

so

```math
\boxed{C=C_0}
```

is independent of `s`.

The active dielectric volume is

```math
V_a=Ad=s^2A_0d_0,
```

so

```math
\boxed{V_a\propto s^2\to0.}
```

Place this capacitor in an otherwise fixed lossless LC resonance. Because `C` remains fixed, the inductance required for a chosen resonance frequency

```math
\omega_0=\frac{1}{\sqrt{LC}}
```

also remains fixed.

Thus neither the resonance frequency nor the external resonator need change as the active dielectric volume tends to zero.

---

## 4. Field scaling

For a fixed modal energy `U`, the capacitor voltage amplitude is fixed because `C=C_0`.

Using phasor amplitudes,

```math
U_e
=
\frac14 C_0|V_c|^2.
```

At resonance, `U=2U_e`, so

```math
|V_c|^2
=
\frac{2U}{C_0},
```

which is independent of `s`.

The electric field in the gap is

```math
E=\frac{V_c}{d}.
```

Therefore

```math
|E|^2\propto\frac{1}{d^2}\propto\frac{1}{s^2}.
```

Meanwhile

```math
V_a\propto s^2.
```

Hence

```math
\boxed{
|E|^2V_a=\text{constant}.
}
```

The divergent field exactly compensates the shrinking dielectric volume.

Because the active dielectric stores essentially all of the capacitor electric energy,

```math
p_a=1
```

for this idealized capacitor loss channel.

Therefore

```math
\boxed{
\gamma_a
=
\frac{\omega_0}{2}\tan\delta
}
```

is independent of active volume.

Consequently

```math
\boxed{
\frac{\gamma_a}{V_a}
\propto
\frac{1}{V_a}
\to\infty.
}
```

This is an explicit passive local-linear counterexample to the conjecture that `gamma_a/V_a` must remain bounded solely because the active material volume vanishes.

---

## 5. Geometry consistency of the scaling

The counterexample is not relying on a parallel-plate approximation that worsens as the structure shrinks.

If a characteristic lateral plate dimension is

```math
\ell\sim\sqrt A\propto\sqrt s,
```

while

```math
d\propto s,
```

then

```math
\frac{\ell}{d}
\propto
\frac{1}{\sqrt s}
\to\infty.
```

Thus the aspect ratio becomes more favorable to the parallel-plate approximation as `s -> 0`, within the continuum model.

The lumped-element approximation also improves relative to a fixed free-space wavelength because the capacitor dimensions shrink.

---

## 6. Consequence for the previous toy detector metric

Retain the earlier bulk dark-event assumption

```math
D=g_dV_a.
```

For this capacitor family,

```math
\gamma_a=\text{constant},
```

while

```math
D\propto V_a\to0.
```

The previously derived optimized one-port metric obeys

```math
\mathcal C_{\max}^2
=
\frac{16\gamma_a}{27\pi D}.
```

Therefore the idealized model predicts

```math
\boxed{
\mathcal C_{\max}^2\propto\frac{1}{V_a},
\qquad
\mathcal C_{\max}\propto\frac{1}{\sqrt{V_a}}.
}
```

At critical coupling, `gamma_e = gamma_a` can also remain finite, so the one-port model can retain

```math
A_0=1
```

and finite modulation bandwidth while the assumed bulk dark-event rate tends to zero.

Thus the earlier conditional volume cancellation is **not** a universal consequence of passive electromagnetism.

It is only valid in a regular shrinking regime in which the active-region field does not scale strongly enough to preserve participation.

---

## 7. Why known per-volume absorption bounds do not rescue an active-volume-only theorem

For a homogeneous local absorber with susceptibility `chi`, fixed external/background field `E_bg`, and polarization

```math
\mathbf P=\epsilon_0\chi\mathbf E,
```

passivity and the optical theorem give a standard material-response bound of the form

```math
\boxed{
P_{\rm abs}
\le
\frac{\omega\epsilon_0}{2}
\frac{|\chi|^2}{\operatorname{Im}\chi}
\int_{V_a}|\mathbf E_{\rm bg}|^2\,dV.
}
```

For a uniform plane-wave background this implies

```math
\boxed{
\frac{\sigma_{\rm abs}}{V_a}
\le
k\frac{|\chi|^2}{\operatorname{Im}\chi}.
}
```

This class of geometry-independent material bound is established prior electromagnetic theory.

It does **not** contradict the capacitor counterexample.

The reason is that the bound is referenced to the field that would exist in the active region in the specified background problem. If a separate ideal lossless antenna, resonator, transformer, or field concentrator is admitted as part of the background environment, that structure can make the background field at the active material scale with geometry.

In the capacitor family above,

```math
|E_{\rm bg}|^2\propto\frac{1}{V_a}.
```

Then

```math
V_a|E_{\rm bg}|^2
```

need not vanish.

So a per-volume material bound does not become an active-volume-only detector bound unless the electromagnetic environment, input channel, and allowed concentrating structure are constrained as well.

This distinction is essential.

---

## 8. Relation to known modal-loss bounds

Prior work also gives material-defined upper bounds on modal nonradiative loss rates for Lorentz/Drude plasmonic systems.

That is consistent with the present logic: a modal material loss rate can remain finite as geometric volume changes, because it is controlled by material dynamics and modal participation rather than by volume alone.

The present counterexample does not claim novelty for participation-factor loss physics or for material-loss-rate bounds.

---

## 9. Where the counterexample must eventually fail physically

The limit `s -> 0` cannot be taken literally for real matter while every continuum parameter remains fixed.

Several assumptions eventually become questionable:

1. **Linear response.** For fixed modal energy, `|E| -> infinity`; real materials saturate, ionize, tunnel, or break down.
2. **Continuum susceptibility.** Once the active region contains only a small number of microscopic absorbers, a bulk `epsilon` and loss tangent cease to be the correct description.
3. **Local response.** At sufficiently small dimensions, spatial dispersion and microscopic charge motion matter.
4. **Classical field amplitude.** For photodetection the energy of one photon is fixed at `hbar omega`; the single-photon electric field grows as mode volume shrinks and cannot be scaled arbitrarily downward.
5. **Dark-event extensivity.** The relation `D = g_d V_a` must fail once the active degrees of freedom are discrete rather than a thermodynamic continuum.
6. **Ideal lossless concentration.** Any real antenna/resonator has additional material, radiative, surface, and fabrication losses that may reintroduce a capability penalty.

These are not small engineering corrections. They identify the physical layer at which a genuinely fundamental bound, if one exists, must live.

---

## 10. Scientific conclusion

The conjecture

```text
passivity alone forces gamma_a / V_a to remain bounded
```

is false under the ideal local linear continuum model when arbitrary lossless field concentration is allowed.

The correct lesson is:

> **Geometric active volume is not the fundamental optical resource. Energy participation can remain finite while geometric volume vanishes.**

Therefore an eventual detector limit must constrain a more physical resource, for example some combination of

- microscopic oscillator number or total oscillator strength;
- material susceptibility together with the allowed concentrating structure;
- single-photon field strength and saturation/nonlinearity;
- nonlocal or atomic length scales;
- full-device size / electromagnetic degrees of freedom;
- bandwidth-integrated coupling to the incident channel;
- fluctuation-dissipation or detailed-balance constraints.

The next research step should determine which of these survives as the minimal unavoidable resource.

---

## 11. Primary-source context

Known ingredients used for orientation, not novelty claims:

- O. D. Miller et al., **Fundamental limits to optical response in absorptive systems**, *Optics Express* 24, 3329-3364 (2016), DOI `10.1364/OE.24.003329`. This work derives geometry-independent per-volume absorption/scattering limits for fixed material susceptibility and external excitation using energy conservation.
- A. Raman, W. Shin, and S. Fan, **Upper Bound on the Modal Material Loss Rate in Plasmonic and Metamaterial Systems**, *Physical Review Letters* 110, 183901 (2013), DOI `10.1103/PhysRevLett.110.183901`. This work shows that modal material loss rates can be bounded by material dynamics rather than arbitrary geometry.

These references narrow the interpretation of the present branch. They do not by themselves supply a detector sensitivity-speed theorem.