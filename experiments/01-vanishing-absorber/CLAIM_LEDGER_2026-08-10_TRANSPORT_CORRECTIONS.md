# Claim Ledger Addendum — 2026-08-10 Transport Corrections

**Status:** canonical addendum to `CLAIM_LEDGER.md` for the downstream/quasi-neutral transport branch. Where an entry below conflicts with an older transport/design entry in `CLAIM_LEDGER.md`, **this addendum and live `CURRENT_STATE.md` take precedence**. Historical entries remain preserved intentionally.

There is still **no novelty claim and no manuscript**.

---

## A1 — purpose-built validation must use downstream minority-electron transport
**Status:** DERIVED DESIGN CONSEQUENCE / PRIMARY-SOURCE CONSISTENT

For the active high-speed validation concept, use

```text
high-Cd optical entrance at z=0
monotonic x(z) decreasing through the absorber
low-Cd collecting junction at z=L.
```

This aligns the composition-gradient minority-electron drive with collection, consistent with the high-speed graded-HgCdTe transport orientation demonstrated by Sang et al. 2022.

The 2023 published sample-A geometry places the junction at the high-Cd side and can repel p-region photoelectrons away from that junction; it is therefore **not** the preferred causal high-speed validation orientation.

Consequence: older purpose-built files that inherited the published sample-A front-collection orientation are provenance/design studies, not the current transport prescription.

---

## A2 — downstream low-frequency inverse uses the CDF kernel
**Status:** DERIVED / ACTIVE

For path-additive mean delay with collection at `L`,

```math
\boxed{
\bar T_i
=\int_0^L F_i(s)q_1(s)ds,
\qquad
F_i(s)=P(X_g\le s).
}
```

The front-collection survival kernel remains correct for the published 2023 A/B structures, but not for the active purpose-built downstream device.

---

## A3 — the ad hoc `25%` local timing perturbation is superseded as mechanism model
**Status:** SUPERSEDED

Earlier programmed-feature calculations used an illustrative local transport perturbation to study optical/RF geometry.

Those calculations remain useful for

```text
feature placement intuition
interface confounding
edge-ramp convergence
width/interdiffusion tolerance
randomization/replication principles.
```

They are **not** the active mechanism prediction.

The active response is computed from a downstream first-passage drift-diffusion equation.

---

## A4 — downstream first-passage complex transfer
**Status:** DERIVED REDUCED MODEL / CHECKED NUMERICALLY

For minority electrons,

```math
\boxed{
D u''+v(z)u'
-\left(\frac1{\tau_{\rm rec}}+s\right)u=0.
}
```

Use an absorbing collecting boundary at `z=L` and reflecting/Robin-loss optical-entrance boundary at `z=0`.

At RF frequency `Omega`, `s=iOmega`.

The collected normalized transfer is

```math
\boxed{
H(\lambda,\Omega)
=
\frac{\int p(z|\lambda)u(z,i\Omega)dz}
{\int p(z|\lambda)u(z,0)dz}.
}
```

This conditions on DC-collected carriers and separates RF timing/transfer from simple collection loss.

---

## A5 — physically derived relocation signal is not intrinsically too small
**Status:** CHECKED NUMERICALLY / CONDITIONAL PARAMETER SCALE

The downstream first-passage model gives degree-scale wavelength-dependent phase changes for broad, explicitly stated HgCdTe transport stresses.

In the later quasi-neutral empirical-velocity central stress, representative `1 GHz` relocation spans are approximately

```text
4.1 -> 5.6 um feature relocation: ~9.1 deg p-p
2.8 -> 5.6 um: ~14.3 deg p-p.
```

These are **not device predictions**.

They establish only that raw signal amplitude is not the leading theoretical objection once the gradient force is aligned with collection.

---

## A6 — principal-complex-log finite differences at high RF are forbidden
**Status:** INVALIDATED NUMERICAL PROCEDURE / PERMANENT REGRESSION RULE

Do **not** estimate a complex response derivative as

```math
[\log H(p+\delta)-\log H(p-\delta)]/(2\delta)
```

using the principal complex logarithm without explicit branch control.

Phase crossings can create artificial `2pi` jumps and false Fisher information.

Use the branch-safe identity

```math
\boxed{
\frac{\partial\ln H}{\partial p}
=\frac{1}{H}\frac{\partial H}{\partial p},
}
```

with `dH/dp` finite-differenced directly.

