# End-to-End Transport-Witness Trace Posterior

**Date:** 2026-08-10  
**Status:** conditional end-to-end uncertainty propagation from multi-distance packet observables to the translated-gradient mechanism parameter; synthetic central transport and provisional detector covariance; no novelty claim

## 1. Question

The previous witness-posterior calculation answered:

> how accurately must direct `v(E,x)`, `D(E,x)`, and `tau(E,x)` be known?

This file answers the more useful experimental question:

> **If a multi-distance Shockley–Haynes / pulse-transport witness has realistic trace-level timing, width, and amplitude errors, does its resulting posterior actually regularize the relocation inverse?**

The answer is yes in the current central model, with substantial margin.

---

## 2. More conservative lifetime model

The first direct-posterior stress used independent

```text
v(E,x) nodes
D(E,x) nodes
```

but only one lifetime amplitude per composition.

That could be overconfident if lifetime changes with field.

The current model therefore uses

```text
24 independent v nodes
24 independent D nodes
24 independent tau nodes
```

at

```text
x = 0.35, 0.43, 0.51
```

and

```text
E = 0.1, 0.3, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0 kV/cm.
```

All three transport surfaces can therefore vary with both field and composition in the posterior.

---

## 3. Multi-distance witness observables

Use the compact distance set

```math
\boxed{5,\ 10,\ 20,\ 40,\ 70,\ 100\ \mu{\rm m}.}
```

At each field, use the synthetic points retaining at least `5%` of the injected packet only as a design-SNR filter.

The regression observables are

```math
\langle t\rangle=t_0+L/v,
```

```math
\operatorname{Var}t=\sigma_0^2+2DL/v^3,
```

```math
\ln Q=\ln Q_0-L/(v\tau).
```

The intercepts absorb common

```text
time zero
pulse/electronics width
injection amplitude.
```

The slopes create the transport posterior.

---

## 4. Synthetic central transport is used only to compute sensitivity

Use the same reproducible central scale

```text
T = 300 K
mu = 9000 cm2/Vs
d = 8 kV/cm
r = 2.2
tau = 1 ns
D = mu kT/q only at the synthetic center.
```

Every `v`, `D`, and `tau` witness node is an independent nuisance direction in the relocation Fisher model.

Therefore the uncertainty propagation does **not** force the posterior to obey

```text
the empirical v(E) formula
Einstein diffusion
or field-independent lifetime.
```

---

## 5. Detector-side model

The relocation experiment uses

```text
feature centers = 2.6, 4.4, 5.6 um
lambda = 2.00-2.40 um
f = 0.5, 1, 2, 3 GHz
high-Cd optical entrance
low-Cd collection.
```

The first-passage solver uses the directly interpolated witness surfaces.

A free majority-band tilt coordinate and free entrance-surface-loss amplitude remain.

Every device/RF channel receives an arbitrary wavelength-independent phase and `ln|H|` intercept.

The detector covariance is still provisional:

```math
w=|H|\sqrt{P_{\rm abs}C_{\rm dc}},
```

with a weighted component-noise scale

```math
\sigma_{\rm comp}=0.10^\circ.
```

Thus all quoted `sigma` values remain **conditional Fisher scales**.

---

## 6. Velocity-only traces already reach the required scale

First ignore packet broadening and packet decay completely.

Use only the distance dependence of the packet centroid.

The resulting current mechanism significances are approximately:

| centroid RMS error per trace | mechanism scale |
|---:|---:|
| 25 ps | ~5.0 sigma |
| 50 ps | ~4.0 sigma |
| 75 ps | ~3.2 sigma |
| 100 ps | ~2.6 sigma |

Therefore the current `3 sigma` crossover occurs between approximately

```text
75 and 100 ps
```

of equal centroid error per distance trace under the synthetic central transport model.

This is significantly less demanding than trying to measure every high-field velocity point to a fixed percentage independently.

The multi-distance regression uses the entire field-dependent timing geometry.

---

## 7. Moderate whole-packet measurement gives a large margin

Use

```text
centroid RMS error = 25 ps
packet RMS-width error = 2 ps
sigma_lnQ = 0.10 per trace.
```

Propagate the resulting field-dependent slope errors independently to the 24 `v`, 24 `D`, and 24 `tau` witness nodes.

