# Supplementary Material — Spectral-Depth Closure Tests for Photocarrier Transport

**Date:** 2026-08-11  
**Status:** working supplement to `MANUSCRIPT_DRAFT.md` / `MANUSCRIPT_DRAFT.tex`; theorem proofs and reviewer-facing assumptions only; priority claims remain explicitly unresolved

This supplement collects derivations that are useful for verification but would obscure the conceptual spine of the main paper. The main text should remain organized around three gedanken experiments:

1. four colors test one Shockley-Ramo spatial mode;
2. DC + one RF identify the homogeneous drift-diffusion-recombination law, while the next RF falsifies it;
3. six colors test whether a resolved second spatial mode is sufficient and whether its RF roots match ordinary boundary or two-carrier physics.

The supplement does **not** broaden the headline claim set.

---

# S1. Exact first-passage spatial semigroup

Let `X_t` be a scalar spatially homogeneous continuous-path strong-Markov process, and let

```math
\tau_d=\inf\{t\ge0:X_t=d\}
```

be first passage over distance `d>0`. Allow independent homogeneous killing with killing time `\zeta`, and define

```math
U_s(d)=E[e^{-s\tau_d}\,1_{\tau_d<\zeta}].
```

For positive `a,b`, any successful continuous path to `a+b` must first hit `a`. Applying the strong-Markov property at `\tau_a`, followed by spatial translation invariance, gives

```math
U_s(a+b)=U_s(a)U_s(b).
```

With `U_s(0)=1` and continuity in `d`, the multiplicative Cauchy equation gives

```math
\boxed{U_s(d)=e^{-\gamma(s)d}.}
```

This exponential spatial law is therefore more general than drift-diffusion. Uniform drift-diffusion adds the specific dispersion relation

```math
\boxed{D\gamma^2+w\gamma=\kappa+s.}
```

The distinction matters throughout the paper: spatial rank/model order is tested before a specific RF dispersion law is imposed.

---

# S2. Shockley-Ramo terminal current is a survival observable

Consider a one-dimensional planar detector with uniform weighting field `E_w`. Let `p(x,t)` be the probability density of a surviving signal carrier, with current density

```math
j(x,t)=w p-D\,\partial_x p,
```

and continuity equation

```math
\partial_t p=-\partial_x j.
```

Take an absorbing collector at `x=L` and a remote upstream boundary. The ensemble Shockley-Ramo current is

```math
I(t)=qE_w\int_{-\infty}^{L}j(x,t)\,dx.
```

For the minimal homogeneous geometry, `p` vanishes at both integration endpoints, so the diffusion boundary contribution cancels:

```math
\int j\,dx
=w\int p\,dx.
```

Define the first-passage survival probability

```math
S(t)=P(T>t)=\int p(x,t)\,dx.
```

Then

```math
\boxed{I(t)=qE_w w S(t).}
```

For no killing,

```math
\widetilde S(s)=\frac{1-U(d,s)}{s},
```

hence

```math
J(d,s)=qE_ww\frac{1-U(d,s)}{s}.
```

With independent uniform Markov killing, the same spatial dependence survives and only the depth-independent prefactor changes. Therefore

```math
\boxed{J(d,s)=C(s)[1-e^{-\gamma(s)d}].}
```

This proves why the raw terminal current contains a constant spatial particular term plus one exponential mode, whereas the arrival flux itself is purely exponential.

A deterministic carrier gives the simplest sanity check. Arrival at time `T=d/w` has transform `e^{-sT}`, while the induced current is a rectangular pulse of duration `T` and transform proportional to `[1-e^{-sT}]/s`.

---

# S3. Four-color closure and rigid finite-width optical kernels

Choose four equally spaced internal source coordinates

```math
d_m=d_0+mh,\qquad m=0,1,2,3.
```

The homogeneous raw-current sequence is

```math
J_m=A+Bq^m,\qquad q=e^{-\gamma h}.
```

First differences are

```math
\Delta J_m=J_{m+1}-J_m=B(q-1)q^m.
```

Therefore

```math
\boxed{(J_2-J_1)^2=(J_1-J_0)(J_3-J_2).}
```

Three coordinates determine

```math
q=\frac{J_2-J_1}{J_1-J_0},
```

and the fourth is a true null measurement because it introduces no parameter.

## S3.1 Common electrical-chain invariance

If

```math
J_m^{meas}=G(\omega)J_m+C(\omega)
```

with the same complex `G,C` for all four colors at one RF frequency, first differencing removes `C` and multiplies all differences by `G`. The four-color closure is unchanged.

## S3.2 Rigid finite-width kernel

Let the point-source coordinate be distributed as one translated shape

