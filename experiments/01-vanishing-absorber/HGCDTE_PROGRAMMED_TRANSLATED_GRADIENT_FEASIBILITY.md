# Programmed Translated-Gradient HgCdTe — Materials Feasibility

**Date:** 2026-08-10  
**Status:** conditional materials/design synthesis using published HgCdTe growth capabilities; no fabrication demonstration and no novelty claim

## 1. Current materials question

The purpose-built validation experiment no longer asks whether the published near-junction sample-A profile can be reconstructed perfectly.

It asks whether HgCdTe can be fabricated as a matched device family in which

```text
front/cap/contact conditions are held common
front and back absorber compositions are held common
and
one internal ~micron-scale high-gradient region is deliberately translated in depth.
```

The current inverse design prefers a genuinely buried feature rather than a boundary-adjacent one.

After front/back interface nuisance terms, fixed total wavelength time, and absorbed-signal-dependent phase precision are included, the conservative reference geometry is approximately

```text
feature centers ~4.1 and 5.6 um
feature total width ~0.9-1.0 um
edge transitions of order 0.1 um
spectral band ~2.00-2.40 um
peak local gradient field ~2 kV/cm.
```

See

- `HGCDTE_PROGRAMMED_INTERFACE_SAFE_JOINT_DESIGN.md`
- `HGCDTE_RELOCATION_EDGE_ENCODING.md`
- `HGCDTE_PROGRAMMED_WIDTH_INTERDIFFUSION.md`.

The earlier `2.6 / 3.2 um` result in this branch was produced by an artificially shallow feature-position grid and is **superseded as the preferred purpose-built geometry**.

---

## 2. MBE is the cleanest direct implementation route

HgCdTe molecular-beam epitaxy has long supported deliberately composition-tailored heterostructures with in-situ composition/thickness control.

Mikhailov et al., *Photonics* **10**, 430 (2023), DOI `10.3390/photonics10040430`, report HgCdTe multiple-quantum-well structures grown by MBE with in-situ ellipsometric composition/thickness determination at approximately

```text
Delta x ~0.0005
Delta d ~0.5 nm.
```

This is **not** a claim that an arbitrary translated HgCdTe gradient can be fabricated to `0.5 nm` accuracy.

It establishes that demonstrated epitaxial layer-control/metrology length scales are far smaller than the present design coordinates:

```text
feature width ~1 um
feature displacement ~1-2 um
edge transition ~0.1 um.
```

Varavin et al., *Journal of Crystal Growth* **159** (1996) 1161-1166, DOI `10.1016/0022-0248(95)00845-4`, also demonstrated composition-controlled HgCdTe heterostructures using in-situ ellipsometry.

For a first purpose-built matched relocation experiment, **MBE remains the most direct route conceptually** because the internal composition program can be specified explicitly versus growth time.

---

## 3. MOCVD is also a strong candidate

Madejczyk et al., *Infrared Physics & Technology* **81** (2017) 276-281, DOI `10.1016/j.infrared.2017.01.020`, report HgCdTe MOCVD heterostructures containing deliberately designed internal graded-gap sublayers and compare the intended structure with SIMS-measured composition profiles.

Their results are useful here because they make interdiffusion part of the real device rather than an afterthought.

A practical MOCVD workflow would be

```text
program the graded segment
-> grow
-> measure realized x(z) by SIMS / optical methods
-> insert realized x(z) into the wavelength x RF forward model.
```

The present numerical interdiffusion stress is favorable to this approach:

```text
Gaussian sigma_d ~0.05 um -> ~8% information-amplitude loss
sigma_d ~0.10 um -> ~20% loss
sigma_d ~0.15 um -> ~33% loss
```

when the peak gradient field is held near `1.95 kV/cm` and the feature is reoptimized while remaining away from both interfaces.

Thus modest smoothing does not destroy the experiment.

---

## 4. Correction — LPE is more programmable than the earlier branch assumed

The earlier version of this file treated LPE mainly as an indirect or awkward route for the translated-gradient control.

That boundary was too pessimistic.

Huo et al., “Improved liquid phase epitaxy method for in-situ growth of HgCdTe with positive composition gradient,” *Journal of Infrared and Millimeter Waves* **43** (2024) 307-315, DOI `10.11972/j.issn.1001-9014.2024.03.003`, established an HgCdTe LPE growth model and experimentally controlled the **sign and magnitude of the longitudinal composition gradient** through mercury-loss rate and cooling conditions.

They grew positive-gradient HgCdTe by slider LPE and verified the longitudinal composition profile using

```text
etch-thinning spectroscopy
and
secondary-ion mass spectrometry (SIMS).
```

The reported positive-gradient material retained good crystal quality, with XRD double-crystal rocking-curve FWHM around `28.8 arcsec`.

Therefore:

> **LPE is a real composition-gradient programming route and should not be dismissed from the purpose-built experiment.**

The remaining question is more specific.

The 2024 work demonstrates controllable broad longitudinal gradient engineering; it does **not yet establish** the exact control operation required here:

```text
same collection-side cap/contact
same absorber endpoints
same total composition change
compact ~1-um buried high-gradient segment
translated by ~1-2 um between matched devices.
```

That localized translation is still more direct to specify in MBE/MOCVD, but it is now a **process-design question for LPE**, not an obvious impossibility.

---

## 5. Current process ranking

The defensible ranking is therefore no longer

```text
MBE/MOCVD feasible; LPE only a fallback.
```

It is

### MBE

```text
most direct route for time-programmed internal profile placement
strong in-situ composition/thickness metrology precedent
cleanest first candidate for matched translated segments.
```

### MOCVD

