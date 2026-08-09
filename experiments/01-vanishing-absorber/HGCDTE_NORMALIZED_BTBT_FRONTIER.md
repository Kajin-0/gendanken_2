# Normalized HgCdTe BTBT Frontier — A Cutoff-Wavelength Collapse in the Simplified Kane Model

**Date:** 2026-08-08  
**Status:** exact nondimensionalization of a published HgCdTe parabolic-barrier BTBT formula after a simplified Kane-mass substitution; material-scaling audit, not a precision device model; no novelty claim

## 1. Purpose

`FIELD_DRIVEN_COLLECTION_TUNNELING.md` showed symbolically that, for fixed collection thickness, increasing collection speed by increasing electric field pushes up a Kane-type band-to-band tunneling current.

`HGCDTE_KANE_SCALE_AUDIT.md` then showed that HgCdTe has a particularly simple approximate band scaling because the Kane velocity is nearly composition independent near the narrow-gap regime.

This note asks a sharper question:

> Does the direct-tunneling law collapse to a material-normalized curve when the HgCdTe band-edge mass is eliminated in favor of `E_g` and the Kane velocity?

Within the stated simplified model, yes.

The result is useful because it cleanly separates

```text
universal dimensionless field dependence
```

from

```text
cutoff wavelength, thickness, and high-field drift transport.
```

---

## 2. Published HgCdTe BTBT formula used as the starting point

A commonly used direct band-to-band tunneling expression for a parabolic barrier in a uniform electric field is

```math
\boxed{
J_{\rm BTBT}
=
\frac{q^3\sqrt{2m^*}\,F V}
{4\pi^3\hbar^2 E_g^{1/2}}
\exp\!\left[
-
\frac{\pi\sqrt{m^*}E_g^{3/2}}
{2\sqrt2\,q\hbar F}
\right].
}
```

Here `F` is electric-field magnitude and `V` is the voltage drop across the tunneling region.

This exact form is used, for example, in the HgCdTe APD analysis by Kopytko et al., *Sensors* **22**, 924 (2022), DOI `10.3390/s22030924`, Eq. (4), citing standard HgCdTe tunneling literature.

For a uniform region of thickness

```math
L,
```

set

```math
V=FL.
```

Then

```math
\boxed{
J_{\rm BTBT}
=
\frac{q^3\sqrt{2m^*}\,L}
{4\pi^3\hbar^2 E_g^{1/2}}
F^2
\exp\!\left(-\frac{F_K}{F}\right),
}
```

with

```math
\boxed{
F_K
=
\frac{\pi\sqrt{m^*}E_g^{3/2}}
{2\sqrt2\,q\hbar}.
}
```

The published formula is prior device physics, not a repository result.

---

## 3. Simplified HgCdTe Kane-mass substitution

Near the narrow-gap Kane regime, use the simplified relation

```math
\boxed{
E_g=2m_Kv_K^2.
}
```

Teppe et al., *Nature Communications* **7**, 12576 (2016), DOI `10.1038/ncomms12576`, report a nearly composition- and temperature-independent HgCdTe Kane velocity around

```math
v_K\simeq1.07\times10^6\ {\rm m/s}
```

near the semimetal-semiconductor transition.

For this **scaling audit only**, identify

```math
m^*=m_K
=\frac{E_g}{2v_K^2}.
```

This is not asserted to be a precision tunneling-mass model for every HgCdTe composition or junction.

The prefactor simplifies because

```math
\frac{\sqrt{2m^*}}
{E_g^{1/2}}
=\frac1{v_K}.
```

The characteristic field becomes

```math
\boxed{
F_K
=\frac{\pi E_g^2}
{4q\hbar v_K}.
}
```

Therefore

```math
\boxed{
J_{\rm BTBT}
=
\frac{q^3L}
{4\pi^3\hbar^2v_K}
F^2
\exp\!\left(-\frac{F_K}{F}\right).
}
```

---

## 4. Dimensionless collapse

Define normalized field

```math
\boxed{x=F/F_K.}
```

Define the current-density scale

```math
\boxed{
J_K
\equiv
\frac{q^3L F_K^2}
{4\pi^3\hbar^2v_K}.
}
```

Then

```math
\boxed{
\frac{J_{\rm BTBT}}{J_K}
=x^2e^{-1/x}.
}
```

Writing

```math
j\equiv J_{\rm BTBT}/J_K,
```

the whole simplified BTBT family is

```math
\boxed{j=x^2e^{-1/x}.}
```

This is the central nondimensionalization.

The function contains no explicit

```text
E_g,
lambda_c,
L,
m^*,
or v_K
```

once `F` and `J` are normalized by their material scales.

---

## 5. Closed forms for the scaling factors

Insert

```math
F_K
=\frac{\pi E_g^2}
{4q\hbar v_K}
```

into `J_K`:

