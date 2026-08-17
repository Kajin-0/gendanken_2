# Publication Roadmap — Existing Research Audit

**Date:** 2026-08-15  
**Status:** **CHECKED PORTFOLIO AUDIT / NON-CLAIM**  
**Purpose:** identify manuscript-scale scientific objects already present in the repository without salami-slicing one result into multiple weak papers.

## 1. Governing rule

The repository contains substantially more derivation than independent publishable claims.

Publication decisions therefore follow

```text
scientific independence
+ coherent falsifiable question
+ quantitative result
+ prior-art separation
+ observable discipline
+ reproducibility
```

rather than file count.

A negative literature search is not priority evidence. Existing manuscript preservation and pseudonymity rules remain unchanged.

---

## 2. Portfolio summary

| Track | Scientific object | Current status | Paper assessment |
|---|---|---|---|
| Paper 01 | Shockley-Ramo spectral-depth closure hierarchy | canonical anonymous Rev. 9 exists | **PURSUE / highest priority** |
| Paper 02 | multidimensional weighting/depletion geometry as a false spectral-transport signature | one realistic 2-D stress family exists | **DEVELOP / strongest independent unused paper seed** |
| Paper 03 | spatial first-passage semigroup and timing-cumulant null tests | exact probability results exist | **NOVELTY GATE BEFORE DRAFTING** |
| Future metrology | graded-HgCdTe spectral timing tomography | finite-kernel inverse and published-device instantiation exist | **HOLD pending independent validation/data** |
| Supporting only | hot-carrier rank-two closure, finite-width optical corrections, recombination/root-law hierarchy | mature supporting theory | **KEEP WITH PAPER 01** |
| Closed | broad Experiment-02 detector-process framework | conceptually resolved; strong prior-art overlap | **NO MANUSCRIPT RECOMMENDED** |
| Closed | Experiment-02 semiconductor thickness optimum | useful reduced scaling; architecture dependent | **NO MANUSCRIPT RECOMMENDED** |
| Provenance | original universal vanishing-absorber/capture-bound routes | counterexamples and narrowing preserved | **DO NOT RESURRECT AS PAPER CLAIMS** |

---

# 3. Paper 01 — current Rev. 9

## Working scientific question

> Can wavelength/depth-resolved terminal-current measurements reject classes of photocarrier transport models before a detailed microscopic parameter fit is trusted?

The manuscript object is the Shockley-Ramo-aware spectral-depth closure hierarchy, not generic wavelength-dependent transit time and not generic Hankel/Prony identification.

The current logical spine is

```text
four-color one-mode null
-> calibrated-kernel one-mode consistency
-> DC + RF physical root law
-> six-color rank-at-most-two null
-> distinct/confluent classification
-> multiplicity-aware physical admissibility
-> higher ordinary model order before exotic interpretation
```

The canonical manuscript remains Rev. 9 and is not modified by this roadmap.

## Submission blockers retained

1. **OPEN — closest-source priority audit.** The exact closest graded-HgCdTe / spectral-depth source must be compared in full technical detail before strong priority language.
2. **OPEN — calibration feasibility.** Derived nanometer-scale coordinate and small phase-tolerance requirements must be tied to a credible calibration architecture rather than left as algebraic requirements.
3. **OPEN — blind combined-physics validation.** A synthetic detector containing multiple ordinary departures simultaneously should be analyzed without giving the inversion the generating mechanism labels. `rank > 2, mechanism unresolved` is an acceptable correct outcome.

## Anti-salami rule

Do not extract the following into separate manuscripts while Paper 01 remains the primary claim:

- hot-to-cold two-state rank-two closure;
- finite-width translated-kernel theorem;
- recombination identifiability/root law;
- arbitrary-spacing calibration;
- nonuniform one-dimensional weighting correction;
- six-color mode-separation noise scaling.

They are defenses, qualifications, or rungs of one hierarchy.

---

# 4. Paper 02 — multidimensional Shockley-Ramo geometry

**Status:** **CANDIDATE DISTINCT APPLICATION — PRIORITY UNPROVEN**

## Existing result

The current 2-D finite-electrode/depletion stress shows that ordinary geometry can create an apparent four-color transport-gradient phase comparable to the nominal microscopic target.

For the refined 75%-contact + depletion stress, the geometry/depletion excess was approximately

```text
100 MHz -> 0.738 x current gradient target
500 MHz -> 0.780 x current gradient target
1 GHz   -> 0.865 x current gradient target
```

while the second spatial mode became statistically resolvable at about

```text
84.6 dB current-step amplitude SNR at 100 MHz
```

compared with approximately

```text
96.1 dB
```

required for the current 100-MHz transport-gradient claim.

The corresponding warning margin was therefore about

```text
11.5 dB
```

for that stress family; the 50%-contact case gave a larger margin of roughly `24.6 dB`.

## Candidate paper question

> When can realistic multidimensional Shockley-Ramo weighting and electrostatic-field geometry imitate a one-dimensional spectral transport signature, and when does that same geometry necessarily reveal itself through increased spatial model order or cross-frequency root-law failure?

This is scientifically distinct from Paper 01 if the result becomes a systematic geometry regime map rather than one additional manuscript stress case.

## Required extension before drafting

Map the geometry response over dimensionless coordinates such as

```math
f_c = W_contact/W_device,
```

```math
\delta_d = W_d/L,
```

```math
\chi_{sc}=V_{sc}/V_{bias},
```

```math
\beta = \sigma_x/(W_{contact}/2),
```

and normalized beam offset

```math
\xi=x_0/(W_{contact}/2).
```

