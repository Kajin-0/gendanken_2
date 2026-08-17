# Noise-weighted root and diffusion bias from remote-kernel leakage

**Date:** 2026-08-15  
**Status:** **DERIVED / DESIGN-LAW CANDIDATE — PRIORITY UNPROVEN**

## 1. Purpose

The Paper-02 program has already established the causal chain

```text
finite generation-kernel support in a nonuniform-velocity region
    -> calibrated-channel leakage
    -> biased one-mode spatial root
    -> positive apparent homogeneous diffusion
```

while same-frequency model residuals can remain very small.

This note turns that qualitative chain into a first-order attribution bound.

The result is useful even if the eventual publication claim changes, because it separates three experimentally distinct quantities:

1. **optical nuisance exposure** — how much each calibrated kernel overlaps the nuisance region;
2. **physical nuisance magnitude** — how strongly the true point-source response differs there;
3. **inverse conditioning** — how strongly a given channel perturbation moves the fitted transport root rather than the residual.

---

## 2. Calibrated one-mode model

At one RF frequency, write the calibrated one-mode channel model as

```math
\mathbf f(C,K,r)
=C\mathbf 1+K\mathbf F(r),
```

where

```math
F_m(r)=\int g_m(z)\varphi_r(z)\,dz.
```

The exact basis `varphi_r` can be the exponential basis or the numerically stable shifted basis used in the kernel-aware Paper-02 solver. Nothing below depends on that reparameterization provided `F_m(r)` is differentiable.

Let the true measured vector be

```math
\mathbf y
=\mathbf f(C,K,r)+\mathbf E+\mathbf n,
```

where

- `E` is a deterministic model-discrepancy / nuisance vector;
- `n` is measurement noise.

Let `W` be a positive-definite Hermitian weighting matrix, ideally the inverse complex covariance of the channel measurements after any required real-imaginary representation is handled consistently.

---

## 3. Full first-order parameter bias

Linearize the one-mode model:

```math
\delta\mathbf f
=\mathcal G\,\delta\boldsymbol\theta,
```

with

```math
\delta\boldsymbol\theta
=
\begin{bmatrix}
\delta C\\
\delta K\\
\delta r
\end{bmatrix},
```

and complex Jacobian

```math
\boxed{
\mathcal G
=
\begin{bmatrix}
\mathbf 1 & \mathbf F & K\mathbf F_r
\end{bmatrix},
}
```

where

```math
\mathbf F_r=\frac{\partial\mathbf F}{\partial r}.
```

For a local weighted least-squares fit, the deterministic pseudo-true parameter displacement is

```math
\boxed{
\delta\boldsymbol\theta
=
(\mathcal G^\dagger W\mathcal G)^{-1}
\mathcal G^\dagger W\mathbf E
+O(\|\mathbf E\|^2).
}
```

This is the local attribution-bias law.

A nuisance component that lies in the model tangent space changes fitted parameters without producing a first-order goodness-of-fit residual.

The post-fit first-order residual is instead

```math
\boxed{
\mathbf e_{\rm post}
=(I-P_{\mathcal G})\mathbf E,
}
```

with

```math
P_{\mathcal G}
=\mathcal G(\mathcal G^\dagger W\mathcal G)^{-1}\mathcal G^\dagger W.
```

Thus parameter bias and model rejection are different projections of the same nuisance vector.

---

## 4. Root-bias formula after eliminating offset and amplitude

The transport root is the quantity of primary interest, so eliminate the two linear nuisance parameters `C,K` explicitly.

Define

```math
X=\begin{bmatrix}\mathbf 1 & \mathbf F\end{bmatrix},
```

and the weighted projector onto the offset/amplitude subspace

```math
P_X=X(X^\dagger W X)^{-1}X^\dagger W.
```

The raw root-sensitivity vector is

```math
\mathbf h=K\mathbf F_r.
```

Its component that cannot be absorbed by re-fitting `C,K` is

```math
\boxed{
\mathbf h_\perp=(I-P_X)\mathbf h.
}
```

Then the first-order fitted-root bias is

```math
\boxed{
\delta r
=
\frac{\mathbf h_\perp^\dagger W\mathbf E}
{\mathbf h_\perp^\dagger W\mathbf h_\perp}
+O(\|\mathbf E\|^2).
}
```

Equivalently,

```math
\boxed{
|\delta r|
\le
\frac{\|\mathbf E\|_W}
{\|\mathbf h_\perp\|_W}
+O(\|\mathbf E\|^2),
}
```

where

