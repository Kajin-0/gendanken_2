# Fixed-Target Hopfield Retuning No-Go — Efficiency or Bandwidth Must Collapse at Infinite Internal Coupling

**Date:** 2026-08-08  
**Status:** derived theorem within the stated two-mode Hopfield + weak local-reservoir model; novelty unassessed  

## 1. Purpose

`NONPERTURBATIVE_HOPFIELD_CAPTURE.md` showed that, for equal bare light and matter frequencies, deep-strong coupling preserves perfect peak reservoir matching but collapses the transfer linewidth as `1/g`.

A natural counterexample is to retune the bare photonic and material frequencies as the coupling grows so that one dressed polariton stays at the desired detector carrier frequency.

This note attacks that escape directly.

The result is stronger than the symmetric example:

> **Within the TRK-consistent two-mode Hopfield model with fixed weak local optical and detector reservoir couplings, any sequence with internal coupling `g -> infinity` while the lower polariton is held at a fixed positive target frequency must drive at least one dressed reservoir coupling to zero. Consequently peak optical-to-detector transfer and transfer bandwidth cannot both remain bounded away from zero.**

This is a model theorem, not a universal photodetector theorem.

---

## 2. Model and assumptions

Use the Hopfield Hamiltonian

```math
H_S
=
\omega_c a^\dagger a
+\omega_b b^\dagger b
+i g(a b^\dagger-a^\dagger b)
+i g(a^\dagger b^\dagger-a b)
+D(a+a^\dagger)^2,
```

with

```math
\boxed{D=\frac{g^2}{\omega_b}}.
```

Assume

1. positive bare frequencies `omega_c`, `omega_b`;
2. the desired dressed lower polariton is held at a fixed frequency

```math
\boxed{\omega_y=\omega_t>0;}
```

3. the physical branch has

```math
\omega_c>\omega_t,
\qquad
\omega_b>\omega_t;
```

4. the optical reservoir couples locally and weakly to the photonic coordinate with fixed wideband amplitude-damping scale `gamma_L > 0`;
5. the irreversible detector reservoir couples locally and weakly to the material coordinate with fixed wideband amplitude-damping scale `gamma_R > 0`;
6. the strong internal light-matter coupling is diagonalized first and the reservoirs are treated in the dressed/global weak-bath description.

The fixed `gamma_L`, `gamma_R` assumption is essential. Scaling either reservoir coupling with `g` introduces a new physical resource and lies outside the theorem.

---

## 3. Exact lower-polariton constraint

The Hopfield squared-frequency matrix can be written

```math
K
=
\begin{pmatrix}
\omega_c^2+4g^2\omega_c/\omega_b
&2g\sqrt{\omega_c\omega_b}\\
2g\sqrt{\omega_c\omega_b}
&\omega_b^2
\end{pmatrix}.
```

Demand that

```math
\omega_t^2
```

be its lower eigenvalue.

Then

```math
\det(K-\omega_t^2 I)=0.
```

Expanding gives

```math
\left(
\omega_c^2
+4g^2\frac{\omega_c}{\omega_b}
-\omega_t^2
\right)
(\omega_b^2-\omega_t^2)
-4g^2\omega_c\omega_b
=0.
```

The coupling terms simplify exactly, yielding

```math
\boxed{
(\omega_c^2-\omega_t^2)
(\omega_b^2-\omega_t^2)
=
4g^2\frac{\omega_c}{\omega_b}\omega_t^2.
}
```

Equivalently,

```math
\boxed{
g^2
=
\frac{\omega_b}
{4\omega_c\omega_t^2}
(\omega_b^2-\omega_t^2)
(\omega_c^2-\omega_t^2).
}
```

This equation describes all bare-frequency retunings on the chosen fixed-target lower-polariton branch.

---

## 4. Exact lower-polariton mixing ratio

Choose the normalized lower-polariton coordinate eigenvector in the form

```math
v_y
=
\begin{pmatrix}
-\sin\theta\\
\cos\theta
\end{pmatrix},
```

where the first component is photonic and the second material.

The second row of

```math
(K-\omega_t^2 I)v_y=0
```

gives

```math
-2g\sqrt{\omega_c\omega_b}\sin\theta
+(\omega_b^2-\omega_t^2)\cos\theta
=0.
```

Therefore

```math
\boxed{
\tan\theta
=
\frac{\omega_b^2-\omega_t^2}
{2g\sqrt{\omega_c\omega_b}}.
}
```

