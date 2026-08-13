# Current Live State — Experiment 02

**Date:** 2026-08-12  
**Status:** exploratory first-principles theory; microscopic-to-electrical decision chain now derived in minimal models  
**Priority:** unassessed; no novelty claim

This is the current state pointer. `RESEARCH_LOG.md` preserves chronology; `CLAIM_LEDGER.md` is the epistemic boundary.

Detailed active derivations:

1. `INTERACTION_ACTION_LOWER_BOUND.md`
2. `N_DIPOLE_SINGLE_MODE_MODEL.md`
3. `COHERENT_CAPTURE_TO_RECORD.md`
4. `TRAVELING_WAVE_CAPTURE.md`
5. `MODE_WEIGHTED_OPTICAL_DEPTH.md`
6. `SEMICONDUCTOR_DECISION_BRIDGE.md`
7. `CONTINUOUS_GAUSSIAN_DECISION.md`

---

## 1. Starting question and current answer

Starting question:

> At what point does a simple collection of atoms become a photodetector?

Current answer:

> **There is no universal atom-count transition. A collection of matter functions as a detector only relative to a specified optical mode/task, interaction time or bandwidth, competing loss, record mechanism, dark/noise statistics, observation interval, and required decision error. Under explicit constraints, minimum effective atom numbers, optical depths, or rate ratios emerge.**

The project now separates

```text
atomic/band crossover
optical access and mode overlap
microscopic photon-matter coupling
excitation / electron-hole generation
competition with loss/recombination
persistent record formation
decision against dark/readout noise
reset/reuse.
```

---

## 2. Operational spine

For accessible detector states conditioned on no photon and one photon,

```math
\rho_D^{(0)},\qquad\rho_D^{(1)},
```

define

```math
\boxed{
\mathcal D_D
=\frac12\|\rho_D^{(1)}-\rho_D^{(0)}\|_1.
}
```

For equal priors,

```math
\boxed{
P_{e,\min}
=\frac12(1-\mathcal D_D).
}
```

This immediately kills absorption as the universal definition:

```text
perfect absorption can coexist with no accessible record;
nonabsorptive/dispersive interaction can produce a record.
```

Electron-hole creation, atom count, gain, and decoherence are likewise not complete detector definitions by themselves.

---

## 3. Resource attack — final deposited energy fails

A degenerate two-state pointer can be conditionally rotated into an orthogonal state with zero final bare detector-energy change.

Thus target discrimination alone does not imply a universal positive final deposited/dissipated energy.

For a pure conditional-unitary detector, finite-time state separation instead obeys the conditional interaction-action bound

```math
\boxed{
\mathcal A_\Delta
\ge
\hbar\arcsin(1-2\epsilon).
}
```

Perfect discrimination requires

```math
\boxed{
\mathcal A_\Delta\ge\pi\hbar/2.
}
```

The underlying quantum-speed-limit geometry is established; no novelty claim is attached.

If each constituent can supply at most action `a_max`, then

```math
N
\ge
\left\lceil
\frac{\hbar\arcsin(1-2\epsilon)}{a_{\max}}
\right\rceil.
```

This is the first recovery of a constrained `N_min`.

---

## 4. Explicit N-dipole acquisition model

For identical resonant dipoles in one mode,

```math
\boxed{G=g\sqrt N.}
```

The matter-only distinguishability is

```math
\boxed{
\mathcal D_D(t)=\sin^2(g\sqrt Nt).
}
```

Perfect transient transfer requires

```math
\boxed{
N_{\min}
=
\left\lceil
\left(\frac{\pi}{2g\tau}\right)^2
\right\rceil.
}
```

This is standard collective-coupling physics used to show that a many-atom threshold can emerge from finite coupling/time without band formation.

But the excitation Rabi-oscillates back, so coherent transfer is still not a persistent detector record.

---

## 5. Record formation is rate matched

Adding optical loss `kappa`, unwanted matter loss `gamma`, and desired record trapping `Gamma` gives, for a photon initially inside the optical mode,

```math
\boxed{
P_R
=
\frac{4G^2\Gamma}
{(\kappa+\gamma+\Gamma)
[4G^2+\kappa(\gamma+\Gamma)]}.
}
```

The trapping optimum is finite:

```math
\boxed{
\Gamma_{\rm opt}
=
\sqrt{
\frac{(\kappa+\gamma)(4G^2+\kappa\gamma)}{\kappa}
}.
}
```

For `gamma=0`,

```math
\Gamma_{\rm opt}=2G.
```

Thus

```text
more irreversible trapping != monotonically better detection.
```

---

## 6. Traveling-wave capture changes the conclusion again

For an actual incident photon with desired optical coupling `kappa_in`, parasitic optical loss, collective matter coupling `G`, matter loss `gamma`, and record rate `Gamma`, the resonant narrowband record efficiency is

