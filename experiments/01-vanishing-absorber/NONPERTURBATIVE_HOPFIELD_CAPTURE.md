# Nonperturbative Hopfield Capture — Perfect Peak Transfer with Vanishing Deep-Strong Bandwidth

**Date:** 2026-08-08  
**Status:** exact symmetric-model reduction using established Hopfield/global-master-equation theory; detector interpretation derived here; strong prior-art overlap; no novelty claim  

## 1. Purpose

The preceding weak-coupling analysis eventually allowed the perturbative radiative-rate estimate to approach the bare optical frequency.

At that point the description

```text
fixed optical transition
+
LDOS enhancement
-> larger Markov decay rate
```

is no longer controlled.

This note replaces that extrapolation by the simplest gauge-consistent quadratic light-matter model and asks:

> If bare light-matter coupling is increased into the deep-strong regime, can irreversible photon capture become arbitrarily broadband and fast?

In the symmetric resonant model the answer is no.

A particularly useful result emerges:

> **Peak transfer between an optical bath and a detector bath can remain perfectly matched while the dressed transfer linewidth collapses as `1/g` in the deep-strong-coupling limit.**

This is closely related to established light-matter decoupling and breakdown-of-Purcell-effect physics. No novelty is claimed for the Hopfield theory or decoupling phenomenon.

---

## 2. Gauge-consistent two-mode Hopfield model

Set `hbar = 1` temporarily.

Use one photonic oscillator `a` with bare frequency `omega_c` and one bosonic material oscillator `b` with bare frequency `omega_b`:

```math
H_S
=
\omega_c a^\dagger a
+\omega_b b^\dagger b
+i g(a b^\dagger-a^\dagger b)
+i g(a^\dagger b^\dagger-a b)
+D(a+a^\dagger)^2.
```

The first interaction term is corotating, the second counterrotating, and `D` is the diamagnetic/self-interaction contribution.

Impose the Thomas-Reiche-Kuhn-consistent choice used in the cited Hopfield treatment:

```math
\boxed{D=\frac{g^2}{\omega_b}.}
```

This is the same two-mode model analyzed by Palafox et al., *Journal of Physics: Photonics* 7, 04LT02 (2025), DOI `10.1088/2515-7647/ae1649`, and is closely related to the deep-strong decoupling analysis of De Liberato, *Physical Review Letters* 112, 016401 (2014).

---

## 3. Exact polariton frequencies

The Hopfield eigenfrequencies are

```math
2\omega_{x,y}^2
=
\omega_c^2+\omega_b^2+4D\omega_c
\pm
\sqrt{
(\omega_c^2-\omega_b^2+4D\omega_c)^2
+16g^2\omega_c\omega_b
}.
```

Now specialize to the clean symmetric case

```math
\omega_c=\omega_b\equiv\omega_0.
```

Then

```math
D=\frac{g^2}{\omega_0}.
```

The two frequencies reduce exactly to

```math
\boxed{
\omega_+
=\sqrt{\omega_0^2+g^2}+g,
}
```

```math
\boxed{
\omega_-
=\sqrt{\omega_0^2+g^2}-g.
}
```

They obey

```math
\boxed{\omega_+\omega_-=\omega_0^2.}
```

For

```math
g\gg\omega_0,
```

```math
\boxed{
\omega_+
\simeq
2g+rac{\omega_0^2}{2g},
}
```

while

```math
\boxed{
\omega_-
\simeq
\frac{\omega_0^2}{2g}.
}
```

Thus increasing bare coupling does not leave a fixed resonance at `omega_0`; the dressed spectrum separates into one very high and one very low polariton branch.

---

## 4. Exact resonant mixing angle

The Hopfield rotation angle satisfies

```math
\tan(2\theta)
=
\frac{4g\omega_0}
{4g^2}
=
\frac{\omega_0}{g}.
```

For the continuous branch with `0 < theta <= pi/4`, define

```math
u
\equiv
\frac{\omega_+}{\omega_0}
=
\sqrt{1+(g/\omega_0)^2}
+\frac{g}{\omega_0}.
```

Then

```math
\boxed{
\tan\theta
=\frac{1}{u}
=\frac{\omega_-}{\omega_0}
=\frac{\omega_0}{\omega_+}.
}
```