```math
p_m(d)=g(d-d_m).
```

Averaging the exponential part gives

```math
\int g(d-d_m)e^{-\gamma d}\,dd
=e^{-\gamma d_m}\int g(u)e^{-\gamma u}\,du.
```

The source width and asymmetry therefore renormalize only `B`; the sequence remains `A+\widetilde Bq^m`. Finite source width alone is not a structural resolution loss.

## S3.3 Affine depth calibration

If true depth and calibrated spectral coordinate obey

```math
z=a+b\mu,
```

then equal spacing in `\mu` remains equal spacing in `z`. Thus the model-order null needs no absolute depth origin and no absolute depth scale. The physical scale `b` is required only when converting the recovered multiplier to dimensional `\gamma,D,w,\kappa`.

---

# S4. Exact DC + RF inversion of homogeneous drift-diffusion-recombination

Uniform transport obeys

```math
D\gamma^2+w\gamma=\kappa+s.
```

At DC let

```math
g_0=\gamma(0),
```

and at RF

```math
g_\omega=\gamma(i\omega).
```

Then

```math
Dg_0^2+wg_0=\kappa,
```

```math
Dg_\omega^2+wg_\omega=\kappa+i\omega.
```

Subtracting eliminates recombination:

```math
D A+w B=i\omega,
```

where

```math
A=g_\omega^2-g_0^2,
\qquad
B=g_\omega-g_0.
```

Because `D,w` are real, the real and imaginary parts form a `2x2` real system. Define

```math
\Delta=\Re A\,\Im B-\Im A\,\Re B.
```

For `\Delta\ne0`, Cramer's rule gives

```math
\boxed{D=-\frac{\omega\Re B}{\Delta},}
```

```math
\boxed{w=\frac{\omega\Re A}{\Delta},}
```

and then

```math
\boxed{\kappa=Dg_0^2+wg_0.}
```

Thus one DC spatial exponent plus one complex RF exponent determine the complete homogeneous three-parameter Markov model. Every additional RF frequency is an overdetermined falsification point.

## S4.1 No-recombination algebra

When `\kappa=0`, write

```math
\gamma=a+ib.
```

Separating

```math
D(a+ib)^2+w(a+ib)=i\omega
```

gives

```math
D(a^2-b^2)+wa=0,
```

```math
2Dab+wb=\omega.
```

Solving yields

```math
\boxed{D=\frac{\omega a}{b(a^2+b^2)},}
```

```math
\boxed{w=\frac{\omega(b^2-a^2)}{b(a^2+b^2)}.}
```

For positive downstream drift and the adopted branch, `0<a<b`.

---

# S5. Six-color rank-two closure and mode-resolution boundary

Suppose five first differences from six source coordinates have two modes:

```math
d_m=a q_1^m+b q_2^m,\qquad m=0,\ldots,4.
```

Define the adjacent Hankel minor

```math
W_m=d_md_{m+2}-d_{m+1}^2.
```

Direct expansion gives

```math
\boxed{W_m=ab(q_1q_2)^m(q_1-q_2)^2.}
```

Therefore

```math
\boxed{W_1^2=W_0W_2}
```

for an exact rank-two sequence, while

```math
\frac{W_{m+1}}{W_m}=q_1q_2.
```

The second-order recurrence

```math
d_{m+2}=S d_{m+1}-P d_m
```

then has

```math
S=q_1+q_2,
\qquad
P=q_1q_2.
```

The same identity exposes the mode-resolution boundary. A second mode becomes unobservable when either `a` or `b` vanishes, or as `q_1->q_2`; the witness collapses quadratically in the root separation.

## S5.1 Noise on the second-mode witness

For

```math
W_0=d_0d_2-d_1^2
```

and independent circular complex current errors `\epsilon_m`, linearization gives

```math
\delta W_0
=-d_2\epsilon_0
+(d_2+2d_1)\epsilon_1
-(d_0+2d_1)\epsilon_2
+d_0\epsilon_3.
```

Hence

```math
\boxed{
\sigma_{W_0}^2
=\sigma_J^2[
|d_2|^2+|d_2+2d_1|^2+|d_0+2d_1|^2+|d_0|^2].
}
```

Near equal current steps,

```math
\sigma_{W_0}\simeq\sqrt{20}|d|\sigma_J.
```

For two comparable visible modes and `\eta=\sigma_J/|d|`, the near-coalescence significance behaves approximately as

```math
Z_2\simeq\frac{|q_1-q_2|^2}{4\sqrt{20}\,\eta}.
```

Thus a nominal `3sigma` design scale is

```math
\boxed{|q_1-q_2|\gtrsim7.33\sqrt{\eta}.}
```

