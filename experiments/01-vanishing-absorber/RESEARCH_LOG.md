# Research Log — Experiment 01: The Vanishing Absorber

This file is chronological. It records why the research direction changed, including failed conjectures and prior-art collisions.

---

## 2026-08-08 — Experiment opened

Guiding question:

> Can an ideal photodetector be made arbitrarily small, arbitrarily fast, arbitrarily sensitive, and still absorb essentially every incident photon?

Initial intuition: shrinking active semiconductor volume may reduce bulk dark-event count and transit distance, while passive optical confinement can restore absorption. The first candidate penalty was photon dwell time / bandwidth.

The provisional schematic relation

```text
eta^2 B <= C V
```

was explicitly recorded as an unproved target, not a result.

Decision: begin with the smallest exact one-port resonator model rather than a general theorem or HgCdTe-specific device physics.

---

## 2026-08-08 — One-port resonator derived

The exact one-port absorptance is

```math
A(\omega)
=\frac{4\gamma_e\gamma_a}
{(\omega-\omega_0)^2+(\gamma_e+\gamma_a)^2}.
```

Critical coupling `gamma_e = gamma_a` gives unit monochromatic absorptance.

The absorbed-power small-signal response is

```math
H_{\rm abs}(\Omega)
=\frac{\Gamma}{\Gamma+i\Omega},
\qquad
\Gamma=\gamma_e+\gamma_a,
```

so

```math
B_{3\rm dB}=\frac{\Gamma}{2\pi}.
```

At critical coupling,

```math
B_{3\rm dB}=\frac{\gamma_a}{\pi}.
```

Thus the initial cavity intuition survives **in terms of absorber loss rate**: if `gamma_a -> 0`, maintaining unity absorption makes the temporal response narrow.

The optical absorptance FWHM is twice the absorbed-power modulation `-3 dB` bandwidth at critical coupling.

### Unexpected optimization

Combining the optical result with the minimal independent Poisson bulk-dark-event model produced

```math
\mathcal C^2
=\frac{4\gamma_a}{\pi D}
\frac{x^2}{(1+x)^3},
\qquad
x=\frac{\gamma_e}{\gamma_a}.
```

The optimum is `x = 2`, not critical coupling, giving `A_0 = 8/9` and an approximately `8.9%` improvement in this particular sensitivity-speed metric relative to critical coupling.

### Verification/corrections

Direct time-domain integration reproduced the modulation transfer function. A numerical coupling scan recovered `x ~= 2.00003`.

Two convention errors were caught before canonical promotion:

1. one harmonic-sign mismatch;
2. an incorrect redundant `Q` rewrite.

The correct relation is

```math
B_{3\rm dB}=\frac{f_0}{2Q_L}.
```

Direction change: the bottleneck became whether `gamma_a` must scale with active volume.

---

## 2026-08-08 — Active-volume-only bound falsified

An explicit shrinking parallel-plate capacitor family was constructed:

```math
d=s d_0,
\qquad
A=s A_0,
\qquad
s\to0.
```

Capacitance stays fixed, while

```math
V_a=Ad\propto s^2\to0.
```

At fixed modal energy,

```math
|E|^2\propto s^{-2},
```

so dielectric participation and `gamma_a` can remain fixed. Therefore

```math
\boxed{\gamma_a/V_a\to\infty.}
```

This kills the conjecture that passivity alone bounds `gamma_a/V_a`, and stops the active-volume-only target `eta^2 B <= C V_a` as a general law.

The divergence obtained by simultaneously retaining `D = g_d V_a` is treated as evidence that continuum optical and extensive dark-event assumptions cannot both be extrapolated to `V_a -> 0`.

Direction change: move from geometric volume to microscopic light-matter resources.

---

## 2026-08-08 — Thermal input-channel branch

A separate restricted calculation considered thermal photons entering through the **same optical channel** as the signal.

For a Lorentzian one-port absorber and Bose occupation `n_bar`, long-time counting gives both the particle term and the bunching term.

The resulting dimensionless capability is

```math
\mathcal C_{\rm th}^2(x)
=\frac{2x}
{\pi\bar n[(1+x)^2+2\bar n x]}.
```

Unlike the independent bulk-dark-event model, this is optimized at

```math
\boxed{x=1}
```

because changing optical coupling changes both signal admission and thermal-background admission.

At critical coupling,

