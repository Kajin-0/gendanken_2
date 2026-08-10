# DC Normalization as a Doob Transform — What Photodetector RF Actually Measures

**Date:** 2026-08-10  
**Status:** **DERIVED / CHECKED** for the stated one-dimensional killed diffusion backward generator; the Doob `h`-transform itself is established probability theory, while the detector interpretation and consequences here are being audited for priority; no novelty claim

## 1. The conceptual question

A photodetector timing measurement is usually normalized by the DC-collected signal so that the reported RF transfer describes the timing of carriers that actually contribute to photocurrent.

That normalization looks innocuous.

Mathematically it performs a very specific conditioning operation.

Consider

```math
\boxed{
D(z)u''+v(z)u'-[\kappa(z)+s]u=0,
}
\tag{1}
```

where `u(z,s)` is the Laplace-weighted first-passage/collection response from generation coordinate `z`.

Define

```math
\boxed{
h(z)\equiv u(z,0).
}
\tag{2}
```

For the first-passage interpretation, `h(z)` is the probability of successful collection before killing/recombination.

The experimentally natural DC-normalized RF field is

```math
\boxed{
F(z,\omega)
\equiv
\frac{u(z,i\omega)}{h(z)}.
}
\tag{3}
```

The question is:

> **What transport process does `F` describe?**

---

# 2. Exact transformation

Write

```math
u=hF.
```

Then

```math
u'=h'F+hF',
```

```math
u''=h''F+2h'F'+hF''.
```

Insert into the RF equation:

```math
D(h''F+2h'F'+hF'')
+v(h'F+hF')
-(\kappa+i\omega)hF=0.
```

Group the terms multiplying `F`:

```math
[D h''+v h'-\kappa h]F.
```

But `h=u(z,0)` satisfies the DC equation

```math
\boxed{
D h''+v h'-\kappa h=0.
}
\tag{4}
```

so those terms cancel exactly.

Divide by `h`:

```math
\boxed{
D F''
+\left(v+2D\frac{h'}{h}\right)F'
-i\omega F
=0.
}
\tag{5}
```

Define

```math
\boxed{
c(z)=\partial_z\ln h(z),
}
\tag{6}

and

```math
\boxed{
w(z)
=v(z)+2D(z)c(z).
}
\tag{7}
```

Then

```math
\boxed{
D(z)F''+w(z)F'-i\omega F=0.
}
\tag{8}

The killing/recombination term has disappeared completely.

---

# 3. Probabilistic interpretation

Equation (8) is the backward equation of the original diffusion **conditioned on successful collection**.

The transformation

```math
u=hF
```

is the classical Doob `h`-transform of a killed Markov process.

The conditioned process has

```text
the same local diffusion coefficient D(z)
no killing term
conditioned drift w(z)=v(z)+2D(z) d_z ln h(z).
```

Thus the quantity measured by DC-normalized RF is not simply the unconditioned microscopic drift.

It is the timing dynamics of the **surviving/collected carrier ensemble**.

This gives a concise physical statement:

> **Recombination does not disappear when RF data are normalized. It reappears as a selection-induced change in the drift of the carriers that survive to collection.**

---

# 4. Exact arbitrary-profile identifiability boundary

Let

```math
r(z,\omega)
\equiv
\partial_z\ln F(z,\omega).
```

From Eq. (8),

```math
\boxed{
D(r'+r^2)+wr=i\omega.
}
\tag{9}

Define

```math
A(z,\omega)=r'+r^2.
```

Write

```math
r=r_R+i r_I,
\qquad
A=A_R+i A_I.
```

Then

```math
D A_R+w r_R=0,
\tag{10}
```

```math
D A_I+w r_I=\omega.
\tag{11}
```

With

```math
\boxed{
\Delta_h
=A_Rr_I-A_Ir_R,
}
\tag{12}

one nonzero RF frequency gives

```math
\boxed{
D(z)
=-\frac{\omega r_R}{\Delta_h},
}
\tag{13}

```math
\boxed{
w(z)
=\frac{\omega A_R}{\Delta_h},
}
\tag{14}

whenever `Delta_h != 0`.

Therefore:

> **Perfect DC-normalized RF data can determine `D(z)` and the conditioned drift `w(z)` locally, but not the original drift and recombination separately without the DC collection field.**

This statement is exact for arbitrary spatial profiles in the stated 1-D model.

---

# 5. Unconditioning the measured transport

The DC field supplies

```math
c=\frac{h'}{h}.
```

Equation (7) gives

