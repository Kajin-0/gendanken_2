# Programmed HgCdTe — Interface-Safe Joint Depth and Spectral Design

**Date:** 2026-08-10  
**Status:** conditional purpose-built validation design; front/back interface nuisance stress, absorbed-signal-dependent phase-noise envelopes, fixed total wavelength-time resource; no fabrication claim and no novelty claim

## 1. Correction to the earlier translated-gradient optimum

The first programmed-profile search allowed feature centers only from approximately `0.8` to `3.2 um` because it inherited the short-wave, near-junction sample-A branch.

That was an artificial design boundary.

When the feature-position search is extended through the `7.6 um` conceptual absorber, the nuisance-orthogonal signal keeps increasing as one translated feature is pushed toward the back side.

That creates a new confounding risk:

```text
front-adjacent feature -> front contact/interface confounding
back-adjacent feature  -> substrate/back-interface confounding.
```

Therefore neither mathematical boundary should be allowed to define the experiment.

---

## 2. Both interfaces are now explicit nuisance sources

Use the programmed `1.0 um` internal gradient segment with

```text
0.10 um entrance ramp
0.80 um high-gradient plateau
0.10 um exit ramp
```

and the same endpoint-preserving slope construction.

Represent common smooth transport with

```math
1,\quad z/L,\quad (z/L)^2,\quad (z/L)^3,
```

and possible front-interface contributions with

```math
\exp(-z/0.30),
\exp(-z/0.50),
\exp(-z/0.75),
\exp(-z/1.00),
```

plus symmetric back-interface terms

```math
\exp[-(L-z)/0.30],
\exp[-(L-z)/0.50],
\exp[-(L-z)/0.75],
\exp[-(L-z)/1.00].
```

All twelve spatial nuisance amplitudes are common to the matched pair and are fitted freely.

An arbitrary wavelength-independent phase and `ln|H|` offset is also fitted independently at every RF frequency.

---

## 3. Fixed-total-time design metric

A denser scan is not free.

For an individual detector channel let the complex-component uncertainty scale with absorbed fraction as

```math
\sigma(\lambda)\propto P_{\rm abs}(\lambda)^{-\beta},
```

with two provisional envelopes:

```text
beta = 1/2 -> statistics-like
beta = 1   -> additive-like phase limit.
```

For independent equal device channels, the paired variance is proportional to

```math
P_1^{-2\beta}+P_2^{-2\beta}.
```

After whitening the data and projecting all common nuisance directions, define

```math
\boxed{
S_{\rm design}
=\frac{\|r_{\rm white}\|}{\sqrt{N_\lambda}}.
}
```

The `1/sqrt(N_lambda)` term holds total wavelength-time resource fixed while comparing scans with different numbers of wavelengths.

This is an information-amplitude metric proportional to fixed-total-time SNR under the stated noise model.

---

## 4. Interface clearance is imposed geometrically

The full `1.0 um` feature support must remain at least a clearance `d_c` from **both** boundaries.

The resulting additive-like (`beta=1`) optima are:

| minimum feature-edge clearance | feature centers | best contiguous band | `S_design` | min `Pabs` |
|---:|---:|---:|---:|---:|
| `0.5 um` | `4.9 -> 6.6 um` | `2.00-2.50 um` | `0.002979` | `0.911` |
| `1.0 um` | `4.6 -> 6.1 um` | `2.00-2.45 um` | `0.002878` | `0.971` |
| `1.5 um` | `4.1 -> 5.6 um` | `2.00-2.40 um` | `0.002727` | `0.991` |
| `2.0 um` | `3.8 -> 5.1 um` | `2.00-2.375 um` | `0.002517` | `0.997` |

The optimum therefore moves inward smoothly as the interface-exclusion zone grows.

The useful information does **not** collapse.

Even increasing the clearance from `1.0` to `2.0 um` costs only about `13%` in the fixed-time information-amplitude metric.

---

## 5. Recommended conservative geometry

Use the `1.5 um` interface-clearance design as the present reference:

```math
\boxed{
z_1\simeq4.1\ {\rm um},
\qquad
z_2\simeq5.6\ {\rm um}.
}
```

The corresponding spectral band is

```math
\boxed{
\lambda\simeq2.00-2.40\ {\rm um}
}
```

with `0.025 um` numerical spacing in the current design calculation.

An exhaustive contiguous-band search over `2.00-3.85 um` for this fixed pair also selects exactly `2.00-2.40 um`; the lower boundary is therefore not merely imposed by the reduced upper-wavelength scan.

The same `4.1 -> 5.6 um`, `2.00-2.40 um` result is obtained for both

