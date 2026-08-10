# Current State — Experiment 01: The Vanishing Absorber

**Date:** 2026-08-10  
**Status:** exploratory; strongest current path is a **purpose-built downstream translated-gradient HgCdTe validation experiment conditioned on independent minority-carrier transport calibration**; wavelength × RF complex response is the internal spatial encoder; no novelty claim

There is still **no manuscript**.

---

## 1. Active question

The original universal detector-bound program, the ballistic timing-peak route, and the attempt to rescue the published 2023 near-junction sample-A geometry by increasingly precise static inversion are all stopped/superseded as the main frontier.

The active question is now:

> **Can wavelength-dependent generation in a known graded-HgCdTe absorber act as an internal position encoder, and can a deliberately translated buried composition-gradient feature produce a complex RF transport fingerprint that follows its known depth after the generic HgCdTe transport law is calibrated independently?**

The contribution, if any, must come from the **inverse/causal validation protocol**, not from the already-known facts that grading changes HgCdTe absorption, carrier drift, or RF response.

---

## 2. Read first

After root `AGENTS.md`:

1. `HGCDTE_DOWNSTREAM_DRIFT_DIFFUSION_RELOCATION.md`
2. `HGCDTE_QUASINEUTRAL_EMPIRICAL_VELOCITY_RELOCATION.md`
3. `HGCDTE_TRANSPORT_WITNESS_CALIBRATION_DESIGN.md`
4. `HGCDTE_PHYSICAL_NUISANCE_RELOCATION_DESIGN.md`
5. `HGCDTE_TRANSLATED_GRADIENT_PRIOR_ART_BOUNDARY.md`
6. `HGCDTE_PROGRAMMED_TRANSLATED_GRADIENT_FEASIBILITY.md`
7. `HGCDTE_PROGRAMMED_INTERFACE_SAFE_JOINT_DESIGN.md`
8. `HGCDTE_PROGRAMMED_WIDTH_INTERDIFFUSION.md`
9. `HGCDTE_LPE_TRANSLATED_GRADIENT_REACHABILITY.md`
10. `HGCDTE_SHORTWAVE_MECHANISM_CONFOUNDING.md`
11. `HGCDTE_SAMPLE_A_CROSSBAND_SELF_CALIBRATION.md`
12. `HGCDTE_SPECTRAL_TIMING_LINEAR_INVERSE.md`
13. `HGCDTE_PUBLISHED_SAMPLE_B_DIMENSIONAL_FORWARD_MATRIX.md`
14. `HGCDTE_SPECTRAL_TIMING_TOMOGRAPHY_PRIOR_ART_AUDIT.md`
15. `CLAIM_LEDGER.md`
16. `RESEARCH_LOG.md`
17. `RESEARCH_LOG_2026-08-10_CONTINUATION.md`
18. `ARCHIVE_STATUS.md`

The older randomization/replication calculations remain useful **experimental-design principles**, but their exact depth/order optima were computed with an earlier ad hoc timing operator and are not current fabrication prescriptions.

---

## 3. Hard prior-art boundary

Do **not** claim novelty for

- wavelength-dependent absorption or generation depth;
- wavelength-dependent detector timing/bandwidth;
- composition-gradient built-in fields in HgCdTe;
- composition-gradient modification of HgCdTe carrier transport;
- faster RF/impulse response in strongly graded HgCdTe;
- graded-HgCdTe spectral response;
- wavelength/depth forward generation modeling;
- localized-position HgCdTe transit measurements;
- Shockley–Haynes measurement of HgCdTe minority-carrier transport;
- optical-load-dependent HgCdTe transient response;
- intentionally engineered positive HgCdTe composition gradients by LPE.

Sang et al. 2022 already measured high-speed graded-HgCdTe response and modeled gradient-driven carrier transport.

Rothman et al. 2010 already measured minority-electron drift velocity, diffusion coefficient, and lifetime versus field in p-type HgCdTe using Shockley–Haynes methods.

