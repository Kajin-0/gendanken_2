# Claim Ledger — Experiment 01

**Updated:** 2026-08-09  
**Status:** exploratory; active frontier is **few-mode wavelength × frequency inverse metrology** of internal transport in compositionally graded HgCdTe; no novelty claim

This file defines the epistemic boundary. `RESEARCH_LOG.md` preserves chronology; specialized files preserve detailed derivations.

## Status vocabulary

- **KNOWN** — established external result used as input.
- **DERIVED** — exact consequence of stated repository assumptions.
- **CHECKED** — independently or numerically verified.
- **CONDITIONAL** — exact only inside stated simplified assumptions.
- **CANDIDATE DISTINCT** — potentially unusual formulation; priority unproven.
- **INVALIDATED** — counterexample/correction found.
- **SUPERSEDED** — replaced by stronger/corrected statement.
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

The useful output can carry the record information.

### H6 — spectral FWHM as architecture-independent carrier speed
**Status:** INVALIDATED

Multipole filters can retain spectral width while changing delay/state weight.

### H7 — low-field mobility extrapolated to high-field HgCdTe
**Status:** INVALIDATED SHORTCUT

High-field HgCdTe transport is non-ohmic.

### H8 — direct BTBT must be first HgCdTe high-field limiter
**Status:** INVALIDATED SHORTCUT

TAT and nonlocal hot-electron / impact-ionization physics can intervene earlier.

### H9 — nonuniform field alone improves homogeneous local WKB leakage at fixed transit time
**Status:** INVALIDATED in the stated homogeneous model

Uniform field is optimal there; heterogeneity is required for a real allocation benefit.

### H10 — local `F_II(x)` can always represent impact-ionization tolerance
**Status:** INVALIDATED GENERALIZATION

Thin/fast II is history dependent.

### H11 — every downstream photoelectron may be treated as cold
**Status:** INVALIDATED

Above-gap photoexcitation gives nonzero initial excess energy.

### H12 — entrance-gap timing maximum is transport independent
**Status:** INVALIDATED GENERALIZATION / SUPERSEDED

Ballistic directed-memory models can give a maximum; drift-diffusion can give a plateau; other momentum distributions can give different short-wave behavior.

### H13 — common timing delay can always be fitted independently of arbitrary internal delay density
**Status:** INVALIDATED GENERALIZATION

A wavelength-independent contribution is degenerate with sufficiently boundary-localized internal delay because the timing kernel tends to unity at the collecting boundary.

### H14 — common timing broadening can always be fitted independently of arbitrary `q_2`
**Status:** INVALIDATED GENERALIZATION

The same boundary/common-mode ambiguity applies to the second timing cumulant.

---

## 2. Supporting results from earlier branches

### P1 — finite passive-network harmonic transfer-area bound
**Status:** DERIVED / CHECKED; ingredients established prior theory; novelty not claimed

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

### P2 — fixed-target Hopfield access collapse
**Status:** CANDIDATE DISTINCT supporting lemma; priority unproven

```math
\boxed{
\min(\Gamma_L,\Gamma_R)\to0
\quad(g\to\infty)
}
```

inside the stated two-mode fixed-resource model.

### P3 — active finite-mode conversion resource
**Status:** DERIVED bookkeeping result built on established singular-mode conversion theory

```math
\boxed{
N_p
\ge
\frac{M_c\arcsin^2\sqrt\eta}
{\Lambda\tau^2}.
}
```

These remain provenance, not the active material frontier.

---

## 3. HgCdTe graded-band supporting results

### G1 — exact linear graded-Kane WKB action
**Status:** DERIVED / CHECKED / CONDITIONAL

```math
\boxed{
\mathcal S(E)
=\frac{\pi\sqrt{S_cS_v}}
{4\hbar v_K}(x_c-x_v)^2.
}
```

### G2 — band-offset-partition invariant geometry
**Status:** DERIVED

```math
\boxed{S_v=S_c-G,}
\qquad
G=-dE_g/dx.
```

### G3 — fixed-conduction-slope Zener ratio
**Status:** DERIVED / CHECKED / CONDITIONAL; priority unassessed

```math
\boxed{
\frac{\mathcal S_Z(\delta)}{\mathcal S_Z(0)}
=\frac{(2-\delta)^2}{4(1-\delta)^{3/2}},
\qquad 0\le\delta<1.
}
```

### Q1 — majority-band pinning in quasi-neutral p material
**Status:** DERIVED / CONDITIONAL

```math
\boxed{
\frac{dE_v}{dx}
\simeq
k_BT\frac{d}{dx}\ln(N_A/N_v).
}
```

