# Sample-A Cross-Band Self-Calibration Limit — Why More Spectral Points Do Not Remove the A-Baseline Degeneracy

**Date:** 2026-08-09  
**Status:** conditional cross-band Fisher/identifiability calculation over the 72-member sample-A profile family; equal independent phase-noise model; illustrative A-localized anomaly; no novelty claim

## 1. Why this test is necessary

The short-wave branch now has a quantitative requirement:

```text
relevant smooth A/B spectral phase-mode amplitudes
must be constrained to roughly the ~0.005 deg RMS class
```

for the current illustrative A-localized anomaly to remain robustly detectable at fixed measurement time.

That immediately raises a possible escape route:

> **Can the needed sample-A smooth baseline simply be calibrated from the existing mid/deep A spectrum, or by fitting one sufficiently broad 2.00-3.83 um spectrum?**

If yes, the `~0.005 deg` prior would not require a genuinely independent calibration.

This note tests both possibilities directly.

---

## 2. Define the A modes in the coordinates that matter to the short-wave experiment

For each of the 72 sample-A profile-family members, build the centered short-wave timing matrix

```text
2.00-2.80 um
0.01 um spacing.
```

Take its first three spatial right-singular modes.

Scale each spatial mode so that its **short-wave spectral phase response** has unit RMS.

Therefore a fitted coefficient uncertainty of

```math
0.005^\circ
```

has exactly the same phase-equivalent meaning as the smooth-mode prior used in the preceding short-wave Fisher calculations.

The question is then:

> How well do other wavelength bands observe those same spatial modes?

---

## 3. Mid/deep A data are nearly blind to the leading short-wave A smooth mode

Use only

```text
2.80-3.83 um
```

sample-A phase data with independent equal

```math
\sigma_\phi=0.10^\circ
```

per wavelength.

Fit the three short-wave-defined A spatial modes from the mid/deep spectral responses.

The resulting coefficient uncertainties, expressed directly in **short-wave-equivalent RMS phase degrees**, are:

### Mode 1

```math
\boxed{
0.272^\circ
\text{ to }
4.917^\circ
}
```

with median

```math
\boxed{1.125^\circ.}
```

### Mode 2

```text
0.0407-1.612 deg
median ~0.362 deg.
```

### Mode 3

```text
0.00190-0.217 deg
median ~0.0487 deg.
```

For the first two modes:

```text
fraction of profiles with sigma_mode <=0.005 deg = 0%.
```

Thus the leading A smooth direction that matters to the short-wave contrast is not merely weakly measured by the mid/deep scan.

It is **orders of magnitude** away from the required calibration scale.

---

## 4. This is the near-junction gauge reappearing in another form

The leading short-wave A mode strongly weights the part of the absorber near the collecting junction.

That is exactly the region where

```math
S_i(0)=1
```

for every front-collection wavelength and where differential spectral leverage collapses.

The mid/deep scan was already shown to be nearly blind to the retained nonlinear/high-field support.

The present result shows that the same blindness also prevents the mid/deep branch from accurately determining the **smooth A baseline mode** that competes with that localized signal.

So the problem is structural, not just a poor choice of estimator.

---

## 5. What phase precision would mid/deep self-calibration require?

Because the linear Fisher coefficient uncertainty scales directly with equal phase noise, ask what per-wavelength mid/deep phase precision would be needed to push all three short-wave-equivalent A smooth-mode uncertainties below

```math
0.005^\circ.
```

Across the 72 profiles, the required equal per-wavelength phase noise ranges approximately

```text
best profile:   ~0.00184 deg
median profile: ~0.000445 deg
worst profile:  ~0.000102 deg.
```

The median requirement is already roughly

```math
\boxed{2.2\times10^2}
```

times smaller in RMS phase than the present `0.10 deg` reference.

Because white-noise averaging time scales as `sigma_phi^-2`, this corresponds to approximately

```math
\boxed{5.1\times10^4}
```

times more white-noise integration for a median profile.

The worst profile approaches

```math
\sim9.7\times10^5
```

times the white-noise integration resource.

These numbers are not proposed experimental specifications. They show that **mid/deep A phase-only self-calibration is not a plausible route to the required short-wave A-mode prior inside the present model.**

---

## 6. Could one broad spectral fit solve everything simultaneously?

A second possible escape route is to combine both bands and fit all unknowns at once.

Use

```text
2.00-3.83 um
0.01 um spacing
184 wavelengths
```

and fit simultaneously:

```text
1 illustrative A-localized anomaly amplitude
3 short-wave-defined smooth A amplitudes
3 short-wave-defined smooth B amplitudes
1 wavelength-independent common phase.
```

