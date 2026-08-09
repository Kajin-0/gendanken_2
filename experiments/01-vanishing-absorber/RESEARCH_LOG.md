# Research Log — Experiment 01: The Vanishing Absorber

Chronological recovery log. Dedicated derivation files preserve the full algebra; this file records **why the direction changed**.

## 2026-08-08 — Experiment opened

Starting question:

> Can an ideal photodetector be made arbitrarily small, fast, sensitive, and perfectly absorbing?

No theorem was assumed.

## One-port resonator

Unity resonant absorption survived for arbitrarily weak absorber loss only by narrowing temporal response. This established the first penalty migration but only in a single-resonance model.

## Active-volume route killed

A shrinking-gap field-concentration counterexample kept finite optical participation while `V_a -> 0`.

**Direction change:** geometric active volume is not the fundamental optical resource.

## Microscopic optical chain

Finite absorber number did not impose a one-photon speed ceiling. LDOS/emitter-size bounds eventually ran into the breakdown of weak-coupling Purcell theory.

**Direction:** treat light and matter nonperturbatively.

## Hopfield / deep-strong branch

A fixed-target Hopfield calculation showed that extreme internal coupling can collapse at least one required external access. Scaling external reservoirs can compensate, but spends a new resource.

Deep-strong decoupling itself is known prior physics. Exact fixed-target corollary retained only as **candidate distinct supporting lemma; priority unproven**.

## Passive multimode theorem

Mode proliferation killed single-resonance bandwidth reasoning but led to a stronger aggregate quantity.

For finite passive strictly proper optical-to-detector networks,

```math
\boxed{
\mathcal I_{L\to R}
\le
\frac{2LR}{L+R}.
}
```

A matched single resonance saturates the bound.

`H_2`/Lyapunov/passivity ingredients are standard; novelty not claimed.

## Feedthrough / continua / autonomous-detector collisions

Ideal direct feedthrough imports infinite Markov bandwidth. Finite passive augmented structured reservoirs retain the harmonic bound.

Major prior-art collisions:

- Young, Sarovar & Leonard (2018): incoming quantum field + absorption + amplification + efficiency/dark-count/timing framework.
- Schwarzhans et al. (2026): autonomous detector thermodynamics, work/reset, dark counts, jitter/dead time, entropy production.

**Decision:** do not reinvent generic capture/amplification or autonomous detector thermodynamics.

## Active conversion / time-dependent capture

Pumped conversion exposed pump/control resources. Known-time dynamic loading can perfectly match one temporal mode but requires controlled coupling and fails as an always-on solution when arrival time is unknown.

Adaptive control moves capacity into measurement/output record dimensions. An unrestricted output continuum exports that distinguishability.

**Decision:** stop stacking abstract detector-resource coordinates and return to actual semiconductor physics.

## Fermi-contact extraction

Sequential tunneling made extraction and reverse thermal loading explicit through Fermi detailed balance.

Finite linewidth then showed that even at `T=0`, a broadened collecting state can overlap occupied states.

## Multipole filter counterexample

Higher-order filters suppress leakage tails much faster at fixed FWHM, but add group/Wigner delay and state count.

**Correction:** spectral FWHM is not architecture-independent carrier speed.

## HgCdTe field-driven collection

Transit contribution:

```math
B_{\rm tr}=c_t v/L,
\qquad c_t\simeq0.44295.
```

Low-field `v=mu F` could not be extrapolated into high field.

## HgCdTe Kane / direct-BTBT normalization

Using a published direct-BTBT expression plus simplified Kane mass relation:

```math
\boxed{j=x^2e^{-1/x},}
```

with

```math
x=F/F_K,
```

```math
F_K\propto\lambda_c^{-2},
```

```math
J_K\propto L\lambda_c^{-4}.
```

An exact Lambert-W field inversion was obtained for a stated BTBT current budget.

## Bulk high-field onset corrected by finite dead space

Bulk `Hg_0.8Cd_0.2Te`, 77 K Monte Carlo work shows non-ohmic/hot-electron/II activity at fields of order `10^2 V/cm`.

This was initially in danger of being misread as a finite-device II threshold.

Correction:

```math
\boxed{
F_{\rm dead}\simeq\chi E_g/(qL),
}
```

and

```math
\boxed{
F_{\rm dead}/F_K
=(4\chi/\pi)(\ell_K/L).
}
```

Finite II probability is nonlocal and depends on carrier energy history.

## Nonlocal mean-energy surrogate

A one-relaxation-time energy model gave

```math
\boxed{
L_{\rm eff}
=\ell_E(1-e^{-L/\ell_E}),
}
```

and

```math
F_{\rm th}^{(\rm mean)}
=\Delta E_{\rm th}/(qL_{\rm eff}).
```

For an analytic energy-dependent II-rate test case, a closed hazard `P_II=1-e^{-Xi}` was derived and numerically checked.

## Relaxation-length phase boundary

