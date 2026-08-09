# Field-Driven Collection Versus Band-to-Band Tunneling — A Narrow-Gap Semiconductor Gedanke

**Date:** 2026-08-08  
**Status:** exact algebra within a fixed-thickness drift + Kane-type tunneling model; directly relevant to narrow-gap photodiodes; no novelty claim

## 1. Question

Suppose optical absorption has already been solved.

Can a semiconductor photodetector be made arbitrarily fast simply by increasing the carrier-collection electric field while its dark current remains fixed?

For a fixed collection thickness, ordinary drift says stronger field reduces transit time.

But in a narrow-gap semiconductor the same field also increases interband tunneling.

This note deliberately strips the problem to those two mechanisms.

---

## 2. Physical motivation from HgCdTe

Field-assisted dark current is established HgCdTe device physics.

Representative experimental/modeling literature finds regimes in which trap-assisted tunneling and direct band-to-band tunneling dominate HgCdTe photodiode dark current as reverse bias is increased, especially at low temperature and/or high field.

Examples include

- Y. K. Su et al., *Proc. SPIE* **3419**, 256-266 (1998), DOI `10.1117/12.311016`;
- F. S. Juang et al., *Journal of the Electrochemical Society* **146**, 1540-1545 (1999), DOI `10.1149/1.1391801`;
- J. Chen et al., *npj Quantum Materials* **6**, 103 (2021), DOI `10.1038/s41535-021-00409-3`.

The 2021 HgCdTe APD study explicitly shows that electric-field distributions strongly control band-to-band tunneling at high reverse bias and that device thickness/doping affect dark current, quantum efficiency, and response time.

This prior device physics is not a repository novelty.

---

## 3. Transit response of one collected carrier

Take a collection region of thickness

```math
L.
```

Assume a carrier crosses it at approximately constant drift velocity

```math
v_d.
```

The transit time is

```math
\boxed{
\tau_{\rm tr}
=\frac{L}{v_d}.
}
```

For the simplest Ramo-Shockley picture, one carrier produces an approximately rectangular induced-current pulse over `tau_tr`.

The normalized magnitude response is

```math
|H(f)|
=
\left|
\frac{\sin(\pi f\tau_{\rm tr})}
{\pi f\tau_{\rm tr}}
\right|.
```

The `-3 dB` condition

```math
|H|=1/\sqrt2
```

has

```math
\pi f_{3\rm dB}\tau_{\rm tr}
\simeq1.39156.
```

Therefore

```math
\boxed{
B_{\rm tr}
\equiv f_{3\rm dB}
=c_t\frac{v_d}{L},
\qquad
c_t\simeq0.44295.
}
```

This is a deliberately minimal single-carrier transit convention. Real diode impulse responses include both carrier types, nonuniform generation, field variation, diffusion, RC loading, multiplication, etc.

---

## 4. Low-field drift

In the linear drift regime,

```math
\boxed{
v_d=\mu F,}
```

where `mu` is mobility and `F` is electric field magnitude.

Then

```math
\boxed{
B_{\rm tr}
=c_t\frac{\mu F}{L}.
}
```

Equivalently, the minimum field needed to obtain a specified transit bandwidth is

```math
\boxed{
F
=\frac{L B_{\rm tr}}
{c_t\mu}.
}
```

Within this regime, increasing field really does increase speed linearly.

---

## 5. Minimal Kane-type direct band-to-band tunneling law

For a direct-gap semiconductor in a roughly uniform field, a Kane/Zener-type tunneling current has the characteristic form

```math
\boxed{
J_{\rm BTBT}
=A F^2
\exp\!\left(-\frac{F_K}{F}\right).
}
```

`A` and `F_K` contain band-structure, effective-mass, gap, and geometry factors.

For the present gedanken calculation their detailed prefactors are not needed; the load-bearing structure is

```text
power-law prefactor x exp(-constant/F).
```

HgCdTe device models use this same strong field dependence, with the tunneling exponent containing approximately the familiar

```math
m^{*1/2}E_g^{3/2}/F
```

combination.

Because HgCdTe can have a very small `E_g`, tunneling is particularly relevant.

---

## 6. Eliminate electric field

Substitute the drift field required for the desired transit bandwidth:

```math
F
=\frac{L B_{\rm tr}}
{c_t\mu}.
```

Then

```math
\boxed{
J_{\rm BTBT}(B_{\rm tr})
=
A
\left(
\frac{L B_{\rm tr}}
{c_t\mu}
\right)^2
\exp\!\left[
-
\frac{F_Kc_t\mu}
{L B_{\rm tr}}
\right].
}
```

At fixed `L`, `mu`, and material parameters, this is monotonic increasing in `B_tr`.

Indeed,

```math
\frac{d}{dB}
\ln J
=\frac2B
+
\frac{F_Kc_t\mu}
{LB^2}
>0.
```

Thus:

> **Within a fixed-thickness linear-drift narrow-gap diode, increasing collection bandwidth by increasing field necessarily increases the direct-tunneling dark-current component.**

This is a model tradeoff, not a universal detector theorem.

---

## 7. Dark-current-limited bandwidth in closed form

Suppose direct tunneling must satisfy

```math
J_{\rm BTBT}\le J_*.
```

