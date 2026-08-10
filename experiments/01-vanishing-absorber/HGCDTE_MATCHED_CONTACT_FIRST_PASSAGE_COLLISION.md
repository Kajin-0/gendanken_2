# Matched-Contact Buried Gradient — Minimal First-Passage Transport Collision

**Date:** 2026-08-09  
**Status:** conditional comparison of two deliberately simple transport limits; same downstream-compensated composition family and optical kernels; no calibrated device timing prediction; no novelty claim

## 1. The question has changed

The matched-contact downstream-compensated family is now geometrically clean enough that the main uncertainty is no longer

```text
can a buried gradient be created while matching the contact side?
```

It is

> **What timing response does that field redistribution actually produce?**

It would be a mistake to answer by assuming

```text
more composition-gradient field -> proportionally faster carrier velocity.
```

The repository has already rejected low-field mobility extrapolation as a universal high-field shortcut.

A still more basic issue appears before high-field physics is even added: **diffusion and boundary conditions can change the sign of the net transit response.**

---

## 2. Do not assert a carrier/band-edge direction from `|dEg/dz|` alone

The accessible published A/B material description gives composition and gradient-field magnitudes but does not expose enough band-edge/doping detail to justify assigning a specific electron-versus-hole collection force from the gap-gradient magnitude alone.

Therefore this calculation uses

```math
F(z)>0
```

only as a conditional **effective field magnitude that assists the collected minority carrier toward `z=0`.**

It does not claim that the present thought-device composition orientation automatically produces that sign for a particular carrier.

A realizable device design must specify the band offsets, doping/junction orientation and electrostatics explicitly.

---

## 3. Same field profiles, two simple transport limits

Use the preferred downstream-compensated family:

```text
control field ~142 V/cm baseline
beta=1 buried peak ~284 V/cm
beta=2 ~425 V/cm
beta=3 ~567 V/cm
```

with compensation behind the `z~4.9 um` feature.

Compare two models.

### Model A — deterministic local drift

```math
\boxed{
v(z)=\mu F(z),
}
```

so

```math
\boxed{
T_{\rm drift}(z)
=\int_0^z\frac{ds}{\mu F(s)}.
}
```

This is the simplest local-drift picture and strongly penalizes any low-field segment because transit time contains `1/F`.

### Model B — Einstein drift-diffusion first passage

Use

```math
D=\mu V_T,
\qquad
V_T=k_BT/q,
```

and the stochastic coordinate

```math
dz
=-\mu F(z)dt
+\sqrt{2D}\,dW.
```

For absorbing collection at the front and a reflecting back boundary,

```math
\boxed{
D T''(z)-\mu F(z)T'(z)=-1,
}
```

with

```math
T(0)=0,
\qquad
T'(L)=0.
```

---

## 4. Mobility factors out of the drift-diffusion shape

Define

```math
\boxed{U(z)=\mu T(z).}
```

Then

```math
\boxed{
V_T U''(z)-F(z)U'(z)=-1.
}
```

Thus, inside this Einstein model:

> **the spatial and spectral shape of the timing perturbation is independent of the chosen mobility; absolute time scales as `1/mu`.**

This makes the model useful as a structural diagnostic without pretending one exact room-temperature mobility applies to every composition/doping state.

All numerical phase examples below use only a reference scaling

```math
\mu_{\rm ref}=10^4\ \mathrm{cm^2/(V\,s)}
```

and can be rescaled exactly as

```math
\Delta T,\Delta\phi
\propto
\mu_{\rm ref}/\mu.
```

The value is a scale coordinate, not a calibrated mobility for the proposed device.

---

## 5. Control transit already shows diffusion is not a tiny correction

At 300 K:

```math
V_T\approx25.85\ \mathrm{mV}.
```

The total composition-gradient potential drop of the endpoint-matched control is about

```math
\boxed{0.108\ \mathrm V\approx4.18\,V_T.}
```

So the layer is not in an asymptotically infinite-Peclet limit.

At the reference mobility, a carrier starting at the back has

```text
deterministic drift transit ~535 ps

reflecting-back drift-diffusion mean first passage ~409 ps.
```

The difference is already substantial before any buried feature is added.

---

## 6. Deterministic drift says concentrating the fixed field drop makes deep transit slower

Because all members have the same composition endpoints, the total gap-derived field drop is redistributed rather than increased.

The high-field buried region is paid for by a lower-field region behind it.

For deterministic local drift, that low-field segment dominates `1/F`.

Back-start transit at the reference mobility becomes approximately

