# Direct Transport-Witness Posterior Propagation

**Date:** 2026-08-10  
**Status:** conditional linearized posterior-propagation design using direct \(v(E,x)\), \(D(E,x)\), and τ witness coordinates; provisional detector covariance; no novelty claim

## 1. Why this is stronger than putting priors on an empirical velocity formula

The relocation experiment does not need to infer a generic HgCdTe velocity law from its own detector traces if companion material measures that law directly.

Therefore the clean uncertainty propagation is not

```text
fit mu,d,r from relocation data
```

but

```text
measure v(E,x), D(E,x), tau(E,x)
on companion p-type material
-> interpolate those measured surfaces through the graded absorber
-> propagate their posterior into the first-passage relocation model.
```

This also avoids forcing the witness data to obey the same compact empirical velocity formula used only as the synthetic central truth.

---

## 2. Witness grid

Use the current minimal three-composition set

```math
\boxed{x=0.35,\ 0.43,\ 0.51.}
```

and the field grid

```text
0.1, 0.3, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0 kV/cm.
```

This gives

```text
24 direct velocity nodes
24 direct diffusion nodes
3 composition-dependent lifetime amplitudes
```

in the first posterior stress.

The local graded-device transport values are bilinearly interpolated through `x` and field.

The current programmed high-gradient regions extend slightly beyond the witness endpoints to approximately

```text
x ~0.344-0.517.
```

The present numerical stress therefore performs only a very small linear edge extrapolation.

A real calibration should preferably move the endpoint witnesses slightly outward or explicitly propagate that extrapolation uncertainty.

---

## 3. Synthetic central truth is not a posterior restriction

For a controlled numerical regression, the central synthetic velocity surface is generated from

```math
v(E)=\frac{\mu E}{1+(E/d)^r}
```

with

```text
mu = 9000 cm2/Vs
d = 8 kV/cm
r = 2.2.
```

The synthetic diffusion center uses

```math
D=\mu k_BT/q
```

and the synthetic lifetime is `1 ns`.

However, the Fisher nuisance coordinates move **each velocity and diffusion witness node independently**.

Thus the posterior is not forced to retain

```text
the empirical analytic velocity law
or
Einstein diffusion.
```

The central formulas merely provide a reproducible reference surface around which uncertainty is propagated.

---

## 4. Detector model used for the propagation

The relocation device retains the active downstream orientation:

```text
high-Cd optical entrance
-> decreasing x(z)
-> low-Cd collecting junction.
```

Use

```text
feature centers = 2.6, 4.4, 5.6 um
lambda = 2.00-2.40 um
f = 0.5, 1, 2, 3 GHz.
```

The local force follows the quasi-neutral gap-gradient model plus one majority-band tilt coordinate

```math
\rho
=\ln\frac{(N_A/N_v)(L)}{(N_A/N_v)(0)}.
```

The first-passage solver uses the directly interpolated

```text
v(E,x)
D(E,x)
tau(E,x).
```

The DOS drift correction remains in the reduced form

```math
D\,d\ln N_c/dz.
```

Each device/RF channel receives an arbitrary wavelength-independent phase and `ln|H|` intercept.

---

## 5. Provisional measurement covariance

The detector experiment still uses the provisional information weight

```math
\boxed{
w(\lambda,f)
=|H|\sqrt{P_{\rm abs}C_{\rm dc}}.
}
```

and an equal weighted phase / `ln|H|` component-noise scale

```math
\sigma_{\rm comp}=0.10^\circ.
```

This is not measured covariance.

The absolute `sigma` values below therefore remain **design scales**, not expected experimental significances.

---

## 6. Numerical convergence matters

A reduced five-field quick study initially suggested a looser velocity calibration requirement.

The full eight-field posterior has more local freedom and is the more conservative model.

Spatial convergence also shifts the velocity-only threshold moderately.

The current canonical regression uses `641` spatial points, with higher-grid spot checks near the same scale.

Do not quote more significant digits than the model supports.

---

## 7. Velocity-only witness requirement

First leave

```text
D(E,x)
tau(E,x)
```

completely unconstrained by the witness posterior.

Give every direct velocity node the same independent log uncertainty

```math
\sigma_{\ln v}.
```

Use the very weak majority-band-tilt prior

```math
\sigma_\rho=1.6.
```

The current `3 sigma` mechanism threshold occurs at approximately

```math
\boxed{
\sigma_{\ln v}\lesssim0.22-0.24.
}
```

A useful rounded requirement is therefore

```text
~20% log precision
```

or roughly `25%` multiplicative one-sigma precision on the direct velocity surface.

That is a much more demanding requirement than the earlier reduced-grid estimate, but it remains a realistic transit-metrology target.

---

## 8. Measuring the whole carrier packet relaxes the velocity requirement sharply

Now suppose the same witness experiment also constrains

```math
\sigma_{\ln D}=0.5,
\qquad
\sigma_{\ln\tau}=0.5.
```

Those are very coarse uncertainties: roughly factor `1.65` per sigma.

Then the allowed equal velocity-node uncertainty for the same current `3 sigma` relocation threshold becomes approximately

```math
\boxed{
\sigma_{\ln v}\lesssim0.74.
}
```

That is approximately a factor

```math
e^{0.74}\approx2.1
```

per sigma.

Therefore:

> **the witness should measure arrival time, packet broadening, and packet decay together.**

Even coarse independent information about diffusion and lifetime prevents the relocation detector from using those degrees of freedom to imitate a different velocity curve.

