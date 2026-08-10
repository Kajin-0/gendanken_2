# Current State — Experiment 01: The Vanishing Absorber

**Date:** 2026-08-09  
**Status:** exploratory; active frontier is **few-mode differential wavelength × RF transport metrology in graded HgCdTe**, now separated into a mid/deep sample-B calibration/temperature program and a short-wave sample-A nonlinear-region contrast program; paired A-B data are treated as calibrated transport contrast rather than two independently recoverable profiles; no novelty claim

## 1. Current question

The original universal detector-bound program and the later universal entrance-gap timing-peak interpretation are stopped branches.

The active question is now:

> **Can a known graded-HgCdTe optical profile act as an internal spectral position encoder so wavelength × RF complex-response data recover a few differential transport modes, and can those modes be validated causally using the published smooth-gradient sample B versus nonlinear-gradient sample A?**

There is still **no manuscript**.

---

## 2. Read first

After root `AGENTS.md`:

1. `HGCDTE_SPECTRAL_TIMING_LINEAR_INVERSE.md`
2. `HGCDTE_PUBLISHED_SAMPLE_B_DIMENSIONAL_FORWARD_MATRIX.md`
3. `HGCDTE_PUBLISHED_SAMPLE_B_HETEROSCEDASTIC_PHASE_NOISE.md`
4. `HGCDTE_PUBLISHED_SAMPLE_B_OPTIMAL_MEASUREMENT_DESIGN.md`
5. `HGCDTE_SAMPLE_B_RF_FREQUENCY_VALIDITY.md`
6. `HGCDTE_PAIRED_SAMPLE_AB_DIFFERENTIAL_PHASE.md`
7. `HGCDTE_PHASE_PRECISION_SNR_REQUIREMENT.md`
8. `HGCDTE_PAIRED_PHASE_COMMON_MODE_REQUIREMENTS.md`
9. `HGCDTE_TEMPERATURE_ISO_KERNEL_DESIGN.md`
10. `HGCDTE_SAMPLE_A_CONSTRAINT_FAMILY_JOINT_ISO_KERNEL.md`
11. `HGCDTE_SAMPLE_A_THERMO_OPTIC_INTERFERENCE.md`
12. `HGCDTE_PAIRED_AB_JOINT_IDENTIFIABILITY.md`
13. `HGCDTE_SAMPLE_A_SHORTWAVE_VISIBILITY.md`
14. `HGCDTE_SAMPLE_A_SHORTWAVE_CALIBRATION_REQUIREMENT.md`
15. `HGCDTE_SPECTRAL_TIMING_TWO_MOMENT_INVERSE.md`
16. `HGCDTE_SPECTRAL_TIMING_TOMOGRAPHY_PRIOR_ART_AUDIT.md`
17. `CLAIM_LEDGER.md`
18. `RESEARCH_LOG.md`
19. `ARCHIVE_STATUS.md`

Older ballistic timing-peak and abstract universal-resource files are provenance only.

---

## 3. Hard prior-art boundary

Do **not** claim novelty for

- wavelength-dependent generation depth;
- wavelength-dependent photodetector timing/bandwidth;
- graded-bandgap carrier acceleration;
- graded-HgCdTe spectral response;
- wavelength- and depth-dependent graded-HgCdTe forward generation models;
- graded-HgCdTe response-time modeling;
- localized-position HgCdTe timing measurements.

The 2022 Sang et al. work already combines wavelength/depth generation with graded-HgCdTe forward transport/response modeling.

Perrais et al. already use localized excitation to study HgCdTe transit timing.

A 2024 same-group paper titled `Potential application of HgCdTe detector with composition gradient in laser measurement` remains an unresolved close collision because its technical text has not been recovered.

Current status:

> **candidate underexplored inverse-metrology method; priority unproven.**

The scientific value must come from demonstrated inverse measurement capability and controlled validation, not from the forward optical physics or elementary inversion algebra.

---

## 4. Orientation-correct inverse

Let

```math
p_i(x)=p(x|\lambda_i,{\rm abs})
```

