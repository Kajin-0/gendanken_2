# Critical-Matching Control Precision — Experiment 02

**Date:** 2026-08-12  
**Status:** active hidden-resource derivation  
**Priority:** unassessed; no novelty claim

`TRAVELING_WAVE_CAPTURE.md` found an important ideal counterexample:

```text
for any nonzero collective coupling G,
a clean one-port detector can reach unit monochromatic conversion
if the record rate Gamma is tuned to critical matching.
```

This file attacks the hidden assumption behind that statement:

> can `Gamma` actually be made arbitrarily small and tuned with arbitrarily fine precision?

---

## 1. Start from the exact clean one-port efficiency

Set

```text
kappa_loss = 0,
gamma = 0,
kappa = kappa_in.
```

At resonance,

```math
\eta_R
=\frac{16\kappa\Gamma G^2}
{(\kappa\Gamma+4G^2)^2}.
```

The ideal matching rate is

```math
\boxed{
\Gamma_{\rm match}
=\frac{4G^2}{\kappa}.
}
```

Define the mismatch ratio

```math
x
=\frac{\Gamma}{\Gamma_{\rm match}}.
```

Then the efficiency simplifies exactly to

```math
\boxed{
\eta_R(x)
=\frac{4x}{(1+x)^2}.
}
```

---

## 2. Exact mismatch penalty

The loss from unity is

```math
\boxed{
1-\eta_R
=\left(\frac{x-1}{x+1}\right)^2.
}
```

This makes the control requirement explicit.

To achieve

```math
\eta_R\ge1-\epsilon,
```

one needs

```math
\boxed{
\frac{|x-1|}{x+1}
\le\sqrt\epsilon.
}
```

Equivalently,

```math
\boxed{
\frac{1-\sqrt\epsilon}{1+\sqrt\epsilon}
\le
\frac{\Gamma}{\Gamma_{\rm match}}
\le
\frac{1+\sqrt\epsilon}{1-\sqrt\epsilon}.
}
```

Thus near-unity efficiency requires an increasingly tight **multiplicative** match.

---

## 3. Log-rate form

Let

```math
u=\ln\frac{\Gamma}{\Gamma_{\rm match}}.
```

Then

```math
\boxed{
\eta_R
=\operatorname{sech}^2(\nu/2).
}
```

Therefore target efficiency requires

```math
\boxed{
|\nu|
\le
2\operatorname{artanh}(\sqrt\epsilon).
}
```

For `epsilon<<1`,

```math
|\nu|
\lesssim2\sqrt\epsilon.
```

So the natural control coordinate is logarithmic/multiplicative rate precision.

---

## 4. A nonzero minimum achievable trapping rate restores N_min

The ideal `G -> 0` counterexample requires

```math
\Gamma_{\rm match}=4G^2/\kappa\to0.
```

Suppose real physics imposes a minimum controllable/effective record rate

```math
\Gamma\ge\Gamma_{\rm floor}>0.
```

This floor could represent a residual irreversible channel, minimum switching speed, leakage, controller limitation, or another architecture-specific constraint.

If

```math
\Gamma_{\rm match}<\Gamma_{\rm floor},
```

the best allowed choice is `Gamma=Gamma_floor`.

Target efficiency `1-epsilon` then requires

```math
\frac{\Gamma_{\rm floor}}
{\Gamma_{\rm match}}
\le
\frac{1+\sqrt\epsilon}
{1-\sqrt\epsilon}.
```

Hence

```math
\boxed{
\Gamma_{\rm match}
\ge
\Gamma_{\rm floor}
\frac{1-\sqrt\epsilon}
{1+\sqrt\epsilon}.
}
```

Using

```math
\Gamma_{\rm match}=\frac{4G^2}{\kappa},
```

gives

```math
\boxed{
G^2
\ge
\frac{\kappa\Gamma_{\rm floor}}{4}
\frac{1-\sqrt\epsilon}
{1+\sqrt\epsilon}.
}
```

For identical dipoles `G^2=Ng^2`,

```math
\boxed{
N
\ge
\frac{\kappa\Gamma_{\rm floor}}{4g^2}
\frac{1-\sqrt\epsilon}
{1+\sqrt\epsilon}.
}
```

Taking the ceiling gives the corresponding integer threshold.

---

## 5. Perfect-efficiency limit

As

```math
\epsilon\to0,
```

the condition becomes

```math
\boxed{
G^2\ge\frac{\kappa\Gamma_{\rm floor}}{4},
}
```

or

```math
\boxed{
N\ge\frac{\kappa\Gamma_{\rm floor}}{4g^2}.
}
```

Thus the earlier statement

```text
any nonzero G can give unit monochromatic efficiency
```

is true only when **arbitrarily slow matched record dynamics are themselves an allowed free resource**.

Once a nonzero rate floor is imposed, a positive matter/coupling threshold reappears.

---

## 6. Finite rate-resolution also becomes a resource

Suppose `Gamma` can be tuned only with finite absolute resolution `delta Gamma`.

Near critical matching the efficiency penalty is second order:

```math
1-\eta_R
\simeq
\frac14
\left(
\frac{\Gamma-\Gamma_{\rm match}}
{\Gamma_{\rm match}}
\right)^2.
```

Therefore a fixed **absolute** tuning error becomes a diverging relative error as

```math
\Gamma_{\rm match}\to0.
```

So even without an explicit `Gamma_floor`, finite control resolution eventually prevents arbitrarily weak `G` from reaching a fixed high-efficiency target.

The exact threshold depends on the controller quantization/error model and should not be universalized without specifying it.

---

## 7. Control precision and bandwidth are distinct

Earlier finite-bandwidth analysis already showed

```text
weak G <-> narrow bandwidth / long time.
```

The present result adds a separate requirement:

```text
weak G <-> increasingly small matched Gamma
         <-> increasingly demanding control floor / relative precision.
```

Thus slowing a detector is useful only if the apparatus can actually realize and stabilize the corresponding slow rate.

Time alone is not the full resource.

---

## 8. New detector-boundary lesson

The ideal critical-coupling counterexample exposed one resource trade:

```text
coupling strength <-> time / bandwidth.
```

The control attack exposes another:

```text
coupling strength <-> rate-setting range and precision.
```

Therefore

```math
\boxed{
\text{arbitrarily weak coupling is not operationally free merely because an exact mathematical match exists.}
}
```

A physical detector theorem must specify the achievable control manifold, not only the Hamiltonian.

---

## 9. Connection to the original atom-count intuition

A positive atom-count threshold can reappear for at least three distinct reasons:

```text
finite interaction time / bandwidth;
competing optical or matter loss;
finite controllable rate range / precision.
```

These thresholds have different physics and must not be conflated with band formation.

The original question therefore keeps returning in a more disciplined form:

> **Minimum N is not universal, but it emerges whenever some alternative resource that could compensate weak microscopic coupling is itself bounded.**

---

## 10. Status

The mismatch identities and rate-floor threshold are **DERIVED** within the clean resonant one-port model.

No novelty claim is made for critical coupling or matching-sensitivity mathematics.

The Experiment-02-specific insight is the resource correction:

> **The `G -> 0` perfect-efficiency counterexample relies on free access to arbitrarily slow and arbitrarily well-controlled matching dynamics. Control range/precision is therefore an independent detector resource.**
