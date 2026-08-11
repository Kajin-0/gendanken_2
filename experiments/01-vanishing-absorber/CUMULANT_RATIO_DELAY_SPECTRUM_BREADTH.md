# Cumulant Ratios as a Direct Measure of Random Delay-Scale Breadth

**Date:** 2026-08-10  
**Status:** exact moment-theory interpretation inside the homogeneous regenerative timing class; no novelty claim for moment mathematics

## 1. Why the cumulant ratios matter physically

The regenerative first-passage theorem gave

```math
\kappa_n(d)
=d\int_0^\infty t^n\nu(dt),
\qquad n\ge2,
```

where `nu(dt)` is the positive per-unit-distance Lévy delay spectrum.

Define the adjacent cumulant ratio

```math
\boxed{
R_n
=
\frac{
\kappa_{n+1}\kappa_{n-1}
}{
\kappa_n^2
},
\qquad n\ge2.
}
\tag{1}
```

The previous Hankel-positivity result gave only

```math
R_n\ge1.
```

But `R_n` has a more direct meaning.

---

## 2. Moment-tilted delay spectrum

Write

```math
m_k=\int_0^\infty t^k\nu(dt).
```

For `n>=2`, define the normalized positive measure

```math
\boxed{
P_{n-1}(dt)
=
\frac{t^{n-1}\nu(dt)}{m_{n-1}}.
}
\tag{2}
```

Under this tilted measure,

```math
E_{n-1}[t]
=\frac{m_n}{m_{n-1}},
```

and

```math
E_{n-1}[t^2]
=\frac{m_{n+1}}{m_{n-1}}.
```

Therefore

```math
\begin{aligned}
R_n
&=\frac{m_{n+1}m_{n-1}}{m_n^2}\\
&=\frac{E_{n-1}[t^2]}{E_{n-1}[t]^2}.
\end{aligned}
```

Hence exactly

```math
\boxed{
R_n
=1+CV_{n-1}^2,
}
\tag{3}
```

where `CV_{n-1}` is the coefficient of variation of delay scale `t` under the moment-tilted spectrum Eq. (2).

Thus `R_n-1` is literally a **dimensionless breadth of the random delay spectrum**.

---

## 3. The experimentally useful `n=3` ratio

For

```math
n=3,
```

```math
R_3
=
\frac{\kappa_4\kappa_2}{\kappa_3^2}.
```

Using standardized timing skewness

```math
\gamma_1
=\kappa_3/\kappa_2^{3/2}
```

and excess kurtosis

```math
\gamma_2
=\kappa_4/\kappa_2^2,
```

```math
\boxed{
R_3
=\frac{\gamma_2}{\gamma_1^2}.
}
\tag{4}
```

Therefore

```math
\boxed{
\frac{\text{excess kurtosis}}
{(\text{skewness})^2}
-1
}
```

is the squared coefficient of variation of the delay scale under the `t^2 nu(t)`-weighted spectrum.

This gives the ratio a direct stochastic meaning.

---

## 4. One single random waiting-time scale

Suppose random timing increments occur at one fixed delay size `tau`,

```math
\nu(dt)=\lambda\delta(t-\tau)dt.
```

Then every moment-weighted distribution is still a point mass at `tau`.

Therefore

```math
CV_{n-1}=0
```

and

```math
\boxed{R_n=1.}
\tag{5}
```

This saturates the general regenerative lower bound.

---

## 5. Exponential random waits

For Poisson waiting events whose individual wait time is exponential,

```math
\nu(t)=\lambda\beta e^{-\beta t},
```

```math
m_n
=\lambda\frac{n!}{\beta^n}.
```

Therefore

```math
\boxed{
R_n
=\frac{n+1}{n}.
}
\tag{6}
```

In particular

```math
\boxed{
R_3=\frac43.
}
\tag{7}
```

So a pure regenerative Poisson-exponential waiting process has

```math
\boxed{
\text{excess kurtosis}
=\frac43(\text{skewness})^2.
}
```

