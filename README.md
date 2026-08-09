# Gedanken 2

First-principles thought experiments in photodetector physics.

This repository follows the physics rather than a predetermined theorem. Failed conjectures, counterexamples, corrections, and prior-art collisions are retained because they define the real result.

## Experiment 01 — The vanishing absorber

> Can an ideal photodetector be made arbitrarily small, arbitrarily fast, arbitrarily sensitive, and still absorb essentially every incident photon?

The answer has never been assumed.

The path has moved much farther than the original active-volume idea:

```text
weak resonant absorber
-> peak absorption can cost temporal bandwidth

active volume
-> not fundamental; field concentration defeats simple V scaling

finite absorber / LDOS / nonperturbative coupling
-> successive microscopic loopholes and access constraints

finite passive multimode network
-> exact harmonic two-access transfer-area bound

active/time-dependent control
-> pump strength and known-mode loading can beat stationary matching

unknown arrival / adaptive control
-> finite storage rank can be replaced by controller/output record rank

unrestricted output continuum
-> kills a universal finite internal space-time capacity law

semiconductor contact
-> useful extraction and reverse thermal loading share the same contact coupling

finite-linewidth energy filter
-> fast extraction produces quantum spectral-tail leakage

multipole filter
-> stronger rejection is possible, but spectral width is not transport speed; delay grows

field-driven narrow-gap collection
-> fixed-thickness speed competes with BTBT

HgCdTe Kane scaling
-> direct-BTBT problem collapses to a simple normalized field/current curve.
```

The active frontier is now **material-specific HgCdTe transport**, not another abstract universal-resource theorem.

## Current strongest HgCdTe normalization

A published uniform-field HgCdTe BTBT model has the form

```math
J_{\rm BTBT}
=
\frac{q^3\sqrt{2m^*}F V}
{4\pi^3\hbar^2E_g^{1/2}}
\exp\left[-
\frac{\pi\sqrt{m^*}E_g^{3/2}}
{2\sqrt2q\hbar F}
\right].
```

For a uniform region `V=FL`, use the simplified narrow-gap Kane relation

```math
m^*=E_g/(2v_K^2),
\qquad
v_K\simeq1.07\times10^6\ {\rm m/s}
```

as a scaling model.

Then

```math
\boxed{
J_{\rm BTBT}
=
\frac{q^3L}{4\pi^3\hbar^2v_K}
F^2e^{-F_K/F}.
}
```

Define

```math
x=F/F_K,
\qquad
j=J/J_K.
```

The entire simplified direct-BTBT family collapses to

```math
\boxed{j=x^2e^{-1/x}.}
```

with

```math
\boxed{
F_K
=\frac{\pi^3\hbar c^2}
{qv_K\lambda_c^2},
}
```

```math
\boxed{
J_K
=\frac{q\pi^3c^4L}
{4v_K^3\lambda_c^4}.
}
```

Therefore

```math
F_K\propto\lambda_c^{-2},
\qquad
J_K\propto L\lambda_c^{-4},
```

while the normalized curve is wavelength independent.

The exact inversion is

```math
\boxed{
F_{\max}^{\rm BTBT}
=
\frac{F_K}
{2W_0[\tfrac12\sqrt{J_K/J_*}]}.
}
```

This is a **scaling result**, not a calibrated HgCdTe device model and not a novelty claim.

## Why this matters

Longer-wavelength HgCdTe becomes less forgiving in two complementary ways.

The characteristic tunneling field falls roughly as

```math
F_K\propto\lambda_c^{-2},
```

while the microscopic Kane length

```math
\ell_K=\hbar v_K/E_g
```

grows as

```math
\ell_K\propto\lambda_c.
```

Representative simplified scales are approximately:

| cutoff | `F_K` | `ell_K` |
|---:|---:|---:|
| 5 um | 6.86e5 V/cm | 2.84 nm |
| 8 um | 2.68e5 V/cm | 4.54 nm |
| 10 um | 1.71e5 V/cm | 5.68 nm |
| 12 um | 1.19e5 V/cm | 6.82 nm |
| 17 um | 5.93e4 V/cm | 9.66 nm |
| 24 um | 2.98e4 V/cm | 13.6 nm |

These numbers are normalization scales, not safe operating fields.

## The missing piece is now high-field transport

For one constant-velocity carrier crossing thickness `L`, the repository uses the rectangular Ramo-pulse convention

```math
\boxed{
B_{\rm tr}
=c_t\frac{v_d}{L},
\qquad
c_t\simeq0.44295.
}
```

The next physically correct frontier is therefore

