# Three-Color Spectral Closure Theorem — A Parameter-Free Test of Internal Depth Encoding

**Date:** 2026-08-10  
**Status:** exact under a spatially homogeneous first-passage segment plus rigid translation of the generation kernel; arbitrary fixed generation width/shape allowed; no novelty claim pending focused prior-art audit

## 1. The simplest detector-specific thought experiment

Consider a graded photodetector in which changing optical wavelength moves the carrier-generation distribution through depth.

Suppose three wavelengths

```math
\lambda_1,\lambda_2,\lambda_3
```

are chosen so their calibrated generation coordinates are equally spaced:

```math
\boxed{
z_{g,2}-z_{g,1}
=z_{g,3}-z_{g,2}
=\Delta z.
}
```

At one RF frequency, measure the **complex**, DC-normalized detector responses

```math
H_1,H_2,H_3.
```

The question is deliberately simple:

> **If wavelength is really acting as an internal spatial coordinate inside one homogeneous transport segment, what must these three complex numbers obey?**

The answer is an exact geometric-mean law.

---

## 2. Homogeneous point-source propagation

Inside a spatially homogeneous one-dimensional first-passage segment, the point-source Laplace/RF solution has an exponential spatial dependence for each complex frequency:

```math
U_s(z)=C_s e^{\gamma_s z}.
```

Here `s=i omega` for RF response.

Allow local Markov recombination/killing as well. Its DC collection field has

```math
U_0(z)=C_0e^{\gamma_0z}.
```

The DC-normalized point-source response therefore propagates as

```math
\frac{U_s(z)}{U_0(z)}
\propto
\exp[(\gamma_s-\gamma_0)z].
```

Define the conditioned propagation constant

```math
\boxed{
\Gamma(s)=\gamma_s-\gamma_0.
}
```

No explicit drift-diffusion formula for `Gamma` is needed for the spectral closure result.

---

## 3. The generation distribution may be broad

Assume wavelength translates one fixed normalized generation shape `g`:

```math
\boxed{
p_\lambda(z)=g[z-z_g(\lambda)].
}
```

Crucially, `g` may be

```text
broad,
asymmetric,
multimodal,
or otherwise complicated.
```

It does not need to approach a delta function.

The distributed-generation DC-normalized response is

```math
H(z_g,s)
=
\frac{
\int g(z-z_g)U_s(z)dz
}{
\int g(z-z_g)U_0(z)dz
}.
```

Set

```math
u=z-z_g.
```

Then

```math
\begin{aligned}
H(z_g,s)
&=
\frac{
C_s e^{\gamma_s z_g}
\int g(u)e^{\gamma_su}du
}{
C_0 e^{\gamma_0 z_g}
\int g(u)e^{\gamma_0u}du
}\\
&=B(s)e^{\Gamma(s)z_g},
\end{aligned}
```

where

```math
\boxed{
B(s)
=
\frac{C_s}{C_0}
\frac{\int g(u)e^{\gamma_su}du}
{\int g(u)e^{\gamma_0u}du}.
}
```

Therefore

```math
\boxed{
H(z_g,s)=B(s)e^{\Gamma(s)z_g}.
}
\tag{1}
```

This is exact for any fixed translated kernel whose required transforms exist and whose support remains within the homogeneous region.

---

## 4. Three-color geometric-mean law

For equally spaced generation coordinates,

```math
z_{g,1}=z_0-\Delta z,
```

```math
z_{g,2}=z_0,
```

```math
z_{g,3}=z_0+\Delta z.
```

Equation (1) gives

```math
H_1=Be^{\Gamma(z_0-\Delta z)},
```

```math
H_2=Be^{\Gamma z_0},
```

```math
H_3=Be^{\Gamma(z_0+\Delta z)}.
```

Hence

```math
\boxed{
H_2^2=H_1H_3.
}
\tag{2}
```

This is a **complex identity**.

It simultaneously predicts

```math
\boxed{
|H_2|^2=|H_1||H_3|,
}
```

and, after continuous phase unwrapping,

```math
\boxed{
2\phi_2=\phi_1+\phi_3
\quad(\mathrm{mod}\ 2\pi).
}
```

No transport coefficient appears.

---

## 5. Why finite optical generation width cancels

A common intuition is that broad absorption depth necessarily destroys a sharp internal spatial test.

Equation (1) shows that this is false for a homogeneous transport segment if the generation profile translates **rigidly**.

All details of the fixed kernel shape are absorbed into the common multiplicative factor

```math
B(s).
```

They cancel exactly from Eq. (2).

Thus the law is independent of

```text
generation width,
generation asymmetry,
generation multimodality,
absolute optical amplitude,
and the fixed shape factor.
```

The relevant optical failure mode is **shape evolution with wavelength**, not width by itself.

---

## 6. General unequal-spacing law

For arbitrary calibrated centers

```math
z_1<z_2<z_3,
```

Eq. (1) predicts one common complex spatial slope:

```math
\boxed{
\frac{
\ln H_2-\ln H_1
}{z_2-z_1}
=
\frac{
\ln H_3-\ln H_2
}{z_3-z_2}
=\Gamma(s),
}
\tag{3}
```

with continuous logarithm branches.

A branch-free exponentiated relation can be constructed when the depth ratios are rational. Equal spacing gives the particularly simple Eq. (2).