---

## 6. Uniform drift-diffusion first passage

For the inverse-Gaussian drift-diffusion Lévy spectrum,

```math
R_n
=\frac{2n-1}{2n-3}.
```

Thus

```math
\boxed{
R_3=\frac53.
}
\tag{8}
```

or

```math
\boxed{
\text{excess kurtosis}
=\frac53(\text{skewness})^2.
}
```

Compared with exponential waits, the `t^2`-weighted drift-diffusion delay spectrum has a larger relative breadth:

```text
exponential waiting spectrum:
CV_tilted^2 = 1/3

inverse-Gaussian drift-diffusion spectrum:
CV_tilted^2 = 2/3.
```

---

## 7. Multiple separated delay scales can produce very large ratios

If `nu(t)` contains substantial weight at widely separated time scales, the tilted coefficient of variation can become large.

For example a two-scale discrete spectrum

```math
\nu
\propto
\delta(t-t_1)+\delta(t-t_2)
```

with

```math
t_2\gg t_1
```

can yield

```math
R_3\gg1.
```

Thus a very large measured

```math
\gamma_2/\gamma_1^2
```

is a natural signature of **broad or multi-scale random delay structure** within the regenerative class.

It does not by itself identify whether the scales arise from traps, energy relaxation, multiple scattering regimes, or another process.

---

## 8. A model-selection interpretation

The timing ratio can therefore be read as

```text
R3 ~1
-> narrowly concentrated random delay scale

R3 = 4/3
-> pure exponential-wait compound-Poisson benchmark

R3 = 5/3
-> ideal uniform drift-diffusion benchmark

R3 >>1
-> broad/multiscale delay spectrum candidate.
```

These benchmark values are **not exclusive mechanism labels**.

Different Lévy spectra can share the same low-order ratio.

The full RF exponent or higher `R_n` values are needed for stronger identification.

---

## 9. Full ratio sequence is a scale-breadth spectrum

For every `n`,

```math
R_n-1
=CV_{n-1}^2.
```

Increasing `n` tilts the positive Lévy spectrum more strongly toward longer delays.

Therefore the sequence

```math
\boxed{
R_2,R_3,R_4,\ldots
}
```

acts as a hierarchy of **delay-scale breadth measurements at progressively stronger long-time weighting**.

For exponential waits,

```math
R_n-1=1/n.
```

For drift-diffusion,

```math
R_n-1=\frac{2}{2n-3}.
```

Different transport mechanisms therefore predict different full ratio sequences even when one low-order ratio happens to agree.

---

## 10. RF access

The required cumulants are derivatives of

```math
\ln H(\omega)
```

at zero RF.

Thus the ratio sequence is, in principle, extractable from complex RF amplitude/phase without direct single-carrier timing.

In practice high-order derivatives become rapidly noise sensitive.

A realistic first experiment would likely use only

```text
R2 = kappa3*kappa1/kappa2^2
and
R3 = kappa4*kappa2/kappa3^2
```

if the RF SNR/bandwidth supports the fourth cumulant.

---

## 11. Numerical regression

`numerics/cumulant_ratio_delay_spectrum_breadth.py`

verifies:

```text
fixed waiting time -> R_n=1
exponential waits -> R_n=(n+1)/n
drift-diffusion -> R_n=(2n-1)/(2n-3)
```

for several orders.

It also verifies directly on a multiscale discrete positive spectrum that

```math
R_n=1+CV_{tilted}^2.
```

---

## 12. Mathematical prior-art boundary

This is an elementary consequence of positive moment measures and therefore not new moment theory.

The candidate detector insight is the physical interpretation:

> **dimensionless transit-time cumulant ratios measure the breadth of the per-distance stochastic delay spectrum required by the carrier dynamics.**

This gives a route from measured RF timing shape to mechanism-neutral statements about whether transport is single-scale, drift-diffusive, or broadly multiscale before fitting a microscopic model.
