# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gendanken_2`  
**Active experiment:** `experiments/01-vanishing-absorber/`  
**Current mode:** **anonymous Rev. 7 working theory manuscript + adversarial revision; strongest result is a Shockley-Ramo-aware spectral-depth closure hierarchy for falsifying photocarrier transport models; HgCdTe is a conditional scaling/stress example; priority remains unproven**

Read this file first.

## CRITICAL: privacy / pseudonymity lock

**Pseudonymity is the default and identifying information is opt-in.** Never insert or restore a legal name, personal email, phone number, street address, precise personal location, employer/affiliation, signature, identifying account handle, or other identifying metadata into a manuscript, repository file, public artifact, PDF metadata, or release unless the user explicitly approves that specific disclosure.

Do not infer disclosure permission from account/profile information, prior files, git history, memory, authorship conventions, or the fact that identifying information appeared previously. Previous disclosure is not continuing consent.

For manuscripts and generated PDFs, the default author and PDF-author metadata are `Anonymous` unless the user explicitly chooses a pseudonym or author identity for that artifact. **A real identity must never become the canonical baseline by default.**

If identity disclosure is explicitly requested, follow `PRIVACY_PROTOCOL.md` and record only the minimum approved disclosure. Scientific preservation and identity disclosure are separate decisions.

The repository follows the physics rather than a predetermined paper. Failed conjectures, observable corrections, numerical corrections, counterexamples, and prior-art collisions are part of the result.

**A working manuscript exists. The canonical manuscript is the anonymous 24-page Rev. 7, validated against the previous Rev. 6 baseline before canonicalization. It is not yet submission-ready; the exact closest-source priority audit and experimental-feasibility attack remain open.**

## CRITICAL: manuscript preservation lock

Before any manuscript edit, read these files in order:

1. root `PRIVACY_PROTOCOL.md`;
2. `experiments/01-vanishing-absorber/MANUSCRIPT_CURRENT.md`;
3. `experiments/01-vanishing-absorber/MANUSCRIPT_BASELINE.md`;
4. `experiments/01-vanishing-absorber/MANUSCRIPT_PRESERVATION_PROTOCOL.md`;
5. `experiments/01-vanishing-absorber/CURRENT_STATE_LIVE.md`;
6. `experiments/01-vanishing-absorber/REV5_ADVERSARIAL_CORRECTIONS_2026-08-11.md`;
7. `experiments/01-vanishing-absorber/REV4_ADVERSARIAL_CORRECTIONS_2026-08-11.md` as predecessor context;
8. the exact verified manuscript source recovered with `python tools/extract_manuscript_baseline.py` when manuscript work is required.

**Do not treat `MANUSCRIPT_DRAFT.tex`, `MANUSCRIPT_DRAFT.md`, the older `CURRENT_STATE.md`, the historical Rev. 3 snapshot, this file's summaries, or an agent handoff as a substitute for the exact current manuscript.**

The immutable Rev. 7 source is stored inside the repository as hash-verified split snapshot parts under `experiments/01-vanishing-absorber/manuscript_history/`. The extractor verifies both the compressed snapshot and decompressed source before writing `MANUSCRIPT_CURRENT.tex`.

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
- `experiments/01-vanishing-absorber/REV7_ADVERSARIAL_CORRECTIONS_2026-08-11.md`
- `experiments/01-vanishing-absorber/MANUSCRIPT_REV7_PRESERVATION_REPORT_2026-08-11.md`
- `experiments/01-vanishing-absorber/REV6_ADVERSARIAL_CORRECTIONS_2026-08-11.md`
- `experiments/01-vanishing-absorber/MANUSCRIPT_REV6_PRESERVATION_REPORT_2026-08-11.md`
- `experiments/01-vanishing-absorber/REV5_ADVERSARIAL_CORRECTIONS_2026-08-11.md`
- `experiments/01-vanishing-absorber/MANUSCRIPT_REV5_PRESERVATION_REPORT_2026-08-11.md`
- `experiments/01-vanishing-absorber/REV4_ADVERSARIAL_CORRECTIONS_2026-08-11.md`
- `experiments/01-vanishing-absorber/MANUSCRIPT_REV4_PRESERVATION_REPORT_2026-08-11.md`
- `experiments/01-vanishing-absorber/PAPER_CLAIM_LEDGER.md`
- newer claim-ledger addenda and theorem/result files as dated.

