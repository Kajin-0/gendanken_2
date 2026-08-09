# Claim Ledger — Experiment 01

**Updated:** 2026-08-08  
**Status:** exploratory; several candidate universal bounds invalidated; fixed-target Hopfield retuning no-go is a model-level candidate distinct lemma with priority unproven  
**Purpose:** keep known inputs, derived results, invalidated ideas, candidate claims, and prior-art collisions separate.

---

## 1. Guiding question

Can an ideal photodetector simultaneously approach

```math
V_a\to0,
\qquad
\eta_{\rm abs}\to1,
\qquad
B\to\infty,
\qquad
\mathrm{intrinsic\ noise}\to0?
```

The project does not assume these limits are incompatible.

The research path has shown that geometric volume, finite absorber number, and arbitrarily large weak-coupling LDOS are each insufficient as standalone explanations of a universal detector limit.

The current strongest internally derived statement concerns **simultaneous optical access and irreversible detector access** in a nonperturbative two-mode Hopfield model.

---

## 2. Established prior/model ingredients — not novelty claims

### K1 — One-port temporal coupled-mode theory

A passive one-port resonance with external amplitude-decay rate `gamma_e` and internal absorptive amplitude-decay rate `gamma_a` has Lorentzian absorptance and critical coupling at `gamma_e = gamma_a`.

### K2 — Dielectric participation loss

For a weakly lossy dielectric in a weakly damped mode,

```math
\gamma_a
=\frac{\omega}{2}p_a\tan\delta.
```

### K3 — Material-response optical bounds

Passivity/optical-theorem bounds constrain absorption for specified material susceptibility and specified excitation. Miller et al., *Optics Express* 24, 3329-3364 (2016), DOI `10.1364/OE.24.003329`.

### K4 — Thermal photon statistics

Thermal photon counting includes both particle and Bose-bunching terms. Zmuidzinas, *Applied Optics* 42, 4989-5008 (2003), DOI `10.1364/AO.42.004989`.

### K5 — Quantum dark-state photodetection

Young, Sarovar & Leonard, *Physical Review A* 97, 033836 (2018), DOI `10.1103/PhysRevA.97.033836`, show that an idealized dark-state detector architecture can approach unit efficiency, negligible dark counts, and minimal jitter under its resource assumptions. Therefore quantum mechanics alone does not justify a universal efficiency-dark-count-jitter tradeoff.

### K6 — Bandwidth-averaged LDOS bounds

Shim, Fan, Johnson & Miller, *Physical Review X* 9, 011043 (2019), DOI `10.1103/PhysRevX.9.011043`, bound LDOS enhancement over nonzero bandwidth when material response, admissible region, and emitter-environment separation are constrained.

### K7 — Finite-wavefunction regularization

Finite emitter wavefunctions regularize point-dipole high-momentum singularities. Scala et al., *New Journal of Physics* 22, 123047 (2020), DOI `10.1088/1367-2630/abd204`.

### K8 — Deep-strong light-matter decoupling

Gauge-consistent ultrastrong/deep-strong coupling can invalidate the monotonic Purcell picture and suppress coupling to external reservoirs. Relevant prior theory includes De Liberato, *Physical Review Letters* 112, 016401 (2014), De Bernardis et al. (2018), and Palafox et al., *Journal of Physics: Photonics* 7, 04LT02 (2025).

These are established ingredients. Do not claim them as repository novelty.

---

## 3. Derived one-port results

Canonical file: `ONE_PORT_RESONATOR_DYNAMICS.md`.

### D1 — Exact absorptance

```math
\boxed{
A(\omega)
=\frac{4\gamma_e\gamma_a}
{(\omega-\omega_0)^2+(\gamma_e+\gamma_a)^2}.
}
```

### D2 — Absorbed-power modulation bandwidth

