# Current State — Experiment 01: The Vanishing Absorber

**Date:** 2026-08-08  
**Status:** exploratory; several naive universal bounds falsified; finite-passive-network transfer-area bound derived; novelty unproven  

## 1. Guiding question

Can an ideal photodetector be made arbitrarily small, arbitrarily fast, arbitrarily sensitive, and still absorb essentially every incident photon?

The project does **not** assume the answer is no.

The useful structure has emerged by repeatedly trying to defeat each apparent tradeoff. The cost has either disappeared entirely or migrated into a deeper physical resource.

The present frontier is no longer geometric detector volume. It is **external access**:

```text
useful optical access
+
irreversible detector/material access.
```

A detector needs both.

---

## 2. Canonical reading order

After root `AGENTS.md`, read:

1. `PASSIVE_MULTIMODE_TRANSFER_AREA_BOUND.md`
2. `HOPFIELD_RESERVOIR_RESOURCE_COST.md`
3. `MULTIMODE_ESCAPE_AUDIT.md`
4. `HOPFIELD_RETUNING_NO_GO.md`
5. `HOPFIELD_RETUNING_PRIOR_ART_SWEEP.md`
6. `NONPERTURBATIVE_HOPFIELD_CAPTURE.md`
7. `OSCILLATOR_STRENGTH_EXTENT_STRESS_TEST.md`
8. `FINITE_EMITTER_FORM_FACTOR.md`
9. `FINITE_TRANSITION_LDOS_BANDWIDTH_BOUND.md`
10. `MICROSCOPIC_SINGLE_TRANSITION.md`
11. `THERMAL_INPUT_CHANNEL.md`
12. `ACTIVE_VOLUME_COUNTEREXAMPLE.md`
13. `ONE_PORT_RESONATOR_DYNAMICS.md`

`CLAIM_LEDGER.md` defines what may currently be claimed.

---

## 3. What failed on the way here

### Geometric active volume

A shrinking lossy capacitor can maintain finite electromagnetic participation and finite absorptive decay while

```math
V_a\to0,
\qquad
\gamma_a/V_a\to\infty.
```

Therefore active volume alone is not a fundamental passive optical resource.

The schematic target

```text
eta^2 B <= C V_a
```

is stopped as a general claim.

### Finite absorber number / two-level saturation

For one incident photon, a two-level transition remains linear in the one-excitation sector. With an irreversible detection channel,

```math
A_d(\omega)
=
\frac{4\gamma_o\gamma_d}
{(\omega-\omega_0)^2+(\gamma_o+\gamma_d)^2},
```

so finite absorber number alone does not create a one-photon speed ceiling.

### Finite oscillator strength and emitter extent

Finite transition extent regularizes the literal point-dipole ultraviolet divergence, but oscillator-strength and extent inequalities alone do not close the weak-coupling problem. Their optimistic perturbative envelope can reach

```math
\Gamma/\omega_0=O(1),
```

where the fixed-transition Markov/Purcell picture ceases to be controlled.

This forced the analysis into nonperturbative light-matter coupling rather than an arbitrary cutoff.

---

## 4. Restricted thermal input-channel result

For one thermal optical input channel, exact Bose counting including bunching gives

```math
\boxed{
\mathcal C_{\rm th,max}^2
=
\frac{1}
{\pi\bar n(2+\bar n)}
}
```

at critical coupling, where

```math
\mathcal C_{\rm th}
=\frac{h\nu\sqrt{B_{3\rm dB}}}
{\mathrm{NEP}_{\rm th}}.
```

The absorber rate, cavity `Q`, and active volume cancel from this **one-channel thermal-background** relation.

This is not an internal-dark-count theorem.

---

## 5. Nonperturbative two-mode Hopfield result

For a TRK-consistent symmetric two-mode Hopfield system,

```math
\omega_\pm
=\sqrt{\omega_0^2+g^2}\pm g.
```

With equal weak local optical and detector bath scales,

```math
\boxed{
\Gamma_{\pm,L}
=\Gamma_{\pm,R}
=\frac{\gamma}
{2\sqrt{1+(g/\omega_0)^2}}.
}
```

Thus a resolved polariton may retain unit **peak** transfer while its transfer linewidth collapses as

```math
\boxed{
\Delta\omega_{\rm FWHM}
\sim
2\gamma\frac{\omega_0}{g}
}
```

for fixed bare frequencies.

This is consistent with established deep-strong light-matter decoupling / breakdown-of-Purcell physics and is not itself a novelty claim.

---

## 6. Fixed-target Hopfield retuning theorem

Allow the bare photonic and material frequencies to vary with `g`, but hold the useful lower polariton at

```math
\boxed{\omega_y=\omega_t>0.}
```

The exact fixed-target branch obeys

