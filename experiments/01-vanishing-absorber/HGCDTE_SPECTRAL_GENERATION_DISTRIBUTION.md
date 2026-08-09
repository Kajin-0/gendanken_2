# HgCdTe Spectral Generation Distribution — Quantum Efficiency Versus Remaining Carrier Drive

**Date:** 2026-08-09  
**Status:** exact optical-depth generation statistics plus conditional graded-band transport consequences; no novelty claim

## 1. Purpose

`HGCDTE_SPECTRAL_GENERATION_TRANSPORT.md` established that a photon of energy `E_gamma` can only create a carrier after the local gap falls below that energy.

That gives an earliest possible generation position, but a real absorbed photon has a distribution of generation positions.

This note derives that distribution and asks:

> **How does increasing optical depth / absorption probability change the remaining transport distance and hot-electron exposure of the detected photons?**

The answer is clean in optical-depth coordinates.

---

## 2. Optical survival and generation probability

For fixed photon energy, let the energetically eligible region begin at `x_gamma`.

Define the accumulated optical depth

```math
\boxed{
y(x)
=\int_{x_\gamma}^{x}
\alpha(E_\gamma,s)ds.
}
```

Let the total eligible-region optical depth be

```math
\boxed{
\tau_\gamma=y(L).
}
```

The photon survival probability to optical depth `y` is

```math
\boxed{S(y)=e^{-y}.}
```

The differential probability of absorption in `dy` is therefore

```math
\boxed{dP_{\rm abs}=e^{-y}dy.}
```

The total single-pass absorption probability is

```math
\boxed{
\eta_\gamma
=1-e^{-\tau_\gamma}.
}
```

---

## 3. Universal conditional generation-depth distribution

Condition on the photon actually being absorbed before the end of the region.

Then

```math
\boxed{
p(y\mid {\rm abs})
=
\frac{e^{-y}}
{1-e^{-\tau_\gamma}},
\qquad
0\le y\le\tau_\gamma.
}
```

This result is independent of the detailed spatial form of `alpha(x)`.

The cumulative distribution is

```math
\boxed{
P(Y\le y\mid{\rm abs})
=
\frac{1-e^{-y}}
{1-e^{-\tau_\gamma}}.
}
```

Thus detected photons are exponentially biased toward the **earliest optically allowed part** of the absorber when expressed in optical-depth coordinates.

---

## 4. Immediate efficiency–transport interpretation

As

```math
\tau_\gamma\to\infty,
```

the single-pass quantum efficiency tends toward unity and the conditional distribution approaches an ordinary exponential concentrated around

```math
y=O(1).
```

So a high-optical-depth detector tends to absorb photons soon after they enter the eligible region.

In a decreasing-gap absorber, that means a detected carrier tends to retain more of the remaining downhill band-edge path.

By contrast, in the optically thin limit, only a small fraction of photons are absorbed, and the detected subset can be biased farther downstream when the local absorption coefficient itself rises with decreasing gap.

This is a spatial form of an efficiency–transport tradeoff.

---

## 5. Map optical depth to local bandgap excess

For an analytic example use

```math
\alpha(E_\gamma,x)
=C[E_\gamma-E_g(x)]^\beta,
\qquad
\beta>-1,
```

inside a linear gap

```math
E_g(x)=E_{g,\rm in}-Gx.
```

Define

```math
u
\equiv
E_\gamma-E_g(x).
```

At the earliest eligible position,

```math
u=0,
```

and at the output

```math
u=\delta E
\equiv
E_\gamma-E_{g,\rm out}.
```

The accumulated optical depth is

```math
\boxed{
y(u)
=\frac{C}{G(\beta+1)}
u^{\beta+1}.}
```

Define

```math
n=\beta+1.
```

Since

```math
\tau_\gamma
=\frac{C}{Gn}(\delta E)^n,
```

```math
\boxed{
u(y)
=\delta E
\left(\frac{y}{\tau_\gamma}\right)^{1/n}.}
```

---

## 6. Remaining downhill carrier drive after generation

At generation, the remaining gap drop to the output is

```math
D(y)
=E_g(x)-E_{g,\rm out}.
```

Because

```math
E_g(x)=E_\gamma-u,
```

```math
\boxed{
D(y)
=\delta E-u(y)
=\delta E
\left[
1-\left(\frac{y}{\tau_\gamma}\right)^{1/n}
\right].}
```

The corresponding remaining geometric distance is

```math
\boxed{
d(y)=D(y)/G.}
```

Thus the optical absorption event directly selects the carrier's remaining band-edge energy and transport distance.

---

## 7. Mean remaining drive among absorbed photons

Using the conditional truncated-exponential distribution,

```math
\langle u\rangle
=
\frac{\delta E}{1-e^{-\tau_\gamma}}
\tau_\gamma^{-1/n}
\gamma\!\left(1+\frac1n,\tau_\gamma\right),
```

where the lowercase `gamma` is the lower incomplete gamma function.

Therefore

```math
\boxed{
\langle D\rangle
=
\delta E
\left[
1-
\frac{
\tau_\gamma^{-1/n}
\gamma(1+1/n,\tau_\gamma)
}
{1-e^{-\tau_\gamma}}
\right].}
```

And

```math
\boxed{
\langle d\rangle
=\langle D\rangle/G.}
```

This is a generation-position statistic, not yet a mean electrical impulse-response time.

---

## 8. Optically thin limit

For

```math
\tau_\gamma\ll1,
```

the conditional absorption density is proportional to the local absorption coefficient.

Then

```math
\boxed{
\langle u\rangle
\to
\delta E\frac{\beta+1}{\beta+2},}
```

so

```math
\boxed{
\langle D\rangle
\to
\frac{\delta E}{\beta+2}.}
```

For the illustrative direct-edge value