and let `q_1(x)` be a path-additive mean-delay density.

For collection at `L`:

```math
\boxed{
\bar T_i
=\int_0^L F_i(s)q_1(s)ds,
\qquad
F_i(s)=P(X_g\le s).
}
```

For front collection at `0`:

```math
\boxed{
\bar T_i
=\int_0^L S_i(s)q_1(s)ds,
\qquad
S_i(s)=P(X_g\ge s).
}
```

The 2023 A/B devices use the second orientation: junction/collection at the high-Cd end.

Use cell-integrated kernels

```math
\boxed{
A_{ij}=\int_{\text{cell }j}K_i(s)ds,
\qquad
\mathbf T=\mathbf A\mathbf q_1.
}
```

Only under a local path-additive interpretation may one write

```math
q_1=1/v_{\rm eff}.
```

---

## 5. Common-delay / common-broadening gauge

For front collection,

```math
S_i(0)=1
```

for every wavelength.

Therefore sufficiently near-junction transport contributes almost the same delay to every wavelength and becomes degenerate with a wavelength-independent device/electronics delay.

The same issue applies to wavelength-independent second-cumulant broadening.

The robust objects are therefore **differential transport modes**.

Regularization choosing one decomposition is not proof of absolute identifiability.

This boundary gauge is now experimentally important because sample A's retained nonlinear/high-field region lies close to the collecting junction.

---

## 6. Two timing moments / full complex response

Under additive conditional timing cumulants:

```math
\boxed{
\mu_i=\int K_iq_1,
}
```

```math
\boxed{
\sigma_i^2
=\int K_iq_2
+\operatorname{Var}_{p_i}[m(X)].
}
```

Only under a local high-Peclet drift-diffusion approximation:

```math
q_1=1/v,
\qquad
q_2\simeq2D/v^3.
```

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

At higher normalized frequency, fit the full complex transfer rather than forcing a mean-delay interpretation.

---

## 7. Published 2023 A/B structures

### Sample B — smooth calibration/control

```text
processed thickness ~3.7 um
nominal FTIR x ~0.316
nonlinear interdiffusion region removed
junction at high-Cd end
remaining linear-gradient field ~100-200 V/cm.
```

The authors infer that this remaining linear field does not strongly alter carrier motion.

### Sample A — nonlinear/high-field contrast

```text
processed thickness ~7.6 um
nominal FTIR x ~0.320
part of nonlinear interdiffusion region retained
junction at high-Cd end
local nonlinear-gradient field approaches ~2e3 V/cm.
```

The accessible primary text also gives the composition-fit functional form, reports the nonlinear/interdiffusion region as approximately `4 um`, reports A's linear field about `30 V/cm` above B at equal temperature, and shows interference near sample A's cutoff.

The exact fitted numerical A/B `x(z)` tuples remain graphical and unavailable in machine-readable form.

---

## 8. Sample-B dimensional optical result

Current 300 K sample-B envelope:

```text
W = 3.7 um
x_low = 0.316
field bracket = 100-200 V/cm
central case = 150 V/cm
Hansen gap + Moazzami above-gap absorption.
```

Central optical points:

| wavelength | `Pabs` | mean generation depth | RMS width |
|---:|---:|---:|---:|
| 2.80 um | 0.998 | 0.677 um | 0.621 um |
| 3.20 um | 0.975 | 1.155 um | 0.860 um |
| 3.37 um | 0.917 | 1.704 um | 0.896 um |
| 3.50 um | 0.786 | 2.369 um | 0.703 um |
| 3.70 um | 0.417 | 3.088 um | 0.383 um |
| 3.85 um | 0.115 | 3.459 um | 0.161 um |
| 3.88 um | 0.070 | 3.523 um | 0.120 um |

Thus

```math
\boxed{
\Delta\langle z\rangle_{2.80\to3.88}
\approx2.85\ {\rm um}.
}
```

At illustrative `v_eff=1e5 m/s`, this is about `28.5 ps` or `10.25 degrees` at `1 GHz`.