This identity is what produces the exact symmetric bath-coupling simplification below.

---

## 5. Optical and detection reservoirs

Interpret the two local weak reservoirs as:

- **left bath** — the useful propagating optical input/output channel, locally coupled to the photonic coordinate;
- **right bath** — an irreversible detector/localization reservoir, locally coupled to the material coordinate.

Let their bare amplitude-damping strengths in the wideband approximation be

```math
\gamma_L,
\qquad
\gamma_R.
```

The strong light-matter interaction belongs inside `H_S` and is diagonalized first. The system-bath couplings remain weak so a global dressed-basis master/input-output treatment is used.

For the upper polariton, the dressed amplitude-decay contributions are

```math
\Gamma_{+,L}
=
\gamma_L
\cos^2\theta
\frac{\omega_0}{\omega_+},
```

```math
\Gamma_{+,R}
=
\gamma_R
\sin^2\theta
\frac{\omega_+}{\omega_0}.
```

For the lower polariton,

```math
\Gamma_{-,L}
=
\gamma_L
\sin^2\theta
\frac{\omega_0}{\omega_-},
```

```math
\Gamma_{-,R}
=
\gamma_R
\cos^2\theta
\frac{\omega_-}{\omega_0}.
```

These are the dressed-rate factors appearing in the global Hopfield master-equation treatment.

---

## 6. Symmetric baths give exact rate matching at every coupling

Now set

```math
\gamma_L=\gamma_R\equiv\gamma.
```

Using

```math
\tan\theta=\frac{1}{u},
```

one finds for **both** polaritons

```math
\Gamma_{+,L}
=\Gamma_{+,R}
=\Gamma_{-,L}
=\Gamma_{-,R}
=
\gamma\frac{u}{u^2+1}.
```

Since

```math
u+\frac1u
=2\sqrt{1+(g/\omega_0)^2},
```

this simplifies to

```math
\boxed{
\Gamma_{\pm,L}
=
\Gamma_{\pm,R}
=
\frac{\gamma}
{2\sqrt{1+(g/\omega_0)^2}}.
}
```

This exact equality is the central result of the symmetric reduction.

The optical and irreversible detector channels remain **critically matched** for each dressed polariton even as the internal light-matter coupling becomes arbitrarily large.

---

## 7. Peak transfer can remain unity

In the regime where one dressed polariton can be treated as a resolved resonance, its linear single-photon / weak-signal transfer probability between the left and right reservoirs has the usual resonant form

```math
T_j(\delta)
=
\frac{
4\Gamma_{j,L}\Gamma_{j,R}
}
{\delta^2+(\Gamma_{j,L}+\Gamma_{j,R})^2},
```

where `j` is `+` or `-` and `delta` is detuning from that polariton.

Because

```math
\Gamma_{j,L}=\Gamma_{j,R},
```

```math
\boxed{T_j(0)=1.}
```

Thus deep-strong light-matter coupling does **not** necessarily destroy monochromatic peak transfer in this ideal symmetric two-reservoir model.

Instead, the cost appears in linewidth.

---

## 8. Exact transfer-linewidth collapse

Define the total amplitude-decay rate of either resolved polariton as

```math
\kappa_j
\equiv
\Gamma_{j,L}+\Gamma_{j,R}.
```

The symmetric result gives

```math
\boxed{
\kappa_+
=\kappa_-
=
\frac{\gamma}
{\sqrt{1+(g/\omega_0)^2}}.
}
```

At matched coupling,

```math
T_j(\delta)
=
\frac{\kappa_j^2}
{\delta^2+\kappa_j^2}.
```

Therefore the angular-frequency FWHM is

```math
\boxed{
\Delta\omega_{j,\rm FWHM}
=2\kappa_j
=
\frac{2\gamma}
{\sqrt{1+(g/\omega_0)^2}}.
}
```

The frequency-integrated transfer area of one resolved Lorentzian is

```math
\boxed{
\int_{-\infty}^{\infty}
T_j(\omega)\,d\omega
=
\pi\kappa_j
=
\frac{\pi\gamma}
{\sqrt{1+(g/\omega_0)^2}}.
}
```

