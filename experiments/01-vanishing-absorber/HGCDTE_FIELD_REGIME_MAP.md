# HgCdTe Field-Regime Map — Direct BTBT Versus High-Field Transport in a Finite Detector

**Date:** 2026-08-09  
**Status:** corrected regime map combining simplified Kane direct BTBT with primary `Hg_0.8Cd_0.2Te` transport scales and a separate finite-length dead-space audit; no novelty claim

## 1. Question

The isolated normalized BTBT model can permit several `kV/cm` before a chosen direct-tunneling current density is reached.

Bulk `Hg_0.8Cd_0.2Te` at 77 K becomes non-ohmic and develops non-negligible impact-ionization physics at much smaller fields.

But these are **different statements**:

```text
bulk hot-electron / II onset
!=
finite-device ionization probability.
```

A finite detector must also give an injected carrier enough distance/history to reach the ionization threshold.

The purpose of this file is therefore limited to the **field ordering of direct BTBT and high-field transport**, while `HGCDTE_IMPACT_IONIZATION_DEAD_SPACE.md` handles the finite-length impact-ionization correction.

---

## 2. Direct-BTBT law

Within the simplified Kane substitution,

```math
\boxed{
J_{\rm BTBT}
=C L F^2
\exp\!\left[-\frac{D}{F\lambda_c^2}\right],
}
```

with

```math
\boxed{
C=\frac{q^3}{4\pi^3\hbar^2v_K},
\qquad
D=\frac{\pi^3\hbar c^2}{qv_K},
}
```

and

```math
v_K\simeq1.07\times10^6\ {\rm m/s}.
```

This is an isolated direct-BTBT model, not a total dark-current model.

---

## 3. Exact direct-BTBT crossover wavelength at a stated field

For a reference field `F_R` and direct-BTBT current-density budget `J_*`, define the cutoff `lambda_x` by

```math
J_{\rm BTBT}(F_R,\lambda_\times,L)=J_*.
```

Provided

```math
C L F_R^2>J_*,
```

```math
\boxed{
\lambda_\times
=
\left[
\frac{D}
{F_R\ln(CLF_R^2/J_*)}
\right]^{1/2}.
}
```

Therefore

```text
lambda_c < lambda_x
-> direct BTBT is below the stated budget at F_R

lambda_c > lambda_x
-> the direct-BTBT budget is crossed before F_R.
```

This is a model crossover, not a fundamental wavelength boundary.

---

## 4. Primary bulk transport scale

Palermo et al., *Solid-State Electronics* **53**, 70–78 (2009), study bulk `Hg_0.8Cd_0.2Te` at 77 K and show that hot-electron transport and impact-ionization processes become relevant at fields of order `10^2 V/cm`.

Related target-composition Monte Carlo/hydrodynamic work shows approximately

```text
below ~50 V/cm
-> nearly ohmic drift

above ~50 V/cm
-> sublinear high-field transport

high field
-> steady-state electron drift approaches a scale ~5e5 m/s

submicron structures
-> transient overshoot can approach ~1.1e6 m/s.
```

These facts establish that `v=mu F` cannot be extrapolated indefinitely.

They do **not** by themselves define a finite-device impact-ionization field ceiling.

---

## 5. Illustrative BTBT crossover map

Take

```text
L = 1 um
v_K = 1.07e6 m/s.
```

The isolated direct-BTBT model gives:

| `F_R` | `lambda_x`, `J*=1e-12 A/cm2` | `lambda_x`, `J*=1e-8 A/cm2` | `lambda_x`, `J*=1e-6 A/cm2` |
|---:|---:|---:|---:|
| 100 V/cm | 74.4 um | 88.8 um | 100.0 um |
| 200 V/cm | 51.5 um | 60.9 um | 68.0 um |
| 500 V/cm | 31.7 um | 37.1 um | 41.0 um |
| 1.0 kV/cm | 22.0 um | 25.5 um | 28.1 um |
| 1.5 kV/cm | 17.7 um | 20.5 um | 22.5 um |

At `500 V/cm`, `L=1 um`, the same model predicts approximately

| cutoff | `J_BTBT` |
|---:|---:|
| 10 um | `8.8e-147 A/cm2` |
| 17 um | `2.1e-49 A/cm2` |
| 24 um | `9.8e-24 A/cm2` |
| 30 um | `2.0e-14 A/cm2` |
| 40 um | `3.4e-7 A/cm2` |

Thus, for ordinary 8–14 um material, direct BTBT is still exponentially closed at fields where bulk transport has already become strongly non-ohmic.

This remains a useful mechanism-ordering result.

---

## 6. Correct finite-device interpretation

Do **not** say

```text
impact ionization limits a 1 um device at 100 V/cm
```

merely because the bulk Monte Carlo rate becomes non-negligible around that field.

For cold injection, the field-work estimate for reaching the ionization threshold is

```math
\boxed{
F_{\rm dead}
\simeq
\frac{E_{\rm th}}{qL}.
}
```

