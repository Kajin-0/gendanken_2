# Current State — Experiment 01: The Vanishing Absorber

**Date:** 2026-08-10  
**Status:** exploratory theory research; strongest frontier is now an **exact nested falsification framework for photocarrier transit dynamics using complex RF response and wavelength as an internal spatial coordinate**; HgCdTe is the leading worked example, not the source of the general theorems; no novelty claim

There is still **no manuscript**.

---

## 1. Active question

The original universal detector-bound program, ballistic timing-peak route, arbitrary-profile static inverse, and fabrication-first translated-gradient design have all served their purpose but are **not** the present research frontier.

The active question is now:

> **What exact, parameter-free relations must a photodetector's complex timing response obey at progressively stronger levels of transport theory, and can wavelength-dependent internal generation supply the spatial coordinate needed to falsify those levels experimentally?**

The goal is a hierarchy

```text
simple gedanken experiment
-> exact theorem
-> parameter-free null prediction
-> explicit failure signatures
-> statistical detection threshold
-> HgCdTe worked example.
```

This is theory-first work. Fabrication feasibility remains supporting context only.

---

## 2. Read first

After root `AGENTS.md`:

1. `THEORY_FALSIFICATION_LADDER.md`
2. `THEORY_CLAIM_LEDGER.md`
3. `MINIMAL_TWO_DEPTH_TWO_FREQUENCY_GEDANKEN.md`
4. `TRANSIT_TIME_CHARACTERISTIC_FUNCTION_NULL_TESTS.md`
5. `SPATIAL_FIRST_PASSAGE_SEMIGROUP_THEOREM.md`
6. `THREE_COLOR_SPECTRAL_CLOSURE_THEOREM.md`
7. `LOCAL_MARKOV_TRANSPORT_CLOSURE_THEOREM.md`
8. `MULTIFREQUENCY_CLOSURE_STATISTICAL_TEST.md`
9. `TRANSPORT_CLOSURE_FAILURE_SIGNATURES.md`
10. `STOCHASTIC_OCCUPATION_TIME_RESPONSE_THEOREM.md`
11. `OCCUPATION_TIME_CUMULANT_HIERARCHY.md`
12. `TRANSLATION_RESPONSE_THEOREM.md`
13. `SPATIAL_DERIVATIVE_NOISE_RESOLUTION.md`
14. `HGCDTE_DOWNSTREAM_DRIFT_DIFFUSION_RELOCATION.md`
15. `HGCDTE_TRANSLATED_GRADIENT_PRIOR_ART_BOUNDARY.md`
16. legacy `CLAIM_LEDGER.md`
17. `RESEARCH_LOG.md`
18. `RESEARCH_LOG_2026-08-10_CONTINUATION.md`
19. `ARCHIVE_STATUS.md`

The many purpose-built HgCdTe fabrication/design files are retained as provenance and future worked-example material. They are no longer the first place to continue theoretical research.

---

## 3. Hard prior-art boundary

Do **not** claim novelty for

- wavelength-dependent photodiode absorption/generation depth;
- wavelength-dependent RF phase, timing, or bandwidth;
- optoelectronic chromatic dispersion;
- using photodiode carrier dynamics for wavelength sensing;
- multi-frequency photodiode response characterization;
- algebraic convection-diffusion coefficient inversion from modulated profiles;
- characteristic-function positive-definiteness;
- Doob `h`-transforms / conditioned diffusion;
- Feynman-Kac / occupation-time mathematics;
- graded-HgCdTe built-in fields and high-speed response;
- localized-position HgCdTe transit measurements.

Important collisions:

```text
Glasser et al. 2021+:
optoelectronic chromatic dispersion from wavelength-dependent absorption depth

Kassa et al. 2026:
DC + RF amplitude + RF phase over multiple modulation frequencies for single-photodiode computational spectroscopy

Wang et al. 2014:
three-wavelength photodiode/receiver phase-response characterization

Sattin / Escande et al.:
local algebraic inversion of modulated convection-diffusion profiles and singularity analysis.
```

The unresolved 2024 paper

`Potential application of HgCdTe detector with composition gradient in laser measurement`

DOI `10.5768/JAO202445.0310009`

remains a close HgCdTe-specific collision whose full technical content has not been recovered.

Current candidate status:

> **integrated detector falsification framework / spectral-depth closure method — priority unproven.**

---

# 4. Level 0 — any positive classical transit-time distribution

If the de-embedded DC-normalized response is

```math
H(\omega)=E[e^{-i\omega T}],
\qquad T\ge0,
```

then `H` is a characteristic function.

Therefore

```math
H(0)=1,
```

```math
H(-\omega)=H(\omega)^*,
```

```math
|H(\omega)|\le1,
```

and for every RF set

```math
\boxed{K_{jk}=H(\omega_j-\omega_k)\succeq0.}
```

A particularly simple exact two-harmonic null is

```math
\boxed{
|H(2\omega)-H(\omega)^2|
\le
1-|H(\omega)|^2.
}
```