```math
\boxed{
v=w-2Dc.
}
\tag{15}

The DC equation divided by `h` is

```math
D(c'+c^2)+vc=\kappa.
```

Substitute Eq. (15):

```math
\boxed{
\kappa
=D(c'-c^2)+wc.
}
\tag{16}

Hence the full inverse can be written in the conceptually natural sequence

```text
normalized RF
-> D(z), conditioned drift w(z)

DC collection probability
-> c(z)

uncondition
-> physical/backward-generator drift v(z), killing kappa(z).
```

This is cleaner than treating `D,v,kappa` as three unrelated fitted parameters.

---

# 6. The uniform effective velocity is now explained

For constant `D,v,kappa`, define

```math
V_*=\sqrt{v^2+4D\kappa}.
```

The DC log-slope is

```math
c
=\frac{V_*-v}{2D}.
```

Therefore

```math
w=v+2Dc=V_*.
```

So the earlier exact recombination degeneracy

```math
V_*=\sqrt{v^2+4D\kappa}
```

is not an accidental algebraic combination.

It is the uniform **conditioned drift** produced by the Doob transformation.

This explains why normalized RF alone cannot decide whether a faster conditional response came from

```text
larger physical drift
or
stronger killing that preferentially removes slow trajectories.
```

Both can produce the same conditioned transport.

---

# 7. A strong physical prediction — recombination can make surviving carriers look faster

Suppose

```math
h'(z)/h(z)>0
```

in the downstream coordinate, meaning collection probability improves as generation moves toward the collector.

Then for `D>0`,

```math
\boxed{
w>v.
}
\tag{17}

Thus the ensemble conditioned on successful collection has a larger downstream drift than the unconditioned process.

This is a selection effect, not an actual increase in microscopic mobility.

Consequently:

> **A lifetime-limited detector can exhibit a conditional RF transit response that appears faster precisely because recombination has removed the slowest trajectories.**

DC collection loss and normalized timing must therefore be interpreted jointly.

---

# 8. Parameter-free RF-frequency closure

Equation (9) must hold at every RF frequency with the **same** real functions

```math
D(z),\qquad w(z).
```

Therefore independent frequencies must reconstruct identical conditioned coefficients:

```math
\boxed{
D_{\omega_1}(z)=D_{\omega_2}(z)=\cdots,
}
\tag{18}

```math
\boxed{
w_{\omega_1}(z)=w_{\omega_2}(z)=\cdots.
}
\tag{19}

This gives a direct falsification of the local Markov drift-diffusion hypothesis without first assigning a microscopic mobility or lifetime.

If the reconstructed conditioned transport depends systematically on RF frequency, the second-order local generator is incomplete.

Possible causes include

```text
trapping/internal states,
nonlocal hot-carrier transport,
ballistic memory,
frequency-dependent electrical contamination,
carrier-carrier effects,
or an incorrect optical depth coordinate.
```

---

# 9. Spectral version

If wavelength provides a calibrated generation coordinate `z_g(lambda)`, then in the localized-generation limit

```math
r(z_g,\omega)
=
\frac{
\partial_\lambda\ln H_{\rm norm}(\lambda,\omega)
}{dz_g/d\lambda}.
\tag{20}

Likewise the DC collection field gives

```math
c(z_g)
=
\frac{
\partial_\lambda\ln I_{\rm DC}(\lambda)
}{dz_g/d\lambda}.
\tag{21}

Thus wavelength is not merely changing absorption.

It can act as the spatial coordinate required to

```text
reconstruct conditioned carrier transport,
measure collection survival,
and mathematically uncondition the surviving trajectories.
```

The finite-width generation theorem specifies when broad optical generation leaves these spectral derivatives unchanged and when kernel-shape corrections must be added.

---

# 10. Relation to established probability theory

The Doob `h`-transform and conditioning of killed diffusion processes are established mathematical tools.

Therefore the existence of Eq. (8) should **not** be presented as a new probability-theory theorem.

The research question is narrower:

> **Has this conditioning structure been exploited in photodetector spectral/RF metrology to distinguish what normalized timing actually identifies from what DC collection is required to recover?**

That application/measurement boundary remains under focused prior-art audit.

---

# 11. Numerical regression

`numerics/doob_conditioned_transport_theorem.py`

solves a strongly varying killed diffusion with

```text
v(z)=1.5[1+0.25 sin(2 pi z)+0.08 sin(6 pi z)]
D(z)=0.06[1+0.20 cos(3 pi z)]
kappa(z)=0.50[1+0.30 sin(4 pi z)]
```

and a nonzero RF frequency.

It checks that

```math
D(r'+r^2)+wr=i\omega
```

holds to numerical precision, reconstructs `D,w` from normalized RF alone, and then reconstructs the original `v,kappa` after supplying the DC field.

All tested profiles are recovered at approximately machine precision.

---

# 12. Falsifiable predictions

### P1 — conditioned-coefficient frequency collapse

Every RF frequency must reconstruct the same `D(z),w(z)` in the local Markov model.

### P2 — normalization removes explicit killing

The normalized field must satisfy a no-killing second-order equation, Eq. (8), with the drift shifted according to Eq. (7).

### P3 — survival selection changes apparent drift

Where the DC collection probability varies spatially, normalized timing should correspond to `w`, not `v`.

### P4 — DC unconditioning closure

The independently measured DC field must transform `D,w` back to `v,kappa` through Eqs. (15)-(16), and the resulting coefficients must predict all RF frequencies.

### P5 — pure normalized-RF lifetime extraction is structurally incomplete

Any method claiming a unique physical `v(z)` and `tau(z)` from perfect normalized RF alone must be using additional assumptions or information beyond the local killed-diffusion model.

---

# 13. Consequence for the theory paper

This result provides a much clearer conceptual spine than generic coefficient fitting:

```text
photocarriers can die before collection
-> observed RF is conditioned on survival
-> DC normalization is mathematically a Doob transform
-> normalized RF measures conditioned transport
-> DC collection field supplies the information removed by conditioning
-> combined data uncondition the process
-> extra RF frequencies falsify the model.
```

A simple gedanken experiment can explain this without advanced device details:

> Release identical random walkers at different positions. Some disappear before reaching the finish line. First study the arrival-time distribution **only among those that finish**. Then separately record the fraction that finish. The first measurement describes the conditioned walkers; only the two measurements together reveal both their underlying motion and their disappearance rate.

That is the cleanest conceptual interpretation presently found.
