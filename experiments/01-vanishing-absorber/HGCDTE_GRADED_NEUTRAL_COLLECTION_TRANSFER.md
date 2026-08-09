# HgCdTe Graded Neutral Absorber — Exact Collection Efficiency and Frequency Response from a Bandgap-Drive Budget

**Date:** 2026-08-09  
**Status:** exact drift+recombination transport in a constant-quasi-field neutral absorber; composition-gradient carrier drive is established prior physics; no novelty claim

## 1. Purpose

`HGCDTE_QUASINEUTRAL_GRADED_PINNING.md` showed that a quasi-neutral p-type graded HgCdTe region naturally approaches

```text
valence band nearly pinned
+
conduction band inherits most of the bandgap gradient.
```

`HGCDTE_LINEAR_GRADED_KANE_WKB.md` showed why that geometry suppresses the ordinary direct-Zener path relative to a same-slope common electrostatic tilt.

The next question is detector-facing:

> **How much carrier-collection speed and efficiency does a finite band-edge drop actually buy?**

This note solves the simplest neutral graded absorber exactly under

- constant conduction-band slope;
- constant minority-electron mobility;
- deterministic drift;
- one exponential minority lifetime;
- no diffusion;
- perfect collection at the depletion/junction boundary.

The model is deliberately minimal, but it produces closed collection and modulation formulas.

---

## 2. Geometry and band-edge drive

Let the quasi-neutral graded absorber occupy

```math
0\le x\le L_g,
```

with the collecting depletion region at

```math
x=L_g.
```

Let the conduction band drop by

```math
\boxed{\Delta E_c>0}
```

from `x=0` to `x=L_g`.

For a linear profile,

```math
\boxed{
-\frac{dE_c}{dx}
=\frac{\Delta E_c}{L_g}.
}
```

Define the equivalent minority-electron quasi-field

```math
\boxed{
F_q
=\frac{\Delta E_c}{qL_g}.
}
```

In the low-field drift approximation,

```math
\boxed{
v_n
=\mu_nF_q
=\frac{\mu_n\Delta E_c}
{qL_g}.
}
```

Therefore the longest deterministic transit time, from `x=0` to the collector, is

```math
\boxed{
T_g
=\frac{L_g}{v_n}
=\frac{qL_g^2}
{\mu_n\Delta E_c}.
}
```

This is the first central relation.

The finite composition/band-edge drop plays the role of an internal transport-energy resource.

---

## 3. Relation to the voltage-transit bound

For a homogeneous electrically driven ohmic region,

```math
T
=\frac{L^2}{\mu V}.
```

Since an electron crossing voltage `V` changes electrostatic potential energy by `qV`, the graded neutral result can be written

```math
\boxed{
T_g
=\frac{L_g^2}
{\mu_n(\Delta E_c/q)}.
}
```

Thus

```text
electrostatic voltage V
```

and

```text
band-edge drop Delta E_c/q
```

have the same kinematic role in this simple drift equation.

They do **not** have the same interband tunneling geometry, which is the reason grading can be advantageous.

---

## 4. Add minority-carrier recombination

Let the minority-electron lifetime in the neutral absorber be

```math
\boxed{\tau_n.}
```

An electron generated at position `x` requires

```math
\boxed{
t_x
=\frac{L_g-x}{v_n}
}
```

to reach the collector.

Under exponential survival,

```math
\boxed{
P_{\rm surv}(x)
=\exp[-t_x/\tau_n].
}
```

Define the dimensionless transport/recombination ratio

```math
\boxed{
\xi
\equiv
\frac{T_g}{\tau_n}
=\frac{qL_g^2}
{\mu_n\tau_n\Delta E_c}.
}
```

This single parameter controls the neutral-region collection problem for uniform generation.

---

## 5. Exact collection efficiency for uniform generation

Assume photocarriers are generated uniformly in `x`.

The collected fraction of generated electrons is

```math
\eta_{\rm col}
=\frac1{L_g}
\int_0^{L_g}
\exp\left[-
\frac{L_g-x}{v_n\tau_n}
\right]dx.
```

Set

```math
u=(L_g-x)/L_g.
```

Then

```math
\boxed{
\eta_{\rm col}(\xi)
=\int_0^1e^{-\xi u}du
=\frac{1-e^{-\xi}}{\xi}.
}
```

This is exact inside the stated drift/recombination model.

Limits:

### Fast collection

```math
\xi\ll1
```

gives

```math
\eta_{\rm col}
=1-\frac\xi2+O(\xi^2).
```

### Slow collection

```math
\xi\gg1
```

gives

```math
\eta_{\rm col}
\simeq\frac1\xi
=\frac{v_n\tau_n}{L_g}.
```

Only carriers generated within approximately one drift length `v_n tau_n` of the collector survive.

---

## 6. Exact inverse — minimum band-edge drop for target collection efficiency

For a required

```math
\eta_{\rm col}\ge\eta_*,
```

define `xi_*` by

```math
\eta_*
=\frac{1-e^{-\xi_*}}{\xi_*}.
```

The nonzero solution is expressible with Lambert `W`:

```math
\boxed{
\xi_*
=\frac1{\eta_*}
+W_0\!\left[
-\frac1{\eta_*}
 e^{-1/\eta_*}
\right].
}
```

Because collection efficiency decreases monotonically with `xi`, the required band-edge drop is

```math
\boxed{
\Delta E_c
\ge
\frac{qL_g^2}
{\mu_n\tau_n\xi_*}.
}
```

For a nearly pinned valence band,

```math
\Delta E_c\simeq\Delta E_g
```

up to the density-of-states/band-offset corrections derived in `HGCDTE_QUASINEUTRAL_GRADED_PINNING.md`.

Thus the composition range required for efficient neutral-region collection can be estimated directly from

```text
absorber thickness
mobility
minority lifetime
target collection efficiency.
```

---

## 7. Exact small-signal collection transfer function

Let the uniform photogeneration rate be weakly modulated at angular frequency `omega`.

Each generation position contributes with

- delay `t_x`;
- survival factor `e^{-t_x/tau_n}`.

Relative to the total generated modulation, the complex collected-flux response is

```math
H(\omega)
=\frac1{L_g}
\int_0^{L_g}
\exp[-(1/\tau_n+i\omega)t_x]dx.
```

Define

```math
\boxed{\Omega=\omega T_g.}
```

Then the integral is exact:

```math
\boxed{
H(\Omega,\xi)
=
\frac{1-e^{-(\xi+i\Omega)}}
{\xi+i\Omega}.
}
```

At zero frequency,

```math
H(0,\xi)
=\eta_{\rm col}(\xi).
```

Therefore the transfer function normalized to its DC collected signal is

```math
\boxed{
\widehat H(\Omega,\xi)
=
\frac{\xi}
{1-e^{-\xi}}
\frac{1-e^{-(\xi+i\Omega)}}
{\xi+i\Omega}.
}
```

This cleanly separates

```text
DC collection loss
```

from

```text
frequency dependence of the surviving carriers.
```

---

## 8. Fast-collection limit recovers the familiar transit constant

For

```math
\xi\to0,
```

```math
\boxed{
\widehat H
\to
\frac{1-e^{-i\Omega}}
{i\Omega}
=e^{-i\Omega/2}
\frac{2\sin(\Omega/2)}{\Omega}.
}
```

Thus

```math
|\widehat H|
=\left|
\frac{\sin(\Omega/2)}
{\Omega/2}
\right|.
```

The half-power solution is

```math
\boxed{
\Omega_{3\rm dB}
\simeq2.7831147565.
}
```

Therefore

```math
\boxed{
f_{3\rm dB}
\simeq
\frac{0.44294647}{T_g}
}
```

and

```math
\boxed{
f_{3\rm dB}
\simeq
0.44294647
\frac{\mu_n\Delta E_c}
{qL_g^2}.
}
```

This recovers the `c_t ~= 0.443` transit constant used earlier in the repository, now directly from the distributed neutral-absorber collection response.

---

## 9. Slow-collection limit exposes a deceptive bandwidth effect

If

```math
\xi\gg1,
```

then `e^{-xi}` is negligible and

```math
\widehat H
\simeq
\frac{\xi}{\xi+i\Omega}.
```

So

```math
\boxed{
\omega_{3\rm dB}
\simeq
\frac1{\tau_n},
}
```

or

```math
\boxed{
f_{3\rm dB}
\simeq
\frac1{2\pi\tau_n}.
}
```

But simultaneously

```math
\boxed{
\eta_{\rm col}
\simeq\frac1\xi\ll1.
}
```

This is a critical interpretation point:

> A slow graded absorber can appear to have a finite normalized modulation bandwidth because only carriers generated near the collector survive. The bandwidth does not imply efficient full-volume collection.

Therefore detector speed must not be quoted without its DC collection efficiency.

---

## 10. Exact collection-bandwidth equation

For arbitrary `xi`, the normalized half-power point is defined by

```math
\boxed{
\left|
\widehat H(\Omega_{3\rm dB},\xi)
\right|^2
=\frac12.
}
```

Using the closed response,

```math
\boxed{
\frac{\xi^2}
{(1-e^{-\xi})^2}
\frac{
1+e^{-2\xi}
-2e^{-\xi}\cos\Omega
}
{\xi^2+\Omega^2}
=\frac12.
}
```

This one-dimensional equation can be solved deterministically for `Omega_3dB(xi)`.

Then

```math
\boxed{
f_{3\rm dB}
=\frac{\Omega_{3\rm dB}(\xi)}
{2\pi T_g}
=\frac{\Omega_{3\rm dB}(\xi)}
{2\pi\xi\tau_n}.
}
```

The only dimensionless control parameter remains `xi`.

---

## 11. Representative dimensionless values

| `xi=T_g/tau_n` | `eta_col` | `Omega_3dB` | `f_3dB T_g` |
|---:|---:|---:|---:|
| 0 | 1 | 2.7831 | 0.44295 |
| 0.1 | 0.9516 | 2.7840 | 0.44308 |
| 0.3 | 0.8639 | 2.7908 | 0.44417 |
| 1 | 0.6321 | 2.8686 | 0.45656 |
| 2 | 0.4323 | 3.1293 | 0.49804 |
| 5 | 0.1987 | 5.0457 | 0.80305 |
| 10 | 0.1000 | 10.0017 | 1.59182 |

