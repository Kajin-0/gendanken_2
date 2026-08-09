# One-Port Resonator Dynamics — Exact Minimal Model

**Date:** 2026-08-08  
**Status:** derived within the stated temporal coupled-mode model; no novelty claim  

## 1. Purpose

This note answers the first concrete question in Experiment 01:

> In the simplest passive one-port resonant absorber, does maintaining strong absorption with weak material loss necessarily impose a temporal-bandwidth penalty?

The derivation is intentionally restricted to one linear optical resonance. It is not a geometry-independent theorem and does not yet include carrier transport, readout, optical background noise, surfaces, tunneling, gain, or multiple resonances.

---

## 2. Normalization

Use one temporal coupled-mode convention throughout.

Let

```math
U(t)=|a(t)|^2
```

be the optical energy stored in the resonant mode, and let

```math
P_{\rm in}=|s_+|^2,
\qquad
P_{\rm out}=|s_-|^2
```

be input and output powers.

Define

- `gamma_e` — amplitude-decay rate associated with leakage into the external port;
- `gamma_a` — amplitude-decay rate associated with absorption in the active material;
- `Gamma = gamma_e + gamma_a` — total amplitude-decay rate.

For a one-port resonance with a lossless background reflection of phase `pi`, choose

```math
\boxed{
\dot a=(i\omega_0-\Gamma)a+\sqrt{2\gamma_e}\,s_+
}
```

and

```math
\boxed{
s_-=-s_+ + \sqrt{2\gamma_e}\,a.
}
```

The absorbed power is

```math
\boxed{
P_{\rm abs}=2\gamma_a |a|^2.
}
```

With no incident field,

```math
\dot U=-2\Gamma U,
```

so the stored-energy lifetime is

```math
\boxed{
\tau_U=\frac{1}{2\Gamma}.
}
```

The loaded quality factor is therefore

```math
\boxed{
Q_L=\frac{\omega_0}{2\Gamma}.
}
```

This fixes the factor-of-two convention before any linewidth or bandwidth is quoted.

---

## 3. Steady-state absorptance

Drive the resonator monochromatically at angular frequency `omega`:

```math
s_+(t)=s_0e^{-i\omega t}.
```

With

```math
\Delta=\omega-\omega_0,
```

the steady-state cavity amplitude is

```math
\boxed{
\tilde a=
\frac{\sqrt{2\gamma_e}\,s_0}
{\Gamma-i\Delta}.
}
```

The reflection coefficient is

```math
r(\omega)
=-1+\frac{2\gamma_e}{\Gamma-i\Delta}
=
\frac{\gamma_e-\gamma_a+i\Delta}
{\Gamma-i\Delta}.
```

Hence

```math
|r|^2
=
\frac{(\gamma_e-\gamma_a)^2+\Delta^2}
{(\gamma_e+\gamma_a)^2+\Delta^2}.
```

Because the system has one external port and the only internal loss is the active absorber,

```math
A(\omega)=1-|r|^2.
```

Therefore

```math
\boxed{
A(\omega)=
\frac{4\gamma_e\gamma_a}
{\Delta^2+(\gamma_e+\gamma_a)^2}.
}
```

The same expression follows directly from `P_abs = 2 gamma_a |a|^2` divided by `P_in`.

### Checks

- `gamma_a -> 0` gives zero absorption.
- `gamma_e -> 0` gives zero coupling and zero absorption.
- `|Delta| -> infinity` gives zero absorption.
- `0 <= A <= 1` for positive decay rates.

---

## 4. Critical coupling

At resonance,

```math
A_0
=
\frac{4\gamma_e\gamma_a}
{(\gamma_e+\gamma_a)^2}.
```

The maximum possible value is unity, reached when

```math
\boxed{
\gamma_e=\gamma_a.
}
```

Thus the familiar critical-coupling condition is recovered from the chosen normalization rather than imported.

At critical coupling, writing `gamma_e = gamma_a = gamma`,

```math
\boxed{
A(\omega)=
\frac{4\gamma^2}{\Delta^2+4\gamma^2}.
}
```

The absorptance half-maximum occurs at

```math
|\Delta|=2\gamma=\Gamma.
```

Hence the **angular-frequency FWHM** is

```math
\boxed{
\Delta\omega_{\rm abs,FWHM}=2\Gamma=4\gamma,
}
```

and the FWHM in ordinary frequency is

```math
\boxed{
\Delta f_{\rm abs,FWHM}=\frac{\Gamma}{\pi}.
}
```

---

## 5. Stored energy at resonance

For arbitrary coupling, on resonance,

```math
U_0
=
\frac{2\gamma_e}{\Gamma^2}P_{\rm in}.
```

