# Matched-Contact Buried Gradient — The Drift/Drift-Diffusion Conflict Is a `D/mu` Crossover

**Date:** 2026-08-09  
**Status:** conditional continuous transport-regime calculation for the preferred downstream-compensated family; reflecting back boundary and infinite bulk lifetime for the crossover map; common assisting-field sensitivity; no calibrated `D/mu` for the proposed device; no novelty claim

## 1. Replace a binary model disagreement by one continuous parameter

The preceding transport studies gave

```text
deterministic local drift
-> strong low-field-compensation penalty

Einstein drift-diffusion
-> modest buried-gradient speedup.
```

Rather than treating these as unrelated models, write the general local drift-diffusion mean first-passage equation

```math
D T''-\mu F T'=-1.
```

Define

```math
\boxed{
\Theta\equiv D/\mu
}
```

with units of volts and

```math
U=\mu T.
```

Then

```math
\boxed{
\Theta U''-F U'=-1.
}
```

Thus `Theta` continuously controls the relative importance of diffusion and drift independently of the absolute mobility scale.

---

## 2. Limiting interpretations

### Deterministic local drift

Formally

```math
\Theta\to0.
```

The equation reduces toward

```math
-FU'=-1,
```

or

```math
T'(z)=1/[\mu F(z)].
```

### Nondegenerate Einstein reference

For a nondegenerate carrier population in local thermal equilibrium,

```math
\boxed{
D/\mu=k_BT/q.
}
```

At 300 K:

```math
\boxed{
\Theta_E\approx25.85\ {\rm mV}.
}
```

The thought device is **not assumed** to obey this classical relation exactly. Degeneracy, nonlocal transport, high-field effects and nonequilibrium carrier distributions can modify the effective relation between diffusion and mobility.

The purpose of `Theta_E` here is only to provide a familiar thermal reference for the numerically determined crossover.

---

## 3. Crossover calculation

Use the preferred matched-contact downstream-compensated family:

```text
beta=1,2,3
buried enhancement near 4.90 um
compensation behind the feature
same front profile and composition endpoints.
```

Use

```text
300 K
reflecting back boundary
infinite bulk lifetime
contrast-device optical generation kernel in both null and alternative
common assisting field = 0, 100, 300 V/cm.
```

Sweep

```math
0.5\ {\rm mV}
\le D/\mu\le
50\ {\rm mV}.
```

Two sign observables are followed.

### Wavelength-averaged transport shift

```math
\overline{\Delta T}
=\langle T_\beta-T_0\rangle_\lambda.
```

### Gauge-free spectral endpoint differential

```math
\boxed{
\Delta T_{\rm end}
=
\Delta T(3.83\,\mu{\rm m})
-
\Delta T(2.80\,\mu{\rm m}).
}
```

The endpoint differential is the cleaner inverse observable because it is insensitive to a wavelength-independent common delay.

---

## 4. Zero added common field

### `beta=1`

The wavelength-averaged timing shift is already on the speedup side throughout the `0.5-50 mV` search interval, although the deterministic limit is extremely close to neutral for the spectrally weighted mean.

The endpoint differential changes sign at

```math
\boxed{
\Theta_{\rm end}\approx9.15\ {\rm mV}.
}
```

### `beta=2`

Mean timing crossover:

```math
\boxed{
\Theta_{\rm mean}\approx6.63\ {\rm mV}.
}
```

Endpoint crossover:

```math
\boxed{
\Theta_{\rm end}\approx13.46\ {\rm mV}.
}
```

### `beta=3`

Mean timing crossover:

```math
\boxed{
\Theta_{\rm mean}\approx8.93\ {\rm mV}.
}
```

Endpoint crossover:

```math
\boxed{
\Theta_{\rm end}\approx15.84\ {\rm mV}.
}
```

Thus the earlier deterministic-versus-Einstein disagreement is not a numerical pathology.

It is a real transport-regime crossover.

---

## 5. Added common assisting field moves the crossover but does not exceed the 300 K Einstein reference in this bracket

Repeat for an added common field shared by control and contrast.

The endpoint crossover moves upward because the common drift reduces the relative effect of diffusion and of the local field redistribution.

Across all

```text
beta=1,2,3
common field = 0, 100, 300 V/cm,
```

the **largest** endpoint-differential crossover is approximately

