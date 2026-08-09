# Active Frequency-Converter Baseline — Pump Resource Required for Simultaneous Conversion Bandwidth

**Date:** 2026-08-08  
**Status:** exact two-mode pumped-converter derivation; strong direct prior-art overlap with quantum frequency conversion; supporting baseline only; no novelty claim  

## 1. Purpose

The passive/absorbing front-end analysis has reached a natural boundary.

A known way to evade passive time-invariant matching limits is to inject work through

- temporal modulation;
- parametric pumping;
- coherent frequency conversion;
- active/non-Foster response.

This note begins the active branch with the smallest analytically controlled quantum-optical model:

> two damped resonant modes coupled coherently by a classical pump.

The goal is not to claim frequency conversion as new. It is to establish a calibrated resource baseline for asking what pump resource is required to broaden photon acceptance beyond a passive detector resonance.

---

## 2. Linearized pumped converter

Let

```text
a  incident/signal-side resonant mode
b  receiving/detector-side resonant mode.
```

In a rotating frame, after linearizing a three- or four-wave-mixing interaction around a strong coherent pump, use

```math
\boxed{
\dot a
=-\Gamma_a a-iG b
+\sqrt{2\Gamma_a}\,s_{\rm in},
}
```

```math
\boxed{
\dot b
=-\Gamma_b b-iG^* a.
}
```

For the clean baseline, all damping is assumed useful:

- `Gamma_a` is the signal-port amplitude-decay rate;
- `Gamma_b` is the receiving/detector-port amplitude-decay rate;
- there is no parasitic loss;
- the classical pump is undepleted.

Choose the pump phase so

```math
G>0.
```

The detector/output amplitude is

```math
s_R=\sqrt{2\Gamma_b}\,b.
```

This model is standard quantum-frequency-conversion coupled-mode theory.

---

## 3. Exact conversion spectrum

For a monochromatic signal with rotating-frame detuning `delta`, solve

```math
(\Gamma_a-i\delta)a+iG b
=\sqrt{2\Gamma_a}\,s_{\rm in},
```

```math
iG a+(\Gamma_b-i\delta)b=0.
```

The conversion amplitude is

```math
\boxed{
\frac{s_R}{s_{\rm in}}
=
\frac{-i\,2G\sqrt{\Gamma_a\Gamma_b}}
{(\Gamma_a-i\delta)(\Gamma_b-i\delta)+G^2}.
}
```

Hence the photon-number conversion probability is

```math
\boxed{
T(\delta)
=
\frac{4G^2\Gamma_a\Gamma_b}
{\left|
(\Gamma_a-i\delta)(\Gamma_b-i\delta)+G^2
\right|^2}.
}
```

---

## 4. Unit peak conversion fixes the pump-enhanced coupling

At resonance,

```math
T_0
=
\frac{4G^2\Gamma_a\Gamma_b}
{(\Gamma_a\Gamma_b+G^2)^2}.
```

By the arithmetic-geometric mean inequality,

```math
\boxed{T_0\le1}
```

with equality precisely when

```math
\boxed{
G^2=\Gamma_a\Gamma_b.
}
```

Thus perfect active frequency conversion still requires a matching condition: the coherent pump-enhanced coupling must match the geometric mean of the two resonator access rates.

This is established converter physics.

---

## 5. Conversion spectrum at unit peak

Impose

```math
G^2=\Gamma_a\Gamma_b.
```

Define

```math
p=\Gamma_a\Gamma_b,
\qquad
d=\Gamma_a-\Gamma_b.
```

Then

```math
\boxed{
T(\delta)
=
\frac{4p^2}
{4p^2+d^2\delta^2+\delta^4}.
}
```

This form makes the bandwidth optimization transparent.

---

## 6. Exact FWHM condition

Let

```math
x=\delta_{1/2}^2,
```

where `delta_{1/2}>0` is the positive half-maximum detuning.

The condition

```math
T(\delta_{1/2})=\frac12
```

gives

```math
\boxed{
x^2+d^2x=4p^2.}
```

The full angular-frequency FWHM is

```math
W=2\sqrt{x}.
```

---

## 7. Minimum pump coupling for a prescribed unit-conversion bandwidth

For fixed

```math
p=G^2,
```

the equation

```math
x^2+d^2x=4p^2
```

shows that any nonzero mismatch

```math
d^2>0
```

reduces `x` and therefore narrows the FWHM.

Hence the **largest FWHM for a given pump-enhanced coupling** occurs at

```math
\boxed{
\Gamma_a=\Gamma_b\equiv\Gamma.
}
```

For the symmetric optimum,

```math
p=\Gamma^2,
\qquad
G=\Gamma,
```

and

```math
x^2=4\Gamma^4.
```

Thus

```math
\delta_{1/2}=\sqrt2\,\Gamma,
```

and

```math
\boxed{
W_{\rm FWHM}=2\sqrt2\,\Gamma.
}
```

Since `G=Gamma`, the exact minimum pump-enhanced coupling compatible with unit peak conversion and FWHM at least `W` is

```math
\boxed{
G_{\min}
=\frac{W}{2\sqrt2}.
}
```

Equality is attained only by the symmetric converter.

---

## 8. Flat-topped critical spectrum

At the optimum

```math
\Gamma_a=\Gamma_b=G=\Gamma,
```

