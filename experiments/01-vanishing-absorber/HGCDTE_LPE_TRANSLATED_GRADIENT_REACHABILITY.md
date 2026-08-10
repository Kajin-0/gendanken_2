# LPE Reachability of the Matched Translated-Gradient HgCdTe Experiment

**Date:** 2026-08-10  
**Status:** process-specific reachability audit against the 2024 slider-LPE growth model and demonstrated gradient scales; no claim that LPE is generally incapable of HgCdTe bandgap engineering; no novelty claim

## 1. Why this audit is necessary

The current strongest validation architecture is a matched pair of HgCdTe devices in which a compact internal composition-gradient segment is translated in depth while the front/back compositions and interface environments are held as nearly identical as possible.

The purpose-built programmed profile currently uses approximately

```text
absorber thickness = 7.6 um
x_front = 0.55
x_back = 0.32
feature total width ~1.0 um
feature edge ramps ~0.1 um
background composition slope ~0.0159 /um
local high-gradient slope ~0.137 /um
local gradient-field scale ~2 kV/cm.
```

The question here is narrow:

> **Can the 2024 experimentally validated slider-LPE mercury-loss/cooling mechanism plausibly generate this compact internal translated segment in one growth trajectory?**

This is different from asking whether LPE can control the *sign* of a broad composition gradient. It can.

---

## 2. Primary LPE source

The process model is from

Q. Huo et al., **“Improved liquid phase epitaxy method for in-situ growth of HgCdTe with positive composition gradient,”** *Journal of Infrared and Millimeter Waves* **43** (2024) 307-315, DOI `10.11972/j.issn.1001-9014.2024.03.003`.

The paper develops a crystallization-controlled slider-LPE model and experimentally validates positive-gradient material using thinning spectroscopy and SIMS.

It is the strongest current primary source for deciding what mercury-loss/cooling control actually demonstrated.

---

## 3. The LPE model is stateful

Huo et al. write the melt-state evolution schematically as

```math
\frac{dn_{Cd}}{dt}
=-vS\frac{\rho}{M}x,
```

```math
\frac{dn_{Hg}}{dt}
=-vS\frac{\rho}{M}(1-x)
-f_g m,
```

```math
\frac{dn_{Te}}{dt}
=-vS\frac{\rho}{M},
```

where `f_g` is the mercury-loss rate.

The instantaneous melt fractions `C_Cd`, `C_Hg`, and `C_Te` are calculated from these state variables.

The deposited composition is then an empirical function

```math
x=X(C_{Cd},C_{Hg}),
```

and the equilibrium crystallization temperature is

```math
T_g=G(C_{Cd},C_{Hg}).
```

Growth velocity is modeled as

```math
\boxed{v=k(T_g-T_t),}
```

with the ordinary constant-ramp schedule

```math
T_t=T_0-\alpha t.
```

Because

```math
\frac{dz}{dt}=v,
```

the local composition gradient is

```math
\boxed{
\frac{dx}{dz}
=\frac{1}{v}\frac{dX(C_{Cd},C_{Hg})}{dt}.
}
```

Therefore mercury loss and cooling can influence local `dx/dz`.

But this is **not a memoryless local control law**.

A mercury-loss pulse changes `n_Hg`, hence the melt composition, hence all subsequent values of `x`, `T_g`, and `v`.

Resetting `f_g` to its earlier value does not reset the melt state to the trajectory that would have existed without the pulse.

A truly localized feature that returns to the same downstream background therefore requires additional compensation in initial composition, temperature trajectory, mercury replenishment, or another growth stage.

The published experiment does not demonstrate such a time-programmed compensation protocol.

---

## 4. What the 2024 experiment actually demonstrated

At fixed cooling rate

```text
alpha = 0.2 C/min,
```

the paper gives average **linear-region** composition gradients

| Hg-loss rate `f_g` (%/min) | average gradient (cm^-1) |
|---:|---:|
| -0.01 | -12.4 |
| 0.00 | -9.0 |
| 0.01 | -4.9 |
| 0.02 | +0.2 |
| 0.03 | +6.9 |
| 0.04 | +16.7 |