The apparent increase in `f_3dB T_g` at large `xi` reflects recombination selecting only short-delay carriers, not improved collection of the full absorber.

---

## 12. Beer-Lambert generation profile

Uniform generation is useful analytically but not optically general.

For illumination at `x=0`, take

```math
w(x)
=\alpha e^{-\alpha x}.
```

Define optical thickness

```math
\boxed{a=\alpha L_g.}
```

Normalize to the photons absorbed in the neutral region:

```math
\int_0^{L_g}w(x)dx
=1-e^{-a}.
```

The exact collected modulation response is

```math
\boxed{
H_{\rm BL}(a,z)
=
\frac{a[e^{-z}-e^{-a}]}
{(a-z)(1-e^{-a})},
\qquad
z=\xi+i\Omega.
}
```

When

```math
z\to a,
```

the removable singularity has limit

```math
\boxed{
H_{\rm BL}
\to
\frac{ae^{-a}}
{1-e^{-a}}.
}
```

At DC,

```math
\boxed{
\eta_{\rm col,BL}
=
\frac{a[e^{-\xi}-e^{-a}]}
{(a-\xi)(1-e^{-a})}.
}
```

This formula makes illumination direction important:

- if light is absorbed mainly near `x=0`, far from the collector, recombination penalty is stronger;
- if the optical field is arranged to generate carriers nearer the collecting boundary, collection improves.

So optical mode engineering and graded transport are coupled through the **spatial generation profile**, not just total absorption.

---

## 13. Bandgap-budget interpretation

In the ideal p-type pinned-valence limit,

```math
\Delta E_c\simeq\Delta E_g.
```

Therefore

```math
\boxed{
T_g
\simeq
\frac{qL_g^2}
{\mu_n\Delta E_g}.
}
```

For a target fast-collection bandwidth in the `xi << 1` regime,

```math
\boxed{
\Delta E_g
\simeq
\frac{qL_g^2}
{0.44294647\mu_n}
 f_{3\rm dB}.
}
```

Equivalently, the maximum speed attainable from grading is bounded by the **available conduction-band/gap drop** across the absorber.

The grading resource cannot be increased indefinitely because the endpoint gaps must still satisfy

- desired optical cutoff / absorption;
- available HgCdTe composition range;
- no carrier-blocking band offset;
- acceptable lifetime and doping;
- positive-gap / desired band ordering.

---

## 14. New design implication

The graded absorber now has two linked requirements:

```text
large Delta E_c
-> faster minority collection
-> less recombination

but

large composition/gap excursion
-> changes where the incident photon is actually absorbed.
```

Therefore the next unavoidable tradeoff is not simply speed versus tunneling.

It is

> **bandgap-gradient transport versus the spatial absorption profile.**

For photons close to the low-gap cutoff, a large fraction of a strongly widened absorber may become optically inactive at that wavelength.

That is the next decisive attack.

---

## 15. Claim boundary

### DERIVED inside the stated constant-quasi-field drift/recombination model

```math
\boxed{
T_g
=\frac{qL_g^2}
{\mu_n\Delta E_c},
}
```

```math
\boxed{
\xi=T_g/\tau_n,
}
```

```math
\boxed{
\eta_{\rm col}
=(1-e^{-\xi})/\xi,
}
```

```math
\boxed{
H(\Omega,\xi)
=[1-e^{-(\xi+i\Omega)}]/(\xi+i\Omega),
}
```

and the normalized `Hhat` above.

For `xi -> 0`,

```math
\boxed{f_{3\rm dB}T_g=0.44294647.}
```

For `xi >> 1`,

```math
\boxed{f_{3\rm dB}\to1/(2\pi\tau_n)}
```

while `eta_col -> 0`.

Beer-Lambert generation response is also derived exactly.

### CHECKED

The half-power values and analytic transfer functions should be protected by a deterministic numerical regression.

### KNOWN / PRIOR

- drift/recombination transport;
- quasi-electric fields in compositionally graded semiconductors;
- graded HgCdTe minority-carrier transport;
- Beer-Lambert absorption.

### NON-CLAIM

This file does not establish

- a diffusion-free description of every HgCdTe absorber;
- a universal mobility or lifetime;
- a complete detector transfer function including depletion, RC, readout or Ramo weighting;
- a universal optimal grade;
- novelty of drift/recombination formulas.

---

## 16. Next decisive step

Attack the new bandgap-budget result with the optical requirement.

For a linear graded absorber, calculate

```text
local Eg(x)
-> local alpha[h nu, Eg(x)]
-> generation profile w(x)
-> collection transfer H(omega)
```

and ask:

> **How much bandgap drop can be spent on minority-carrier drive before near-cutoff absorptance/quantum efficiency degrades enough to erase the transport benefit?**

Start with a deliberately simple absorption-edge model before importing a detailed HgCdTe absorption coefficient.