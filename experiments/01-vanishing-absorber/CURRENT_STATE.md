# Current State — Experiment 01: The Vanishing Absorber

**Date:** 2026-08-08  
**Status:** one-resonance model derived; broader bound unresolved; no novelty claim  

## 1. Active question

Can an ideal photodetector be made arbitrarily small, arbitrarily fast, arbitrarily sensitive, and still absorb essentially every incident photon?

The project does not assume the answer is no. The present task is to identify exactly which physical assumptions create or remove the apparent tradeoff.

---

## 2. Canonical detailed derivation

The first exact model is now documented in:

`ONE_PORT_RESONATOR_DYNAMICS.md`

It treats a passive linear one-port optical resonance with external amplitude-decay rate `gamma_e` and active-material absorptive amplitude-decay rate `gamma_a`.

Using the `exp(-i omega t)` convention,

```math
\dot a=
(-i\omega_0-\gamma_e-\gamma_a)a
+\sqrt{2\gamma_e}\,s_+,
```

with stored energy `U=|a|^2` and absorbed power

```math
P_{\rm abs}=2\gamma_aU.
```

---

## 3. Results established within the one-resonance model

### 3.1 Steady-state absorptance

```math
\boxed{
A(\omega)=
\frac{4\gamma_e\gamma_a}
{(\omega-\omega_0)^2+(\gamma_e+\gamma_a)^2}
}
```

Unity on-resonance absorption occurs at critical coupling:

```math
\boxed{\gamma_e=\gamma_a.}
```

This is established resonator theory rederived here to fix normalization.

### 3.2 Energy lifetime

With

```math
\Gamma=\gamma_e+\gamma_a,
```

the stored energy decays as `exp(-2 Gamma t)`, so

```math
\boxed{
\tau_U=\frac{1}{2\Gamma},
\qquad
Q_L=\frac{\omega_0}{2\Gamma}.
}
```

### 3.3 Absorbed-power modulation bandwidth

For a resonant optical carrier with small incident-power modulation, the fractional absorbed-power transfer function is

```math
\boxed{
H_{\rm abs}(\Omega)=
\frac{\Gamma}{\Gamma+i\Omega}.
}
```

Therefore

```math
\boxed{
B_{3\rm dB}
=
\frac{\gamma_e+\gamma_a}{2\pi}.
}
```

At critical coupling,

```math
\boxed{
B_{3\rm dB}^{\rm crit}
=
\frac{\gamma_a}{\pi}.
}
```

Thus, **within this architecture**, if `gamma_a -> 0` and unity absorption is preserved by critical coupling, the absorbed-power modulation bandwidth also tends to zero.

### 3.4 Optical linewidth is not modulation bandwidth

At critical coupling,

```math
\boxed{
\Delta f_{\rm abs,FWHM}
=2B_{3\rm dB}^{\rm crit}.
}
```

Equivalently,

```math
B_{3\rm dB}=\frac{f_0}{2Q_L},
\qquad
\Delta f_{\rm abs,FWHM}=\frac{f_0}{Q_L}.
```

This distinction is now fixed and should not be blurred later.

### 3.5 Integrated absorption

```math
\boxed{
\int A(f)\,df
=
\frac{2\gamma_e\gamma_a}
{\gamma_e+\gamma_a}.
}
```

At critical coupling,

```math
\boxed{
\int A(f)\,df
=
\gamma_a
=
\pi B_{3\rm dB}^{\rm crit}.
}
```

This may provide the natural bridge to later frequency-integrated electromagnetic bounds.

---

## 4. How active material enters the optical loss rate

For weak dielectric loss,

```math
\boxed{
\gamma_a
=
\frac{\omega\epsilon_0}{4U}
\int_{V_a}
\epsilon''(\mathbf r,\omega)|\mathbf E|^2\,dV.
}
```

Therefore `gamma_a proportional to V_a` follows only in a regular shrinking limit where material response and normalized field intensity do not themselves diverge as the active volume shrinks.

This is **not** yet a general result.

