# Minimal Two-Depth, Two-Frequency Transport Gedanken Experiment

**Date:** 2026-08-10  
**Status:** exact in a uniform 1-D conditioned drift-diffusion segment; designed as the simplest conceptual entry point to the broader theory; no novelty claim

## 1. The thought experiment

Forget HgCdTe for a moment.

Consider a one-dimensional material with a collector to the right.

You can create otherwise identical carriers at two known positions

```text
z1
z2 = z1 + Delta z
```

inside one uniform transport segment.

At one RF angular frequency `omega`, measure the complex collected response for carriers born at each point and form the ratio

```math
\boxed{
R_\omega
=\frac{F(z_2,\omega)}{F(z_1,\omega)}.
}
```

Any source amplitude, common optical phase, and common electronics transfer cancel in the ratio.

Define the complex spatial propagation constant

```math
\boxed{
\gamma_\omega
=\frac{\ln R_\omega}{\Delta z},
}
```

with the phase branch unwrapped continuously.

That is the entire first gedanken experiment.

---

## 2. Exact prediction of uniform local drift-diffusion

For real conditioned drift `w>0` toward the collector and diffusion coefficient `D>0`,

```math
D F''+wF'-i\omega F=0.
```

The physical root is

```math
\boxed{
\gamma_\omega
=
\frac{
\sqrt{w^2+4iD\omega}-w
}{2D}.
}
```

Write

```math
\gamma=a+ib.
```

Then one single complex measurement gives

```math
\boxed{
D
=
\frac{\omega a}
{b(a^2+b^2)},
}
```

and

```math
\boxed{
w
=
\frac{\omega(b^2-a^2)}
{b(a^2+b^2)}.
}
```

No transient waveform fit is required.

No numerical drift-diffusion solution is required.

The inverse is algebraic.

---

## 3. One-frequency sign cone

For

```text
D>0
w>0
omega>0
```

the exact inverse immediately requires

```math
\boxed{
a>0,}
```

```math
\boxed{
b>0,}
```

and

```math
\boxed{
b^2>a^2.}
```

Therefore

```math
\boxed{
0<\Re\gamma<\Im\gamma.
}
```

This is a parameter-free one-frequency prediction.

Interpretation:

```text
Re gamma -> spatial attenuation of the RF response
Im gamma -> spatial phase accumulation.
```

In an ideal downstream positive-drift local drift-diffusion segment, attenuation per unit depth cannot exceed phase accumulation per unit depth.

Violation of this cone falsifies that simple model immediately.

It does not by itself identify the replacement mechanism.

---

## 4. The second frequency is a pure model test

Now repeat the same two-depth ratio at a second RF frequency.

The first frequency already supplied both unknown local transport coefficients:

```text
D
w.
```

Therefore the second frequency introduces **zero new local transport parameters**.

It must give

```math
\boxed{
D(\omega_2)=D(\omega_1),
}
```

and

```math
\boxed{
w(\omega_2)=w(\omega_1).
}
```

Thus the minimal model-falsification experiment is simply

```text
2 generation depths
x
2 RF frequencies.
```

One frequency identifies.

The second frequency falsifies or confirms closure.

This is the simplest form of the full multi-frequency theorem.

---

## 5. Why DC-normalized RF measures conditioned carriers

Suppose carriers may recombine locally before reaching the collector.

Let

```math
h(z)
```

be the probability that a carrier born at `z` is eventually collected.

The experimentally natural normalized RF transfer is

```math
F(z,\omega)
=\frac{U(z,i\omega)}{h(z)}.
```

The conditioning theorem shows that `F` obeys drift-diffusion with conditioned drift

```math
\boxed{
w
=v+2D\partial_z\ln h,
}
```

not necessarily the unconditioned physical drift `v`.

So RF timing of collected carriers alone does not generally separate drift from recombination.

---

## 6. Add one DC depth measurement

In the simplest uniform semi-infinite / single-exponential collection geometry,

```math
h(z)\propto e^{cz},
```

with

```math
c=\partial_z\ln h.
```

