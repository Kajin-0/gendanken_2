# Semiconductor Decision Bridge — Experiment 02

**Date:** 2026-08-12  
**Status:** active conditional derivation  
**Priority:** unassessed; no novelty claim

This file returns the abstract detector-boundary program to the original semiconductor question:

> If a photon is absorbed and creates an electron-hole pair, when does that become detection?

The goal is to express the entire path from incident photon to binary readout in one minimal decision model.

---

## 1. Separate the stages

For a simple semiconductor slab, define

```text
eta_mode = optical coupling / interface / mode-overlap factor
P_abs    = probability the incident photon is absorbed in the active region
eta_eh   = probability an absorbed photon creates the relevant mobile/useful excitation
P_col    = probability that excitation is separated/collected before being lost
P_read   = probability the collected event produces the chosen persistent/readable record
```

Then define the signal-click probability per incident photon

```math
\boxed{
\eta_s
=\eta_{\rm mode}P_{\rm abs}\eta_{eh}P_{\rm col}P_{\rm read}.
}
```

This is a deliberately factorized minimal model. Correlated pathways, gain, carrier multiplication, trapping/re-emission, interference, multiple passes, etc. can violate the simple product structure.

Its conceptual purpose is to enforce

```text
absorption
!= electron-hole creation
!= useful carrier separation
!= persistent record
!= successful decision.
```

---

## 2. Optical-depth contribution

For a noninterfering single-pass slab,

```math
P_{\rm abs}
=1-e^{-\alpha L},
```

where

```text
alpha = absorption coefficient
L     = active optical thickness.
```

Thus

```math
\boxed{
\eta_s
=\eta_{\rm mode}
(1-e^{-\alpha L})
\eta_{eh}P_{\rm col}P_{\rm read}.
}
```

This already replaces total atom count by an optical-depth resource `alpha L`.

---

## 3. Minimal carrier-collection race

If a useful excitation faces two independent exponential hazards,

```text
Gamma_ext = desired extraction / separation / collection rate
Gamma_rec = unwanted recombination / loss rate,
```

then

```math
\boxed{
P_{\rm col}
=\frac{\Gamma_{\rm ext}}
{\Gamma_{\rm ext}+\Gamma_{\rm rec}}.
}
```

Equivalently, with characteristic times

```math
\tau_{\rm ext}=1/\Gamma_{\rm ext},
\qquad
\tau_{\rm rec}=1/\Gamma_{\rm rec},
```

```math
\boxed{
P_{\rm col}
=\frac{1}
{1+\tau_{\rm ext}/\tau_{\rm rec}}.
}
```

This is the simplest explicit answer to the question

> when does an electron-hole pair become useful charge?

It becomes likely to contribute to a detector record when extraction/separation wins the dynamical race against recombination/loss.

But this is still only one stage of detection.

---

## 4. Add dark records

Let dark clicks occur as an independent Poisson process of rate

```math
R_d.
```

Choose an observation window `tau`.

Under the no-photon hypothesis `H0`, the probability of at least one dark click is

```math
\boxed{
p_0
=1-e^{-R_d\tau}.
}
```

Under the one-photon hypothesis `H1`, assume the signal produces a click with probability `eta_s`, independently of the dark process.

The probability of no click under `H1` is

```math
(1-\eta_s)e^{-R_d\tau},
```

so

```math
\boxed{
p_1
=1-(1-\eta_s)e^{-R_d\tau}.
}
```

Here `p_0` and `p_1` are the click probabilities under the two hypotheses.

---

## 5. Exact binary distinguishability of the click record

For a binary output `Y in {no click, click}`, the total-variation distance between the two output distributions is simply

```math
|p_1-p_0|.
```

Substitution gives

```math
\boxed{
\mathcal D_{\rm click}
=\eta_s e^{-R_d\tau}.
}
```

For equal priors, the optimum error using this binary record is

```math
\boxed{
P_e
=\frac12
\left(1-\eta_s e^{-R_d\tau}\right).
}
```

This is an especially useful bridge between the abstract trace-distance formulation and a practical detector click model.

The result says that detector discrimination is degraded by two logically separate failures:

```text
signal does not produce the chosen record
and/or
a dark record destroys the evidential value of a click.
```

---

## 6. Full minimal semiconductor expression

Combining the previous stages,

```math
\boxed{
\mathcal D_{\rm click}
=
\eta_{\rm mode}
(1-e^{-\alpha L})
\eta_{eh}
\frac{\Gamma_{\rm ext}}
{\Gamma_{\rm ext}+\Gamma_{\rm rec}}
P_{\rm read}
\,e^{-R_d\tau}.
}
```

Therefore

```math
\boxed{
P_e
=\frac12\left[
1-
\eta_{\rm mode}
(1-e^{-\alpha L})
\eta_{eh}
\frac{\Gamma_{\rm ext}}
{\Gamma_{\rm ext}+\Gamma_{\rm rec}}
P_{\rm read}
\,e^{-R_d\tau}
\right].
}
```

This formula is **CONDITIONAL** on the simple independent-stage / binary-click model. It is not claimed as a universal detector equation.

Its conceptual value is that every stage now has a distinct physical meaning.

---

## 7. A sharp impossibility condition from dark events

Target equal-prior error

```math
P_e\le\epsilon
```

requires

```math
\eta_s e^{-R_d\tau}
\ge 1-2\epsilon.
```

Since `eta_s <= 1`, a necessary condition is

```math
\boxed{
e^{-R_d\tau}
\ge 1-2\epsilon.
}
```

Equivalently,