Historical manuscript sources retained for provenance:

- anonymous Rev. 3 snapshot under `manuscript_history/`;
- `experiments/01-vanishing-absorber/MANUSCRIPT_DRAFT.md`;
- `experiments/01-vanishing-absorber/MANUSCRIPT_DRAFT.tex`;
- `experiments/01-vanishing-absorber/MANUSCRIPT_REFERENCES.bib`;
- `experiments/01-vanishing-absorber/SUPPLEMENTARY_MATERIAL.md`.

The main task is now **adversarial manuscript revision, proof consolidation, numerical reproducibility, realistic-device falsification, and narrow priority audit**, not broad new theorem generation.

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

**Live `main` overrides snapshots and recovery notes except that an explicitly designated immutable manuscript baseline must be recovered through its recorded hash-verified repository snapshot rather than reconstructed from an older draft.**

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

**REV. 7 submission blockers:** the closest-looking 2024 graded-HgCdTe paper has verified bibliographic metadata but its exact full text has not yet been lawfully recovered and audited. That exact-source audit remains OPEN and blocks submission-level priority/novelty claims. Related-paper searches do not substitute for reading it.

Do not use `first`, `new fundamental`, `universal`, `novel`, etc. without a focused primary-source audit and claim-ledger update.

---

## 3. Canonical reading order

1. `PRIVACY_PROTOCOL.md`
2. `experiments/01-vanishing-absorber/MANUSCRIPT_CURRENT.md`
3. `experiments/01-vanishing-absorber/MANUSCRIPT_BASELINE.md`
4. `experiments/01-vanishing-absorber/MANUSCRIPT_PRESERVATION_PROTOCOL.md`
5. `experiments/01-vanishing-absorber/CURRENT_STATE_LIVE.md`
6. `experiments/01-vanishing-absorber/REV7_ADVERSARIAL_CORRECTIONS_2026-08-11.md`
7. `experiments/01-vanishing-absorber/REV6_ADVERSARIAL_CORRECTIONS_2026-08-11.md`
8. `experiments/01-vanishing-absorber/REV5_ADVERSARIAL_CORRECTIONS_2026-08-11.md`
7. `experiments/01-vanishing-absorber/REV4_ADVERSARIAL_CORRECTIONS_2026-08-11.md`
8. `experiments/01-vanishing-absorber/PAPER_CLAIM_LEDGER.md`
8. `experiments/01-vanishing-absorber/PAPER_CLAIM_LEDGER_REV3_GEOMETRY_ADDENDUM_2026-08-11.md` when present
9. `experiments/01-vanishing-absorber/REALISTIC_GEOMETRY_CLOSURE_STRESS.md` when present
10. `experiments/01-vanishing-absorber/MANUSCRIPT_BLUEPRINT_ADVERSARIAL.md`
11. `experiments/01-vanishing-absorber/SUPPLEMENTARY_MATERIAL.md`
12. supporting theorem files only as needed.

When manuscript work is requested, recover the exact verified `MANUSCRIPT_CURRENT.tex` before editing it. The old `MANUSCRIPT_DRAFT.*`, Rev. 3 snapshot, and `CURRENT_STATE.md` remain provenance only.

---

## 4. Current paper spine

The paper remains organized around three simple gedanken experiments.

### Gedanken I — four colors

Choose four wavelengths corresponding to four equally spaced internal source coordinates. In the minimal homogeneous one-carrier planar Shockley-Ramo model,

```math
\boxed{(J_2-J_1)^2=(J_1-J_0)(J_3-J_2).}
```

Three source coordinates identify one spatial multiplier `q`. The fourth is a parameter-free null measurement.

**Important branch qualification, retained in Rev. 6:** this four-color null is a statement in `q`-space and is branch-independent. Converting

```math
q=e^{-\gamma h}
```

to a continuous exponent has the branch family

```math
\gamma_n=-\frac{\operatorname{Log}q+2\pi i n}{h}.
```

Physical inversion to `D,w,kappa` is therefore conditional on a uniquely selected spatial-logarithm branch. A sufficient principal-branch anti-alias condition is

```math
|\operatorname{Im}\gamma|h<\pi.
```

