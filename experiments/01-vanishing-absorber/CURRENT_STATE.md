# Current State — Experiment 01: The Vanishing Absorber

**Date:** 2026-08-09  
**Status:** exploratory; active frontier is **few-mode, differential wavelength × RF-frequency transport metrology** in graded HgCdTe, with sample-B calibration, paired A/B differential phase, and a provisional common-wavelength temperature control; no novelty claim

## 1. Current question

The original universal detector-bound program and the later universal entrance-gap timing-peak interpretation are stopped branches.

The active question is now:

> **Can a known graded-HgCdTe optical profile be used as an internal spectral encoder so complex wavelength × RF measurements recover a small number of differential internal transport modes, and can that inverse be validated causally using the published smooth-gradient sample B versus nonlinear-gradient sample A?**

There is still **no manuscript**.

---

## 2. Read first

After root `AGENTS.md`:

1. `HGCDTE_SPECTRAL_TIMING_LINEAR_INVERSE.md`
2. `HGCDTE_PUBLISHED_SAMPLE_B_DIMENSIONAL_FORWARD_MATRIX.md`
3. `HGCDTE_PUBLISHED_SAMPLE_B_PHASE_PRECISION.md`
4. `HGCDTE_PUBLISHED_SAMPLE_B_HETEROSCEDASTIC_PHASE_NOISE.md`
5. `HGCDTE_PUBLISHED_SAMPLE_B_OPTIMAL_MEASUREMENT_DESIGN.md`
6. `HGCDTE_SAMPLE_B_RF_FREQUENCY_VALIDITY.md`
7. `HGCDTE_TEMPERATURE_ISO_KERNEL_DESIGN.md`
8. `HGCDTE_PAIRED_SAMPLE_AB_DIFFERENTIAL_PHASE.md`
9. `HGCDTE_PAIRED_AB_TEMPERATURE_DESIGN.md`
10. `HGCDTE_PHASE_PRECISION_SNR_REQUIREMENT.md`
11. `HGCDTE_PAIRED_PHASE_COMMON_MODE_REQUIREMENTS.md`
12. `HGCDTE_SAMPLE_A_CONSTRAINT_FAMILY_JOINT_ISO_KERNEL.md`
13. `HGCDTE_SPECTRAL_TIMING_TWO_MOMENT_INVERSE.md`
14. `HGCDTE_SPECTRAL_TIMING_TOMOGRAPHY_PRIOR_ART_AUDIT.md`
15. `CLAIM_LEDGER.md`
16. `RESEARCH_LOG.md`
17. `ARCHIVE_STATUS.md`

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

---

## 4. Orientation-correct linear inverse

Let

```math
p_i(x)=p(x|\lambda_i,{\rm abs})
```

and let `q_1(x)` be a path-additive mean-delay density.

### Collection at `L`

```math
\boxed{
\bar T_i
=\int_0^L F_i(s)q_1(s)ds,
\qquad F_i(s)=P(X_g\le s).
}
```

### Collection at `0`

```math
\boxed{
\bar T_i
=\int_0^L S_i(s)q_1(s)ds,
\qquad S_i(s)=P(X_g\ge s).
}
```

The 2023 sample A/B geometry is front collection: the junction is at the high-Cd end.

Use cell-integrated kernels

```math
\boxed{
A_{ij}=\int_{\text{cell }j}K_i(s)ds
}
```

so

```math
\boxed{
\mathbf T=\mathbf A\mathbf q_1.
}
```

Only under a local path-additive interpretation may one report

```math
q_1=1/v_{\rm eff}.
```

---

## 5. Common-delay / common-broadening gauge

A wavelength-independent delay is not generically separable from arbitrary transport concentrated near the collecting boundary, because the timing kernel tends to unity there for every wavelength.

The same issue applies to wavelength-independent second-cumulant broadening.

Therefore the robustly measurable objects are **differential transport modes**.

Use

```text
differential phase/timing
independent common-chain calibration
boundary transport priors
or a lower-dimensional physical parameterization.
```

Regularization choosing one decomposition is not proof of identifiability.

---

## 6. Two timing moments

For the orientation-correct kernel `K_i`, additive conditional timing cumulants give

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

Do not identify reconstructed `q_2` with microscopic diffusion without transport validation.

---

## 7. Frequency-domain observable

For timing distribution `T_i`,

```math
H_i(\Omega)=\langle e^{-i\Omega T_i}\rangle.
```

Low-frequency cumulants give

```math
\arg H_i=-\Omega\mu_i+O(\Omega^3),
```

```math
\ln|H_i|=-\frac{\Omega^2}{2}\sigma_i^2+O(\Omega^4).
```

Hence

