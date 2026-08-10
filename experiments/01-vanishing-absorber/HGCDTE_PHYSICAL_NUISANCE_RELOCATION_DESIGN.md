# Physical-Nuisance Relocation Design — Corrected Mechanism-Identifiability Limit

**Date:** 2026-08-10  
**Status:** corrected conditional response-geometry design around the downstream drift–diffusion model; a previous high-RF Fisher advance was invalidated by a complex-log branch-cut artifact; no novelty claim

## 1. Question

The downstream first-passage calculation predicts a large, readily measurable transport response when the buried composition-gradient feature is moved.

The harder question is:

> **Can that response be attributed specifically to the localized gradient field if ordinary mobility, recombination, overall field scale, high-field velocity law, and entrance-surface loss are not independently known?**

This file answers that mechanism-identifiability question around one explicit central transport model.

---

## 2. Mechanism coordinate

Keep the realized optical composition profile `x(z)` fixed.

Let

```math
s(z)=|dx/dz|
```

be the programmed composition-slope magnitude and

```math
s_0=(x_{\rm front}-x_{\rm back})/L
```

the same-endpoint smooth background slope.

For transport sensitivity only define

```math
\boxed{
s_{\rm eff}(z;\eta)
=s_0+\eta[s(z)-s_0].
}
```

`eta=1` gives the full programmed local-gradient transport field.

`eta=0` removes the localized slope deviation from the **transport field** while retaining the same measured optical `x(z)` profile.

This is a nested statistical mechanism coordinate, not a claim that `eta` is a laboratory knob or a separately self-consistent crystal.

The target derivative is

```math
\partial\ln H/\partial\eta.
```

---

## 3. Central sensitivity point

Use

```text
T = 300 K
mu_n = 9000 cm2/Vs
chi_E = 0.50
tau_rec = 1.0 ns
v_sat = 1e5 m/s
entrance S = 1e5 cm/s.
```

These are sensitivity coordinates, not calibrated device parameters.

The velocity-saturation law is also a reduced uncertainty model rather than a validated HgCdTe high-field constitutive law.

---

## 4. Physical nuisance directions

Marginalize the localized-gradient target against free common derivatives with respect to

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

Also allow an arbitrary wavelength-independent

```text
phase offset
and
ln|H| offset
```

for every device and RF frequency.

Thus an apparent mechanism signal cannot come merely from a constant electrical/channel phase or gain.

---

## 5. Provisional signal weighting

Use

```math
\boxed{
w(\lambda,f)
=|H(\lambda,f)|
\sqrt{P_{\rm abs}(\lambda)C_{\rm dc}(\lambda)},
}
```

where `C_dc` is the modeled DC collection probability.

This is a provisional statistics-like information weight only.

It reflects the fact that points with weak absorption, poor collection, or attenuated RF response carry less information.

It must ultimately be replaced by measured wavelength × RF phase/magnitude covariance.

---

## 6. Critical numerical correction — do not finite-difference the principal complex logarithm

The first version of this calculation evaluated

```math
\frac{\ln H(p+\delta)-\ln H(p-\delta)}{2\delta}
```

using the principal complex logarithm.

At high RF, phase can cross the branch cut of `log`, producing an artificial `2pi` jump and a false large derivative.

That artifact created the earlier apparent `~4-5 degree` mechanism separation at high RF.

The correct branch-safe derivative is

```math
\boxed{
\frac{\partial\ln H}{\partial p}
=
\frac{1}{H}\frac{\partial H}{\partial p}.
}
```

Numerically use

```math
\boxed{
\frac{1}{H(p)}
\frac{H(p+\delta)-H(p-\delta)}{2\delta}.
}
```

All results below use this corrected derivative.

The previously reported dramatic high-RF Fisher improvement is **invalidated**.

---

## 7. Corrected result — the transport signal is large, but mechanism attribution remains poor

The physics-derived first-passage model still gives degree-scale field-induced phase changes over broad transport stresses.

That result is unaffected by the logarithm-derivative correction.

What changes is the **local parameter identifiability**.

Using

```text
lambda = 2.00-2.40 um
RF = 0.5, 1, 2, 3 GHz
```

and the provisional signal-dependent weighting, the localized-gradient derivative remains almost inside the span of the five generic physical transport nuisance derivatives.

The best current three-depth design has a target-to-nuisance angle of only about

```math
\boxed{0.12^\circ.}
```

This is an extremely weak structural separation.

---

## 8. Corrected depth optimization

Scan feature centers

