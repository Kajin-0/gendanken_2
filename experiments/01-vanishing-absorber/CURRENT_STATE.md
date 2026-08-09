# Current State — Experiment 01: The Vanishing Absorber

**Date:** 2026-08-08  
**Status:** exploratory; several candidate bounds falsified; fixed-target Hopfield transfer no-go derived as a model-level candidate lemma; novelty unproven  

## 1. Guiding question

Can an ideal photodetector be made arbitrarily small, arbitrarily fast, arbitrarily sensitive, and still absorb essentially every incident photon?

The project deliberately does not assume that the answer is no.

The useful outcome so far has been a sequence of **penalty migrations**: when one apparent constraint is removed, the cost reappears in a deeper physical resource—or the proposed bound fails entirely.

---

## 2. Canonical supporting notes

Read in this order after `AGENTS.md`:

1. `ONE_PORT_RESONATOR_DYNAMICS.md`
2. `ACTIVE_VOLUME_COUNTEREXAMPLE.md`
3. `THERMAL_INPUT_CHANNEL.md`
4. `MICROSCOPIC_SINGLE_TRANSITION.md`
5. `FINITE_TRANSITION_LDOS_BANDWIDTH_BOUND.md`
6. `FINITE_EMITTER_FORM_FACTOR.md`
7. `OSCILLATOR_STRENGTH_EXTENT_STRESS_TEST.md`
8. `NONPERTURBATIVE_HOPFIELD_CAPTURE.md`
9. `HOPFIELD_RETUNING_NO_GO.md`
10. `HOPFIELD_RETUNING_PRIOR_ART_SWEEP.md`

`CLAIM_LEDGER.md` defines what may and may not currently be claimed.

---

## 3. Stage A — one-port resonant absorber

For a passive one-port resonance,

```math
A(\omega)
=
\frac{4\gamma_e\gamma_a}
{(\omega-\omega_0)^2+(\gamma_e+\gamma_a)^2}.
```

The absorbed-power small-signal bandwidth is

```math
\boxed{
B_{3\rm dB}
=
\frac{\gamma_e+\gamma_a}{2\pi}.
}
```

At critical coupling,

```math
\boxed{
\gamma_e=\gamma_a,
\qquad
A_0=1,
\qquad
B_{3\rm dB}=\frac{\gamma_a}{\pi}.
}
```

Thus **if** the active optical loss rate tends to zero, unity monochromatic absorption becomes proportionally narrow in this architecture.

The optical absorptance FWHM and absorbed-power modulation bandwidth are not the same quantity; at critical coupling,

```math
\Delta f_{\rm abs,FWHM}
=2B_{3\rm dB}.
```

---

## 4. Stage B — geometric active volume is not fundamental

For weak dielectric loss,

```math
\gamma_a
=\frac{\omega}{2}p_a\tan\delta,
```

where `p_a` is active electric-energy participation.

An explicit parallel-plate family with

```math
d=s d_0,
\qquad
A=s A_0
```

keeps capacitance and participation finite while

```math
V_a=Ad\propto s^2\to0.
```

For fixed modal energy,

```math
|E|^2\propto s^{-2},
```

so the active loss rate can stay finite and

```math
\boxed{
\gamma_a/V_a\to\infty.
}
```

Therefore passivity alone does **not** support a universal active-volume-only optical bound when arbitrary ideal field concentration is allowed.

The schematic target

```text
eta^2 B <= C V_a
```

is stopped as a general claim.

---

## 5. Stage C — thermal photons in the same optical channel

For one thermal spatial/polarization input channel with Bose occupation `n_bar` approximately constant across the resonance, exact thermal counting including bunching gives a distinct sensitivity-speed relation.

Using

```math
\mathcal C_{\rm th}
=\frac{h\nu\sqrt{B_{3\rm dB}}}
{\mathrm{NEP}_{\rm th}},
```

the coupling-dependent result is

```math
\boxed{
\mathcal C_{\rm th}^2(x)
=
\frac{2x}
{\pi\bar n\left[(1+x)^2+2\bar n x\right]},
\qquad
x=\frac{\gamma_e}{\gamma_a}.
}
```

The optimum is

```math
\boxed{x=1}
```

rather than the `x=2` optimum obtained earlier for an independent Poisson bulk-dark-event model.

At critical coupling,

```math
\boxed{
\mathcal C_{\rm th,max}^2
=
\frac{1}{\pi\bar n(2+\bar n)}.
}
```

Here the absorber rate, cavity `Q`, and active volume cancel because the useful signal and thermal noise enter through the same optical channel.

This is a **one-channel thermal-background result**, not an internal-dark-count theorem.

---

## 6. Stage D — one microscopic transition still does not close the loophole

Replace the continuum absorber by

```text
|g> <-> |e> -> |d>,
```