```math
\boxed{
(\omega_c^2-\omega_t^2)
(\omega_b^2-\omega_t^2)
=
4g^2\frac{\omega_c}{\omega_b}\omega_t^2.
}
```

With fixed positive local optical and detector reservoir scales `gamma_L`, `gamma_R`, the dressed lower-polariton rates satisfy

```math
\boxed{
\min(\Gamma_L,\Gamma_R)\to0
\qquad
(g\to\infty,\ \omega_y=\omega_t).
}
```

For a resolved transfer pole,

```math
T_0
=\frac{4\Gamma_L\Gamma_R}
{(\Gamma_L+\Gamma_R)^2},
```

```math
\Delta\omega_{\rm FWHM}
=2(\Gamma_L+\Gamma_R).
```

Therefore peak transfer and linewidth cannot both remain bounded away from zero in the fixed-target infinite-internal-coupling limit **for fixed local bath resources**.

Current prior-art status:

> **candidate distinct supporting lemma; priority unproven.**

Do not call it new, first, fundamental, or universal.

---

## 7. Reservoir-engineering escape has a quantitative cost

`HOPFIELD_RESERVOIR_RESOURCE_COST.md` asks how strongly the bare optical/detector reservoirs must be scaled to defeat the fixed-bath theorem.

Require

```math
T_0\ge\eta_*>0,
\qquad
\Delta\omega_{\rm FWHM}\ge W_*>0.
```

These requirements imply the exact dressed-rate floor

```math
\boxed{
\min(\Gamma_L,\Gamma_R)
\ge
\Gamma_*
}
```

with

```math
\boxed{
\Gamma_*
=
\frac{W_*}{4}
\left(1-\sqrt{1-\eta_*}\right).
}
```

Optimizing over every allowed fixed-target bare-frequency retuning gives

```math
\boxed{
\max(\gamma_L,\gamma_R)
\ge
\Gamma_*
\sqrt{1+2g/\omega_t}.
}
```

Hence, for

```math
g\gg\omega_t,
```

at least one bare external reservoir coupling must grow as

```math
\boxed{
\max(\gamma_L,\gamma_R)
\gtrsim
\Gamma_*
\sqrt{2g/\omega_t}.
}
```

The symmetric retuning family asymptotically saturates this `sqrt(g)` scaling.

Thus `"just increase the external coupling"` is a legitimate escape only by spending an unbounded external-access resource. Eventually that escape also leaves the weak-reservoir/Markov regime assumed by the theorem.

---

## 8. Multimode attack: mode count is a real resource

A naive theorem based only on the **largest internal coupling anywhere in a multimode system** is false: a disconnected spectator sector can carry `g -> infinity` while the useful detector block remains unchanged.

A growing bank of individually narrow matched resonances can also tile a fixed band. In the sparse independent-resonance limit,

```math
\int\frac{d\omega}{2\pi}T_j(\omega)
=\Gamma_j
```

for a matched resonance with rate `Gamma_j`.

Therefore preserving finite integrated response while every useful linewidth scale tends to zero requires a growing number/density of useful modes, schematically

```math
N(g)\Gamma(g)=O(1).
```

Mode proliferation is therefore a genuine resource, not a free loophole.

Recent multiresonant absorption theory independently treats spectral mode density and decay rates as broadband-response resources.

---

## 9. New finite-passive-network transfer-area theorem

The sparse-resonance approximation is no longer necessary.

Consider an arbitrary finite stable passive linear network

```math
\dot{\mathbf a}
=
\left[-iH-(\Gamma_L+\Gamma_R+\Gamma_I)\right]\mathbf a
+B_L\mathbf s_L,
```

with

```math
H=H^\dagger,
```

```math
B_LB_L^\dagger=2\Gamma_L,
```

and detector output

```math
\mathbf y_R=C_R\mathbf a,
\qquad
C_R^\dagger C_R=2\Gamma_R.
```

No direct left-to-detector feedthrough is included.

Define

```math
G_{RL}(s)
=C_R(sI-A)^{-1}B_L
```

and the full frequency-integrated transfer area

```math
\boxed{
\mathcal I_{L\to R}
=
\int_{-\infty}^{\infty}
\frac{d\omega}{2\pi}
\operatorname{Tr}
\left[
G_{RL}^\dagger(i\omega)
G_{RL}(i\omega)
\right].
}
```

The controllability Gramian `Q_L` obeys

```math
AQ_L+Q_LA^\dagger+2\Gamma_L=0.
```

Passivity gives the exact operator inequality

```math
\boxed{0\preceq Q_L\preceq I.}
```

Therefore

```math
\mathcal I_{L\to R}
=2\operatorname{Tr}(\Gamma_RQ_L)
\le2\operatorname{Tr}\Gamma_R.
```

The dual observability argument gives

```math
\mathcal I_{L\to R}
\le2\operatorname{Tr}\Gamma_L.
```

