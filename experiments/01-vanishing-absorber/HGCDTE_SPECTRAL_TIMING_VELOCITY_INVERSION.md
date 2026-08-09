# HgCdTe Spectral Timing Velocity Inversion — Using Wavelength to Probe the Local Collection Velocity

**Date:** 2026-08-09  
**Status:** exact inversion in the sharp high-optical-depth generation limit for a path-additive one-dimensional collection delay; detector-facing consequence of the entrance-gap switch; priority unassessed; no novelty claim

## 1. Purpose

The entrance-gap crossover result says that below the entrance gap, photon energy primarily changes **where the carrier is generated**.

That makes the wavelength sweep more than a qualitative timing test.

If the collection delay from a known generation position is path additive, then the derivative of delay with photon energy directly probes the local effective carrier velocity at the generation position.

Question:

> Can wavelength-resolved timing be inverted into a spatial transport profile in a monotonic graded absorber?

In the sharp-generation limit, yes.

---

## 2. Graded generation-position map

Use a monotonic linear gap

```math
\boxed{
E_g(x)=E_{g,\rm in}-Gx,
\qquad G>0.
}
```

For photon energies inside the graded-gap interval,

```math
E_{g,\rm out}<E_\gamma<E_{g,\rm in},
```

the earliest allowed generation position is

```math
\boxed{
x_g(E_\gamma)
=\frac{E_{g,\rm in}-E_\gamma}{G}.
}
```

Hence

```math
\boxed{
\frac{dx_g}{dE_\gamma}
=-\frac1G.
}
```

The photon energy therefore labels position in the gradient.

---

## 3. Path-additive collection delay

Suppose the intrinsic mean collection time for a carrier created at `x_g` can be written

```math
\boxed{
T(x_g)
=\int_{x_g}^{L}
\frac{dx}{v_{\rm eff}(x)}.
}
```

Here `v_eff(x)>0` is an **effective longitudinal collection velocity**.

This object need not be the microscopic instantaneous band velocity.

Depending on the transport regime it may represent

- drift velocity;
- a local first-moment hydrodynamic velocity;
- a coarse-grained mean first-passage velocity;
- another effective path-additive transport speed.

The inversion is valid only to the extent that this local path-additive description is valid.

---

## 4. Exact spectral derivative

Differentiate with respect to generation position:

```math
\boxed{
\frac{dT}{dx_g}
=-\frac1{v_{\rm eff}(x_g)}.
}
```

Then use

```math
\frac{dx_g}{dE_\gamma}
=-\frac1G.
```

Therefore

```math
\boxed{
\frac{dT}{dE_\gamma}
=
\frac{1}
{Gv_{\rm eff}[x_g(E_\gamma)]}.
}
```

Invert:

```math
\boxed{
v_{\rm eff}[x_g(E_\gamma)]
=
\frac{1}
{G\,dT/dE_\gamma}.
}
```

This is the central result.

---

## 5. Spatial coordinate recovered from photon energy

Because

```math
x_g(E_\gamma)
=\frac{E_{g,\rm in}-E_\gamma}{G},
```

the measured spectral derivative can be plotted directly as a spatial velocity profile:

```math
\boxed{
v_{\rm eff}(x)
=
\left[
G\,
\frac{dT}{dE_\gamma}
\right]^{-1}_{
E_\gamma=E_{g,\rm in}-Gx
}.
}
```

Thus

```text
photon energy
-> generation position
-> local derivative of collection delay
-> effective local carrier velocity.
```

This is a form of transport tomography supplied by the band-gap gradient itself.

---

## 6. Wavelength form

Use

```math
E_\gamma=\frac{hc}{\lambda}.
```

Then

```math
\frac{dE_\gamma}{d\lambda}
=-\frac{hc}{\lambda^2}.
```

Therefore

```math
\frac{dT}{dE_\gamma}
=-\frac{\lambda^2}{hc}
\frac{dT}{d\lambda}.
```

The inversion becomes

```math
\boxed{
v_{\rm eff}[x_g(\lambda)]
=-
\frac{hc}
{G\lambda^2\,dT/d\lambda}.
}
```

Inside the graded-gap interval, increasing wavelength moves generation downstream and should reduce the path length, so

```math
dT/d\lambda<0
```

for positive collection velocity in this simple model.

---

## 7. Constant-velocity limit

If

```math
v_{\rm eff}(x)=v_d,
```

then

```math
T(E_\gamma)
=\frac{E_\gamma-E_{g,\rm out}}
{Gv_d}.
```

Hence

```math
\boxed{
\frac{dT}{dE_\gamma}
=\frac1{Gv_d},
}
```

and the inversion exactly recovers

```math
\boxed{v_{\rm eff}=v_d.}
```

This is the drift-diffusion result already derived elsewhere in the repository.

---

## 8. Differential timing removes an absolute electronics delay

Suppose the measured low-frequency group delay is

```math
\boxed{
T_{\rm meas}(E_\gamma)
=T_{\rm det}(E_\gamma)+T_{\rm common},
}
```

where `T_common` is a wavelength-independent readout / cable / amplifier delay.

Then

```math
\boxed{
\frac{dT_{\rm meas}}{dE_\gamma}
=
\frac{dT_{\rm det}}{dE_\gamma}.
}
```

So the velocity inversion is insensitive to an additive wavelength-independent group delay.

This is a practical advantage over trying to infer an absolute sub-nanosecond transit time from one waveform.

