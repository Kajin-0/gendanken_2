# HgCdTe Spectral Timing Linear Inverse — Reconstructing Delay Density Without Differentiating Noisy Data

**Date:** 2026-08-09  
**Status:** exact linear-operator formulation under a path-additive mean-delay model with known optical generation kernels; synthetic inversion target; no novelty claim

## 1. Purpose

The pointwise spectral timing inversion

```math
v_{\rm eff}=1/[G(dT/dE_\gamma)]
```

is simple but numerical differentiation amplifies measurement noise.

Finite optical depth also turns the point measurement into a spatially averaged one.

There is a better formulation.

Because carrier collection delay is linear in the local **delay density**

```math
q(x)=1/v_{\rm eff}(x),
```

the complete wavelength-resolved mean-delay data form a linear inverse problem for `q(x)`.

No derivative is required.

---

## 2. Generation distribution

For wavelength / photon energy index `i`, let

```math
\boxed{
p_i(x)
=p(x|E_{\gamma,i},{\rm abs})
}
```

be the normalized conditional generation-position density inside the active region:

```math
\int_0^L p_i(x)dx=1.
```

The kernel may come from

- Beer-Lambert absorption in a graded material;
- a transfer-matrix / FDTD optical calculation;
- a measured/calibrated optical model.

No power-law edge assumption is required for the linear inverse below.

---

## 3. Path-additive mean collection time

Define local delay density

```math
\boxed{
q(s)=\frac1{v_{\rm eff}(s)}.
}
```

For a carrier generated at `x`, let the mean collection delay be

```math
\boxed{
T(x)
=\int_x^L q(s)ds.
}
```

The mean intrinsic delay at photon energy `i` is

```math
\boxed{
\bar T_i
=\int_0^L p_i(x)T(x)dx.
}
```

Substitute `T(x)`:

```math
\bar T_i
=\int_0^L p_i(x)
\left[
\int_x^L q(s)ds
\right]dx.
```

---

## 4. Swap the integration order

The region of integration is

```text
0 <= x <= s <= L.
```

Therefore

```math
\bar T_i
=\int_0^L q(s)
\left[
\int_0^s p_i(x)dx
\right]ds.
```

Define the cumulative generation kernel

```math
\boxed{
K_i(s)
\equiv
P(X_g\le s|E_{\gamma,i},{\rm abs})
=\int_0^s p_i(x)dx.
}
```

Then

```math
\boxed{
\bar T_i
=\int_0^L K_i(s)q(s)ds.
}
```

This is the central linear-operator identity.

---

## 5. Physical interpretation of the cumulative kernel

A local delay element `q(s) ds` contributes to a detected event only if that event was generated **upstream** of position `s`.

The probability of that condition is exactly

```math
K_i(s)=P(X_g\le s).
```

So the timing kernel is not the local absorption density itself.

It is its **cumulative distribution**.

This is why the timing inversion is naturally linear in `q=1/v`.

---

## 6. Discrete inverse problem

Discretize the device into spatial cells `j` of widths `Delta x_j`.

Let

```math
q_j\approx q(x_j).
```

For measured wavelength `i`, define

```math
\boxed{
A_{ij}=K_i(x_j)\Delta x_j.
}
```

Then

```math
\boxed{
\mathbf T
=\mathbf A\mathbf q.
}
```

This is a standard linear inverse problem.

The unknown is the **spatial delay density** `q`, from which

```math
\boxed{
v_{\rm eff}(x_j)=1/q_j.}
```

provided `q_j>0`.

---

## 7. Include common readout delay as a nuisance parameter

Suppose every timing datum contains a wavelength-independent electronics / cable / amplifier delay `c`:

```math
\boxed{
T_i^{\rm meas}
=\sum_jA_{ij}q_j+c.
}
```

Augment the system with one constant column:

```math
\boxed{
\mathbf T^{\rm meas}
=
\begin{bmatrix}
\mathbf A & \mathbf 1
\end{bmatrix}
\begin{bmatrix}
\mathbf q\\
c
\end{bmatrix}.
}
```

Thus the common delay can be estimated simultaneously instead of removed by numerical differentiation.

This is a major practical advantage of the full inverse formulation.

---

## 8. Regularization

The matrix is generally ill conditioned because neighboring wavelength kernels overlap strongly.

A natural smoothness-regularized estimate is

```math
\boxed{
(\hat{\mathbf q},\hat c)
=\arg\min
\left\|
\mathbf A\mathbf q+c\mathbf1-\mathbf T^{\rm meas}
\right\|_2^2
+
\lambda
\left\|
\mathbf D_2\mathbf q
\right\|_2^2,
}
```

where `D_2` is a second-difference operator.

Physical constraints may additionally impose

```math
\boxed{q_j>0.}
```

More sophisticated inversions can use

- positivity-constrained least squares;
- Bayesian smoothness priors;
- total variation if sharp transport interfaces are expected;
- parameterized transport models instead of free `q_j`.

The repository should not choose one method as universally optimal.

---

## 9. Sharp-generation limit recovers the derivative result

