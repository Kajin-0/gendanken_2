# Finite-generation-kernel × electrostatic-gradient interaction

**Date:** 2026-08-15  
**Status:** **CHECKED in conditional model / DERIVED MECHANISM PARTIALLY ISOLATED / PRIORITY UNPROVEN**

## 1. Why this note is necessary

The first Paper-02 electrostatic calculation showed that a full-width planar device with a collector-side depletion field can return a positive apparent diffusion coefficient even though the trajectory model contains no microscopic diffusion.

A local deterministic field-gradient theorem was then derived for point sources launched inside a region where `v'(z) != 0`.

However, the actual HgCdTe spectral channels used by the numerical stress have mean generation depths

```text
2.0, 2.5, 3.0, 3.5, 4.0, 4.5 um,
```

while the 3.0 um collector-side depletion region in a 7.6 um absorber begins at

```math
z_d=7.6-3.0=4.6\ \mu\mathrm m.
```

Therefore all six nominal source centers lie upstream of the field-gradient region.

The calibrated optical kernels nevertheless have finite width and tails that extend past `z_d`.

This raises a sharper causal question:

> Is the observed false diffusion a local effect at the source centers, or does it require finite generation width overlapping the downstream electrostatic gradient?

The point-source versus finite-kernel calculation answers this directly.

---

## 2. Reproducible calculation

Script:

```text
experiments/01-vanishing-absorber/numerics/paper02_point_vs_kernel_causal_test.py
```

GitHub Actions run:

```text
run id       31917583825
artifact     paper02-point-vs-kernel
artifact id  9255370581
sha256       715e6f2775cfe77888b7a9b55f4e71cf4ae4c92bd0fbe1831839d7b022794ad7
```

Common device model:

```text
absorber thickness            7.6 um
full-width planar contact     yes
depletion width               3.0 um
depletion start               4.6 um
space-charge drop             0.05 V
total bias                    0.30 V
microscopic diffusion         0
recombination                 0
trajectory model              deterministic saturated drift
field mesh                    121 x 91
trajectory step               0.020 um
```

Three source families were tested.

### A. Point sources entirely upstream of depletion

```text
z = 2.0, 2.5, 3.0, 3.5, 4.0, 4.5 um
```

### B. Point sources inside depletion

```text
z = 4.8, 5.3, 5.8, 6.3, 6.8, 7.3 um
```

### C. Actual calibrated finite optical kernels

The original six HgCdTe wavelength channels, with the same upstream mean-depth sequence used in the spectral-depth stress.

---

## 3. Result: upstream point sources give zero false diffusion

For the point sources ending at `z=4.5 um`, all source-coordinate intervals lie upstream of the depletion boundary.

The six-channel first-difference sequence is numerically exact rank one:

```text
maximum rank-one fit residual = 7.83e-15
```

A 100 MHz homogeneous drift-diffusion inversion returns

```math
\boxed{
D_{\rm eff}=1.735\times10^{-12}\ {\rm m^2/s},
}
```

which is numerical zero on the scale of the other results.

The inferred drift scale is

```math
w_{\rm eff}=2.6556\times10^4\ {\rm m/s}.
```

The same fitted homogeneous law remains exact at 1 GHz to approximately

```text
1.55e-11 relative residual.
```

Thus the downstream depletion region does **not** by itself alter the source-spacing exponent for ideal point sources launched entirely in the upstream constant-velocity region.

This is a powerful internal control.

---

## 4. Positive control: point sources inside depletion give positive false diffusion

For point sources inside the field-gradient region, the same deterministic zero-diffusion device returns

```math
\boxed{
D_{\rm eff}=4.8711\times10^{-3}\ {\rm m^2/s}>0.
}
```

with

```math
w_{\rm eff}=2.7750\times10^4\ {\rm m/s}.
```

The rank-one approximation is no longer exact because the velocity varies appreciably over the source-coordinate range:

```text
max rank-one fit residual:
100 MHz    1.68e-3
500 MHz    8.34e-3
1 GHz      1.64e-2
```

Nevertheless, the homogeneous law identified at 100 MHz remains within

```text
0.233 % at 1 GHz.
```

This is the expected positive control for the deterministic field-gradient theorem.

---

## 5. Finite kernels centered upstream recover the hidden false diffusion

The actual calibrated finite optical kernels have the same nominal mean-depth range as case A, yet their kernel-aware one-mode inversion returns

```math
\boxed{
D_{\rm eff}=2.6098\times10^{-3}\ {\rm m^2/s}.
}
```