At fixed

```text
f_g = 0.035 %/min,
```

the positive-gradient cooling-rate sweep gives approximately

| cooling rate (C/min) | average positive gradient (cm^-1) |
|---:|---:|
| 0.15 | 18.8 |
| 0.20 | 11.3 |
| 0.30 | 5.5 |
| 0.40 | 2.8 |

The experimentally grown positive-gradient sample used approximately

```text
f_g = 0.035 %/min
alpha = 0.2 C/min
T_start = 480 C
growth time = 50 min
thickness ~9 um
modeled average gradient ~11.3 cm^-1.
```

Thus the key demonstrated capability is:

> **continuous control of a broad linear composition gradient through the balance between segregation, Hg loss, and cooling.**

---

## 5. The compact relocation target is a different gradient regime

The current programmed validation profile has representative full-feature coordinates approximately

```text
x ~0.5166
-> over 1.0 um
x ~0.3917.
```

Therefore

```math
\Delta x\approx0.1249
```

across one micron.

That is an **average full-feature gradient** of approximately

```math
\boxed{1.25\times10^3\ {\rm cm^{-1}}.}
```

The local high-gradient plateau is approximately

```math
\boxed{1.37\times10^3\ {\rm cm^{-1}}.}
```

The background programmed slope is already approximately

```math
1.59\times10^2\ {\rm cm^{-1}}.
```

Compare with the strongest positive broad linear-gradient point reported in the 2024 control study:

```math
18.8\ {\rm cm^{-1}}.
```

The ratios are therefore approximately

```text
programmed background / reported maximum ~8.5x
programmed 1-um feature average / reported maximum ~66x
programmed local high-gradient plateau / reported maximum ~73x.
```

This is not a small extrapolation of the demonstrated process.

---

## 6. A useful thickness interpretation

At a constant composition gradient of

```math
18.8\ {\rm cm^{-1}},
```

the thickness needed to accumulate

```math
\Delta x=0.1249
```

would be

```math
L=\frac{0.1249}{18.8}\ {\rm cm}
\approx66.4\ \mu{\rm m}.
```

The current design asks for the same composition change in approximately

```math
1\ \mu{\rm m}.
```

That is the clearest scale mismatch.

---

## 7. Field-scale comparison

Using the canonical Hansen gap derivative near `x~0.45` at 300 K,

```math
\frac{dE_g}{dx}\approx1.39\ {\rm eV},
```

the band-edge gradient scale is approximately

```text
18.8 cm^-1 -> ~26 V/cm
159 cm^-1 -> ~221 V/cm
1370 cm^-1 -> ~1.90 kV/cm.
```

Thus the `~2 kV/cm` internal segment belongs to a qualitatively steeper spatial-composition regime than the 2024 mercury-loss-controlled linear gradients.

---

## 8. Why the natural LPE steep-gradient mechanism does not solve the relocation experiment

The 2024 paper explicitly separates ordinary LPE material into two spatial regions:

```text
1. a substrate-adjacent interdiffusion region
   thickness typically ~3-5 um
   steep Cd composition change

2. a growth-controlled linear composition region
   much more gradual composition change.
```

This explains how LPE can contain steep local composition gradients even though the demonstrated mercury-loss-controlled **linear** gradients are only of order tens of `cm^-1`.

But the steep mechanism is tied to the substrate/layer interface.

That is exactly the geometry the current inverse-design branch rejected because an interface-pinned transport feature is difficult to distinguish from boundary/contact/interface effects.

Therefore

> **using the natural LPE interdiffusion zone would restore the old mechanism-confounding problem rather than solve it.**

---

## 9. Deliberately naive mercury-loss extrapolation

For scale only, take the last measured/modelled secant of the Huo mercury-loss sweep:

```text
0.03 -> 0.04 %/min
6.9 -> 16.7 cm^-1.
```

This local secant is approximately