Perrais et al. already used localized excitation to study HgCdTe transit timing.

Huo et al. 2024 demonstrated control of broad HgCdTe longitudinal composition gradients through mercury-loss/cooling conditions.

The 2024 paper

`Potential application of HgCdTe detector with composition gradient in laser measurement`

DOI `10.5768/JAO202445.0310009`

remains an unresolved close collision because its full technical content has not been recovered.

Current candidate status:

> **candidate inverse-metrology / translated-feature validation method; priority unproven.**

---

## 4. Critical orientation correction

The 2023 published sample-A geometry puts the junction at the **high-Cd end**. Its strong nonlinear gradient can repel p-region photoelectrons away from that junction.

That is not the correct orientation for a purpose-built high-speed gradient-transport validation experiment.

The active conceptual device is instead

```text
z = 0:
high-Cd optical entrance

x(z) decreases monotonically
through the graded absorber

z = L:
low-Cd collecting junction.
```

This aligns the composition-gradient minority-electron drive with collection, consistent with the high-speed graded-HgCdTe transport orientation demonstrated in the 2022 work.

Practical consequence:

> **if the low-Cd junction is on the epitaxial top side, the clean experiment may require substrate/backside illumination.**

That optical complexity is preferable to using the wrong carrier-force direction and can be incorporated into a calibrated optical kernel.

---

## 5. Exact low-frequency inverse remains useful but is no longer the mechanism model

For downstream collection at `L`, with generation coordinate `X_g`, the path-additive mean-delay inverse uses

```math
\boxed{
\bar T_i
=\int_0^L F_i(s)q_1(s)ds,
\qquad
F_i(s)=P(X_g\le s).
}
```

This is the correct downstream CDF operator.

It remains useful for

```text
orientation
low-frequency mode counting
and experimental intuition.
```

But the active mechanism calculation no longer assigns an ad hoc local delay density or an illustrative `25%` velocity perturbation.

The physical transport response is computed from a first-passage drift–diffusion model.

---

## 6. Physics-derived first-passage transport

For a minority electron beginning at `z`, solve

```math
\boxed{
D u''(z)
+v(z)u'(z)
-\left(\frac{1}{\tau_{\rm rec}}+s\right)u(z)=0.
}
```

Use

```math
u(L,s)=1
```

at the collecting junction and a reflecting/Robin-loss condition at the optical entrance.

At RF angular frequency `Omega`, set

```math
s=i\Omega.
```

The normalized collected RF transfer is

```math
\boxed{
H(\lambda,\Omega)
=
\frac{
\int p(z|\lambda)u(z,i\Omega)dz
}{
\int p(z|\lambda)u(z,0)dz
}.
}
```

This conditions on collected carriers and separates timing/transfer from simple loss in DC collection probability.

---

## 7. Quasi-neutral p-type band self-consistency removes the arbitrary field fraction

The earlier reduced transport model used

```math
E_{\rm eff}=\chi_E|dE_g/dz|/q
```

with a free scalar `chi_E`.

That is no longer the preferred central model.

In a p-type quasi-neutral interior,

```math
E_v(z)
\simeq
E_F+k_BT\ln\frac{N_A}{N_v}.
```

Since

```math
E_c=E_v+E_g,
```

```math
\boxed{
\frac{dE_c}{dz}
\simeq
\frac{dE_g}{dz}
+k_BT\frac{d}{dz}\ln\frac{N_A}{N_v}.
}
```

If `N_A/N_v` varies slowly, the total minority-electron conduction-band slope is therefore close to the **full gap gradient**.

This is consistent with the 2025 electron-affinity result that roughly two-thirds of a composition-driven gap change is intrinsic conduction-band offset: the equilibrium electrostatic potential supplies the additional tilt required to pin the majority-hole band.

The physically meaningful uncertainty is the doping/DOS profile and non-quasi-neutral boundary physics, not an arbitrary free interior field multiplier.