```math
\boxed{
B_{\rm tr,max}
=\frac{c_t}{L}
\,v_d(F_{\max}^{\rm BTBT}).
}
```

The important restraint is that `v_d(F)` must come from a real high-field HgCdTe transport model.

A primary Monte Carlo study of `Hg_0.8Cd_0.2Te` at 77 K reports hot-electron/non-ohmic and impact-ionization behavior already around `100 V/cm`. The direct-BTBT-only field ceiling can be several `kV/cm`, so low-field mobility cannot simply be extrapolated to that point.

The accessible primary-source text states that analytical velocity interpolation formulas exist but does not expose their coefficients. The repository therefore does **not** invent a generic saturation law just to complete a plot.

## Supporting semiconductor trail

The current material branch also contains several deliberately simplified counterexample/audit models:

- `FERMI_CONTACT_EXTRACTION_REVERSE_LOADING.md` — Fermi detailed balance links useful extraction and reverse loading.
- `RESONANT_ENERGY_FILTER_SPEED_LEAKAGE.md` — finite lifetime creates zero-temperature Lorentzian-tail leakage.
- `MULTIPOLE_ENERGY_FILTER_DELAY_AUDIT.md` — higher-order filters beat the single-Lorentzian tail but spend internal states/delay.
- `FIELD_DRIVEN_COLLECTION_TUNNELING.md` — at fixed collection thickness, higher field-driven transit speed increases direct BTBT.
- `BALLISTIC_BARRIER_SPEED_LEAKAGE.md` — shrinking collection distance eventually removes a one-barrier tunneling exponent.
- `HGCDTE_KANE_SCALE_AUDIT.md` — maps the abstract quantum scales onto realistic infrared cutoff wavelengths.
- `HGCDTE_NORMALIZED_BTBT_FRONTIER.md` — current normalized direct-BTBT model.

## Earlier strongest passive result

The earlier finite passive-network theorem remains useful provenance.

For aggregate optical and detector access budgets

```math
L=\operatorname{Tr}\Gamma_L,
\qquad
R=\operatorname{Tr}\Gamma_R,
```

```math
\boxed{
\mathcal I_{L\to R}
\le
\frac{2LR}{L+R}.
}
```

Its mathematical ingredients are standard passive-system theory. It is not currently the active paper direction.

## Publication status

The project remains **exploratory**.

No manuscript exists. No current equation is presented as a new universal photodetector limit.

The repository has deliberately rejected several attractive but false overgeneralizations, including

- active-volume-only limits;
- finite-absorber one-photon limits;
- finite internal storage as an always-on detector capacity;
- single-Lorentzian speed/leakage scaling as universal;
- spectral FWHM as an architecture-independent transport speed;
- low-field mobility extrapolation into the HgCdTe high-field regime.

## Canonical files

Start with:

- [`AGENTS.md`](AGENTS.md)
- [`CURRENT_STATE.md`](experiments/01-vanishing-absorber/CURRENT_STATE.md)
- [`CLAIM_LEDGER.md`](experiments/01-vanishing-absorber/CLAIM_LEDGER.md)
- [`HGCDTE_NORMALIZED_BTBT_FRONTIER.md`](experiments/01-vanishing-absorber/HGCDTE_NORMALIZED_BTBT_FRONTIER.md)
- [`HGCDTE_KANE_SCALE_AUDIT.md`](experiments/01-vanishing-absorber/HGCDTE_KANE_SCALE_AUDIT.md)
- [`FIELD_DRIVEN_COLLECTION_TUNNELING.md`](experiments/01-vanishing-absorber/FIELD_DRIVEN_COLLECTION_TUNNELING.md)
- [`BALLISTIC_BARRIER_SPEED_LEAKAGE.md`](experiments/01-vanishing-absorber/BALLISTIC_BARRIER_SPEED_LEAKAGE.md)
- [`RESEARCH_LOG.md`](experiments/01-vanishing-absorber/RESEARCH_LOG.md)
- [`ARCHIVE_STATUS.md`](experiments/01-vanishing-absorber/ARCHIVE_STATUS.md)

Earlier derivations remain in the experiment directory as provenance.

## Current frontier

The next calculation is narrowly defined:

> **Obtain a traceable high-field `v_d(F)` law for a definite HgCdTe composition and temperature, combine it with the normalized BTBT inversion, and determine whether direct BTBT actually sets the maximum carrier-transit bandwidth before hot-electron/impact-ionization or another mechanism intervenes.**

New agents should read [`AGENTS.md`](AGENTS.md) first.