If this fails beyond measurement uncertainty, the observable cannot even be represented as a positive classical transit-time distribution. Do not fit drift/diffusion before fixing that problem.

---

# 5. Level 1 — wavelength as a homogeneous internal spatial coordinate

For a scalar, spatially homogeneous, continuous-path strong-Markov first-passage coordinate,

```math
\boxed{U_s(a+b)=U_s(a)U_s(b).}
```

Continuity implies

```math
U_s(d)=e^{-\gamma_s d}.
```

DC normalization preserves exponential spatial propagation.

If wavelength rigidly translates one generation kernel

```math
p_\lambda(z)=g[z-z_g(\lambda)],
```

then even an arbitrarily broad/asymmetric fixed `g` gives

```math
\boxed{
H(z_g,\omega)=B(\omega)e^{\Gamma(\omega)z_g}.
}
```

Therefore three wavelengths with equally spaced calibrated generation centers obey

```math
\boxed{
H_2(\omega)^2=H_1(\omega)H_3(\omega).
}
```

This is the current simplest detector-specific null prediction:

> **three colors in -> one complex identity out.**

Generation **shape evolution**, not finite width by itself, is the optical correction.

A hidden mixture of two propagation populations generically breaks this scalar semigroup law.

---

# 6. Level 2 — real local Markov drift-diffusion

For conditioned transport

```math
D(z)F''+w(z)F'-i\omega F=0,
```

define

```math
r_\omega=\partial_z\ln F,
```

```math
A_\omega=r_\omega'+r_\omega^2.
```

Then exactly

```math
D A_\omega+w r_\omega=i\omega.
```

With

```math
\delta_\omega
=\Re A_\omega\Im r_\omega
-\Im A_\omega\Re r_\omega,
```

one nonsingular frequency gives the real apparent coefficients

```math
\boxed{
D_{app}(\omega)
=-\omega\Re r_\omega/\delta_\omega,
}
```

```math
\boxed{
w_{app}(\omega)
=\omega\Re A_\omega/\delta_\omega.
}
```

### Exact closure theorem

One real frequency-independent local second-order Markov generator exists at that depth **if and only if**

```math
\boxed{
D_{app}(\omega)=\mathrm{constant},
\qquad
w_{app}(\omega)=\mathrm{constant}
}
```

across RF frequency.

For `N` frequencies there are

```math
\boxed{2(N-1)}
```

real closure conditions.

The previously used three-frequency complex determinant is **only necessary, not sufficient**; common complex effective coefficients are an explicit counterexample.

---

# 7. Minimal two-depth / two-frequency gedanken experiment

For a uniform segment,

```math
\gamma(\omega)
=\frac{\sqrt{w^2+4iD\omega}-w}{2D}.
```

Two generation depths determine

```math
\gamma
=\frac{\ln[H(z_2)/H(z_1)]}{z_2-z_1}.
```

Write

```math
\gamma=a+ib.
```

Then one complex RF measurement gives exactly

```math
\boxed{
D=\frac{\omega a}{b(a^2+b^2)},
}
```

```math
\boxed{
w=\frac{\omega(b^2-a^2)}{b(a^2+b^2)}.
}
```

For positive downstream drift,

```math
\boxed{0<a<b.}
```

The **second RF frequency adds no transport parameter**.

It is therefore a pure model test:

```math
D(\omega_2)=D(\omega_1),
\qquad
w(\omega_2)=w(\omega_1).
```

This is likely the best opening gedanken experiment for a future paper.

---

# 8. DC normalization is a physical conditioning operation

Let

```math
h(z)=U(z,0)
```

be successful collection probability before local Markov recombination.

The normalized RF field obeys an exact conditioned equation with

```math
\boxed{
w_{cond}
=v+2D\partial_z\ln h.
}
```

Therefore normalized RF measures the dynamics of carriers **conditioned on eventual collection**.

It does not generally separate physical drift from recombination.

The DC collection field provides the missing information.

In the simple uniform exponential case,

```math
c=\partial_z\ln h,
```

```math
v=w-2Dc,
```

```math
\kappa=Dc^2+vc,
```

```math
\tau=1/\kappa.
```

---

# 9. What closure failure looks like

A single low-frequency drift-diffusion fit is weak evidence because memory can hide as renormalized apparent coefficients.

For

```math
D r^2+wr=\Psi(s),
\qquad
\Psi(s)=c_1s+c_2s^2+\cdots,
```

forcing ordinary drift-diffusion gives

```math
w_{app}(0)=w/c_1,
```

```math
D_{app}(0)=D/c_1-c_2w^2/c_1^3.
```

Explicit theory archetypes now exist for

```text
reversible trapping -> one-pole turnover
finite flux/momentum relaxation -> low-RF renormalization + even-frequency dispersion
leading spatial nonlocality -> D_app-D ~ +omega^2, w_app-w ~ -omega^2.
```

Closure failure falsifies the smaller model but does not uniquely identify a microscopic mechanism.

---

# 10. Statistical closure test

Stack `N` apparent coefficient vectors `(D_j,w_j)` with full covariance `C`.

Fit one common pair by generalized least squares.

