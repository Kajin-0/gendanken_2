# Finite Emitter Form Factor — Regularizing the Point-Dipole Near-Field Divergence

**Date:** 2026-08-08  
**Status:** exact analytic toy regularization plus known finite-wavefunction prior-art context; no novelty claim  

## 1. Purpose

The preceding LDOS power-bandwidth analysis showed that a point transition near a constrained passive environment has a finite coupling ceiling at fixed emitter-environment separation `d`, but the local point-dipole bound grows as `d^(-3)` and therefore loses content as `d -> 0`.

This note asks whether the transition itself supplies a physical spatial cutoff before an arbitrary fabrication distance is imposed.

The answer is yes at the model level:

> A spatially extended transition density suppresses arbitrarily large wave-vector coupling, replacing the point-dipole `d^(-3)` divergence by a finite scale set by the emitter wavefunction size.

This mechanism is established in more complete finite-wavefunction QED treatments. The calculation below is a deliberately simple planar/high-`k` model that makes the scaling transparent.

---

## 2. Point-emitter near-field scaling

For an electric dipole near a planar local-response interface, the quasistatic high-transverse-wave-vector contribution to the electric LDOS has the generic structure

```math
\rho_{\rm nf}
\propto
\int_0^\infty
K^2 e^{-2Kd}
\operatorname{Im}r_p(K,\omega)
\,dK,
```

where

- `K` is in-plane wave vector;
- `d` is emitter-interface separation;
- `r_p` is the `p`-polarized reflection amplitude.

For a local dielectric response,

```math
r_p(K,\omega)
\to r_\infty(\omega)
```

at sufficiently large `K`.

Factoring out the asymptotic reflection amplitude leaves the point-source integral

```math
I_{\rm point}(d)
=
\int_0^\infty K^2e^{-2Kd}\,dK.
```

Exactly,

```math
\boxed{
I_{\rm point}(d)
=\frac{1}{4d^3}.
}
```

This is the familiar geometric origin of the local near-field `d^(-3)` scaling.

The divergence arises because a point source has nonzero Fourier weight at arbitrarily large `K`.

---

## 3. Extended transition-density model

Replace the point transition by a finite transition polarization whose transverse Fourier coupling is Gaussian.

Define the squared spatial form factor by

```math
\boxed{
|F(K)|^2
=e^{-a^2K^2},
}
```

where `a` is a characteristic transition-density radius.

The exact meaning of `a` depends on the chosen real-space convention; only the high-`K` cutoff behavior matters for this toy model.

The near-field integral becomes

```math
I(d,a)
=
\int_0^\infty
K^2
e^{-2Kd-a^2K^2}
\,dK.
```

This integral can be evaluated exactly.

Writing

```math
u=\frac{d}{a},
```

one obtains

```math
\boxed{
I(d,a)
=
\frac{1}{4a^3}
\left[
\sqrt\pi(1+2u^2)e^{u^2}\operatorname{erfc}(u)
-2u
\right].
}
```

The dimensions are `length^(-3)`, as required.

---

## 4. Limiting cases

### 4.1 Far from the emitter-size scale

For

```math
d\gg a,
```

the Gaussian form factor is approximately unity over the wave vectors selected by `e^{-2Kd}`.

The asymptotic expansion gives

```math
\boxed{
I(d,a)
\to
\frac{1}{4d^3}
}
```

at leading order.

Thus the extended transition reproduces the point-dipole result when the emitter is far enough from the interface compared with its own spatial extent.

### 4.2 Vanishing geometric separation

At

```math
d=0,
```

the exact integral remains finite:

```math
\boxed{
I(0,a)
=
\frac{\sqrt\pi}{4a^3}.
}
```

Therefore the point-source divergence is replaced by the finite emitter-size scale

```math
\boxed{
\rho_{\rm nf,max}
\propto a^{-3}
}
```

within this local planar toy model.

The source cannot couple efficiently to spatial Fourier components with

```math
K\gg a^{-1}.
```

---

## 5. Effective short-distance cutoff

It is sometimes useful to ask what point-emitter separation would produce the same high-`K` integral as the extended emitter at geometric contact.

Set

```math
\frac{1}{4d_{\rm eff}^3}
=
\frac{\sqrt\pi}{4a^3}.
```

Then

```math
\boxed{
d_{\rm eff}
=\pi^{-1/6}a
\approx0.909\,a.
}
```

This does **not** mean finite-size physics is literally equivalent to moving a point dipole away from the surface. It is only a convenient way to compare the leading `K^2` integral.

The physical statement is that the transition-density form factor supplies its own high-wave-vector cutoff.

---

