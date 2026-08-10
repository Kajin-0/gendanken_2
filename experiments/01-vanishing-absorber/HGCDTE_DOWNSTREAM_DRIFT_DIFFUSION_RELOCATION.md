# Downstream Drift–Diffusion Relocation — Correcting the Transport Orientation and Removing the Ad Hoc Timing Perturbation

**Date:** 2026-08-10  
**Status:** physics-derived first-passage transport sensitivity model anchored to published graded-HgCdTe drift–diffusion equations; material parameters remain sensitivity coordinates rather than a calibrated device prediction; no novelty claim

## 1. Why the transport model had to change

The matched translated-gradient branch was originally optimized with an illustrative local timing perturbation of the form

```math
v(z)=v_0[1-0.25h(z)].
```

That was useful for asking a geometry question:

> where does wavelength × RF data have spatial leverage on a buried feature?

It was **not** a physical prediction of what a composition-gradient field actually does to minority electrons.

A primary-source cross-check exposed a more important issue: the direction of the composition gradient relative to the collecting junction matters.

---

## 2. Two published HgCdTe geometries have different transport roles

### Sang et al. 2022 — high-speed graded detector

Sang et al., *Journal of Infrared and Millimeter Waves* **41** (2022), DOI `10.11972/j.issn.1001-9014.2022.06.005`, model and measure a graded HgCdTe detector in which the composition-gradient built-in field assists minority-carrier transport to the junction.

Their 1D p-region continuity model is

```math
D_n\frac{\partial^2\Delta n}{\partial z^2}
+\mu_n\varepsilon_{\rm built-in}
\frac{\partial\Delta n}{\partial z}
-\frac{\Delta n}{\tau_n}
+G_L(z,\lambda)=0.
```

They use

```math
D_n/\mu_n=k_BT/q
```

and an effective composition-gradient field based on the bandgap change across the graded absorber.

Experimentally, the strongly graded VPE device showed a much faster room-temperature zero-bias response than the weakly graded LPE device, including approximately

```text
VPE: ~1.33 ns / ~750 MHz
LPE: ~8.7 ns / ~115 MHz.
```

The forward fact that graded HgCdTe can accelerate transport and change RF response is therefore prior art.

### Xu et al. 2023 — retained nonlinear region near the high-Cd junction

Xu et al., *Journal of Infrared and Millimeter Waves* **42** (2023), DOI `10.11972/j.issn.1001-9014.2023.03.001`, deliberately place the junction at the high-Cd side in the sample-A/B experiment used earlier in this repository.

Their discussion states that the strong nonlinear-gradient field in sample A can repel p-region photoelectrons away from the junction as the field increases.

That geometry is useful for studying saturation/space-charge behavior.

It is **not** the clean orientation for a high-speed built-in-field transport-localization experiment.

---

## 3. Correct purpose-built orientation

For the relocation validation experiment use

```text
z=0:
high-Cd optical entrance

monotonic graded absorber:
x decreases with z

z=L:
low-Cd collecting junction.
```

Then the phenomenological composition-gradient drive is aligned with minority-electron collection.

This orientation also preserves the desired spectral encoding:

- at short wavelength the high-Cd entrance can remain transparent until the local bandgap becomes low enough for absorption;
- changing wavelength moves that first strongly absorbing region deeper or shallower;
- the same physical carrier-driving field points toward the collecting junction.

The low-frequency inverse in this geometry uses the **downstream CDF kernel**, not the front-collection survival kernel.

---

## 4. Practical optical consequence

If a conventional n-on-p epitaxial sequence places the low-Cd junction on the top surface, the high-Cd side may have to be illuminated through the substrate/backside.

That introduces

```text
substrate transmission
front/back reflection
passivation/AR layers
possible etalon structure
and alignment/path calibration.
```

Those are real experimental complications.

However, they alter the optical generation kernel, which can in principle be measured and modeled.

Using the wrong junction/gradient orientation changes the carrier-force direction itself and is a more fundamental error.

Thus the corrected transport direction takes precedence over the earlier preference for simple front-side optics.

---

## 5. Backward first-passage equation

For an electron beginning at position `z`, let

```math
u(z,s)
```

be the Laplace transform of successful first passage to the collecting boundary.

For local drift velocity `v(z)`, diffusion coefficient `D`, and bulk recombination lifetime `tau_rec`, the backward equation is

```math
\boxed{
D u''(z)
+v(z)u'(z)
-\left(\frac{1}{\tau_{\rm rec}}+s\right)u(z)=0.
}
```

The collecting boundary is absorbing:

```math
\boxed{u(L,s)=1.}
```

The optical entrance is first treated as reflecting:

```math
u'(0,s)=0.
```

A surface-loss stress replaces this by

```math
\boxed{D u'(0,s)=S u(0,s),}
```

where `S` is an effective entrance-surface recombination velocity.

This is a one-dimensional reduced model, not a full junction/device simulation.

---

## 6. Einstein diffusion and effective gradient field

Use

