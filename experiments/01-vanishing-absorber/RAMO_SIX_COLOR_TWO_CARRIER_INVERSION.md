# Six-Color Shockley-Ramo Closure — Complete Homogeneous Two-Carrier Inversion

**Date:** 2026-08-10  
**Status:** **DERIVED / CHECKED / CONDITIONAL** for two independent homogeneous carrier species in a planar raw-current model; generic noiseless mode amplitudes/root tracking assumed; no novelty claim for recurrence/system-identification mathematics

## 1. Why this matters

The most obvious conventional counterexample to the one-carrier four-color law is not a boundary or exotic transport.

It is simply

```text
one photogenerated electron
+
one photogenerated hole.
```

Both can induce terminal current.

That raises the first-difference spatial rank from one to two.

The key result is that this does **not** force the analysis into an arbitrary six-parameter nonlinear fit.

Six colors recover the two spatial roots first.  DC plus one RF then determines each carrier's

```text
D
w
kappa
```

separately.

A second RF frequency is a simultaneous falsification point for both species.

---

## 2. Independent homogeneous carrier modes

Let the generation coordinate be `z` between two collection directions.

For the electron branch, define positive propagation magnitude

```math
\gamma_e(s)>0
```

through

```math
\boxed{
D_e\gamma_e^2+w_e\gamma_e
=\kappa_e+s.
}
\tag{1}
```

For the hole branch, similarly

```math
\boxed{
D_h\gamma_h^2+w_h\gamma_h
=\kappa_h+s.
}
\tag{2}
```

The spatial signs are opposite because increasing `z` shortens one carrier's collection path while lengthening the other's.

After absorbing fixed collector-distance factors into amplitudes, the raw planar current has the form

```math
\boxed{
J(z,s)
=C_0(s)
+C_e(s)e^{+\gamma_e(s)z}
+C_h(s)e^{-\gamma_h(s)z}.
}
\tag{3}
```

The amplitudes can be arbitrary nonzero functions of RF frequency in the algebra below.

---

## 3. Six colors recover the two spatial roots

Sample

```math
z_m=z_0+mh,
\qquad m=0,\ldots,5.
```

First differences remove the constant term:

```math
\Delta J_m
=a_e q_e^m+a_h q_h^m,
```

where

```math
q_e=e^{+\gamma_e h},
```

```math
q_h=e^{-\gamma_h h}.
```

Thus the five first differences satisfy a second-order recurrence and the rank-two Hankel determinant

```math
\boxed{
\det
\begin{pmatrix}
\Delta J_0&\Delta J_1&\Delta J_2\\
\Delta J_1&\Delta J_2&\Delta J_3\\
\Delta J_2&\Delta J_3&\Delta J_4
\end{pmatrix}=0.
}
\tag{4}
```

When both amplitudes are nonzero and the roots are distinct, recurrence recovery gives

```math
q_e,
\qquad
q_h.
```

Then

```math
\boxed{
r_e=\frac1h\log q_e=+\gamma_e,
}
```

```math
\boxed{
r_h=\frac1h\log q_h=-\gamma_h.
}
\tag{5}
```

Log branches must be tracked continuously.

---

## 4. DC naturally labels the collection directions

At DC with positive recombination rates,

```math
\gamma_e(0),\gamma_h(0)
```

are real and nonnegative.

Therefore the two signed spatial roots are

```text
positive root -> one collection direction
negative root -> the opposite collection direction.
```

This provides a natural root label in generic noiseless data.

Continue each root continuously from DC into RF rather than re-sorting it independently at every frequency.

If a mode amplitude vanishes or roots become numerically unresolved, identifiability is lost and the theorem should not be forced.

---

## 5. DC + one RF inversion for each species

For either carrier species `c`, let

```math
g_{c0}=\gamma_c(0),
```

```math
g_{c\omega}=\gamma_c(i\omega).
```

Define

```math
A_c=g_{c\omega}^2-g_{c0}^2,
```

