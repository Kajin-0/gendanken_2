# Active Theory Claim Ledger — Experiment 01

**Updated:** 2026-08-10  
**Purpose:** epistemic boundary for the new theory-first falsification framework. The older `CLAIM_LEDGER.md` remains authoritative provenance for earlier branches; this file records claims developed after the theory pivot.

## Status vocabulary

- **KNOWN** — established external mathematics/physics used as input.
- **DERIVED** — exact consequence of stated assumptions.
- **CHECKED** — independently/numerically verified.
- **CONDITIONAL** — valid only inside stated reduced model/measurement assumptions.
- **CANDIDATE DISTINCT — PRIORITY UNPROVEN** — potentially unusual detector formulation; literature boundary incomplete.
- **INVALIDATED** — explicit counterexample/correction found.
- **SUPERSEDED** — replaced by a stronger/corrected result.
- **OPEN** — unresolved.
- **NON-CLAIM** — explicitly not asserted.

---

## A. Model-independent timing layer

### T0 — RF timing response as a characteristic function
**Status:** KNOWN probability theory / DERIVED detector null-test application

If a de-embedded DC-normalized response is a positive classical transit-time distribution,

```math
H(\omega)=E[e^{-i\omega T}],
```

then `H` is positive definite:

```math
K_{jk}=H(\omega_j-\omega_k)\succeq0.
```

### T1 — two-harmonic timing inequality
**Status:** DERIVED / CHECKED

```math
\boxed{
|H(2\omega)-H(\omega)^2|
\le1-|H(\omega)|^2.
}
```

A violation excludes *any* positive classical transit-time distribution for the tested observable, before drift-diffusion is considered.

### T2 — characteristic-function mathematics is not a novelty claim
**Status:** NON-CLAIM

Positive-definiteness/Bochner-type constraints are established mathematics. Candidate value is their use as a detector timing validation layer.

---

## B. Spatial-coordinate / semigroup layer

### S0 — spatial first-passage semigroup
**Status:** KNOWN strong-Markov consequence / DERIVED application

For a scalar, spatially homogeneous, continuous-path strong-Markov first-passage coordinate with no unresolved state,

```math
\boxed{U_s(a+b)=U_s(a)U_s(b).}
```

Continuity gives

```math
U_s(d)=e^{-\gamma_s d}.
```

### S1 — three-color geometric-mean law
**Status:** DERIVED / CHECKED / CONDITIONAL

If wavelength rigidly translates one generation kernel through a homogeneous segment, three wavelengths with equally spaced calibrated generation centers obey

```math
\boxed{H_2(\omega)^2=H_1(\omega)H_3(\omega).}
```

### S2 — finite generation width does not by itself spoil S1
**Status:** DERIVED / CHECKED

Any fixed translated kernel shape factors into one wavelength-independent multiplicative transform at fixed RF. Width, asymmetry, and multimodality cancel from the geometric-mean law.

### S3 — generation-shape evolution is the relevant optical correction
**Status:** DERIVED

If kernel shapes differ with wavelength,

```math
H_j=B_j e^{\Gamma z_j},
```

and

```math
H_2^2/(H_1H_3)=B_2^2/(B_1B_3).
```

### S4 — hidden-population mixture can break scalar spatial semigroup closure
**Status:** CHECKED counterexample

A mixture

```math
p e^{-\Gamma_1d}+(1-p)e^{-\Gamma_2d}
```

generically violates the three-point geometric-mean relation even if each component separately propagates homogeneously.

### S5 — wavelength-dependent RF phase from absorption depth is prior art
**Status:** KNOWN / HARD BOUNDARY

Optoelectronic chromatic dispersion and wavelength-dependent photodiode RF response are established. Do not claim novelty for using absorption depth to create wavelength-dependent RF phase/amplitude.

---

## C. Real local Markov drift-diffusion layer

### M0 — exact local log-response equation
**Status:** DERIVED

For conditioned local drift-diffusion

```math
D F''+wF'-i\omega F=0,
```

define

```math
r_\omega=\partial_z\ln F,
\qquad
A_\omega=r_\omega'+r_\omega^2.
```

Then exactly

```math
\boxed{DA_\omega+wr_\omega=i\omega.}
```

### M1 — per-frequency real apparent coefficients
**Status:** DERIVED

With

```math
\delta_\omega
=\Re A_\omega\Im r_\omega-
\Im A_\omega\Re r_\omega,
```

and `delta != 0`,

```math
\boxed{D_{app}=-\omega\Re r/\delta,}
```

```math
\boxed{w_{app}=\omega\Re A/\delta.}
```

### M2 — exact real multi-frequency closure theorem
**Status:** DERIVED / CHECKED

One real frequency-independent second-order local Markov generator exists at a depth **iff** `D_app` and `w_app` are each frequency-independent over the measured nonsingular RF set.

For `N` frequencies this gives `2(N-1)` real closure conditions.

### M3 — complex 3x3 determinant alone is sufficient
**Status:** INVALIDATED

The complex determinant

```math
det[A_j,r_j,i\omega_j]=0
```