At critical coupling,

```math
\boxed{
U_0=\frac{P_{\rm in}}{2\gamma_a}.
}
```

Therefore, as `gamma_a -> 0` while critical coupling is maintained,

```math
U_0\propto \frac{1}{\gamma_a}
```

for fixed continuous incident power.

This is the steady-state manifestation of the increasing photon dwell time.

---

## 6. Small-signal absorbed-power modulation response

The relevant detector bandwidth is not automatically the optical spectral linewidth. Derive the absorbed-power response explicitly.

Set the optical carrier exactly on resonance and apply a small real amplitude modulation:

```math
s_+(t)=s_0+\delta s(t),
\qquad
|\delta s|\ll |s_0|.
```

The steady-state carrier amplitude is

```math
a_0=\frac{\sqrt{2\gamma_e}}{\Gamma}s_0.
```

The perturbation obeys

```math
\delta\dot a + \Gamma\,\delta a
=
\sqrt{2\gamma_e}\,\delta s.
```

For a modulation component proportional to `exp(i Omega t)`,

```math
\frac{\delta a/a_0}{\delta s/s_0}
=
\frac{\Gamma}{\Gamma+i\Omega}.
```

To first order,

```math
\frac{\delta P_{\rm in}}{P_{\rm in}}
=2\frac{\delta s}{s_0},
```

and

```math
\frac{\delta P_{\rm abs}}{P_{\rm abs}}
=2\frac{\delta a}{a_0}.
```

Thus the **fractional absorbed-power transfer function** is

```math
\boxed{
H_{\rm abs}(\Omega)
=
\frac{\delta P_{\rm abs}/P_{\rm abs}}
{\delta P_{\rm in}/P_{\rm in}}
=
\frac{\Gamma}{\Gamma+i\Omega}.
}
```

Therefore

```math
|H_{\rm abs}(\Omega)|^2
=
\frac{\Gamma^2}{\Gamma^2+\Omega^2}.
```

The exact small-signal `-3 dB` modulation angular frequency is

```math
\boxed{
\Omega_{3\rm dB}=\Gamma=\gamma_e+\gamma_a,
}
```

or

```math
\boxed{
B_{3\rm dB}=\frac{\gamma_e+\gamma_a}{2\pi}.
}
```

At critical coupling,

```math
\boxed{
B_{3\rm dB}^{\rm crit}=\frac{\gamma_a}{\pi}.
}
```

This is the first decisive result for the thought experiment: **within this one-resonance model, if `gamma_a -> 0` and critical coupling is maintained, the usable small-signal absorbed-power bandwidth tends to zero linearly with `gamma_a`.**

---

## 7. Optical linewidth is not detector modulation bandwidth

Combining the previous sections gives, at critical coupling,

```math
\boxed{
\Delta f_{\rm abs,FWHM}=2B_{3\rm dB}^{\rm crit}.
}
```

Thus the optical absorption FWHM and the detector's small-signal modulation `-3 dB` bandwidth are related but are not numerically identical.

Using `Q_L = omega_0/(2 Gamma)`, the modulation bandwidth can also be written

```math
\boxed{
B_{3\rm dB}=\frac{f_0}{2Q_L} \times \frac{1}{2}
=\frac{f_0}{4Q_L}.
}
```

Equivalently,

```math
\boxed{
B_{3\rm dB}=\frac{\Gamma}{2\pi}.
}
```

The explicit `f_0/(4Q_L)` form is retained only to emphasize the photon-lifetime scaling.

---

## 8. Large-signal turn-on is different again

If the incident field is switched suddenly from zero to a constant resonant amplitude at `t=0`,

```math
a(t)=a_{\rm ss}\left(1-e^{-\Gamma t}\right).
```

Hence

```math
\boxed{
\frac{P_{\rm abs}(t)}{P_{\rm abs,ss}}
=
\left(1-e^{-\Gamma t}\right)^2.
}
```

So a large-signal optical turn-on is not a single exponential in absorbed power even though the small-signal modulation response is first-order.

Do not interchange:

- field-amplitude decay time `1/Gamma`;
- stored-energy lifetime `1/(2 Gamma)`;
- optical absorption FWHM;
- small-signal absorbed-power `-3 dB` bandwidth;
- large-signal rise time.

---

## 9. Integrated absorptance

The Lorentzian area is

```math
\boxed{
\int_{-\infty}^{\infty}A(\omega)\,d\omega
=
\frac{4\pi\gamma_e\gamma_a}{\gamma_e+\gamma_a}.
}
```

At critical coupling,

```math
\boxed{
\int A(\omega)\,d\omega=2\pi\gamma_a.
}
```

In ordinary frequency,

