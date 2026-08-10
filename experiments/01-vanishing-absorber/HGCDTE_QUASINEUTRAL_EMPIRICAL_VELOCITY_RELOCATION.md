# Quasi-Neutral Graded-HgCdTe Relocation with an Empirical Velocity Law

**Date:** 2026-08-10  
**Status:** corrected conditional transport/identifiability model using quasi-neutral band self-consistency plus an experimentally motivated HgCdTe velocity-field law; low-temperature APD fit parameters are used only as broad scale constraints, not as a calibrated 300 K law; no novelty claim

## 1. Why the field model changes again

The first downstream drift-diffusion relocation calculation used

```math
E_{\rm eff}=\chi_E|dE_g/dz|/q
```

with a free scalar `chi_E`.

That was deliberately cautious, but two pieces of physics now make it unnecessarily loose.

### 2025 electron-affinity result

Rhiger and Mustafa, *Journal of Applied Physics* **138**, 165701 (2025), DOI `10.1063/5.0300709`, derive a revised HgCdTe electron affinity and show that approximately two-thirds of a composition-driven gap change appears intrinsically in the conduction-band offset.

Their current expression also keeps the electrostatic and electron-affinity drift terms separate.

### Quasi-neutral p-type equilibrium

In the p-type graded absorber interior,

```math
E_v(z)\simeq E_F+k_BT\ln\!\frac{N_A}{N_v}.
```

Therefore

```math
\boxed{
\frac{dE_c}{dz}
\simeq
\frac{dE_g}{dz}
+k_BT\frac{d}{dz}\ln\!\frac{N_A}{N_v}.
}
```

If `N_A/N_v` varies slowly, the **total** minority-electron conduction-band slope is nearly the full gap gradient.

There is no contradiction with the approximately two-thirds intrinsic band-offset result: the equilibrium electrostatic potential supplies the additional tilt required to keep the majority-hole band nearly pinned.

The arbitrary `chi_E` central model is therefore superseded.

---

## 2. Density-of-states correction

The 2025 current equation also contains the effective-mass / conduction-DOS term.

In reduced particle-drift form,

```math
\boxed{
v_e(z)
=-\frac{\mu}{q}\frac{dE_c}{dz}
+D\frac{d\ln N_c}{dz}.
}
```

For nondegenerate electrons

```math
N_c\propto(m_e^*)^{3/2}.
```

Use the standard HgCdTe device-model approximation

```math
m_e^*/m_0\propto E_g,
```

so

```math
\boxed{
\frac{d\ln N_c}{dz}
\simeq
\frac{3}{2}\frac{d\ln E_g}{dz}.
}
```

Across the current `x=0.55 -> 0.32` profile at 300 K, this term is a correction to the dominant gap-gradient drive rather than a free field of comparable magnitude.

The repository does not float it as an arbitrary unconstrained spectral mode.

---

## 3. Majority-band tilt coordinate

Parameterize the total variation of the majority-band quantity by

```math
\boxed{
\rho
=\ln
\frac{(N_A/N_v)(L)}{(N_A/N_v)(0)}.
}
```

In this first stress assume a linear change through the absorber:

```math
\frac{d}{dz}\ln\frac{N_A}{N_v}=\frac{\rho}{L}.
```

Then the force-equivalent field toward the collecting junction is

```math
\boxed{
F_{\rm force}(z)
=
\frac{|dE_g/dz|}{q}
-rac{k_BT}{q}\frac{\rho}{L}.
}
```

`rho=0` is the central quasi-neutral uniform-ratio case.

This is a sensitivity coordinate, not a claim that real doping is exactly linear.

A factor-of-two total change in `N_A/N_v` corresponds to

```math
k_BT\ln2\approx0.018\ {\rm eV}
```

at 300 K, small compared with the approximately `0.32 eV` total gap change across the present profile.

---

## 4. Direct HgCdTe transport measurements define the velocity-law scale

Rothman et al., *Journal of Electronic Materials* **39** (2010) 837-845, DOI `10.1007/s11664-010-1247-8`, directly measured minority-electron

```text
drift velocity
diffusion coefficient
and lifetime
```

versus electric field in p-type HgCdTe using Shockley-Haynes measurements at `80-200 K`.

The paper reports, for example,

```text
MWIR p-type minority electron mobility ~15,000-20,000 cm2/Vs at 80 K
measured saturation velocities ~2e6-6e6 cm/s.
```

Thus the transport calibration required by the relocation experiment is an **established HgCdTe measurement**, not an invented control procedure.

