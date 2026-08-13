# Current Live State — Experiment 02

**Date:** 2026-08-12  
**Status:** exploratory first-principles theory; microscopic acquisition + record-formation models now derived  
**Priority:** unassessed; no novelty claim

This is the current state pointer for Experiment 02. Historical reasoning is in `RESEARCH_LOG.md`; epistemic status is in `CLAIM_LEDGER.md`.

Detailed active derivations:

1. `INTERACTION_ACTION_LOWER_BOUND.md`
2. `N_DIPOLE_SINGLE_MODE_MODEL.md`
3. `COHERENT_CAPTURE_TO_RECORD.md`

## 1. Starting question and current answer

Starting question:

> At what point does a simple collection of atoms become a photodetector?

Current answer:

> **There is no universal atom-count transition. A detector boundary emerges only after specifying how quickly the optical hypothesis must create an accessible state distinction, how competing loss acts, how long the distinction must persist, and how the record is read/reset. Under explicit microscopic constraints, minimum atom counts do emerge.**

The experiment now distinguishes three physically different reasons why `N` can matter:

```text
SPECTRAL CROSSOVER
N large -> dense spectrum / band-like description

ACQUISITION CROSSOVER
N coherently coupled dipoles -> stronger photon-matter matrix element

RECORD CROSSOVER
additional dynamics -> metastability / trapping / gain / redundancy
```

These are not the same boundary.

## 2. Operational detector criterion remains trace-distance discrimination

For the chosen accessible detector subsystem `D`, compare the states conditioned on no photon and one photon:

```math
\rho_D^{(0)},\qquad\rho_D^{(1)}.
```

Define

```math
\boxed{
\mathcal D_D
=\frac12\|\rho_D^{(1)}-\rho_D^{(0)}\|_1.
}
```

For equal priors,

```math
\boxed{
P_{e,\min}
=\frac12(1-\mathcal D_D).
}
```

This remains the operational spine of the experiment.

Consequences already established:

```text
perfect absorption can coexist with D_D=0;
nonabsorptive/dispersive interaction can produce D_D>0;
therefore absorption is neither sufficient nor universally necessary.
```

Electron-hole generation, gain, decoherence, and atom count are likewise not complete detector definitions by themselves.

## 3. First resource attack — deposited energy fails, interaction action survives

A degenerate two-state pointer can be conditionally rotated into an orthogonal state while its final bare detector energy change remains zero.

Therefore target discrimination alone does **not** imply a universal positive final energy separation or deposited/dissipated energy per event.

For a pure conditional-unitary detector,

```math
H_0(t)=H_D(t),
\qquad
H_1(t)=H_D(t)+V(t).
```

After removing common evolution, let `V_I(t)` generate the relative detector branch. For branch angle

```math
\theta
=\arccos|\langle D^{(0)}|D^{(1)}\rangle|,
```

pure-state trace distance gives

```math
\mathcal D_D=\sin\theta.
```

Thus target error `epsilon` requires

```math
\theta\ge\arcsin(1-2\epsilon).
```

Established quantum-state geometry yields

```math
\theta(\tau)
\le
\frac{1}{\hbar}
\int_0^\tau\Delta V_I(t)dt.
```

Define

```math
\mathcal A_\Delta
=\int_0^\tau\Delta V_I(t)dt.
```

Then

```math
\boxed{
\mathcal A_\Delta
\ge
\hbar\arcsin(1-2\epsilon).
}
```

For perfect discrimination,

```math
\boxed{
\mathcal A_\Delta\ge\pi\hbar/2.
}
```

The degenerate qubit construction saturates the perfect-discrimination value.

Interpretation:

```text
final detector energy difference -> not universal
finite interaction action        -> required in this finite-time pure/unitary model
```

No novelty claim is attached to the quantum speed-limit mathematics.

## 4. General constrained atom-count bound

If the differential interaction is decomposed as

```math
V_I(t)=\sum_{j=1}^{N}v_j(t)
```

and each local constituent is limited to integrated half-spectral-range action

```math
a_j
=\int_0^\tau
\frac{\lambda_{\max}[v_j]-\lambda_{\min}[v_j]}{2}
\,dt
\le a_{\max},
```

then

```math
\boxed{
N
\ge
\left\lceil
\frac{\hbar\arcsin(1-2\epsilon)}{a_{\max}}
\right\rceil.
}
```