is necessary but not sufficient; common complex coefficients provide a counterexample.

### M4 — minimal uniform two-depth inversion
**Status:** DERIVED / CHECKED

For uniform transport and

```math
\gamma=a+ib,
```

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

One RF frequency identifies `D,w`; a second RF frequency adds no parameter and becomes a pure model test.

### M5 — downstream positive-drift sign cone
**Status:** DERIVED

For `D>0,w>0,omega>0`,

```math
\boxed{0<\Re\gamma<\Im\gamma.}
```

### M6 — algebraic convection-diffusion inversion is not a novelty claim
**Status:** HARD PRIOR-ART BOUNDARY

Sattin/Escande and related modulated-transport work already develops local algebraic convection/diffusion inversion and singularity analysis. Candidate value must lie in the detector-specific nested closure framework, not coefficient extraction alone.

---

## D. DC conditioning / recombination layer

### C0 — DC normalization is a conditioning transform
**Status:** KNOWN Doob-transform mathematics / DERIVED detector consequence

For local killing/recombination with collection probability `h(z)`, the DC-normalized RF field obeys a conditioned equation with

```math
\boxed{w_{cond}=v+2D\partial_z\ln h.}
```

### C1 — normalized RF alone does not generally separate physical drift and recombination
**Status:** DERIVED STRUCTURAL IDENTIFIABILITY LIMIT

RF of successful carriers measures conditioned transport. Physical `v` and killing rate require the DC collection field.

### C2 — uniform exponential unconditioning
**Status:** DERIVED / CHECKED / CONDITIONAL

For

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

## E. Closure-failure hierarchy

### F0 — low-frequency fit agreement does not establish Markov transport
**Status:** DERIVED

For temporal memory

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

Memory can therefore hide as renormalized low-RF transport coefficients.

### F1 — reversible trapping archetype
**Status:** DERIVED / CHECKED / CONDITIONAL

A one-pole trapping/release memory produces a characteristic RF turnover in apparent coefficients.

### F2 — finite flux/momentum-relaxation archetype
**Status:** DERIVED / CHECKED / CONDITIONAL

A telegraph-like correction shifts low-RF apparent diffusion and produces higher-frequency dispersion.

### F3 — leading spatial nonlocal correction
**Status:** DERIVED / CHECKED / CONDITIONAL

For

```math
C F'''+D F''+wF'-sF=0,
```

uniform low-RF apparent coefficients obey

```math
D_{app}-D\propto+\omega^2,
```

```math
w_{app}-w\propto-\omega^2.
```

### F4 — closure failure is not unique mechanism identification
**Status:** NON-CLAIM

Frequency dispersion falsifies the smaller local Markov model; additional mechanism-specific tests are required.

---

## F. Stochastic local-perturbation layer

### O0 — occupation-time response theorem
**Status:** DERIVED / CHECKED; mathematics closely related to established Feynman-Kac/occupation-time theory

For arbitrary successful trajectories and an ideal local clock perturbation,

```math
\boxed{
S(z,\omega)
=-i\omega A_h
\frac{E[e^{-i\omega T}\ell(z)]}{H(\omega)}.
}
```

No Markov or drift-diffusion assumption is required.

### O1 — global occupation response sum rule
**Status:** DERIVED / CHECKED

```math
\boxed{
\int S(z,\omega)dz
=A_h\omega\partial_\omega\ln H(\omega).
}
```

### O2 — low-frequency local occupation interpretation
**Status:** DERIVED / CHECKED

```math
\frac{S}{-i\omega A_h}
=
E[\ell(z)]
-i\omega Cov[T,\ell(z)]
+O(\omega^2).
```

### O3 — full local timing-cumulant hierarchy
**Status:** DERIVED / CHECKED

```math
\rho_\omega(z)
=
\sum_{n=0}^{\infty}
\frac{(-i\omega)^n}{n!}
\kappa(\ell(z),T,\ldots,T).
```

### O4 — every local mixed cumulant integrates to the next global timing cumulant
**Status:** DERIVED / CHECKED

```math
\boxed{
\int dz\,\kappa(\ell(z),T,\ldots,T)
=\kappa_{n+1}(T).
}
```

Thus mean, variance, skewness, and higher transit-time cumulants have exact spatial decompositions under the ideal clock perturbation.

### O5 — local clock perturbation is an idealization
**Status:** NON-CLAIM / IMPORTANT BOUNDARY

A real electric-field/composition perturbation generally changes path probabilities and transport coefficients as well as local clock accumulation. The occupation theorem is an exact baseline/null, not automatically the response of a real graded layer.

---

## G. Deterministic translated-feature limit

### R0 — deterministic point-feature factorization
**Status:** DERIVED / CHECKED / CONDITIONAL

For monotonic deterministic path transport,

```math
R_{\lambda,\omega}(z)
\propto p_\lambda(z)e^{-i\omega T(z)}.
```

### R1 — relocation magnitude reconstructs generation PDF
**Status:** DERIVED / CONDITIONAL

Normalized `|R(z)|` gives `p_lambda(z)` exactly in the point-feature deterministic limit.

