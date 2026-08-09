# Claim Ledger — Experiment 01

**Updated:** 2026-08-08  
**Status:** exploratory; naive volume and absorber-count bounds invalidated; harmonic passive-access theorem plus restricted optical/thermal corollaries derived; no novelty claim  
**Purpose:** distinguish prior theory, internal derivations, invalidated routes, conditional results, and explicit non-claims.

---

## 1. Active organizing question

The original question was

```math
V_a\to0,
\qquad
\eta\to1,
\qquad
B\to\infty,
\qquad
\mathrm{noise}\to0?
```

The surviving organizing concept is no longer geometric volume. It is

```text
optical access
+
irreversible detector/material access
+
thermodynamic cost of making that detector access effectively one-way.
```

---

## 2. Prior ingredients — never claim as repository novelty

Established ingredients include

- temporal coupled-mode theory and critical coupling;
- `H2` norms, Lyapunov Gramians, passive state-space systems;
- optical material-response / LDOS power-bandwidth bounds;
- deep-strong light-matter decoupling and Purcell-effect collapse;
- quantum dark-state detector architectures;
- reaction-coordinate / pseudomode treatment of structured reservoirs;
- Bose thermal photon bunching;
- thermodynamic upper bounds on sums of external optical coupling rates;
- multiresonant broadband absorption theory;
- local/KMS detailed balance for thermal reservoirs;
- Bode-Fano causal matching limits.

---

## 3. Invalidated general routes

### H1 — active volume

`ACTIVE_VOLUME_COUNTEREXAMPLE.md` gives an ideal passive continuum family with

```math
V_a\to0,
\qquad
\gamma_a=\text{constant},
\qquad
\gamma_a/V_a\to\infty.
```

Therefore the general statements

```text
passivity alone bounds gamma_a/V_a
```

and

```text
eta^2 B <= C V_a
```

are **STOPPED** unless new explicit constraints are added.

### H2 — finite absorber count / saturation

For one photon, a two-level absorber remains linear in the one-excitation sector.

Finite absorber count alone is **STOPPED** as the missing universal one-photon speed resource in the Markov/RWA model.

### H3 — largest internal multimode coupling

A spectator sector can carry arbitrarily large internal coupling without affecting the detector transfer block.

Any theorem based only on

```text
largest internal coupling anywhere -> infinity
```

is **STOPPED**.

---

## 4. Supporting one-port and thermal-channel results

### D1 — one-port modulation bandwidth

```math
\boxed{
B_{3\rm dB}
=\frac{\gamma_e+\gamma_a}{2\pi}.
}
```

At critical coupling,

```math
B_{3\rm dB}=\gamma_a/\pi.
```

### D2 — toy independent bulk-dark-event optimum

For the stated Poisson bulk-event model, the chosen sensitivity-speed metric is optimized at

```math
\gamma_e=2\gamma_a,
\qquad
A_0=8/9.
```

Not universal.

### D3 — one thermal optical channel

Exact Bose counting gives

```math
\boxed{
\mathcal C_{\rm th,max}^2
=\frac1{\pi\bar n(2+\bar n)}
}
```

at critical coupling.

This is a thermal input-background result, not an internal-dark-count theorem.

---

## 5. Microscopic weak- and strong-coupling supporting results

### D4 — conditional finite-transition LDOS ceiling

Finite bandwidth-averaged coupling is bounded when passive material response, admissible environment, finite signal bandwidth, and nonzero emitter-environment separation are fixed.

### D5 — finite-emitter regularization

Finite transition density removes the literal point-dipole ultraviolet divergence.

### D6 — oscillator-strength/extent insufficiency

Those inequalities alone do not close the perturbative problem before the formal enhanced rate reaches `O(omega_0)`, where the weak-coupling Markov/Purcell picture fails.

### D7 — symmetric deep-strong Hopfield narrowing

A resolved dressed transfer resonance may remain perfectly rate matched while its linewidth collapses as deep-strong coupling increases.

The mechanism is prior deep-strong decoupling physics.

### D8 — fixed-target Hopfield retuning theorem

Hold

```math
\omega_y=\omega_t>0
```

while retuning bare frequencies and taking `g -> infinity`.

