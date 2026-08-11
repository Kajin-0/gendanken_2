# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gendanken_2`  
**Active experiment:** `experiments/01-vanishing-absorber/`  
**Current mode:** **theory-first transport research; strongest frontier is an exact nested falsification framework using complex RF response plus wavelength as an internal spatial coordinate; HgCdTe is the leading worked example, not the source of the general theory; no novelty claim**

Read this file first.

The repository follows the physics rather than a predetermined paper. Failed conjectures, numerical corrections, counterexamples, and prior-art collisions are part of the result.

**There is still no manuscript.**

---

## 1. Mandatory repository protocol

Before every write:

1. fetch live `main` / current target;
2. inspect intervening changes when needed;
3. fetch the exact current blob SHA before replacing a file;
4. never overwrite stale state;
5. preserve failed/corrected branches;
6. make narrow edits where practical;
7. update the canonical state when the scientific frontier actually changes.

**Live `main` overrides snapshots and recovery notes.**

Do not delete an old result merely because it was superseded. Mark it explicitly and preserve why the direction changed.

---

## 2. Epistemic labels

Use explicitly:

- **KNOWN**
- **DERIVED**
- **CHECKED**
- **CONDITIONAL**
- **CANDIDATE DISTINCT — PRIORITY UNPROVEN**
- **INVALIDATED**
- **SUPERSEDED**
- **OPEN**
- **NON-CLAIM**

A negative literature search is not novelty evidence.

Do not use `first`, `new fundamental`, `universal`, etc. without a focused primary-source audit and claim-ledger update.

---

## 3. Canonical reading order

1. `experiments/01-vanishing-absorber/CURRENT_STATE.md`
2. `experiments/01-vanishing-absorber/THEORY_FALSIFICATION_LADDER.md`
3. `experiments/01-vanishing-absorber/THEORY_CLAIM_LEDGER.md`
4. `experiments/01-vanishing-absorber/MINIMAL_TWO_DEPTH_TWO_FREQUENCY_GEDANKEN.md`
5. `experiments/01-vanishing-absorber/TRANSIT_TIME_CHARACTERISTIC_FUNCTION_NULL_TESTS.md`
6. `experiments/01-vanishing-absorber/SPATIAL_FIRST_PASSAGE_SEMIGROUP_THEOREM.md`
7. `experiments/01-vanishing-absorber/THREE_COLOR_SPECTRAL_CLOSURE_THEOREM.md`
8. `experiments/01-vanishing-absorber/LOCAL_MARKOV_TRANSPORT_CLOSURE_THEOREM.md`
9. `experiments/01-vanishing-absorber/MULTIFREQUENCY_CLOSURE_STATISTICAL_TEST.md`
10. `experiments/01-vanishing-absorber/TRANSPORT_CLOSURE_FAILURE_SIGNATURES.md`
11. `experiments/01-vanishing-absorber/STOCHASTIC_OCCUPATION_TIME_RESPONSE_THEOREM.md`
12. `experiments/01-vanishing-absorber/OCCUPATION_TIME_CUMULANT_HIERARCHY.md`
13. `experiments/01-vanishing-absorber/TRANSLATION_RESPONSE_THEOREM.md`
14. `experiments/01-vanishing-absorber/SPATIAL_DERIVATIVE_NOISE_RESOLUTION.md`
15. `experiments/01-vanishing-absorber/HGCDTE_DOWNSTREAM_DRIFT_DIFFUSION_RELOCATION.md`
16. `experiments/01-vanishing-absorber/HGCDTE_TRANSLATED_GRADIENT_PRIOR_ART_BOUNDARY.md`
17. legacy `experiments/01-vanishing-absorber/CLAIM_LEDGER.md`
18. `experiments/01-vanishing-absorber/RESEARCH_LOG.md`
19. `experiments/01-vanishing-absorber/RESEARCH_LOG_2026-08-10_CONTINUATION.md`
20. `experiments/01-vanishing-absorber/ARCHIVE_STATUS.md`

The many older HgCdTe fabrication/design files are supporting provenance. Do not restart fabrication optimization unless a theoretical prediction specifically requires a feasibility check.

---

## 4. Current research path

