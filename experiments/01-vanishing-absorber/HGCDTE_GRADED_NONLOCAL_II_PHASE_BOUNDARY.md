# HgCdTe Graded Nonlocal Carrier-Energy Phase Boundary

**Date:** 2026-08-09  
**Status:** exact mean-energy result inside the repository one-relaxation-length surrogate; no novelty claim

## Question

A quasi-neutral p-type HgCdTe gradient can approximately pin the valence band while a decreasing gap gives minority electrons a downhill conduction-band slope. This suppresses the ordinary same-direction direct-Zener geometry.

Does the same grading also remove hot-electron energy buildup?

No. The carrier energy depends on the total conduction-band slope, independent of whether that slope came from electrostatics or composition.

## General graded-band energy history

Define

```math
S_c(x)=-dE_c/dx>0.
```

For mean excess energy `epsilon(x)` and energy-relaxation length `ell_E(x)`, use

```math
\boxed{
\frac{d\varepsilon}{dx}
=S_c(x)-\frac{\varepsilon}{\ell_E(x)}.
}
```

For cold injection,

```math
\boxed{
\varepsilon(x)=
\int_0^x S_c(s)
\exp\!\left[-\int_s^x\frac{du}{\ell_E(u)}\right]ds.
}
```

This is path dependent. Therefore nonlocal carrier heating should not be hidden inside a purely local field ceiling in the thin/fast regime.

## Linear quasi-neutral p-type gradient

Take

```math
E_v\approx\text{constant},
```

```math
E_g(x)=E_{g0}-Gx,
```

so

```math
E_c(x)=E_{c0}-Gx,
\qquad S_c=G.
```

For constant `ell_E`,

```math
\boxed{
\varepsilon(x)=G\ell_E(1-e^{-x/\ell_E}).
}
```

Let the graded region length be `L`, define

```math
\Delta E_g=GL,
\qquad
r=L/\ell_E,
```

and

```math
A(r)=\frac{1-e^{-r}}{r}.
```

Then

```math
\boxed{
\varepsilon(L)=\Delta E_g A(r).
}
```

## Local pair-creation threshold

Use the standard HgCdTe APD simplification

```math
\boxed{
E_{\rm th}(x)=\chi E_g(x),
}
```

with `chi` of order unity.

Because `epsilon(x)` rises while `E_th(x)` falls, the mean trajectory reaches threshold inside the gradient iff it reaches threshold by the exit.

Define

```math
\zeta=\Delta E_g/E_{g0}.
```

The threshold condition is

```math
\zeta A(r)\ge\chi(1-\zeta).
```

Hence the exact phase boundary is

```math
\boxed{
\zeta_{\rm II}(r,\chi)
=\frac{\chi}
{\chi+(1-e^{-r})/r}.
}
```

The mean-energy threshold is accessible when

```math
\boxed{
\zeta\ge\zeta_{\rm II}.
}
```

## Ballistic limit

For `L/ell_E -> 0`,

```math
\boxed{
\zeta_{\rm II}\to\frac{\chi}{1+\chi}.
}
```

For `chi=1`,

```math
\boxed{
\zeta_{\rm II}=1/2.
}
```

Equivalently, in the ballistic graded limit,

```math
\varepsilon=E_{g0}-E_g,
```

so threshold access occurs when

```math
\boxed{
E_g=\frac{E_{g0}}{1+\chi}.
}
```

For `chi=1`, the local gap has fallen to one half of its entrance value.

## Strong relaxation

For `L >> ell_E`,

```math
\frac{1-e^{-r}}{r}\simeq\frac{\ell_E}{L},
```

and

```math
\boxed{
\zeta_{\rm II}\simeq
\frac{\chi}{\chi+\ell_E/L}.
}
```

Strong energy relaxation pushes the mean threshold toward nearly complete gap reduction.

This does not eliminate stochastic ionization by the high-energy tail.

## Physical interpretation

The grading affects two mechanisms differently:

```text
direct Zener tunneling
-> depends on relative Ec/Ev geometry
-> grading can strongly suppress it at fixed conduction drive

carrier heating
-> depends on total downhill Ec slope
-> grading does not remove the energy supplied to the useful electron
```

Moreover, the local pair-creation threshold falls as the gap falls.

Thus the penalty can migrate from direct interband tunneling to nonlocal hot-electron physics.

## Correction to the local-tolerance picture

`HGCDTE_TAT_TOLERANCE_FIELD_ALLOCATION.md` is appropriate for local inverse-field tunneling constraints such as TAT/BTBT.

For nonlocal carrier heating, use the path-dependent energy state

```math
\varepsilon(x)=
\int_0^x S_c(s)
\exp\!\left[-\int_s^xdu/\ell_E(u)\right]ds
```

unless a local-equilibrium reduction has been justified.

## Prior-art boundary

Established HgCdTe work already shows composition-gradient carrier drive and energy-dependent impact-ionization physics. Recent HgCdTe APD Monte Carlo models explicitly evolve electron energy and evaluate an energy-dependent ionization probability, often using a threshold close to the local gap.

The formula above is a reduction inside the repository surrogate. Priority of the exact dimensionless phase boundary has not been established.

## Next step

Carry this nonlocal energy state through a finite graded absorber plus collection boundary while imposing TAT/BTBT locally. The key missing material input remains a trustworthy energy-relaxation model for the target HgCdTe composition and temperature.
