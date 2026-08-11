# Shockley-Ramo Observable Correction — Arrival Flux Is Not Generic Terminal Photocurrent

**Date:** 2026-08-10  
**Status:** major observable-level correction; exact reduced results for a planar uniform-weighting single-carrier model; prior-art Shockley-Ramo signal formation is established; no novelty claim for Ramo theory

## 1. Why this correction is mandatory

The theory branch repeatedly used

```math
H(\omega)=\mathbb E[e^{-i\omega T}]
```

as the complex timing response of a carrier with collection/first-passage time `T`.

That object is perfectly well defined as a **collection-flux / arrival-time transform**.

It is **not automatically the terminal RF photocurrent of a semiconductor detector**.

The Shockley-Ramo theorem states that moving charge induces electrode current continuously while it moves.  The measured terminal impulse therefore depends on the carrier trajectory and the detector weighting field, not only on the instant at which the carrier reaches the collecting boundary.

This distinction is classical detector physics and must be enforced before the spectral-depth null tests are presented as photodiode observables.

The correction is not a small prefactor.  Even the simplest uniform deterministic transit gives a direct counterexample to the old identification.

---

# 2. Two observables that must remain distinct

## 2.1 Collection-flux / arrival observable

For a successful first-passage time `T_d` across distance `d`, define

```math
\boxed{
U(d,s)=\mathbb E[e^{-sT_d}].
}
```

For a homogeneous scalar first-passage semigroup,

```math
\boxed{
U(d,s)=e^{-\gamma(s)d}.
}
```

At RF, `s=i omega`.

All exact arrival-time characteristic-function, spatial-semigroup, inverse-Gaussian timing, and first-passage cumulant statements apply to this observable.

## 2.2 Shockley-Ramo terminal-current observable

For a charge moving along trajectory `X_t`, the electrode current is controlled by the weighting field.

In a planar one-dimensional geometry with constant weighting field `E_w`, a reduced single-carrier trajectory gives

```math
i(t)=q E_w \dot X_t
```

in the Shockley-Ramo description.

The frequency-domain terminal signal is therefore a path-current functional,

```math
\boxed{
J(s)=\mathbb E\left[
\int_0^{\tau}e^{-st}qE_w\,dX_t
\right],
}
```

with the appropriate stopping time `tau`.

This is not generically equal to `U(d,s)`.

---

# 3. The simplest counterexample — deterministic uniform drift

Let one conserved carrier start a distance `d` from the collector and move at constant speed `w>0` in a planar detector with constant weighting field.

Its transit time is

```math
T=d/w.
```

The **arrival observable** is

```math
\boxed{
U(d,i\omega)=e^{-i\omega d/w}.
}
```

But the induced current is a rectangular pulse while the charge moves,

```math
i(t)=qE_w w,
\qquad 0<t<d/w.
```

Therefore

```math
\boxed{
J(d,i\omega)
=qE_w w
\frac{1-e^{-i\omega d/w}}{i\omega}.
}
```

The raw terminal current is an **affine exponential in depth**, not a pure exponential.

Consequently the old three-color geometric-mean law

```math
J_2^2=J_1J_3
```

fails even though the underlying transport is perfectly uniform and deterministic.

That is an explicit counterexample to using the arrival-flux three-color theorem as a generic terminal-current identity.

---

# 4. Uniform drift-diffusion gives the same affine-exponential structure

Now take homogeneous one-dimensional drift-diffusion without an upstream boundary or carrier loss:

```math
D\partial_z^2+w\partial_z.
```

For collection distance `d`, the first-passage transform is

```math
\boxed{
U(d,s)=e^{-\gamma(s)d},
}
```

with

```math
\boxed{
D\gamma^2+w\gamma=s.
}
```

For constant planar weighting field, the expected induced-current transform solves the inhomogeneous backward resolvent equation

```math
\boxed{
D J''+wJ'-sJ=-g,
}
```

where `g=qE_w w` is the constant local mean Ramo-current source in this reduced model.

With zero remaining current at the collector,

```math
J(0,s)=0
```

in distance-to-collector coordinates, the solution is