This is the first clean recovery of the original `N` question:

> `N_min` is a **derived** threshold once the per-constituent interaction resource is bounded; it is not a universal material phase boundary.

## 5. Exact one-photon + N-dipole specialization

For `N` identical resonant two-level dipoles coupled to one quantized optical mode,

```math
H_I
=\hbar g\sum_{j=1}^N
(a\sigma_j^+ + a^\dagger\sigma_j^-).
```

In the one-excitation manifold the photon couples only to the symmetric bright state

```math
|W_N\rangle
=\frac{1}{\sqrt N}\sum_j|g\cdots e_j\cdots g\rangle
```

with collective frequency

```math
\boxed{G=g\sqrt N.}
```

Starting from `|1_gamma,G>`,

```math
|\Psi_1(t)\rangle
=
\cos(Gt)|1_\gamma,G\rangle
-i\sin(Gt)|0_\gamma,W_N\rangle.
```

Tracing out the optical mode gives the matter-only distinguishability

```math
\boxed{
\mathcal D_D(t)=\sin^2(g\sqrt Nt).
}
```

Hence

```math
\boxed{
P_{e,\min}(t)
=\frac12\cos^2(g\sqrt Nt).
}
```

On the first transfer lobe,

```math
\boxed{
N_{\min}
=
\left\lceil
\frac{[\arcsin\sqrt{1-2\epsilon}]^2}
{g^2\tau^2}
\right\rceil.
}
```

For perfect transient transfer,

```math
\boxed{
N_{\min}
=
\left\lceil
\left(\frac{\pi}{2g\tau}\right)^2
\right\rceil.
}
```

Thus the concrete symmetric single-mode architecture gives

```math
\boxed{N_{\min}\propto(g\tau)^{-2}.}
```

This `sqrt(N)` collective enhancement is established Dicke/Tavis--Cummings physics. Its role here is to show exactly how a many-atom threshold can emerge without band formation.

## 6. Coupling expressed in microscopic optical parameters

For an aligned electric-dipole transition in an ideal single-mode normalization,

```math
E_{\rm zpf}
=\sqrt{\frac{\hbar\omega}{2\epsilon_0V_{\rm eff}}},
```

```math
\boxed{
g
=|\mathbf d\cdot\mathbf e|
\sqrt{\frac{\omega}{2\hbar\epsilon_0V_{\rm eff}}}.
}
```

Therefore the closed-model atom threshold can be written

```math
\boxed{
N_{\min}
=
\left\lceil
\frac{
2\hbar\epsilon_0V_{\rm eff}
[\arcsin\sqrt{1-2\epsilon}]^2
}
{|\mathbf d\cdot\mathbf e|^2\omega\tau^2}
\right\rceil.
}
```

This is the first direct bridge from the Gedanken boundary to dipole strength, optical confinement, and interaction time.

## 7. Coherent excitation still does not make a persistent detector

The lossless matter excitation Rabi-oscillates back into the optical mode.

Therefore

```text
strong acquisition != persistent record.
```

This forced the next model to add a long-lived record state.

## 8. Minimal coherent-capture -> record model

Use states

```text
|P> : photon in optical mode
|M> : collective matter excitation
|R> : persistent accessible record
```

with

```text
G      = g sqrt(N) coherent P <-> M coupling
kappa  = optical-mode population loss
 gamma  = unwanted matter population loss
Gamma  = desired M -> R record-trapping rate.
```

The acquisition amplitudes obey

```math
\dot c_P=-\frac{\kappa}{2}c_P-iGc_M,
```

```math
\dot c_M=-\frac{\gamma+\Gamma}{2}c_M-iGc_P.
```

The exact probability that the initial in-mode photon ultimately produces the persistent record is

```math
\boxed{
P_R
=
\frac{4G^2\Gamma}
{(\kappa+\gamma+\Gamma)
[4G^2+\kappa(\gamma+\Gamma)]}.
}
```

The formula was independently checked by numerical integration of the amplitude equations for multiple parameter sets, with tested absolute agreement at approximately `1e-11`.

## 9. Irreversibility must be rate-matched

Maximizing `P_R` over the desired trapping rate gives

```math
\boxed{
\Gamma_{\rm opt}
=
\sqrt{
\frac{(\kappa+\gamma)(4G^2+\kappa\gamma)}{\kappa}
}
}
```