```math
980\ {\rm cm^{-1}} / (\%/{\rm min}).
```

If one **incorrectly extrapolates this slope** all the way to the current `1370 cm^-1` target, the implied mercury-loss rate is approximately

```math
\boxed{f_g\sim1.42\%/{\rm min}.}
```

That is about

```text
35x
```

the largest `0.04 %/min` point in the published sweep.

At the experimental average growth rate

```text
9 um / 50 min ~0.18 um/min,
```

a one-micron segment takes roughly `5.6 min`, so this extrapolated rate corresponds to an Hg-loss amount of order `8%` of the mother-liquor mass reference during that short interval.

This is **not a prediction**.

It is only a diagnostic showing that the compact target lies far outside the calibrated control regime.

---

## 10. Can time-dependent LPE controls still work in principle?

The model does not mathematically forbid time-varying

```text
f_g(t)
alpha(t)
```

or a more general `T(t)`.

So the correct statement is **not**

```text
LPE can never make an internal localized gradient.
```

The correct statement is:

> **The published single-run slider-LPE mechanism does not provide evidence that the current compact 1-um, ~2-kV/cm, translationally matched feature is reachable.**

A credible LPE implementation would need to demonstrate at least one of:

```text
large, rapid and reversible Hg chemical-potential control during growth
multi-stage melt/contact sequences
multiple epitaxy / regrowth
an intentionally buried interdiffusion interface
or a substantially broader/lower-gradient validation feature.
```

Each option needs a new process-specific model.

---

## 11. Multiple epitaxy is a real but scientifically different LPE route

LPE is capable of sophisticated buried HgCdTe structures.

W. Gawron and A. Rogalski, *Infrared Physics & Technology* **43** (2002) 157-163, DOI `10.1016/S1350-4495(02)00135-4`, report buried multi-junction HgCdTe structures and explicitly discuss advanced bandgap engineering using multiple epitaxy, selective growth, profiled substrates, and combinations of those methods.

Therefore LPE should remain in the fabrication tree.

But multiple epitaxy/regrowth creates a different validation problem:

```text
extra growth interfaces
potential trap/recombination changes
more difficult device-to-device matching
additional optical/electrical nuisance coordinates.
```

Those are precisely the kinds of interface effects the translated-gradient control was designed to suppress.

So a multi-stage LPE solution is possible only if its new interfaces can themselves be matched or independently characterized.

---

## 12. Fabrication-route decision after this audit

### MBE

```text
strongest route for the present compact translated feature
composition can be programmed directly versus growth time
no need to invoke a huge transient melt-composition excursion.
```

### MOCVD

```text
credible second route
must model/measure interdiffusion and realized x(z)
compact internal grading is naturally programmable.
```

### Single-run slider LPE

```text
excellent evidence for broad positive/negative gradient control
not currently supported for the compact ~1-um translated ~2-kV/cm feature
natural steep gradient remains substrate pinned.
```

### Multi-stage LPE / regrowth

```text
technologically possible
scientifically secondary because added interfaces reintroduce confounding.
```

---

## 13. Consequence for the active research program

Do **not** spend more numerical effort trying to force the current compact programmed profile into the 2024 single-run LPE control envelope.

The stronger path is now:

1. keep the interface-safe matched-relocation experiment as the physics design;
2. treat MBE as the default first fabrication model;
3. treat MOCVD as the diffusion-aware alternative;
4. retain LPE as a separate process-specific branch requiring a redesigned, broader feature or multi-stage growth architecture;
5. if an LPE-native design is pursued, optimize it under LPE-reachable gradient/thickness constraints rather than importing the MBE-like `1 um / 2 kV/cm` segment.

---

## 14. Numerical regression

`numerics/hgcdte_lpe_translated_gradient_reachability.py`

The numerical file reproduces the published gradient-control scale comparison, Hansen field conversion, the `~66 um` equivalent-thickness result, and the deliberately nonphysical high-end mercury-loss extrapolation used only as an out-of-domain diagnostic.