The current linearized mechanism scale is approximately

```math
\boxed{14\sigma.}
```

Again, this is not an expected experimental significance.

It shows that the witness posterior would be much tighter than the present minimum identifiability requirement if those trace-level errors are achievable.

---

## 8. A deliberately conservative whole-packet case still clears the threshold

Use

```text
centroid RMS error = 50 ps
packet RMS-width error = 5 ps
sigma_lnQ = 0.20 per trace.
```

The current mechanism scale remains approximately

```math
\boxed{6.9\sigma.}
```

under the same provisional detector covariance.

Thus the witness calibration does not require extremely precise packet-shape metrology to be scientifically useful in the current model.

---

## 9. Common calibration-scale biases do not dominate

A realistic witness can have correlated errors from

```text
distance scale
time-base calibration
pulse-width calibration
charge normalization.
```

To stress this, decompose each transport-family posterior into

```math
C
=\operatorname{diag}(\sigma_{\rm shape}^2)
+\sigma_{\rm common}^2\mathbf1\mathbf1^T.
```

Then take an intentionally enormous

```text
sigma_common = 10
```

in log units for the entire velocity, diffusion, and lifetime families.

The moderate whole-packet case changes only slightly, remaining near

```text
~14 sigma,
```

and the conservative case remains around

```text
~6.7 sigma.
```

This confirms the experimental-design intuition:

> **the relocation inverse needs the shape of transport versus field and composition much more than one absolute common scale.**

The multi-distance intercept/slope construction is therefore well matched to the inverse problem.

---

## 10. Why the velocity-only result does not make D and tau optional

Velocity-only calibration can cross the current linearized `3 sigma` threshold, but measuring the full packet remains the better experiment.

Reasons:

1. direct `D(E,x)` avoids forcing Einstein diffusion in the detector model;
2. direct `tau(E,x)` prevents recombination changes from masquerading as altered first-passage timing;
3. packet width and decay provide independent model-failure diagnostics;
4. the whole-packet posterior is much more robust to common velocity calibration errors;
5. a failed simple drift-diffusion packet model becomes visible immediately in the residual pulse shape.

Thus the practical target remains

```text
centroid + variance + charge
```

rather than centroid alone.

---

## 11. High-field D remains the hardest witness measurement

The end-to-end posterior agrees with the preceding multi-distance scale analysis.

Velocity centroid and lifetime amplitude slopes are comparatively easy.

At high field, diffusion adds only a modest variance slope on top of the common pulse/electronics width.

Therefore facility effort should preferentially improve

```text
packet-width stability
instrument impulse characterization
and/or the longest usable propagation distance
```

rather than chasing sub-picosecond centroid timing.

---

## 12. Current facility interpretation

The witness requirement can now be stated in trace-level terms.

### Minimum useful path

A multi-distance centroid experiment with roughly

```text
<=75 ps RMS centroid error per trace
```

already reaches the current linearized mechanism threshold in the synthetic central model.

### Preferred path

Aim approximately for

```text
centroid <=50 ps
packet RMS width <=5 ps
sigma_lnQ <=0.2
```

per trace.

That conservative case gives a substantial current posterior margin while remaining far less stringent than the earlier abstract `0.005 degree` detector-mode calibration problem.

---

## 13. What must replace these synthetic numbers in a real campaign

The following must be measured rather than inherited:

```text
actual p-type lifetime at 300 K
actual usable propagation distances
actual packet SNR versus field
actual impulse/pulse-width covariance
actual contact-field uniformity
actual field-dependent D and v
actual composition interpolation error.
```

The present calculation is a **facility-design feasibility check**, not a final error budget.

---

## 14. Next experimental-design step

The witness branch is now mature enough that another abstract Fisher refinement has lower value than a concrete device/facility design.

The next useful task is:

> **Specify a realistic witness mask/contact geometry and acquisition protocol for one HgCdTe growth facility, including propagation distances, optical injection spot, field-contact spacing, voltage/pulse limits, and how the packet centroid/variance/charge will be extracted.**

If no facility is yet selected, preserve the current generic multi-distance design and return to the main relocation experiment by propagating optical-profile and detector covariance uncertainty.

---

## 15. Numerical implementation

`numerics/hgcdte_transport_witness_trace_posterior.py`
