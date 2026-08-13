# Mathematical and Photodetector Prior-Art Audit — Experiment 02

**Date:** 2026-08-12  
**Status:** active primary-source audit; broad framework novelty substantially narrowed  
**Priority:** unresolved; no novelty claim

This file audits the provisional detector-process framework against established statistical decision theory, quantum channel/process comparison, and photodetector-specific measurement/modeling literature.

The purpose is adversarial:

> determine which parts of Experiment 02 are already established theory and prevent a detector-specific synthesis from being overstated as a new general framework.

Negative search results are not novelty evidence. Where a close source exists, it is treated as a hard claim boundary.

---

## 1. Provisional Experiment-02 framework under audit

The current synthesis represents detector implementation `D`, resource model `R`, and allowed strategy `sigma` by an accessible process such as

```math
K_{D,\sigma}^{(R)}(dy\,dt\,dc|x),
```

with capability region

```math
\mathfrak C_D(R)
=\{K_{D,\sigma}^{(R)}:\sigma\in\Sigma_D(R)\},
```

and task-specific optimum risk

```math
R_D^*(\Pi|R)
=\inf_{K\in\mathfrak C_D(R)}\inf_\delta R(\delta,K;\Pi).
```

The audit asks whether the following layers are new:

```text
A. full conditional detector output rather than one scalar FOM;
B. all-task comparison / detector partial order;
C. quantum channel comparison;
D. multi-round/adaptive detector process;
E. platform-independent photodetector measurement description;
F. general physical quantum-photodetector modeling;
G. detector-specific resource-constrained synthesis/tradeoffs.
```

The current result is that **A-F are strongly covered by established literature in substance**. Only a narrower version of G remains open for possible distinct contribution.

---

## 2. Classical all-task ordering — Blackwell

### Primary source

David Blackwell,

```text
Equivalent Comparisons of Experiments,
Annals of Mathematical Statistics 24(2), 265-272 (1953),
DOI: 10.1214/aoms/1177729032.
```

Blackwell's comparison of statistical experiments establishes the classical connection between

```text
one experiment being at least as useful as another for every decision problem
```

and

```text
one experiment being obtainable from the other by hypothesis-independent randomization / garbling
```

under the theorem's conditions.

### Consequence for Experiment 02

The Experiment-02 statement

```math
K_B=T\circ K_A
```

and the interpretation

```text
A is universally at least as informative as B
```

are **KNOWN classical decision-theory structure**, not a new detector theorem.

Likewise, detector incomparability and task-dependent ranking reversal are expected whenever neither statistical experiment Blackwell-dominates the other.

### Claim boundary

```text
PRIOR ART:
full conditional output as a statistical experiment;
all-task risk comparison;
garbling/post-processing partial order;
incomparability across decision problems.
```

**No novelty claim is permitted for this mathematical layer.**

---

## 3. Le Cam comparison / deficiency lineage

Le Cam's theory of comparison of statistical experiments and deficiency extends the same general program beyond exact Blackwell equivalence by quantifying how closely one experiment can simulate another.

A later author-primary reference is

```text
L. Le Cam and G. L. Yang,
Asymptotics in Statistics: Some Basic Concepts,
2nd ed., Springer (2000).
```

The exact original-paper lineage should be recovered before manuscript citation, but the conceptual prior-art boundary is already clear:

```text
approximate experiment comparison / deficiency
is established statistics,
not a detector-specific invention.
```

### Consequence

If Experiment 02 later introduces an approximate detector ordering such as

```text
A can simulate B within tolerance epsilon
```

that should be framed relative to Le Cam/deficiency-type ideas, not presented as a new abstract comparison principle.

---

## 4. Quantum statistical-model comparison — Buscemi

### Primary source

Francesco Buscemi,

```text
Comparison of Quantum Statistical Models: Equivalent Conditions for Sufficiency,
Communications in Mathematical Physics 310, 625-647 (2012),
arXiv:1004.3794,
DOI: 10.1007/s00220-012-1421-3.
```