```math
\boxed{
J_K
=
\frac{qL E_g^4}
{64\pi\hbar^4v_K^3}.
}
```

Now use the detector-scale optical-gap approximation

```math
E_g\simeq\frac{hc}{\lambda_c}.
```

Then

```math
\boxed{
F_K
=\frac{\pi^3\hbar c^2}
{qv_K\lambda_c^2},
}
```

and

```math
\boxed{
J_K
=\frac{q\pi^3c^4L}
{4v_K^3\lambda_c^4}.
}
```

Thus the two scales obey

```math
\boxed{F_K\propto\lambda_c^{-2},}
```

```math
\boxed{J_K\propto L\lambda_c^{-4}.}
```

The normalized shape is unchanged.

---

## 6. Exact inversion

The normalized current relation is

```math
j=x^2e^{-1/x}.
```

Let

```math
y=1/x.
```

Then

```math
j=\frac{e^{-y}}{y^2}.
```

Therefore

```math
\frac{y}{2}e^{y/2}
=\frac1{2\sqrt j}.
```

Using the principal Lambert function,

```math
\boxed{
x(j)
=\frac1
{2W_0\!\left(1/(2\sqrt j)\right)}.
}
```

Hence a specified direct-tunneling current-density ceiling `J_*` gives

```math
\boxed{
F_{\max}^{\rm BTBT}
=
\frac{F_K}
{2W_0\!\left[
\frac12\sqrt{J_K/J_*}
\right]}.
}
```

This is the direct HgCdTe specialization of the generic Lambert-W inversion already encountered in `FIELD_DRIVEN_COLLECTION_TUNNELING.md`.

---

## 7. Transit bandwidth should now use the real velocity-field law

Do **not** substitute

```math
v_d=\mu F
```

at the fields obtained above unless the field is actually in the ohmic regime.

HgCdTe high-field transport is strongly non-ohmic.

Palermo et al., *Solid-State Electronics* **53**, 70-78 (2009), DOI `10.1016/j.sse.2008.10.003`, report Monte Carlo electron transport for `Hg_0.8Cd_0.2Te` at 77 K and find hot-electron behavior and impact-ionization physics emerging at fields of order `100 V/cm`, far below the multi-kV/cm fields that a direct-BTBT-only constraint may permit.

Therefore the correct next-stage master relation is

```math
\boxed{
B_{\rm tr,max}
=
\frac{c_t}{L}
\,v_d\!\left(F_{\max}^{\rm BTBT}ight),
\qquad
c_t\simeq0.44295.
}
```

Here

```math
v_d(F)
```

must come from an experimentally validated or microscopic HgCdTe transport model.

This deliberately separates

```text
BTBT field limit
```

from

```text
carrier velocity response to that field.
```

---

## 8. Kinematic upper envelope

The Kane velocity

```math
v_K
```

is a band-dispersion parameter, not a measured drift saturation velocity.

Nevertheless, within the simplest two-band Kane dispersion it supplies a natural group-velocity ceiling.

Thus an optimistic kinematic envelope is

```math
\boxed{
B_{\rm tr}
\lesssim
c_t\frac{v_K}{L}.
}
```

Numerically, for

```math
v_K=1.07\times10^6\ {\rm m/s},
```

this gives approximately

| `L` | `c_t v_K/L` |
|---:|---:|
| 0.25 um | 1.90 THz |
| 0.5 um | 0.948 THz |
| 1 um | 0.474 THz |
| 2 um | 0.237 THz |
| 5 um | 94.8 GHz |
| 10 um | 47.4 GHz |

These are **not practical drift-bandwidth predictions**. They are optimistic band-velocity envelopes.

---

## 9. Illustrative direct-BTBT field ceilings

Using

```math
v_K=1.07\times10^6\ {\rm m/s}
```

and `L = 1 um`, the simplified model gives the following field ceilings for selected direct-BTBT-only current-density targets.

| cutoff | `F_K` | `F_max` @ `1e-6 A/cm2` | `F_max` @ `1e-4 A/cm2` | `F_max` @ `1e-2 A/cm2` | `F_max` @ `1 A/cm2` |
|---:|---:|---:|---:|---:|---:|
| 5 um | 6.86e5 V/cm | 2.44e4 V/cm | 2.87e4 V/cm | 3.49e4 V/cm | 4.42e4 V/cm |
| 8 um | 2.68e5 V/cm | 1.02e4 V/cm | 1.21e4 V/cm | 1.49e4 V/cm | 1.93e4 V/cm |
| 10 um | 1.71e5 V/cm | 6.71e3 V/cm | 8.04e3 V/cm | 1.00e4 V/cm | 1.31e4 V/cm |
| 12 um | 1.19e5 V/cm | 4.78e3 V/cm | 5.77e3 V/cm | 7.22e3 V/cm | 9.56e3 V/cm |
| 17 um | 5.93e4 V/cm | 2.51e3 V/cm | 3.06e3 V/cm | 3.89e3 V/cm | 5.27e3 V/cm |

