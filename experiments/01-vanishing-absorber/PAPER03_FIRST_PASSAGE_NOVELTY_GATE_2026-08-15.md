# Paper 03 Novelty Gate — Spatial First-Passage Semigroup and Cumulant Nulls

**Date:** 2026-08-15  
**Status:** **PRELIMINARY PRIMARY-SOURCE AUDIT / PRIORITY OPEN / NO MANUSCRIPT**  
**Candidate class:** detector-transport application of established stochastic-process mathematics

## 1. Candidate statement being tested

The mathematics itself is not claimed as new.

For scalar homogeneous regenerative successful first-passage transport over distance `d`, the repository uses

```math
T_{a+b}\overset d=T_a+T_b',
```

which implies a distance-parameter convolution semigroup

```math
E[e^{-sT_d}]=e^{-d\Phi(s)}.
```

When finite moments exist,

```math
\kappa_n[T_d]\propto d
```

for every order `n`, and therefore standardized cumulants obey

```math
\lambda_n(d)\propto d^{1-n/2}.
```

Uniform drift-diffusion specializes to inverse-Gaussian first passage with

```math
\kappa_n
=(2n-3)!!(2D)^{n-1}d/w^{2n-1}.
```

The only candidate paper claim is the detector-specific use of **multiple known generation depths as a parameter-free spatial semigroup/cumulant falsification test for carrier transport**.

A negative search result is not novelty evidence.

---

## 2. Observable discipline

This is a mandatory boundary.

The natural object is a successful collection/arrival-time observable

```math
U(d,s)=E[e^{-sT_d}],
```

or an independently reconstructed collection-time distribution.

It is **not automatically the raw terminal photocurrent**.

Primary transient-current theory explicitly warns that measured external current in a planar semiconductor contains electrode/displacement-current structure in addition to a naive carrier-arrival picture. Therefore a Paper-03 experiment must either

```text
measure/estimate the collection-time distribution itself;
```

or

```text
derive the map from terminal current to the required arrival observable under explicit device assumptions.
```

This prevents the earlier observable error that motivated the Shockley-Ramo correction in Paper 01.

---

## 3. Primary-source collision classes found in the first pass

### 3.1 Classical time-of-flight transport is deep prior art

Scher and Montroll's 1975 work on anomalous transit-time dispersion is a foundational continuous-time-random-walk treatment of dispersive transport in amorphous solids:

```text
H. Scher and E. W. Montroll,
"Anomalous transit-time dispersion in amorphous solids,"
Physical Review B 12, 2455 (1975).
```

This blocks any broad claim that using transit-time distributions or stochastic waiting-time models to diagnose semiconductor transport is new.

The later amorphous-semiconductor literature developed extensive time-of-flight interpretation for drift mobility, trapping, dispersive transport, and density-of-states inference.

### 3.2 Full transient shape is already used as spectroscopy

Seynhaeve et al. showed that the post-transit time-of-flight photocurrent can be used spectroscopically and, within their multiple-trapping model, related the post-transit current to a Laplace transform of the density of states:

```text
G. F. Seynhaeve, R. P. Barclay, G. J. Adriaenssens, and J. M. Marshall,
"Post-transit time-of-flight currents as a probe of the density of states in hydrogenated amorphous silicon,"
Physical Review B 39, 10196 (1989).
DOI: 10.1103/PhysRevB.39.10196
```

Therefore Paper 03 cannot claim that higher information in a transient, beyond a single transit time, is a new transport diagnostic.

### 3.3 Inhomogeneous fields are an established TOF confound

Published TOF work has explicitly shown that nonuniform electric fields can alter transient shapes and yield apparent mobility / density-of-states features that differ from the underlying transport:

```text
"Time-of-flight measurements in inhomogeneous electric fields,"
Journal of Non-Crystalline Solids 352, 1122-1125 (2006).
DOI: 10.1016/j.jnoncrysol.2005.12.045
```

This is relevant because a spatial-semigroup violation is not automatically evidence for exotic stochastic transport; ordinary field inhomogeneity is a candidate failure mechanism.

### 3.4 General current-transient theory already separates internal transport from measured current

A rigorous planar-device transient-current formalism has been published that emphasizes the role of electrode charge, internal space charge, and displacement current in translating carrier dynamics to measured current:

```text
"Theory of Current Transients in Planar Semiconductor Devices: Insights and Applications to Organic Solar Cells,"
Physical Review Applied 3, 044014 (2015).
DOI: 10.1103/PhysRevApplied.3.044014
```

This strengthens, rather than weakens, the need for the Paper-03 observable lock.

### 3.5 First-passage / inverse-Gaussian mathematics is established

The first-passage distribution of Brownian motion with constant drift is classical and is widely recognized as inverse Gaussian. Modern first-passage literature continues to use and extend these results.

Therefore neither

```text
inverse-Gaussian first passage
```

nor

```text
cumulants of a first-passage distribution
```

can carry novelty by themselves.

---

## 4. What the first pass did NOT locate

The initial targeted search did **not** locate a direct primary-source collision for the exact detector construction

```text
known set of generation depths d_m
+
reconstructed successful carrier-arrival distributions
->
test whether log Laplace/characteristic transforms are affine in d
->
test linear-in-d cumulants and standardized-cumulant power laws
->
use violations as parameter-free falsification of homogeneous scalar regenerative transport
->
only then fit a drift-diffusion or higher model.
```

