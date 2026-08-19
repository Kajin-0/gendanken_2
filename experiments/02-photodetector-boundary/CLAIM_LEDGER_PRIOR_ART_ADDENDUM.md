# Claim Ledger Addendum — Prior-Art Boundary

**Date:** 2026-08-12  
**Status:** active addendum; broad framework novelty substantially narrowed  
**Priority:** unresolved; no novelty claim

Read together with

```text
CLAIM_LEDGER.md
CLAIM_LEDGER_PROCESS_ADDENDUM.md
MATHEMATICAL_PRIOR_ART_AUDIT.md
CRITICAL_COUPLING_PRIOR_ART_AUDIT.md
DSTAR_TEMPORAL_PRIOR_ART_AUDIT.md
```

This addendum records claim corrections produced by the primary-source audit. It intentionally does not rewrite earlier exploratory statements out of history.

---

## PA1 — complete statistical experiment / all-task comparison
**Status:** KNOWN PRIOR ART

Blackwell's comparison of experiments already establishes the classical all-decision-problem ordering / garbling structure.

No novelty claim is permitted for

```text
full conditional output as a statistical experiment;
universal usefulness ordering across decision problems;
hypothesis-independent post-processing / garbling dominance;
task-dependent incomparability when neither experiment dominates.
```

## PA2 — approximate experiment comparison / deficiency
**Status:** KNOWN PRIOR ART

Le Cam comparison/deficiency theory already treats approximate simulation/comparison of statistical experiments.

Do not present approximate detector-channel comparison as a new abstract principle.

## PA3 — quantum statistical-model comparison
**Status:** KNOWN PRIOR ART

Buscemi's quantum comparison/sufficiency framework and related literature cover quantum extensions of statistical-experiment ordering.

## PA4 — quantum channel comparison / deficiency
**Status:** KNOWN PRIOR ART

Jenčová and related work cover comparison of quantum channels/statistical experiments through discrimination/simulation criteria.

## PA5 — multi-round adaptive process formalism
**Status:** KNOWN PRIOR ART

Quantum-comb / quantum-network theory already provides higher-order formalisms for memory-assisted, multi-round, adaptive quantum processes.

Experiment 02 may use this machinery but cannot claim the general process formalism as new.

## PA6 — photodetector POVM as a platform-independent complete measurement object
**Status:** DIRECT PHOTODETECTOR PRIOR ART

S. J. van Enk's `Photodetector figures of merit in terms of POVMs` explicitly derives detector figures of merit from a full POVM and motivates the POVM as a platform-independent photodetector description.

This directly blocks novelty claims of the form

```text
replace scalar detector figures of merit by the complete quantum measurement object;
use the full measurement object for platform-independent detector comparison.
```

## PA7 — general microscopic quantum photodetector modeling framework
**Status:** DIRECT PHOTODETECTOR PRIOR ART

Young, Sarovar, and Léonard developed a general quantum-photodetector modeling framework connecting underlying physical dynamics to detector response/performance.

Do not claim that Experiment 02 newly invents a general light-matter-to-readout quantum detector framework.

## PA8 — fundamental microscopic photodetector tradeoffs from coherence/backaction
**Status:** DIRECT PHOTODETECTOR PRIOR ART

Young, Sarovar, and Léonard also derived single-photon detector performance limits associated with quantum coherence/backaction.

The mere existence of microscopic quantum detector bounds/tradeoffs is therefore not a novelty route.

---

## PA9 — provisional detector-process framework
**Status:** USEFUL SYNTHESIS / PRIORITY UNPROVEN / BROAD NOVELTY REJECTED

The object

```math
\mathfrak C_D(R)
=\{K_{D,\sigma}^{(R)}:\sigma\in\Sigma_D(R)\}
```

and task risk

```math
R_D^*(\Pi|R)
```

are mathematically natural combinations of established decision/process/resource ideas.

Current safe interpretation:

> **bookkeeping / synthesis language for this Gedanken program, not a new foundational detector theory.**

A future contribution would require new physically justified detector constraints that yield a nontrivial theorem, impossibility result, bound, or experimental/design consequence not already contained in established frameworks.