These values are **illustrative outputs of the isolated direct-BTBT model**, not predicted safe operating fields for real HgCdTe.

Real devices can be limited earlier by

- trap-assisted tunneling;
- SRH generation;
- impact ionization / avalanche;
- field nonuniformity;
- surface leakage;
- contact leakage;
- hot-carrier effects;
- velocity nonlinearity.

The 2021 HgCdTe APD study by Chen et al., *npj Quantum Materials* **6**, 103, DOI `10.1038/s41535-021-00409-3`, explicitly shows that BBT and avalanche dark current compete at high reverse bias and that the internal field distribution is strongly controlled by doping and layer thickness.

---

## 10. What the normalized collapse tells us

The dimensionless law

```math
j=x^2e^{-1/x}
```

means that the direct-tunneling part of the problem has a very simple hierarchy.

At a fixed normalized dark-current budget

```math
j=J_*/J_K,
```

the allowed normalized field

```math
x=F/F_K
```

is the same for every cutoff wavelength.

The wavelength penalty enters entirely through

```math
F_K\propto\lambda_c^{-2}
```

and

```math
J_K\propto L\lambda_c^{-4}.
```

However, a fixed **absolute** current-density budget does not correspond to fixed `j`, because `J_K` itself changes strongly with wavelength.

Therefore statements such as

```text
longer wavelength always lowers the allowed normalized field by lambda^-2
```

would be too crude for a fixed engineering dark-current specification.

Use the exact Lambert inversion.

---

## 11. Thickness scaling has two competing appearances

The characteristic field

```math
F_K
```

does not depend on region thickness in the uniform-field model.

But

```math
J_K\propto L.
```

Thus, for a fixed absolute `J_*`, reducing `L` raises the normalized current allowance

```math
j_*=J_*/J_K
```

and therefore permits a somewhat larger fraction `F/F_K` before the integrated BTBT current-density model reaches `J_*`.

At the same time the transit factor contains

```math
B_{\rm tr}\propto v_d/L.
```

So thinning the collection region helps transit speed twice in this stripped model:

1. shorter crossing distance;
2. less integrated tunneling generation at the same local field.

This is precisely why real ultrathin photon-trapping detectors are such a strong counterexample to naive thickness-speed-dark-current triangles.

Eventually the `L -> 0` extrapolation fails through the microscopic transport mechanisms already audited in `BALLISTIC_BARRIER_SPEED_LEAKAGE.md` and `HGCDTE_KANE_SCALE_AUDIT.md`.

---

## 12. Reproducibility

The companion script

```text
numerics/hgcdte_btbt_normalized_sweep.py
```

computes

- `E_g(lambda_c)`;
- `F_K(lambda_c)`;
- `J_K(lambda_c,L)`;
- the normalized curve `j(x)`;
- numerical inversion for `F_max(J_*)` without external special-function dependencies;
- the optimistic `c_t v_K/L` transit envelope.

It is a deterministic scaling/regression calculation, not a device simulator.

---

## 13. Claim boundary

### Derived exactly after the stated substitutions

```math
\boxed{
J/J_K=x^2e^{-1/x}
}
```

with

```math
\boxed{
F_K=\frac{\pi^3\hbar c^2}
{qv_K\lambda_c^2}
}
```

and

```math
\boxed{
J_K=\frac{q\pi^3c^4L}
{4v_K^3\lambda_c^4}.
}
```

### Prior physics

- the HgCdTe direct-BTBT formula;
- Kane dispersion / approximately universal `v_K` near the transition;
- non-ohmic high-field electron transport;
- high-field BBT/TAT/avalanche competition in HgCdTe APDs.

### Not established

- that `m^*=E_g/(2v_K^2)` is quantitatively accurate for BTBT at every cutoff;
- that `E_g=hc/lambda_c` is sufficient for precision device modeling;
- a universal HgCdTe safe-field curve;
- an accurate high-field `v_d(F)` model for arbitrary composition/doping;
- a complete dark-current or speed limit;
- novelty of the nondimensionalization.

---

## 14. Next decisive calculation

The direct-BTBT side is now sufficiently normalized.

The next calculation should **not** invent a phenomenological velocity-saturation law.

Instead:

1. obtain a primary-source HgCdTe `v_d(F)` interpolation or digitizable Monte Carlo curve for a specific composition and temperature;
2. combine it with the exact `F_max(J_*)` relation above;
3. produce `B_tr,max(lambda_c,L,J_*)` for that stated transport model;
4. compare the field at which BTBT reaches the target against the field at which hot-electron transport / impact ionization already changes the drift law;
5. then determine whether BTBT actually controls the best transit speed or whether another transport mechanism intervenes first.

Do not call the resulting frontier fundamental unless all competing dark-current and speed mechanisms are included or explicitly bounded.