The first cavity calculation therefore establishes a penalty in terms of `gamma_a`, not directly in terms of geometric volume.

---

## 5. First detector-level toy result

Retain the idealized bulk dark-event model

```math
D=g_dV,
```

with independent events, one collected charge per event, unity post-absorption collection, no internal gain, and a one-sided shot-noise convention.

Then

```math
\mathrm{NEP}^2
=
\frac{2(h\nu)^2D}{A_0^2}.
```

Define

```math
\boxed{
\mathcal C
=
\frac{h\nu\sqrt{B_{3\rm dB}}}
{\mathrm{NEP}}.
}
```

This is dimensionless.

Writing

```math
x=\frac{\gamma_e}{\gamma_a},
```

gives

```math
\boxed{
\mathcal C^2
=
\frac{4\gamma_a}{\pi D}
\frac{x^2}{(1+x)^3}.
}
```

The maximum occurs at

```math
\boxed{x=2,}
```

not at critical coupling.

Thus the optimum of this specific toy sensitivity-speed metric is

```math
\boxed{
\gamma_e=2\gamma_a,
\qquad
A_0=\frac89,
\qquad
B_{3\rm dB}=\frac{3\gamma_a}{2\pi}.
}
```

and

```math
\boxed{
\mathcal C_{\max}^2
=
\frac{16\gamma_a}{27\pi D}.
}
```

Relative to exact critical coupling,

```math
\boxed{
\frac{\mathcal C_{\max}}
{\mathcal C_{\rm crit}}
=
\sqrt{\frac{32}{27}}
\approx1.08866.
}
```

So sacrificing peak absorption from `1` to `8/9` improves this particular combined metric by about `8.9%`.

This is a model result, not a universal detector optimum.

---

## 6. Conditional volume cancellation

If a regular regime exists in which

```math
\gamma_a=\kappa V
```

while

```math
D=g_dV,
```

then the active volume cancels:

```math
\boxed{
\mathcal C_{\max}^2
=
\frac{16\kappa}{27\pi g_d}.
}
```

This is the first exact realization of the original volume-cancellation idea.

Its weakness is now precise: it depends on whether `gamma_a/V` remains bounded and well behaved as the active volume is reduced.

---

## 7. Verification state

The modulation transfer function was checked by direct time-domain integration of the cavity envelope equation.

At

```text
Omega/Gamma = 0.5, 1, 2
```

the numerical normalized modulation amplitudes were approximately

```text
0.89449, 0.70746, 0.44757
```

versus analytic values

```text
0.89443, 0.70711, 0.44721.
```

A numerical coupling scan also recovered the optimum near

```text
gamma_e/gamma_a = 2.
```

The detailed note records two convention errors caught during the audit before this state was updated: a time-harmonic sign mismatch and an incorrect redundant `Q` rewrite. The corrected central decay-rate formulas are the ones above.

---

## 8. What remains explicitly unestablished

We have **not** shown that:

- `gamma_a/V` is bounded for arbitrary passive geometries;
- `gamma_a proportional to V` survives extreme field concentration;
- a geometry-independent `eta^2 B <= C V` relation exists;
- a universal `sqrt(B)/NEP` bound exists;
- one optical resonance is optimal;
- traveling-wave, multi-resonant, antenna, slow-light, nonreciprocal, time-varying, active, avalanche, photoconductive-gain, nonlocal, or quantum-assisted architectures obey the same restriction;
- any detector-level result here is novel.

---

## 9. Next decisive question

The first thought-experiment step has resolved cleanly:

> A vanishingly weak absorber can retain unity monochromatic absorption in a one-port cavity, but only by making the resonant optical response proportionally narrow.

The next problem is deeper:

> **Can passive electromagnetic design make `gamma_a/V` increase without bound as `V -> 0`, while preserving a physically meaningful incident channel and material model?**

This is now the correct place to challenge the apparent limit.

Do **not** add HgCdTe-specific transport yet.

The next stage should examine electromagnetic concentration and material-response bounds, beginning with the weakest assumptions possible and actively searching for counterexamples.
