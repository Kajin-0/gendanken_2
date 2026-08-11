# Spectral-depth closure tests for falsifying photocarrier transport from Shockley-Ramo current

**Draft date:** 2026-08-10  
**Status:** working theory manuscript; priority explicitly unresolved; no `first`, `novel`, or equivalent priority claim

---

## Abstract

Photodetector frequency response is commonly interpreted by selecting a transport model and fitting material or circuit parameters to measured amplitude and phase.  We ask a different question: **can the detector be made to falsify simple transport hypotheses before a richer model is fitted?**  The key experimental resource is wavelength-dependent generation depth.  In a monotonic absorber, several wavelengths can be selected so that their calibrated carrier-generation coordinates are equally spaced inside the device.  We show that, after treating terminal-current formation with the Shockley-Ramo theorem, a homogeneous one-carrier planar detector obeys an exact four-channel spatial closure,

```math
(J_2-J_1)^2=(J_1-J_0)(J_3-J_2),
```

where `J_m` is the complex raw modulated terminal current per calibrated generated-carrier amplitude.  Spatial first differences isolate the internal propagation multiplier and remove a wavelength-independent complex gain and additive offset.  For uniform drift-diffusion with first-order recombination, four channels at DC plus the same four channels at one nonzero modulation frequency determine the diffusion coefficient, drift velocity, and recombination rate algebraically; every additional RF frequency introduces no new transport parameter and therefore becomes a null test.  If the one-mode closure fails, six internal coordinates test a two-mode model.  An exact Hankel-minor identity,

```math
W_m=d_md_{m+2}-d_{m+1}^2
=ab(q_1q_2)^m(q_1-q_2)^2,
```

both supplies a rank-two closure and exposes the mode-resolution boundary as two spatial roots merge or one observable amplitude vanishes.  Finite scalar boundaries and conventional electron-hole transport then obey different RF root constraints, allowing ordinary explanations to be tested before invoking anomalous transport.  We derive leading corrections from wavelength-dependent optical-source shape, amplitude calibration, internal-coordinate distortion, and independent measurement noise.  In the deterministic high-Peclet limit, the low-frequency four-channel phase closure measures a local combination of derivatives of the inverse carrier velocity.  As a worked example, a conditional graded-HgCdTe model predicts a gradient-sensitive four-channel phase closure of approximately `-0.012 deg` at `100 MHz`, `-0.059 deg` at `500 MHz`, and `-0.110 deg` at `1 GHz`; an independent shooting implementation reproduces the stochastic calculation.  The framework does not claim that wavelength-dependent photodiode timing, Shockley-Ramo signal formation, Hankel model identification, or drift-diffusion inversion are new.  Its purpose is to combine an internal spectral coordinate with observable-corrected spatial and RF closure relations into a deliberately falsification-driven transport measurement.

---

# I. Introduction

A photodetector impulse or frequency response contains information about carrier generation, transport, recombination, contacts, internal electric fields, and the external readout chain.  The usual inverse problem is therefore underdetermined in spirit even when a particular numerical fit is well conditioned: several physical mechanisms can change the same measured phase or bandwidth, and a flexible model can often absorb a discrepancy without establishing which assumption actually failed.

The present work takes a different approach.  Instead of beginning with a detailed transport model and asking how accurately its parameters can be fitted, we begin with deliberately simple **null hypotheses** and ask what exact relations measured data must satisfy if those hypotheses are correct.  A model is promoted only after the lower-order alternative survives its closure tests.  The goal is not to eliminate modeling.  It is to order the modeling process so that additional physics is introduced because a simpler model has been falsified rather than because a larger parameter set fits better.

The spatial coordinate required for such a test can, in suitable photodetectors, be supplied optically.  Wavelength-dependent absorption depth and the associated phase or bandwidth variation of photodiodes are established phenomena.  Optoelectronic chromatic dispersion has, for example, used wavelength-dependent carrier-generation depth to encode wavelength in RF phase [4].  More recent work has combined DC response and multi-frequency RF amplitude and phase for single-photodiode computational spectroscopy.  Likewise, time-domain Hankel methods have been applied to photodetector impulse responses to determine dynamical model order [5].  We do **not** claim these ingredients as new.

The question considered here is narrower:

> **What exact spatial closure relations follow if wavelength is calibrated as an internal source coordinate, the terminal current is treated with Shockley-Ramo signal formation, and the resulting spatial propagation modes are required to obey a common physical law across RF frequency?**

Three gedanken experiments organize the answer.

1. **Four internal source coordinates, one RF frequency.**  Does one homogeneous first-difference propagation mode describe the measured current?
2. **The same coordinates at DC and another RF frequency.**  Do one real diffusion coefficient, drift velocity, and recombination rate survive the change in clock frequency?
3. **If one spatial mode fails, six internal coordinates.**  Are exactly two ordinary modes sufficient, and do their RF roots obey the constraints of a finite boundary or two conventional carrier species?

