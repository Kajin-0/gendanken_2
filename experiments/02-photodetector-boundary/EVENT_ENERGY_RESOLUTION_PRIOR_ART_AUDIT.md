# Event-Energy Sensitivity Prior-Art Audit — Experiment 02

**Date:** 2026-08-12  
**Status:** direct detector prior-art collision; novelty rejected for full-NEP event-energy metric  
**Priority:** no novelty claim

This file supplements `DSTAR_TEMPORAL_PRIOR_ART_AUDIT.md`.

The Experiment-02 task-specific metric

```math
E_{\min}
\propto
\left[
\int\frac{|\tilde q(f)|^2}
{\mathrm{NEP}^2(f)}df
\right]^{-1/2}
```

was introduced as the natural known-waveform Gaussian event-energy scale.

A direct detector-literature audit shows that frequency-integrated NEP / optimum-filter energy resolution is already established in thermal/calorimetric detector theory.

---

## 1. Direct detector precedent

### Primary source

S. H. Moseley, J. C. Mather, and D. McCammon,

```text
Thermal detectors as x-ray spectrometers,
Journal of Applied Physics 56 (1984).
```

This classic work treats thermal detectors as energy-resolving spectrometers and derives optimum energy-resolution performance from the detector response and noise, rather than from a single low-frequency scalar sensitivity.

Related bolometer/calorimeter theory by Mather and later TES literature develops the same noise-weighted optimum-filter viewpoint.

Exact equation/convention metadata should be checked from the primary full text before manuscript citation.

---

## 2. Consequence for Experiment 02

The idea

```text
integrate the signal spectrum against inverse detector-noise spectrum
to obtain optimum event-energy resolution
```

is therefore **direct detector prior art**, not merely generic matched-filter prior art.

This blocks novelty claims for

```math
\mathcal K_D[q]
=\int |\tilde q(f)|^2/\mathrm{NEP}_D^2(f)df
```

or

```math
E_{\min}
\propto1/\sqrt{\mathcal K_D[q]}
```

as a new general event-energy detector metric.

---

## 3. What remains useful

The Experiment-02 one-pole relation

```math
\boxed{
d^2=E^2D^{*2}/(A\tau)
}
```

under the explicit conventional one-sided-NEP normalization remains a compact bridge between

```text
specific detectivity D*
and
optimum single-event energy discrimination.
```

Its pedagogical value is that it makes the missing temporal coordinate explicit for detector communities that commonly quote `D*` independently of response time.

But its underlying physics is standard optimum-filter detector theory.

---

## 4. Claim correction

### Previous possible interpretation

```text
A generalized event-energy detector metric emerges from the Gedanken experiment.
```

### Corrected interpretation

```text
The Gedanken experiment re-derives an established optimum-filter / energy-resolution structure and uses it to expose why scalar D* does not determine arbitrary transient-event performance.
```

Status:

**RE-DERIVED / DIRECT DETECTOR PRIOR ART / NO NOVELTY CLAIM.**

---

## 5. Implication for the broader project

This collision further reduces the plausible novelty space.

The project should not seek novelty in

```text
full-frequency NEP integration;
matched-filter pulse sensitivity;
minimum event energy;
energy resolution from detector noise PSD.
```

Those are established.

The remaining open question is increasingly whether **any specific cross-layer physical resource constraint** in Experiment 02 produces a genuinely new theorem or experimentally useful impossibility/design condition.
