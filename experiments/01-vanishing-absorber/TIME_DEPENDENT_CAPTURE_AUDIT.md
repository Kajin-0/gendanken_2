# Time-Dependent Capture Audit — Known Temporal Mode, Bounded Coupling, and the Cost of Perfect Loading

**Date:** 2026-08-08  
**Status:** exact one-port time-varying loading identities; strong direct prior-art overlap with single-photon storage/control; supporting active-baseline result only; no novelty claim  

## 1. Purpose

Passive frequency-domain bounds can be exceeded by explicitly time-dependent systems. A particularly favorable thought experiment is therefore:

> Suppose the incident photon's temporal wavepacket and arrival time are known in advance. Can a detector tune its coupling in time and perfectly absorb the pulse even when the pulse is much broader than the detector's passive resonance?

The answer is yes in the ideal model.

But the required time-dependent coupling is fixed by the pulse shape, and finite coupling strength imposes an exact loading-time/efficiency resource bound.

This branch is closely related to established single-photon quantum-memory and tunable-absorber theory. No novelty is claimed for dynamic impedance matching.

---

## 2. One-port time-dependent resonator

Use the repository's amplitude-decay convention.

Let

```math
U(t)=|a(t)|^2
```

be stored energy / single-photon occupation amplitude norm, and let

```math
P_{\rm in}(t)=|s_{\rm in}(t)|^2.
```

For a phase-matched incident temporal mode, take

```math
\boxed{
\dot a(t)
=-\kappa(t)a(t)
+\sqrt{2\kappa(t)}\,s_{\rm in}(t),
}
```

```math
\boxed{
s_{\rm out}(t)
=-s_{\rm in}(t)
+\sqrt{2\kappa(t)}\,a(t).
}
```

Assume

- one lossless storage mode during the loading stage;
- one input/output channel;
- nonnegative time-dependent amplitude coupling `kappa(t)`;
- no internal dissipative detector sink during the loading interval;
- phase/frequency matching has been separately supplied if the incident temporal envelope has time-dependent phase.

---

## 3. Perfect zero-reflection loading fixes the coupling uniquely

Perfect loading requires

```math
s_{\rm out}(t)=0
```

throughout the pulse.

Therefore

```math
\boxed{
a(t)
=\frac{s_{\rm in}(t)}{\sqrt{2\kappa(t)}}.
}
```

With zero output and no internal loss, energy conservation gives

```math
\dot U(t)=P_{\rm in}(t).
```

For an initially empty storage mode,

```math
\boxed{
U(t)
=F(t)
\equiv
\int_{-\infty}^{t}
P_{\rm in}(t')\,dt'.
}
```

But zero reflection also gives

```math
U(t)
=\frac{P_{\rm in}(t)}{2\kappa(t)}.
```

Hence the exact required coupling is

```math
\boxed{
\kappa_{\rm perfect}(t)
=
\frac{P_{\rm in}(t)}
{2F(t)}
=
\frac12\frac{d}{dt}\ln F(t).
}
```

This is the temporal analogue of impedance matching.

The coupling is not an independently selectable detector parameter once the target temporal mode is fixed.

---

## 4. Hard leading edges require singular ideal coupling

Suppose a pulse begins at finite time `t0` and near its leading edge

```math
P_{\rm in}(t)
\sim
C(t-t_0)^n,
\qquad
n>-1.
```

Then

```math
F(t)
\sim
\frac{C}{n+1}
(t-t_0)^{n+1}.
```

Therefore

```math
\boxed{
\kappa_{\rm perfect}(t)
\sim
\frac{n+1}{2(t-t_0)}
}
```

as

```math
t\to t_0^+.
```

Thus any finite-support pulse with an ordinary algebraic leading edge requires divergent instantaneous coupling for exact zero-reflection loading into an initially empty single mode.

This reproduces the physical obstruction found in prior tunable single-photon absorber theory.

---

## 5. Infinite-tail pulses can avoid the singularity

The singularity is not universal for all temporal shapes.

For example, an exponentially rising intensity

```math
P_{\rm in}(t)
\propto
e^{2\gamma t}
```

extending from the infinite past gives

```math
F(t)
=\frac{P_{\rm in}(t)}{2\gamma},
```

and therefore

```math
\boxed{
\kappa_{\rm perfect}=\gamma
}
```

is constant.

This is the time-reversed free-decay mode of the cavity.

So the correct statement is not `perfect dynamic capture always requires infinite coupling`; it is that exact coupling is set by the pulse's cumulative-energy hazard, and hard finite starts generically make that hazard singular.

---

## 6. Exact finite-coupling capture bound over a finite control window

Now impose only

```math
0\le\kappa(t)\le\kappa_{\max}
```

on a loading interval

```math
[t_0,T],
\qquad
\tau=T-t_0.
```

For an initially empty cavity, the exact final amplitude is

```math
\boxed{
a(T)
=
\int_{t_0}^{T}
\sqrt{2\kappa(t)}
\exp\!\left[-\int_t^T\kappa(u)du\right]
 s_{\rm in}(t)dt.
}
```

Define the capture kernel

