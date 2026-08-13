# Time-Tagged Semiconductor Point-Process Decision — Experiment 02

**Date:** 2026-08-12  
**Status:** new conditional refinement; exact likelihood process + strong-dark asymptote  
**Priority:** requires direct prior-art audit before novelty language

The previous thickness models used a binary `click / no click` coarse graining over a gate. This file retains the complete set of detection timestamps.

The purpose is to test whether the earlier geometry–transport–dark-event feasibility scaling survives when the observer uses strictly more information.

It largely does in the strong-dark/thin-device limit.

---

## 1. Geometry and signal-event density

Use the same one-dimensional slab:

```text
z=0       illuminated surface
z=L       collecting boundary
```

Parameters:

```text
alpha = optical absorption coefficient
beta  = inverse carrier-survival length
v     = effective carrier transport speed
eta_0 = thickness-independent transduction/readout prefactor
```

A photon absorbed at depth `z` has useful-event weight

```math
\eta_0\alpha e^{-\alpha z}
e^{-\beta(L-z)}dz.
```

Assume a surviving signal generated at `z` reaches the output after

```math
\boxed{
t=\frac{L-z}{v}.}
```

Thus

```math
z=L-vt,
\qquad
0\le t\le T,
\qquad
T=\frac Lv.
```

The **unnormalized signal-event time density** is therefore

```math
\boxed{
q_L(t)
=\eta_0\alpha v
e^{-\alpha L}
e^{(\alpha-\beta)vt},
\qquad 0\le t\le L/v.
}
```

Its integral is the useful signal-event probability

```math
\int_0^{L/v}q_L(t)dt
=\eta_s(L),
```

with

```math
\eta_s(L)
=\eta_0\frac{\alpha}{\alpha-\beta}
(e^{-\beta L}-e^{-\alpha L})
```

for `alpha != beta`.

---

## 2. Dark process

Assume homogeneous independent dark events with rate density `r_d` per active volume.

For detector area `A` and thickness `L`, the dark timestamp process is homogeneous Poisson with rate

```math
\boxed{
\lambda_d(L)=r_dAL.
}
```

Over the transport gate

```math
T=L/v,
```

the mean number of dark events is

```math
\boxed{
\mu(L)
=\lambda_dT
=\frac{r_dA}{v}L^2
=\zeta L^2,
}
```

where

```math
\boxed{
\zeta=\frac{r_dA}{v}.}
```

---

## 3. Full output under H0 and H1

Let the observed output be the entire finite set of timestamps

```math
Y=\{t_1,\ldots,t_N\}.
```

Under

```text
H0: no incident photon,
```

`Y` is simply the homogeneous Poisson dark process.

Under

```text
H1: one incident photon,
```

the output is

```text
same Poisson dark process
+
at most one independent signal point
```

with unnormalized time density `q_L(t)`.

Equivalently,

```math
P_1
=(1-\eta_s)P_0
+\eta_s Q,
```

where `Q` is the distribution obtained by taking a dark-process realization and adding one signal point drawn from normalized density

```math
f_L(t)=q_L(t)/\eta_s(L).
```

This mixture structure is exact inside the model.

---

## 4. Exact likelihood ratio

For a Poisson background with positive constant rate `lambda_d`, adding one independent point with density `f_L` gives the Radon-Nikodym derivative

```math
\frac{dQ}{dP_0}(Y)
=\sum_{t_i\in Y}
\frac{f_L(t_i)}{\lambda_d}.
```

Therefore

```math
\boxed{
\Lambda(Y)
\equiv
\frac{dP_1}{dP_0}(Y)
=1-\eta_s(L)
+
\sum_{t_i\in Y}
\frac{q_L(t_i)}{\lambda_d(L)}.
}
```

For equal priors, the optimum decision is

```text
choose H1 if Lambda(Y) > 1.
```

Thus the sufficient statistic is a weighted sum over all observed timestamps:

```math
\boxed{
S(Y)
=\sum_{t_i\in Y}q_L(t_i).
}
```

A dark click occurring at a time where the expected signal density is high carries more evidence than one at a low-signal time.

This information is lost by binary `any click / no click` readout.

---

## 5. Exact total-variation factorization

Because

```math
P_1=(1-\eta_s)P_0+\eta_s Q,
```

we have

```math
P_1-P_0
=\eta_s(Q-P_0).
```

Therefore

```math
\boxed{
\mathcal D_{\rm full}(L)
=\eta_s(L)
\operatorname{TV}(Q,P_0).
}
```

This gives a clean cross-layer separation:

```text
eta_s(L)
= probability the photon creates a useful signal event;

TV(Q,P0)
= how distinguishable that extra event is from the dark point process.
```

The first factor is transduction/transport physics.
The second is readout/statistical-background physics.

---

## 6. Exact general bounds

Because total variation is at most one,

```math
\boxed{
\mathcal D_{\rm full}(L)
\le\eta_s(L).
}
```