If wavelength `i` creates carriers at a sharply localized position `x_g`, then

```math
p_i(x)\to\delta(x-x_g).
```

Therefore

```math
K_i(s)\to H(s-x_g),
```

and

```math
\bar T(E_\gamma)
=\int_{x_g(E_\gamma)}^Lq(s)ds.
```

Differentiating gives

```math
\boxed{
G\frac{d\bar T}{dE_\gamma}
=q[x_g(E_\gamma)],
}
```

which is exactly

```math
\boxed{
v_{\rm eff}
=1/[G(dT/dE_\gamma)].
}
```

So the derivative tomography is the singular-kernel limit of the full linear inverse.

---

## 10. Finite-depth kernel connection

For the linear-gap power-law edge model, the generation density relative to the first allowed point becomes a stationary Weibull kernel away from the downstream truncation.

The full operator then represents a smoothed cumulative version of that optical point-spread function.

This makes the hierarchy clear:

```text
sharp optical localization
-> pointwise derivative tomography

finite known optical kernel
-> linear deconvolution for q(x)

unknown optical kernel
-> transport and optics are not separately identifiable without additional information.
```

---

## 11. Identifiability

The inversion requires sufficiently diverse kernels `K_i(s)`.

If all wavelengths generate the same spatial distribution, the rows of `A` are nearly identical and the internal delay profile cannot be recovered.

A monotonic graded gap is useful precisely because it causes the generation kernel to move spatially with photon energy.

The entrance-gap crossover marks the point where this spatial scan saturates:

```math
E_\gamma\ge E_{g,\rm in}
\quad\Rightarrow\quad
x_g\to0.
```

Wavelengths far above the entrance gap therefore add little new **position-tomography rank** in the sharp-limit model. Their value is instead in probing hot-carrier injection and scattering.

---

## 12. Spatial resolution

The inverse cannot resolve transport structure much finer than the wavelength-dependent optical generation kernels permit.

A local absorption length / Weibull scale `ell_alpha` therefore acts as an approximate point-spread length.

Additional resolution limits come from

- wavelength sampling density;
- spectral linewidth of the source;
- uncertainty in `E_g(x)`;
- timing noise;
- regularization strength;
- nonlocal carrier transport.

Thus this is not unlimited tomography.

Its value is that the resolution is physically calculable from detector optics rather than guessed.

---

## 13. Synthetic reconstruction target

A meaningful numerical falsification should use

```text
known nonuniform velocity v_true(x)
+
finite wavelength-dependent generation kernels
+
unknown common timing offset
+
added timing noise.
```

Generate

```math
\mathbf T_{\rm synth}
=\mathbf A\mathbf q_{\rm true}
+c\mathbf1
+\boldsymbol\epsilon,
```

then reconstruct `q` without giving the inversion the true profile.

Success should be judged by

- profile reconstruction error;
- recovery of a localized slow/fast region;
- common-delay recovery;
- stability versus timing noise;
- resolution versus optical kernel width.

A regression implementing this test accompanies the present note.

---

## 14. Experimental observable

The preferred data are low-frequency group delay or impulse centroid versus wavelength under identical detector conditions.

Absolute waveform rise time is less attractive because multiple poles and threshold conventions obscure the linear transit interpretation.

If

```math
H_{\rm meas}(\Omega,E_\gamma)
=H_{\rm det}(\Omega,E_\gamma)
H_{\rm common}(\Omega),
```

and `H_common` is wavelength independent, its group delay enters as the fitted nuisance constant `c`.

A wavelength-dependent optical path delay must be calibrated separately.

---

## 15. Reviewer-level significance test

The algebra alone is not enough for publication significance.

Wavelength-dependent carrier generation and response time are old photodiode physics.

The useful question is whether this inverse formulation can recover transport information that ordinary bandwidth comparison does not.

A convincing result would demonstrate at least one of

- reconstruction of a nonuniform carrier-velocity profile;
- detection/localization of a slow transport layer;
- independent agreement with a transport simulation;
- recovery of a profile from real wavelength-resolved timing data.

Until then, treat this as a candidate measurement method rather than a new detector principle.

---

## 16. Claim boundary

### Derived

```math
\boxed{
\bar T_i
=\int_0^L K_i(s)q(s)ds,
\qquad
K_i(s)=P(X_g\le s|E_i,{\rm abs}).
}
```

and the corresponding discrete linear system including a constant timing nuisance parameter.

### Conditional

- path-additive mean delay;
- known/calibrated optical generation kernels;
- wavelength-independent additive common delay;
- sufficient kernel diversity for inversion.

### Not established

- experimental stability in HgCdTe;
- unique high-resolution reconstruction for arbitrary profiles;
- calibrated HgCdTe kernels;
- novelty / priority.

---

## 17. Next decisive work

1. run the synthetic inversion regression;
2. quantify reconstruction error versus timing-noise level and optical kernel width;
3. estimate the timing precision required for micron/submicron spatial resolution in a plausible HgCdTe gradient;
4. only then decide whether a real-device inverse design is justified.
