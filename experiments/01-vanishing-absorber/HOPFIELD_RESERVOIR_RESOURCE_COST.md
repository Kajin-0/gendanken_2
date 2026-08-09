# Fixed-Target Hopfield Reservoir Compensation Cost

**Date:** 2026-08-08  
**Status:** derived corollary within the fixed-target two-mode Hopfield + weak local-reservoir model; no novelty claim  

## 1. Purpose

`HOPFIELD_RETUNING_NO_GO.md` proved that with fixed local optical and detector reservoir coupling scales,

```math
\min(\Gamma_L,\Gamma_R)\to0
```

when the internal light-matter coupling `g -> infinity` while the useful lower polariton is kept at a fixed target frequency `omega_t > 0`.

A natural escape is to scale the bare reservoir couplings themselves with `g`.

This note does not forbid that escape. It quantifies the additional resource required.

The main result is:

> **If a fixed-target lower-polariton resonance is required to retain both a nonzero minimum peak transfer and a nonzero minimum linewidth as `g` grows, then at least one bare local reservoir coupling scale must grow at least as `sqrt(g/omega_t)`. The symmetric retuning family asymptotically saturates this scaling.**

Thus scaled reservoir engineering is not a free refutation of the fixed-bath theorem; it moves the cost into the external access resources.

---

## 2. Starting point

For the resolved lower-polariton transfer resonance,

```math
T_0
=
\frac{4\Gamma_L\Gamma_R}
{(\Gamma_L+\Gamma_R)^2},
```

and

```math
\Delta\omega_{\rm FWHM}
=2(\Gamma_L+\Gamma_R).
```

Require fixed performance targets

```math
\boxed{T_0\ge\eta_*>0}
```

and

```math
\boxed{\Delta\omega_{\rm FWHM}\ge W_*>0.}
```

The question is what these requirements force on the bare local bath scales `gamma_L` and `gamma_R`.

---

## 3. Performance requirements imply a dressed-rate floor

Let

```math
S=\Gamma_L+\Gamma_R
```

and define the smaller dressed-rate fraction

```math
p
=\frac{\min(\Gamma_L,\Gamma_R)}{S},
\qquad
0<p\le\frac12.
```

Then

```math
T_0=4p(1-p).
```

The condition

```math
T_0\ge\eta_*
```

therefore requires

```math
p
\ge
\frac{1-\sqrt{1-\eta_*}}{2}.
```

Meanwhile

```math
\Delta\omega_{\rm FWHM}=2S\ge W_*
```

gives

```math
S\ge\frac{W_*}{2}.
```