The residual statistic

```math
Q
=(\hat g-X\hat\theta)^TC^{-1}(\hat g-X\hat\theta)
```

obeys, under linearized Gaussian errors,

```math
\boxed{Q\sim\chi^2_{2N-2}}
```

under the Markov null.

Under an alternative, the noncentrality

```math
\boxed{
\Lambda=\mu_\perp^TC^{-1}\mu_\perp
}
```

sets rejection power.

Thus the exact theorem already has a conventional significance framework.

---

# 11. Arbitrary stochastic paths — occupation-time theorem

For any successful trajectory `X_t` with random transit time `T`, define

```math
\ell(z)=\int_0^T\delta(X_t-z)dt.
```

Apply an ideal weak local **clock perturbation**.

For a point perturbation of area `A_h`, the exact first logarithmic response is

```math
\boxed{
S(z,\omega)
=-i\omega A_h
\frac{E[e^{-i\omega T}\ell(z)]}{H(\omega)}.
}
```

No Markov, drift-diffusion, or deterministic-path assumption is required.

Exact global sum rule:

```math
\boxed{
\int S(z,\omega)dz
=A_h\omega\partial_\omega\ln H(\omega).
}
```

Low RF:

```math
\boxed{
\frac{S}{-i\omega A_h}
=E[\ell(z)]
-i\omega Cov[T,\ell(z)]
+O(\omega^2).
}
```

So a local clock scan resolves

```text
where successful carriers spend their mean time
and which regions contribute to global transit-time dispersion.
```

---

# 12. Full spatial timing-cumulant hierarchy

The frequency-tilted occupation field has the exact expansion

```math
\boxed{
\rho_\omega(z)
=
\sum_{n=0}^{\infty}
\frac{(-i\omega)^n}{n!}
\kappa(\ell(z),T,\ldots,T).
}
```

Since every trajectory obeys

```math
\int\ell(z)dz=T,
```

```math
\boxed{
\int dz\,
\kappa(\ell(z),T,\ldots,T)
=
\kappa_{n+1}(T).
}
```

Therefore the theory provides exact spatial decompositions of

```text
mean transit time
variance
skewness
and every higher timing cumulant.
```

This is a stronger theoretical target than a simple velocity map.

---

# 13. Deterministic translated-feature limit

For monotonic deterministic transport, the earlier translated-feature theorem becomes much stronger:

```math
R_{\lambda,\omega}(z)
\propto
p_\lambda(z)e^{-i\omega T(z)}.
```

Hence

```text
normalized magnitude -> generation PDF
phase slope / omega -> local slowness q(z).
```

and

```math
\int R dz=-i\omega A_h.
```

These are now treated as **strong limiting null predictions** rather than assumptions to impose on stochastic data.

---

# 14. Spatial differentiation is the practical resolution cost

For noisy `y=ln F` samples, a centered first derivative has

```text
variance ~ h^-2
bias^2 ~ h^4
```

with optimum

```math
\boxed{
h_{1,*}=(3\sigma_y/|y'''|)^{1/3}.}
```

A centered second derivative has

```text
variance ~ h^-4
bias^2 ~ h^4
```

with optimum

```math
\boxed{
h_{2,*}=864^{1/8}(\sigma_y/|y''''|)^{1/4}.}
```

With white averaging,

```text
first-derivative spatial scale ~ t^-1/6
second-derivative scale ~ t^-1/8.
```

Brute-force averaging therefore improves arbitrary-profile spatial resolution very slowly.

This favors the simple uniform/three-color gedanken experiments as the first falsification targets.

---

# 15. Where HgCdTe fits now

HgCdTe remains a particularly useful worked example because a monotonic composition/bandgap profile can make wavelength act as an internal generation-depth coordinate, while composition gradients also modify minority-carrier transport.

But the general theorems above do **not** depend on HgCdTe.

The existing repository work on

```text
published A/B structures
sample-B spectral kernels
translated-gradient controls
first-passage HgCdTe transport
band-edge self-consistency
MBE/MOCVD/LPE feasibility
```

should now be used to answer one narrower question:

> **What numerical size of the exact null residuals should a plausible HgCdTe experiment show under ordinary drift-diffusion versus specific trapping/nonlocal alternatives?**

That is a worked falsifiable prediction, not a fabrication project.

---

# 16. Immediate next work

The highest-value next steps are:

1. finish focused prior-art audits for the detector-specific three-color semigroup closure, characteristic-function timing diagnostics, and local perturbation cumulant spectroscopy;
2. construct one minimal HgCdTe theoretical example with a credible monotonic `x(z)` and absorption law;
3. compute the three-color closure exactly including real wavelength-dependent kernel-shape correction;
4. compute two-frequency `D_app,w_app` under conventional drift-diffusion, trapping, relaxation, and a nonlocal alternative;
5. derive predicted effect sizes relative to plausible response precision;
6. only after that reassess whether the result is distinct and complete enough to begin a paper.

Do **not** return to detailed fabrication optimization unless a theoretical prediction specifically requires a feasibility check.
