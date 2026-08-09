# Unified Three-Level Capture Machine — Propagating Photon, Amplified Click, Reset, and Dark-State Currents

**Date:** 2026-08-08  
**Status:** minimal analytic testbed joining propagating optical capture to an autonomous detector cycle; strong prior-art overlap with quantum photodetector and three-level thermal-machine models; no novelty claim  

## 1. Purpose

Two major prior frameworks now constrain the research direction:

- Young, Sarovar & Léonard (2018) already treat the incoming quantum field, absorption, amplification, and monitored detector states in one quantum model;
- Schwarzhans et al. (2026) already treat detector amplification/readout/reset as an autonomous nonequilibrium thermal machine with efficiency, internal dark counts, jitter, dead time, and entropy production.

The purpose of this note is therefore **not** to claim a new three-level detector model.

It is to build the smallest analytically solvable testbed in which the repository's passive capture/access results can be compared directly with thermodynamic click/reset observables.

---

## 2. Three internal states

Use

```text
|0>  reset/ground state
|1>  metastable detection-ready state
|2>  optically activated state.
```

The cycle is

```text
work/reset source
|0> <----------> |1>
                   |
                   | incident optical photon
                   v
                  |2>
                   |
                   | counted detector output
                   v
                  |0>.
```

Let

```math
E_0<E_1<E_2.
```

The signal transition is

```math
\hbar\omega_L=E_2-E_1,
```

while the amplified detector output transition is

```math
\hbar\omega_R=E_2-E_0.
```

Therefore

```math
\boxed{
\omega_R
=
\omega_L+\omega_{10},
\qquad
\omega_{10}=(E_1-E_0)/\hbar.
}
```

The extra output energy is supplied by the free energy stored in the detection-ready state.

---

## 3. Single-photon capture and conversion when the detector is ready

First condition on the detector being in `|1>` and ignore reset during the short capture event.

Let the optical input channel couple `|1> <-> |2>` with **amplitude-decay** rate

```math
\Gamma_L,
```

and let the counted detector continuum couple `|2> -> |0>` with amplitude-decay rate

```math
\Gamma_R.
```

Include other passive loss from `|2>` through

```math
\Gamma_I\ge0.
```

For a weak/single-photon input with detuning

```math
\delta=\omega-\omega_L,
```

the activated-state envelope has the same one-pole form as the earlier passive capture model:

```math
c_2(\omega)
\propto
\frac{\sqrt{2\Gamma_L}}
{\Gamma_L+\Gamma_R+\Gamma_I-i\delta}.
```

The probability density for conversion of the incident photon into the counted detector output channel is therefore

```math
\boxed{
T_{L\to R}(\omega)
=
\frac{4\Gamma_L\Gamma_R}
{\delta^2+(\Gamma_L+\Gamma_R+\Gamma_I)^2}.
}
```

This is a frequency-converting scattering probability under photon-flux normalization. The output photon is centered at `omega_R`, not `omega_L`.

---

## 4. Peak conversion and bandwidth

On resonance,

```math
\boxed{
T_0
=
\frac{4\Gamma_L\Gamma_R}
{(\Gamma_L+\Gamma_R+\Gamma_I)^2}.
}
```

If

```math
\Gamma_I=0,
```

then unit conditional conversion is possible at

```math
\boxed{\Gamma_L=\Gamma_R.}
```

The angular-frequency FWHM is

```math
\boxed{
\Delta\omega_{\rm FWHM}
=2(\Gamma_L+\Gamma_R+\Gamma_I).
}
```

The all-frequency conversion area is

```math
\boxed{
\mathcal I_{L\to R}
=
\int_{-\infty}^{\infty}
\frac{d\omega}{2\pi}T_{L\to R}(\omega)
=
\frac{2\Gamma_L\Gamma_R}
{\Gamma_L+\Gamma_R+\Gamma_I}.
}
```

Thus the single-event ready-state detector exactly reproduces the one-mode harmonic-access structure derived earlier.

The stored free energy can amplify the **energy** of the counted output quantum, but it does not by itself remove the optical/detector rate-matching requirement for capture probability.

---

## 5. Energy gain and reset energy

For resonant conversion,

```math
\hbar\omega_R
=
\hbar\omega_L+(E_1-E_0).
```

