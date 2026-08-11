# Hot-Carrier Two-State Closure — Thermalization as a Spatial Mode

**Date:** 2026-08-11  
**Status:** **DERIVED / CHECKED / CONDITIONAL**; direct response to the remaining initial-state/thermalization concern in adversarial review; no novelty claim

## 1. Question

Changing wavelength can change more than generation depth. A carrier may begin in a high-energy or otherwise non-equilibrated internal state and then relax while it propagates.

The relevant question for the spectral-depth hierarchy is therefore:

> **Does finite thermalization destroy the spatial closure construction, or does it appear as another resolvable spatial mode?**

A minimal two-state model gives an exact answer.

---

## 2. Minimal deterministic hot -> cold model

Let `d` be distance to the collector.

A cold carrier moves toward the collector at constant velocity `v_c`.

A hot carrier moves at constant velocity `v_h` and relaxes irreversibly to the cold state at rate

```math
\rho=1/\tau_h.
```

Use a uniform planar weighting field and Laplace/RF variable `s`.

The cold-state expected raw induced-current transform obeys

```math
v_c J_c'(d)+sJ_c(d)=v_c,
\qquad
J_c(0)=0,
```

so

```math
\boxed{
J_c(d,s)
=\frac{v_c}{s}
\left(1-e^{-\lambda_c d}\right),
\qquad
\lambda_c=\frac{s}{v_c}.
}
\tag{1}
```

The hot-state transform obeys

```math
v_hJ_h'(d)+(s+\rho)J_h(d)-\rho J_c(d)=v_h,
\qquad
J_h(0)=0.
```

Its exact solution can be written

```math
\boxed{
J_h(d,s)
=A(s)+B_c(s)e^{-\lambda_c d}
+B_h(s)e^{-\lambda_h d},
}
\tag{2}
```

with

```math
\boxed{
\lambda_h=\frac{s+\rho}{v_h}
}
\tag{3}
```

and

```math
A=
\frac{s v_h+\rho v_c}
{s(s+\rho)},
```

```math
B_c
=-\frac{\rho v_c^2}
{s\,[v_c(s+\rho)-s v_h]},
```

```math
B_h=-A-B_c.
```

The removable repeated-root case is obtained by continuity when `lambda_h=lambda_c`.

---

## 3. Thermalization length

At RF, `s=i omega`. The hot exponent has

```math
\Re\lambda_h=\rho/v_h.
```

Therefore the memory of the initial hot state decays over the exact spatial scale

```math
\boxed{
\ell_h=\frac{v_h}{\rho}=v_h\tau_h.
}
\tag{4}
```

This is the natural dimensionless control for the spectral-depth experiment.

If

```text
ell_h << distance to collector,
```

the hot initial condition is forgotten before collection and the cold mode dominates.

If

```text
ell_h ~ sampled internal distances,
```

the second spatial mode can be visible.

---

## 4. Wavelength-independent initialization gives exact rank two

Suppose a fraction `f` of generated carriers begins in the hot state and `1-f` begins cold, with the **same `f` for every spectral channel**.

Then

```math
J_f(d,s)
=(1-f)J_c+fJ_h
```

has the form

```math
\boxed{
J_f(d,s)
=A_f(s)
+C_f(s)e^{-\lambda_c d}
+H_f(s)e^{-\lambda_h d}.
}
\tag{5}
```

Thus raw current contains one depth-independent particular term plus **two spatial exponentials**.

For equally spaced internal coordinates, first differences contain exactly two exponential modes.

Therefore:

```math
\boxed{
\text{constant hot-state initialization}
\Longrightarrow
\text{six-color rank-two closure exactly.}
}
\tag{6}
```

Finite thermalization is therefore not, by itself, an uncontrolled breakdown of the spectral-depth hierarchy.

It promotes the model order from one to two.

---

## 5. What actually breaks fixed-rank closure

Let the hot fraction depend on wavelength/channel:

```math
f_m=f_0+\delta f_m.
```

Then

```math
J_m
=J_{f_0}(d_m)
+\delta f_m
\left[J_h(d_m)-J_c(d_m)\right].
\tag{7}
```

The first term is an exact two-mode sequence.

The second has a channel-dependent coefficient. Unless `delta f_m` itself has a special finite-exponential structure, the fixed-coefficient rank-two closure is generically broken.

Therefore the relevant initial-state requirement is not

```text
no thermalization,
```

but rather

```text
initial internal-state distribution sufficiently invariant across the spectral channels,
```

or explicitly modeled.

---

## 6. Connection to the graded-gap excess-energy theorem

For an ideal linearly graded gap

```math
E_g(z)=E_{g0}-Gz
```

