# Shockley-Ramo Four-Color Transport — DC + One-RF Complete Uniform Inversion

**Date:** 2026-08-10  
**Status:** **DERIVED / CHECKED / CONDITIONAL** for homogeneous one-dimensional drift-diffusion with uniform Markov recombination and the planar raw-current observable; algebraic inversion itself is not a novelty claim

## 1. Why recombination does not kill the four-color core

The adversarial question is immediate:

> **Does ordinary homogeneous carrier recombination add another spatial mode and destroy the four-color raw-current closure?**

No.

Uniform Markov recombination changes the spatial propagation exponent but preserves the affine-exponential raw-current form.

This gives a stronger complete gedanken experiment:

```text
four colors at DC
+
four colors at one RF
-> D, drift, and recombination rate

second RF
-> pure falsification measurement.
```

---

## 2. Killed drift-diffusion first passage

Let the carrier have

```text
diffusion D > 0
downstream drift w > 0
uniform killing/recombination rate kappa >= 0.
```

The successful first-passage transform over distance `d` is

```math
\boxed{
U(d,s)=e^{-\gamma(s)d},
}
```

where

```math
\boxed{
D\gamma(s)^2+w\gamma(s)=\kappa+s.
}
\tag{1}
```

At DC,

```math
\gamma_0\equiv\gamma(0)
```

is real and nonnegative.

At RF,

```math
\gamma_\omega\equiv\gamma(i\omega)
```

is complex.

---

## 3. Raw Shockley-Ramo current keeps one exponential mode

For uniform planar weighting and the reduced one-carrier geometry, the density of carriers still alive and not yet collected is

```math
M(t)=P(t<T,\ t<\zeta),
```

where `zeta` is the Markov killing time.

The ensemble Ramo current is proportional to `w M(t)`.

For spatially homogeneous exponential killing,

```math
M(t)=e^{-\kappa t}S_0(t),
```

where `S_0` is the no-killing first-passage survival.

Hence

```math
\widetilde M(s)
=\frac{1-U(d,s)}{s+\kappa}.
```

Therefore

```math
\boxed{
J(d,s)
=C(s)
\left[1-e^{-\gamma(s)d}\right],
}
\tag{2}
```

with a depth-independent prefactor

```math
C(s)\propto\frac{w}{s+\kappa}.
```

Thus uniform recombination does **not** raise the first-difference spatial rank.

The exact four-color closure still holds at DC and RF.

---

## 4. Recover the DC and RF spatial exponents

For four equally spaced source distances

```math
d_m=d_0+mh,
```

first differences obey

```math
\Delta J_m(s)=B(s)e^{-\gamma(s)d_m}.
```

Thus

```math
\boxed{
q(s)
=\frac{\Delta J_1(s)}{\Delta J_0(s)},
}
```

and

```math
\boxed{
\gamma(s)
=-\frac1h\log q(s).
}
\tag{3}
```

At DC this yields

```math
\gamma_0.
```

At one RF frequency it yields

```math
\gamma_\omega.
```

Common complex gain and common additive current offset cancel in the spatial differencing as before.

---

## 5. Exact elimination of recombination

Equation (1) at DC is

```math
D\gamma_0^2+w\gamma_0=\kappa.
\tag{4}
```

At RF,

```math
D\gamma_\omega^2+w\gamma_\omega
=\kappa+i\omega.
\tag{5}
```

Subtract Eq. (4) from Eq. (5):

```math
\boxed{
D A+w B=i\omega,
}
\tag{6}
```

where

```math
A=\gamma_\omega^2-\gamma_0^2,
```

```math
B=\gamma_\omega-\gamma_0.
```

Since `D,w` are real, Eq. (6) contains two real equations for two real unknowns.

Define

```math
\boxed{
\Delta
=\Re A\,\Im B
-\Im A\,\Re B.
}
```

For `Delta != 0`,

```math
\boxed{
D
=-\frac{\omega\Re B}{\Delta},
}
\tag{7}
```

