# Translated-Gradient Pair — Matching and Model-Knowledge Tolerances

**Date:** 2026-08-10  
**Status:** conditional tolerance analysis around the purpose-built `2.6 / 3.2 um` matched-contact design; no fabrication qualification and no novelty claim

## 1. Matching can be parameterized cleanly

For any smooth/contact nuisance spatial mode `q_k`, write the two device amplitudes as

```math
q_{2,k}=c_k+\frac{\delta_k}{2},
\qquad
q_{1,k}=c_k-\frac{\delta_k}{2}.
```

Then the paired first-order response is

```math
\boxed{
J_2 q_{2,k}-J_1 q_{1,k}
=(J_2-J_1)c_k
+\frac{J_2+J_1}{2}\delta_k.
}
```

This separates two physically different resources:

```text
c_k     -> common matched variation; can be fitted freely
δ_k     -> differential fabrication/contact mismatch; must be small or calibrated.
```

The translated-gradient design works because the target is well separated from the **common** nuisance span. It fails if arbitrary independent nuisance amplitudes are allowed.

---

## 2. Response-space mismatch requirement

Use the same eight nuisance shapes as the translated-gradient design:

```text
1
z/L
(z/L)^2
(z/L)^3
exp(-z/0.30 um)
exp(-z/0.50 um)
exp(-z/0.75 um)
exp(-z/1.00 um).
```

Normalize each differential-mismatch response column to RMS one. Its coefficient then represents a response-equivalent mismatch amplitude.

Common nuisance amplitudes remain free.

### Phase-only operating point

If the phase noise is

```math
\sigma_\phi=0.010^\circ
```

per wavelength/RF point, the largest equal independent Gaussian prior on the eight differential mismatch modes that still gives `3 sigma` for the illustrative translated-gradient signal is approximately

```math
\boxed{
\sigma_{\rm mismatch}
\lesssim0.00253^\circ\ {\rm RMS}.
}
```

### Provisional complex-response operating point

Under the explicit approximation that phase and `ln|H|` have equal independent component noise corresponding to

```text
0.030 degree-equivalent
```

the corresponding mismatch limit is

```math
\boxed{
\sigma_{\rm mismatch}
\lesssim0.00290^\circ
}
```

response-equivalent RMS.

These are not microscopic composition or contact tolerances. They are the allowed amplitudes of the **residual differential spectral/RF nuisance fingerprints after normalization**.

---

## 3. Fabrication-coordinate tolerance test

The realized profile need not equal the design exactly if it is measured and inserted into the forward model.

To quantify the cost of **unmodelled** deviations, use a deliberately strict criterion:

```text
fit the realized target with the nominal target after projecting nominal common nuisances;
require fitted target amplitude within +/-10%;
require residual-target cosine >=0.99.
```

Then vary each fabrication coordinate symmetrically in both signs.

The resulting first tolerance envelope is:

| unmodelled coordinate | symmetric tolerance under stated criterion |
|---|---:|
| common shift of both feature centers | `~0.117 um` |
| error in feature-center separation | `~0.0657 um` |
| differential Gaussian width `Delta sigma` | `~0.0103 um` |
| differential front composition `Delta x_front` | `~0.00133` |
| differential back composition `Delta x_back` | `~0.00725` |
| differential slope-modulation parameter `Delta a` | `~0.146` |

Interpretation:

- absolute depth registration at roughly the `0.1 um` scale is adequate for this nominal fingerprint;
- relative feature separation should be known to roughly `0.07 um` for a `10%` amplitude model;
- **differential width is substantially more sensitive**, at the order of `10 nm` in the present Gaussian parameterization;
- the front composition is much more sensitive than the back composition because the short-wave spectral encoder is controlled strongly by the high-Cd entrance region.

These numbers are **model-knowledge requirements**, not necessarily growth tolerances. If the realized `x(z)` is characterized accurately, the model should use the realized profile rather than pretending it equals the nominal design.

---

## 4. A useful exact cancellation — a wavelength-independent electrical pole drops out

