# Claim Ledger — Experiment 01

**Updated:** 2026-08-09  
**Status:** exploratory; active frontier is wavelength × frequency inverse metrology of internal transport in compositionally graded HgCdTe; no novelty claim

This file defines the epistemic boundary. `RESEARCH_LOG.md` preserves chronology; specialized files preserve detailed derivations.

## Status vocabulary

- **KNOWN** — established external result used as input.
- **DERIVED** — exact consequence of stated repository assumptions.
- **CHECKED** — independently or numerically verified.
- **CONDITIONAL** — exact only inside a deliberately simplified model.
- **CANDIDATE DISTINCT** — potentially unusual formulation; priority unproven.
- **INVALIDATED** — explicit counterexample or correction found.
- **SUPERSEDED** — replaced by a stronger/corrected statement.
- **OPEN** — unresolved.
- **NON-CLAIM** — explicitly not asserted.

---

## 1. Permanent invalidations / stopped shortcuts

### H1 — active-volume-only universal detector limit
**Status:** INVALIDATED

Ideal field concentration permits finite optical participation while active material volume tends to zero.

### H2 — finite absorber count as one-photon speed limit
**Status:** INVALIDATED

The one-photon / one-excitation sector remains linear.

### H3 — finite internal storage rank as universal always-on detector capacity
**Status:** INVALIDATED

Adaptive branching and output continua export the missing distinguishability.

### H4 — spectral FWHM as architecture-independent carrier speed
**Status:** INVALIDATED

Multipole structures can keep spectral width fixed while changing delay/state weight.

### H5 — low-field mobility extrapolated into high-field HgCdTe
**Status:** INVALIDATED SHORTCUT

Primary high-field HgCdTe transport is non-ohmic and velocity need not increase monotonically with field.

### H6 — direct BTBT must be the first HgCdTe high-field limiter
**Status:** INVALIDATED SHORTCUT

TAT and nonlocal hot-electron / impact-ionization physics can intervene earlier.

### H7 — nonuniform field alone improves homogeneous local WKB leakage at fixed transit time
**Status:** INVALIDATED IN THE STATED HOMOGENEOUS LOCAL MODEL

Uniform field is optimal under the derived assumptions; a genuine benefit requires material/defect/transport heterogeneity.

### H8 — local `F_II(x)` can always be inserted into a tunneling field-tolerance envelope
**Status:** INVALIDATED GENERALIZATION

Thin/fast impact ionization is path/history dependent unless local equilibration is justified.

### H9 — downstream photoelectrons may be treated as cold
**Status:** INVALIDATED

For `E_gamma > E_g(x)`, optical generation gives nonzero carrier excess energy.

### H10 — entrance-gap timing maximum is transport independent
**Status:** INVALIDATED GENERALIZATION / SUPERSEDED

The forward-ballistic model gives a maximum; strong-scattering drift-diffusion gives a plateau; finite momentum-memory surrogates permit several post-crossover shapes.

The transport-independent object is the entrance-gap **initial-condition switch**, not a mandatory maximum.

### H11 — wavelength-dependent generation + graded-HgCdTe timing is a new forward model
**Status:** INVALIDATED NOVELTY ROUTE

Primary graded-HgCdTe work already combines wavelength/depth-dependent photogeneration, composition-gradient transport, QE/response modeling, and measured high-speed response.

### H12 — position-resolved HgCdTe transit metrology is new
**Status:** INVALIDATED NOVELTY ROUTE

Primary HgCdTe APD work already uses localized photoexcitation at different positions to study transit-time response.

---

## 2. Important retained supporting results

These remain correct within their stated models but are not the active publication frontier.

### P1 — finite passive-network transfer-area bound
**Status:** DERIVED / CHECKED

```math
\boxed{
\mathcal I_{L\to R}
\le
\frac{2LR}{L+R}.}
```

### P2 — graded-Kane direct-Zener geometry
**Status:** DERIVED / CHECKED / CONDITIONAL

```math
\boxed{
\mathcal S(E)
=\frac{\pi\sqrt{S_cS_v}}
{4\hbar v_K}(x_c-x_v)^2.}
```

With `G=-dE_g/dx`, `S_v=S_c-G`, and `delta=G/S_c`,

```math
\boxed{
\frac{\mathcal S_Z(\delta)}
{\mathcal S_Z(0)}
=
\frac{(2-\delta)^2}
{4(1-\delta)^{3/2}}.}
```

### P3 — quasi-neutral p-type majority-band pinning
**Status:** DERIVED / CONDITIONAL

For nondegenerate holes with `p approximately N_A`,

```math
\boxed{
\frac{dE_v}{dx}
\simeq
k_BT\frac{d}{dx}\ln(N_A/N_v).}
```