This absence is only a reason to continue the audit. It is **not** evidence that the construction is novel.

---

## 5. Narrow candidate contribution after collisions

The candidate is now explicitly **not**

```text
TOF carrier transport;
transit-time distributions;
continuous-time random walks;
dispersive transport;
using transient shape to infer traps/DOS;
first-passage theory;
inverse-Gaussian drift-diffusion timing;
cumulants in stochastic transport;
nonuniform-field effects on TOF.
```

The narrower possible contribution is:

> **A depth-indexed, model-falsification hierarchy for successful carrier-arrival statistics in which spatial homogeneity/regeneration is tested first through convolution-semigroup and cumulant scaling laws, before assigning a microscopic transport model.**

This must still survive a much broader primary-source audit.

---

## 6. Strongest exact nulls worth auditing

### 6.1 Transform-affinity null

For equal depth increments `h`,

```math
\log U(d+h,s)-\log U(d,s)
```

must be independent of `d` for the scalar homogeneous regenerative class.

Equivalently, for three equally spaced depths,

```math
U_{m+1}^2=U_mU_{m+2}
```

at each transform coordinate `s`, subject to the observable and conditioning assumptions.

### 6.2 Cumulant linearity

For every finite cumulant,

```math
\Delta^2_d\kappa_n=0.
```

This gives parameter-free depth-curvature nulls separately for

```text
mean;
variance;
third cumulant;
fourth cumulant;
...
```

### 6.3 Standardized-cumulant scaling

For example,

```math
CV\propto d^{-1/2},
```

```math
\text{skewness}\propto d^{-1/2},
```

```math
\text{excess kurtosis}\propto d^{-1}.
```

These are spatial central-limit signatures of independent regenerative increments.

### 6.4 Drift-diffusion-specific ratios

The inverse-Gaussian hierarchy contains parameter-free relations among cumulants. These are a lower rung than a full parameter fit: the ratios can kill ordinary drift-diffusion even when mean/variance can be fit.

The exact ratios must be rederived and independently checked before manuscript use.

---

## 7. Next audit searches required

The first pass was not exhaustive. Before a GO decision, inspect primary literature under the following terminology, including older non-digital phrasing:

```text
moments of time-of-flight photocurrent;
moments / cumulants of carrier transit-time distribution;
transit-time dispersion moments;
distance scaling of TOF moments;
multiple sample thickness time-of-flight;
thickness scaling of photocurrent transient shape;
first-passage carrier collection semiconductor;
arrival-time distribution photodiode;
collection-time distribution photodiode;
Laplace transform transit-time semiconductor;
semigroup charge transport;
renewal / regenerative carrier transport;
inverse Gaussian carrier transit;
Wald distribution semiconductor transport;
method of moments transient photoconductivity.
```

Citation chains from Scher-Montroll, Marshall/Tiedje reviews, modern TOF chapters, and transient-current theory should be followed backward rather than relying only on keyword search.

---

## 8. Experimental architecture gate

A theory paper is not recommended until one credible measurement architecture is specified.

Potential architectures include

### A. Multiple physical generation positions

Use tightly localized excitation at known depths/positions in a detector or transport slab and reconstruct the collection-arrival distribution at each position.

### B. Spectrally encoded depth

Use a calibrated monotonic optical structure to move the generation distribution with wavelength, but only if the optical kernel can be deconvolved sufficiently to recover the required arrival observable.

### C. Multiple thickness samples

Use otherwise matched devices/slabs with multiple transport distances. This risks sample-to-sample nuisance variation but maps directly to the distance-semigroup question.

The measurement must report timing resolution, instrument-response deconvolution, censoring/failed-collection treatment, and enough repeated events to estimate higher cumulants without uncontrolled estimator bias.

---

## 9. Statistical feasibility gate

Higher cumulants are noise sensitive.

Before manuscript drafting, derive or simulate at minimum

```text
variance/bias of estimated kappa_2, kappa_3, kappa_4;
required number of independent events versus skewness/kurtosis;
instrument-response convolution bias;
timing quantization bias;
finite observation-window / right-censoring bias;
failed-collection conditioning bias;
correlated-event effects;
robust transform-domain alternatives when high moments are unstable.
```

A likely practical outcome is that transform-domain semigroup tests are statistically superior to direct fourth-cumulant tests. That should be determined rather than assumed.

---

## 10. Go/no-go decision

### GO to paper development only if

```text
[ ] focused primary-source audit finds no direct collision with the depth-indexed null hierarchy;
[ ] an arrival/collection observable can be defined without conflating terminal current;
[ ] at least one realistic measurement architecture is specified;
[ ] finite-sample statistics show useful power at credible event counts/timing precision;
[ ] ordinary confounds are mapped to specific null failures rather than called exotic transport;
[ ] the paper can state a falsifiable result stronger than "TOF distributions contain information".
```

### NO-GO if

```text
the hierarchy is already standard TOF moment analysis under different terminology;
```

or

```text
the required arrival distribution cannot be experimentally separated from the terminal-current observable without model assumptions as strong as the model being tested.
```

---

## 11. Current verdict

The first audit **reduces** the claim space substantially but does not yet kill the candidate.

The surviving object is narrow enough to justify further investigation:

```text
spatially indexed semigroup/cumulant null tests
for successful carrier-arrival statistics
as a model-falsification layer before microscopic fitting.
```

Status remains

> **PRIORITY OPEN / NO MANUSCRIPT.**