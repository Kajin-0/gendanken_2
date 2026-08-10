# Replicated Randomized MBE Translation Series

**Date:** 2026-08-10  
**Status:** conditional experimental-design result; real random run-to-run covariance remains unmeasured; no novelty claim

## 1. Why replication is required

Optimizing feature depth versus chronological growth order rejects smooth chamber/process drift, but it does not measure genuinely random run-to-run variation.

A real translated-gradient validation series therefore needs at least two feature depths grown more than once.

The repeated samples serve two roles:

1. estimate same-structure run-to-run variance directly;
2. add mechanism information at depth coordinates where the wavelength × RF fingerprint changes rapidly.

The second role is not obvious in advance, so the replicate depths should be optimized rather than automatically placed at the shallow/deep extremes.

---

## 2. Starting six-run design

The current six-depth set is

```text
2.0, 2.4, 2.8, 4.6, 5.2, 5.6 um.
```

The optimized chronological order under quadratic drift is

```text
4.6, 2.0, 2.4, 5.6, 2.8, 5.2 um.
```

The fixed-total-resource reference is the ideal perfectly matched `4.1/5.6 um` two-device pair with common nuisance amplitudes.

---

## 3. Eight-run construction

Choose two of the six feature depths and repeat each once.

For every candidate anchor pair, insert the two replicates in every distinct chronological slot while preserving the relative order of the original optimized six-run backbone.

This produces an eight-run sequence while keeping the earlier randomization logic intact.

The same physical nuisance basis is used:

```text
cubic smooth bulk
four collection-side interface exponentials
four back-side interface exponentials
wavelength-independent complex offsets.
```

The nuisance amplitudes are allowed either quadratic or cubic dependence on chronological run number.

---

## 4. Quadratic chronological drift — best repeats are `2.8 / 4.6 um`

The strongest repeated-depth pair is

```math
\boxed{2.8\ {\rm um}\quad\text{and}\quad4.6\ {\rm um}.}
```

The strongest tested schedule is

```text
run 1 -> 2.8 um
run 2 -> 4.6 um
run 3 -> 2.0 um
run 4 -> 2.4 um
run 5 -> 5.6 um
run 6 -> 2.8 um
run 7 -> 4.6 um
run 8 -> 5.2 um.
```

Its fixed-total-resource score is approximately

```math
\boxed{0.002196.}
```

Relative to the ideal perfectly matched two-device reference:

```math
\boxed{S/S_{\rm ideal}\approx1.35.}
```

Thus the replicated eight-run design can contain **more** nuisance-orthogonal mechanism information than the ideal two-device comparison despite dividing total measurement resource across eight samples.

---

## 5. Cubic chronological drift — best repeats shift to `2.8 / 5.2 um`

Under the stronger assumption that every modeled nuisance amplitude may drift cubically with run number, the strongest replicate pair becomes

```math
\boxed{2.8\ {\rm um}\quad\text{and}\quad5.2\ {\rm um}.}
```

The strongest tested schedule is

```text
run 1 -> 5.2 um
run 2 -> 2.8 um
run 3 -> 4.6 um
run 4 -> 2.0 um
run 5 -> 2.4 um
run 6 -> 5.6 um
run 7 -> 2.8 um
run 8 -> 5.2 um.
```

Its score is approximately

```math
\boxed{0.001877,}
```

or

```math
\boxed{1.15\times}
```

the ideal perfectly matched two-device reference.

So the replication benefit survives a substantially more flexible chronological drift model.

---

## 6. Why the optimizer does not choose the extreme depths

Replication is most useful where the mechanism response has large **local curvature with feature depth**.

Repeating the extreme shallow/deep devices mostly reproduces information already present in the broad contrast.

Repeating interior high-leverage depths instead tests whether

```text
same designed structure
+
different chronological run
```

returns the same wavelength × RF fingerprint exactly where the depth law is changing most strongly.

That makes the repeats simultaneously

```text
process controls
and
mechanism controls.
```

---

## 7. What the repeats let the real experiment measure

For each replicated depth, compare the realized pair after conditioning on measured

```text
x(z)
layer thickness
junction/contact resistance
Hall parameters if available
electrical RF pole
optical throughput
and processing batch.
```

The residual same-depth difference becomes a direct empirical estimate of the run-to-run transport nuisance that cannot be learned from a one-sample-per-depth series.

This variance can then enter the hierarchical wavelength × RF fit rather than being guessed as a prior.

---

## 8. Recommended first fabrication set

If eight epitaxial runs are practical, the current preferred design is:

### moderate smooth-drift assumption

```text
2.8, 4.6, 2.0, 2.4, 5.6, 2.8, 4.6, 5.2 um
```

### more conservative cubic-drift assumption

```text
5.2, 2.8, 4.6, 2.0, 2.4, 5.6, 2.8, 5.2 um.
```

The exact order should be recomputed after a real MBE facility supplies its historical process covariance.

---

## 9. Nonclaims

Do not claim

```text
quadratic/cubic drift is the true MBE error process
replication automatically eliminates random defects
these eight depths/orders are universal
or the illustrative transport perturbation is a real device prediction.
```

The checked statement is:

> **In the current finite-RF model, properly chosen replicate depths strengthen rather than dilute the translated-feature experiment while providing the same-depth observations needed to estimate random run-to-run transport variance.**

---

## 10. Numerical regression

`numerics/hgcdte_randomized_growth_replication_design.py`
