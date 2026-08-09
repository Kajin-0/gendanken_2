# Research Log — Experiment 01: The Vanishing Absorber

This file is chronological. It records why the research direction changed, especially when a counterexample killed the conjecture that motivated the branch.

---

## 2026-08-08 — Experiment opened

Guiding question:

> Can an ideal photodetector be made arbitrarily small, arbitrarily fast, arbitrarily sensitive, and still absorb essentially every incident photon?

Initial intuition:

```text
smaller active volume
-> fewer bulk dark events / shorter transport

passive optical confinement
-> recover absorption

maybe the penalty reappears as optical dwell time / bandwidth.
```

No theorem was assumed.

The schematic possibility

```text
eta^2 B <= C V
```

was recorded only as a motivating target, not a result.

Decision: start with one exact resonator before generalizing.

---

## 2026-08-08 — One-port resonator derived

Using one temporal coupled-mode convention throughout gave

```math
A(\omega)
=
\frac{4\gamma_e\gamma_a}
{(\omega-\omega_0)^2+(\gamma_e+\gamma_a)^2},
```

and the absorbed-power modulation response

```math
H_{\rm abs}(\Omega)
=\frac{\Gamma}{\Gamma+i\Omega},
\qquad
\Gamma=\gamma_e+\gamma_a.
```

Hence

```math
B_{3\rm dB}
=\frac{\Gamma}{2\pi}.
```

At critical coupling,

```math
\gamma_e=\gamma_a,
\qquad
A_0=1,
\qquad
B_{3\rm dB}=\frac{\gamma_a}{\pi}.
```

The intuitive dwell-time penalty therefore survives **in terms of `gamma_a`**.

An important factor-of-two distinction also emerged:

```math
\Delta f_{\rm abs,FWHM}
=2B_{3\rm dB}^{\rm crit}.
```

The optical linewidth is not numerically identical to detector modulation bandwidth.

### Unexpected coupling optimum

Combining the optical result with the minimal independent Poisson bulk-dark-event model produced

```math
\mathcal C^2
=
\frac{4\gamma_a}{\pi D}
\frac{x^2}{(1+x)^3},
\qquad
x=\gamma_e/\gamma_a.
```

The optimum was not critical coupling but

```math
x=2,
\qquad
A_0=8/9.
```

This improved the toy sensitivity-speed metric by about `8.9%` relative to exact critical coupling.

The result emerged from the algebra rather than being targeted.

### Conditional volume cancellation

If

```math
\gamma_a=\kappa V,
\qquad
D=g_dV,
```

then active volume cancels from the toy optimized metric.

The weakness was immediately identified: `gamma_a proportional to V` had not been established for field-concentrating structures.

### Checks/corrections

Direct time-domain integration reproduced the modulation transfer function.

Two redundant convention mistakes were caught before canonical promotion:

1. a time-harmonic sign mismatch;
2. an incorrect `Q` rewrite of an already-correct decay-rate formula.

The corrected relation is

```math
B_{3\rm dB}=f_0/(2Q_L).
```

---

## 2026-08-08 — Active-volume-only route falsified

The next branch deliberately tried to defeat

```math
\gamma_a\propto V_a.
```

A shrinking parallel-plate capacitor provides an explicit ideal continuum counterexample.

Choose

```math
d=s d_0,
\qquad
A=s A_0,
```

so capacitance stays fixed but

```math
V_a=Ad\propto s^2\to0.
```

For fixed modal energy,

```math
|E|^2\propto s^{-2},
```

so electric participation and therefore `gamma_a` can remain finite.

Thus

```math
\boxed{
gamma_a/V_a\to\infty.
}
```

Direction change:

> Geometric active volume is not the fundamental optical resource.

The active-volume-only law and the conjecture that passivity bounds `gamma_a/V_a` were stopped.

The apparent divergence is not a prediction of infinite real detector performance; it shows that continuum electromagnetic response and extensive dark-event scaling cannot both be extrapolated indefinitely.

---

## 2026-08-08 — Thermal signal-channel branch

A restricted passive thermal-input problem was solved exactly, including Bose bunching.

For one thermal spatial/polarization mode, the optimized sensitivity-speed quantity is

```math
\boxed{
\mathcal C_{\rm th,max}^2
=\frac1{\pi\bar n(2+\bar n)}.
}
```

The optimum moves back to critical coupling.

Interpretation:

> when signal and background photons enter through the same optical channel, the absorber rate and `Q` cancel from this restricted ratio.

This is a background-channel result, not an internal-dark-count theorem.

---

## 2026-08-08 — Finite microscopic absorber tested

The continuum absorber was replaced by one optical transition plus an irreversible dark detection state.