That is a measurement scale, not a sample-B velocity prediction.

---

## 9. Sample-B few-mode rank and phase precision

For 80 spatial cells, `0.01 um` wavelength steps, `Pabs>=0.05`, and cell-integrated front kernels, relative singular-mode counts above `[1e-1,1e-2,1e-3,1e-4]` are

```text
100 V/cm -> [2,5,10,20]
150 V/cm -> [2,5,10,21]
200 V/cm -> [2,5,11,23].
```

Interpretation:

> **few-mode band-limited tomography, not pointwise depth imaging.**

A synthetic

```text
25% slowdown
center 2.30 um
sigma 0.35 um
baseline v=1e5 m/s
```

produces about

```math
0.935^\circ
```

peak-to-peak residual phase at 1 GHz.

At equal `0.10 degree` phase noise, a rank-3 inversion gives roughly `17.5%` median noise error relative to the recoverable rank-3 target; rank 5 is already noise dominated.

---

## 10. Heteroscedastic sample-B covariance and measurement resource

Across the retained sample-B scan, the absorbed-signal ratio is approximately

```math
\boxed{
P_{\rm abs}(2.80)/P_{\rm abs}(3.89)\approx17.6.
}
```

For a `0.10 degree` short-wave phase floor:

```text
statistics-like sigma_phi ~ Pabs^(-1/2)
-> long-wave sigma_phi ~0.42 degree
-> rank-3 error ~0.28

additive-like sigma_phi ~ Pabs^(-1)
-> long-wave sigma_phi ~1.76 degree
-> rank-3 error ~0.45.
```

Equalizing precision costs approximately

```text
~17.6x incident-power × integration-time resource
```

in the statistics-like case, or

```text
~309x integration time
```

in the simple additive-noise fixed-power limit.

Thus **optical rank and experimental rank are different objects**.

---

## 11. Sample-B D-optimal wavelength design

For

```text
3 smooth transport modes
+
1 common-phase nuisance,
```

the current reduced D-optimal supports are approximately:

### Statistics-like fixed-power noise

```text
2.800, 3.410, 3.632, 3.840 um.
```

### Additive-like fixed-power noise

```text
2.800, 3.400, 3.596, 3.780 um.
```

Each receives about one quarter of normalized time.

For the two fixed-power noise scalings, generalized D-information scale improves by about `34%` versus uniform-time use of the dense retained scan.

This is a **sample-B calibration design**, not the optimal wavelength set for localizing sample A's nonlinear region.

---

## 12. RF-frequency validity

Using only optical generation-depth broadening and deterministic `T=z/v`, current sample-B kernels give approximately

```math
\boxed{
f_{\max}\sim0.13\,v/W
}
```

for the illustrative criterion `|H|>0.98`.

Examples:

```text
v=1e5 m/s -> ~3.5 GHz
v=3e4 m/s -> ~1.05 GHz
v=1e4 m/s -> ~0.35 GHz.
```

This is an optical-only envelope; stochastic/electrical broadening can tighten it.

RF frequency should be adaptive.

---

## 13. Paired A/B phase cancellation and metrology requirements

For simultaneous same-source measurement at identical wavelength/frequency:

```math
\boxed{
\Delta\phi_{AB}
=-\Omega
(\mathbf A_A\mathbf q_A-
 \mathbf A_B\mathbf q_B)
+\Delta\phi_{\rm path}
+\Delta\phi_{\rm elec}.
}
```

Arbitrary common source phase cancels.

A reciprocal arm/device swap can cancel stable arm/channel asymmetry but gives no free white-noise SNR.

White-noise phase resource:

```math
\boxed{
\sigma_\phi^2\simeq\frac{S_I}{I_1^2t},
\qquad
\rho=\frac{I_1^2t}{S_I},
\qquad
\sigma_\phi\simeq\rho^{-1/2}.
}
```

Scales:

```text
0.10 degree single phase -> ~55.2 dB coherent power-SNR
0.10 degree A-B differential target, equal independent channels -> ~58.2 dB/channel.
```

For equal correlated channels:

```math
\sigma_{AB}=\sigma\sqrt{2(1-\rho_c)}.
```

For a `0.10 degree` target:

```text
1 degree individual RMS -> rho_c >0.995
5 degree -> rho_c >0.9998
10 degree -> rho_c >0.99995.
```

Reciprocal-swap residual:

```math
\boxed{
\delta\phi_{\rm swap}
=[\psi(t_1)-\psi(t_2)]/2.
}
```

A `0.10 degree` swap systematic budget therefore requires differential arm drift below roughly `0.20 degree` over the swap interval.

---

## 14. Mid/deep temperature control survives sample-A profile uncertainty

Because the exact A fit is graphical, an explicit 72-profile A sensitivity family was constructed from the published fit law and textual constraints:

```text
W_A = 7.6 um
conditional x_s = 0.320
A linear field = 130, 150, 180, 200 V/cm
Delta z = 3.5, 4.0, 4.5 um
processed front field = 1800, 2000, 2200 V/cm
both mathematical surface-field roots retained.
```

The `Delta z` and front-field spans are sensitivity coordinates, not experimental confidence intervals.

For the `3.632 um` 300 K common reference, equal-weight joint A/B kernel matching gives across all 72 profiles:

```text
215 K:
lambda* = 3.793356-3.793566 um
A mismatch = 0.215-0.229%
B mismatch = 0.447-0.453%
A Pabs = 0.290-0.410
B Pabs ~0.474

115 K:
lambda* = 4.004157-4.004870 um
A mismatch = 0.400-0.445%
B mismatch = 0.857-0.873%
A Pabs = 0.213-0.309
B Pabs = 0.357-0.358.
```

Provisional common schedule:

```text
300 K -> 3.632 um
215 K -> ~3.7935 um
115 K -> ~4.0045 um.
```

Exact A digitization is still needed for calibrated inversion and final uncertainty propagation, but it is no longer a hard feasibility gate for this mid/deep control.

---

## 15. Empirical thermo-optic interference does not destroy the mid/deep schedule

The candidate wavelengths satisfy the local-gap condition at almost one fixed composition coordinate:

```text
300 K, 3.6320 um -> x_edge = 0.337580
215 K, 3.7935 um -> x_edge = 0.337746
115 K, 4.0045 um -> x_edge = 0.337837.
```

Thus

```math
\Delta x_{\rm edge}<2.6\times10^{-4}.
```

Using the published composition/temperature-dependent HgCdTe real-index relation in a coherent one-return interference stress, across all 72 A profiles, `R=0.1-0.9`, and four reflection phases:

```text
215 K:
lambda* = 3.792986-3.794120 um
A mismatch <= ~0.74%
B mismatch <= ~0.48%

115 K:
lambda* = 4.002940-4.007453 um
A mismatch <= ~1.73%
B mismatch <= ~0.98%.
```

So generic interference strength is no longer the leading threat to the **wavelength location** of the mid/deep temperature control.

This is not yet a full repeated-reflection transfer-matrix model and does not calibrate absolute optical throughput.

---

## 16. Paired data cannot recover arbitrary smooth A and B profiles independently

The first three smooth spectral response subspaces of A and B overlap strongly.

Across the 72 A-profile family, principal angles are approximately

```text
theta1 = 0.210-0.875 deg, median 0.336 deg
theta2 = 3.524-15.695 deg, median 10.318 deg
theta3 = 33.546-65.356 deg, median 54.407 deg.
```

After column normalization, the weakest paired singular ratio is

```text
1 A mode + 1 B mode -> 0.0590-0.1937
2 + 2 -> 0.00853-0.04042
3 + 3 -> 0.001831-0.007633.
```

Thus a symmetric three-mode-per-device fit has a geometry-only weak-direction amplification of roughly

```text
130-550x
```

before real covariance or model uncertainty.

Correct interpretation:

> **paired data are well suited to transport contrast, not to independently reconstructing several arbitrary smooth modes in both devices.**

Sample-B calibration is therefore an identifiability requirement, not merely a useful control.