```math
\boxed{
\int A(f)\,df
=
\frac{2\gamma_e\gamma_a}{\gamma_e+\gamma_a},
}
```

and at critical coupling

```math
\boxed{
\int A(f)\,df=\gamma_a=\pi B_{3\rm dB}^{\rm crit}.
}
```

This is potentially useful later because geometry-independent electromagnetic bounds are often naturally stated as frequency-integrated response constraints.

---

## 10. How material absorption enters `gamma_a`

For weak dielectric loss, using complex relative permittivity

```math
\epsilon_r=\epsilon'+i\epsilon'',
```

and the `exp(-i omega t)` convention, the time-averaged absorbed power in active volume `V_a` is

```math
P_{\rm abs}
=
\frac{\omega\epsilon_0}{2}
\int_{V_a}\epsilon''(\mathbf r,\omega)|\mathbf E|^2\,dV.
```

Since `P_abs = 2 gamma_a U`, first-order perturbation theory gives

```math
\boxed{
\gamma_a
=
\frac{\omega\epsilon_0}{4U}
\int_{V_a}\epsilon''(\mathbf r,\omega)|\mathbf E|^2\,dV.
}
```

For dispersive media, `U` must use the appropriate dispersive electromagnetic-energy expression; the simple nondispersive energy density must not be used blindly.

### Crucial logical point

If, as the active volume shrinks,

- the material loss function remains fixed;
- the normalized field intensity in the absorber remains bounded;
- the total modal energy normalization remains regular;

then the overlap integral scales approximately with active volume and one obtains

```math
\gamma_a \propto V_a.
```

But this proportionality is **not universal**.

A geometry may increase local field concentration as `V_a` shrinks. Singular local-response models, extreme confinement, strong dispersion, nonlocality, or material changes can also alter the scaling. Therefore the present calculation proves a penalty in terms of `gamma_a`, not yet in terms of geometric volume alone.

This is the main assumption that must be attacked next.

---

## 11. Immediate detector-level consequence in the minimal dark-event model

Now add only the idealized bulk dark-event process already defined in Experiment 01.

Let

```math
D=g_dV
```

be the total dark-event rate. Assume:

- independent events;
- one collected charge `q` per event;
- unity internal collection after optical absorption;
- no gain;
- one-sided shot-noise convention.

Then

```math
S_I=2q^2D.
```

For on-resonance absorptance `A_0`, the current responsivity is

```math
R_I=A_0\frac{q}{h\nu}.
```

Therefore

```math
\boxed{
\mathrm{NEP}^2
=
\frac{2(h\nu)^2D}{A_0^2}.
}
```

Define the dimensionless sensitivity-speed quantity

```math
\boxed{
\mathcal C
\equiv
\frac{h\nu\sqrt{B_{3\rm dB}}}{\mathrm{NEP}}.
}
```

Let

```math
x=\frac{\gamma_e}{\gamma_a}.
```

Then

```math
A_0=\frac{4x}{(1+x)^2},
```

```math
B_{3\rm dB}=\frac{\gamma_a(1+x)}{2\pi},
```

and hence

```math
\boxed{
\mathcal C^2
=
\frac{4\gamma_a}{\pi D}
\frac{x^2}{(1+x)^3}.
}
```

### Critical coupling is not the optimum of this metric

Differentiate with respect to `x`:

```math
\frac{d}{dx}
\left[
\frac{x^2}{(1+x)^3}
\right]
=0
```

which gives the nonzero optimum

```math
\boxed{x=2.}
```

Thus

```math
\boxed{
\gamma_e=2\gamma_a,
\qquad
A_0=\frac{8}{9},
\qquad
B_{3\rm dB}=\frac{3\gamma_a}{2\pi}.
}
```

At this point

```math
\boxed{
\mathcal C_{\max}^2
=
\frac{16\gamma_a}{27\pi D}.
}
```

At exact critical coupling,

```math
\mathcal C_{\rm crit}^2
=
\frac{\gamma_a}{2\pi D}.
```

Therefore

```math
\boxed{
\frac{\mathcal C_{\max}}{\mathcal C_{\rm crit}}
=
\sqrt{\frac{32}{27}}
\approx 1.08866.
}
```

So allowing the peak absorption to fall from `1` to `8/9` improves this particular sensitivity-speed metric by about `8.9%`.

This is not claimed as a universal optimum. It follows only from the present one-mode optical response plus the stated bulk Poisson dark-event model.

---

## 12. Conditional volume cancellation

Suppose a regular weak-participation limit exists such that

```math
\gamma_a=\kappa V
```

with `kappa` independent of `V` over the scaling regime, while

```math
D=g_dV.
```

