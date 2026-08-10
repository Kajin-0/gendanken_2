# Randomized MBE Growth Order — Recovering Translation Causality Without Same-Wafer Selective Growth

**Date:** 2026-08-10  
**Status:** conditional experimental-design result; sequential MBE implementation is technologically conventional, but real run-to-run covariance is not yet measured; no novelty claim

## 1. Problem

The multi-depth translated-gradient series is scientifically attractive because the wavelength × RF fingerprint must change with the known location of the buried internal feature.

The strongest fabrication version would put several feature depths on one wafer.

However, the present literature audit has not established a HgCdTe-specific moving-shutter process capable of producing the required lateral depth series with a common final cap/contact stack.

That raises a practical question:

> **Can several ordinary sequential MBE growths retain the causal advantage of the depth series even when the chamber/process drifts from run to run?**

The answer is much better than a monotonic growth sequence suggests.

---

## 2. Do not grow feature depth monotonically with time

Suppose the six feature depths are grown chronologically as

```text
2.0, 2.4, 2.8, 4.6, 5.2, 5.6 um.
```

Then feature depth and run number are strongly correlated.

A smooth chamber drift can partially imitate the depth law.

This is avoidable.

Instead, deliberately scramble the feature depth versus chronological run number.

For example, the strongest six-run order in the current exhaustive search is

```math
\boxed{
4.6,\ 2.0,\ 2.4,\ 5.6,\ 2.8,\ 5.2\ \mu{\rm m}.
}
```

Now a smooth chronological drift does not look like a smooth feature-depth dependence.

This is classical experimental randomization applied to the internal-transport inverse.

---

## 3. Nuisance model

Use the current flexible physical nuisance basis:

```text
cubic smooth bulk transport
four collection-side exponential interface shapes
four back-side exponential interface shapes
wavelength-independent complex offset for each RF/device contrast.
```

For each physical nuisance amplitude, allow chronological run dependence

```math
\boxed{
a(r)=a_0+a_1r+\cdots+a_pr^p,}
```

where `r` is normalized run order.

The feature-depth assignment is permuted independently of `r`.

Two hard stresses are used:

```text
6 runs -> arbitrary quadratic drift in every nuisance amplitude
7 runs -> arbitrary cubic drift in every nuisance amplitude.
```

This is not a claim that real MBE errors are polynomial.

The point is to quantify how much smooth temporal process drift can be rejected by experimental ordering alone.

---

## 4. Fixed-total-time reference

The ideal reference remains the current boundary-safe

```text
4.1 / 5.6 um
```

two-device comparison with all bulk/interface nuisance amplitudes perfectly common.

Its fixed-total-resource information score is approximately

```math
S_{\rm ideal}\approx0.001630.
```

This is a normalization scale, not a measured SNR.

---

## 5. Six runs — quadratic process drift

Use the previously optimized six-depth set

```text
2.0, 2.4, 2.8, 4.6, 5.2, 5.6 um.
```

If grown in monotonic feature-depth order, the quadratic-drift score is approximately

```math
0.001415,
```

or about `87%` of the ideal perfectly matched pair.

Exhaust all

```math
6!=720
```

chronological assignments.

The strongest order is

```text
run 1 -> 4.6 um
run 2 -> 2.0 um
run 3 -> 2.4 um
run 4 -> 5.6 um
run 5 -> 2.8 um
run 6 -> 5.2 um.
```

Its score is approximately

```math
\boxed{0.001605,}
```

which is

```math
\boxed{98.5\%}
```

of the ideal perfectly matched two-device reference.

That is the key result.

> **Nearly all of the ideal structural-relocation information can survive even when every modeled bulk/front/back-interface nuisance amplitude is allowed an arbitrary quadratic chronological drift, provided the growth order is deliberately decorrelated from feature depth.**

---

## 6. Growth order matters materially

Across all 720 six-run permutations, the fixed-time score spans approximately

```text
minimum ~0.000515
median  ~0.001235
maximum ~0.001605.
```

Only about

```text
7.2%
```

of random orders exceed `90%` of the ideal pair score.

Therefore the conclusion is **not** simply

```text
randomize somehow.
```

The order should be treated as an experimental-design variable and selected before growth.

This is analogous to choosing wavelengths or RF frequencies optimally.

---

## 7. Seven runs — cubic process drift

Use the seven-depth set

```text
2.0, 2.4, 2.8, 4.4, 4.8, 5.2, 5.6 um.
```

