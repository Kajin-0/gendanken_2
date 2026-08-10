# Current State — Experiment 01: The Vanishing Absorber

**Date:** 2026-08-09  
**Status:** exploratory; active frontier is **few-mode differential wavelength × RF transport metrology in graded HgCdTe**; the experiment is now split into a mid/deep calibration-temperature branch and a short-wave sample-A nonlinear-region contrast branch; paired A-B data are treated as calibrated contrast rather than two independently recoverable profiles; no novelty claim

There is still **no manuscript**.

---

## 1. Active question

The original universal detector-bound program and the later universal entrance-gap timing-peak interpretation are stopped branches.

The active question is:

> **Can a known graded-HgCdTe optical profile act as an internal spectral position encoder so wavelength × RF complex-response data recover a few differential transport modes, and can those modes be validated causally using the published smooth-gradient sample B versus nonlinear-gradient sample A?**

The scientific value must come from demonstrated inverse measurement capability and controlled validation, not from the already-known forward optical physics or elementary inversion algebra.

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
15. `HGCDTE_SAMPLE_A_SHORTWAVE_TWO_BAND_DESIGN.md`
16. `HGCDTE_SAMPLE_A_SHORTWAVE_GLOBAL_DESIGN.md`
17. `HGCDTE_SPECTRAL_TIMING_TWO_MOMENT_INVERSE.md`
18. `HGCDTE_SPECTRAL_TIMING_TOMOGRAPHY_PRIOR_ART_AUDIT.md`
19. `CLAIM_LEDGER.md`
20. `RESEARCH_LOG.md`
21. `ARCHIVE_STATUS.md`

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

The 2024 same-group paper

`Potential application of HgCdTe detector with composition gradient in laser measurement`

remains an unresolved close collision because its full technical text has not been recovered.

Current candidate status:

> **candidate underexplored inverse-metrology method; priority unproven.**

---

## 4. Exact inverse and boundary gauge

For front collection at `0`, with conditional generation distribution `p_i(x)` and path-additive mean-delay density `q_1(x)`, use the survival kernel

```math
\boxed{
\bar T_i
=\int_0^L S_i(s)q_1(s)ds,
\qquad
S_i(s)=P(X_g\ge s).
}
```

Cell-integrated discretization:

```math
\boxed{
A_{ij}=\int_{\mathrm{cell}\ j}S_i(s)ds,
\qquad
\mathbf T=\mathbf A\mathbf q_1.
}
```

Only under a local path-additive interpretation may one write

```math
q_1=1/v_{\rm eff}.
```

The crucial gauge is

```math
S_i(0)=1
```

for every wavelength.

Therefore sufficiently near-junction transport becomes almost wavelength independent and is degenerate with common device/electronics delay.

The robust objects are **differential transport modes**, not arbitrary absolute delay profiles.

The same common/boundary ambiguity applies to the second timing cumulant.

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

At higher normalized frequency, fit the full complex transfer instead of forcing a mean-delay interpretation.

Only under a local high-Peclet drift-diffusion approximation:

```math
q_1=1/v,
\qquad
q_2\simeq2D/v^3.
```

Do not identify reconstructed `q_2` with microscopic diffusion without transport validation.

---

## 6. Published A/B structures

### Sample B — smooth calibration/control

```text
processed thickness ~3.7 um
nominal FTIR x ~0.316
nonlinear interdiffusion region removed
junction at high-Cd end
remaining linear-gradient field ~100-200 V/cm.
```

The authors infer that the remaining weak linear gradient does not strongly alter carrier motion.

### Sample A — nonlinear/high-field contrast

```text
processed thickness ~7.6 um
nominal FTIR x ~0.320
part of nonlinear interdiffusion region retained
junction at high-Cd end
local nonlinear-gradient field approaches ~2e3 V/cm.
```

The primary 2023 text also gives the composition-fit functional form, reports an approximately `4 um` nonlinear/interdiffusion region, reports A's linear field about `30 V/cm` above B at equal temperature, and shows interference near sample A's cutoff.

The exact fitted numerical A/B `x(z)` tuples remain graphical rather than machine readable.

---

## 7. Sample-B mid/deep calibration branch

Current 300 K sample-B central envelope:

```text
W = 3.7 um
x_low = 0.316
linear field = 150 V/cm
Hansen gap + Moazzami above-gap absorption.
```

Representative optical points:

```text
2.80 um -> Pabs 0.998, mean depth 0.677 um
3.88 um -> Pabs 0.070, mean depth 3.523 um.
```

Thus

```math
\boxed{\Delta\langle z\rangle\approx2.85\ {\rm um}.}
```

At illustrative `v_eff=1e5 m/s`, this corresponds to about `28.5 ps` or `10.25 degrees` at `1 GHz`.