```math
\boxed{D=\mu k_BT/q.}
```

For the composition profile `x(z)`, define the local bandgap-gradient scale

```math
\left|\frac{dE_g}{dz}\right|
=
\left|\frac{dE_g}{dx}\frac{dx}{dz}\right|.
```

Following the phenomenological Sang-style transport convention, write

```math
\boxed{
E_{\rm eff}(z)
=\chi_E
\left|\frac{dE_g}{dz}\right|/q.
}
```

The dimensionless factor

```math
\chi_E
```

is explicit and important.

`chi_E=1` corresponds to assigning the full bandgap-gradient scale to the effective carrier-driving field, similar to the published simplified model.

The repository does **not** assert that this is a microscopic conduction-band-offset identity.

Until the band-edge partition and electrostatics are modeled independently, `chi_E` is a sensitivity coordinate.

The low-field drift law is

```math
v(z)=\mu E_{\rm eff}(z).
```

A deliberately smooth high-field sensitivity stress uses

```math
\boxed{
v(z)
=\frac{\mu E_{\rm eff}}
{1+\mu E_{\rm eff}/v_{\rm sat}}.
}
```

This saturation law is not claimed as a calibrated HgCdTe velocity-field relation.

---

## 7. Complex RF transfer including recombination

Let the conditional optical generation density be

```math
p(z|\lambda,{\rm abs}).
```

At RF angular frequency `Omega`, solve the backward equation with

```math
s=i\Omega.
```

The collected complex response is proportional to

```math
\int p(z|\lambda)u(z,i\Omega)dz.
```

Normalize by the DC collection probability:

```math
\boxed{
H(\lambda,\Omega)
=
\frac{
\int p(z|\lambda)u(z,i\Omega)dz
}{
\int p(z|\lambda)u(z,0)dz
}.
}
```

This conditions the RF transfer on collected carriers and prevents a simple change in collection efficiency from being mislabeled as timing phase.

Magnitude and phase are both retained.

---

## 8. Remove the purely optical difference between translated structures

Even when two structures have identical endpoints, translating an internal composition-gradient segment slightly changes `x(z)` and therefore changes the optical generation kernel.

That is not automatically a transport-field signal.

For each device define

```math
\boxed{
\Delta_{\rm field}
=\ln H_{\rm field}
-\ln H_{\rm field\ off}.
}
```

The field-off calculation uses the **same** `x(z)` optical profile, recombination model, diffusion coefficient, and boundaries but sets the graded-field drive to zero.

For features at depths `z1,z2`, define

```math
\boxed{
R(\lambda,\Omega)
=\Delta_{\rm field}(z_2)
-\Delta_{\rm field}(z_1).
}
```

Then remove one arbitrary wavelength-independent complex term at each RF.

`R` is the **field-induced relocation fingerprint**.

This is the appropriate object for asking whether moving the internal gradient field moves the measured transport response.

---

## 9. Internal spectral encoding survives in the corrected orientation

For the old `4.1 / 5.6 um` translated pair, illumination from the high-Cd side gives approximately the following conditional mean generation depths in the current Hansen/Moazzami model.

### Feature at `4.1 um`

```text
2.0 um -> ~2.23 um
2.1 um -> ~3.43 um
2.2 um -> ~4.23 um
2.3 um -> ~4.46 um
2.4 um -> ~4.59 um.
```

### Feature at `5.6 um`

```text
2.0 um -> ~2.24 um
2.1 um -> ~3.54 um
2.2 um -> ~4.67 um
2.3 um -> ~5.51 um
2.4 um -> ~5.88 um.
```

Modeled absorption remains very high:

```text
Pabs >~0.9908
```

through this short spectral band for the pair.

Thus the high-Cd entrance simultaneously gives

```text
strong absorption
+
a multi-micron wavelength-driven generation-position sweep
+
field orientation toward the collecting junction.
```

---

## 10. Central transport stress gives a degree-scale relocation signal

Use the explicit sensitivity point

```text
T = 300 K
mu_n = 9000 cm2/Vs
chi_E = 0.50
tau_rec = 1 ns
no velocity cap
entrance S = 0
lambda = 2.00-2.40 um
f = 1 GHz.
```

These numbers are **not a fitted parameter set for the proposed structure**.

They are a central numerical stress point.

The mean-preserving programmed profile then gives effective gradient-field scales of approximately

```text
background ~107 V/cm
buried high-gradient region ~950-970 V/cm.
```

For the `4.1 / 5.6 um` pair, the field-induced relocation fingerprint has

```math
\boxed{
\Delta\phi_{\rm p-p}(1\ {\rm GHz})
\approx1.81^\circ.
}
```

The phase RMS across the wavelength scan is approximately

```math
\boxed{0.63^\circ.}
```

This is about an order of magnitude larger than the earlier ad hoc local-delay example for comparable geometry.

Therefore the physically motivated graded-field signal is **not obviously too small**.

---

## 11. Spatial convergence

The central `1 GHz` peak-to-peak result is

