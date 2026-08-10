# Research Log Continuation — 2026-08-10

This file continues `RESEARCH_LOG.md` without rewriting the earlier chronology.

Purpose: record **why the direction changed** from published A/B short-wave calibration toward a purpose-built matched translated-gradient validation experiment.

---

## Sample-A profile uncertainty stopped being the main feasibility gate

The 2023 Xu et al. primary text exposed the sample-A composition-fit law and several textual structural constraints, while the fitted numerical tuple remained graphical.

A 72-profile sample-A sensitivity family was therefore built rather than inventing one exact profile.

The mid/deep joint A/B temperature iso-kernel schedule survived that uncertainty.

For a `3.632 um` 300 K reference, the common matched wavelength stayed near

```text
215 K -> ~3.7935 um
115 K -> ~4.0045 um.
```

Conclusion: exact A digitization remains necessary for calibrated inversion, but it is not the sole feasibility gate for mid/deep temperature control.

---

## Interference did not kill the mid/deep schedule

The 2023 paper reports interference near sample A's cutoff.

A one-return coherent interference stress was first run with broad reflectivity/index envelopes, then with a composition/temperature-dependent HgCdTe refractive-index relation.

The common mid/deep schedule moved only slightly.

The key geometric reason is that the retuned wavelengths follow nearly one fixed local band-edge composition coordinate.

Conclusion: generic interference strength is not the leading threat to the **wavelength location** of the mid/deep temperature control, although a calibrated full optical stack is still absent.

---

## Paired A/B does not support two arbitrary smooth profile inverses

The first several smooth A and B spectral-response modes were compared directly.

Their subspaces overlap strongly.

For three smooth modes per device, the weakest normalized paired singular direction is of order `10^-3` to `10^-2`, implying roughly `10^2-10^3` geometric amplification before real covariance/model uncertainty.

Conclusion:

> paired A/B data should be interpreted as calibrated transport **contrast**, not as two independent arbitrary transport profiles.

Sample-B calibration became an identifiability requirement rather than merely a convenient control.

---

## Critical geometry correction — the published A nonlinear region is too close to the collecting boundary

The front-collection survival kernel satisfies

```math
S_i(0)=1
```

for every wavelength.

The published sample-A nonlinear/high-field region sits close to that same boundary.

Using composition-gradient-field excess only as a **spatial support template**, the mid/deep scan was found to have very little differential leverage there.

For one fixed illustrative `25%` support-shaped transport perturbation, the mid/deep phase span was below the current `~0.1 degree` target throughout the 72-profile family.

Conclusion: the sample-B-optimized mid/deep band is the wrong primary localizer for sample A's near-junction region.

---

## Short-wave access solved raw visibility but exposed a worse calibration problem

Moving to `2.0-2.8 um` shifts the local gap coordinate toward the high-Cd near-junction region.

For the same illustrative perturbation, the median phase leverage increased by roughly an order of magnitude.

However, the A-localized short-wave spectral fingerprint was almost contained in the span of three smooth A and three smooth B modes.

The principal-angle median was only of order `0.03 degree`.

Conclusion:

> short wavelengths solve the raw signal problem, not the mechanism-separation problem.

---

## Global wavelength design could not remove the smooth-mode calibration floor

A fixed-total-time two-band search first found a strong pair near

```text
2.00 um
and
~2.69 um.
```

A full arbitrary-support wavelength allocation then confirmed that the optimum essentially collapses to the same two-band structure.

With an equal smooth-mode prior around `0.005 degree`, the illustrative target can cross `3 sigma` across the current profile family.

At a `0.010 degree` prior, even globally optimized wavelength allocation fails to guarantee `3 sigma`.

Conclusion: there is no spectral-sampling trick that eliminates the calibration floor.

---

## Both A and B baselines matter

Separating the smooth-mode priors showed that neither sample B calibration alone nor sample A calibration alone is enough.

The approximate equal-prior boundary was around a few millidegrees, with an elliptical A/B tradeoff in response-equivalent prior space.

Conclusion: the static short-wave published-A experiment requires an unusually accurate **A smooth baseline as well as B control**.

---

## Mid/deep A cannot cheaply self-calibrate the short-wave A baseline

The first short-wave A smooth mode is weakly visible in mid/deep A phase data.

At `0.10 degree` per wavelength, its short-wave-equivalent uncertainty is orders of magnitude larger than the few-millidegree prior needed by the static A-localized test.

A broad `2.0-3.83 um` no-prior fit also remains badly conditioned.

Conclusion: merely collecting a broader spectrum does not solve the A-baseline problem.

---

## Short-wave temperature difference-in-differences failed the full-kernel test

Temperature was an attractive causal perturbation because the mid/deep branch supports robust iso-kernel retuning.

But short-wave full A/B kernels cannot be held nearly invariant at 215/115 K by simple wavelength retuning.

The baseline leakage term

```math
[A(T)-A(T_0)]q_0
```

therefore re-enters the subtraction.

Conclusion: temperature remains a useful mid/deep control but is the wrong primary perturbation for near-junction short-wave localization.

