# Current State — Experiment 01: The Vanishing Absorber

**Date:** 2026-08-09  
**Status:** exploratory; active frontier is wavelength × frequency **inverse metrology** of internal transport in compositionally graded HgCdTe; no novelty claim

## 1. Current question

The original active-volume hypothesis was falsified long ago in the research path. The active problem is now much narrower and detector specific:

> **Can a known monotonic HgCdTe composition / band-gap profile be used as an internal spectral position encoder, so wavelength-resolved complex timing data can be inverted into a spatial carrier-transport profile without physically scanning the excitation position?**

There is still **no manuscript**.

---

## 2. Read first

After root `AGENTS.md`:

1. `HGCDTE_SPECTRAL_TIMING_LINEAR_INVERSE.md`
2. `HGCDTE_SPECTRAL_TIMING_KERNEL_TOMOGRAPHY.md`
3. `HGCDTE_SPECTRAL_TIMING_TWO_MOMENT_INVERSE.md`
4. `HGCDTE_SPECTRAL_TIMING_DIFFERENTIAL_PHASE.md`
5. `HGCDTE_SPECTRAL_TIMING_TOMOGRAPHY_RESOLUTION.md`
6. `HGCDTE_SPECTRAL_TIMING_TOMOGRAPHY_PRIOR_ART_AUDIT.md`
7. `HGCDTE_PUBLISHED_GRADED_DEVICE_TOMOGRAPHY_CASE.md`
8. `HGCDTE_ENTRANCE_GAP_INITIAL_CONDITION_SWITCH.md`
9. `CLAIM_LEDGER.md`
10. `RESEARCH_LOG.md`
11. `ARCHIVE_STATUS.md`

The earlier ballistic timing-peak files are provenance only.

---

## 3. What prior art already establishes

Do **not** claim novelty for

- wavelength-dependent generation depth in photodiodes;
- wavelength-dependent transit time / bandwidth;
- composition-gradient carrier acceleration;
- graded HgCdTe spectral response;
- wavelength- and depth-dependent generation in graded-HgCdTe forward models;
- graded-HgCdTe response-time modeling;
- localized-position transit-time measurements in HgCdTe.

The 2022 graded-HgCdTe paper already writes a depth- and wavelength-dependent generation rate and solves a forward optoelectronic response model.

Perrais et al. already measured HgCdTe APD transit behavior using localized excitation at different positions.

A 2024 same-group paper titled `Potential application of HgCdTe detector with composition gradient in laser measurement` is especially close application prior art; its full technical content has not yet been recovered. Priority is therefore explicitly unresolved.

---

## 4. Narrow candidate contribution

For photon-energy index `i`, let

```math
p_i(x)
=p(x|E_{\gamma,i},{\rm abs})
```

be the known normalized carrier-generation density.

Define

```math
\boxed{
K_i(s)
=P(X_g\le s|E_{\gamma,i},{\rm abs})
=\int_0^s p_i(x)dx.
}
```

Let the conditional mean collection delay for generation at `x` be path additive:

```math
\boxed{
m(x)=\int_x^Lq_1(s)ds.}
```

Then the wavelength-dependent mean delay is

```math
\boxed{
\mu_i
=\int_0^L K_i(s)q_1(s)ds.
}
```

Discretely,

```math
\boxed{
\mathbf T
=\mathbf A\mathbf q_1+c_1\mathbf1.
}
```

The possible contribution is the **inverse use** of this system to reconstruct an internal delay-density profile.

Under a local path-additive transport interpretation,

```math
\boxed{q_1(x)=1/v_{\rm eff}(x).}
```

This is the only active candidate contribution. The forward physics itself is prior art.

---

## 5. Sharp-generation limit

For a linear monotonic gap

```math
E_g(x)=E_{g,\rm in}-Gx,
```

inside the graded-gap interval,

```math
\boxed{
x_g(E_\gamma)
=\frac{E_{g,\rm in}-E_\gamma}{G}.}
```

If generation is sharply localized and delay is path additive,

```math
\boxed{
\frac{dT}{dE_\gamma}
=\frac1{Gv_{\rm eff}[x_g(E_\gamma)]},
}
```

hence

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

This pointwise relation is a limiting case, not the preferred noisy-data reduction.

---

## 6. Finite optical depth

For the local analytic edge law

```math
\alpha=C(E_\gamma-E_g)^\beta
```

inside a linear gap, the generation offset `z=x-x_g` has a stationary Weibull kernel away from downstream truncation.

Then

```math
\boxed{
G\frac{d\bar T}{dE_\gamma}
=\int p(z)\frac{dz}{v_{\rm eff}(x_g+z)}.}
```

Thus finite optical depth makes the spectral derivative a **kernel-averaged inverse velocity**.

Near the long-wave cutoff the kernel is truncated and the full finite-depth forward model must be used.

The full linear inverse

```math
\mathbf T=\mathbf A\mathbf q_1+c_1\mathbf1
```

is preferred because it avoids numerical differentiation and naturally includes finite optical depth.

---

## 7. Second timing moment

If the conditional timing variance is also path additive,

```math
\boxed{
V(x)=\int_x^Lq_2(s)ds,}
```

then

```math
\boxed{
\sigma_i^2
=\int_0^L K_i(s)q_2(s)ds
+\operatorname{Var}_{p_i}[m(X)].}
```

After reconstructing `q_1`, the second term is calculable from the optical kernel.

Define

```math
\boxed{
y_{2,i}
=\sigma_i^2-\operatorname{Var}_{p_i}[m(X)].}
```