At each point calculate at minimum

```text
four-color phase excess over planar same-optics baseline;
geometry-mimic fraction relative to the reference transport signal;
sigma2/sigma1 and sigma3/sigma2 of the six-color Hankel matrix;
3-sigma second-mode SNR threshold;
warning margin versus the SNR needed for the transport claim;
RF dependence of the fitted two-root physical constraints;
collection fraction and exact DC Shockley-Ramo consistency error.
```

A parameterized sweep script is added with this roadmap.

## Predeclared scientific outcomes

### Outcome A — geometry self-announces

Large false transport signatures are accompanied by an observable higher spatial mode or root-law violation before the transport-claim SNR is reached.

This supports a practical falsification hierarchy.

### Outcome B — geometry can hide

There exists a broad physically ordinary region in which geometry produces an order-one transport-like signature while remaining effectively rank one / physically admissible at the relevant precision.

This would be a stronger warning result and would force revision of the current interpretation protocol.

### Outcome C — geometry is small

Across a sufficiently broad realistic parameter domain, multidimensional geometry produces only a small fraction of the target signal.

This would be useful validation but probably not justify a standalone paper without a stronger theorem or calibrated device application.

## Go/no-go threshold for standalone manuscript

**GO** if either Outcome A or Outcome B survives a broad parameter sweep, numerical refinement, and at least one materially different geometry family.

**NO-GO as standalone paper** if the result reduces to a narrow corner of one chosen finite-contact geometry with no general organizing variable or experimentally actionable consequence.

---

# 5. Paper 03 — spatial first-passage semigroup / cumulant nulls

**Status:** **CANDIDATE DISTINCT APPLICATION — PRIORITY UNPROVEN / NO MANUSCRIPT YET**

## Existing mathematical object

For scalar homogeneous regenerative successful first-passage transport,

```math
T_{a+b}\overset d=T_a+T_b',
```

so

```math
E[e^{-sT_d}]=e^{-d\Phi(s)}.
```

Whenever the required moments exist,

```math
\kappa_n[T_d]\propto d,
```

and standardized cumulants satisfy

```math
\lambda_n(d)\propto d^{1-n/2}.
```

For ordinary uniform drift-diffusion the inverse-Gaussian hierarchy is

```math
\kappa_n
=(2n-3)!!(2D)^{n-1}d/w^{2n-1}.
```

The mathematics is established probability theory. The only possible paper claim is a detector-transport application or experimentally useful falsification construction.

## Observable lock

This track applies naturally to an **arrival / successful collection-time observable** such as

```math
U(d,s)=E[e^{-sT_d}],
```

not automatically to raw terminal Shockley-Ramo current.

No Paper-03 draft may blur this distinction.

## Novelty gate

Before drafting, perform a focused primary-source audit against

```text
semiconductor time-of-flight transport;
transient-current technique;
first-passage spectroscopy;
inverse-Gaussian carrier transit models;
subordinator / Levy-process system identification;
depth-resolved impulse response;
photodiode transit-time distribution reconstruction;
cumulant-based transport diagnostics.
```

The candidate survives only if the specific construction

```text
multiple known generation depths
-> spatial convolution-semigroup test
-> parameter-free cumulant/null relations
-> mechanism falsification from violations
```

is meaningfully distinct and experimentally useful.

## Go/no-go

**GO:** focused audit finds a defensible detector-specific gap and the repository can specify an actual observable/measurement architecture that tests the nulls.

**NO-GO:** the application is only a relabeling of standard time-of-flight / first-passage statistics.

---

# 6. Graded-HgCdTe spectral timing tomography — hold

The repository already contains a finite-kernel linear inverse

```math
T=Aq+c1,
```

with synthetic recovery and a physically adjacent published-device instantiation.

However, wavelength-dependent generation depth, transit-time variation, graded-HgCdTe acceleration, spatial timing, and forward wavelength/depth modeling all have substantial prior art.

Additional algebra has low marginal value.

Reopen this as a manuscript track only when at least one of the following exists:

1. independent experimental wavelength-resolved timing data;
2. a blind TCAD / Monte-Carlo transport profile generated independently of the inversion;
3. an experimentally relevant buried transport feature that ordinary total bandwidth cannot localize but the spectral inverse can.

---

# 7. Explicitly closed publication routes

## Experiment 02 broad detector boundary

Retain as rigorous conceptual synthesis. Do not claim a new general detector-process theory because the formal layers substantially overlap statistical experiment comparison, Blackwell/garbling order, quantum measurement/instrument theory, and process/channel comparison.

## Semiconductor thickness branch

Retain the useful scaling family

```math
L_*\sim(s/pK)^{1/p},
\qquad
\mu_*=s/p,
```

and the mixed linear/quadratic optimum, but do not manufacture a paper around it. The coefficients and exponents are architecture dependent and the branch overlaps standard absorber/noise/device optimization.

## Early universal absorber/capture bounds

Retain as provenance and failed-route documentation. Do not restore invalidated universal language.

---

# 8. Execution order

```text
1. finish Paper 01 submission blockers;
2. develop Paper 02 geometry regime map in parallel without touching Rev. 9;
3. run Paper 03 prior-art gate before any manuscript drafting;
4. hold spectral timing tomography for independent validation;
5. leave Experiment 02 and early universal-bound branches closed unless a genuinely new narrow theorem appears.
```

The expected portfolio is therefore deliberately conservative:

```text
one current manuscript
+ one strong independent development track
+ one high-risk theory novelty gate
+ one future validation/metrology track.
```

That is preferable to maximizing manuscript count at the expense of scientific independence.