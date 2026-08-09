# Claim Ledger — Experiment 01

**Updated:** 2026-08-08  
**Status:** exploratory; one-resonance model derived  
**Purpose:** keep known inputs, derivations, conjectures, and invalidated ideas from being conflated.

---

## 1. Active question

Can an ideal photodetector simultaneously approach

```math
V\to0,
\qquad
\eta_{\rm abs}\to1,
\qquad
B\to\infty,
\qquad
\mathrm{intrinsic\ noise}\to0?
```

The project does not assume these limits are incompatible.

---

## 2. Known or model-defining ingredients

### K1 — Bulk event-rate scaling

For a uniform volumetric dark-generation event-rate density `g_d`,

```math
\Gamma_d=g_dV.
```

This is an extensivity assumption/model definition, not a new result.

### K2 — Temporal coupled-mode framework

A passive linear one-port resonance can be represented by a single complex mode amplitude coupled to one external channel and one internal absorptive channel.

This is established resonator theory.

### K3 — Critical coupling

Unity monochromatic absorption in the one-port model occurs when external leakage equals internal absorption loss.

This is established resonator physics, rederived here to lock conventions.

### K4 — Optical confinement can separate collection area from active material volume

Resonators, antennas, gratings, photon trapping, slow-light structures, etc. can increase optical interaction with a small absorber.

This is established photonic engineering, not a novelty claim.

---

## 3. Derived results within the one-resonance model

Canonical derivation:

`ONE_PORT_RESONATOR_DYNAMICS.md`

### D1 — Exact absorptance

With external amplitude-decay rate `gamma_e`, absorptive amplitude-decay rate `gamma_a`, and detuning `Delta = omega - omega_0`,

```math
\boxed{
A(\omega)=
\frac{4\gamma_e\gamma_a}
{\Delta^2+(\gamma_e+\gamma_a)^2}.
}
```

### D2 — Critical-coupling condition

```math
\boxed{\gamma_e=\gamma_a}
```

gives `A(omega_0)=1`.

### D3 — Energy lifetime and quality factor

With `Gamma = gamma_e + gamma_a`,

```math
\boxed{
\tau_U=\frac{1}{2\Gamma},
\qquad
Q_L=\frac{\omega_0}{2\Gamma}.
}
```

### D4 — Small-signal absorbed-power modulation response

For a resonant optical carrier,

```math
\boxed{
H_{\rm abs}(\Omega)
=
\frac{\Gamma}{\Gamma+i\Omega}.
}
```

Therefore

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

**Interpretation:** in this architecture, maintaining unity absorption while `gamma_a -> 0` forces the absorbed-power modulation bandwidth to zero.

### D5 — Optical linewidth versus modulation bandwidth

At critical coupling,

```math
\boxed{
\Delta f_{\rm abs,FWHM}=2B_{3\rm dB}^{\rm crit}.
}
```

Equivalently,

```math
B_{3\rm dB}=\frac{f_0}{2Q_L},
\qquad
\Delta f_{\rm abs,FWHM}=\frac{f_0}{Q_L}.
```

