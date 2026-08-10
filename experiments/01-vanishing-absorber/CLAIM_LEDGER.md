# Claim Ledger — Experiment 01

**Updated:** 2026-08-09  
**Status:** exploratory; active frontier is **few-mode differential wavelength × RF transport metrology** in graded HgCdTe, with a mid/deep calibration-temperature branch and a short-wave sample-A nonlinear-region contrast branch; no novelty claim

This file is the epistemic boundary. `CURRENT_STATE.md` is the operational front door; `RESEARCH_LOG.md` preserves chronology; specialized files preserve detailed derivations and numerical regressions.

## Status vocabulary

- **KNOWN** — established external result used as input.
- **DERIVED** — exact consequence of stated repository assumptions.
- **CHECKED** — independently or numerically verified.
- **CONDITIONAL** — valid only inside stated assumptions/model.
- **CANDIDATE DISTINCT — PRIORITY UNPROVEN** — potentially unusual formulation; literature boundary incomplete.
- **INVALIDATED** — counterexample/correction found.
- **SUPERSEDED** — replaced by a stronger/corrected statement.
- **OPEN** — unresolved.
- **NON-CLAIM** — explicitly not asserted.

---

# 1. Permanent invalidations / stopped shortcuts

### H1 — active-volume-only universal detector limit
**Status:** INVALIDATED

Ideal field concentration can retain finite optical participation while active material volume tends to zero.

### H2 — finite absorber count as one-photon speed limit
**Status:** INVALIDATED

The one-photon / one-excitation sector remains linear.

### H3 — largest internal coupling as universal multimode resource
**Status:** INVALIDATED

Spectator strongly coupled sectors provide counterexamples.

### H4 — finite internal storage rank as universal detector capacity
**Status:** INVALIDATED

Adaptive branching and unrestricted output continua can export distinguishability.

### H5 — local Landauer erasure as universal detector-event cost
**Status:** INVALIDATED

The useful output can itself carry the event record.

### H6 — spectral FWHM as architecture-independent carrier speed
**Status:** INVALIDATED

Multipole filtering can retain spectral width while changing delay/state weight.

### H7 — low-field mobility extrapolated to high-field HgCdTe
**Status:** INVALIDATED SHORTCUT

High-field HgCdTe transport is non-ohmic.

### H8 — direct BTBT must be the first HgCdTe high-field limiter
**Status:** INVALIDATED SHORTCUT

Trap-assisted tunneling and nonlocal hot-carrier / impact-ionization physics can intervene earlier.

### H9 — nonuniform field alone improves homogeneous local WKB leakage at fixed transit
**Status:** INVALIDATED IN THE STATED MODEL

Uniform field is optimal in that homogeneous local formulation; useful allocation requires additional material/transport structure.

### H10 — local impact-ionization field tolerance is generally sufficient
**Status:** INVALIDATED GENERALIZATION

Thin/fast impact ionization is history dependent.

### H11 — every downstream photoelectron may be treated as cold
**Status:** INVALIDATED

Above-gap excitation gives nonzero initial excess energy.

### H12 — entrance-gap timing maximum is transport independent
**Status:** INVALIDATED / SUPERSEDED

Directed ballistic memory can give a peak, strong momentum randomization can give a plateau, and other momentum distributions can give other behavior.

### H13 — common mean delay can always be fitted independently of arbitrary internal `q_1`
**Status:** INVALIDATED GENERALIZATION

Boundary-localized internal delay is degenerate with wavelength-independent common delay.

### H14 — common timing broadening can always be fitted independently of arbitrary `q_2`
**Status:** INVALIDATED GENERALIZATION

The same boundary/common-mode ambiguity applies to the second timing cumulant.

### H15 — equal phase precision across wavelength is a realistic fixed-power default
**Status:** INVALIDATED AS DEFAULT

Absorbed signal varies strongly across the sample-B mid/deep scan.