```math
\boxed{
J(d,s)
=\frac{g}{s}
\left[1-e^{-\gamma(s)d}\right].
}
\tag{1}
```

Thus diffusion does not restore the old three-color current law.

It preserves the **constant plus one exponential** structure.

---

# 5. Exact four-color terminal-current closure

Take four equally spaced internal source distances

```math
d_m=d_0+m\Delta d,
\qquad m=0,1,2,3.
```

Equation (1) has the form

```math
J_m=A+Bq^m,
```

with

```math
q=e^{-\gamma\Delta d}.
```

First differences are therefore

```math
\Delta J_m
\equiv J_{m+1}-J_m
=B(q-1)q^m.
```

They form a geometric sequence.

Hence the terminal-current analogue of the three-color arrival law is

```math
\boxed{
(J_2-J_1)^2
=(J_1-J_0)(J_3-J_2).
}
\tag{2}
```

This is an exact **four-color first-difference closure** for the stated planar homogeneous single-carrier model.

The spatial multiplier follows directly from

```math
\boxed{
q
=\frac{J_2-J_1}{J_1-J_0}
=\frac{J_3-J_2}{J_2-J_1}.
}
\tag{3}
```

Therefore

```math
\boxed{
\gamma
=-\frac{1}{\Delta d}\log q,
}
\tag{4}
```

with the logarithm branch followed continuously across RF.

Once `gamma=a+ib` is known at one RF frequency, the same exact uniform drift-diffusion inversion developed earlier applies:

```math
\boxed{
D
=\frac{\omega a}
{b(a^2+b^2)},
}
```

```math
\boxed{
w
=\frac{\omega(b^2-a^2)}
{b(a^2+b^2)}.
}
```

A second RF frequency again adds no transport parameter and becomes a pure closure test.

---

# 6. Useful invariances of the four-color law

Suppose the measured de-embedded current at one RF frequency contains an arbitrary **wavelength-independent multiplicative chain factor** `G(omega)`:

```math
J_m^{meas}=G(\omega)J_m.
```

Every difference is multiplied by `G`, so Eq. (2) is unchanged.

Likewise an arbitrary wavelength-independent additive offset

```math
J_m^{meas}=GJ_m+C
```

is removed by the first differences.

Therefore the four-color closure is automatically insensitive to

```text
common RF gain,
common RF phase,
and a common additive complex offset
```

at fixed frequency.

Wavelength-dependent chain errors do not cancel and remain a calibration requirement.

---

# 7. Broad rigid generation kernels remain compatible

Let wavelength translate one fixed generation shape through the homogeneous segment:

```math
p_m(d)=g(d-d_m).
```

Averaging Eq. (1) over that source gives

```math
J_m=A+\tilde B q^m,
```

because the constant term remains constant and the exponential acquires only the fixed transform of `g`.

Thus Eq. (2) survives **arbitrary finite width and asymmetry** so long as

```text
the source shape translates rigidly,
its support remains inside the homogeneous region,
and the same weighting-field/transport law applies across the translated support.
```

Wavelength-dependent source-shape evolution is again the relevant optical correction.

---

# 8. DC normalization is not innocuous

The common experimental transfer

```math
H_{norm}(d,\omega)
=\frac{J(d,i\omega)}{J(d,0)}
```

is not generally affine-exponential in `d`.

For deterministic uniform drift,

```math
\boxed{
H_{norm}
=\frac{1-e^{-i\omega d/w}}
{i\omega d/w}.
}
```

This is the transform of a rectangular current pulse normalized by its total induced charge.

It is neither the first-passage transform

```math
e^{-i\omega d/w}
```

nor an affine exponential in `d` because of the extra factor `1/d`.

Therefore

> **arrival flux, raw induced RF current, and DC-normalized terminal-current transfer are three distinct observables.**

A theory paper must state which one is being tested before applying any characteristic-function, semigroup, cumulant, or Hankel identity.

---

# 9. Characteristic-function positivity must be relabeled

If a normalized terminal-current impulse response is everywhere nonnegative and integrates to unity, its Fourier transform is indeed a characteristic function of a **charge-weighted signal-time distribution**.

But that random time is not generally the carrier first-passage time.