```text
control  -> 535 ps
beta=1   -> 561 ps
beta=2   -> 649 ps
beta=3   -> 981 ps.
```

Thus the strongest buried gradient makes the deep deterministic transit **much slower**, even though it locally raises the field near `4.9 um`.

This is the familiar convexity penalty of redistributing a fixed field budget in a local drift-only model.

---

## 7. Drift-diffusion gives the opposite net trend

With the absorbing-front / reflecting-back Einstein first-passage model, the same structures give approximately

```text
control  -> 409 ps
beta=1   -> 399 ps
beta=2   -> 393 ps
beta=3   -> 391 ps
```

at the same reference mobility scale.

Here diffusion reduces the penalty of the weak back-side region enough that the buried assisting field produces a modest net reduction in mean first-passage time.

Therefore even the **sign** of the overall timing change is not robust between these two simple limits.

---

## 8. Use the known contrast optical kernel when comparing transport hypotheses

The control and contrast composition profiles have different internal optical kernels.

To isolate transport rather than optical-generation change, compare two hypotheses using the **same contrast-device generation distribution** `p_beta(z,lambda)`:

### Null transport hypothesis

```math
T_{\rm null}(\lambda)
=\int p_\beta(z,\lambda)T_0(z)dz.
```

### Buried-gradient transport hypothesis

```math
T_{\rm alt}(\lambda)
=\int p_\beta(z,\lambda)T_\beta(z)dz.
```

The model-discrimination signal is

```math
\boxed{
\Delta T_{\rm tr}(\lambda)
=T_{\rm alt}-T_{\rm null}.
}
```

This prevents ordinary control/contrast generation-depth differences from being mislabeled as transport.

---

## 9. Both simple models predict a large spectral signature — but not the same physics

After removing wavelength-independent delay and converting to `1 GHz` phase at the reference mobility:

### Deterministic drift

```text
beta=1 -> ~10.7 deg peak-to-peak
beta=2 -> ~33.7 deg
beta=3 -> ~87.8 deg.
```

### Drift-diffusion first passage

```text
beta=1 -> ~4.29 deg peak-to-peak
beta=2 -> ~7.62 deg
beta=3 -> ~10.16 deg.
```

All values scale as

```math
10^4/\mu
```

for mobility in `cm^2/(V s)` inside these surrogates.

The important conclusion is **not** that the signal will be this large.

It is:

> **the proposed matched-contact ladder is capable of producing a spectrally structured timing response in simple transport models, but the magnitude and even overall transit trend are strongly model dependent.**

---

## 10. Why neither surrogate is a device prediction

Both models omit important HgCdTe device physics:

```text
self-consistent junction / doping electrostatics
velocity saturation and non-ohmic transport
hot-electron / nonlocal energy relaxation
recombination and finite lifetime
surface/back recombination instead of a reflecting boundary
trap dynamics
space charge under optical loading
field-dependent optical absorption
contact and series resistance
diffusion-coefficient deviations from a simple Einstein form.
```

The deterministic model is especially unreliable when diffusion is material.

The reflecting-back drift-diffusion model is also a strong boundary assumption, not a measured device condition.

Therefore no speedup/slowdown claim should be attached to the `beta` ladder yet.

---

## 11. The result is still useful

The collision gives the purpose-built validation experiment a clearer role.

A matched gradient-strength ladder can test **which transport description is consistent with the measured wavelength × RF response**.

For example, a measured spectral timing change that

```text
scales with beta
appears at the designed buried spectral coordinate
and
matches one independently specified transport model across RF frequency
```

would be much stronger evidence than fitting an arbitrary `q(z)` profile to one device.

Conversely, failure of the timing signature to follow the designed gradient ladder would directly falsify the assumed mechanism/model.

---

## 12. Next decisive model

The next transport calculation should sit between the two extremes above:

> **solve a one-dimensional drift-diffusion / continuity model with finite recombination and explicit back-surface boundary condition, while treating the buried composition profile and optical generation exactly.**

Before making it more microscopic, sweep the unknown but physically meaningful boundary parameters:

```text
minority-carrier lifetime
back-surface recombination velocity
common junction/bulk electric field
mobility / diffusion scale.
```

The goal is not to fit arbitrary parameters.

It is to determine whether the **sign and spectral location** of the beta-dependent timing response survive realistic boundary/recombination uncertainty.

Only after that should high-field nonlocal corrections be added.

Numerical implementation:

`numerics/hgcdte_matched_contact_first_passage_surrogate.py`
