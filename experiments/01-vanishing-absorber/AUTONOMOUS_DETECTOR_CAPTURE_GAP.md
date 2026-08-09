# Prior-Art Boundary — Propagating-Field Detector Dynamics Versus Autonomous Detector Thermodynamics

**Date:** 2026-08-08  
**Status:** major scope-defining prior-art collision; targeted junction search negative so far; no novelty claim  

## 1. Two primary prior frameworks now define the boundary

### A. Young, Sarovar & Léonard — Physical Review A 98, 063835 (2018)

**“General Modeling Framework for Quantum Photodetectors.”**

This work treats

```text
quantized incoming photon field
+
optical absorption
+
internal detector dynamics
+
amplification / monitored states
```

as one coupled quantum system.

The paper explicitly models few-photon wavepackets incident on a subwavelength detector, defines detection efficiency, dark counts, jitter and latency, and allows the input pulse to be propagated through the detector's internal dynamics before a monitored output is registered.

Therefore the following are **not** novelty targets for this repository:

- joining a propagating quantum field to detector matter;
- modeling absorption and amplification in one quantum framework;
- defining efficiency/dark counts/timing from the incoming field and monitored detector states;
- saying that detector architecture affects these performance metrics.

The inspected framework does not provide an autonomous nonequilibrium thermodynamic accounting of the work source, heat currents, entropy production, or reset cost.

---

### B. Schwarzhans et al. — PRX Quantum 7, 033001 (2026)

**“Quantum Detectors as Autonomous Machines: Assessing the Nonequilibrium Thermodynamics of Information Acquisition.”**

This work constructs a minimal autonomous quantum particle detector maintained out of equilibrium by a quantum thermal machine.

It explicitly analyzes

- detection efficiency;
- gain;
- detection jitter;
- dead time;
- steady-state dark count rate;
- entropy production / dissipation.

Its transient protocol treats the target quantum excitation as already present in a two-level system coupled to the gain medium rather than deriving its capture from a propagating optical spectrum.

The authors explicitly identify capture as outside the thermodynamic stage they analyze and note that capture may bring additional costs and inefficiencies.

Therefore generic autonomous-detector thermodynamics, dark-count/dead-time/jitter tradeoffs, and thermodynamic reset/amplification costs are also **not** open novelty targets for this repository.

---

## 2. The prior-art box

The two frameworks cover complementary pieces:

```text
Young et al. (2018)
propagating quantum field
-> absorption
-> amplification / monitored output

Schwarzhans et al. (2026)
captured target excitation
-> autonomous nonequilibrium amplification
-> click current / reset
-> entropy production, dark counts, jitter, dead time
```

Thus the repository must not claim that either

```text
capture + amplification
```

or

```text
amplification + thermodynamic detector costs
```

is conceptually new.

---

## 3. The narrowed candidate junction

The remaining candidate gap is the **intersection**:

> **A propagating-field photodetector whose externally normalized spectral capture/access is constrained by passive electromagnetic resource bounds, while the amplification/readout/reset stage is itself an autonomous thermodynamic machine with explicit entropy production and internal dark counts.**

In schematic form,

```text
propagating optical continuum
        |
        v
causal/passive capture and storage
        |
        v
autonomous nonequilibrium detector machine
        |
        v
registered click
```

with the full theory retaining simultaneously

- incident-field normalization;
- capture probability versus optical frequency;
- capture bandwidth / integrated transfer;
- internal detector dark current;
- external thermal/background photons admitted through the capture band;
- jitter/dead time;
- thermodynamic work/heat/entropy resources.

---

## 4. What the targeted search found

A focused 2026 search was performed using combinations of

```text
photodetector
photon capture
input-output
propagating photon
bandwidth
thermodynamics
entropy production
autonomous detector
dark counts
```

and direct searches combining the titles/authors of the 2018 and 2026 frameworks.

The search recovered

- Young et al. (2018) as the major propagating-field / absorption / amplification framework;
- Schwarzhans et al. (2026) as the major autonomous thermodynamic detector framework;
- detector-specific experimental/theoretical work on bandwidth, blackbody-background counts, and dark-count statistics;
- quantum-measurement thermodynamic literature;
- input-output photon-counter models.

No inspected primary source was found that explicitly combines the **passive broadband capture/access constraint** with an **autonomous thermodynamic detector back end** in one source-resolved detector model.

This is a **negative search result only**. It is not proof of novelty or priority.

---

## 5. Relation to repository results

The repository's strongest front-end result is

```math
\boxed{
\mathcal I_{L\to R}
\le
\frac{2LR}{L+R}
}
```

for a finite passive strictly proper optical-to-receiving network, where

```math
L=\operatorname{Tr}\Gamma_L,
\qquad
R=\operatorname{Tr}\Gamma_R.
```

For a target angular-frequency band `W`,

```math
\boxed{
\overline T_B
\le
\frac{4\pi LR}{W(L+R)}.
}
```

The repository has also separated

```text
internal detector dark events
```

from

```text
real external thermal/background photons admitted by the optical acceptance band.
```

Those distinctions can be carried into a thermodynamically autonomous detector model.

---

## 6. Serial composition remains only a first diagnostic

`CAPTURE_TO_CLICK_COMPOSITION.md` uses the deliberately simple factorization

```math
\eta_{\rm ext}(\omega)
=
\eta_{\rm cap}(\omega)\eta_D.
```

This is useful for resource bookkeeping but is not the final model.

Young et al. already show that absorption and amplification can be dynamically coupled rather than artificially time-separated.

Therefore a publishable next step cannot merely multiply a capture efficiency by a back-end efficiency and call the result a unified detector theory.

The serial result should be retained as a limiting/reference case.

---

## 7. Current novelty boundary

Do **not** claim novelty for

- a quantum incoming-field photodetector model;
- coupling photon absorption to amplification;
- efficiency/dark-count/jitter definitions from quantum trajectories or monitored states;
- autonomous detector thermodynamics;
- entropy-production versus detector-performance tradeoffs;
- dark-count/jitter or dark-count/dead-time tradeoffs;
- generic capture-to-click efficiency factorization.

The only plausible unresolved target now is narrower:

> **a bandwidth/access-aware thermodynamic photodetector model in which propagating optical capture and autonomous detector energetics are treated consistently in the same resource accounting.**

Priority remains unproven.

---

## 8. Next decisive model

Do not build another generic three-state detector cycle.

Instead, build the minimum unified model that contains the missing intersection:

1. one explicitly normalized incident optical channel / few-photon wavepacket;
2. one or more capture states coupled to that channel;
3. an autonomous thermodynamic gain/readout subsystem rather than a phenomenological measurement operator;
4. thermal forward/reverse rates and an explicit work source;
5. a counted output channel;
6. external thermal photon occupation in the incident channel;
7. internal dark-count current with the incident field in vacuum;
8. an externally normalized spectral click probability `eta_ext(omega)`;
9. entropy production and dead-time/jitter observables from the same Liouvillian.

Then test whether the passive harmonic capture/access bound remains a valid upper envelope once the back end is dynamically coupled instead of represented by a serial black box.

Only if that survives should the project reassess publication potential.