In the one-excitation sector the two-level system remains linear, giving the same matched-rate transfer structure.

Therefore finite absorber number / saturation did **not** create the hoped-for one-photon speed ceiling.

Prior-art collision with Young, Sarovar & Leonard dark-state quantum photodetector models reinforced the lesson:

> quantum mechanics alone does not imply a universal efficiency-dark-count-jitter tradeoff without architectural and thermodynamic resource assumptions.

Direction change: constrain the **optical coupling rate** of a finite transition instead.

---

## 2026-08-08 — Finite transition and bandwidth-averaged LDOS

Established bandwidth-averaged LDOS theory gives finite enhancement once the passive environment, material response, finite bandwidth, and nonzero emitter-environment separation are fixed.

The result still diverges as separation tends to zero.

Direction change: the missing resource appears to be microscopic spatial extent/nonlocality rather than active volume.

---

## 2026-08-08 — Finite emitter form factor

A finite transition-density form factor regularizes the literal point-dipole ultraviolet divergence.

A Gaussian transition density replaces the `d^{-3}` contact divergence by finite `a^{-3}` scaling.

TRK/oscillator-strength relations also tie transition dipole strength to a nonzero wavefunction extent when selected oscillator strength is fixed.

This looked promising but was immediately stress-tested by allowing oscillator strength itself to vary.

---

## 2026-08-08 — Oscillator-strength/extent route insufficient

Combining bare radiative strength, finite-emitter extent, and optimistic LDOS scaling gave a perturbative upper envelope that increases as selected oscillator strength decreases.

This does **not** establish an achievable divergence.

It establishes that those inequalities alone do not close the problem.

The formal envelope reaches

```math
\Gamma/\omega_0=O(1),
```

where treating the interaction as an enhanced Markov decay rate becomes self-inconsistent.

Direction change: diagonalize the light-matter sector nonperturbatively.

---

## 2026-08-08 — Nonperturbative Hopfield capture

A TRK-consistent two-mode Hopfield model was used with weak local optical and detector reservoirs.

For equal bare frequencies and equal local bath scales,

```math
\Gamma_{\pm,L}
=\Gamma_{\pm,R}
=\frac{\gamma}
{2\sqrt{1+(g/\omega_0)^2}}.
```

Each resolved polariton remains perfectly matched, so peak transfer can remain unity, but

```math
\Delta\omega_{\rm FWHM}
\sim2\gamma\frac{\omega_0}{g}.
```

Thus strong internal hybridization does not produce unlimited useful bandwidth.

This is consistent with established deep-strong light-matter decoupling / breakdown-of-Purcell physics.

Counterexample proposed: retune the bare frequencies with `g` so the useful dressed pole stays at the desired detector carrier.

---

## 2026-08-08 — Fixed-target Hopfield retuning no-go

The retuning attack produced a stronger two-mode statement.

Hold

```math
\omega_y=\omega_t>0
```

while allowing bare-frequency retuning and taking `g -> infinity`.

The exact fixed-target relation is

```math
(\omega_c^2-\omega_t^2)
(\omega_b^2-\omega_t^2)
=4g^2\frac{\omega_c}{\omega_b}\omega_t^2.
```

For fixed local optical/detector bath resources, a contradiction proof gives

```math
\boxed{
\min(\Gamma_L,\Gamma_R)\to0.
}
```

Therefore peak transfer and linewidth cannot both remain finite at fixed target frequency in the `g -> infinity` limit.

The symmetric retuning family keeps peak transfer at one but narrows as `g^{-1/2}` rather than `g^{-1}`.

Physical interpretation:

```text
optical access
+
irreversible material access
```

must both survive; infinite internal coupling cannot substitute for both.

---

## 2026-08-08 — Focused prior-art collision on fixed-target lemma

The search target was the exact fixed-dressed-frequency retuning/two-reservoir statement, not generic deep-strong decoupling.

Closest work establishes Purcell collapse, dressed decay suppression, heat-current suppression, and multimode decoupling.

No inspected source stated the exact fixed-target theorem.

Verdict:

> **candidate distinct supporting lemma; priority unproven.**

No novelty language is permitted.

---

## 2026-08-08 — Reservoir-engineering escape quantified

The next attack allowed the bare optical/detector reservoir couplings themselves to scale with `g`.

Demand fixed performance

```math
T_0\ge\eta_*,
\qquad
\Delta\omega_{\rm FWHM}\ge W_*.
```

This forces a dressed-rate floor

```math
\Gamma_*
=\frac{W_*}{4}
\left(1-\sqrt{1-\eta_*}\right).
```

