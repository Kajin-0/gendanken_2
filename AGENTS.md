# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gendanken_2`  
**Active experiment:** `experiments/01-vanishing-absorber/`  
**Current mode:** **theory-first adversarial consolidation; strongest frontier is a Shockley-Ramo-aware spectral-depth closure hierarchy for falsifying photocarrier transport models; HgCdTe is the leading worked example; no novelty claim**

Read this file first.

The repository follows the physics rather than a predetermined paper. Failed conjectures, observable corrections, numerical corrections, counterexamples, and prior-art collisions are part of the result.

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
- **CANDIDATE DISTINCT APPLICATION — PRIORITY UNPROVEN**
- **INVALIDATED**
- **SUPERSEDED**
- **OPEN**
- **NON-CLAIM**

A negative literature search is not novelty evidence.

Do not use `first`, `new fundamental`, `universal`, etc. without a focused primary-source audit and claim-ledger update.

---

## 3. Canonical reading order

1. `experiments/01-vanishing-absorber/CURRENT_STATE.md`
2. `experiments/01-vanishing-absorber/PAPER_CORE_ADVERSARIAL_CONSOLIDATION.md`
3. `experiments/01-vanishing-absorber/PAPER_CLAIM_LEDGER.md`
4. `experiments/01-vanishing-absorber/SHOCKLEY_RAMO_OBSERVABLE_CORRECTION.md`
5. `experiments/01-vanishing-absorber/SHOCKLEY_RAMO_SURVIVAL_THEOREM.md`
6. `experiments/01-vanishing-absorber/RAMO_FOUR_COLOR_OPTICAL_ERROR_THEOREM.md`
7. `experiments/01-vanishing-absorber/RAMO_FOUR_COLOR_SLOWNESS_GRADIENT_THEOREM.md`
8. `experiments/01-vanishing-absorber/RAMO_FOUR_COLOR_SPACING_OPTIMUM.md`
9. `experiments/01-vanishing-absorber/FIVE_COLOR_BOUNDARY_ROOT_PAIR_CLOSURE.md`
10. `experiments/01-vanishing-absorber/HGCDTE_RAMO_FOUR_COLOR_GRADIENT_PREDICTION.md`
11. supporting `experiments/01-vanishing-absorber/THEORY_FALSIFICATION_LADDER.md`
12. supporting `experiments/01-vanishing-absorber/THEORY_CLAIM_LEDGER.md`
13. supporting `experiments/01-vanishing-absorber/SPATIAL_FIRST_PASSAGE_SEMIGROUP_THEOREM.md`
14. supporting `experiments/01-vanishing-absorber/LOCAL_MARKOV_TRANSPORT_CLOSURE_THEOREM.md`
15. supporting `experiments/01-vanishing-absorber/TRANSLATION_RESPONSE_THEOREM.md`
16. `experiments/01-vanishing-absorber/ARCHIVE_STATUS.md`
17. `experiments/01-vanishing-absorber/RESEARCH_LOG.md`
18. `experiments/01-vanishing-absorber/RESEARCH_LOG_2026-08-10_CONTINUATION.md`

Older fabrication/design and published-sample rescue files are provenance/supporting context.  Do not restart those branches unless an active theoretical prediction specifically requires a feasibility check.

---

## 4. Current scientific path

```text
vanishing-absorber thought experiment
-> universal detector-resource route repeatedly narrowed/killed

HgCdTe wavelength-depth branch
-> spectral generation coordinate

static spectral inverse
-> few-mode conditioning/contact gauge limits

purpose-built translated-gradient design
-> causal geometry improved
-> but fabrication optimization is not the research goal

THEORY-FIRST PIVOT
-> exact first-passage / RF transport closures

first-passage three-color semigroup theorem
-> mathematically valid for arrival/collection-flux observable

ADVERSARIAL OBSERVABLE CORRECTION
-> generic terminal photodiode current is not first-passage flux
-> Shockley-Ramo current is induced continuously
-> old direct terminal-current three-color law INVALIDATED

Shockley-Ramo survival theorem
-> in minimal planar one-carrier homogeneous geometry:
   J(d,s) proportional to [1-exp(-gamma d)]/s

four-color first-difference closure
-> first differences isolate one exponential spatial propagator
-> three points identify, fourth falsifies

second RF frequency
-> inferred real D,w must repeat
-> one RF identifies; the next tries to kill drift-diffusion

ordinary counterexamples
-> electron-hole pair breaks one-mode closure but has rank-two differences
-> finite boundary also rank two

RF root geometry
-> boundary: real constant root sum, imaginary linear root product
-> deterministic e/h: imaginary linear root sum, real quadratic root product

controlled nonuniform transport
-> low-RF four-color phase closure measures slowness-gradient combination

real optical source-shape evolution
-> leading variance error enters only through third discrete difference

statistics
-> four-color noise stencil (1,-3,3,-1)
-> sqrt(20) independent-noise amplification
-> cube-root spacing optimum

corrected HgCdTe worked example
-> mean depths 2.5/3.0/3.5/4.0 um
-> raw-Ramo gradient-sensitive phase excess ~-0.0124 deg @100 MHz
-> agrees with independent low-RF slowness-gradient theorem
```

---

## 5. Observable discipline — mandatory

Always state which response is being modeled.

### Arrival / collection-flux observable

```math
U(d,s)=E[e^{-sT_d}].
```

This is the natural object for