---

## Optical-load curvature became a control, not a novelty route

Optical-load differencing initially looked attractive because normalized linear-absorption kernels can remain fixed while carrier state changes.

A three-load second difference has optimal dwell ratio `1:2:1` and cancels static plus approximately linear load-dependent terms.

However, prior-art review recovered HgCdTe transient-photovoltage/lifetime work in which response changes with steady optical background.

Conclusion:

> optical-load-dependent timing is established prior art. Load curvature can be a nuisance-rejecting control construction, but it is not the project contribution.

A further exact point was noted: if optical load does not change the normalized spatial generation kernel, load differencing does not create a new spatial imaging operator.

---

## Finite RF rotates sensitivity but does not rescue the published geometry

The full finite-frequency complex Jacobian was built over

```text
0.25, 0.5, 1, 2, 3 GHz.
```

Frequency diversity increases the geometric angle between the illustrative A-localized target and smooth A/B nuisance space, but not enough to make the no-prior published geometry well conditioned.

Conclusion: RF is a real information coordinate, but it cannot substitute for physical experimental control.

---

## Contact/interface confounding became the decisive failure

A generic near-junction exponential transport contribution was compared with the published sample-A nonlinear-region support.

The fingerprints can be made extremely close; adding smooth bulk modes makes the separation smaller still.

Prior HgCdTe transient work also shows contact/interface transients themselves can depend on material composition and temperature.

The published A and B devices do not provide perfectly matched collection-side conditions.

Conclusion:

> an A-B timing difference cannot by itself be attributed uniquely to the retained nonlinear composition-gradient region.

This changed the research question from “how accurately can we invert sample A?” to “what device geometry would make the mechanism identifiable?”

---

## Purpose-built matched-contact control introduced

A three-device validation family was proposed:

```text
C  -> smooth endpoint/contact-matched control
G1 -> one buried compact internal gradient feature
G2 -> same feature translated deeper.
```

Then

```text
G-C
-> existence/high-signal contrast

G2-G1
-> causal relocation test.
```

If the wavelength × RF fingerprint moves with the internal feature while boundaries remain fixed, contact/interface attribution becomes substantially harder.

---

## Endpoint-preserving translated composition profile constructed

A mean-preserving modulation of composition-slope magnitude was used:

```math
s(z)=s_0[1+a(h-\langle h\rangle)].
```

Because the modulation has zero spatial mean, translating `h(z)` leaves

```text
x(0)
x(L)
and total composition change
```

fixed.

A first Gaussian feature showed that a buried `~2 kV/cm` gradient enhancement is mathematically compatible with a monotonic `7.6 um` composition profile.

---

## First matched-pair result — matching is an identifiability condition

With common smooth/contact nuisance amplitudes, a translated pair separates much more strongly than the published near-junction feature.

If those nuisance amplitudes are allowed to vary independently in both devices, the separation collapses again.

Exact decomposition:

```math
q_2=c+\delta/2,
\qquad
q_1=c-\delta/2,
```

```math
J_2q_2-J_1q_1
=(J_2-J_1)c+\frac{J_2+J_1}{2}\delta.
```

Conclusion:

> matched fabrication is part of the identifiability design, not an experimental convenience.

---

## Wavelength-independent electrical poles can be removed exactly

For

```math
M_j(\lambda,f)=E_j(f)H_j(\lambda,f),
```

one arbitrary wavelength-independent complex intercept at each RF frequency removes the factor `E_2(f)/E_1(f)` from the relocation fingerprint.

Conclusion: a pure wavelength-independent RC/readout mismatch is not the leading electrical systematic in this design.

Wavelength-dependent or signal-state-dependent electrical effects remain open.

---

## Gaussian profile replaced by a growth-programmable segment

The Gaussian slope bump was only a mathematical convenience.

It was replaced by a compact programmed high-gradient segment with a micron-scale width and finite transition ramps.

A nominal `1.0 um` feature with `0.1 um` edge ramps can reproduce approximately

```text
background gradient field ~2e2 V/cm
local maximum ~2 kV/cm
```

while preserving endpoint composition.

The fabrication-like segment increased mechanism separation rather than degrading it.

---

## Materials feasibility became plausible across MBE, MOCVD, and LPE

Primary literature established:

### MBE

Deliberate HgCdTe composition/thickness programming and in-situ ellipsometric control are well established. Reported quantum-well metrology scales are far finer than the micron-scale relocation required here.

### MOCVD

Designed internal graded sublayers have been fabricated and realized `x(z)` measured by SIMS. Interdiffusion must be included explicitly.

### LPE correction

A 2024 primary study by Huo et al. demonstrated control of longitudinal HgCdTe composition-gradient sign/magnitude using mercury-loss rate and cooling trajectory, with the resulting `x(z)` verified by thinning spectroscopy and SIMS.

Conclusion: LPE is more programmable than the earlier branch assumed. The exact matched compact feature translation remains unproven for all three routes.

---

## Major numerical correction — the first depth grid was artificially shallow