First solve the Kane form for the maximum field.

Let

```math
y=F_K/F.
```

Then

```math
J_*
=A F_K^2
\frac{e^{-y}}{y^2}.
```

Hence

```math
\frac{y}{2}
e^{y/2}
=
\frac12
\sqrt{\frac{AF_K^2}{J_*}}.
```

Using the principal Lambert `W` function,

```math
\boxed{
F_{\max}
=
\frac{F_K}
{2W_0\!\left[
\frac12
\sqrt{AF_K^2/J_*}
\right]}.
}
```

Therefore, while linear drift remains valid,

```math
\boxed{
B_{\rm tr,max}^{(J)}
=
\frac{c_t\mu F_K}
{2L\,
W_0\!\left[
\frac12
\sqrt{AF_K^2/J_*}
\right]}.
}
```

This is merely an algebraic inversion of the stated models; no novelty is claimed.

---

## 8. Velocity saturation makes excess field strictly harmful to transit speed

Real drift velocity does not remain

```math
v_d=\mu F
```

indefinitely.

Let

```math
v_d\le v_{\rm sat}.
```

Then the collection transit bandwidth obeys the absolute fixed-thickness kinematic ceiling

```math
\boxed{
B_{\rm tr}
\le
c_t\frac{v_{\rm sat}}{L}.
}
```

Once the carrier velocity is near saturation, additional electric field produces little or no transit-speed benefit.

But the tunneling current remains strongly field dependent.

Therefore beyond the velocity-saturation region,

```text
more field
-> much more tunneling leakage
-> essentially no transit-bandwidth benefit.
```

This is a particularly clean engineering consequence of the gedanken model.

---

## 9. Important counterexample: shrink the collection thickness

The fixed-thickness tradeoff is not fundamental.

From

```math
B_{\rm tr}
=c_t\frac{\mu F}{L},
```

one can increase speed by reducing `L` rather than increasing `F`.

For a fixed target `B_tr`, the required field becomes

```math
F
=\frac{LB_{\rm tr}}
{c_t\mu},
```

which **decreases** as `L` is reduced.

Thus within this stripped-down model,

```text
L down
-> faster transit
-> lower field needed for a fixed speed
-> less field-induced BTBT.
```

That is a direct counterexample to any universal statement of the form

```text
more detector speed necessarily means more tunneling dark current.
```

The theorem requires `L` to be fixed.

---

## 10. Why this reconnects to the original vanishing-absorber experiment

Ordinary planar absorption would object that reducing `L` also reduces optical absorption.

But the very first branch of this repository already showed that arbitrary field concentration / resonant optical structures prevent **geometric active thickness alone** from being a fundamental optical resource.

So optical photon trapping can, at least in idealized models, partially decouple

```text
optical path length
```

from

```text
carrier transit thickness.
```

This is not hypothetical: photon-trapping-enhanced infrared APDs experimentally exploit ultrathin absorbing regions to reduce dark current and improve carrier transit while retaining optical absorption.

Therefore the field-tunneling model does not close the original thought experiment by itself.

It moves the question to what happens when `L` becomes electronically microscopic.

---

## 11. Next possible penalty at small `L`

As `L` is reduced far enough, continuum drift transport must eventually give way to other physics:

- direct contact-to-contact tunneling;
- wavefunction overlap across the collection region;
- quantum confinement / altered band structure;
- ballistic rather than drift transport;
- interface and surface generation becoming non-negligible;
- finite contact and depletion widths;
- breakdown of a local electric-field transport description.

Thus the natural next question is

> **Can an optically trapped photodetector make the electronic collection distance arbitrarily small without opening a field-independent quantum-leakage path between its contacts/reservoirs?**

That is a cleaner continuation of the original vanishing-absorber gedanken experiment than simply increasing reverse bias indefinitely.

---

## 12. Claim boundary

### Derived within the fixed-thickness low-field model

```math
\boxed{
J_{\rm BTBT}(B_{\rm tr})
=
A
\left(
\frac{LB_{\rm tr}}
{c_t\mu}
\right)^2
\exp\!\left[-
\frac{F_Kc_t\mu}
{LB_{\rm tr}}
\right].
}
```

### Established qualitative HgCdTe physics

- reverse bias can drive TAT and BTBT dark-current mechanisms;
- narrow bandgap makes tunneling especially important;
- electric-field engineering, doping, and multiplication-region thickness materially affect dark current and speed in HgCdTe APDs.

### Invalidated as a general claim

```text
faster collection always requires higher field and therefore more BTBT
```

is false if collection thickness is also allowed to shrink.

### Not established

- a universal HgCdTe speed-dark-current theorem;
- a lower bound on collection thickness;
- a complete dark-current model;
- the relation between this simple transit response and all measured detector bandwidths;
- novelty of the composed formula.

---

## 13. Next decisive question

Do not optimize detailed HgCdTe doping profiles yet.

The next gedanken experiment should attack the small-`L` escape:

> **Let optical absorption remain high by ideal photon trapping. Send the carrier collection distance `L -> 0`. Does direct quantum transport between the electronic reservoirs then create an unavoidable leakage floor before the transit time can vanish?**

Use the smallest finite-barrier quantum-transport model first.

If that also admits an escape, record it and follow the logic.