Then

```math
\boxed{
\mathbf y_2
=\mathbf A\mathbf q_2+c_2\mathbf1.}
```

So the **same spatial kernel matrix** can reconstruct a timing-broadening profile.

Only in a local high-Peclet drift-diffusion approximation may one identify

```math
\boxed{q_1=1/v,}
```

```math
\boxed{q_2\simeq2D/v^3.}
```

Do not call `q_2` a microscopic diffusion coefficient without validating that transport closure.

---

## 8. Frequency-domain observable

For carrier timing distribution `T_lambda`,

```math
\boxed{
H_\lambda(\Omega)
=\langle e^{-i\Omega T_\lambda}\rangle.}
```

At low modulation frequency,

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

Thus

```text
phase
-> mean delay / q1

magnitude curvature
-> timing variance / q2.
```

For two wavelengths and a wavelength-independent common chain,

```math
\boxed{
\Delta T
\simeq-\Delta\phi/\Omega.}
```

A local phase-resolution scale is

```math
\boxed{
\sigma_{x,\phi}
\sim
v_{\rm eff}\sigma_\phi/\Omega.}
```

At illustrative `v_eff=1e5 m/s`, one degree at `1 GHz` corresponds to about `0.28 um`. This is only a scale estimate.

---

## 9. Synthetic inversion status

Current deterministic regressions demonstrate only mathematical conditioning:

### Mean-delay inversion

With finite optical kernels, a nonuniform synthetic velocity profile, an unknown common timing offset, and small timing noise, the regularized inverse recovers the imposed smooth transport profile and localized slow region.

### Two-moment inversion

A separate synthetic slow-velocity region and high-broadening region can be reconstructed independently in a controlled case.

### Conditioning

Broader optical kernels reduce the number of recoverable spatial modes strongly.

For one normalized SVD audit, the count above relative singular-value threshold `1e-2` fell from approximately

```text
29 -> 18 -> 13 -> 10
```

as the optical kernel scale increased from

```text
0.02 L -> 0.05 L -> 0.10 L -> 0.20 L.
```

These are synthetic model results, **not experimental performance claims**.

---

## 10. Experimental resolution budget

Independent limits include

```text
optical generation-kernel width
source wavelength resolution
gap-profile uncertainty
timing / phase precision
matrix conditioning / regularization
nonlocal carrier transport.
```

For a linear gradient,

```math
\boxed{
\sigma_{x,\lambda}
\simeq
\frac{hc}{G\lambda^2}\sigma_\lambda.}
```

The local timing scale is

```math
\boxed{
\sigma_{x,T}\sim v_{\rm eff}\sigma_T.}
```

Dense wavelength sampling does not overcome a broad optical kernel.

The number of wavelengths is not the number of recoverable spatial degrees of freedom.

---

## 11. Published HgCdTe validation target

### 2022 VPE graded detector

Reported ingredients include

```text
x_Cd approximately 0.57 -> 0.31
FTIR / etch-derived composition-depth profiling
front-side illumination
1.33 ns zero-bias response at 300 K
high-speed impulse and LCA/VNA characterization.
```

Its timing measurement used `1.55 um`, which has strong surface absorption and therefore does not scan the generation kernel through the MWIR gradient.

The same paper already provides the forward generation structure

```math
G_L(z,\lambda)
=\alpha(z,\lambda)\phi_0
\exp\!\left[-\int_0^z\alpha(u,\lambda)du\right].
```

That can be normalized directly into the `p_i(z)` needed by the inverse.

### 2023 graded samples

Reported processed thicknesses are approximately

```text
7.6 um
3.7 um,
```

with composition-gradient fields altering minority-carrier collection and spectral response.

These structures provide realistic dimensional scales, but the exact fitted composition-profile parameters are embedded in figures and have not yet been recovered reliably.

---

## 12. Prior-art boundary

Strong collisions now include

- Perrais et al.: localized-position HgCdTe transit-time measurement;
- Singh et al.: grading-induced HgCdTe impulse-response improvement;
- Sang et al. 2022: wavelength/depth generation + graded transport + response-time forward model;
- Xu et al. 2023: spectral response used to infer spatial collection differences in graded HgCdTe;
- 2024 multiphysics graded-HgCdTe forward simulations including wavelength effects;
- an unresolved 2024 paper titled `Potential application of HgCdTe detector with composition gradient in laser measurement`.

Therefore the project does **not** claim novelty for any forward wavelength/timing coupling.

Current candidate status:

> **candidate underexplored inverse-metrology method; priority unproven.**

The scientific value, if any, must come from recovering useful internal transport information that existing forward modeling or ordinary bandwidth measurements do not provide.

---

## 13. Best validation

The strongest validation is now

```text
known dimensional Eg(x)
+
known/calibrated p(x|lambda)
+
wavelength × frequency complex-response data
->
reconstruct q1(x), optionally q2(x)
```

and compare against

```text
localized-position excitation timing
or
validated transport simulation.
```

Agreement would demonstrate the inverse measurement capability.

---

## 14. Current next step

Do **not** add more generic inverse mathematics.

Next priorities:

1. recover a real dimensional graded profile from primary data;
2. calculate its actual `p_i(x)` and `A` matrix;
3. predict differential RF phase/magnitude versus wavelength;
4. determine achievable spatial modes and required phase precision;
5. obtain/read the 2024 laser-measurement paper before any novelty language;
6. reassess manuscript readiness only after real-device inversion or independent validation.