```text
differential phase -> differential mean-delay modes
magnitude curvature -> differential timing-broadening modes.
```

At higher normalized frequency, fit the full complex transfer instead of forcing a mean-delay interpretation.

---

## 8. Published 2023 structures

The primary 2023 study gives a natural control/contrast pair.

### Sample B — calibration/control

```text
processed thickness ~3.7 um
nominal FTIR x ~0.316
nonlinear interdiffusion region removed
junction at high-Cd end
remaining linear-gradient field ~100-200 V/cm.
```

The authors infer that this remaining linear field does not strongly alter carrier motion.

### Sample A — nonlinear-gradient contrast

```text
processed thickness ~7.6 um
nominal FTIR x ~0.320
part of nonlinear interdiffusion region retained
junction at high-Cd end
local nonlinear-gradient field approaches ~2e3 V/cm.
```

The accessible primary text also gives the explicit composition-fit functional form, reports the nonlinear/interdiffusion region as approximately `4 um`, reports A's linear field as about `30 V/cm` larger than B at equal temperature, and shows interference near sample A's cutoff.

The authors attribute the samples' different photoelectric behavior primarily to the effect of composition-gradient field on minority-carrier motion.

This suggests

```text
sample B -> smooth calibration case
sample A -> nonlinear/high-field transport-contrast case.
```

The exact fitted A/B `x(z)` parameter tuples remain unavailable in machine-readable form; the curves/parameters are graphical.

---

## 9. Sample-B dimensional optical envelope

Current 300 K envelope:

```text
W=3.7 um
x_low=0.316
field bracket=100-200 V/cm
```

Using the correct Hansen relation:

```math
E_{g,\rm low}=0.312314\ {\rm eV},
\qquad
\lambda_{g,\rm low}=3.9699\ {\rm um}.
```

The field bracket implies approximately

```text
100 V/cm -> x_high=0.34348 -> 3.5494 um
150 V/cm -> x_high=0.35721 -> 3.3708 um
200 V/cm -> x_high=0.37091 -> 3.2094 um.
```

The current optical kernels use the Moazzami above-gap absorption model.

---

## 10. Real sample-B optical result

For the central `150 V/cm` envelope:

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
\boxed{\Delta\langle z\rangle\approx2.85\ {\rm um}}
```

from `2.80` to `3.88 um`.

At illustrative `v_eff=1e5 m/s`, this is about `28.5 ps` or `10.25 degrees` at `1 GHz`.

That is a measurement scale, not a sample-B velocity prediction.

---

## 11. Few-mode spatial rank

For 80 spatial cells, `0.01 um` wavelength steps, `Pabs>=0.05`, and cell-integrated front-collection kernels, relative singular-mode counts above `[1e-1,1e-2,1e-3,1e-4]` are

```text
100 V/cm -> [2,5,10,20]
150 V/cm -> [2,5,10,21]
200 V/cm -> [2,5,11,23].
```

The safe interpretation is:

> **few-mode band-limited tomography, not pointwise depth imaging.**

The experimentally sensible first target is about `3-4` smooth differential transport modes.

---

## 12. Phase-noise hierarchy

A synthetic

```text
25% slowdown
center 2.30 um
sigma 0.35 um
baseline v=1e5 m/s
```

produces only about

```math
0.935^\circ
```

peak-to-peak residual spectral phase at `1 GHz`.

With equal `0.10 degree` phase noise, a three-mode inversion gives roughly `17.5%` median error relative to the recoverable rank-3 target.

But equal noise is optimistic because absorbed signal collapses near cutoff.

At fixed incident power, the current `2.80 -> 3.89 um` absorbed-signal ratio is about

```math
17.6.
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

Thus **optical rank and experimental rank are different objects**.

The correct inverse uses the noise-whitened, common-mode-projected matrix.

---

## 13. Measurement-resource allocation

Equalizing phase precision near cutoff is expensive.

For the current endpoints:

```text
statistics/photon-like equal absorbed count
-> ~17.6x more incident-power × integration-time resource

simple additive-noise coherent averaging at fixed power
-> ~309x more integration time.
```

Prefer varying averaging time over large optical-power changes until detector linearity versus optical loading is independently verified.

---

## 14. D-optimal wavelength/time design

For the first experimental target

```text
3 smooth transport modes
+
1 common-phase nuisance,
```

a reduced four-parameter D-optimal design uses about four effective wavelength bands.

### Statistics-like fixed-power noise

```text
~2.800 um
~3.410 um
~3.632 um
~3.840 um.
```

### Additive-like fixed-power noise

```text
~2.800 um
~3.400 um
~3.596 um
~3.780 um.
```

Each gets about one quarter of total time in the saturated reduced design.

