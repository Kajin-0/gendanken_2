# Physical-Nuisance Relocation Design — High RF Breaks the Transport-Law Degeneracy

**Date:** 2026-08-10  
**Status:** conditional Fisher/response-geometry design around a reduced downstream drift–diffusion model; physical parameters and covariance are not yet calibrated; exact wavelength support not frozen; no novelty claim

## 1. Why arbitrary timing nuisance modes are no longer the right design test

The earlier short-wave work allowed several generic smooth timing modes for samples A and B.

That was intentionally conservative, but after introducing the downstream drift–diffusion first-passage operator the more relevant reviewer question is physical:

> **Can a translated localized composition-gradient field be distinguished from ordinary uncertainty in mobility, recombination, overall field scale, high-field velocity law, and entrance-surface loss?**

This file answers that narrower question around one explicit sensitivity point.

---

## 2. Localized-gradient mechanism coordinate

Keep the **realized optical composition profile** `x(z)` fixed.

Write the programmed composition-slope magnitude as

```math
s(z)=\left|dx/dz\right|
```

and the same-endpoint smooth background slope as

```math
s_0=(x_{\rm front}-x_{\rm back})/L.
```

For transport sensitivity only, define

```math
\boxed{
s_{\rm eff}(z;\eta)
=s_0+\eta[s(z)-s_0].
}
```

Then

```text
eta=1 -> full programmed local-gradient transport field
eta=0 -> smooth background transport field
         evaluated on the same measured optical x(z).
```

`eta` is **not** a laboratory knob and `eta=0` is not claimed to be a self-consistent alternate crystal.

It is a nested statistical mechanism coordinate that asks whether the complex-response data require the *localized deviation* of the transport field from a smooth graded background once the optical profile itself is already known.

The target vector is

```math
\partial\ln H/\partial\eta.
```

---

## 3. Central transport sensitivity point

Use

```text
T = 300 K
mu_n = 9000 cm2/Vs
chi_E = 0.50
tau_rec = 1.0 ns
v_sat = 1e5 m/s
entrance surface S = 1e5 cm/s.
```

These are **sensitivity coordinates**, not a fitted HgCdTe material parameter set.

The smooth velocity saturation law is only a reduced high-field uncertainty coordinate.

The real experiment must replace these values/laws with independently measured or literature-validated transport inputs.

---

## 4. Physical nuisance parameters

Marginalize the target against free common derivatives with respect to

```math
\ln\mu,
\qquad
\ln\chi_E,
\qquad
\ln\tau_{\rm rec},
\qquad
\ln v_{\rm sat},
\qquad
\ln S.
```

These nuisance directions are calculated by finite differences of the full first-passage complex transfer.

Also permit an arbitrary wavelength-independent

```text
phase offset
and
ln|H| offset
```

for every device and every RF frequency.

Therefore the design is not gaining information merely from a channel-dependent constant phase or gain.

---

## 5. Provisional signal-dependent weighting

Let

```math
C_{\rm dc}(\lambda)
=\int p(z|\lambda)u(z,0)dz
```

be the modeled DC collection probability.

Use the provisional statistics-like complex-log-response weight

```math
\boxed{
w(\lambda,f)
=|H(\lambda,f)|
\sqrt{P_{\rm abs}(\lambda)C_{\rm dc}(\lambda)}.
}
```

This captures three unavoidable trends:

```text
less absorption -> less signal
less DC collection -> less signal
smaller RF transfer -> less coherent modulation amplitude.
```

It is **not** a measured covariance model.

A laboratory design must replace this weighting by the actual phase/magnitude covariance versus wavelength and RF frequency.

---

## 6. Fixed-resource design score

Whiten the target and nuisance derivatives by the provisional weight, project the target from the nuisance span, and define

```math
\boxed{
S
=\frac{\|d_{\eta,\perp}\|}
{\sqrt{N_{\rm device}N_fN_\lambda}}.
}
```

This score is proportional to fixed-total-resource information under the stated equal-component convention.

It is **not** an absolute experimental detection significance.

---

## 7. The key correction — low RF cannot identify the mechanism

For the final four-depth geometry discussed below, use the full `2.00-2.40 um` wavelength grid.

With

```text
0.25, 0.50, 1.0 GHz
```

the score is only approximately

```math
1.28\times10^{-4},
```

and the localized-gradient derivative lies only about

```math
0.08^\circ
```

from the physical nuisance span.

Thus low-frequency mean-delay behavior is highly degenerate with ordinary changes in

```text
mobility
field scale
lifetime
velocity law
and entrance loss.
```

This is a physical identifiability limit, not merely a phase-noise problem.

---

## 8. High RF changes the geometry dramatically

At higher normalized frequency, the complex response depends on the full first-passage-time distribution rather than only its first moment.

For the same four-depth geometry:

### Two-frequency high-RF support

```text
1.5, 3.0 GHz
```

gives approximately

```math
S\approx0.00511
```

with target-to-nuisance angle about

```math
4.25^\circ.
```

### Four-frequency support

```math
\boxed{1.5,\ 2.0,\ 2.5,\ 3.0\ {\rm GHz}}
```

gives

```math
\boxed{S\approx0.00514}
```

and angle about

```math
\boxed{4.51^\circ.}
```