### H16 — front/back illumination is an obviously useful rank booster
**Status:** REJECTED FOR CURRENT SAMPLE-B ENVELOPE

The rank benefit is modest while sapphire/epoxy/passivation optical complexity increases.

### H17 — paired source cancellation and independent device iso-kernel schedules combine automatically
**Status:** INVALIDATED GENERALIZATION

Direct common-source cancellation requires the same wavelength at A and B; exact one-device iso-kernel wavelengths are generally device specific.

---

# 2. Supporting provenance results

These remain valid inside their stated assumptions but are not the active publication claim.

### P1 — passive harmonic transfer-area bound
**Status:** DERIVED / CHECKED

```math
\boxed{
\mathcal I_{L\to R}
\le
\frac{2LR}{L+R},
\qquad
L=\operatorname{Tr}\Gamma_L,
\quad
R=\operatorname{Tr}\Gamma_R.
}
```

### G1 — linear graded-Kane WKB action
**Status:** DERIVED / CHECKED / CONDITIONAL

```math
\boxed{
\mathcal S(E)
=\frac{\pi\sqrt{S_cS_v}}
{4\hbar v_K}(x_c-x_v)^2.
}
```

### G2 — band-edge geometry identity
**Status:** DERIVED

```math
\boxed{S_v=S_c-G,}
\qquad
G=-dE_g/dx.
```

### Q1 — quasi-neutral p-type majority-band pinning
**Status:** DERIVED / CONDITIONAL

```math
\boxed{
\frac{dE_v}{dx}
\simeq
k_BT\frac{d}{dx}\ln(N_A/N_v).
}
```

### N1 — nonlocal mean carrier-energy state
**Status:** DERIVED / CONDITIONAL

```math
\boxed{
\frac{d\varepsilon}{dx}
=S_c(x)-\frac{\varepsilon}{\ell_E(x)}.
}
```

### N2 — linear graded mean-impact-ionization phase boundary
**Status:** DERIVED / CHECKED / CONDITIONAL

```math
\boxed{
\zeta_{\rm II}(r,\chi)
=
\frac{\chi}
{\chi+(1-e^{-r})/r}.
}
```

---

# 3. Active inverse operator

### I1 — downstream collection uses a CDF kernel
**Status:** DERIVED

```math
\boxed{
\bar T_i
=\int_0^L F_i(s)q_1(s)ds,
\qquad
F_i(s)=P(X_g\le s).
}
```

### I2 — front collection uses a survival kernel
**Status:** DERIVED

```math
\boxed{
\bar T_i
=\int_0^L S_i(s)q_1(s)ds,
\qquad
S_i(s)=P(X_g\ge s).
}
```

The published 2023 A/B geometry uses front collection.

### I3 — cell-integrated discrete operator
**Status:** DERIVED

```math
\boxed{
A_{ij}=\int_{\mathrm{cell}\ j}K_i(s)ds,
\qquad
\mathbf T=\mathbf A\mathbf q_1.
}
```

Only under a local path-additive interpretation:

```math
q_1=1/v_{\rm eff}.
```

### I4 — common-delay boundary gauge
**Status:** DERIVED IDENTIFIABILITY LIMIT

For front collection,

```math
S_i(0)=1.
```

Near-junction transport is therefore nearly wavelength independent and cannot generically be separated from arbitrary common delay without additional information.

### I5 — second timing moment
**Status:** DERIVED / CONDITIONAL ON ADDITIVE CONDITIONAL CUMULANTS

```math
\boxed{
\sigma_i^2
=\int K_i(s)q_2(s)ds
+\operatorname{Var}_{p_i}[m(X)].
}
```

The same common/boundary ambiguity applies to `q_2`.

### I6 — local drift-diffusion interpretation
**Status:** CONDITIONAL

```math
\boxed{q_1=1/v,}
```

```math
\boxed{q_2\simeq2D/v^3.}
```

### I7 — complex-response cumulants
**Status:** KNOWN TRANSFORM CONSEQUENCE / DERIVED APPLICATION

