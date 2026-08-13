# One Photon + N Identical Dipoles — Experiment 02

**Date:** 2026-08-12  
**Status:** exact closed-system one-excitation model; microscopic specialization of the interaction-action program  
**Priority:** no novelty claim; Tavis--Cummings / Dicke collective coupling is established

## 1. Purpose

The previous result showed that a minimum atom count emerges once the maximum interaction action available from each constituent is bounded.

That result was deliberately abstract:

```math
N
\ge
\left\lceil
\frac{\hbar\arcsin(1-2\epsilon)}{a_{\max}}
\right\rceil.
```

The next question is whether a recognizable photon--matter Hamiltonian produces a more physical `N` scaling.

Use the simplest possible absorptive model:

```text
one quantized optical mode
one photon
N identical resonant two-level dipoles
all dipoles initially in the ground state
closed, lossless evolution during the acquisition interval
matter subsystem interrogated after time tau.
```

This is not yet a realistic photodetector. It is a controlled bridge from the abstract detector boundary to microscopic light--matter coupling.

---

## 2. Tavis--Cummings interaction

Let

```math
|G\rangle
=|g_1g_2\cdots g_N\rangle
```

be the collective matter ground state.

In the rotating-wave and resonant single-mode model,

```math
H_I
=
\hbar g
\sum_{j=1}^{N}
\left(
 a\sigma_j^+
+a^\dagger\sigma_j^-
\right),
```

where `g` is the single-dipole coupling frequency.

Define the normalized symmetric one-excitation state

```math
|W_N\rangle
=
\frac{1}{\sqrt N}
\sum_{j=1}^{N}
|g_1\cdots e_j\cdots g_N\rangle.
```

In the one-excitation manifold,

```math
|P\rangle
\equiv
|1_\gamma\rangle|G\rangle,
```

```math
|M\rangle
\equiv
|0_\gamma\rangle|W_N\rangle.
```

The interaction acts as

```math
H_I|P\rangle
=
\hbar g\sqrt N\,|M\rangle,
```

```math
H_I|M\rangle
=
\hbar g\sqrt N\,|P\rangle.
```

Thus the entire `N`-dipole problem collapses in this sector to

```math
H_I
=
\hbar G_N\sigma_x,
\qquad
G_N=g\sqrt N.
```

The photon couples only to the symmetric bright matter state; the other `N-1` one-excitation states are dark in this ideal symmetric model.

---

## 3. Exact one-photon evolution

Starting with one photon and all dipoles in the ground state,

```math
|\Psi_1(0)\rangle=|P\rangle,
```

the exact resonant evolution is

```math
\boxed{
|\Psi_1(t)\rangle
=
\cos(G_Nt)|P\rangle
-i\sin(G_Nt)|M\rangle.
}
```

Equivalently,

```math
|\Psi_1(t)\rangle
=
\cos(g\sqrt Nt)
|1_\gamma,G\rangle
-i\sin(g\sqrt Nt)
|0_\gamma,W_N\rangle.
```

For the no-photon hypothesis,

```math
|\Psi_0(t)\rangle
=|0_\gamma,G\rangle
```

in this ideal interaction picture.

The key microscopic scale is therefore

```math
\boxed{g\sqrt N\,t}.
```

This is already a more physical answer than raw atom count.

---

## 4. Matter-only detector state

The detector observer is granted access to the matter but not to the optical mode.

Under the no-photon hypothesis,

```math
\rho_D^{(0)}
=|G\rangle\langle G|.
```

Under the one-photon hypothesis, tracing out the optical mode gives

```math
\rho_D^{(1)}(t)
=
\cos^2(G_Nt)|G\rangle\langle G|
+
\sin^2(G_Nt)|W_N\rangle\langle W_N|.
```

The optical states `|1>` and `|0>` are orthogonal, so the field trace removes the corresponding coherence.

The difference is

```math
\rho_D^{(1)}-\rho_D^{(0)}
=
\sin^2(G_Nt)
\left(
|W_N\rangle\langle W_N|
-|G\rangle\langle G|
\right).
```

Because `|G>` and `|W_N>` are orthogonal,

```math
\boxed{
\mathcal D_D(t)
=
\sin^2(g\sqrt Nt).
}
```

This is an exact result for the stated model.

Interpretation:

```text
sin^2(g sqrt(N) t)
= probability that the optical excitation has been transferred into matter
= matter-only trace distance from the no-photon detector state.
```

For this minimal absorptive model, transfer probability and detector-state distinguishability coincide.

That coincidence is model-specific and must not be promoted back into a universal definition of detection.

---

## 5. Exact equal-prior detection error

The equal-prior Helstrom error is

```math
P_{e,\min}(t)
=
\frac12
\left[1-\mathcal D_D(t)\right].
```

Therefore

```math
\boxed{
P_{e,\min}(t)
=
\frac12\cos^2(g\sqrt Nt).
}
```