This is roughly half the inside-depletion point-source value and more than nine orders of magnitude above the upstream point-source numerical floor.

The calibrated-kernel one-mode fit remains extremely good:

```text
100 MHz    1.64e-5
500 MHz    8.33e-5
1 GHz      1.74e-4
```

and the wrong homogeneous law remains within

```text
0.889 % at 1 GHz.
```

Therefore the current hidden confound is not explained by the local source-center velocity gradient, because that gradient is zero at the nominal centers.

The false diffusion requires the **finite spatial support of the optical generation kernels to sample the downstream nonuniform field**.

---

## 6. Causal conclusion

The predeclared causal gate was:

```text
finite-kernel interaction supported if
|D_eff(upstream point)| << D_eff(finite kernels)
and inside-depletion point sources give positive D_eff.
```

The measured values are

```text
upstream point sources       1.735e-12 m^2/s
finite calibrated kernels    2.610e-3  m^2/s
inside-depletion points      4.871e-3  m^2/s
```

so the gate is passed by an enormous margin.

The active mechanism in the current HgCdTe stress is therefore:

```text
finite optical generation width
        x
downstream electrostatic velocity gradient
        x
Shockley-Ramo path integration
        ->
transport-like complex spectral-depth curvature
        ->
positive apparent homogeneous diffusion
```

The multiplication signs above denote a causal interaction, not literal algebraic multiplication.

---

## 7. Why the point-source control is exact upstream

The deterministic planar Ramo response obeys

```math
\frac{\partial H}{\partial z}
=-\frac1L+\frac{i\omega}{v(z)}H.
```

If `v(z)=v_0` over a source-coordinate interval, then its derivative response on that interval is

```math
P(z,\omega)
\propto e^{i\omega z/v_0}
```

up to a frequency-dependent coefficient determined by everything downstream.

The downstream field structure changes the common coefficient but not the local exponential ratio between point sources inside the same constant-velocity interval.

Hence equally spaced upstream point sources remain exactly rank one with a purely imaginary spatial exponent and therefore `D_eff=0`.

This explains the numerical control result without requiring the downstream device to be homogeneous.

The finite optical kernels evade this invariance because each measured spectral channel averages `P(z,omega)` over a distribution that extends across regions with different local source-coordinate laws.

---

## 8. Revised interpretation of the deterministic field-gradient theorem

`PAPER02_DETERMINISTIC_FIELD_GRADIENT_THEOREM_2026-08-15.md` remains correct for local point-source probing inside a region of nonzero `v'(z)`.

It is **not by itself the complete explanation of the current upstream-centered finite-kernel result**.

The current result requires an additional averaging step:

```math
J_m(\omega)=\int g_m(z)H(z,\omega)\,dz.
```

When `g_m` overlaps both the upstream constant-velocity region and the downstream gradient region, changes in kernel shape/weight with wavelength alter the relative mixture of the two source-coordinate response laws.

That mixture can remain very close to the calibrated one-mode manifold while generating a real quadratic frequency coefficient that the homogeneous inversion interprets as diffusion.

---

## 9. Stronger publication-level candidate claim

The broad claim

> nonuniform electric fields bias semiconductor transport measurements

is established prior art and is not a viable novelty claim.

The narrower candidate now emerging is:

> **Finite optical generation depth can couple a spatially remote electrostatic field gradient into a wavelength-resolved Shockley-Ramo transport measurement, producing a positive apparent homogeneous diffusion coefficient even when all nominal source centers lie outside the nonuniform-field region and microscopic diffusion is zero.**

A further distinctive element is that the confound can remain close to both

1. the same-frequency calibrated one-mode manifold, and
2. the low-frequency homogeneous drift-diffusion dispersion manifold.

This makes it an identifiability problem rather than merely a generic transit-time distortion.

**Priority remains unproven.**

---

## 10. Immediate next falsification

The next calculation should directly ablate the suspected cause.

For each calibrated optical kernel `g_m(z)` compute its depletion-overlap probability

```math
p_{d,m}=\int_{z_d}^{L}g_m(z)\,dz.
```

Then repeat the kernel-aware inversion for:

1. the full physical kernels;
2. kernels truncated to `z<z_d` and renormalized;
3. depletion-tail-only kernels where numerically meaningful;
4. continuously scaled tail weight.

The strongest causal prediction is

```text
remove depletion overlap -> D_eff collapses toward zero.
```

A controlled tail-weight sweep should then reveal how the false diffusion scales with overlap rather than merely correlating with it.

Only after that ablation succeeds should the program expand to depletion-width/voltage sweeps or manuscript drafting.
