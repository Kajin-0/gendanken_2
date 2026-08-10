# Translation-Response Theorem — A Movable Internal Perturbation Separates Optical Generation from Deterministic Transit

**Date:** 2026-08-10  
**Status:** **DERIVED** inside an explicit one-dimensional deterministic path-transport model; finite-width and numerical identities **CHECKED**; stochastic drift-diffusion generalization stated separately; **no novelty/priority claim**

## 1. The gedanken experiment

Consider the simplest possible one-dimensional photodetector.

```text
z = 0                         z = L
optical entrance  ----------> collecting boundary
```

A photon of wavelength `lambda` creates a carrier at a random depth

```math
X_\lambda\sim p_\lambda(z),
\qquad
\int_0^L p_\lambda(z)\,dz=1.
```

After generation, the carrier moves monotonically toward `L` with local transit slowness

```math
q(z)>0.
```

For simple drift,

```math
q(z)=1/v(z).
```

The transit time for a carrier generated at `x` is therefore

```math
\boxed{
T(x)=\int_x^L q(s)\,ds.
}
```

Now insert a weak internal transport perturbation of known shape `h`, and imagine translating that same perturbation through the device:

```math
\boxed{
q_{\epsilon,z_0}(z)
=q(z)+\epsilon h(z-z_0).
}
```

The thought experiment asks only:

> **How does the detector response change when the same weak internal perturbation is moved from one known depth to another?**

This produces several exact identities.

---

# 2. Low-frequency theorem

The mean transit time at wavelength `lambda` is

```math
\bar T_\lambda
=\int_0^L p_\lambda(x)T(x)\,dx.
```

Define the generation CDF

```math
F_\lambda(z)
=\int_0^z p_\lambda(x)\,dx.
```

Changing the order of integration gives

```math
\boxed{
\bar T_\lambda
=\int_0^L F_\lambda(z)q(z)\,dz.
}
```

For the translated perturbation, define the linear mean-delay response

```math
D_\lambda(z_0)
\equiv
\left.
\frac{\partial\bar T_\lambda}{\partial\epsilon}
\right|_{\epsilon=0}.
```

Then

```math
\boxed{
D_\lambda(z_0)
=\int_0^L F_\lambda(z)h(z-z_0)\,dz.
}
```

Differentiate with respect to perturbation position. If the feature is internal so the boundary term vanishes,

```math
\begin{aligned}
\frac{dD_\lambda}{dz_0}
&=-\int F_\lambda(z)h'(z-z_0)\,dz\\
&=\int F_\lambda'(z)h(z-z_0)\,dz.
\end{aligned}
```

Since

```math
F_\lambda'(z)=p_\lambda(z),
```

we obtain the first central result:

```math
\boxed{
\frac{dD_\lambda}{dz_0}
=
\int_0^L p_\lambda(z)h(z-z_0)\,dz.
}
\tag{1}
```

## Interpretation

Translation differentiates the cumulative timing kernel.

The ordinary timing measurement contains the smooth CDF `F_lambda`.

The **position derivative of a translated perturbation response contains the local generation density `p_lambda` itself**, blurred only by the known perturbation shape.

This is the mathematical reason a translated internal feature can be far better localized than an arbitrary static transport profile.

---

# 3. Point-feature limit — direct generation-density measurement

Let the perturbation become narrow while retaining finite area

```math
A_h=\int h(z)\,dz,
```

so

```math
h(z-z_0)\to A_h\delta(z-z_0).
```

Equation (1) becomes

```math
\boxed{
\frac{dD_\lambda}{dz_0}
=A_h p_\lambda(z_0).
}
\tag{2}
```

Thus a scan of one weak point-like internal delay perturbation through depth directly traces the optical generation PDF.

No inversion of a broad CDF kernel is required.

---

# 4. Exact finite-displacement probability law

For the same infinitesimal feature moved from `z_1` to `z_2>z_1`, integrate (2):

```math
\boxed{
D_\lambda(z_2)-D_\lambda(z_1)
=
A_h\int_{z_1}^{z_2}p_\lambda(z)\,dz.
}
\tag{3}
```

