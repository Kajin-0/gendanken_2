# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gendanken_2`  
**Active experiment:** `experiments/01-vanishing-absorber/`  
**Current mode:** **working theory manuscript + adversarial revision; strongest result is a Shockley-Ramo-aware spectral-depth closure hierarchy for falsifying photocarrier transport models; HgCdTe is the leading worked example; priority remains unproven**

Read this file first.

## CRITICAL: privacy / pseudonymity lock

**Pseudonymity is the default and identifying information is opt-in.** Never insert or restore a legal name, personal email, phone number, street address, precise personal location, employer/affiliation, signature, identifying account handle, or other identifying metadata into a manuscript, repository file, public artifact, PDF metadata, or release unless the user explicitly approves that specific disclosure.

Do not infer disclosure permission from account/profile information, prior files, git history, memory, authorship conventions, or the fact that identifying information appeared previously. Previous disclosure is not continuing consent.

For manuscripts and generated PDFs, the default author and PDF-author metadata are `Anonymous` unless the user explicitly chooses a pseudonym or author identity for that artifact. **A real identity must never become the canonical baseline by default.**

If identity disclosure is explicitly requested, follow `PRIVACY_PROTOCOL.md` and record only the minimum approved disclosure. Scientific preservation and identity disclosure are separate decisions.

The repository follows the physics rather than a predetermined paper. Failed conjectures, observable corrections, numerical corrections, counterexamples, and prior-art collisions are part of the result.

**A working manuscript exists. The canonical pre-geometry manuscript is the recovered 16-page Rev. 3 by Anonymous. It is not submission-ready.**

## CRITICAL: manuscript preservation lock

Before any manuscript edit, read these files in order:

1. `experiments/01-vanishing-absorber/MANUSCRIPT_CURRENT.md`
2. `experiments/01-vanishing-absorber/MANUSCRIPT_BASELINE.md`
3. `experiments/01-vanishing-absorber/MANUSCRIPT_PRESERVATION_PROTOCOL.md`
4. `experiments/01-vanishing-absorber/CURRENT_STATE_LIVE.md`
5. the exact verified manuscript source recovered with `python tools/extract_manuscript_baseline.py` when manuscript work is required.

**Do not treat `MANUSCRIPT_DRAFT.tex`, `MANUSCRIPT_DRAFT.md`, the older `CURRENT_STATE.md`, this file's historical summaries, or an agent handoff as a substitute for the exact current manuscript.**

The immutable Rev. 3 source is stored inside the repository as hash-verified split snapshot parts under `experiments/01-vanishing-absorber/manuscript_history/`. The extractor verifies both the compressed snapshot and decompressed source before writing `MANUSCRIPT_CURRENT.tex`.

The mandatory default is:

> **Preserve first; integrate second; rewrite only when explicitly requested by the user.**

Integrating a theorem, simulation, reviewer response, correction, or counterexample does **not** authorize opportunistic compression or restructuring of unrelated manuscript material.

Any manuscript-changing PR must run `tools/check_manuscript_preservation.py`. The check is designed to stop accidental section/subsection/reference/equation loss, unexpected author/title changes, large line-count shrinkage, and large replacement of established source. A destructive rewrite may bypass the guard only when the current user explicitly requested a large rewrite and the repository contains the required verbatim-user-quote justification defined in `MANUSCRIPT_PRESERVATION_PROTOCOL.md`.

A handoff summary is navigation only. **It is never source-of-truth manuscript content.**

Current manuscript/state sources:

- `experiments/01-vanishing-absorber/MANUSCRIPT_CURRENT.md`
- `experiments/01-vanishing-absorber/MANUSCRIPT_BASELINE.md`
- `experiments/01-vanishing-absorber/MANUSCRIPT_PRESERVATION_PROTOCOL.md`
- `experiments/01-vanishing-absorber/CURRENT_STATE_LIVE.md`
- `experiments/01-vanishing-absorber/PAPER_CLAIM_LEDGER.md`
- newer claim-ledger addenda and theorem/result files as dated.

Historical manuscript sources retained for provenance:

- `experiments/01-vanishing-absorber/MANUSCRIPT_DRAFT.md`
- `experiments/01-vanishing-absorber/MANUSCRIPT_DRAFT.tex`
- `experiments/01-vanishing-absorber/MANUSCRIPT_REFERENCES.bib`
- `experiments/01-vanishing-absorber/SUPPLEMENTARY_MATERIAL.md`

The main task is now **adversarial manuscript revision, proof consolidation, numerical reproducibility, realistic-geometry/transport falsification, and narrow priority audit**, not broad new theorem generation.

---

## 1. Mandatory repository protocol

Before every write:

1. fetch live `main` / current target;
2. inspect intervening changes when needed;
3. fetch the exact current blob SHA before replacing a file;
4. never overwrite stale state;
5. preserve failed/corrected branches and why they failed;
6. make narrow edits where practical;
7. update canonical state when the scientific frontier changes;
8. for manuscript work, recover/verify the exact current manuscript and run the preservation guard before merge.

