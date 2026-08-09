# Claim Ledger — Experiment 01

**Updated:** 2026-08-09  
**Status:** exploratory; active frontier is **few-mode differential wavelength × RF transport metrology** in graded HgCdTe; strongest validation path is a sample-B calibration followed by paired A/B transport contrast; no novelty claim

This file is the epistemic boundary. `RESEARCH_LOG.md` preserves chronology; specialized files preserve detailed derivations and failed branches.

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

## 1. Permanent invalidations / stopped shortcuts

### H1 — active-volume-only universal detector limit
**Status:** INVALIDATED

Ideal field concentration can retain finite optical participation while active material volume tends to zero.

### H2 — finite absorber count as one-photon speed limit
**Status:** INVALIDATED

The one-photon / one-excitation sector remains linear.

### H3 — largest internal coupling as universal multimode resource
**Status:** INVALIDATED

Spectator strongly coupled sectors are counterexamples.

### H4 — finite internal storage rank as universal detector capacity
**Status:** INVALIDATED

Adaptive branching / unrestricted output continua export distinguishability.

### H5 — local Landauer erasure as universal detector-event cost
**Status:** INVALIDATED

The useful output can itself carry the record information.

### H6 — spectral FWHM as architecture-independent carrier speed
**Status:** INVALIDATED

Multipole filters can retain spectral width while changing delay/state weight.

### H7 — low-field mobility extrapolated to high-field HgCdTe
**Status:** INVALIDATED SHORTCUT

High-field HgCdTe transport is non-ohmic.

### H8 — direct BTBT must be the first HgCdTe high-field limiter
**Status:** INVALIDATED SHORTCUT

TAT and nonlocal hot-electron / impact-ionization physics can intervene earlier.

### H9 — nonuniform field alone improves homogeneous local WKB leakage at fixed transit time
**Status:** INVALIDATED in stated homogeneous local model

Uniform field is optimal there; material/transport heterogeneity is required for a true allocation benefit.

### H10 — local `F_II(x)` always represents impact-ionization tolerance
**Status:** INVALIDATED GENERALIZATION

Thin/fast impact ionization is history dependent.

### H11 — every downstream photoelectron may be treated as cold
**Status:** INVALIDATED

Above-gap photoexcitation gives nonzero initial excess energy.

### H12 — entrance-gap timing maximum is transport independent
**Status:** INVALIDATED GENERALIZATION / SUPERSEDED

Directed ballistic memory can give a peak, strong momentum randomization can give a plateau, and other momentum distributions can produce other short-wave behavior.

### H13 — common mean delay can always be fitted independently of arbitrary internal `q_1`
**Status:** INVALIDATED GENERALIZATION

Boundary-localized internal delay is degenerate with wavelength-independent common delay because the collection-boundary timing kernel tends to unity at every wavelength.

### H14 — common timing broadening can always be fitted independently of arbitrary `q_2`
**Status:** INVALIDATED GENERALIZATION

The same boundary/common-mode ambiguity applies to the second timing cumulant.

### H15 — equal phase precision across wavelength is a realistic default at fixed incident power
**Status:** INVALIDATED AS DEFAULT

The published-sample optical model gives strongly wavelength-dependent absorbed signal, so fixed-power phase covariance is generally heteroscedastic.

### H16 — front/back illumination is an obviously valuable rank booster
**Status:** REJECTED FOR CURRENT SAMPLE-B ENVELOPE

Reversing illumination changes kernels but adds little to the strongly conditioned spatial modes while introducing sapphire/epoxy/passivation optical complexity.

### H17 — paired A/B source cancellation and independent device iso-kernel schedules can be combined automatically
**Status:** INVALIDATED GENERALIZATION

Common-source phase cancellation requires the same wavelength at both devices. Exact iso-kernel matching generally gives device-specific wavelengths unless a common **joint iso-kernel** solution exists.

---

## 2. Supporting earlier material/transport results

These remain provenance and may be reused, but they are not the active publication claim.

### P1 — passive harmonic transfer-area bound
**Status:** DERIVED / CHECKED; ingredients established prior theory

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

Nearly constant `N_A/N_v` gives `E_v approximately constant`, hence `S_c approximately G` for decreasing gap.

### B1 — barrier-free compensation condition
**Status:** DERIVED

