# Claim Ledger — Experiment 01

**Updated:** 2026-08-08  
**Status:** exploratory; one-resonance model derived; active-volume-only optical bound invalidated in ideal local continuum electrodynamics  
**Purpose:** keep known inputs, derivations, conjectures, invalidated ideas, and prior-art collisions separate.

---

## 1. Active question

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

The current issue is no longer whether a weak one-port absorber becomes slow. That is established within the one-resonance model.

The current issue is what physical resource replaces geometric active volume once field concentration is allowed.

---

## 2. Known or model-defining ingredients

### K1 — Bulk event-rate scaling

For a uniform volumetric dark-generation event-rate density `g_d`,

```math
D=g_dV_a.
```

This is an extensivity assumption/model definition. It is not expected to remain valid when the active degrees of freedom become microscopic and discrete.

### K2 — Temporal coupled-mode framework

A passive linear one-port resonance can be represented by a complex mode amplitude coupled to an external channel and an internal absorptive channel.

Established resonator theory.

### K3 — Critical coupling

Unity monochromatic absorption in the one-port model occurs when external leakage equals internal absorption loss.

Established resonator physics.

### K4 — Dielectric participation-factor loss

For a weakly lossy dielectric in a weakly damped resonator,

```math
\gamma_a
=
\frac{\omega}{2}p_a\tan\delta,
```

where `p_a` is the electric-energy participation fraction of the active dielectric.

This is standard resonator loss physics.

### K5 — Material-response absorption bounds

Passivity and the optical theorem give geometry-independent absorption bounds for a specified lossy susceptibility and specified background excitation. A representative homogeneous-isotropic form is

```math
P_{\rm abs}
\le
\frac{\omega\epsilon_0}{2}
\frac{|\chi|^2}{\operatorname{Im}\chi}
\int_{V_a}|\mathbf E_{\rm bg}|^2\,dV.
```

For a uniform plane wave,

```math
\frac{\sigma_{\rm abs}}{V_a}
\le
k\frac{|\chi|^2}{\operatorname{Im}\chi}.
```

This is prior electromagnetic theory, not a repository novelty claim.

Primary source: Miller et al., *Optics Express* 24, 3329-3364 (2016), DOI `10.1364/OE.24.003329`.

---

## 3. Derived results — one-port resonator

Canonical derivation:

`ONE_PORT_RESONATOR_DYNAMICS.md`

### D1 — Absorptance

```math
\boxed{
A(\omega)=
\frac{4\gamma_e\gamma_a}
{(\omega-\omega_0)^2+(\gamma_e+\gamma_a)^2}.
}
```

### D2 — Critical coupling

```math
\boxed{\gamma_e=\gamma_a}
```

gives `A(omega_0)=1`.