Buscemi develops a quantum randomization/comparison criterion for statistical models and connects quantum-information ordering with sufficiency, explicitly as a quantum extension of classical statistical comparison ideas.

### Consequence for Experiment 02

The move from

```text
classical detector experiment
```

to

```text
quantum output states/channels compared by decision usefulness
```

is established theory.

### Claim boundary

```text
PRIOR ART:
quantum statistical experiment comparison;
quantum sufficiency/randomization criteria;
all-task quantum-information ordering.
```

**No novelty claim is permitted for this layer.**

---

## 5. Quantum channels and deficiency — Jenčová

### Primary source

Anna Jenčová,

```text
Comparison of quantum channels and statistical experiments,
IEEE Transactions on Information Theory 62 (2016),
arXiv:1512.07016.
```

This work develops comparison/deficiency notions directly for quantum channels using discrimination tasks and connects them to quantum statistical experiments.

### Consequence for Experiment 02

The provisional idea

```math
\Phi_D:\rho_{\rm opt}\mapsto\rho_{\rm out}
```

and ordering detectors through channel simulation/post-processing is not new in mathematical form.

If a future detector theorem uses

```text
quantum channel deficiency;
post-processing comparison;
discrimination-success ordering,
```

it must explicitly inherit this literature.

---

## 6. Multi-round adaptive processes — Chiribella, D'Ariano, Perinotti

### Primary source

G. Chiribella, G. M. D'Ariano, and P. Perinotti,

```text
Theoretical framework for quantum networks,
Physical Review A 80, 022339 (2009),
arXiv:0904.4483.
```

The paper gives a general quantum-network framework, with quantum combs describing transformations achievable by networks and explicitly covering multi-step/memory transformations, including discrimination, estimation, tomography, and general network composition.

Related primary work:

```text
G. Chiribella, G. M. D'Ariano, and P. Perinotti,
Memory Effects in Quantum Channel Discrimination,
Physical Review Letters 101, 180501 (2008).
```

### Consequence for Experiment 02

The Experiment-02 upgrade

```text
one-use detector channel
-> multi-round detector process with memory and adaptive strategy
```

is an application of established higher-order quantum-process/network theory.

### Claim boundary

```text
PRIOR ART:
quantum combs/testers;
multi-round memory-assisted process description;
adaptive quantum-network strategies;
channel discrimination with memory.
```

**No novelty claim is permitted for the general process formalism.**

---

## 7. Direct photodetector collision — van Enk POVM figures of merit

### Primary source

S. J. van Enk,

```text
Photodetector figures of merit in terms of POVMs,
arXiv:1705.09640 (2017).
```

The paper explicitly starts from the fact that a quantum measurement is fully described by a POVM and shows how many photodetector figures of merit can be defined from the detector POVM.

It further motivates the POVM as a **platform-independent description for comparing different types of photodetectors**, precisely because the POVM acts on the incoming-light Hilbert space rather than being tied to a specific material platform.

The paper discusses conventional detector figures such as response time, bandwidth, dark counts, efficiency, wavelength resolution, and photon-number resolution and derives figures/tradeoffs from the POVM description.

### Consequence for Experiment 02

This is a **close photodetector-specific prior-art collision** with any broad statement of the form

```text
replace individual detector figures of merit
with the complete quantum measurement object
for platform-independent detector comparison.
```

### Hard claim correction

The following must be treated as **KNOWN / PRIOR ART**, not as an Experiment-02 novelty:

```text
full POVM as a platform-independent photodetector description;
deriving multiple detector FOMs from that full measurement description;
using the full quantum measurement rather than one scalar FOM to compare detector types.
```

This materially narrows the possible Experiment-02 contribution.

---

## 8. Direct photodetector collision — Young, Sarovar, Léonard general framework

### Primary source

Kevin C. Young, Mohan Sarovar, and François Léonard,

```text
General modeling framework for quantum photodetectors,
Physical Review A 98, 063835 (2018),
arXiv:1811.08018,
DOI: 10.1103/PhysRevA.98.063835.
```