---

## 5. Empirical velocity law

Recent HgCdTe APD modeling uses the impulse-response-motivated form

```math
\boxed{
v(F)
=\frac{\mu F}
{1+(|F|/d)^r}.
}
```

Guerra et al., *Journal of Electronic Materials* **55** (2026) 6628-6637, DOI `10.1007/s11664-026-12921-y`, fit this form to SWIR and MWIR APD data.

Their Table I spans approximately

### SWIR `x=0.4`, 80 K

```text
mu ~4000-4650 cm2/Vs
d ~10.1-11.5 kV/cm
r ~1.91-2.18.
```

### MWIR `x=0.3`, 160 K

```text
mu ~25,900-34,400 cm2/Vs
d ~4.1-7.8 kV/cm
r ~1.91-2.79.
```

The fitted values depend on the rest of the avalanche model, and the authors explicitly state that the high-field velocity formulation may be incomplete.

Therefore these are **not** imported as 300 K material constants.

They are used only to establish that a physically relevant `d` scale is several `kV/cm`, not arbitrarily close to the proposed `~2 kV/cm` internal gradient.

---

## 6. The proposed feature is below the APD saturation-field scale

For the present programmed profile, the quasi-neutral full-gap gradient gives approximately

```text
background force scale ~220 V/cm
local feature force scale ~1.9 kV/cm.
```

Using `r=2.2`, the empirical velocity-law reduction factor at `1.9 kV/cm` is

```text
d = 4 kV/cm  -> velocity reduction ~16%
d = 8 kV/cm  -> ~4%
d = 12 kV/cm -> ~2%.
```

Thus the compact feature is not operating deep in the avalanche-APD high-field saturation regime.

This is a crucial physical scale correction.

---

## 7. Central 300 K stress

Use

```text
mu = 9000 cm2/Vs
d = 8 kV/cm
r = 2.2
rho = 0
tau_rec = 1 ns
entrance S = 1e5 cm/s.
```

These are explicit sensitivity coordinates.

`d=8 kV/cm` and `r=2.2` are not claimed to be measured 300 K values for the proposed structure.

The purpose is to ask how mechanism identifiability changes once the velocity law is constrained to an experimentally recognizable HgCdTe form.

---

## 8. First-passage model

Use the same downstream first-passage equation

```math
D u''+v(z)u'
-\left(\frac1\tau+i\Omega\right)u=0,
```

with

```text
high-Cd optical entrance at z=0
low-Cd collecting junction at z=L
Robin entrance loss
absorbing collecting boundary.
```

The local velocity is

```math
\boxed{
v(z)
=
\frac{\mu F_{\rm force}(z)}
{1+[|F_{\rm force}(z)|/d]^r}
+D\frac{d\ln N_c}{dz}.
}
```

The optical `x(z)` remains the measured/programmed profile.

The localized transport mechanism coordinate remains

```math
s_{\rm eff}(z;\eta)
=s_0+\eta[s(z)-s_0].
```

---

## 9. The physically derived relocation signal is large

At the central stress, the field-feature relocation signal is of order many degrees at `1 GHz` for wide feature translations.

Representative current results are approximately

```text
4.1 -> 5.6 um: ~9.1 deg peak-to-peak
2.8 -> 5.6 um: ~14.3 deg peak-to-peak.
```

These are not device predictions.

They show that once the quasi-neutral full conduction-band drive is used, **signal amplitude is not the limiting issue**.

Mechanism attribution remains the harder question.

---

## 10. Correct branch-safe physical nuisance set

Use the local target derivative

```math
\partial\ln H/\partial\eta
```

and marginalize it against

```text
ln(mu)
ln(d)
r
rho
ln(tau_rec)
ln(S)
```

plus one arbitrary wavelength-independent phase and `ln|H|` offset per device/RF channel.

All complex derivatives use

```math
\frac{\partial\ln H}{\partial p}
=\frac{1}{H}\frac{\partial H}{\partial p},
```

not finite differences of the principal complex logarithm.

The provisional signal weighting remains

```math
|H|\sqrt{P_{\rm abs}C_{\rm dc}}.
```

---

## 11. Completely unbounded velocity-law shape is still degenerate

Use

```text
lambda = 2.00-2.40 um
f = 0.5, 1, 2, 3 GHz
component noise scale = 0.10 deg-equivalent.
```

If all six physical nuisance amplitudes are allowed to float with no bounds, the current best three-depth design is approximately

```math
\boxed{2.6,\ 4.4,\ 5.6\ \mu{\rm m}}
```