Define the output/input quantum-energy ratio

```math
\boxed{
G_E
\equiv
\frac{\omega_R}{\omega_L}
=
1+
\frac{E_1-E_0}
{E_2-E_1}.
}
```

After a successful click the internal system is in `|0>`, so it must be restored to `|1>` before another identical event.

At the level of energy accounting, the detector must replenish

```math
\boxed{E_1-E_0}
```

per ideal completed cycle.

A thermodynamic work/free-energy statement stronger than this requires a specified reset reservoir and is not inferred from energy conservation alone.

---

## 6. Fully reversible dark-state rate model

To study dark operation and reset, now replace the coherent optical event by the long-time population kinetics of a three-state continuous-time Markov cycle.

Define population-transition rates

```text
u : 0 -> 1   reset / preparation
 d : 1 -> 0  reverse reset
 a : 1 -> 2  optical upward transition
 b : 2 -> 1  optical downward transition
 c : 2 -> 0  forward counted detector transition
 e : 0 -> 2  reverse detector-bath transition.
```

The optical upward rate `a` may contain external thermal/background photons and, in a weak incoherent-signal treatment, a signal-induced contribution. It should not automatically be called internal dark excitation.

The master equation is

```math
\dot p_0
=-(u+e)p_0+d p_1+c p_2,
```

```math
\dot p_1
=u p_0-(d+a)p_1+b p_2,
```

```math
\dot p_2
=e p_0+a p_1-(c+b)p_2.
```

---

## 7. Exact dark steady state

Define

```math
\boxed{
Z
=
ac+ae+au
+bd+be+bu
+cd+cu+de.
}
```

The exact stationary probabilities are

```math
\boxed{
p_0
=
\frac{ac+bd+cd}{Z},
}
```

```math
\boxed{
p_1
=
\frac{be+bu+cu}{Z},
}
```

```math
\boxed{
p_2
=
\frac{ae+au+de}{Z}.
}
```

They sum to unity and are nonnegative for positive rates.

---

## 8. Gross forward clicks versus net thermodynamic current

If the physical readout records every forward detector-channel transition

```text
2 -> 0,
```

then the **gross forward click rate** is

```math
\boxed{
R_+
=c p_2
=
\frac{c(ae+au+de)}{Z}.
}
```

The reverse detector-bath transition rate is

```math
\boxed{
R_-
=e p_0
=
\frac{e(ac+bd+cd)}{Z}.
}
```

The **net detector-channel current** is

```math
J_D=R_+-R_-.
```

Using the stationary probabilities,

```math
\boxed{
J_D
=
\frac{uac-dbe}{Z}.
}
```

This is also the net clockwise cycle current.

Thus

```math
\boxed{
R_+\neq J_D
}
```

whenever the reverse detector rate is non-negligible.

This distinction is load-bearing for dark-count definitions.

---

## 9. Equilibrium thought check

If the three edges satisfy detailed balance with zero cycle affinity,

```math
u a c=d b e,
```

then

```math
\boxed{J_D=0.}
```

But the gross forward jump rate `R_+` need not vanish.

So a detector whose observable literally counts forward output quanta can register microscopic forward jumps even when the **net thermodynamic current is zero**.

Conversely, a macroscopic current meter sensitive only to net energy flow would naturally report `J_D`.

Therefore the correct dark-count observable depends on the physical readout.

One must not identify a thermodynamic current with a click rate without specifying how the detector channel is monitored.

---

## 10. Cycle affinity and entropy production

For the classical unicyclic rate model, define the dimensionless cycle affinity

```math
\boxed{
\mathcal A
=
\ln\!\frac{uac}{dbe}.
}
```

Under local detailed balance, the steady-state entropy-production rate of the cycle is the standard stochastic-thermodynamic expression

```math
\boxed{
\dot S_i
=k_B J_D\mathcal A
\ge0.
}
```

This is established unicyclic stochastic thermodynamics, not a new repository theorem.

The important detector point is again that entropy production is controlled by the **net cycle current**, whereas a raw jump-counting readout can depend on `R_+`.

---

## 11. Internal versus external false events

The rate `a` on the optical edge should be decomposed conceptually as

```math
a=a_{\rm bg}+a_{\rm sig}
```

for external background and signal-induced excitation in a weak incoherent description.