**Live `main` overrides snapshots and recovery notes except that an explicitly designated immutable manuscript baseline must be recovered through its recorded hash-verified repository snapshot rather than reconstructed from an older `main` draft.**

Do not delete an old scientific result merely because it was superseded. Mark it explicitly and preserve why the direction changed.

Do not make manuscript changes directly on `main`; use a branch/PR so the preservation check and full diff can be inspected.

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

1. `experiments/01-vanishing-absorber/MANUSCRIPT_CURRENT.md`
2. `experiments/01-vanishing-absorber/MANUSCRIPT_BASELINE.md`
3. `experiments/01-vanishing-absorber/MANUSCRIPT_PRESERVATION_PROTOCOL.md`
4. `experiments/01-vanishing-absorber/CURRENT_STATE_LIVE.md`
5. `experiments/01-vanishing-absorber/PAPER_CLAIM_LEDGER.md`
6. `experiments/01-vanishing-absorber/PAPER_CLAIM_LEDGER_REV3_GEOMETRY_ADDENDUM_2026-08-11.md` when present
7. `experiments/01-vanishing-absorber/REALISTIC_GEOMETRY_CLOSURE_STRESS.md` when present
8. `experiments/01-vanishing-absorber/MANUSCRIPT_BLUEPRINT_ADVERSARIAL.md`
9. `experiments/01-vanishing-absorber/SUPPLEMENTARY_MATERIAL.md`
10. `experiments/01-vanishing-absorber/SHOCKLEY_RAMO_OBSERVABLE_CORRECTION.md`
11. `experiments/01-vanishing-absorber/SHOCKLEY_RAMO_SURVIVAL_THEOREM.md`
12. `experiments/01-vanishing-absorber/RAMO_FOUR_COLOR_OPTICAL_ERROR_THEOREM.md`
13. `experiments/01-vanishing-absorber/RAMO_FOUR_COLOR_SLOWNESS_GRADIENT_THEOREM.md`
14. `experiments/01-vanishing-absorber/RAMO_FOUR_COLOR_SPACING_OPTIMUM.md`
15. `experiments/01-vanishing-absorber/HGCDTE_RAMO_FOUR_COLOR_GRADIENT_PREDICTION.md`
16. supporting theory files only as needed.

When manuscript work is requested, recover the exact verified `MANUSCRIPT_CURRENT.tex` before editing it. The old `MANUSCRIPT_DRAFT.*` and `CURRENT_STATE.md` remain provenance only.

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

The newer realistic-geometry stress reinforces the interpretation order:

```text
four colors -> detect one-mode failure
six colors  -> determine whether another spatial mode is resolved
RF roots    -> test ordinary mechanism laws
only then   -> assign a mechanism-specific transport interpretation
```

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

### A four-color phase residual uniquely identifies a transport gradient

**INVALIDATED GENERALIZATION.** The realistic finite-electrode/depletion stress can generate an order-unity fraction of the current one-dimensional gradient target. Model order and geometry must be controlled before mechanism assignment.

### Five-color polynomial annihilation removes arbitrary detector geometry

**INVALIDATED GENERALIZATION.** It remains exact for the stated one-dimensional polynomial observation forcing, not for an arbitrary curved multidimensional weighting potential with bent trajectories.

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

The realistic 2-D hardening calculation now supplies an additional ordinary-device confound. For the representative 75%-contact + 3 um depletion-like stress, the geometry/depletion excess over the planar same-optics baseline is approximately:

```text
100 MHz -> -0.008841 deg = 0.738 x current 1-D gradient target
500 MHz -> -0.045827 deg = 0.780 x target
1 GHz   -> -0.095513 deg = 0.865 x target
```

This geometry family is **CHECKED / CONDITIONAL**, not a calibrated device simulation and not a theorem for arbitrary geometry. At 100 MHz its second spatial mode becomes nominally detectable around `84.6 dB` current-step amplitude SNR, below the present `96.1 dB` gradient-specific requirement, and its fitted effective rank-two roots fail the homogeneous finite-boundary root-sum law.

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

Do **not** reopen broad exploratory theory unless manuscript review or realistic-device falsification exposes a genuine missing theorem.

Priority now:

1. preserve the exact 16-page Rev. 3 source and keep the manuscript-preservation guard passing;
2. keep the realistic 2-D geometry result as a separate auditable hardening result until it is surgically integrated into the exact manuscript;
3. continue the narrow primary-source priority audit for the exact spectral-depth four-/six-color closure construction;
4. advance the geometry attack to one plausible self-consistent 2-D semiconductor Poisson/drift-diffusion structure with diffusion and analyze the synthetic spectral/RF data blindly using the same hierarchy;
5. convert independent numerical checks into reproducibility tables / supplement material;
6. only after these pass, choose a target journal and adapt formatting.

The objective is the smallest set of exact, falsifiable predictions that a skeptical reviewer cannot dismiss as an observable mismatch, an uncontrolled ordinary mechanism, a geometry artifact, or rediscovery of known photodiode response physics.
