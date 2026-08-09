# Research Log — Experiment 01: The Vanishing Absorber

This file is chronological. It records why the research direction changed, not just the final equations.

---

## 2026-08-08 — Experiment opened

### Starting motivation

Use a simple photodetector thought experiment to probe whether familiar engineering tradeoffs hide a more general physical constraint.

The guiding question was chosen because it is easy to state without committing to a particular detector material or architecture:

> Can an ideal photodetector be made arbitrarily small, arbitrarily fast, arbitrarily sensitive, and still absorb essentially every incident photon?

### Initial physical tension

Shrinking the active semiconductor volume appears to help at least two desirable directions in an idealized detector:

- bulk thermally generated event count decreases with active volume for fixed generation-rate density;
- carrier transit distances can decrease.

But ordinary optical absorption also falls as absorbing material is removed.

The thought experiment therefore grants ideal passive optical confinement and asks where any unavoidable cost reappears.

### First candidate mechanism

A one-port critically coupled resonance suggests that weak absorber loss can be compensated by weak external leakage, preserving unity on-resonance absorption while increasing photon dwell time.

This raises the possibility that a thickness/volume penalty can migrate from absorption efficiency into temporal bandwidth.

### Important restraint

No general theorem was accepted from this intuition.

In particular, the provisional relation

```text
eta^2 B <= C V
```

was explicitly demoted from an apparent target formula to an unproved example of what a later bound might resemble.

### Current decision

Do not begin with general electromagnetic bounds or HgCdTe-specific physics.

First derive the complete one-port resonator response from the dynamical equation and determine exactly which bandwidth and lifetime relations are true.

Only then attempt to generalize or find counterexamples.

---

## 2026-08-08 — One-port resonator derived

### The intuition survives, but in a more precise form

Using one temporal coupled-mode normalization throughout gives

```math
A(\omega)=
\frac{4\gamma_e\gamma_a}
{(\omega-\omega_0)^2+(\gamma_e+\gamma_a)^2}.
```

At critical coupling,

```math
\gamma_e=\gamma_a,
```

so unity monochromatic absorption is possible even for arbitrarily small `gamma_a` in the ideal model.

However, the absorbed-power response to small modulation is

```math
H_{\rm abs}(\Omega)
=
\frac{\Gamma}{\Gamma+i\Omega},
\qquad
\Gamma=\gamma_e+\gamma_a.
```

Therefore

```math
B_{3\rm dB}
=
\frac{\Gamma}{2\pi}.
```

At critical coupling,

```math
B_{3\rm dB}^{\rm crit}
=
\frac{\gamma_a}{\pi}.
```

So the original cavity intuition is correct **in terms of absorber loss rate**: weaker absorptive decay forces a narrower absorbed-power modulation response when unity absorption is maintained by critical coupling.

### Important distinction discovered

The optical absorption linewidth is not the same numerical bandwidth as the absorbed-power modulation response.

At critical coupling,

```math
\Delta f_{\rm abs,FWHM}
=2B_{3\rm dB}^{\rm crit}.
```

This factor of two would have been easy to miss if the optical spectrum had simply been called the detector bandwidth.

### Unexpected optimization result

The next step combined the one-port optical result with the minimal Poisson bulk-dark-event model.

Define

```math
\mathcal C
=
\frac{h\nu\sqrt{B_{3\rm dB}}}
{\mathrm{NEP}}.
```

This quantity is dimensionless.

Writing

```math
x=\frac{\gamma_e}{\gamma_a}
```

gives

```math
\mathcal C^2
=
\frac{4\gamma_a}{\pi D}
\frac{x^2}{(1+x)^3}.
```

The optimum is not critical coupling.

Instead,

```math
\boxed{x=2,}
```

which gives

```math
A_0=\frac89,
\qquad
B_{3\rm dB}=\frac{3\gamma_a}{2\pi}.
```

The resulting `C` is about `8.9%` larger than at exact critical coupling.

This was not a target result. It emerged naturally from asking what happens when speed and dark-noise-limited sensitivity are optimized together rather than demanding exactly 100% absorption.

### First exact volume cancellation — but conditional

If

```math
\gamma_a=\kappa V
```

and the bulk dark-event rate is

```math
D=g_dV,
```

then

```math
\mathcal C_{\max}^2
=
\frac{16\kappa}{27\pi g_d}.
```

The active volume cancels.

This is the first exact appearance of the motivating sensitivity-speed cancellation, but it is not yet a fundamental bound because `gamma_a proportional to V` is only valid in a regular weak-participation limit.

### Numerical check

Direct time-domain integration reproduced the analytic modulation response at representative normalized frequencies.

At

```text
Omega/Gamma = 0.5, 1, 2
```

the numerical response amplitudes were approximately

```text
0.89449, 0.70746, 0.44757
```

compared with