Therefore

> **The change in mean timing response is exactly proportional to the probability that the photon generates the carrier between the two feature positions.**

This is a direct falsifiable prediction.

For a positive added-delay feature,

```math
h\ge0,
```

Equation (1) also gives

```math
\boxed{
\frac{dD_\lambda}{dz_0}\ge0.
}
\tag{4}
```

So moving the same positive delay perturbation toward the downstream collector must change the mean-delay response monotonically in this model.

A robust sign reversal falsifies at least one assumption of the deterministic local path model.

---

# 5. Low-frequency sum rule and moment identities

For an even perturbation shape with area `A_h`, define

```math
r_\lambda(z_0)
=\frac{1}{A_h}\frac{dD_\lambda}{dz_0}.
```

Equation (1) is a convolution:

```math
\boxed{
r_\lambda=p_\lambda*g,
\qquad
g=h/A_h.
}
\tag{5}
```

If the translated feature is scanned over the full support,

```math
\boxed{
\int r_\lambda(z_0)\,dz_0=1.
}
\tag{6}
```

For an even feature centered at zero,

```math
\boxed{
\langle z_0\rangle_r
=\langle z\rangle_{p_\lambda},
}
\tag{7}
```

and

```math
\boxed{
\operatorname{Var}(r_\lambda)
=
\operatorname{Var}(p_\lambda)
+
\operatorname{Var}(g).
}
\tag{8}
```

Hence the centroid of the relocation-slope curve gives the mean generation depth exactly, while its variance is the optical generation variance plus the known feature-width variance.

These identities are independent of the baseline transport profile `q(z)`.

---

# 6. Finite-RF theorem

Now use the full complex deterministic transit response

```math
\boxed{
H_\lambda(\omega)
=\int_0^L
p_\lambda(x)e^{-i\omega T(x)}\,dx.
}
\tag{9}
```

Define the linear logarithmic response to perturbation strength

```math
D_{\lambda,\omega}(z_0)
\equiv
\left.
\frac{\partial}{\partial\epsilon}
\ln H_{\lambda,\omega}[q+\epsilon h_{z_0}]
\right|_{\epsilon=0}.
```

The perturbation changes a carrier's time by

```math
\delta T(x)
=\epsilon\int_x^L h(z-z_0)\,dz.
```

Therefore

```math
\delta H
=-i\omega\epsilon
\int_0^L
p_\lambda(x)e^{-i\omega T(x)}
\left[
\int_x^Lh(z-z_0)dz
\right]dx.
```

Exchange the order of integration:

```math
\boxed{
D_{\lambda,\omega}(z_0)
=-i\omega
\int_0^Lh(z-z_0)C_{\lambda,\omega}(z)\,dz,
}
\tag{10}
```

where

```math
C_{\lambda,\omega}(z)
=\frac{1}{H_\lambda(\omega)}
\int_0^z
p_\lambda(x)e^{-i\omega T(x)}dx.
```

Differentiate with respect to feature position:

```math
\boxed{
R_{\lambda,\omega}(z_0)
\equiv
\frac{\partial D_{\lambda,\omega}}{\partial z_0}
=
-\frac{i\omega}{H_\lambda(\omega)}
\int_0^L
h(z-z_0)
 p_\lambda(z)e^{-i\omega T(z)}dz.
}
\tag{11}
```

This is the finite-RF translation-response theorem.

Translation converts the cumulative complex sensitivity into a convolution with the **local complex field**

```math
\boxed{
a_{\lambda,\omega}(z)
=
\frac{p_\lambda(z)e^{-i\omega T(z)}}{H_\lambda(\omega)}.
}
\tag{12}
```

---

# 7. Point-feature factorization — optics and transport separate

For

```math
h(z-z_0)=A_h\delta(z-z_0),
```

Equation (11) becomes

```math
\boxed{
R_{\lambda,\omega}(z_0)
=
-\frac{i\omega A_h}{H_\lambda(\omega)}
 p_\lambda(z_0)e^{-i\omega T(z_0)}.
}
\tag{13}
```

This factorization yields two striking inverse identities.