```math
\boxed{
\arg H_i(\Omega)
=-\Omega\mu_i+O(\Omega^3),
}
```

```math
\boxed{
\ln|H_i(\Omega)|
=-\frac{\Omega^2}{2}\sigma_i^2+O(\Omega^4).
}
```

At higher normalized RF frequency, fit the full complex transfer.

---

# 4. Sample-B calibration claims

### B1 — literature-constrained sample-B geometry
**Status:** CONDITIONAL ON CURRENT PROFILE ENVELOPE

```text
processed W ~3.7 um
nominal x ~0.316
nonlinear interdiffusion region removed
junction at high-Cd end
linear-gradient field ~100-200 V/cm.
```

### B2 — real above-gap sample-B optical leverage
**Status:** CHECKED NUMERICALLY / CONDITIONAL

Central `150 V/cm` envelope:

```text
2.80 um -> Pabs ~0.998, mean depth ~0.677 um
3.88 um -> Pabs ~0.070, mean depth ~3.523 um.
```

Hence

```math
\boxed{\Delta\langle z\rangle\approx2.85\ {\rm um}.}
```

### B3 — illustrative phase scale
**Status:** CONDITIONAL SCALE, NOT DEVICE PREDICTION

At illustrative `v_eff=1e5 m/s`:

```text
Delta T ~28.5 ps
Delta phi ~10.25 deg at 1 GHz.
```

### B4 — sample-B few-mode rank
**Status:** CHECKED NUMERICALLY / CONDITIONING DIAGNOSTIC

For 80 cells and current retained wavelength scan:

```text
100 V/cm -> [2,5,10,20]
150 V/cm -> [2,5,10,21]
200 V/cm -> [2,5,11,23]
```

above relative singular thresholds `[1e-1,1e-2,1e-3,1e-4]`.

Interpretation: **few-mode band-limited tomography**.

### B5 — heteroscedastic mid/deep phase noise matters
**Status:** CHECKED NUMERICALLY / CONDITIONAL SCALING MODELS

```math
P_{\rm abs}(2.80)/P_{\rm abs}(3.89)\approx17.6.
```

At fixed incident power, optical rank is not experimental rank.

### B6 — reduced D-optimal sample-B design
**Status:** CHECKED NUMERICALLY / CONDITIONAL

For three smooth B modes plus one common-phase nuisance:

```text
statistics-like support ~2.800, 3.410, 3.632, 3.840 um
additive-like support ~2.800, 3.400, 3.596, 3.780 um.
```

### B7 — optical-only RF validity
**Status:** CHECKED NUMERICALLY / CONDITIONAL

For deterministic `T=z/v` and `|H|>0.98`:

```math
\boxed{f_{\max}\approx0.13\,v/W.}
```

Additional carrier/electrical broadening can tighten this.

---

# 5. Paired A/B metrology claims

### PAB1 — common source-phase cancellation
**Status:** DERIVED

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

Simultaneous same-source same-wavelength subtraction removes arbitrary common source phase.

### PAB2 — reciprocal arm swap
**Status:** DERIVED / CONDITIONAL ON STABILITY AND RECIPROCITY

A reciprocal swap cancels stable arm asymmetry in the swapped average.

### PAB3 — paired observable is transport contrast
**Status:** DERIVED

Paired data directly constrain A-minus-B transport contrast, not either absolute profile.

### PAB4 — smooth A/B modes overlap strongly
**Status:** CHECKED NUMERICALLY / CONDITIONAL ON CURRENT OPTICAL ENVELOPES

For the first three smooth response subspaces across the 72 A-profile family:

```text
principal angle 1 = 0.210-0.875 deg
principal angle 2 = 3.524-15.695 deg
principal angle 3 = 33.546-65.356 deg.
```

For a symmetric `3+3` fit the weakest normalized singular ratio is

```text
0.001831-0.007633.
```

Therefore independent arbitrary multi-mode A and B reconstruction from paired data is not a credible first interpretation.