```text
strong heterostructure/graded-layer precedent
realized profile must include precursor-switching and interdiffusion
SIMS-based x(z) reconstruction fits the current inverse philosophy well.
```

### LPE

```text
experimentally demonstrated control of composition-gradient sign/magnitude
through mercury-loss and cooling trajectory
excellent relevance to the published A/B lineage
but compact internal translation with fixed endpoints remains to be demonstrated.
```

No method has yet been shown, in the literature recovered here, to fabricate the **exact matched translated pair** proposed by this project.

---

## 6. Growth-programmable profile family

The Gaussian slope modulation used earlier was only a mathematical prototype.

The current design uses a compact programmed region in the composition-slope magnitude.

Nominal scale:

```text
total width ~0.9-1.0 um
edge transition ~0.1 um
background gradient field of order a few 10^2 V/cm
localized maximum ~2 kV/cm.
```

A mean-preserving slope construction keeps

```math
\int_0^L \frac{dx}{dz}dz
```

fixed, so both endpoint compositions remain fixed as the internal feature moves.

The exact trapezoidal shape is not sacred.

A process-specific reachable profile should replace it.

---

## 7. Edge sharpness is not a severe fabrication requirement

A dedicated spatial-convergence calculation at `80`, `160`, and `320` transport cells found that programmed edge transitions from approximately

```text
25 to 100 nm
```

lie on an essentially flat information plateau in the current model.

A `100 nm` result is converged at the sub-percent level from `160` to `320` cells.

Broadening to roughly `200 nm` costs about `30%` in fixed-time information amplitude.

Therefore there is no evidence that the experiment requires an atomically abrupt or ultrasharp internal interface.

A transition of order

```math
\boxed{0.1\ \mu{\rm m}}
```

is already near the resolved optimum.

---

## 8. Total width is likewise tolerant

At fixed peak gradient field near `1.95 kV/cm`, the unblurred width scan gives a broad optimum around

```text
~0.9-1.1 um
```

with approximately `1.0 um` best on the current numerical grid.

After moderate interdiffusion the optimum shifts only slightly toward `~0.9 um`.

This is favorable experimentally because the validation structure does not depend on one exact layer width.

---

## 9. The realized profile must be measured, not assumed

The strongest recurring lesson from the inverse work is that **fabrication tolerance and profile-knowledge tolerance are not the same thing**.

The device does not need to reproduce the nominal `x(z)` exactly if the realized profile can be characterized and propagated through the optical/RF model.

For the experiment, independent profile characterization is part of the measurement architecture:

```text
SIMS where appropriate
spectral/etch-thinning reconstruction
XRD / ellipsometric growth metrology
and process-specific calibration.
```

The forward kernel should be calculated from the measured profile.

What must be tightly matched physically is the part that cannot simply be corrected optically afterward, especially

```text
collection-side cap/contact/junction environment
broad doping/process state
and residual device-specific transport artifacts.
```

---

## 10. Current materials conclusion

The purpose-built experiment is **not blocked by an obviously unrealistic spatial scale**.

The current physics asks for

```text
micron-scale internal composition-gradient programming
~0.1-um transition scale
~1-2-um controlled relocation
and matched boundary conditions.
```

All three major HgCdTe epitaxial families now have relevant composition-engineering precedent:

```text
MBE   -> strongest direct placement precedent
MOCVD -> strong graded-heterostructure precedent with explicit interdiffusion
LPE   -> demonstrated programmable longitudinal gradient sign/magnitude.
```

What remains unproven is the **specific matched relocation structure**, not the general ability to engineer HgCdTe composition profiles.

---

## 11. Next materials calculation

The generic Gaussian interdiffusion model should now be replaced by a **process-specific reachable-profile model**.

Three branches are meaningful:

```text
MBE:
flux/shutter transient + Hg/Cd intermixing

MOCVD:
precursor switching + growth-temperature diffusion

LPE:
mercury-loss/cooling trajectory from the 2024 growth model.
```

For each branch, generate the reachable `x(z)` family and pass it directly through the interface-safe wavelength × RF design objective.

That will tell us whether the idealized translated feature survives the actual growth physics.

---

## 12. Primary materials references

1. N. N. Mikhailov et al., “Interband Electron Transitions Energy in Multiple HgCdTe Quantum Wells at Room Temperature,” *Photonics* **10**, 430 (2023), DOI `10.3390/photonics10040430`.
2. V. S. Varavin et al., “Molecular beam epitaxy of high quality Hg1-xCdxTe films with control of the composition distribution,” *Journal of Crystal Growth* **159**, 1161-1166 (1996), DOI `10.1016/0022-0248(95)00845-4`.
3. P. Madejczyk et al., “Engineering steps for optimizing high temperature LWIR HgCdTe photodiodes,” *Infrared Physics & Technology* **81**, 276-281 (2017), DOI `10.1016/j.infrared.2017.01.020`.
4. W. Gawron and A. Rogalski, “HgCdTe buried multi-junction photodiodes fabricated by the liquid phase epitaxy,” *Infrared Physics & Technology* **43**, 157-163 (2002), DOI `10.1016/S1350-4495(02)00135-4`.
5. Q. Huo et al., “Improved liquid phase epitaxy method for in-situ growth of HgCdTe with positive composition gradient,” *Journal of Infrared and Millimeter Waves* **43**, 307-315 (2024), DOI `10.11972/j.issn.1001-9014.2024.03.003`.

Numerical design files:

- `numerics/hgcdte_programmed_translated_gradient_design.py`
- `numerics/hgcdte_programmed_joint_depth_spectral_design.py`
- `numerics/hgcdte_relocation_edge_convergence.py`
- `numerics/hgcdte_programmed_width_interdiffusion.py`
