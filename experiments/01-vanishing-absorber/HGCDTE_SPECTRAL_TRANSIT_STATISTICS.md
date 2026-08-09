# HgCdTe Spectral Transit Statistics — Corrected Ballistic Baseline with Photoexcitation Energy

**Date:** 2026-08-09  
**Status:** exact ballistic two-band/Kane transit integral combined with exact conditional optical-depth generation statistics and a parameterized electron photon-excess fraction; no novelty claim

## 1. Purpose

A photon absorbed downstream of the local band edge creates an electron with nonzero initial kinetic excess. The first version of this note treated every generation event as cold and is superseded by this corrected form.

The goal remains narrow:

> **Given a wavelength-dependent generation-position distribution in a linearly graded absorber, what ballistic transit-time distribution follows before adding scattering?**

---

## 2. Geometry and optical generation coordinate

Let

```math
E_0=E_{g,\rm out},
```

```math
E_\gamma=E_0+\delta E,
```

and define normalized photon excess

```math
\boxed{s=\delta E/E_0.}
```

For the illustrative local absorption law

```math
\alpha=C(E_\gamma-E_g)^\beta,
```

set

```math
n=\beta+1.
```

Conditioned on absorption, optical depth `y` obeys

```math
\boxed{
p(y|{\rm abs})
=\frac{e^{-y}}{1-e^{-\tau}},
\qquad 0<y<\tau.
}
```

The local photon excess is

```math
\boxed{
u(y)
=\delta E
\left(\frac{y}{\tau}\right)^{1/n}.}
```

Define

```math
\boxed{q(y)=u(y)/\delta E.}
```

Then

```math
\boxed{
q(y)=\left(\frac{y}{\tau}\right)^{1/n},
\qquad 0\le q\le1.
}
```

The remaining geometric band-edge drop is

```math
\boxed{D=\delta E(1-q).}
```

and the remaining distance is

```math
\boxed{d=D/G.}
```

---

## 3. Photoelectron initial excess

Let the electron receive fraction

```math
\boxed{\xi_e}
```

of the local photon excess:

```math
\boxed{
\varepsilon_{\rm gen}=\xi_eu.
}
```

For the symmetric two-band Kane optical transition,

```math
\boxed{\xi_e=1/2.}
```

Real HgCdTe requires a multiband optical-transition model, so retain `xi_e` explicitly.

---

## 4. Exact ballistic transit from a downstream generation point

The conserved electron energy is

```math
\boxed{
\mathcal E
=E_\gamma-(1-\xi_e)u.
}
```

Define the electron excess above the local conduction edge at generation and at the output:

```math
\boxed{
z_s=\xi_eu,}
```

```math
\boxed{
z_0=\delta E-(1-\xi_e)u.}
```

For the two-band Kane conduction dispersion and linear downstream gap,

```math
\boxed{
T_{\rm bal}(u)
=
\frac1{Gv_K}
\left[
\Phi(z_0;\mathcal E)
-
\Phi(z_s;\mathcal E)
\right],
}
```

where

```math
\boxed{
\Phi(z;\mathcal E)
=
\sqrt{\mathcal Ez}
+
\frac{z^{3/2}}
{3\sqrt{\mathcal E}}.
}
```

Checks:

```text
u=0
-> earliest allowed cold-edge generation
-> recovers previous formula

u=delta E
-> generation at output
-> z_s=z_0
-> T=0.
```

---

## 5. Dimensionless transit function

Normalize energies by `E_0`.

For

```math
q=u/\delta E,
```

define

```math
\boxed{
e
=\mathcal E/E_0
=1+s[1-(1-\xi_e)q],
}
```

```math
\boxed{
z_s^*
=\xi_esq,
}
```

```math
\boxed{
z_0^*
=s[1-(1-\xi_e)q].
}
```

Define

```math
\boxed{
\phi(z,e)
=\sqrt{ez}
+\frac{z^{3/2}}{3\sqrt e}.
}
```

Then

```math
\boxed{
\theta(q;s,\xi_e)
\equiv
\frac{Gv_K}{E_0}T_{\rm bal}
=
\phi(z_0^*,e)-\phi(z_s^*,e).
}
```

This is the corrected universal ballistic timing kernel.

---

## 6. Conditional mean and timing spread

The dimensionless mean is

```math
\boxed{
\langle\theta\rangle
=
\frac1{1-e^{-\tau}}
\int_0^\tau
 e^{-y}
\theta\!\left[
(y/\tau)^{1/n};s,\xi_e
\right]dy.
}
```

The second moment is

```math
\boxed{
\langle\theta^2\rangle
=
\frac1{1-e^{-\tau}}
\int_0^\tau
 e^{-y}
\theta\!\left[
(y/\tau)^{1/n};s,\xi_e
\right]^2dy.
}
```

Hence the generation-position contribution to timing spread is

```math
\boxed{
\sigma_\theta
=
\sqrt{\langle\theta^2\rangle-
\langle\theta\rangle^2}.
}
```

Absolute scales are

```math
\boxed{
\langle T\rangle
=\frac{E_0}{Gv_K}\langle\theta\rangle,
}
```

```math
\boxed{
\sigma_T
=\frac{E_0}{Gv_K}\sigma_\theta.
}
```

These contain only generation-position timing variation. They omit scattering, diffusion, avalanche statistics, electronics, etc.

---

## 7. Optically thick limit — robust wavelength-delay curve

As

```math
\tau\to\infty,
```

the absorbed population concentrates near the earliest allowed point:

```math
q\to0.
```

Therefore the result becomes independent of `xi_e`:

```math
\boxed{
\langle\theta\rangle
\to
\theta_\infty(s),
}
```

where

```math
\boxed{
\theta_\infty(s)
=
\frac{\sqrt s}{\sqrt{1+s}}
\left(1+\frac43s\right).
}
```

and

```math
\boxed{\sigma_\theta\to0.}
```

Thus the high-optical-depth ballistic delay is

```math
\boxed{
T_\infty(E_\gamma)
=
\frac{E_0}{Gv_K}
\theta_\infty\!\left(
\frac{E_\gamma-E_0}{E_0}
\right).
}
```

Equivalent energy form:

```math
\boxed{
T_\infty
=
\frac1{Gv_K}
\left[
\sqrt{\delta E(E_0+\delta E)}
+
\frac{\delta E^{3/2}}
{3\sqrt{E_0+\delta E}}
\right].
}
```

This relative wavelength trend does not require an absorption-coefficient calibration once the optically thick limit is justified.

---

## 8. Wavelength form of the thick-limit prediction

Using approximately

```math
E_0=hc/\lambda_c,
```

```math
E_\gamma=hc/\lambda,
```

then

```math
\boxed{
s=\lambda_c/\lambda-1.}
```

So

```math
\boxed{
T_\infty(\lambda)
=\frac{E_0}{Gv_K}
\theta_\infty(\lambda_c/\lambda-1).
}
```

At fixed device profile, delay ratios between two wavelengths in this limit are simply

```math
\boxed{
\frac{T_\infty(\lambda_1)}
{T_\infty(\lambda_2)}
=
\frac{
\theta_\infty(\lambda_c/\lambda_1-1)
}{
\theta_\infty(\lambda_c/\lambda_2-1)
}.
}
```

The unknown absolute gradient and Kane velocity cancel from the ratio.

---

## 9. Near-cutoff asymptote

For

```math
s\ll1,
```

```math
\boxed{
\theta_\infty(s)
\simeq\sqrt s.
}
```

Hence

```math
\boxed{
T_\infty
\sim
\frac{E_0}{Gv_K}
\sqrt{\frac{E_\gamma-E_0}{E_0}}.
}
```

or in wavelength language near cutoff,

```math
\boxed{
T_\infty
\propto
\sqrt{\lambda_c-\lambda}
}
```

up to the first-order conversion between photon energy and wavelength.

So the ideal graded ballistic transport delay tends to zero toward cutoff, while the optical absorption strength simultaneously weakens.

---

## 10. Representative thick-limit dimensionless curve

For a detector with endpoint cutoff `lambda_c=10 um`, the dimensionless thick-limit delay factor is

| wavelength | `s=lambda_c/lambda-1` | `theta_infty` |
|---:|---:|---:|
| 9.5 um | 0.0526 | 0.239 |
| 9 um | 0.111 | 0.363 |
| 8 um | 0.250 | 0.596 |
| 7 um | 0.429 | 0.861 |
| 6 um | 0.667 | 1.195 |
| 5 um | 1.000 | 1.650 |

These are dimensionless ratios, not predicted nanoseconds.

---

## 11. Optical-depth dependence with photoexcitation correction

Numerical quadrature for the illustrative `beta=1/2` model confirms

```text
increasing tau
-> larger mean remaining transport
-> mean ballistic delay approaches theta_infty(s).
```

However the generation-position timing spread is **not generally monotonic** in `tau`.

It can increase slightly between very thin and moderate optical depth before decreasing toward zero in the optically thick limit.

Therefore do not summarize the result as

```text
higher QE -> lower timing jitter
```

without specifying the optical-depth regime.

The robust statement is

```math
\boxed{
\tau\to\infty
\Rightarrow
\langle\theta\rangle\to\theta_\infty,
\quad
\sigma_\theta\to0.
}
```

---

## 12. Role of `xi_e`

At finite optical depth, the timing distribution depends on `xi_e` because downstream-generated electrons begin with different velocities.

Larger `xi_e` generally reduces the geometric transit time of downstream events because more photon excess is initially placed in the electron.

But the optically thick limit is insensitive to `xi_e` because absorption is concentrated where `u -> 0`.

Thus the **high-QE wavelength-delay asymptote is more robust** than finite-QE hot-electron or timing predictions.

---

## 13. Prior-art posture

Established HgCdTe literature already covers

- grading-induced carrier drift and faster response;
- spectral response of compositionally graded devices;
- tunable-pulse impulse-response measurements;
- carrier transit as a possible fast-response limit.

A focused primary-source search has not yet located the exact analytic map

```text
wavelength
-> generation optical-depth distribution
-> graded ballistic transit distribution.
```

Status: candidate underexplored analytic connection; priority unproven.

---

## 14. Claim boundary

### Exact within the stated symmetric/two-band ballistic model

The transit integral and the `theta(q;s,xi_e)` representation.

### Exact optical statistic

The truncated-exponential generation distribution in optical-depth coordinates.

### Conditional

The power-law `y -> q` map and use of a constant `xi_e`.

### Not established

- real HgCdTe multiband `xi_e`;
- scattering-limited wavelength-resolved timing;
- measured intrinsic `T(lambda)` after de-embedding electronics;
- calibrated optical depth versus wavelength;
- novelty.

---

## 15. Next decisive test

Two routes are now useful:

1. **experimental collision:** find or reanalyze tunable-pulse HgCdTe measurements at several wavelengths under fixed bias/readout and look for the predicted intrinsic delay trend after common electronic poles are removed;
2. **material calibration:** implement a primary-source HgCdTe absorption model and multiband photon-excess partition to move beyond the analytic baseline.

Do not add more abstract detector resources before testing one of these.
