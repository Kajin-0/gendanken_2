# Traveling-Wave Active Converter — Pump–Bandwidth Scaling from Phase Mismatch

**Date:** 2026-08-08  
**Status:** exact undepleted traveling-wave conversion baseline plus local-dispersion asymptotics; established nonlinear-optics ingredients; no novelty claim  

## 1. Purpose

The cavity result

```math
N_p\propto W^2
```

could have been an artifact of storing the signal and converted field in resonators.

This note attacks that possibility with a traveling-wave three-wave-mixing model.

The result is useful:

> A continuum/traveling-wave converter does not automatically eliminate the pump–bandwidth cost. At fixed nonlinear coefficient and finite phase-mismatch dispersion, shortening the interaction to broaden the acceptance requires a proportionally stronger pump.

For ordinary first-order phase mismatch, pump intensity again scales as `W^2`.

This is not claimed as a universal active-detector theorem.

---

## 2. Standard undepleted-pump equations

Let `A_s(z)` and `A_r(z)` be flux-normalized slowly varying amplitudes of the incident signal and converted receiving wave.

After replacing a strong pump by a classical undepleted amplitude, write

```math
\frac{dA_s}{dz}
=-iq A_r e^{-i\Delta k z},
```

```math
\frac{dA_r}{dz}
=-iq^* A_s e^{+i\Delta k z}.
```

Choose pump phase so

```math
q>0.
```

Here

- `q` has units of inverse length;
- `Delta k` is the phase mismatch;
- `L` is the nonlinear interaction length.

For a fixed device and mode normalization,

```math
q\propto |A_p|
```

and therefore

```math
q^2\propto \Phi_p
```

where `Phi_p` is an appropriate pump photon-flux / intensity resource.

The exact proportionality depends on `chi^(2)` or `chi^(3)`, effective mode area, normalization, etc., and is left explicit.

---

## 3. Exact conversion probability

With signal input only at `z=0`, the standard solution gives

```math
\boxed{
\eta(\Delta k)
=
\frac{q^2}
{q^2+(\Delta k/2)^2}
\sin^2\!\left[
L\sqrt{
q^2+(\Delta k/2)^2
}
\right].
}
```

This is established traveling-wave frequency-conversion theory.

At exact phase matching,

```math
\eta(0)=\sin^2(qL).
```

---

## 4. Unit on-center conversion

Perfect on-center conversion requires

```math
\boxed{
qL=\frac{\pi}{2}
}
```

for the shortest interaction branch.

Thus broadening the converter by shortening `L` requires

```math
\boxed{
q=\frac{\pi}{2L}.
}
```

This is the traveling-wave analogue of increasing the pump-enhanced coherent coupling in the cavity model.

---

## 5. Universal half-maximum mismatch constant

Impose the unit-conversion condition

```math
qL=\frac\pi2.
```

Define the dimensionless mismatch

```math
x\equiv\frac{\Delta k L}{2},
```

and

```math
a\equiv\frac\pi2.
```

Then

```math
\eta(x)
=
\frac{a^2}{a^2+x^2}
\sin^2\!\sqrt{a^2+x^2}.
```

The first positive solution of

```math
\eta(x_{1/2})=\frac12
```

is

```math
\boxed{
x_{1/2}\approx1.25457202234609.}
```

Therefore the conversion FWHM is controlled by the condition

```math
\boxed{
\frac{|\Delta k|L}{2}
=x_{1/2}
}
```

at the two half-maximum frequencies, provided the local phase-mismatch expansion is monotonic and symmetric enough for the stated approximation.

---

## 6. Local dispersion expansion

Let the signal detuning from the conversion center be

```math
\delta=\omega-\omega_0.
```

Suppose the first nonzero derivative of the phase mismatch occurs at order `m`:

```math
\boxed{
\Delta k(\delta)
\simeq
\frac{D_m}{m!}\delta^m.
}
```

Examples:

```text
m=1  ordinary group-velocity mismatch
m=2  first-order group-velocity matched; quadratic dispersion dominates
m=3  first two mismatch derivatives canceled, etc.
```

Let the angular-frequency FWHM be

```math
W.
```

For a locally symmetric line, the positive half-width is approximately

```math
\delta_{1/2}=W/2.
```

Then the half-maximum condition gives

```math
\frac{L}{2}
\frac{|D_m|}{m!}
\left(\frac{W}{2}\right)^m
=x_{1/2}.
```

Solving for interaction length,

```math
\boxed{
L
=
\frac{
2^{m+1}m!x_{1/2}
}{
|D_m|W^m
}.
}
```

---

## 7. Pump coupling required for bandwidth `W`

Use

```math
q=\frac\pi{2L}.
```

Substitution gives

```math
\boxed{
q
=
\frac{
\pi |D_m|
}{
2^{m+2}m!x_{1/2}
}
W^m.
}
```

Thus, because pump intensity/photon flux scales as `q^2`, the local-dispersion resource scaling is

```math
\boxed{
\Phi_p
\propto
W^{2m}.
}
```

This is the central result of the traveling-wave baseline.

---

## 8. Ordinary group-velocity mismatch

For

```math
m=1,
```

```math
\Delta k\simeq D_1\delta.
```