Optimizing across all allowed fixed-target retunings yields

```math
\boxed{
\max(\gamma_L,\gamma_R)
\ge
\Gamma_*
\sqrt{1+2g/\omega_t}.
}
```

Deep in strong coupling, at least one external reservoir resource must therefore grow as `sqrt(g)`.

The symmetric retuning family asymptotically saturates this scaling.

Direction change:

> Scaling the reservoirs is a valid escape only by spending an unbounded new external-access resource; eventually it also exits the weak-bath model.

---

## 2026-08-08 — Multimode escape audit

Two distinct multimode effects were separated.

### Spectator counterexample

A disconnected spectator sector can carry an arbitrarily large coupling while the useful detector block remains unchanged.

Therefore no general theorem may be phrased only in terms of the largest coupling anywhere in a multimode Hamiltonian.

### Spectral tiling

A bank of increasingly narrow matched resonances can preserve finite broadband response if useful mode count/density increases sufficiently fast.

In the sparse-resonance model,

```math
N(g)\Gamma(g)=O(1)
```

is the natural compensation scaling.

Contemporary multiresonant absorption theory independently treats spectral mode density as a broadband-response resource.

This showed that a genuine multimode statement should concern an **integrated transfer resource**, not individual linewidths.

---

## 2026-08-08 — Passive multimode transfer-area theorem

The sparse-resonance restriction was then removed.

For an arbitrary finite stable passive linear network

```math
A=-iH-(\Gamma_L+\Gamma_R+\Gamma_I),
```

with input/output normalization

```math
B_LB_L^\dagger=2\Gamma_L,
\qquad
C_R^\dagger C_R=2\Gamma_R,
```

define

```math
G_{RL}(s)=C_R(sI-A)^{-1}B_L.
```

The frequency-integrated transfer is the squared `H_2` norm:

```math
\mathcal I_{L\to R}
=
\int\frac{d\omega}{2\pi}
\operatorname{Tr}(G_{RL}^\dagger G_{RL}).
```

The left controllability Gramian satisfies

```math
AQ_L+Q_LA^\dagger+2\Gamma_L=0.
```

Passivity gives

```math
0\preceq Q_L\preceq I,
```

and the dual detector observability Gramian satisfies the analogous inequality.

Therefore

```math
\boxed{
\mathcal I_{L\to R}
\le
2\min(
\operatorname{Tr}\Gamma_L,
\operatorname{Tr}\Gamma_R
).
}
```

This handles arbitrary finite mode count, coherent coupling topology, overlapping resonances, and internal interference inside the stated passive Markov/LTI class.

For a target band of angular width `W`,

```math
\boxed{
\overline T_B
\le
\frac{4\pi}{W}
\min(
\operatorname{Tr}\Gamma_L,
\operatorname{Tr}\Gamma_R
).
}
```

Thus broadband efficient transfer requires an aggregate external-access budget on **both** sides.

### Why this changed the project

Mode count is not the final resource either.

Internal modes can redistribute transfer in frequency, but at fixed total optical/detector boundary access they cannot create unlimited integrated useful transfer.

The two previous escape routes now have one common interpretation:

```text
stronger reservoirs
or
more useful resonances

=> additional external access budget.
```

### Prior-art posture

`H_2`, Lyapunov Gramians, scattering-passive systems, and multiresonant broadband bounds are established prior mathematics/physics.

An initial targeted search did not locate the exact two-access trace inequality stated as a photodetector transfer-area result.

That negative search is not a novelty claim.

Current treatment:

> useful detector-facing passivity corollary; novelty unproven and not claimed.

### Verification

A deterministic random-matrix regression was added:

`numerics/passive_multimode_h2_stress.py`.

It checks the Gramian operator inequality and transfer-area bound across random passive networks and directly integrates a representative multimode transfer spectrum.

---

## Current direction

The research question is now substantially different from where it started.

The most robust surviving statement is:

> **Within a finite passive linear detector network, internal electromagnetic complexity can reshape the transfer spectrum but cannot replace the requirement for access to both the optical input reservoir and the irreversible detector reservoir. Frequency-integrated useful transfer is bounded by the smaller aggregate external-access budget.**

This is not yet claimed as novel or publication-ready.

Next attacks:

1. look for a tighter two-sided trace inequality;
2. treat direct finite-band bypass/feedthrough explicitly;
3. test strongly structured/non-Markovian reservoirs by expanding them into reaction-coordinate modes when possible;
4. map the abstract access matrices onto microscopic photodetector resources;
5. only then reintroduce dark-count, thermal reverse-rate, amplification, and reset thermodynamics;
6. broaden prior-art search before any manuscript decision.