---

## 7. The spectral curvature null

Equation (1) is equivalent to

```math
\boxed{
\partial_{z_g}^2\ln H=0.
}
\tag{4}
```

Thus the second derivative of complex log response with respect to the calibrated internal generation coordinate must vanish throughout a homogeneous segment.

If the coordinate is supplied by wavelength,

```math
z_g=z_g(\lambda),
```

then

```math
\boxed{
\frac{d}{d\lambda}
\left[
\frac{1}{dz_g/d\lambda}
\frac{d\ln H}{d\lambda}
\right]
=0.
}
\tag{5}
```

Equation (5) is a wavelength-domain null test after calibrating the spectral-to-depth map.

---

## 8. What a violation means

A robust failure of Eq. (2) or Eq. (5) means at least one assumption is false.

Possible causes include

```text
transport coefficients varying with depth,
generation-kernel shape changing with wavelength,
proximity to a boundary/interface,
multiple carrier populations,
non-exponential spatial propagation,
frequency-dependent optical/electrical contamination,
or incorrect spectral-to-depth calibration.
```

The three-color law is therefore not by itself a unique test of transport nonlocality.

Its purpose is more basic:

> **validate that wavelength is functioning as the intended internal spatial coordinate inside a homogeneous propagation region before extracting transport coefficients.**

---

## 9. Optical-shape correction

If the generation kernel changes shape with wavelength,

```math
p_j(z)=g_j(z-z_{g,j}),
```

then

```math
H_j=B_j(s)e^{\Gamma z_{g,j}},
```

where

```math
B_j(s)
=
\frac{C_s}{C_0}
\frac{\int g_j(u)e^{\gamma_su}du}
{\int g_j(u)e^{\gamma_0u}du}.
```

For equally spaced centers,

```math
\boxed{
\frac{H_2^2}{H_1H_3}
=
\frac{B_2^2}{B_1B_3}.
}
\tag{6}
```

Thus calibrated optical shape evolution produces an explicit correction factor.

This is useful experimentally:

```text
uncorrected closure failure
-> could be optics or transport

optically predicted B_j correction applied
-> remaining failure tests propagation homogeneity/modeling.
```

---

## 10. Connection to the two-depth transport theorem

Once Eq. (3) is satisfied, any wavelength pair gives the same

```math
\Gamma(\omega).
```

For uniform local conditioned drift-diffusion,

```math
\Gamma(\omega)
=
\frac{
\sqrt{w^2+4iD\omega}-w
}{2D}
```

in the simple no-DC-killing representation, or the equivalent conditioned difference of roots when DC normalization is explicit.

Therefore the experimental hierarchy becomes

```text
THREE wavelengths at one RF
-> test internal spectral-coordinate/homogeneous-propagation closure

if passed:
ONE wavelength pair
-> extract Gamma(omega)

SECOND RF frequency
-> test whether inferred real D,w remain frequency independent.
```

This separates

```text
spectral-coordinate validity
from
transport-law validity.
```

---

## 11. Minimal spectral gedanken experiment

The detector-specific thought experiment can now be stated in one sentence:

> **Choose three colors that generate carriers at three equally spaced internal depths and ask whether the middle complex RF response is the geometric mean of the outer two.**

If yes, the first spatial closure is passed.

Then repeat at another RF frequency.

The same device becomes a test of the transport law without physically scanning a source through the material.

---

## 12. Sharp graded-gap realization

In an ideal monotonic graded-gap absorber with a sharp local absorption edge,

```math
E_g[z_g(\lambda)]
=hc/\lambda.
```

Thus equal depth spacing can be chosen from the known composition/gap profile.

Real absorption broadening gives a finite kernel `g`.

The theorem shows that broadening itself is harmless if its shape remains approximately translated; measured/modelled shape evolution is the correction that matters.

This is precisely why a compositionally graded absorber is interesting as a passive internal coordinate system.

---

## 13. Numerical verification

`numerics/three_color_spectral_geometric_mean_law.py`

uses an intentionally

```text
broad
asymmetric
bimodal
```

generation kernel.

It independently integrates the RF and DC fields for three translated centers and verifies to numerical precision that

```math
H_2^2=H_1H_3
```

and that both neighboring complex spatial slopes equal the imposed conditioned propagation constant.

The same script deliberately changes only the middle generation-kernel shape and confirms that the geometric-mean law is then violated.

---

## 14. Prior-art boundary

Classical photodiode theory has long modeled transit-time-limited frequency response, diffusion contributions, and wavelength-dependent carrier generation.

Therefore do not claim novelty for any of those ingredients individually.

The candidate result to audit is narrower:

> **the use of calibrated wavelength-translated internal generation kernels to impose a parameter-free complex spatial closure law, followed by multi-frequency local-transport falsification.**

Priority is unresolved.

---

## 15. Why this is likely central to the eventual paper

The theory now has a very simple experimental narrative:

```text
three colors
-> validate wavelength as an internal depth coordinate

two RF frequencies
-> validate or falsify local Markov drift-diffusion

DC spectral collection
-> undo successful-carrier conditioning

controlled local perturbation
-> spatially decompose timing cumulants / test richer path physics.
```

Each step adds information only after the previous, more general null test has survived.

That is a much cleaner paper structure than reconstructing a large arbitrary transport profile from the outset.