```text
vanishing-absorber thought experiment
-> universal active-volume route killed

abstract resource-bound branches
-> successive counterexamples

HgCdTe grading branch
-> wavelength-dependent internal generation coordinate

ballistic timing peak
-> killed as universal by scattering dependence

spectral timing inverse
-> exact CDF/survival operators
-> few-mode conditioning limit

published HgCdTe A/B validation attempt
-> raw spectral leverage exists
-> smooth-mode/contact confounding prevents unique mechanism attribution

purpose-built translated-gradient control
-> improves causal geometry
-> fabrication feasibility checked

USER/PROJECT CORRECTION
-> fabrication is not the research goal
-> return to theory-first gedanken experiments and falsifiable predictions

exact uniform drift-diffusion propagation
-> one complex spatial slope gives D and conditioned drift

recombination-conditioning theorem
-> DC-normalized RF measures successful-carrier conditioned dynamics
-> DC collection field is required to recover physical drift/recombination

exact arbitrary-profile local closure
-> D(z),w(z) recoverable algebraically from local complex response derivatives
-> real multi-frequency frequency-independence is the actual falsification law

complex determinant correction
-> 3x3 complex determinant is necessary but not sufficient
-> common complex coefficients are counterexample

characteristic-function Level-0 test
-> timing interpretation itself must satisfy positive-definite RF constraints

spatial first-passage semigroup
-> homogeneous scalar strong-Markov propagation is exponential in distance
-> three equally spaced spectral generation coordinates obey H2^2=H1 H3

optoelectronic-chromatic-dispersion prior-art collision
-> wavelength-dependent absorption depth and RF phase/amplitude are established
-> candidate contribution must be closure/falsification, not spectral dynamics alone

closure-failure hierarchy
-> trapping, relaxation, spatial nonlocality give distinct apparent-coefficient dispersion archetypes

stochastic occupation-time theorem
-> arbitrary successful paths + local clock perturbation
-> exact spatial occupation response and global RF derivative sum rule

occupation cumulant hierarchy
-> local mixed occupation/transit cumulants integrate to global timing cumulants of every order

CURRENT FRONTIER
-> audit detector-specific closure laws against primary prior art
-> build one clean HgCdTe worked example
-> calculate exact expected null residuals under drift-diffusion and alternatives
-> assess paper readiness only after those collisions.
```

---

## 5. Hard prior-art boundary

Do **not** claim novelty for

- photodiode transit-time-limited frequency response;
- wavelength-dependent absorption or generation depth;
- wavelength-dependent RF phase/timing/bandwidth;
- optoelectronic chromatic dispersion;
- photodiode carrier dynamics used for wavelength sensing/computational spectroscopy;
- multi-frequency photodiode RF characterization;
- algebraic inversion of modulated convection-diffusion profiles;
- characteristic-function positive-definiteness;
- Doob `h`-transforms / conditioned diffusion;
- occupation-time or Feynman-Kac mathematics;
- graded-HgCdTe transport acceleration;
- localized-position HgCdTe transit measurement.

Important current collisions:

```text
Glasser et al. 2021+:
optoelectronic chromatic dispersion from wavelength-dependent absorption depth

Kassa et al. 2026:
multi-frequency DC/RF amplitude/RF phase single-photodiode computational spectroscopy

Wang et al. 2014:
three-wavelength optical-receiver/photodiode phase-response characterization

Sattin / Escande et al.:
local algebraic convection-diffusion inversion from modulated profiles

2024 HgCdTe close collision:
Potential application of HgCdTe detector with composition gradient in laser measurement
DOI 10.5768/JAO202445.0310009
full technical content still unresolved.
```

The current candidate is the **integrated detector falsification ladder**, not any one known ingredient.

---

## 6. Level-0 timing null

If

```math
H(\omega)=E[e^{-i\omega T}],
```

then

```math
K_{jk}=H(\omega_j-\omega_k)\succeq0.
```

A simple two-harmonic consequence is

```math
\boxed{
|H(2\omega)-H(\omega)^2|
\le1-|H(\omega)|^2.
}
```

Failure means the de-embedded observable is not any positive classical timing distribution. Fix that before transport inference.

---

## 7. Level-1 spectral spatial-semigroup null

For scalar homogeneous continuous-path strong-Markov first passage,

```math
U_s(a+b)=U_s(a)U_s(b)
```

and therefore

```math
U_s(d)=e^{-\gamma_s d}.
```

A rigidly translated finite-width generation kernel preserves exponential dependence on its center.

Three wavelengths with equally spaced calibrated generation centers must obey

```math
\boxed{H_2^2=H_1H_3.}
```

This is currently the simplest detector-specific exact null prediction.

---

## 8. Level-2 real local Markov drift-diffusion closure

For

```math
D F''+wF'-i\omega F=0,
```

define

