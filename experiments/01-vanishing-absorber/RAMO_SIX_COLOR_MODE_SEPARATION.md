# Six-Color Shockley-Ramo Closure — Exact Two-Mode Separation Witness

**Date:** 2026-08-10  
**Status:** **DERIVED / CHECKED** algebraic identifiability theorem for a two-mode first-difference sequence; Hankel/Prony mathematics itself is established and not a novelty claim

## 1. Why rank two is not automatically useful

The reduced paper core uses six internal source coordinates when the one-mode four-color closure fails.

Five first differences are then tested for spatial rank two.

But a skeptical objection remains:

> **Even if the noiseless sequence has rank two, can the two modes actually be separated when their spatial exponents are close or one amplitude is weak?**

There is an exact answer.

---

## 2. Two-mode first-difference sequence

Let

```math
\boxed{
d_m=a q_1^m+b q_2^m,
\qquad m=0,1,2,3,4.
}
\tag{1}
```

Here

```text
d_m = J_{m+1}-J_m
```

and

```math
q_j=e^{r_j h}
```

are the two spatial multipliers over internal-source spacing `h`.

The complex amplitudes `a,b` include all mode weights, boundary amplitudes, carrier-current prefactors, and rigid optical-source transform factors.

---

## 3. Exact adjacent Hankel-minor identity

Define

```math
\boxed{
W_m
=d_m d_{m+2}-d_{m+1}^2,
\qquad m=0,1,2.
}
\tag{2}
```

Substitute Eq. (1):

```math
\begin{aligned}
W_m
&=ab
\left(
q_1^m q_2^{m+2}
+q_2^m q_1^{m+2}
-2q_1^{m+1}q_2^{m+1}
\right)\\
&=ab(q_1q_2)^m(q_1-q_2)^2.
\end{aligned}
```

Therefore

```math
\boxed{
W_m
=ab(q_1q_2)^m(q_1-q_2)^2.
}
\tag{3}
```

This is the exact two-mode separation witness.

---

## 4. Structural identifiability boundary

Equation (3) vanishes if

```text
a = 0,
b = 0,
or q1 = q2.
```

Thus two modes become structurally indistinguishable when

```text
one mode has zero observable amplitude
or
the two spatial multipliers coincide.
```

More importantly, for nearby roots

```math
|W_m|
\propto
|a b|\,|q_1-q_2|^2.
```

So the direct observable evidence for two distinct modes collapses **quadratically** as the roots merge.

This is the correct warning to attach to every six-color root-recovery claim.

---

## 5. A compact six-color rank-two closure

The minors themselves form a geometric sequence:

```math
\boxed{
\frac{W_{m+1}}{W_m}=q_1q_2
}
\tag{4}
```

whenever the denominator is nonzero.

Therefore six colors imply the parameter-free identity

```math
\boxed{
W_1^2=W_0W_2.
}
\tag{5}
```

Equation (5) is an alternative scalar form of the rank-two closure.

It complements the standard `3x3` Hankel determinant

```math
\det
\begin{pmatrix}
d_0&d_1&d_2\\
d_1&d_2&d_3\\
d_2&d_3&d_4
\end{pmatrix}=0.
```

The `W_m` representation is particularly useful because it simultaneously exposes the **mode-separation scale**.

---

## 6. Recover the root product directly

Equation (4) gives

```math
\boxed{
P\equiv q_1q_2
=\frac{W_1}{W_0}
=\frac{W_2}{W_1}.
}
\tag{6}
```

The equality of the two ratios is another overdetermined check.

Once `P` is known, the second-order recurrence

```math
\boxed{
d_{m+2}=S d_{m+1}-P d_m
}
\tag{7}
```

gives

```math
S=q_1+q_2.
```

Then

```math
q_{1,2}
=\frac{S\pm\sqrt{S^2-4P}}{2}.
```

The discriminant is

```math
\boxed{
S^2-4P=(q_1-q_2)^2.
}
\tag{8}
```

So the same root-separation quantity appears independently in the Hankel minor and the quadratic root map.

---

## 7. Why direct recurrence inversion becomes unstable

A common noiseless recovery uses

```math
\begin{pmatrix}
d_1&-d_0\\d_2&-d_1\end{pmatrix}
\begin{pmatrix}S\\P\end{pmatrix}
=
\begin{pmatrix}d_2\\d_3\end{pmatrix}.
```

The determinant of this coefficient matrix is exactly

```math
\boxed{
\det M
=d_0d_2-d_1^2
=W_0.
}
\tag{9}
```

Thus the direct recurrence-coefficient estimator has sensitivity proportional to

```math
1/|W_0|
\propto
\frac{1}
{|ab|\,|q_1-q_2|^2}
```

near the singular boundary.

Root extraction then contains an additional inverse discriminant through

```math
\sqrt{S^2-4P}=q_1-q_2.
```

The exact noise exponent depends on estimator and perturbation direction, so no universal cubic error law is asserted.

The robust conclusion is simpler:

> **two-mode root recovery becomes rapidly ill-conditioned as the observable mode amplitudes vanish or the spatial multipliers merge.**

---

## 8. Physical interpretation

The theorem gives a quantitative meaning to phrases such as

```text
"the second carrier is too weak to resolve"
```

or

```text
"the boundary mode is nearly degenerate with the bulk mode."
```

The relevant observable scale is

```math
\boxed{
|ab|\,|q_1-q_2|^2.
}
```

Not merely

```text
the number of colors
```

or

```text
the formal rank in exact arithmetic.
```

This should be propagated into every material-specific six-color forecast.

---

## 9. Relation to boundary and two-carrier mechanisms

### Finite scalar boundary

The two `q_j` come from roots of one scalar drift-diffusion-recombination quadratic.

The mode-separation theorem says whether those roots can be resolved from the spatial samples before applying the Vieta RF constraints.

### Electron-hole pair

The amplitudes `a,b` encode the relative Ramo strengths of the electron and hole modes.

If one carrier contributes negligibly over the measured spectral/RF band, `ab -> 0` and the six-color data correctly collapse toward effective rank one.

Thus the hierarchy does not force a two-carrier interpretation when the second carrier is physically invisible.

---

## 10. Numerical regression

`numerics/ramo_six_color_mode_separation.py`

verifies

```text
W_m = a b (q1 q2)^m (q1-q2)^2
W1/W0 = q1 q2
W1^2 = W0 W2
recovery of S=q1+q2 and P=q1q2
W0 ~ (q1-q2)^2 near root coalescence
strong growth of recurrence-estimator sensitivity as W0 -> 0.
```

---

## 11. Paper-level role

This theorem closes an important logical gap in the six-color hierarchy.

The manuscript should not say

> "six colors determine two modes."

without qualification.

The defensible statement is

> **Six colors provide an exact rank-two closure and, when the observable witness `|ab(q1-q2)^2|` is sufficiently above noise, permit recovery of the two spatial multipliers.  The recovery becomes singular when either mode disappears or the roots coalesce.**

This makes the model-order test falsifiable and quantitatively honest rather than purely formal.