The two-frequency design already captures most of the available mechanism information; the additional high-RF points provide modest extra robustness/shape information.

Adding all the low-RF points at the same total resource can reduce the score because they consume measurement time while contributing little mechanism separation.

---

## 9. Is 3 GHz physically measurable in the central model?

For the candidate feature-depth family, the central-model transfer at `3 GHz` is attenuated but not zero.

For representative depths in the emerging design, minimum modeled `|H|` at `3 GHz` is of order

```text
~0.14-0.15
```

while some wavelengths/depths remain substantially larger.

Thus high RF is expensive in coherent signal but still carries information after the provisional `|H|` weighting.

This is exactly why a covariance-aware design is required.

If the real detector is slower than the central stress, the useful frequency support must move downward.

If it is faster, higher RF may become even more valuable.

No universal `3 GHz` prescription is claimed.

---

## 10. Reoptimized feature depths

Use the dense

```text
2.00-2.40 um
```

spectral grid and the high-RF support

```text
1.5, 2.0, 2.5, 3.0 GHz.
```

Scan feature centers

```text
2.0 to 5.6 um
in 0.2-um steps
```

with at least `0.4 um` separation.

### Best two-depth design

```math
\boxed{2.8,\ 5.6\ \mu{\rm m}}
```

with score about

```math
0.00274.
```

### Best three-depth design

```math
\boxed{2.4,\ 2.8,\ 5.6\ \mu{\rm m}}
```

with score about

```math
0.00489.
```

### Best four-depth design

```math
\boxed{2.4,\ 2.8,\ 5.2,\ 5.6\ \mu{\rm m}}
```

with

```math
\boxed{S\approx0.00514}
```

and target-to-nuisance angle approximately

```math
\boxed{4.51^\circ.}
```

### Best five-depth design

Approximately

```text
2.4, 2.8, 4.8, 5.2, 5.6 um
```

with score only about

```math
0.00517.
```

The fifth depth therefore adds only about **0.5%** fixed-resource information in this central reduced model.

The four-depth design is the better first complexity/benefit point.

---

## 11. The depth structure is physically interpretable

The optimum forms two local depth clusters:

```text
shallow cluster ~2.4-2.8 um
deep cluster ~5.2-5.6 um.
```

This is not the same pattern as the older ad hoc-delay optimization.

The high-RF model benefits from observing how the first-passage distribution changes

```text
within the shallow regime
within the deep regime
and across the large shallow/deep relocation.
```

The close pair inside each cluster helps distinguish a **local depth derivative of the mechanism fingerprint** from a global change in mobility or high-field velocity law.

---

## 12. Exact wavelength support is intentionally not frozen

A sparse wavelength optimizer on the fine `0.025 um` grid tends to place support near

```text
~2.00 um
~2.025 um
one or two intermediate points
and ~2.40 um.
```

That can improve fixed-time information under the present deterministic optical model.

However, those closely spaced short-wave points exploit sharp band-edge/generation-depth structure.

When the candidate wavelengths are forced onto a coarser `0.05 um` grid, the apparent gain drops substantially.

Therefore exact sparse wavelengths are now an **optical-uncertainty problem**, not a solved measurement-design result.

Before accepting them, propagate at least

```text
measured x(z) uncertainty
absorption-model uncertainty
backside/substrate transfer
wavelength calibration
and reflection/interference.
```

The robust conclusion is the useful `~2.0-2.4 um` band, not the present `25 nm`-spaced optimum.

---

## 13. What this result changes

The earlier experimental intuition was

```text
short wavelength gives spatial leverage
+
more RF points may help.
```

The physics-derived calculation is sharper:

> **High RF is not just extra SNR or extra phase. It is the main coordinate that separates the localized-gradient mechanism from uncertainty in the generic transport law.**

The low-frequency inverse remains valuable for coarse transport/timing calibration.

The **mechanism validation** should deliberately reach the frequency range where the full first-passage distribution changes shape.

---

## 14. Current design hierarchy

### Calibration

Use lower RF and broader wavelength coverage to determine

```text
DC collection
low-order timing
instrument/electrical transfer
and coarse transport parameters.
```

### Mechanism validation

Use the four-depth translated-feature family near

```text
2.4, 2.8, 5.2, 5.6 um
```

and concentrate information in the highest RF range that remains experimentally coherent.

The present central-model candidate is

```text
~1.5-3 GHz.
```

### Optical support

Retain `~2.0-2.4 um` as the current band, but do not freeze a sparse wavelength list until optical uncertainties are propagated.

---

## 15. Major remaining limitation

The current calculation assumes the five transport nuisance parameters are **common** across the translated-depth family.

Real separate MBE growths can have run-dependent

```text
mobility
lifetime
doping
defect/trap population
surface loss
and velocity-field behavior.
```

Therefore the older randomization/replication design principle remains highly relevant, but its exact depth/order optima must be recomputed with the physical-nuisance derivatives.

The next steps are:

1. add measured optical-profile uncertainty;
2. allow low-order chronological drift in physical transport parameters across growths;
3. optimize growth order and replicate depths under the corrected transport model;
4. replace the provisional RF weighting by measured covariance.

---

## 16. Numerical implementation

`numerics/hgcdte_physical_nuisance_relocation_design.py`
