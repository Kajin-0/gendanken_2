# Critical-Coupling / Capture Prior-Art Audit — Experiment 02

**Date:** 2026-08-12  
**Status:** primary-source audit; broad novelty rejected for critical-coupling branch  
**Priority:** unresolved; no novelty claim

This file audits the Experiment-02 branch

```text
collective coupling
-> coherent capture
-> irreversible record trap
-> traveling-wave impedance matching
-> finite bandwidth / control precision
-> constrained N thresholds.
```

The purpose is not to ask whether the algebra is correct; it is to ask whether the physical result is genuinely new after established cavity-QED, single-photon absorption, quantum-memory, and critical-coupling literature is credited.

---

## 1. Experiment-02 equations under audit

The internal-mode record model gives

```math
P_R
=\frac{4G^2\Gamma}
{(\kappa+\gamma+\Gamma)[4G^2+\kappa(\gamma+\Gamma)]}.
```

For `gamma=0`, optimization gives

```math
\Gamma_{\rm opt}=2G.
```

The clean one-port traveling-wave model gives

```math
\Gamma_{\rm match}=\frac{4G^2}{\kappa}
```

for unit resonant record conversion.

Writing

```math
x=\Gamma/\Gamma_{\rm match},
```

the clean resonant efficiency is

```math
\eta_R=\frac{4x}{(1+x)^2},
```

so

```math
1-\eta_R
=\left(\frac{x-1}{x+1}\right)^2.
```

A nonzero realizable rate floor `Gamma_floor` then gives the detector-specific corollary

```math
G^2
\ge
\frac{\kappa\Gamma_{\rm floor}}{4}
\frac{1-\sqrt\epsilon}{1+\sqrt\epsilon}
```

for target efficiency `1-epsilon`.

For identical microscopic couplings, `G^2=Ng^2` converts this into a conditional `N_min`.

---

## 2. Impedance-matched single-photon absorption is established

### Primary source

M. Dilley, P. Nisbet-Jones, B. W. Shore, and A. Kuhn,

```text
Single-photon absorption in coupled atom-cavity systems,
Physical Review A 85, 023834 (2012),
DOI 10.1103/PhysRevA.85.023834.
```

This work analyzes absorption of a single-photon wave packet by an atom coupled to a cavity and constructs the control needed for impedance-matched absorption / storage of the incident photon.

### Consequence for Experiment 02

The broad statement

```text
near-perfect traveling single-photon capture can result from matching external optical coupling to internal light-matter/storage dynamics
```

is established cavity-QED / quantum-memory physics.

The Experiment-02 one-port matching condition is therefore **not a credible novelty claim merely because it is written in detector-record language**.

---

## 3. Optical-depth-limited photon storage is established

### Primary source

A. V. Gorshkov, A. André, M. Fleischhauer, A. S. Sørensen, and M. D. Lukin,

```text
Universal Approach to Optimal Photon Storage in Atomic Media,
Physical Review Letters 98, 123601 (2007),
DOI 10.1103/PhysRevLett.98.123601.
```

Related papers in the same series develop optimal photon storage/retrieval in atomic media and show the central role of optical depth / cooperativity-type resources.

### Consequence for Experiment 02

The transition

```text
literal atom count
-> collective coupling / optical depth
```

is physically natural but not new.

The Experiment-02 statement that extended matter should be organized by mode-weighted oscillator strength / optical depth rather than raw total `N` is **strongly prior-art aligned**.

---

## 4. Collective bright-state coupling is established

The scaling

```math
G=g\sqrt N
```

for identical coherently coupled two-level systems is standard Dicke/Tavis--Cummings physics.

Likewise, for nonuniform coupling,

```math
G^2=\sum_j|g_j|^2
```

is the natural bright-superposition norm.

These are not Experiment-02 novelty.

---

## 5. Critical matching is standard input-output physics

The structure

```math
\eta(x)=\frac{4x}{(1+x)^2}
```

is the canonical algebraic form of two-rate matching / critical coupling.

The exact variables differ among cavities, resonators, absorbers, memories, and detector models, but the physical statement

```text
perfect on-resonance absorption/conversion when external and internal rates are matched
```

is established.

Therefore the Experiment-02 formula

```math
\Gamma_{\rm match}=4G^2/\kappa
```

should presently be classified as a **model-specific critical-coupling specialization**, not a new fundamental detector law.

---

## 6. The `Gamma_opt=2G` internal-mode result is probably a simple damped-transfer optimum

The result

