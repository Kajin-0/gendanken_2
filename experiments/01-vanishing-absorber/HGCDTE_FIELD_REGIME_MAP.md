# HgCdTe Field-Regime Map — When Direct BTBT Actually Becomes Relevant to Transit Speed

**Date:** 2026-08-09  
**Status:** exact algebra within the simplified Kane direct-BTBT model, combined with primary/author-deposited `Hg_0.8Cd_0.2Te` transport scales; regime map, not a calibrated device limit; no novelty claim

## 1. Question

The normalized direct-BTBT model can predict fields of several `kV/cm` before a chosen direct-tunneling current density is reached.

But bulk `Hg_0.8Cd_0.2Te` at 77 K becomes non-ohmic and impact-ionization-sensitive far below many of those fields.

The relevant question is therefore not simply

```text
what field is allowed by direct BTBT?
```

but

> **At the field where carrier transport has already entered its high-field regime, is direct BTBT actually large enough to matter?**

This note answers that question without fitting an arbitrary velocity curve.

---

## 2. Direct-BTBT law in a form useful for field ordering

From `HGCDTE_NORMALIZED_BTBT_FRONTIER.md`, after the simplified Kane-mass substitution,

```math
\boxed{
J_{\rm BTBT}
=
C L F^2
\exp\!\left[-\frac{D}{F\lambda_c^2}\right],
}
```

where

```math
\boxed{
C=\frac{q^3}
{4\pi^3\hbar^2v_K},
}
```

```math
\boxed{
D=\frac{\pi^3\hbar c^2}
{qv_K},
}
```

and

```math
v_K\simeq1.07\times10^6\ {\rm m/s}
```

is used for the HgCdTe Kane scaling audit.

All quantities in this note must be used in one consistent unit system.

---

## 3. Exact crossover wavelength at any reference field

Choose a physically meaningful reference field

```math
F_R
```

such as

- onset of strong hot-electron physics;
- approximate approach to bulk drift-velocity saturation;
- onset of a specified impact-ionization probability;
- another independently determined transport field.

Let the allowed direct-BTBT current density be

```math
J_*.
```

Set

```math
J_{\rm BTBT}(F_R,\lambda_\times,L)=J_*.
```

Then

```math
\frac{J_*}{C L F_R^2}
=
\exp\!\left[-
\frac{D}
{F_R\lambda_\times^2}
\right].
```

Provided

```math
C L F_R^2>J_*,
```

the crossover wavelength is exactly

```math
\boxed{
\lambda_\times
=
\left[
\frac{D}
{F_R
\ln(C L F_R^2/J_*)}
\right]^{1/2}.
}
```

Interpretation:

- if `lambda_c < lambda_x`, direct BTBT is below `J_*` at the reference field;
- if `lambda_c > lambda_x`, the direct-BTBT budget is already exceeded before reaching that reference field.

This is not a fundamental wavelength boundary. It is the exact crossing of two stated engineering/model criteria.

---

## 4. Primary transport scales for `Hg_0.8Cd_0.2Te` at 77 K

Palermo et al., *Solid-State Electronics* **53**, 70–78 (2009), DOI `10.1016/j.sse.2008.10.003`, perform Monte Carlo transport calculations specifically for `Hg_0.8Cd_0.2Te` at 77 K and report that hot-electron transport and impact ionization become important at fields of order, and even below, `100 V/cm`.

A later Monte Carlo study of the same composition reports

```text
below ~50 V/cm: approximately ohmic velocity-field response
above ~50 V/cm: sublinear velocity increase
high field: drift velocity tends toward ~5e5 m/s.
```

Daoudi et al., *J. Phys.: Conf. Ser.* **193**, 012003 (2009), simulate a 0.2 um low-doped `Hg_0.8Cd_0.2Te` region at 77 K. They report a local field extremum near `2.1 kV/cm`, transient velocity overshoot near `1.1e6 m/s`, and cite a steady-state MCT saturation velocity of order `5e5 m/s`. Their current-voltage calculation shows impact ionization becoming important at the higher simulated biases.

These results establish the scale hierarchy but do **not** supply one universally calibrated bulk `v(F)` curve for every doping/device geometry.

---

## 5. Illustrative crossover wavelengths

Take

```text
L = 1 um
v_K = 1.07e6 m/s.
```

For several direct-BTBT current-density budgets, the exact crossover equation gives:

| reference field `F_R` | `lambda_x` for `J*=1e-12 A/cm2` | `lambda_x` for `J*=1e-8 A/cm2` | `lambda_x` for `J*=1e-6 A/cm2` |
|---:|---:|---:|---:|
| 100 V/cm | 74.4 um | 88.8 um | 100.0 um |
| 200 V/cm | 51.5 um | 60.9 um | 68.0 um |
| 500 V/cm | 31.7 um | 37.1 um | 41.0 um |
| 1.0 kV/cm | 22.0 um | 25.5 um | 28.1 um |
| 1.5 kV/cm | 17.7 um | 20.5 um | 22.5 um |

These numbers are outputs of the **isolated direct-BTBT model**.

They do not include trap-assisted tunneling, SRH generation, surface leakage, Auger/impact ionization, or nonuniform fields.

---

## 6. Immediate consequence for ordinary LWIR HgCdTe

The table shows a strong ordering.

At the `~100 V/cm` field scale where primary `x=0.20`, 77 K transport calculations already enter hot-electron / impact-ionization physics, direct BTBT would not reach even an extraordinarily strict `1e-12 A/cm2` criterion until the simplified cutoff were of order `74 um` for `L=1 um`.

At `500 V/cm`, the corresponding crossover remains around `32 um` for the same very strict criterion.

Therefore, within this stripped model:

> **For ordinary 8–14 um HgCdTe at 77 K, the material enters nonlinear transport and impact-ionization physics long before direct BTBT becomes the mechanism that limits field-driven transit speed.**

This does **not** mean direct BTBT is unimportant in reverse-biased HgCdTe devices. It means that direct BTBT is not the first high-field physics encountered when trying to increase drift speed in the stated bulk-LWIR regime.

Longer-wavelength / smaller-gap devices and much higher operating fields move toward the tunneling branch rapidly.

---

## 7. Direct examples at `F = 500 V/cm`

For `L=1 um`, the same simplified direct-BTBT model gives approximately

| cutoff | `J_BTBT(500 V/cm)` |
|---:|---:|
| 10 um | `8.8e-147 A/cm2` |
| 17 um | `2.1e-49 A/cm2` |
| 24 um | `9.8e-24 A/cm2` |
| 30 um | `2.0e-14 A/cm2` |
| 40 um | `3.4e-7 A/cm2` |

The absolute smallness at ordinary IR cutoffs is the important point.

The exponent is still so large that the direct-BTBT channel is effectively closed at this field in the simplified model.

---

## 8. Transit-speed envelope from the measured/simulated velocity scale

Using the repository rectangular Ramo-pulse convention

```math
B_{\rm tr}
=c_t\frac{v}{L},
\qquad
c_t\simeq0.44295,
```

and the target-composition steady-state velocity scale

```math
v_{\rm sat}\sim5\times10^5\ {\rm m/s},
```

gives the purely kinematic transit envelope

| collection length `L` | `c_t v_sat/L` |
|---:|---:|
| 0.2 um | 1.11 THz |
| 0.5 um | 443 GHz |
| 1 um | 221 GHz |
| 2 um | 111 GHz |
| 5 um | 44.3 GHz |
| 10 um | 22.1 GHz |

These are **not complete detector bandwidth predictions**.

Carrier lifetime, diffusion, contacts, RC loading, trapping, avalanche dynamics, and readout can be slower.

The submicron hydrodynamic overshoot value `~1.1e6 m/s` is a transient nonlocal effect and must not be substituted as a universal bulk saturation velocity.

---

## 9. A general marginal-cost identity

The direct-BTBT law has logarithmic field sensitivity

```math
\boxed{
\frac{d\ln J_{\rm BTBT}}
{d\ln F}
=
2+\frac{F_K}{F}.
}
```

For transit response

```math
B_{\rm tr}\propto v(F),
```

define the local transport elasticity

```math
\boxed{
s_v(F)
=\frac{d\ln v}
{d\ln F}.
}
```

Then wherever `s_v != 0`,

```math
\boxed{
\frac{d\ln J_{\rm BTBT}}
{d\ln B_{\rm tr}}
=
\frac{2+F_K/F}
{s_v(F)}.
}
```

This identity is independent of the particular velocity interpolation.

It gives a useful physical interpretation:

### Ohmic regime

If

```math
s_v\simeq1,
```

field still buys speed efficiently.

### Velocity-saturation regime

As

```math
s_v\to0^+,
```

the marginal direct-BTBT cost per fractional speed improvement diverges:

```math
\boxed{
\frac{d\ln J}{d\ln B}\to+\infty.
}
```

The absolute direct-BTBT current may still be tiny, but **additional field is becoming a very inefficient way to buy transit speed**.

### Negative differential velocity

If

```math
s_v<0,
```

then increasing field simultaneously

```text
increases direct BTBT
and
decreases transit speed.
```