Hence

```math
\boxed{
\mathcal I_{L\to R}
\le
2\min\!\left(
\operatorname{Tr}\Gamma_L,
\operatorname{Tr}\Gamma_R
\right).
}
```

This result handles arbitrary finite mode count, coherent internal couplings, overlapping resonances, and internal interference inside the stated passive Markov/LTI class.

It does **not** say modes cannot reshape or broaden the response. It says they cannot create unlimited integrated useful transfer at fixed total boundary-access budgets.

Mathematically this is an `H_2`/Lyapunov passivity corollary. Those ingredients are standard systems theory. The exact detector-facing inequality is **not currently claimed as novel**.

---

## 10. Fixed-band external-access floor

For a target angular-frequency band of width `W`, define

```math
\overline T_B
=
\frac1W
\int_B
\operatorname{Tr}
\left[
G_{RL}^\dagger G_{RL}
\right]d\omega.
```

The transfer-area theorem gives

```math
\boxed{
\overline T_B
\le
\frac{4\pi}{W}
\min\!\left(
\operatorname{Tr}\Gamma_L,
\operatorname{Tr}\Gamma_R
\right).
}
```

Therefore maintaining

```math
\overline T_B\ge T_*>0
```

requires

```math
\boxed{
\min\!\left(
\operatorname{Tr}\Gamma_L,
\operatorname{Tr}\Gamma_R
\right)
\ge
\frac{T_*W}{4\pi}.
}
```

This is not an absolute detector bandwidth limit.

It is an **external-access resource law**: broadband efficient transfer requires sufficient aggregate access on both the optical and irreversible detector sides.

---

## 11. Verification state

The passive multimode theorem has two levels of checking:

1. exact Lyapunov/Gramian proof in `PASSIVE_MULTIMODE_TRANSFER_AREA_BOUND.md`;
2. deterministic random-network regression in `numerics/passive_multimode_h2_stress.py`, including direct numerical frequency integration for a representative multimode network.

The regression checks

```math
0\preceq Q_L\preceq I
```

and

```math
\mathcal I_{L\to R}
\le
2\min(\operatorname{Tr}\Gamma_L,\operatorname{Tr}\Gamma_R).
```

No continuous-integration workflow is justified yet.

---

## 12. Prior-art boundary

Established prior theory already includes

- `H_2` transfer norms and Lyapunov Gramians;
- scattering-passive linear systems;
- Maxwell equations formulated as scattering-passive systems;
- passive quantum linear-system realizations;
- broadband absorption/emission bounds for many coupled resonances;
- deep-strong and multimode light-matter decoupling.

A targeted initial search has not identified the exact two-access trace inequality above stated as a photodetector transfer-area bound.

That is a **negative search result only**.

The result should currently be treated as a detector-facing consequence of established systems mathematics, not as a priority claim.

---

## 13. What remains outside the theorem

The finite passive transfer-area theorem does not cover

- direct optical-to-detector feedthrough/bypass not counted in `Gamma_L`, `Gamma_R`;
- active gain;
- explicit time variation;
- nonlinear/saturating dynamics;
- genuinely infinite-dimensional non-Markovian reservoirs without a finite passive realization;
- a complete microscopic mapping from `Tr Gamma` to semiconductor material resources;
- detector dark-count/thermal/reset thermodynamics.

Structured reservoirs that can be represented by promoting a finite number of reaction-coordinate/pseudomode degrees of freedom into the internal network remain compatible with the theorem once the residual boundary access is counted.

---

## 14. Current interpretation

The original thought experiment has changed form.

The strongest surviving statement is no longer

```text
small absorber -> unavoidable bandwidth penalty.
```

It is closer to

```text
internal electromagnetic sophistication cannot replace
both optical access and irreversible detector access.
```

For the finite passive linear class,

```math
\boxed{
\text{frequency-integrated useful transfer}
\le
2\times
\text{the smaller total external-access budget}.
}
```

The two-mode deep-strong result supplies one mechanism by which access disappears; the multimode theorem shows that adding finite internal complexity cannot evade the aggregate access accounting.

---

## 15. Next decisive questions

The research should now test the access theorem rather than return to active volume.

1. **Tightness:** can the two-sided trace bound be sharpened without adding assumptions?
2. **Direct paths:** how should finite-band feedthrough/bypass access be counted?
3. **Infinite/structured reservoirs:** does a useful extension survive continuum or strongly non-Markovian baths?
4. **Microscopic detector mapping:** what semiconductor quantities determine the optical and irreversible access budgets?
5. **Thermodynamics/noise:** how do dark events, thermal reverse rates, amplification, and reset cost constrain useful access?
6. **Prior art:** perform a broader passive-network/scattering search before considering any manuscript.

Do **not** add HgCdTe-specific transport until the general access-resource structure survives these attacks.