No smooth-mode priors are supplied.

At

```math
\sigma_\phi=0.10^\circ
```

per wavelength, the illustrative anomaly significance across the 72 A profiles is only

```math
\boxed{
0.0616\sigma
\text{ to }
0.565\sigma
}
```

with median

```math
\boxed{0.134\sigma.}
```

The anomaly spectral vector remains extremely close to the combined smooth-plus-common nuisance subspace:

```text
principal angle:
0.0146-0.326 deg
median ~0.0639 deg.
```

Thus broadening the wavelength interval does not remove the underlying degeneracy.

---

## 7. White-noise scale required for a no-prior broad self-fit

Because the broad no-prior fit remains linear, detection significance scales inversely with equal phase noise.

The per-wavelength phase noise required for a `3 sigma` anomaly detection is therefore

```text
worst profile:  ~0.00205 deg
median profile: ~0.00448 deg
best profile:   ~0.0188 deg.
```

To guarantee `3 sigma` across the current family requires approximately

```math
\boxed{
\sigma_\phi\lesssim0.00205^\circ
}
```

at every one of the 184 wavelengths under the present equal-noise model.

Relative to the `0.10 deg` reference, the corresponding white-noise integration multiplier is about

```math
\boxed{2.4\times10^3.}
```

Again, this is not a proposed instrument specification. It demonstrates that **brute-force spectral self-calibration is a very inefficient way to break the A-baseline degeneracy.**

---

## 8. What this rules out

The following strategy is no longer credible as the primary path:

```text
measure A and B over enough wavelengths
-> fit arbitrary smooth A and B baselines
-> extract the localized A feature from the same static spectrum.
```

The response geometry is too close to singular.

Adding more wavelengths within the same static optical family provides far less new information than the raw number of measurements suggests.

This is consistent with the earlier global wavelength-allocation result, where the fixed-time optimum collapsed to two short-wave spectral clusters rather than spreading time over many wavelengths.

---

## 9. The new implication — change the experiment, not merely the estimator

The static sample-A smooth baseline is the problematic nuisance.

Therefore the highest-value next route is a measurement in which that static baseline cancels to first order.

The natural candidate is a **causal difference-in-differences** observable:

```text
same sample A
same sample B
same spectral coordinate / controlled optical kernel
before and after a physical perturbation
```

such as temperature or another independently controlled transport perturbation.

Schematically, if

```math
D_{AB}(u)
=\Phi_A(u)-\Phi_B(u),
```

then compare

```math
\boxed{
\Delta D_{AB}
=D_{AB}(u_2)-D_{AB}(u_1).
}
```

Static smooth A/B transport terms cancel if they are unchanged, and only their **perturbation response** remains as nuisance structure.

That may be dramatically easier to constrain than the absolute A baseline to `~0.005 deg`.

Whether it actually is easier must be tested rather than assumed.

---

## 10. Current experimental interpretation

The hierarchy is now sharper:

```text
sample B alone
-> cannot carry the full identifiability burden

mid/deep A phase calibration
-> far too weak for the leading short-wave A mode

broad static spectral self-fit
-> still nearly singular

therefore
-> use an independently constrained physical baseline
   or a causal differential perturbation that cancels the static baseline.
```

This is a stronger conclusion than merely saying that `0.005 deg` calibration is challenging.

The current model says that **spectral phase data from the same static device family do not naturally provide that calibration.**

---

## 11. What remains conditional

This result assumes

- the current 72-member A profile sensitivity family;
- Hansen/Moazzami Beer-Lambert optical kernels;
- first three short-wave A/B smooth SVD modes as the nuisance model;
- the illustrative 25% A-localized anomaly;
- equal independent phase noise;
- phase-only mean-delay information.

A richer physical model, amplitude information, bias response, temperature response, microscopic transport constraints, or independent structural information can add genuinely new directions.

That is precisely why the next step should introduce a **new physical perturbation**, not merely more samples of the same static spectrum.

---

## 12. Next decisive collision

Test whether a temperature-controlled short-wave difference-in-differences measurement can remove the static A-baseline degeneracy while preserving useful sensitivity to the nonlinear-region transport response.

The first checks should be:

1. construct temperature-retuned short-wave A/B kernels with a common wavelength at each temperature;
2. keep the lower wavelength inside the validated optical model rather than extrapolating below `2 um`;
3. quantify how much of the static six-mode nuisance subspace cancels in temperature difference;
4. derive the residual calibration/drift precision required for a transport-change observable.

Numerical implementation for the present self-calibration test:

`numerics/hgcdte_sample_a_crossband_self_calibration.py`