Cell-integrated singular-mode counts above `[1e-1,1e-2,1e-3,1e-4]` are

```text
100 V/cm -> [2,5,10,20]
150 V/cm -> [2,5,10,21]
200 V/cm -> [2,5,11,23].
```

Interpretation:

> **few-mode band-limited tomography, not pointwise depth imaging.**

---

## 8. Sample-B covariance and optimized mid/deep design

Across the retained sample-B scan,

```math
P_{\rm abs}(2.80)/P_{\rm abs}(3.89)\approx17.6.
```

At fixed incident power, equal phase noise is therefore not a realistic default.

For a `0.10 degree` short-wave phase floor:

```text
statistics-like sigma_phi ~ Pabs^(-1/2)
-> long-wave sigma_phi ~0.42 degree

additive-like sigma_phi ~ Pabs^(-1)
-> long-wave sigma_phi ~1.76 degree.
```

For `3` smooth B transport modes plus `1` common phase nuisance, current reduced D-optimal supports are approximately

```text
statistics-like:
2.800, 3.410, 3.632, 3.840 um

additive-like:
2.800, 3.400, 3.596, 3.780 um.
```

This is a **sample-B calibration design**, not the A-localized contrast design.

---

## 9. RF validity

Using only optical generation-depth broadening and deterministic `T=z/v`, current sample-B kernels give the illustrative envelope

```math
\boxed{f_{\max}\sim0.13\,v/W}
```

for `|H|>0.98`.

Examples:

```text
v=1e5 m/s -> ~3.5 GHz
v=3e4 m/s -> ~1.05 GHz
v=1e4 m/s -> ~0.35 GHz.
```

This is optical-only; stochastic carrier and electrical broadening can tighten it.

RF frequency should be adaptive.

---

## 10. Paired A/B phase and metrology requirements

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

A reciprocal arm/device swap can remove stable arm asymmetry under the stated reciprocity assumptions, but it is not a free random-noise SNR gain.

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
0.10 degree A-B differential target with equal independent channels -> ~58.2 dB/channel.
```

For equal correlated channels and a `0.10 degree` differential target:

```text
1 degree individual RMS -> rho_c >0.995
5 degree -> rho_c >0.9998
10 degree -> rho_c >0.99995.
```

A `0.10 degree` reciprocal-swap systematic budget requires differential arm drift below roughly `0.20 degree` over the swap interval.

---

## 11. Mid/deep joint temperature control is conditionally robust

Because the exact A fit is unavailable numerically, a 72-profile sensitivity family was built from the published fit law and textual constraints.

For the common `3.632 um` 300 K reference, Beer-Lambert joint A/B matching gives across all 72 profiles approximately

```text
215 K:
lambda* = 3.793356-3.793566 um
A mismatch = 0.215-0.229%
B mismatch = 0.447-0.453%

