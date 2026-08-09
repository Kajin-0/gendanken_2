# HgCdTe Graded Absorber + Wide-Gap Boundary — Drive, Relax, and Keep the Leakage Field Out of the Absorber

**Date:** 2026-08-09  
**Status:** exact two-region result inside the repository mean-energy and minimum-compensation models; no novelty claim

## 1. Purpose

The current branch has separated two mechanisms:

```text
graded quasi-neutral absorber
-> band-structure drive for minority electrons
-> suppresses ordinary direct-Zener overlap
-> may still create hot-electron energy

wide-gap collection boundary
-> must supply barrier-free band alignment
-> carries unavoidable electrostatic field
-> vulnerable to TAT / BTBT.
```

This note asks whether the collection boundary necessarily makes the nonlocal carrier-heating problem worse.

At minimum electrostatic compensation, it does the opposite.

## 2. Absorber exit state

For the linear quasi-neutral p-type graded absorber of `HGCDTE_GRADED_NONLOCAL_II_PHASE_BOUNDARY.md`,

```math
E_g(x)=E_{g0}-Gx,
```

```math
S_c=G,
```

and for constant absorber relaxation length `ell_E,a`,

```math
\boxed{
\varepsilon_a
=\Delta E_g^{(a)}
\frac{1-e^{-L_a/\ell_{E,a}}}
{L_a/\ell_{E,a}}.
}
```

The absorber remains below the repository mean II threshold if

```math
\varepsilon_a
<\chi E_{g,a},
```

where

```math
E_{g,a}=E_{g0}-\Delta E_g^{(a)}.
```

## 3. Wider-gap collection boundary

Let the collection boundary increase the local gap by

```math
\Delta E_g^{(b)}>0.
```

Let `alpha` be the conduction-band share of that material gap increase.

Before electrostatic compensation, the material conduction edge rises by

```math
\alpha\Delta E_g^{(b)}.
```

A potential drop `V_b` lowers the electron band edges by `qV_b`, so the net conduction-edge change is

```math
\boxed{
\Delta E_c^{(b)}
=\alpha\Delta E_g^{(b)}-qV_b.
}
```

Barrier-free electron extraction requires

```math
\boxed{
qV_b\ge\alpha\Delta E_g^{(b)}.
}
```

## 4. Minimum compensation makes the boundary conduction edge flat

At the minimum barrier-free voltage,

```math
\boxed{
qV_b=\alpha\Delta E_g^{(b)},
}
```

so

```math
\boxed{
\Delta E_c^{(b)}=0.
}
```

Thus the useful electron sees no net downhill conduction-band work across the boundary.

The electrostatic field is present, but the rising material conduction edge exactly compensates its energy drop in the total band landscape.

This distinction is essential: hot-carrier work must be computed from the total `E_c(x)` slope, not from the electrostatic field alone in a graded heterostructure.

## 5. The boundary becomes a relaxation region

Let `s` measure distance through the boundary and let the boundary energy-relaxation length be `ell_E,b`.

At minimum compensation,

```math
S_c^{(b)}=0.
```

Therefore

```math
\boxed{
\frac{d\varepsilon}{ds}
=-\frac{\varepsilon}{\ell_{E,b}}.
}
```

With incoming energy `epsilon_a`,

```math
\boxed{
\varepsilon_b(s)
=\varepsilon_a e^{-s/\ell_{E,b}}.
}
```

At the same time the boundary gap increases, so for

```math
E_{\rm th}(s)=\chi E_g(s),
```

the mean II threshold rises downstream.

Hence

```text
electron excess energy decreases
+
local II threshold increases.
```

## 6. No-new-crossing theorem for the minimum-compensation boundary

Suppose the electron enters the boundary below threshold:

```math
\varepsilon_a<\chi E_{g,a}.
```

For every `s>0`,

```math
\varepsilon_b(s)\le\varepsilon_a,
```

while

```math
E_g(s)\ge E_{g,a}.
```

Therefore

```math
\boxed{
\varepsilon_b(s)
<\chi E_g(s)
\quad\text{for all }s.
}
```

So, within the deterministic mean-energy model:

> **a minimally compensated monotonic wider-gap boundary cannot create a new impact-ionization threshold crossing if the carrier entered below threshold.**

This is exact under the stated assumptions.

It does not imply zero stochastic II probability from a high-energy tail.

## 7. Overcompensation reintroduces carrier drive

Define excess compensation voltage

```math
\Delta V
=V_b-\alpha\Delta E_g^{(b)}/q
\ge0.
```

Then the boundary conduction edge drops by

```math
\boxed{
D_c=q\Delta V.
}
```

For a boundary width `w`, a uniform total conduction slope would be

```math
\boxed{
S_c^{(b)}=q\Delta V/w.
}
```

The mean-energy equation becomes

```math
\frac{d\varepsilon}{ds}
=S_c^{(b)}-\frac{\varepsilon}{\ell_{E,b}}.
```

Thus overcompensation spends extra electrostatic field to accelerate the electron through the boundary.

It may reduce boundary transit time, but it also

- increases TAT/BTBT field stress;
- adds hot-electron energy;
- removes part of the relaxation benefit.

So minimum compensation is the lowest-leakage / lowest-heating boundary reference state, while extra compensation is an explicit speed resource that must be justified by a transport calculation.

## 8. Architecture-level interpretation

The current idealized architecture therefore has a natural separation:

```text
quasi-neutral graded absorber
-> use composition-induced Ec slope for collection
-> keep electrostatic field and direct-Zener overlap low

wide-gap boundary
-> supply the unavoidable band-alignment voltage
-> place field in high-gap / low-defect material
-> at minimum compensation keep Ec flat
-> allow hot electrons to relax before the contact/readout region.
```

This does not eliminate TAT, interface states, or stochastic impact ionization. It makes their spatial roles explicit.

## 9. Prior-art boundary

Compositionally graded HgCdTe and carrier-relaxation regions in HgCdTe APDs are established device physics. Recent graded APD work explicitly uses wide-gap gradients for carrier transport and discusses electron relaxation before multiplication.

The present result is only the stripped-down consequence of combining the repository self-consistent grading, boundary compensation, and mean-energy equations.

No novelty claim is made.

## 10. Next decisive model

The next calculation should use a finite profile with

1. a graded quasi-neutral absorber;
2. a transition into the wide-gap boundary;
3. minimum and overcompensated boundary cases;
4. local TAT/BTBT exponent constraints;
5. the nonlocal carrier-energy state across both regions.

The key quantitative unknown remains `ell_E(x,E)` for the target HgCdTe composition and temperature.