Instead of demanding a full unknown `tau_E(F)` interpolation, the project solved for the critical relaxation length at which mean-II threshold and a chosen BTBT budget exchange order:

```math
\frac{1-e^{-y_*}}{y_*}=r,
\qquad
r=F_{\rm dead}/F_J,
```

```math
\boxed{
y_*=1/r+W_0[-r^{-1}e^{-1/r}].}
```

For ordinary LWIR examples, the critical `tau_E` lies in the sub-ps/few-ps regime.

Primary data do not currently justify assigning the target high-field value exactly.

## TAT becomes the more realistic early tunneling channel

A simple HgCdTe TAT exponent gives

```math
\boxed{
F_{\rm TAT}/F_K
=\frac{16}{3\pi}(\Delta_t/E_g)^{3/2}.
}
```

Near-band-edge traps can therefore reduce the tunneling exponent field by orders of magnitude relative to direct BTBT.

Measured/fitted LWIR HgCdTe studies report technologically realistic TAT trap densities around `10^13–10^14 cm^-3` in some devices.

A TAT/BTBT current ratio and crossover trap-density condition were derived.

**Direction:** treat field allocation as a materials-quality problem, not a single intrinsic BTBT ceiling.

## Homogeneous field-shaping attack

Could a nonuniform `F(x)` give the same transit time with less local WKB leakage?

For

```math
v(F)=\mu F/[1+(F/d)^r],
```

and

```math
g(F)=AF^pe^{-K/F},
```

leakage is strictly convex as a function of reciprocal velocity over the rising branch; the falling branch is dominated.

Therefore

```math
\boxed{G[F]\ge Lg(F_0)}
```

at fixed transit time, with equality only for uniform field.

**Direction change:** field shaping alone is not the escape; heterogeneity is.

## Two-region heterostructure allocation

For spatially varying local laws, the optimum satisfies

```math
\boxed{
-\frac{\partial g/\partial F}
{\partial(1/v)/\partial F}
=\lambda.
}
```

Interpretation:

> Put field where the local material buys the most transit improvement per unit leakage cost.

A dimensionless two-region example lowered modeled leakage by ~20.6% at the same transit time.

## Voltage cost of redistribution

For ohmic spatial transport,

```math
\boxed{
VT
\ge
\left[\int dx/\sqrt{\mu(x)}\right]^2.
}
```

The same two-region example required only ~2.2% extra bias for the ~20.6% leakage reduction.

Thus heterostructure field protection consumes voltage but can have exponential leakage leverage.

## Bandgap-gradient escape

Composition grading changes the Hamiltonian rather than merely redistributing one field variable.

Using

```math
H=U I+v_Kp\sigma_x+\Delta\sigma_z,
```

```math
E_c=U+\Delta,
\qquad
E_v=U-\Delta,
```

a gap gradient can slope the conduction band while pulling the valence edge in the opposite direction.

This suggested a genuine escape from the homogeneous electrostatic speed–Zener tradeoff.

Primary HgCdTe work confirms composition-gradient built-in/quasi-electric carrier-driving fields are real and technologically used.

## 2026-08-09 — Exact linear graded-gap Kane WKB result

For linear band edges

```math
E_c=E_{c0}-S_cx,
```

```math
E_v=E_{v0}-S_vx,
```

the forbidden-region WKB action integrates exactly:

```math
\boxed{
\mathcal S(E)
=\frac{\pi\sqrt{S_cS_v}}
{4\hbar v_K}(x_c-x_v)^2.
}
```

The constant-gap/common-field limit recovers the previous Kane exponent.

Decompose

```math
S_c=S_U+S_\Delta,
\qquad
S_v=S_U-S_\Delta.
```

Hold useful conduction slope `S_c=S` fixed and define

```math
\eta=S_\Delta/S.
```

For `0<=eta<1/2`,

```math
\boxed{
\frac{\mathcal S_Z(\eta)}
{\mathcal S_Z(0)}
=\frac{(1-\eta)^2}
{(1-2\eta)^{3/2}}.
}
```

This is strictly increasing.

As `eta -> 1/2-`, the valence turning point recedes and the action diverges. For stronger grading, if the finite region remains positive-gap and terminates before gap closure, that conventional two-turning-point direct-Zener path is absent inside the ideal model.

A direct numerical WKB integration reproduces the closed formula.

### Prior-art status

Graded HgCdTe, WKB graded-gap analysis, Kane/Zener tunneling and analytical heterojunction band profiles are established prior work.

A focused search did **not** locate this exact fixed-conduction-slope ratio.

Verdict:

> **exact internally derived linear-profile WKB corollary; priority unassessed; no novelty claim.**

## Current direction

The next attack is self-consistent and finite:

```text
realistic HgCdTe composition profile
+
band-offset partition
+
Poisson electrostatics
-> full Ec(x), Ev(x)
-> transit
-> direct WKB
-> TAT/interface states
-> nonlocal II.
```

Do not return to a uniform-field detector estimate or open a manuscript yet.