The work develops a systematic framework for modeling quantum photodetectors from the underlying physical processes and is motivated by the need to connect microscopic physics to detector performance.

The framework treats detector dynamics beyond a bare optical POVM, including the physical mechanism by which the optical interaction is converted into an observable detector response.

### Consequence for Experiment 02

This is a close collision with any broad claim that Experiment 02 newly provides

```text
a general physical quantum-photodetector framework
linking light-matter interaction, detector dynamics, amplification/readout,
and detector performance.
```

That conceptual territory is already occupied.

### Hard claim correction

Do **not** claim novelty for

```text
general quantum photodetector modeling;
physics-to-readout detector framework;
using microscopic detector dynamics to derive performance behavior.
```

Any surviving Experiment-02 contribution must be narrower.

---

## 9. Direct photodetector collision — Young, Sarovar, Léonard coherence/backaction limits

### Primary source

Kevin C. Young, Mohan Sarovar, and François Léonard,

```text
Fundamental limits to single-photon detection determined by quantum coherence and backaction,
Physical Review A 97, 033836 (2018),
arXiv:1803.10558,
DOI: 10.1103/PhysRevA.97.033836.
```

This work analyzes fundamental single-photon detector performance limits from quantum coherence/backaction and identifies detector design/performance constraints from a microscopic quantum treatment.

### Consequence for Experiment 02

The broad program

```text
derive fundamental photodetector resource/performance tradeoffs from microscopic quantum dynamics
```

also has direct prior art.

Experiment 02 therefore cannot rely on the mere existence of microscopic quantum bounds/tradeoffs as its distinction.

Specific equations derived in Experiment 02 still require their own source-by-source novelty audits.

---

## 10. Audit matrix

| Experiment-02 layer | Closest established lineage | Current status |
|---|---|---|
| Full conditional output/statistical experiment | Blackwell / Le Cam | **PRIOR ART** |
| All-task partial order / garbling | Blackwell | **PRIOR ART** |
| Approximate comparison / deficiency | Le Cam | **PRIOR ART** |
| Quantum statistical comparison | Buscemi | **PRIOR ART** |
| Quantum channel comparison/deficiency | Jenčová | **PRIOR ART** |
| Multi-round/memory/adaptive process | Chiribella et al. quantum combs/networks | **PRIOR ART** |
| Photodetector full POVM vs multiple FOMs | van Enk | **DIRECT PRIOR ART** |
| General microscopic quantum photodetector framework | Young/Sarovar/Léonard | **DIRECT PRIOR ART** |
| Quantum-coherence/backaction detector limits | Young/Sarovar/Léonard | **DIRECT PRIOR ART** |
| Resource-constrained physical tradeoffs derived in this experiment | multiple physics lineages; not yet fully audited | **OPEN / PRIORITY UNPROVEN** |
| Unified photodetector-specific resource ledger across microscopic capture -> records -> electrical decisions -> repeated-use closure | no conclusion from current audit | **SYNTHESIS / PRIORITY UNPROVEN** |

---

## 11. Provisional-framework claim correction

The statement

> A photodetector should be represented by a complete channel/process rather than one scalar figure of merit.

is **not a credible novelty claim** after the van Enk + statistical/quantum comparison literature is credited.

The statement

> Detector performance is task dependent and universal superiority is a process/channel partial order.

is also largely an application of established decision theory / channel comparison.

The statement

> Adaptive/memory detector operation requires a multi-time process description.

is covered in general by established quantum-network/comb theory.

Therefore the broad `PROVISIONAL_DETECTOR_PROCESS_FRAMEWORK.md` should be treated as a **useful synthesis and bookkeeping language**, not a new foundational formalism.

---

## 12. What may remain distinct enough to investigate

The audit does **not** yet show that Experiment 02 has no useful contribution.

It moves the possible contribution into a much narrower space:

### A. Photodetector-specific resource closure across physical layers

