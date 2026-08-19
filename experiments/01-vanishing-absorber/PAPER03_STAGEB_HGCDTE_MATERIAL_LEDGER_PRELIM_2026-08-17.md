# Paper 03 Stage-B HgCdTe material ledger — preliminary source gate

**Date:** 2026-08-17  
**Status:** **SOURCE-QUALIFIED DESIGN RECORD / NO MATERIAL-SPECIFIC RESULT**

## 1. Purpose

The generic Stage-B solver is intentionally synthetic. Before any HgCdTe-specific operating state is calculated, the Stage-B model contract requires every dimensional material input to be tied to a composition, temperature, doping regime, source, and model relation.

This record fixes the first material-specific design choice **before** a HgCdTe Stage-B result is calculated.

## 2. First material coordinate

The cleanest first material coordinate is a **uniform** Hg1-xCdxTe absorber near

```text
x = 0.30
```

rather than the existing Stage-A `x=0.55 -> 0.32` composition gradient.

Reason: a graded alloy requires the composition-dependent conduction/valence-band edge (or electron-affinity / electrochemical-potential) gradient to enter the carrier flux. Merely inserting spatially varying `Eg(x)` or `ni(x)` into

```math
J_n=-q\mu_n n\nabla\psi+qD_n\nabla n
```

would omit the band-edge quasi-electric force. A graded-x Stage-B model will therefore be a later extension with the band-edge term written explicitly, not an implicit parameter substitution.

## 3. Energy gap

Primary source:

```text
G. L. Hansen, J. L. Schmit, T. N. Casselman,
"Energy gap versus alloy composition and temperature in Hg1-xCdxTe,"
Journal of Applied Physics 53 (1982), DOI 10.1063/1.330018.
```

Use

```math
E_g(x,T)=
-0.302+1.93x-0.81x^2+0.832x^3
+5.35\times10^{-4}(1-2x)T
```

with `Eg` in eV and `T` in K.

At `x=0.30`:

```text
T = 300 K -> Eg = 0.290764 eV -> hc/Eg = 4.2641 um
T = 230 K -> Eg = 0.275784 eV -> hc/Eg = 4.4957 um
T =  77 K -> Eg = 0.243042 eV -> hc/Eg = 5.1013 um
```

The wavelength values are only band-gap scale coordinates, not detector spectral-cutoff claims.

## 4. Intrinsic carrier concentration

Primary source:

```text
G. L. Hansen, J. L. Schmit,
"Calculation of intrinsic carrier concentration in Hg1-xCdxTe,"
Journal of Applied Physics 54 (1983), DOI 10.1063/1.332153.
```

The published fitted Kane-model expression is

```math
n_i =
[5.585-3.820x+1.753\times10^{-3}T
-1.364\times10^{-3}xT]\times10^{14}
E_g^{3/4}T^{3/2}\exp[-E_g/(2k_BT)]
```

in `cm^-3`. The authors report the fit as approximately 1% accurate to their calculation for `Eg>0`, `50<T<300 K`, `x<0.7`, and within about 15% of the Hall-derived experimental intrinsic concentration.

For `x=0.30`, the resulting scale is

```text
T = 300 K -> ni ~= 3.60e15 cm^-3
T = 230 K -> ni ~= 6.00e14 cm^-3
T =  77 K -> ni ~= 1.18e9  cm^-3
```

A later implementation may compare the 1983 fit against the more accurate Kane-model expression in

```text
Gopal et al., "Expression for intrinsic carrier concentration in Hg1-xCdxTe,"
Solid State Communications 92 (1994) 357-360,
DOI 10.1016/0038-1098(94)90717-X,
```

which reports approximately 1% accuracy for alloys with `x>=0.17`.

## 5. Immediate carrier-content consequence

A 2021 primary lifetime study reports post-growth-annealed n-type HgCdTe(100) MWIR epilayers with

```text
x = 0.262 to 0.336
residual donor concentration ~= 1e15 cm^-3
operating/material study range = 230 to 300 K
```

and measured 300-K minority-carrier lifetimes of approximately `5-11 us` for ~4-um-cutoff material and `0.2-1 us` for ~5.4-um-cutoff material:

```text
M. Kopytko et al.,
"Minority carrier lifetime in HgCdTe(100) epilayers and their potential application to background radiation limited MWIR photodiodes,"
Semiconductor Science and Technology 36 (2021) 055003,
DOI 10.1088/1361-6641/abea6d.
```