```math
\boxed{qV_b\ge\alpha\Delta E_g^{(b)}.}
```

### B2 — peak-field lower bound
**Status:** DERIVED

```math
\boxed{F_{\max}\ge V_b/w.}
```

### N1 — nonlocal mean carrier-energy state
**Status:** DERIVED / CONDITIONAL

```math
\boxed{
\frac{d\varepsilon}{dx}
=S_c(x)-\frac{\varepsilon}{\ell_E(x)}.
}
```

### N2 — linear graded mean-II phase boundary
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

## 3. Spectral-generation supporting results

### S1 — earliest allowed generation position
**Status:** DERIVED / CONDITIONAL ON LOCAL-GAP ABSORPTION

For a monotonic linear gap,

```math
\boxed{
x_g(E_\gamma)
=\max\left[
0,
\frac{E_{g,\rm in}-E_\gamma}{G}
\right].
}
```

### S2 — exact conditional optical-depth generation law
**Status:** KNOWN probability consequence / DERIVED application

```math
\boxed{
p(y|{\rm abs})
=\frac{e^{-y}}{1-e^{-\tau_\gamma}}.}
```

### S3 — photoelectron excess-energy partition
**Status:** DERIVED / CONDITIONAL

```math
\boxed{
\varepsilon_{\rm gen}
=\xi_e[E_\gamma-E_g(x)].
}
```

### S4 — drift-diffusion first-passage moments
**Status:** DERIVED / CONDITIONAL; standard first-passage physics

```math
\boxed{\langle T|d\rangle=d/v_d,}
```

```math
\boxed{\operatorname{Var}(T|d)=2Dd/v_d^3.}
```

### S5 — entrance-gap initial-condition switch
**Status:** DERIVED / CONDITIONAL ON SHARP GENERATION; supporting only

Below the entrance gap photon energy primarily moves generation position; above it the entrance is already allowed and additional photon energy changes the injected carrier state.

No mandatory timing peak/cusp is claimed.

---

## 4. Active inverse-metrology operator

### I1 — downstream collection
**Status:** DERIVED

For collection at `L`,

```math
\boxed{
\bar T_i
=\int_0^L F_i(s)q_1(s)ds,
\qquad
F_i(s)=P(X_g\le s|\lambda_i,{\rm abs}).
}
```

### I2 — front collection
**Status:** DERIVED

For collection at `0`,

```math
\boxed{
\bar T_i
=\int_0^L S_i(s)q_1(s)ds,
\qquad
S_i(s)=P(X_g\ge s|\lambda_i,{\rm abs}).
}
```

The published 2023 sample A/B geometry uses this survival-kernel orientation.

### I3 — cell-integrated discrete operator
**Status:** DERIVED

```math
\boxed{
A_{ij}=\int_{\mathrm{cell}\ j}K_i(s)ds,
}
```

```math
\boxed{\mathbf T=\mathbf A\mathbf q_1.}
```

Only under a local path-additive interpretation:

```math
\boxed{q_1=1/v_{\rm eff}.}
```

### I4 — common-delay gauge
**Status:** DERIVED IDENTIFIABILITY LIMIT

Spectral data identify differential transport modes more robustly than absolute common/boundary delay.

### I5 — second timing moment
**Status:** DERIVED / CONDITIONAL ON ADDITIVE CONDITIONAL CUMULANTS

```math
\boxed{
\sigma_i^2
=\int K_i(s)q_2(s)ds
+\operatorname{Var}_{p_i}[m(X)].
}
```

After subtracting generation-position broadening:

```math
\boxed{\mathbf y_2=\mathbf A\mathbf q_2.}
```

Common second-cumulant broadening has the same gauge ambiguity.

### I6 — local two-profile interpretation
**Status:** CONDITIONAL

```math
\boxed{q_1=1/v,}
```

```math
\boxed{q_2\simeq2D/v^3.}
```

### I7 — complex-response cumulants
**Status:** KNOWN transform consequence / DERIVED application

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

At higher normalized RF frequency, fit the full complex transfer rather than forcing the low-order cumulant form.

---

## 5. Published sample-B dimensional results

### D1 — literature-constrained geometry
**Status:** DERIVED / CONDITIONAL ON PROFILE ENVELOPE