```math
h(t)
=
\sqrt{2\kappa(t)}
\exp\!\left[-\int_t^T\kappa(u)du\right].
```

For a normalized one-photon temporal mode,

```math
\int_{t_0}^{T}|s_{\rm in}(t)|^2dt=1,
```

Cauchy-Schwarz gives

```math
|a(T)|^2
\le
\int_{t_0}^{T}|h(t)|^2dt.
```

But

```math
\int_{t_0}^{T}|h(t)|^2dt
=
1-
\exp\!\left[-2\int_{t_0}^{T}\kappa(t)dt\right].
```

Therefore

```math
\boxed{
\eta_{\rm cap}
\le
1-
\exp\!\left[-2\int_{t_0}^{T}\kappa(t)dt\right]
\le
1-e^{-2\kappa_{\max}\tau}.
}
```

This is an exact finite-window resource bound for the one-mode time-dependent loader.

---

## 7. Tightness and optimal temporal mode

For a specified coupling schedule, the Cauchy-Schwarz bound is saturated by choosing the incoming temporal mode proportional to

```math
\boxed{
s_{\rm opt}(t)
\propto
\sqrt{2\kappa(t)}
\exp\!\left[-\int_t^T\kappa(u)du\right].
}
```

Thus

```math
\boxed{
\eta_{\max}[\kappa]
=
1-
\exp\!\left[-2\int_{t_0}^{T}\kappa(t)dt\right].
}
```

For the pointwise constraint `kappa <= kappa_max`, the largest possible integrated coupling occurs at

```math
\kappa(t)=\kappa_{\max},
```

giving the tight optimum over all pulse shapes and schedules:

```math
\boxed{
\eta_{\max}
=
1-e^{-2\kappa_{\max}\tau}.
}
```

The corresponding optimal pulse is a truncated rising exponential.

---

## 8. Coupling-rate x loading-time resource floor

To achieve target capture probability

```math
\eta_{\rm cap}\ge\eta,
```

one necessarily needs

```math
1-e^{-2\kappa_{\max}\tau}
\ge\eta.
```

Therefore

```math
\boxed{
\kappa_{\max}\tau
\ge
\frac12
\ln\frac{1}{1-\eta}.
}
```

This is the clean resource form of the finite-window result.

It is a time-domain coupling-strength / interaction-duration relation, not a direct spectral-bandwidth theorem.

A conversion to frequency bandwidth requires specifying a pulse family or a time-bandwidth convention.

---

## 9. Relation to prior single-photon capture theory

Several established results directly overlap this branch.

### Nurdin, James & Yamamoto (2016)

They derive the time-dependent coupling required for perfect absorption of arbitrary traveling single-photon temporal profiles by a tunable single input-output quantum system and explicitly note the singularity and practical coupling-strength limitation.

### Dilley et al. (2012)

They derive control pulses for perfect capture of arbitrary temporal photon shapes in an atom-cavity Raman system through dynamic impedance matching.

### Recent fast-storage work

Modern cavity-assisted quantum-memory theory explicitly studies finite-bandwidth / short-pulse limits and optimization of time-dependent coupling or cavity linewidth. Recent 2026 work finds a critical bandwidth above which efficiency degrades even with optimized modulation for the studied spin-ensemble architecture.

Therefore dynamic loading, pulse-specific impedance matching, and finite-control storage limits are established research areas.

The repository uses them only to identify which resource replaces the passive stationary bandwidth constraint.

---

## 10. What this says about the detector gedanken experiment

If the photon temporal mode and arrival schedule are known, a time-dependent detector can adapt to that mode and evade the requirement that one passive stationary resonance match the entire pulse spectrum.

But the escape spends at least two resources:

```text
knowledge/synchronization of the target temporal mode
+
finite time-dependent coupling strength integrated over the loading window.
```

This motivates the next question:

> What if the arrival time is not known, as in an always-on photodetector?

The answer cannot be obtained from spectral bandwidth alone; temporal-mode coverage becomes a separate resource.

---

## 11. Claim boundary

### Derived exactly within the scalar time-varying loader

Perfect zero-reflection schedule:

```math
\boxed{
\kappa(t)
=
\frac{P_{\rm in}(t)}
{2\int_{-\infty}^{t}P_{\rm in}(t')dt'}.
}
```

Finite-window capture bound:

```math
\boxed{
\eta_{\rm cap}
\le
1-e^{-2\int\kappa dt}
\le
1-e^{-2\kappa_{\max}\tau}.
}
```

Necessary resource:

```math
\boxed{
\kappa_{\max}\tau
\ge
\frac12\ln\frac1{1-\eta}.
}
```

### Not established

- novelty of these time-domain identities;
- a universal spectral bandwidth form;
- a universal work cost for modulating `kappa(t)`;
- capture limits with multiple storage modes;
- limits under real-time measurement/adaptive feedback;
- always-on unknown-arrival detector performance.

---

## 12. Next decisive step

Replace the known single temporal mode by an uncertainty set of mutually orthogonal possible arrival modes.

Ask how many such modes a finite detector storage space can accept before irreversible reset/readout.

That problem is independent of the detailed modulation waveform and leads naturally to a temporal-mode capacity bound.