Then the active volume cancels from the dimensionless capability.

At the optimized coupling point,

```math
\boxed{
\mathcal C_{\max}^2
=
\frac{16\kappa}{27\pi g_d},
}
```

independent of `V`.

At critical coupling,

```math
\boxed{
\mathcal C_{\rm crit}^2
=
\frac{\kappa}{2\pi g_d}.
}
```

This is the first exact appearance of the volume-cancellation idea in the project, but it is explicitly conditional on `gamma_a proportional to V` and on the minimal noise model.

It must **not** be promoted to a geometry-independent photodetector bound.

---

## 13. Numerical falsification check

A direct time-domain integration of

```math
\dot a=-\Gamma a+\sqrt{2\gamma_e}\,s(t)
```

with small sinusoidal incident-power modulation reproduces

```math
|H_{\rm abs}|=
\frac{\Gamma}{\sqrt{\Gamma^2+\Omega^2}}
```

at representative frequencies.

For example, at `Omega/Gamma = 0.5, 1, 2`, the normalized numerical modulation amplitudes are approximately

```text
0.89449, 0.70746, 0.44757
```

compared with analytic values

```text
0.89443, 0.70711, 0.44721.
```

A numerical scan over coupling ratio also places the maximum of `A_0 sqrt(B)` at

```text
x = gamma_e/gamma_a ~= 2.00003,
A_0 ~= 0.888884,
```

consistent with the exact result `x=2`, `A_0=8/9`.

A repository script should preserve this test if the result becomes load-bearing in later work.

---

## 14. What is established and what is not

### Derived within this model

1. The absorptance is

```math
A(\omega)=
\frac{4\gamma_e\gamma_a}
{(\omega-\omega_0)^2+(\gamma_e+\gamma_a)^2}.
```

2. Unity on-resonance absorption requires `gamma_e = gamma_a`.
3. The stored-energy lifetime is `1/[2(gamma_e+gamma_a)]`.
4. The resonant small-signal absorbed-power bandwidth is

```math
B_{3\rm dB}=\frac{\gamma_e+\gamma_a}{2\pi}.
```

5. At critical coupling, `B_3dB = gamma_a/pi`; thus weak absorber loss forces narrow temporal response in this architecture.
6. At critical coupling, optical absorptance FWHM is twice the small-signal detector modulation bandwidth.
7. Under the ideal bulk dark-event model, the dimensionless quantity `h nu sqrt(B)/NEP` is maximized at `gamma_e = 2 gamma_a`, not at critical coupling.
8. If both `gamma_a` and dark-event rate scale linearly with the same active volume, that volume cancels from this toy-model sensitivity-speed metric.

### Not established

- `gamma_a proportional to V` for arbitrary geometries;
- a geometry-independent absorption-bandwidth-volume theorem;
- a universal NEP-bandwidth limit;
- optimality of a single resonance;
- robustness against multiple resonances, traveling-wave structures, antennas, slow light, nonreciprocity, temporal modulation, gain, avalanche multiplication, photoconductive gain, nonlocal response, or quantum optical resources;
- novelty of any detector-level synthesis above.

---

## 15. Next decisive question

The one-port cavity did not fail. It sharpened the problem.

The next question is no longer

> Does a weak critically coupled absorber become slow?

Within this model, yes.

The next question is

> **Can passive electromagnetic design make `gamma_a/V` grow without bound as active volume tends to zero while preserving a physically meaningful input channel and material model?**

If the answer is yes, the volume-cancellation picture can be evaded even before adding semiconductor transport.

If the answer is no under identifiable assumptions, then a genuinely more general material-response bound may exist.

The next stage should therefore attack `gamma_a/V`, not yet add HgCdTe-specific transport physics.

---

## 16. Prior-theory anchors

The temporal coupled-mode structure used here is established resonator theory. Relevant primary/background sources include:

- S. Fan, W. Suh, and J. D. Joannopoulos, *Temporal coupled-mode theory for the Fano resonance in optical resonators*, JOSA A 20, 569–572 (2003), DOI: `10.1364/JOSAA.20.000569`.
- Z. Ruan and S. Fan, *Temporal coupled-mode theory for light scattering by an arbitrarily shaped object supporting a single resonance*, Phys. Rev. A 85, 043828 (2012), DOI: `10.1103/PhysRevA.85.043828`.
- Z. Zhao, C. Guo, and S. Fan, *Connection of temporal coupled-mode-theory formalisms for a resonant optical system and its time-reversal conjugate*, Phys. Rev. A 99, 033839 (2019), DOI: `10.1103/PhysRevA.99.033839`.

These are background theory, not evidence that the detector-level combination or optimization derived here is novel.