```math
\boxed{
R_d\tau
\le
-\ln(1-2\epsilon).
}
```

For small `epsilon`,

```math
\boxed{
R_d\tau\lesssim2\epsilon.
}
```

Thus no amount of absorption, atom number, gain, or carrier collection can reach the target binary decision error if the expected number of dark events in the decision window is too large.

This is the detector analogue of the optical escape ceiling found in `TRAVELING_WAVE_CAPTURE.md`.

---

## 8. Optical-depth requirement including dark events

Define

```math
\eta_{\rm int}
=\eta_{eh}
P_{\rm col}
P_{\rm read}.
```

Then the target condition is

```math
\eta_{\rm mode}
(1-e^{-\alpha L})
\eta_{\rm int}
e^{-R_d\tau}
\ge 1-2\epsilon.
```

Provided the right-hand-side demand is below the non-absorption ceiling,

```math
\frac{(1-2\epsilon)e^{R_d\tau}}
{\eta_{\rm mode}\eta_{\rm int}}<1,
```

we get

```math
\boxed{
\alpha L
\ge
-\ln\left[
1-
\frac{(1-2\epsilon)e^{R_d\tau}}
{\eta_{\rm mode}\eta_{\rm int}}
\right].
}
```

If

```math
(1-2\epsilon)e^{R_d\tau}
\ge
\eta_{\rm mode}\eta_{\rm int},
```

then increasing optical thickness without bound cannot satisfy the target.

Again, more absorber cannot repair a downstream record problem.

---

## 9. Carrier-rate requirement

Suppose all other factors are fixed and define the required collection probability

```math
P_{\rm col}\ge P_*.
```

From

```math
P_{\rm col}
=\frac{\Gamma_{\rm ext}}
{\Gamma_{\rm ext}+\Gamma_{\rm rec}},
```

we obtain

```math
\boxed{
\frac{\Gamma_{\rm ext}}{\Gamma_{\rm rec}}
\ge
\frac{P_*}{1-P_*}.
}
```

or

```math
\boxed{
\frac{\tau_{\rm rec}}{\tau_{\rm ext}}
\ge
\frac{P_*}{1-P_*}.
}
```

For high collection probability `P_*=1-delta`,

```math
\frac{\Gamma_{\rm ext}}{\Gamma_{\rm rec}}
\gtrsim\frac{1}{\delta}.
```

Thus the semiconductor detector boundary contains another rate ratio, directly analogous to the collective-coupling/loss ratios in the microscopic model.

---

## 10. Where electron-hole pair generation sits

The original question can now be answered very precisely in this model.

Photon absorption can produce an electron-hole excitation:

```text
incident photon
-> absorption
-> electron-hole excitation.
```

But detection requires subsequent successful branches:

```text
electron-hole excitation
-> survives binding/recombination/trapping losses
-> charge separation / collection
-> readable record
-> decision distinguishable from dark output.
```

So

```math
\boxed{
\text{electron-hole generation is a transduction event, not by itself the detector boundary.}
}
```

It is the semiconductor-specific microscopic encoding stage inside the broader record-formation chain.

---

## 11. New detector coordinates

The minimum model is naturally described by dimensionless quantities such as

```math
\boxed{
\alpha L,
\qquad
\frac{\Gamma_{\rm ext}}{\Gamma_{\rm rec}},
\qquad
R_d\tau,
\qquad
\eta_{\rm mode}\eta_{eh}P_{\rm read}.
}
```

The detector boundary is therefore a surface in this space.

Increasing one coordinate cannot always compensate for another:

```text
alpha L -> infinity cannot overcome excessive dark events;
alpha L -> infinity cannot overcome zero collection probability;
infinite collection cannot recover photons never coupled into the absorber;
gain cannot recover information lost before the record exists.
```

This is a much stronger structure than a single threshold in atom count.

---

## 12. Connection to conventional detector metrics

The present model is event-based rather than small-signal/noise-spectral-density based.

Nevertheless it provides a conceptual route to conventional metrics:

```text
external quantum efficiency
<-> eta_s before dark-event penalty

dark-count rate
<-> R_d

timing window / jitter
<-> choice and uncertainty of tau

carrier lifetime / transit time
<-> Gamma_rec and Gamma_ext

absorptance / optical thickness
<-> alpha L.
```

NEP and `D*` compress different combinations of signal response, noise density, area, and bandwidth and therefore should not be treated as the fundamental detector boundary without additional assumptions.

That comparison should be developed separately so this experiment does not inherit the conventions of one detector architecture as axioms.

---

## 13. Strongest current physical answer

For an ordinary semiconductor detector, a useful concise hierarchy is now

```text
optical access
-> absorption (alpha L)
-> electron-hole excitation
-> carrier survival / separation (Gamma_ext/Gamma_rec)
-> persistent readout record
-> discrimination against dark events (R_d tau).
```

The boundary is not the point where atoms first form bands, nor the point where a photon first creates an electron-hole pair.

It is the region where the **entire chain** preserves enough information to meet the demanded decision error.

---

## 14. Next attack

The most natural next questions are:

1. Replace the ideal binary click record with a continuous noisy electrical output and derive the detector-state distinguishability for Gaussian current/voltage noise.
2. Determine how responsivity, NEP, `D*`, bandwidth, integration time, and dark noise appear as projections of the same hypothesis-discrimination problem.
3. Ask whether two detectors with identical conventional `D*` can occupy very different positions in this decision-performance space because their temporal response differs.

The third point links naturally to a separate ongoing thought experiment, but it should be imported only if doing so clarifies this experiment rather than conflating projects.
