# HgCdTe Spectral Drift-Diffusion Robustness — The Ballistic Peak Becomes an Entrance-Gap Knee

**Date:** 2026-08-09  
**Status:** exact first-passage results inside a one-dimensional constant-coefficient drift-diffusion model, combined with the existing graded-generation geometry; this **narrows/corrects** the earlier ballistic timing-peak claim; no novelty claim

## 1. Purpose

The current spectral-timing branch predicts that photon wavelength changes where a carrier can first be generated in a monotonic HgCdTe gap gradient.

The first transport treatment used a forward ballistic Kane trajectory and predicted a delay maximum at the wavelength corresponding to the entrance gap.

That is not yet a robust semiconductor prediction because momentum scattering changes what "hotter photoelectron" means for longitudinal collection.

This note attacks the prediction in the opposite transport limit:

> **strong momentum randomization / drift-diffusion transport.**

The result is a substantive correction.

The wavelength-to-generation-distance mapping survives exactly, but the short-wave decrease of delay is not generic. In the strong-scattering limit the ballistic peak becomes an **entrance-gap knee into a full-length transit plateau**.

---

## 2. Overdamped transport model

Let `X(t)` be the electron position along the collection coordinate.

Use the one-dimensional drift-diffusion stochastic process

```math
\boxed{
dX
=v_d\,dt
+\sqrt{2D}\,dW_t,
}
```

with

```math
v_d>0,
```

constant drift velocity toward the collecting boundary at `x=L`, and diffusion coefficient `D`.

The model is intentionally simple:

- momentum has already relaxed;
- the transport coefficients are treated as local effective constants over the trajectory;
- no claim is made that real high-field HgCdTe has wavelength-independent `v_d` or `D`;
- the model tests whether the earlier spectral timing maximum survives once directed ballistic motion is removed.

Define the remaining distance after generation at `x_g`:

```math
\boxed{
d=L-x_g.}
```

Let `T` be the first-passage time to `x=L`.

---

## 3. Exact mean first-passage time

Let

```math
m_1(x)=\mathbb E[T\mid X(0)=x].
```

The backward drift-diffusion equation is

```math
D m_1''(x)+v_d m_1'(x)=-1,
```

with absorbing boundary

```math
m_1(L)=0.
```

The physically bounded solution upstream is

```math
\boxed{
m_1(x)=\frac{L-x}{v_d}.
}
```

Therefore

```math
\boxed{
\mathbb E[T\mid d]
=\frac{d}{v_d}.
}
```

The mean drift-diffusion collection time is independent of `D` for this constant positive-drift first-passage problem.

Diffusion affects the spread, not the mean.

---

## 4. Exact first-passage variance

The first-passage density is the inverse-Gaussian form

```math
\boxed{
f(t\mid d)
=\frac{d}{\sqrt{4\pi D t^3}}
\exp\!\left[
-\frac{(d-v_dt)^2}{4Dt}
\right],
\qquad t>0.
}
```

Its variance is

```math
\boxed{
\operatorname{Var}(T\mid d)
=\frac{2Dd}{v_d^3}.
}
```

Thus the transport-only timing spread scales as

```text
more remaining distance
-> more diffusion timing variance.
```

---

## 5. Exact transfer function and low-frequency group delay

The Laplace transform of the first-passage distribution is

```math
\boxed{
\mathcal H(s\mid d)
=\mathbb E[e^{-sT}]
=
\exp\!\left[
\frac{d}{2D}
\left(
v_d-\sqrt{v_d^2+4Ds}
\right)
\right].
}
```

With

```math
s=i\Omega,
```

this is the collection transfer function for a delta generation event at remaining distance `d` in the present model.

Expanding around zero modulation frequency,

```math
\ln \mathcal H(i\Omega\mid d)
=-i\Omega\frac{d}{v_d}
-\Omega^2\frac{Dd}{v_d^3}
+O(\Omega^3).
```

