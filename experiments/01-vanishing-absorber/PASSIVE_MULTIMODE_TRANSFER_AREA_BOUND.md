# Passive Multimode Transfer-Area Bound — External Access, Not Mode Count, Limits Integrated Transfer

**Date:** 2026-08-08  
**Status:** exact derivation for a finite-dimensional stable passive Markov/LTI network; mathematical ingredients are standard control/passivity theory; detector interpretation retained as a supporting result; no novelty claim  

## 1. Purpose

`MULTIMODE_ESCAPE_AUDIT.md` showed that a growing bank of narrow resonances can compensate the collapse of each individual linewidth by increasing the number/density of useful modes.

That construction raises the real question:

> Can arbitrarily complicated passive multimode interference produce arbitrarily large **frequency-integrated optical-to-detector transfer** while the total optical and detector access resources remain fixed?

For the finite passive linear network defined below, the answer is no.

The exact result is

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
2\min\!\left[
\operatorname{Tr}\Gamma_L,
\operatorname{Tr}\Gamma_R
\right].
}
```

The result is independent of

- the number of internal modes;
- their frequencies;
- coherent internal coupling topology;
- resonance overlap;
- Fano interference inside the finite state-space model;
- reciprocity.

What matters is the total access encoded at the two external boundaries.

This is a passivity/resource-accounting result, not a universal Maxwell theorem.

---

## 2. Finite passive network model

Let the internal complex mode-amplitude vector be

```math
\mathbf a(t)\in\mathbb C^N.
```

Use the amplitude equation

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

Interpret

- `Gamma_L` — coupling/damping associated with the useful optical input/output reservoir(s);
- `Gamma_R` — coupling/damping associated with the irreversible detector reservoir(s);
- `Gamma_I` — all additional unobserved passive loss.

Normalize the left input matrix by

```math
\boxed{
B_LB_L^\dagger=2\Gamma_L.
}
```

The detector-reservoir output is

```math
\boxed{
\mathbf y_R=C_R\mathbf a,
}
```

with

```math
\boxed{
C_R^\dagger C_R=2\Gamma_R.
}
```

Assume `A` is Hurwitz stable.

There is **no direct feedthrough/bypass from the left optical input to the detector output** in this model. A direct feedthrough term is a separate access resource and is discussed later.

---

## 3. Optical-to-detector transfer matrix

The strictly proper transfer matrix is

```math
\boxed{
G_{RL}(s)
=C_R(sI-A)^{-1}B_L.
}
```

For a monochromatic input, the total transferred fraction summed over input/output channels is represented by

```math
\operatorname{Tr}
\left[
G_{RL}^\dagger(i\omega)
G_{RL}(i\omega)
\right].
```

Define its full frequency-integrated area

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

`mathcal I` has units of angular frequency.

Mathematically this is the squared `H_2` norm of the strictly proper transfer block.

---

## 4. Controllability Gramian

Let `Q_L` solve

```math
\boxed{
AQ_L+Q_LA^\dagger+2\Gamma_L=0.
}
```

For stable `A`,

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
\operatorname{Tr}
(C_RQ_LC_R^\dagger)
=
2\operatorname{Tr}(\Gamma_RQ_L).
}
```

---

## 5. Passivity forces `0 <= Q_L <= I`

The passive state matrix obeys

```math
A+A^\dagger
=-2(\Gamma_L+\Gamma_R+\Gamma_I).
```

Define

```math
Z_L=I-Q_L.
```

Subtracting the Gramian equation from the equation for `I` gives

```math
AZ_L+Z_LA^\dagger
+2(\Gamma_R+\Gamma_I)=0.
```

Therefore

```math
\boxed{
Z_L
=
\int_0^\infty
 e^{At}
2(\Gamma_R+\Gamma_I)
 e^{A^\dagger t}
\,dt
\succeq0.
}
```

Hence

```math
\boxed{
0\preceq Q_L\preceq I.
}
```

Physical interpretation: starting from excitation injected through the left access, the state-space reachability Gramian cannot exceed the unit passive energy metric because some energy must leave through the right reservoir or other passive loss.

---

## 6. First transfer-area bound

Using