The earlier apparent several-degree high-RF mechanism separation was caused by this branch-cut error and is **INVALIDATED**.

---

## A7 — quasi-neutral p-type equilibrium removes an arbitrary interior field multiplier
**Status:** DERIVED / CONDITIONAL ON QUASI-NEUTRAL NONDEGENERATE INTERIOR

For p-type quasi-neutral material,

```math
E_v(z)
\simeq
E_F+k_BT\ln\frac{N_A}{N_v}.
```

Therefore

```math
\boxed{
\frac{dE_c}{dz}
\simeq
\frac{dE_g}{dz}
+k_BT\frac{d}{dz}\ln\frac{N_A}{N_v}.
}
```

For slowly varying `N_A/N_v`, the total minority-electron conduction-band slope is close to the full gap gradient.

Thus the earlier free scalar

```text
chi_E * dEg/dz
```

is superseded as the central interior-force parameterization.

The physically meaningful uncertainties are the doping/DOS profile and non-quasi-neutral boundary/junction fields.

---

## A8 — 2025 electron-affinity result is consistent with quasi-neutral screening
**Status:** KNOWN EXTERNAL RESULT / DERIVED CONSISTENCY

Rhiger & Mustafa 2025 find that approximately two-thirds of a composition-driven HgCdTe gap change appears intrinsically in the conduction-band offset.

This does **not** contradict `dE_c/dz ~ dE_g/dz` for a p-type quasi-neutral interior.

The equilibrium electrostatic potential supplies the additional band tilt required to keep the majority-hole band nearly pinned.

Do not treat intrinsic band-offset partition and total equilibrium band slope as interchangeable quantities.

---

## A9 — conduction-band density-of-states drift is a correction, not an arbitrary field
**Status:** DERIVED / CONDITIONAL MATERIAL MODEL

Use

```math
\boxed{
v_e
=-\frac{\mu}{q}\frac{dE_c}{dz}
+D\frac{d\ln N_c}{dz}.
}
```

For nondegenerate electrons with the standard HgCdTe modeling approximation `m_e^* proportional to E_g`,

```math
\frac{d\ln N_c}{dz}
\simeq
\frac32\frac{d\ln E_g}{dz}.
```

Across the current composition range this is a modest correction to the dominant gap-driven drift and should not be floated as an unconstrained response direction without material evidence.

---

## A10 — empirical HgCdTe velocity-law scale is bounded by existing transport data
**Status:** KNOWN EXTERNAL SCALE / CONDITIONAL APPLICATION

Direct Shockley-Haynes work has measured minority-electron `v(E)`, `D(E)`, and lifetime in p-type HgCdTe.

Recent HgCdTe APD modeling uses

```math
\boxed{
v(F)=\frac{\mu F}{1+(|F|/d)^r}}
```

with fitted scales roughly

```text
d ~4-11 kV/cm
r ~1.9-2.8
```

in published SWIR/MWIR low-temperature examples.

These values are **not** calibrated 300 K constants for the proposed structure, but they establish a physically relevant constitutive scale.

The purpose-built local gradient force is only about `~1.9 kV/cm`, below the fitted APD saturation-field scale.

---

## A11 — completely unbounded velocity-law shape is not identifiable from relocation data alone
**Status:** CHECKED NUMERICALLY / CONDITIONAL CENTRAL MODEL

In the quasi-neutral empirical-velocity first-passage model, marginalize a localized-gradient mechanism coordinate against free

```text
ln(mu)
ln(d)
r
rho = ln[(N_A/N_v)(L)/(N_A/N_v)(0)]
ln(tau)
ln(surface loss)
```

plus wavelength-independent complex channel offsets.

For the current provisional `2.00-2.40 um`, `0.5-3 GHz`, `0.10 deg`-equivalent component-noise stress, the best current three-depth no-prior design reaches only about

```math
\boxed{1.1\sigma.}
```

Therefore the relocation data should not be asked to learn an arbitrary high-field velocity curve and attribute the localized mechanism simultaneously.

---

## A12 — broad physically motivated velocity-law constraints remove the artificial singularity
**Status:** CHECKED NUMERICALLY / CONDITIONAL FISHER SCALE

Impose only broad priors

```text
sigma_ln(d)=0.7  (~factor 2 per sigma)
sigma_r=0.5
```

while leaving mobility, lifetime, surface loss, and majority-band tilt free.

The current central linearized mechanism scale rises to approximately