```text
0.89443, 0.70711, 0.44721
```

from the analytic first-order transfer function.

A numerical coupling scan independently placed the optimum near

```text
gamma_e/gamma_a = 2.00003.
```

### Convention errors caught before state promotion

The first draft of the detailed derivation contained two redundant convention mistakes:

1. a mismatch between the `exp(-i omega t)` harmonic convention and the sign of the resonant-frequency term in the amplitude equation;
2. an incorrect rewrite of the already-correct `B_3dB = Gamma/(2 pi)` result in terms of loaded `Q`.

They were corrected before `CURRENT_STATE.md` was advanced.

The correct relation is

```math
B_{3\rm dB}=\frac{f_0}{2Q_L}.
```

The main decay-rate result and the `gamma_e/gamma_a = 2` optimization were unaffected.

### Direction change

The cavity question is now sufficiently answered for this stage.

The bottleneck moved to whether active material volume itself constrains `gamma_a`.

---

## 2026-08-08 — Active-volume-only bound falsified in the continuum model

### Counterexample search succeeded

The next branch deliberately tried to defeat the assumption

```math
\gamma_a\propto V_a.
```

An explicit family of ideal dielectric capacitors does so.

Take a parallel-plate capacitor filled by the active dielectric and scale

```math
d=s d_0,
\qquad
A=s A_0,
\qquad
s\to0.
```

Then

```math
C=\frac{\epsilon_0\epsilon' A}{d}=C_0
```

stays fixed while

```math
V_a=Ad\propto s^2\to0.
```

For fixed resonant modal energy, the capacitor voltage remains fixed and therefore

```math
|E|^2\propto d^{-2}\propto s^{-2}.
```

Hence

```math
|E|^2V_a=\text{constant}.
```

For fixed dielectric loss tangent and finite electric-energy participation,

```math
\gamma_a
=
\frac{\omega}{2}p_a\tan\delta
```

stays finite while `V_a -> 0`.

Thus

```math
\boxed{\gamma_a/V_a\to\infty.}
```

The detailed derivation is in `ACTIVE_VOLUME_COUNTEREXAMPLE.md`.

### What failed

The conjecture that passivity alone should keep `gamma_a/V_a` bounded is false under ideal local linear continuum electrodynamics when arbitrary lossless field concentration is allowed.

The earlier conditional volume cancellation remains algebraically correct only in scaling families where `gamma_a proportional to V_a` actually holds.

The provisional active-volume-only law

```text
eta^2 B <= C V_a
```

is therefore no longer an active target.

### Why established material bounds do not contradict the counterexample

Primary electromagnetic-limit work such as Miller et al. bounds absorption for a specified material susceptibility and specified background excitation. If a separate field concentrator is allowed to reshape the background field, then the local field at the shrinking active material can itself increase as volume falls.

Thus a per-volume material-response bound is not automatically an active-volume-only detector bound.

The resource accounting must include the electromagnetic environment or a more microscopic material quantity.

### Toy detector consequence exposes the model breakdown

If the old continuum dark-event law

```math
D=g_dV_a
```

is retained simultaneously with the fixed-`gamma_a` capacitor family, then

```math
\mathcal C_{\max}\propto V_a^{-1/2}.
```

The resulting divergence is not interpreted as infinite physical detector performance. It is a diagnostic that the continuum electromagnetic model and the extensive dark-event model cannot both be extrapolated to arbitrarily small active volume.

### Microscopic physics becomes unavoidable

For fixed modal energy the field grows as the gap shrinks. For a one-photon excitation, the available energy scale is fixed by `hbar omega`, so the single-photon field also grows rather than being rescaled away.

Eventually the following continuum assumptions fail:

- linear material response;
- local bulk susceptibility;
- thermodynamic extensivity of dark events;
- an arbitrarily large number of microscopic absorbers inside `V_a`;
- ideal lossless field concentration.

### Important prior-art collision

Young, Sarovar & Léonard, *Physical Review A* 97, 033836 (2018), developed a fully quantum single-photon detector model in which rapid incoherent transfer to an optically dark monitored state can, under their ideal assumptions, simultaneously approach unit efficiency, negligible dark counts, and minimal jitter.

That result is important because it warns against assuming that quantum mechanics alone supplies a universal efficiency-dark-count-speed tradeoff. Architecture and thermodynamic resource accounting matter.

It does not solve the active-volume problem studied here.

### Direction change

The active question is now microscopic rather than geometric:

> What physical resource cannot be concentrated away when the active material approaches a finite number of absorbers?

Candidate resources include oscillator number, total oscillator strength, transition dipole moment, single-photon saturation, nonlocal/atomic length scales, and thermodynamic free-energy/reset resources.

The next calculation should use a finite microscopic absorber model and should separately test the restricted passive-equilibrium case, where detailed balance has a chance to produce a real bound.