Hence the low-frequency group delay is exactly

```math
\boxed{
\tau_g(d)
=-\left.\frac{d}{d\Omega}
\arg\mathcal H(i\Omega\mid d)
\right|_{\Omega=0}
=\frac{d}{v_d}.
}
```

This directly supports the repository's proposed differential-group-delay measurement: in the drift-diffusion limit, the measured low-frequency carrier group delay is the mean first-passage collection time.

---

## 6. Add the random generation-position distribution

Let the optical absorption process generate a random position `X_g` and therefore random remaining distance

```math
D_g=L-X_g.
```

Conditioned on generation distance `d`, the transport statistics above apply.

By total expectation,

```math
\boxed{
\mathbb E[T]
=\frac{\mathbb E[D_g]}{v_d}.
}
```

By total variance,

```math
\boxed{
\operatorname{Var}(T)
=\frac{2D\,\mathbb E[D_g]}{v_d^3}
+
\frac{\operatorname{Var}(D_g)}{v_d^2}.
}
```

This separation is useful:

```text
first term
-> momentum-scattering / diffusion timing spread

second term
-> optical generation-position timing spread.
```

The optical and transport contributions are therefore not interchangeable.

---

## 7. High-optical-depth spectral limit inside the graded gap range

Use the existing linear gap

```math
E_g(x)=E_{g,\rm in}-Gx,
```

with

```math
E_{g,\rm out}=E_{g,\rm in}-GL.
```

For

```math
E_{g,\rm out}<E_\gamma<E_{g,\rm in},
```

the first energetically allowed absorption position is

```math
\boxed{
x_\gamma
=\frac{E_{g,\rm in}-E_\gamma}{G}.
}
```

In the high-optical-depth limit the generation distribution is concentrated near that first allowed position, so

```math
\boxed{
d_\gamma
=L-x_\gamma
=\frac{E_\gamma-E_{g,\rm out}}{G}.
}
```

Therefore

```math
\boxed{
\langle T\rangle
\to
\frac{E_\gamma-E_{g,\rm out}}
{Gv_d}.
}
```

The mean collection delay rises linearly with photon energy across the graded-gap interval because the generation point moves upstream.

The corresponding transport variance is

```math
\boxed{
\operatorname{Var}(T)
\to
\frac{2D}{v_d^3}
\frac{E_\gamma-E_{g,\rm out}}{G}.
}
```

---

## 8. Above the entrance gap

For

```math
E_\gamma\ge E_{g,\rm in},
```

the full graded absorber is energetically allowed.

In the high-optical-depth limit the generation point is pinned near the physical entrance:

```math
x_g\to0,
```

so

```math
\boxed{
d\to L.}
```

If the strong-scattering transport coefficients are taken wavelength independent, then

```math
\boxed{
\langle T\rangle
\to
\frac{L}{v_d}
}
```

and

```math
\boxed{
\operatorname{Var}(T)
\to
\frac{2DL}{v_d^3}.
}
```

Additional photon energy does **not** automatically reduce longitudinal collection time because the photoelectron's excess kinetic energy is not equivalent to a persistent forward drift velocity after momentum randomization.

---

## 9. Corrected spectral signature

Combine the two high-optical-depth branches:

```math
\boxed{
\langle T(E_\gamma)\rangle
=
\begin{cases}
\dfrac{E_\gamma-E_{g,\rm out}}{Gv_d},
& E_{g,\rm out}<E_\gamma<E_{g,\rm in},\\[3mm]
\dfrac{L}{v_d},
& E_\gamma\ge E_{g,\rm in},
\end{cases}
}
```

under the stated constant-coefficient strong-scattering assumptions.

Thus the robust geometry produces

```text
long-wave endpoint
-> vanishing remaining distance
-> small intrinsic collection delay

move to higher photon energy through graded interval
-> generation moves upstream
-> delay increases

entrance-gap photon energy
-> generation reaches physical entrance

higher photon energy
-> generation cannot move farther upstream
-> mean delay approaches a full-length drift plateau.
```