```text
first-passage semigroup
characteristic-function timing nulls
inverse-Gaussian first-passage cumulants
regenerative/subordinator timing theory.
```

### Raw planar terminal-current observable

Under the minimal Shockley-Ramo model,

```math
J(d,s)=C(s)[1-U(d,s)].
```

This is the active paper observable for the four-color finite-difference closure.

### DC-normalized terminal-current response

This is generally **not** the same spatial functional form as either object above.

Do not import arrival-time identities into a DC-normalized current transfer without deriving the signal-formation mapping explicitly.

---

## 6. Active headline nulls

### Four colors — one spatial terminal-current mode

For four equally spaced internal source coordinates,

```math
\boxed{
(J_2-J_1)^2
=(J_1-J_0)(J_3-J_2).
}
```

### One RF — infer the propagator

```math
q_s=(J_2-J_1)/(J_1-J_0),
```

```math
\gamma=-\ln q_s/h.
```

### Uniform real drift-diffusion

If

```math
D\gamma^2+w\gamma=i\omega,
```

then one RF gives

```math
D=\omega a/[b(a^2+b^2)],
```

```math
w=\omega(b^2-a^2)/[b(a^2+b^2)],
```

for `gamma=a+ib`.

### Second RF — no new parameter

```math
\boxed{
D(\omega_2)=D(\omega_1),
\qquad
w(\omega_2)=w(\omega_1).
}
```

### If one-mode closure fails

Use six source coordinates and test rank two in the **first differences** before adding exotic physics.

---

## 7. Major invalidations — never silently resurrect

### Generic terminal current equals first-passage characteristic function

**INVALIDATED.**

### Generic terminal-current three-color geometric-mean law

**INVALIDATED.**

### Direct inverse-Gaussian skewness/kurtosis null on arbitrary photocurrent waveform

**INVALIDATED AS A GENERIC OBSERVABLE CLAIM.**  The first-passage theorem remains valid for the arrival propagator/recovered propagation exponent.

### Earlier large HgCdTe three-color phase mainly measures the bulk gradient

**INVALIDATED / SUPERSEDED.**  A reflecting entrance boundary generated nearly all of that curvature.

### Rank two means a boundary

**INVALIDATED GENERALIZATION.**  A conventional electron-hole pair is already rank two.

### Three-frequency complex determinant alone proves one real DD generator

**INVALIDATED.**  Real per-frequency `D_app,w_app` closure is required.

---

## 8. Hard prior-art boundary

Do **not** claim novelty for

```text
Shockley-Ramo induced-current theory
photodiode impulse-response modeling
wavelength-dependent absorption/generation depth
wavelength-dependent photodiode RF phase/bandwidth
optoelectronic chromatic dispersion
multi-frequency photodiode characterization
frequency-domain drift-diffusion modeling
Prony/Hankel/system-identification mathematics
first-passage semigroups / inverse-Gaussian theory
algebraic convection-diffusion inversion
Doob/Feynman-Kac/occupation-time mathematics
graded-HgCdTe transport/high-speed response.
```

The current candidate is narrower:

```text
calibrated spectral internal source coordinate
+
Shockley-Ramo-aware spatial finite differences
+
minimal color-count model-order closure
+
RF root-algebra falsification of ordinary transport mechanisms.
```

**Status:** CANDIDATE DISTINCT APPLICATION — PRIORITY UNPROVEN.

Targeted negative searches are not priority evidence.

---

## 9. Current HgCdTe worked example

Use `HGCDTE_RAMO_FOUR_COLOR_GRADIENT_PREDICTION.md`, not the superseded boundary-confounded three-color prediction.

Current explicit stress:

```text
L=7.6 um
T=300 K
linear x=0.55 -> 0.32
mean generation depths = 2.5,3.0,3.5,4.0 um
lambda ~2.134651,2.215042,2.301173,2.393907 um
Pabs >0.9993
```

At `100 MHz`:

```text
variable raw-Ramo closure phase ~ -0.00993 deg
homogeneous same-optics floor ~ +0.00246 deg
gradient-sensitive excess ~ -0.01238 deg
point-source slowness-gradient theorem ~ -0.01254 deg.
```

This is a consistency stress, not a calibrated device prediction.

---

## 10. What is demoted from the headline paper

Keep, but do not let these dominate the current manuscript path:

```text
arbitrary-profile derivative inversion
occupation-time/local-clock spectroscopy
full Levy delay-spectrum reconstruction
translated-gradient fabrication optimization
published sample-A/B rescue calculations.
```

They can become appendices or follow-up papers if needed.

---

## 11. Next decisive work

Do **not** add unrelated general mathematics.

Priority:

1. focused primary-source audit for exact equal-internal-depth four-/six-color finite-difference closure protocols;
2. derive the stochastic Shockley-Ramo current closure beyond the minimal half-line/uniform model and identify which assumptions preserve finite spatial rank;
3. propagate generated-carrier-amplitude calibration and wavelength-dependent external-chain errors;
4. stress the HgCdTe quartet one ordinary effect at a time: finite diffusion, recombination, second carrier, finite boundary;
5. quantify whether the model hierarchy remains separable at realistic covariance;
6. only then produce a manuscript outline.

The objective is not to maximize the number of claims.  It is to end with the smallest set of exact predictions that a skeptical reviewer cannot dismiss as an observable mismatch, uncontrolled conventional effect, or rediscovery of known photodiode response physics.
