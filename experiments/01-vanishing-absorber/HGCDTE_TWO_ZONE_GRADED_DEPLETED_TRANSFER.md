# HgCdTe Two-Zone Graded Absorber + Depleted Collector — Exact Transfer Factorization and Timing Budget

**Date:** 2026-08-09  
**Status:** exact linear transfer composition in a minimal two-zone detector model; Shockley–Ramo and drift/recombination ingredients are standard prior physics; no novelty claim

## 1. Purpose

The graded-neutral-absorber branch established two things:

1. a quasi-neutral p-type composition grade can drive minority electrons while approaching a band geometry that suppresses the ordinary direct-Zener path;
2. the same grade couples the spatial optical-generation profile to minority-carrier delay and recombination.

A real photodiode still needs a collecting junction / depleted region.

This note builds the smallest architecture that contains both pieces:

```text
incident light
   |
   v
quasi-neutral graded absorber / transport region
   |
   v
depleted collector
   |
   v
external terminal current.
```

The aim is not to model an APD. It is to identify exactly how the two regions combine in time.

---

## 2. Region G — quasi-neutral graded absorber

Let the graded neutral region occupy

```math
0\le x\le L_g
```

and deliver minority electrons to the depleted interface at `x=L_g`.

Let the external collected-flux transfer from incident photons to **arrival at the depletion boundary** be

```math
\boxed{H_g(\omega).}
```

This may be any of the kernels already derived in the repository.

For the most general local optical law in a linear grade,

```math
H_g(\omega;r)
=
\frac{L_gr}{\varepsilon}
\int_{\delta_f}^{\varepsilon}
\alpha(\delta)
 e^{-\mathcal T(\delta;r)}
 e^{-(1/\tau_n+i\omega)t_g(\delta;r)}
 d\delta.
```

At DC,

```math
\boxed{\eta_g=H_g(0)}
```

is the fraction of incident photons that generate a minority electron which survives to the depleted interface.

Define the normalized neutral-region timing response

```math
\boxed{
\widehat H_g(\omega)
=H_g(\omega)/H_g(0).
}
```

Then

```math
\widehat H_g(0)=1.
```

---

## 3. Region D — depleted collector

Let the depleted collector have width

```math
\boxed{W_d}
```

and, in the first model, a constant electron drift velocity

```math
\boxed{v_d.}
```

The transit time is

```math
\boxed{
T_d=\frac{W_d}{v_d}.
}
```

Assume

- no carrier loss in the depleted region;
- no avalanche multiplication;
- uniform weighting field over the depleted region;
- the neutral region contributes negligibly to terminal current before the electron enters the depletion region.

These assumptions are intentionally restrictive so that the collector response is exact and transparent.

---

## 4. Shockley–Ramo current pulse

An electron entering the depletion region at time `t_0` produces, under constant velocity and uniform weighting field, the rectangular induced-current pulse

```math
\boxed{
i_d(t|t_0)
=
\frac{q}{T_d}
\Theta(t-t_0)
\Theta(t_0+T_d-t).
}
```

Its time integral is exactly one elementary charge:

```math
\int i_d dt=q.
```

Normalize its Fourier response to collected charge `q`.

Then

```math
R_d(\omega)
=
\frac1{T_d}
\int_0^{T_d}
e^{-i\omega t}dt.
```

Therefore

```math
\boxed{
R_d(\omega)
=
\frac{1-e^{-i\omega T_d}}
{i\omega T_d}
}
```

or equivalently

```math
\boxed{
R_d(\omega)
=
e^{-i\omega T_d/2}
\operatorname{sinc}\!\left(
\frac{\omega T_d}{2}
\right),
}
```

where

```math
\operatorname{sinc}z=\frac{\sin z}{z}.
```

At DC,

```math
R_d(0)=1.
```

---

## 5. Exact two-zone factorization

The depleted collector is time invariant in this model.

An electron arriving from the neutral region simply launches the same Ramo pulse shifted by its arrival time.

Therefore the external terminal-current transfer is the convolution of

```text
neutral arrival-time response
```

with

```text
depletion-region Ramo pulse.
```

In frequency space,

```math
\boxed{
H_{\rm det}(\omega)
=H_g(\omega)R_d(\omega).
}
```

At zero frequency,

```math
\boxed{
H_{\rm det}(0)=H_g(0)=\eta_g.
}
```

Thus, in the lossless-depletion baseline, the depleted collector changes the **timing response** but not the DC external collected QE.

The normalized detector response is

```math
\boxed{
\widehat H_{\rm det}(\omega)
=
\widehat H_g(\omega)
R_d(\omega).
}
```