This hierarchy is intentionally conservative.  A failed four-channel law is not labeled nonlocal transport: an ordinary electron-hole pair or a finite boundary is already sufficient to break it.  A rank-two fit is not automatically interpreted physically: the second-mode Hankel minor must first be statistically resolved.  Only after lower-order optical, signal-formation, boundary, and model-order explanations have been tested do we interpret a residual in terms of transport inhomogeneity or richer carrier dynamics.

The analysis is developed first in one dimension because the objective is to derive exact falsifiable statements rather than an immediately comprehensive device model.  A graded HgCdTe absorber is then used as a worked material example.  HgCdTe is particularly useful because its composition-dependent bandgap can make wavelength a strong internal generation coordinate, while graded-bandgap transport and high-speed response are already experimentally established [6].  The material calculation is presented as a conditional prediction under explicit assumptions, not as a calibrated forecast for a named detector.

---

# II. Observable first: collection flux is not terminal current

## A. First-passage transform

Consider one signal carrier generated a distance `d` from a collecting boundary.  Let `T_d` be its successful first-passage time and define

```math
U(d,s)=\mathbb E[e^{-sT_d}].
\tag{1}
```

For a homogeneous scalar first-passage process, spatial translation and the strong-Markov property imply a multiplicative semigroup,

```math
U(d_1+d_2,s)=U(d_1,s)U(d_2,s).
```

Under continuity in `d`,

```math
\boxed{
U(d,s)=e^{-\gamma(s)d}.
}
\tag{2}
```

For uniform drift-diffusion with downstream drift `w>0`, diffusion coefficient `D>0`, and uniform first-order recombination/killing rate `\kappa`, the propagation exponent satisfies

```math
\boxed{
D\gamma^2+w\gamma=\kappa+s.
}
\tag{3}
```

Equation (2) is a statement about an arrival/collection-flux observable.  It is not, by itself, the measured terminal-current transfer function.

## B. Shockley-Ramo current as a survival observable

The distinction follows directly from signal formation.  Let `p(x,t)` be the density of carriers still present in a one-dimensional homogeneous transport region terminating at an absorbing collector `x=L`.  With constant drift and diffusion,

```math
\partial_t p=-\partial_x j,
\qquad
j=wp-D\partial_xp.
\tag{4}
```

Define the first-passage survival probability

```math
S(t)=\int_{-\infty}^{L}p(x,t)\,dx.
\tag{5}
```

For a uniform planar weighting field `E_w`, the Shockley-Ramo theorem [1,2] gives the ensemble induced current

```math
I(t)=qE_w\int_{-\infty}^{L}j(x,t)\,dx.
```

If `p` vanishes at the absorbing collector and remote upstream boundary, the diffusion boundary term cancels and

```math
\boxed{
I(t)=qE_w w S(t).
}
\tag{6}
```

Since the first-passage density is `f_T=-dS/dt`,

```math
\widetilde S(s)=\frac{1-U(d,s)}{s}
```

without recombination.  Hence

```math
\boxed{
J(d,s)=qE_w w\frac{1-U(d,s)}{s}.
}
\tag{7}
```

With independent uniform Markov recombination at rate `\kappa`, the alive-and-uncollected probability acquires the factor `e^{-\kappa t}`, giving the same spatial form with a depth-independent prefactor,

```math
\boxed{
J(d,s)=C(s)\left[1-e^{-\gamma(s)d}\right],
}
\tag{8}
```

where `\gamma` obeys Eq. (3).

This observable correction is central.  A deterministic carrier provides the simplest counterexample to conflating arrival and current.  Its arrival response is `e^{-i\omega d/w}`, whereas its planar Shockley-Ramo current is a rectangular pulse whose Fourier transform is proportional to

```math
\frac{1-e^{-i\omega d/w}}{i\omega}.
```

Thus the direct three-position geometric-mean law applies to the ideal arrival field, not to generic terminal current.  The measured-current construction requires one additional spatial difference.

---

# III. Gedanken experiment I: four colors isolate one spatial propagator

## A. Four equally spaced internal source coordinates

Let four optical channels generate carriers at calibrated internal source coordinates

```math
d_m=d_0+mh,
\qquad m=0,1,2,3.
\tag{9}
```

For the moment, treat each source as point-like.  From Eq. (8),

```math
J_m=A+Bq^m,
\qquad
q=e^{-\gamma h},
\tag{10}
```

where all depth-independent factors have been absorbed into `A` and `B`.

Define first spatial differences

```math
\Delta J_m=J_{m+1}-J_m.
\tag{11}
```

Then

```math
\Delta J_m=B(q-1)q^m,
\tag{12}
```

so the three first differences form a geometric sequence.  The resulting exact four-channel closure is

```math
\boxed{
(J_2-J_1)^2
=(J_1-J_0)(J_3-J_2).
}
\tag{13}
```

Equation (13) is the minimal terminal-current null considered in this paper.

Three coordinates estimate the spatial multiplier,

```math
\boxed{
q
=\frac{J_2-J_1}{J_1-J_0},
}
\tag{14}
```

and the fourth asks whether the same multiplier predicts the next step.  The spatial propagation exponent follows as

```math
\boxed{
\gamma
=-\frac{1}{h}\log q,
}
\tag{15}
```