Exhaust all

```math
7!=5040
```

chronological orders while allowing a cubic trend in every nuisance amplitude.

The strongest order is

```math
\boxed{
4.8,\ 2.4,\ 2.0,\ 5.2,\ 2.8,\ 5.6,\ 4.4\ \mu{\rm m}.
}
```

Its score is approximately

```math
\boxed{0.001420,}
```

or

```math
\boxed{87.1\%}
```

of the ideal perfectly matched pair.

Thus even an aggressively flexible smooth chronological drift does not destroy the relocation test if enough feature depths and an optimized order are used.

---

## 8. Why scrambling works

A smooth process drift is a function of **run number**.

The mechanism prediction is a function of **feature depth**.

If depth is grown monotonically with run number, those coordinates are nearly the same and the nuisance can imitate the target.

If the depths are deliberately interleaved,

```text
shallow -> deep -> shallow -> deep ...
```

the mechanism and drift coordinates become geometrically different.

The model can then use

```text
run number
feature depth
wavelength
RF frequency
```

as separate explanatory coordinates.

That is exactly the sort of causal structure the original published A/B comparison lacked.

---

## 9. Random run error is still real

Polynomial drift rejection does **not** remove

```text
random composition errors
random thickness errors
random defect populations
random contact resistance
random trap populations
or unmeasured processing changes.
```

Therefore a real experiment should add replication.

At minimum, include repeated growths at one shallow and one deep feature depth.

A stronger design would include

```text
replicated anchor depths
+
measured x(z) for every wafer
+
Hall / junction / contact characterization
+
measured electrical RF transfer
+
chronological process logs.
```

The repeated anchor depths give an empirical random-effect variance instead of forcing all variation into a smooth drift model.

---

## 10. Practical consequence

This result changes the fabrication hierarchy.

### Strongest but process-development-heavy

```text
same-wafer multi-depth MBE series
```

if a credible HgCdTe region-selective depth-control process is developed.

### Strongest near-term conventional route

```text
6-7 separate MBE growths
with deliberately optimized nonmonotonic feature-depth order
and replicated anchor depths.
```

### Minimum experiment

```text
one shallow / one deep matched pair
```

but its mechanism attribution is more dependent on run-to-run matching.

The randomized multi-run series is therefore the preferred realistic first fabrication plan unless a same-wafer method becomes available.

---

## 11. Relation to MBE capability

Existing HgCdTe MBE literature supports the underlying vertical profile control:

```text
compositionally graded and multilayer detector structures
in-situ ellipsometric growth control
sub-micron/nanometer-scale layer definition
and post-growth composition/thickness mapping.
```

Those capabilities are sufficient to make a **sequential translated-depth series** a much more conventional process target than the same-wafer moving-shutter concept.

The unresolved materials question is no longer whether MBE can place a buried feature at several depths.

It is:

> **What is the actual covariance of transport-relevant run-to-run changes after conditioning on measured composition, thickness, doping, interface, and contact variables?**

That must ultimately be measured rather than assumed.

---

## 12. Current experimental recommendation

The current strongest practical validation program is:

1. choose six feature depths approximately
   `2.0, 2.4, 2.8, 4.6, 5.2, 5.6 um`;
2. grow them in the optimized nonmonotonic order
   `4.6, 2.0, 2.4, 5.6, 2.8, 5.2 um`;
3. add at least two replicated anchor-depth growths if material budget permits;
4. characterize realized `x(z)` and layer thickness on every wafer;
5. process contacts/junctions in as common a batch as practical;
6. measure the same `2.00-2.40 um x 0.25-3 GHz` complex-response grid;
7. fit feature-depth response jointly with chronological process drift and measured physical covariates;
8. require the **depth law**, not merely an A-B phase difference, to agree with the transport forward model.

The seven-depth/cubic design is the more conservative alternative if process drift is expected to be strongly nonlinear.

---

## 13. Nonclaims

Do not claim

```text
real MBE run drift is quadratic or cubic
the optimized ordering is universal
the current illustrative 25% transport feature is a device prediction
profile metrology removes all random transport variation
the method is novel
or the experiment is manuscript ready.
```

The checked result is narrower:

> **Deliberately decorrelating feature depth from chronological growth order can preserve nearly all of the ideal translated-feature information while making the experiment robust to smooth run-to-run nuisance drift in the current model.**

---

## 14. Numerical regression

`numerics/hgcdte_randomized_growth_translation_series.py`
