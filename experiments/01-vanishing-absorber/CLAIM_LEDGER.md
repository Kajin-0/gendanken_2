# Claim Ledger — Experiment 01

**Updated:** 2026-08-10  
**Status:** exploratory; strongest active path is **matched translated-gradient wavelength × RF transport validation in graded HgCdTe**; no novelty claim

This file is the epistemic boundary. `CURRENT_STATE.md` is the operational front door; `RESEARCH_LOG.md` preserves chronology; specialized files preserve derivations and numerical regressions.

## Status vocabulary

- **KNOWN** — established external result used as input.
- **DERIVED** — exact consequence of stated assumptions.
- **CHECKED** — independently or numerically verified.
- **CONDITIONAL** — valid only inside stated model/parameter envelope.
- **CANDIDATE DISTINCT — PRIORITY UNPROVEN** — potentially unusual combination; literature boundary incomplete.
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

Directed ballistic memory can give a peak; strong momentum randomization can give a plateau; other momentum distributions give other behavior.

### H13 — common mean delay can always be fitted independently of arbitrary internal `q_1`
**Status:** INVALIDATED GENERALIZATION

Boundary-localized internal delay is degenerate with wavelength-independent common delay.

### H14 — common timing broadening can always be fitted independently of arbitrary `q_2`
**Status:** INVALIDATED GENERALIZATION

The same boundary/common ambiguity applies to the second timing cumulant.

### H15 — equal phase precision across wavelength is a realistic fixed-power default
**Status:** INVALIDATED AS DEFAULT

Absorbed signal varies strongly with wavelength.

### H16 — front/back illumination is an obviously useful rank booster
**Status:** REJECTED FOR CURRENT SAMPLE-B ENVELOPE

Rank gain is modest relative to the extra optical/systematic complexity.

### H17 — paired source cancellation and independent device iso-kernel schedules combine automatically
**Status:** INVALIDATED GENERALIZATION

Direct common-source cancellation requires the same wavelength at both devices.

### H18 — denser/sparser wavelength selection alone can remove the published-A smooth-mode calibration floor
**Status:** INVALIDATED IN CURRENT MODEL

Global fixed-time optimization of the `2.0-2.8 um` short-wave scan collapses toward two wavelength bands, but a several-millidegree smooth-mode prior remains necessary.

### H19 — mid/deep A data can self-calibrate the short-wave A baseline cheaply
**Status:** INVALIDATED IN CURRENT MODEL

The leading short-wave A mode is weakly visible in the mid/deep scan; broad no-prior self-calibration remains severely ill-conditioned.

### H20 — finite RF diversity alone cures the published-A mechanism degeneracy
**Status:** INVALIDATED IN CURRENT MODEL

`0.25-3 GHz` complex data rotate the spatial sensitivity operator but leave the near-junction target very close to smooth/contact nuisance space.

### H21 — a published sample-A timing difference can be uniquely attributed to the nonlinear composition-gradient region
**Status:** INVALIDATED GENERALIZATION

Generic near-junction/contact transport plus smooth bulk changes can closely mimic that fingerprint.

### H22 — short-wave temperature difference-in-differences is an optically clean near-junction causal control
**Status:** INVALIDATED IN CURRENT OPTICAL MODEL

Short-wave full kernels do not remain sufficiently invariant under temperature retuning; static baseline leakage re-enters the difference.

### H23 — optical-load timing/curvature is a candidate novelty
**Status:** INVALIDATED AS NOVELTY ROUTE

HgCdTe transient response versus steady optical load is prior art. Load differencing can be a control technique but not the central claim.

### H24 — `2.6 -> 3.2 um` is the purpose-built global feature-depth optimum
**Status:** SUPERSEDED

That result came from an inherited feature-position grid ending at `3.2 um`. Once depth, both interfaces, spectral band, absorbed-signal noise, and fixed total time are treated jointly, the preferred feature pair moves deeper.

### H25 — the largest principal angle is automatically the best experiment
**Status:** INVALIDATED DESIGN SHORTCUT

A geometry with a larger angle can have smaller absolute nuisance-orthogonal signal. The design objective must include signal norm and covariance.

### H26 — an ultrasharp `<50 nm` programmed gradient edge is required
**Status:** INVALIDATED BY SPATIAL CONVERGENCE

At 320 transport cells, `25-100 nm` edge ramps form an approximately `1%` information plateau; a `~0.1 um` transition is already near the resolved optimum.