```text
201 grid points  -> ~1.843 deg
401              -> ~1.807 deg
801              -> ~1.811 deg
1601             -> ~1.813 deg.
```

The degree-scale result is therefore not a coarse-grid artifact.

---

## 12. Broad mobility / field-fraction / lifetime stress

Sweep

```text
mu_n = 3000, 9000, 20000, 40000 cm2/Vs
chi_E = 0.10, 0.25, 0.50, 1.00
tau_rec = infinity, 3, 1, 0.5, 0.2 ns
```

at `1 GHz`, with no imposed velocity saturation.

Across the full stress set, the old `4.1 / 5.6 um` field-induced relocation phase span is approximately

```math
\boxed{
0.196^\circ
\;\text{to}\;
11.66^\circ,
}
```

with median about

```math
\boxed{2.20^\circ.}
```

Some slow/high-recombination stress points have poor `1 GHz` transfer magnitude.

That does not imply they are experimentally useless; it means RF frequency must be adapted to the actual transport regime rather than fixed at `1 GHz` by convention.

---

## 13. Smooth velocity-saturation stress

At the central

```text
mu=9000 cm2/Vs
chi_E=0.5
tau=1 ns
```

point, imposing the illustrative smooth velocity cap still leaves approximately

```text
no cap       -> ~1.81 deg p-p
v_sat 5e5 m/s -> ~1.60 deg
2e5           -> ~1.36 deg
1e5           -> ~1.09 deg
5e4           -> ~0.92 deg.
```

Thus the degree-scale central result is not produced solely by allowing arbitrarily large `mu E` drift velocity.

A real high-field velocity law is still required before predicting a fabricated device.

---

## 14. Entrance-surface recombination stress

At the same central transport point:

```text
S = 0 cm/s    -> ~1.81 deg
1e4           -> ~1.80 deg
1e5           -> ~1.73 deg
1e6           -> ~1.44 deg.
```

Therefore the corrected high-Cd optical entrance does not require a perfectly reflecting carrier boundary for the central field-induced relocation signature to survive.

The entrance surface must still be characterized in a real device.

---

## 15. Major consequence — the old geometry optimum is superseded

The earlier `4.1 / 5.6 um` feature-center pair was optimized using a deterministic-transit Jacobian and an imposed 25% localized delay perturbation.

With the downstream drift–diffusion model, a coarse raw scan of interface-safe feature centers from `2.0` to `5.6 um` instead pushes the central model toward a broader relocation, approximately

```math
\boxed{2.0 / 5.6\ \mu{\rm m}}
```

before nuisance projection.

Its `1 GHz` field-induced phase span is roughly

```text
~2.9 deg
```

in the current central stress.

This is **not yet the final optimum** because

```text
interface nuisances
real RF covariance
backside optical stack
parameter uncertainty
and absorption-dependent phase precision
```

have not yet been included in that new optimization.

The important conclusion is simply:

> **all old feature-depth, wavelength, RF, randomization, and replicate-depth optima must be rerun with the physics-derived transport operator.**

The earlier results remain valuable design/provenance studies but are not current numerical prescriptions.

---

## 16. What this model still omits

The present first-passage model is much stronger than the ad hoc timing perturbation, but it is still reduced.

Missing or simplified physics include

```text
composition-dependent mobility
measured high-field velocity-field relation
conduction/valence-band offset partition
electrostatic Poisson solution and doping profile
depletion-region transit
junction capacitance / electrical transfer
trap-assisted dynamics
carrier-density dependence / space charge
nonuniform lifetime
full 2D/3D geometry
and substrate/passivation optical transfer.
```

These are now the right refinement directions.

More abstract inverse algebra is lower priority.

---

## 17. Prior-art boundary after the correction

Do not claim novelty for

```text
graded HgCdTe accelerating carriers
graded HgCdTe having faster RF response
bandgap-gradient drift-diffusion modeling
wavelength-dependent generation depth
or photodetector RF timing measurements.
```

Those are already established in the cited literature.

The potentially distinct experimental idea remains narrower:

> **use wavelength as an internal spatial encoder and deliberately relocate a buried graded-field feature, then test whether the measured complex RF transport fingerprint follows the predicted spatial relocation law.**

Priority remains unproven, especially while the 2024 `Potential application of HgCdTe detector with composition gradient in laser measurement` paper remains technically unresolved.

---

## 18. Next decisive calculation

Replace the old deterministic-Jacobian design optimization with the downstream first-passage operator.

The next design must jointly optimize

```text
feature depths
wavelengths / optical resource
RF frequencies
and experimental ordering
```

while marginalizing **physical nuisance parameters**, not arbitrary local-delay basis functions.

At minimum include sensitivity to

```text
mobility
recombination lifetime
gradient-field fraction
entrance/back-interface loss
measured x(z) error
electrical complex offsets
and real wavelength/RF covariance.
```

Only after that rerun should the multi-depth MBE growth sequence be frozen.

---

## 19. Numerical implementation

`numerics/hgcdte_downstream_drift_diffusion_relocation.py`