```text
2.0 to 5.6 um
in 0.2-um steps
```

with at least `0.4 um` between selected centers.

For

```text
RF = 0.5, 1, 2, 3 GHz
```

the fixed-resource optima are approximately:

### Two depths

```math
\boxed{5.2,\ 5.6\ \mu{\rm m}}
```

with score

```text
~1.40e-4.
```

### Three depths

```math
\boxed{2.4,\ 5.2,\ 5.6\ \mu{\rm m}}
```

with the largest current score

```math
\boxed{S\approx1.59\times10^{-4}}
```

and target-to-nuisance angle

```math
\boxed{\theta\approx0.122^\circ.}
```

### Four depths

```text
~3.4, 4.4, 5.2, 5.6 um
```

with a **lower** fixed-resource score.

### Five depths

```text
~2.4, 3.4, 4.4, 5.2, 5.6 um
```

again with a lower score.

Therefore simply adding more translated devices does not cure the transport-law degeneracy.

Three depths already saturate the no-prior information under this reduced central model.

---

## 9. High RF is useful for measuring transport, but not enough for mechanism attribution

For the corrected three-depth design:

```text
0.25, 0.50, 1.0 GHz
-> score ~1.38e-4

0.5, 1, 2, 3 GHz
-> score ~1.59e-4

1.5, 2, 2.5, 3 GHz
-> score ~1.47e-4.
```

Thus extending to higher RF provides only a modest improvement once the derivative is evaluated correctly and the signal attenuation is included.

The important distinction is now:

> **High RF can reveal a large non-single-pole transport response, but it does not by itself identify whether that response came from the localized gradient field or from a different high-field velocity law.**

That is a much stronger and more defensible conclusion than the superseded high-RF Fisher claim.

---

## 10. Why the degeneracy is physically reasonable

The localized gradient changes the carrier drift history.

But so do

```text
mobility
field-to-band-edge partition
recombination lifetime
velocity saturation
surface loss.
```

Within a short one-dimensional absorber, several of those parameters alter the first-passage distribution in very similar ways.

A wavelength × RF scan can measure that the transport law is different.

Without independent constraints, it cannot reliably say which constitutive parameter caused the difference.

This is not a failure of signal amplitude.

It is a **mechanism-identifiability limit**.

---

## 11. Experimental consequence — independent transport calibration is mandatory

The next step is no longer “add more wavelengths” or “add more RF points.”

The highest-value question is:

> **How tightly must the generic high-field transport law be independently constrained before the translated-gradient mechanism parameter becomes identifiable?**

The obvious calibration targets are

```text
mobility / low-field diffusion
recombination lifetime
high-field velocity relation
surface recombination / passivation response
and the effective band-edge field partition.
```

Some can be measured on dedicated calibration structures rather than inferred simultaneously from the relocation devices.

The high-field velocity law is likely the most important because allowing `v_sat` to float was the dominant collapse in earlier pairwise stresses.

---

## 12. Relation to the randomized/replicated growth series

Randomized feature-depth order and replicated depths remain good experimental-design principles because they reject fabrication drift and estimate random run-to-run variation.

But their **old numerical depth/order optima are not current prescriptions**.

More importantly, randomization cannot solve a constitutive-law degeneracy that is common to every device.

Therefore the correct hierarchy is now

```text
1. independently calibrate generic transport law;
2. measure/characterize realized x(z) for every device;
3. then optimize translated depths / randomized growth order;
4. finally test whether the residual depth law requires the localized gradient term.
```

---

## 13. Optical uncertainty remains open

The sparse wavelength optimization performed before the branch-cut correction is also superseded.

Do not freeze exact wavelength supports yet.

The broad short-wave band

```text
~2.0-2.4 um
```

still gives strong internal generation-depth leverage in the corrected orientation, but exact support must be redone after

```text
measured x(z) uncertainty
absorption-model uncertainty
substrate/backside transfer
reflection/interference
and real covariance
```

are propagated.

---

## 14. Current strongest conclusion

The project now has two separate statements:

### Signal feasibility

**CHECKED / CONDITIONAL:** a physically derived downstream drift–diffusion model predicts a sizable wavelength-dependent RF response when the buried graded-field feature is moved.

### Mechanism identifiability

**NEGATIVE / CONDITIONAL:** in the same reduced model, that response is almost degenerate with plausible uncertainty in the generic transport law unless those transport parameters are independently constrained.

That distinction should remain explicit in every future claim.

---

## 15. Numerical implementation

`numerics/hgcdte_physical_nuisance_relocation_design.py`