```math
\boxed{
\mathcal C_{\rm th,max}^2
=\frac{1}{\pi\bar n(2+\bar n)}.
}
```

The absorber rate and geometric volume cancel from this restricted one-channel background relation.

Interpretation: the optimum coupling itself identifies where the dominant noise enters the detector.

This branch is not an internal-dark-count theorem.

---

## 2026-08-08 — Single-transition absorber tested

The bulk dielectric was replaced by a microscopic three-state detector:

```text
|g> <-> |e> -> |d>,
```

where `|d>` is an irreversible dark detection state.

With at most one input photon, the dynamics stays in the one-excitation sector, so two-level saturation is never reached. The detection probability is again Lorentzian:

```math
A_d(\omega)
=\frac{4\gamma_o\gamma_d}
{(\omega-\omega_0)^2+(\gamma_o+\gamma_d)^2}.
```

Matched rates give unit monochromatic transfer, and if both rates are treated as free Markov parameters the response can be broadened.

Therefore finite absorber number / saturation alone does not supply the missing single-photon speed bound.

### Prior-art collision

Young, Sarovar & Leonard (PRA 97, 033836, 2018) already analyze closely related dark-state detector physics and show near-ideal efficiency/dark-count/jitter performance under their stated nonequilibrium assumptions.

Direction change: constrain the microscopic optical rate rather than absorber number.

---

## 2026-08-08 — Bandwidth-averaged LDOS bound applied

Known arbitrary-bandwidth projected-LDOS theory was applied to the finite-transition detector.

For fixed passive material response, finite signal bandwidth, admissible surrounding region, and finite emitter-environment separation `d`, the useful optical rate cannot be treated as arbitrarily large over the whole signal band.

A model self-consistency condition was obtained:

```math
\Delta\omega_s
\le
\Gamma_0[1+F_B(\Delta\omega_s)].
```

In a narrowband low-loss near-field approximation,

```math
\left(\frac{\Delta\omega_s}{\omega_0}\right)^2
\lesssim
\frac{\Gamma_0/\omega_0}
{8(k_0d)^3}
\frac{\chi^2}{\epsilon}.
```

But the bound still diverges as `d -> 0`.

Direction change: determine whether microscopic emitter extent or nonlocality supplies the missing spatial scale.

---

## 2026-08-08 — Finite transition-density form factor

A Gaussian squared transition form factor

```math
|F(K)|^2=e^{-a^2K^2}
```

was used to regularize the planar high-`K` near field.

The exact toy integral is

```math
I(d,a)
=\frac{1}{4a^3}
\left[
\sqrt\pi(1+2u^2)e^{u^2}\operatorname{erfc}(u)-2u
\right],
\qquad u=d/a.
```

At contact,

```math
I(0,a)=\frac{\sqrt\pi}{4a^3},
```

so finite transition extent removes the literal point-dipole `d^{-3}` divergence.

For one directional oscillator strength,

```math
f_x=\frac{2m\omega_0}{\hbar}|x_{ge}|^2,
```

Cauchy-Schwarz gives

```math
\sigma_x\ge |x_{ge}|
=\sqrt{\frac{\hbar f_x}{2m\omega_0}}.
```

Thus, at fixed nonzero transition strength, spatial extent and dipole strength cannot be shrunk independently.

---

## 2026-08-08 — Oscillator-strength/extent stress test

The next adversarial question allowed the selected transition oscillator strength itself to vary.

Using

```math
\frac{\Gamma_0}{\omega_0}
=\frac23\alpha f_x k_0\lambda_C
```

and a generic finite-emitter near-field envelope

```math
F_{\rm LDOS}\lesssim\frac{C_{\rm env}}{(k_0a)^3},
```

together with the minimum extent inferred from `f_x`, gives the perturbative upper envelope

```math
\frac{\Gamma_{\rm pert}}{\omega_0}
\lesssim
\frac{2^{5/2}}3
\frac{\alpha C_{\rm env}}
{\sqrt{f_xk_0\lambda_C}}.
```

This envelope grows as `f_x^{-1/2}` if the selected transition strength is allowed to shrink.

This does **not** prove an achievable divergence. It proves that oscillator-strength and finite-emitter inequalities alone do not algebraically close the weak-coupling problem.

The formal envelope eventually reaches `Gamma/omega_0 = O(1)`, exactly where the Markov/Purcell-rate description stops being controlled.