The characteristic spectral feature is therefore

```math
\boxed{
E_\gamma=E_{g,\rm in}
}
```

or

```math
\boxed{
\lambda_{\rm knee}\simeq hc/E_{g,\rm in}.
}
```

---

## 10. What happened to the ballistic timing maximum?

The earlier ballistic branch predicted

```text
rise through the graded-gap interval
-> maximum at entrance-gap wavelength
-> decrease at still higher photon energy.
```

That decrease relied on translating increasing photoelectron excess energy into increasing **forward** group velocity over the fixed full-length path.

The strong-scattering drift-diffusion model removes that assumption.

Once momentum is randomized and transport is described only by the effective drift `v_d`, the short-wave decrease disappears unless `v_d` itself increases with photon energy or another transient-memory mechanism is retained.

Therefore the previous statement

```text
"the entrance-gap timing maximum is robust"
```

is **too strong**.

The safer model hierarchy is

```text
robust generation geometry
-> entrance-gap spectral knee / change in timing slope

ballistic or persistent hot-carrier velocity memory
-> knee can sharpen into a true maximum followed by a short-wave decline.
```

---

## 11. Finite momentum-relaxation bridge

A simple first-moment momentum-relaxation model illustrates the crossover.

Let the mean longitudinal velocity obey

```math
\boxed{
\frac{d\bar v}{dt}
=\frac{v_d-\bar v}{\tau_m}.
}
```

For initial directed mean velocity `v_0`,

```math
\boxed{
\bar v(t)
=v_d+(v_0-v_d)e^{-t/\tau_m}.
}
```

The mean displacement is

```math
\boxed{
d
=v_dT
+(v_0-v_d)\tau_m
(1-e^{-T/\tau_m}).
}
```

At fixed full-length distance `d=L`, increasing a **directed** `v_0` reduces `T`.

But if the optically generated ensemble has negligible mean longitudinal velocity at creation,

```math
v_0\simeq0,
```

then extra photon energy does not by itself create the ballistic short-wave decline.

The existence and size of a true post-entrance-gap decrease therefore depend on the momentum-space distribution and its relaxation, not on energy partition alone.

---

## 12. Prior-art / external-physics posture

Primary HgCdTe Monte Carlo work at 77 K already shows that electron transport is controlled by microscopic scattering, hot-electron dynamics, velocity relaxation, energy relaxation, and impact ionization rather than a simple ballistic trajectory.

The present note does **not** claim drift-diffusion first-passage theory as new.

Its repository role is adversarial:

> it demonstrates that the previously proposed entrance-gap **maximum** is transport-model dependent, while the entrance-gap change in generation geometry remains.

---

## 13. Revised falsification target

The experimental target should therefore be broadened.

Do not require a strict local maximum.

Look for a reproducible wavelength feature near

```math
\boxed{\lambda\simeq hc/E_{g,\rm in}}
```

in one or more of

- differential low-frequency group delay;
- impulse centroid;
- diffusion/transit timing variance;
- slope of timing versus photon energy.

Possible outcomes are physically diagnostic:

```text
rise -> plateau
= strong momentum-randomizing transport

rise -> maximum -> decline
= persistent hot-carrier velocity memory / energy-dependent transport

no entrance-gap feature
= optical generation is not localized as assumed, another transport pole dominates, or the graded model is inadequate.
```

This is a stronger falsification framework than treating one ballistic curve shape as mandatory.

---

## 14. Next decisive work

The next step should use either

1. a calibrated hydrodynamic / Boltzmann transport closure for `Hg_0.8Cd_0.2Te` near 77 K, including velocity and energy relaxation; or
2. a small Monte Carlo transport surrogate with explicit momentum randomization and optical generation positions.

The goal is now to predict the **shape transition** between the ballistic maximum and the drift-diffusion plateau, not to preserve the maximum by assumption.