```math
\boxed{
w
=\frac{\omega\Re A}{\Delta}.
}
\tag{8}
```

Then recover recombination from the DC exponent:

```math
\boxed{
\kappa
=D\gamma_0^2+w\gamma_0,
}
\tag{9}
```

and

```math
\boxed{
\tau=1/\kappa
}
```

when `kappa>0` is interpreted as one uniform first-order lifetime.

---

## 6. No-recombination limit

If

```math
\kappa\to0,
```

then

```math
\gamma_0\to0.
```

Equations (7)-(8) reduce to the earlier one-frequency formulas using only

```math
\gamma_\omega=a+ib.
```

So the recombination theorem is a strict extension of the minimal uniform drift-diffusion inversion.

---

## 7. The second RF frequency is again pure falsification

After DC plus one RF determine

```text
D
w
kappa,
```

the model has no remaining transport freedom.

Every additional RF frequency must produce a spatial exponent satisfying

```math
\boxed{
D\gamma(\omega)^2
+w\gamma(\omega)
=\kappa+i\omega.
}
\tag{10}
```

Equivalently, repeating Eqs. (7)-(9) at multiple RF frequencies must give the same real

```math
D,
\qquad
w,
\qquad
\kappa.
```

Thus the experiment has a particularly simple logic:

```text
DC + one RF -> identify the complete uniform Markov model
second RF -> try to falsify it.
```

---

## 8. Strong falsification conditions

The uniform model fails if, beyond uncertainty,

```text
D reconstructed from different RF frequencies changes,
w changes with RF,
kappa changes with RF,
kappa acquires a significant imaginary component,
D <= 0,
or the four-color spatial closure itself fails.
```

These failure channels distinguish

```text
model order failure
from
frequency-law failure.
```

Do not absorb them immediately into an arbitrary `D(omega)` fit.

---

## 9. Important limitations

The theorem assumes

```text
one dominant signal carrier
homogeneous D and drift over the sampled segment
uniform first-order Markov recombination
uniform planar weighting field
remote upstream boundary / no extra boundary spatial mode
calibrated relative generated-carrier amplitude
one spatial propagation exponent after first differencing.
```

A second carrier, finite boundary, spatially varying coefficients, trapping memory, nonuniform weighting field, or non-Markov loss can add modes or RF dispersion.

Those effects belong at the next rung of the falsification hierarchy.

---

## 10. Why this is cleaner than DC-normalized-current fitting

The earlier conditioning analysis correctly showed that normalizing an arrival/RF field by successful DC collection changes the inferred drift through a Doob transform.

For the **raw terminal current**, the four-color spatial differencing provides another route:

```text
recover the DC spatial exponent
recover the RF spatial exponent
subtract their dispersion equations
solve D,w,kappa directly.
```

This keeps the observable mapping explicit and avoids pretending that a DC-normalized current transfer is itself a first-passage characteristic function.

---

## 11. Numerical regression

`numerics/ramo_recombination_complete_inversion.py`

constructs exact raw-current sequences with

```text
D = 0.12
w = 1.70
kappa = 0.45
```

and arbitrary common complex RF gain/offset.

Four-color differencing recovers `gamma0` and `gamma(omega)`.

Equations (7)-(9) recover all three physical coefficients to numerical precision at several RF frequencies.

---

## 12. Paper-level significance

This result strengthens the reduced paper core because recombination no longer has to be treated as an external calibration in the simplest homogeneous model.

The minimal theoretical experiment can be stated as:

> **Use four calibrated internal source coordinates to recover the spatial propagation exponent at DC and one RF frequency.  Those two exponents uniquely determine homogeneous diffusion, drift, and first-order recombination.  Repeat at a second RF frequency; any disagreement falsifies the entire three-parameter local Markov model.**

The surrounding algebra is classical.  The candidate contribution remains the spectral-depth / Shockley-Ramo-aware falsification architecture, not the existence of quadratic drift-diffusion roots.