That field range is strictly dominated with respect to these two quantities.

This marginal relation is more robust than identifying a universal saturation field.

---

## 10. Why the field hypothesis changed

The earlier working intuition was

```text
raise field
-> faster extraction
-> eventually direct BTBT sets the speed ceiling.
```

The target-composition transport literature shows that this is generally too simple.

For ordinary LWIR `Hg_0.8Cd_0.2Te` at 77 K the ordering is closer to

```text
low field
-> ohmic high-mobility transport

~50-100 V/cm
-> hot-electron / non-ohmic / impact-ionization physics begins

few hundred V/cm and above
-> velocity approaches a high-field scale; marginal speed benefit collapses

still higher fields / longer wavelengths
-> direct BTBT can become technologically important.
```

Thus the immediate practical frontier is not a two-way

```text
transit speed vs direct BTBT
```

tradeoff.

It is a multi-mechanism high-field problem.

---

## 11. Impact ionization must be treated as a separate probability budget

Let the local impact-ionization rate experienced by a carrier be

```math
\Gamma_{\rm II}(F)
```

and let it traverse a uniform region of length `L` with velocity `v(F)`.

Under a minimal Poisson-event approximation, the mean number of ionization events during one transit is

```math
\boxed{
\Xi_{\rm II}(F)
=
\Gamma_{\rm II}(F)
\frac{L}{v(F)}.
}
```

The probability of at least one event is

```math
\boxed{
P_{\rm II}
=1-e^{-\Xi_{\rm II}}.
}
```

For an allowed probability `p_*`, the necessary condition is

```math
\boxed{
\frac{\Gamma_{\rm II}(F)}
{v(F)}
\le
\frac{-\ln(1-p_*)}{L}.
}
```

Equivalently, defining the ionization coefficient

```math
\alpha_{\rm II}(F)
=\Gamma_{\rm II}(F)/v(F),
```

```math
\boxed{
\alpha_{\rm II}(F)L
\le
-\ln(1-p_*).
}
```

This is standard stochastic transport accounting, not a new HgCdTe ionization law.

It shows why impact ionization should be imposed as an **independent field constraint**, not hidden inside the drift-velocity fit.

---

## 12. General field-selection problem

The next realistic model should determine

```math
F_{\rm opt}
=
\arg\max_F v(F)
```

subject to separate constraints such as

```math
J_{\rm BTBT}(F)\le J_*,
```

```math
P_{\rm II}(F)\le p_*,
```

```math
J_{\rm TAT}(F)\le J_{\rm TAT,*},
```

plus field-uniformity and device constraints.

The corresponding transit response is

```math
\boxed{
B_{\rm tr,max}
=c_t\frac{v(F_{\rm opt})}{L}.
}
```

This formulation avoids pretending that one high-field mechanism is universally dominant.

---

## 13. Claim boundary

### Derived exactly within the stated direct-BTBT model

- crossover wavelength

```math
\lambda_\times
=
\left[
\frac{D}
{F_R\ln(CLF_R^2/J_*)}
\right]^{1/2};
```

- logarithmic BTBT field slope

```math
\frac{d\ln J}{d\ln F}=2+F_K/F;
```

- marginal speed/current identity

```math
\frac{d\ln J}{d\ln B}
=\frac{2+F_K/F}{s_v(F)}.
```

### Established external transport physics

- `Hg_0.8Cd_0.2Te` at 77 K becomes non-ohmic / hot-electron / impact-ionization-sensitive at low fields of order `10^2 V/cm`;
- target-composition steady-state drift velocity approaches a scale of order `5e5 m/s`;
- submicron HgCdTe can show transient velocity overshoot substantially above the bulk saturation scale.

### Not established

- a unique field where `x=0.20` reaches exactly 90%, 95%, etc. of saturation velocity;
- a calibrated impact-ionization coefficient over the full field range;
- a complete dark-current model;
- a fundamental speed limit;
- novelty of the algebraic regime map.

---

## 14. Next decisive step

The direct-BTBT-first hypothesis has now been falsified for the ordinary LWIR field scale within the simplified model.

Next:

1. recover the `Hg_0.8Cd_0.2Te`, 77 K impact-ionization interpolation/rate curve if possible;
2. impose a stated multiplication/ionization probability budget for a defined collection length;
3. compare that field ceiling directly against the transport saturation envelope and direct-BTBT ceiling;
4. only then add trap-assisted tunneling and generation-recombination mechanisms;
5. after the diode-like field problem is closed, compare the result with photoconductors, where carrier lifetime and photoconductive gain can dominate the speed physics instead of transit time.
