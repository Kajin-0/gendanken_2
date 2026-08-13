# Experiment 02 Manuscript — Adversarial Referee Review, Round 2

**Date:** 2026-08-13  
**Target:** `MANUSCRIPT_DRAFT.md`  
**Review mode:** hostile but constructive scientific review  
**Current disposition:** **major revision**; viable as a conceptual/foundations or advanced-pedagogical article, not as a new general photodetection theory

---

## Executive assessment

The manuscript has a coherent question, a transparent Gedanken structure, and several technically useful counterexamples. Its main scientific strength is not a new formalism but the disciplined elimination of plausible intrinsic material boundaries for photodetection. The paper can become publishable if it is made narrower, more precise, and more explicit about the distinction between a physical measurement model and the semantic placement of a `detector` boundary inside a composite apparatus.

The draft is not yet submission-ready. The largest risks are conceptual overreach rather than algebraic error.

---

## Major comment 1 — the contribution must be framed as an elimination argument, not as a new definition theorem

The strongest defensible contribution is:

```text
candidate intrinsic boundary
-> counterexample
-> failure mode
-> missing architecture/task/resource specification
-> operational resolution.
```

The manuscript should not imply that it has discovered POVMs, instruments, quantum-to-classical channels, or task-dependent detector comparison. Those structures are established. The contribution is the photodetector-specific Gedanken chain connecting atomic excitation, semiconductor electron-hole generation, absorption, readout, and measurement architecture.

**Required revision:** state this contribution in the abstract, introduction, scope section, and conclusion. Remove language that sounds like a new general detector formalism.

---

## Major comment 2 — `detector endpoint` must not be mistaken for a fundamental microscopic quantum-to-classical transition

The draft currently uses a classical-outcome measurement channel to distinguish a detector endpoint from a coherent transducer. This is useful operationally, but it can be misread as asserting that a real detector contains a unique physical instant at which quantum dynamics becomes classical.

That is not required by POVM/instrument theory and would conflict with the paper's own conclusion that the system cut is movable.

The safe statement is:

> `Detector endpoint` denotes the level of description at which the measurement is declared complete and an outcome variable is exposed to the user or subsequent decision rule. This is an operational partition, not a claim of a unique fundamental classicalization event.

The outcome can be physically encoded in quantum degrees of freedom while being treated as an effectively classical record for the declared task.

**Required revision:** make this qualification explicit and remove any suggestion that entanglement breaking of the classical marginal identifies a unique material boundary in nature.

---

## Major comment 3 — downstream processing cannot create distinguishability

The sentence in Sec. II suggesting that a weak interaction can become measurable if the downstream readout is sufficiently sensitive is too loose.

For a fixed physical output state/channel, hypothesis-independent post-processing cannot increase distinguishability. In the quantum case, trace distance is contractive under CPTP maps; in the classical case, total variation distance obeys the analogous data-processing inequality.

A correct version is:

> A small but nonzero physical distinction can be exploited by an appropriate measurement, but downstream amplification or signal processing cannot create information absent from the physical output. Increasing interaction time, repeated probing, collective coupling, or another physical resource can increase the distinction before the final readout.

**Required revision:** correct the statement in Sec. II and ensure amplification is consistently described as making an existing distinction robust/readable rather than creating the original photon information.

---

## Major comment 4 — a single atom defeats a universal atom-count threshold only as part of a measurement architecture

The one-atom argument is correct in spirit but must be phrased carefully. A fluorescing atom plus an unmeasured emitted photon is not by itself a completed detector endpoint. Ionization followed by electron collection, or fluorescence followed by a measurement of the emitted field, is a measurement architecture containing one microscopic atom as the light-sensitive element.

**Required revision:** say `a single atom can be the active microscopic element of a detector architecture`, not `a single atom is intrinsically a detector`.

---

## Major comment 5 — remove the interaction-action bound from the main manuscript

The bound

```math
A_Delta >= hbar asin(1-2 epsilon)
```

is conditional on a specific pure-state relative-unitary construction and a precise definition of the interaction uncertainty/action. It is scientifically legitimate inside that model, but it is not needed for the manuscript's central argument and creates disproportionate referee burden.

The Tavis-Cummings example alone provides a cleaner conditional atom-number threshold:

```math
P_transfer(t)=sin^2(g sqrt(N) t),
```

so on the first transfer lobe a target useful-transfer probability `P_req` implies

```math
N >= [asin(sqrt(P_req))/(g tau)]^2.
```

Perfect transient transfer gives

```math
N >= (pi/(2 g tau))^2.
```

This directly demonstrates the paper's intended principle: an atom-number threshold appears only after coupling and interaction time are constrained.

**Required revision:** remove the interaction-action subsection from the main paper. Preserve it in the research record or a possible technical appendix.

---

## Major comment 6 — do not present `Gamma_match = 4G^2/kappa` as though it were the general result of the cited cavity-memory literature

The Experiment-02 constant-rate one-port model gives

```math
Gamma_match = 4 G^2 / kappa
```

under its own resonant Markovian assumptions. Dilley et al. establish impedance-matched single-photon capture using a time-dependent control field in a specific atom-cavity model. The physical family is clearly related, but the paper must not imply that the exact Experiment-02 constant-rate formula is quoted from Dilley et al.

**Required revision:** either remove the explicit formula from the main manuscript or label it unambiguously as `in the simplified one-port model used in the Gedanken analysis`. Cite Dilley only for the broader established principle that suitable impedance matching/control can enable complete photon-to-matter state mapping.