---

# 2. Core inverse claims

### I1 — downstream collection uses a CDF kernel
**Status:** DERIVED

```math
\boxed{
\bar T_i=\int_0^L F_i(s)q_1(s)ds,
\qquad F_i(s)=P(X_g\le s).
}
```

### I2 — front collection uses a survival kernel
**Status:** DERIVED

```math
\boxed{
\bar T_i=\int_0^L S_i(s)q_1(s)ds,
\qquad S_i(s)=P(X_g\ge s).
}
```

Published A/B and the current purpose-built front-collection geometry use the survival form.

### I3 — cell-integrated discrete operator
**Status:** DERIVED

```math
\boxed{
A_{ij}=\int_{\mathrm{cell}\ j}K_i(s)ds,
\qquad
\mathbf T=\mathbf A\mathbf q_1.
}
```

Only under a local path-additive interpretation may one write `q_1=1/v_eff`.

### I4 — front-boundary common-delay gauge
**Status:** DERIVED IDENTIFIABILITY LIMIT

```math
\boxed{S_i(0)=1}
```

for every wavelength. Sufficiently near-junction transport is therefore almost wavelength independent and generically confounded with common delay.

### I5 — complex-response low-frequency cumulants
**Status:** KNOWN TRANSFORM CONSEQUENCE / DERIVED APPLICATION

```math
\arg H_i=-\Omega\mu_i+O(\Omega^3),
```

```math
\ln|H_i|=-\frac{\Omega^2}{2}\sigma_i^2+O(\Omega^4).
```

At higher normalized RF frequency the full complex transfer must be fitted.

---

# 3. Published-sample benchmark claims

### B1 — sample B provides real few-mode spectral leverage
**Status:** CHECKED NUMERICALLY / CONDITIONAL

For the central `3.7 um`, `150 V/cm` profile envelope, mean generation depth shifts by about `2.85 um` between the useful short and long ends of the mid/deep scan.

Relative singular-mode counts above `[1e-1,1e-2,1e-3,1e-4]` are approximately

```text
[2,5,10,21].
```

Interpretation: **few-mode band-limited tomography**, not pointwise imaging.

### B2 — sample-B mid/deep phase covariance is heteroscedastic
**Status:** CHECKED NUMERICALLY / CONDITIONAL

Absorbed signal changes by about `17.6x` across the retained scan, so the noise-whitened inverse is the experimentally relevant object.

### B3 — sample-B mid/deep D-optimal supports
**Status:** CHECKED NUMERICALLY / CONDITIONAL

For three smooth modes plus common phase, representative supports are

```text
statistics-like: 2.800, 3.410, 3.632, 3.840 um
additive-like:   2.800, 3.400, 3.596, 3.780 um.
```

### B4 — mid/deep temperature iso-kernel control is robust
**Status:** CHECKED NUMERICALLY / CONDITIONAL

A useful joint reference remains approximately

```text
300 K -> 3.632 um
215 K -> ~3.793 um
115 K -> ~4.005 um,
```

with small modeled A/B kernel mismatch across the current sample-A sensitivity family and thermo-optic stress.

### B5 — published A/B smooth response modes overlap strongly
**Status:** CHECKED NUMERICALLY / CONDITIONAL

A symmetric arbitrary multi-mode A/B inversion is badly conditioned; paired data are better interpreted as calibrated contrast.

### B6 — published A near-junction short-wave visibility is real but insufficient for attribution
**Status:** CHECKED NUMERICALLY / CONDITIONAL

`2.0-2.8 um` gives much larger raw phase leverage on the retained nonlinear region than the mid/deep scan, but that spectral fingerprint remains nearly contained in smooth/contact nuisance space.

---

# 4. Metrology-resource claims

### M1 — white-noise phase variance
**Status:** DERIVED / HIGH-SNR APPROXIMATION

```math
\boxed{
\sigma_\phi^2\simeq\frac{S_I}{I_1^2t}.
}
```

Representative scale:

```text
0.10 deg single phase -> ~55.2 dB coherent power-SNR
0.10 deg A-B difference with equal independent channels -> ~58.2 dB/channel.
```

### M2 — same-source paired phase cancellation
**Status:** DERIVED

At the same wavelength/frequency, arbitrary common source phase cancels from the A-B difference.

