# Companion HgCdTe Transport Witnesses — Calibrating \(v(E)\), \(D(E)\), and τ Before the Relocation Test

**Date:** 2026-08-10  
**Status:** experimental-control design based on established HgCdTe Shockley–Haynes / impulse-response metrology; exact geometry, doping, contacts, and temperature program remain to be specified with a fabrication facility; no novelty claim

## 1. Why this calibration is now the highest-value experiment

The purpose-built translated-gradient structures produce a large physics-derived wavelength × RF transport signal in the downstream drift–diffusion model.

The remaining attribution question is narrower:

> **Is the measured depth-dependent response caused by the localized composition-gradient field, or can an incorrectly assumed generic minority-electron velocity law reproduce it?**

The corrected inverse no longer needs an arbitrary unconstrained transport law if that law is measured independently.

HgCdTe already has an established precedent for exactly this type of measurement.

Rothman et al., *Journal of Electronic Materials* **39** (2010), DOI `10.1007/s11664-010-1247-8`, used Shockley–Haynes measurements in p-type HgCdTe to estimate

```text
minority-electron drift velocity
minority-electron diffusion coefficient
and lifetime
```

as functions of electric field.

Therefore this calibration should be treated as a **standard control measurement**, not part of the candidate novelty.

---

## 2. Why one witness composition is insufficient

The purpose-built graded absorber spans

```text
x_front ~0.55
x_back  ~0.32.
```

More importantly, the **localized high-gradient segment itself** spans a substantial composition interval that changes with its translated depth.

For the current three-depth quasi-neutral design:

### feature center `2.6 um`

```text
feature x range ~0.392-0.517
center x ~0.454.
```

### feature center `4.4 um`

```text
feature x range ~0.363-0.488
center x ~0.424.
```

### feature center `5.6 um`

```text
feature x range ~0.344-0.469
center x ~0.406.
```

The union of the high-gradient regions is therefore approximately

```math
\boxed{x\approx0.344-0.517.}
```

A single uniform-composition witness would force an unvalidated assumption that the velocity law is composition independent over that whole range.

Published HgCdTe APD fits already show that the empirical mobility / saturation-field parameters vary with Cd composition.

---

## 3. Minimal three-composition witness set

Use approximately

```math
\boxed{x=0.35,\ 0.43,\ 0.51.}
```

These values

```text
bracket the actual high-gradient feature range
+
place one witness near the middle
+
permit a direct check of whether interpolation in x is adequate.
```

The middle witness is scientifically important.

With only two endpoint compositions, any linear interpolation fits by construction.

The third point tests whether

```text
mu(x)
d(x)
r(x)
D(x)
and tau(x)
```

are sufficiently smooth for the relocation forward model.

If the middle witness violates the interpolation uncertainty budget, add more compositions rather than forcing a low-order fit.

---

## 4. Optical scale of the three witnesses

Using the Hansen gap at 300 K:

```text
x=0.35 -> Eg ~0.358 eV -> lambda_g ~3.46 um
x=0.43 -> Eg ~0.467 eV -> lambda_g ~2.66 um
x=0.51 -> Eg ~0.579 eV -> lambda_g ~2.14 um.
```

This gives a practical guide for selecting above-gap pulsed excitation while retaining composition selectivity.

The calibration laser wavelength does **not** have to equal the relocation experiment wavelength.

Its role is to create a localized minority-electron packet whose motion under known lateral field can be measured.

---

## 5. A practical first geometry

A useful first scale is a p-type lateral transport bar with approximately

```text
minority-electron drift path ~100 um
same intended acceptor doping scale as the relocation absorber
same surface/passivation process as far as practical
localized pulsed optical injection
separate collection contact downstream.
```

The exact Shockley–Haynes contact geometry should follow the facility's proven implementation rather than this conceptual sketch.

The `100 um` length is chosen because it converts the relevant field range into convenient voltages and timing.

---

## 6. Relevant field window

The current purpose-built gradient structure produces approximately

```text
background quasi-neutral gap-force scale ~0.2 kV/cm
localized feature scale ~1.9 kV/cm.
```

The calibration should therefore span at least

```math
\boxed{0.1-3\ {\rm kV/cm}.}
```

This brackets the actual interior force scale with margin on both sides.

For a `100 um = 0.01 cm` drift length:

```text
0.1 kV/cm -> 1 V
0.3 kV/cm -> 3 V
1.0 kV/cm -> 10 V
2.0 kV/cm -> 20 V
3.0 kV/cm -> 30 V.
```

Use pulsed operation or an appropriate duty cycle if self-heating becomes relevant.

---

## 7. Expected timing scale

For the empirical velocity law

```math
v(E)=\frac{\mu E}{1+(E/d)^{2.2}},
```

stress the broad envelope

```text
mu = 4,000-20,000 cm2/Vs
d  = 4-12 kV/cm.
```

For a 100-um drift path, the corresponding transit-time envelope is approximately