For the two realistic noise scalings, the optimized design improves the generalized D-information scale by about `34%` versus spreading the same time uniformly over all retained wavelengths, equivalent in this reduced model to roughly `75%` of the uniform-scan time for the same generalized information volume.

This is conditional experimental design, not a universal four-wavelength prescription.

---

## 15. RF-frequency validity

Using only optical generation-depth broadening and deterministic `T=z/v`, the current sample-B kernels give approximately

```math
\boxed{f_{\max}\sim0.13\,v/W}
```

for the illustrative criterion `|H|>0.98`.

Examples:

```text
v=1e5 m/s -> ~3.5 GHz
v=3e4 m/s -> ~1.05 GHz
v=1e4 m/s -> ~0.35 GHz.
```

This is an optical-only envelope; stochastic carrier and electrical broadening can tighten it.

RF frequency should therefore be adaptive, not fixed at `1 GHz` by assumption.

---

## 16. Paired A/B phase cancellation

If A and B are driven simultaneously by the same coherent modulated source at the same wavelength/frequency,

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

The entire arbitrary common source phase cancels.

A reciprocal device/arm swap can cancel stable arm/channel asymmetry under the stated reciprocity assumptions.

The paired observable measures **transport contrast**, not either absolute profile.

---

## 17. Temperature iso-kernel design — sample B

Holding wavelength fixed while changing temperature is not a clean transport test because `E_g(T)` and `alpha(T)` move the generation kernel.

Define an iso-kernel wavelength by

```math
\boxed{
\lambda_*(T)
=\arg\min_\lambda
\frac{\|\mathbf A(T,\lambda)-\mathbf A(T_0,\lambda_0)\|_2}
{\|\mathbf A(T_0,\lambda_0)\|_2}.
}
```

For the current sample-B envelope:

```text
300 K 3.410 um
-> 215 K 3.52095 um, mismatch ~2.45%
-> 115 K 3.65954 um, mismatch ~5.08%

300 K 3.632 um
-> 215 K 3.79272 um, mismatch ~0.44%
-> 115 K 4.00268 um, mismatch ~0.84%

300 K 3.840 um
-> 215 K 4.04232 um, mismatch ~0.043%
-> 115 K 4.31011 um, mismatch ~0.112%.
```

The shallow `2.800 um` reference can be matched at `215 K`, but at `115 K` its mathematical optimum moves to about `1.15 um`, outside the spectral region used to establish the current absorption fit. Constraining to `lambda>=2 um` leaves about `17.5%` kernel mismatch.

Therefore temperature comparisons should use **full-kernel-matched wavelengths**, and low-temperature experiments should drop/redefine the shallow mode unless a validated shorter-wave optical model is available.

---

## 18. Compatibility correction — paired A/B plus iso-kernel

The two strongest controls do **not** combine automatically.

Simultaneous A-B source-phase cancellation requires both devices to see the **same wavelength**.

Exact one-device iso-kernel matching generally gives device-specific wavelengths because A and B have different composition profiles.

The correct common-wavelength design is therefore

```math
\boxed{
\lambda_*(T)
=\arg\min_\lambda
\left[
w_A\epsilon_A^2(T,\lambda)
+w_B\epsilon_B^2(T,\lambda)
\right].
}
```

Independent A/B iso-kernel schedules therefore remain invalid as a direct common-source cancellation protocol.

---

## 19. Phase precision and common-mode requirements

For coherent photocurrent

```math
i(t)=I_1\cos(\Omega t+\phi)+n(t)
```

with one-sided white current-noise PSD `S_I` and coherent integration time `t`, the high-SNR phase variance is

```math
\boxed{
\sigma_\phi^2\simeq\frac{S_I}{I_1^2t}.
}
```

Defining

```math
\rho=\frac{I_1^2t}{S_I},
```

```math
\boxed{\sigma_\phi\simeq\rho^{-1/2}.}
```

Thus

```text
0.10 degree single-phase precision -> ~55.2 dB coherent power-SNR
0.10 degree A-B differential precision with equal independent channels -> ~58.2 dB/channel.
```

For correlated A/B phase errors,

```math
\boxed{
\sigma_{AB}^2
=\sigma_A^2+\sigma_B^2-2\rho_c\sigma_A\sigma_B.
}
```

For equal channels and a `0.10 degree` differential target:

```text
1 degree individual RMS -> rho_c >0.995
5 degree -> rho_c >0.9998
10 degree -> rho_c >0.99995.
```

A reciprocal swap leaves residual

```math
\boxed{
\delta\phi_{\rm swap}
=[\psi(t_1)-\psi(t_2)]/2.
}
```

so a `0.10 degree` systematic budget requires differential arm drift substantially below about `0.20 degree` over the swap interval.