Nearly constant `N_A/N_v` gives approximately `E_v constant` and `S_c approximately G`.

### P4 — collection-boundary electrostatic cost
**Status:** DERIVED

```math
\boxed{qV_b\ge\alpha\Delta E_g^{(b)},}
```

and for one-sign compensation field over width `w`,

```math
\boxed{F_{\max}\ge V_b/w.}
```

### P5 — nonlocal graded mean-energy state
**Status:** DERIVED / CONDITIONAL

```math
\boxed{
\frac{d\varepsilon}{dx}
=S_c(x)-\frac{\varepsilon}{\ell_E(x)}.}
```

The derived mean-II phase boundaries remain sensitivity tools, not stochastic onset theorems.

---

## 3. Spectral-generation geometry

### S1 — earliest allowed generation position
**Status:** DERIVED / CONDITIONAL ON LOCAL-GAP ABSORPTION

For linear

```math
E_g(x)=E_{g,\rm in}-Gx,
```

```math
\boxed{
x_g(E_\gamma)
=\max\!\left[
0,
\frac{E_{g,\rm in}-E_\gamma}{G}
\right].}
```

### S2 — entrance-gap initial-condition switch
**Status:** DERIVED / CONDITIONAL

Below `E_g,in`, photon energy moves the first allowed generation position. Above `E_g,in`, the generation position is pinned and photon energy changes the injected carrier state.

A visible cusp or maximum is **not** guaranteed.

### S3 — conditional generation distribution
**Status:** DERIVED APPLICATION OF STANDARD ABSORPTION STATISTICS

In optical-depth coordinates, conditioned on absorption,

```math
\boxed{
p(y|{\rm abs})
=\frac{e^{-y}}{1-e^{-\tau_\gamma}}.}
```

For `alpha=C(E_gamma-E_g)^beta` in a linear gap, the downstream generation offset has a Weibull kernel away from finite-length truncation.

---

## 4. Active candidate — first-moment spectral timing inverse

### I1 — full linear mean-delay operator
**Status:** DERIVED / CONDITIONAL

For wavelength `i`, define

```math
p_i(x)=p(x|E_{\gamma,i},{\rm abs}),
```

```math
\boxed{K_i(s)=P(X_g\le s|E_{\gamma,i},{\rm abs}).}
```

If conditional mean delay is path additive,

```math
m(x)=\int_x^Lq_1(s)ds,
```

then

```math
\boxed{
\mu_i
=\int_0^L K_i(s)q_1(s)ds.}
```

Discretely,

```math
\boxed{
\mathbf T
=\mathbf A\mathbf q_1+c_1\mathbf1.}
```

This is the current core inverse-metrology result.

### I2 — local velocity interpretation
**Status:** CONDITIONAL

When a path-additive local mean-transport description is valid,

```math
\boxed{q_1(x)=1/v_{\rm eff}(x).}
```

In the sharp linear-gradient limit,

```math
\boxed{
v_{\rm eff}[x_g(E_\gamma)]
=\frac1{G\,dT/dE_\gamma}.}
```

For a general monotonic gap,

```math
\boxed{
v_{\rm eff}(x_g)
=-\frac1{E_g'(x_g)\,dT/dE_\gamma}.}
```

Do not interpret `q_1` as microscopic instantaneous velocity without validating the transport closure.

### I3 — finite-depth kernel interpretation
**Status:** DERIVED / CONDITIONAL

Away downstream truncation in the analytic Weibull case,

```math
\boxed{
G\frac{d\bar T}{dE_\gamma}
=\int p(z)\frac{dz}{v_{\rm eff}(x_g+z)}.}
```

Thus finite optical depth gives a kernel-weighted inverse velocity rather than a point value.

---

## 5. Second timing moment

### I4 — two-moment inverse
**Status:** DERIVED / CONDITIONAL

Let conditional timing variance be

```math
V(x)=\int_x^Lq_2(s)ds.
```

Then

```math
\boxed{
\sigma_i^2
=\int_0^L K_i(s)q_2(s)ds
+\operatorname{Var}_{p_i}[m(X)].}
```

After reconstructing `q_1`, define

```math
\boxed{
y_{2,i}
=\sigma_i^2-\operatorname{Var}_{p_i}[m(X)].}
```

so

```math
\boxed{
\mathbf y_2
=\mathbf A\mathbf q_2+c_2\mathbf1.}
```

### I5 — drift-diffusion interpretation of `q_2`
**Status:** CONDITIONAL ONLY

In a local high-Peclet drift-diffusion approximation,

```math
\boxed{q_1=1/v,}
```

```math
\boxed{q_2\simeq2D/v^3.}
```

Do not label reconstructed `q_2` as a microscopic diffusion coefficient without validation.