Do **not** resurrect the unrestricted statement that one measured `q` globally determines a unique `gamma`.

### Gedanken II — DC + RF

Uniform real drift-diffusion-recombination obeys

```math
D\gamma^2+w\gamma=\kappa+s.
```

Conditional on a uniquely selected spatial-log branch, DC plus one nonzero RF structurally determine `D,w,kappa`. Every additional RF frequency introduces no new material parameter and is therefore a falsification point.

Conceptual statement, with the qualification kept explicit:

> **After branch selection, DC + one RF identify the minimal model; the next RF tries to kill it.**

### Gedanken III — six colors and higher order

If the one-mode closure fails, use six source coordinates and test whether two first-difference spatial modes are resolved.

For

```math
d_m=a q_1^m+b q_2^m,
```

```math
\boxed{W_m=d_md_{m+2}-d_{m+1}^2
=ab(q_1q_2)^m(q_1-q_2)^2.}
```

A second mode must be statistically resolved before roots are interpreted.

**REV. 6 qualification:** rank detection is only the first threshold. A resolved second mode must also have sufficiently precise recurrence parameters before physical root-law discrimination. For `P=W_1/W_0=q_1q_2`, the optimistic independent equal-significance limit gives `sigma_P/|P| ~ sqrt(2)/Z`, so `Z=3` still implies about 47.1% relative product uncertainty. Operational order: **rank detection -> parameter resolution -> physical-law discrimination**. Algebraic branch immunity is not statistical robustness. Degeneracies can reduce observable rank, so use **rank at most two** when referring to the general two-mode mechanism.

Failure of rank two does **not** imply exotic transport. Continue through higher ordinary finite-rank mechanisms before richer/nonlocal interpretations.

The interpretation order is:

```text
rank 1 / four colors
-> rank 2 / six colors if resolved
-> higher ordinary finite rank if needed
-> RF root-law constraints
-> only then mechanism-specific or richer/nonlocal interpretation
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

## 6. Rev. 4/5/6 mathematical boundary conditions — never regress

### Spatial-log branch ambiguity

**CORRECTED IN REV. 4.** The multiplier `q` is measured; `gamma` is multi-valued modulo `2 pi i/h`. Positivity of fitted `D,w` alone does not guarantee the correct branch. Use anti-alias bounds, continuity, additional RF points, or spatial design to select a branch.

### Known arbitrary spacing

**CORRECTED IN REV. 4.** The first three positions constrain one or more candidate roots of the unequal-spacing equation; they do not generically guarantee uniqueness. The fourth position filters candidates. Claim unique physical inversion only when one admissible candidate remains after all constraints.

### Rank-two branch/permutation discipline and low-RF observation-mode boundary

**ADDED IN REV. 5.** For a homogeneous finite-boundary scalar rank-two model, test the branch-free multiplier product first:

```math
q_+q_-=e^{(r_++r_-)h}=e^{-wh/D}\in\mathbb R_{>0},
```

and require it to be RF-independent. Only after this check should the two logarithmic root branches be unwrapped. Branch integers and root pairing/permutation across frequency must be fixed by independent physical bounds, multiple spacings when available, and continuity; never choose them merely to make a mechanism law pass.

Also retain the Rev. 5 low-RF resolution boundary: a linear weighting-field mode has `q_weight=1` while `q_transport -> 1` as RF tends to zero. The rank-two witness therefore collapses quadratically. On the manuscript scale the optimistic equal-mode 3-sigma separation requirement is about `116.2 / 88.4 / 76.7 dB` at `100 / 500 / 1000 MHz`; the complementary five-color annihilation cost is about `46.3 / 32.3 / 26.4 dB`. Neither defense is free at low RF.

### Linear weighting field and polynomial annihilation

For

```math
DJ''+wJ'-(\kappa+s)J=-[wE_w+DE_w'],
```

when `kappa+s != 0`, a polynomial forcing of degree `p` has a particular solution of the same degree. For a linear weighting field this gives the ordinary `q_weight=1` observation mode and a five-color/second-difference exact annihilation construction.

At the singular point

```text
s=0, kappa=0, w>0
```

the particular degree generically rises by one. For `E_w=E_0+E_1 z`,

```math
J_p=-E_0z-\frac{E_1}{2}z^2.
```

A linear field therefore requires **third differences / six colors** for exact polynomial annihilation at the singular DC/no-recombination point. Do not apply the five-color theorem there.

**REV. 6 interpretation lock:** prescribed one-dimensional `E_w(z)` is an effective observation-operator surrogate, not a generic self-consistent finite-pixel electrostatic geometry. Real finite-electrode nonuniformity generally requires multidimensional electrostatics and lateral trajectories.

---

## 6A. Rev. 7 scientific locks — never regress

### Adversarial-review discipline

A hostile referee report is **evidence and an attack vector, not authority or a task list**. Independently determine whether each objection is mathematically correct, physically relevant in the stated regime, numerically supported, and within scope. Then explicitly classify it as accepted, narrowed, rejected, useful stress test, or out-of-scope. Do not overcorrect a valid but limited criticism, and do not defend an invalid manuscript claim merely because it is already in the paper.

### Classical finite-exponential attribution

The geometric one-mode identity and two-mode Hankel/Casoratian identities belong to the classical Prony/ESPRIT/matrix-pencil family. Never imply that those algebraic identities themselves are novel. The candidate distinction is the detector-specific construction that creates and physically constrains the spatial sequence.

### HgCdTe force baseline

The current headline worked stress uses the 2025 electron-affinity relation

```math
chi(x)=5.32+0.45x-E_g(x,300 K)
```

and therefore

```math
E_{drive}^{grad}=|(dE_g/dx-0.45)dx/dz|,
```

with `xi_e~0.666--0.695` for the worked `x=0.55 -> 0.32` profile. The historical `xi=1` calculation is a sensitivity case, not the canonical Rev. 7 HgCdTe baseline.

Canonical finite-width gradient-sensitive phase stresses are approximately `-0.0220167 / -0.1064448 / -0.1942321 degree` at 100 / 500 / 1000 MHz.

### Recombination interpretation

Do not repeat the false statement that nonlinear Auger recombination is intrinsically incompatible with a first-order small-signal `kappa`. A nonlinear recombination law can be linearized around an operating point; the graded-material issue is the resulting spatially varying differential rate.

The Rev. 7 deliberately steep 5-us-anchored recombination profile changes the closure by less than `4e-7 degree` over 0.1--1 GHz in the specified conditional stress. This does **not** establish negligible recombination for high injection, depletion, every composition profile, or every detector architecture.

### Current experimental/resource scales

Use the Rev. 7 propagated scales, not Rev. 5/6 values: conditioning optimum about `5.85 GHz`; optimistic weighting-mode rank-two separation about `108.6 / 81.2 / 70.5 dB`; five-color penalty about `42.4 / 28.7 / 23.2 dB`; 3-sigma current-step SNR `90.9 / 82.9 / 77.1 / 71.4 dB` at 100/250/500/1000 MHz; nonaffine coordinate RMS about `4.5 nm`; irregular phase RMS `1.88e-4 / 9.15e-4 / 1.71e-3 degree` at 100/500/1000 MHz.

The proposed common-reference/interleaved-wavelength coherent architecture is **not demonstrated feasibility**. Residual spectral-phase/depth and baseline-covariance performance remain open experimental requirements.

---

## 7. Major invalidations — never silently resurrect

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

**INVALIDATED GENERALIZATION.** Geometry, weighting field, source-state evolution, and other ordinary mechanisms can produce closure failure. Model order and observation geometry must be controlled before mechanism assignment.

### Five-color polynomial annihilation removes arbitrary detector geometry

**INVALIDATED GENERALIZATION.** It applies to the stated one-dimensional polynomial observation forcing under the corrected degree conditions, not arbitrary curved multidimensional geometry.

### Five colors always annihilate a linear weighting field

**INVALIDATED AT THE SINGULAR DC/NO-RECOMBINATION POINT.** Away from `kappa+s=0`, five colors remain exact for the stated one-dimensional linear forcing. At `s=kappa=0`, use six colors/third differences.

---

## 8. Current HgCdTe worked example

Use the corrected raw-Ramo four-color stochastic calculation.

Explicit optical stress:

```text
L = 7.6 um
T = 300 K
linear x = 0.55 -> 0.32
mean generation depths = 2.5, 3.0, 3.5, 4.0 um
lambda ~ 2.134651, 2.215042, 2.301173, 2.393907 um
Pabs > 0.9993
```

For no recombination, the gradient-sensitive closure phase remains approximately

```text
100 MHz -> -0.011978 deg
500 MHz -> -0.058727 deg
1 GHz   -> -0.110405 deg
```

The point-source low-RF slowness-gradient result gives approximately `-0.01254 deg` at 100 MHz.

Rev. 6 retains the exact conditional transport law used to generate these numbers: linear composition, Hansen gap and derivative, Einstein diffusion, the inherited empirical **field-rolloff sensitivity law** (not an asymptotic saturation law), reduced density-of-states gradient correction, stochastic backward equation, and bounded semi-infinite entrance match.  At the sampled grading fields the rolloff changes the low-field velocity by only about 0.15--0.18%, so the reported closure values are unchanged.

The stochastic finite-difference result was independently reproduced with an adaptive shooting construction to approximately `10^-6 degree` agreement or better at the reported RF points. This is **numerical cross-verification of the same specified conditional model**, not physical validation of HgCdTe at `10^-6 degree`.

These are conditional theory predictions, not calibrated forecasts for an existing detector.

**REV. 6 HgCdTe normalization:** the previously reported finite-width target and resource budget are the conditional `xi=1` baseline of the force-partition sensitivity stress, not generic HgCdTe material specifications. The manuscript now varies `xi` explicitly.

Rev. 6 retains the deliberately independent residual-error stresses, but they are **derived design requirements rather than demonstrated calibration performance**:

```text
nonaffine source-coordinate RMS:
100 MHz -> 3.828 nm
500 MHz -> 3.780 nm
1 GHz   -> 3.626 nm

