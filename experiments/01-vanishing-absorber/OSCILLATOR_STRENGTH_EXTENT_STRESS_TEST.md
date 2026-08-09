# Oscillator-Strength / Extent Stress Test — Where Perturbative LDOS Theory Runs Out

**Date:** 2026-08-08  
**Status:** analytic stress test of existing constraints; demonstrates insufficiency, not an achievable divergence theorem; no novelty claim  

## 1. Purpose

`FINITE_EMITTER_FORM_FACTOR.md` showed that a finite transition-density size `a` removes the literal point-dipole `d^{-3}` ultraviolet divergence.

It also gave, for one Cartesian direction of a nonrelativistic electric-dipole transition,

```math
f_{ge}^{(x)}
=
\frac{2m\omega_0}{\hbar}|x_{ge}|^2
```

and therefore

```math
\sigma_x
\ge
|x_{ge}|
=
\sqrt{\frac{\hbar f_{ge}^{(x)}}{2m\omega_0}}.
```

A tempting conclusion is that oscillator strength plus this finite wavefunction extent may automatically produce a finite broadband optical-coupling ceiling.

This note stress-tests that conclusion.

The result is negative but useful:

> **The oscillator-strength sum-rule constraint and finite-emitter size constraint, by themselves, do not algebraically yield a finite perturbative coupling ceiling when the oscillator strength of the selected transition is also allowed to vary.**

The apparent divergence instead drives the calculation into the ultrastrong/nonperturbative regime where the decay-rate / Purcell picture used to obtain it ceases to be self-consistent.

---

## 2. Bare radiative rate of one directional transition

Let the electric-dipole matrix element be

```math
\mathbf d=e\langle g|\mathbf r|e\rangle.
```

For one transition polarized along `x`, use

```math
f_x
=
\frac{2m\omega_0}{\hbar}|x_{ge}|^2.
```

The free-space electric-dipole population-decay rate is

```math
\Gamma_0
=
\frac{\omega_0^3e^2|x_{ge}|^2}
{3\pi\epsilon_0\hbar c^3}.
```

Eliminating `|x_ge|^2` gives

```math
\boxed{
\Gamma_0
=
\frac{e^2\omega_0^2}{6\pi\epsilon_0mc^3}
f_x.
}
```

Define

```math
\alpha
=\frac{e^2}{4\pi\epsilon_0\hbar c},
\qquad
\lambda_C
=\frac{\hbar}{mc},
\qquad
k_0=\frac{\omega_0}{c}.
```

Then

```math
\boxed{
\frac{\Gamma_0}{\omega_0}
=\frac23\alpha f_x k_0\lambda_C.
}
```

For ordinary optical/infrared transitions this bare fractional linewidth is small.

---

## 3. Minimum extent associated with a fixed nonzero transition strength

From Cauchy-Schwarz,

```math
\sigma_x\ge |x_{ge}|.
```

Using the oscillator-strength definition,

```math
\boxed{
\sigma_x
\ge
\ell_f
\equiv
\sqrt{
\frac{\hbar f_x}{2m\omega_0}
}
=
\sqrt{
\frac{f_x\lambda_C}{2k_0}
}.
}
```

For **fixed nonzero `f_x`**, this indeed gives a nonzero microscopic length.

The key question is what happens if the selected transition strength itself is allowed to become small.

---

## 4. Generic finite-emitter near-field envelope

The previous finite-emitter calculation showed that replacing a point transition by a finite transition-density form factor turns a local near-field `d^{-3}` divergence into a finite contact scaling of the form

```math
\rho_{\rm nf}
\sim
\frac{1}{a^3}
```

for a characteristic emitter size `a`.

To keep this stress test independent of one exact Gaussian convention, write an optimistic perturbative LDOS-enhancement envelope as

```math
\boxed{
F_{\rm LDOS}
\lesssim
\frac{C_{\rm env}}
{(k_0a)^3},
}
```

where `C_env` is a dimensionless factor containing the allowed passive material response, orientation, bandwidth weighting, and geometry.

This is **not** asserted as a universal exact coefficient. It represents the common high-`k` cubic scaling after the transition's own form factor has supplied the ultraviolet cutoff.

If the smallest allowed emitter scale is estimated by

```math
a=\ell_f,
```

then

```math
k_0a
=
\sqrt{\frac{f_xk_0\lambda_C}{2}}.
```

Therefore

```math
\boxed{
F_{\rm LDOS}
\lesssim
C_{\rm env}
\left(
\frac{2}{f_xk_0\lambda_C}
\right)^{3/2}.
}
```

---

## 5. The combined perturbative envelope does not close

In the weak-coupling Markov picture, the environmentally enhanced radiative rate is estimated as

```math
\Gamma_{\rm pert}
\sim
\Gamma_0F_{\rm LDOS}.
```

Combining the previous expressions gives

```math
\boxed{
\frac{\Gamma_{\rm pert}}{\omega_0}
\lesssim
\frac{2^{5/2}}{3}
\frac{\alpha C_{\rm env}}
{\sqrt{f_xk_0\lambda_C}}.
}
```

Thus the **upper envelope allowed by these inequalities grows as**

```math
\boxed{
f_x^{-1/2}}
```

when the selected oscillator strength tends to zero.

This does **not** prove that a physical sequence of emitters achieves a divergent decay rate.

It proves something narrower and important:

> The presently retained constraints — one-transition oscillator strength, Cauchy-Schwarz wavefunction extent, and a local finite-emitter `a^{-3}` LDOS envelope — are insufficient to derive a finite upper bound by algebra alone.