---

## Major comment 7 — tighten the D* / NEP convention and keep this as the primary engineering example

This is the strongest quantitative section for a detector audience, but the terminology should be exact.

The derivation assumes:

```text
- a short fixed-energy optical event;
- normalized one-pole signal response h(t)=(1/tau) exp(-t/tau) u(t);
- flat one-sided output-noise PSD S_n^(1);
- common Gaussian covariance;
- matched-filter readout;
- same active area;
- D* interpreted through a one-sided input-referred NEP amplitude spectral density.
```

To avoid dimensional ambiguity, call the quantity explicitly a one-sided input-referred **power-noise amplitude spectral density**, `NEP_ASD`, with units W/sqrt(Hz), and write

```math
D^* = sqrt(A) / NEP_ASD
```

under the stated 1-Hz normalization convention.

Then

```math
d^2 = E^2 D*^2/(A tau)
```

is a conditional benchmark, not a new definition of D*.

**Required revision:** put the convention in the equation text, not in a later caveat.

---

## Major comment 8 — demote the semiconductor thickness model

The generalized asymptotic model

```math
eta_s ~ S L^s,
mu_d ~ K L^p,
D(L) ~ S L^s exp(-K L^p)
```

and

```math
L_* ~ (s/(pK))^(1/p)
```

are clean. However, the model is deliberately reduced, and realistic SPAD/APD architectures can change both the coefficients and exponent through surface dark counts, tunneling, field-dependent collection, fixed timing windows, afterpulsing, and separate absorption/multiplication regions.

The main conceptual paper does not need a long device-optimization section.

**Required revision:** retain this only as a compact illustration or boxed example. Do not present `sqrt(v/(2 r_d A))` in the main manuscript as a design law.

---

## Major comment 9 — compress the Landauer discussion

The paper only needs to establish that `one detected photon -> k_B T ln 2 of heat` is not a universal identity.

Landauer concerns logically irreversible processing/erasure under specified thermodynamic assumptions; measurement correlation is not identical to erasure. Faist et al. further show that the work cost of a logical process depends on discarded information conditional on output and can require one-shot quantities.

The current section risks opening an entire thermodynamics paper inside a photodetection paper.

**Required revision:** reduce to one compact subsection. Avoid making stronger claims about globally closed cycles unless all reservoirs, side information, and work-storage systems are explicitly modeled.

---

## Major comment 10 — terminology correction from the original motivation

Absorption followed by later photon emission should be called fluorescence/spontaneous emission (or radiative recombination in the semiconductor context), not the external photoelectric effect.

Semiconductor electron-hole generation is one possible result of optical absorption; it is not the conceptual opposite of photon re-emission.

**Required revision:** make this clarification explicitly in the introduction or Sec. V because it resolves the original conceptual confusion that motivated the Gedanken experiment.

---

## Major comment 11 — remove the finite-size band-spacing heuristic unless it earns a citation and a clear role

The estimate

```math
delta E ~ 1/[g(E)V]
```

is a reasonable density-of-states heuristic, but the manuscript does not need it to show that band formation is not the measurement boundary. It risks distracting reviewers into debating finite-size solid-state crossover details.

**Required revision:** compress band formation to a qualitative statement or explicitly label the estimate heuristic and nonuniversal.

---

## Major comment 12 — citation correction

The current Jenčová reference is incorrect as a journal citation.

Directly verified publication:

```text
A. Jenčová,
"Comparison of quantum channels and statistical experiments,"
2016 IEEE International Symposium on Information Theory (ISIT),
pp. 2249-2253 (2016),
DOI: 10.1109/ISIT.2016.7541699.
Extended version: arXiv:1512.07016.
```

Do not list it as an IEEE Transactions on Information Theory paper.

---

## Minor comments

1. Prefer `intrinsic material boundary independent of the declared architecture` over `observer-independent boundary`.
2. Use `measurement outcome` rather than `classicalization event`.
3. Replace `the detector` with `the declared detector subsystem` when the system cut matters.
4. Define whether `D*` is low-frequency, white-noise, or frequency-dependent whenever used.
5. Avoid equating `record` with `persistent material state`; a transient accessible pulse may be a record for a sufficiently fast readout.
6. Make clear that QND detection defeats `absorption is necessary`, not that practical optical QND detection is easy.
7. The abstract should lose at least one quantitative example; two detailed formulas make the conceptual contribution look less focused.
8. The conclusion should state what was **not** established: no new POVM/instrument formalism, no universal resource lower bound, no universal detector ranking.

---

## Recommended revised structure

```text
I. Introduction and scope
II. Operational test: distinguishable accessible outcomes
III. Candidate intrinsic boundaries and counterexamples
    A. atom count / band formation
    B. absorption
    C. electron-hole generation
    D. persistent local memory / irreversibility
IV. Transducer versus declared measurement endpoint
V. Why conditional thresholds still arise
    A. Tavis-Cummings finite-time N threshold
    B. D* + temporal-response counterexample
    C. brief semiconductor thickness scaling illustration
VI. Thermodynamic reset: what Landauer does and does not say
VII. Relation to established theory / contribution boundary
VIII. Discussion and conclusion
```

This structure is shorter and makes the paper read as one argument rather than a collection of derived side branches.

---

## Referee recommendation after revision

If the above changes are made, I would reassess the manuscript as a possible **Perspective / Foundations / advanced pedagogical article**. I would still not recommend submission as a conventional original-theory Article unless the journal explicitly values conceptual syntheses or a narrow new theorem is added independently.