Direction change: diagonalize the light-matter system nonperturbatively instead of imposing an arbitrary rate cutoff.

---

## 2026-08-08 — Nonperturbative Hopfield capture

A TRK-consistent two-mode Hopfield model was used with one photonic oscillator, one material oscillator, and weak local optical/detector reservoirs.

For equal bare frequencies,

```math
\omega_\pm
=\sqrt{\omega_0^2+g^2}\pm g.
```

For equal local bath scales, exact dressed rates for both polaritons are

```math
\Gamma_{\pm,L}
=\Gamma_{\pm,R}
=\frac{\gamma}
{2\sqrt{1+(g/\omega_0)^2}}.
```

Thus each resolved polariton can remain perfectly impedance/rate matched and retain unit peak transfer while its transfer linewidth collapses:

```math
\Delta\omega_{\rm FWHM}
=\frac{2\gamma}
{\sqrt{1+(g/\omega_0)^2}}
\sim2\gamma\frac{\omega_0}{g}.
```

This is consistent with established deep-strong light-matter decoupling / breakdown-of-Purcell physics.

Counterexample proposed: retune the bare frequencies with `g` so one dressed pole remains at the desired signal carrier.

---

## 2026-08-08 — Fixed-target retuning no-go derived

The retuning attack produced the strongest current model-level result.

Hold the lower polariton at a fixed positive target frequency

```math
\omega_y=\omega_t
```

while allowing `omega_c(g)` and `omega_b(g)` to vary and sending `g -> infinity`.

The exact fixed-target branch obeys

```math
(\omega_c^2-\omega_t^2)
(\omega_b^2-\omega_t^2)
=4g^2\frac{\omega_c}{\omega_b}\omega_t^2.
```

The lower-polariton mixing ratio is

```math
\tan\theta
=\frac{\omega_b^2-\omega_t^2}
{2g\sqrt{\omega_c\omega_b}}.
```

For fixed positive local optical and detector bath scales, a contradiction proof yields

```math
\boxed{
\min(\Gamma_L,\Gamma_R)\to0.
}
```

For a resolved transfer resonance,

```math
T_0
=\frac{4\Gamma_L\Gamma_R}
{(\Gamma_L+\Gamma_R)^2},
```

and

```math
\Delta\omega_{\rm FWHM}
=2(\Gamma_L+\Gamma_R).
```

Therefore peak transfer and linewidth cannot both remain bounded away from zero in the fixed-target `g -> infinity` limit.

### Explicit symmetric retuning

For `omega_c = omega_b = Omega(g)`, holding the lower pole at `omega_t` requires

```math
\Omega^2=\omega_t^2+2g\omega_t.
```

Equal local bath scales keep peak transfer at unity but

```math
\Delta\omega_{\rm FWHM}
=\frac{2\gamma\sqrt{\omega_t^2+2g\omega_t}}
{g+\omega_t}
\sim2\gamma\sqrt{\frac{2\omega_t}{g}}.
```

Retuning changes the asymptotic narrowing from `g^{-1}` to `g^{-1/2}` in this family but does not remove it.

Interpretation: the detector must retain both optical access and irreversible material/detector access. At infinite internal coupling and fixed target frequency, at least one access vanishes in this model.

---

## 2026-08-08 — Focused prior-art collision on fixed-target lemma

The search target was not generic deep-strong decoupling. It was specifically:

```text
fixed dressed frequency
+ arbitrary bare-frequency retuning
+ g -> infinity
+ fixed local optical and detector bath resources
=> one dressed bath overlap -> 0
=> peak transfer or bandwidth -> 0.
```

Closest inspected work establishes deep-strong decoupling, Purcell-effect collapse, gauge-consistent dressed dissipation, `1/g` decay suppression for fixed bare parameters, heat-current suppression, and multimode decoupling.

No inspected source was found stating the exact fixed-target retuning theorem above.

Current verdict:

> **candidate distinct supporting lemma; priority unproven.**

This is a negative search result, not a novelty claim.

---

## Current direction

The next adversarial target is the most plausible escape from the current theorem:

> Can a multimode optical environment or deliberately scaled reservoir engineering preserve finite optical-to-detector peak transfer and finite bandwidth at fixed target frequency as internal light-matter coupling becomes arbitrarily large?

Do not add HgCdTe-specific transport yet. The research has not reached the material-specific layer.