115 K:
lambda* = 4.004157-4.004870 um
A mismatch = 0.400-0.445%
B mismatch = 0.857-0.873%.
```

Provisional common schedule:

```text
300 K -> 3.632 um
215 K -> ~3.7935 um
115 K -> ~4.0045 um.
```

A composition-resolved thermo-optic one-return interference stress leaves the schedule close to the same wavelengths:

```text
215 K -> 3.792986-3.794120 um
115 K -> 4.002940-4.007453 um
```

with worst sample-A kernel mismatch below about `0.74%` and `1.73%`, respectively, over the stated stress family.

The schedule follows nearly one fixed local-gap composition coordinate:

```text
x_edge ~0.3376-0.3378
```

from 300 to 115 K.

This is not yet a calibrated full transfer-matrix result.

---

## 12. Paired A/B data are contrast data, not two independent inverses

The first three smooth A/B spectral response subspaces overlap strongly.

Across the 72 A-profile family:

```text
principal angle 1 = 0.210-0.875 deg
principal angle 2 = 3.524-15.695 deg
principal angle 3 = 33.546-65.356 deg.
```

For a symmetric `3 A modes + 3 B modes` fit, the weakest normalized paired singular ratio is only

```text
0.001831-0.007633,
```

corresponding to roughly `130-550x` geometry-only weak-direction amplification before real covariance or model uncertainty.

Therefore:

> **sample-B calibration is an identifiability requirement. Paired data should be interpreted as calibrated transport contrast, not as two arbitrary smooth absolute profiles.**

---

## 13. Critical sample-A correction — mid/deep wavelengths are nearly blind to the retained nonlinear region

Using the nonlinear composition-gradient-field excess only as a spatial support template,

```math
w_A(z)\propto[F_{\rm grad}(z)-F_{\rm lin}]_+,
```

the retained nonlinear region lies near the collecting junction:

```text
support centroid ~0.46-1.43 um
median ~0.88 um
90% support depth ~1.03-2.65 um.
```

In the `2.8-3.83 um` band, support-weighted normalized differential visibility is only

```text
0.0025-0.0430
median ~0.0089.
```

For the illustrative transport perturbation

```math
v(z)=10^5[1-0.25w_A(z)]\ {\rm m/s},
```

the mid/deep scan produces only

```text
0.0023-0.0469 degree peak-to-peak @1 GHz
median ~0.0173 degree.
```

That is below the current `~0.1 degree` differential-phase target throughout the profile family.

---

## 14. Short-wave `2.0-2.8 um` access restores raw A-specific leverage

At 300 K:

```text
2.8 um -> local gap coordinate x ~0.4125
2.6 um -> ~0.4373
2.4 um -> ~0.4660
2.2 um -> ~0.4993
2.0 um -> ~0.5385.
```

Thus shorter wavelength moves first allowed generation into the near-junction nonlinear region.

For the same illustrative 25% support-shaped perturbation:

```text
2.4-2.8 um -> 0.0329-0.1723 deg p-p, median 0.0627
2.2-2.8 um -> 0.0637-0.2934 deg, median 0.1305
2.0-2.8 um -> 0.1081-0.3706 deg, median 0.2110.
```

The median phase leverage is therefore about `12x` larger than in the mid/deep scan.

Both devices remain strongly absorbing in the current model, while A's mean generation depth moves much more strongly than B's.

`2.0 um` is the lower edge of the currently validated Moazzami optical range used here. Do not extrapolate below it without another optical model.

---

## 15. Short-wave visibility is still almost degenerate with smooth A/B transport

Build one A-localized anomaly response plus the first three smooth short-wave modes of A and first three of B.

The principal angle from the anomaly spectrum to the six-dimensional smooth nuisance subspace is only

```math
\boxed{0.0063^\circ-0.708^\circ}
```

with median

```math
\boxed{0.029^\circ.}
```

Thus short-wave access solves the **raw visibility** problem but not the **model-separation** problem.

The illustrative anomaly phase RMS is

```text
0.0315-0.1206 degree
median ~0.0651 degree @1 GHz.
```

Smooth-mode calibration is therefore the limiting inverse resource.

---

## 16. Dense short-wave calibration requirement

For an 81-point `2.00-2.80 um` scan with independent equal

```math
\sigma_\phi=0.10^\circ
```

per wavelength, the illustrative anomaly gives:

```text
smooth nuisance known:
SNR 2.83-10.85, median 5.86, 91.7% >=3 sigma

0.005 degree phase-equivalent nuisance prior:
SNR 2.39-9.16, median 4.94, 79.2% >=3 sigma

0.010 degree prior:
SNR 1.75-6.71, median 3.62, 50% >=3 sigma

0.030 degree prior:
0% >=3 sigma.
```

The nuisance prior is a normalized **spectral phase-mode amplitude uncertainty**, not a local velocity uncertainty.

---

## 17. Exhaustive two-band design

Keep the same total coherent integration resource as the dense 81-point scan, but concentrate it into two wavelengths.

Because an arbitrary wavelength-independent differential phase remains, the gauge-free two-point observable is their phase difference.

For white variance `~1/t`, equal time at the two wavelengths is analytically optimal:

```math
\boxed{t_1=t_2=T_{\rm tot}/2.}
```

Exhaustive search over all `3240` wavelength pairs gives:

```text
smooth nuisance known:
2.00 / 2.80 um -> worst SNR 4.863

0.002 degree prior:
2.00 / 2.72 um -> worst SNR 4.237

0.005 degree prior:
2.00 / 2.69 um -> worst SNR 3.093
all 72 profiles >=3 sigma