### M3 — reciprocal arm swap cancels stable arm asymmetry only under reciprocity/stability
**Status:** DERIVED / CONDITIONAL

It is not a free white-noise gain.

### M4 — wavelength-independent electrical transfer cancels from the relocation fingerprint
**Status:** DERIVED

If

```math
M_j(\lambda,f)=E_j(f)H_j(\lambda,f),
```

then fitting/removing one arbitrary complex wavelength-independent intercept at each RF frequency eliminates `E_2(f)/E_1(f)` exactly.

Wavelength-dependent or signal-state-dependent electrical effects remain dangerous.

---

# 5. Matched-relocation claims

### R1 — relocation probes the derivative of spatial sensitivity
**Status:** DERIVED

For

```math
y(\lambda,f;z_0)=\int K_{\lambda,f}(z)q_f(z-z_0)dz,
```

a small translation gives

```math
\boxed{
\Delta y\simeq\Delta z\int K'_{\lambda,f}(z)q_f(z-z_0)dz.
}
```

For a flat compact feature `[a,b]`,

```math
\boxed{
\partial y/\partial z_0=A[K(b)-K(a)].
}
```

Relocation therefore creates a signed **edge fingerprint**.

### R2 — matched `C/G1/G2` geometry is a stronger causal control than published A/B
**Status:** DERIVED DESIGN LOGIC / CHECKED NUMERICALLY

```text
C  -> smooth endpoint/contact-matched control
G1 -> buried compact high-gradient feature at z1
G2 -> same feature translated to z2.
```

`G2-G1` tests whether the fingerprint translates with the internal feature instead of staying attached to an interface.

### R3 — endpoint-preserving programmed profiles are mathematically constructible
**Status:** DERIVED

A mean-preserving modulation of composition slope can translate a compact high-gradient region while keeping total composition change and both endpoint compositions fixed.

### R4 — programmed feature reproduces the relevant field scale
**Status:** CHECKED NUMERICALLY / CONDITIONAL

A `~0.9-1.0 um` feature with `~0.1 um` transitions can maintain a background gradient of order a few `10^2 V/cm` and local maximum near `1.95-2.0 kV/cm` in the conceptual `7.6 um`, `x_front~0.55`, `x_back~0.32` absorber.

The field is a design coordinate, not a transport prediction.

### R5 — both interfaces must be treated as confounders
**Status:** DERIVED DESIGN REQUIREMENT / CHECKED NUMERICALLY

If only the front interface is penalized, the optimizer exploits the back boundary. Front and back interface nuisance modes plus explicit feature clearance are therefore required.

### R6 — conservative interface-safe depth/spectral design
**Status:** CHECKED NUMERICALLY / CONDITIONAL

With the full feature kept roughly `1.5 um` from both interfaces, fixed total wavelength time, front/back interface nuisances, and either provisional absorbed-signal phase-noise scaling, the stable reference is approximately

```text
feature centers ~4.1 and ~5.5-5.6 um
spectral band ~2.00-2.40 um
RF set 0.25, 0.5, 1, 2, 3 GHz.
```

Exact tenth-micron coordinates are not universal.

### R7 — fixed-time interior design improves on the inherited shallow pair
**Status:** CHECKED NUMERICALLY / CONDITIONAL

Under the same front/back nuisance and covariance rules, the interface-safe interior design gives roughly

```text
~1.9x nuisance-orthogonal information amplitude
~3.6x Fisher information
```

relative to the earlier restricted `2.6 -> 3.2 um` pair.

### R8 — edge-ramp information plateau
**Status:** CHECKED NUMERICALLY WITH SPATIAL CONVERGENCE

At `320` transport cells, `25-100 nm` programmed edge transitions differ by only about `1%` in the current information metric.

A `200 nm` transition costs roughly `30%` relative to `100 nm`.

### R9 — useful total feature width is broad
**Status:** CHECKED NUMERICALLY / CONDITIONAL

At fixed peak gradient near `1.95 kV/cm`, the useful unblurred region is roughly

```text
0.9-1.1 um
```

with `~1.0 um` best on the present grid.

### R10 — moderate interdiffusion degrades gradually
**Status:** CHECKED NUMERICALLY / CONDITIONAL GAUSSIAN BLUR MODEL

After reoptimization and conservative `3 sigma_d` boundary clearance, information-amplitude losses are approximately

```text
sigma_d=0.05 um -> ~8%
sigma_d=0.10 um -> ~20%
sigma_d=0.15 um -> ~33%.
```

