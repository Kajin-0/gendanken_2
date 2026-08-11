# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gendanken_2`  
**Active experiment:** `experiments/01-vanishing-absorber/`  
**Current mode:** **working theory manuscript + adversarial revision; strongest result is a Shockley-Ramo-aware spectral-depth closure hierarchy for falsifying photocarrier transport models; HgCdTe is the leading worked example; priority remains unproven**

Read this file first.

The repository follows the physics rather than a predetermined paper. Failed conjectures, observable corrections, numerical corrections, counterexamples, and prior-art collisions are part of the result.

**A working manuscript now exists. It is not submission-ready.**

Main sources:

- `experiments/01-vanishing-absorber/MANUSCRIPT_DRAFT.md`
- `experiments/01-vanishing-absorber/MANUSCRIPT_DRAFT.tex`
- `experiments/01-vanishing-absorber/MANUSCRIPT_REFERENCES.bib`
- `experiments/01-vanishing-absorber/SUPPLEMENTARY_MATERIAL.md`

The main task is now **adversarial manuscript revision, proof consolidation, numerical reproducibility, and narrow priority audit**, not broad new theorem generation.

---

## 1. Mandatory repository protocol

Before every write:

1. fetch live `main` / current target;
2. inspect intervening changes when needed;
3. fetch the exact current blob SHA before replacing a file;
4. never overwrite stale state;
5. preserve failed/corrected branches and why they failed;
6. make narrow edits where practical;
7. update canonical state when the scientific frontier changes.

**Live `main` overrides snapshots and recovery notes.**

Do not delete an old scientific result merely because it was superseded. Mark it explicitly and preserve why the direction changed.

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

Do not use `first`, `new fundamental`, `universal`, `novel`, etc. without a focused primary-source audit and claim-ledger update.

---

## 3. Canonical reading order

1. `experiments/01-vanishing-absorber/MANUSCRIPT_DRAFT.md`
2. `experiments/01-vanishing-absorber/PAPER_CLAIM_LEDGER.md`
3. `experiments/01-vanishing-absorber/MANUSCRIPT_BLUEPRINT_ADVERSARIAL.md`
4. `experiments/01-vanishing-absorber/SUPPLEMENTARY_MATERIAL.md`
5. `experiments/01-vanishing-absorber/CURRENT_STATE.md`
6. `experiments/01-vanishing-absorber/SHOCKLEY_RAMO_OBSERVABLE_CORRECTION.md`
7. `experiments/01-vanishing-absorber/SHOCKLEY_RAMO_SURVIVAL_THEOREM.md`
8. `experiments/01-vanishing-absorber/RAMO_FOUR_COLOR_OPTICAL_ERROR_THEOREM.md`
9. `experiments/01-vanishing-absorber/RAMO_FOUR_COLOR_SLOWNESS_GRADIENT_THEOREM.md`
10. `experiments/01-vanishing-absorber/RAMO_FOUR_COLOR_SPACING_OPTIMUM.md`
11. `experiments/01-vanishing-absorber/HGCDTE_RAMO_FOUR_COLOR_GRADIENT_PREDICTION.md`
12. supporting theory files only as needed.

Older fabrication/design and published-sample rescue files are provenance/supporting context. Do not restart those branches unless an active manuscript claim specifically requires a feasibility check.

---

## 4. Current paper spine

The paper should remain organized around three simple gedanken experiments.

### Gedanken I — four colors

Choose four wavelengths corresponding to four equally spaced internal source coordinates. In the minimal homogeneous one-carrier planar Shockley-Ramo model,

```math
\boxed{(J_2-J_1)^2=(J_1-J_0)(J_3-J_2).}
```

Three source coordinates identify one spatial multiplier. The fourth is a parameter-free null measurement.

### Gedanken II — DC + RF

Recover the spatial exponent `gamma` from the four-color sequence. Uniform real drift-diffusion-recombination obeys

```math
D\gamma^2+w\gamma=\kappa+s.
```

DC plus one nonzero RF determine `D,w,kappa`. Every additional RF frequency is a falsification point because it introduces no new material parameter.

Conceptual statement:

> **DC + one RF identify the minimal model; the next RF tries to kill it.**

### Gedanken III — six colors

If the one-mode closure fails, use six source coordinates and test whether exactly two first-difference spatial modes are resolved.

For

```math
d_m=a q_1^m+b q_2^m,
```

```math
\boxed{W_m=d_md_{m+2}-d_{m+1}^2
=ab(q_1q_2)^m(q_1-q_2)^2.}
```

