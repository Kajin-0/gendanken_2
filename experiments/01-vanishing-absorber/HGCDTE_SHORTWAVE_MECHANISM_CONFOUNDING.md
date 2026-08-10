# Short-Wave Mechanism Confounding — A Gradient-Region Timing Feature Can Be Mimicked by Near-Junction / Contact Transport

**Date:** 2026-08-09  
**Status:** conditional mechanism-identifiability stress using finite-RF complex response; simple physically motivated nuisance templates; no claim that any contact artifact is actually present; no novelty claim

## 1. Why detection is not enough

The short-wave branch was designed to make sample A's retained nonlinear/high-field region optically visible.

Suppose an A-specific wavelength × RF timing feature is successfully measured.

That still leaves the mechanism question:

> **Does the feature uniquely identify transport associated with the nonlinear composition-gradient region, or could a near-junction/contact change produce essentially the same response?**

This matters especially because prior HgCdTe transient studies show that metal-semiconductor contact effects, junction capacitance, trap filling, and carrier recombination can all alter transient waveforms.

Some of those contact-related transient signatures also vary with Cd composition and temperature.

Therefore the published A/B material contrast cannot be treated as automatically free of contact confounding.

---

## 2. Candidate target

Use the same illustrative sample-A nonlinear-region support as the preceding work:

```math
w_A(z)
\propto
[F_{\rm grad}(z)-F_{\rm lin}]_+.
```

The illustrative transport perturbation remains

```math
v(z)=10^5[1-0.25w_A(z)]\ {\rm m/s}.
```

This support is motivated by the location of the retained nonlinear composition-gradient field only.

It is **not** a claim that the real transport change is proportional to field.

---

## 3. Measurement space used for the mechanism test

Use the finite-RF complex Jacobian with

```text
lambda = 2.00-2.80 um
0.01 um wavelength spacing
f = 0.25, 0.50, 1.0, 2.0, 3.0 GHz
phase + log-magnitude
all 72 sample-A profile-family members
central sample-B optical envelope
baseline v0=1e5 m/s.
```

At each RF frequency remove an arbitrary wavelength-independent complex response before comparing mechanism fingerprints.

Thus a simple common chain phase/gain term is not being used to create artificial discrimination.

---

## 4. Smooth bulk nuisance templates

Instead of allowing arbitrary SVD modes, first use a very small physically interpretable bulk basis.

For sample A:

```math
1,
\qquad
z/L_A,
\qquad
(z/L_A)^2.
```

For sample B:

```math
1,
\qquad
z/L_B,
\qquad
(z/L_B)^2.
```

These represent broad uniform, linear-depth, and quadratic-depth transport changes.

With only these six smooth bulk nuisance directions, the principal angle from the candidate A nonlinear-region fingerprint to their span is already only

```math
\boxed{
0.060^\circ
\text{ to }
1.94^\circ
}
```

with median

```math
\boxed{0.159^\circ.}
```

Thus even simple smooth transport changes absorb most of the target fingerprint.

---

## 5. A single near-junction exponential already looks similar to the candidate

Represent an effective near-junction/contact-related transport response by

```math
\boxed{
q_c(z)\propto e^{-z/\ell_c}.
}
```

This is an **effective transport support template**.

It is not a claim that a physical metal-semiconductor interface extends `ell_c` into the HgCdTe.

Scan

```text
ell_c = 0.05, 0.10, 0.20, 0.30,
        0.50, 0.75, 1.00, 1.50, 2.00 um.
```

For every A-profile family member, find the single exponential whose full wavelength × RF complex fingerprint is closest to the nonlinear-gradient-region target.

The best single-contact-template angle is

```math
\boxed{
0.247^\circ
\text{ to }
3.60^\circ
}
```

with median

```math
\boxed{1.26^\circ.}
```

The best effective scale is always

```text
0.50 or 0.75 um
```

for the current 72-profile family.

This is not an exact degeneracy, but it is already close enough that mechanism attribution would require much more than simply detecting a short-wave phase feature.

---

## 6. One contact term plus ordinary bulk changes nearly reproduces the candidate exactly

Now allow

```text
A quadratic smooth bulk basis
B quadratic smooth bulk basis
+
one A near-junction exponential.
```

### `ell_c = 0.50 um`

The target-to-nuisance principal angle becomes

