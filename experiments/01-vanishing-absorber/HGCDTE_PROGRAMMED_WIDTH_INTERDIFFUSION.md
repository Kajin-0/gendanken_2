# Programmed Gradient Width and Interdiffusion Robustness

**Date:** 2026-08-10  
**Status:** conditional purpose-built design stress; peak gradient held near `1.95 kV/cm`, both interfaces excluded, absorbed-signal-dependent phase noise, fixed wavelength-time resource; no fabrication claim and no novelty claim

## 1. Why total feature width is the next physical shape variable

The relocation calculation showed that sharpening the programmed feature edge below roughly `0.1 um` gives essentially no additional resolved information.

That leaves a more physical question:

> **How wide should the buried high-gradient region be, and how much interdiffusion can blur it before the relocation fingerprint becomes too smooth to distinguish from bulk/interface transport?**

A very narrow feature has strong localization but little integrated transport leverage.

A very broad feature has more material volume but begins to resemble an ordinary smooth composition gradient.

The optimum should therefore occur at a finite width.

---

## 2. Fair comparison at fixed gradient-field scale

For every tested total width and interdiffusion blur:

1. start with a programmed trapezoidal feature in the **composition-slope magnitude**;
2. use a nominal `0.10 um` edge ramp;
3. convolve the feature with a Gaussian blur of standard deviation `sigma_d`;
4. subtract the spatial mean so the front/back compositions and total composition change remain exactly fixed;
5. choose one common slope-modulation amplitude for the translated pair so a reference buried feature reaches approximately

```math
\boxed{F_{\max}\simeq1.95\ {\rm kV/cm}.}
```

This prevents a wider or sharper profile from winning merely because it was assigned a larger peak built-in field.

The imposed `25%` support-shaped transport perturbation remains an illustrative visibility probe and is not inferred from the field magnitude.

---

## 3. Interdiffusion is represented explicitly

Let the programmed slope feature before diffusion be `h_0(z)`.

Use

```math
h(z)=G_{\sigma_d}*h_0(z),
```

where `G_sigma` is a Gaussian kernel.

Then

```math
s(z)=s_0\left[1+a(h-\langle h\rangle)\right].
```

The mean subtraction preserves endpoint composition exactly after smoothing.

To keep the blurred feature genuinely internal, the geometric constraint is made more conservative:

```text
nominal feature edge + 3 sigma_d
must remain at least 1.5 um from each absorber interface.
```

Thus diffusion broadening cannot quietly push the optimized feature back into a boundary-confounded region.

---

## 4. Measurement model

The width scan uses the same mature purpose-built design metric:

```text
f = 0.25, 0.50, 1, 2, 3 GHz
phase + ln|H|
front + back interface nuisance exponentials
cubic common bulk transport nuisance
arbitrary complex offset at each RF frequency
absorbed-signal-dependent phase precision
fixed total wavelength-time resource.
```

The wavelength interval always begins at `2.00 um`; its upper edge is optimized jointly with feature depth.

Feature centers are searched at `0.1 um` spacing.

---

## 5. Unblurred optimum is broad, not razor thin

For `sigma_d=0`, scan total feature widths

```text
0.70, 0.80, 0.90, 1.00, 1.10 um.
```

Under the additive-like phase-noise envelope, the fixed-time information-amplitude scores are approximately

| total width | best score | representative centers | wavelength band |
|---:|---:|---:|---:|
| `0.70 um` | `0.00237` | `4.0 -> 5.7 um` | `2.00-2.55 um` |
| `0.80 um` | `0.00252` | `4.0 -> 5.6 um` | `2.00-2.50 um` |
| `0.90 um` | `0.00264` | `4.2 -> 5.6 um` | `2.00-2.45 um` |
| `1.00 um` | **`0.00267`** | `4.1 -> 5.5 um` | `2.00-2.40 um` |
| `1.10 um` | `0.00263` | `4.2 -> 5.5 um` | `2.00-2.35 um` |

The top is shallow.

A `0.9-1.1 um` feature is therefore effectively one broad design family rather than a sharply tuned optimum.

This is preferable experimentally: the design does not depend on holding one exact width.

---

## 6. Modest interdiffusion shifts the optimum only slightly

After Gaussian broadening, the strongest tested widths become approximately

