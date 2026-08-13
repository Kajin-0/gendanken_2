# Research Log — Experiment 02: The Photodetector Boundary

Chronological reasoning log. This file records **why the direction changed**, including failed boundaries, counterexamples, and corrected definitions. Detailed algebra lives in the dedicated derivation files.

---

## 2026-08-12 — Experiment opened

Starting question:

> At what point does a simple collection of atoms become a photodetector? If light is absorbed and re-emitted versus absorbed and a charge pair is generated, when does that happen and what is the boundary?

Initial intuitive chain:

```text
few atoms / atomic absorption
-> many atoms / semiconductor bands
-> electron-hole generation
-> photodetector.
```

The project explicitly refused to assume this chain was correct.

---

## Re-emission versus electron-hole generation — terminology corrected

Interband absorption can create an electron-hole excitation that later recombines radiatively.

Therefore

```text
photon absorbed and re-emitted
```

and

```text
photon absorbed and electron-hole pair generated
```

are not generally mutually exclusive alternatives.

**Direction:** separate absorption physics from detector-record physics.

---

## Universal atom-count threshold attacked — failed

A single atom can in principle encode photon arrival through excitation, ionization, or another readable state change.

A macroscopic absorber can absorb and then leave no accessible material record.

**Conclusion:** there is no universal `N_c` without specifying interaction, readout, persistence, and noise.

**Direction:** replace atom count with hypothesis discrimination.

---

## Operational detector definition introduced

For photon/no-photon hypotheses, define accessible material states

```math
\rho_D^{(0)},\qquad\rho_D^{(1)}.
```

Use

```math
\mathcal D_D
=\frac12\|\rho_D^{(1)}-\rho_D^{(0)}\|_1.
```

For equal priors,

```math
P_{e,\min}
=\frac12(1-\mathcal D_D).
```

**Conclusion:** detection becomes a quantitative discrimination problem rather than a phase-of-matter label.

---

## Absorption as the detector boundary attacked — failed twice

### Perfect absorber, no accessible record

If

```math
P_{\rm abs}=1
```

but

```math
\rho_D^{(1)}=\rho_D^{(0)},
```

then the material does not discriminate the optical hypotheses.

### Nonabsorptive dispersive record

A surviving photon can correlate with a distinguishable matter pointer.

**Conclusion:** absorption is neither sufficient nor universally necessary.

---

## Atomic-to-band crossover separated

Increasing `N` can turn sparse molecular/atomic spectra into dense band-like spectra, but this is a condensed-matter crossover, not the detector definition.

**Direction:** locate electron-hole generation separately.

---

## Electron-hole generation separated from mobile/collected charge

An absorbed photon can create a bound or mobile excitation. A minimal competing-rate collection model is

```math
P_{\rm col}
=\frac{\Gamma_{\rm col}}
{\Gamma_{\rm col}+\Gamma_r+\Gamma_{nr}}.
```

**Conclusion:**

```text
absorption
!= pair generation
!= collection
!= readable event.
```

---

## Gain reinterpreted

Naive idea:

```text
1 photon -> 1 electron -> 10^6 electrons -> more information.
```

Corrected interpretation:

```text
microscopic photon-conditioned distinction
-> gain/transduction
-> larger separation of practical output distributions.
```

**Conclusion:** gain stabilizes/enlarges an existing distinction against later readout limitations; it does not create photon-arrival information that was absent upstream.

---

## Irreversibility moved from axiom to dynamical question

Closed photon + detector + environment evolution can remain unitary while a reduced detector develops a metastable pointer record.

**Conclusion:** operational irreversibility must be tied to subsystem choice, information dispersal, metastability, and accessibility.

**Direction:** explicitly require record persistence.

---

## Momentary encoding versus persistent record

A system can satisfy `D_D(t)>0` briefly and then lose the distinction before any permitted readout.

**Conclusion:** acquisition and retention are separate resources.

---

## Universal deposited-energy lower bound attacked — failed

A degenerate two-state pointer can be conditionally rotated into an orthogonal state while its final bare detector-energy difference is zero.

However finite-time pure-state separation still requires interaction action:

```math
\mathcal A_\Delta
\ge
\hbar\arcsin(1-2\epsilon).
```

Perfect discrimination requires

```math
\mathcal A_\Delta\ge\pi\hbar/2.
```

**Conclusion:** final deposited energy is not universal; finite interaction action survives in the stated pure/unitary model.

Detailed derivation: `INTERACTION_ACTION_LOWER_BOUND.md`.

---

## Constrained N recovered

If each constituent can supply at most interaction action `a_max`,

```math
N
\ge
\left\lceil
\frac{\hbar\arcsin(1-2\epsilon)}{a_{\max}}
\right\rceil.
```

**Conclusion:** `N_min` can exist after a microscopic resource cap is stated.

---

## Exact one-photon + N-dipole model

For identical resonant two-level dipoles,

```math
G=g\sqrt N.
```

The matter-only distinguishability is

```math
\mathcal D_D(t)=\sin^2(g\sqrt Nt).
```