Thus even perfect timestamp processing cannot overcome failure to create a useful signal event.

Now coarse-grain the full timestamp set to

```text
no events / at least one event.
```

The corresponding Bernoulli distinguishability is

```math
\mathcal D_{\rm binary}(L)
=\eta_s(L)e^{-\mu(L)}.
```

Data processing cannot increase distinguishability, so

```math
\boxed{
\eta_s(L)e^{-\mu(L)}
\le
\mathcal D_{\rm full}(L)
\le
\eta_s(L).
}
```

This exactly locates the earlier binary model as a conservative coarse graining.

---

## 7. Exact chi-square divergence

Under `P0`, define

```math
Z(Y)
=\sum_{t_i\in Y}
\frac{q_L(t_i)}{\lambda_d}.
```

Poisson-point-process identities give

```math
E_0[Z]=\eta_s.
```

Hence

```math
\chi^2(P_1\|P_0)
=E_0[(\Lambda-1)^2]
=\operatorname{Var}_0(Z).
```

For a Poisson process,

```math
\boxed{
\chi^2(P_1\|P_0)
=
\int_0^{L/v}
\frac{q_L^2(t)}{\lambda_d(L)}dt.
}
```

For `alpha != beta`, substitution gives

```math
\boxed{
\chi^2(P_1\|P_0)
=\frac{
\eta_0^2\alpha^2v
}{
2r_dAL(\alpha-\beta)
}
\left(
e^{-2\beta L}-e^{-2\alpha L}
\right).
}
```

For `alpha=beta`, the continuous limit is

```math
\boxed{
\chi^2(P_1\|P_0)
=
\frac{\eta_0^2\alpha^2v}{r_dA}
e^{-2\alpha L}.
}
```

Consequently,

```math
\mathcal D_{\rm full}
\le\frac12\sqrt{\chi^2(P_1\|P_0)}
```

provides another decision-feasibility upper bound.

---

## 8. Special case alpha = beta: signal timestamps are uniform

When

```math
\alpha=\beta,
```

```math
q_L(t)
=\eta_0\alpha v e^{-\alpha L}
```

is constant throughout the gate.

Thus a signal timestamp has the same uniform temporal distribution as a homogeneous dark timestamp.

In this special case, the actual times contain no extra information beyond the **total event count** `N`.

The useful signal probability is

```math
\eta_s(L)
=\eta_0\alpha L e^{-\alpha L}.
```

The dark count is

```math
N_0\sim\operatorname{Poisson}(\mu),
\qquad
\mu=\zeta L^2.
```

Conditional on a useful signal event,

```math
N_1=N_0+1.
```

---

## 9. Exact total variation for the shifted-Poisson problem

Let

```math
p_n=e^{-\mu}\frac{\mu^n}{n!}.
```

The total variation between

```text
Poisson(mu)
```

and

```text
1 + Poisson(mu)
```

is

```math
\frac12\sum_{n=0}^{\infty}|p_n-p_{n-1}|,
```

with `p_{-1}=0`.

Because the Poisson pmf is unimodal, the telescoping rise/fall gives

```math
\boxed{
\operatorname{TV}[
\operatorname{Poisson}(\mu),
1+\operatorname{Poisson}(\mu)
]
=p_{\max}(\mu),
}
```

where

```math
p_{\max}(\mu)
=\max_n e^{-\mu}\mu^n/n!.
```

Therefore

```math
\boxed{
\mathcal D_{\rm full}(L)
=\eta_s(L)p_{\max}[\mu(L)]
}
```

for `alpha=beta`.

This is an exact full-output decision result in the stated model.

---

## 10. Low-dark regime: binary click/no-click is already optimal

For

```math
0\le\mu<1,
```

the Poisson mode is `n=0`, so

```math
p_{\max}=e^{-\mu}.
```

Therefore

```math
\boxed{
\mathcal D_{\rm full}
=\eta_s e^{-\mu}
=\mathcal D_{\rm binary}
\qquad (\mu<1,\ \alpha=\beta).
}
```

Thus when the expected dark count is below one and signal/dark timestamps have the same shape, no count/timestamp processing can improve on the simple binary readout for total-variation discrimination.

---

## 11. Higher-dark regime: count resolution becomes valuable

For larger `mu`,

```math
p_{\max}(\mu)
\sim\frac1{\sqrt{2\pi\mu}}
```

by the local Gaussian/Stirling approximation.

Hence

```math
\mathcal D_{\rm full}
\sim
\frac{\eta_s}{\sqrt{2\pi\mu}}.
```

In contrast, binary click/no-click gives

```math
\mathcal D_{\rm binary}
=\eta_s e^{-\mu}.
```

So at high dark count, retaining count information changes the penalty from exponential to algebraic.

This is a concrete example of the general Experiment-02 principle:

```text
coarse readout can destroy detector information that remains present in the full output process.
```

---

## 12. Strong-dark/thin-device scaling with full output

Now take the regime

```math
\zeta\gg\alpha^2,\beta^2
```