The project has explicitly linked

```text
microscopic coupling / interaction action
-> collective capture / critical matching
-> control precision and bandwidth
-> mode-weighted oscillator strength / optical depth
-> semiconductor e-h generation / extraction
-> dark-event and waveform decision geometry
-> timing / spatial-search resources
-> repeated-use memory / correlation
-> one-shot / causal / thermodynamic closure.
```

Whether this **cross-layer resource ledger** is already present in photodetector literature as one coherent construction remains OPEN.

This is a synthesis question, not yet a theorem claim.

### B. Specific conditional tradeoff laws

Several Experiment-02 equations may be useful as detector-specific specializations, for example

```text
critical-matching control-floor threshold;
loss-constrained N laws;
mode-weighted constituent interpretation;
equal-D* event-decision counterexample;
retention/reset control-range relation.
```

Each equation requires a dedicated prior-art audit before any novelty language.

### C. Resource-constrained achievable detector-process region

The generic optimization

```math
\mathfrak C_D(R)
```

is mathematically natural and likely not new by itself.

A possible contribution would require the resource model `R` to encode **new, physically justified photodetector constraints** that lead to a nontrivial theorem, bound, impossibility result, or experimentally useful comparison that is not already contained in the established frameworks.

That remains OPEN.

---

## 13. Strongest safe statement after this audit

The strongest safe interpretation is currently:

> **Experiment 02 is not discovering a new general theory of statistical/quantum detector comparison. Established decision theory, quantum channel/process theory, and photodetector POVM/modeling literature already cover the broad formal layers. The remaining research opportunity, if any, is a narrower photodetector-specific synthesis or new physical resource constraint that produces nontrivial detector tradeoffs beyond those established frameworks.**

Status: **AUDIT CONCLUSION / NO NOVELTY CLAIM.**

---

## 14. Immediate next work

Do not write a manuscript.

Next:

1. audit the individual Experiment-02 quantitative tradeoff laws against cavity-QED, coherent absorption, photodetection, control, and detector-physics prior art;
2. inspect the Young/Sarovar/Léonard framework in detail and map which Experiment-02 resource coordinates it already contains;
3. compare van Enk's POVM-derived FOM tradeoffs against the task-specific metric/channel-ordering branch;
4. audit photodetection instruments/continuous measurement theory to determine whether persistent-record/readout dynamics are already naturally represented there;
5. only after that decide whether a genuinely distinct theorem/problem remains.

---

## 15. Primary-source list for the current audit

```text
D. Blackwell,
Equivalent Comparisons of Experiments,
Ann. Math. Statist. 24, 265-272 (1953),
DOI 10.1214/aoms/1177729032.

F. Buscemi,
Comparison of Quantum Statistical Models: Equivalent Conditions for Sufficiency,
Commun. Math. Phys. 310, 625-647 (2012),
arXiv:1004.3794,
DOI 10.1007/s00220-012-1421-3.

A. Jencova,
Comparison of quantum channels and statistical experiments,
IEEE Trans. Inf. Theory 62 (2016),
arXiv:1512.07016.

G. Chiribella, G. M. D'Ariano, P. Perinotti,
Theoretical framework for quantum networks,
Phys. Rev. A 80, 022339 (2009),
arXiv:0904.4483.

S. J. van Enk,
Photodetector figures of merit in terms of POVMs,
arXiv:1705.09640 (2017).

K. C. Young, M. Sarovar, F. Leonard,
General modeling framework for quantum photodetectors,
Phys. Rev. A 98, 063835 (2018),
arXiv:1811.08018,
DOI 10.1103/PhysRevA.98.063835.

K. C. Young, M. Sarovar, F. Leonard,
Fundamental limits to single-photon detection determined by quantum coherence and backaction,
Phys. Rev. A 97, 033836 (2018),
arXiv:1803.10558,
DOI 10.1103/PhysRevA.97.033836.
```

Before manuscript citation, verify complete bibliographic metadata and exact claims against the primary full texts.