Perfect transient first-lobe transfer requires

```math
N_{\min}
=\left\lceil(\pi/(2g\tau))^2\right\rceil.
```

**Conclusion:** a many-atom threshold can arise from collective optical coupling and finite time without band formation.

Detailed derivation: `N_DIPOLE_SINGLE_MODE_MODEL.md`.

---

## Coherent transfer as persistent detection attacked — failed

The matter excitation Rabi-oscillates back into the optical mode.

**Conclusion:** strong acquisition is not yet a persistent detector record.

**Direction:** add a long-lived record channel and competing loss.

---

## Initial-in-mode coherent capture -> record

With collective coupling `G`, optical loss `kappa`, unwanted matter loss `gamma`, and desired record trapping `Gamma`,

```math
P_R
=
\frac{4G^2\Gamma}
{(\kappa+\gamma+\Gamma)
[4G^2+\kappa(\gamma+\Gamma)]}.
```

The analytic result was checked against direct numerical integration at about `1e-11` absolute agreement in tested cases.

Detailed derivation: `COHERENT_CAPTURE_TO_RECORD.md`.

---

## More irreversibility is always better — attacked and failed

The exact record probability has finite optimum

```math
\Gamma_{\rm opt}
=
\sqrt{
\frac{(\kappa+\gamma)(4G^2+\kappa\gamma)}{\kappa}
}.
```

For `gamma=0`,

```math
\Gamma_{\rm opt}=2G.
```

Too little trapping fails to freeze the excitation; too much overdamps coherent acquisition while optical escape remains available.

**Conclusion:** record formation must be rate matched.

---

## Traveling-wave capture introduced

The photon was no longer placed inside the optical mode by assumption.

For an incident one-photon spectral component,

```math
\eta_R(\delta)
=
\frac{\kappa_{\rm in}\Gamma G^2}
{\left|
(\kappa/2-i\delta_c)
((\gamma+\Gamma)/2-i\delta_m)
+G^2
\right|^2}.
```

At resonance,

```math
\eta_R(0)
=
\frac{16\kappa_{\rm in}\Gamma G^2}
{[\kappa(\gamma+\Gamma)+4G^2]^2}.
```

**Conclusion:** external detection separates into optical matching and matter-to-record branching.

Detailed derivation: `TRAVELING_WAVE_CAPTURE.md`.

---

## Peak-efficiency atom threshold attacked — failed

In the clean one-port limit,

```math
\Gamma_{\rm match}=4G^2/\kappa
```

gives

```math
r(0)=0,
\qquad
\eta_R(0)=1.
```

This works for any nonzero `G` if arbitrarily slow/narrowband operation is allowed.

**Conclusion:** unit monochromatic efficiency does not impose a positive `N_min`.

**Hidden resource found:** bandwidth/time.

---

## Collective cooperativity and optical-access ceilings emerged

Optimized external efficiency is

```math
\eta_{R,\max}
=\eta_{\rm esc}\frac{C_N}{1+C_N},
```

where

```math
\eta_{\rm esc}=\kappa_{\rm in}/\kappa,
\qquad
C_N=4G^2/(\kappa\gamma).
```

**Conclusion:** optical access/parasitic loss and coherent coupling/matter loss are independent ceilings. More atoms cannot repair an inaccessible optical port.

---

## Bandwidth restored a finite N threshold

In the clean critically matched bad-cavity benchmark,

```math
P_R=\frac{\Gamma}{\Gamma+B},
\qquad
\Gamma=4Ng^2/\kappa.
```

Hence

```math
N
\ge
\frac{\kappa B}{8g^2}
\frac{1-2\epsilon}{\epsilon}.
```

**Conclusion:** weak coupling can preserve peak efficiency only by narrowing useful spectral/temporal acceptance.

---

## Literal total atom count attacked — failed

For unequal microscopic couplings,

```math
G^2=\sum_j|g_j|^2.
```

Only one bright superposition couples directly to the ideal optical mode.

Atoms outside the optical field, at nodes, or poorly aligned contribute little.

**Conclusion:** the microscopic resource is mode-weighted oscillator strength, not literal total atom count.

Detailed derivation: `MODE_WEIGHTED_OPTICAL_DEPTH.md`.

---

## Continuum limit -> optical depth

For a dilute single-pass absorber,

```math
\mathrm{OD}=n\sigma L
=\frac{N_{\rm col}\sigma}{A},
```

and

```math
P_{\rm abs}=1-e^{-\mathrm{OD}}.
```

In the ideal high-efficiency single-pass limit,

```math
\mathrm{OD}_{\min}=-\ln(2\epsilon).
```

**Conclusion:** in extended matter, column density / optical depth is more physically meaningful than total atom count.

The contrast with resonant critical coupling showed explicitly that architecture changes the apparent matter requirement by trading absorber strength against optical dwell time/bandwidth.

---

## Returned to semiconductor electron-hole physics

For a minimal slab,

```math
\eta_s
=\eta_{\rm mode}
(1-e^{-\alpha L})
\eta_{eh}
P_{\rm col}
P_{\rm read}.
```

