# Arbitrary Spectral-Depth Spacing and Calibration Uncertainty

**Date:** 2026-08-11  
**Status:** **DERIVED / CHECKED / CONDITIONAL**; response to adversarial review of the wavelength-to-depth calibration requirement

## 1. Equal spacing is convenient, not fundamental

The headline four-color identity assumes equally spaced internal source coordinates because this turns the one-mode sequence into a geometric progression.

But the underlying one-mode model is

```math
\boxed{
J(z)=A+B e^{rz}.
}
\tag{1}
```

If the four actual calibrated source positions are known but not equally spaced, the model remains overdetermined.

Let

```math
\Delta_m=z_{m+1}-z_m,
```

and

```math
d_m=J_{m+1}-J_m.
```

Then

```math
\boxed{
d_m
=B e^{rz_m}(e^{r\Delta_m}-1).
}
\tag{2}
```

Therefore

```math
\boxed{
\frac{d_1}{d_0}
=e^{r\Delta_0}
\frac{e^{r\Delta_1}-1}
{e^{r\Delta_0}-1}.
}
\tag{3}
```

The first three source coordinates determine the single complex exponent `r` numerically, with the physical log/root branch tracked continuously.

The fourth coordinate predicts

```math
\boxed{
\left(\frac{d_2}{d_1}\right)_{pred}
=e^{r\Delta_1}
\frac{e^{r\Delta_2}-1}
{e^{r\Delta_1}-1}.
}
\tag{4}
```

Thus the falsification logic survives arbitrary **known** source spacing.

For

```math
\Delta_0=\Delta_1=\Delta_2=h,
```

Eqs. (3)-(4) reduce immediately to

```math
\frac{d_1}{d_0}
=\frac{d_2}{d_1}
=e^{rh},
```

which is the simple four-color geometric closure.

---

## 2. Consequence for wavelength-to-depth calibration

A known nonlinear map

```math
z=f(\lambda)
```

does **not** by itself create a false model-order failure.

It simply means the actual nonuniform positions should be used in Eqs. (3)-(4) rather than pretending that the source coordinates are equally spaced.

The dangerous quantity is therefore

```text
uncertainty in the calibrated source positions,
not nonlinearity of the calibration map itself.
```

This is a more accurate statement than saying that the method fundamentally requires an affine wavelength-to-depth map.

---

## 3. Exact first-order sensitivity to position errors around equal spacing

Let the intended equal positions be

```math
z_m^{(0)}=z_0+mh,
```

and let the true positions contain small errors

```math
z_m=z_m^{(0)}+\epsilon_m.
```

For the exact one-mode sequence, define

```math
q=e^{rh}.
```

Linearizing the logarithmic equal-spacing closure gives

```math
\boxed{
\delta\mathcal C_4
=\frac{r}{q-1}
\left[
\epsilon_0-(q+2)\epsilon_1
+(2q+1)\epsilon_2-q\epsilon_3
\right].
}
\tag{5}
```

At small `|rh|`,

```math
\boxed{
\delta\mathcal C_4
\simeq
\frac{
\epsilon_0-3\epsilon_1+3\epsilon_2-\epsilon_3
}{h}
+O(r\epsilon).
}
\tag{6}
```

The leading position-error sensitivity is again the third-difference stencil.

Consequences:

- common position offset cancels;
- common scale/linear drift cancels;
- smooth low-order correlated calibration errors are much less dangerous than independent channel-by-channel position errors;
- arbitrary known offsets can be handled exactly with the unequal-spacing closure rather than treated as errors.

---

## 4. Smooth quadratic calibration curvature

To connect with the manuscript's previous local formula, parameterize a smooth calibration distortion as

```math
\boxed{
z
=\mu
+\frac{c}{2}(\mu-\mu_c)^2.
}
\tag{7}
```

Here `c` has units of inverse length.

For a quartet with nominal spacing `h`, the three true spacings are

```math
h(1-ch),
\qquad
h,
\qquad
h(1+ch).
```

If one incorrectly applies the equal-spacing geometric identity rather than using the known true spacings, the low-order closure bias is

```math
\boxed{
\mathcal C_{4,coord}
=h^2\left[rc+c^2\right]
+O(h^4c, c^3).
}
\tag{8}
```

The `rc` term gives the leading RF phase bias; the `c^2` term gives a small DC/amplitude bias.

This is consistent with the earlier differential expression

```math
\mathcal C_{4,coord}
=h^2[r f''-(\ln f')''].
```

---

## 5. Worked HgCdTe curvature tolerance if equal spacing is assumed blindly

Take the manuscript quartet

```text
2.5, 3.0, 3.5, 4.0 um
```

with

```text
h = 0.5 um
quartet center = 3.25 um
```

and the homogeneous path-harmonic velocity used for the optical control.

For the quadratic distortion in Eq. (7), the exact point-source one-mode calculation shows that a curvature of only approximately

```text
c ~ 0.0042-0.0046 per um
```

produces a phase bias equal to 10% of the current worked HgCdTe gradient-sensitive signal over `100 MHz-1 GHz`.

At the outer quartet points, whose nominal distance from the quartet center is `0.75 um`, this corresponds to a nonlinear endpoint displacement

```math
\delta z_{edge}
=\frac12 c(0.75\ \mu m)^2
```

of only about

```text
~1.2-1.3 nm.
```

This is a stringent requirement **if the experiment insists on using the equal-spacing identity with an imperfectly known nonlinear coordinate map.**

It should not be misread as a universal need to know absolute generation depth to one nanometer.

---

## 6. How to avoid the artificial nanometer equality requirement

The correct experimental strategy is:

1. estimate the actual mean internal coordinates and their covariance from the best optical/material calibration available;
2. use the arbitrary-spacing Eqs. (3)-(4) rather than forcing equal spacing in physical depth;
3. propagate the coordinate covariance jointly with complex-current covariance;
4. reserve the simple equal-spacing identity for cases where its additional calibration simplicity is actually justified.

Thus the paper's strongest conceptual statement should be adjusted from

```text
four equally spaced colors are mandatory
```

to

```text
four calibrated internal source coordinates overdetermine one spatial mode;
equal spacing produces the especially simple nuisance-free geometric identity.
```

---

## 7. Paper consequence

The adversarial review was correct that depth calibration needs a quantitative error budget.

The more precise conclusion is two-sided:

- **bad news:** blindly assuming equal spacing can generate transport-scale false phase from nanometer-scale nonlinear spacing errors in the current tiny-signal HgCdTe stress;
- **good news:** known nonlinear spacing can be incorporated exactly without changing model order or adding a transport parameter.

The next practical analysis should therefore estimate the covariance of the source coordinates from realistic optical/material uncertainty rather than impose an absolute equal-spacing tolerance by fiat.

Numerical regression:

`numerics/arbitrary_spacing_depth_calibration.py`