A weak transition can carry a smaller dipole moment while the associated minimum size inferred from that same matrix element shrinks even faster in the cubic near-field enhancement factor.

---

## 6. Relation to the halfspace coefficient used previously

For the narrowband orientation-averaged halfspace scaling in `FINITE_TRANSITION_LDOS_BANDWIDTH_BOUND.md`, one may schematically write

```math
C_{\rm env}
\sim
\frac{M}{8},
```

where `M` denotes the relevant dimensionless material-response factor after the bandwidth approximation.

Then

```math
\boxed{
\frac{\Gamma_{\rm pert}}{\omega_0}
\lesssim
\frac{\sqrt2}{6}
\frac{\alpha M}
{\sqrt{f_xk_0\lambda_C}}.
}
```

The formal crossover at which this perturbative upper envelope becomes order unity occurs at roughly

```math
\boxed{
f_x
\sim
\frac{\alpha^2M^2}
{18k_0\lambda_C}.
}
```

This crossover should **not** be interpreted as an achievable design formula. It marks where the assumptions behind a rate-enhancement calculation can become self-inconsistent.

---

## 7. Why `Gamma / omega_0 ~ 1` is a theory boundary

The LDOS / Fermi-golden-rule / Markov picture assumes that the emitter can still be described as an approximately fixed transition weakly coupled to a reservoir characterized by a decay rate.

When the light-matter interaction becomes comparable with the bare optical frequencies, that decomposition fails.

Established ultrastrong-coupling theory requires, depending on representation and microscopic model,

- counter-rotating interactions;
- gauge-consistent treatment of the light-matter Hamiltonian;
- diamagnetic / `A^2` contributions or their gauge-equivalent counterparts;
- higher matter levels when a two-level truncation is no longer controlled;
- dressed-system rather than bare-cavity master equations.

De Bernardis et al., *Physical Review A* 98, 053819 (2018), explicitly show that two-level approximations become gauge-sensitive in ultrastrong coupling and analyze double-well and square-well dipoles.

De Bernardis, Jaako & Rabl, *Physical Review A* 97, 043820 (2018), develop a nonperturbative cavity-QED framework for strongly coupled dipoles and LC fields.

These are prior theory, not repository novelty.

---

## 8. Stronger coupling does not imply indefinitely faster irreversible emission

There is an especially relevant prior warning against extrapolating the Purcell picture monotonically.

De Liberato, *Physical Review Letters* 112, 016401 (2014), analyzes the deep-strong-coupling regime and finds a regime in which increasing coupling leads to **light-matter decoupling**; the ordinary Purcell enhancement reverses and spontaneous emission decreases rather than increasing indefinitely.

This is model-dependent prior physics, not a universal theorem for all detector architectures.

But it directly invalidates the extrapolation

```text
larger local field / LDOS
-> arbitrarily larger Markov decay rate
-> arbitrarily faster detector
```

once the system has entered a nonperturbative light-matter regime.

---

## 9. What has been falsified and what has not

### Falsified as a sufficient argument

The following chain is **not sufficient** to establish a universal detector bound:

```text
TRK oscillator-strength constraint
+
finite wavefunction extent
+
local finite-emitter LDOS cutoff
-> finite universal optical coupling rate.
```

The inequalities currently retained do not close because their perturbative envelope can grow as `f_x^{-1/2}`.

### Not established

This note does **not** establish that:

- a physical family of optical transitions can achieve the formal `f_x -> 0` divergence;
- deep-strong coupling permits arbitrarily fast detection;
- light-matter decoupling occurs in every relevant photodetector geometry;
- the exact detector optimum lies at `Gamma/omega_0 ~ 1`;
- a universal nonperturbative optical-coupling bound has been derived.

---

## 10. The resource that is now missing

The weak-coupling description treated the emitter's transition and the electromagnetic environment as separable resources.

The stress test shows that this separation itself breaks down at the edge of the problem.

A more fundamental optical statement must constrain the **combined microscopic Hamiltonian**, including at least

- the complete spectrum of matter states rather than one chosen oscillator strength;
- the charge/mass content generating the optical transitions;
- the full transition/current density rather than a point dipole;
- the electromagnetic mode structure and its microscopic material degrees of freedom;
- gauge-required self-interaction/diamagnetic terms;
- the bandwidth of the incident channel.

The next question is therefore not another weak-coupling LDOS optimization.

It is:

> **Does a gauge-consistent nonperturbative light-matter Hamiltonian impose a finite upper bound on irreversible capture rate or usable detector bandwidth for a fixed set of charged degrees of freedom and a specified incident channel?**

This is a substantially deeper problem and should be attacked with the simplest exactly solvable nonperturbative model before attempting a general theorem.

---

## 11. Recommended next model

The cleanest next step is a **Hopfield-type microscopic absorber** rather than another two-level Markov model:

1. one material oscillator with fixed charge/mass oscillator-strength budget;
2. one electromagnetic resonant mode or one explicitly normalized waveguide channel;
3. the gauge-required quadratic field/self-polarization term;
4. an irreversible detector reservoir coupled to the material coordinate;
5. exact diagonalization of the lossless light-matter sector at arbitrary coupling;
6. then weak coupling of the resulting polaritons to the input/output and detection reservoirs.

The first question is qualitative and decisive:

> As nominal bare light-matter coupling is increased without bound, does the maximum irreversible photon-capture rate saturate, decrease, or continue to grow?

Do not infer the answer from the Purcell regime.