```math
\boxed{
\eta_R(0)
=
\frac{16\kappa_{\rm in}\Gamma G^2}
{[\kappa(\gamma+\Gamma)+4G^2]^2}.
}
```

Equivalently,

```math
\eta_R(0)
=
\beta_R
\frac{4\kappa_{\rm in}\kappa_m}
{(\kappa+\kappa_m)^2},
```

with

```math
\kappa_m=4G^2/(\gamma+\Gamma),
\qquad
\beta_R=\Gamma/(\gamma+\Gamma).
```

This exposes optical critical coupling directly.

---

## 7. Major counterexample — perfect peak efficiency can occur for arbitrarily weak nonzero coupling

In the clean one-port limit,

```text
kappa_loss=0,
gamma=0,
```

critical matching is

```math
\boxed{
\Gamma_{\rm match}=4G^2/\kappa.
}
```

At resonance,

```math
r=0,
\qquad
\eta_R=1.
```

This can occur for any nonzero `G` if slow/narrowband operation is allowed.

Therefore

> **peak monochromatic efficiency alone does not imply a positive atom-count threshold. Weak coupling is paid for in bandwidth/time.**

---

## 8. External efficiency separates into optical escape and collective cooperativity

Optimizing external capture gives

```math
\boxed{
\Gamma_{\rm opt}
=\gamma+\frac{4G^2}{\kappa}
}
```

and

```math
\boxed{
\eta_{R,\max}
=\eta_{\rm esc}\frac{C_N}{1+C_N},
}
```

where

```math
\eta_{\rm esc}=\kappa_{\rm in}/\kappa,
```

and

```math
\boxed{
C_N=\frac{4G^2}{\kappa\gamma}.
}
```

Thus

```text
optical-access / parasitic-loss ceiling
and
collective-coupling / matter-loss ceiling
```

are independent. Increasing `N` cannot repair inaccessible optical escape.

Finite incident bandwidth restores an `N_min`; in the clean matched bad-cavity Lorentzian benchmark,

```math
P_R=\frac{\Gamma}{\Gamma+B},
\qquad
\Gamma=4Ng^2/\kappa,
```

so

```math
\boxed{
N
\ge
\frac{\kappa B}{8g^2}
\frac{1-2\epsilon}{\epsilon}.
}
```

---

## 9. Literal atom count is replaced by mode-weighted coupling

For unequal microscopic couplings,

```math
\boxed{
G^2=\sum_j|g_j|^2.
}
```

Only one bright superposition couples directly to the ideal optical mode.

Atoms outside the mode, at nodes, or poorly aligned with the field contribute little.

Therefore the natural microscopic quantity is **mode-weighted oscillator strength**, not total physical atom count.

In a dilute traveling-wave continuum this becomes optical depth,

```math
\boxed{
\mathrm{OD}=n\sigma L
=\frac{N_{\rm col}\sigma}{A},
}
```

with

```math
P_{\rm abs}=1-e^{-\mathrm{OD}}.
```

For an ideal single-pass high-efficiency target,

```math
\boxed{
\mathrm{OD}_{\min}=-\ln(2\epsilon).
}
```

---

## 10. Semiconductor bridge — electron-hole generation located precisely

For a minimal semiconductor slab,

```math
\boxed{
\eta_s
=\eta_{\rm mode}
(1-e^{-\alpha L})
\eta_{eh}
P_{\rm col}
P_{\rm read}.
}
```

With an independent extraction/recombination race,

```math
\boxed{
P_{\rm col}
=\frac{\Gamma_{\rm ext}}
{\Gamma_{\rm ext}+\Gamma_{\rm rec}}.
}
```

Therefore electron-hole generation is the semiconductor-specific **microscopic transduction/encoding stage**, not the complete detector boundary.

The excitation must still survive, separate/collect, become an accessible record, and remain distinguishable from dark output.

---

## 11. Binary dark-event decision boundary

For independent Poisson dark clicks of rate `R_d` over decision window `tau`, the exact binary click/no-click distinguishability is

```math
\boxed{
\mathcal D_{\rm click}
=\eta_s e^{-R_d\tau}.
}
```

Hence

```math
\boxed{
P_e
=\frac12(1-\eta_s e^{-R_d\tau}).
}
```

A necessary condition for target `P_e<=epsilon` is

```math
\boxed{
R_d\tau
\le
-\ln(1-2\epsilon).
}
```

For small `epsilon`, `R_d tau` must be approximately `<=2 epsilon`.

No amount of absorber thickness, atom number, or gain can repair a dark-event budget that already violates this condition.

---

## 12. Continuous Gaussian electrical readout — current strongest bridge to engineering metrics

Replace binary clicks with