where `|d>` is an irreversible dark detection state.

With at most one input photon, the accessible sector contains only one excitation, so two-level saturation is not invoked.

The detection probability is again

```math
\boxed{
A_d(\omega)
=
\frac{4\gamma_o\gamma_d}
{(\omega-\omega_0)^2+(\gamma_o+\gamma_d)^2}.
}
```

Perfect monochromatic transfer occurs at

```math
\gamma_o=\gamma_d.
```

If the rates are treated as free Markov parameters, scaling both upward broadens the detector without reducing peak transfer.

Therefore **finite absorber number / two-level saturation is not the missing single-photon resource**.

This branch has strong prior-art overlap with quantum dark-state detector models and is not a novelty candidate.

---

## 7. Stage E — constrained passive LDOS creates a conditional bandwidth ceiling

For a finite electric transition in the weak-coupling/Markov regime, radiative rate is controlled by projected LDOS.

Established arbitrary-bandwidth LDOS theory gives a finite average enhancement when the following are fixed:

- passive material response;
- nonzero signal bandwidth;
- admissible surrounding region;
- finite emitter-environment separation `d`.

Applying that known LDOS bound to the matched-rate microscopic detector yields the implicit condition

```math
\boxed{
\Delta\omega_s
\le
\Gamma_0
\left[1+F_B(\Delta\omega_s)
\right],
}
```

under the same narrowband Markov/free-space-rate normalization stated in the detailed note.

In a narrowband low-loss near-field approximation,

```math
\boxed{
\left(
\frac{\Delta\omega_s}{\omega_0}
\right)^2
\lesssim
\frac{\Gamma_0/\omega_0}
{8(k_0d)^3}
\frac{\chi^2}{\epsilon}.
}
```

This is conditional, not universal, and still diverges as `d -> 0`.

---

## 8. Stage F — finite transition density regularizes the point-dipole divergence

A point emitter has high-spatial-frequency weight at arbitrarily large wave vector.

A simple Gaussian transition-density form factor

```math
|F(K)|^2=e^{-a^2K^2}
```

changes the local near-field integral from

```math
I_{\rm point}(d)
=\frac{1}{4d^3}
```

to

```math
\boxed{
I(d,a)
=\frac{1}{4a^3}
\left[
\sqrt\pi(1+2u^2)e^{u^2}\operatorname{erfc}(u)
-2u
\right],
\qquad
u=d/a.
}
```

At geometric contact,

```math
\boxed{
I(0,a)
=\frac{\sqrt\pi}{4a^3}.
}
```

Thus finite transition extent replaces the literal point-source divergence by a microscopic `a^{-3}` scale.

For one directional oscillator strength,

```math
f_x
=\frac{2m\omega_0}{\hbar}|x_{ge}|^2,
```

Cauchy-Schwarz implies

```math
\boxed{
\sigma_x
\ge
|x_{ge}|
=\sqrt{
\frac{\hbar f_x}{2m\omega_0}
}.
}
```

The emitter size and transition strength therefore cannot be varied independently when `f_x` is fixed.

---

## 9. Stage G — oscillator strength plus finite extent is still insufficient in perturbation theory

Combining

```math
\Gamma_0/\omega_0
=\frac23\alpha f_x k_0\lambda_C
```

with an optimistic finite-emitter near-field envelope

```math
F_{\rm LDOS}
\lesssim
\frac{C_{\rm env}}{(k_0a)^3}
```

and the minimum extent inferred from the selected transition gives

```math
\boxed{
\frac{\Gamma_{\rm pert}}{\omega_0}
\lesssim
\frac{2^{5/2}}{3}
\frac{\alpha C_{\rm env}}
{\sqrt{f_x k_0\lambda_C}}.
}
```

The **upper envelope permitted by these inequalities** grows as `f_x^{-1/2}` if the selected oscillator strength is allowed to shrink.

This does not prove an achievable divergence. It proves that TRK/oscillator-strength information plus a finite-emitter cutoff does not algebraically close the problem by itself.

The perturbative estimate eventually reaches the regime

```math
\Gamma/\omega_0=O(1),
```

where the fixed-transition LDOS/Markov picture is no longer self-consistent.

---

## 10. Stage H — nonperturbative Hopfield model reverses the naive speed extrapolation

Use a TRK-consistent two-mode Hopfield Hamiltonian with photonic frequency `omega_c`, material frequency `omega_b`, internal coupling `g`, and

```math
D=g^2/\omega_b.
```

For equal bare frequencies

```math
\omega_c=\omega_b=\omega_0,
```

the exact polariton frequencies are

```math
\boxed{
\omega_\pm
=\sqrt{\omega_0^2+g^2}\pm g.
}
```