Nearly constant `N_A/N_v` gives `E_v approximately constant` and hence `S_c approximately G` for decreasing gap.

### B1 — barrier-free compensation voltage
**Status:** DERIVED

```math
\boxed{qV_b\ge\alpha\Delta E_g^{(b)}.}
```

### B2 — peak-field lower bound
**Status:** DERIVED

```math
\boxed{F_{\max}\ge V_b/w.}
```

### B3 — local tunneling voltage capacity
**Status:** DERIVED / CONDITIONAL

```math
\boxed{
F_{\rm allow}(x)
=\min_m\frac{F_m(x)}{\Sigma_m},
}
```

with feasibility

```math
\boxed{
V_b\le\int F_{\rm allow}(x)dx.
}
```

### N1 — path-dependent mean carrier-energy state
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

These results remain supporting architecture/transport provenance.

---

## 4. Spectral generation / transport results

### S1 — wavelength-dependent generation geometry
**Status:** DERIVED / CONDITIONAL ON LOCAL-GAP ABSORPTION

For a monotonic linear gap,

```math
\boxed{
x_g(E_\gamma)
=\max\!\left[
0,
\frac{E_{g,\rm in}-E_\gamma}{G}
\right].
}
```

### S2 — exact conditional optical-depth generation distribution
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

### S4 — exact drift-diffusion first-passage statistics
**Status:** DERIVED / CONDITIONAL; standard physics, no novelty claim

```math
\boxed{\langle T|d\rangle=d/v_d,}
```

```math
\boxed{\operatorname{Var}(T|d)=2Dd/v_d^3.}
```

### S5 — entrance-gap initial-condition switch
**Status:** DERIVED / CONDITIONAL ON SHARP GENERATION; supporting, not current headline

Photon energy changes generation position below the entrance gap and primarily changes injected carrier state after the entrance becomes optically allowed.

### S6 — post-crossover timing shape
**Status:** CHECKED across simplified transport limits

Peak / plateau / continued variation are model dependent; no universal timing maximum survives.

---

## 5. Active inverse-metrology claims

### I1 — downstream-collection mean-delay operator
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

### I2 — front-collection mean-delay operator
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

The published 2023 sample-B geometry uses this survival-kernel orientation.

### I3 — discrete linear inverse
**Status:** DERIVED

With cell-integrated orientation-correct kernels,

```math
\boxed{
\mathbf T=\mathbf A\mathbf q_1.
}
```

Under a local path-additive interpretation,

```math
\boxed{q_1=1/v_{\rm eff}.}
```

This local velocity identification is CONDITIONAL.

### I4 — common-delay gauge
**Status:** DERIVED IDENTIFIABILITY LIMIT

Wavelength data alone do not generically separate an arbitrary wavelength-independent delay from sufficiently boundary-localized internal delay density.

Robust strategies are differential timing, independent common-delay calibration, a boundary prior, or a lower-dimensional physical model.

### I5 — second timing-moment operator
**Status:** DERIVED / CONDITIONAL ON ADDITIVE CONDITIONAL CUMULANTS

```math
\boxed{
\sigma_i^2
=\int K_i(s)q_2(s)ds
+\operatorname{Var}_{p_i}[m(X)].
}
```

After subtracting the known generation-position contribution,

```math
\boxed{
\mathbf y_2=\mathbf A\mathbf q_2.
}
```

The common second-cumulant component has the same gauge ambiguity.

### I6 — local drift-diffusion interpretation of two profiles
**Status:** CONDITIONAL

```math
\boxed{q_1=1/v,}
```

```math
\boxed{q_2\simeq2D/v^3.}
```

Do not identify reconstructed `q_2` with microscopic diffusion before validating local transport.

### I7 — low-frequency complex-response cumulants
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

Hence differential RF phase probes differential mean delay and magnitude curvature probes timing variance.

---

## 6. Published sample-B dimensional results

### D1 — sample-B dimensional envelope
**Status:** DERIVED / CONDITIONAL ON ENDPOINT INTERPRETATION

Published inputs:

```text
W ~ 3.7 um
nominal x ~ 0.316
nonlinear region removed
linear-gradient field ~100-200 V/cm.
```

Taking `x=0.316` as a nominal low-Cd endpoint at 300 K, Hansen gives

```math
\boxed{E_{g,\rm low}=0.312314\ {\rm eV},}
```

```math
\boxed{\lambda_{g,\rm low}=3.9699\ {\rm um}.}
```

The field bracket implies

```text
100 V/cm -> x_high=0.34348 -> lambda_high=3.5494 um
150 V/cm -> x_high=0.35721 -> lambda_high=3.3708 um
200 V/cm -> x_high=0.37091 -> lambda_high=3.2094 um.
```