## 7.1 Magnitude gives the optical generation density

Because `p_lambda` is real and nonnegative,

```math
|R_{\lambda,\omega}(z)|
=\frac{\omega|A_h|}{|H_\lambda|}p_\lambda(z).
```

Normalize over depth:

```math
\boxed{
p_\lambda(z)
=
\frac{|R_{\lambda,\omega}(z)|}
{\int_0^L|R_{\lambda,\omega}(u)|du}.
}
\tag{14}
```

Thus the perturbation strength and the absolute complex transfer cancel.

In the ideal translated-point-feature gedanken experiment, **one RF frequency and one optical wavelength are sufficient to recover the complete generation-depth PDF over the region where the feature can be scanned.**

## 7.2 Phase slope gives local transit slowness

From (13),

```math
\arg R(z)
=\text{constant}-\omega T(z).
```

Since

```math
\frac{dT}{dz}=-q(z),
```

```math
\boxed{
q(z)
=
\frac{1}{\omega}
\frac{d}{dz}\arg R_{\lambda,\omega}(z).
}
\tag{15}
```

Under local deterministic drift,

```math
\boxed{
v(z)=
\left[
\frac{1}{\omega}
\frac{d}{dz}\arg R(z)
\right]^{-1}.
}
\tag{16}
```

Therefore the **magnitude of the same complex relocation field maps the optics, while its phase gradient maps the transport.**

This separation is the strongest theoretical result presently found in this branch.

---

# 8. A wavelength-independent complex sum rule

Integrate (13) over all feature positions:

```math
\begin{aligned}
\int_0^LR_{\lambda,\omega}(z)dz
&=-\frac{i\omega A_h}{H_\lambda}
\int_0^Lp_\lambda(z)e^{-i\omega T(z)}dz\\
&=-i\omega A_h.
\end{aligned}
```

Hence

```math
\boxed{
\int_0^LR_{\lambda,\omega}(z)dz
=-i\omega A_h.
}
\tag{17}
```

The right-hand side is independent of

```text
wavelength,
optical generation profile,
baseline velocity profile,
and detector transfer H.
```

For a real perturbation amplitude `epsilon`, multiply the right-hand side by `epsilon`.

This is a particularly strong falsification check: after dividing by `-i omega`, complete relocation scans at different wavelengths must collapse to the same complex feature area within the deterministic first-order model.

---

# 9. Cross-wavelength and cross-frequency null tests

Equation (13) implies more parameter-free consistency relations.

For two wavelengths at the same RF frequency,

```math
\frac{R_{\lambda_1,\omega}(z)}
{R_{\lambda_2,\omega}(z)}
=
\frac{p_{\lambda_1}(z)}{p_{\lambda_2}(z)}
\frac{H_{\lambda_2}(\omega)}{H_{\lambda_1}(\omega)}.
```

The transit factor cancels.

Therefore

```math
\boxed{
\frac{d}{dz}
\arg
\frac{R_{\lambda_1,\omega}(z)}
{R_{\lambda_2,\omega}(z)}=0.
}
\tag{18}
```

where both generation densities are nonzero.

Likewise, (15) predicts

```math
\boxed{
\frac{1}{\omega}
\frac{d}{dz}\arg R_{\lambda,\omega}(z)
=q(z)
}
\tag{19}
```

for **every wavelength and RF frequency** in the deterministic model.

Thus reconstructed `q(z)` must collapse across `lambda` and `omega`.

Failure of this collapse is not merely experimental inconvenience. It directly falsifies the deterministic local path model and signals physics such as

```text
diffusive path dispersion,
recombination-conditioned transport,
nonlocal/high-field dynamics,
feature-induced optical changes,
or nonlinear perturbation response.
```

This gives a built-in route from a simple null hypothesis to richer transport physics.

---

# 10. Finite-width features — exact convolution and deconvolution

Define the reversed feature

```math
\tilde h(z)=h(-z).
```

Equation (11) can be written

```math
\boxed{
R_{\lambda,\omega}
=-i\omega
(\tilde h*a_{\lambda,\omega}).
}
\tag{20}
```