for `kappa>0`.

In the clean limit `gamma=0`,

```math
\boxed{\Gamma_{\rm opt}=2G=2g\sqrt N.}
```

This corrects another tempting shortcut:

```text
more irreversible trapping != monotonically better detection.
```

When optical escape competes:

```text
Gamma too small -> the excitation is not frozen before it returns/is lost;
Gamma too large -> coherent transfer is overdamped while the photon leaks out.
```

A finite matching condition is optimal.

The broad physics resembles established overdamping / quantum-Zeno / critical-coupling ideas; exact prior-art mapping remains open.

## 10. Maximum persistent-record probability

At optimal trapping,

```math
\boxed{
P_{R,\max}
=
\frac{4G^2}
{[\sqrt{\kappa(\kappa+\gamma)}
+\sqrt{4G^2+\kappa\gamma}]^2}.
}
```

For `gamma=0`,

```math
\boxed{
P_{R,\max}
=
\left(\frac{2G}{\kappa+2G}\right)^2.
}
```

Thus near-unity record formation requires collective acquisition to outrun optical escape in this initial-in-mode model.

## 11. Loss-constrained atom-count law

For `gamma=0`, optimized `Gamma`, no dark records, and a perfectly distinguishable record state, long-time record trace distance is `D_R=P_R,max`.

Target equal-prior error `epsilon` therefore implies

```math
\boxed{
N
\ge
\left[
\frac{\kappa}{2g}
\frac{\sqrt{1-2\epsilon}}
{1-\sqrt{1-2\epsilon}}
\right]^2.
}
```

For small `epsilon`,

```math
\boxed{
N_{\min}
\sim
\left(\frac{\kappa}{2g\epsilon}\right)^2.
}
```

This is substantially more demanding than transient coherent transfer because a persistent detector record must win against a real competing loss channel.

## 12. Current resource decomposition

The experiment now has a concrete three-stage hierarchy:

```text
ACQUISITION
photon-conditioned coherent coupling / interaction action

COMPETITION + RETENTION
acquisition rate versus optical/matter loss and record trapping

RESET
separate logical/thermodynamic recycling problem
```

For a thermally activated bistable record, the separate conditional retention result remains

```math
E_b
\ge
k_BT
\ln\left[
\frac{\nu_0\tau_{\rm rec}}
{-\ln(1-p_d)}
\right].
```

Landauer-type cost is not attached automatically to acquisition; reset must be specified.

## 13. Strongest conceptual result so far

The detector boundary is becoming a **dynamical rate-ratio problem**, not a static transition in matter.

Natural coordinates now include

```math
\frac{g\sqrt N}{\kappa},
\qquad
\frac{g\sqrt N}{\gamma},
\qquad
\frac{\Gamma}{g\sqrt N}.
```

The emerging chain is

```text
microscopic constitution
-> available light-matter coupling
-> state-separation speed
-> competition with loss
-> rate-matched conversion into a persistent record
-> readout/reset.
```

This is currently the strongest physical answer to the original question.

## 14. Current frontier

The present record model starts with the photon **already inside** the optical mode. It therefore does not yet solve actual capture of a traveling incident photon.

The next attack is:

```text
traveling one-photon wavepacket
-> input coupling kappa_in
-> parasitic optical loss kappa_loss
-> collective matter coupling g sqrt(N)
-> record trapping Gamma
-> output/reflection/transmission versus persistent record probability.
```

The goal is to determine whether near-unity external quantum efficiency reduces to a true impedance-matching / critical-coupling condition and then express that condition in optical depth, cross section, oscillator strength, mode volume, and bandwidth.

Only after that should the model be specialized back to semiconductor photoconductors/photodiodes and realistic detector metrics.

## 15. Mandatory caveats

- The interaction-action theorem used here is an established quantum-speed-limit consequence, not claimed new.
- `sqrt(N)` collective coupling is established Dicke/Tavis--Cummings physics.
- The record-trapping optimum has not yet undergone a direct prior-art audit and must not be called novel.
- Current microscopic models are idealized and do not yet include traveling-wave input matching, detuning/disorder, realistic semiconductor bands, thermal initial mixtures, dark-record generation, or reset.
- Experiment 01 remains separate and untouched.
