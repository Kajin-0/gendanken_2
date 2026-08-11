# Paper Claim Ledger Addendum — Adversarial Review Revision

**Date:** 2026-08-11  
**Purpose:** adds only claims produced by the conditioning, nonuniform-weighting-field, and depth-calibration review pass. `PAPER_CLAIM_LEDGER.md` remains the base ledger.

## CND1 — determinant geometry

**Status:** DERIVED / CHECKED

For

```math
\delta g
=\gamma(i\omega)-\gamma(0)
=u+iv,
```

the real DC+RF inversion determinant is

```math
\boxed{\Delta=-v(u^2+v^2).}
```

The structural singularity is therefore the small RF-to-DC root-displacement limit.

## CND2 — conditioned-drift factorization

**Status:** DERIVED / CHECKED

Define

```math
V_*=\sqrt{w^2+4D\kappa}.
```

Then

```math
D=\omega u/[v(u^2+v^2)],
```

```math
V_*=\omega(v^2-u^2)/[v(u^2+v^2)],
```

```math
w=V_*-2Dg_0,
```

```math
\kappa=V_*g_0-Dg_0^2.
```

This is the preferred conditioning parameterization of the DC+RF inverse.

## CND3 — exact intrinsic conditioning functions

**Status:** DERIVED / CHECKED / CONDITIONAL ON ISOTROPIC SMALL ROOT ERROR

With

```math
\chi=\Re\delta g/\Im\delta g,
```

```math
K_D
=\sqrt{\chi^4+6\chi^2+1}/\chi,
```

```math
K_V
=\sqrt{1+\chi^2}\sqrt{\chi^4+6\chi^2+1}/(1-\chi^2).
```

Low RF gives

```math
K_D\sim V_*^2/(D\omega),
```

while `K_V -> 1`.

## CND4 — balanced normalized-frequency optimum

**Status:** DERIVED / CHECKED / CONDITIONAL

The minimax intrinsic root-conditioning point is

```math
\boxed{\chi_*=1/\sqrt3}
```

or equivalently

```math
\boxed{D\omega_*/V_*^2=\sqrt3.}
```

At this point

```math
K_D=K_V=\sqrt{28/3}.
```

This is not a universal optimum RF once external parasitics/noise are included.

## CND5 — current HgCdTe RF range is not diffusion-optimal

**Status:** CHECKED / CONDITIONAL WORKED SCALE

For `D~0.02327 m^2/s`, `V_*~3.45e4 m/s`, the intrinsic balanced point is approximately `14.1 GHz`.

At `100 MHz`, `500 MHz`, and `1 GHz`, `K_D` is approximately `81`, `17`, and `8.8`, while `K_V` remains near unity.

Thus closure detectability and precise diffusion extraction are distinct measurement requirements.

---

## WF1 — exact nonuniform-weighting observation operator

**Status:** DERIVED

For one-dimensional weighting field `E_w(z)`,

```math
I(t)=q\int E_w j\,dz
```

implies

```math
\boxed{
I(t)=q\int[wE_w+D E_w']p\,dz
}
```

under the stated boundary assumptions.

The corresponding backward equation is

```math
\boxed{
D J''+wJ'-(\kappa+s)J
=-[wE_w+D E_w'].
}
```

Weighting-field nonuniformity is therefore an observation-operator effect, not a change in the transport generator.

## WF2 — linear weighting gradient raises first-difference rank to two

**Status:** DERIVED / CHECKED / CONDITIONAL

For locally linear `E_w`, the current is a linear particular solution plus the transport exponential, so

```math
\boxed{\Delta J_m=C+Bq^m.}
```

One first-difference multiplier is exactly

```math
\boxed{q_{weight}=1}
```

and RF-independent.

This provides a conventional six-color diagnostic for a weighting-field gradient.

## WF3 — weighting gradient can mimic the low-RF transport-gradient phase

**Status:** DERIVED / CHECKED / IMPORTANT LIMITATION

For deterministic homogeneous transport and low RF,

```math
\boxed{
\mathcal C_{4,w}
\simeq+i\omega h^2\beta/v,
}
```

where `beta=partial_z ln E_w`.

This is `O(omega)` and phase-like, the same RF order as the slowness-gradient term. RF scaling alone is therefore insufficient to separate them.

## WF4 — current quartet weighting-field tolerance

**Status:** CHECKED / CONDITIONAL WORKED EXAMPLE

In the current HgCdTe quartet, a linear weighting-field variation of `1%` across the `1.5 um` quartet produces approximately

```text
0.00191 deg @100 MHz
0.00883 deg @500 MHz
0.01346 deg @1 GHz.
```

For this stress, keeping the weighting contribution below 10% of the transport-gradient signal requires roughly `<0.64-0.83%` field variation across the quartet unless the field is independently modeled.

---

## Z1 — equal internal spacing is not fundamental

**Status:** DERIVED / CHECKED

For known arbitrary source positions, one affine-exponential current mode remains overdetermined.

With

```math
d_m=J_{m+1}-J_m,
```

and

```math
Delta_m=z_{m+1}-z_m,
```

```math
\frac{d_1}{d_0}
=e^{r\Delta_0}
\frac{e^{r\Delta_1}-1}{e^{r\Delta_0}-1}
```

determines the one complex spatial exponent, after which the fourth coordinate predicts `d_2/d_1`.

Equal spacing is the special case that reduces this test to the geometric identity.

## Z2 — known nonlinear depth calibration is not a false positive

**Status:** DERIVED

A known nonlinear spectral-to-depth map should be used directly in the arbitrary-spacing closure.

The dangerous quantity is **uncertainty in the internal source coordinates**, not nonlinearity of the map itself.

## Z3 — equal-spacing closure sensitivity to small position errors

**Status:** DERIVED

Around equal spacing,

```math
\boxed{
\delta C_4
=\frac{r}{q-1}
[\epsilon_0-(q+2)\epsilon_1+(2q+1)\epsilon_2-q\epsilon_3].
}
```

At small `|rh|`, the leading position-error mode is the third-difference stencil

```text
(1,-3,3,-1)/h.
```

Common and affine position errors cancel at leading order.

## Z4 — blindly assuming equal spacing can be extremely demanding for the current tiny signal

**Status:** CHECKED / CONDITIONAL WORKED EXAMPLE

For a quadratic coordinate distortion

```math
z=mu+(c/2)(mu-mu_c)^2,
```

using the equal-spacing identity without correcting the known unequal spacing produces 10% of the current HgCdTe gradient phase for approximately

```text
c ~0.0042-0.0046 /um,
```

corresponding to only `~1.2-1.3 nm` nonlinear endpoint displacement across the quartet.

This is **not** a universal absolute-depth requirement. It is a warning against using the equal-spacing shortcut when the nonlinear spacing is not known accurately enough.

---

## Paper consequence

The revised manuscript must now distinguish three separate questions:

```text
Does the current sequence falsify one spatial mode?

If not, is the recovered transport coefficient inversion actually well conditioned?

If one mode fails, is the extra spatial structure transport physics or a known observation-operator effect such as weighting-field nonuniformity?
```

These distinctions strengthen rather than broaden the paper's central falsification philosophy.