For fixed local optical and detector reservoir resources,

```math
\boxed{
\min(\Gamma_L,\Gamma_R)\to0.
}
```

Peak transfer and linewidth cannot both stay bounded away from zero for the resolved target mode.

**Status:** candidate distinct supporting lemma; priority unproven.

### D9 — reservoir compensation cost

For target peak transfer `eta_*` and FWHM `W_*`, define

```math
\Gamma_*
=\frac{W_*}{4}
\left(1-\sqrt{1-\eta_*}\right).
```

Then the fixed-target two-mode model requires

```math
\boxed{
\max(\gamma_L,\gamma_R)
\ge
\Gamma_*
\sqrt{1+2g/\omega_t}.
}
```

This shows reservoir engineering is an additional resource; it is not forbidden.

---

## 6. Canonical passive multimode theorem

Canonical file: `PASSIVE_MULTIMODE_TRANSFER_AREA_BOUND.md`.

For a finite stable passive linear network with no direct `L -> R` feedthrough,

```math
A=-iH-(\Gamma_L+\Gamma_R+\Gamma_I),
\qquad
H=H^\dagger,
```

and

```math
L=\operatorname{Tr}\Gamma_L,
\qquad
R=\operatorname{Tr}\Gamma_R,
```

define

```math
\mathcal I_{L\to R}
=
\int_{-\infty}^{\infty}
\frac{d\omega}{2\pi}
\operatorname{Tr}[G_{RL}^\dagger G_{RL}].
```

### D10 — exact Gramian decomposition

In the controllability-Gramian eigenbasis,

```math
\boxed{
q_i
=\frac{\ell_i}{\ell_i+r_i+\iota_i}
}
```

and

```math
\boxed{
\frac{\mathcal I_{L\to R}}2
=
\sum_i
\frac{\ell_i r_i}{\ell_i+r_i+\iota_i}.
}
```

### D11 — exact harmonic access bound

```math
\boxed{
\mathcal I_{L\to R}
\le
\frac{2LR}{L+R}.
}
```

The earlier loose inequality `I <= 2 min(L,R)` is superseded.

The harmonic bound is tight; a single passive resonance saturates it.

### D12 — equality condition

Saturation requires no participating parasitic loss and

```math
\boxed{
\ell_i/r_i=L/R
}
```

for every transfer-active Gramian direction.

### D13 — fixed-band access floor

For target band width `W`,

```math
\boxed{
\overline T_B
\le
\frac{4\pi LR}{W(L+R)}.
}
```

Therefore `Tbar_B >= T_*` requires

```math
\boxed{
\frac{LR}{L+R}
\ge
\frac{T_*W}{4\pi}.
}
```

**Status:** exact internally derived detector-facing passivity corollary. Mathematical ingredients are prior theory. No novelty claim.

---

## 7. Direct-feedthrough audit

Canonical file: `DIRECT_FEEDTHROUGH_AND_BAND_LIMIT.md`.

### D14 — all-frequency theorem does not include ideal feedthrough

If

```math
G_{RL}=D_{RL}+G_{\rm res}
```

with nonzero frequency-independent `D_RL`, then the total all-frequency `H2` area diverges.

Thus the no-feedthrough assumption is genuinely load-bearing.

A pure prompt map

```math
G_{RL}=1
```

is an explicit passive Markov counterexample to any finite all-frequency theorem based only on internal `L,R` traces.

This does not imply physical infinite-bandwidth photodetection; the ideal feedthrough inserts that bandwidth by assumption.

### D15 — finite-band prompt + resonant accounting

For angular-frequency band width `W`,

```math
\boxed{
\sqrt{\mathcal I_B}
\le
\sqrt{\frac{W}{2\pi}}\,\|D_{RL}\|_F
+
\sqrt{\frac{2LR}{L+R}}.
}
```

The resonant excess `G_RL-D_RL` continues to obey the harmonic theorem.

---

## 8. Structured-reservoir audit

Canonical file: `STRUCTURED_RESERVOIR_ACCESS_AUDIT.md`.

### D16 — conditional continuum extension

For passive finite augmented realizations `G_n` with

```math
G_n\to G \quad\text{in }H2,
```