```text
statistics-like beta=1/2
and
additive-like beta=1
```

phase-noise scaling.

This stability is more important than a small difference in numerical score.

---

## 6. Detailed conditional signal scales for the `1.5 um`-clearance design

For the additive-like envelope:

```text
N_lambda = 17
min Pabs = 0.99078
minimum baseline |H| over 0.25-3 GHz ~0.9833
weighted nuisance-separation angle ~12.32 deg
1-GHz differential phase p-p ~0.391 deg.
```

The unweighted phase-only target, after fitting common smooth + front/back interface nuisance directions and one phase intercept per RF, leaves a phase-vector residual norm of approximately

```math
\boxed{0.484^\circ.}
```

The modeled wavelength scan moves the conditional mean generation depth approximately

```text
feature at 4.1 um:
2.00 um -> 2.23 um
2.40 um -> 4.59 um

feature at 5.6 um:
2.00 um -> 2.24 um
2.40 um -> 5.88 um.
```

Thus the chosen spectral interval moves generation through the two buried feature locations while remaining almost completely absorbed.

---

## 7. Why this beats the earlier `2.6 / 3.2 um` design at fixed resource

When the earlier pair is reoptimized under the **same** rules

```text
front + back interface nuisances
absorbed-signal-dependent additive-like noise
arbitrary complex RF intercepts
fixed total wavelength-time resource
```

its best contiguous band is approximately

```text
2.00-3.225 um
```

and its information-amplitude score is

```text
~0.001446.
```

The conservative interior design gives

```text
~0.002727.
```

Therefore

```math
\boxed{
\frac{S_{4.1\to5.6}}{S_{2.6\to3.2}}
\approx1.89.
}
```

At equal total averaging resource that is approximately

```text
1.89x SNR
or
3.56x Fisher information
```

under the stated linearized model.

The improvement comes while **increasing**, not reducing, protection against boundary artifacts.

---

## 8. Illustrative fixed-resource SNR scale

For comparison only, suppose

```text
five RF frequencies are retained in every candidate design;
one wavelength dwell unit gives 0.10-deg-equivalent complex-component noise
per individual full-absorption channel;
the two device-channel noises are independent;
total wavelength-time resource equals 81 such wavelength dwell units.
```

The independent-channel `sqrt(2)` penalty is already included in the whitening model.

Then the `4.1 -> 5.6 um`, `2.00-2.40 um` design gives an illustrative complex-response detection scale of roughly

```math
\boxed{{\rm SNR}\sim14}
```

for the same imposed `25%` feature-supported transport perturbation.

This should **not** be read as a detector-performance prediction.

It is a resource-normalized consequence of the current idealized complex-response covariance model. Real wavelength/RF covariance, systematic errors, feature amplitude, and transport physics can move the number substantially.

---

## 9. The deeper optimum changes the experimental interpretation

The purpose-built experiment no longer needs to reproduce the published sample-A near-junction geometry.

The strongest current logic is instead:

```text
keep both interfaces far from the deliberately moved feature
use the graded composition primarily to encode wavelength-dependent generation depth
translate the same internal transport structure by ~1.5 um
measure whether the wavelength x RF fingerprint translates with it.
```

This is a cleaner causal experiment than asking whether an unknown near-contact high-field region changes response.

---

## 10. Hard boundary on the result

Do not call `4.1 / 5.6 um` a universal optimum.

It is conditional on

```text
L = 7.6 um
x_front = 0.55
x_back = 0.32
1.0-um programmed gradient segment
~2-kV/cm local gradient scale
Hansen gap + Moazzami absorption
baseline deterministic v = 1e5 m/s
illustrative 25% supported transport perturbation
0.25-3 GHz RF set
chosen common bulk/interface nuisance family
and the two Pabs-based noise envelopes.
```

The strongest robust statement is narrower:

> **Once both interfaces, signal-dependent phase precision, and fixed measurement time are included, the design still prefers a genuinely buried relocation pair; a conservative `1.5 um` interface clearance gives a stable `4.1 -> 5.6 um` / `2.00-2.40 um` solution under both provisional noise scalings.**

---

## 11. Next design question

The next numerical optimization should vary the **feature width and edge-ramp length** under a fixed physically plausible maximum gradient field, rather than assuming the current `1.0 / 0.1 um` programmed segment.

The reason is now clear: relocation converts a compact spatial feature into an edge-sensitive differential fingerprint. Feature sharpness may therefore be a direct identifiability resource, but only until epitaxial interdiffusion and optical spatial resolution erase the benefit.

Numerical implementation:

`numerics/hgcdte_programmed_joint_depth_spectral_design.py`