---

## 8. Conduction-DOS correction

The 2025 HgCdTe current equation also contains the effective-mass/DOS drift term.

Use

```math
\boxed{
v_e
=-\frac{\mu}{q}\frac{dE_c}{dz}
+D\frac{d\ln N_c}{dz}.
}
```

For nondegenerate electrons

```math
N_c\propto(m_e^*)^{3/2}.
```

Using the standard HgCdTe device-model approximation `m_e^* proportional to E_g`, the DOS correction is approximately

```math
\frac{d\ln N_c}{dz}
\simeq
\frac32\frac{d\ln E_g}{dz}.
```

Across the present `x~0.32-0.55` design range it is a modest correction to the gap-driven drift, not a free response direction of comparable scale.

---

## 9. Empirical velocity law replaces the arbitrary smooth saturation law

Use the HgCdTe transport/APD-motivated form

```math
\boxed{
v(F)
=\frac{\mu F}
{1+(|F|/d)^r}.
}
```

Direct/published HgCdTe data provide useful scale information:

```text
Rothman et al. 2010:
Shockley-Haynes v(E), D(E), tau(E) in p-type HgCdTe, 80-200 K
saturation velocity ~2e6-6e6 cm/s
MWIR low-field minority-electron mobility ~1.5e4-2.0e4 cm2/Vs at 80 K

Guerra et al. 2026 APD fits:
d ~4-11 kV/cm
r ~1.9-2.8
across x~0.3-0.4 examples at 80-160 K.
```

The authors explicitly warn that the APD velocity formulation can be incomplete.

Therefore these values are **broad scale constraints**, not a calibrated 300 K constitutive law for the proposed structure.

---

## 10. The purpose-built field scale is below the APD saturation-field scale

For the present programmed profile:

```text
background quasi-neutral gap-gradient force ~0.2 kV/cm
local compact feature force ~1.9 kV/cm.
```

At `E~1.9 kV/cm` and `r=2.2`, the empirical velocity reduction is only approximately

```text
d = 4 kV/cm  -> ~16%
d = 8 kV/cm  -> ~4%
d = 12 kV/cm -> ~2%.
```

Thus the validation feature is not operating deep inside the avalanche high-field regime.

That sharply reduces how much freedom the unknown high-field velocity curve should physically have.

---

## 11. Physics-derived relocation signal is comfortably measurable in scale

At one explicit central stress

```text
T = 300 K
mu = 9000 cm2/Vs
d = 8 kV/cm
r = 2.2
rho = ln[(N_A/N_v)(L)/(N_A/N_v)(0)] = 0
tau = 1 ns
entrance surface loss S = 1e5 cm/s,
```

the current first-passage model gives degree-scale wavelength-dependent relocation signals at `1 GHz`.

Representative values:

```text
feature 4.1 -> 5.6 um:
~9.1 deg peak-to-peak

feature 2.8 -> 5.6 um:
~14.3 deg peak-to-peak.
```

These are **not device predictions**.

They establish only that signal amplitude is no longer the leading theoretical objection.

---

## 12. Mechanism identifiability must use branch-safe complex derivatives

A previous high-RF Fisher calculation falsely suggested several-degree separation from transport nuisances because it finite-differenced the principal complex logarithm across phase branch cuts.

That result is invalidated.

Use

```math
\boxed{
\frac{\partial\ln H}{\partial p}
=\frac{1}{H}\frac{\partial H}{\partial p}
}
```

with `dH/dp` finite-differenced directly.

Never use raw finite differences of the principal `log(H)` at high RF without phase-unwrapping/branch control.

This correction is now a permanent numerical regression requirement.

---

## 13. Completely unbounded transport-law shape remains non-identifiable

In the quasi-neutral empirical-velocity model, use the local mechanism coordinate

```math
s_{\rm eff}(z;\eta)
=s_0+\eta[s(z)-s_0]
```

and marginalize against free

