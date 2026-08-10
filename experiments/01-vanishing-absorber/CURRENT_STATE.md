# Current State — Experiment 01: The Vanishing Absorber

**Date:** 2026-08-10  
**Status:** exploratory; strongest current path is a **purpose-built matched translated-gradient HgCdTe validation experiment** using wavelength × RF complex response as an internal spatial encoder; the published A/B pair remains valuable prior/control physics but is no longer considered a clean causal validation geometry; no novelty claim

There is still **no manuscript**.

---

## 1. Active question

The original universal detector-bound program, the later ballistic timing-peak route, and the attempt to rescue the published near-junction sample-A geometry by increasingly precise static calibration have all been superseded as the main frontier.

The active question is now:

> **Can a known compositionally graded HgCdTe absorber use wavelength as an internal position encoder so complex wavelength × RF data resolve differential transport, and can that inference be validated causally by translating the same buried internal gradient feature between otherwise matched devices?**

The project must earn its value through a clean inverse measurement and a falsifiable control geometry.

The forward facts that graded composition changes optical generation and carrier transport are already prior art.

---

## 2. Read first

After root `AGENTS.md`:

1. `HGCDTE_TRANSLATED_GRADIENT_PRIOR_ART_BOUNDARY.md`
2. `HGCDTE_PROGRAMMED_INTERFACE_SAFE_JOINT_DESIGN.md`
3. `HGCDTE_RELOCATION_EDGE_ENCODING.md`
4. `HGCDTE_PROGRAMMED_WIDTH_INTERDIFFUSION.md`
5. `HGCDTE_PROGRAMMED_TRANSLATED_GRADIENT_FEASIBILITY.md`
6. `HGCDTE_TRANSLATED_GRADIENT_MATCHING_TOLERANCES.md`
7. `HGCDTE_CONTACT_INTERFACE_CONFOUNDING.md`
8. `HGCDTE_SHORTWAVE_FINITE_RF_JACOBIAN.md`
9. `HGCDTE_SAMPLE_A_CROSSBAND_SELF_CALIBRATION.md`
10. `HGCDTE_SAMPLE_A_SHORTWAVE_GLOBAL_DESIGN.md`
11. `HGCDTE_SAMPLE_A_SHORTWAVE_CALIBRATION_REQUIREMENT.md`
12. `HGCDTE_PAIRED_AB_JOINT_IDENTIFIABILITY.md`
13. `HGCDTE_SPECTRAL_TIMING_LINEAR_INVERSE.md`
14. `HGCDTE_PUBLISHED_SAMPLE_B_DIMENSIONAL_FORWARD_MATRIX.md`
15. `HGCDTE_SPECTRAL_TIMING_TOMOGRAPHY_PRIOR_ART_AUDIT.md`
16. `CLAIM_LEDGER.md`
17. `RESEARCH_LOG.md`
18. `ARCHIVE_STATUS.md`

The published-sample A/B and mid/deep temperature branches remain important provenance and controls, but they are no longer the strongest mechanism-validation design.

---

## 3. Hard prior-art boundary

Do **not** claim novelty for

- wavelength-dependent absorption / generation depth;
- wavelength-dependent detector timing or bandwidth;
- composition-gradient built-in fields in HgCdTe;
- composition-gradient modification of HgCdTe carrier transport;
- high-speed or RF response of graded HgCdTe;
- graded-HgCdTe spectral response;
- wavelength/depth forward generation modeling;
- localized-position HgCdTe transit measurements;
- optical-load-dependent HgCdTe transient response;
- intentionally engineered positive composition gradients by LPE.

Sang et al. 2022 already measured high-speed graded-HgCdTe response and explicitly modeled composition-gradient-induced carrier transport. Their experiments include `1550 nm` impulse/RF excitation, `50 MHz-1 GHz` frequency response, and additional `2 um` switching tests.

Perrais et al. already used localized excitation to study HgCdTe transit timing.

Huo et al. 2024 demonstrated programmable positive HgCdTe composition gradients by LPE through mercury-loss/cooling control.

The 2024 same-group paper

`Potential application of HgCdTe detector with composition gradient in laser measurement`

DOI `10.5768/JAO202445.0310009`

remains an unresolved close collision because its full technical content has not been recovered.

Current candidate status:

> **candidate underexplored inverse-metrology / matched-relocation validation method; priority unproven.**

---

## 4. Core inverse and boundary gauge