```math
\boxed{
B_{3\rm dB}
=\frac{\gamma_e+\gamma_a}{2\pi}.
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

### D3 — Optical linewidth is distinct

At critical coupling,

```math
\boxed{
\Delta f_{\rm abs,FWHM}
=2B_{3\rm dB}.
}
```

### D4 — Independent bulk-dark-event toy optimum

For the model `D = g_d V_a`, one-sided Poisson event noise, unity collection and no gain,

```math
\mathcal C
=\frac{h\nu\sqrt{B_{3\rm dB}}}{\mathrm{NEP}}
```

obeys

```math
\boxed{
\mathcal C^2
=\frac{4\gamma_a}{\pi D}
\frac{x^2}{(1+x)^3},
\qquad
x=\frac{\gamma_e}{\gamma_a}.
}
```

The optimum is

```math
\boxed{x=2,\qquad A_0=8/9.}
```

This is model-specific, not universal.

---

## 4. Active-volume counterexample

Canonical file: `ACTIVE_VOLUME_COUNTEREXAMPLE.md`.

Scale a lossy parallel-plate capacitor as

```math
d=s d_0,
\qquad
A=s A_0,
\qquad
s\to0.
```

Then capacitance remains fixed while

```math
V_a=Ad\propto s^2\to0.
```

For fixed modal energy,

```math
|E|^2\propto s^{-2},
```

so the active participation and `gamma_a` can remain finite. Hence

```math
\boxed{
\gamma_a/V_a\to\infty.
}
```

### D5 — Consequence

Geometric active volume alone does not bound absorptive modal rate in the ideal local-linear passive continuum model when arbitrary ideal field concentration is allowed.

---

## 5. Thermal input-channel result

Canonical file: `THERMAL_INPUT_CHANNEL.md`.

For one thermal spatial/polarization input channel with approximately constant Bose occupation `n_bar` over the resonance, exact counting including bunching gives

```math
\boxed{
\mathcal C_{\rm th}^2(x)
=\frac{2x}
{\pi\bar n[(1+x)^2+2\bar n x]}.
}
```

### D6 — Thermal-channel optimum

The unique positive optimum is critical coupling:

```math
\boxed{x=1.}
```

At the optimum,

```math
\boxed{
\mathcal C_{\rm th,max}^2
=\frac{1}{\pi\bar n(2+\bar n)}.
}
```

This is a one-channel thermal-background relation, not an internal-dark-count theorem.

---

## 6. Microscopic single-transition result

Canonical file: `MICROSCOPIC_SINGLE_TRANSITION.md`.

For one optically active state with optical amplitude rate `gamma_o` and irreversible dark-state amplitude rate `gamma_d`, the one-excitation detection probability is

```math
\boxed{
A_d(\omega)
=\frac{4\gamma_o\gamma_d}
{(\omega-\omega_0)^2+(\gamma_o+\gamma_d)^2}.
}
```

### D7 — Finite absorber count is insufficient

With at most one input photon, the two-level saturation nonlinearity is not accessed. Matched rates `gamma_o = gamma_d` reproduce the same critical-coupling structure.

Therefore finite absorber number / saturation alone does not impose a single-photon speed ceiling inside the Markov model.

Strong prior-art overlap: not a novelty candidate.

---

## 7. Conditional LDOS bandwidth constraint

Canonical file: `FINITE_TRANSITION_LDOS_BANDWIDTH_BOUND.md`.

Applying established bandwidth-averaged projected-LDOS limits to the matched microscopic detector gives the model self-consistency condition

```math
\boxed{
\Delta\omega_s
\le
\Gamma_0[1+F_B(\Delta\omega_s)]
}
```

under the note's stated weak-coupling/Markov assumptions.

In a narrowband low-loss near-field approximation,

```math
\boxed{
\left(\frac{\Delta\omega_s}{\omega_0}\right)^2
\lesssim
\frac{\Gamma_0/\omega_0}
{8(k_0d)^3}
\frac{\chi^2}{\epsilon}.
}
```

### D8 — Limitation

This becomes unbounded as `d -> 0`; finite emitter-environment separation is an essential resource assumption.

The LDOS theorem itself is prior work.

---

## 8. Finite emitter form factor

Canonical file: `FINITE_EMITTER_FORM_FACTOR.md`.

For the toy squared transition form factor

```math
|F(K)|^2=e^{-a^2K^2},
```

the planar high-`K` integral is

```math
\boxed{
I(d,a)
=\frac{1}{4a^3}
\left[
\sqrt\pi(1+2u^2)e^{u^2}\operatorname{erfc}(u)-2u
\right],
\qquad u=d/a.
}
```

At contact,

```math
\boxed{
I(0,a)=\frac{\sqrt\pi}{4a^3}.
}
```

### D9 — Oscillator-strength extent inequality

For one directional transition,

```math
f_x=\frac{2m\omega_0}{\hbar}|x_{ge}|^2,
```

and Cauchy-Schwarz gives

```math
\boxed{
\sigma_x
\ge |x_{ge}|
=\sqrt{\frac{\hbar f_x}{2m\omega_0}}.
}
```

Finite transition extent therefore regularizes the literal point-dipole divergence for fixed transition strength.

---

## 9. Oscillator-strength / extent stress test

Canonical file: `OSCILLATOR_STRENGTH_EXTENT_STRESS_TEST.md`.

The bare radiative rate may be written

```math
\boxed{
\frac{\Gamma_0}{\omega_0}
=\frac23\alpha f_x k_0\lambda_C.
}
```

Combining this with an optimistic finite-emitter envelope

```math
F_{\rm LDOS}\lesssim C_{\rm env}/(k_0a)^3
```

and the minimum extent inferred from the selected transition gives the perturbative upper envelope

```math
\boxed{
\frac{\Gamma_{\rm pert}}{\omega_0}
\lesssim
\frac{2^{5/2}}{3}
\frac{\alpha C_{\rm env}}
{\sqrt{f_x k_0\lambda_C}}.
}
```

### D10 — Insufficiency result

The retained oscillator-strength and finite-extent inequalities do not algebraically close the problem: their perturbative upper envelope grows as `f_x^{-1/2}` if the selected oscillator strength is allowed to decrease.

This is not an achievable divergence theorem. It identifies the point where the perturbative decay-rate picture becomes self-inconsistent.

---

## 10. Nonperturbative symmetric Hopfield result

Canonical file: `NONPERTURBATIVE_HOPFIELD_CAPTURE.md`.

Use the TRK-consistent two-mode Hopfield model. For equal bare frequencies `omega_c = omega_b = omega_0`,

```math
\boxed{
\omega_\pm
=\sqrt{\omega_0^2+g^2}\pm g.
}
```

With equal weak local optical and detector bath scales `gamma`, both polaritons have exact matched dressed rates

```math
\boxed{
\Gamma_{\pm,L}
=\Gamma_{\pm,R}
=\frac{\gamma}
{2\sqrt{1+(g/\omega_0)^2}}.
}
```

### D11 — Peak survives while bandwidth collapses

A resolved polariton can retain unit peak transfer while

```math
\boxed{
\Delta\omega_{\rm FWHM}
=\frac{2\gamma}
{\sqrt{1+(g/\omega_0)^2}}
\sim2\gamma\frac{\omega_0}{g}.
}
```

Thus arbitrarily increasing bare internal coupling does not yield arbitrarily broad useful transfer in this model.

The decoupling phenomenon is established prior physics; this detector interpretation is not yet a novelty claim.

---

## 11. Fixed-target Hopfield retuning theorem

Canonical file: `HOPFIELD_RETUNING_NO_GO.md`.

Hold the lower polariton at a fixed positive target frequency

```math
\omega_y=\omega_t>0
```

while retuning the bare frequencies and sending `g -> infinity`.

The exact fixed-target branch obeys

```math
\boxed{
(\omega_c^2-\omega_t^2)
(\omega_b^2-\omega_t^2)
=4g^2\frac{\omega_c}{\omega_b}\omega_t^2.
}
```

The lower-polariton mixing angle obeys

```math
\boxed{
\tan\theta
=\frac{\omega_b^2-\omega_t^2}
{2g\sqrt{\omega_c\omega_b}}.
}
```

For fixed positive local optical and detector bath scales `gamma_L`, `gamma_R`, the dressed lower-polariton rates are

```math
\Gamma_L
=\gamma_L\sin^2\theta\frac{\omega_c}{\omega_t},
```

```math
\Gamma_R
=\gamma_R\cos^2\theta\frac{\omega_t}{\omega_b}.
```

### D12 — Fixed-target retuning no-go

For every allowed sequence with

```math
g\to\infty,
\qquad
\omega_y=\omega_t>0,
```

and fixed local bath coupling resources,

```math
\boxed{
\min(\Gamma_L,\Gamma_R)\to0.
}
```

For one resolved lower-polariton transfer resonance,

```math
T_0
=\frac{4\Gamma_L\Gamma_R}
{(\Gamma_L+\Gamma_R)^2},
```

```math
\Delta\omega_{\rm FWHM}
=2(\Gamma_L+\Gamma_R).
```

Therefore peak transfer and transfer bandwidth cannot both remain bounded away from zero in the `g -> infinity` fixed-target limit.

### D13 — Symmetric retuning example

For `omega_c = omega_b = Omega(g)` and fixed lower target `omega_t`,

```math
\boxed{
\Omega^2
=\omega_t^2+2g\omega_t.
}
```

With equal local bath scales, peak transfer remains unity but

```math
\boxed{
\Delta\omega_{\rm FWHM}
=\frac{2\gamma\sqrt{\omega_t^2+2g\omega_t}}
{g+\omega_t}
\sim2\gamma\sqrt{\frac{2\omega_t}{g}}.
}
```

Retuning slows the asymptotic collapse from `g^{-1}` to `g^{-1/2}` in this family but does not remove it.

---

## 12. Candidate claim status

Canonical literature note: `HOPFIELD_RETUNING_PRIOR_ART_SWEEP.md`.

A focused initial search found extensive prior theory on deep-strong light-matter decoupling, Purcell-effect collapse, dressed dissipation, suppressed heat transport, and multimode decoupling.

No inspected source was found stating the exact fixed-dressed-frequency + arbitrary bare retuning + two-required-local-reservoir-overlap theorem above.

Current status:

> **CANDIDATE DISTINCT SUPPORTING LEMMA — PRIORITY UNPROVEN.**

Do not use `new`, `first`, `fundamental`, `universal`, or equivalent priority language.

Additional older polariton/open-harmonic-system literature must be searched before publication positioning.

---

## 13. Invalidated / stopped general claims

### H1 — Active-volume-only optical bound

Stopped. The shrinking-capacitor family invalidates `gamma_a/V_a <= constant` from passivity alone.

### H2 — Universal active-volume cancellation

Stopped as a general claim. It is conditional on `gamma_a proportional to V_a`.

### H3 — Universal schematic law `eta^2 B <= C V_a`

Stopped.

### H4 — Finite absorber number / saturation supplies the missing one-photon bound

Stopped. The one-excitation sector is linear.

### H5 — Oscillator strength + finite emitter extent automatically supplies a finite perturbative coupling ceiling

Stopped as a sufficient argument. The retained inequalities do not close when the selected transition strength varies.

### H6 — Arbitrarily large weak-coupling LDOS implies arbitrarily fast detector

Stopped. The perturbative description fails as coupling becomes nonperturbative, and the Hopfield model exhibits decoupling/linewidth collapse.

### H7 — Universal efficiency-dark-count-jitter tradeoff from quantum mechanics alone

Stopped. Resource-dependent dark-state detector counterexamples exist in prior theory.

---

## 14. Open questions

### C1 — Multimode robustness

Does a general multimode passive electromagnetic environment defeat or preserve the fixed-target two-access-channel no-go?

### C2 — Reservoir-resource scaling

Can `gamma_L` and/or `gamma_R` be scaled with internal coupling strongly enough to preserve both efficiency and bandwidth, and what physical resource cost does that require?

### C3 — Strong/non-Markov reservoirs

Does the result survive when the optical or detector reservoirs themselves are strongly coupled or structured?

### C4 — Thermodynamic irreversibility/reset

What free-energy, entropy-production, or reset resource is required to keep the detection transition effectively one-way while suppressing false events?

### C5 — Fermionic / finite-level generalization

Does an analogous two-access-channel constraint survive beyond the harmonic Hopfield matter model?

---

## 15. Explicit non-claims

Do not claim that

- real detector performance diverges as active volume tends to zero;
- the Hopfield retuning theorem is a universal photodetector theorem;
- the two-mode theorem automatically covers multimode photonic continua;
- bath coupling strengths can be scaled for free;
- thermal-background photons are internal dark counts;
- a full detector thermodynamic bound has been derived;
- the fixed-target lemma is novel or publishable before broader prior-art review.

---

## 16. Correction history

### C0.1 — Time-harmonic sign convention

Corrected during the one-port derivation before canonical promotion.

### C0.2 — Quality-factor rewrite

The correct relation is

```math
\boxed{B_{3\rm dB}=\frac{f_0}{2Q_L}.}
```

The earlier redundant `f_0/(4Q_L)` rewrite was incorrect.

---

## 17. Next promotion criterion

Do not promote the fixed-target lemma into a publication claim until it survives

1. a multimode/general-scattering counterexample attempt;
2. explicit accounting for scaled reservoir couplings;
3. a broader older-literature search in polariton transport and open harmonic networks;
4. numerical/algebraic symbolic checks of the retuned theorem where useful;
5. a precise statement of which detector architectures lie outside its scope.