With

```math
E_{\rm th}=\chi E_g,
```

and the repository Kane length

```math
\ell_K=\hbar v_K/E_g,
```

```math
\boxed{
\frac{F_{\rm dead}}{F_K}
=
\frac{4\chi}{\pi}
\frac{\ell_K}{L}.
}
```

See `HGCDTE_IMPACT_IONIZATION_DEAD_SPACE.md` for the full derivation and limitations.

For `chi=1`, `L=1 um`, representative field-work thresholds are

```text
8 um  -> 1.55 kV/cm
10 um -> 1.24 kV/cm
12 um -> 1.03 kV/cm
17 um -> 729 V/cm
24 um -> 517 V/cm.
```

These are not ionization-probability thresholds; they are the idealized distances/fields needed to supply approximately one gap energy to a cold carrier.

---

## 7. The mechanism-order conclusion after correction

The earlier phrase

> impact ionization occurs before BTBT because bulk II starts around 100 V/cm

was too crude for a finite detector.

The corrected statement is:

> **For ordinary micron-scale MWIR/LWIR HgCdTe, high-field carrier transport becomes non-ohmic well before direct BTBT is important, and the cold-carrier impact-ionization threshold can become accessible at fields still far below the direct-BTBT characteristic scale because `L >> ell_K`. The actual ionization probability is history dependent and must be calculated separately.**

This is the current canonical interpretation.

---

## 8. Transit-speed envelope

The rectangular Ramo-current-pulse convention remains

```math
\boxed{
B_{\rm tr}
=c_t\frac{v}{L},
\qquad
c_t\simeq0.44295.
}
```

Using only the target-composition high-field velocity scale

```math
v\sim5\times10^5\ {\rm m/s}
```

gives the kinematic envelope

| `L` | `c_t v/L` |
|---:|---:|
| 0.2 um | 1.11 THz |
| 0.5 um | 443 GHz |
| 1 um | 221 GHz |
| 2 um | 111 GHz |
| 5 um | 44.3 GHz |
| 10 um | 22.1 GHz |

These are not full detector bandwidth predictions.

---

## 9. General marginal field-cost identity

For the simplified direct-BTBT law,

```math
\boxed{
\frac{d\ln J_{\rm BTBT}}
{d\ln F}
=2+\frac{F_K}{F}.
}
```

Define

```math
\boxed{
s_v(F)
=\frac{d\ln v}{d\ln F}.
}
```

Since `B_tr proportional to v`, wherever `s_v != 0`,

```math
\boxed{
\frac{d\ln J_{\rm BTBT}}
{d\ln B_{\rm tr}}
=
\frac{2+F_K/F}{s_v(F)}.
}
```

Therefore

```text
s_v ~ 1
-> field efficiently buys speed

s_v -> 0+
-> marginal speed benefit collapses

s_v < 0
-> more field gives more BTBT and less transit speed.
```

The absolute direct-BTBT current may still be negligible; this is a marginal field-selection identity.

---

## 10. Realistic field-selection problem

A complete diode-like field problem should maximize

```math
v(F)
```

subject to separate constraints

```math
J_{\rm BTBT}(F)\le J_*,
```

```math
P_{\rm II}[F,L,E(t)]\le p_*,
```

```math
J_{\rm TAT}(F)\le J_{\rm TAT,*},
```

plus SRH, surface, contact, field-profile, and readout constraints.

The transit contribution is then

```math
\boxed{
B_{\rm tr,max}
=c_t\frac{v(F_{\rm opt})}{L}.
}
```

The impact-ionization term must be history dependent in a thin region unless a validated nonlocal coefficient is supplied.

---

## 11. Claim boundary

### Derived within the direct-BTBT model

```math
\boxed{
\lambda_\times
=
\left[
\frac{D}
{F_R\ln(CLF_R^2/J_*)}
\right]^{1/2},
}
```

```math
\boxed{
\frac{d\ln J}{d\ln F}=2+F_K/F,
}
```

```math
\boxed{
\frac{d\ln J}{d\ln B}
=\frac{2+F_K/F}{s_v(F)}.
}
```

### Corrected external interpretation

- bulk `x=0.20`, 77 K transport becomes non-ohmic at low fields;
- finite-device II probability additionally depends on dead space / carrier energy history;
- direct BTBT remains exponentially small at ordinary LWIR cutoffs over much of that high-field-transport regime.

### Not established

- a calibrated finite-device `P_II(F,L)` for `x=0.20`, 77 K;
- a complete dark-current model;
- a fundamental speed limit;
- novelty of the regime map.

---

## 12. Next step

Use `HGCDTE_IMPACT_IONIZATION_DEAD_SPACE.md` as the immediate frontier.

Build the minimal finite-length carrier-energy trajectory and integrate an energy-dependent HgCdTe ionization rate along it.

Do not replace the nonlocal problem with a guessed local `alpha(F)` merely for convenience.