Published sample-B facts:

```text
processed W ~3.7 um
nominal FTIR x ~0.316
nonlinear interdiffusion region removed
junction at high-Cd end
remaining linear-gradient field ~100-200 V/cm.
```

The current envelope conditionally uses `x=0.316` as the low-Cd endpoint.

At 300 K:

```math
\boxed{E_{g,\rm low}=0.312314\ {\rm eV},}
```

```math
\boxed{\lambda_{g,\rm low}=3.9699\ {\rm um}.}
```

Field-bracket inferred high-Cd endpoints:

```text
100 V/cm -> x_high=0.34348 -> 3.5494 um
150 V/cm -> x_high=0.35721 -> 3.3708 um
200 V/cm -> x_high=0.37091 -> 3.2094 um.
```

### D2 — real above-gap optical kernels
**Status:** CHECKED NUMERICALLY / CONDITIONAL

Using the current Hansen gap and Moazzami above-gap absorption implementation, the central 150 V/cm profile gives approximately

```text
2.80 um -> Pabs=0.998, mean depth=0.677 um
3.88 um -> Pabs=0.070, mean depth=3.523 um.
```

Thus

```math
\boxed{\Delta\langle z\rangle\approx2.85\ {\rm um}.}
```

### D3 — illustrative total phase scale
**Status:** CONDITIONAL SCALE, NOT DEVICE PREDICTION

At illustrative `v_eff=1e5 m/s`:

```math
\boxed{\Delta T\approx28.5\ {\rm ps},}
```

```math
\boxed{|\Delta\phi|\approx10.25^\circ\quad\text{at }1\ {\rm GHz}.}
```

### D4 — optical spatial-mode count
**Status:** CHECKED NUMERICALLY / CONDITIONING DIAGNOSTIC

For 80 cells, `0.01 um` wavelength spacing, `Pabs>=0.05`, and cell-integrated front kernels:

```text
100 V/cm -> [2,5,10,20]
150 V/cm -> [2,5,10,21]
200 V/cm -> [2,5,11,23]
```

above relative singular thresholds `[1e-1,1e-2,1e-3,1e-4]`.

Interpretation: **few-mode band-limited tomography**, not pointwise depth imaging.

---

## 6. Experimental-noise / design results

### E1 — subtle-anomaly phase scale
**Status:** CHECKED NUMERICALLY / ILLUSTRATIVE

For synthetic

```text
baseline v=1e5 m/s
25% slowdown
center=2.30 um
sigma=0.35 um
f=1 GHz,
```

residual spectral anomaly phase is approximately

```math
\boxed{0.935^\circ\ \mathrm{peak\ to\ peak}.}
```

### E2 — equal-noise rank-3 recovery
**Status:** CHECKED NUMERICALLY / ILLUSTRATIVE

At `0.10 degree` independent per-wavelength phase noise:

```text
~17.5% median error relative to recoverable rank-3 target
~0.13 um 90%-quantile peak-location error.
```

Five-mode recovery is already noise dominated for this anomaly.

### E3 — heteroscedastic covariance
**Status:** CHECKED NUMERICALLY / CONDITIONAL SCALING MODELS

Current retained endpoint absorbed-signal ratio:

```math
\boxed{P_{\rm abs}(2.80)/P_{\rm abs}(3.89)\approx17.6.}
```

For `0.10 degree` short-wave phase noise:

```text
statistics-like sigma_phi proportional to Pabs^(-1/2)
-> long-wave sigma_phi ~0.42 degree
-> rank-3 noise error ~0.28

additive-like sigma_phi proportional to Pabs^(-1)
-> long-wave sigma_phi ~1.76 degree
-> rank-3 noise error ~0.45.
```

Hence **optical rank is not experimental rank**. Use a noise-whitened, common-mode-projected information matrix.

### E4 — equal-precision measurement-resource cost
**Status:** CONDITIONAL SCALING RESULT

At fixed incident power:

```text
statistics-like equal absorbed-count precision
-> ~17.6x more integration-time resource near 3.89 um

simple additive-noise coherent averaging
-> ~309x more integration time near 3.89 um.
```

Do not raise optical power aggressively without validating detector linearity/transport invariance.

