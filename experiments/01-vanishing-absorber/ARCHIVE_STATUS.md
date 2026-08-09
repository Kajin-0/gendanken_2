# Experiment 01 — Artifact Status Map

**Date:** 2026-08-08  
**Purpose:** preserve the adversarial research trail without allowing stopped or superseded branches to compete with the current frontier.

> Live `main`, root `AGENTS.md`, `CURRENT_STATE.md`, and `CLAIM_LEDGER.md` are authoritative.

---

## A. Canonical current frontier

Read first:

1. `CURRENT_STATE.md`
2. `CLAIM_LEDGER.md`
3. `PASSIVE_MULTIMODE_TRANSFER_AREA_BOUND.md`
4. `HOPFIELD_RESERVOIR_RESOURCE_COST.md`
5. `MULTIMODE_ESCAPE_AUDIT.md`
6. `HOPFIELD_RETUNING_NO_GO.md`
7. `HOPFIELD_RETUNING_PRIOR_ART_SWEEP.md`
8. `RESEARCH_LOG.md`
9. `ARCHIVE_STATUS.md`

There is still **no manuscript**.

---

## B. Current strongest supporting result

### `PASSIVE_MULTIMODE_TRANSFER_AREA_BOUND.md`

Status: **active model-level theorem / detector-facing passivity corollary; novelty unassessed and not claimed**.

For a finite stable passive linear network with total optical and detector access budgets

```math
L=\operatorname{Tr}\Gamma_L,
\qquad
R=\operatorname{Tr}\Gamma_R,
```

and no direct `L -> R` feedthrough,

```math
\boxed{
\mathcal I_{L\to R}
\le
\frac{2LR}{L+R}.
}
```

The proof uses an exact Gramian-basis decomposition and Cauchy-Schwarz.

This supersedes the preliminary loose bound

```math
\mathcal I_{L\to R}
\le2\min(L,R).
```

The loose bound remains only as historical provenance in `RESEARCH_LOG.md`.

---

## C. Active nonperturbative supporting branch

### `HOPFIELD_RETUNING_NO_GO.md`

Status: **active supporting theorem; candidate distinct lemma; priority unproven**.

Role: shows one explicit mechanism by which the two required external accesses collapse when internal light-matter coupling is taken to infinity at fixed dressed target frequency and fixed local bath resources.

### `HOPFIELD_RESERVOIR_RESOURCE_COST.md`

Status: **active supporting resource theorem**.

Role: quantifies the cost of defeating the fixed-bath Hopfield result by scaling the bare external reservoirs. Fixed peak transfer and linewidth require at least one bare reservoir coupling to grow asymptotically as `sqrt(g)`.

### `HOPFIELD_RETUNING_PRIOR_ART_SWEEP.md`

Status: **active targeted negative literature search**.

Verdict: candidate distinct fixed-target lemma; priority unproven. Deep-strong decoupling itself is established prior physics.

### `NONPERTURBATIVE_HOPFIELD_CAPTURE.md`

Status: **active supporting derivation with strong prior-art overlap**.

Role: symmetric example showing unit peak transfer can coexist with linewidth collapse in deep strong coupling.

---

## D. Multimode branch

### `MULTIMODE_ESCAPE_AUDIT.md`

Status: **active adversarial audit**.

Key conclusions:

- a theorem based only on the largest internal coupling anywhere in a multimode system is false due to spectator sectors;
- growing useful mode count/density can compensate shrinking individual linewidths;
- mode proliferation is an explicit resource;
- the correct general quantity is integrated transfer, leading to the harmonic access theorem.

---

## E. Earlier active supporting derivations

These remain scientifically useful provenance but are no longer the active frontier:

### `OSCILLATOR_STRENGTH_EXTENT_STRESS_TEST.md`

Shows finite extent + selected oscillator-strength inequalities do not close the weak-coupling problem before the perturbative rate reaches `O(omega)`.

### `FINITE_EMITTER_FORM_FACTOR.md`

Shows finite transition density regularizes the literal point-dipole ultraviolet divergence.

### `FINITE_TRANSITION_LDOS_BANDWIDTH_BOUND.md`

Applies established bandwidth-averaged LDOS bounds to the finite-transition detector problem under explicit environment/separation assumptions.

### `MICROSCOPIC_SINGLE_TRANSITION.md`

Shows finite absorber number / saturation alone does not create a one-photon speed ceiling in the one-excitation Markov/RWA model.

### `THERMAL_INPUT_CHANNEL.md`

Derives the restricted one-channel thermal-background sensitivity-speed relation including Bose bunching.

### `ONE_PORT_RESONATOR_DYNAMICS.md`

Fixes one-port normalization and derives the exact absorbed-power modulation bandwidth.

---

## F. Direction-changing counterexample

### `ACTIVE_VOLUME_COUNTEREXAMPLE.md`

Status: **active historical counterexample; branch-closing result**.

It explicitly invalidates an active-volume-only passive optical bound in the admitted ideal local continuum model.

Do not delete it; it prevents future agents from resurrecting the original conjecture.

---

## G. Stopped / invalidated general routes

Do not restart without a new assumption that directly defeats the recorded counterexample or failure.

### Active-volume-only theorem — STOPPED

Invalidated general statements include

```text
passivity alone bounds gamma_a/V_a
```

and

```text
eta^2 B <= C V_a
```

as universal active-volume laws.

### Finite absorber count as the missing one-photon limit — STOPPED

The one-excitation sector remains linear.

### Largest multimode coupling as a universal control parameter — STOPPED

A disconnected spectator sector is a direct counterexample.

### Preliminary `2 min(L,R)` multimode bound — SUPERSEDED

Still true but noncanonical. The harmonic theorem

```math
2LR/(L+R)
```

is strictly stronger and tight.

---

## H. Numerical material

Active directory:

`numerics/`

### `one_port_time_domain_check.py`

Status: active validation of the one-port modulation transfer function.

### `passive_multimode_h2_stress.py`

Status: active deterministic stress/regression test.

Checks

- `0 <= Q_L <= I`;
- the exact Gramian-basis diagonal identity;
- the harmonic access bound;
- exact single-mode saturation;
- direct frequency integration versus the Gramian/H2 result.

Current dependency: NumPy.

No CI workflow is justified yet.

---

## I. Literature status

No integrated novelty audit exists yet.

Important primary anchors already encountered include

- passive/scattering linear-system theory;
- Maxwell scattering-passive realizations;
- passive quantum linear-system realizations;
- geometry-independent optical-response and LDOS bounds;
- dark-state quantum photodetector models;
- deep-strong light-matter decoupling;
- multiresonant broadband absorption/emission bounds.

The exact harmonic two-access trace inequality requires a deeper control/network/microwave/scattering prior-art search before any publication positioning.

---

## J. Current forward branch

The next attacks are:

1. search specifically for an equivalent harmonic `H_2` / passive-network inequality;
2. formulate finite-band direct-feedthrough access accounting;
3. test genuinely infinite-dimensional or strongly structured passive reservoirs;
4. map abstract access traces onto microscopic semiconductor optical and irreversible-relaxation resources;
5. then reintegrate noise, reverse thermal rates, amplification, and reset thermodynamics.

Do not add HgCdTe-specific transport until at least the first three are resolved.

---

## K. Archival rule

Do not delete a useful failed branch merely to make the repository cleaner.

When a result is superseded or invalidated:

1. update `CURRENT_STATE.md`;
2. update `CLAIM_LEDGER.md`;
3. record the chronology in `RESEARCH_LOG.md`;
4. mark status here;
5. keep the derivation when it documents an important counterexample, correction, or narrowing of scope.
