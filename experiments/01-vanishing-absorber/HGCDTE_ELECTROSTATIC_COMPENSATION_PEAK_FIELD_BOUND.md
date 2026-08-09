# HgCdTe Electrostatic Compensation Peak-Field Bound — Why Delta Doping Cannot Make Band Alignment Field-Free

**Date:** 2026-08-09  
**Status:** exact one-dimensional electrostatic integral inequality; application to HgCdTe boundary band alignment; no novelty claim

## 1. Purpose

`HGCDTE_BOUNDARY_LAYER_TAT_TRADEOFF.md` first assumed an approximately uniform compensating field across a wide-gap collection transition.

Real HgCdTe barrier structures use composition grading, doping modulation, delta doping, depletion layers, and other electrostatic shaping. These techniques can strongly modify the band profile and are established device-engineering tools.

The adversarial question is:

> Can a nonuniform electrostatic profile provide the same minority-carrier barrier cancellation with a smaller maximum electric field than the uniform-field estimate, thereby evading the TAT width requirement?

In one dimension, no.

---

## 2. Required electrostatic compensation

Let a material gap increase `Delta E_g > 0` create a conduction-band material offset

```math
\Delta E_c^{\rm mat}=\alpha\Delta E_g.
```

To make minority-electron extraction barrier free, the electrostatic potential-energy drop across the boundary must satisfy

```math
\boxed{
qV_b\ge\alpha\Delta E_g.
}
```

The smallest compensation resource occurs at equality.

Let the entire compensating electrostatic region have width `w` and field profile `F(x)`.

Then

```math
\boxed{
V_b=\int_0^w F(x)\,dx
}
```

up to the chosen sign convention; below use the magnitude required in the collection direction.

---

## 3. Exact maximum-field inequality

For any integrable field profile of one sign,

```math
\left|\int_0^wF(x)dx\right|
\le
w\,\max_{0\le x\le w}|F(x)|.
```

Therefore

```math
\boxed{
F_{\max}
\ge
\frac{|V_b|}{w}.
}
```

Combining with the minimum barrier-free compensation gives

```math
\boxed{
F_{\max}
\ge
\frac{\alpha\Delta E_g}{qw}.
}
```

Equality requires a spatially uniform field of the required sign almost everywhere.

Thus the uniform field is not an arbitrary pessimistic choice. It is the **minimum possible peak field** for a fixed compensating voltage and physical width.

---

## 4. Consequence for doping and delta-doping profiles

Doping modulation or a delta-doped sheet can reshape the electrostatic potential so that an undesirable band discontinuity is removed.

However, once the required compensation voltage and available transition width are fixed, the integral inequality remains.

Therefore such electrostatic engineering can

- place the field preferentially in a wider-gap or cleaner region;
- reshape a conduction/valence barrier;
- reduce the field where traps are worst;
- redistribute depletion charge;

but it cannot make the required total potential drop occur with

```math
F_{\max}<V_b/w.
```

A highly localized space-charge sheet generally makes the peak field larger than the uniform-field minimum.

This is a field-allocation problem, not a free removal of the electrostatic resource.

---

## 5. Profile-independent TAT width floor

Suppose a local trap-assisted tunneling exponent is controlled by

```math
\exp(-F_{\rm TAT}/|F|).
```

To guarantee that the field nowhere exceeds

```math
F_{\rm allow}=F_{\rm TAT}/\Sigma_t,
```

where `Sigma_t` is a chosen exponent margin, it is necessary that

```math
F_{\max}\le F_{\rm allow}.
```

The peak-field inequality then gives

```math
\frac{\alpha\Delta E_g}{qw}
\le
\frac{F_{\rm TAT}}{\Sigma_t}.
```

Therefore

```math
\boxed{
w
\ge
\frac{\alpha\Delta E_g}
{qF_{\rm TAT}}
\Sigma_t.
}
```

This is exactly the width floor found from the uniform-field model, but it is now a **necessary one-dimensional peak-field condition for arbitrary electrostatic shaping**.

The earlier uniform model saturates this peak-field inequality.

---

## 6. Direct-BTBT version

If the allowed peak field is instead set by a desired direct-Zener exponent `Sigma_Z`, with local scale `F_K`, then

```math
F_{\max}\le F_K/\Sigma_Z
```

requires

```math
\boxed{
w
\ge
\frac{\alpha\Delta E_g}
{qF_K}
\Sigma_Z.
}
```

Again, nonuniform electrostatic shaping cannot beat this peak-field condition at fixed compensation voltage and width.

It may still improve the **integrated current** by placing the unavoidable high field in material with larger `F_K`, larger `F_TAT`, or lower trap density.

That distinction is important.

---

## 7. Connection to the earlier heterostructure allocation theorem

The repository already found, for heterogeneous regions, the marginal-cost rule

```math
-\frac{\partial g/\partial F}
{\partial(1/v)/\partial F}
=\lambda.
```

The present result is complementary.

The marginal-cost theorem says where a finite field resource should be placed to reduce leakage for a transport target.

The peak-field inequality says that if a definite compensation voltage must occur over a finite distance, **some point must carry at least the average field**.

Thus the best boundary design problem is not

```text
make the field disappear,
```

but

```text
spread the required potential drop and place its unavoidable field
where the material has the highest leakage tolerance.
```

This aligns naturally with wide-gap grading and delta-doped barrier design.

---

## 8. Prior-art boundary

HgCdTe barrier-detector literature already demonstrates that composition grading, doping modulation, and delta doping can eliminate or strongly reduce minority-carrier band discontinuities while suppressing dark current.

Those device concepts are not repository novelty.

The present result is only the elementary but useful accounting identity

```math
\boxed{F_{\max}\ge V_b/w}
```

combined with the HgCdTe compensation requirement.

No mathematical or physical novelty is claimed.

---

## 9. What this result does not say

It does not say

- uniform field minimizes total TAT current for every nonuniform trap profile;
- delta doping is ineffective;
- depletion engineering cannot improve a device;
- the field has one sign in every real boundary;
- interface dipoles cannot contribute to band alignment;
- the local TAT exponent alone predicts current.

If interface dipoles or nonelectrostatic band offsets provide part of the compensation, then the required electrostatic `V_b` must be reduced accordingly before applying the inequality.

---

## 10. Next physical question

With the peak-field loophole closed, the remaining practical freedom is **where to place the unavoidable electrostatic field**.

The next boundary model should therefore use measured/fitted trap spectra and ask whether the field can be concentrated in a sufficiently wide-gap, sufficiently low-defect layer that

```text
minority electron barrier ~ 0
+
peak TAT acceptable
+
direct BTBT negligible
+
transit delay negligible.
```

If that is possible, the limiting resource is no longer a generic speed law. It is control of the defect spectrum and high-field spatial placement in the heterostructure.