```math
\|\mathbf x\|_W^2=\mathbf x^\dagger W\mathbf x.
```

The denominator

```math
\boxed{\|\mathbf h_\perp\|_W}
```

is the effective root-identification sensitivity after offset/amplitude freedom is removed.

Small `||h_perp||_W` means that the root is poorly conditioned even if the raw spectral contrast is large.

---

## 5. Remote-region optical bound

Suppose the physical discrepancy is confined to spatial region `R`:

```math
\delta H(z)=0\qquad z\notin R.
```

For calibrated normalized nonnegative generation kernels,

```math
E_m
=\int_R g_m(z)\delta H(z)\,dz.
```

Define the restricted overlap

```math
p_m=\int_R g_m(z)\,dz
```

and a physical response bound

```math
H_R=\sup_{z\in R}|\delta H(z)|.
```

Then channel by channel,

```math
\boxed{|E_m|\le p_m H_R.}
```

For diagonal weights

```math
W=\operatorname{diag}(w_m),
```

this gives

```math
\|\mathbf E\|_W
\le
H_R\left(\sum_m w_mp_m^2\right)^{1/2}.
```

Combining with the root-bias formula,

```math
\boxed{
|\delta r|
\le
H_R
\frac{\left(\sum_m w_mp_m^2\right)^{1/2}}
{\|\mathbf h_\perp\|_W}
+O(H_R^2).
}
```

This is the first reusable Paper-02 attribution bound.

It has the expected exact zero-overlap limit:

```math
p_m=0\ \forall m
\quad\Longrightarrow\quad
\delta r=0
```

to all orders because then the exact leakage vector is zero, not merely bounded.

---

## 6. Interpretation of the three factors

The bound can be written schematically as

```math
\boxed{
\text{root bias}
\lesssim
\text{nuisance response}
\times
\text{kernel exposure}
\times
\text{inverse susceptibility}.
}
```

More explicitly:

### Physical nuisance scale

```math
H_R.
```

This describes how different the real point-source response can become inside the nuisance region.

### Optical exposure

```math
\left(\sum_m w_mp_m^2\right)^{1/2}.
```

This depends on the **full calibrated kernel support**, not merely the source means.

### Inverse susceptibility

```math
\frac1{\|\mathbf h_\perp\|_W}.
```

This measures how easily channel perturbations can move the fitted spatial root after the offset and amplitude have been re-optimized.

A small remote overlap can therefore still create a substantial parameter bias if the inverse is poorly conditioned or the nuisance response is large.

---

## 7. Why fit residual can stay small while root bias is large

Let

```math
P_{\mathcal G}
```

be the full one-mode tangent projector.

Decompose

```math
\mathbf E
=P_{\mathcal G}\mathbf E
+(I-P_{\mathcal G})\mathbf E.
```

The first term moves the fitted parameters.
The second term produces the post-fit residual.

Therefore no universal bound of the form

```text
large parameter bias => large model residual
```

exists.

A nuisance can satisfy

```math
\|P_{\mathcal G}\mathbf E\|_W
\gg
\|(I-P_{\mathcal G})\mathbf E\|_W
```

and then look almost perfectly one-mode while strongly biasing the recovered root.

This is the arbitrary-kernel weighted form of the earlier tangent-confound theorem.

---

## 8. Propagation from root bias to apparent diffusion

Use the Fourier convention of the current Paper-02 numerical tests,

```math
D\gamma^2+w\gamma=-i\omega,
```

with

```math
\gamma=a+ib,
\qquad
\gamma=-r
```

for the current coordinate convention.

For `kappa=0`, solving the two real equations gives

```math
\boxed{
D
=-\frac{\omega a}
{b(a^2+b^2)},
}
```

and

```math
\boxed{
w
=\frac{\omega(a^2-b^2)}
{b(a^2+b^2)}.
}
```

The local diffusion sensitivity is

```math
\boxed{
\frac{\partial D}{\partial a}
=
\frac{\omega(a^2-b^2)}
{b(a^2+b^2)^2},
}
```

```math
\boxed{
\frac{\partial D}{\partial b}
=
\frac{\omega a(a^2+3b^2)}
{b^2(a^2+b^2)^2}.
}
```

Therefore

```math
|\delta D|
\le
L_D|\delta\gamma|+O(|\delta\gamma|^2),
```

where

```math
\boxed{
L_D=
\left[
\left(\frac{\partial D}{\partial a}\right)^2
+
\left(\frac{\partial D}{\partial b}\right)^2
\right]^{1/2}.
}
```

Since `delta gamma=-delta r`, the remote-region attribution bound becomes

