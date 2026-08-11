# Adversarial Review Response — Conditioning and Weighting-Field Revision

**Date:** 2026-08-11  
**Status:** active manuscript revision checkpoint; two highest-priority reviewer criticisms resolved analytically and numerically; main manuscript integration still required before submission

## 1. Review disposition

The external adversarial review was largely correct.

The mathematical closure identities themselves were independently re-derived successfully. The two strongest remaining criticisms were:

1. the DC+RF inversion had structural identifiability but no comparable conditioning/error analysis near its determinant singularity;
2. the uniform Shockley-Ramo weighting-field assumption had not been stressed quantitatively, despite being capable of changing the observation operator.

Both issues have now been worked through.

Canonical new files:

- `DC_RF_INVERSION_CONDITIONING_THEOREM.md`
- `numerics/dc_rf_inversion_conditioning.py`
- `NONUNIFORM_WEIGHTING_FIELD_CLOSURE.md`
- `numerics/nonuniform_weighting_field_closure.py`

---

# 2. DC+RF conditioning result

Let

```math
g_0=\gamma(0),
```

and

```math
\delta g
=\gamma(i\omega)-g_0
=u+iv.
```

The manuscript determinant simplifies exactly to

```math
\boxed{
\Delta=-v(u^2+v^2).
}
```

So the practical singularity is geometrically the limit where the RF propagation root barely separates from the DC root.

Define

```math
V_*=\sqrt{w^2+4D\kappa}=w+2Dg_0.
```

Then

```math
\boxed{
D=\frac{\omega u}{v(u^2+v^2)},
}
```

```math
\boxed{
V_*=\frac{\omega(v^2-u^2)}{v(u^2+v^2)},
}
```

followed by

```math
w=V_*-2Dg_0,
```

```math
\kappa=V_*g_0-Dg_0^2.
```

This factorization separates the problem into

```text
complex RF root displacement -> D and conditioned drift scale V_*
DC root -> physical drift/recombination unconditioning.
```

## 2.1 Exact dimensionless conditioning

Define

```math
\chi=\Re\delta g/\Im\delta g,
```

and

```math
\xi=D\omega/V_*^2.
```

They obey exactly

```math
\boxed{
\xi
=\frac{\chi(1+\chi^2)}{(1-\chi^2)^2}.
}
```

For isotropic small root-displacement error, the local relative condition numbers are

```math
\boxed{
K_D
=\frac{\sqrt{\chi^4+6\chi^2+1}}{\chi},
}
```

and

```math
\boxed{
K_V
=\frac{\sqrt{1+\chi^2}\sqrt{\chi^4+6\chi^2+1}}{1-\chi^2}.
}
```

At low RF,

```math
K_D\sim V_*^2/(D\omega),
```

while

```math
K_V\to1.
```

Thus low RF can robustly measure the drift-like timing scale while being intrinsically poor for diffusion.

## 2.2 Balanced optimum

The minimax point is

```math
\boxed{\chi_*=1/\sqrt3,}
```

which corresponds to

```math
\boxed{D\omega_*/V_*^2=\sqrt3.}
```

At that point

```math
\boxed{K_D=K_V=\sqrt{28/3}\simeq3.055.}
```

For the manuscript's illustrative homogeneous HgCdTe scale

```text
D ~0.02327 m^2/s
V_* ~3.45e4 m/s
```

this gives

```text
f* ~14.1 GHz.
```

At the current RF points:

| RF | `K_D` | `K_V` |
|---:|---:|---:|
| 100 MHz | ~81.4 | ~1.001 |
| 500 MHz | ~16.6 | ~1.017 |
| 1 GHz | ~8.82 | ~1.063 |

### Manuscript consequence

The paper must distinguish

```text
closure-signal detectability
from
precision of the recovered diffusion coefficient.
```

The current sub-GHz/GHz HgCdTe closure example can be a falsifiable signal even when complete `D` extraction is badly conditioned.

---

# 3. Nonuniform weighting-field result

For arbitrary one-dimensional weighting field `E_w(z)`, the Shockley-Ramo current is

```math
I(t)
=q\int E_w j\,dz.
```

With homogeneous drift-diffusion and vanishing carrier density at the integration boundaries,

```math
\boxed{
I(t)
=q\int[wE_w+D E_w']p\,dz.
}
```

The exact expected-current backward equation is therefore

```math
\boxed{
D J''+wJ'-(\kappa+s)J
=-[wE_w(z)+D E_w'(z)].
}
```

This establishes that weighting-field nonuniformity changes the **observation operator**, not the transport generator.

## 3.1 Linear weighting gradient has a diagnostic spatial mode

For locally linear `E_w`, the forced solution is one linear particular term plus the ordinary transport exponential.

After spatial first differencing,

```math
\boxed{
\Delta J_m=C+Bq^m.
}
```

Thus a linear weighting-field gradient raises the first-difference rank from one to two with one multiplier

```math
\boxed{q_{weight}=1}
```

that is independent of RF frequency.

This gives the six-color hierarchy a direct conventional explanation to test.

## 3.2 Low-RF degeneracy with transport gradient

For deterministic homogeneous transport and

```math
E_w=E_0[1+\epsilon f(z)],
```

the leading weighting contribution is

```math
\boxed{
\mathcal C_{4,w}
=-\epsilon h^2e^{\gamma(L-z_c)}
[f''-\gamma f']
+O(\epsilon h^4,\epsilon^2).
}
```

For a locally linear weighting field at low RF,

```math
\boxed{
\mathcal C_{4,w}
\simeq+i\omega h^2\beta/v,
}
```

where

```math
\beta=\partial_z\ln E_w.
```

This is phase-like and linear in RF, exactly the same RF order as the local slowness-gradient signal.

Therefore frequency scaling alone cannot distinguish the two.

The weighting field must be

```text
computed independently,
constrained geometrically,
or detected through the extra q=1 spatial mode.
```

## 3.3 Worked HgCdTe tolerance

Using the same real optical quartet and a homogeneous transport control, an imposed linear weighting-field variation gives approximately

| weighting-field change across 1.5 um quartet | 100 MHz | 500 MHz | 1 GHz |
|---:|---:|---:|---:|
| 0.5% | +0.00093 deg | +0.00431 deg | +0.00661 deg |
| 1.0% | +0.00191 deg | +0.00883 deg | +0.01346 deg |

Relative to the manuscript stochastic gradient signal, keeping this simple weighting-field contamination below 10% requires approximately

```text
<0.64% variation across quartet @100 MHz
<0.68% @500 MHz
<0.83% @1 GHz.
```

These are worked-example tolerances, not universal detector specifications.

### Manuscript consequence

Nonuniform weighting field should be promoted from a generic limitations bullet to an explicit conventional rung of the falsification hierarchy.

---

# 4. What remains from the review

The two largest gaps are now resolved.

The next highest-value manuscript revisions are:

1. convert nonlinear spectral-to-depth calibration curvature into a numerical false-closure tolerance for the HgCdTe quartet;
2. stress the source-state/excess-energy assumption with a deliberately perturbed wavelength-dependent initial-state model rather than only comparing the first two excess-energy moments;
3. integrate the new conditioning and weighting-field sections into `MANUSCRIPT_DRAFT.md/.tex` and the supplement;
4. update the measurement-resource discussion so it does not imply that closure detection automatically permits precise `D,w,kappa` extraction;
5. continue narrow priority audit only after these physical-error analyses are complete.

No new broad theory branch is justified at this checkpoint.