with absorption depending only on total local photon excess energy

```math
u=E_gamma-E_g(z),
```

the generation distribution in `nu` is wavelength-independent.

Thus any initial-state probability that depends only on `nu`, for example

```math
f=f(\nu),
```

has the same generated distribution at all wavelengths in that ideal limit.

The hot-state amplitude is then wavelength-independent and the two-state thermalization process remains exact rank two.

This gives the excess-energy invariance theorem a precise role:

> **it protects the fixed spatial model order against wavelength-dependent initialization.**

It is a sufficient protection, not a fundamental requirement of the spectral-depth method.

---

## 7. Current HgCdTe quartet: excess-energy variation is small

For the current Hansen/Moazzami quartet with mean generation depths

```text
2.5, 3.0, 3.5, 4.0 um,
```

the generation-weighted mean total excess energies are approximately

```text
52.3532 meV
52.4276 meV
52.4782 meV
52.4726 meV.
```

Peak-to-peak variation is only

```math
\boxed{\Delta \bar E_{ex}\simeq0.125\ \mathrm{meV}.}
\tag{8}
```

The standard deviation changes only from about

```text
33.235 -> 32.694 meV.
```

This does not prove microscopic hot-state invariance, but it shows that the current quartet is close to the ideal translated-excess-energy construction in its first two moments.

---

## 8. Quantitative two-state stress

Use a deliberately strong generic stress tied to the current HgCdTe velocity scale:

```text
v_c = 3.45e4 m/s
v_h = 6.90e4 m/s
f0 = 0.5
RF = 100 MHz
quartet z = 2.5,3.0,3.5,4.0 um
L = 7.6 um.
```

Vary the thermalization length `ell_h`.

For wavelength-independent `f0`, the one-mode four-color phase closure is approximately

| `ell_h` | four-color phase |
|---:|---:|
| `0.25 um` | `~1e-8 deg` |
| `0.50 um` | `+0.0000246 deg` |
| `1.0 um` | `+0.000868 deg` |
| `2.0 um` | `+0.00373 deg` |
| `5.0 um` | `+0.00547 deg` |
| `10 um` | `+0.00423 deg` |

Thus a long-lived internal state can produce a four-color failure of the same order as the current transport-gradient target.

But this failure is generated by an exact second spatial mode and therefore belongs on the six-color branch of the hierarchy.

---

## 9. Wavelength-dependent initialization tolerance

Parameterize a local dependence of hot fraction on the generation-weighted mean excess energy,

```math
f_m
=f_0
+g_E
(\bar E_m-\langle\bar E\rangle),
```

where `g_E=df/dE` is used only as a sensitivity coordinate.

Using the actual four HgCdTe excess-energy means above, require the wavelength-dependent initialization contribution to the 100-MHz closure to remain below 10% of the current gradient-sensitive target

```text
0.1 x 0.01198 deg.
```

For the generic two-state stress, the corresponding allowed peak-to-peak variation in initial hot fraction is approximately

| `ell_h` | allowed `Delta f` across quartet for 10% contamination |
|---:|---:|
| `0.25 um` | `~0.78 %` |
| `0.50 um` | `~0.44 %` |
| `1.0 um` | `~0.29 %` |
| `2.0 um` | `~0.25 %` |
| `5.0 um` | `~0.29 %` |
| `10 um` | `~0.38 %` |

These are **conditional sensitivity numbers**, not HgCdTe thermalization measurements.

They show the scale at which wavelength-dependent initialization would become material for the present very small four-color target.

---

## 10. Important interpretation rule

A second thermalization mode can produce a detectable one-mode closure failure before the six-color second-mode minor reaches high significance at the same measurement precision.

Therefore the correct logic is

```text
four-color closure fails
-> test six-color second-mode witness

if second-mode witness significant
-> recover/test two-state or other rank-two roots

if second-mode witness not significant
-> mechanism remains unresolved at present SNR
```

and **not**

```text
four-color closure fails
-> therefore velocity gradient.
```

The hierarchy is conservative by design.

---

## 11. Scientific disposition

The initial-state objection does not invalidate the paper core.

It adds a precise boundary:

```text
wavelength-independent finite thermalization
-> extra spatial mode, handled by six colors

wavelength-dependent initialization
-> source-state systematic that must be bounded or modeled.
```

For the current graded-HgCdTe quartet, the optical model nearly preserves the excess-energy distribution, which suppresses the most obvious route to wavelength-dependent initialization.

The remaining uncertainty is microscopic: how sensitive the relevant hot-state populations are to the residual sub-meV differences in the generated excess-energy distribution.

That is a material-specific question and should not be converted into an unsupported universal claim.