In the deep-strong limit,

```math
\boxed{
\Delta\omega_{j,\rm FWHM}
\simeq
2\gamma\frac{\omega_0}{g},
}
```

and

```math
\boxed{
\int T_j\,d\omega
\simeq
\pi\gamma\frac{\omega_0}{g}.
}
```

So despite unit peak transfer,

```math
\boxed{
\text{usable resonant transfer bandwidth}
\propto g^{-1}
\to0.
}
```

This is a nonperturbative version of penalty migration.

---

## 9. Relation to established deep-strong decoupling

Palafox et al. derive dressed polariton decay rates in the same two-mode Hopfield model and show that, with one local bath connected, both polariton decay rates fall asymptotically as `1/g` in the deep-strong regime.

They also show that steady heat current between two baths vanishes as `1/g`.

De Liberato previously showed, through an input-output treatment, that sufficiently deep strong coupling can reverse the ordinary Purcell trend and lead to effective light-matter decoupling.

The present symmetric calculation is consistent with that prior physics.

The repository-specific interpretation is simply:

> When the right reservoir is regarded as the irreversible photodetection channel, arbitrarily increasing the internal light-matter coupling does not yield arbitrarily broadband photon capture. The dressed modes decouple from **both** the optical and detector reservoirs.

No priority claim is made for this phenomenon.

---

## 10. An even stronger obstruction at fixed signal carrier

The previous linewidth calculation is generous because it allows the signal to follow one of the shifted polariton resonances.

But the original bare transition frequency is `omega_0`.

As `g` grows,

```math
\omega_+\to2g,
\qquad
\omega_-\to\frac{\omega_0^2}{2g}.
```

Neither dressed resonance remains near `omega_0`.

Therefore, for a signal whose carrier frequency is held fixed at the original `omega_0`, increasing `g` eventually moves the resonant spectral weight away from the desired signal rather than creating a broader detector centered on it.

A possible escape is to retune the bare material/cavity frequencies as `g` changes. That is a different resource-constrained problem and has not yet been analyzed.

---

## 11. Domain of the transfer formula

The independent-resonance transfer expression is appropriate when

- the system-bath couplings are weak compared with the dressed frequencies;
- the relevant polariton is spectrally resolved;
- a global dressed-basis system-bath description is valid;
- the baths are sufficiently broadband over the polariton linewidth.

It should not be used in the nearly degenerate `g -> 0` limit, where the polariton separation can become comparable to bath-induced linewidths and secularizing the two dressed resonances separately is not controlled.

The exact Hopfield eigenfrequencies themselves remain valid outside that open-system approximation.

---

## 12. What this closes

The earlier perturbative loophole was

```text
make LDOS larger
-> make gamma_o larger
-> make detector arbitrarily fast.
```

The Hopfield analysis shows why this cannot simply be extrapolated through arbitrary coupling:

```text
weak coupling:
Purcell enhancement / faster exchange

ultrastrong coupling:
strongly hybridized polaritons

deep strong coupling:
reservoir overlaps fall
-> transfer linewidth collapses ~ 1/g.
```

Thus an arbitrarily large **bare internal coupling constant** is not itself a route to arbitrarily large useful detector bandwidth in this gauge-consistent quadratic model.

---

## 13. What remains open

This does not yet establish a universal photodetector theorem.

Possible escapes or generalizations include:

1. retuning bare frequencies with coupling so that one dressed pole remains at a fixed target carrier;
2. multimode rather than two-mode electromagnetic environments;
3. nonbosonic finite-level matter beyond the harmonic Hopfield approximation;
4. active/time-varying or nonreciprocal environments;
5. structured detector reservoirs rather than wideband local damping;
6. direct detector-reservoir coupling to different microscopic observables;
7. strong coupling of the dressed system to the reservoirs, where the weak-bath global master equation no longer applies.

The most immediate adversarial test is **retuning**:

> Can `omega_c(g)` and `omega_b(g)` be varied so that one polariton remains at the desired photodetection frequency while its matched optical-to-detector transfer bandwidth grows rather than collapses?

That question should be answered before treating deep-strong decoupling as a general speed bound.