A target

```math
P_e\le\epsilon
```

requires

```math
\sin^2(g\sqrt N\tau)
\ge
1-2\epsilon.
```

On the first monotonic transfer interval

```math
0\le g\sqrt N\tau\le\pi/2,
```

this gives

```math
\boxed{
g\sqrt N\tau
\ge
\arcsin\sqrt{1-2\epsilon}.
}
```

Hence

```math
\boxed{
N
\ge
\frac{
\left[\arcsin\sqrt{1-2\epsilon}\right]^2
}{g^2\tau^2}.
}
```

With integer atom count,

```math
\boxed{
N_{\min}
=
\left\lceil
\frac{
\left[\arcsin\sqrt{1-2\epsilon}\right]^2
}{g^2\tau^2}
\right\rceil
}
```

provided operation is chosen on the first transfer lobe.

For perfect matter-record discrimination,

```math
\boxed{
g\sqrt N\tau=\frac{\pi}{2}}
```

and therefore

```math
\boxed{
N_{\min}^{(\epsilon=0)}
=
\left\lceil
\left(\frac{\pi}{2g\tau}\right)^2
\right\rceil.
}
```

This is the first mechanism-specific atom-count law in Experiment 02.

---

## 6. Numerical scale in dimensionless coupling

The threshold angle

```math
\alpha_\epsilon
\equiv
\arcsin\sqrt{1-2\epsilon}
```

is

```text
epsilon = 0.10  -> alpha = 1.10715 rad
epsilon = 0.01  -> alpha = 1.42890 rad
epsilon = 0.001 -> alpha = 1.52606 rad
epsilon = 0     -> alpha = pi/2 = 1.57080 rad
```

So for `g tau = 0.1`,

```text
epsilon = 0.10  -> N_min = 123
epsilon = 0.01  -> N_min = 205
epsilon = 0.001 -> N_min = 233
epsilon = 0     -> N_min = 247
```

For `g tau = 0.01`, all of these counts are larger by a factor of `100`.

The important scaling is

```math
\boxed{N_{\min}\propto(g\tau)^{-2}.}
```

Weak coupling or short interaction time can therefore make a many-atom ensemble necessary even though no universal atom-count boundary exists.

---

## 7. Why the scaling is quadratic

The collective bright-state matrix element is

```math
G_N=g\sqrt N.
```

To reach a fixed state-transfer pulse area,

```math
G_N\tau\sim1.
```

Therefore

```math
\sqrt N\sim\frac{1}{g\tau},
```

or

```math
N\sim\frac{1}{(g\tau)^2}.
```

This is a physically stronger result than the previous general spectral-range counting bound because the Tavis--Cummings Hamiltonian supplies additional structure.

The previous bound says only that total available local action must be sufficient.

The present model says that, for a single photon coupling coherently to `N` identical ground-state dipoles through one bright collective mode, the usable matrix element grows only as `sqrt(N)`.

Thus architecture determines how microscopic resources combine.

---

## 8. Connection to dipole matrix element and mode volume

For a single electric-dipole transition coupled to a quantized mode, the vacuum electric-field scale is

```math
E_{\rm zpf}
=
\sqrt{\frac{\hbar\omega}{2\epsilon_0V_{\rm eff}}}
```

for the idealized polarization-aligned mode normalization used here.

The single-emitter coupling frequency is

```math
\boxed{
g
=\frac{|\mathbf d\cdot\mathbf e|E_{\rm zpf}}{\hbar}
=|\mathbf d\cdot\mathbf e|
\sqrt{\frac{\omega}{2\hbar\epsilon_0V_{\rm eff}}}.
}
```

Substituting into the atom-count requirement gives

```math
\boxed{
N_{\min}
=
\left\lceil
\frac{
2\hbar\epsilon_0V_{\rm eff}
\left[\arcsin\sqrt{1-2\epsilon}\right]^2
}
{
|\mathbf d\cdot\mathbf e|^2\omega\tau^2
}
\right\rceil.
}
```

This exposes the physical levers:

```text
larger transition dipole -> fewer emitters required
smaller optical mode volume -> fewer emitters required
longer coherent dwell time -> fewer emitters required
higher target fidelity -> more interaction resource required.
```

The exact numerical prefactor depends on mode normalization, polarization/orientation, detuning, and the validity of the rotating-wave single-mode model.

---

## 9. The original solid-state intuition is now partly explained

The experiment started from an intuition that "enough atoms" somehow turns optical interaction into detector behavior.

The current result gives a precise mechanism by which that intuition can become true without invoking band formation:

```text
one weak dipole
-> insufficient photon--matter pulse area in the available time

many identical dipoles
-> one symmetric bright state
-> matrix element enhanced by sqrt(N)
-> sufficient excitation transfer
-> matter contains a distinguishable photon-conditioned state.
```

