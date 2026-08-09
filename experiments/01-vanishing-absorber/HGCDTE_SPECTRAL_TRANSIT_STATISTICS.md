# HgCdTe Spectral Transit Statistics — An Analytic Baseline for Mean Delay and Generation-Position Jitter

**Date:** 2026-08-09  
**Status:** exact cold-ballistic two-band/Kane transit law combined with the exact conditional optical-depth generation distribution; no novelty claim

## 1. Purpose

`HGCDTE_SPECTRAL_GENERATION_DISTRIBUTION.md` gives the generation-position statistics for photons that are actually absorbed in a graded region.

This note propagates that distribution through the cold ballistic Kane trajectory.

The aim is not to predict a real HgCdTe impulse response yet. It is to isolate the response-time structure produced by

```text
wavelength-dependent absorption position
+
linear band-gap grading
```

without inserting an unjustified high-field mobility law.

---

## 2. Cold ballistic trajectory from an arbitrary generation point

Assume the favorable quasi-neutral p-type geometry with approximately pinned valence band.

Let an electron be generated cold at a point where the local gap is

```math
E_s.
```

Let the final narrow-gap endpoint be

```math
E_0<E_s.
```

Define the remaining downhill gap drop

```math
\boxed{
D=E_s-E_0.}
```

For a linear downstream gradient of magnitude `G`, the remaining distance is

```math
\boxed{d=D/G.}
```

---

## 3. Kane group velocity along the no-loss trajectory

Set the pinned valence edge to zero. Then locally

```math
U=\Delta=E_g/2.
```

A cold electron generated at the local conduction edge has conserved total energy

```math
E=E_s
```

in the ballistic static-band model.

Define the fractional local drop from the generation gap

```math
u
=\frac{E_s-E_g}{E_s}.
```

The two-band/Kane dispersion gives

```math
\boxed{
\frac{v_g}{v_K}
=\frac{2\sqrt u}{1+u}.
}
```

At generation, `u=0`; the electron accelerates as the local gap falls.

---

## 4. Exact ballistic transit time

The final fractional drop is

```math
\boxed{
\zeta_D
=\frac{D}{E_s}.
}
```

Direct integration gives

```math
\boxed{
T_{\rm bal}(D)
=
\frac{d}{v_K}
\left[
\frac1{\sqrt{\zeta_D}}
+
\frac{\sqrt{\zeta_D}}3
\right].
}
```

Equivalent energy-only form:

```math
\boxed{
T_{\rm bal}(D)
=
\frac1{Gv_K}
\left[
\sqrt{D(E_0+D)}
+
\frac{D^{3/2}}
{3\sqrt{E_0+D}}
\right].
}
```

This is finite despite the zero initial velocity because the near-start singularity in `1/v` is integrable.

---

## 5. Dimensionless transit function

Define

```math
\boxed{d_*=D/E_0.}
```

and

```math
\boxed{
\theta
\equiv
\frac{Gv_K}{E_0}T_{\rm bal}.}
```

Then

```math
\boxed{
\theta(d_*)
=
\frac{\sqrt{d_*}}
{\sqrt{1+d_*}}
\left(1+\frac43d_*\right).
}
```

This dimensionless transit law depends only on the remaining drop relative to the endpoint gap.

It is monotonic increasing with `d_*`.

---

## 6. Generation-position map for one photon energy

For photon energy

```math
E_\gamma=E_0+\delta E,
```

define the normalized photon excess

```math
\boxed{s=\delta E/E_0.}
```

Use the illustrative local absorption model

```math
\alpha=C(E_\gamma-E_g)^\beta,
```

and

```math
n=\beta+1.
```

Conditioned on absorption, optical depth `y` has density

```math
p(y|{\rm abs})
=\frac{e^{-y}}{1-e^{-\tau}},
\qquad
0<y<\tau,
```

where `tau` is the total eligible-region optical depth.

The remaining normalized gap drop after generation is

```math
\boxed{
d_*(y)
=s\left[
1-\left(\frac{y}{\tau}\right)^{1/n}
\right].}
```

Therefore every absorbed event maps directly to a dimensionless transit time

```math
\boxed{
\theta(y)=\theta[d_*(y)].}
```

---

## 7. Exact integral for mean ballistic transit

The conditional mean dimensionless transit is

```math
\boxed{
\langle\theta\rangle
=
\frac1{1-e^{-\tau}}
\int_0^\tau
 e^{-y}
\theta\!\left(
 s\left[1-(y/\tau)^{1/n}\right]
\right)dy.
}
```

Hence

```math
\boxed{
\langle T_{\rm bal}\rangle
=
\frac{E_0}{Gv_K}
\langle\theta\rangle.
}
```

This is a universal dimensionless baseline parameterized by only

```text
normalized photon excess s
optical depth tau
near-edge absorption exponent beta.
```

Absolute material scale enters through `E_0/(G v_K)`.

---

## 8. Generation-position contribution to timing spread

Define

```math
\boxed{
\langle\theta^2\rangle
=
\frac1{1-e^{-\tau}}
\int_0^\tau
 e^{-y}
\theta[d_*(y)]^2dy.
}
```