A wavelength-dependent optical/readout delay would still contaminate the inversion and must be controlled or modeled.

---

## 9. Connection to the entrance-gap crossover

The inversion works on the **long-wave / graded-gap side**:

```math
E_{g,\rm out}<E_\gamma<E_{g,\rm in}.
```

At

```math
E_\gamma=E_{g,\rm in},
```

the generation position reaches the physical entrance.

For higher photon energies,

```math
x_g=0,
```

so

```math
\boxed{dx_g/dE_\gamma=0.}
```

The path-length tomography is then exhausted.

Any further wavelength dependence primarily probes

```text
initial carrier energy / momentum distribution
+
energy-dependent scattering
+
transport coefficients
+
optical penetration beyond the sharp-generation approximation.
```

This provides a natural division of the spectral timing experiment:

```text
below entrance gap
-> spatial transport tomography

above entrance gap
-> hot-carrier injection / relaxation spectroscopy.
```

---

## 10. General nonlinear gap profile

The linear gradient is not essential.

For a monotonic gap profile, define the earliest allowed generation point implicitly by

```math
\boxed{E_g[x_g(E_\gamma)]=E_\gamma.}
```

Then

```math
\boxed{
\frac{dx_g}{dE_\gamma}
=
\frac1{E_g'(x_g)}.
}
```

For decreasing gap,

```math
E_g'(x_g)<0.
```

With path-additive delay,

```math
\frac{dT}{dE_\gamma}
=-\frac1{v_{\rm eff}(x_g)}
\frac1{E_g'(x_g)}.
```

Therefore the generalized inversion is

```math
\boxed{
v_{\rm eff}(x_g)
=-
\frac{1}
{E_g'(x_g)\,dT/dE_\gamma}.
}
```

This is the more useful device-design form because a measured composition profile need not be perfectly linear.

---

## 11. Finite optical depth turns the inversion into an integral problem

The exact local inversion assumes that absorbed photons are strongly concentrated near the earliest allowed position.

At finite optical depth, the measured timing observable is an average over the conditional generation distribution:

```math
\boxed{
\bar T(E_\gamma)
=\int dx\,
p(x|E_\gamma,{\rm abs})
T(x;E_\gamma).
}
```

Differentiation then acts on both

- the transport delay `T(x)`;
- the wavelength-dependent generation kernel `p(x|E_gamma,abs)`.

The simple local formula becomes a Fredholm/inverse problem rather than a pointwise identity.

Therefore the sharp-limit inversion should first be used as

```text
an asymptotic diagnostic
+
a design principle for the experiment,
```

not as an automatic data-reduction formula for an optically thin device.

A calibrated `alpha(E_gamma,x)` would allow the finite-depth inverse problem to be solved numerically.

---

## 12. Diffusion / nonlocal transport limitation

The local path-additive form

```math
T(x_g)=\int dx/v_{\rm eff}(x)
```

is exact for deterministic local travel time and is a useful first-moment closure.

For strongly nonlocal transport, velocity overshoot, broad first-passage distributions, recombination, or position-dependent diffusion, the mean delay need not decompose into this simple integral.

In that case the measured spectral derivative still probes

```math
-\frac1{G}\frac{\partial\mathcal F}{\partial x_g}
```

from the general entrance-gap switch formalism, but interpreting it as a local velocity requires additional transport assumptions.

Thus the hierarchy is

```text
transport-independent:
entrance-gap initial-condition switch

path-additive transport:
spectral timing derivative -> local effective velocity

calibrated Boltzmann / Monte Carlo:
spectral timing derivative -> full transport-state sensitivity.
```

---

## 13. Experimental implication

For a known composition profile `E_g(x)`, measure intrinsic differential group delay versus wavelength at fixed temperature and bias.

Inside the graded absorption interval:

1. convert wavelength to photon energy;
2. map photon energy to `x_g` from the measured/calculated gap profile;
3. differentiate the timing curve;
4. infer the local effective velocity from the inversion above;
5. compare the inferred profile with independent transport modeling.

At the entrance-gap wavelength, stop interpreting the slope as position tomography; the experiment transitions into a probe of injected hot-carrier dynamics.

This makes the entrance-gap crossover a **calibration boundary between two different spectroscopic uses of the same timing sweep**.

---

## 14. Claim boundary

### Derived exactly under stated assumptions

- the linear-gradient inversion
  ```math
  v_{\rm eff}=1/[G(dT/dE_\gamma)];
  ```
- the nonlinear-profile generalization
  ```math
  v_{\rm eff}=-1/[E_g'(x_g)(dT/dE_\gamma)];
  ```
- cancellation of an additive wavelength-independent delay in the derivative.

### Conditional assumptions

- high optical depth / localized generation;
- monotonic known `E_g(x)`;
- path-additive mean collection delay;
- negligible wavelength dependence of unrelated readout/optical delays.

### Not established

- that real graded HgCdTe satisfies the local inversion quantitatively;
- a calibrated `v_eff(x)` for any specific detector;
- uniqueness of the finite-optical-depth inverse problem;
- priority or novelty.

---

## 15. Next decisive test

Before promoting this as more than a useful analytic consequence, perform a focused prior-art collision on

```text
wavelength-resolved timing
+
graded-band generation depth
+
carrier-velocity / transit tomography.
```

Then test the inversion on a synthetic finite-optical-depth detector using a known velocity profile to determine when the pointwise formula remains accurate and when full deconvolution is required.