with the logarithm branch tracked continuously as frequency or source coordinate is varied.

## B. Why the null is experimentally attractive

At fixed RF frequency, suppose the measured spectral channels share an arbitrary complex chain gain `G(\omega)` and common complex offset `C(\omega)`:

```math
J_m^{\rm meas}=GJ_m+C.
\tag{16}
```

First differences remove `C` and multiply every `\Delta J_m` by the same `G`; Eq. (13) is unchanged.  Therefore common RF gain, common RF phase, and wavelength-independent additive offset do not need to be known to test the one-mode closure.

The remaining requirements are relative rather than absolute: the optical channels must be calibrated to the intended internal coordinate and to a common generated-carrier modulation amplitude, and wavelength-dependent external transfer factors must be bounded or modeled.

## C. Finite generation width

Point generation is not required.  Let the generation distribution for channel `m` be one fixed shape translated by `d_m`:

```math
p_m(d)=g(d-d_m).
```

Averaging Eq. (8) over `g` gives

```math
J_m=A+\widetilde B q^m,
```

where the finite source shape appears only in `\widetilde B`.  Equation (13) therefore survives arbitrary source width, asymmetry, or multimodality under **rigid translation**.

The relevant optical systematic is not finite width itself but wavelength-dependent **shape evolution**.  We quantify that correction in Sec. VI.

## D. Affine coordinate calibration is sufficient for the null

Suppose the spectral coordinate `\mu` is mapped to the true physical coordinate by

```math
z=a+b\mu.
\tag{17}
```

Four equally spaced values of `\mu` remain equally spaced in `z`; Eq. (13) is exact for arbitrary offset `a` and nonzero scale `b`.  Thus the basic model-order null does not require absolute knowledge of the depth origin or scale.  The scale becomes necessary only when the dimensionless multiplier is converted into physical `D`, `w`, or `\kappa`.

---

# IV. Gedanken experiment II: one RF identifies, the next RF falsifies

The four-channel test isolates `\gamma(s)` before any transport coefficient is fitted.  We now impose the more specific hypothesis of homogeneous real drift-diffusion with uniform Markov recombination, Eq. (3).

## A. No-recombination limit

When `\kappa=0`, let

```math
\gamma(i\omega)=a+ib.
```

Separating real and imaginary parts of

```math
D\gamma^2+w\gamma=i\omega
```

gives the exact inversion

```math
\boxed{
D
=\frac{\omega a}
{b(a^2+b^2)},
}
\tag{18}
```

```math
\boxed{
w
=\frac{\omega(b^2-a^2)}
{b(a^2+b^2)}.
}
\tag{19}
```

For `D>0`, `w>0`, and `\omega>0` on the downstream branch,

```math
\boxed{0<a<b.}
\tag{20}
```

One RF frequency therefore identifies the two material coefficients within the stated model.  A second frequency introduces no additional parameter and predicts

```math
\boxed{
D(\omega_2)=D(\omega_1),
\qquad
w(\omega_2)=w(\omega_1).
}
\tag{21}
```

## B. Complete inversion with recombination

Uniform recombination does not add another spatial mode.  Use the four-channel sequence at DC to obtain

```math
g_0=\gamma(0)
```

and at one nonzero RF to obtain

```math
g_\omega=\gamma(i\omega).
```

The DC and RF equations are

```math
Dg_0^2+wg_0=\kappa,
\tag{22}
```

```math
Dg_\omega^2+wg_\omega=\kappa+i\omega.
\tag{23}
```

Subtract them and define

```math
A=g_\omega^2-g_0^2,
\qquad
B=g_\omega-g_0,
```

```math
\Delta
=\Re A\,\Im B-
\Im A\,\Re B.
\tag{24}
```

For `\Delta\neq0`, the real coefficients are

```math
\boxed{
D=-\frac{\omega\Re B}{\Delta},
}
\tag{25}
```

```math
\boxed{
w=\frac{\omega\Re A}{\Delta},
}
\tag{26}
```

and

```math
\boxed{
\kappa=Dg_0^2+wg_0.
}
\tag{27}
```

Thus four spectral channels at DC plus the same four channels at one nonzero RF frequency determine the complete homogeneous three-parameter Markov model.  Every additional RF frequency is overdetermined and must reproduce the same real `D`, `w`, and `\kappa`.

The experimental philosophy is therefore unusually simple:

> **DC plus one RF identifies the minimal model; the next RF frequency tries to kill it.**

A frequency-dependent fitted `D(\omega)` is not the first interpretation of a disagreement.  It is evidence that the stated homogeneous Markov model has failed and that a higher rung of the hierarchy should be tested.

---

# V. Gedanken experiment III: when one spatial mode fails

A nonzero four-channel residual does not establish anomalous transport.  Two completely conventional mechanisms already generate two spatial modes: a finite boundary and a second signal carrier.

## A. Six coordinates and the exact two-mode witness

Use six source coordinates, producing five first differences.  Suppose

```math
d_m=a q_1^m+b q_2^m,
\qquad m=0,\ldots,4.
\tag{28}
```

Define the adjacent `2\times2` Hankel minors

