# Research Log — Experiment 01: The Vanishing Absorber

Chronological recovery log. Dedicated derivation files preserve the full algebra; this file records **why the direction changed**.

---

## 2026-08-08 — Experiment opened

Starting question:

> Can an ideal photodetector be made arbitrarily small, arbitrarily fast, arbitrarily sensitive, and still absorb essentially every incident photon?

Initial intuition:

```text
smaller active volume
-> fewer bulk dark events

passive optical confinement
-> recover absorption

possible cost
-> increased optical dwell time / reduced response bandwidth.
```

The project explicitly refused to assume that a volume-based theorem existed.

---

## One-port resonator

The first exact model showed that a weak absorber can retain unity resonant absorption at critical coupling while its useful temporal response narrows as absorber loss decreases.

A factor-of-two distinction was established between spectral absorption FWHM and small-signal absorbed-power response bandwidth.

A toy bulk-dark-event sensitivity-speed metric was optimized at modest overcoupling rather than exact critical coupling.

Direction: ask whether absorber loss rate must scale with active volume.

---

## Active-volume theorem falsified

A shrinking-gap passive dielectric family retained finite energy participation and finite absorptive decay while active volume tended to zero.

Therefore geometric active volume alone is not a universal optical resource.

Direction: replace geometric volume with microscopic transition resources.

---

## Microscopic transition / LDOS / finite-emitter branch

Finite absorber number did not impose a one-photon speed ceiling because the one-excitation sector remained linear.

Bandwidth-averaged LDOS bounds gave useful conditional constraints, but point-dipole divergences required finite emitter extent and weak-coupling formulas eventually failed as the formal rate approached the optical frequency.

Direction: move to nonperturbative light-matter coupling.

---

## Hopfield / deep-strong branch

A gauge-consistent two-mode model reproduced established deep-strong light-matter decoupling.

Holding a dressed mode at a fixed detector frequency while taking internal coupling large gave the supporting result

```math
\min(\Gamma_L,\Gamma_R)\to0
```

for fixed local reservoir resources.

Reservoir strengthening can evade the collapse but then becomes an explicit new resource.

Direction: test arbitrary multimode passive networks.

---

## Finite passive multimode theorem

The optical-to-detector transfer area was written as an `H2` norm.

A preliminary bound

```math
\mathcal I\le2\min(L,R)
```

was superseded by the sharper exact harmonic form

```math
\boxed{
\mathcal I
\le
\frac{2LR}{L+R}.
}
```

A single resonance saturates it.

This made **external access** a more robust resource than internal mode count.

Direct feedthrough and structured-continuum audits then showed the precise scope of the finite-network theorem.

---

## Optical access + autonomous detector thermodynamics

Prior-art collisions narrowed the problem sharply.

Young, Sarovar & Leonard (2018) already treat incoming few-photon fields, absorption, amplification, efficiency, dark counts, and timing.

Schwarzhans et al. (2026) already treat autonomous detector work/reset, entropy production, internal dark counts, jitter, and dead time.

The repository therefore did not claim generic capture+amplification or generic detector thermodynamics as new.

A three-level testbed was used only to understand how optical capture, readiness, click events, and thermodynamic cycle current differ.

Publication audit verdict:

> continue research; do not write a manuscript yet.

---

## Active frequency conversion / time-dependent capture

Pumped frequency converters showed that active control can buy bandwidth, but architecture-specific `W^2` pump scaling was not universal.

A singular-value formulation showed that pump photons purchase finite conversion-channel strength, with the device coupling operator remaining another resource.

Time-dependent impedance matching can capture one known temporal mode efficiently, but unknown arrival time reintroduced storage/output mode capacity.

Adaptive feedforward then showed that the missing rank can be exported into the measurement/output record.

An unrestricted output continuum therefore defeats a universal finite detector-only space-time capacity theorem.

Direction: stop adding abstract resource coordinates and return to a real semiconductor detector.

---

## Semiconductor contact / energy-filter branch

