# Current Live State — Experiment 01 / Spectral-Transport Program

**Date:** 2026-08-17  
**Status:** Paper 01 preserved; Paper 02 merged/frozen; Paper 03 combined-physics challenge active.  
**Priority:** execute the predeclared blind combined-physics validation without modifying canonical manuscripts unless a material scientific defect is found.

This is the current state pointer. The complete superseded 2026-08-11 live-state record is preserved byte-for-byte as

```text
CURRENT_STATE_ARCHIVE_2026-08-11.md
```

Use that archive and the dedicated adversarial records for detailed Paper 01 numerical history. Do not allow the archive's old portfolio numbering to override this file or `PUBLICATION_ROADMAP_CURRENT.md`.

---

## 1. Current portfolio

```text
Paper 01
Spectral-depth closure tests for falsifying photocarrier transport
from Shockley--Ramo current
-> canonical anonymous Rev. 9 retained

Paper 02
Apparent diffusion from deterministic velocity gradients in
wavelength-resolved unipolar photodetector transport
-> Rev. 9 referee-response manuscript merged through PR #18
-> frozen except for a material scientific defect or submission-specific work

Paper 03
Multidimensional geometry + combined ordinary detector physics
as a false spectral-transport signature
-> predeclared blind challenge
-> Stage A active on PR #19

Paper 04 candidate
Spatial first-passage semigroup / timing-cumulant nulls
-> novelty gate required before drafting
```

Historical files created when the geometry project was called Paper 02 retain their old filenames for provenance. In particular,

```text
numerics/paper02_geometry_parameter_sweep.py
.github/workflows/paper02-geometry-quick.yml
```

are now development inputs to current Paper 03, not parts of the merged current Paper 02 manuscript.

---

## 2. Paper 01 preservation lock

The canonical Paper 01 manuscript remains the anonymous Rev. 9 baseline:

```text
MANUSCRIPT_REV9_ANON_2026-08-11.tex
SHA-256 = df62813f764f051684ec52162095a5103296b71da1549b4c96829b0168fa1ce4
compiled pages = 28
author/PDF metadata = Anonymous
```

Its scientific hierarchy remains

```text
spectral wavelength
-> calibrated generation coordinate / known kernels
-> Shockley-Ramo terminal-current observable
-> four-channel one-mode falsification
-> DC + RF physical root law
-> six-channel rank-at-most-two test
-> distinct/confluent classification
-> multiplicity/branch/permutation-aware physical admissibility
-> higher ordinary model order before mechanism assignment
```

The Rev. 9 corrections and all Rev. 4--8 hardening remain mandatory. The archived 2026-08-11 state contains the detailed checklist and numerical values.

Do not rewrite Paper 01 merely to incorporate Paper 03 bookkeeping. Paper 03 is first an external validation attack on the hierarchy.

---

## 3. Paper 01 remaining blockers

Three substantive fronts remain:

1. **Closest-source priority audit.** Strong priority language still requires direct technical comparison with the closest graded-HgCdTe / spectral-depth source.
2. **Calibration feasibility.** The nanometer-scale coordinate, common depth scale, phase, optical-kernel, shared-composition, and same-optics covariance requirements require a credible calibration architecture.
3. **Blind combined-physics validation.** Several ordinary departures must coexist in an independent synthetic detector and be analyzed without giving the hierarchy the generating mechanism labels.

The third blocker is now the active Paper 03 development track.

A safe blind outcome remains

```text
rank > 2
mechanism unresolved
```

because the hierarchy is a falsification structure, not a guaranteed mechanism classifier.

---

## 4. Paper 02 — merged and frozen

PR #18 merged the validated Paper 02 Rev. 9 referee-response manuscript to `main`.

Current Paper 02 concerns transport identifiability: a deterministic nonuniform velocity profile can yield a positive fitted effective diffusion coefficient when data are interpreted with the wrong homogeneous drift-diffusion inverse.

Its exact-continuum reference values remain approximately

```text
100 MHz -> D_eff = 2.6182e-3 m^2/s
500 MHz -> D_eff = 2.5508e-3 m^2/s
1 GHz   -> D_eff = 2.3506e-3 m^2/s
```

with the upstream point-source controls at numerical-zero diffusion under the stated construction.

Paper 02 is not the geometry project. Do not create another Paper 02 revision merely to repair portfolio numbering.

---

## 5. Checked geometry seed inherited by Paper 03

The separately auditable deterministic geometry stress remains

```text
REALISTIC_GEOMETRY_CLOSURE_STRESS.md
numerics/realistic_geometry_closure_stress.py
```

For the refined 75%-contact + depletion-like stress, the geometry/depletion four-color excess was approximately

```text
100 MHz -> 0.738 x the reference 1-D gradient target
500 MHz -> 0.780 x target
1 GHz   -> 0.865 x target
```

At 100 MHz the second-mode witness required about

```text
84.6 dB current-step amplitude SNR
```

versus about

```text
96.1 dB
```

for the reference transport claim, leaving an approximately `11.5 dB` early-warning margin in that stress family.

The 50%-contact case gave an even larger warning margin. The fitted two-root response also failed the simple RF-independent physical root-sum law.

This result is checked only under its stated deterministic high-Peclet assumptions. It is not a calibrated detector simulation and is not a theorem for arbitrary geometry.

The historical parameterized regime-map implementation is

```text
numerics/paper02_geometry_parameter_sweep.py
```

and must be reused rather than duplicated.

---

## 6. Paper 03 predeclared combined-physics challenge