The initial translated-feature search ended at `3.2 um` because it inherited the sample-A short-wave geometry.

Extending the grid showed increasing information as one feature moved toward the back boundary.

That was not accepted as a result because it simply replaced the front-interface confound with a back-interface opportunity.

Conclusion: **both boundaries must be explicit nuisance sources.**

---

## Interface-safe joint depth and wavelength optimization

The design was rebuilt with

```text
front interface nuisance exponentials
back interface nuisance exponentials
cubic smooth bulk nuisance
arbitrary complex intercept per RF
Pabs-dependent phase precision
fixed total wavelength-time resource.
```

The full programmed feature was also required to remain a chosen distance from both boundaries.

With `1.5 um` feature-edge clearance, both the statistics-like and additive-like phase-noise envelopes select approximately

```text
feature center 1 ~4.1 um
feature center 2 ~5.5-5.6 um
wavelength band ~2.00-2.40 um.
```

The exact tenth-micron depth is not treated as a fabrication target.

Relative to the earlier shallow pair under the same rules, the interior design gives roughly

```text
~1.9x information amplitude
~3.6x Fisher information.
```

Conclusion: the strongest current experiment is genuinely **buried**, not boundary-adjacent.

---

## Relocation interpreted as edge encoding

For

```math
y(\lambda,f;z_0)=\int K_{\lambda,f}(z)q_f(z-z_0)dz,
```

a small translation gives

```math
\Delta y\simeq\Delta z\int K'_{\lambda,f}(z)q_f(z-z_0)dz.
```

For a flat compact feature `[a,b]`:

```math
\frac{\partial y}{\partial z_0}=A[K(b)-K(a)].
```

Conclusion: the relocation comparison is a signed **edge fingerprint**. This explains why it is harder for smooth/boundary nuisance modes to mimic than a simple feature-amplitude comparison.

The algebra is elementary and is not a novelty claim.

---

## Apparent ultrasharp-edge optimum rejected as numerical under-resolution

The canonical transport grid initially had only `80` cells over `7.6 um`, about `95 nm/cell`.

An apparent preference for a `~50 nm` transition was therefore below numerical resolution.

The calculation was rebuilt at

```text
80
160
320 cells.
```

At 320 cells, edge ramps from `25` to `100 nm` form only an approximately `1%` information plateau.

A `200 nm` transition loses roughly `30%` relative to `100 nm`.

Conclusion:

> there is no resolved evidence that an ultrasharp interface is needed; `~0.1 um` is already near the information plateau.

---

## Total feature width and generic interdiffusion stress

Feature width was then varied at approximately fixed `1.95 kV/cm` peak gradient field.

The useful unblurred range is broad:

```text
~0.9-1.1 um
```

with `~1.0 um` best on the current grid.

A Gaussian interdiffusion blur was then imposed, with the nominal feature edge plus `3 sigma_d` still required to clear both boundaries by `1.5 um`.

After reoptimization:

```text
sigma_d=0.05 um -> ~8% information-amplitude loss
sigma_d=0.10 um -> ~20% loss
sigma_d=0.15 um -> ~33% loss.
```

The statistics-like and additive-like absorbed-signal noise envelopes choose essentially the same geometry.

A 320-cell check reproduces the selected scores.

Conclusion: moderate interdiffusion degrades the experiment gradually rather than destroying identifiability.

---

## Prior-art boundary tightened around the surviving contribution

Sang et al. 2022 already report high-speed room-temperature graded-HgCdTe response, composition-gradient built-in-field transport modeling, `1550 nm` impulse/RF excitation, `50 MHz-1 GHz` frequency response, and `2 um` switching measurements.

Therefore the project **cannot** claim novelty for

```text
graded HgCdTe high-speed response
RF measurement of graded HgCdTe
short-wave timing of graded HgCdTe
or composition-gradient modification of carrier transit.
```

The surviving candidate has narrowed to

```text
wavelength deliberately used as an internal spatial encoder
+
complex wavelength x RF inverse
+
matched buried-feature relocation
+
causal test that the fingerprint moves with the feature.
```

Priority remains unproven.

The 2024 Applied Optics paper

```text
Potential application of HgCdTe detector with composition gradient in laser measurement
DOI 10.5768/JAO202445.0310009
```

remains unresolved because full primary technical text has not been recovered.

---

## Current frontier

The geometry is now mature enough that further free-form optimization has diminishing value.

Do **not** add another generic inverse theorem.

The next decisive theoretical/material step is:

> **Choose one actual HgCdTe growth route and generate a process-reachable matched translated `x(z)` family from its growth physics, then pass that family through the interface-safe fixed-resource wavelength × RF design.**

Parallel blockers:

```text
recover the 2024 Applied Optics close-collision paper
obtain real wavelength x RF phase/magnitude covariance and drift
characterize wavelength-dependent electrical-state effects
validate transport beyond the illustrative deterministic baseline
measure realized x(z)
and obtain matched-device data.
```

There is still **no manuscript** and no novelty claim.