A second mode must be statistically resolved before roots are interpreted. Finite boundaries and conventional electron-hole transport then have different RF root constraints.

---

## 5. Observable discipline — mandatory

Always state which response is being modeled.

### Arrival / collection-flux observable

```math
U(d,s)=E[e^{-sT_d}].
```

This is exponential in propagation distance for the homogeneous scalar first-passage semigroup.

### Raw planar terminal-current observable

Under the minimal Shockley-Ramo geometry,

```math
\boxed{J(d,s)=C(s)[1-U(d,s)]}
```

(up to the conventional `1/s` factor absorbed into `C`).

This is the active manuscript observable.

### DC-normalized terminal-current response

This is generally **not** the same spatial functional form as either object above.

Never import arrival-time identities into terminal current without deriving the signal-formation mapping.

---

## 6. Major invalidations — never silently resurrect

### Generic terminal current equals first-passage characteristic function

**INVALIDATED.** Shockley-Ramo current is induced continuously.

### Generic terminal-current three-color geometric-mean law

**INVALIDATED.** A deterministic rectangular induced-current pulse is a counterexample. The corrected raw-current null uses four source coordinates and first differences.

### Direct inverse-Gaussian skewness/kurtosis null on arbitrary photocurrent waveform

**INVALIDATED AS A GENERIC OBSERVABLE CLAIM.** The first-passage mathematics remains valid for the arrival propagator/recovered propagation exponent.

### Earlier large HgCdTe three-color phase mainly measures the bulk gradient

**INVALIDATED / SUPERSEDED.** A reflecting entrance boundary generated nearly all of that curvature.

### Rank two means a boundary

**INVALIDATED GENERALIZATION.** A conventional electron-hole pair is already rank two.

### Three-frequency complex determinant alone proves one real DD generator

**INVALIDATED.** Real multi-frequency coefficient/root closure is required.

---

## 7. Current HgCdTe worked example

Use the corrected raw-Ramo four-color stochastic calculation, not the superseded boundary-confounded three-color result.

Explicit stress:

```text
L = 7.6 um
T = 300 K
linear x = 0.55 -> 0.32
mean generation depths = 2.5, 3.0, 3.5, 4.0 um
lambda ~ 2.134651, 2.215042, 2.301173, 2.393907 um
Pabs > 0.9993
```

For no recombination, gradient-sensitive closure phase is approximately

```text
100 MHz -> -0.011978 deg
500 MHz -> -0.058727 deg
1 GHz   -> -0.110405 deg
```

The point-source low-RF slowness-gradient result gives approximately `-0.01254 deg` at 100 MHz.

The stochastic calculation has been independently reproduced with an adaptive shooting construction to approximately `10^-6 degree` agreement or better at the reported RF points.

These are **conditional theory predictions**, not calibrated forecasts for an existing detector.

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
Shockley-Ramo-aware spatial first differences
+
minimal four-/six-color model-order closure
+
RF root-algebra falsification of ordinary photocarrier transport mechanisms.
```

**Status:** CANDIDATE DISTINCT APPLICATION — PRIORITY UNPROVEN.

Targeted negative searches are not priority evidence.

---

## 9. What is demoted from the headline manuscript

Keep as supporting theory/provenance, but do not let these dominate the main paper:

```text
arbitrary-profile derivative inversion
occupation-time/local-clock spectroscopy
full Levy delay-spectrum reconstruction
translated-gradient fabrication optimization
published sample-A/B rescue calculations.
```

They can become supplement material or follow-up papers only if they materially support the reduced manuscript.

---

## 10. Next decisive work

Do **not** reopen broad exploratory theory unless manuscript review exposes a genuine missing theorem.

Priority now:

1. compile/QA the LaTeX manuscript and synchronize any build fixes back to the repository;
2. keep main-text proofs concise and move long derivations to `SUPPLEMENTARY_MATERIAL.md`;
3. continue the narrow primary-source priority audit for the exact spectral-depth four-/six-color closure construction;
4. stress the surviving claims against nonuniform weighting fields and depletion-region signal formation;
5. convert the independent numerical checks into a reproducibility table / supplement section;
6. only after these pass, choose a target journal and adapt formatting.

The objective is the smallest set of exact, falsifiable predictions that a skeptical reviewer cannot dismiss as an observable mismatch, an uncontrolled ordinary mechanism, or rediscovery of known photodiode response physics.