Then

```math
\boxed{
L
=
\frac{4x_{1/2}}
{|D_1|W},
}
```

and

```math
\boxed{
q
=
\frac{\pi|D_1|}{8x_{1/2}}W.
}
```

Therefore

```math
\boxed{
\Phi_p\propto W^2.
}
```

So the same quadratic pump-resource scaling found in the two-mode resonator appears in an ordinary traveling-wave converter, although for a completely different physical reason:

```text
cavity converter:
linewidth rates grow with W
-> coherent intermode coupling must grow with W

traveling-wave converter:
interaction length shrinks as 1/W
-> pump coupling per length must grow as W.
```

---

## 9. Group-velocity matching moves the bottleneck

If

```math
D_1=0
```

but

```math
D_2\ne0,
```

then

```math
m=2.
```

The accepted bandwidth now scales as

```math
W\propto L^{-1/2},
```

while unit conversion still requires

```math
q\propto L^{-1}.
```

Therefore

```math
\boxed{
q\propto W^2,
\qquad
\Phi_p\propto W^4.
}
```

This does **not** mean group-velocity matching is harmful in practical converters. It means that once the first-order mismatch is canceled, the asymptotic bandwidth dependence is controlled by the next nonzero dispersion coefficient.

At fixed target bandwidth, a small `D_2` can still be far better than a large `D_1`.

The point is conceptual:

> canceling one mismatch order moves the remaining scaling to the next physical dispersion resource rather than proving bandwidth is free.

---

## 10. General penalty migration

For the first nonzero mismatch derivative of order `m`,

```math
\boxed{
q\propto |D_m|W^m,
\qquad
\Phi_p\propto |D_m|^2W^{2m}.
}
```

Thus broadband active conversion is controlled jointly by

```text
pump strength
+
interaction length
+
phase-mismatch dispersion.
```

The pump requirement disappears from this local argument only if the phase mismatch remains essentially zero throughout the desired band without forcing `L` to shrink.

That idealization would itself require a special broadband dispersion/phase-matching resource.

---

## 11. Relation to existing frequency-conversion literature

Broadband quantum frequency conversion and waveform conversion are established fields.

Examples include

- Raman-memory conversion over very large absolute frequency ranges;
- engineered sum-frequency conversion for photon waveform reshaping;
- microresonator and waveguide frequency converters with high efficiency;
- group-velocity / quasi-phase-matching engineering.

Therefore the statement that traveling-wave converters can be broadband, and the exact coupled-wave solution above, are not novelty claims.

This note only uses that established physics to stress-test the detector pump-resource logic.

---

## 12. Crucial limitation: this is not a universal `W^2` theorem

The exponent depends on the phase-mismatch structure and the converter architecture.

The result does not cover

- chirped or apodized quasi-phase matching;
- adiabatic frequency conversion;
- pump pulses with time-dependent instantaneous frequency;
- spatially varying nonlinear coupling;
- multiple simultaneous pump tones;
- resonant slow-light enhancement;
- nonlocal/nonstationary conversion;
- direct time-switching / energy trapping;
- active matching without frequency conversion.

Such architectures may alter the scaling.

Therefore do not promote

```text
pump power must always scale as W^2
```

into a general claim.

---

## 13. What survives the continuum attack

The continuum model does support a more modest statement:

> **Broadband active conversion requires a trade among pump strength, interaction length, and phase-mismatch dispersion. A traveling-wave continuum does not make bandwidth free.**

This is a physical mechanism, not yet a fundamental bound.

Together with `MULTIMODE_ACTIVE_PUMP_RESOURCE.md`, it suggests that the correct general active resource may be an **integrated nonlinear coupling norm weighted by pump energy and dispersion**, rather than pump photons alone.

---

## 14. Claim boundary

### Derived within the stated traveling-wave model

At shortest-branch unit on-center conversion,

```math
qL=\pi/2.
```

The half-maximum mismatch constant is

```math
x_{1/2}\approx1.25457202234609.
```

If

```math
\Delta k\simeq D_m\delta^m/m!,
```

then

```math
\boxed{
q
=
\frac{\pi|D_m|}
{2^{m+2}m!x_{1/2}}
W^m
}
```

and hence

```math
\boxed{
\Phi_p\propto W^{2m}.
}
```

### Not established

- novelty of this scaling;
- a universal active-conversion exponent;
- a bound on `D_m`;
- a bound on the nonlinear coefficient;
- a universal pump-work / bandwidth theorem;
- optimality against chirped/adaptive/time-switched converters.

---

## 15. Next direction

The cavity and ordinary traveling-wave calculations both produce quadratic pump-resource scaling under their natural fixed-device assumptions, while multimode subdivision preserves it if the aggregate single-photon nonlinear coupling budget is fixed.

The remaining mathematical bottleneck is now explicit:

> **Can the active frequency-conversion interaction be written as an operator whose integrated coupling norm is bounded by pump energy and a finite nonlinear material resource, independent of how the device is divided into modes or space?**

A successful result of that type would be much closer to a genuine work–bandwidth resource theorem.

If no such bound exists because time-dependent control can arbitrarily reshape coupling at fixed work, the active branch may instead terminate with an explicit counterexample.