```math
H_0:y(t)=n(t),
\qquad
H_1:y(t)=s(t)+n(t),
```

where `n(t)` is zero-mean Gaussian noise with the same covariance under both hypotheses.

The complete decision coordinate is the Mahalanobis / matched-filter distance

```math
\boxed{
d^2
=\langle s,C^{-1}s\rangle.
}
```

For stationary noise with two-sided PSD `S_n^{(2)}(f)`,

```math
\boxed{
d^2
=\int_{-\infty}^{\infty}
\frac{|\tilde s(f)|^2}
{S_n^{(2)}(f)}df.
}
```

Equal-prior optimum error is

```math
\boxed{
P_e
=Q(d/2).
}
```

Thus the practical detector boundary for Gaussian readout is the **noise-weighted distance between the entire photon and no-photon waveforms**.

---

## 13. NEP and D* are projections of the decision distance

If

```math
\tilde s(f)=\mathcal R(f)\tilde p(f),
```

then define input-referred two-sided optical noise

```math
S_P^{(2)}(f)
=\frac{S_n^{(2)}(f)}{|\mathcal R(f)|^2}.
```

The decision distance becomes

```math
\boxed{
d^2
=\int_{-\infty}^{\infty}
\frac{|\tilde p(f)|^2}
{S_P^{(2)}(f)}df
=\int
\frac{|\tilde p(f)|^2}
{\mathrm{NEP}_2^2(f)}df.
}
```

A full frequency-dependent NEP or `D*(f)` can in principle feed this integral.

A single quoted `D*` at one frequency generally cannot.

---

## 14. Equal D* fast-versus-slow counterexample

For a one-pole detector

```math
h(t)=\frac1\tau e^{-t/\tau}u(t)
```

with DC responsivity `R_0`, a short optical pulse of energy `E`, and flat one-sided output-noise PSD `S_n^{(1)}` gives

```math
\boxed{
d^2
=\frac{(R_0E)^2}{\tau S_n^{(1)}}
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

Therefore, at equal area and equal low-frequency white-noise `D*`,

```math
\boxed{d\propto\tau^{-1/2}.}
```

A faster detector discriminates a short fixed-energy optical event better in this model even though conventional `D*` is identical.

This is a precise decision-theoretic counterexample to

```text
same D* -> same event-detection performance.
```

The result is conditional on the stated one-pole, white-noise, matched-filter assumptions.

---

## 15. Finite decision time strengthens the temporal penalty

For observation only over `0<t<T`,

```math
\boxed{
d^2(T)
=\frac{E^2}{\tau\,\mathrm{NEP}^2}
\left(1-e^{-2T/\tau}\right).
}
```

For `T<<tau`,

```math
d^2(T)
\simeq
\frac{2E^2T}{\tau^2\mathrm{NEP}^2}.
```

A slow detector therefore pays an especially severe penalty under a strict decision deadline.

---

## 16. Strongest organizing result so far

The detector boundary has evolved from

```text
How many atoms?
```

into

```text
For a specified optical task and observation window,
how far apart are the photon/no-photon accessible output distributions
in the physically relevant noise metric?
```

The chain is now

```text
material constitution
-> optical access / mode overlap
-> mode-weighted coupling or optical depth
-> microscopic excitation / electron-hole generation
-> acquisition/extraction versus loss/recombination
-> persistent record
-> electrical signal transfer R(f)
   and noise PSD S_n(f)
-> noise-weighted waveform distance d
-> decision error.
```

This suggests there may be **no architecture-independent scalar detector quality** unless the class of optical tasks is specified first.

Conventional metrics are task-independent summaries of parts of this chain, not the fundamental boundary themselves.

---

## 17. Current frontier

The next strongest attacks are:

```text
signal-dependent noise
-> shot / generation-recombination / gain noise
-> covariance differs under H0 and H1

unknown photon arrival time
-> timing search / jitter / trials penalty

then
-> ask whether a task-specific scalar detectivity can be defined
   from optimum decision distance.
```

Separately, a focused primary-source audit of the established components and nearest detector-specific formulations is required before novelty language.

---

## 18. Mandatory caveats

- Trace distance / Helstrom discrimination are established.
- Quantum-speed-limit geometry is established.
- Dicke/Tavis--Cummings collective coupling is established.
- Cooperativity, input-output critical coupling, Beer-Lambert optical depth, Gaussian detection theory, and matched filtering are established structures.
- The detector-boundary synthesis and conditional cross-stage laws have not yet undergone a focused prior-art audit.
- Current models omit realistic complications including dephasing/disorder, multimode continua, full semiconductor bandstructure, signal-dependent noise, gain statistics, timing jitter, nonstationary drift, saturation, and reset.
- Experiment 01 remains separate and untouched.