For device `j`, suppose the measured transfer factorizes as

```math
M_j(\lambda,f)
=E_j(f)H_j(\lambda,f),
```

where `E_j(f)` is an arbitrary device/readout electrical transfer that is independent of wavelength.

Take the paired log response:

```math
\ln M_2-\ln M_1
=
\ln H_2-\ln H_1
+
\ln E_2-\ln E_1.
```

The analysis already removes a wavelength-independent complex offset separately at each RF frequency. Let that centering operator be `C_lambda`. Then

```math
\boxed{
C_\lambda[\ln E_2(f)-\ln E_1(f)]=0.
}
```

Therefore a **pure wavelength-independent RC/contact/readout pole mismatch cancels exactly** in the translated-gradient wavelength fingerprint.

This is materially better than the earlier optical-load-curvature branch, where load-dependent electrical poles had to be de-embedded state by state.

What remains dangerous is

```text
wavelength-dependent detector impedance
wavelength-dependent amplitude-to-phase conversion
signal-level-dependent electronics
or any electrical effect correlated with the spectral scan.
```

Those do not cancel automatically.

---

## 5. Why the front-composition tolerance matters twice

The numerical `Delta x_front ~0.0013` value above is only an **optical/model-fingerprint** tolerance under the nominal-analysis test.

Front composition also affects the semiconductor/contact environment itself.

The preceding prior-art audit already found that HgCdTe contact-induced transient behavior can depend on Cd composition and temperature.

Therefore the collection-side composition should be treated as a dual control variable:

```text
optical-kernel matching
+
contact-physics matching.
```

A measured optical profile can correct the first.

It cannot automatically correct unknown composition-dependent contact dynamics.

Thus matching the front/cap composition remains a genuine fabrication-control requirement even if the optical forward model is excellent.

---

## 6. Current practical interpretation

The purpose-built pair no longer demands that two devices be identical in every microscopic respect.

It demands three things:

```text
1. common smooth/contact variation must dominate over differential variation;
2. residual differential nuisance fingerprints must be calibrated to a few millidegrees;
3. the realized internal composition profiles must be measured accurately enough to update the optical forward model.
```

This is a more realistic experimental specification than asking for an impossible perfectly identical pair.

---

## 7. Strongest current experimental sequence

A clean program is now:

### A. Fabricate / characterize matched translated-gradient pair

Measure independently

```text
x(z)
feature center and width
front/cap composition
thickness
contact geometry
static impedance.
```

### B. Instrument-only wavelength × RF calibration

Establish differential phase/magnitude covariance and confirm wavelength-independent electrical transfer cancellation.

### C. Fit common nuisance modes

Allow shared smooth/contact terms to float.

### D. Test translated-gradient target

Ask whether the remaining wavelength × RF complex response requires the predicted feature-translation fingerprint.

### E. Reciprocal / repeated fabrication validation

Repeat with another translated pair or reverse the feature displacement so a fabrication-specific artifact cannot masquerade as the internal mechanism.

---

## 8. What still blocks a manuscript-level claim

- growth/anneal feasibility of the mean-preserving translated `x(z)` family;
- demonstrated profile metrology at the required depth/width scale;
- real differential wavelength × RF covariance;
- wavelength-dependent detector/readout electrical effects;
- transport-model validation beyond deterministic baseline drift;
- focused prior-art audit for deliberately translated internal HgCdTe composition-gradient control structures;
- actual experimental data.

---

## 9. Next decisive direction

The highest-value next theoretical step is now **materials feasibility**, not another inverse-conditioning calculation:

> **Can a realistic HgCdTe growth/interdiffusion process produce two monotonic profiles with the same high-Cd collection-side cap and endpoints but with a comparable nonlinear-gradient enhancement centered near `2.6` and `3.2 um`?**

If not, the profile family must be redesigned around a fabrication-reachable control variable.

Numerical implementation:

`numerics/hgcdte_translated_gradient_mismatch_tolerances.py`