A Fermi contact established the expected detailed-balance relation between extraction and reverse thermal loading.

A single resonant energy filter added lifetime-broadening leakage even at zero temperature, but a multipole filter showed that spectral FWHM is not a universal transport-speed variable: sharper tails can be bought with more internal delay/state weight.

Direction: use actual narrow-gap semiconductor field-driven collection.

---

## HgCdTe direct-BTBT normalization

A standard HgCdTe direct-tunneling expression combined with the simplified Kane relation gave

```math
j=x^2e^{-1/x},
```

with field scale

```math
F_K\propto\lambda_c^{-2}
```

and current scale

```math
J_K\propto L\lambda_c^{-4}.
```

This clean normalization separated tunneling from high-field transport.

Primary HgCdTe work made clear that low-field mobility cannot be extrapolated into the relevant high-field regime; velocity can become non-ohmic, saturate, or decrease.

Direction: treat TAT and nonlocal impact ionization explicitly rather than assuming direct BTBT is first.

---

## TAT and nonlocal II

A standard trap-assisted-tunneling exponent showed why shallow traps can activate leakage at fields far below the direct-BTBT scale.

A finite dead-space / energy-relaxation surrogate was developed for impact ionization:

```math
L_{\rm eff}
=\ell_E(1-e^{-L/\ell_E}).
```

This replaced a bulk field-onset statement with carrier energy history.

The missing quantitative input became a calibrated energy-relaxation and energy-dependent II model for the target HgCdTe composition near 77 K.

---

## Homogeneous field-profile theorem

For the stated homogeneous drift and local WKB leakage models, field shaping alone could not beat the speed–leakage trade at fixed transit time.

Uniform field was the optimum.

This was an important negative result:

> nonuniform electric field is not automatically beneficial; a real escape requires material heterogeneity.

Direction: allocate field across heterogeneous regions.

---

## Heterostructure allocation

A variational condition showed that a heterogeneous detector should place field until each region has the same marginal leakage cost per marginal transit-time improvement.

A separate voltage–transit inequality made bias an independent resource.

Direction: ask whether composition grading can change the Hamiltonian itself rather than merely move the electrostatic field.

---

## Graded-band HgCdTe — direct-Zener escape

A two-band/Kane linear-edge model was solved exactly.

At fixed conduction-band downhill slope, replacing common electrostatic tilt with a decreasing gap increased the direct-Zener WKB action.

The decisive geometry was rewritten without relying on a symmetric band-offset assumption:

```math
S_v=S_c-G,
```

where

```math
G=-dE_g/dx.
```

Defining

```math
\delta=G/S_c,
```

the exact linear-profile action ratio became

```math
\boxed{
\frac{\mathcal S_Z(\delta)}
{\mathcal S_Z(0)}
=
\frac{(2-\delta)^2}
{4(1-\delta)^{3/2}}.
}
```

It diverges as `delta -> 1-`.

This was a genuine direction change: composition grading can preserve useful conduction drive while removing the relative band geometry that enables the ordinary direct-Zener path.

---

## Self-consistent electrostatics — quasi-neutral majority-band pinning

A uniformly depleted multi-micron graded layer produced an unrealistic `N_eff L^2` Poisson burden.

The correct interior picture became quasi neutral.

For p-type material,

```math
\frac{dE_v}{dx}
\simeq
k_BT\frac{d}{dx}\ln(N_A/N_v).
```

For nearly constant `N_A/N_v`,

```math
E_v\approx\text{constant},
```

and therefore

```math
S_c\approx G.
```

So self-consistent equilibrium can naturally approach the favorable direct-Zener geometry rather than destroying it.

Direction: find where the unavoidable electrostatic penalty reappears.

---

## Collection boundary — voltage and local tunneling

A wider-gap collection transition can remain barrier free for minority electrons only if

```math
qV_b\ge\alpha\Delta E_g^{(b)}.
```

Any one-sign field over width `w` obeys

```math
F_{\max}\ge V_b/w.
```

Delta doping or depletion shaping cannot remove that integral electrostatic requirement.

