# Relocation as Edge Encoding — Why the Purpose-Built Control Separates Better

**Date:** 2026-08-10  
**Status:** exact first-order identity plus numerical spatial-convergence check; explanatory design principle, not a novelty claim

## 1. Relocation is not merely another amplitude comparison

Let a localized transport contribution have shape

```math
q_f(z-z_0)
```

and let the wavelength/frequency sensitivity operator be `K_{lambda,f}(z)`.

At low frequency, `K` is the orientation-correct timing kernel. At finite RF, the same argument applies to the complex first-order Jacobian.

The measured contribution is

```math
y(\lambda,f;z_0)
=\int K_{\lambda,f}(z)q_f(z-z_0)\,dz.
```

Translate the same feature by a small distance `Delta z`:

```math
q_f(z-z_0-\Delta z)-q_f(z-z_0)
\simeq
-\Delta z\,q_f'(z-z_0).
```

Therefore

```math
\boxed{
\Delta y
\simeq
-\Delta z
\int K_{\lambda,f}(z)q_f'(z-z_0)\,dz.
}
```

If the feature vanishes at the integration boundaries, integration by parts gives

```math
\boxed{
\Delta y
\simeq
\Delta z
\int K'_{\lambda,f}(z)q_f(z-z_0)\,dz.
}
```

So a relocation experiment probes the **spatial derivative of the measurement sensitivity**, not merely its absolute overlap with one localized feature.

---

## 2. Flat feature limit — the signal is an edge difference

For an ideal compact feature of amplitude `A` on `[a,b]`,

```math
q_f(z)=A\,\mathbf 1_{[a,b]}(z),
```

and

```math
y=A\int_a^b K(z)dz.
```

Translate both edges by `Delta z`:

```math
\boxed{
\frac{\partial y}{\partial z_0}
=A[K(b)-K(a)].
}
```

Thus the first-order relocation fingerprint is a **bipolar edge measurement**:

```text
one contribution from the leading feature edge
minus
one contribution from the trailing feature edge.
```

At finite RF, `K` is complex, so both phase and log-magnitude carry the edge contrast.

---

## 3. Why this helps against smooth/contact nuisance modes

A broad amplitude change can often be represented by combinations of

```text
constant transport
slow polynomial bulk variation
or one-sided interface-localized terms.
```

A translated compact feature instead creates two spatially separated contributions with opposite sign.

That signed structure is harder for low-order smooth modes or a single boundary-localized process to mimic, especially when

```text
the feature is buried away from both interfaces
and
wavelength moves the generation distribution across both edges.
```

This explains why the matched `G2-G1` relocation comparison is substantially better conditioned than the published sample-A near-junction amplitude comparison.

The algebra itself is elementary and is **not** a novelty claim.

Its value here is as an experimental-design principle.

---

## 4. Why an infinitely sharp interface is not required

The edge identity could tempt one to make the programmed composition transition arbitrarily abrupt.

That would be the wrong conclusion.

The actual sensitivity operator has finite spatial bandwidth because generation depth is distributed and carrier transit response is integrated over depth.

Once an edge is sharper than that effective spatial resolution, additional sharpness should provide little new information.

The numerical model must also resolve the proposed edge before such a conclusion is trusted.

---

## 5. Spatial convergence test

The canonical calculation originally used

```text
80 cells over 7.6 um
-> cell width ~0.095 um.
```

An apparent preference for a `0.05 um` edge ramp was therefore initially under-resolved.

Rebuild the full finite-RF calculation at

```text
80 cells  -> 95.0 nm/cell
160 cells -> 47.5 nm/cell
320 cells -> 23.75 nm/cell
```

for the fixed conservative pair

```text
feature centers = 4.1 and 5.6 um
feature total width = 1.0 um
lambda = 2.00-2.40 um
f = 0.25, 0.50, 1, 2, 3 GHz
front + back interface nuisances
additive-like Pabs-dependent noise.
```

Compare transition ramps

```text
25, 50, 75, 100, 150, 200 nm.
```

---

## 6. Converged result

At `320` cells, the fixed-total-time information score is approximately

| edge ramp | design score |
|---:|---:|
| `25 nm` | `0.002743` |
| `50 nm` | `0.002746` |
| `75 nm` | `0.002760` |
| `100 nm` | `0.002734` |
| `150 nm` | `0.002525` |
| `200 nm` | `0.001904` |

The `25-100 nm` range has only about a **1% total spread**.

The `100 nm` result changes by less than `0.1%` from `160` to `320` cells.

By contrast, broadening the transition from `100` to `200 nm` reduces the score by about

```math
\boxed{30\%.}
```

Therefore:

> **There is no resolved numerical evidence that the experiment needs an ultrasharp interface. A transition of order `0.1 um` is already on the information plateau in the present model.**

---

## 7. Practical interpretation

This is favorable for fabrication.

The design should not chase the mathematically sharpest possible composition interface.

The more useful priorities are

```text
preserve the feature's integrated gradient contrast
keep its two edges spatially distinguishable
measure the realized x(z)
keep the whole feature away from both interfaces
and preserve matching between G1 and G2.
```

Interdiffusion that broadens a nominal `0.1 um` transition modestly is therefore not automatically fatal.

Broadening toward several tenths of a micron can become an identifiability cost and should be propagated through the measured profile.

---

## 8. Connection to the current design

The interface-safe joint optimization selected approximately

```text
G1 feature center ~4.1 um
G2 feature center ~5.6 um
lambda ~2.00-2.40 um.
```

The relocation identity explains why this geometry works:

```text
short wavelengths establish a common shallow reference response;
longer wavelengths in the selected band move generation through the buried edges;
the G2-G1 subtraction converts that movement into a signed edge fingerprint;
front/back interface terms remain spatially separated from the deliberately moved feature.
```

This is the cleanest conceptual statement of the current experiment.

---

## 9. Next theoretical refinement

Feature **total width** still matters because it sets the separation between the two encoded edges.

The next shape calculation should vary total width under

```text
fixed endpoint compositions
fixed approximate maximum gradient field
explicit interdiffusion broadening
and the interface-clearance constraint.
```

The correct objective remains covariance-weighted nuisance-orthogonal signal, not raw phase span or principal angle alone.

Numerical implementation:

`numerics/hgcdte_relocation_edge_convergence.py`
