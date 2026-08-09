# Prior-Art Collision — Autonomous Detector Thermodynamics Starts After Capture

**Date:** 2026-08-08  
**Status:** major scope-defining prior-art collision; no novelty claim  

## 1. Source

E. Schwarzhans, T. J. G. Apollaro, I. Khomchenko, M. P. E. Lock, M. T. Mitchison, and M. Huber,

**“Quantum Detectors as Autonomous Machines: Assessing the Nonequilibrium Thermodynamics of Information Acquisition,”**

*PRX Quantum* **7**, 033001 (2026), DOI `10.1103/wm5p-tjtg`.

Published 1 July 2026.

---

## 2. What the paper already does

The paper constructs a self-contained autonomous quantum particle detector maintained in a nonequilibrium steady state.

Its model includes

- a work source implemented by a quantum thermal machine;
- a three-level gain medium with a metastable detection-ready state;
- coherent interaction with the quantum excitation to be detected;
- a thermal detection channel producing an amplified output;
- reset back to the detection-ready state.

It explicitly defines and studies

- detection efficiency;
- gain;
- detection jitter;
- dead time;
- steady-state dark count rate;
- entropy production.

The paper reports thermodynamic performance tradeoffs including increased dissipation for improved detector performance and inverse trends between dark counts and jitter/dead time in its model.

These topics are therefore **not open novelty targets** for this repository in generic form.

---

## 3. Their input excitation is already present

Their transient detection protocol does not begin with a propagating optical field incident on the detector.

The detector is first allowed to reach its nonequilibrium steady state. To model a detection event, the target system `S` is then conditioned/replaced into its excited state before the coupled detector dynamics are evolved.

Thus their efficiency is a **conditional post-capture detection/amplification efficiency** for an excitation that is already present in the target degree of freedom.

It is not an externally normalized spectral capture efficiency from a propagating optical channel.

---

## 4. The authors explicitly identify capture as outside their thermodynamic analysis

In their conclusion, the authors state that their thermodynamic analysis focuses on amplification after the particle has been captured and note that capture itself may carry additional costs and inefficiencies.

This is the most important prior-art boundary for the present repository.

It means that building another generic autonomous three-state/cyclic detector and rediscovering dark-count/dead-time/entropy tradeoffs would mostly duplicate a problem that has now been treated directly and recently.

---

## 5. What their paper does not supply

In the inspected paper, no incident-field spectral bandwidth figure of merit is formulated for the capture stage.

In particular, it does not derive

- capture probability as a function of incident optical frequency;
- a propagating-channel absorption/capture bandwidth;
- a broadband optical access budget;
- a Maxwell/passivity/Bode-Fano capture bound;
- a multimode integrated optical-to-detector transfer-area theorem;
- a composition from external optical capture to autonomous amplification/readout.

The word `bandwidth` does not appear as a detector performance metric in the inspected article text.

---

## 6. Relation to this repository

This repository approached the detector from the opposite side.

The strongest general finite-network result here is the capture/access statement

```math
\mathcal I_{L\to R}
\le
\frac{2LR}{L+R},
```

with

```math
L=\operatorname{Tr}\Gamma_L
```

the aggregate propagating optical access and

```math
R=\operatorname{Tr}\Gamma_R
```

the aggregate irreversible receiving-side access.

For a target angular-frequency band `W`,

```math
\overline T_B
\le
\frac{4\pi LR}{W(L+R)}.
```

The project then connected a known thermodynamic ceiling on one free-space optical channel to a minimum receiving-side access resource.

These results address **capture/access before amplification**, whereas Schwarzhans et al. explicitly focus on the thermodynamic detector machinery after capture.

---

## 7. Natural composition

The scientifically natural architecture is now

```text
propagating optical mode
        |
        v
capture / storage front end
        |
        v
excitation already present in S
        |
        v
autonomous amplification / readout / reset
        |
        v
registered macroscopic click.
```

This separates two efficiencies:

```math
\eta_{\rm cap}(\omega)
```

for capture from the propagating optical channel and

```math
\eta_D
```

for the conditional autonomous detector back end.

Under a serial architecture with no bypass and approximately frequency-independent back-end efficiency across the capture band,

```math
\boxed{
\eta_{\rm ext}(\omega)
=
\eta_{\rm cap}(\omega)\eta_D.
}
```

This composition is elementary; it is not itself a novelty claim.

Its value is that it identifies the missing interface between two existing bodies of theory.

---

## 8. Dark-count accounting must also be separated

Schwarzhans et al. define dark counts from the detector's nonequilibrium steady-state detection current in the absence of externally injected target excitations.

That is an **internal detector dark-count current**.

A real optical system can additionally generate counts from actual background photons entering through the accepted optical channel.

Therefore future work must distinguish

```text
internal autonomous-detector dark counts
```

from

```text
external thermal/background photon counts admitted by the capture bandwidth.
```

This distinction is consistent with the repository's earlier thermal-input-channel calculation.

---

## 9. Current novelty boundary

Do **not** claim novelty for

- autonomous detector thermodynamics;
- entropy-production versus efficiency tradeoffs;
- dark-count/jitter tradeoffs;
- dark-count/dead-time tradeoffs;
- metastable-state amplification;
- defining dark counts as a steady-state detector current;
- generic thermodynamic costs of reset/readout.

The potentially useful unexplored junction is narrower:

> **external propagating-mode capture bandwidth and access resources composed with an autonomous nonequilibrium detector back end.**

Whether this junction is genuinely unpublished remains to be established by a targeted prior-art search.

---

## 10. Direction change

Do not independently build the generic thermodynamic detector cycle that was planned before this collision.

Instead:

1. treat the 2026 autonomous-detector model as prior back-end theory;
2. retain the repository harmonic access theorem as front-end theory;
3. derive the clean serial capture-to-click composition;
4. distinguish external background counts from internal detector dark counts;
5. search specifically for prior work that already joins spectral optical capture to autonomous detector thermodynamics.

Only after that search should the project decide whether the capture-to-click bridge is a viable paper direction.