```math
W_m=d_md_{m+2}-d_{m+1}^2.
\tag{29}
```

Direct substitution gives

```math
\boxed{
W_m
=ab(q_1q_2)^m(q_1-q_2)^2.
}
\tag{30}
```

Several useful consequences follow at once.

First, the six-channel rank-two closure can be written

```math
\boxed{
W_1^2=W_0W_2.
}
\tag{31}
```

or equivalently as the vanishing `3\times3` Hankel determinant of the five first differences.

Second,

```math
\boxed{
\frac{W_{m+1}}{W_m}=q_1q_2
}
\tag{32}
```

when the denominator is nonzero.  The recurrence

```math
d_{m+2}=S d_{m+1}-P d_m
```

then gives `S=q_1+q_2` and `P=q_1q_2`.

Most importantly, Eq. (30) exposes the identifiability boundary.  Evidence for two distinct modes vanishes if either observable mode amplitude is zero or if the roots merge, and it collapses quadratically as `|q_1-q_2|\to0`.  The determinant of the two-equation recurrence system is itself `W_0`; root recovery is therefore expected to become unstable exactly where the data cease to resolve the second mode.

## B. Noise significance of the second mode

Let `J_0,\ldots,J_3` have independent circular complex RMS noise `\sigma_J`.  Linearizing

```math
W_0=d_0d_2-d_1^2
```

gives

```math
\delta W_0
=-d_2\epsilon_0
+(d_2+2d_1)\epsilon_1
-(d_0+2d_1)\epsilon_2
+d_0\epsilon_3.
\tag{33}
```

Therefore

```math
\boxed{
\sigma_{W_0}^2
=\sigma_J^2
\left[
|d_2|^2+|d_2+2d_1|^2+
|d_0+2d_1|^2+|d_0|^2
\right].
}
\tag{34}
```

Near equal current steps `d_0\simeq d_1\simeq d_2=d`,

```math
\sigma_{W_0}\simeq\sqrt{20}|d|\sigma_J.
\tag{35}
```

For two comparable visible modes, define `\eta=\sigma_J/|d|`.  The near-coalescence significance scales approximately as

```math
Z_2
\simeq
\frac{|q_1-q_2|^2}
{4\sqrt{20}\,\eta}.
\tag{36}
```

A `3\sigma` design scale is therefore

```math
\boxed{
|q_1-q_2|
\gtrsim7.33\sqrt{\eta}.
}
\tag{37}
```

For `\eta=10^{-4}`, the two multipliers need to differ by approximately `0.073`; for `\eta=10^{-5}`, by approximately `0.023`.  The exact threshold depends on relative complex mode amplitudes and the full covariance, but Eq. (37) demonstrates that the six-channel extension has a finite resolvable region rather than being only a noiseless algebraic construction.

## C. Finite scalar boundary

For uniform `D`, `w`, and `\kappa`, any linear finite-boundary conditions alter only the amplitudes of the two homogeneous roots of

```math
D r^2+w r-(\kappa+i\omega)=0.
\tag{38}
```

Once the two roots are recovered from the six-channel sequence, Vieta's formulas require

```math
\boxed{
r_++r_-=-\frac{w}{D}
}
\tag{39}
```

to be real and RF-independent, and

```math
\boxed{
r_+r_-=-\frac{\kappa+i\omega}{D}.
}
\tag{40}
```

Thus

```math
D=-\frac{\omega}{\Im(r_+r_-)},
\quad
w=-D\Re(r_++r_-),
\quad
\kappa=-D\Re(r_+r_-).
\tag{41}
```

The arbitrary boundary amplitudes do not enter these coefficient tests.

## D. Two conventional carrier species

An electron-hole pair can also yield rank two.  In a homogeneous independent-carrier model,

```math
J(z,s)=C_0(s)+
C_e(s)e^{+\gamma_e(s)z}+
C_h(s)e^{-\gamma_h(s)z}.
\tag{42}
```

Each positive propagation magnitude obeys its own equation,

```math
D_c\gamma_c^2+w_c\gamma_c=\kappa_c+s.
\tag{43}
```

At DC, the signs of the two spatial roots naturally label opposite collection directions in the generic recombining case.  Track those roots continuously to one RF frequency and apply Eqs. (25)-(27) separately to each species.  Six coordinates at DC plus one RF can therefore determine

```math
(D_e,w_e,\kappa_e),
\qquad
(D_h,w_h,\kappa_h),
```

in generic noiseless data.  Every additional RF frequency simultaneously overdetermines both triples.

The central point is methodological rather than algebraic: **model-order failure is diagnosed before a microscopic mechanism is named.**  Boundaries and a second carrier are not nuisance terms automatically inserted into the one-mode model; they are separate, testable rungs with their own RF root constraints.

---

# VI. What a controlled four-channel failure measures

Once the one-mode observable and optical-source hypotheses have been controlled, a small closure residual can be related to spatially varying transport.

Consider deterministic downstream transit with local slowness

```math
q(z)=1/v(z)
```

and a uniform weighting field.  For a point-generated carrier at `z`, the raw-current transform is, up to a depth-independent factor,