```math
\boxed{
|\delta D|
\le
L_D H_R
\frac{\left(\sum_m w_mp_m^2\right)^{1/2}}
{\|\mathbf h_\perp\|_W}
+O(H_R^2).
}
```

This is a direct design inequality connecting optical support, device-level nuisance response, inverse conditioning, and material-parameter bias.

---

## 9. Particularly important near-pure-drift limit

Near a true zero-diffusion drift response,

```math
a=\Re\gamma\to0,
```

while

```math
b\simeq-\frac{\omega}{w}.
```

Then

```math
D
\simeq
-\frac{\omega a}{b^3}
```

and therefore

```math
\boxed{
D_{\rm app}
\simeq
\frac{w^3}{\omega^2}\,\Re\gamma.
}
```

For a nuisance-induced root shift from a zero-diffusion baseline,

```math
\boxed{
\delta D
\simeq
\frac{w^3}{\omega^2}\,\delta(\Re\gamma).
}
```

This exposes a severe low-frequency susceptibility:

```math
\boxed{
\frac{\partial D}{\partial\Re\gamma}
\propto\omega^{-2}.
}
```

The physical diffusion signature itself has exactly this scaling inverted:

```math
\Re\gamma
\sim
D\omega^2/w^3.
```

Thus a very small nuisance-induced real part of the recovered spatial exponent can be interpreted as a substantial positive diffusion coefficient at low RF.

The effect is not an algebraic anomaly. It is the natural conditioning of extracting a quadratic-in-frequency parameter from a response dominated by the linear-in-frequency drift phase.

---

## 10. Numerical check against the current kernel-aware depletion example

At 100 MHz the calibrated-kernel depleted calculation gives approximately

```math
\gamma
=(60.6881-i\,24446.95)\ \mathrm{m^{-1}}.
```

The exact homogeneous inversion gives

```math
D_{\rm eff}
=2.60980\times10^{-3}\ \mathrm{m^2/s},
```

```math
w_{\rm eff}
=2.57010\times10^4\ \mathrm{m/s}.
```

Using only the near-pure-drift approximation

```math
D_{\rm app}
\simeq
\frac{w^3}{\omega^2}\Re\gamma
```

gives

```math
D_{\rm app}
\simeq
2.60972\times10^{-3}\ \mathrm{m^2/s}.
```

The relative difference from the exact inversion is only about

```math
3.1\times10^{-5}.
```

Thus the entire false diffusion coefficient in this example is essentially the inversion's interpretation of a nuisance-induced real spatial exponent of only about

```text
61 per metre
```

against an RF phase exponent magnitude of about

```text
2.44e4 per metre.
```

That extreme scale separation explains why the fitted channel sequence can look excellent while the inferred `D` is materially wrong.

---

## 11. Experimental design consequence

A claim of microscopic diffusion from spectral-depth RF data should not be based only on

- small same-frequency one-mode residual;
- a positive fitted `D`;
- or agreement of one additional low-RF point.

For a known nuisance region `R`, a stronger attribution test is:

1. calibrate the complete generation kernels `g_m(z)`;
2. compute or bound each restricted overlap `p_m`;
3. bound the physically allowed point-response departure `H_R` from electrostatics/geometry;
4. evaluate the root-conditioning denominator `||h_perp||_W`;
5. propagate the resulting root-bias bound to `D` using `L_D` or the near-drift expression above;
6. require the claimed microscopic diffusion to exceed that systematic attribution bound at the desired confidence level.

This converts the Paper-02 phenomenon from a warning into a quantitative detector-design / inference criterion.

---

## 12. Limits of the present bound

The current formula is first order in the nuisance response and assumes a locally unique one-mode fit.

It does not yet include

- branch ambiguity in the spatial logarithm;
- uncertainty in the calibrated optical kernels themselves;
- correlated uncertainty in electrostatic nuisance bounds;
- higher-order parameter shifts for large leakage;
- multi-frequency joint fitting;
- rank-two or higher alternatives.

Those effects can be layered on after the first-order result is validated numerically.

---

## 13. Next validation

The strongest immediate check is to use the existing continuous tail-weight ablation and verify that, for small tail scale, the measured fitted-root and `D_eff` derivatives agree with the Jacobian prediction above.

That test should compare

```math
\frac{d r}{d s}
```

and

```math
\frac{d D_{\rm eff}}{d s}
```

at small remote-tail scale `s` against the analytic linearized inverse.

If that passes, the bias law becomes the natural theoretical spine of a possible standalone Paper 02.