### E5 — D-optimal wavelength/time design
**Status:** CHECKED NUMERICALLY / CONDITIONAL

For three smooth transport-mode amplitudes plus one common-phase nuisance:

Statistics-like optimal supports are approximately

```text
2.800, 3.410, 3.632, 3.840 um.
```

Additive-like supports are approximately

```text
2.800, 3.400, 3.596, 3.780 um.
```

Each receives about `25%` of normalized time in the saturated four-parameter design.

The two realistic fixed-power scalings improve generalized D-information scale by about `34%` relative to uniform time over the retained dense scan, corresponding in this reduced model to about `75%` of the uniform-scan time for the same generalized information volume.

This is not a universal four-wavelength prescription.

### E6 — RF-frequency validity
**Status:** CHECKED NUMERICALLY / CONDITIONAL OPTICAL-ONLY RESULT

For deterministic `T=z/v` and current sample-B optical kernels, an illustrative `|H|>0.98` envelope is

```math
\boxed{f_{\max}\approx0.13\,v/W.}
```

Examples:

```text
v=1e5 m/s -> ~3.5 GHz
v=3e4 m/s -> ~1.05 GHz
v=1e4 m/s -> ~0.35 GHz.
```

Additional stochastic/electrical broadening can tighten this.

---

## 7. Published A/B control/contrast interpretation

### A1 — sample B as smooth calibration/control
**Status:** PRIMARY-SOURCE INTERPRETATION / EXPERIMENTAL DESIGN CONSEQUENCE

The 2023 study reports that sample B's nonlinear region was removed and its remaining linear-gradient field is only about `100-200 V/cm`; the authors infer this field does not strongly alter carrier motion.

### A2 — sample A as nonlinear/high-field contrast
**Status:** PRIMARY-SOURCE INTERPRETATION / EXPERIMENTAL DESIGN CONSEQUENCE

Sample A retains part of the nonlinear interdiffusion region and reaches local composition-gradient field near `2e3 V/cm`. The authors attribute the A/B photoelectric difference primarily to composition-gradient effects on minority-carrier motion.

Therefore

```text
sample B -> calibration/control
sample A -> nonlinear/high-field transport contrast.
```

This is not yet a timing measurement.

---

## 8. Paired A/B differential-phase claims

### PAB1 — common source-phase cancellation
**Status:** DERIVED

If A and B are measured simultaneously from the same coherent modulated source at the same wavelength/frequency,

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

### PAB2 — reciprocal arm swap
**Status:** DERIVED / CONDITIONAL ON STABILITY/RECIPROCITY

A reciprocal A/B arm/channel swap can cancel stable arm asymmetry in the average of the two swapped differential measurements.

### PAB3 — paired observable is a contrast
**Status:** DERIVED

The paired measurement constrains

```text
A transport - B transport
```

more directly than either absolute profile.

---

## 9. Temperature iso-kernel claims

### T1 — fixed wavelength is optically confounded across temperature
**Status:** DERIVED MODEL CONSEQUENCE

Because `E_g(x,T)` and `alpha(E,x,T)` change with temperature,

```math
\mathbf A=\mathbf A(T,\lambda).
```

Holding wavelength fixed generally changes the spatial generation/timing kernel while transport changes.

### T2 — iso-kernel wavelength definition
**Status:** DERIVED EXPERIMENTAL DESIGN

```math
\boxed{
\lambda_*(T)
=\arg\min_\lambda
\frac{
\|\mathbf A(T,\lambda)-\mathbf A(T_0,\lambda_0)\|_2
}{
\|\mathbf A(T_0,\lambda_0)\|_2
}.
}
```

### T3 — sample-B mid/deep iso-kernel matches
**Status:** CHECKED NUMERICALLY / CONDITIONAL ON CURRENT SAMPLE-B ENVELOPE

Using 300 K reference bands:

```text
3.410 um
-> 215 K 3.52095 um, mismatch ~2.45%
-> 115 K 3.65954 um, mismatch ~5.08%

3.632 um
-> 215 K 3.79272 um, mismatch ~0.44%
-> 115 K 4.00268 um, mismatch ~0.84%

3.840 um
-> 215 K 4.04232 um, mismatch ~0.043%
-> 115 K 4.31011 um, mismatch ~0.112%.
```