An optical-background-driven click is produced by a real incoming photon and is therefore not an internal detector dark count.

A clean internal-dark test sets

```math
a_{\rm sig}=0,
\qquad
a_{\rm bg}=0
```

and asks whether the remaining detector/reset reservoirs can populate `|2>` and generate a forward `2 -> 0` event.

In this minimal cycle, with `a=0`,

```math
\boxed{
R_{\rm dc,int}^{(+)}
=
\frac{cde}
{bd+be+bu+cd+cu+de}.
}
```

This is a **gross forward-jump** dark rate for the particular readout definition used here.

It vanishes if either

```math
d=0
```

or

```math
e=0.
```

Exact one-way reset (`d=0`) or exact one-way detector bath (`e=0`) therefore removes this minimal internal false-count path, but either idealization represents an infinite or singular thermodynamic bias in a local-detailed-balance model.

---

## 12. Relation to the 2026 autonomous-machine detector

Schwarzhans et al. define their detector signal through a net detection-channel current containing a forward emission term and a reverse thermal-absorption term.

The present note does not claim that their observable is incorrect; their detector output is explicitly formulated as a current.

Instead it identifies a measurement-choice distinction:

```text
net detector current
versus
gross forward click events.
```

For a true event-resolved click counter, the latter can be the relevant observable. For an energy/current readout, the former can be the correct one.

A future comparison must use the observable corresponding to the actual physical readout rather than translating one into the other silently.

---

## 13. Relation to the 2018 incoming-field framework

Young, Sarovar & Léonard already provide a general quantum framework in which the incoming photon wavepacket, absorption, amplification, monitored-state population, dark counts, and timing can be treated without an artificial field/matter time separation.

The present three-level model is therefore not proposed as a more general quantum detector framework.

Its role is narrower: it makes the **access resource, stored amplification energy, reset cycle, and gross-versus-net count distinction analytically transparent** in one solvable example.

---

## 14. What this model teaches

Within the stated assumptions:

1. the stored metastable energy can amplify the counted output energy without improving conditional optical capture beyond the rate-matching structure;
2. a successful event consumes the ready-state energy resource and creates a reset requirement;
3. the dark steady state is a thermodynamic cycle rather than an isolated reverse rate;
4. gross forward click events and net detector current are distinct observables;
5. equilibrium can have zero net current while still having nonzero microscopic forward/reverse jump activity;
6. internal dark counts and externally admitted thermal/background photons must remain separated.

---

## 15. Claim boundary

### Derived within this minimal model

Single-event conversion:

```math
\boxed{
T_{L\to R}(\omega)
=
\frac{4\Gamma_L\Gamma_R}
{(\omega-\omega_L)^2
+(\Gamma_L+\Gamma_R+\Gamma_I)^2}.
}
```

Integrated conversion:

```math
\boxed{
\mathcal I_{L\to R}
=
\frac{2\Gamma_L\Gamma_R}
{\Gamma_L+\Gamma_R+\Gamma_I}.
}
```

Dark steady-state net current:

```math
\boxed{
J_D
=
\frac{uac-dbe}{Z}.
}
```

Gross forward click rate:

```math
\boxed{
R_+
=
\frac{c(ae+au+de)}{Z}.
}
```

### Not established

- novelty of the three-level architecture;
- a universal gross-click thermodynamic bound;
- that every physical detector counts forward output quanta rather than net current;
- a complete quantum trajectory model of the autonomous work source;
- that the finite passive harmonic theorem remains unchanged for every pumped detector operating point;
- a universal efficiency-bandwidth-entropy-dark-count theorem.

---

## 16. Next decisive attack

The important next question is now precise:

> **Does a nonequilibrium autonomous work source allow the incident optical transition itself to become active enough to evade the passive capture/access theorem, and if so, how much thermodynamic resource is spent in doing so?**

Equivalently, extend the ready-state scattering calculation to a detector whose optical transition is embedded in its autonomous nonequilibrium steady state rather than conditioned on a passive ready state.

This is where the 2018 propagating-field framework and the 2026 autonomous-machine framework genuinely have to meet.

A useful first calculation is the small-signal optical susceptibility/scattering response of the three-level machine around its dark nonequilibrium steady state, followed by a check of whether net optical gain appears when population inversion is supplied by the reset/work source.