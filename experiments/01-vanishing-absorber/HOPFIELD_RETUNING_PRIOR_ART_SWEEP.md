# Prior-Art Sweep — Fixed-Target Hopfield Retuning No-Go

**Date:** 2026-08-08  
**Status:** targeted negative search result; **not proof of novelty or priority**  

## 1. Candidate statement being tested

The exact repository result in `HOPFIELD_RETUNING_NO_GO.md` is:

> In the TRK-consistent two-mode Hopfield model, hold the lower polariton at a fixed positive target frequency while the internal light-matter coupling `g -> infinity`. If the local optical and detector reservoir coupling scales remain fixed, then at least one dressed reservoir coupling tends to zero. Therefore peak optical-to-detector transfer and transfer linewidth cannot both remain bounded away from zero.

The search target is this **fixed-dressed-frequency retuning statement**, not generic deep-strong light-matter decoupling.

---

## 2. Search concepts used

Targeted searches combined variants of:

```text
Hopfield
fixed polariton frequency
fixed lower polariton
retuning / detuning
bath overlap
polariton linewidth
decay rate
deep strong coupling
light-matter decoupling
```

Searches were concentrated on primary journal/preprint sources rather than reviews.

---

## 3. Closest prior theory inspected

### Simone De Liberato — PRL 112, 016401 (2014)

**Light-Matter Decoupling in the Deep Strong Coupling Regime: The Breakdown of the Purcell Effect**

DOI `10.1103/PhysRevLett.112.016401`

Establishes that sufficiently deep strong coupling can lead to effective light-matter decoupling and reversal/collapse of the ordinary Purcell enhancement.

**Collision:** strong conceptual overlap with the asymptotic mechanism.

**Difference found in the inspected source:** not the fixed-target retuning theorem with two separately required local reservoir overlaps and the efficiency-or-bandwidth corollary.

---

### García-Ripoll, Peropadre & De Liberato — 2015

**Light-matter decoupling and `A^2` term detection in superconducting circuits**

arXiv `1410.7785`; Scientific Reports 5, 16055 (2015).

Shows that realistic minimal coupling and the diamagnetic `A^2` term can suppress spontaneous emission / produce effective decoupling from a waveguide.

**Collision:** directly supports the physical role of gauge-required self-interaction in preventing naive monotonic Purcell extrapolation.

**Difference found:** does not state the present fixed lower-polariton frequency retuning asymptotic with an independent detector reservoir.

---

### De Bernardis, Jaako & Rabl — PRA 97, 043820 (2018)

**Cavity Quantum Electrodynamics in the Nonperturbative Regime**

DOI `10.1103/PhysRevA.97.043820`

Develops nonperturbative cavity-QED treatment beyond the simple weak-coupling two-level picture.

**Collision:** strongly overlaps the need for a gauge-consistent full light-matter Hamiltonian.

**Difference found:** no inspected statement matching the fixed-target two-reservoir no-go.

---

### Mercurio et al. — PR Research 4, 023048 (2022)

**Regimes of Cavity QED under Incoherent Excitation: From Weak to Deep Strong Coupling**

DOI `10.1103/PhysRevResearch.4.023048`

Treats emission and dissipation across weak, ultrastrong, and deep-strong regimes using a gauge-consistent dressed treatment and studies light-matter decoupling.

**Collision:** close open-system physics and output-flux context.

**Difference found:** no fixed-target retuning theorem located in the inspected source.

---

### Palafox et al. — Journal of Physics: Photonics 7, 04LT02 (2025)

**Thermodynamic decoupling in the deep-strong coupling regime**

DOI `10.1088/2515-7647/ae1649`; arXiv `2510.20969`.

This is the closest algebraic source.

It uses the same two-mode Hopfield Hamiltonian with

```math
D=g^2/\omega_b
```

and derives dressed upper/lower polariton frequencies and local-bath decay rates. For fixed bare frequencies, both polariton decay rates fall asymptotically as `1/g` in deep strong coupling. The steady heat current between two local baths also vanishes as `1/g`.

**Collision:** the repository derivation directly uses this established dressed-rate framework.

**Difference found:** the inspected paper does not hold one dressed polariton at a fixed target frequency while co-varying `omega_c(g)` and `omega_b(g)`, nor state the resulting theorem that at least one of two required local reservoir couplings must vanish for every such retuning sequence.

Text searches of the accessible primary source found no matches for `fixed frequency`, `retun`, or `detun` in this sense.

---

### Hale et al. — Advanced Optical Materials (2026)

**Multi-Mode Deep Strong Coupling in a Multi Quantum Well Fabry-Perot Cavity**

DOI `10.1002/adom.71288`; arXiv `2508.19840`.

Reports/analyses multimode deep-strong coupling and light-matter decoupling using a multi-photonic, multi-electronic Hopfield model.

**Collision:** important evidence that decoupling is not merely an artifact of a single photonic mode.

**Difference found:** no inspected fixed-target two-reservoir asymptotic theorem.

---

## 4. Current novelty boundary

The following are **established prior physics and must not be claimed as new**:

- deep-strong light-matter decoupling;
- breakdown/reversal of the Purcell effect;
- the importance of the diamagnetic / self-interaction term;
- dressed/global master-equation treatment in ultrastrong and deep-strong coupling;
- polariton decay rates tending to zero at large coupling for fixed bare parameters in Hopfield-type models;
- suppression of heat transport at deep strong coupling;
- multimode light-matter decoupling.

The only presently distinct mathematical statement identified in this repository is the **fixed-target retuning corollary**:

```text
omega_y = omega_t fixed > 0,
g -> infinity,
gamma_L and gamma_R fixed

=> min(Gamma_L, Gamma_R) -> 0

=> peak transfer and transfer bandwidth
   cannot both stay bounded away from zero.
```

No inspected source was found stating this exact result.

That is a **negative search result, not evidence sufficient for a priority claim**.

---

## 5. Current verdict

**CANDIDATE DISTINCT SUPPORTING LEMMA — PRIORITY UNPROVEN.**

Do not call the theorem `new`, `first`, `fundamental`, or `universal`.

Before any publication claim, additional searches should include:

1. older polariton transport literature using Hopfield coefficients and detuning-dependent linewidths;
2. microwave/circuit implementations where bare frequencies are explicitly tuned while coupling changes;
3. mathematical literature on open coupled harmonic oscillators and transfer/scattering bandwidth;
4. multimode generalizations and reaction-coordinate mappings that may contain an equivalent asymptotic result in different notation.

The theorem is currently worth preserving because it closes a concrete counterexample to the detector thought experiment even if it ultimately proves to be known.