| field | voltage across 100 um | transit-time envelope |
|---:|---:|---:|
| 0.1 kV/cm | 1 V | 5-25 ns |
| 0.3 kV/cm | 3 V | 1.7-8.4 ns |
| 1.0 kV/cm | 10 V | 0.50-2.62 ns |
| 2.0 kV/cm | 20 V | 0.25-1.52 ns |
| 3.0 kV/cm | 30 V | 0.17-1.28 ns |

Thus the calibration naturally spans

```text
slow nanosecond transport at low field
through
sub-nanosecond transport near the highest feature field.
```

Modern HgCdTe impulse measurements already use multi-GHz instrumentation; room-temperature SWIR APDs have been characterized with a 16-GHz impulse setup.

So the timing scale is not obviously instrument limited.

---

## 8. What to extract from a Shockley–Haynes trace

For each composition and field, measure at multiple propagation distances if possible.

### Packet centroid / arrival time

Gives the drift velocity:

```math
\boxed{v(E,x)=\Delta z/\Delta t.}
```

Using two or more propagation distances removes an arbitrary optical/electrical time-zero offset.

### Packet temporal broadening

Constrains the diffusion coefficient.

For a simple drift-diffusion packet, the width growth with propagation gives an estimate of

```math
D(E,x).
```

Do not force Einstein equilibrium if the measured diffusion mobility differs from drift mobility; the 2010 HgCdTe measurements explicitly observed hot-electron diffusion behavior.

### Packet amplitude / collected charge versus propagation

Constrains the effective minority-carrier lifetime and loss:

```math
\tau(E,x)
```

once collection/contact effects are independently de-embedded.

---

## 9. Do not overfit one analytic velocity law

The current inverse uses

```math
v(E)=\mu E/[1+(E/d)^r]
```

because it is compact and has direct HgCdTe precedent.

The calibration experiment should **not** be designed merely to estimate `mu,d,r` at all costs.

First plot the measured

```text
v(E)
D(E)
tau(E)
```

directly.

Then compare

```text
low-field linear mobility
empirical saturation law
monotone spline / Gaussian-process interpolation
or another physically justified constitutive model.
```

If the simple law fails, the relocation model should use the measured interpolation rather than force a misleading closed form.

---

## 10. What precision is actually needed?

The current linearized relocation calculation is reassuring.

If the velocity-law parameters `d` and `r` are allowed completely unbounded amplitudes, mechanism attribution is nearly singular.

But imposing only very broad scale constraints

```text
sigma_ln(d) ~0.7  (roughly factor 2 per sigma)
sigma_r ~0.5
```

already removes that artificial singularity in the central model.

These are much looser than a well-executed direct transit experiment should be capable of providing.

Therefore the witness experiment does **not** need metrological perfection to be scientifically valuable.

Its primary job is to rule out wildly different local velocity-field curves that the relocation data alone cannot distinguish.

---

## 11. Recommended measurement matrix

For each of

```text
x ~0.35
x ~0.43
x ~0.51,
```

measure approximately

```text
T = 300 K first
E = 0.1, 0.3, 0.5, 1, 1.5, 2, 2.5, 3 kV/cm
at least two transport distances
multiple pulse averages / repeat traces.
```

Then repeat at one or two lower temperatures only if the relocation experiment itself will use them.

The room-temperature measurement is the decisive first priority because importing an 80-K APD velocity law into a 300-K graded absorber would otherwise remain a major modeling weakness.

---

## 12. Match the material, not merely the nominal composition

The witness layers should match, as closely as practical,

```text
growth method
doping species and concentration
anneal history
surface/passivation
crystal orientation
and material quality
```

of the relocation structures.

The 2010 Shockley–Haynes work found p-type minority-electron drift mobility lower than n-type mobility of the same composition, partly from acceptor/heavy-hole scattering.

Therefore literature n-type Hall mobility is **not** a sufficient substitute for this witness measurement.

---

## 13. Strongest experimental hierarchy after this result

### A. Transport witnesses

Measure

```text
v(E,x), D(E,x), tau(E,x)
```

at three representative compositions.

### B. Relocation structures

Grow the translated internal-gradient structures and measure each realized `x(z)`.

### C. Instrument calibration

Measure complex electrical/optical transfer and covariance independently.

### D. Joint inference

Condition the relocation fit on the witness-derived transport posterior and the measured `x(z)` for each structure.

### E. Causal test

Ask whether the **feature-depth dependence** of the wavelength × RF response requires the localized composition-gradient field beyond the calibrated generic transport law.

This is a much stronger experiment than trying to infer everything from the detector traces alone.

---

## 14. Nonclaims

Do not claim

```text
100 um is the final optimal test-bar length
three compositions are guaranteed sufficient
v(E) follows the empirical saturation law exactly
the low-temperature APD velocity parameters apply at 300 K
or transport calibration is part of the candidate novelty.
```

The checked result is narrower:

> **The composition and timing scales required to calibrate the relocation inverse are compatible with established HgCdTe minority-carrier transit metrology, and a minimal three-composition witness set directly spans the high-gradient region of the current design.**

---

## 15. Numerical regression

`numerics/hgcdte_transport_witness_calibration_design.py`
