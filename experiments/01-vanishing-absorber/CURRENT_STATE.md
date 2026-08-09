# Current State — Experiment 01: The Vanishing Absorber

**Date:** 2026-08-08  
**Status:** exploratory; several naive universal bounds falsified; exact passive multimode harmonic access bound derived; no novelty claim  

## 1. Guiding question

Can an ideal photodetector be made arbitrarily small, arbitrarily fast, arbitrarily sensitive, and still absorb essentially every incident photon?

The project does not assume that these goals are fundamentally incompatible.

The research has progressively moved away from geometric active volume toward a more durable requirement:

```text
useful optical access
+
irreversible detector/material access.
```

A detector needs both.

---

## 2. Canonical frontier

Read after root `AGENTS.md`:

1. `PASSIVE_MULTIMODE_TRANSFER_AREA_BOUND.md`
2. `HOPFIELD_RESERVOIR_RESOURCE_COST.md`
3. `MULTIMODE_ESCAPE_AUDIT.md`
4. `HOPFIELD_RETUNING_NO_GO.md`
5. `HOPFIELD_RETUNING_PRIOR_ART_SWEEP.md`
6. older supporting stages only as needed for provenance.

`CLAIM_LEDGER.md` is the epistemic boundary.

---

## 3. Earlier routes that failed

### Active volume

A shrinking ideal dielectric capacitor can keep finite optical participation and finite absorptive decay while

```math
V_a\to0,
\qquad
\gamma_a/V_a\to\infty.
```

Therefore passivity alone does not support a universal active-volume law such as

```text
eta^2 B <= C V_a.
```

### Finite absorber number

For one incident photon, a two-level transition remains linear in the one-excitation sector. Finite absorber number / saturation alone therefore does not impose a one-photon speed ceiling in the Markov/RWA model.

### Weak-coupling oscillator-strength route

Finite transition extent regularizes the literal point-dipole divergence, but oscillator-strength and extent inequalities alone do not close the problem before the enhanced decay estimate reaches

```math
\Gamma/\omega_0=O(1),
```

where weak-coupling Purcell-rate theory ceases to be controlled.

These failures forced the analysis into nonperturbative light-matter coupling and then general passive-network theory.

---

## 4. Restricted thermal-channel result retained

For one thermal optical input channel, exact Bose counting including bunching gives

```math
\boxed{
\mathcal C_{\rm th,max}^2
=
\frac1{\pi\bar n(2+\bar n)}
}
```

at critical coupling, with

```math
\mathcal C_{\rm th}
=\frac{h\nu\sqrt{B_{3\rm dB}}}
{\mathrm{NEP}_{\rm th}}.
```

This is a one-channel thermal-background relation, not an internal-dark-count theorem.

---

## 5. Fixed-target Hopfield result

For a TRK-consistent two-mode Hopfield system, keep the lower polariton at

```math
\omega_y=\omega_t>0
```

while allowing bare-frequency retuning and sending the internal light-matter coupling

```math
g\to\infty.
```

For fixed positive local optical and detector reservoir scales,

```math
\boxed{
\min(\Gamma_L,\Gamma_R)\to0.
}
```

Thus for a resolved transfer resonance, peak transfer and linewidth cannot both remain bounded away from zero.

A focused search found extensive deep-strong decoupling prior art but no inspected source stating this exact fixed-target two-reservoir retuning theorem.

Current status:

> **candidate distinct supporting lemma; priority unproven.**

No novelty language is permitted.

---

## 6. Scaling the reservoirs has an explicit cost

Require

```math
T_0\ge\eta_*>0,
\qquad
\Delta\omega_{\rm FWHM}\ge W_*>0.
```

Then each dressed access rate must exceed

```math
\boxed{
\Gamma_*
=
\frac{W_*}{4}
\left(1-\sqrt{1-\eta_*}\right).
}
```

Optimizing over all fixed-target bare-frequency retunings yields

```math
\boxed{
\max(\gamma_L,\gamma_R)
\ge
\Gamma_*
\sqrt{1+2g/\omega_t}.
}
```

Hence in deep strong coupling a reservoir-engineering escape requires at least one bare access resource to grow as

```math
\sqrt{g/\omega_t}.
```

The symmetric retuning family asymptotically saturates that scaling.

This does not forbid strong reservoir engineering. It shows that it is a new resource and eventually exits the weak-bath model.

---

## 7. Multimode attack

Two multimode lessons are already secure.

1. A theorem based only on the largest internal coupling anywhere in a multimode Hamiltonian is false because a disconnected spectator sector can carry the divergent coupling.
2. A growing bank of individually narrow resonances can tile a fixed band if useful mode count/density also grows.

Thus mode count/density is a genuine resource.

However, mode proliferation does **not** defeat the aggregate access accounting below.

---

## 8. Exact passive multimode harmonic access theorem

Consider an arbitrary finite stable passive linear network

```math
\dot{\mathbf a}
=
A\mathbf a+B_L\mathbf s_L,
```

with

```math
A
=-iH-(\Gamma_L+\Gamma_R+\Gamma_I),
\qquad
H=H^\dagger,
```

and

```math
B_LB_L^\dagger=2\Gamma_L,
\qquad
C_R^\dagger C_R=2\Gamma_R.
```

The detector output is

```math
\mathbf y_R=C_R\mathbf a,
```

and there is no direct `L -> R` feedthrough.

Define

```math
G_{RL}(s)=C_R(sI-A)^{-1}B_L
```

and the full frequency-integrated transfer

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

Let

```math
L=\operatorname{Tr}\Gamma_L,
\qquad
R=\operatorname{Tr}\Gamma_R.
```

The exact theorem is