Comparison with the intrinsic-concentration scale above is decisive:

```text
x = 0.30, 300 K: ni ~= 3.6e15 cm^-3 > 1e15 cm^-3 residual-donor scale
x = 0.30, 230 K: ni ~= 6.0e14 cm^-3, same order as 1e15 cm^-3 residual-donor scale
```

Therefore a low-doped HOT MWIR HgCdTe material coordinate in the 230-300 K range is **not accepted as a single-electron operating-state model by default**.

Under the existing Stage-B model contract, the material-specific solver must instead use coupled

```text
psi, n, p
```

unless an explicitly sourced donor concentration is chosen high enough that minority-hole charge/current is quantitatively negligible under a predeclared unipolarity criterion.

This is a model-selection result, not a device-performance claim.

## 6. Electron mobility

Primary modern source with direct experimental comparison:

```text
S. Najafi Bavani, M. S. Akhoundi Khezrabad,
"The electron mobility in Hg1-xCdxTe (x=0.22 and 0.3): A comparison between experimental and theoretical results,"
Materials Research Bulletin 140 (2021) 111325,
DOI 10.1016/j.materresbull.2021.111325.
```

The study covers `x=0.22` and `x=0.30`, temperature dependence over approximately `75-300 K`, doping dependence, and Hall measurements on annealed / In-doped n-type material. This is the preferred mobility source family for the first `x=0.30` material coordinate.

Do **not** freeze a single mobility value from the Stage-A `9000 cm^2/(V s)` sensitivity coordinate. Stage A explicitly did not calibrate that number as a material parameter.

A material-specific mobility value/range remains **OPEN** until the source's exact donor concentration and temperature row matching the selected Stage-B coordinate is extracted.

## 7. Dielectric permittivity

The commonly used empirical static relation

```math
\epsilon_s(x) \approx 20.5-15.5x+5.7x^2
```

would give approximately `16.36` at `x=0.30` (small coefficient variants occur in the literature).

However, the original primary experimental provenance of this polynomial has not yet been recovered to the standard required for the material ledger. It therefore remains

```text
STATUS = OPEN / DO NOT FREEZE YET
```

rather than silently adopting the formula from a later review/device paper.

## 8. Recombination

The Kopytko et al. 2021 study is an appropriate primary anchor for the lifetime/recombination regime at `x~0.3`, `230-300 K`, and low residual n-type doping. It explicitly discusses Auger-, radiative-, and SRH-limited behavior and reports measured lifetimes.

For Stage B:

- lifetime will not be inserted as a free number merely to reproduce Stage-A behavior;
- the first material-specific recombination law must match the selected temperature/doping regime;
- if the operating-state calculation is bipolar, recombination must be written consistently in `n,p`, not as a hidden one-carrier sink.

Exact Auger/SRH parameterization remains **OPEN** pending extraction of the source equations/parameter rows selected for the first coordinate.

## 9. Contact / doping coordinate

The first material-specific run must choose one of two explicitly different routes:

### Route A — low-doped HOT material

```text
x ~= 0.30
T = 230-300 K
N_D ~ 1e15 cm^-3 scale
carrier model = bipolar psi,n,p
```

This is the preferred scientifically representative route because it is directly aligned with primary HOT MWIR lifetime data.

### Route B — deliberately strongly n-type unipolar validation

Choose a directly sourced `N_D >> ni` coordinate and predeclare a quantitative minority-carrier bound. This may be useful as a recovery/limiting test but must not be substituted for Route A and called representative low-doped HOT material.

## 10. Current material-specific decision

```text
uniform x=0.30 first material family -> selected
230-300 K low-doped HOT anchor       -> source-supported
single-electron material model       -> rejected by default
bipolar psi,n,p Stage-B extension    -> required for preferred Route A
Eg source                            -> source-qualified
ni source                            -> source-qualified
mobility source family               -> source-qualified; exact row/value still OPEN
permittivity                         -> OPEN primary provenance
recombination parameterization       -> OPEN exact source extraction
contact/doping boundary prescription -> OPEN until bipolar implementation lock
material-specific numerical result   -> none
science_interpretation_ready         -> false
```

No HgCdTe Stage-B simulation should be interpreted until the generic self-consistent numerical gates pass and the OPEN material-ledger coordinates above are closed.