with

```math
P_{\rm col}
=\frac{\Gamma_{\rm ext}}
{\Gamma_{\rm ext}+\Gamma_{\rm rec}}.
```

**Conclusion:** electron-hole generation is the semiconductor-specific transduction stage. It becomes useful detection only after survival/separation, record formation, and readout.

Detailed derivation: `SEMICONDUCTOR_DECISION_BRIDGE.md`.

---

## Dark-event decision boundary derived

For independent Poisson dark clicks of rate `R_d` over decision window `tau`,

```math
\mathcal D_{\rm click}
=\eta_s e^{-R_d\tau}.
```

and

```math
P_e
=\frac12(1-\eta_s e^{-R_d\tau}).
```

A necessary target condition is

```math
R_d\tau
\le
-\ln(1-2\epsilon).
```

For small `epsilon`, `R_d tau` must be approximately `<=2 epsilon`.

**Conclusion:** no amount of atom number, absorptance, or gain can overcome a dark-event budget that already destroys the needed evidential contrast.

---

## Continuous Gaussian electrical readout introduced

Binary click output was replaced by

```math
H_0:y(t)=n(t),
\qquad
H_1:y(t)=s(t)+n(t),
```

with common Gaussian covariance.

The exact decision coordinate is the noise-whitened waveform distance

```math
\boxed{
d^2
=\langle s,C^{-1}s\rangle
=\int_{-\infty}^{\infty}
\frac{|\tilde s(f)|^2}
{S_n^{(2)}(f)}df.
}
```

Equal-prior optimum error is

```math
\boxed{P_e=Q(d/2).}
```

**Conclusion:** at the electrical-output level, detector quality for a task is the separation of the complete photon/no-photon waveform distributions in the inverse-noise metric.

Detailed derivation: `CONTINUOUS_GAUSSIAN_DECISION.md`.

---

## NEP and D* reinterpreted as projections

If

```math
\tilde s(f)=\mathcal R(f)\tilde p(f),
```

then

```math
\boxed{
d^2
=\int
\frac{|\tilde p(f)|^2}
{\mathrm{NEP}_2^2(f)}df.
}
```

A full frequency-dependent input-referred noise model can therefore determine the decision distance.

A scalar `D*` quoted at one frequency generally cannot.

**Conclusion:** conventional figures of merit are descriptors feeding the decision problem; they are not the universal detector boundary.

---

## Same D* -> same event performance attacked — failed

For a one-pole detector

```math
h(t)=\frac1\tau e^{-t/\tau}u(t)
```

with a short optical pulse of energy `E` and white one-sided output noise,

```math
\boxed{
d^2
=\frac{E^2}{\tau\,\mathrm{NEP}^2}.
}
```

Using

```math
\mathrm{NEP}=\sqrt A/D^*,
```

```math
\boxed{
d^2
=\frac{E^2D^{*2}}{A\tau}.
}
```

Thus at equal area and equal low-frequency white-noise `D*`,

```math
d\propto\tau^{-1/2}.
```

**Conclusion:** two detectors with identical conventional `D*` can have different optimum discrimination error for a short fixed-energy event solely because their temporal responses differ.

This directly validates the intuition that a scalar detectivity omits task-relevant time structure.

---

## Finite decision deadline sharpens the difference

If the output is observed only for `0<t<T`,

```math
\boxed{
d^2(T)
=\frac{E^2}{\tau\,\mathrm{NEP}^2}
(1-e^{-2T/\tau}).
}
```

For `T<<tau`,

```math
d^2(T)
\simeq
\frac{2E^2T}{\tau^2\mathrm{NEP}^2}.
```

**Conclusion:** a slow detector pays an even stronger penalty under a short decision deadline.

---

## Current strongest organizing picture

The path is now

```text
material constitution
-> optical access / mode overlap
-> mode-weighted coupling or optical depth
-> microscopic excitation / electron-hole generation
-> acquisition/extraction versus loss/recombination
-> persistent record
-> electrical transfer function + noise spectrum
-> noise-weighted photon/no-photon waveform distance
-> decision error
-> reset/reuse.
```

Every attempted universal scalar boundary has so far exposed a missing resource coordinate:

```text
N                  -> per-constituent coupling/time
peak efficiency    -> bandwidth
more atoms         -> mode overlap / optical escape
more absorber      -> downstream collection / dark events
D*                 -> temporal/spectral task structure.
```

The strongest answer to the starting question is therefore:

> **A collection of atoms becomes useful as a photodetector only relative to a specified measurement task. The physically relevant boundary is a performance surface of the complete optical–matter–record–noise dynamics, not a universal atom count or one scalar figure of merit.**

---

## Current frontier

Next attacks:

```text
signal-dependent noise
-> covariance differs under photon/no-photon hypotheses
-> shot / generation-recombination / gain noise

unknown arrival time / timing jitter
-> search over temporal mode / trials penalty

then
-> test whether a task-specific scalar detectivity can be defined
   from optimum decision distance.
```

A focused primary-source prior-art audit remains mandatory before novelty language.