A TAT width/delay criterion followed immediately.

Measured/fitted HgCdTe trap spectra showed that the boundary is not automatically doomed, but shallow interface states can be much more dangerous than geometrical delay.

---

## Local tunneling field allocation

For a fixed boundary voltage and a local TAT tolerance field `F_T(x)`, the exact maximin profile is

```math
F_{\rm opt}(x)\propto F_T(x).
```

For several **local** inverse-field tunneling mechanisms, define

```math
F_{\rm allow}(x)
=\min_m F_m(x)/\Sigma_m.
```

Then

```math
V_b\le\int F_{\rm allow}(x)dx
```

is the exact one-dimensional feasibility condition.

This established a useful local-tunneling **voltage capacity** of the boundary.

At this point the earlier suggestion of placing a generic local `F_II(x)` inside the same envelope was recognized as wrong in the nonlocal thin-device regime.

---

## 2026-08-09 — Graded nonlocal carrier-energy phase boundary

The mean carrier-energy equation was generalized from homogeneous field to an arbitrary conduction-band landscape:

```math
\boxed{
\frac{d\varepsilon}{dx}
=S_c(x)-\frac{\varepsilon}{\ell_E(x)}.
}
```

Thus hot-electron energy depends on the **total conduction-band slope**, not on whether the slope came from electrostatic potential or composition grading.

This exposed the next penalty migration:

> grading can suppress direct-Zener overlap while leaving hot-electron energy input intact.

For the favorable quasi-neutral linear graded absorber

```math
E_g=E_{g0}-Gx,
\qquad
S_c=G,
```

and constant `ell_E`,

```math
\varepsilon(L)
=\Delta E_g
\frac{1-e^{-L/\ell_E}}
{L/\ell_E}.
```

Using

```math
E_{\rm th}=\chi E_g,
```

define

```math
\zeta=\Delta E_g/E_{g0},
\qquad
r=L/\ell_E.
```

The exact mean-energy threshold boundary is

```math
\boxed{
\zeta_{\rm II}
=
\frac{\chi}
{\chi+(1-e^{-r})/r}.
}
```

In the ballistic limit,

```math
\boxed{
\zeta_{\rm II}\to\chi/(1+\chi).
}
```

For `chi=1`, the electron reaches mean II threshold after roughly one-half of the entrance gap has been removed.

A deterministic numerical regression confirmed the phase boundary.

---

## Graded absorber + wide-gap relaxation boundary

The collection boundary was then combined with the nonlocal energy state.

At minimum barrier-free compensation,

```math
qV_b=\alpha\Delta E_g^{(b)},
```

the net conduction-edge step is zero:

```math
\Delta E_c^{(b)}=0.
```

Therefore the boundary adds no downhill conduction-band work.

The carrier energy relaxes while the local gap and approximate II threshold rise:

```math
\varepsilon_b(s)
=\varepsilon_a e^{-s/\ell_{E,b}}.
```

Consequently, if the electron enters below the mean II threshold, the minimally compensated monotonic wider-gap boundary cannot create a new mean-threshold crossing in this model.

This produced a clean architecture-level division of labor:

```text
quasi-neutral graded absorber
-> carrier drive
-> direct-Zener suppression
-> nonlocal hot-electron constraint

wide-gap collection boundary
-> unavoidable electrostatic voltage
-> TAT/BTBT field allocation
-> hot-electron relaxation at minimum compensation.
```

Overcompensation is now recognized as an explicit extra speed resource: it can add boundary acceleration but simultaneously increases field-assisted leakage stress and carrier heating.

---

## Current frontier

The next task is not another abstract theorem.

Build a finite graded-absorber + collection-boundary **phase map** that evaluates simultaneously

```text
transit time
+
local TAT/BTBT margin
+
nonlocal carrier-energy / II margin.
```

Use a parameter sweep over energy-relaxation length until target-composition HgCdTe data are recovered.

Do not use low-field mobility as the high-field velocity model.

Do not write a manuscript yet.