This is the central two-zone result.

---

## 6. Immediate bandwidth consequence

Because the normalized neutral arrival kernel is a passive positive-delay distribution,

```math
|\widehat H_g(\omega)|\le1.
```

Likewise

```math
|R_d(\omega)|\le1.
```

Therefore the full response cannot remain above half power beyond the half-power point of either factor.

If `f_{3dB,g}` is the neutral-region first half-power frequency, and the depleted rectangular-pulse response has

```math
\boxed{
f_{3dB,d}
=\frac{0.44294647}{T_d}
=0.44294647\frac{v_d}{W_d},
}
```

then

```math
\boxed{
f_{3dB,det}
\le
\min(
f_{3dB,g},
f_{3dB,d}
).
}
```

This inequality is exact under the stated factorized model.

The total bandwidth is generally **strictly smaller** when both regions have comparable delay spread.

---

## 7. Timing-distribution interpretation

Normalize the neutral arrival impulse response to unit DC area and interpret it as a probability density of neutral-region arrival delay:

```math
\boxed{p_g(t).}
```

The depleted rectangular Ramo pulse corresponds to a uniform timing kernel

```math
\boxed{
p_d(t)
=\frac1{T_d},
\qquad
0<t<T_d.
}
```

The full normalized timing kernel is the convolution

```math
\boxed{
p_{\rm det}
=p_g*p_d.
}
```

Therefore the timing random variable may be written

```math
\boxed{t_{\rm det}=t_g+u_d,}
```

where

```math
u_d\sim\operatorname{Uniform}(0,T_d)
```

and is independent of the neutral arrival delay in this baseline.

---

## 8. Exact mean delay

The uniform Ramo contribution has mean

```math
\boxed{
\langle u_d\rangle=T_d/2.
}
```

Hence

```math
\boxed{
\langle t_{\rm det}\rangle
=
\langle t_g\rangle
+\frac{T_d}{2}.
}
```

The depletion region therefore adds half its transit time to the centroid of the terminal-current impulse response.

---

## 9. Exact timing-variance addition

The uniform Ramo kernel has variance

```math
\boxed{
\operatorname{Var}(u_d)
=\frac{T_d^2}{12}.
}
```

Independent convolution adds variances exactly:

```math
\boxed{
\sigma_{t,\rm det}^2
=
\sigma_{t,g}^2
+
\frac{T_d^2}{12}.
}
```

This is a stronger and more interpretable statement than simply saying that one region has the smaller bandwidth.

It says:

> **Every timing-spread contribution that grading removes from the neutral absorber leaves an irreducible depleted-collector contribution `T_d^2/12` in this baseline.**

The penalty has migrated again.

---

## 10. Low-frequency transfer expansion

For any normalized delay distribution with finite variance,

```math
\widehat H(\omega)
=
1-i\omega\langle t\rangle
-\frac{\omega^2}{2}\langle t^2\rangle
+O(\omega^3).
```

Therefore

```math
\boxed{
|\widehat H(\omega)|^2
=
1-\omega^2\sigma_t^2
+O(\omega^4).
}
```

For the two-zone detector,

```math
\boxed{
|\widehat H_{\rm det}|^2
=
1-
\omega^2
\left(
\sigma_{t,g}^2+
\frac{T_d^2}{12}
\right)
+O(\omega^4).
}
```

Thus the timing-variance budget is also the exact leading low-frequency magnitude-rolloff budget.

---

## 11. Special case — uniform neutral generation, negligible recombination

If the neutral graded region has constant velocity and carriers are generated uniformly throughout a fully active length, then the neutral arrival-delay distribution is itself uniform over

```math
0<t<T_g.
```

Therefore

```math
\boxed{
\widehat H_g
=
e^{-i\omega T_g/2}
\operatorname{sinc}(\omega T_g/2).
}
```

The total response is

```math
\boxed{
\widehat H_{\rm det}
=
e^{-i\omega(T_g+T_d)/2}
\operatorname{sinc}(\omega T_g/2)
\operatorname{sinc}(\omega T_d/2).
}
```

and

```math
\boxed{
\sigma_t^2
=
\frac{T_g^2+T_d^2}{12}.
}
```

This makes the two transit contributions completely symmetric at the timing-variance level.

---

## 12. Graded near-cutoff absorber changes only the first factor

For the general graded absorption kernel already derived,

```math
H_g(\omega;r)
```

contains

- spatial optical generation;
- minority-carrier drift delay;
- recombination survival.

The depleted collector simply multiplies it by `R_d`.