irregular channel-phase RMS:
100 MHz -> 1.023e-4 deg
500 MHz -> 5.017e-4 deg
1 GHz   -> 9.431e-4 deg
```

These are not absolute depth or common-delay requirements; smooth common/affine components cancel strongly.

---

## 9. Separate geometry hardening result

The realistic 2-D finite-electrode/depletion stress remains separate from the canonical manuscript.

For the representative 75%-contact + 3 um depletion-like stress, the geometry/depletion excess over the planar same-optics baseline is approximately:

```text
100 MHz -> -0.008841 deg = 0.738 x current 1-D gradient target
500 MHz -> -0.045827 deg = 0.780 x target
1 GHz   -> -0.095513 deg = 0.865 x target
```

This geometry family is **CHECKED / CONDITIONAL**, not a calibrated device simulation and not a theorem for arbitrary geometry. At 100 MHz its second spatial mode becomes nominally detectable around `84.6 dB` current-step amplitude SNR, below the present `96.1 dB` gradient-specific requirement, and its fitted effective rank-two roots fail the homogeneous finite-boundary root-sum law.

Do not promote this calculation into the headline manuscript as definitive geometry closure until the more realistic self-consistent 2-D transport attack is completed.

---

## 10. Hard prior-art boundary

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
minimal color-count model-order closure
+
branch-controlled spatial root recovery
+
RF root-algebra falsification of ordinary photocarrier transport mechanisms.
```

**Status:** CANDIDATE DISTINCT APPLICATION — PRIORITY UNPROVEN.

Targeted negative searches are not priority evidence.

---

## 11. What is demoted from the headline manuscript

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

## 12. Next decisive work

Do **not** reopen broad exploratory theory unless manuscript review or realistic-device falsification exposes a genuine missing theorem.

Priority now:

1. preserve the exact anonymous 22-page Rev. 6 source and keep both manuscript-preservation and privacy guards passing;
2. keep the realistic 2-D geometry result as a separate auditable hardening result rather than treating it as a calibrated detector prediction;
3. continue the narrow primary-source priority audit for the exact spectral-depth closure construction;
4. advance the geometry attack to one plausible self-consistent 2-D semiconductor Poisson/drift-diffusion structure with diffusion and analyze the synthetic spectral/RF data blindly using the same hierarchy;
5. convert independent numerical checks into reproducibility tables / supplement material;
6. only after these pass, choose a target journal and adapt formatting.

The objective is the smallest set of exact, falsifiable predictions that a skeptical reviewer cannot dismiss as an observable mismatch, spatial alias, uncontrolled ordinary mechanism, geometry artifact, calibration artifact, or rediscovery of known photodiode response physics.
