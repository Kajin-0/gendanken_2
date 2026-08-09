# Active Conversion Singular-Value Resource Bound — Pump Photons Versus Number of Converted Modes

**Date:** 2026-08-08  
**Status:** exact finite-mode linear-algebra resource inequality built on established Schmidt-mode frequency-conversion theory; no novelty claim  

## 1. Purpose

Broadband quantum frequency conversion is naturally described in terms of Schmidt / singular modes. Established quantum-pulse-gate theory shows that, in the natural temporal-mode basis, frequency conversion acts as independent beamsplitter-like transformations between paired input/output modes.

This note uses that established structure to ask a narrower resource question:

> If a finite coherent pump generates the mode-conversion matrix, how much total conversion singular-value strength can that pump create?

The result is exact for a finite static bilinear converter and does not assume cavities or independent spectral bins.

---

## 2. Finite single-photon mode spaces

Let

```math
\mathbf a=(a_1,\ldots,a_M)^T
```

be orthogonal incident modes and

```math
\mathbf b=(b_1,\ldots,b_N)^T
```

be receiving/output modes.

Use a pump-linearized number-conserving conversion Hamiltonian

```math
\boxed{
\frac{H_{\rm conv}}{\hbar}
=
\mathbf b^\dagger K\mathbf a
+
\mathbf a^\dagger K^\dagger\mathbf b,
}
```

where

```math
K\in\mathbb C^{N\times M}
```

has units of angular frequency.

This describes an ideal coherent frequency converter after the classical pump has been inserted into the nonlinear interaction.

Dissipation, detuning, pump depletion, and added noise are excluded in this first resource calculation.

---

## 3. Singular-mode decomposition

Take the singular-value decomposition

```math
\boxed{
K=U\Sigma V^\dagger,
}
```

with nonzero singular values

```math
\sigma_j\ge0.
```

Define transformed mode operators

```math
\tilde{\mathbf b}=U^\dagger\mathbf b,
\qquad
\tilde{\mathbf a}=V^\dagger\mathbf a.
```

Then

```math
\boxed{
\frac{H_{\rm conv}}{\hbar}
=
\sum_j
\sigma_j
\left(
\tilde b_j^\dagger\tilde a_j
+
\tilde a_j^\dagger\tilde b_j
\right).
}
```

Thus the conversion problem decomposes into independent Rabi / beamsplitter rotations.

This singular-mode structure is established frequency-conversion theory and is not a repository novelty claim.

---

## 4. Conversion probability for each singular channel

Let the interaction act for duration

```math
\tau.
```

For one photon initially in input singular mode `j`, the exact conversion probability is

```math
\boxed{
\eta_j
=\sin^2(\sigma_j\tau).
}
```

Suppose at least `M_c` orthogonal input singular modes must each satisfy

```math
\eta_j\ge\eta,
\qquad
0<\eta\le1.
```

Define

```math
\boxed{
\theta_\eta
\equiv
\arcsin\sqrt\eta,
\qquad
0<\theta_\eta\le\pi/2.
}
```

Every such channel necessarily obeys

```math
\boxed{
\sigma_j\tau
\ge
\theta_\eta.
}
```

The inequality remains true even if a channel is over-rotated onto a later high-conversion branch, because every point with `sin^2 x >= eta` has `|x| >= theta_eta`.

---

## 5. Required conversion-matrix norm

The Frobenius/Hilbert-Schmidt norm is

```math
\|K\|_F^2
=\sum_j\sigma_j^2.
```

If `M_c` orthogonal channels meet the efficiency target,

```math
\|K\|_F^2
\ge
M_c
\frac{\theta_\eta^2}{\tau^2}.
```

Therefore

```math
\boxed{
\|K\|_F^2
\ge
\frac{M_c}{\tau^2}
\arcsin^2\sqrt\eta.
}
```

This is the minimum total conversion singular-value strength required for the stated multimode task.

---

## 6. Pump-generated conversion matrix

Let the converter be driven by coherent pump modes with complex amplitudes

```math
\alpha_p.
```

Assume the linearized conversion matrix depends linearly on those pump amplitudes:

```math
\boxed{
K(\boldsymbol\alpha)
=\sum_{p=1}^{P}
\alpha_p K_p,
}
```

where each matrix `K_p` is the conversion matrix produced by one unit pump amplitude in pump mode `p`.

Define total coherent pump photon number

```math
\boxed{
N_p
=\sum_p|\alpha_p|^2.
}
```

This is the natural finite-mode pump norm under coherent-state normalization.

---

## 7. Pump-to-conversion Gram matrix

Define

```math
\boxed{
C_{pq}
\equiv
\operatorname{Tr}
(K_p^\dagger K_q).
}
```

`C` is Hermitian positive semidefinite.

Then

```math
\|K(\boldsymbol\alpha)\|_F^2
=
\boldsymbol\alpha^\dagger
C
\boldsymbol\alpha.
```

Hence

```math
\boxed{
\|K\|_F^2
\le
\lambda_{\max}(C)
N_p.
}
```

Define the finite-device pump-to-conversion strength

```math
\boxed{
\Lambda
\equiv
\lambda_{\max}(C).
}
```

`Lambda` has units of angular-frequency squared per pump photon in the chosen mode normalization.

---

## 8. Exact pump-photon lower bound

Combine the required singular-value strength with the pump upper bound:

```math
\frac{M_c\theta_\eta^2}{\tau^2}
\le
\|K\|_F^2
\le
\Lambda N_p.
```

Therefore

```math
\boxed{
N_p
\ge
\frac{
M_c\,\arcsin^2\sqrt\eta
}{
\Lambda\tau^2
}.
}
```

This is the central finite-mode resource inequality.

It says that a coherent pump with finite photon number can create only a finite total amount of independent conversion rotation strength when the material/device conversion operator `Lambda` is fixed.

---

## 9. Equality conditions

The pump-side inequality is saturated when the coherent pump amplitude vector is an eigenvector of `C` associated with

```math
\lambda_{\max}(C)=\Lambda.
```

The conversion-side inequality is saturated when exactly `M_c` singular values are active and each obeys

```math
\sigma_j\tau=\theta_\eta
```

on the first conversion branch.

Thus exact saturation requires both

```text
optimal pump supermode
```

and

```text
equal minimum singular rotations on all required converted modes.
```

---

## 10. Approximate bandwidth–latency interpretation

A time interval of duration `T` and angular-frequency span `W` support an effective number of approximately orthogonal time-frequency degrees of freedom of order the Shannon/Slepian number

```math
M_{\rm eff}
\sim
\frac{WT}{2\pi}
```

when `WT >> 1`.

This is an asymptotic mode-counting statement, not an exact finite-dimensional identity because no nonzero function is simultaneously perfectly time- and band-limited.

If the conversion interaction time is of order the accepted temporal window,

```math
\tau\sim T,
```

then inserting

```math
M_c\sim WT/(2\pi)
```

into the exact finite-mode inequality suggests the scaling

```math
\boxed{
N_p
\gtrsim
\frac{
\arcsin^2\sqrt\eta
}{2\pi\Lambda}
\frac{W}{T}.
}
```

Equivalently,

```math
\boxed{
N_p T
\gtrsim
\frac{
\arcsin^2\sqrt\eta
}{2\pi\Lambda}
W.
}
```

This should be interpreted only as a **bandwidth–latency mode-counting corollary** under the stated identification of `T` and `tau`.

It is not yet a rigorous continuous-time detector theorem.

---

## 11. Relation to the earlier `W^2` results

The cavity and ordinary traveling-wave models produced

```text
pump resource ~ W^2
```

under their particular fixed-device assumptions.

The singular-value inequality shows why that exponent should not be assumed universal.

The more general finite-mode statement is

```text
pump photons
x
pump-to-conversion operator strength
x
interaction time^2
>=
number of efficiently converted orthogonal modes.
```

A specific architecture determines how

- `Lambda`;
- interaction time;
- number of useful modes;

scale with the desired spectral bandwidth.

Thus `W^2` is one possible architecture-level realization, not the fundamental object.

---

## 12. Prior-art collision

Temporal-mode-selective frequency conversion and Schmidt-mode decompositions are established quantum nonlinear optics.

Relevant work by Brecht, Silberhorn, Raymer, Reddy, and collaborators shows explicitly that nonlinear frequency conversion defines natural Schmidt mode pairs whose conversion efficiencies are independent beamsplitter-like coefficients.

Therefore this repository does **not** claim novelty for

- Schmidt modes of frequency conversion;
- singular-mode conversion channels;
- pump shaping to select temporal modes;
- multimode quantum pulse gates.

The only added step here is resource bookkeeping with a finite coherent pump norm and a pump-to-conversion Gram operator.

Its priority is unassessed and no novelty is claimed.

---

## 13. What remains hidden in `Lambda`

The entire microscopic nonlinear optical resource is now concentrated into

```math
\boxed{
\Lambda
=\lambda_{\max}(C).
}
```

A real device determines `Lambda` through

- nonlinear susceptibility;
- interaction volume / length;
- field normalization;
- phase matching;
- spatial and temporal mode overlap;
- material oscillator strengths and dispersion.

If device size/material amount can be increased without constraint, `Lambda` can generally increase and the pump-photon requirement can fall.

Therefore `Lambda` must not be treated as a universal constant.

---

## 14. Claim boundary

### Derived exactly for the finite static bilinear converter

If `M_c` orthogonal singular channels each convert with probability at least `eta` during time `tau`, and the pump-generated coupling satisfies

```math
K=\sum_p\alpha_pK_p,
```

then

```math
\boxed{
N_p
\ge
\frac{
M_c\arcsin^2\sqrt\eta
}{
\lambda_{\max}(C)\tau^2
}.
}
```

### Not established

- novelty of this finite-mode inequality;
- an exact continuous-bandwidth version;
- a universal material bound on `Lambda`;
- validity for time-ordered noncommuting conversion Hamiltonians;
- validity for gain rather than number-conserving conversion;
- added-noise / dark-count consequences;
- a universal pump-work theorem.

---

## 15. Next decisive question

The active problem has now been reduced to two possible routes:

1. derive a physical upper bound on `Lambda` from a finite nonlinear material / Maxwell resource; or
2. find an explicit time-dependent/control counterexample showing that noncommuting pump protocols can outperform any static singular-value resource accounting at fixed pump energy.

The second attack is particularly important because time-modulated absorbers are already known to beat passive Bode–Fano limits by storing incident energy and changing the system after the pulse arrives.

Before claiming a general active resource law, the repository must test such genuinely time-dependent protocols.