---

## PA10 — critical coupling / unit single-photon capture
**Status:** PRIOR ART / STANDARD PHYSICS

Near-perfect single-photon capture through impedance matching in cavity/atom/storage systems is established.

The Experiment-02 clean one-port condition

```math
\Gamma_{\rm match}=4G^2/\kappa
```

is currently treated as a model-specific critical-coupling specialization, not new fundamental detector physics.

## PA11 — collective coupling and mode-weighted N
**Status:** PRIOR ART / STANDARD STRUCTURE

```math
G=g\sqrt N
```

and

```math
G^2=\sum_j|g_j|^2
```

are standard Dicke/Tavis--Cummings / bright-mode structure.

The replacement of literal `N` by optical depth / oscillator-strength overlap in extended matter is likewise strongly prior-art aligned.

## PA12 — weak coupling traded against bandwidth/time
**Status:** PRIOR ART / STANDARD RESONANT-STORAGE CONSEQUENCE

The ability to preserve peak resonant efficiency while narrowing bandwidth / extending interaction time is established cavity/storage physics.

## PA13 — critical-coupling control-floor threshold
**Status:** DERIVED COROLLARY / PRIORITY UNPROVEN / LOW NOVELTY EXPECTATION

```math
G^2
\ge
\frac{\kappa\Gamma_{\rm floor}}{4}
\frac{1-\sqrt\epsilon}{1+\sqrt\epsilon}
```

is a transparent corollary of the standard mismatch law once a nonzero control-rate floor is imposed.

It should not anchor a novelty claim unless a real detector architecture provides a physically unavoidable `Gamma_floor` and the resulting bound has distinct practical/theoretical content.

---

## PA14 — Gaussian matched-filter waveform distance
**Status:** ESTABLISHED DETECTION THEORY

```math
d^2
=\int|\tilde s(f)|^2/S_n(f)\,df
```

is standard Gaussian hypothesis-testing / matched-filter structure.

## PA15 — equal D* does not imply equal arbitrary-waveform performance
**Status:** DERIVED PHOTODETECTOR COUNTEREXAMPLE / UNDERLYING THEORY PRIOR ART / NO NOVELTY CLAIM

The one-pole benchmark is useful but not new detection theory.

With conventional **one-sided** NEP ASD,

```math
\boxed{
d^2
=\frac{E^2}{\tau\mathrm{NEP}_1^2}
=\frac{E^2D^{*2}}{A\tau}.
}
```

With two-sided NEP ASD,

```math
\boxed{
d^2
=\frac{E^2}{2\tau\mathrm{NEP}_2^2}.
}
```

The factor-of-two distinction is purely convention and must be stated explicitly.

## PA16 — full NEP(f) kernel / task dependence
**Status:** ESTABLISHED SIGNAL-DETECTION CONSEQUENCE

For linear Gaussian tasks,

```math
d_D^2[p]
=\int|\tilde p(f)|^2/\mathrm{NEP}_{2,D}^2(f)\,df.
```

Crossing decision kernels can reverse task ranking. This is an application of established statistical-experiment logic, not a new universal detector theorem.

---

## PA17 — current possible contribution space
**Status:** OPEN / PRIORITY UNPROVEN

After the audit, possible distinct work is narrowed to:

```text
A. a genuinely new photodetector-specific physical resource constraint;
B. a new quantitative tradeoff law that survives direct source-level comparison;
C. a useful cross-layer synthesis that produces a new experimentally testable design rule or impossibility result;
D. a resource-constrained achievable detector-process result that is more than generic decision/process theory.
```

A synthesis alone may be useful pedagogically without being novel research.

## PA18 — manuscript status
**Status:** NON-CLAIM / BLOCKED

No manuscript should be drafted from the broad framework at this stage.

Before any novelty language:

```text
audit remaining detector-specific equations;
map Young/Sarovar/Léonard in detail;
audit photodetection instrument/continuous-measurement theory;
identify one surviving nontrivial physical statement;
then perform an adversarial closest-source comparison on that statement.
```