Therefore in spatial Fourier space

```math
\boxed{
\widehat R(k)
=-i\omega
\widehat{\tilde h}(k)
\widehat a(k).
}
\tag{21}
```

Whenever the known feature transfer `h_hat(k)` is nonzero,

```math
\boxed{
\widehat a(k)
=
\frac{\widehat R(k)}
{-i\omega\widehat{\tilde h}(k)}.
}
\tag{22}
```

Thus finite feature width is not a conceptual loss of identifiability in noiseless data; it is a **bandwidth/noise problem**.

For an even narrow feature with normalized second moment `sigma_h^2`,

```math
\boxed{
\frac{R(z)}{-i\omega A_h}
=
a(z)
+
\frac{\sigma_h^2}{2}a''(z)
+O(\sigma_h^4).
}
\tag{23}
```

This explains why the earlier HgCdTe edge-ramp calculation saturated once the programmed edge became sharper than the optical/transport spatial scale.

---

# 11. Fundamental noise-limited localization statement

Let any finite set of measured real observables be collected into

```math
\mathbf y
\sim
\mathcal N(\boldsymbol\mu(z_0),\mathbf C),
```

where `z_0` is a translated feature position.

The Fisher information for depth is

```math
\boxed{
\mathcal I(z_0)
=
\left(
\frac{\partial\boldsymbol\mu}{\partial z_0}
\right)^T
\mathbf C^{-1}
\left(
\frac{\partial\boldsymbol\mu}{\partial z_0}
\right).
}
\tag{24}
```

Hence every unbiased estimator obeys

```math
\boxed{
\sigma_{z_0}
\ge
\mathcal I(z_0)^{-1/2}.
}
\tag{25}
```

If nuisance responses span columns of a whitened matrix `N`, use the orthogonal projector

```math
P_\perp
=I-N(N^TN)^+N^T
```

and

```math
\boxed{
\mathcal I_{\rm useful}
=
\mathbf g^T
C^{-1/2}P_\perp C^{-1/2}
\mathbf g,
\qquad
\mathbf g=\partial_{z_0}\boldsymbol\mu.
}
\tag{26}
```

The relocation theorem identifies `g` explicitly. This converts the earlier numerical design problem into a rigorous resolution bound.

---

# 12. Sharp absorption-edge gedanken limit

The result becomes especially transparent in an ideal graded-gap absorber.

Suppose the absorption edge is infinitely sharp and the monotonic local gap maps each wavelength to one generation depth

```math
E_g(z_g)=hc/\lambda,
```

so

```math
p_\lambda(z)=\delta(z-z_g(\lambda)).
```

For an infinitesimal delay feature,

```math
D_\lambda(z_0)
=A_hF_\lambda(z_0)
```

is a step.

Moving the feature from `z_1` to `z_2` produces

```math
\boxed{
D_\lambda(z_2)-D_\lambda(z_1)
=
\begin{cases}
A_h,& z_g(\lambda)\in(z_1,z_2),\\
0,& \text{otherwise}.
\end{cases}
}
\tag{27}
```

The detector therefore produces an ideal **spectral top-hat relocation signal** whose edges are

```math
\boxed{
\lambda_j=\frac{hc}{E_g(z_j)}.
}
\tag{28}
```

For a small displacement,

```math
\boxed{
\Delta\lambda
\simeq
-\frac{hc}{E_g^2}
\frac{dE_g}{dz}\Delta z.
}
\tag{29}
```

Real absorption broadening smooths the top-hat, but the edge positions and convolution structure remain directly testable.

This is perhaps the simplest experimental picture of the entire theory:

> **move one internal transport feature, and the spectral timing window must move with the local bandgap coordinate.**

---

# 13. What survives beyond deterministic transport

The deterministic factorization (13)-(19) should **not** be assumed for drift-diffusion without proof.

For the active first-passage model

```math
\mathcal L_su
=
D u''+v(z)u'-(\kappa+s)u=0,
```

perturb the local drift

```math
v(z)\to v(z)+\epsilon h(z-z_0).
```

The first variation `w_s=partial_epsilon u_s` satisfies