and the linearized mechanism significance is only about

```math
\boxed{1.1\sigma.}
```

The target-to-nuisance angle is only about `0.11 deg`.

Therefore the inverse cannot learn an arbitrary high-field velocity curve and a localized gradient mechanism simultaneously from these data alone.

---

## 12. Broad empirical velocity constraints remove the artificial singularity

Now impose only broad scale information consistent with the range already seen in HgCdTe transport/APD fits:

```text
sigma_ln(d) = 0.7
```

which is roughly a factor-of-two one-sigma uncertainty in `d`, and

```text
sigma_r = 0.5.
```

Keep

```text
mu
tau_rec
surface loss
and rho
```

unconstrained.

Then the same linearized three-depth mechanism significance rises to approximately

```math
\boxed{12.8\sigma}
```

under the provisional `0.10 deg` component-noise convention.

Even the deliberately broader stress

```text
sigma_ln(d) = 1.0
sigma_r = 0.7
sigma_rho = 2.0
```

still gives about

```math
\boxed{9.7\sigma.}
```

These are **conditional Fisher scales**, not expected experimental detection significances.

They make one narrower point:

> **The previous mechanism collapse required the velocity-law shape to vary over a far broader amplitude range than is physically suggested by existing HgCdTe transport measurements.**

---

## 13. Why this is not permission to skip calibration

The 2010 Shockley-Haynes data are `80-200 K` and the 2026 APD fits are at `80 K` and `160 K`.

The proposed relocation experiment is presently centered near `300 K` and spans a graded composition range wider than either single calibration sample.

The 2026 authors also explicitly warn that their velocity model can overpredict saturation behavior.

Therefore the literature provides a **prior scale**, not a final constitutive law.

A purpose-built same-material calibration is still the correct experiment.

---

## 14. Strongest calibration experiment

Fabricate a companion p-type HgCdTe transport structure from the same epitaxial campaign and measure

```text
minority-electron drift velocity v(E)
diffusion coefficient D(E)
lifetime tau(E)
```

over the actual field range relevant to the relocation devices, especially

```text
~0.1-3 kV/cm.
```

The most direct precedent is Shockley-Haynes / localized-pulse transport metrology.

An impulse-response-versus-applied-field structure is another viable implementation if the carrier path length and electrical transfer can be de-embedded accurately.

This calibration is **not part of the candidate novelty**.

It is established HgCdTe transport metrology used to constrain the inverse.

---

## 15. High-temperature evidence is encouraging

Rothman et al., *Journal of Electronic Materials* **54** (2025) 8323-8334, DOI `10.1007/s11664-025-12133-w`, report SWIR HgCdTe APD impulse-response and bandwidth characterization up to room temperature.

At `300 K`, they observe bias-dependent signal onset and attribute the delay partly to reduced electron velocity at higher electric field; measured bandwidth reaches about `1.4 GHz` in one device type.

This does not directly give the low-kV/cm `v(E)` law needed here.

It does show that high-temperature HgCdTe impulse transport is experimentally accessible with GHz-class instrumentation.

---

## 16. Current interpretation

The research hierarchy has now narrowed substantially:

```text
optical generation-position encoder
-> viable

purpose-built downstream gradient orientation
-> required

physics-derived first-passage transport signal
-> large enough

arbitrary constitutive-law fit from relocation data alone
-> not identifiable

quasi-neutral band self-consistency
-> removes arbitrary interior field fraction

empirical HgCdTe velocity-law scale
-> makes remaining constitutive uncertainty bounded

same-material v(E), D, tau calibration
-> decisive next control.
```

The remaining scientific challenge is no longer generic phase precision or arbitrary optical rank.

It is whether a measured **depth-dependent relocation law**, conditioned on independently measured carrier transport, requires the localized internal gradient feature.

---

## 17. Nonclaims

Do not claim

```text
the 2010/2026 velocity parameters apply unchanged at 300 K
the empirical velocity formula is exact
12.8 sigma is an expected laboratory significance
the proposed gradient structure has already been fabricated
or the relocation method is novel.
```

The checked conclusion is narrower:

> **The apparent mechanism degeneracy becomes severe only when the HgCdTe velocity-field curve is allowed to vary essentially without physical bounds. Existing transport data already constrain its scale enough that a dedicated same-material velocity calibration is a realistic path to a well-posed relocation test.**

---

## 18. Numerical implementation

`numerics/hgcdte_quasineutral_empirical_velocity_relocation.py`