Combining the two inequalities yields

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
\equiv
\frac{W_*}{4}
\left(1-\sqrt{1-\eta_*}\right).
}
```

This rate floor is exact for the stated peak-transfer and linewidth requirements.

Checks:

- `eta_* -> 0` gives `Gamma_* -> 0`, as expected;
- `eta_* = 1` gives `Gamma_* = W_*/4`, corresponding to perfectly matched rates `Gamma_L = Gamma_R = W_*/4`.

---

## 4. Fixed-target Hopfield bounds on the dressed rates

Use the notation

```math
G=\frac{g}{\omega_t},
\qquad
y=\frac{\omega_b}{\omega_t}>1.
```

From `HOPFIELD_RETUNING_NO_GO.md`,

```math
\Gamma_R
\le
\gamma_R\frac{\omega_t}{\omega_b}
=\frac{\gamma_R}{y}.
```

Therefore retaining

```math
\Gamma_R\ge\Gamma_*
```

requires

```math
\boxed{
\gamma_R
\ge
\Gamma_* y.
}
```

The same fixed-target derivation also gives

```math
\Gamma_L
\le
\gamma_L
\frac{(\omega_b^2-\omega_t^2)^2}
{4g^2\omega_b\omega_t}.
```

In dimensionless form,

```math
\Gamma_L
\le
\gamma_L
\frac{(y^2-1)^2}
{4G^2y}.
```

Hence retaining

```math
\Gamma_L\ge\Gamma_*
```

requires

```math
\boxed{
\gamma_L
\ge
\Gamma_*
\frac{4G^2y}
{(y^2-1)^2}.
}
```

Every fixed-target retuning sequence that keeps the requested detector performance must satisfy both bare-resource inequalities.

---

## 5. Optimize over every allowed material retuning

For a given `G`, define

```math
F_1(y)=y,
```

and

```math
F_2(y)
=\frac{4G^2y}{(y^2-1)^2}.
```

`F_1` increases monotonically for `y>1`, while `F_2` decreases monotonically because

```math
\frac{d}{dy}\ln F_2
=\frac1y-\frac{4y}{y^2-1}<0.
```

Therefore the minimum possible value of

```math
\max(F_1,F_2)
```

occurs where they cross:

```math
y
=\frac{4G^2y}{(y^2-1)^2}.
```

For `y>1`,

```math
(y^2-1)^2=4G^2,
```

so

```math
\boxed{
y_*
=\sqrt{1+2G}.
}
```

At this point

```math
F_1(y_*)=F_2(y_*)=\sqrt{1+2G}.
```

Thus, for **every** allowed fixed-target bare-frequency retuning,

```math
\boxed{
\max(\gamma_L,\gamma_R)
\ge
\Gamma_*
\sqrt{1+2g/\omega_t}.
}
```

Substituting the performance floor,

```math
\boxed{
\max(\gamma_L,\gamma_R)
\ge
\frac{W_*}{4}
\left(1-\sqrt{1-\eta_*}\right)
\sqrt{1+2g/\omega_t}.
}
```

This is the main resource-cost result.

---

## 6. Deep-strong asymptotic scaling

For

```math
g\gg\omega_t,
```

the bound becomes

```math
\boxed{
\max(\gamma_L,\gamma_R)
\gtrsim
\Gamma_*
\sqrt{\frac{2g}{\omega_t}}.
}
```

Therefore retaining fixed nonzero peak transfer and fixed nonzero linewidth requires at least one bare local reservoir coupling resource to diverge as

```math
\boxed{\sqrt g.}
```

The original fixed-bath theorem is recovered immediately: if both `gamma_L` and `gamma_R` remain bounded, the performance requirements must eventually fail.

---

## 7. Symmetric retuning asymptotically saturates the scaling

The exact symmetric fixed-target family has

```math
\omega_c=\omega_b=\Omega,
```

with

```math
\boxed{
\frac{\Omega}{\omega_t}
=\sqrt{1+2G}.
}
```

Thus it chooses exactly the value `y_*` that optimizes the lower bound above.

For equal bare bath scales

```math
\gamma_L=\gamma_R=\gamma,
```

the exact dressed rates are

```math
\boxed{
\Gamma_L=\Gamma_R
=\gamma
\frac{\sqrt{1+2G}}
{2(1+G)}.
}
```

To maintain

```math
\Gamma_L=\Gamma_R\ge\Gamma_*,
```

one needs

```math
\boxed{
\gamma
\ge
2\Gamma_*
\frac{1+G}
{\sqrt{1+2G}}.
}
```

The ratio of this exact symmetric requirement to the general lower bound is

```math
\frac{
2(1+G)/\sqrt{1+2G}
}{
\sqrt{1+2G}
}
=
\frac{2(1+G)}{1+2G}
\to1.
```

Hence the `sqrt(g)` lower-bound scaling is asymptotically sharp within the stated two-mode model.

---

## 8. The escape eventually leaves the weak-reservoir model

The dressed/global treatment used in the Hopfield notes assumes that the external optical and detector reservoirs remain weakly coupled relative to the system frequencies and can be represented by smooth wideband damping scales.

But the compensation bound requires

```math
\max(\gamma_L,\gamma_R)\to\infty
```

as `g -> infinity` if fixed transfer performance is demanded.

Therefore a putative asymptotic escape by scaling the reservoirs eventually exits the regime in which the present weak-bath model is controlled.

This does **not** prove that nonperturbatively strong reservoir engineering is impossible.

It identifies the next resource layer:

```text
internal light-matter coupling
-> dressed access suppression
-> stronger external reservoir coupling
-> nonperturbative / broadband reservoir physics.
```

Any claimed refutation by scaling `gamma_L` or `gamma_R` must therefore specify the physical reservoir, its bandwidth, its own energy storage and loss, and the regime in which a local Markov damping rate remains meaningful.

---

## 9. Interpretation

The fixed-target theorem said that internal coupling cannot be increased without limit while keeping both useful external accesses finite **for fixed bath resources**.

The present result says more:

> **To compensate the dressed decoupling and retain fixed detector efficiency and bandwidth, one must increase an external access resource without bound; the least favorable bare reservoir rate grows at least as `sqrt(g/omega_t)`.**

This is a resource-accounting statement, not a universal no-go against all reservoir engineering.

---

## 10. Scope

The result assumes

- the two-mode TRK-consistent Hopfield system;
- a fixed positive lower-polariton target frequency;
- a resolved target resonance;
- local optical and detector reservoirs represented by weak wideband amplitude-damping scales;
- the same dressed-rate formulas as `HOPFIELD_RETUNING_NO_GO.md`.

It does not cover

- non-Markovian structured reservoirs;
- reservoir couplings treated nonperturbatively as additional system modes;
- direct bypass channels;
- time variation or active gain;
- multimode internal systems.

Those are legitimate next attacks.

---

## 11. Next use

This result should be used when assessing the phrase "just increase the external coupling as `g` grows."

The correct response is not that such scaling is forbidden. It is that it has a quantitative cost and eventually requires a new nonperturbative model.

The separate multimode attack should now ask whether finite or growing mode count can distribute the two required accesses without demanding the same divergent local reservoir resources.