```math
J(z,s)
=\int_z^L
\exp\left[-s\int_z^xq(u)du\right]dx.
\tag{44}
```

At low frequency,

```math
J(z,s)=(L-z)-sA(z)+O(s^2),
```

with

```math
A(z)=\int_z^L(L-u)q(u)du.
```

For four equally spaced source depths with spacing `h` and quartet midpoint `z_c`, the logarithmic closure

```math
\mathcal C_4
=2\ln\Delta J_1-
\ln\Delta J_0-
\ln\Delta J_2
```

obeys

```math
\boxed{
\mathcal C_4
=-s h^2
\left[
2q'(z_c)-(L-z_c)q''(z_c)
\right]
+O(sh^4,s^2).
}
\tag{45}
```

For locally linear slowness,

```math
\boxed{
\frac{\Im\mathcal C_4}{\omega}
=-2h^2q'(z_c)
}
\tag{46}
```

under the `e^{-i\omega t}` convention.

Equation (46) is deliberately not applied to every nonzero four-channel residual.  It is the **positive prediction after** lower-order alternatives have been controlled: one spatial mode must remain appropriate, source-shape evolution must be bounded, and the high-Peclet local expansion must be justified.

---

# VII. Optical and calibration errors have finite-difference structure

## A. Wavelength-dependent source shape

Let channel `m` have generation distance

```math
D_m=\mu_m+U_m,
\qquad
\mathbb E[U_m]=0,
```

with equally spaced means `\mu_m=\mu_0+mh` and centered variances `v_m=\sigma_m^2`.  Expanding the homogeneous raw-current closure gives the leading source-width error

```math
\boxed{
\mathcal C_{4,\mathrm{opt}}
=\frac{\gamma}{2h}
(v_3-3v_2+3v_1-v_0)
+O(\gamma^2).
}
\tag{47}
```

The first-order correction is therefore proportional to the **third discrete difference** of the generation variance.  Constant, linear, or quadratic variance evolution across the quartet produces no first-order width contamination.  This cancellation does not eliminate optical modeling: higher centered moments and higher powers of `\gamma` remain.

## B. Relative generated-carrier and external-gain calibration

At sufficiently low RF, the ideal raw current is locally affine in the source coordinate.  If a small residual multiplicative channel error remains,

```math
\widetilde J_m=(1+\epsilon_m)J_m,
```

the first-order closure error is

```math
\boxed{
\delta\mathcal C_4
=-\frac{\Delta^3(\epsilon_mJ_m)}{B},
}
\tag{48}
```

where `B` is the affine current step.  Common fractional gain and a linear fractional spectral drift cancel to first order.  The dangerous component is channel-to-channel irregularity or higher spectral curvature.

## C. Internal-coordinate distortion

If the true coordinate is `z=f(\mu)`, affine `f=a+b\mu` leaves Eq. (13) exact.  For a smooth nonlinear map,

```math
\boxed{
\mathcal C_{4,\mathrm{coord}}
=h^2\left[
\gamma f''-(\ln f')''
\right]_{\mu_c}
+O(h^4).
}
\tag{49}
```

Thus absolute depth origin and common scale error do not produce false model-order failure.  Local curvature in the wavelength-to-depth mapping does.

## D. Initial excess-energy state

Wavelength can change not only generation depth but also photon excess energy.  A useful ideal result limits this confound.  Let

```math
E_g(z)=E_{g0}-Gz
```

and suppose the local absorption coefficient depends only on the local photon excess energy

```math
u=E_\gamma-E_g(z),
\qquad
\alpha=\alpha(\nu).
```

Changing photon energy translates the threshold depth, but the generation distribution expressed in `\nu` is

```math
\boxed{
p_\nu(\nu)
=\frac{\alpha(\nu)}{G}
\exp\left[-\frac{1}{G}
\int_0^\nu\alpha(u)du\right],
}
\tag{50}
```

which is independent of photon energy in the untruncated ideal limit.  Thus a graded absorber can translate the generation coordinate while preserving the complete **total excess-energy distribution**.  Real bandstructure and absorption violate the assumptions quantitatively; the HgCdTe example below is close in its first two excess-energy moments but not exactly invariant.

---

# VIII. Independent-noise cost and spatial spacing

The same finite differences that reject low-order systematics amplify uncorrelated noise.

Let independent circular complex errors have `\mathbb E|\epsilon_m|^2=\sigma_J^2`.  Linearizing the four-channel log closure gives

```math
\delta\mathcal C_4
=\frac{\epsilon_0}{d_0}
-\left(\frac1{d_0}+\frac2{d_1}\right)\epsilon_1
+\left(\frac2{d_1}+\frac1{d_2}\right)\epsilon_2
-\frac{\epsilon_3}{d_2}.
\tag{51}
```

In the equal-step limit,

```math
\boxed{
\sigma_{\mathcal C_4}
\simeq\sqrt{20}\frac{\sigma_J}{|d|},
}
\tag{52}
```

corresponding to the third-difference stencil `(1,-3,3,-1)`.