```math
\boxed{
\mathcal I_{L\to R}
\le
\frac{2LR}{L+R}.
}
```

The right side is the harmonic mean of the total optical and detector access budgets.

This supersedes the earlier looser inequality

```math
\mathcal I_{L\to R}
\le2\min(L,R).
```

---

## 9. Why the harmonic bound is exact

Let `Q_L` be the controllability Gramian:

```math
AQ_L+Q_LA^\dagger+2\Gamma_L=0.
```

Diagonalize `Q_L`. In that basis define diagonal nonnegative rates

```math
\ell_i,
\qquad
r_i,
\qquad
\iota_i
```

from `Gamma_L`, `Gamma_R`, and parasitic `Gamma_I`.

The diagonal of the commutator `[H,Q_L]` vanishes identically, so the Lyapunov equation gives

```math
\boxed{
q_i
=\frac{\ell_i}
{\ell_i+r_i+\iota_i}.
}
```

Therefore

```math
\boxed{
\frac{\mathcal I_{L\to R}}2
=
\sum_i
\frac{\ell_i r_i}
{\ell_i+r_i+\iota_i}.
}
```

Dropping parasitic loss can only increase the expression. Cauchy-Schwarz then gives

```math
\sum_i
\frac{\ell_i r_i}
{\ell_i+r_i}
\le
\frac{LR}{L+R},
```

which closes the theorem.

A single passive resonance saturates the harmonic bound exactly.

Equality in the multimode case requires no participating parasitic loss and the same optical-to-detector access ratio in every transfer-active Gramian direction:

```math
\frac{\ell_i}{r_i}
=\frac{L}{R}.
```

Thus the theorem is the aggregate multimode analogue of rate matching / critical coupling.

---

## 10. Fixed-band resource floor

For a target angular-frequency band of width `W`, define

```math
\overline T_B
=
\frac1W
\int_B
\operatorname{Tr}(G_{RL}^\dagger G_{RL})\,d\omega.
```

Then

```math
\boxed{
\overline T_B
\le
\frac{4\pi LR}
{W(L+R)}.
}
```

Demanding

```math
\overline T_B\ge T_*
```

requires

```math
\boxed{
\frac{LR}{L+R}
\ge
\frac{T_*W}{4\pi}.
}
```

For matched total access budgets

```math
L=R=\Gamma_{\rm access},
```

this becomes

```math
\boxed{
\Gamma_{\rm access}
\ge
\frac{T_*W}{2\pi}.
}
```

This is not an absolute bandwidth limit. It is an external-access resource requirement.

---

## 11. What the multimode theorem does and does not say

It **does** allow

- arbitrary finite mode count;
- overlapping resonances;
- internal interference;
- bright/dark combinations;
- arbitrary finite Hermitian internal coupling;
- passive parasitic loss;
- nonreciprocal phase structure compatible with passive Hermitian dynamics.

At fixed `L` and `R`, those internal changes can redistribute transfer in frequency but cannot increase the full transfer area beyond the harmonic bound.

It does **not** cover

- direct `L -> R` feedthrough/bypass;
- active gain;
- explicit time variation;
- nonlinear/saturating dynamics;
- genuinely infinite-dimensional non-Markovian reservoirs without a finite passive realization;
- strong boundary coupling if the local Markov damping representation itself fails.

Finite structured reservoirs that can be promoted into additional internal reaction-coordinate/pseudomode degrees of freedom remain compatible with the theorem once their residual boundary access is counted.

---

## 12. Verification

`numerics/passive_multimode_h2_stress.py` now tests

- `0 <= Q_L <= I`;
- the exact Gramian-basis identity for `q_i`;
- the harmonic transfer-area bound;
- single-mode saturation of the bound;
- direct numerical frequency integration of a representative multimode transfer spectrum.

A private 4,000-network stress test across `N=1,2,4,8` found no violation; the Gramian-basis identity agreed to roughly `3e-15` in the sampled cases.

No CI workflow is justified yet.

---

## 13. Prior-art boundary

The proof uses standard systems-theory ingredients:

- `H_2` norms;
- Lyapunov Gramians;
- scattering-passive linear systems;
- passive state-space energy balance.

Contemporary multiresonant optical theory also derives broadband absorption/emission bounds using modal density, quasinormal modes, and decay-rate resources.

An initial targeted search has not located this exact **harmonic two-access trace inequality** stated as an optical-to-detector transfer-area theorem.

That negative search is not evidence of novelty.

Current posture:

> **exact internally derived detector-facing passivity corollary; priority unassessed; no novelty claim.**

---

## 14. Current interpretation

The thought experiment has now reached a substantially more general form:

> **Internal electromagnetic complexity can reshape useful detector transfer, but in a finite passive linear network it cannot replace simultaneous access to the optical input and irreversible detector reservoirs. The full frequency-integrated transfer is bounded by the harmonic mean of their aggregate access budgets.**

The two-mode Hopfield result explains one mechanism by which access can collapse at extreme internal coupling. The multimode theorem shows that arbitrary finite internal complexity cannot evade the aggregate access accounting.

---

## 15. Next decisive tests

1. search systems/network/scattering literature specifically for the harmonic trace inequality;
2. test finite-band direct feedthrough and whether it admits a clean additive resource accounting;
3. test genuinely infinite-dimensional and strongly structured passive reservoirs;
4. map `L` and `R` onto microscopic semiconductor optical-coupling and irreversible-relaxation resources;
5. then reintroduce dark-event, thermal reverse-rate, amplification, and reset thermodynamics;
6. only after these attacks decide whether a manuscript is scientifically justified.

Do not return to HgCdTe-specific transport yet.