The correct experimental order is therefore: establish a significant minor first, recover roots second.

---

# S6. Ordinary rank-two mechanisms have different RF root laws

## S6.1 Finite scalar boundary

For constant `D,w,\kappa`, any linear finite-boundary condition changes mode amplitudes but not the two roots of

```math
D r^2+w r-(\kappa+i\omega)=0.
```

Vieta gives

```math
\boxed{r_++r_-=-w/D,}
```

which is real and RF-independent, and

```math
\boxed{r_+r_-=-(\kappa+i\omega)/D.}
```

Thus the root product has a constant real part and an imaginary part exactly linear in RF frequency.

## S6.2 Independent electron and hole contributions

A conventional two-carrier planar signal can be written

```math
J(z,s)=C_0(s)+C_e(s)e^{+\gamma_e(s)z}+C_h(s)e^{-\gamma_h(s)z}.
```

After first differencing there are two spatial modes. Each positive propagation magnitude obeys its own drift-diffusion-recombination law

```math
D_c\gamma_c^2+w_c\gamma_c=\kappa_c+s.
```

The two signed roots therefore do not, in general, obey the single-quadratic boundary sum/product constraints. In the deterministic no-recombination limit the root sum is imaginary and linear in RF while the root product is real and quadratic in RF, qualitatively distinct from the finite-boundary scalar case.

This is why rank two is a model-order statement, not a mechanism label.

---

# S7. Low-frequency four-color slowness-gradient theorem

For deterministic downstream transport with local slowness

```math
q(z)=1/v(z),
```

one point-generated carrier gives, up to a common factor,

```math
J(z,s)=\int_z^L
\exp[-s\int_z^x q(u)du]dx.
```

Expanding at low `s`,

```math
J(z,s)=(L-z)-sA(z)+O(s^2),
```

with

```math
A(z)=\int_z^L(L-u)q(u)du.
```

For four equally spaced source depths with spacing `h` and quartet midpoint `z_c`, define

```math
\mathcal C_4
=2\ln\Delta J_1-\ln\Delta J_0-\ln\Delta J_2.
```

A centered Taylor expansion gives

```math
\boxed{
\mathcal C_4
=-s h^2[2q'(z_c)-(L-z_c)q''(z_c)]
+O(sh^4,s^2).
}
```

For locally linear slowness,

```math
\boxed{\Im\mathcal C_4/\omega=-2h^2q'(z_c)}
```

under the `e^{-i\omega t}` convention.

This theorem is deliberately downstream of the lower-order null tests. A nonzero closure is not automatically a velocity-gradient measurement unless source-shape evolution, extra modes, boundary influence, and the high-Peclet approximation are controlled.

---

# S8. Optical and calibration error expansions

## S8.1 Mean-centered source-shape evolution

Let source channel `m` have random internal coordinate

```math
D_m=\mu_m+U_m,
\qquad E[U_m]=0,
```

with equally spaced means `\mu_m=\mu_0+mh`. Let `v_m=E[U_m^2]`.

For a homogeneous exponential spatial mode, expanding the source transform around the mean gives the leading log-closure contamination

```math
\boxed{
\mathcal C_{4,opt}
=\frac{\gamma}{2h}
(v_3-3v_2+3v_1-v_0)+O(\gamma^2).
}
```

The first-order optical-width error is therefore a third discrete difference. Constant, linear, and quadratic variance evolution vanish at this order.

## S8.2 Relative amplitude error

At low RF the ideal raw current is locally affine in depth. For

```math
\widetilde J_m=(1+\epsilon_m)J_m,
```

the leading closure error is

```math
\boxed{\delta\mathcal C_4=-\Delta^3(\epsilon_mJ_m)/B,}
```

where `B` is the affine current step. Common gain and smooth low-order spectral calibration drift are therefore strongly rejected; irregular channel-to-channel error is more dangerous.

## S8.3 Nonlinear spectral-to-depth map

If the true coordinate is `z=f(\mu)`, affine `f` is exact. For smooth nonlinear distortion,

```math
\boxed{
\mathcal C_{4,coord}
=h^2[\gamma f''-(\ln f')'']_{\mu_c}+O(h^4).
}
```

Thus the key calibration requirement is local curvature, not absolute depth accuracy.

---

# S9. Excess-energy invariance in an ideal linearly graded gap

Let

```math
E_g(z)=E_{g0}-Gz
```

and assume local absorption depends only on the total photon excess energy

```math
\nu=E_\gamma-E_g(z),
\qquad
\alpha=\alpha(\nu).
```

Changing photon energy translates the threshold depth but does not change the generation distribution in `\nu`. Beer-Lambert absorption gives