```math
\boxed{12.8\sigma}
```

under the provisional `0.10 deg` component-noise convention.

Even broader

```text
sigma_ln(d)=1.0
sigma_r=0.7
sigma_rho=2.0
```

gives about `9.7 sigma` in the same conditional model.

These are **not expected laboratory significances**.

They show only that the earlier mechanism collapse required the velocity law to vary over a range much broader than existing HgCdTe transport data suggest.

---

## A13 — independent same-material transport calibration is a required control
**Status:** DERIVED DESIGN REQUIREMENT / ESTABLISHED-METHOD PRECEDENT

Before final mechanism attribution, independently constrain

```text
minority-electron v(E,x)
D(E,x)
tau(E,x)
```

in companion p-type HgCdTe from the same material campaign.

Shockley-Haynes / localized-pulse transit measurement is a direct established precedent.

This calibration is **not** part of the candidate novelty.

---

## A14 — minimal current witness-composition set
**Status:** CHECKED DESIGN SCALE / CONDITIONAL

For the current three-depth programmed relocation family, the high-gradient regions span approximately

```text
x ~0.344-0.517.
```

A minimal first witness set is

```math
\boxed{x\approx0.35,\ 0.43,\ 0.51.}
```

The middle point is a model-check coordinate: it tests whether interpolation of `v(E,x),D(E,x),tau(E,x)` across composition is defensible.

A real witness campaign should add compositions if that interpolation fails its uncertainty budget.

---

## A15 — witness timing/voltage scale is practical
**Status:** CHECKED SCALE / CONDITIONAL GEOMETRY

For a conceptual `100 um` drift path,

```text
0.1-3 kV/cm -> 1-30 V.
```

Across a deliberately broad mobility/velocity-law envelope, transit times are approximately

```text
0.1 kV/cm -> 5-25 ns
0.3 kV/cm -> 1.7-8.4 ns
1.0 kV/cm -> 0.50-2.62 ns
2.0 kV/cm -> 0.25-1.52 ns
3.0 kV/cm -> 0.17-1.28 ns.
```

These scales are compatible with established HgCdTe impulse/transit metrology.

`100 um` is a useful design scale, not a frozen device length.

---

## A16 — do not force Einstein diffusion after witness data exist
**Status:** DESIGN CORRECTION / KNOWN EXPERIMENTAL MOTIVATION

The current reduced first-passage model still uses `D=mu kT/q` as a baseline simplification.

Direct p-type HgCdTe transit data report diffusion mobility exceeding drift mobility under some conditions, consistent with hot-electron diffusion.

Therefore once witness data are available, use measured/interpolated `D(E,x)` independently rather than forcing Einstein equilibrium at high field.

This is a current model limitation and a required next refinement.

---

## A17 — exact old randomized/replicated growth schedules are superseded
**Status:** SUPERSEDED AS NUMERICAL PRESCRIPTION / PRINCIPLE RETAINED

Earlier ad hoc timing models produced specific six/eight-run feature-depth orders.

The principles

```text
randomize feature depth versus chronological growth order
replicate high-leverage depths
fit measured process covariates
```

remain strong experimental design.

The exact old depth/order schedules must be recomputed after the witness-derived transport posterior and measured covariance are inserted into the first-passage model.

---

## A18 — current candidate claim boundary
**Status:** CANDIDATE DISTINCT — PRIORITY UNPROVEN

The potentially distinctive object is **not**

```text
graded HgCdTe transport
graded HgCdTe RF response
wavelength-dependent generation depth
or Shockley-Haynes transport metrology.
```

It is the narrower protocol:

> **Use wavelength as an internal spatial encoder, deliberately relocate a buried graded-field feature, independently calibrate the generic carrier transport law, and test whether the measured complex RF fingerprint follows the predicted feature-depth law.**

Priority remains unproven, especially while the 2024 `Potential application of HgCdTe detector with composition gradient in laser measurement` paper remains technically unresolved.

---

## Current next step

Build a witness-derived **transport posterior** rather than hand-set `d,r` priors:

1. parameterize `v(E,x)`, `D(E,x)`, and `tau(E,x)` through the three witness compositions;
2. assign realistic measurement errors from a transit experiment;
3. interpolate through the graded absorber;
4. propagate that posterior through the downstream first-passage model;
5. determine whether three compositions are sufficient and what witness precision is actually required;
6. only then reoptimize translated depths, wavelength/RF allocation, growth order, and replication.