If the photonic coordinate is weakly coupled to an optical bath and the matter coordinate to an irreversible detector bath with equal bare damping scale `gamma`, the dressed bath rates are exactly

```math
\boxed{
\Gamma_{\pm,L}
=\Gamma_{\pm,R}
=
\frac{\gamma}
{2\sqrt{1+(g/\omega_0)^2}}.
}
```

Hence each resolved polariton can retain unit **peak** transfer while its transfer FWHM collapses as

```math
\boxed{
\Delta\omega_{\rm FWHM}
=\frac{2\gamma}
{\sqrt{1+(g/\omega_0)^2}}
\sim
2\gamma\frac{\omega_0}{g}.
}
```

Arbitrarily large bare internal coupling therefore does not yield arbitrarily large useful detector bandwidth in this model.

This is consistent with established deep-strong light-matter decoupling / breakdown-of-Purcell physics.

---

## 11. Stage I — fixed-target retuning no-go

A stronger result survives retuning of the bare frequencies.

Hold the lower polariton at

```math
\boxed{\omega_y=\omega_t>0}
```

while allowing `omega_c(g)` and `omega_b(g)` to vary and sending

```math
g\to\infty.
```

On the physical lower-polariton branch,

```math
\boxed{
(\omega_c^2-\omega_t^2)
(\omega_b^2-\omega_t^2)
=
4g^2\frac{\omega_c}{\omega_b}\omega_t^2.
}
```

The lower-polariton mixing angle obeys

```math
\boxed{
\tan\theta
=
\frac{\omega_b^2-\omega_t^2}
{2g\sqrt{\omega_c\omega_b}}.
}
```

With fixed positive local optical and detector bath scales `gamma_L`, `gamma_R`, the dressed rates satisfy

```math
\Gamma_R
\le
\gamma_R\frac{\omega_t}{\omega_b},
```

and

```math
\Gamma_L
\le
\gamma_L
\frac{(\omega_b^2-\omega_t^2)^2}
{4g^2\omega_b\omega_t}.
```

A contradiction argument then gives

```math
\boxed{
\min(\Gamma_L,\Gamma_R)
\to0
\qquad
(g\to\infty,\ \omega_y=\omega_t).
}
```

For resolved-polariton transfer,

```math
T_0
=\frac{4\Gamma_L\Gamma_R}
{(\Gamma_L+\Gamma_R)^2},
```

```math
\Delta\omega_{\rm FWHM}
=2(\Gamma_L+\Gamma_R).
```

Therefore peak transfer and linewidth **cannot both remain bounded away from zero** as `g -> infinity` at fixed target frequency with fixed local reservoir coupling resources.

This is currently the strongest internally derived model-level statement.

---

## 12. Prior-art status of the fixed-target lemma

A targeted search found extensive prior work on

- deep-strong light-matter decoupling;
- collapse/reversal of Purcell enhancement;
- gauge-consistent dressed dissipation;
- `1/g` polariton decay for fixed bare parameters;
- deep-strong heat-current suppression;
- multimode light-matter decoupling.

No inspected source was found stating the exact **fixed dressed frequency + arbitrary bare retuning + two required local reservoir overlaps** theorem above.

This is recorded in

`HOPFIELD_RETUNING_PRIOR_ART_SWEEP.md`.

Current status:

> **candidate distinct supporting lemma; priority unproven.**

Do not call it new, first, fundamental, or universal.

---

## 13. Current physical interpretation

The thought experiment has moved far from geometric detector volume.

The recurring structure is now

```text
useful optical access
+
irreversible detector/material access
```

A detector must retain both.

In the current nonperturbative model, attempting to make internal light-matter coupling arbitrarily large while retaining a fixed target frequency forces at least one of those two accesses to disappear.

This is a deeper form of penalty migration than the original weak-absorber cavity argument.

---

## 14. What is still not established

We have **not** established

- a universal photodetector sensitivity-speed theorem;
- that the fixed-target Hopfield no-go survives arbitrary multimode environments;
- that it survives scaling the optical/detector reservoir couplings themselves with `g`;
- a theorem for strong/non-Markovian detector reservoirs;
- a theorem for active, time-varying, or nonreciprocal structures;
- a complete fermionic finite-level matter treatment;
- a thermodynamic minimum work/reset cost;
- novelty or publication significance of the fixed-target lemma.

---

## 15. Next decisive test

The next adversarial target should be the most plausible escape from the current lemma:

> **Can a multimode optical environment or deliberately scaled reservoir engineering maintain finite optical-to-detector peak transfer and bandwidth at fixed target frequency as the internal light-matter coupling becomes arbitrarily large?**

Do not add HgCdTe-specific transport yet.

If the two-mode result survives a meaningful multimode/general-scattering extension, the project may finally have a robust detector-level theoretical structure worth shaping into a paper.