### T4 — shallow mode failure at 115 K
**Status:** CHECKED NUMERICALLY / MODEL-RANGE LIMIT

The `2.800 um`, 300 K shallow reference mathematically matches near `1.15 um` at 115 K, outside the spectral range used to establish the current absorption fit.

Constraining to `lambda>=2 um` leaves approximately `17.5%` full-kernel mismatch.

Do not use the unconstrained `1.15 um` value as a validated optical prediction.

### T5 — full-kernel matching is the relevant criterion
**Status:** DERIVED

Matching only mean generation depth does not guarantee equal timing weighting; the cell-integrated cumulative/survival kernel is the correct object.

---

## 10. Paired A/B temperature compatibility limit

### PT1 — independent A/B iso-kernel schedules are incompatible with direct common-source cancellation unless wavelengths coincide
**Status:** DERIVED

Simultaneous source-phase cancellation requires the same source wavelength at both devices.

### PT2 — joint common-wavelength iso-kernel design
**Status:** DERIVED EXPERIMENTAL DESIGN

Define normalized kernel errors `epsilon_A,B`. A common comparison wavelength should solve

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

### PT3 — joint A/B iso-kernel feasibility
**Status:** OPEN

Cannot be evaluated until sample A's actual optical/composition profile is recovered.

### PT4 — residual kernel bias
**Status:** DERIVED

For device `d`,

```math
\boxed{
\delta T_{\rm opt,d}
=\delta\mathbf A_d\mathbf q_d,
}
```

and

```math
\boxed{
|\delta T_{\rm opt,d}|
\le
\|\delta\mathbf A_d\|_2
\|\mathbf q_d\|_2.
}
```

A small percentage kernel mismatch is therefore not automatically the same percentage timing error.

---

## 11. Established external ingredients — do not claim novelty

Primary literature already establishes

- graded HgCdTe devices and spectral response;
- composition-gradient effects on carrier motion;
- wavelength/depth-dependent generation in graded HgCdTe;
- forward response-time modeling;
- localized-position HgCdTe transit measurements;
- microscopic HgCdTe transport / Monte Carlo methods;
- wavelength-dependent photodiode bandwidth more broadly.

The 2024 close-collision paper remains incompletely inspected.

Negative search is not novelty evidence.

---

## 12. Current candidate statement

**Status:** CANDIDATE DISTINCT — PRIORITY UNPROVEN

The only candidate contribution still worth testing is:

> **Use a known graded-HgCdTe optical profile and wavelength-resolved complex response to reconstruct a finite set of differential internal timing modes, and validate those modes against controlled A/B material-structure and temperature perturbations without physically scanning generation position.**

The value must come from demonstrated inverse metrology and falsifiable validation, not from the forward generation physics or elementary algebra alone.

---

## 13. Current open questions

### O1 — actual sample A/B profiles

Need fitted/digitized `x_A(z)` and `x_B(z)` rather than the current sample-B field-bracket envelope.

### O2 — sample-A optics

Need interference/reflection-aware kernels if the reported sample-A interference is material.

### O3 — realistic instrument covariance

Need wavelength × RF-frequency phase/magnitude covariance for a tunable-MWIR measurement.

### O4 — joint A/B iso-kernel schedule

Need sample-A kernel matrix before feasibility can be assessed.

### O5 — independent transport validation

Need localized-position timing or a validated microscopic transport model on the same/equivalent structure.

### O6 — second-moment feasibility

Need actual magnitude-curvature precision before `q_2` becomes experimentally credible.

### O7 — 2024 close prior art

Need full technical inspection of `Potential application of HgCdTe detector with composition gradient in laser measurement`.

### O8 — publication significance

**OPEN. No manuscript yet.**

---

## 14. Explicit non-claims

The project does **not** presently claim

- a universal photodetector sensitivity-speed theorem;
- a universal active-volume bound;
- a universal entrance-gap timing maximum;
- pointwise high-resolution `v(z)` imaging;
- absolute common-delay recovery from spectral data alone;
- absolute common-broadening recovery from spectral data alone;
- calibrated sample-A/B carrier velocity or diffusion;
- actual internal defects in sample A or B;
- existence of a useful joint A/B iso-kernel schedule;
- novelty or priority for the inverse method;
- manuscript readiness.