For front collection at `0`, with known conditional generation density `p_i(x)` and path-additive mean-delay density `q_1(x)`, use

```math
\boxed{
\bar T_i
=\int_0^L S_i(s)q_1(s)ds,
\qquad
S_i(s)=P(X_g\ge s).
}
```

Cell-integrated form:

```math
\boxed{
A_{ij}=\int_{\mathrm{cell}\ j}S_i(s)ds,
\qquad
\mathbf T=\mathbf A\mathbf q_1.
}
```

Only under a local path-additive interpretation may one identify

```math
q_1=1/v_{\rm eff}.
```

The crucial gauge is

```math
S_i(0)=1
```

for every wavelength.

Therefore sufficiently near the collecting boundary, transport is almost wavelength independent and becomes degenerate with common device/electronics delay.

This is why the published sample-A near-junction high-gradient region turned out to be an intrinsically poor mechanism-localization geometry.

---

## 5. Frequency-domain observable

For timing transfer

```math
H_i(\Omega)=\langle e^{-i\Omega T_i}\rangle,
```

low-frequency cumulants give

```math
\arg H_i=-\Omega\mu_i+O(\Omega^3),
```

```math
\ln|H_i|=-\frac{\Omega^2}{2}\sigma_i^2+O(\Omega^4).
```

At higher normalized frequency the full complex response must be used.

Finite RF rotates the spatial sensitivity operator and adds real information, but the published A/B geometry remains strongly confounded even with `0.25-3 GHz` complex data.

RF diversity is therefore useful but is **not** a substitute for a cleaner physical control.

---

## 6. What the published A/B branch taught us

The published 2023 devices remain scientifically useful.

### Sample B

```text
processed thickness ~3.7 um
nominal FTIR x ~0.316
nonlinear interdiffusion region removed
weak linear gradient ~100-200 V/cm
junction at high-Cd end.
```

It remains a useful smooth calibration/control device.

### Sample A

```text
processed thickness ~7.6 um
nominal FTIR x ~0.320
part of nonlinear interdiffusion region retained
local gradient field near ~2 kV/cm
nonlinear region close to the collecting junction.
```

Short wavelengths `2.0-2.8 um` increase raw sensitivity to that region by roughly an order of magnitude compared with the mid/deep scan.

But the A-localized short-wave fingerprint is almost contained in ordinary smooth A/B transport response space.

The static short-wave experiment therefore requires smooth-mode priors at approximately the few-millidegree level.

A global fixed-time wavelength allocation cannot eliminate this calibration floor.

---

## 7. Published A/B is not a clean mechanism-identification pair

Two independent failures occur.

### A/B smooth-mode overlap

Several smooth A and B transport modes have strongly overlapping spectral response subspaces, so paired A-B data cannot reconstruct arbitrary smooth profiles in both devices independently.

### Contact/interface confounding

The sample-A nonlinear-region timing fingerprint can be reproduced extremely closely by a generic near-junction/contact transport contribution plus smooth bulk changes.

Therefore

> **observing an A-B timing difference would not by itself prove that the retained nonlinear composition-gradient region caused the difference.**

This is a mechanism-identifiability failure, not merely a phase-noise problem.

---

## 8. Strongest validation architecture — matched feature relocation

Replace the uncontrolled A/B comparison with a purpose-built matched family.

### `C` — smooth control

```text
same absorber endpoints
same contact/cap/junction environment
same thickness
smooth internal grading.
```

### `G1`

```text
same boundaries and broad process state
one buried compact high-gradient region at z1.
```

### `G2`

```text
same boundaries and feature shape
same total composition change
same high-gradient region translated to z2.
```

Then

```text
G - C
-> high-signal test that an additional internal transport component exists

G2 - G1
-> causal relocation test: does the wavelength x RF fingerprint move with the
   internal feature rather than staying attached to an interface/artifact?
```

The second comparison is the stronger mechanism test.

---

## 9. Why relocation is a better spatial observable

Let

```math
y(\lambda,f;z_0)
=\int K_{\lambda,f}(z)q_f(z-z_0)dz.
```

For a small translation `Delta z`,

```math
\boxed{
\Delta y
\simeq
\Delta z
\int K'_{\lambda,f}(z)q_f(z-z_0)dz.
}
```

For an ideal flat feature on `[a,b]`,

```math
\boxed{
\frac{\partial y}{\partial z_0}
=A[K(b)-K(a)].
}
```