```text
ln(mu)
ln(d)
r
rho
ln(tau)
ln(surface loss)
```

plus wavelength-independent complex channel offsets.

For

```text
lambda = 2.00-2.40 um
f = 0.5, 1, 2, 3 GHz
provisional weighted component noise = 0.10 deg-equivalent,
```

a best current three-depth no-prior design is approximately

```text
2.6, 4.4, 5.6 um
```

but reaches only about

```math
\boxed{1.1\sigma}
```

if `d` and `r` are allowed unlimited local amplitudes.

Therefore the relocation data cannot simultaneously learn an arbitrary velocity-field curve and uniquely attribute the response to the localized gradient.

---

## 14. Broad physical velocity constraints remove the artificial singularity

The same linearized model changes dramatically once the empirical velocity curve is merely restricted to a physically plausible scale.

Use deliberately broad priors

```text
sigma_ln(d) = 0.7
~ factor 2 per sigma

sigma_r = 0.5.
```

Leave

```text
mu
tau
surface loss
and rho
```

unconstrained.

Then the central linearized mechanism significance rises to about

```math
\boxed{12.8\sigma}
```

under the provisional `0.10 degree` component-noise convention.

Even

```text
sigma_ln(d) = 1.0
sigma_r = 0.7
sigma_rho = 2.0
```

gives about

```math
\boxed{9.7\sigma}.
```

These are **conditional Fisher scales**, not expected laboratory significances.

The important conclusion is narrower:

> **the severe mechanism degeneracy appears only if the HgCdTe velocity curve is allowed to vary over a range much broader than existing transport measurements suggest.**

---

## 15. Decisive companion experiment — transport witnesses

The strongest next experimental control is now explicit:

> **measure minority-electron `v(E,x)`, `D(E,x)`, and `tau(E,x)` independently in companion p-type HgCdTe material over the actual field/composition range of the relocation structures.**

The current translated high-gradient regions span approximately

```text
x ~0.344-0.517.
```

A minimal first witness set is

```math
\boxed{x\approx0.35,\ 0.43,\ 0.51.}
```

The middle point tests whether interpolation in composition is actually valid rather than assuming it from two endpoints.

At 300 K their approximate Hansen-gap wavelengths are

```text
x=0.35 -> ~3.46 um
x=0.43 -> ~2.66 um
x=0.51 -> ~2.14 um.
```

---

## 16. Transport-witness timing scale is practical

A conceptual `100 um` Shockley-Haynes drift path converts

```text
0.1-3 kV/cm
```

to only

```text
1-30 V.
```

Across a deliberately broad

```text
mu = 4000-20000 cm2/Vs
d = 4-12 kV/cm
r = 2.2
```

envelope, expected 100-um transit times are approximately

```text
0.1 kV/cm -> 5-25 ns
0.3 kV/cm -> 1.7-8.4 ns
1.0 kV/cm -> 0.50-2.62 ns
2.0 kV/cm -> 0.25-1.52 ns
3.0 kV/cm -> 0.17-1.28 ns.
```

This is compatible with established HgCdTe transit/impulse metrology.

Room-temperature HgCdTe APDs have already been characterized with multi-GHz impulse instrumentation.

The exact witness geometry should follow the fabrication facility's proven implementation.

---

## 17. What the witness experiment must extract

Use multiple drift distances if practical.

From packet motion:

```text
arrival-time slope -> v(E,x)
packet broadening -> D(E,x)
amplitude/charge decay -> tau(E,x).
```

Do not force Einstein-equilibrium diffusion if the measurement disagrees; the 2010 p-type HgCdTe measurements found diffusion mobility systematically above drift mobility, consistent with hot-electron diffusion.

Fit the empirical `mu,d,r` form only if supported by the data.

A measured interpolation/spline is acceptable and may be preferable.

---

## 18. Fabrication architecture

### Preferred material route

