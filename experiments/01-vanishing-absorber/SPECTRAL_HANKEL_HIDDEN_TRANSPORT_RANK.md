# Spectral Hankel Rank — Counting Hidden Transport Modes with Equally Spaced Colors

**Date:** 2026-08-10  
**Status:** classical finite-dimensional realization/Hankel-rank mathematics applied to an internal spectral-depth coordinate; exact under stated homogeneous linear propagation assumptions; no novelty claim for the mathematics

## 1. From one propagation mode to hidden transport state

The three-color law

```math
H_1^2=H_0H_2
```

tests whether one scalar exponential propagation mode describes the measured response over equally spaced internal depths.

If it fails, there are several possibilities:

```text
spatial inhomogeneity,
optical-kernel evolution,
boundary effects,
or transport carrying unresolved internal state.
```

Suppose the optics and spatial homogeneity have been independently controlled well enough that hidden transport state is a serious candidate.

Then the natural question is not immediately

> Is there a particular trap model?

It is

> **How many observable propagation degrees of freedom are required by the data?**

There is an exact algebraic hierarchy for that question.

---

## 2. Finite-dimensional homogeneous propagation

At one fixed RF/Laplace frequency `s`, let the internal transport state be an `n`-component vector.

Propagation over one equal spatial interval

```math
\Delta z
```

is represented by one matrix

```math
M_s.
```

For a source at the `m`th equally spaced coordinate, a scalar measured response can be written

```math
\boxed{
y_m=c^TM_s^m b.
}
\tag{1}
```

Here

```text
b -> source/initial-state vector
M_s -> one-step homogeneous propagation operator
c -> scalar readout/collection vector.
```

No diagonalization is assumed.

This encompasses, for example,

```text
multiple mobile populations,
mobile + trapped states,
energy/momentum state variables,
or any finite linear internal-state model
```

at the level of the fixed-frequency propagation equation.

---

## 3. Cayley-Hamilton gives an exact recurrence

Let the characteristic polynomial of `M` be

```math
p(r)
=r^n+a_{n-1}r^{n-1}+\cdots+a_1r+a_0.
```

Cayley-Hamilton gives

```math
M^n+a_{n-1}M^{n-1}+\cdots+a_0I=0.
```

Multiply by `c^T M^m` on the left and `b` on the right:

```math
\boxed{
y_{m+n}
+a_{n-1}y_{m+n-1}
+\cdots
+a_0y_m
=0.
}
\tag{2}
```

Thus every finite-dimensional homogeneous propagation model produces a scalar spatial-response sequence obeying a finite-order linear recurrence.

This remains true for non-diagonalizable matrices.

---

## 4. Hankel rank theorem

Build the Hankel matrix

```math
\boxed{
\mathcal H_{pq}=y_{p+q}.
}
```

A finite block can be factorized as

```math
\mathcal H
=
\begin{pmatrix}
c^T\\c^TM\\c^TM^2\\\vdots
\end{pmatrix}
\begin{pmatrix}
b&Mb&M^2b&\cdots
\end{pmatrix}.
```

Therefore

```math
\boxed{
\operatorname{rank}\mathcal H\le n.
}
\tag{3}
```

Hence every

```math
(n+1)\times(n+1)
```

Hankel determinant must vanish:

```math
\boxed{
\det[y_{i+j}]_{i,j=0}^{n}=0.
}
\tag{4}
```

The observable rank can be lower than the internal state dimension if some states are not excited or not visible at the readout.

Thus Hankel rank measures the **minimal observable realization order**, not automatically the microscopic number of physical carrier states.

---

## 5. Rank one — the three-color law

For `n=1`,

```math
y_m=Cr^m.
```

The `2x2` Hankel determinant is

```math
\det
\begin{pmatrix}
y_0&y_1\\y_1&y_2\end{pmatrix}
=y_0y_2-y_1^2.
```

Therefore rank-one propagation requires

```math
\boxed{
y_1^2=y_0y_2.}
\tag{5}
```

This is exactly the three-color geometric-mean closure.

So the existing three-color law is the first member of a much larger rank hierarchy.

---

## 6. Rank two — five-color closure

Suppose two observable propagation modes are required.

Generically

```math
y_m=c_1r_1^m+c_2r_2^m,
```

although Eq. (2) also covers non-diagonalizable cases.

The three-color relation need not hold.

But five equally spaced internal coordinates supply

```math
y_0,y_1,y_2,y_3,y_4,
```

and rank at most two requires

```math
\boxed{
\det
\begin{pmatrix}
y_0&y_1&y_2\\
y_1&y_2&y_3\\
y_2&y_3&y_4
\end{pmatrix}
=0.
}
\tag{6}
```

Thus a possible experimental pattern is

```text
three-color/rank-1 closure fails
but
five-color/rank-2 closure passes.
```

That would be direct evidence that **one scalar propagation coordinate is insufficient but a two-dimensional homogeneous linear propagation state is sufficient over the measured region/frequency**.

It would not yet say what the second state physically is.

---

## 7. General color-count hierarchy

To test

```math
\operatorname{rank}\le n,
```

one convenient square Hankel null uses

```math
2n+1
```

consecutive equally spaced source coordinates:

```math
y_0,\ldots,y_{2n}.
```

Then test