```math
\boxed{
\mathcal L_sw_s
=-h(z-z_0)u_s'(z)
}
\tag{30}
```

with homogeneous linearized boundary conditions.

If `G_s(x,z)` is the corresponding Green function, then

```math
w_s(x)
=-\int G_s(x,z)h(z-z_0)u_s'(z)dz.
```

For

```math
N_s=\int p_\lambda(x)u_s(x)dx,
\qquad
H=N_{i\omega}/N_0,
```

the exact first-order logarithmic response is again an integral of the translated feature against a spatial sensitivity kernel:

```math
\boxed{
\delta\ln H
=
\epsilon
\int h(z-z_0)J_{\lambda,\omega}(z)dz,
}
\tag{31}
```

where `J` is determined by the forward solution, Green function, generation profile, and the DC normalization term.

Therefore translation gives

```math
\boxed{
\frac{\partial}{\partial z_0}\delta\ln H
=
\epsilon
\int h(z-z_0)J'_{\lambda,\omega}(z)dz.
}
\tag{32}
```

The general principle survives:

> **translating a known local perturbation differentiates the physical sensitivity kernel.**

But the remarkable deterministic separation

```text
magnitude -> p(z)
phase slope -> q(z)
```

is now a falsifiable limiting prediction rather than an identity to impose on real HgCdTe data.

The difference between (13) and the first-passage result is itself scientifically useful: it measures how stochastic/nonlocal carrier transport departs from monotonic deterministic transit.

---

# 14. Strongest falsifiable predictions

The theory now makes several unusually sharp predictions from a very simple gedanken experiment.

### P1 — probability-window law

For a narrow positive delay feature translated `z1 -> z2`, the low-frequency change is proportional to the probability of generation between those depths, Eq. (3).

### P2 — monotonic relocation law

For positive local added delay, the mean timing perturbation cannot reverse sign as the feature is translated downstream, Eq. (4).

### P3 — optical reconstruction

In the deterministic point-feature limit, normalized relocation-response magnitude exactly equals `p_lambda(z)`, Eq. (14).

### P4 — transport reconstruction

The unwrapped spatial phase gradient exactly equals `omega q(z)`, Eq. (15).

### P5 — wavelength/frequency collapse

Every wavelength and RF frequency must reconstruct the same `q(z)`, Eq. (19).

### P6 — complex translation sum rule

The integrated complex relocation gradient is exactly `-i omega A_h`, independent of wavelength and baseline transport, Eq. (17).

### P7 — sharp-edge spectral window

In the ideal graded-gap limit, translating the feature creates a spectral top-hat whose edges are set only by the local bandgap at the two feature depths, Eqs. (27)-(29).

Any one of these can fail experimentally. Their failure patterns discriminate the assumptions that failed.

---

# 15. Why this is a stronger theoretical direction

The earlier project asked whether a broad unknown internal transport profile could be reconstructed from wavelength-dependent timing.

That inverse is intrinsically smooth and poorly conditioned.

The translated-perturbation gedanken experiment changes the mathematical object:

```text
static unknown profile
-> integral sensitivity kernel

known translated perturbation
-> derivative of sensitivity kernel

point-feature limit
-> local complex field.
```

In the deterministic model this produces an exact separation of optical generation and local transport from one complex response field.

That is a much stronger theoretical statement than the previous numerical observation that a buried translated feature was easier to distinguish from contacts.

---

# 16. Immediate next theory work

1. derive `J_{lambda,omega}(z)` explicitly for the first-passage drift-diffusion model and determine which deterministic sum rules survive;
2. obtain the low-frequency stochastic limit in terms of first-passage/occupation-time moments;
3. derive perturbative corrections to Eqs. (14)-(19) in small diffusion/Peclet number;
4. derive the Fisher-resolution scaling for finite feature width and multiple `(lambda,omega)` channels;
5. then return to HgCdTe as a worked falsifiable example;
6. perform a focused primary-source audit specifically for translated/internal-perturbation inverse methods before any priority language.

Numerical regression:

`numerics/translation_response_theorem.py`