---

## 9. The middle composition is quantitatively necessary

Fix the two endpoint witness velocity surfaces to

```math
\sigma_{\ln v}(x=0.35)
=\sigma_{\ln v}(x=0.51)
=0.20.
```

Leave `D` and `tau` unconstrained.

If the `x=0.43` velocity surface is **not measured at all**, the current mechanism significance falls below `3 sigma`.

At the converged full-field stress, the middle witness requires approximately

```math
\boxed{
\sigma_{\ln v}(x=0.43)
\lesssim0.37-0.39
}
```

to recover the current `3 sigma` threshold.

That corresponds to only about `45-50%` multiplicative one-sigma precision.

The middle witness is therefore not redundant.

It prevents unmeasured curvature in

```math
v(E,x)
```

from hiding between two calibrated endpoint compositions.

---

## 10. Majority-band / doping-profile knowledge can remain very coarse

With direct velocity-surface uncertainty near

```text
sigma_ln(v) ~0.20
```

and `D,tau` otherwise free, the current `3 sigma` threshold allows a total majority-band tilt uncertainty of order

```math
\sigma_\rho\sim1.7-1.9.
```

Since

```math
\rho=\ln[(N_A/N_v)(L)/(N_A/N_v)(0)],
```

this corresponds to a several-fold multiplicative uncertainty in the total ratio across the absorber.

Thus ordinary Hall/doping/profile characterization is unlikely to need extraordinary precision for the quasi-neutral **interior** correction.

Non-quasi-neutral junction and boundary fields remain a separate calibration problem.

---

## 11. Correlated witness calibration errors

Many witness errors will not be independent.

For example,

```text
transport distance calibration
time-base calibration
or a common geometry scale
```

can shift every measured velocity by nearly the same multiplicative factor.

Represent a witness-family covariance as

```math
C
=\sigma_{\rm shape}^2I
+\sigma_{\rm common}^2\mathbf1\mathbf1^T.
```

A deliberately extreme stress uses

```text
velocity shape sigma = 0.20
diffusion shape sigma = 0.50
lifetime shape sigma = 0.50
common log-scale sigma = 10
```

for each family.

The current mechanism scale remains approximately

```math
\boxed{5.8\sigma}
```

under the provisional detector-noise convention.

Therefore the inverse is much more sensitive to the **shape** of transport versus field/composition than to one absolute global calibration scale once `v`, `D`, and `tau` are measured together.

---

## 12. Experimental implication

The witness experiment should be designed around **differential transport shape**, not heroic absolute accuracy.

A strong protocol is:

1. use at least two propagation distances for each composition;
2. use the same field grid at every witness composition;
3. extract packet centroid, width, and integrated amplitude;
4. fit common timing/length calibration parameters explicitly;
5. retain their covariance rather than converting every point to independent error bars;
6. propagate the full posterior to the relocation model.

This naturally separates

```text
common calibration scale
from
field-dependent transport shape.
```

---

## 13. Why three compositions remain the minimum sensible set

Two endpoint compositions can calibrate a linear interpolation only by assumption.

The third composition allows the experiment to test that assumption.

The posterior calculation shows that the middle point needs only moderate precision, but leaving it absent is enough to cross the current mechanism-identifiability boundary.

Therefore the present minimal witness set remains

```math
\boxed{x\approx0.35,\ 0.43,\ 0.51.}
```

A fourth composition should be added only if the middle point demonstrates significant curvature that cannot be covered by the propagated interpolation error.

---

## 14. Important limitation — central \(D\) still uses Einstein only to generate synthetic data

The synthetic center uses

```math
D=\mu k_BT/q.
```

But direct p-type HgCdTe transit data show that diffusion mobility can exceed drift mobility under hot-electron conditions.

Therefore the real workflow must use

```text
measured D(E,x)
```

independently.

The present posterior already permits every `D(E,x)` node to vary independently, so this limitation affects only the synthetic center, not the structure of the uncertainty model.

The next transport refinement should use a non-Einstein synthetic center informed by witness or published data once appropriate `300 K` values exist.

---

## 15. What is now actually required from the witness experiment

The earlier phrase “measure \(v,D,	au\)” was correct but vague.

The current posterior makes it concrete:

### minimum velocity-only route

Aim for roughly

```text
20-25% local velocity-surface precision
```

across the full field/composition grid if diffusion and lifetime remain otherwise uncalibrated.

### preferred whole-packet route

If `D` and `tau` are each constrained only to factor-`~1.6` scales, velocity can be much less precise—roughly factor `~2` per sigma in the present model.

### composition interpolation

The middle `x~0.43` witness should reach at least roughly

```text
40% log-scale precision
```

when endpoint velocity surfaces are around `20%`.

These are intentionally rounded design targets.

---

## 16. Consequence for the main relocation experiment

The next stage should **not** reoptimize feature depths yet.

First replace the synthetic witness priors with a plausible measurement covariance from an actual Shockley–Haynes / pulse-transport geometry.

Then:

```text
witness posterior
+
measured x(z) posterior
+
measured detector complex covariance
->
first-passage relocation posterior
->
reoptimize feature depths / wavelength / RF / growth order.
```

This is the first point in the research chain where the dominant transport uncertainty can be tied to a conventional, independently measurable material property rather than an arbitrary inverse prior.

---

## 17. Numerical implementation

`numerics/hgcdte_transport_witness_posterior_propagation.py`