### PAB5 — sample-B calibration is an identifiability requirement
**Status:** DERIVED DESIGN CONSEQUENCE / CHECKED BY RESPONSE GEOMETRY

The paired experiment should first constrain B and the smooth A baseline, then infer additional A-specific contrast.

---

# 6. Phase-resource claims

### M1 — white-noise phase variance
**Status:** DERIVED / HIGH-SNR APPROXIMATION

For coherent photocurrent amplitude `I1`, one-sided white current-noise PSD `S_I`, and integration time `t`:

```math
\boxed{
\sigma_\phi^2\simeq\frac{S_I}{I_1^2t}.
}
```

Defining

```math
\rho=I_1^2t/S_I,
```

```math
\boxed{\sigma_\phi\simeq\rho^{-1/2}.}
```

### M2 — representative coherent SNR scales
**Status:** DERIVED

```text
0.10 deg single-phase precision -> ~55.2 dB coherent power-SNR
0.10 deg differential precision with equal independent A/B channels -> ~58.2 dB/channel.
```

### M3 — correlated A/B phase requirement
**Status:** DERIVED

```math
\boxed{
\sigma_{AB}^2
=\sigma_A^2+\sigma_B^2-2\rho_c\sigma_A\sigma_B.
}
```

For equal channels and a `0.10 degree` differential target:

```text
1 deg individual RMS -> rho_c >0.995
5 deg -> >0.9998
10 deg -> >0.99995.
```

### M4 — reciprocal-swap drift
**Status:** DERIVED

```math
\boxed{
\delta\phi_{\rm swap}
=[\psi(t_1)-\psi(t_2)]/2.
}
```

A `0.10 degree` swap-only systematic budget therefore requires differential arm drift below about `0.20 degree` over the swap interval.

---

# 7. Temperature-control claims

### T1 — fixed wavelength is optically confounded across temperature
**Status:** DERIVED MODEL CONSEQUENCE

Because

```math
\mathbf A=\mathbf A(T,\lambda),
```

fixed wavelength does not hold the optical timing kernel fixed as temperature changes.

### T2 — iso-kernel wavelength definition
**Status:** DERIVED EXPERIMENTAL DESIGN

```math
\boxed{
\lambda_*(T)
=\arg\min_\lambda
\frac{\|\mathbf A(T,\lambda)-\mathbf A(T_0,\lambda_0)\|_2}
{\|\mathbf A(T_0,\lambda_0)\|_2}.
}
```

### T3 — sample-B mid/deep iso-kernel matches
**Status:** CHECKED NUMERICALLY / CONDITIONAL

For the current central envelope:

```text
300 K 3.632 um
-> 215 K 3.79272 um, mismatch ~0.44%
-> 115 K 4.00268 um, mismatch ~0.84%.
```

### T4 — joint A/B common-wavelength schedule
**Status:** CHECKED NUMERICALLY / CONDITIONAL SENSITIVITY RESULT

Across the 72 A-profile family, the common `3.632 um` 300 K reference gives approximately

```text
215 K -> 3.793356-3.793566 um
115 K -> 4.004157-4.004870 um
```

with sub-percent to ~1% B mismatch and sub-percent A mismatch in Beer-Lambert optics.

### T5 — empirical thermo-optic interference preserves the mid/deep schedule
**Status:** CHECKED NUMERICALLY / CONDITIONAL ONE-RETURN MODEL

With composition-resolved empirical HgCdTe refractive index and a broad coherent returned-wave stress:

```text
215 K -> 3.792986-3.794120 um
115 K -> 4.002940-4.007453 um
```

with worst A kernel mismatch below about `0.74%` and `1.73%`, respectively.

### T6 — schedule approximately follows a fixed local-gap composition
**Status:** DERIVED / CHECKED NUMERICALLY

```text
300 K, 3.6320 um -> x_edge 0.337580
215 K, 3.7935 um -> 0.337746
115 K, 4.0045 um -> 0.337837.
```