### D2 — published above-gap optical kernels
**Status:** CHECKED NUMERICALLY / CONDITIONAL

Using Moazzami et al. 2005

```math
\alpha(E,x,T)
=K(x,T)[(E-E_g)/E]^{n(x,T)}
```

with no Urbach/reflection/interference corrections, the central 150 V/cm profile shifts conditional mean generation depth from approximately

```text
0.677 um at 2.80 um
```

to

```text
3.523 um at 3.88 um,
```

while single-pass absorbed fraction changes from approximately `0.998` to `0.070`.

### D3 — illustrative total differential phase scale
**Status:** CONDITIONAL SCALE, NOT DEVICE PREDICTION

At illustrative `v_eff=1e5 m/s`, the `2.846 um` mean-depth shift corresponds to

```math
\boxed{\Delta T\approx28.5\ {\rm ps}}
```

and

```math
\boxed{|\Delta\phi|\approx10.25^\circ\quad\text{at }1\ {\rm GHz}.}
```

### D4 — real-matrix mode count
**Status:** CHECKED NUMERICALLY / CONDITIONING DIAGNOSTIC

For 80 spatial cells, `0.01 um` wavelength spacing, and `P_abs>=0.05`:

```text
100 V/cm -> modes above [1e-1,1e-2,1e-3,1e-4] = [2,5,10,20]
150 V/cm -> [2,5,10,21]
200 V/cm -> [2,5,11,23].
```

The robust conclusion is a **few-mode band-limited tomography**, not pointwise depth imaging.

### D5 — phase-noise anomaly test
**Status:** CHECKED NUMERICALLY / ILLUSTRATIVE

For the central optical matrix and a synthetic

```text
25% slowdown
center 2.30 um
sigma 0.35 um
baseline v=1e5 m/s,
```

the residual anomaly phase is approximately

```math
\boxed{0.935^\circ\text{ peak-to-peak at }1\ {\rm GHz}.}
```

A three-mode truncated inversion at `0.10 degree` independent phase noise gives approximately

```text
17.5% median error relative to the recoverable rank-3 target
0.13 um 90%-quantile peak-location error.
```

At `0.25 degree`, localization degrades strongly.

Five-mode inversion is already noise dominated near `0.10 degree` for this anomaly.

This is not an instrument-performance or sample-defect claim.

---

## 7. Established external ingredients — do not claim novelty

Primary literature already establishes

- graded HgCdTe devices and spectral response;
- composition-gradient transport effects;
- wavelength/depth-dependent generation in graded HgCdTe;
- forward response-time modeling;
- localized-position HgCdTe transit measurements;
- HgCdTe microscopic transport / Monte Carlo methods;
- wavelength-dependent photodiode bandwidth more broadly.

A close 2024 `Potential application ... in laser measurement` paper remains incompletely inspected.

Negative search is not novelty evidence.

---

## 8. Current candidate statement

**Status:** CANDIDATE DISTINCT — PRIORITY UNPROVEN

The only candidate contribution still worth testing is:

> **Use a known monotonic graded-HgCdTe optical profile and wavelength-resolved complex response to reconstruct a finite set of differential internal mean-delay and timing-broadening modes, without physically scanning the generation position.**

The value must come from demonstrated inverse metrology, not from the forward physics or the algebra alone.

---

## 9. Open questions

### O1 — actual sample-B profile

Need the fitted/digitized `x(z)` data rather than the current field-bracket envelope.

### O2 — realistic optical corrections

Need to assess Urbach tail, reflection/interference, free-carrier absorption, and wavelength-dependent optical coupling where material.

### O3 — instrument covariance

Need realistic wavelength/frequency phase and magnitude covariance for a tunable MWIR complex-response experiment.

### O4 — independent transport validation

Need localized-position timing or validated microscopic transport for the same/equivalent structure.

### O5 — second-moment feasibility

Need real magnitude-curvature precision before `q_2` becomes experimentally credible.

### O6 — close 2024 prior art

Need full technical inspection of the 2024 laser-measurement paper.

### O7 — publication significance

**OPEN.** No manuscript yet.

---

## 10. Explicit non-claims

The project does **not** presently claim

- a universal photodetector sensitivity-speed theorem;
- a universal active-volume bound;
- a universal entrance-gap timing maximum;
- pointwise high-resolution transport imaging;
- absolute common-delay recovery from spectral data alone;
- absolute common-broadening recovery from spectral data alone;
- calibrated sample-B carrier velocity or diffusion;
- a measured `q_1(z)` or `q_2(z)` profile;
- novelty or priority for spectral timing tomography;
- manuscript readiness.
