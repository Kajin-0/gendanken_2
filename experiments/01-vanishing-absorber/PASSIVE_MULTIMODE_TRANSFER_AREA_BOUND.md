# Passive Multimode Transfer-Area Bound — Harmonic External-Access Limit

**Date:** 2026-08-08  
**Status:** exact derivation for a finite-dimensional stable passive Markov/LTI network; mathematical ingredients are standard control/passivity theory; no novelty claim  

## 1. Result

Consider an arbitrary finite stable passive linear network connecting a useful optical reservoir `L` to an irreversible detector reservoir `R`, with no direct `L -> R` feedthrough.

Define total bare access budgets

```math
L\equiv\operatorname{Tr}\Gamma_L,
\qquad
R\equiv\operatorname{Tr}\Gamma_R.
```

Then the full frequency-integrated transfer obeys

```math
\boxed{
\mathcal I_{L\to R}
\equiv
\int_{-\infty}^{\infty}
\frac{d\omega}{2\pi}
\operatorname{Tr}
\left[
G_{RL}^\dagger(i\omega)
G_{RL}(i\omega)
\right]
\le
\frac{2LR}{L+R}.
}
```

The right side is the harmonic mean of the two aggregate external-access budgets.

This is stronger than the preliminary bound

```math
\mathcal I_{L\to R}
\le
2\min(L,R),
```

which remains true but is no longer canonical.

The harmonic bound is tight: a single lossless internal resonance saturates it exactly.

The theorem is independent of

- internal mode count;
- internal resonance frequencies;
- coherent Hermitian coupling topology;
- overlap of resonances;
- internal Fano-type interference;
- reciprocity;
- additional passive parasitic loss.

It is a finite passive-network resource result, not a universal nonlinear/active/Maxwell theorem.

---

## 2. Model

Let

```math
\mathbf a(t)\in\mathbb C^N
```

be the internal amplitude vector and write

```math
\boxed{
\dot{\mathbf a}
=A\mathbf a+B_L\mathbf s_L,
}
```

with

```math
\boxed{
A
=-iH
-(\Gamma_L+\Gamma_R+\Gamma_I).
}
```

Assume

```math
H=H^\dagger,
```

and

```math
\Gamma_L\succeq0,
\qquad
\Gamma_R\succeq0,
\qquad
\Gamma_I\succeq0.
```

`Gamma_I` represents any additional unobserved passive loss.

Normalize the optical input and detector output by

```math
\boxed{
B_LB_L^\dagger=2\Gamma_L,
}
```

```math
\boxed{
\mathbf y_R=C_R\mathbf a,
\qquad
C_R^\dagger C_R=2\Gamma_R.
}
```

Assume `A` is Hurwitz stable.

The strictly proper transfer block is

```math
\boxed{
G_{RL}(s)
=C_R(sI-A)^{-1}B_L.
}
```

---

## 3. `H_2` / Gramian representation

Let the left controllability Gramian satisfy

```math
\boxed{
AQ_L+Q_LA^\dagger+2\Gamma_L=0.
}
```

Then

```math
Q_L
=
\int_0^\infty
 e^{At}(2\Gamma_L)e^{A^\dagger t}
\,dt
\succeq0.
```

The standard `H_2` identity gives

```math
\boxed{
\mathcal I_{L\to R}
=
2\operatorname{Tr}(\Gamma_RQ_L).
}
```

A first passivity argument gives

```math
0\preceq Q_L\preceq I,
```

and therefore the preliminary trace bound

```math
\mathcal I_{L\to R}
\le
2\min(L,R).
```

The sharper result follows by using the **diagonal part of the Lyapunov equation in the eigenbasis of `Q_L`**.

---

## 4. Exact diagonal identity

Diagonalize

```math
Q_L
=U\,\operatorname{diag}(q_1,\ldots,q_N)\,U^\dagger.
```

In this basis define the nonnegative diagonal matrix elements

```math
\ell_i
=\left(U^\dagger\Gamma_LU\right)_{ii},
```

```math
r_i
=\left(U^\dagger\Gamma_RU\right)_{ii},
```

```math
\iota_i
=\left(U^\dagger\Gamma_IU\right)_{ii}.
```

The Lyapunov equation can be written

```math
-i[H,Q_L]
-\{\Gamma_L+\Gamma_R+\Gamma_I,Q_L\}
+2\Gamma_L
=0.
```

For every eigenvector of `Q_L`, the diagonal matrix element of the commutator vanishes exactly:

```math
\left([H,Q_L]\right)_{ii}=0.
```