---

# 8. Sample-A short-wave contrast claims

### SW1 — retained nonlinear region is near the collection boundary
**Status:** CHECKED NUMERICALLY / CONDITIONAL SUPPORT MODEL

Using the published gradient-field excess only as a spatial support template:

```text
support centroid ~0.46-1.43 um
median ~0.88 um
90% cumulative support depth ~1.03-2.65 um.
```

No transport law proportional to field is assumed.

### SW2 — mid/deep scan is nearly blind to that support
**Status:** CHECKED NUMERICALLY / CONDITIONAL

For `2.8-3.83 um`, support-weighted normalized differential visibility is

```text
0.0025-0.0430
median ~0.0089.
```

For the illustrative 25% support-shaped perturbation:

```text
0.0023-0.0469 deg peak-to-peak at 1 GHz
median ~0.0173 deg.
```

### SW3 — `2.0-2.8 um` restores raw A-specific leverage
**Status:** CHECKED NUMERICALLY / CONDITIONAL

For the same illustrative perturbation:

```text
2.0-2.8 um -> 0.1081-0.3706 deg p-p
median ~0.2110 deg.
```

Median leverage is about `12x` the mid/deep value.

### SW4 — short-wave anomaly remains nearly inside the smooth A/B nuisance subspace
**Status:** CHECKED NUMERICALLY / CONDITIONAL

Principal angle to the six-mode smooth nuisance subspace:

```math
\boxed{0.0063^\circ-0.708^\circ}
```

with median `0.029 degree`.

Thus raw visibility does not by itself establish identifiability.

### SW5 — dense short-wave detection depends strongly on smooth-mode prior precision
**Status:** CHECKED NUMERICALLY / CONDITIONAL FISHER MODEL

At `0.10 degree` independent per-wavelength phase noise:

```text
0.005 deg phase-equivalent smooth-mode prior
-> worst SNR ~2.39
-> 79.2% of profiles >=3 sigma

0.010 deg prior
-> worst SNR ~1.75
-> 50% >=3 sigma

0.030 deg prior
-> 0% >=3 sigma.
```

### SW6 — equal time is exactly optimal for a two-wavelength difference
**Status:** DERIVED UNDER WHITE `1/t` VARIANCE

For fixed `t1+t2=T`:

```math
\operatorname{Var}(\phi_1-\phi_2)
=\sigma_0^2\left(\frac1{t_1}+\frac1{t_2}\right)
```

is minimized by

```math
\boxed{t_1=t_2=T/2.}
```

### SW7 — exhaustive robust two-band design
**Status:** CHECKED NUMERICALLY / CONDITIONAL

With total time equal to the dense 81-point reference scan:

```text
0.002 deg smooth prior:
2.00 / 2.72 um -> worst SNR 4.237

0.005 deg prior:
2.00 / 2.69 um -> worst SNR 3.093
all 72 profiles >=3 sigma

0.010 deg prior:
~2.04 / 2.69 um -> worst SNR 1.956.
```

At the `0.005 degree` prior, the dense uniform scan requires about `2.31x` the total integration time to match the optimized pair's worst-case significance.

### SW8 — global arbitrary-support fixed-time design effectively collapses to two spectral clusters
**Status:** CHECKED NUMERICALLY / CONDITIONAL CONVEX MAXIMIN DESIGN

The full 81-weight Fisher allocation problem is convex.

At `0.005 degree` prior:

```text
50% time at 2.00 um
50% time in a narrow 2.68-2.69 um cluster
weighted upper center ~2.688 um
worst SNR ~3.09273.
```

The simple `2.00/2.69 um` pair is only about `0.0028%` worse.

### SW9 — adding wavelengths cannot rescue a `0.010 degree` smooth-mode prior at fixed total time
**Status:** CHECKED NUMERICALLY / CONDITIONAL GLOBAL DESIGN

The globally optimized arbitrary-support allocation reaches only

```math
\boxed{1.959\sigma}
```