### D6 — Integrated absorptance

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
\boxed{
\int A(f)\,df=\gamma_a.
}
```

### D7 — Weak-loss material-overlap expression

For weak dielectric loss,

```math
\boxed{
\gamma_a
=
\frac{\omega\epsilon_0}{4U}
\int_{V_a}
\epsilon''|\mathbf E|^2\,dV.
}
```

This is a standard perturbative material-loss relation used here to expose the dependence on active-material participation.

### D8 — Toy sensitivity-speed metric

Under the minimal Poisson bulk-dark-event model,

```math
D=g_dV,
```

```math
\mathrm{NEP}^2
=
\frac{2(h\nu)^2D}{A_0^2},
```

and defining

```math
\mathcal C
=
\frac{h\nu\sqrt{B_{3\rm dB}}}{\mathrm{NEP}},
```

with

```math
x=\frac{\gamma_e}{\gamma_a},
```

gives

```math
\boxed{
\mathcal C^2
=
\frac{4\gamma_a}{\pi D}
\frac{x^2}{(1+x)^3}.
}
```

### D9 — Optimum coupling for this specific metric

The nonzero maximum occurs at

```math
\boxed{x=2.}
```

Thus

```math
\boxed{
\gamma_e=2\gamma_a,
\qquad
A_0=\frac89,
\qquad
B_{3\rm dB}=\frac{3\gamma_a}{2\pi}.
}
```

and

```math
\boxed{
\mathcal C_{\max}^2
=
\frac{16\gamma_a}{27\pi D}.
}
```

This improves `C` by approximately `8.9%` relative to exact critical coupling.

This is not claimed as a universal detector optimum.

### D10 — Conditional volume cancellation

If, over a regular scaling regime,

```math
\gamma_a=\kappa V
```

and

```math
D=g_dV,
```

then

```math
\boxed{
\mathcal C_{\max}^2
=
\frac{16\kappa}{27\pi g_d},
}
```

so `V` cancels.

The cancellation is a derived **conditional toy-model result**, not a universal bound.

---

## 4. Verification state

### V1 — Modulation response

Direct time-domain integration of the resonant cavity-envelope equation agrees with

```math
|H_{\rm abs}|
=
\frac{\Gamma}{\sqrt{\Gamma^2+\Omega^2}}
```

at representative frequencies to better than roughly `4e-4` absolute amplitude in the initial check.

### V2 — Coupling optimization

A numerical scan recovers the optimum near

```text
gamma_e/gamma_a = 2.00003
```

with

```text
A_0 ~= 0.888884,
```

consistent with `2` and `8/9`.

A dedicated repository regression script has not yet been promoted to canonical infrastructure.

---

## 5. Active conjectures / open questions

### C1 — Bounded active-loss rate per active volume

There may exist physically meaningful conditions under which

```math
\frac{\gamma_a}{V}
```

cannot diverge as `V -> 0` for passive local materials coupled to a specified incident channel.

**Status:** open; now the primary theoretical target.

### C2 — General passive material-response bound

A frequency-integrated electromagnetic bound may constrain absorption strength or active loss rate in terms of material susceptibility and absorber amount.

**Status:** plausible from known classes of optical bounds; exact statement not yet selected.

### C3 — Detector-level geometry-independent sensitivity-speed bound

If C1/C2 yields a rigorous optical/material constraint and the relevant intrinsic fluctuation rate remains extensive in the same active material, a detector-level bound may result after eliminating active volume.

**Status:** speculative.

---

## 6. Explicitly unestablished statements

Do not present any of the following as results:

- `gamma_a proportional to V` for arbitrary field-concentrating structures;
- bounded `gamma_a/V` without a proof and explicit material/input-channel assumptions;
- `eta^2 B <= C V` as a universal law;
- `sqrt(B)/NEP <= constant` as a universal detector bound;
- optimality of a single resonance;
- the claim that passive nanophotonics cannot improve every sensible detector figure of merit simultaneously;
- the claim that cavity photon lifetime always sets total detector bandwidth;
- the claim that active volume alone determines dark current or NEP in real detectors;
- any claim of novelty or priority.

---

## 7. Correction history

### H1 — Time-harmonic sign convention

The first draft of the one-port derivation combined an `exp(-i omega t)` drive with the opposite sign convention in the resonant-frequency term of the amplitude equation.

It was corrected before the result was promoted into `CURRENT_STATE.md`.

### H2 — Redundant quality-factor rewrite

The first draft correctly derived

```math
B_{3\rm dB}=\frac{\Gamma}{2\pi}
```

but incorrectly rewrote it as `f_0/(4Q_L)`.

Given

```math
Q_L=\frac{\omega_0}{2\Gamma},
```

the correct relation is

```math
\boxed{
B_{3\rm dB}=\frac{f_0}{2Q_L}.
}
```

The decay-rate result and optimized-coupling result were unaffected.

---

## 8. Promotion criteria remain unchanged

A conjecture can move to **derived result** only after:

1. assumptions are explicit;
2. normalization and bandwidth conventions are explicit;
3. units and limiting cases pass;
4. the derivation is internally checked;
5. obvious counterexamples are tested.

A result can move to **publication claim candidate** only after, additionally:

6. an independent derivation or numerical falsification test where feasible;
7. focused primary-source prior-art comparison;
8. explicit statement of architectures/regimes outside the claim.
