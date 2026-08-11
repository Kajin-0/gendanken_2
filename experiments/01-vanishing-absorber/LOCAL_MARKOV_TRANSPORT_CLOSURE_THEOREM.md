# Exact Real Multi-Frequency Closure for Local Drift-Diffusion

**Date:** 2026-08-10  
**Status:** exact theorem inside the stated 1-D local second-order Markov transport model; parameter-free falsification criterion; no novelty claim pending focused prior-art audit

## 1. Gedanken experiment

Imagine an ideal detector in which the complex, DC-normalized first-passage response can be resolved as a function of generation depth `z` and RF angular frequency `omega`:

```math
F(z,\omega).
```

No HgCdTe-specific assumption is needed yet.

Assume only that successfully collected carriers are described locally by a one-dimensional second-order Markov drift-diffusion generator

```math
\boxed{
D(z)F''(z,\omega)
+w(z)F'(z,\omega)
-i\omega F(z,\omega)=0,
}
```

with real

```text
D(z) > 0
w(z) real
```

and no explicit RF-frequency dependence in those local coefficients.

The earlier conditioning result explains why `w` is the **conditioned drift** after DC normalization; physical unconditioned drift and recombination require the DC collection field to undo that conditioning.

---

## 2. Logarithmic response variables

Define

```math
\boxed{
r_\omega(z)=\partial_z\ln F(z,\omega),
}
```

and

```math
\boxed{
A_\omega(z)
=r_\omega'(z)+r_\omega^2(z)
=\frac{F''(z,\omega)}{F(z,\omega)}.
}
```

Then the transport equation becomes locally

```math
\boxed{
D A_\omega+w r_\omega=i\omega.
}
```

This is exact for arbitrarily varying `D(z)` and `w(z)`; no WKB or slowly-varying approximation has been used.

---

## 3. One frequency gives a real 2 x 2 inverse

Write

```math
r=r_R+i r_I,
\qquad
A=A_R+i A_I.
```

Because `D,w` are real,

```math
D A_R+w r_R=0,
```

```math
D A_I+w r_I=\omega.
```

Define the local determinant

```math
\boxed{
\delta_\omega
=A_R r_I-A_I r_R.
}
```

If

```math
\delta_\omega\ne0,
```

the unique real coefficients inferred from that frequency are

```math
\boxed{
D_{\rm app}(\omega)
=-\frac{\omega r_R}{\delta_\omega},
}
```

```math
\boxed{
w_{\rm app}(\omega)
=\frac{\omega A_R}{\delta_\omega}.
}
```

`delta_omega=0` is therefore the exact local single-frequency identifiability singularity.

---

## 4. Exact multi-frequency closure theorem

Take any set of frequencies

```math
\Omega=\{\omega_1,\ldots,\omega_N\}
```

for which every `delta_omega` is nonzero.

### Theorem

There exists one real, frequency-independent local second-order Markov drift-diffusion operator

```math
D(z)\partial_z^2+w(z)\partial_z
```

that generates all measured responses at that depth **if and only if**

```math
\boxed{
D_{\rm app}(\omega_1)
=D_{\rm app}(\omega_2)
=\cdots
=D_{\rm app}(\omega_N)
}
```

and

```math
\boxed{
w_{\rm app}(\omega_1)
=w_{\rm app}(\omega_2)
=\cdots
=w_{\rm app}(\omega_N).
}
```

### Proof

**Necessity.** If one real `D,w` generates every frequency, the two real equations above have a unique solution at each nonsingular frequency. Therefore every per-frequency solution must equal that same `D,w`.

**Sufficiency.** If the apparent coefficients are the same real numbers at every frequency, then by construction those common values satisfy

```math
D A_\omega+w r_\omega=i\omega
```

for every measured frequency. Hence one real local second-order Markov generator exists at that depth.

QED.

This gives

```math
\boxed{2(N-1)}
```

independent real closure conditions relative to one reference frequency.

---

## 5. Parameter-free polynomial form

Avoid divisions by `delta_omega` by cross-multiplying.

For any pair `j,k`, local Markov closure requires

```math
\boxed{
\omega_j\Re r_j\,\delta_k
-
\omega_k\Re r_k\,\delta_j=0,
}
```

and

```math
\boxed{
\omega_j\Re A_j\,\delta_k
-
\omega_k\Re A_k\,\delta_j=0.
}
```

These are parameter-free null relations involving only the measured complex response field and its spatial derivatives.

---

## 6. Correction: the 3 x 3 complex determinant is weaker

A compact necessary relation is