## 6. Why this is not merely an ad hoc cutoff

A first-principles finite-wavefunction treatment by Scala, Pepe, Facchi, Pascazio & Słowik, *New Journal of Physics* 22, 123047 (2020), DOI `10.1088/1367-2630/abd204`, derives the atom-field interaction without the point-dipole approximation.

Their calculation shows that

- point-like Green-tensor contributions can become nonintegrable at high momentum;
- the natural finite spatial extent of the atomic wavefunctions regularizes the relevant decay-rate terms;
- the characteristic momentum cutoff is of order the inverse spatial size of the participating wavefunctions;
- medium granularity introduces another competing microscopic length/momentum scale.

The Gaussian model above is not their derivation. It is a transparent analytical proxy for the same physical mechanism.

No novelty is claimed for finite-emitter regularization.

---

## 7. A transition-strength lower bound on state extent

The finite emitter radius `a` should not simply be inserted as a free fabrication parameter.

For one nonrelativistic particle and one Cartesian direction `x`, define the transition oscillator strength

```math
\boxed{
f_{ge}^{(x)}
=
\frac{2m\omega_0}{\hbar}
|x_{ge}|^2,
}
```

where

```math
x_{ge}=\langle g|x|e\rangle.
```

For a single electron, the Thomas-Reiche-Kuhn sum rule constrains the sum of these directional oscillator strengths over all final states.

Now define the ground-state centered coordinate

```math
\widetilde x_g
=x-\langle g|x|g\rangle.
```

Because `g` and `e` are orthogonal,

```math
\langle g|\widetilde x_g|e\rangle
=x_{ge}.
```

Cauchy-Schwarz gives

```math
|x_{ge}|^2
\le
\langle g|\widetilde x_g^2|g\rangle
\equiv
\sigma_{x,g}^2.
```

The same argument centered on the excited state gives

```math
|x_{ge}|^2
\le
\sigma_{x,e}^2.
```

Therefore any transition carrying nonzero oscillator strength obeys

```math
\boxed{
\sigma_{x,g},\sigma_{x,e}
\ge
|x_{ge}|
=
\sqrt{
\frac{\hbar f_{ge}^{(x)}}
{2m\omega_0}
}.
}
```

This is a genuine microscopic length scale tied to the transition strength and frequency rather than to lithography.

---

## 8. What this does and does not solve

For a **fixed nonzero oscillator strength**, the preceding inequality prevents the wavefunction extent from being taken to zero independently of the optical transition matrix element.

That is progress: the ultraviolet cutoff and the optical coupling are no longer unrelated free parameters.

But it does **not** yet produce a universal detector bound.

The loopholes are now more subtle:

1. The oscillator strength of one chosen transition can be made small while total oscillator strength is redistributed among other transitions.
2. The Gaussian `a` is a model form-factor scale, whereas a real transition density can have anisotropic or nodal structure.
3. The surrounding medium also becomes spatially nonlocal and granular at large `K`.
4. A transition embedded in the same material that provides the field concentration cannot cleanly be separated into a point emitter plus external halfspace.
5. Strong/ultrastrong coupling invalidates the simple Markov spontaneous-emission picture.

Thus the finite-emitter calculation closes the literal point-source divergence but does not yet close the full detector thought experiment.

---

## 9. Candidate combined resource

The optical branch now suggests that a meaningful microscopic resource must involve **both** transition strength and spatial extent.

A schematic pair is

```math
\left(f_{ge},\ a\right)
```

with the constraint

```math
\boxed{
a
\gtrsim
\sqrt{\frac{\hbar f_{ge}}{2m\omega_0}}
}
```

for an appropriate directional extent and oscillator-strength definition.

The surrounding electromagnetic structure contributes a second nonlocal length/material response.

An eventual bound may therefore need a full transition-density functional rather than a scalar `V_a`, `d`, or even `f` alone.

---

## 10. Current conclusion

The sequence is now:

```text
point dipole + local medium
    -> d^(-3) near-field divergence

finite transition density
    -> high-K form factor suppresses coupling
    -> contact response finite ~ a^(-3)

fixed nonzero oscillator strength
    -> state extent cannot be taken independently to zero
```

This identifies a real microscopic spatial resource, but it is not yet a closed universal theorem.

The next decisive test should ask whether **transition oscillator strength plus finite transition-density extent** is sufficient to bound useful broadband coupling, or whether one can still evade the bound by redistributing oscillator strength / shaping the transition density / exploiting the environment's own microscopic nonlocality.

A parallel route is to model the surrounding electron gas nonlocally; that should be treated as a separate ultraviolet regularization and compared with the emitter-size cutoff rather than conflated with it.