```text
minimum ~0.00038 deg
median ~0.0142 deg
maximum ~0.0896 deg.
```

### `ell_c = 0.75 um`

```text
minimum ~0.00022 deg
median ~0.0080 deg
maximum ~0.115 deg.
```

Thus a **single** physically simple near-junction nuisance template, when combined with ordinary smooth A/B transport changes, can reproduce the candidate nonlinear-gradient-region complex timing fingerprint to extremely high accuracy.

This remains true even after adding RF-frequency diversity through `3 GHz` and using both phase and magnitude.

---

## 7. What can and cannot be inferred from a detected A-specific feature

A successful short-wave experiment may support

> **an additional near-junction transport response is required in sample A.**

It does **not**, from timing data alone, establish

> **that the response is caused specifically by the nonlinear composition-gradient field.**

The spectral/RF inverse does not have enough spatial/mechanism resolution to distinguish the candidate gradient support from a generic near-junction transport/contact contribution once reasonable smooth nuisance terms are allowed.

This is a stronger limitation than statistical phase precision.

It is a structural mechanism-identifiability limit.

---

## 8. Why the published A/B pair is not a perfect contact control

The 2023 published samples were deliberately processed to retain different portions of the composition profile.

The current sample-A sensitivity family consequently permits a much higher collection-side Cd composition than the smooth sample-B envelope.

Meanwhile earlier HgCdTe transient-photovoltage work reports that metal-semiconductor/contact-induced transient behavior changes with Cd composition and temperature.

Therefore

```text
sample A has nonlinear gradient
sample B does not
```

is not the only physical difference that can affect a near-junction transient.

Their collection-side semiconductor/contact environments are not guaranteed to be dynamically identical.

Paired A/B subtraction remains useful, but it is not a definitive mechanism-control experiment for contact-versus-gradient attribution.

---

## 9. Consequence — a purpose-built matched-contact pair is the cleaner validation experiment

The strongest validation device pair would preserve, as closely as possible,

```text
same collection-side composition/cap layer
same junction geometry
same doping near the junction
same metallization/contact process
same package/readout
same total optical entrance conditions
```

while changing primarily

```text
the buried/internal composition-gradient structure of interest.
```

Conceptually:

### Control device

```text
identical front/junction/contact stack
smooth internal grading
```

### Contrast device

```text
identical front/junction/contact stack
same outer dimensions as far as practical
+
a buried nonlinear-gradient region placed where the spectral encoder has leverage.
```

That is a much stronger causal test than relying solely on the existing published A/B pair.

---

## 10. This also suggests a device-design problem

The published sample-A nonlinear region happens to lie close to the collecting boundary, where the survival-kernel inverse is least sensitive and contact confounding is strongest.

A purpose-built validation structure could deliberately move the distinguishing buried gradient region farther from the contact while keeping the front stack matched.

That may improve three things simultaneously:

```text
spectral differential visibility
separation from boundary/common-delay gauge
separation from contact/interface artifacts.
```

This is now a more interesting design variable than simply adding more wavelengths or RF frequencies.

---

## 11. Hard claim boundary after this test

Do not claim, from the proposed short-wave timing inverse alone,

```text
we measured the nonlinear composition-gradient transport profile
```

or

```text
the A-B timing difference proves the gradient field caused the change.
```

The strongest defensible statement without additional control is closer to

> **the data require an A-specific near-junction differential transport component consistent with, but not unique to, the retained nonlinear-gradient region.**

Specific attribution requires independent contact/interface validation or a matched-contact structure.

---

## 12. Next decisive direction

The highest-value next numerical design problem is no longer the published sample-A geometry itself.

It is:

> **Where should a buried nonlinear-gradient perturbation be placed in a matched-contact graded-HgCdTe validation structure to maximize spectral/RF distinguishability from contact and smooth-bulk nuisances?**

That converts the mechanism-confounding failure into a constructive experimental-design problem.

A useful first calculation should sweep the center/depth/width of a localized transport-support feature while keeping the collection-side stack fixed, then optimize the wavelength band for the worst-case principal angle against

```text
contact exponential
smooth A/B bulk terms
common phase
and measured electrical response.
```

Numerical implementation for the present confounding test:

`numerics/hgcdte_shortwave_mechanism_confounding.py`