```math
0\preceq Q_L\preceq I
```

in

```math
\mathcal I_{L\to R}
=2\operatorname{Tr}(\Gamma_RQ_L)
```

gives

```math
\boxed{
\mathcal I_{L\to R}
\le
2\operatorname{Tr}\Gamma_R.
}
```

This already says that arbitrarily many optical modes cannot create unbounded integrated transfer into a detector reservoir whose total access matrix trace remains fixed.

---

## 7. Dual bound from observability

Now let `P_R` solve the observability Lyapunov equation

```math
\boxed{
A^\dagger P_R+P_RA+2\Gamma_R=0.
}
```

The same argument gives

```math
\boxed{
0\preceq P_R\preceq I.
}
```

The dual `H_2` identity gives

```math
\mathcal I_{L\to R}
=
\operatorname{Tr}
(B_L^\dagger P_RB_L)
=2\operatorname{Tr}(\Gamma_LP_R).
```

Therefore

```math
\boxed{
\mathcal I_{L\to R}
\le
2\operatorname{Tr}\Gamma_L.
}
```

Combining both inequalities yields the main result:

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

---

## 8. Single-mode check

For one internal mode with amplitude-decay rates `gamma_L` and `gamma_R` and no other loss,

```math
T(\omega)
=
\frac{4\gamma_L\gamma_R}
{(\omega-\omega_0)^2+(\gamma_L+\gamma_R)^2}.
```

Its exact area is

```math
\boxed{
\mathcal I
=
\frac{2\gamma_L\gamma_R}
{\gamma_L+\gamma_R}.
}
```

The general theorem gives

```math
\mathcal I
\le
2\min(\gamma_L,\gamma_R).
```

If one rate is much smaller than the other, for example `gamma_L << gamma_R`, then

```math
\mathcal I
\simeq2\gamma_L,
```

so the factor of `2` in the theorem is asymptotically attainable.

For exact matching `gamma_L=gamma_R=gamma`,

```math
\mathcal I=\gamma,
```

while the general bound gives `2 gamma`; the bound is not always tight.

---

## 9. Fixed target-band corollary

Let a target angular-frequency band `B` have width

```math
W=|B|.
```

Define the average total transfer in that band:

```math
\boxed{
\overline T_B
=
\frac1W
\int_B
\operatorname{Tr}
\left[
G_{RL}^\dagger(i\omega)
G_{RL}(i\omega)
\right]
\,d\omega.
}
```

Because the target-band integral cannot exceed the full-line integral,

```math
\overline T_B
\le
\frac{2\pi}{W}
\mathcal I_{L\to R}.
```

Hence

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

Equivalently, demanding

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

This is an **external-access budget floor**, not an absolute bandwidth limit.

Bandwidth can be increased, but the required total optical and detector coupling resources must increase with it.

---

## 10. Why internal mode count does not evade the result

The matrices `H`, `Gamma_L`, `Gamma_R`, and `Gamma_I` may have arbitrary finite dimension.

Therefore adding

- more cavity modes;
- more material modes;
- stronger coherent internal couplings;
- overlapping resonances;
- dark/bright internal superpositions;
- nonreciprocal phase structure in the Hermitian Hamiltonian;

cannot increase `mathcal I` beyond the trace bound **if the total boundary-access matrices remain fixed**.

A multimode escape must therefore spend at least one new resource:

```text
larger Tr Gamma_L,
larger Tr Gamma_R,
direct feedthrough,
active/time-varying elements,
non-Markovian reservoir structure,
or an effectively infinite-dimensional continuum not captured by fixed finite access budgets.
```

This makes the mode-density resource identified in `MULTIMODE_ESCAPE_AUDIT.md` more precise: proliferating useful modes can broaden response only if the aggregate access budget represented by the reservoir couplings is also available.

---

## 11. Relation to standard systems theory

The derivation uses standard mathematical ingredients:

- the `H_2` norm as a frequency-integrated squared transfer magnitude;
- controllability and observability Gramians;
- continuous Lyapunov equations;
- scattering/passive linear-system energy balance.

These ingredients are established in control theory and passive linear-system theory.

Relevant general sources include