This identity is exact on the fixed-target branch.

---

## 5. Dressed optical and detector reservoir rates

For the lower polariton, the dressed amplitude-decay contribution from the optical bath is

```math
\boxed{
\Gamma_L
=
\gamma_L
\sin^2\theta
\frac{\omega_c}{\omega_t}.
}
```

The dressed contribution from the material/detection bath is

```math
\boxed{
\Gamma_R
=
\gamma_R
\cos^2\theta
\frac{\omega_t}{\omega_b}.
}
```

These are the lower-polariton specializations of the global Hopfield dressed-rate factors.

Two elementary upper bounds will be sufficient.

First,

```math
\boxed{
\Gamma_R
\le
\gamma_R\frac{\omega_t}{\omega_b}.
}
```

Second, since

```math
\sin^2\theta\le\tan^2\theta,
```

the exact mixing ratio gives

```math
\Gamma_L
\le
\gamma_L
\frac{\omega_c}{\omega_t}
\frac{(\omega_b^2-\omega_t^2)^2}
{4g^2\omega_c\omega_b}.
```

Thus

```math
\boxed{
\Gamma_L
\le
\gamma_L
\frac{(\omega_b^2-\omega_t^2)^2}
{4g^2\omega_b\omega_t}.
}
```

---

## 6. Theorem: at least one dressed reservoir coupling must vanish

Consider any sequence of allowed parameter triples

```math
(g_n,\omega_{c,n},\omega_{b,n})
```

such that

```math
g_n\to\infty
```

while

```math
\omega_y=\omega_t
```

remains fixed.

We prove

```math
\boxed{
\min(\Gamma_{L,n},\Gamma_{R,n})
\to0.
}
```

### Proof by contradiction

Suppose not.

Then there exists some

```math
\epsilon>0
```

and an infinite subsequence for which

```math
\Gamma_L\ge\epsilon,
\qquad
\Gamma_R\ge\epsilon.
```

From

```math
\Gamma_R
\le
\gamma_R\frac{\omega_t}{\omega_b},
```

we must have

```math
\omega_b
\le
\frac{\gamma_R\omega_t}{\epsilon}.
```

Thus `omega_b` is bounded above on that subsequence.

Because the physical branch also has

```math
\omega_b>\omega_t>0,
```

the quantity

```math
\frac{(\omega_b^2-\omega_t^2)^2}
{\omega_b\omega_t}
```

is bounded above by a finite constant on that subsequence.

But then

```math
\Gamma_L
\le
\frac{C}{g^2}
```

for some finite `C` independent of `g` on the subsequence.

Since

```math
g\to\infty,
```

this forces

```math
\Gamma_L\to0,
```

contradicting

```math
\Gamma_L\ge\epsilon.
```

Therefore

```math
\boxed{
\min(\Gamma_L,\Gamma_R)\to0.
}
```

QED.

---

## 7. Corollary: efficiency and bandwidth cannot both remain finite

For one resolved lower polariton bridging the optical and detector reservoirs, the weak-signal transfer probability is

```math
T(\delta)
=
\frac{4\Gamma_L\Gamma_R}
{\delta^2+(\Gamma_L+\Gamma_R)^2}.
```

The peak transfer is

```math
\boxed{
T_0
=
\frac{4\Gamma_L\Gamma_R}
{(\Gamma_L+\Gamma_R)^2}.
}
```

The angular-frequency FWHM is

```math
\boxed{
\Delta\omega_{\rm FWHM}
=2(\Gamma_L+\Gamma_R).
}
```

The theorem says

```math
\min(\Gamma_L,\Gamma_R)\to0.
```

There are only two possibilities.

### Case A — the larger rate remains finite/nonzero

Then the ratio of the smaller to larger rate tends to zero, and

```math
\boxed{T_0\to0.}
```

Peak photon-transfer efficiency collapses.

### Case B — the rates remain matched enough to preserve nonzero peak transfer

If `T_0` is bounded away from zero, the ratio `Gamma_L/Gamma_R` cannot diverge or vanish.

Since the smaller rate tends to zero, the larger rate must then also tend to zero.

Therefore

```math
\boxed{
\Delta\omega_{\rm FWHM}\to0.
}
```

Hence no sequence with

```math
g\to\infty
```

and fixed target `omega_t` can retain both

```math
T_0\ge\eta_*>0
```

and