and finite limiting terminal access

```math
L_n\to L,
\qquad
R_n\to R,
```

one obtains

```math
\boxed{
\|G\|_{H2}^2
\le
\frac{2LR}{L+R}.
}
```

Thus structured spectral complexity alone does not evade the access theorem under finite passive embedding assumptions.

Possible escapes are direct/high-frequency feedthrough, divergent boundary access, failure of `H2` convergence, nonreducible residual strong coupling, or active/nonlinear/time-varying physics.

This is conditional, not a universal continuum theorem.

---

## 9. Thermodynamic optical-access bridge

Canonical file: `THERMODYNAMIC_OPTICAL_ACCESS_BRIDGE.md`.

Prior thermodynamic theory bounds the sum of **energy-decay** rates from optical modes in angular-frequency interval `W` into one free-space channel:

```math
\sum_m\gamma_{m,n}
\le
\frac{W}{2\pi}.
```

The repository uses amplitude-decay rates, so

```math
\boxed{
L_B\le\frac{W}{4\pi}.
}
```

Combining with D11 gives, under the restricted band/modal assumptions,

### D17 — one-channel detector-access requirement

```math
\boxed{
\overline T_B
\le
\frac{R_B}{R_B+W/(4\pi)}.
}
```

Hence achieving `Tbar_B >= eta` requires

```math
\boxed{
R_B
\ge
\frac{\eta}{1-\eta}
\frac{W}{4\pi}.
}
```

**Status:** restricted corollary with strong prior-art overlap. Thermodynamic external-coupling bounds and radiative/internal rate matching are established theory.

---

## 10. Thermal irreversibility result

Canonical file: `THERMAL_IRREVERSIBILITY_COST.md`.

Model a detector localization transition

```text
|e> -> |d>
```

with energy release

```math
\Delta=E_e-E_d>0
```

into a thermal bath at temperature `T`.

Local detailed balance gives

```math
\boxed{
\frac{k_\uparrow}{k_\downarrow}
=e^{-\Delta/(k_BT)}.
}
```

Using the minimal convention

```math
k_\downarrow=2R_B,
```

and D17 yields

### D18 — minimum forward localization rate

```math
\boxed{
k_\downarrow
\ge
\frac{\eta}{1-\eta}
\frac{W}{2\pi}.
}
```

### D19 — minimum reverse thermal-activation rate at fixed bias

```math
\boxed{
k_\uparrow
\ge
\frac{\eta}{1-\eta}
\frac{W}{2\pi}
\exp[-\Delta/(k_BT)].
}
```

### D20 — minimum energy bias for fixed reverse-activation budget

If

```math
k_\uparrow\le D_{\rm rev},
```

then, when the logarithm argument exceeds unity,

```math
\boxed{
\Delta
\ge
k_BT
\ln\!\left[
\frac{\eta W}
{2\pi(1-\eta)D_{\rm rev}}
\right].
}
```

`D_rev` is a reverse thermal-activation budget, **not automatically an observable dark-count rate**.

---

## 11. Explicit non-claims

Do not claim that

- active volume fundamentally limits detector bandwidth;
- finite absorber number fundamentally limits one-photon speed;
- the Hopfield fixed-target theorem is universal or novel;
- the harmonic access theorem is novel;
- direct feedthrough is impossible;
- every structured reservoir satisfies the finite-embedding assumptions;
- D17 is universal beyond its one-free-space-channel/modal setting;
- `D_rev` equals detector dark counts;
- a minimum reset work has been derived;
- the project has a universal sensitivity-speed-dark-count theorem;
- the project is ready for a manuscript.

---

## 12. Current frontier

Build the complete minimal detector cycle

```text
|g> -- photon --> |e>
|e> <-> |d>       thermal detector bath
|d> -- readout/reset --> |g>.
```

The next result must explicitly define

1. what transition produces a recorded count;
2. false-count pathways without an input photon;
3. reset dynamics and work/reservoir resource;
4. dead time and steady-state count statistics;
5. how optical access `L`, detector access `R`, bandwidth, efficiency, and observable dark counts fit into one consistent cycle.

Only then reassess whether a detector-specific paper has emerged.