worst case.

Thus inadequate smooth-mode calibration, not wavelength sampling density, is the limiting resource in that regime.

### SW10 — global robust calibration threshold
**Status:** CHECKED NUMERICALLY / CONDITIONAL

For the current illustrative anomaly, total time, noise scale, profile family, and six-mode nuisance model:

```math
\boxed{
\sigma_{\rm prior,max}\approx0.00528^\circ
}
```

is the largest phase-equivalent smooth-mode prior width for which the globally optimized short-wave design guarantees `>=3 sigma` across all 72 profiles.

Do not interpret `0.00528 degree` as a universal detector or instrument constant.

---

# 9. Current candidate contribution

**Status:** CANDIDATE DISTINCT — PRIORITY UNPROVEN

The only candidate contribution worth pursuing is:

> **Use a known graded-HgCdTe optical profile and wavelength-resolved complex response to reconstruct a finite set of differential internal timing modes, then validate those modes through calibrated A/B material-structure and temperature perturbations without physically scanning the generation position.**

The current strongest experimental realization is not one universal wavelength scan:

```text
mid/deep branch
-> calibrate smooth transport / instrument / temperature controls

short-wave branch
-> concentrate spectral leverage on sample A's retained nonlinear region

paired A-B observable
-> calibrated transport contrast

~0.005 deg phase-equivalent smooth-mode knowledge
-> current robust feasibility threshold for the illustrative short-wave test.
```

The value must come from demonstrated metrology and falsifiable validation, not from forward generation physics alone.

---

# 10. Established external ingredients — do not claim novelty

Prior literature already establishes

- wavelength-dependent generation depth and bandwidth;
- graded-bandgap carrier acceleration;
- graded-HgCdTe spectral response;
- wavelength/depth-dependent generation in graded HgCdTe;
- graded-HgCdTe forward transport/response-time modeling;
- localized-position HgCdTe transit measurements;
- microscopic HgCdTe transport / Monte Carlo methods.

The 2024 close-collision paper remains incompletely inspected.

Negative search is not novelty evidence.

---

# 11. Current open questions

### O1 — actual A/B composition profiles

Need fitted/digitized `x_A(z)` and `x_B(z)` for calibrated inversion and final uncertainty propagation.

### O2 — measured differential covariance

Need wavelength × RF phase/magnitude covariance, residual differential phase PSD, Allan deviation, swap repeatability, and wavelength-repeatability error.

### O3 — `~0.005 degree` smooth-mode calibration feasibility

Need to determine whether the instrument plus sample-B/sample-A baseline calibration can actually constrain the relevant normalized smooth spectral phase modes to the required class.

### O4 — full sample-A optical stack

Need repeated-reflection/reflection/interface modeling if calibrated throughput or kernel shape requires more than the current one-return stress model.

### O5 — independent transport validation

Need localized-position timing or a validated microscopic transport model on the same/equivalent structure.

### O6 — 2024 close prior art

Need full technical inspection of `Potential application of HgCdTe detector with composition gradient in laser measurement`.

### O7 — real complex-response data

No experimental A/B wavelength × RF data have yet been inverted.

### O8 — publication significance

**OPEN. No manuscript yet.**

---

# 12. Explicit non-claims

The project does **not** presently claim

- a universal photodetector sensitivity-speed theorem;
- a universal active-volume bound;
- a universal entrance-gap timing maximum;
- pointwise high-resolution `v(z)` imaging;
- absolute common-delay recovery from spectral data alone;
- absolute common-broadening recovery from spectral data alone;
- calibrated sample-A/B carrier velocity or diffusion;
- actual internal defects in sample A or B;
- that the illustrative 25% sample-A transport perturbation is real;
- that `0.00528 degree` is a universal calibration requirement;
- that the exact real-device optimum wavelengths are `2.00/2.69 um`;
- that the current one-return interference model is a calibrated optical stack;
- novelty or priority for the inverse method;
- manuscript readiness.