so the optimum thickness scales as

```math
L=\frac{x}{\sqrt\zeta}.
```

Then

```math
\alpha L\ll1,
\qquad
\beta L\ll1,
```

and the signal-event density becomes approximately uniform in time regardless of the finite difference `alpha-beta`.

To leading order,

```math
\eta_s(L)
\sim
\eta_0\alpha L
=
\frac{\eta_0\alpha x}{\sqrt\zeta},
```

while

```math
\mu=\zeta L^2=x^2.
```

Therefore the **full** point-process distinguishability obeys

```math
\boxed{
\mathcal D_{\rm full}
\sim
\frac{\eta_0\alpha}{\sqrt\zeta}
\,x\,p_{\max}(x^2).
}
```

The strong-dark optimization has therefore reduced to a universal one-variable count problem.

---

## 13. The leading optimum occurs at mean dark count mu = 1/2

For `0<=mu<1`,

```math
p_{\max}=e^{-\mu}.
```

Define

```math
g(\mu)=\sqrt\mu\,p_{\max}(\mu).
```

On the first interval,

```math
g(\mu)=\sqrt\mu e^{-\mu},
```

which is maximized at

```math
\boxed{\mu_*=1/2.}
```

with

```math
\boxed{
g_{\max}=1/\sqrt{2e}.}
```

For the subsequent Poisson-mode intervals, direct piecewise evaluation gives smaller maxima, approaching `1/sqrt(2pi)` asymptotically.

Thus the global leading strong-dark optimum is

```math
\boxed{
\mu_*=1/2,
\qquad
x_*=1/\sqrt2.
}
```

and hence

```math
\boxed{
L_*
\sim
\frac1{\sqrt{2\zeta}}
=
\sqrt{\frac{v}{2r_dA}}.
}
```

This is exactly the thickness scale obtained from the earlier binary coarse-grained model.

---

## 14. Strong-dark maximum distinguishability survives full time-tag processing

At the leading optimum,

```math
\boxed{
\mathcal D_{\max}^{\rm full}
\sim
\frac{\eta_0\alpha}
{\sqrt{2e\zeta}}
=
\eta_0\alpha
\sqrt{
\frac{v}{2e\,r_dA}
}.
}
```

Therefore the earlier strong-dark feasibility scaling was **not an artifact of binary click/no-click readout**.

The reason is physically transparent:

```text
the optimum itself occurs at mu=1/2 < 1,
```

where binary readout is already sufficient in the leading uniform-time limit.

This is the strongest robustness result of the semiconductor-thickness branch so far.

---

## 15. Decision-feasibility asymptote

For required

```math
D_{\rm req}=1-2\epsilon,
```

the full-output strong-dark asymptote gives

```math
\boxed{
\frac{r_dA}{v}
\lesssim
\frac{\eta_0^2\alpha^2}
{2eD_{\rm req}^2}.
}
```

Equivalently,

```math
\boxed{
v
\gtrsim
\frac{2e\,r_dA\,D_{\rm req}^2}
{\eta_0^2\alpha^2}.
}
```

Within the asymptotic model, this leading condition survives access to the complete timestamp/count record.

---

## 16. What has changed relative to the earlier binary model

### General regime

Full time-tag/count processing can outperform binary click/no-click, sometimes dramatically.

### Strong dark-time optimum

The leading optimum moves into a regime with mean dark count `1/2`, where binary readout is already sufficient to leading order.

Therefore the strong-dark scaling survives.

This is exactly the kind of adversarial robustness test Experiment 02 requires:

```text
upgrade the observer;
see whether the apparent bound disappears;
retain it only if the stronger observer cannot remove the leading limitation.
```

---

## 17. Mandatory caveats

- One-dimensional slab.
- Constant absorption coefficient and exponential survival model.
- Deterministic drift arrival time `(L-z)/v` for a surviving event.
- Homogeneous independent Poisson dark timestamps.
- At most one signal timestamp.
- No signal timing jitter beyond absorption depth.
- No detector dead time, afterpulsing, gain statistics, or dark-rate modulation by the optical event.
- Full exact TV for `alpha != beta` is not given in elementary closed form.
- The strong-dark result uses the thin-device uniform-time limit.

---

## 18. Current status

**DERIVED / CONDITIONAL / ROBUST TO FULL TIME-TAG READOUT IN THE STRONG-DARK ASYMPTOTE / PRIORITY UNASSESSED.**

This is now the strongest narrow candidate result in Experiment 02:

```math
\boxed{
\mathcal D_{\max}
\sim
\eta_0\alpha
\sqrt{
\frac{v}{2e\,r_dA}
},
\qquad
\mu_*\to1/2.
}
```

It directly couples optics, transport, geometry, dark statistics, and binary decision performance, and survives replacement of the binary coarse-grained observer by the complete point-process observer at leading order.

The next step is a focused prior-art audit of this exact strong-dark point-process scaling before expanding the physical model further.