Therefore each direction with

```math
\ell_i+r_i+\iota_i>0
```

obeys

```math
\boxed{
q_i
=\frac{\ell_i}
{\ell_i+r_i+\iota_i}.
}
```

If the denominator vanishes, positivity of the damping matrices implies

```math
\ell_i=r_i=\iota_i=0,
```

so that direction contributes nothing to the transfer area.

This identity is the key simplification: **the internal Hamiltonian disappears from the diagonal energy-partition relation.**

---

## 5. Exact transfer-area decomposition

Using the eigenbasis of `Q_L`,

```math
\frac{\mathcal I_{L\to R}}{2}
=
\operatorname{Tr}(\Gamma_RQ_L)
=
\sum_i r_iq_i.
```

Hence

```math
\boxed{
\frac{\mathcal I_{L\to R}}{2}
=
\sum_i
\frac{\ell_i r_i}
{\ell_i+r_i+\iota_i}.
}
```

Parasitic loss can only reduce every term, so

```math
\frac{\mathcal I_{L\to R}}{2}
\le
\sum_i
\frac{\ell_i r_i}
{\ell_i+r_i}.
```

The remaining problem is purely scalar.

---

## 6. Cauchy-Schwarz closes the bound

Use the identity

```math
\frac{\ell_i r_i}{\ell_i+r_i}
=
\frac14
\left[
(\ell_i+r_i)
-
\frac{(\ell_i-r_i)^2}
{\ell_i+r_i}
\right].
```

Summing gives

```math
\sum_i
\frac{\ell_i r_i}{\ell_i+r_i}
=
\frac14
\left[
L+R
-
\sum_i
\frac{(\ell_i-r_i)^2}
{\ell_i+r_i}
\right].
```

By Cauchy-Schwarz / Titu's lemma,

```math
\sum_i
\frac{(\ell_i-r_i)^2}
{\ell_i+r_i}
\ge
\frac{
\left[
\sum_i(\ell_i-r_i)
\right]^2
}
{
\sum_i(\ell_i+r_i)
}.
```

Since

```math
\sum_i\ell_i=L,
\qquad
\sum_i r_i=R,
```

we obtain

```math
\sum_i
\frac{\ell_i r_i}{\ell_i+r_i}
\le
\frac14
\left[
L+R
-
\frac{(L-R)^2}{L+R}
\right]
=
\frac{LR}{L+R}.
```

Therefore

```math
\boxed{
\mathcal I_{L\to R}
\le
\frac{2LR}{L+R}.
}
```

QED.

---

## 7. Equality conditions

The proof shows what is needed to saturate the bound.

First, no participating direction may have parasitic loss:

```math
\iota_i=0.
```

Second, equality in Cauchy-Schwarz requires the ratio

```math
\frac{\ell_i-r_i}
{\ell_i+r_i}
```

to be the same for every participating direction. Equivalently,

```math
\boxed{
\frac{\ell_i}{r_i}
=\frac{L}{R}
}
```

for all transfer-active directions.

Thus optimal integrated transfer requires **local matching in the same aggregate ratio as the global optical/detector access budgets**.

A single internal resonance automatically satisfies this condition and gives

```math
\boxed{
\mathcal I
=
\frac{2\gamma_L\gamma_R}
{\gamma_L+\gamma_R},
}
```

exactly saturating the theorem.

For matched total budgets `L=R=Gamma`,

```math
\boxed{
\mathcal I\le\Gamma.
}
```

---

## 8. Physical interpretation

The bound is stronger than saying the smaller reservoir is the bottleneck.

It says both access budgets enter through their harmonic mean:

```math
\boxed{
\text{integrated transfer area}
\le
\operatorname{HM}(L,R).
}
```

A very large optical coupling cannot compensate for an arbitrarily weak detector reservoir, and vice versa.

If

```math
L\ll R,
```

then

```math
\mathcal I
\lesssim2L,
```

while for matched budgets

```math
L=R,
```

```math
\mathcal I\le L=R.
```

This is the aggregate multimode analogue of ordinary rate matching / critical coupling.

---

## 9. Fixed target-band corollary

For a target angular-frequency band `B` of width

```math
W=|B|,
```

define the average total transfer

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

Since the band integral cannot exceed the full-line integral,

```math
\boxed{
\overline T_B
\le
\frac{4\pi LR}
{W(L+R)}.
}
```

Therefore a required average transfer

```math
\overline T_B\ge T_*
```

implies

```math
\boxed{
\frac{LR}{L+R}
\ge
\frac{T_*W}{4\pi}.
}
```

