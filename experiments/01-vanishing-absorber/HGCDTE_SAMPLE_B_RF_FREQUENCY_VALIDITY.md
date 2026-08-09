# Published Sample B — RF-Frequency Validity of the Mean-Delay Phase Approximation

**Date:** 2026-08-09  
**Status:** exact optical-generation timing transfer for deterministic `T=z/v`; isolates one source of finite-frequency phase bias; no calibrated transport claim; no novelty claim

## 1. Why this check matters

The inverse often uses

```math
\arg H_\lambda(\Omega)
\simeq
-\Omega\langle T_\lambda\rangle.
```

Increasing RF frequency improves phase leverage, but the approximation eventually fails because the generation-position distribution itself has finite timing width.

The published-sample calculation therefore asks:

> **Before adding carrier diffusion/scattering, how high in RF frequency can one go before the optical generation-depth distribution alone makes phase noticeably nonlinear?**

---

## 2. Exact optical timing transfer

Use the literature-constrained `150 V/cm` sample-B optical kernels.

Assume only for this diagnostic a deterministic local transit law

```math
\boxed{T=z/v.}
```

For conditional generation density `p_\lambda(z)`, the exact carrier timing transfer is

```math
\boxed{
H_\lambda(\Omega)
=\int p_\lambda(z)
\exp\!\left(-i\Omega z/v\right)dz.
}
```

The first-moment approximation is

```math
\boxed{
\phi_1(\lambda,\Omega)
=-\Omega\langle z\rangle_\lambda/v.
}
```

Compare

```math
\arg H_\lambda
```

against `phi_1` directly.

This isolates **optical generation-position broadening** only. Any additional stochastic transport broadening can make the usable low-frequency regime smaller.

---

## 3. Sample-B optical timing width

For the current central profile, the largest conditional generation-depth RMS width among the representative useful wavelengths is about

```math
\sigma_z\sim0.9\ {\rm um}.
```

At

```math
v=10^5\ {\rm m/s},
```

this is only about

```math
\sigma_T\sim9\ {\rm ps}.
```

Therefore at `1 GHz`,

```math
\Omega\sigma_T\sim0.06,
```

which already suggests that the first-moment phase approximation should be excellent for this particular speed scale.

---

## 4. Exact 1-GHz result

Across representative wavelengths from `2.80` to `3.88 um`:

### `v = 1e5 m/s`

```text
worst phase bias at 1 GHz < 0.002 degree
minimum |H| > 0.998.
```

### `v = 3e4 m/s`

```text
worst phase bias at 1 GHz ~0.04 degree
minimum |H| ~0.983.
```

### `v = 1e4 m/s`

```text
worst phase bias at 1 GHz ~1.2 degree
minimum |H| ~0.85.
```

Thus `1 GHz` is not intrinsically a safe or unsafe frequency. Its validity depends directly on the carrier transit scale.

---

## 5. Frequency envelope

Two simple diagnostics were scanned:

```text
worst first-moment phase bias < 0.10 degree
```

and

```text
optical timing transfer magnitude |H| > 0.98.
```

The `|H|>0.98` condition is slightly more restrictive for the current optical kernels.

Approximate upper frequencies are

| illustrative velocity | `f_max` from optical `|H|>0.98` |
|---:|---:|
| `1e5 m/s` | ~3.5 GHz |
| `5e4 m/s` | ~1.75 GHz |
| `3e4 m/s` | ~1.05 GHz |
| `1e4 m/s` | ~0.35 GHz |

The phase-bias `0.1 degree` criterion gives a somewhat higher envelope.

---

## 6. Dimensionless rule for the current optical kernels

The magnitude envelope scales linearly with velocity because the exact transfer depends on

```math
\Omega z/v.
```

For the current sample-B optical distributions,

```math
\boxed{
\frac{f_{\max}W}{v}
\approx0.13
}
```

for the illustrative requirement

```math
|H|>0.98.
```

Equivalently,

```math
\boxed{
f_{\max}\approx0.13\,v/W.}
```

This coefficient is **not universal**. It depends on the optical generation kernels and on the chosen error/magnitude criterion.

---

## 7. Experimental consequence

The RF plan should be adaptive.

A useful sequence is

```text
start at low RF frequency
-> estimate differential mean-delay scale
-> infer whether transport is fast or slow
-> raise RF frequency until phase leverage improves without large higher-moment distortion
-> use full complex-response fitting once the first-moment approximation is no longer adequate.
```

Do not prescribe `1 GHz` independently of the observed device dynamics.

---

## 8. Important asymmetry

Slower transport gives a larger differential phase for a given spatial feature:

```math
|\Delta\phi|\propto1/v.
```

But slower transport also makes the timing distribution resolve at a lower RF frequency.

Therefore the gain from simply increasing phase sensitivity by slowing transport or increasing frequency is self-limiting.

The correct observable at higher normalized frequency is the **full complex transfer**, not a forced mean-delay interpretation.

---

## 9. What is still missing

The present exact transfer includes only optical generation-position spread.

Real HgCdTe may add

- drift-diffusion first-passage variance;
- momentum and energy relaxation;
- trapping/recombination tails;
- RC / impedance poles;
- contact or packaging response.

If these factors are wavelength independent they may partly cancel in a differential measurement, but any wavelength-dependent contribution changes the complex-response model.

Thus the current frequency envelope is best treated as an **optical-only upper bound on the simplicity of the phase interpretation**, not a guaranteed device bandwidth.

---

## 10. Claim boundary

### CHECKED NUMERICALLY / CONDITIONAL

For the current sample-B Moazzami optical kernels and deterministic `T=z/v`:

- `1 GHz` first-moment phase bias is negligible near `v=1e5 m/s`;
- it remains small near `3e4 m/s`;
- it is no longer negligible near `1e4 m/s`;
- the current `|H|>0.98` optical-only envelope is approximately `f < 0.13 v/W`.

### NOT ESTABLISHED

- actual sample-B transport speed;
- actual device safe RF band;
- full stochastic carrier transfer;
- electrical/packaging transfer;
- novelty / priority.

---

## 11. Reproducibility

`numerics/hgcdte_sample_b_frequency_validity.py`

Next experimental-design work should optimize RF frequency jointly with wavelength and averaging time using a measured or validated full complex-response covariance/model.