For local killing rate

```math
\kappa=1/\tau,
```

the conditioned drift is

```math
\boxed{
w=\sqrt{v^2+4D\kappa}.
}
```

and

```math
\boxed{
c=\frac{w-v}{2D}.
}
```

Hence once RF has supplied `D,w`, the DC collection slope gives

```math
\boxed{
v=w-2Dc,
}
```

and

```math
\boxed{
\kappa=Dc^2+vc.
}
```

Therefore

```math
\boxed{
\tau=1/\kappa.
}
```

The minimal complete ideal experiment becomes

```text
2 depths
+
DC collection ratio
+
2 RF frequencies.
```

The information roles are unusually clean:

```text
RF frequency 1 -> identify D and conditioned drift
RF frequency 2 -> falsify the local Markov model
DC depth dependence -> undo conditioning and recover physical drift + recombination.
```

---

## 7. Illustrative detector-scale numbers

The numerical regression uses only an example scale

```text
D = 0.20 m^2/s
v = 1.00e5 m/s
tau = 1 us
Delta z = 1 um
f = 0.5 and 2 GHz.
```

The corresponding conditioned drift is approximately

```text
100004 m/s.
```

For the `1 um` depth separation, the model predicts approximately

```text
0.5 GHz:
phase difference ~1.79 deg

2.0 GHz:
phase difference ~6.55 deg.
```

Both RF frequencies independently recover the same `D,w` to numerical precision, and the DC slope returns the original `v,tau`.

These values are **illustrative**, not HgCdTe device predictions.

---

## 8. Why this is a better opening gedanken experiment

The original project repeatedly became complicated because it started by asking for a whole internal transport profile.

This experiment asks something much smaller:

> **If I move the birth position of an otherwise identical carrier by a known distance, how must its complex response change if transport is ordinary local drift-diffusion?**

The answer is exact.

And more importantly, it is easy to falsify.

There is no need initially to reconstruct

```text
an arbitrary velocity profile
a microscopic scattering distribution
a full detector simulation
or a detailed material band structure.
```

The hierarchy can then be built naturally:

```text
uniform two-depth theorem
-> multi-frequency closure
-> DC unconditioning
-> arbitrary spatially varying exact closure
-> wavelength as passive internal depth selector
-> translated-feature local witness
-> real HgCdTe worked example.
```

---

## 9. Spectral detector realization

A graded absorber provides a natural way to approximate the otherwise hypothetical movable generation point.

Changing wavelength shifts the internal generation distribution.

The finite-width theorem already shows an important robustness result:

> if the generation distribution translates without changing shape, its finite width factors out of the uniform logarithmic transport slope exactly.

Thus the point-source gedanken experiment is not merely an unattainable idealization.

A calibrated wavelength-dependent generation kernel can approximate the same information without physically scanning a laser spot through the material.

Shape evolution with wavelength becomes a calculable correction rather than an automatic resolution failure.

---

## 10. Falsification outcomes

### Outcome A

```text
D_app and w_app are constant across RF frequency.
```

Then local Markov drift-diffusion survives this test over the measured band.

### Outcome B

```text
D_app or w_app disperses with frequency.
```

Then no one real frequency-independent local second-order drift-diffusion generator explains the conditioned response.

This points toward

```text
trapping/memory
finite relaxation
spatially nonlocal transport
multiple populations
or another missing state.
```

### Outcome C

The one-frequency sign cone itself fails.

Then the simple positive downstream local drift-diffusion description is already inconsistent before any multi-frequency analysis.

---

## 11. Paper-level role

This should be the conceptual opening of any eventual manuscript because it contains the central idea with almost no machinery:

> **One RF frequency identifies two transport coefficients from a complex spatial response. The second RF frequency has nowhere to hide: it becomes an exact test of the transport law itself.**

The later wavelength/HgCdTe construction then answers only one practical question:

> how can a detector provide those internal generation coordinates without cutting into the device?

Numerical regression:

`numerics/minimal_two_depth_two_frequency_gedanken.py`