So feature relocation creates a **signed edge fingerprint** rather than another smooth amplitude perturbation.

That is why it separates more strongly from low-order bulk and one-sided interface nuisance modes.

The identity is elementary and is not a novelty claim.

---

## 10. Growth-programmable feature

Use a monotonic endpoint-preserving composition profile with a compact high-gradient segment in the **composition-slope magnitude**.

Current useful family:

```text
absorber thickness L ~7.6 um
conceptual endpoints x_front ~0.55, x_back ~0.32
feature total width ~0.9-1.0 um
edge transition ~0.1 um
background gradient field of order 2e2 V/cm
local peak field ~1.95-2.0 kV/cm.
```

The exact trapezoid is not physically privileged.

It is a process-programmable proxy that can later be replaced by the measured realized `x(z)`.

---

## 11. Interface-safe joint depth/spectral design

Once the artificial shallow depth limit is removed, a raw optimizer tries to exploit the back boundary.

Therefore front **and** back interface nuisance modes are included, and the entire programmed feature is required to remain away from both interfaces.

With a conservative `1.5 um` feature-edge clearance, fixed total wavelength-time resource, and either

```text
statistics-like sigma_phi proportional to Pabs^(-1/2)
```

or

```text
additive-like sigma_phi proportional to Pabs^(-1),
```

the reference design is approximately

```math
\boxed{
z_1\sim4.1\ \mu m,
\qquad
z_2\sim5.5-5.6\ \mu m,
}
```

with

```math
\boxed{
\lambda\sim2.00-2.40\ \mu m.
}
```

The exact tenth-micron center is not stable enough to treat as a fabrication target; the robust conclusion is the **interior, micron-scale relocation geometry**.

For the nominal `~1 um` feature:

```text
minimum modeled Pabs ~0.99
minimum baseline |H| over 0.25-3 GHz ~0.98
1-GHz differential phase span ~0.36-0.39 deg
nuisance-orthogonal phase-vector norm of order 0.5 deg.
```

Under the current idealized covariance model, this is a finite precision problem rather than the near-singular published-A attribution problem.

---

## 12. Fixed measurement resource matters

The design score is not raw response or principal angle alone.

After covariance whitening and nuisance projection, use

```math
\boxed{
S_{\rm design}
=\frac{\|r_{\rm white}\|}{\sqrt{N_\lambda}}.
}
```

The `1/sqrt(N_lambda)` factor prevents a dense wavelength scan from winning merely because it consumes more total averaging time.

Under the same front/back nuisance and fixed-time rules, the conservative interior design carries roughly

```text
~1.9x information amplitude
~3.6x Fisher information
```

relative to the earlier restricted `2.6 -> 3.2 um` pair.

---

## 13. Edge sharpness is not the limiting fabrication resource

A spatial convergence test at

```text
80 cells  -> ~95 nm/cell
160 cells -> ~47.5 nm/cell
320 cells -> ~23.8 nm/cell
```

shows that edge ramps from roughly

```text
25-100 nm
```

lie on an approximately `1%` information plateau.

Broadening a `100 nm` edge to about `200 nm` costs roughly `30%` in fixed-time information amplitude.

Therefore

> **there is no resolved numerical evidence that an ultrasharp internal interface is required; ~0.1 um is already near the information plateau.**

---

## 14. Total width and interdiffusion are also tolerant

At fixed peak gradient field near `1.95 kV/cm`, the useful unblurred width range is broad:

```text
~0.9-1.1 um
```

with about `1.0 um` best on the current grid.

After Gaussian interdiffusion broadening, the optimum shifts only slightly toward `~0.9 um`.

Current fixed-time information-amplitude losses relative to the unblurred optimum are approximately

```text
sigma_d = 0.05 um -> ~8%
sigma_d = 0.10 um -> ~20%
sigma_d = 0.15 um -> ~33%.
```

The statistics-like and additive-like absorbed-signal noise envelopes choose essentially the same geometries.

A `320`-cell confirmation reproduces the trend.

---

## 15. Matching is an identifiability condition

For a nuisance mode write

```math
q_2=c+\delta/2,
\qquad
q_1=c-\delta/2.
```

Then

```math
\boxed{
J_2q_2-J_1q_1
=(J_2-J_1)c
+\frac{J_2+J_1}{2}\delta.
}
```

Common matched variation `c` can be fitted.

Differential mismatch `delta` creates the dangerous artifact.