```math
\boxed{
p_\nu(\nu)
=\frac{\alpha(\nu)}{G}
\exp[-G^{-1}\int_0^\nu\alpha(u)du].
}
```

The expression contains no photon energy. Thus, in the ideal untruncated limit, wavelength moves the internal generation coordinate without changing the complete total excess-energy distribution.

This does not prove that all microscopic initial-state variables are wavelength invariant in a real semiconductor. It provides a precise baseline against which real-bandstructure and thermalization corrections can be calculated.

---

# S10. Four-channel independent-noise covariance and spacing law

For

```math
\mathcal C_4
=2\ln d_1-\ln d_0-\ln d_2,
```

linearized independent current errors give

```math
\delta\mathcal C_4
=\epsilon_0/d_0
-(1/d_0+2/d_1)\epsilon_1
+(2/d_1+1/d_2)\epsilon_2
-\epsilon_3/d_2.
```

Near equal differences `d_m\simeq d`,

```math
\boxed{\sigma_{\mathcal C_4}\simeq\sqrt{20}\sigma_J/|d|.}
```

The coefficient pattern is the third-difference stencil `(1,-3,3,-1)`.

If the dominant smooth systematic is `Ah^2` while independent closure noise is `B/h`, then

```math
MSE(h)=A^2h^4+B^2/h^2
```

has optimum

```math
\boxed{h_*=(B/(\sqrt2 A))^{1/3}.}
```

If white averaging gives `\sigma_J\propto t^{-1/2}`, then `h_*\propto t^{-1/6}`. This slow law quantifies why geometry and systematic rejection matter more than brute-force averaging for spatial resolution.

---

# S11. HgCdTe numerical validation chain

The main paper's worked example uses:

```text
L = 7.6 um
T = 300 K
linear x = 0.55 -> 0.32
mean generation depths = 2.5, 3.0, 3.5, 4.0 um
wavelengths ~ 2.134651, 2.215042, 2.301173, 2.393907 um
Pabs > 0.9993
```

Optics:

- Hansen-Schmit-Casselman bandgap;
- Moazzami above-gap absorption;
- full finite Beer-Lambert generation kernels rather than point sources.

Transport stress:

- mobility sensitivity scale `9000 cm^2/V/s`;
- Einstein diffusion at 300 K;
- quasi-neutral graded-gap force model;
- `8 kV/cm` velocity-saturation sensitivity scale;
- reduced density-of-states gradient correction.

The stochastic raw-current response solves

```math
D J''+v(z)J'-[\kappa+s]J=-v(z)
```

with collector condition `J(L)=0` and an upstream semi-infinite homogeneous matching condition chosen specifically to avoid the earlier reflecting-boundary confound.

For `\kappa=0`, the gradient-sensitive excess is approximately

```text
100 MHz -> -0.011978 deg
500 MHz -> -0.058727 deg
1 GHz   -> -0.110405 deg
```

The deterministic point-source low-RF theorem predicts approximately `-0.01254 deg` at 100 MHz.

An independent adaptive shooting construction reproduces the stochastic finite-difference solution at the `~10^-6 degree` level or better over these RF points. The agreement is a numerical cross-check of the explicit conditional model, not experimental validation.

---

# S12. What remains outside the present paper

The repository contains broader exact theory that should not be pulled into the headline manuscript unless a reviewer or derivation requires it:

- characteristic-function positivity tests for a true arrival-time observable;
- Doob-conditioned drift/recombination identifiability;
- arbitrary-profile local derivative inversion;
- local-clock occupation-time spectroscopy;
- full timing-cumulant spatial decomposition;
- Levy/random-delay spectral reconstruction;
- translated-gradient fabrication optimization;
- the earlier published-sample A/B inverse branch.

Those results remain scientifically useful, but the present paper is stronger if it stays centered on the observable-corrected four-/six-color falsification architecture.

---

# S13. Epistemic boundary

The following ingredients are established and are not claimed as new:

```text
Shockley-Ramo induced-current theory
wavelength-dependent photodiode absorption depth and RF phase
optoelectronic chromatic dispersion
frequency-domain drift-diffusion
first-passage semigroups
Hankel/Prony model-order identification
algebraic convection-diffusion inversion
graded-HgCdTe transport and high-speed response.
```

The candidate contribution under audit is specifically:

```text
spectral wavelength -> calibrated internal source coordinate
+
Shockley-Ramo-aware spatial first differences
+
minimal four-/six-color model-order closure
+
RF root-algebra falsification of ordinary photocarrier transport hypotheses.
```

**Priority remains unproven.** Negative literature searches must not be converted into novelty language.