the spectrum simplifies to

```math
\boxed{
T(\delta)
=
\frac{4\Gamma^4}
{4\Gamma^4+\delta^4}
=
\frac{1}
{1+\delta^4/(4\Gamma^4)}.
}
```

The quadratic detuning term cancels exactly.

This produces the familiar flat-topped critical-conversion line shape noted in prior microresonator quantum-frequency-conversion theory.

---

## 9. Pump photon-number resource

Let the pump-enhanced coherent coupling be

```math
\boxed{
G=g_0\sqrt{N_p},
}
```

where

- `g_0` is the single-pump-photon coupling constant for the chosen nonlinear interaction and mode normalization;
- `N_p` is the intracavity coherent pump photon number.

Then the bandwidth condition gives

```math
N_p
=\frac{G^2}{g_0^2}
\ge
\boxed{
\frac{W^2}{8g_0^2}
}.
```

Therefore this specific active architecture has the resource scaling

```math
\boxed{
N_{p,\min}
\propto W^2
}
```

for **simultaneous unit-peak conversion over a FWHM `W`**.

This is an architecture-specific baseline, not a universal active-detector theorem.

---

## 10. Pump stored energy and maintenance power

The coherent pump stores approximately

```math
\boxed{
U_p
=\hbar\omega_p N_p.
}
```

Therefore

```math
\boxed{
U_p
\ge
\hbar\omega_p
\frac{W^2}{8g_0^2}.
}
```

If the pump mode itself has amplitude-decay rate

```math
\Gamma_p,
```

its stored energy decays at rate `2 Gamma_p`. Maintaining the undepleted coherent pump then requires at least the dissipative replenishment power

```math
P_{p,\rm hold}
=2\Gamma_p U_p.
```

Hence

```math
\boxed{
P_{p,\rm hold}
\ge
\frac{\hbar\omega_p\Gamma_p}{4g_0^2}
W^2.
}
```

This maintenance-power statement assumes a resonantly maintained pump mode with the stated loss rate. It is not a universal work bound.

---

## 11. Energy per converted quantum is a different resource

For sum-frequency conversion,

```math
\omega_R=\omega_L+\omega_p.
```

Energy conservation implies that an ideal successfully converted signal quantum acquires pump energy

```math
\hbar\omega_p.
```

This **event energy** is conceptually distinct from the coherent pump field required to maintain a large coupling `G` and broad simultaneous conversion bandwidth.

Therefore active detector accounting must distinguish

```text
pump energy transferred per detected photon
```

from

```text
standing/maintenance pump resource needed to create broadband coupling.
```

---

## 12. Direct prior-art collision

Z. Vernon, M. Liscidini, and J. E. Sipe,

**“Quantum frequency conversion and strong coupling of photonic modes using four-wave mixing in integrated microresonators,”**
*Physical Review A* **94**, 023810 (2016), DOI `10.1103/PhysRevA.94.023810`.

They derive analytic quantum-frequency-conversion spectra, pump-power requirements, strong intermode coupling, and the flat-topped critical conversion response of pumped microresonators.

Therefore the following are **not novelty claims** of this repository:

- pump-enhanced coherent mode coupling;
- critical pump strength for unit conversion;
- flat-topped conversion spectra;
- pump-power requirements for microresonator frequency conversion;
- the idea that active frequency conversion can shift single photons while preserving quantum statistics.

This note is a calibrated baseline for the next resource question.

---

## 13. Relation to passive Bode–Fano escape

Time-modulated and active electromagnetic structures are already known to exceed limits that apply only to passive linear time-invariant matching.

For example, time-modulated energy trapping has been demonstrated theoretically and experimentally as a route beyond a passive Bode–Fano absorption bound for short pulses.

Thus the qualitative statement

```text
active/time-varying systems can beat passive bandwidth bounds
```

is established prior physics.

The useful detector question is instead

> **what active resource must scale with the gained photon-capture bandwidth while click probability and noise are held fixed?**

---

## 14. Claim boundary

### Derived exactly within this two-mode model

For unit peak conversion and angular FWHM `W`,

```math
\boxed{
G\ge\frac{W}{2\sqrt2}.
}
```

For `G=g_0 sqrt(N_p)`,

```math
\boxed{
N_p\ge\frac{W^2}{8g_0^2}.
}
```

Equality occurs for

```math
\Gamma_a=\Gamma_b=G.
```

### Not established

- novelty of these converter formulas;
- a universal quadratic pump-resource law for all active capture systems;
- optimality against multimode pumps, broadband traveling-wave conversion, frequency sweeps, or time-modulated capture;
- a minimum thermodynamic work cost;
- a pump-noise / dark-count bound;
- that frequency conversion by itself improves total detector performance.

---

## 15. Next adversarial attack

The obvious counterexample to the `W^2` scaling is to distribute the pump resource over

- multiple frequency-conversion channels;
- a broadband traveling-wave nonlinear medium;
- multiple pump tones;
- a temporally swept resonance;
- a non-Foster / actively matched front end.

The next question is therefore:

> **Can a multimode or continuum pump reduce the total pump-resource scaling below `W^2`, and if so is there a more general pump spectral-norm / photon-flux bound on integrated conversion?**

Do not treat the present `W^2` result as fundamental until that attack is completed.