The purpose-built geometry becomes strongly degenerate again if the two devices are allowed arbitrary independent contact/bulk changes.

Thus matched fabrication is not cosmetic; it is part of the identifiability proof.

The exact mismatch tolerances should be recomputed for the final interface-safe/process-specific profile rather than inherited from the earlier shallow design.

---

## 16. Wavelength-independent electrical response cancels exactly

Suppose

```math
M_j(\lambda,f)=E_j(f)H_j(\lambda,f),
```

where `E_j(f)` is any wavelength-independent electrical/readout transfer.

After taking the paired log response and removing an arbitrary complex wavelength-independent intercept at each RF frequency,

```math
\boxed{
C_\lambda[\ln E_2(f)-\ln E_1(f)]=0.
}
```

Therefore a pure wavelength-independent RC/readout mismatch is not the leading electrical problem in the relocation fingerprint.

The dangerous electrical terms are those that vary with wavelength, signal level, or device optical state.

---

## 17. Materials feasibility

The required spatial scale is not obviously unrealistic.

### MBE

Strong direct precedent for programmed HgCdTe composition/thickness profiles and in-situ control. This remains the cleanest conceptual first route.

### MOCVD

Strong graded-heterostructure precedent; realized interdiffusion must be measured and inserted into the model.

### LPE

The 2024 Huo et al. work demonstrated control of HgCdTe longitudinal composition-gradient sign/magnitude through mercury-loss and cooling conditions and verified the profile by thinning spectroscopy and SIMS.

Therefore LPE is also a real candidate for broad gradient programming.

What none of the recovered literature yet establishes is the **specific matched translated internal feature** required here.

---

## 18. Published sample B and temperature control are now secondary controls

The earlier sample-B work remains valid and useful:

```text
smooth few-mode calibration
heteroscedastic phase-noise design
mid/deep D-optimal wavelengths
and robust ~3.632 -> 3.793 -> 4.005 um temperature iso-kernel schedule.
```

But these are no longer the main mechanism-identification experiment.

The published A/B pair should be treated as

```text
literature-grounded phenomenology / benchmark
```

while the matched translated-gradient family supplies the cleaner causal test.

---

## 19. Important nonclaims

Do not claim

- pointwise high-resolution `v(z)` reconstruction;
- absolute common delay/broadening from wavelength data alone;
- transport proportionality to composition-gradient field;
- that the illustrative `25%` feature-supported perturbation is a device prediction;
- that `4.1` and `5.6 um` are universal optimal feature depths;
- that the trapezoidal profile is a fabrication recipe;
- that any particular growth method has demonstrated the exact matched translated pair;
- novelty/priority;
- manuscript readiness.

---

## 20. Active numerical regressions

Most important current files:

```text
numerics/hgcdte_programmed_joint_depth_spectral_design.py
numerics/hgcdte_programmed_width_interdiffusion.py
numerics/hgcdte_relocation_edge_convergence.py
numerics/hgcdte_programmed_gradient_tolerances.py
numerics/hgcdte_matched_contact_translated_gradient_design.py
numerics/hgcdte_shortwave_finite_rf_jacobian.py
numerics/hgcdte_contact_confounding.py
numerics/hgcdte_sample_a_crossband_self_calibration.py
```

Older sample-A/B scripts remain provenance and benchmark calculations.

---

## 21. Current blockers

The remaining blockers are concrete:

1. **full technical recovery of the 2024 Applied Optics close-collision paper**;
2. a process-specific reachable `x(z)` model for MBE, MOCVD, or LPE rather than generic smoothing;
3. a final matched-pair mismatch tolerance analysis on that process-specific profile;
4. real wavelength × RF phase/magnitude covariance and drift data;
5. wavelength-dependent electrical-state characterization;
6. a validated transport model beyond the deterministic illustrative baseline;
7. independent measurement of the realized depth profile;
8. actual matched-device data.

---

## 22. Next decisive work

Do **not** add another generic inverse theorem or optimize another arbitrary geometric parameter.

The strongest next theoretical/material step is:

> **Choose one realistic HgCdTe growth route and generate a reachable family of matched translated `x(z)` profiles from its actual process physics, then pass that family through the interface-safe fixed-resource wavelength × RF design.**

In parallel, the most important literature task remains recovery of DOI `10.5768/JAO202445.0310009`.

The most important experimental input remains real differential wavelength × RF covariance.

Only after those are resolved should manuscript readiness or novelty language be reconsidered.