```math
\Delta\omega_{\rm FWHM}\ge W_*>0
```

for fixed positive constants `eta_*`, `W_*`.

This proves the fixed-target retuning no-go within the stated model.

---

## 8. Exact symmetric-retuning example

The theorem contains the symmetric retuning family as a simple special case.

Set

```math
\omega_c=\omega_b\equiv\Omega(g)
```

and demand

```math
\omega_-=\omega_t.
```

From

```math
\omega_-
=\sqrt{\Omega^2+g^2}-g,
```

one obtains

```math
\boxed{
\Omega^2
=\omega_t^2+2g\omega_t.
}
```

The upper polariton is then

```math
\boxed{
\omega_+
=\omega_t+2g.
}
```

For equal local bath strengths

```math
\gamma_L=\gamma_R=\gamma,
```

the two dressed rates remain exactly matched:

```math
\Gamma_L
=\Gamma_R
=
\frac{\gamma}
{2\sqrt{1+(g/\Omega)^2}}.
```

Using the retuning relation,

```math
\boxed{
\Gamma_L
=\Gamma_R
=
\frac{\gamma\sqrt{\omega_t^2+2g\omega_t}}
{2(g+\omega_t)}.
}
```

Thus

```math
T_0=1
```

for the target lower polariton, but

```math
\boxed{
\Delta\omega_{\rm FWHM}
=
\frac{2\gamma\sqrt{\omega_t^2+2g\omega_t}}
{g+\omega_t}.
}
```

At large `g`,

```math
\boxed{
\Delta\omega_{\rm FWHM}
\sim
2\gamma\sqrt{\frac{2\omega_t}{g}}
\to0.
}
```

Retuning slows the collapse from `g^{-1}` in the fixed-bare-frequency symmetric family to `g^{-1/2}`, but it does not remove it.

---

## 9. Physical interpretation

The no-go is not caused by a shortage of internal hybridization.

The internal coupling is becoming arbitrarily large.

The obstruction is that a fixed-frequency dressed excitation cannot retain finite overlap with **both** local reservoirs as the Hopfield parameters are pushed to infinite coupling while the bath coupling resources themselves remain fixed.

The detector needs two things simultaneously:

```text
optical access
+
irreversible material access.
```

At infinite internal coupling and fixed target frequency, at least one access channel disappears.

This is a more precise form of light-matter decoupling for the photodetection transfer problem.

---

## 10. Relation to prior theory

Established deep-strong-coupling literature already shows that local radiative decay and nonequilibrium heat transport can collapse at very large light-matter coupling in gauge-consistent Hopfield-type models.

Relevant primary sources include

- Simone De Liberato, *Physical Review Letters* 112, 016401 (2014), DOI `10.1103/PhysRevLett.112.016401`;
- D. De Bernardis, T. Jaako & P. Rabl, *Physical Review A* 97, 043820 (2018), DOI `10.1103/PhysRevA.97.043820`;
- D. De Bernardis et al., *Physical Review A* 98, 053819 (2018), DOI `10.1103/PhysRevA.98.053819`;
- S. Palafox et al., *Journal of Physics: Photonics* 7, 04LT02 (2025), DOI `10.1088/2515-7647/ae1649`.

The exact fixed-target retuning theorem above has not yet undergone a focused prior-art search.

Do **not** describe it as new or publishable until that search is performed.

---

## 11. Scope limitations

The theorem does not cover

- scaling `gamma_L` or `gamma_R` with `g`;
- strong/non-Markovian coupling to the input or detector reservoirs;
- more than one photonic or material oscillator;
- time-varying, active, or nonreciprocal couplers;
- direct optical coupling to the detector reservoir bypassing the chosen photonic/material partition;
- a target frequency that itself scales with `g`;
- fermionic finite-level matter outside the bosonized Hopfield model.

Each is a legitimate counterexample direction.

---

## 12. Next decisive test

Before generalizing, perform a focused prior-art collision search for the mathematical statement:

```text
fixed dressed frequency
+ TRK Hopfield coupling g -> infinity
+ fixed local bath coupling strengths
=> at least one dressed bath overlap -> 0
=> peak transfer or linewidth -> 0.
```

If that exact statement is already known, retain it as a clean supporting lemma.

If it is not found, the next adversarial extension should be a **multimode optical environment**, because a reviewer can reasonably argue that two-mode decoupling may be bypassed by redistributing optical coupling across many modes.