There is therefore no advantage in taking the internal spacing `h` arbitrarily small.  If the dominant smooth systematic behaves as `Ah^2` and the independent closure noise as `B/h`, the approximate mean-square error

```math
\mathrm{MSE}=A^2h^4+B^2/h^2
```

has the cube-root optimum

```math
\boxed{
h_*=\left(\frac{B}{\sqrt2A}\right)^{1/3}.
}
\tag{53}
```

Under white averaging, `\sigma_J\propto t^{-1/2}`, so `h_*\propto t^{-1/6}`.  Experimental geometry and systematic cancellation therefore improve usable spatial resolution much more effectively than brute-force integration alone.

---

# IX. Conditional HgCdTe worked prediction

## A. Optical model and spectral coordinates

We now ask whether the corrected four-channel closure produces a finite, internally consistent signal in a recognizable graded infrared material.  The example is deliberately simple and is **not** a model of a named fabricated detector.

Take a `7.6 \mu\mathrm m` HgCdTe absorber at `300 K` with a linear composition profile

```text
x(0)=0.55,
qquad
x(L)=0.32.
```

The bandgap is computed from the Hansen-Schmit-Casselman empirical relation [8], and above-gap absorption from the Moazzami et al. HgCdTe model [9].  Four wavelengths are chosen so the conditional mean generation depths are

```math
\boxed{
2.5,\ 3.0,\ 3.5,\ 4.0\ \mu\mathrm m.
}
\tag{54}
```

The corresponding modeled wavelengths are approximately

```text
2.134651,
2.215042,
2.301173,
2.393907 um,
```

and all four modeled absorbed fractions exceed `0.9993`.  The conditional generation widths are approximately `0.79 \mu\mathrm m`, so the calculation is not a delta-source stress.

The generation-weighted total photon excess energy above the local bandgap is also nearly matched across the quartet: its mean varies only from approximately `52.35` to `52.48 meV`, and its standard deviation from approximately `33.24` to `32.69 meV`.  This is consistent with the graded-gap invariance mechanism of Eq. (50), while leaving electron-hole partition and finite thermalization memory as possible higher-order corrections.

## B. Conditional transport stress

Use a mobility sensitivity scale of `9000 cm^2 V^{-1} s^{-1}`, Einstein diffusion at `300 K`, the quasi-neutral composition-gap force scale developed in the model, an `8 kV cm^{-1}` velocity-saturation sensitivity scale, and the reduced density-of-states gradient correction.  These are explicit sensitivity coordinates, not claimed room-temperature constants for a particular device.

The resulting downstream drift varies from approximately

```math
3.76\times10^4
\quad\mathrm{to}\quad
3.21\times10^4\ \mathrm{m/s}.
```

Finite diffusion is retained through the backward equation for the expected discounted raw induced current,

```math
\boxed{
D J''(z)+v(z)J'(z)-[\kappa+s]J(z)=-v(z).
}
\tag{55}
```

The collector condition is `J(L)=0`.  To avoid reintroducing the reflecting-boundary confound that invalidated an earlier calculation, the optical entrance is matched mathematically to a bounded semi-infinite homogeneous continuation rather than treated as a reflecting surface.

For each RF frequency, Eq. (55) is averaged over the four full Hansen/Moazzami generation kernels.  A homogeneous comparison uses the **same optical kernels, diffusion coefficient, and recombination rate**, but replaces the graded drift by its path-harmonic mean.  The difference between the two four-channel closures is called the gradient-sensitive excess.

## C. Predicted closure scale

For `\kappa=0`, the stochastic calculation gives approximately

| RF frequency | Graded-current closure phase | Homogeneous same-optics phase | Gradient-sensitive excess |
|---:|---:|---:|---:|
| `100 MHz` | `-0.00952 deg` | `+0.00246 deg` | **`-0.01198 deg`** |
| `500 MHz` | `-0.04643 deg` | `+0.01230 deg` | **`-0.05873 deg`** |
| `1 GHz` | `-0.08572 deg` | `+0.02470 deg` | **`-0.11041 deg`** |

The deterministic point-source low-frequency theorem, Eq. (45), predicts approximately `-0.01254 deg` at `100 MHz` for the same velocity profile and spacing, close to the full finite-width diffusion result.

Uniform Markov recombination does not erase the effect in the tested range.  An illustrative `10 ns` lifetime gives approximately `-0.01205 deg` excess at `100 MHz`; an illustrative `1 ns` lifetime gives approximately `-0.01275 deg` at the same frequency.

The stochastic result has also been reproduced with a numerically independent adaptive shooting construction.  The canonical sparse finite-difference boundary-value solve and the independent shooting implementation agree on the gradient-sensitive excess to approximately `10^{-6}` degree or better at `100 MHz`, `500 MHz`, and `1 GHz`.

These numbers are falsifiable consequences of the stated model, not predictions for an existing device.

## D. Measurement resource

For independent equal complex current noise, the exact four-sample covariance gives the following approximate `3\sigma` requirements, expressed as amplitude SNR of the mean spatial current step:

| RF frequency | Allowed `\sigma_J/\langle|\Delta J|\rangle` | Amplitude SNR |
|---:|---:|---:|
| `100 MHz` | `1.56\times10^{-5}` | `96.1 dB` |
| `250 MHz` | `3.88\times10^{-5}` | `88.2 dB` |
| `500 MHz` | `7.68\times10^{-5}` | `82.3 dB` |
| `1 GHz` | `1.47\times10^{-4}` | `76.7 dB` |

The cleanest low-frequency asymptotic regime is therefore statistically demanding.  Higher RF frequency increases the predicted gradient-sensitive closure and relaxes the independent-noise requirement, but also increases exposure to parasitic electrical phase, boundaries, extra carrier modes, and nonlocal dynamics.  The theory predicts an experimental tradeoff rather than a universal optimum frequency.

---

# X. Discussion

## A. What a failed closure means

The framework is designed to avoid a common inverse-problem error: treating every deviation from a simple model as evidence for a preferred richer mechanism.

A practical interpretation sequence is instead:

```text
four-channel one-mode closure
        |
        | passes
        v
recover one gamma(s)
        |
        v
DC + RF real D,w,kappa closure


four-channel one-mode closure
        |
        | fails
        v
is the second-mode Hankel witness significant?
        |
        | no
        v
one-mode failure unresolved at present SNR
        |
        | yes
        v
six-channel rank-two closure
        |
        v
recover two spatial roots
        |
        +--> finite-boundary root law?
        |
        +--> two-carrier DD/recombination law?
        |
        +--> neither: richer model required
```

This ordering is the principal conceptual point.  A boundary is not a correction coefficient added automatically.  A second carrier is not a nuisance basis inserted because a fit is poor.  Each is a new model with additional spatial modes and corresponding RF algebra that can itself fail.

## B. Relation to established photodiode frequency-response physics

Wavelength-dependent absorption depth and its effect on photodiode RF phase are established.  Glasser et al. demonstrated optoelectronic chromatic dispersion in a Ge PN photodiode and used the phase dependence for wavelength monitoring [4].  Graded HgCdTe has likewise been shown to modify carrier transport and high-speed detector response; Sang et al. reported a room-temperature graded-bandgap HgCdTe detector with a `1.33 ns` total response time and modeled the composition-gradient built-in field [6].  Direct Shockley-Haynes measurements have independently characterized minority-electron drift velocity, diffusion coefficient, and lifetime in HgCdTe [7].

The present framework does not attempt to establish these phenomena.  It asks whether spectral channels can be arranged as an **internal spatial sequence** and subjected to finite-difference model-order and RF closure tests.

## C. Relation to system identification

Hankel matrices, Prony recurrences, and minimal-realization theory are established tools.  Recent photodetector work has used a Hankel matrix on a **time-sampled detector impulse response** to determine model order [5].  Equation (30) is therefore not presented as new Hankel mathematics.

The distinction considered here is the coordinate on which the sequence is built.  The sequence is not a set of successive time samples of one impulse response.  It is formed from **spectrally selected internal generation coordinates**, after Shockley-Ramo-aware spatial differencing.  The recovered spatial roots are then constrained by transport equations across RF frequency.

Whether this complete spectral-depth construction has appeared previously remains an open priority question.  Targeted searches have not identified an equivalent construction, but a negative literature search is not evidence of priority.  The framework should therefore be judged on the correctness and usefulness of its predictions, not on a claim of being first.

## D. Limits of the one-dimensional model

The exact closures rely on deliberately strong assumptions at the lowest rung.  Real devices can violate them through

- nonuniform weighting field;
- finite depletion regions and contact-specific signal formation;
- spatially varying drift, diffusion, or recombination;
- electron-hole coexistence;
- trapping or internal state populations;
- finite boundaries;
- space charge and carrier-carrier interactions;
- nonlocal or hot-carrier transport;
- wavelength-dependent generation-shape evolution;
- wavelength-dependent external electrical or optical transfer.

The theory does not assert that such effects are small in every photodiode.  Its intended use is precisely the opposite: each effect should be introduced only when the lower-order closure shows that it is needed or when independent device knowledge requires it.

## E. What is directly falsifiable

The paper makes several compact predictions under explicitly nested assumptions.

1. **One homogeneous raw-current mode:** four equally spaced internal source coordinates satisfy Eq. (13).
2. **One homogeneous DD/recombination generator:** DC plus one RF determine `D,w,\kappa`; all additional RF frequencies reproduce them.
3. **Two spatial modes:** the six-channel first-difference minors obey Eq. (31), and the observable second-mode signal scales as `ab(q_1-q_2)^2`.
4. **Finite scalar boundary:** the two recovered roots obey Eqs. (39)-(40) at all RF frequencies.
5. **Two homogeneous carrier species:** each signed root independently obeys Eq. (43) with RF-invariant real coefficients.
6. **Controlled high-Peclet inhomogeneity:** the low-RF four-channel phase closure approaches Eq. (45), and Eq. (46) for locally linear inverse velocity.
7. **Graded-HgCdTe stress:** under the stated conditional optical and transport model, the gradient-sensitive phase excess is approximately `-0.012 deg` at `100 MHz`, `-0.059 deg` at `500 MHz`, and `-0.110 deg` at `1 GHz`.