```text
sigma_d = 0.00 um -> width ~1.00 um
sigma_d = 0.05 um -> width ~0.90 um
sigma_d = 0.10 um -> width ~0.90 um
sigma_d = 0.15 um -> width ~0.90 um.
```

The corresponding best fixed-time information amplitudes are approximately

| Gaussian interdiffusion `sigma_d` | best score | loss vs unblurred optimum |
|---:|---:|---:|
| `0.00 um` | `0.00267` | `0%` |
| `0.05 um` | `0.00247` | **`~8%`** |
| `0.10 um` | `0.00213` | **`~20%`** |
| `0.15 um` | `0.00179` | **`~33%`** |

Thus interdiffusion degrades the experiment gradually rather than causing an abrupt identifiability failure.

---

## 7. The geometry adapts as the feature broadens

The optimizer responds to diffusion by moving the pair modestly inward and favoring a slightly shorter band.

Representative additive-like results for the strongest width at each blur are

```text
sigma_d=0.00:
width ~1.0 um
z ~4.1 -> 5.5 um
lambda ~2.00-2.40 um
min Pabs ~0.992

sigma_d=0.05:
width ~0.9 um
z ~4.1 -> 5.5 um
lambda ~2.00-2.45 um
min Pabs ~0.991

sigma_d=0.10:
width ~0.9 um
z ~3.8 -> 5.3 um
lambda ~2.00-2.40 um
min Pabs ~0.995

sigma_d=0.15:
width ~0.9 um
z ~3.7 -> 5.1 um
lambda ~2.00-2.40 um
min Pabs ~0.996.
```

The trend is physically sensible: broader effective features require more room from both interfaces and reduce the advantage of probing the deepest edge.

---

## 8. Noise-model robustness

Repeat the winning geometries using the statistics-like envelope

```math
\sigma_\phi\propto P_{\rm abs}^{-1/2}
```

instead of the additive-like

```math
\sigma_\phi\propto P_{\rm abs}^{-1}.
```

The same width/depth/band solutions are selected to the numerical resolution of the current search.

That robustness is expected because the optimized spectral bands remain highly absorbing (`Pabs` typically above `0.99`).

The exact phase-noise law is therefore not driving the width result.

---

## 9. Spatial convergence

The selected designs were independently reevaluated with `320` transport cells across the `7.6 um` absorber.

Representative additive-like scores are

```text
sigma_d=0.00, width=1.0 um -> 0.002676
sigma_d=0.05, width=0.9 um -> 0.002467
sigma_d=0.10, width=0.9 um -> 0.002131
sigma_d=0.15, width=0.9 um -> 0.001790.
```

These reproduce the `160`-cell optimization results at the relevant precision.

Therefore the width/interdiffusion trend is not the sub-cell edge artifact found in the earlier ramp-only sweep.

---

## 10. Physical design rule

The current numerical evidence supports a simple materials target:

```math
\boxed{
\text{program a buried high-gradient region of order }1\ \mu{\rm m}\text{ wide}
}
```

with

```text
edge transitions ~0.1 um or moderately smoother
peak gradient field ~2 kV/cm
and the entire broadened region kept well away from both interfaces.
```

Do not over-optimize the exact width.

The experimentally meaningful requirement is closer to

```text
~0.9-1.1 um before strong diffusion
```

than to one unique numerical layer thickness.

---

## 11. Implication for epitaxial feasibility

This result is favorable for a real growth program because the useful feature is **micron scale**, not a narrow quantum-well-like layer.

Moderate interface smoothing can be measured and incorporated into the forward model, and even `sigma_d~0.1 um` retains roughly `80%` of the current information amplitude.

A process that broadens the internal feature by several tenths of a micron would become a significant design penalty, but does not imply a mathematical singularity.

---

## 12. Next materials step

The correct next calculation is no longer another geometric sweep.

It is to replace the generic Gaussian blur with a **process-specific composition-transfer model** for the chosen growth route:

```text
MBE shutter/flux transient + Hg/Cd intermixing,
or
MOCVD precursor-switching + diffusion,
or
LPE cooling/Hg-loss trajectory.
```

That model should generate the actual reachable `x(z)` family, which can then be passed directly through the wavelength × RF design calculation.

Numerical implementation:

`numerics/hgcdte_programmed_width_interdiffusion.py`