The statistics-like and additive-like noise envelopes choose essentially the same geometries.

### R11 — matching is an identifiability condition
**Status:** DERIVED / CHECKED NUMERICALLY

Writing

```math
q_2=c+\delta/2,
\qquad q_1=c-\delta/2,
```

gives

```math
\boxed{
J_2q_2-J_1q_1
=(J_2-J_1)c+\frac{J_2+J_1}{2}\delta.
}
```

Common nuisance variation can be fitted; differential mismatch can mimic the target. Allowing fully independent contact/bulk nuisance amplitudes collapses the separation.

### R12 — earlier shallow programmed mismatch tolerances are provenance, not final specs
**Status:** SUPERSEDED AS FINAL SPECIFICATION

The few-millidegree and tenth-micron tolerance calculations around the `2.6/3.2 um` prototype remain useful demonstrations of method but must be recomputed for the final interface-safe process-specific profile.

---

# 6. Materials feasibility claims

### F1 — HgCdTe composition programming exists in MBE
**Status:** KNOWN

Published MBE work demonstrates deliberately composition-tailored HgCdTe heterostructures and in-situ composition/thickness metrology on scales far smaller than the current micron-scale relocation coordinates.

This does not prove fabrication of the exact proposed profile.

### F2 — HgCdTe graded heterostructures exist in MOCVD
**Status:** KNOWN

Published MOCVD work demonstrates designed graded sublayers with realized `x(z)` characterized by SIMS; interdiffusion must be included in the forward model.

### F3 — LPE longitudinal gradient sign/magnitude is programmable
**Status:** KNOWN

Huo et al. 2024 experimentally controlled positive HgCdTe composition gradients using mercury-loss and cooling conditions and verified the longitudinal profile by thinning spectroscopy and SIMS.

### F4 — exact matched translated internal feature has been demonstrated
**Status:** OPEN / NON-CLAIM

No recovered source yet establishes the exact `same boundaries + compact buried feature translated in depth` device pair proposed here.

---

# 7. Prior-art boundary

### PA1 — graded-HgCdTe high-speed/RF response
**Status:** KNOWN PRIOR ART

Sang et al. 2022 report room-temperature graded-HgCdTe impulse/frequency response and explicit composition-gradient carrier-transport modeling, including `1550 nm` RF excitation over `50 MHz-1 GHz` and `2 um` switching tests.

### PA2 — localized HgCdTe transit timing
**Status:** KNOWN PRIOR ART

Perrais et al. and related HgCdTe timing work block broad claims for localized transit measurement.

### PA3 — 2024 laser-measurement close collision
**Status:** OPEN

Xu et al., *Journal of Applied Optics* 45 (2024) 549-556, DOI `10.5768/JAO202445.0310009`, is verified by metadata, but its full technical content has not been recovered.

It remains a priority blocker.

### PA4 — surviving candidate distinction
**Status:** CANDIDATE DISTINCT — PRIORITY UNPROVEN

The potentially underexplored combination is

```text
known graded x(z) as a wavelength position encoder
+
complex wavelength x RF inverse
+
few-mode/differential interpretation
+
matched buried-feature relocation
+
causal test that the fingerprint moves with the feature.
```

Negative literature search is not novelty evidence.

---

# 8. Important nonclaims

Do **not** claim

- pointwise high-resolution internal velocity imaging;
- absolute common timing from wavelength data alone;
- transport proportional to composition-gradient field;
- that the illustrative `25%` transport perturbation is a real-device prediction;
- universal optimal wavelengths or feature depths;
- that the programmed trapezoid is a fabrication recipe;
- that MBE, MOCVD, or LPE has already demonstrated the exact matched relocation pair;
- novelty/priority;
- manuscript readiness.

---

# 9. Current decisive blockers

1. recover full technical content of DOI `10.5768/JAO202445.0310009`;
2. choose a growth route and replace generic blur with a process-specific reachable `x(z)` family;
3. recompute final mismatch tolerances on that reachable family;
4. obtain real wavelength × RF phase/magnitude covariance, drift, and wavelength-dependent electrical-state data;
5. validate transport beyond the deterministic illustrative baseline;
6. characterize realized `x(z)` independently;
7. obtain matched-device data.

Until then:

> **candidate underexplored inverse-metrology / matched-relocation validation method; priority unproven; no manuscript.**