```math
\boxed{
\det
\begin{pmatrix}
y_0&y_1&\cdots&y_n\\
y_1&y_2&\cdots&y_{n+1}\\
\vdots&\vdots&\ddots&\vdots\\
y_n&y_{n+1}&\cdots&y_{2n}
\end{pmatrix}
=0.
}
\tag{7}
```

So the hierarchy is

```text
3 colors -> test observable rank <=1
5 colors -> test rank <=2
7 colors -> test rank <=3
etc.
```

In noisy data, singular values / structured low-rank likelihood tests are preferable to raw determinants.

---

## 8. Why this is more general than a sum of exponentials

If `M` is diagonalizable, Eq. (1) reduces to a sum of exponentials in spatial step number.

But if `M` contains Jordan blocks, terms like

```math
m^q r^m
```

appear.

The simple distinct-exponential representation then fails, while the Cayley-Hamilton recurrence and Hankel-rank theorem remain exact.

The numerical regression explicitly tests such a non-diagonalizable realization.

Thus the rank statement is the safer theorem.

---

## 9. Broad rigidly translated generation kernels

For point generation, the state is propagated from one well-defined source coordinate.

Now let one finite optical generation shape `g(u)` be translated through a homogeneous vector propagation region.

If the point response is

```math
c^Te^{Az}b,
```

then averaging over a translated kernel centered at `z_g` gives

```math
\begin{aligned}
y(z_g)
&=\int g(u)c^Te^{A(z_g+u)}b\,du\\
&=c^Te^{Az_g}
\left[
\int g(u)e^{Au}du
\right]b.
\end{aligned}
```

The finite kernel therefore only changes the effective source vector.

It does **not** increase the propagation-state dimension as long as its shape translates rigidly.

Consequently the same Hankel-rank hierarchy survives finite fixed optical width.

Kernel-shape evolution with wavelength remains a correction that must be modeled or calibrated.

---

## 10. Important DC-normalization caveat

For a scalar one-mode process, dividing RF response by DC response preserves a single exponential and therefore the three-color law.

For a general hidden-state process, however,

```math
H_{norm}(z)
=\frac{N_{RF}(z)}{N_{DC}(z)}
```

is a **ratio** of two finite-dimensional spatial sequences and need not itself have the same finite Hankel rank.

Therefore hidden-state rank analysis should preferentially use

```text
absolute/de-embedded complex RF response per calibrated incident optical amplitude
```

or reconstruct the RF numerator using the separately measured DC response.

The DC and RF spatial sequences can then each be tested for finite realization rank.

Do not blindly apply Eq. (7) to an arbitrary RF/DC ratio in the multistate case.

---

## 11. Physical interpretation of rank patterns

### Rank 1 passes

Consistent with one scalar homogeneous propagation mode over the tested region at that RF.

Ordinary scalar drift-diffusion is one possibility, but not the only one.

### Rank 1 fails, rank 2 passes

At least two observable propagation degrees of freedom are required under the homogeneous finite-state assumption.

Candidates include

```text
mobile + trapped population,
two carrier subpopulations,
energy-relaxation state,
valley/subband state,
or another hidden linear mode.
```

### Rank keeps increasing with added colors

Possible interpretations include

```text
continuous/distributed memory,
spatial inhomogeneity,
strong optical-kernel evolution,
nonlinear transport,
or simply insufficient signal-to-noise / bad coordinate calibration.
```

A high apparent rank is not automatically exotic physics.

---

## 12. RF frequency adds another axis

The rank can be tested independently at each RF frequency.

That produces a new observable:

```math
\boxed{r_{obs}(\omega)=\text{minimal supported spatial Hankel rank}.}
```

A frequency-dependent observable rank would be particularly informative.

For example, a slow hidden state may be invisible at low RF but become dynamically distinguishable near its characteristic exchange/relaxation scale.

Thus the experiment can ask not only

> what are the effective transport coefficients?

but

> **how many transport degrees of freedom become dynamically visible as RF frequency increases?**

This is a model-selection statement before microscopic interpretation.

---

## 13. Relation to system-identification prior art

Hankel rank, finite linear recurrences, Prony-type exponential reconstruction, Cayley-Hamilton realizations, and minimal-state realization theory are established mathematical/control-system tools.

Therefore **none of the rank mathematics is claimed as new**.

The candidate detector application is:

> **use wavelength-selected, equally spaced internal generation coordinates to convert a graded photodetector into a spatial realization-order test for hidden carrier-transport state.**

A focused prior-art audit is required before any priority claim.

---

## 14. Numerical regression

`numerics/spectral_hankel_hidden_transport_rank.py`

checks:

```text
rank 1:
2x2 Hankel determinant vanishes

rank 2:
2x2 determinant is nonzero but 3x3 determinant vanishes

rank 3 with a Jordan block:
3x3 determinant is nonzero but 4x4 determinant vanishes.
```

It also verifies the exact Cayley-Hamilton recurrence for each realization.

---

## 15. Why this matters to the paper

The three-color law can now be presented as more than a special identity.

It is the first rung of a **spectral hidden-state dimension hierarchy**:

```text
three colors
-> is one scalar propagation mode sufficient?

five colors
-> if not, are two modes sufficient?

seven colors
-> if not, are three modes sufficient?
```

Only after the minimal observable dimension is established should the paper ask whether those modes correspond to ordinary drift/diffusion, traps, hot-carrier energy, multiple populations, or another physical mechanism.

This is closely aligned with the project's theory-first principle:

> **measure the minimum structure the data require before assigning microscopic meaning to it.**