### R2 — relocation phase slope reconstructs local slowness
**Status:** DERIVED / CONDITIONAL

```math
q(z)=\omega^{-1}\partial_z\arg R.
```

### R3 — deterministic relocation complex sum rule
**Status:** DERIVED / CHECKED

```math
\int R dz=-i\omega A_h.
```

### R4 — deterministic factorization is not to be imposed on stochastic transport
**Status:** NON-CLAIM

Its failure is potentially diagnostic of path dispersion/backtracking/conditioning or perturbation-induced path changes.

---

## H. Statistical / resolution claims

### Q0 — multi-frequency closure chi-square test
**Status:** DERIVED / CONDITIONAL ON LINEARIZED GAUSSIAN COVARIANCE

For `N` apparent `(D,w)` pairs with known covariance, the GLS common-coefficient residual obeys

```math
\boxed{Q\sim\chi^2_{2N-2}}
```

under the local Markov null.

### Q1 — noncentrality controls rejection power
**Status:** DERIVED

```math
\Lambda=\mu_\perp^TC^{-1}\mu_\perp.
```

### Q2 — first-derivative finite-difference optimum
**Status:** DERIVED / CONDITIONAL

```math
h_{1,*}=(3\sigma_y/|y'''|)^{1/3}.
```

With white averaging, `h1* ~ t^-1/6`.

### Q3 — second-derivative finite-difference optimum
**Status:** DERIVED / CONDITIONAL

```math
h_{2,*}=864^{1/8}(\sigma_y/|y''''|)^{1/4}.
```

With white averaging, `h2* ~ t^-1/8`.

### Q4 — these finite-difference laws are not universal information bounds
**Status:** NON-CLAIM

They depend on the stated estimator/noise/smoothness assumptions.

---

## I. Active candidate contribution

### A0 — integrated detector falsification ladder
**Status:** CANDIDATE DISTINCT — PRIORITY UNPROVEN

The candidate is the integrated framework

```text
characteristic-function timing validation
-> spectral spatial-semigroup / three-color closure
-> real multi-frequency local Markov closure
-> DC unconditioning
-> closure-failure mechanism hierarchy
-> local occupation/cumulant perturbation spectroscopy
-> HgCdTe graded-absorber realization.
```

No individual mathematical ingredient should be assumed novel.

### A1 — three-color spectral geometric-mean detector law
**Status:** CANDIDATE DISTINCT — PRIORITY UNPROVEN

The exact `H2^2=H1H3` detector null for equally spaced calibrated generation coordinates under rigid spectral translation/homogeneous first-passage propagation requires focused literature audit.

### A2 — detector use of characteristic-function positivity
**Status:** CANDIDATE DISTINCT APPLICATION — PRIORITY UNPROVEN

Probability theorem is known; systematic photodetector timing diagnostic use is not established by the current search.

### A3 — occupation/cumulant spatial detector spectroscopy
**Status:** CANDIDATE DISTINCT APPLICATION — PRIORITY UNPROVEN

Occupation/Feynman-Kac mathematics is known. Use of a translated internal perturbation to spatially decompose detector timing cumulants requires dedicated prior-art audit.

---

## J. Hard recent prior-art collisions

### PA1 — optoelectronic chromatic dispersion
**Status:** KNOWN COLLISION

Glasser et al. (2021) and follow-up work explicitly use wavelength-dependent photodiode absorption depth to produce RF phase shifts / effective chromatic dispersion.

### PA2 — multi-frequency OED computational spectroscopy
**Status:** KNOWN CLOSE CONTEXT

A 2026 single-photodiode computational spectroscopy work uses DC, RF amplitude, and RF phase across many modulation frequencies to infer optical wavelength from absorption-depth-dependent dynamics.

### PA3 — three-wavelength photodiode phase characterization
**Status:** KNOWN CONTEXT

Wang et al. (2014) used three optical wavelengths in a photodiode/receiver phase-response characterization algorithm. Current accessible abstract indicates calibration/characterization intent, not the internal-depth semigroup null developed here.

### PA4 — modulated convection-diffusion algebraic inverse
**Status:** KNOWN COLLISION

Sattin/Escande et al. already developed local algebraic inversion of modulated convection-diffusion profiles and singularity analysis.

### PA5 — unresolved 2024 HgCdTe laser-measurement paper
**Status:** OPEN CLOSE COLLISION

`Potential application of HgCdTe detector with composition gradient in laser measurement`, DOI `10.5768/JAO202445.0310009`, remains incompletely accessible.

---

## K. Current nonclaims

Do not claim yet:

- a first-ever spectral transport tomography method;
- novelty of wavelength-dependent RF timing in a photodiode;
- novelty of algebraic drift/diffusion inversion;
- novelty of Doob conditioning or occupation-time cumulants;
- a universal spatial-resolution bound;
- that closure failure uniquely proves trapping, hot carriers, or nonlocality;
- that HgCdTe is required for the theory;
- manuscript readiness.

The current goal is to sharpen the theorem package and falsification predictions until the literature boundary and a realistic worked example justify manuscript construction.