```math
\boxed{
\det
\begin{pmatrix}
A_1&r_1&i\omega_1\\
A_2&r_2&i\omega_2\\
A_3&r_3&i\omega_3
\end{pmatrix}
=0.
}
```

This follows because

```math
(A_j,r_j,i\omega_j)\cdot(D,w,-1)=0.
```

However, that determinant tests existence of common **complex** coefficients as well.

It is therefore **necessary but not sufficient** for physical drift-diffusion with real `D,w`.

An explicit numerical counterexample in

`numerics/local_markov_real_closure_hierarchy.py`

uses one frequency-independent complex pair

```text
D_complex = D0(1+0.2 i)
w_complex = w0(1-0.1 i).
```

The three-frequency complex determinant remains at numerical zero, while the real apparent coefficients vary strongly with RF frequency.

Thus the real-frequency-independence theorem supersedes determinant-only closure as the canonical test.

---

## 7. Simplest uniform-channel version

If the local medium is spatially uniform over the probed interval, then

```math
r_\omega'=0,
\qquad
A_\omega=r_\omega^2.
```

Write

```math
r_\omega=a_\omega+i b_\omega.
```

Then

```math
\delta_\omega
=-b_\omega(a_\omega^2+b_\omega^2),
```

and the exact one-frequency inversion reduces to

```math
\boxed{
D_{\rm app}
=
\frac{\omega a}
{b(a^2+b^2)},
}
```

```math
\boxed{
w_{\rm app}
=
\frac{\omega(b^2-a^2)}
{b(a^2+b^2)}.
}
```

Therefore the easiest gedanken experiment is:

```text
1. generate carriers at two known depths;
2. measure their complex RF transfer ratio;
3. infer r_omega from the logarithmic ratio;
4. repeat at several RF frequencies;
5. ask whether D_app and w_app are constant.
```

No transient waveform fitting is required.

---

## 8. Low-frequency identifiability scaling

For uniform drift-diffusion,

```math
r_\omega
=\frac{\sqrt{w^2+4iD\omega}-w}{2D}.
```

At low RF,

```math
r_\omega
=\frac{i\omega}{w}
+\frac{D\omega^2}{w^3}
-\frac{2iD^2\omega^3}{w^5}
+\cdots.
```

Hence

```math
\boxed{
\delta_\omega
\sim
-\frac{\omega^3}{w^3}.
}
```

The local inverse therefore becomes rapidly ill-conditioned as `omega -> 0`.

Conceptually:

```text
phase ~ O(omega) -> drift information
real log-slope ~ O(omega^2) -> diffusion information
single-frequency determinant ~ O(omega^3).
```

This is why very low-frequency phase can determine delay/drift well while carrying almost no independent information about diffusion.

---

## 9. Strong falsifiability statement

The theorem does **not** say that closure failure uniquely identifies a particular microscopic mechanism.

It says something more basic and rigorous:

> **If either `D_app(z,omega)` or `w_app(z,omega)` varies reproducibly with RF frequency beyond measurement/model uncertainty, then no real frequency-independent local second-order Markov drift-diffusion equation can generate the measured conditioned response at that depth.**

Possible causes then include

```text
trapping / memory
finite momentum or energy relaxation
nonlocal spatial transport
multiple carrier populations
frequency-dependent boundary physics
or failure of the one-dimensional reduction.
```

Those mechanisms require separate discriminants.

---

## 10. Relation to prior inverse work

Convection-diffusion coefficient inversion from modulated amplitude/phase profiles is established prior art. In particular, Sattin, Escande and co-workers reduced periodically modulated convection-diffusion inverse problems to local algebraic matrix inversions and emphasized singular/ill-conditioned points.

Therefore do **not** claim novelty for

```text
local algebraic extraction of convection and diffusion from modulated profiles
```

by itself.

The potentially distinctive detector-theory package remains the combination of

```text
wavelength as an internal generation-depth coordinate
DC conditioning / unconditioning
multi-frequency real closure as a detector null test
finite-width spectral translation results
and translated internal-feature witnesses.
```

Priority remains unproven.

---

## 11. Next theorem

The closure test turns the question around.

Instead of fitting every dataset with ever-more-elaborate transport coefficients, ask:

> **What frequency dependence does each physically motivated departure from local Markov drift-diffusion imprint on `D_app(omega)` and `w_app(omega)`?**

That produces a falsification hierarchy for trapping, relaxation, and spatial nonlocality.

Numerical regression:

`numerics/local_markov_real_closure_hierarchy.py`