```math
\boxed{
\Theta_{\rm end,max}\approx21.41\ {\rm mV}.
}
```

This occurs inside the strong-common-field portion of the sensitivity bracket.

The classical 300 K Einstein value is still above it:

```math
25.85-21.41
\approx
\boxed{4.44\ {\rm mV}}.
```

---

## 6. At `D/mu = kBT/q`, every tested design/common-field case lies on the same sign branch

Evaluate all nine

```text
3 beta values x 3 common-field values
```

at

```math
D/\mu=25.85\ {\rm mV}.
```

For every case:

```text
wavelength-averaged contrast-minus-control timing shift < 0
and
endpoint differential < 0.
```

Within this local drift-diffusion model, the nondegenerate Einstein reference therefore predicts that the buried-gradient redistribution reduces the mean collected transit time and gives the same spectral sign across the complete common-field bracket.

---

## 7. This substantially narrows the earlier ambiguity

The project no longer has an undefined choice between two unrelated narratives.

The timing sign is controlled by a concrete parameter:

```math
\boxed{D/\mu.}
```

Roughly:

```text
small D/mu
-> compensation penalty dominates
-> local-drift-like branch

D/mu above ~10-20 mV
-> diffusion assists crossing the weak compensation region
-> buried-gradient speedup branch.
```

The exact threshold depends on gradient strength, common field and observable.

---

## 8. Why the gauge-free crossover is the more important one

A wavelength-independent change in total delay is experimentally entangled with device/electronics common delay.

Therefore the sign of

```math
\overline{\Delta T}
```

is less robust experimentally than the sign of spectral structure.

The endpoint differential

```math
\Delta T(3.83)-\Delta T(2.80)
```

is explicitly differential in wavelength and survives the common-delay gauge.

Its crossover is consistently higher than the mean-delay crossover.

For the strong `beta=3`, zero-common-field structure:

```text
mean sign becomes diffusion-like near 8.93 mV
endpoint spectral sign near 15.84 mV.
```

This separation matters when comparing transport models to data.

---

## 9. Relationship to the finite-lifetime/back-boundary result

The separate finite-recombination calculation fixed

```math
D/\mu=k_BT/q
```

and then varied

```text
bulk lifetime
back boundary
common field.
```

It found that the `beta=3` endpoint sign remained on the speedup branch across that full sensitivity set.

The present crossover calculation explains why:

```text
25.85 mV
```

lies safely above the no-killing crossover values found here.

So finite lifetime and boundary loss reduce the signal but do not create the fundamental sign ambiguity.

The ambiguity comes from the diffusion-to-mobility ratio itself.

---

## 10. What must now be known about a real device

The next transport question is much sharper than `what is the mobility?`

The crucial combination is

```math
\boxed{D/\mu,}
```

along with the actual carrier/band-edge force direction.

A mobility value by itself cannot decide which timing branch applies.

Likewise, fitting a single effective velocity from one frequency or wavelength would hide the mechanism.

The real validation should constrain or predict

```text
carrier type and band-edge slope
D/mu or generalized Einstein relation
common junction/bulk field
recombination / boundary loss
and RF-frequency response.
```

---

## 11. Remaining caution

This is still a local drift-diffusion model.

It omits

```text
velocity saturation
hot-carrier / nonlocal energy relaxation
field-dependent scattering
degenerate-carrier corrections
traps
space charge
self-consistent junction electrostatics.
```

Those effects can invalidate the simple constant `D/mu` description.

But the calculation has already done something useful:

> **it identifies a quantitative transport-regime boundary that any more complete model must reproduce or explain away.**

---

## 12. Next decisive work

The strongest next move is not another arbitrary transport parameter sweep.

It is to anchor the thought device to a **self-consistent band-edge and carrier model**:

1. specify p-type or n-type absorber / junction orientation;
2. decompose the graded bandgap into conduction- and valence-band edges rather than using `|dEg/dz|` alone;
3. determine the sign and magnitude of the force on the collected minority carrier;
4. use a generalized `D/mu` appropriate to the resulting carrier statistics;
5. then rerun the `beta=0,1,2,3` timing ladder.

If that physically specified model still lands above the `~10-20 mV` crossover and preserves the buried spectral signature, the matched-contact validation design becomes substantially more credible.

Numerical implementation:

`numerics/hgcdte_matched_contact_diffusion_ratio_crossover.py`
