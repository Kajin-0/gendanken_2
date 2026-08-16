# Mean-preserving depletion-tail ablation

**Date:** 2026-08-15  
**Status:** **CHECKED in conditional model / CAUSAL CONTROL PASSED / PRIORITY UNPROVEN**

## 1. Question

The direct finite-kernel tail ablation established that removing optical-generation support inside the collector-side depletion region collapses the positive apparent diffusion coefficient.

A possible objection remained:

> truncating and renormalizing each optical kernel also shifts its mean generation depth, so perhaps the collapse is caused by changing the nominal source-coordinate sequence rather than by removing overlap with the electrostatic region.

This control eliminates that objection.

---

## 2. Mean-preserving construction

For each physical generation kernel `g_m(z)`, all support at and beyond the depletion boundary

```math
z_d=4.6\ \mu\mathrm m
```

was removed.

The surviving upstream density was then exponentially tilted:

```math
g_m^{\rm mp}(z)
\propto
g_m(z)\exp[\lambda_m(z-z_{m,0})],
\qquad z<z_d,
```

with

```math
g_m^{\rm mp}(z)=0,
\qquad z\ge z_d,
```

and `lambda_m` chosen independently so that

```math
\int z g_m^{\rm mp}(z)dz
=
\int z g_m(z)dz
```

for every channel.

The exact modified kernels were used consistently in both

1. the forward Shockley-Ramo current average, and
2. the calibrated finite-kernel one-mode inverse.

No delta-source or rigid-kernel approximation was introduced.

---

## 3. Reproducibility

Script:

```text
experiments/01-vanishing-absorber/numerics/paper02_mean_preserving_tail_ablation.py
```

GitHub Actions run:

```text
run id       31917802506
artifact     paper02-mean-preserving-tail-ablation
artifact id  9255439098
sha256       3b068ca870e527bb834064b2f25665a99bd71546d53a5e7e6c725d228551be87
```

The same fine numerical settings were retained:

```text
field mesh              121 x 91
source quadrature       13 x 41
trajectory step         0.020 um
bias                    0.30 V
depletion width         3.0 um
space-charge drop       0.05 V
microscopic diffusion   0
recombination           0
```

---

## 4. Means were preserved to numerical precision

Original channel means:

```text
2.0, 2.5, 3.0, 3.5, 4.0, 4.5 um
```

Maximum absolute mean error after removing all depletion-region support and tilting the upstream density:

```math
\boxed{9.33\times10^{-15}\ \mu\mathrm m.}
```

All modified depletion-overlap probabilities are exactly zero in the numerical quadrature.

The required exponential tilt is mild for the shallow channels and strongest for the 4.5 um channel because its original mean lies only 0.1 um upstream of the depletion boundary:

```text
channel mean   lambda [1/um]
2.0 um         0.0326
2.5 um         0.0832
3.0 um         0.2070
3.5 um         0.5239
4.0 um         1.4961
4.5 um        10.4550
```

The shape change is deliberately not claimed to be a realizable optical material. It is a mathematical causal control: exact mean coordinate retained, nuisance-region support removed.

---

## 5. Result

### Physical full kernels

```math
D_{\rm eff}=2.609795\times10^{-3}\ {\rm m^2/s},
```

```math
w_{\rm eff}=2.57010\times10^4\ {\rm m/s}.
```

Kernel-aware one-mode residual:

```text
max over 0--1 GHz = 1.738e-4
```

Wrong homogeneous-law residual at 1 GHz:

```text
8.885e-3.
```

### Tails removed and merely renormalized

```math
D_{\rm eff}=-9.6543\times10^{-7}\ {\rm m^2/s}.
```

### Tails removed with every original mean restored

```math
\boxed{
D_{\rm eff}=-7.6810\times10^{-8}\ {\rm m^2/s}.
}
```

The magnitude collapse relative to the physical kernels is

```math
\boxed{
\frac{|D_{\rm eff}^{\rm mp}|}{|D_{\rm eff}^{\rm full}|}
=2.943\times10^{-5},
}
```

or approximately a

```text
33,977 x
```

reduction.

The 1 GHz homogeneous-law residual becomes

```text
4.65e-8,
```

and the maximum calibrated one-mode residual is only

```text
1.89e-7.
```

---

## 6. Causal conclusion

The false diffusion does not require a shift of the channel mean-depth coordinate.

With the original six means held fixed to numerical precision,

```text
finite support in depletion present
    -> D_eff = +2.61e-3 m^2/s

finite support in depletion removed
    -> D_eff ~= 0
```

while the microscopic simulation truth remains `D=0` in both cases.

Therefore the active variable is the **restricted support/shape of the optical generation kernels inside the remote electrostatic region**, not their nominal mean depths.

This strengthens the remote-region leakage theorem from a support argument to a controlled numerical causality result.

---

## 7. Continuous tail-weight result

A separate ablation continuously scaled the physical kernel density inside depletion by factors

```text
0, 0.1, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 2
```

with exact renormalization and exact modified-kernel inversion.

The corresponding apparent diffusion coefficients were

```text
tail scale   D_eff [m^2/s]
0.00        -0.000000965
0.10         0.0008871
0.25         0.0015966
0.50         0.0021581
0.75         0.0024392
1.00         0.0026098
1.25         0.0027264
1.50         0.0028129
2.00         0.0029365
```

The response is monotone over the tested positive-tail range and saturates as overlap becomes large.

For the physical kernels (`tail scale = 1`), depletion overlap increases strongly with channel depth:

```text
nominal mean   depletion overlap
2.0 um          0.60 %
2.5 um          1.65 %
3.0 um          4.20 %
3.5 um          9.78 %
4.0 um         20.60 %
4.5 um         38.89 %
```

Even the shallow channels therefore have nonzero remote overlap, and the overlap changes by almost two orders of magnitude across the six-channel sequence.

---

## 8. Scientific implication

A mean-depth description is insufficient for attribution.

Two sets of calibrated source kernels can have exactly the same sequence of mean generation depths but produce radically different inferred material-transport parameters because their support relative to a nonuniform electrostatic region differs.

For a spectral-depth inverse, the relevant optical nuisance coordinates include restricted quantities such as

```math
p_{m,R}=\int_R g_m(z)dz
```

and, when needed, higher moments of `g_m` restricted to the nuisance region.

This is a sharper statement than the ordinary observation that wavelength changes absorption depth.

---

## 9. Next gate

The current mechanism is now causally isolated within the quadratic space-charge surrogate. The next scientific requirement is **generality across an independent electrostatic profile family**.

A clean test should retain

- the same physical optical kernels;
- the same planar Shockley-Ramo observation operator;
- zero microscopic diffusion;

but replace the Poisson-generated depletion profile with independent prescribed deterministic velocity profiles, for example linear and exponential downstream acceleration.

If positive `D_eff` and low-RF homogeneous-law mimicry survive across those families, the effect is no longer attributable to the specific finite-difference electrostatic surrogate.