The swap is a systematic-rejection technique, not a free white-noise SNR gain.

---

## 20. New result — sample-A constraint family supports a robust mid/deep common A/B temperature schedule

The exact sample-A fitted parameters are still graphical. Instead of inventing them, use the primary 2023 fit law and reported text constraints to build an explicit sensitivity family.

Current family:

```text
W_A = 7.6 um
conditional x_s = 0.320
A linear field = 130, 150, 180, 200 V/cm
Delta z = 3.5, 4.0, 4.5 um
processed front field = 1800, 2000, 2200 V/cm
both mathematical surface-field roots retained.
```

The `Delta z` and front-field spans are sensitivity ranges, **not** experimental uncertainty bars.

This gives `72` sample-A profiles. Across that deliberately broad family, the `3.632 um` 300 K common reference gives:

```text
215 K:
common lambda = 3.793356-3.793566 um
A kernel mismatch = 0.215-0.229%
B kernel mismatch = 0.447-0.453%
A Pabs = 0.290-0.410
B Pabs ~0.474

115 K:
common lambda = 4.004157-4.004870 um
A kernel mismatch = 0.400-0.445%
B kernel mismatch = 0.857-0.873%
A Pabs = 0.213-0.309
B Pabs = 0.357-0.358.
```

Therefore the earlier statement

```text
joint A/B iso-kernel feasibility is completely blocked until exact x_A(z) is recovered
```

is too strong.

The corrected status is:

> **Within the current Hansen/Moazzami Beer-Lambert sensitivity model, a useful mid/deep common-wavelength temperature control exists and its approximate wavelength is extremely insensitive to the unresolved sample-A profile.**

A provisional schedule is

```text
300 K -> 3.632 um
215 K -> ~3.7935 um
115 K -> ~4.0045 um.
```

The deeper `3.840 um` reference matches even more accurately, but at 115 K modeled sample-A absorption falls to only about `0.017-0.027`; the primary paper also reports A-side interference near cutoff. It is therefore rejected as the preferred first paired-temperature band.

Exact sample-A digitization is still required for calibrated A inversion, shallow-mode design, joint transport-mode identifiability, and final uncertainty propagation.

---

## 21. Rejected/low-value branch — reverse illumination

Opposite-side illumination through the sapphire-supported side was considered because it changes the optical kernels without changing the device transport.

The current sample-B envelope gives only modest improvement in strongly conditioned spatial modes while adding sapphire/epoxy/passivation dispersion and alignment complexity.

**Status:** rejected for now. Front illumination plus optimized wavelengths and paired A/B phase is the cleaner path.

---

## 22. Current strongest experimental hierarchy

### Stage 1 — sample B / instrument calibration

Before interpreting HgCdTe transport, measure and validate

```text
optical kernels
sigma_A(lambda,f)
sigma_B(lambda,f)
rho_c(lambda,f)
residual differential phase PSD
Allan deviation / drift versus time
swap repeatability
frequency regime
few-mode inverse stability.
```

### Stage 2 — interference-aware sample-A optics

The new constraint-family result weakens the exact-profile feasibility blocker, but the primary sample-A data explicitly show interference near cutoff.

Add a reflection/interference-aware optical model and test whether the provisional

```text
3.632 -> 3.7935 -> 4.0045 um
```

common schedule survives.

### Stage 3 — recover the actual A/B profile fits

Digitize/recover the graphical fit parameters when a usable primary figure becomes available and replace the sensitivity envelopes with the real profiles.

### Stage 4 — paired transport contrast

Use simultaneous A/B differential phase, reciprocal arm swaps, adaptive RF frequency, and the validated common-wavelength temperature perturbation to test for extra internal transport structure associated with sample A's retained nonlinear-gradient region.

---

## 23. What remains missing

- exact fitted/digitized sample A and B `x(z)` curves;
- interference/reflection-aware sample-A generation kernels;
- full technical text of the 2024 close-collision paper;
- realistic wavelength × RF-frequency phase/magnitude covariance;
- calibrated transport model / independent localized-position validation;
- real complex-response data.

---

## 24. Next decisive work

Do **not** add another generic inverse theorem.

The highest-value next theoretical/numerical collision is:

> **Build an interference-aware optical model for sample A and test whether the provisional `3.632 -> 3.7935 -> 4.0045 um` common A/B temperature schedule survives.**

In parallel, the decisive pre-detector metrology experiment remains measurement of the two-arm differential phase covariance and drift.

Exact sample-A profile recovery remains important, but it is no longer the sole feasibility gate for the mid/deep common-wavelength temperature control.

Only after real-data or independently validated inversion should manuscript readiness be reassessed.