```math
\Gamma_{\rm opt}=2G
```

for the clean internal-mode model comes from optimizing a two-state coherent-transfer process with irreversible trapping.

Its physical content is the familiar competition

```text
trapping too slow -> coherent return / loss;
trapping too fast -> overdamped / Zeno-like inhibition of transfer.
```

This broad phenomenon is established.

### Current claim status

The exact algebraic form is useful and checked, but there is currently **no basis for a novelty claim**.

A source-specific search for this precise minimal model may still be worthwhile if the equation is ever used as a standalone result, but it should be presumed prior-art-adjacent rather than novel.

---

## 7. Finite bandwidth as the cost of weak coupling is also established in quantum-memory/cavity physics

The Experiment-02 conclusion

```text
arbitrarily weak nonzero coupling can preserve peak resonant efficiency only by narrowing the useful bandwidth / increasing interaction time
```

is the ordinary time-bandwidth / cooperativity trade implicit in resonant storage and cavity capture.

It is conceptually important for killing an atom-count threshold, but not likely new physics.

---

## 8. Control-floor threshold is the most detector-specific algebraic corollary in this branch

The derived condition

```math
G^2
\ge
\frac{\kappa\Gamma_{\rm floor}}{4}
\frac{1-\sqrt\epsilon}{1+\sqrt\epsilon}
```

makes explicit what happens when the ideal matching rate cannot be made arbitrarily small.

This does add a useful engineering resource coordinate:

```text
minimum controllable irreversible rate / control resolution.
```

However, mathematically it follows immediately from the standard critical-coupling mismatch curve once a rate floor is imposed.

### Current status

**DERIVED DETECTOR-SPECIFIC COROLLARY / PRIORITY UNPROVEN / LOW NOVELTY EXPECTATION.**

It should not anchor a manuscript unless a real detector architecture supplies a nontrivial physically unavoidable `Gamma_floor` and the resulting bound is experimentally/design relevant in a way not already covered by control/critical-coupling literature.

---

## 9. Loss-constrained N laws are likewise reparameterizations unless the loss/resource model is new

Replacing

```math
G^2
```

by

```math
Ng^2
```

turns critical-coupling/cooperativity requirements into atom-count thresholds.

That is useful for returning to the original Gedanken question, but the `N` form does not by itself create new physics.

A meaningful contribution would require a new unavoidable microscopic bound on one or more of

```text
single-emitter coupling g;
mode volume;
bandwidth;
parasitic loss;
control-rate floor;
allowed optical architecture;
interaction time.
```

without leaving another compensating resource free.

---

## 10. Audit disposition

| Experiment-02 statement | Disposition |
|---|---|
| `G=g sqrt(N)` collective enhancement | **PRIOR ART** |
| `G^2=sum |g_j|^2` bright-mode weighting | **PRIOR ART / STANDARD STRUCTURE** |
| optical depth replacing literal N in extended media | **PRIOR ART** |
| perfect/near-perfect single-photon capture by impedance matching | **DIRECT PRIOR ART** |
| weak coupling traded against bandwidth/time | **PRIOR ART / STANDARD CONSEQUENCE** |
| finite optimum between coherent transfer and trapping | **PRIOR-ART-ADJACENT; NO NOVELTY CLAIM** |
| exact clean mismatch curve `4x/(1+x)^2` | **STANDARD CRITICAL-COUPLING ALGEBRA** |
| control-floor-induced `G_min` / `N_min` | **DERIVED COROLLARY; PRIORITY UNPROVEN; LOW NOVELTY EXPECTATION** |

---

## 11. Strongest safe scientific value of this branch

The branch remains valuable for the Gedanken experiment because it demonstrates, transparently, **why a universal atom-count threshold fails**:

```text
weak microscopic coupling can be traded against dwell time / bandwidth / optical architecture;
raw atom count gives way to collective mode overlap / optical depth;
finite loss or finite control constraints restore conditional thresholds.
```

That is a strong conceptual teaching/result chain even if its ingredients are established.

The branch should therefore be retained as **supporting physics**, not advertised as the likely novel center of the project.

---

## 12. Direction after this audit

The next quantitative branch to audit is the detector-decision result

```math
d^2=E^2D^{*2}/(A\tau)
```

and the stronger claim that equal conventional `D*` can imply unequal event-detection performance when temporal response differs.

That result may also be a straightforward matched-filter/time-bandwidth consequence. It needs direct comparison with conventional detector SNR/NEP bandwidth theory before any novelty is assigned.