```text
MBE -> strongest first route for a compact translated internal feature
MOCVD -> credible diffusion-aware alternative
single-run slider LPE -> not supported for the current compact ~1 um / ~2 kV/cm feature
multi-stage LPE -> possible but added interfaces reintroduce confounding.
```

The 2024 LPE control paper demonstrated broad linear gradients of order tens of `cm^-1`; the compact programmed feature is of order `10^3 cm^-1`.

### Growth matching

Measured realized `x(z)` should be inserted into each device's optical/transport forward model.

The structures do **not** need to be geometrically identical at the nominal-recipe level if their realized profiles are accurately characterized.

The dangerous residual is transport variation not explained by measured structure.

---

## 19. Randomization/replication principles remain valid, exact old schedules do not

Earlier deterministic-timing calculations showed that

```text
nonmonotonic growth order
+
replicated feature depths
```

can separate a feature-depth law from smooth chronological fabrication drift and estimate random run-to-run variance.

Those principles remain strong.

However, the exact previously optimized six/eight-run depth orders were derived with the superseded ad hoc timing operator.

Do **not** use them as final growth prescriptions.

After `v(E,x),D(E,x),tau(E,x)` are calibrated, rerun

```text
feature-depth selection
growth order
replicate-depth selection
wavelength allocation
and RF allocation
```

with the calibrated first-passage model.

---

## 20. Published sample B / temperature branch remains useful but secondary

The earlier sample-B work remains valid as

```text
smooth few-mode optical calibration
heteroscedastic phase-noise design
mid/deep wavelength design
and temperature iso-kernel control.
```

The robust mid/deep schedule around

```text
300 K 3.632 um
-> 215 K ~3.793 um
-> 115 K ~4.005 um
```

remains a useful independent control branch.

It is no longer the primary mechanism-localization experiment.

---

## 21. Current strongest experimental hierarchy

### Stage 1 — material transport calibration

Measure companion p-type HgCdTe

```text
v(E,x)
D(E,x)
tau(E,x)
```

at approximately `x=0.35,0.43,0.51`, beginning at 300 K.

### Stage 2 — optical/profile characterization

For every translated-gradient structure measure the realized

```text
x(z)
layer thickness
optical transfer
and relevant doping/profile variables.
```

### Stage 3 — instrument/electrical calibration

Measure wavelength × RF complex covariance, channel offsets, drift, and electrical transfer independently.

### Stage 4 — translated-feature complex-response experiment

Use high-Cd-side illumination and low-Cd-side collection.

Measure wavelength × RF complex response for several known feature depths.

### Stage 5 — joint inference

Condition the transport model on the witness posterior and each measured `x(z)`.

Ask whether the **depth law** of the response requires the localized gradient feature.

### Stage 6 — randomized/replicated fabrication validation

Only after the calibrated forward model is stable, optimize the number/order of feature-depth growths and replicated anchors against measured process covariance.

---

## 22. Current blockers

- direct 300 K `v(E,x),D(E,x),tau(E,x)` data for the intended p-type material campaign;
- measured realized `x(z)` for a purpose-built translated-gradient structure;
- high-Cd-side/backside optical transfer including substrate/reflection effects;
- measured wavelength × RF complex-response covariance;
- calibrated electrical/junction transfer;
- explicit doping / non-quasi-neutral boundary model where quasi-neutral approximation fails;
- full technical content of the unresolved 2024 laser-measurement prior-art paper;
- actual fabricated translated-gradient control series.

---

## 23. Next decisive work

Do **not** add another generic inverse theorem or another arbitrary timing basis.

The highest-value next theoretical/experimental design step is:

> **turn the three-composition transport-witness concept into a facility-ready calibration specification and propagate a realistic `v(E,x),D(E,x),tau(E,x)` posterior through the translated-gradient first-passage model.**

In parallel, continue the focused prior-art search for the unresolved 2024 laser-measurement paper.

Only after the transport law and real covariance are independently constrained should the final translated-depth / wavelength / RF / growth-order design be frozen or manuscript readiness reassessed.