```math
B_c=g_{c\omega}-g_{c0}.
```

Subtracting the DC and RF dispersion equations gives

```math
D_c A_c+w_c B_c=i\omega.
```

With real `D_c,w_c` and nonsingular

```math
\Delta_c
=\Re A_c\Im B_c
-\Im A_c\Re B_c,
```

recover

```math
\boxed{
D_c
=-\frac{\omega\Re B_c}{\Delta_c},
}
\tag{6}
```

```math
\boxed{
w_c
=\frac{\omega\Re A_c}{\Delta_c},
}
\tag{7}
```

and

```math
\boxed{
\kappa_c
=D_c g_{c0}^2+w_c g_{c0}.
}
\tag{8}
```

Apply Eqs. (6)-(8) separately to the electron and hole propagation magnitudes.

Thus

```text
6 colors at DC
+
6 colors at one RF
```

identify, in the ideal generic case,

```math
\boxed{
D_e,w_e,\kappa_e,
D_h,w_h,\kappa_h.
}
```

---

## 6. Every additional RF frequency is a simultaneous null test

After the six parameters are fixed, each later RF frequency must satisfy both

```math
\boxed{
D_e\gamma_e^2+w_e\gamma_e
=\kappa_e+i\omega,
}
```

and

```math
\boxed{
D_h\gamma_h^2+w_h\gamma_h
=\kappa_h+i\omega.
}
```

Equivalently, independently repeating Eqs. (6)-(8) must recover the same real coefficients for each species.

So a two-carrier model remains strongly falsifiable despite having more physical parameters.

The correct logic is still

```text
first identify minimal spatial rank
then infer the corresponding physical roots
then use RF redundancy to try to kill the model.
```

---

## 7. Relation to the deterministic root signature

In the zero-diffusion/zero-recombination limit,

```math
\gamma_e=i\omega/v_e,
```

in the signed RF exponent convention used for the deterministic current, while the opposite carrier has the opposite spatial sign.

The resulting pair gives the earlier limiting signatures

```math
r_e+r_h
=i\omega(1/v_e-1/v_h),
```

```math
r_er_h
=\omega^2/(v_ev_h).
```

The complete DC+RF inversion here is more general and should replace the deterministic root geometry when diffusion/recombination are appreciable.

The deterministic formulas remain useful as an intuitive high-field/high-Peclet limit.

---

## 8. What can break the theorem

The six-color two-carrier model can fail because of

```text
spatially varying coefficients,
finite boundaries adding further roots,
nonuniform weighting field,
carrier coupling,
trapping/internal states,
space charge,
nonlocal/hydrodynamic transport,
wavelength-dependent source-shape evolution,
mode amplitude cancellation,
or insufficient depth sampling to resolve the roots.
```

A failed rank-two closure should therefore trigger a higher model-order test before mechanism-specific fitting.

---

## 9. Numerical regression

`numerics/ramo_two_carrier_complete_inversion.py`

uses independent electron/hole parameters and arbitrary RF-dependent mode amplitudes.

It verifies:

```text
six-color recovery of both signed spatial roots
DC root labeling by collection direction
DC + one-RF recovery of D,w,kappa for both species
coefficient invariance across several additional RF frequencies.
```

All six physical coefficients are recovered to numerical precision in the noiseless stress.

---

## 10. Paper-level consequence

This closes the simplest reviewer objection to the one-carrier four-color gedanken experiment:

> **"A real photodiode has electrons and holes, so the closure failure is trivial."**

Yes—the one-mode closure can fail for that entirely conventional reason.

But the theory then makes a stronger, still parameter-constrained prediction:

> **Six colors should expose exactly two first-difference propagation modes.  DC plus one RF fixes the transport/recombination coefficients of both modes.  The next RF frequency must reproduce them.**

Thus ordinary two-carrier signal formation becomes a testable rung of the hierarchy rather than an uncontrolled loophole.