---

## 6. Frequency-domain observable

### I6 — low-frequency phase and magnitude cumulants
**Status:** KNOWN MATHEMATICS / DERIVED APPLICATION

```math
H_\lambda(\Omega)
=\langle e^{-i\Omega T_\lambda}\rangle.
```

At low frequency,

```math
\boxed{
\arg H_\lambda
=-\Omega\mu_\lambda+O(\Omega^3),}
```

```math
\boxed{
\ln|H_\lambda|
=-\frac{\Omega^2}{2}\sigma_\lambda^2+O(\Omega^4).}
```

For wavelength-independent common electronics,

```math
\boxed{\Delta T\simeq-\Delta\phi/\Omega.}
```

---

## 7. Synthetic conditioning results

### C1 — mean-delay profile recovery
**Status:** CHECKED IN SYNTHETIC MODEL ONLY

A deterministic regression reconstructs a smooth nonuniform synthetic `q_1` profile with finite optical kernels, common delay, and small timing noise.

### C2 — separate mean/broadening anomaly recovery
**Status:** CHECKED IN SYNTHETIC MODEL ONLY

A two-moment regression separately reconstructs a slow-transport region and a spatially distinct high-broadening region in a controlled synthetic case.

### C3 — inverse is spatially band limited
**Status:** CHECKED IN SYNTHETIC MODEL ONLY

Broader generation kernels sharply reduce recoverable singular modes. Wavelength count is not recoverable spatial degree-of-freedom count.

### C4 — extreme-cutoff truncation matters
**Status:** CHECKED IN SYNTHETIC MODEL ONLY

Near the long-wave cutoff, the eligible region truncates the generation kernel and can strongly bias the stationary/narrow-kernel inversion.

These are conditioning checks, not experimental performance claims.

---

## 8. Prior-art boundary

### K1 — forward wavelength/depth generation + graded HgCdTe transport
**Status:** KNOWN PRIOR ART

The 2022 graded-HgCdTe study already writes a wavelength- and depth-dependent generation rate and couples spatially varying composition, internal field, transport, QE, and response-time modeling.

### K2 — spatial HgCdTe transit measurement
**Status:** KNOWN PRIOR ART

Perrais et al. already use localized photoexcitation at different positions to study HgCdTe APD transit response.

### K3 — spectral inference of spatial collection in graded HgCdTe
**Status:** KNOWN PRIOR ART

The 2023 graded-HgCdTe work uses spectral response and controlled profile removal to infer how composition-gradient fields alter carrier collection.

### K4 — close unresolved 2024 application paper
**Status:** OPEN PRIOR-ART RISK

A 2024 paper from the same research group is titled

`Potential application of HgCdTe detector with composition gradient in laser measurement`

(DOI `10.5768/JAO202445.0310009`). Metadata are confirmed, but its full technical contents have not been recovered in the current search.

Do not make a novelty claim until it is read.

### K5 — active candidate claim boundary
**Status:** CANDIDATE UNDEREXPLORED / PRIORITY UNPROVEN

The inspected sources have not yet shown the specific inverse workflow

```text
known monotonic Eg(x)
+
known p(x|lambda)
+
wavelength x frequency timing data
->
regularized spatial reconstruction of q1(x), optionally q2(x).
```

This negative search is not novelty evidence.

---

## 9. Current open questions

### O1 — real dimensional optical kernels
Need a published/measured dimensional `x_Cd(z)` / `E_g(z)` profile and calibrated `alpha(z,lambda)`.

### O2 — experimental phase/timing precision
Need realistic wavelength-dependent phase stability and complex-response precision for a tunable MWIR implementation.

### O3 — independent validation
Need comparison against localized-position excitation or a validated transport simulation.

### O4 — inverse transport closure
Need to determine when reconstructed `q_1` is meaningfully `1/v(x)` and when nonlocal transport requires a more general interpretation.

### O5 — second-moment viability
Need to determine whether magnitude-curvature precision is sufficient to reconstruct `q_2` experimentally.

### O6 — 2024 laser-measurement paper
Need the full paper before any priority claim.

### O7 — publication significance
Continue research. Do not open a manuscript yet.

---

## 10. Explicit non-claims

The project does **not** presently claim

- a universal photodetector sensitivity-speed theorem;
- a universal active-volume bound;
- a new forward wavelength-dependent detector model;
- a new observation that absorption depth affects transit time;
- a new method for localized-position transit measurement in general;
- a universal entrance-gap timing maximum or visible cusp;
- that `q_1` always equals microscopic carrier velocity inverse;
- that `q_2` is always a microscopic diffusion parameter;
- experimental HgCdTe tomography performance;
- novelty or priority for the inverse-metrology method;
- manuscript readiness.