### D3 — Absorbed-power modulation bandwidth

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
B_{3\rm dB}^{\rm crit}
=
\frac{\gamma_a}{\pi}.
}
```

Thus `gamma_a -> 0` with unity absorption implies a narrow absorbed-power response in this architecture.

### D4 — Optical linewidth versus modulation bandwidth

At critical coupling,

```math
\boxed{
\Delta f_{\rm abs,FWHM}=2B_{3\rm dB}^{\rm crit}.
}
```

### D5 — Integrated absorptance

```math
\boxed{
\int A(f)\,df
=
\frac{2\gamma_e\gamma_a}
{\gamma_e+\gamma_a}.
}
```

At critical coupling,

```math
\boxed{\int A(f)\,df=\gamma_a.}
```

### D6 — Toy dark-event sensitivity-speed metric

For

```math
D=g_dV_a
```

and

```math
\mathcal C
=
\frac{h\nu\sqrt{B_{3\rm dB}}}{\mathrm{NEP}},
```

with a one-sided Poisson event-noise model,

```math
\boxed{
\mathcal C^2
=
\frac{4\gamma_a}{\pi D}
\frac{x^2}{(1+x)^3},
\qquad
x=\frac{\gamma_e}{\gamma_a}.
}
```

The optimum occurs at

```math
\boxed{x=2,}
```

so

```math
\boxed{
A_0=\frac89,
\qquad
B_{3\rm dB}=\frac{3\gamma_a}{2\pi},
\qquad
\mathcal C_{\max}^2
=
\frac{16\gamma_a}{27\pi D}.
}
```

This is a model result, not a universal detector optimum.

---

## 4. Derived result — active-volume counterexample

Canonical derivation:

`ACTIVE_VOLUME_COUNTEREXAMPLE.md`

Take an ideal parallel-plate capacitor filled by the active dielectric and scale

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

remains fixed while

```math
\boxed{V_a=Ad\propto s^2\to0.}
```

For fixed modal energy, capacitor voltage stays fixed and

```math
|E|^2\propto s^{-2}.
```

Therefore

```math
|E|^2V_a=\text{constant}.
```

The active dielectric participation stays finite, so for fixed loss tangent

```math
\boxed{
\gamma_a
=
\frac{\omega}{2}p_a\tan\delta
=\text{constant}.
}
```

Hence

```math
\boxed{
\frac{\gamma_a}{V_a}\to\infty.
}
```

### D7 — Consequence

Geometric active volume alone does **not** bound the absorptive modal decay rate in the ideal local linear continuum model when arbitrary ideal field concentration is allowed.

### D8 — Toy metric divergence under the same assumptions

If the separate dark-event assumption `D = g_d V_a` is retained while `gamma_a` stays fixed, then

```math
\boxed{
\mathcal C_{\max}^2\propto V_a^{-1},
\qquad
\mathcal C_{\max}\propto V_a^{-1/2}.
}
```

This divergence is a diagnostic that the combined continuum/noise assumptions break before `V_a -> 0`; it is not a prediction of infinite real detector performance.

---

## 5. Invalidated conjectures

### H1 — Bounded `gamma_a/V_a` from passivity alone

Earlier conjecture:

```text
passivity may force gamma_a / V_a to remain bounded as V_a -> 0
```

**Status: INVALIDATED under the ideal local-linear model with arbitrary lossless field concentration.**

The constant-capacitance shrinking-gap family is an explicit counterexample.

### H2 — Universal active-volume cancellation

Earlier conditional result:

```math
\gamma_a=\kappa V_a,
\qquad
D=g_dV_a
\Rightarrow
\mathcal C_{\max}^2
=\frac{16\kappa}{27\pi g_d}.
```

The algebra remains correct **when its premise holds**, but the premise `gamma_a proportional to V_a` is not general.

Therefore active-volume cancellation is not a universal passive detector law.

### H3 — Universal law of the form `eta^2 B <= C V_a`

No such active-volume-only law is supported by the current analysis.

Treat the earlier expression only as historical motivation, not an active conjecture.

---

## 6. Why prior per-volume optical bounds do not restore H1

The Miller-type material bound is referenced to the field in a specified background problem.

If an ideal lossless field concentrator is treated as part of that background, then the field at the active material can itself scale as the active region shrinks.

In the capacitor family,

```math
|E_{\rm bg}|^2\propto\frac{1}{V_a},
```

so

```math
V_a|E_{\rm bg}|^2
```

need not vanish.

Therefore a material-per-volume bound is not the same as an active-volume-only detector bound.

The full electromagnetic environment and allowed material resources matter.

---

## 7. Current open questions

### C1 — Microscopic absorber resource

What replaces geometric volume when the continuum dielectric description fails?

Candidate resources include:

- absorber number;
- total oscillator strength;
- transition dipole strength;
- single-photon saturation field;
- nonlocal/atomic length scales.

**Status:** primary open question.

### C2 — Thermodynamic resource

Can an ideal detector evade sensitivity/speed/dark-count tradeoffs by using irreversible, nonequilibrium internal states or amplification, and if so what free-energy/reset resource must be counted?

**Status:** open; directly relevant prior quantum-photodetector literature exists.

### C3 — Constrained electromagnetic bound

If the full passive concentrating structure, its materials, bounding region, and input channel are constrained, can a useful frequency-integrated optical bound be combined with detector noise?

**Status:** plausible but no exact detector statement selected.

### C4 — Equilibrium thermal bound

For a detector restricted to passive thermal equilibrium, detailed balance or fluctuation-dissipation may link absorptance to thermal excitation/dark events.

**Status:** promising restricted problem; not universal for driven nonequilibrium detectors.

---

## 8. Important prior-art collision

Young, Sarovar & Léonard, *Physical Review A* 97, 033836 (2018), DOI `10.1103/PhysRevA.97.033836`, developed a fully quantum photodetector model and showed that a detector architecture with rapid incoherent transfer from the optically active state to an optically dark monitored state can, in their idealized model, approach 100% efficiency, zero dark counts, and minimal jitter.

This is important for the present project because it argues strongly against assuming a universal quantum efficiency-dark-count-jitter tradeoff without specifying thermodynamic and architectural resources.

Their result does not address the exact active-volume question studied here, but it narrows the next target.

---

## 9. Explicit non-claims

Do not claim that:

- real detector performance diverges as active volume tends to zero;
- ideal lossless concentration exists at arbitrarily small physical scale;
- continuum `epsilon` and `tan delta` remain meaningful for a few microscopic absorbers;
- `D = g_d V_a` survives to the single-absorber limit;
- oscillator strength, detailed balance, nonlocality, or quantum backaction already yields a universal detector theorem here;
- any present detector-level result is novel.

---

## 10. Correction history retained

### C0.1 — Time-harmonic sign convention

Corrected during the one-port derivation before state promotion.

### C0.2 — Quality-factor rewrite

The correct relation is

```math
\boxed{B_{3\rm dB}=\frac{f_0}{2Q_L}.}
```

The earlier redundant `f_0/(4Q_L)` rewrite was incorrect and was removed.

---

## 11. Next promotion criterion

Do not promote a new bound until it survives:

1. explicit resource accounting;
2. a counterexample search including lossless concentration and nonequilibrium dark-state architectures;
3. microscopic normalization of optical coupling;
4. thermal/detailed-balance checks where equilibrium is assumed;
5. primary-source prior-art comparison.