---

## 17. Critical correction — the mid/deep scan is nearly blind to A's retained nonlinear region

Use the published composition-gradient field only as a **spatial support template**:

```math
w_A(z)\propto[F_{\rm grad}(z)-F_{\rm lin}]_+.
```

Do **not** assume transport is proportional to field.

Across the 72 A profiles, the nonlinear support lies near the junction:

```text
support centroid = ~0.46-1.43 um
median ~0.88 um
90% support depth = ~1.03-2.65 um
median ~1.76 um.
```

In the current `2.8-3.83 um` band, the support-weighted normalized differential visibility is only

```math
\boxed{
0.0025-0.0430
}
```

with median about `0.0089`.

For the illustrative

```math
v(z)=10^5[1-0.25w_A(z)]\ {\rm m/s},
```

the mid/deep band gives only

```text
0.0023-0.0469 degree peak-to-peak @1 GHz
median ~0.0173 degree.
```

That is below the present `~0.1 degree` differential-phase target for every profile-family member.

Therefore the sample-B-optimized mid/deep scan should **not** be used as the primary localizer of sample A's nonlinear region.

---

## 18. Short-wave `2.0-2.8 um` scan restores raw A-specific leverage

At 300 K the local band-edge coordinate moves toward higher Cd composition as wavelength shortens:

```text
2.8 um -> x_edge ~0.4125
2.6 um -> ~0.4373
2.4 um -> ~0.4660
2.2 um -> ~0.4993
2.0 um -> ~0.5385.
```

Thus shorter wavelengths move the first allowed generation point into the near-junction nonlinear region.

For the same illustrative 25% support-shaped perturbation:

```text
2.4-2.8 um -> p-p phase 0.0329-0.1723 deg, median 0.0627
2.2-2.8 um -> 0.0637-0.2934 deg, median 0.1305
2.0-2.8 um -> 0.1081-0.3706 deg, median 0.2110.
```

The `2.0-2.8 um` median phase leverage is therefore about **12x larger** than the mid/deep result for the same imposed perturbation.

Optically this band is favorable in the current model:

```text
sample A:
Pabs(2.0) >0.99999
Pabs(2.8) >0.997
median mean-depth shift ~1.83 um

sample B:
Pabs(2.0) ~0.99996
Pabs(2.8) ~0.99772
mean-depth shift only ~0.296 um.
```

So A undergoes a large internal generation-position sweep while B remains shallow and both devices remain strongly absorbing.

`2.0 um` is at the short-wave edge of the current Moazzami fit range; do not extrapolate below it without another validated optical model.

---

## 19. Short-wave raw signal is still almost degenerate with smooth A/B transport

The short-wave scan solves the **raw visibility** problem but not the **model-separation** problem.

Build one physical A-localized anomaly response plus the first three smooth short-wave transport modes of A and first three of B.

After common-phase projection, the principal angle from the physical anomaly spectrum to the six-dimensional smooth nuisance subspace is only

```math
\boxed{
0.0063^\circ-0.708^\circ
}
```

with median

```math
\boxed{0.029^\circ.}
```

Thus the A-localized spectrum can be reproduced extremely closely by ordinary smooth A/B transport combinations.

The illustrative 25% anomaly has phase RMS

```math
\boxed{
0.0315^\circ-0.1206^\circ
}
```

with median `0.0651 degree` at 1 GHz over `2.0-2.8 um`.

This makes **smooth-mode calibration** the limiting inverse problem.

---

## 20. Quantified short-wave calibration requirement

Use 81 wavelengths from `2.00` to `2.80 um`, independent equal per-wavelength phase noise

```math
\sigma_\phi=0.10^\circ,
```

and normalize the anomaly plus six smooth nuisance response columns to unit spectral RMS. A nuisance prior is therefore a **phase-equivalent spectral-mode amplitude prior**, not a local velocity error.

For the illustrative A-localized anomaly:

| smooth-mode prior | anomaly posterior sigma | SNR range | median SNR | profiles `>=3 sigma` |
|---:|---:|---:|---:|---:|
| known | 0.01111 deg | 2.83-10.85 | 5.86 | 91.7% |
| 0.005 deg | ~0.01317 deg | 2.39-9.16 | 4.94 | 79.2% |
| 0.010 deg | ~0.01796-0.01798 deg | 1.75-6.71 | 3.62 | 50.0% |
| 0.020 deg | ~0.03030-0.03038 deg | 1.04-3.98 | 2.14 | 31.9% |
| 0.030 deg | ~0.04359-0.04383 deg | 0.72-2.76 | 1.49 | 0% |

To guarantee at least `3 sigma` over all 72 profiles under this illustrative model, the maximum equal per-wavelength noise is approximately

```text
known smooth nuisance -> 0.0944 deg
0.002 deg nuisance priors -> 0.0909 deg
0.005 deg nuisance priors -> 0.0697 deg.
```

Therefore:

> **short-wave spectral access gives enough raw signal, but calibrated separation from smooth A/B transport is now the limiting inverse problem.**

---

## 21. Current two-band experimental architecture

The project should no longer force one wavelength scan to do every job.

### Band A — short-wave A-specific contrast

```text
~2.0-2.8 um at 300 K
```

Purpose:

```text
move generation through A's retained nonlinear/high-field region
keep A and B strongly absorbing
maximize A-specific differential phase leverage
fit localized A contrast using calibrated smooth-mode priors.
```

### Band B — mid/deep B calibration and temperature control

```text
~3.4-4.0 um
```

Purpose:

```text
sample-B few-mode transport calibration
mid/deep optical-model validation
common A/B temperature iso-kernel control
provisional schedule 3.632 -> ~3.793 -> ~4.005 um.
```

The bands answer different scientific questions and should not be merged into one nominal D-optimal wavelength list.

---

## 22. Current strongest experimental hierarchy

### Stage 1 — two-arm metrology calibration

Before interpreting HgCdTe transport, measure

```text
sigma_A(lambda,f)
sigma_B(lambda,f)
rho_c(lambda,f)
residual differential phase PSD
Allan deviation / drift versus time
swap repeatability
frequency dependence
amplitude-to-phase conversion.
```

### Stage 2 — sample-B smooth transport calibration

Use the mid/deep band and full complex RF response to obtain a posterior/covariance on the few B modes that enter the paired observable.

### Stage 3 — constrain sample-A smooth baseline

Use spectral/temperature/bias information that is not dominated solely by the retained nonlinear region so the short-wave anomaly cannot be absorbed into arbitrary smooth A modes.

### Stage 4 — short-wave paired A-B contrast

Use approximately `2.0-2.8 um` to test whether an A-specific near-junction transport component is required after smooth A/B calibration.

### Stage 5 — mid/deep temperature difference-in-differences

Use the robust common-wavelength schedule as a separate causal transport perturbation/control rather than as the primary localizer of the nonlinear region.

### Stage 6 — independent transport validation

Compare with localized-position timing or a validated microscopic transport model.

---

## 23. What remains missing

- exact fitted/digitized sample A and B `x(z)` curves;
- full repeated-reflection/interference optical stack if needed for calibrated throughput;
- full technical text of the 2024 close-collision paper;
- measured wavelength × RF phase/magnitude covariance;
- calibrated sample-B smooth-mode posterior;
- calibrated sample-A smooth baseline;
- real complex-response data;
- independent microscopic/localized-position transport validation.

---

## 24. Next decisive work

Do **not** add another generic inverse theorem or merely sample more wavelengths uniformly.

The highest-value numerical design problem is now:

> **Optimize a sparse short-wave wavelength/RF design for the conditional information on an A-localized nonlinear-region contrast after marginalizing calibrated smooth A/B nuisance modes.**

The objective should be posterior anomaly variance / Fisher information after nuisance marginalization, **not raw peak-to-peak phase**.

In parallel, the decisive experimental input remains the measured two-arm differential covariance and drift.

Only after real-data or independently validated inversion should manuscript readiness be reassessed.