Therefore all previous graded-absorber results remain modular.

For example, an optimum transparent-front / absorbing-rear grade may dramatically reduce

```math
\sigma_{t,g}
```

without changing the depleted collector term.

This gives a clean design objective:

```text
first
-> minimize neutral-region delay/recombination with grading

then
-> make the depletion collector sufficiently fast that it does not erase that benefit.
```

---

## 13. Kinematic depletion floor

If the depleted region has an allowed maximum steady drift velocity

```math
v_{d,\max},
```

then

```math
\boxed{
T_d
\ge
\frac{W_d}{v_{d,\max}}.
}
```

Hence

```math
\boxed{
\sigma_{t,d}^2
\ge
\frac{W_d^2}
{12v_{d,\max}^2}.
}
```

and

```math
\boxed{
f_{3dB,d}
\le
0.44294647
\frac{v_{d,\max}}{W_d}.
}
```

This is only as meaningful as the specified velocity envelope.

Do not use transient velocity overshoot as a universal steady-state `v_max`.

---

## 14. Where the dark-current problem has moved

The quasi-neutral graded absorber can, in principle, keep much of the **electrostatic high field** out of the narrow-gap optical region.

But the depleted collector still requires an electrostatic field.

Therefore the high-field leakage problem becomes spatially localized:

```text
neutral graded absorber
-> optical absorption
-> quasi-field collection
-> low direct-Zener common-mode tilt in ideal pinning limit

thin depleted collector
-> electrostatic field
-> Ramo response
-> TAT / BTBT / nonlocal II burden.
```

This is a much more device-like architecture than a uniformly high-field narrow-gap absorber.

The next question is not whether field is eliminated.

It is:

> **How thin / wide-gap can the depleted collector be made while still accepting carriers from the graded absorber without a blocking band offset?**

---

## 15. Simple two-zone response optimization statement

The full detector speed problem in this baseline can now be written as

```math
\boxed{
\max
\ f_{3dB,\rm det}
}
```

subject to

```text
neutral-zone external QE >= eta_*
neutral-zone available bandgap grade
collector width W_d
collector velocity law v_d(F_d)
collector TAT / BTBT / II budgets
band-offset transfer condition
applied bias / Poisson electrostatics.
```

The exact transfer factorization avoids hiding any of these constraints inside a fitted single time constant.

---

## 16. Important caveats

The factorized result assumes

- negligible terminal weighting field in the neutral region;
- no diffusion contribution;
- no carrier loss in depletion;
- no velocity variation across depletion;
- no avalanche multiplication;
- no hole-current contribution;
- no RC/readout filtering;
- no feedback of photocarrier space charge on field.

In a real diode, Ramo weighting extends through the electrostatic geometry and both carrier species can contribute.

The present model is a clean baseline, not a complete detector impulse response.

---

## 17. Claim boundary

### DERIVED / CHECKED inside the stated two-zone linear model

```math
\boxed{
H_{\rm det}(\omega)
=H_g(\omega)R_d(\omega),
}
```

```math
\boxed{
R_d
=e^{-i\omega T_d/2}
\operatorname{sinc}(\omega T_d/2),
}
```

```math
\boxed{
\langle t_{\rm det}\rangle
=\langle t_g\rangle+T_d/2,
}
```

```math
\boxed{
\sigma_{t,\rm det}^2
=\sigma_{t,g}^2+T_d^2/12,
}
```

and

```math
\boxed{
f_{3dB,\rm det}
\le
\min(f_{3dB,g},0.44294647/T_d).
}
```

### KNOWN / PRIOR

- Shockley–Ramo induced current;
- rectangular constant-velocity transit response;
- convolution / timing-variance addition;
- graded neutral minority-carrier transport.

### NON-CLAIM

This file does not establish

- a universal two-zone HgCdTe bandwidth;
- that the neutral region has zero weighting field;
- a full APD response;
- a complete dark-current model;
- novelty of the factorization.

---

## 18. Next decisive attack

The two-zone timing problem is now explicit.

The next physical question is the **interface / collector design**:

> **Can a wider-gap depleted collector accept minority electrons from the low-gap graded absorber without a conduction-band barrier while keeping enough of the applied field out of the absorber to suppress TAT/BTBT?**

Build the smallest band-offset model next:

1. low-gap absorber endpoint;
2. wider-gap collector gap;
3. conduction-band offset fraction;
4. electrostatic drop across collector;
5. carrier transfer condition over/through the offset;
6. direct WKB/TAT burden in the depleted collector.

Only then should Poisson be added in full.