0.010 degree prior:
~2.04 / 2.69 um -> worst SNR 1.956
only ~59.7% of profiles >=3 sigma.
```

At the `0.005 degree` prior, the dense uniform scan would need about `2.31x` the total integration time to match the two-band worst-case significance.

---

## 18. Global arbitrary-support optimization confirms the calibration floor

Allow arbitrary nonnegative time weights over **all 81 short-wave wavelengths** with the same total time.

For each profile,

```math
\mathbf F_p(\mathbf w)
=
\frac{T_{\rm tot}}{\sigma_{\phi,0}^2}
\sum_i w_i\mathbf x_{pi}\mathbf x_{pi}^T
+\mathbf P.
```

The normalized anomaly variance

```math
g_p(\mathbf w)
=
\frac{\mathbf e_0^T\mathbf F_p^{-1}\mathbf e_0}{A_p^2}
```

is convex in the wavelength weights, so minimizing `max_p g_p` over the simplex is a convex maximin design problem.

Numerical solution with analytic gradients gives:

### `0.002 degree` prior

```text
2.00 um -> 50%
2.72 um -> 50%
worst SNR = 4.237.
```

### `0.005 degree` prior

```text
2.00 um -> 50%
upper cluster 2.68-2.69 um -> 50%
weighted upper center ~2.688 um
worst SNR = 3.09273.
```

The simple `2.00/2.69 um` pair gives `3.09265`, only about `0.0028%` lower.

Thus the global fixed-time solution effectively collapses to two spectral clusters.

### `0.010 degree` prior

The global solution still forms two clusters near

```text
lower weighted center ~2.047 um
upper weighted center ~2.688 um
```

but reaches only

```math
\boxed{1.959\sigma}
```

worst case.

Therefore adding or redistributing wavelengths at the same total time does **not** rescue inadequate smooth-mode calibration.

The global robust `3 sigma` calibration threshold is approximately

```math
\boxed{\sigma_{\rm prior,max}\approx0.00528^\circ.}
```

This is essentially the same threshold obtained from the strict two-band search.

---

## 19. Current experimental architecture

The project should not force one spectral scan to do every job.

### Branch A — mid/deep calibration and temperature control

Use approximately `2.8-4.0 um` for

```text
sample-B smooth transport calibration
instrument covariance
RF validity
common-mode/swap validation
mid/deep optical-model checks
joint A/B temperature iso-kernel control.
```

### Branch B — short-wave A-localized contrast

After the smooth A/B spectral contribution is calibrated, use approximately

```text
~2.00 um
and
~2.69 um
```

with concentrated integration time to test whether an additional A-specific near-junction transport component is required.

The short-wave pair is **not** a replacement for the calibration scan. It is the efficient follow-up observable once calibration exists.

---

## 20. What is now the decisive bottleneck

The wavelength-design problem is no longer the leading theoretical uncertainty.

Within the current reduced model:

```text
raw short-wave signal -> sufficient
wavelength allocation -> essentially solved
adding more wavelengths -> cannot rescue loose priors
```

The dominant unresolved resource is:

> **Can the instrument + sample-B/sample-A smooth-baseline calibration constrain the relevant normalized smooth spectral phase modes to approximately `0.005 degree RMS` or better over the short-wave measurement interval?**

That is now a concrete, falsifiable metrology requirement rather than a qualitative statement that phase precision should be good.

---

## 21. Current experimental hierarchy

### Stage 1 — two-arm metrology calibration

Measure before interpreting HgCdTe transport:

```text
sigma_A(lambda,f)
sigma_B(lambda,f)
rho_c(lambda,f)
residual differential phase PSD
Allan deviation / drift versus time
swap repeatability
frequency dependence
amplitude-to-phase conversion
wavelength-repeatability phase error.
```

### Stage 2 — sample-B smooth transport calibration

Use the mid/deep branch and full complex RF response to obtain a posterior/covariance on the B modes that enter the paired observable.

### Stage 3 — constrain sample-A smooth baseline

Use spectral/temperature/bias information not dominated solely by the retained nonlinear region so the short-wave contrast cannot be absorbed into arbitrary smooth A modes.

### Stage 4 — short-wave paired A-B contrast

Use the globally optimized two-cluster design near `~2.00` and `~2.69 um` after the smooth-mode posterior reaches the required phase-equivalent scale.

### Stage 5 — mid/deep temperature difference-in-differences

Use the robust common-wavelength schedule as a separate causal transport perturbation/control.

### Stage 6 — independent validation

Compare with localized-position timing or a validated microscopic transport model.

---

## 22. What remains missing

- exact fitted/digitized sample A and B `x(z)` curves;
- full repeated-reflection optical stack if calibrated throughput requires it;
- full technical text of the 2024 close-collision paper;
- measured wavelength × RF phase/magnitude covariance;
- demonstrated `~0.005 degree RMS` smooth-mode calibration capability;
- calibrated sample-B smooth-mode posterior;
- calibrated sample-A smooth baseline;
- real complex-response data;
- independent microscopic/localized-position transport validation.

---

## 23. Next decisive work

Do **not** add another generic inverse theorem or another ad hoc wavelength set.

The highest-value theoretical/metrology step is now:

> **Translate the `~0.005 degree RMS` smooth-mode requirement into a concrete calibration experiment: required coherent SNR/integration time, allowable differential drift, wavelength-repeatability error, and sample-B posterior precision across RF frequency.**

In parallel, the decisive laboratory input remains measurement of the two-arm differential covariance and drift before detector inversion.

Only after real-data or independently validated inversion should manuscript readiness be reassessed.