```math
r=\partial_z\ln F,
\qquad
A=r'+r^2.
```

At each nonsingular frequency,

```math
D_{app}
=-\omega\Re r/
(\Re A\Im r-\Im A\Re r),
```

```math
w_{app}
=\omega\Re A/
(\Re A\Im r-\Im A\Re r).
```

The exact physical closure is

```math
\boxed{
D_{app}(\omega)=\text{constant},
\qquad
w_{app}(\omega)=\text{constant}.
}
```

For `N` RF frequencies this yields `2(N-1)` real null conditions.

---

## 9. Minimal gedanken experiment

Inside a uniform segment, two generation depths give one complex propagation constant

```math
\gamma=a+ib.
```

One RF frequency determines

```math
D=\omega a/[b(a^2+b^2)],
```

```math
w=\omega(b^2-a^2)/[b(a^2+b^2)].
```

Positive downstream transport requires

```math
0<a<b.
```

A second RF frequency adds no parameter and is therefore a pure model test.

This is the preferred conceptual opening for any future manuscript.

---

## 10. Conditioning rule

For local Markov recombination with collection probability `h(z)`, DC normalization transforms the physical drift to

```math
\boxed{
w_{cond}=v+2D\partial_z\ln h.}
```

Do not interpret normalized RF `w` as the physical drift without the DC field.

---

## 11. Stochastic occupation/cumulant theorem

For arbitrary successful paths,

```math
\ell(z)=\int_0^T\delta(X_t-z)dt.
```

A point-like ideal local clock perturbation gives

```math
S(z,\omega)
=-i\omega A_h
E[e^{-i\omega T}\ell(z)]/H(\omega).
```

Exact sum rule:

```math
\boxed{
\int S dz
=A_h\omega\partial_\omega\ln H.
}
```

The frequency expansion spatially decomposes every timing cumulant:

```math
\int dz\,
\kappa(\ell(z),T,\ldots,T)
=\kappa_{n+1}(T).
```

This is a major theory target. Do not assume a real composition/electric-field perturbation is automatically a pure clock perturbation.

---

## 12. Statistical discipline

A closure failure must exceed propagated measurement/model covariance.

For `N` RF frequencies and apparent `(D,w)` pairs, generalized least-squares closure gives

```math
Q\sim\chi^2_{2N-2}
```

under the linearized Gaussian Markov null.

Use measured covariance when available; do not quote significance from raw parameter differences.

---

## 13. Numerical integrity

Every major exact/conditional theorem should have a deterministic numerical regression when feasible.

Current active regressions include

```text
numerics/transit_time_characteristic_function_null_tests.py
numerics/spatial_semigroup_three_color_test.py
numerics/three_color_spectral_geometric_mean_law.py
numerics/local_markov_real_closure_hierarchy.py
numerics/minimal_two_depth_two_frequency_gedanken.py
numerics/transport_closure_failure_archetypes.py
numerics/multifrequency_closure_statistical_test.py
numerics/spatial_derivative_bias_variance_resolution.py
numerics/stochastic_occupation_time_response_theorem.py
numerics/occupation_time_cumulant_hierarchy.py
numerics/translation_response_theorem.py
```

If a numerical script exposes a contradiction, correct the theorem/docs immediately and preserve the failed statement as superseded/invalidated.

---

## 14. HgCdTe role

Use HgCdTe as the primary **worked physical example** because a graded composition/bandgap can supply a strong wavelength-to-depth coordinate and because carrier transport physics is rich enough to challenge simple drift-diffusion.

Do not make the paper depend on a custom growth run or lab access.

The theoretical deliverable should be predictions such as

```text
three-color closure residual under a realistic x(z)
frequency dispersion expected from ordinary drift-diffusion
contrast with trapping/nonlocal models
required phase/log-magnitude precision for falsification.
```

Existing fabrication studies are only evidence that the gedanken coordinates are not obviously impossible.

---

## 15. Immediate forward work

Do **not** return to generic inverse algebra or fabrication optimization.

Priority:

1. finish targeted primary-source prior-art audits of the detector-specific closure/null laws;
2. derive realistic finite-kernel corrections to the three-color closure;
3. select one credible HgCdTe graded profile as a worked example;
4. predict the full null-test hierarchy under conventional drift-diffusion;
5. predict controlled violations under trapping, relaxation, and nonlocal alternatives;
6. calculate covariance/precision thresholds;
7. only then reassess manuscript readiness.

The paper, if it emerges, should be built from **simple falsifiable gedanken experiments**, not from a long numerical device-design story.