```math
\beta=1/2,
```

```math
\boxed{
\langle D\rangle
\to0.4\,\delta E.}
```

The few photons that are absorbed in an optically thin graded edge are therefore biased toward the downstream region where absorption is stronger.

---

## 9. Optically thick limit

For

```math
\tau_\gamma\gg1,
```

the typical generation optical depth remains `O(1)` while

```math
u/\delta E
\sim
\tau_\gamma^{-1/n}.
```

Therefore

```math
\boxed{
\langle D\rangle
\to\delta E.}
```

High single-pass efficiency pushes the detected population toward the earliest eligible generation region, leaving nearly the full remaining downhill band-edge drop.

---

## 10. Fraction of absorbed photons whose mean trajectory reaches the II threshold

For a carrier generated with remaining gap drop `D`, the current constant-gradient / constant-relaxation model gives exit mean excess energy

```math
\boxed{
\varepsilon_{\rm out}(D)
=G\ell_E
\left[1-e^{-D/(G\ell_E)}\right].}
```

The exit threshold is

```math
\chi E_{g,\rm out}.
```

Define

```math
K=G\ell_E.
```

If

```math
K\le\chi E_{g,\rm out},
```

then even an indefinitely long remaining segment cannot raise the **mean** energy to threshold, so the mean-threshold-accessible fraction is zero.

If

```math
K>\chi E_{g,\rm out},
```

the critical remaining gap drop satisfies

```math
K[1-e^{-D_c/K}]
=\chi E_{g,\rm out},
```

hence

```math
\boxed{
D_c
=-K\ln\!\left[
1-\frac{\chi E_{g,\rm out}}{K}
\right].}
```

If

```math
D_c\ge\delta E,
```

no absorbed photon at that energy reaches the deterministic mean threshold.

If

```math
0<D_c<\delta E,
```

mean-threshold access occurs for early enough absorption such that

```math
D\ge D_c.
```

Equivalently,

```math
u\le\delta E-D_c.
```

For the power-law absorption model, define

```math
\boxed{
y_c
=\tau_\gamma
\left(
1-\frac{D_c}{\delta E}
\right)^n.}
```

Then the fraction of **absorbed photons** whose deterministic mean carrier trajectory reaches the II threshold is

```math
\boxed{
f_{\rm mean-II}
=
\frac{1-e^{-y_c}}
{1-e^{-\tau_\gamma}}.}
```

This is not an impact-ionization probability. It is the fraction of generation positions for which the repository mean-energy trajectory becomes threshold accessible.

---

## 11. Ballistic limit of the threshold-accessible fraction

For

```math
\ell_E\to\infty,
```

```math
D_c\to\chi E_{g,\rm out}.
```

Thus if

```math
\delta E\le\chi E_{g,\rm out},
```

```math
\boxed{f_{\rm mean-II}=0.}
```

in the ballistic mean-threshold model.

If

```math
\delta E>\chi E_{g,\rm out},
```

then

```math
\boxed{
y_c
=\tau_\gamma
\left(
1-
\frac{\chi E_{g,\rm out}}
{\delta E}
\right)^{\beta+1}.}
```

and

```math
\boxed{
f_{\rm mean-II}
=
\frac{
1-\exp[-y_c]
}
{1-e^{-\tau_\gamma}}.}
```

As `tau_gamma -> infinity`, this fraction tends to one whenever `y_c` grows without bound.

Thus for sufficiently energetic photons, demanding very high single-pass absorption can bias nearly all detected events toward generation positions with large remaining carrier drive.

---

## 12. The important detector interpretation

The gradient produces a wavelength-dependent trade:

```text
larger optical depth
-> higher absorption probability
-> earlier generation within the eligible region
-> longer remaining transport distance
-> larger remaining downhill band-edge drive
-> potentially larger hot-electron exposure.
```

But for near-cutoff photons satisfying

```math
E_\gamma-E_{g,\rm out}
\le
\chi E_{g,\rm out},
```

the ballistic deterministic mean-II threshold remains inaccessible regardless of generation position.

Therefore the strongest efficiency–hot-electron conflict appears for photons sufficiently far above the narrow-gap endpoint, not necessarily at the detector cutoff itself.

---

## 13. Relation to response time

The remaining distance distribution

```math
d(y)=D(y)/G
```

can be pushed through either

- the cold ballistic Kane transit law; or
- a future calibrated scattering-limited transport model.

The resulting distribution of electrical transit times is then weighted by the same optical generation statistics.

This is the correct route to a wavelength-resolved impulse response.

---

## 14. Claim boundary

### Exact

The conditional optical-depth distribution

```math
\boxed{
p(y|{\rm abs})
=e^{-y}/(1-e^{-\tau_\gamma})
}
```

is exact for one-pass local absorption.

The map from `y` to remaining drive is exact for the stated linear gap and power-law local absorption model.

### Conditional

The mean-II fraction uses the repository deterministic energy-relaxation surrogate and should not be confused with a stochastic ionization probability.

### Not established

- calibrated HgCdTe `alpha(E,x)`;
- actual II probability;
- full impulse-response distribution;
- optical interference/coherence;
- photon recycling;
- Urbach-tail generation upstream of the nominal gap crossing;
- novelty.

---

## 15. Next decisive calculation

The next useful quantity is the **wavelength-resolved electrical response**:

```math
H(\omega;E_\gamma)
=
\int dx\,
p(x|E_\gamma,{\rm abs})
H_{\rm carrier}(\omega|x).
```

Before adding a calibrated transport solver, the cold ballistic Kane trajectory can be used as the analytic baseline.

This will tell us whether a graded absorber can produce a spectrally dependent response time in which near-cutoff photons are intrinsically generated closer to collection while shorter-wavelength photons traverse more of the gradient.