For equal total access budgets

```math
L=R=\Gamma_{\rm access},
```

this reduces to

```math
\boxed{
\Gamma_{\rm access}
\ge
\frac{T_*W}{2\pi}.
}
```

This is an external-access resource floor, not an absolute bandwidth limit.

---

## 10. Why arbitrary finite internal mode complexity does not evade it

The proof never assumes isolated resonances or diagonal internal Hamiltonians.

`H` may contain arbitrary finite Hermitian couplings, including complex phases. Thus the result permits

- overlapping modes;
- internal Fano interference;
- bright/dark superpositions;
- multimode photonic and material sectors;
- nonreciprocal phase structure compatible with a Hermitian passive Hamiltonian;
- arbitrary finite passive parasitic loss.

Mode proliferation can reshape the spectrum, but at fixed

```math
L=Tr Gamma_L,
\qquad
R=Tr Gamma_R,
```

it cannot increase the full transfer area above their harmonic mean.

To increase broadband transfer, an architecture must spend additional access resource, introduce a direct path, use active/time-varying dynamics, or leave the finite passive Markov/LTI class.

---

## 11. Direct feedthrough

If

```math
\mathbf y_R
=D_{RL}\mathbf s_L+C_R\mathbf a,
```

with

```math
D_{RL}\ne0,
```

then the full-line `H_2` integral is not the appropriate metric because a frequency-independent direct term has infinite area over an infinite frequency axis.

Physically, direct feedthrough is a separate broadband access resource.

Over a finite target band it contributes a finite term proportional to

```math
W\operatorname{Tr}(D_{RL}^\dagger D_{RL}),
```

plus interference with the resonant pathway.

It must be counted explicitly rather than described as a multimode loophole.

---

## 12. Structured / non-Markovian reservoirs

A finite structured reservoir can often be represented by promoting reaction-coordinate or pseudomode degrees of freedom into the internal state vector, leaving residual passive Markov boundaries.

When such a finite realization exists, the theorem applies to the enlarged system with the residual boundary access matrices.

The present proof does not cover

- genuinely infinite-dimensional reservoirs without a finite passive realization;
- strong boundary coupling for which the chosen local damping representation fails;
- active gain;
- explicit time dependence;
- nonlinear or saturating detector dynamics.

---

## 13. Mathematical prior-art boundary

The proof uses established mathematical ingredients:

- `H_2` transfer norms;
- controllability/observability Gramians;
- continuous Lyapunov equations;
- passive/scattering energy balance.

Relevant general sources include

- O. J. Staffans and G. Weiss, *SIAM Journal on Control and Optimization* **50** (2012), DOI `10.1137/110846403`;
- G. Weiss and O. J. Staffans, *SIAM Journal on Control and Optimization* **51** (2013), DOI `10.1137/120869444`;
- J. E. Gough and G. Zhang, arXiv `1311.1375`, on passive quantum linear-system realizations.

Broadband multimode optical-response bounds are also established in coupled-resonator and quasinormal-mode literature.

An initial targeted search has **not** identified this exact harmonic two-access trace bound stated in optical-to-detector language.

That is a negative search result only.

Do not claim novelty or priority without a much broader systems/network/scattering literature audit.

---

## 14. Numerical verification

`numerics/passive_multimode_h2_stress.py` performs deterministic random-network tests.

The regression checks

- the Lyapunov solution;
- `0 <= Q_L <= I`;
- the integrated transfer bound;
- direct numerical frequency integration for one representative multimode system.

The script should now use the harmonic trace bound

```math
\mathcal I_{L\to R}
\le
\frac{2LR}{L+R}
```

as its canonical assertion.

---

## 15. Current significance

This result gives the cleanest version yet of the recurring detector idea:

> **Internal electromagnetic sophistication can redistribute useful transfer, but it cannot replace simultaneous access to the optical input and irreversible detector reservoirs. In a finite passive linear network, the total frequency-integrated transfer is bounded by the harmonic mean of those aggregate access budgets.**

This is a robust model-level organizing statement.

It is not yet a claimed new photodetector theorem.

---

## 16. Next attacks

1. search control/network/scattering literature specifically for the harmonic trace inequality;
2. test whether a finite-band version including direct feedthrough has an equally clean resource decomposition;
3. test infinite-dimensional passive limits and strong structured reservoirs;
4. map `L` and `R` onto microscopic semiconductor optical-coupling and irreversible-relaxation resources;
5. add thermal/dark/reset thermodynamics only after that mapping is explicit.