No semiconductor band is required.

Thus there are at least two completely different reasons why increasing atom count may matter:

```text
1. condensed-matter reason:
   discrete levels become dense / band-like;

2. detector-coupling reason:
   collective photon--matter matrix element becomes large enough.
```

These are separate crossovers.

That separation is one of the clearest conceptual outcomes of the Gedanken experiment so far.

---

## 10. But this is still not a practical detector

At the perfect-transfer time,

```math
|1,G\rangle
\rightarrow
-i|0,W_N\rangle.
```

If the coherent interaction remains on, the excitation Rabi-oscillates back into the optical mode.

Therefore

```text
strong acquisition
!= persistent record.
```

A real detector needs another process to freeze, decohere, trap, amplify, spatially separate, or otherwise preserve the acquired distinction long enough for readout.

This is not a defect of the model. It demonstrates exactly why Experiment 02 separated acquisition from retention.

The minimal chain is now

```text
single photon
-> coherent collective transfer
-> W-state matter record
-> [missing retention mechanism]
-> robust detector output.
```

The bracketed step is the next physical boundary.

---

## 11. Losses are expected to introduce cooperativity

The closed model assumes no optical leakage and no dipole decoherence during transfer.

A realistic extension must include at least

```text
optical-mode loss rate kappa
matter coherence / decay rate gamma
collective coherent coupling g sqrt(N).
```

The natural competition is therefore between

```math
g\sqrt N,
\qquad
\kappa,
\qquad
\gamma.
```

This strongly suggests that the useful open-system boundary will collapse onto a collective-cooperativity-like coordinate such as

```math
C_N\sim\frac{Ng^2}{\kappa\gamma},
```

up to convention-dependent numerical factors.

That is a hypothesis for the next step, not yet a derived Experiment-02 result.

If confirmed, it would be scientifically useful even if entirely established physics:

> the apparently philosophical question "when do atoms become a detector?" would reduce, under a concrete optical architecture, to a competition between collective information-acquisition rate and loss/decoherence rates.

---

## 12. Adversarial checks

### Check A — does the result accidentally redefine absorption as detection?

No. In this specific model the matter trace distance equals the excitation-transfer probability because there are only two orthogonal matter sectors and one optical mode. Earlier counterexamples still prove this equivalence is not universal.

### Check B — is `sqrt(N)` a novelty claim?

No. Collective `sqrt(N)` coupling of identical two-level emitters to a common mode is established Dicke / Tavis--Cummings physics.

### Check C — does the `N_min` law define a universal critical atom number?

No. It depends explicitly on `g`, `tau`, resonance, symmetry, mode structure, initial state, allowed error, and closed-system assumptions.

### Check D — does perfect transfer imply a stable detector click?

No. The coherent excitation returns unless another retention/readout process intervenes.

### Check E — can arbitrary geometry use the same `sqrt(N)` law?

No. Phase mismatch, inhomogeneous couplings, detuning, spatial extent, disorder, and dark-state participation can reduce or alter collective enhancement.

---

## 13. Established foundations

- R. H. Dicke, **"Coherence in Spontaneous Radiation Processes,"** *Physical Review* **93**, 99 (1954), DOI `10.1103/PhysRev.93.99`.
- M. Tavis and F. W. Cummings, **"Exact Solution for an N-Molecule--Radiation-Field Hamiltonian,"** *Physical Review* **170**, 379 (1968), DOI `10.1103/PhysRev.170.379`.

These sources establish the collective light--matter physics. No novelty claim is attached to the Hamiltonian, symmetric-state reduction, or `sqrt(N)` enhancement.

---

## 14. Current strongest insight

The original atom-count question has now split into three distinct meanings of "more atoms":

```text
SPECTRAL CROSSOVER
more atoms -> denser electronic spectrum -> band-like description

ACQUISITION CROSSOVER
more coherently coupled dipoles -> larger collective matrix element -> faster photon-to-matter state transfer

RECORD CROSSOVER
more / different degrees of freedom may provide metastability, decoherence, gain, or redundancy -> persistent readable record
```

Only the second has been quantified here, and the third remains the practical detector boundary.

---

## 15. Next attack

Add the smallest possible irreversible-looking ingredient without losing analytic transparency:

```text
one photon + N dipoles + one optical mode
+ optical loss kappa
+ matter decay/dephasing gamma
+ one irreversible/trapping channel Gamma_rec that converts |W_N> into a long-lived record state |R>.
```

Then ask:

```text
What relation among g sqrt(N), kappa, gamma, and Gamma_rec
maximizes probability of ending in |R>
while minimizing dark/false records?
```

That model would connect

```text
coherent photon capture
-> competition with loss
-> irreversible-looking record formation
```

and should reveal whether the next detector boundary is best described by cooperativity, impedance matching, a rate-matching condition, or a new composite resource.