The governing record is

```text
PAPER03_COMBINED_PHYSICS_CHALLENGE_2026-08-17.md
```

Scientific question:

> When finite geometry, nonuniform electrostatics, diffusion, recombination, realistic optical kernels, and later self-consistent charge/contact/multicarrier effects coexist in an independent forward model, does the hierarchy reject an inadequate low-dimensional transport interpretation before a false microscopic parameter claim becomes statistically defensible?

### Blind boundary

The forward side may know fields, geometry, diffusion, lifetime, contact rules, and trajectory histories.

The blind analysis may receive only legitimate measurement/calibration inputs such as

```text
complex J(lambda, omega);
channel/frequency information;
known calibrated kernels where required;
predeclared noise/calibration information.
```

It must not receive the hidden mechanism label, true diffusion coefficient, true lifetime, internal field, or trajectory fates.

### Observable lock

The selected-electrode response remains Shockley--Ramo terminal current. Every discrete trajectory accumulates actual weighting-potential increments. At DC,

```math
H(0)=phi_w(r_end)-phi_w(r_0).
```

Recombination or opposite-contact collection therefore does **not** get forced to the selected-contact endpoint value.

---

## 7. Paper 03 staged execution

### Stage A — active

Reuse the checked 2-D potential/weighting machinery and add stochastic transport

```math
dr=v(r)dt+sqrt(2D)dW
```

plus an optional exponential recombination hazard.

Current implementation:

```text
numerics/paper03_combined_physics_challenge.py
.github/workflows/paper03-combined-physics-stageA.yml
```

Required Stage-A gates:

```text
D=0, tau=infinity -> checked deterministic recovery path;
DC endpoint-Ramo telescope -> numerical precision;
fixed-seed reproducibility;
explicit terminal fates;
particle-count and step-size convergence before scientific phase interpretation;
mechanism-blind analysis API.
```

Stage A is a combined-physics seed. It is **not** a self-consistent semiconductor Poisson/drift-diffusion solution.

### Stage B — next after Stage-A numerical lock

Implement and independently validate one charge-coupled semiconductor forward model containing at minimum

```text
Poisson electrostatics;
explicit fixed charge/doping prescription;
carrier statistics;
field-dependent drift;
diffusion;
recombination;
contact boundary conditions;
and a separately solved weighting potential.
```

The forward model must pass soluble-limit or independent-formulation checks before its synthetic currents are used as scientific evidence.

### Stage C

Run the blind hierarchy over the declared combined geometry/transport coordinates, add measurement-noise/SNR analysis only after numerical uncertainty is controlled, and repeat the decisive behavior in a materially different geometry family.

---

## 8. Paper 03 GO / NO-GO

Standalone **GO** requires all of:

```text
numerical recovery and convergence;
strict blind-analysis separation;
a broad physically ordinary regime with a clear Outcome A or B;
a materially different second geometry family;
an observable/SNR consequence;
a focused prior-art audit leaving a defensible contribution.
```

Outcome A:

```text
large confound self-announces through model order / root-law failure
before the mechanism-specific claim threshold.
```

Outcome B:

```text
large confound remains hidden at the tested model order and physical root laws
through the mechanism-specific claim precision.
```

Outcome B would force a narrowing of the Paper 01 interpretation protocol.

A narrow one-geometry sensitivity, a result that disappears under refinement, or an inverse that requires hidden generator labels is standalone **NO-GO**.

---

## 9. Paper 04 candidate

The first-passage/cumulant branch is now current Paper 04 candidate.

Its exact probability structure is not by itself a novelty claim. Before any manuscript drafting, perform the focused primary-source audit against semiconductor time-of-flight, transient-current technique, first-passage spectroscopy, inverse-Gaussian transit models, subordinator/Levy-process system identification, depth-resolved impulse response, photodiode transit-time reconstruction, and cumulant-based diagnostics.

Keep its observable distinction explicit: successful collection/arrival-time transforms are not automatically raw Shockley--Ramo terminal current.

---

## 10. Current execution order

```text
1. preserve Paper 01 and frozen Paper 02;
2. finish Paper 03 Stage-A invariant execution and numerical convergence;
3. implement/validate Paper 03 Stage-B self-consistent forward physics;
4. run the blind combined regime map;
5. test a materially different geometry family;
6. feed only defensible validation consequences back into Paper 01 readiness;
7. run the Paper 04 novelty gate before drafting.
```

Do not start another broad speculative branch while the Paper 03 combined-physics gate is unresolved unless a material contradiction appears.

---

## 11. Mandatory recovery order

For a new agent continuing this program:

1. root `PRIVACY_PROTOCOL.md`;
2. root `AGENTS.md`;
3. root `PUBLICATION_ROADMAP_CURRENT.md`;
4. `MANUSCRIPT_CURRENT.md` and manuscript preservation records when Paper 01 work is required;
5. this file;
6. `CURRENT_STATE_ARCHIVE_2026-08-11.md` for the complete prior Paper 01 live-state detail;
7. `PAPER03_COMBINED_PHYSICS_CHALLENGE_2026-08-17.md`;
8. `REALISTIC_GEOMETRY_CLOSURE_STRESS.md`;
9. `numerics/realistic_geometry_closure_stress.py`;
10. historical `numerics/paper02_geometry_parameter_sweep.py`;
11. `numerics/paper03_combined_physics_challenge.py`.

**Preserve first; integrate second; rewrite only when scientifically necessary.**

**Pseudonymity first; identifying information only when explicitly approved for that artifact.**