Each statement can fail.  That is the design criterion.

---

# XI. Conclusion

Wavelength-dependent generation depth can be used for more than fitting a photodiode's phase-versus-wavelength curve.  If several spectral channels are calibrated as internal source coordinates, their complex terminal currents form a spatial sequence that can be subjected to exact model-order and transport-law closure tests.

Correct treatment of the electrical observable is essential.  The carrier first-passage transform is exponential in homogeneous propagation distance, but a planar Shockley-Ramo current is a survival-type observable containing a depth-independent particular term.  Spatial first differencing removes that term.  Four source coordinates then provide an exact one-mode current closure and recover the spatial propagation exponent.  DC plus one RF frequency determine the complete homogeneous drift-diffusion-recombination model; the next RF frequency introduces no new transport parameter and therefore becomes a falsification measurement.

When the one-mode null fails, six coordinates test whether exactly two observable spatial modes suffice.  The exact minor

```math
W_m=ab(q_1q_2)^m(q_1-q_2)^2
```

both gives the rank-two closure and exposes the mode-separation limit.  Finite boundaries and two conventional carrier species then make different RF root predictions.  A richer physical model is warranted only if these lower-order closures fail.

The resulting program is deliberately modest in one sense and ambitious in another.  It does not seek an unrestricted pointwise reconstruction of every internal transport coefficient.  Instead it seeks measurements whose simplest models make **too many predictions**: predictions across color, spatial model order, RF frequency, and ordinary boundary/carrier alternatives.  The purpose is not to make transport fitting unnecessary.  It is to make the detector itself participate in deciding when a transport model has failed.

---

# References

1. W. Shockley, “Currents to Conductors Induced by a Moving Point Charge,” *Journal of Applied Physics* **9**, 635–636 (1938). DOI: `10.1063/1.1710367`.
2. S. Ramo, “Currents Induced by Electron Motion,” *Proceedings of the IRE* **27**, 584–585 (1939). DOI: `10.1109/JRPROC.1939.228757`.
3. W. Dabrowski, “Transport equations and Ramo's theorem: Applications to the impulse response of a semiconductor detector and to the generation-recombination noise in a semiconductor junction,” *Progress in Quantum Electronics* **13**, 233–266 (1989). DOI: `10.1016/0079-6727(89)90004-9`.
4. Z. Glasser, P. K. Dubey, A. Dutta, E. Liokumovitch, R. Abramov, and S. Sternklar, “Optoelectronic chromatic dispersion and wavelength monitoring in a photodiode,” *Optics Express* **29**, 19839–19852 (2021). DOI: `10.1364/OE.424157`.
5. Y. Sun, Z. Zhang, X. Xing, P. Hu, and J. Tan, “Complete model identification for measuring photodetector's data age in high-speed and high-precision interferometry,” *Optics Express* **33**, 15125–15140 (2025). DOI: `10.1364/OE.550721`.
6. M.-S. Sang, G.-Q. Xu, H. Qiao, and X.-Y. Li, “High speed uncooled MWIR infrared HgCdTe photodetector based on graded bandgap structure,” *Journal of Infrared and Millimeter Waves* **41**, 972–979 (2022). DOI: `10.11972/j.issn.1001-9014.2022.06.005`.
7. J. Rothman, G. Vojetta, B. Moselle, L. Mollard, S. Gout, and J.-P. Chamonal, “Shockley–Haynes Characterization of Minority-Carrier Drift Velocity, Diffusion Coefficient, and Lifetime in HgCdTe Avalanche Photodiodes,” *Journal of Electronic Materials* **39**, 837–845 (2010). DOI: `10.1007/s11664-010-1247-8`.
8. G. L. Hansen, J. L. Schmit, and T. N. Casselman, “Energy gap versus alloy composition and temperature in Hg1−xCdxTe,” *Journal of Applied Physics* **53**, 7099–7101 (1982). DOI: `10.1063/1.330018`.
9. K. Moazzami, J. Phillips, D. Lee, S. Krishnamurthy, G. Benoit, Y. Fink, and T. Tiwald, “Detailed Study of Above Bandgap Optical Absorption in HgCdTe,” *Journal of Electronic Materials* **34**, 773–778 (2005). DOI: `10.1007/s11664-005-0019-3`.
10. G.-Q. Xu et al., “Potential application of HgCdTe detector with composition gradient in laser measurement,” *Journal of Applied Optics* **45**(3), 549–556 (2024). DOI: `10.5768/JAO202445.0310009`. **Note for draft:** bibliographic existence is confirmed, but the full technical text has not yet been recovered for a complete priority audit.

---

## Draft integrity notes

- Do not replace “priority unresolved” with novelty language without a focused primary-source audit.
- The 2024 HgCdTe reference remains technically unresolved despite confirmed metadata.
- Do not use the superseded three-color boundary-confounded HgCdTe result.
- Do not apply first-passage timing cumulant identities directly to generic terminal current.
- Main-text numerical HgCdTe values should continue to be regression-tested against both the sparse BVP and independent shooting implementations before submission.