- O. J. Staffans and G. Weiss, *SIAM Journal on Control and Optimization* **50** (2012), `A Physically Motivated Class of Scattering Passive Linear Systems`, DOI `10.1137/110846403`;
- G. Weiss and O. J. Staffans, *SIAM Journal on Control and Optimization* **51** (2013), `Maxwell's Equations as a Scattering Passive Linear System`, DOI `10.1137/120869444`;
- J. E. Gough and G. Zhang, arXiv `1311.1375`, `On Realization Theory of Quantum Linear Systems`, including passive/lossless bounded-real realizations.

A targeted initial search has not identified this exact two-access trace inequality stated as an optical-to-detector transfer-area bound.

That negative search is **not** evidence of novelty.

Treat this result as a useful detector-facing corollary of standard passivity/Gramian theory unless a broader literature review establishes otherwise.

---

## 12. Relation to multiresonant absorption literature

This theorem is consistent with, but not identical to, contemporary broadband-absorption bounds.

Collin and Giteau, *PRX Energy* **5**, 023006 (2026), DOI `10.1103/1tzg-hgqx`, derive broadband-absorption bounds for multiple overlapping resonances using quasinormal modes, radiative/nonradiative decay rates, and mode-density/resource accounting.

Huang, Yeung, and Raman, *Frontiers in Optics* (2020), `Limits on Thermal Emission from Multiple Coupled Resonators`, derive bounds on total emitted power versus bandwidth for arbitrary numbers of coupled resonators in temporal coupled-mode theory.

Those results concern absorption/emission objectives. The present note instead isolates transfer between two separately identified access reservoirs in a finite passive state-space network.

No priority distinction is claimed.

---

## 13. Direct feedthrough and bypass channels

If the detector output contains a direct left-to-right term

```math
\mathbf y_R
=D_{RL}\mathbf s_L+C_R\mathbf a,
```

then the strictly proper `H_2` integral over the entire real frequency axis is no longer the appropriate resource metric when `D_RL != 0`: a frequency-independent direct term has infinite full-line `H_2` energy.

Physically, such a bypass is an additional direct optical-to-detector access channel.

It must be counted explicitly rather than treated as an internal-mode loophole.

Over a finite target band, a direct term contributes a finite amount proportional to the target bandwidth and `Tr(D_RL^dagger D_RL)`.

---

## 14. Non-Markovian and strong-reservoir regimes

A structured or strongly coupled external reservoir can often be represented by promoting reaction-coordinate / pseudomode degrees of freedom into an enlarged internal state vector and leaving a residual Markov boundary coupling.

When that finite enlargement is valid, the same theorem applies to the enlarged passive network and the new residual `Gamma_L`, `Gamma_R`.

The theorem does not by itself cover

- genuinely infinite-dimensional reservoirs without a finite rational representation;
- active gain;
- explicitly time-varying systems;
- nonlinear/saturating dynamics;
- direct bypass/feedthrough not counted in the access budget.

These remain legitimate counterexample directions.

---

## 15. Current interpretation

The original thought experiment repeatedly tried to improve detector performance by increasing **internal** electromagnetic sophistication:

```text
field concentration
-> stronger light-matter coupling
-> more modes
-> retuning / hybridization.
```

For the finite passive linear class here, none of those operations creates unlimited frequency-integrated transfer at fixed external access budgets.

The resource statement is instead

```math
\boxed{
\text{integrated useful transfer}
\lesssim
\text{smaller total external access budget}.
}
```

This does not say that bandwidth is fundamentally bounded.

It says that broadband efficient detection requires proportionally sufficient access to **both** the optical and irreversible detector sides.

That is the most general form so far of the recurring two-access idea.

---

## 16. Next tests

Before any publication positioning:

1. run numerical random-matrix stress tests of the Lyapunov inequality;
2. search passive-network and scattering literature more deeply for an equivalent trace/H2 result;
3. test whether a tighter two-sided bound involving both access traces can be proved;
4. analyze finite-band direct-feedthrough contributions explicitly;
5. determine how the finite-network access budget maps onto a microscopic photodetector: oscillator strength, collection channels, irreversible relaxation, and thermal/noise reservoirs.

Do not yet call this a new detector theorem.