The generation-position timing standard deviation in this cold-ballistic baseline is

```math
\boxed{
\sigma_\theta
=
\sqrt{
\langle\theta^2\rangle
-
\langle\theta\rangle^2
}.}
```

Thus

```math
\boxed{
\sigma_T
=
\frac{E_0}{Gv_K}\sigma_\theta.
}
```

This is **not** the total detector timing jitter. It includes only variation in optical generation position mapped through the ballistic graded transit.

---

## 9. High-optical-depth limit

As

```math
\tau\to\infty,
```

the absorbed photons are concentrated near the earliest eligible optical depth.

Then

```math
d_*\to s,
```

so

```math
\boxed{
\langle\theta\rangle
\to
\theta(s),
}
```

and

```math
\boxed{
\sigma_\theta\to0.}
```

Therefore high single-pass absorptance drives the ballistic baseline toward

```text
longer mean transit for that wavelength
+
smaller generation-position timing spread.
```

The actual detector can have additional jitter sources.

---

## 10. Optically thin limit

For

```math
\tau\ll1,
```

the conditional optical-depth variable is approximately uniform on `[0,tau]`.

Define

```math
t=y/\tau.
```

Then

```math
\boxed{
\langle\theta\rangle_{\rm thin}
=
\int_0^1
\theta\!\left(
 s[1-t^{1/n}]
\right)dt.
}
```

The absorbed subset is spread across the eligible region and is biased downstream by the rising local absorption coefficient.

It therefore has a shorter mean remaining transit than the optically thick limit, but a broader generation-position timing distribution.

---

## 11. Representative dimensionless values

For the illustrative direct-edge exponent

```math
\beta=1/2,
```

the following values come from numerical quadrature of the exact integrals.

### `s=0.1`

| optical depth `tau` | absorptance | `<theta>` | `sigma_theta` |
|---:|---:|---:|---:|
| 0.1 | 0.095 | 0.196 | 0.079 |
| 1.0 | 0.632 | 0.216 | 0.076 |
| 2.303 | 0.900 | 0.241 | 0.068 |
| 5.0 | 0.993 | 0.276 | 0.049 |

### `s=0.5`

| optical depth `tau` | absorptance | `<theta>` | `sigma_theta` |
|---:|---:|---:|---:|
| 0.1 | 0.095 | 0.502 | 0.226 |
| 1.0 | 0.632 | 0.560 | 0.222 |
| 2.303 | 0.900 | 0.635 | 0.204 |
| 5.0 | 0.993 | 0.740 | 0.154 |

### `s=1.0`

| optical depth `tau` | absorptance | `<theta>` | `sigma_theta` |
|---:|---:|---:|---:|
| 0.1 | 0.095 | 0.808 | 0.396 |
| 1.0 | 0.632 | 0.909 | 0.392 |
| 2.303 | 0.900 | 1.042 | 0.365 |
| 5.0 | 0.993 | 1.232 | 0.281 |

These are dimensionless model values, not HgCdTe response-time predictions.

---

## 12. Near-cutoff scaling

For

```math
s\ll1,
```

```math
\theta(d_*)\simeq\sqrt{d_*}.
```

Therefore the characteristic transit scale behaves roughly as

```math
\boxed{
T\propto
\frac{E_0}{Gv_K}
\sqrt{s}
}
```

up to an optical-depth-dependent dimensionless factor.

Thus, in the ideal graded ballistic model, the transport delay of absorbed photons tends downward as the photon energy approaches the narrow-gap endpoint.

The opposing effect is that near-edge optical absorption also becomes weak.

---

## 13. Physical interpretation

The simple graded detector has a built-in spectral sorting mechanism:

```text
near-cutoff photons
-> eligible only very near the low-gap end
-> short transport
-> weak absorption

higher-energy photons
-> eligible farther upstream
-> longer transport
-> larger hot-electron exposure
-> easier optical absorption.
```

Within one wavelength channel, increasing optical depth then trades

```text
higher quantum efficiency
for
longer mean transport
but smaller generation-position timing spread.
```

This is a more specific and testable statement than a generic detector `speed versus efficiency` slogan.

---

## 14. Important caveats

The result assumes

- one-dimensional illumination and transport;
- monotonic linear gap grading;
- local incoherent Beer-Lambert absorption;
- a power-law near-edge absorption model for the explicit `y -> d_*` map;
- pinned valence band;
- cold ballistic electron generation;
- no energy or momentum scattering in the transit law;
- no weighting-field nonuniformity;
- no diffusion tail;
- no recombination;
- no optical interference or cavity enhancement.

Real HgCdTe timing can be dominated by other mechanisms.

---

## 15. Next decisive comparison

The next question should now be empirical/theoretical prior-art rather than more algebra:

> **Has wavelength-dependent carrier-generation position in compositionally graded HgCdTe already been explicitly connected to wavelength-dependent response time or timing jitter?**

If that connection is already established, the repository should treat the present calculation as a compact analytic baseline.

If not, the next useful physics step is to add one calibrated HgCdTe absorption law and compare the predicted spectral response trend with published graded-detector frequency-response data.
