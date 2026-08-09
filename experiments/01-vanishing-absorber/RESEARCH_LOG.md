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

The bottleneck has moved.

The active question is no longer simply whether a weak critically coupled absorber becomes slow. It does in this model.

The next question is:

> Can passive electromagnetic design make `gamma_a/V` diverge as active volume tends to zero while preserving a physical input channel and material model?

That question attacks the assumption on which the apparent volume cancellation rests.

Do not add material-specific carrier transport until this electromagnetic question is understood.