For example, the deterministic rectangular Ramo pulse corresponds to a uniform signal-time distribution on `[0,T]`, even though the carrier arrival time itself is exactly `T`.

Thus Level-0 positive-definiteness remains a potentially useful **signal-formation consistency test**, but it cannot automatically be interpreted as a transit-time-distribution test.

Likewise, the inverse-Gaussian first-passage skewness/kurtosis identities must not be imposed on generic normalized terminal-current impulse responses.

---

# 10. Finite boundary and additional carrier species change spatial rank predictably

The inhomogeneous terminal-current equation has one particular solution plus the homogeneous propagation modes.

### Interior one-carrier scalar transport

```text
constant particular mode
+ one propagation exponential
```

so raw current has spatial rank at most `2`, while its first differences have rank `1`.

### Uniform scalar second-order transport with a finite boundary

```text
constant particular mode
+ two homogeneous spatial roots
```

so first differences have rank at most `2`.

Therefore **six colors** provide five first differences and can test the rank-two Hankel condition

```math
\boxed{
\det
\begin{pmatrix}
\Delta J_0&\Delta J_1&\Delta J_2\\
\Delta J_1&\Delta J_2&\Delta J_3\\
\Delta J_2&\Delta J_3&\Delta J_4
\end{pmatrix}=0.
}
\tag{5}
```

The two recovered multipliers can then be subjected to the same root-sum/root-product boundary closure developed for the raw first-passage numerator.

Multiple carrier species or unresolved populations can add additional modes and must not be mistaken automatically for anomalous bulk transport.

---

# 11. What does not survive without further work

The simple four-color theorem is **not** claimed for an arbitrary real photodiode.

Potential violations include

```text
nonuniform weighting field,
electron and hole contributions of comparable strength,
spatially varying drift/diffusion,
finite boundaries,
recombination with full two-carrier signal formation,
trapping or internal states,
nonlocal carrier dynamics,
wavelength-dependent generation-shape evolution,
and wavelength-dependent external transfer functions.
```

These are not nuisances to hide.

They are precisely what the higher-rank / multi-frequency falsification hierarchy is intended to detect.

---

# 12. Adversarial disposition of the existing theory

## Survives unchanged as mathematics of the specified observable

```text
first-passage spatial semigroup
uniform drift-diffusion first-passage inversion
first-passage inverse-Gaussian cumulant ratios
regenerative/subordinator timing hierarchy
occupation-time response theorem
```

## Must be relabeled

```text
H=E[e^-iomegaT]
```

is an **arrival/collection-flux observable**, not generic terminal photocurrent.

Characteristic-function positivity applied to normalized terminal current refers to the signal-time weighting distribution when that impulse is positive, not automatically the carrier arrival distribution.

## Must be replaced for ordinary planar terminal current

```text
old 3-color current closure
```

by the Ramo-compatible first-difference law

```math
\boxed{
(J_2-J_1)^2
=(J_1-J_0)(J_3-J_2).
}
```

This correction materially strengthens the scientific integrity of the proposed paper.

---

# 13. Paper consequence

The observable distinction should appear near the beginning of any manuscript.

A clean theoretical structure is now

```text
Ideal arrival-flux gedanken
-> strongest first-passage theorems

then

Shockley-Ramo signal formation
-> show why generic terminal current differs
-> derive the experimentally closer 4-color difference closure

then

higher spatial rank + RF closure
-> boundaries / multiple populations / memory
```

The first-passage results remain valuable as exact limiting theory.

The Shockley-Ramo correction prevents them from being overclaimed as direct identities of every measured photodiode RF transfer.

---

## Numerical regression

`numerics/ramo_four_color_current_closure.py`

checks

```text
arrival-flux 3-color closure,
raw Ramo-current 4-color first-difference closure,
exact recovery of D and w,
invariance to common multiplicative complex gain,
invariance to common additive complex offset,
and failure of the old 3-color law for raw and DC-normalized terminal current.
```

## Established signal-formation literature boundary

Shockley-Ramo induced-current theory and its application to semiconductor-detector / photodiode impulse response are established and are **not novelty claims**.  The candidate contribution, if any, is the spectral-depth closure/falsification architecture built on the correctly distinguished observable classes.
