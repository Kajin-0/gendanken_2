# HgCdTe Mean-II-Safe Transit Ceiling — Gap-Drop Drive Versus Required Energy-Relaxation Distance

**Date:** 2026-08-09  
**Status:** exact inversion of the graded mean-energy phase boundary plus a Kane-velocity kinematic bound; conditional model result; no novelty claim

## 1. Purpose

`HGCDTE_GRADED_NONLOCAL_II_PHASE_BOUNDARY.md` gives the mean-energy safety boundary for a linear quasi-neutral p-type graded absorber:

```math
\zeta
<
\frac{\chi}
{\chi+(1-e^{-r})/r},
```

with

```math
\zeta=\Delta E_g/E_{g0},
\qquad
r=L/\ell_E.
```

This note inverts that relation.

Question:

> If a design uses a specified fraction of the entrance gap as downhill conduction-band drive, what minimum energy-relaxation distance and transit time are required to remain below the deterministic mean II threshold?

## 2. Ballistic-safe regime

As `r -> 0`,

```math
\zeta_{\rm II}\to\frac{\chi}{1+\chi}.
```

Therefore if

```math
\boxed{
\zeta
\le
\frac{\chi}{1+\chi},
}
```

the cold ballistic mean-energy trajectory remains below the threshold surrogate throughout the linear gradient.

Within this particular model, II does not impose a minimum `L/ell_E` in that regime.

Other speed/leakage constraints still apply.

## 3. Relaxation-required regime

For

```math
\zeta>\frac{\chi}{1+\chi},
```

define

```math
\boxed{
a
\equiv
\chi\frac{1-\zeta}{\zeta}.
}
```

Then

```math
0<a<1.
```

The mean-II safety boundary is obtained from

```math
\boxed{
\frac{1-e^{-r_{\min}}}{r_{\min}}=a.
}
```

Because `(1-e^-r)/r` decreases monotonically from `1` to `0`, there is one positive solution.

## 4. Exact Lambert-W solution

Starting from

```math
1-ar=e^{-r},
```

set

```math
y=1-ar.
```

The positive solution is

```math
\boxed{
r_{\min}
=
\frac1a
+
W_0\!\left[
-\frac1a e^{-1/a}
\right].
}
```

The `W_{-1}` branch gives the trivial `r=0` root of the rearranged equation and is not the physical positive solution for `0<a<1`.

Thus mean-II-safe operation requires

```math
\boxed{
L
\ge
\ell_E r_{\min}.
}
```

Strict inequality is appropriate if the design must remain below rather than exactly at the mean threshold.

## 5. Representative dimensionless values for `chi=1`

| fractional gap drop `zeta` | `r_min = L/ell_E` |
|---:|---:|
| 0.50 | 0 |
| 0.55 | 0.416 |
| 0.60 | 0.874 |
| 0.70 | 2.026 |
| 0.80 | 3.921 |
| 0.90 | 8.999 |
| 0.95 | 19.000 |

The required relaxation distance rises rapidly as the final gap approaches zero.

## 6. Kane-velocity kinematic lower bound on transit time

In the simplified two-band/Kane dispersion

```math
(E-U)^2
=\Delta^2+(\hbar v_Kk)^2,
```

the group velocity magnitude is bounded by the Kane velocity:

```math
\boxed{|v_g|<v_K.}
```

Therefore any carrier crossing a region of length `L` satisfies

```math
\boxed{
T_{\rm tr}
\ge
\frac{L}{v_K}.
}
```

Combining with the mean-II-safe length requirement gives

```math
\boxed{
T_{\rm tr}
\ge
\frac{\ell_E}{v_K}
\left\{
\frac1a
+W_0\!\left[-\frac1a e^{-1/a}\right]
\right\}.
}
```

This is a **kinematic lower bound**. Real scattering and non-ballistic transport generally make the transit time longer.

## 7. Conditional transit-bandwidth form

For the ideal single-carrier rectangular induced-current pulse, the normalized frequency response is a sinc and its `-3 dB` point is approximately

```math
f_{3\rm dB}\tau_{\rm tr}\simeq0.443.
```

Under that specific convention,

```math
\boxed{
B_{\rm tr}
\lesssim
0.443\frac{v_K}
{\ell_E r_{\min}}.
}
```

This bandwidth form is not universal. The robust statement is the transit-time lower bound above.

## 8. Physical interpretation

The design variable `zeta` measures how much of the entrance bandgap is spent as downhill conduction-band energy.

If `zeta` is modest, even a ballistic cold electron does not catch the falling II threshold.

If `zeta` is larger than the ballistic-safe fraction, the electron must lose energy while traversing the gradient. That requires finite `L/ell_E` and therefore finite transit time.

So within the current model:

```text
more gap-drop drive
-> stronger carrier acceleration
-> lower downstream II threshold
-> more required energy relaxation
-> minimum relaxation distance / time.
```

This is a distinct constraint from direct Zener tunneling, which grading can suppress through relative band geometry.

## 9. Important caveats

The result assumes

- linear gap grading;
- quasi-neutral p-type majority-band pinning;
- constant `ell_E`;
- cold injection;
- deterministic mean carrier energy;
- `E_th=chi E_g`;
- simplified two-band Kane velocity ceiling;
- no stochastic high-energy tail;
- no carrier-carrier heating or large-signal space charge.

It is not a calibrated HgCdTe speed limit.

## 10. Next step

Use the exact `r_min(zeta,chi)` relation as one axis of the finite-device phase map and place the local boundary tunneling-voltage condition on another axis.

The remaining material parameter controlling the vertical scale is `ell_E` for the target HgCdTe composition and temperature.
