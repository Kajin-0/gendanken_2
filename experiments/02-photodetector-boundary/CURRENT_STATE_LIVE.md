# Current Live State — Experiment 02

**Date:** 2026-08-12  
**Status:** exploratory first-principles theory; external capture, mode-weighted coupling, and semiconductor decision bridge now derived  
**Priority:** unassessed; no novelty claim

This is the current state pointer for Experiment 02. `RESEARCH_LOG.md` preserves chronology; `CLAIM_LEDGER.md` is the epistemic boundary.

Detailed active derivations:

1. `INTERACTION_ACTION_LOWER_BOUND.md`
2. `N_DIPOLE_SINGLE_MODE_MODEL.md`
3. `COHERENT_CAPTURE_TO_RECORD.md`
4. `TRAVELING_WAVE_CAPTURE.md`
5. `MODE_WEIGHTED_OPTICAL_DEPTH.md`
6. `SEMICONDUCTOR_DECISION_BRIDGE.md`

---

## 1. Starting question and current answer

Starting question:

> At what point does a simple collection of atoms become a photodetector?

Current answer:

> **There is no universal atom-count transition. A collection of matter enters a useful detector regime only relative to a specified optical mode, interaction time/bandwidth, loss environment, record mechanism, dark-event budget, and decision target. Under explicit constraints, minimum effective atom numbers or optical depths emerge.**

Three different roles of `N` remain separated:

```text
SPECTRAL CROSSOVER
N large -> dense spectrum / band-like description

ACQUISITION CROSSOVER
more mode-coupled oscillator strength -> stronger optical-matter coupling

RECORD / DECISION CROSSOVER
loss, trapping, dark events, bandwidth, and readout determine whether the acquired distinction survives.
```

These are not the same boundary.

---

## 2. Operational spine — photon/no-photon distinguishability

For an explicitly chosen accessible detector subsystem `D`, compare

```math
\rho_D^{(0)},\qquad \rho_D^{(1)}.
```

Define

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

Consequences already established:

```text
perfect absorption can coexist with D_D=0;
nonabsorptive/dispersive interaction can produce D_D>0;
therefore absorption is neither sufficient nor universally necessary.
```

Electron-hole creation, gain, atom count, and decoherence are likewise not complete detector definitions by themselves.

---

## 3. First lower-bound attack — final deposited energy fails

A degenerate two-state pointer can be conditionally rotated into an orthogonal state while its final bare detector-energy change remains zero.

Therefore target discrimination alone does **not** imply a universal positive final energy separation or dissipated/deposited energy per event.

For a pure conditional-unitary branch model, established state-space geometry gives

```math
\boxed{
\mathcal A_\Delta
\equiv
\int_0^\tau \Delta V_I(t)dt
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

The degenerate qubit pointer saturates the perfect-discrimination value.

Interpretation:

```text
final detector energy difference -> not universal
finite interaction action        -> required in this finite-time pure/unitary model.
```

No novelty claim is attached to the quantum-speed-limit mathematics.

---

## 4. General constrained atom-count recovery

If the interaction decomposes into local terms and each constituent supplies at most action `a_max`, then

```math
\boxed{
N
\ge
\left\lceil
\frac{\hbar\arcsin(1-2\epsilon)}{a_{\max}}
\right\rceil.
}
```

Thus a minimum `N` is **derived after the per-constituent resource is bounded**; it is not a universal material phase boundary.

---

## 5. Exact one-photon + N-dipole model

For `N` identical resonant two-level dipoles in one quantized optical mode,

```math
H_I
=\hbar g\sum_j
(a\sigma_j^+ + a^\dagger\sigma_j^-).
```

The photon couples only to the symmetric bright state with

```math
\boxed{G=g\sqrt N.}
```

Starting from one photon and all dipoles in the ground state,

```math
\boxed{
\mathcal D_D(t)
=\sin^2(g\sqrt Nt).
}
```

Hence on the first transfer lobe,

```math
\boxed{
N_{\min}
=
\left\lceil
\frac{[\arcsin\sqrt{1-2\epsilon}]^2}
{g^2\tau^2}
\right\rceil.
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

Thus this closed coherent architecture gives

```math
N_{\min}\propto(g\tau)^{-2}.
```

The `sqrt(N)` enhancement is established Dicke/Tavis--Cummings physics.

---

## 6. Coherent excitation is not yet a persistent detector record

In the lossless one-mode model the excitation Rabi-oscillates back into the optical mode.

Therefore

```text
strong photon -> matter transfer
!=
persistent detector record.
```

This forced the addition of a long-lived record channel.

---

## 7. Initial-in-mode coherent-capture -> record result

For

```text
G      = g sqrt(N) coherent photon <-> matter coupling
kappa  = optical-mode population loss
gamma  = unwanted matter loss
Gamma  = desired matter -> record trapping rate,
```

with the photon initially inside the optical mode,

```math
\boxed{
P_R
=
\frac{4G^2\Gamma}
{(\kappa+\gamma+\Gamma)
[4G^2+\kappa(\gamma+\Gamma)]}.
}
```

The analytic expression was checked against direct numerical integration at approximately `1e-11` absolute agreement for tested parameter sets.

Maximizing over `Gamma` gives

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
\boxed{\Gamma_{\rm opt}=2G.}
```

Thus

```text
more irreversible trapping != monotonically better detection.
```

Too little trapping fails to freeze the excitation; too much overdamps acquisition while optical escape remains available.

---

## 8. Traveling-wave external capture — exact narrowband kernel

The latest model no longer assumes the photon begins in the optical mode.

Use

```text
kappa_in   = desired input/output port coupling
kappa_loss = parasitic optical loss
kappa      = kappa_in + kappa_loss
G          = collective matter coupling
gamma      = unwanted matter loss
Gamma      = desired record trapping
q          = gamma + Gamma.
```

The frequency-resolved record-conversion kernel for a traveling one-photon spectral component is

```math
\boxed{
\eta_R(\delta)
=
\frac{\kappa_{\rm in}\Gamma G^2}
{\left|
\left(\frac{\kappa}{2}-i\delta_c\right)
\left(\frac{q}{2}-i\delta_m\right)
+G^2
\right|^2}.
}
```

At exact resonance,

```math
\boxed{
\eta_R(0)
=
\frac{16\kappa_{\rm in}\Gamma G^2}
{[\kappa(\gamma+\Gamma)+4G^2]^2}.
}
```

Define

```math
\kappa_m
=\frac{4G^2}{\gamma+\Gamma},
\qquad
\beta_R
=\frac{\Gamma}{\gamma+\Gamma}.
```

Then

```math
\boxed{
\eta_R(0)
=
\beta_R
\frac{4\kappa_{\rm in}\kappa_m}
{(\kappa+\kappa_m)^2}.
}
```

This cleanly separates optical matching from matter-to-record branching.

---

## 9. Major correction — unit peak efficiency does not require large N

In the ideal one-port limit

```text
kappa_loss = 0,
gamma      = 0,
```

critical matching is

```math
\boxed{
\Gamma_{\rm match}
=\frac{4G^2}{\kappa}
=\frac{4Ng^2}{\kappa}.
}
```

At this point

```math
r(0)=0,
\qquad
\eta_R(0)=1.
```

Therefore **any nonzero `G` can reach unit monochromatic resonant conversion in this ideal one-port model if the record rate is correspondingly slowed.**

This kills a new shortcut:

```text
high peak efficiency -> minimum N.
```

What weak coupling costs is bandwidth/time, not necessarily peak efficiency.

---

## 10. External-capture optimum and collective cooperativity

For fixed `G`, `kappa`, and `gamma`, external narrowband conversion is optimized at

```math
\boxed{
\Gamma_{\rm opt}
=\gamma+\frac{4G^2}{\kappa}.
}
```

The resulting maximum is

```math
\boxed{
\eta_{R,\max}(0)
=
\frac{\kappa_{\rm in}}{\kappa}
\frac{4G^2}{4G^2+\kappa\gamma}.
}
```

Define

```math
\eta_{\rm esc}
=\frac{\kappa_{\rm in}}{\kappa},
```

and

```math
\boxed{
C_N
=\frac{4G^2}{\kappa\gamma}.
}
```

Then

```math
\boxed{
\eta_{R,\max}(0)
=\eta_{\rm esc}\frac{C_N}{1+C_N}.
}
```

The cooperativity structure is established cavity-QED physics.

Two independent ceilings appear:

```text
eta_esc                 -> optical-access / parasitic-loss ceiling
C_N/(1+C_N)             -> coherent-coupling versus matter-loss ceiling.
```

No increase in atom number can repair an optical-access ceiling without changing the architecture.

---

## 11. Cooperativity-based constrained atom-count law

For required record probability

```math
\eta_{\rm req}=1-2\epsilon,
```

finite cooperativity requires

```math
\eta_{\rm req}<\eta_{\rm esc}.
```

Then

```math
\boxed{
C_N
\ge
\frac{\eta_{\rm req}}
{\eta_{\rm esc}-\eta_{\rm req}}
}
```

and therefore

```math
\boxed{
N
\ge
\frac{\kappa\gamma}{4g^2}
\frac{\eta_{\rm req}}
{\eta_{\rm esc}-\eta_{\rm req}}.
}
```

For an ideal one-port optical interface,

```math
\boxed{
N
\ge
\frac{\kappa\gamma}{4g^2}
\frac{1-2\epsilon}{2\epsilon}.
}
```

This is a loss-limited atom-count law, not a universal detector threshold.

---

## 12. Finite bandwidth restores a threshold even when intrinsic loss vanishes

In the clean one-port critical-coupling limit and bad-cavity regime,

```math
\eta_R(\delta)
\simeq
\frac{\Gamma^2}{\delta^2+\Gamma^2},
\qquad
\Gamma=\frac{4Ng^2}{\kappa}.
```

For a Lorentzian one-photon spectrum with HWHM `B`,

```math
\boxed{
P_R
=\frac{\Gamma}{\Gamma+B}.
}
```

Demanding `P_R >= 1-2 epsilon` gives

```math
\boxed{
N
\ge
\frac{\kappa B}{8g^2}
\frac{1-2\epsilon}{\epsilon}.
}
```

For small `epsilon`,

```math
N_{\min}
\sim
\frac{\kappa B}{8g^2\epsilon}.
```

Thus weak coupling can preserve unit peak efficiency only by sacrificing bandwidth.

---

## 13. Total atom count is replaced by mode-weighted coupling

For nonuniform microscopic couplings,

```math
H_I
=\hbar\sum_j
(g_j a\sigma_j^+ + g_j^*a^\dagger\sigma_j^-).
```

The bright-state coupling is

```math
\boxed{
G^2
=\sum_j|g_j|^2.
}
```

Only the bright superposition

```math
|B\rangle
\propto
\sum_jg_j|e_j\rangle
```

couples directly to the ideal optical mode.

Therefore atoms outside the mode, at nodes, or with poor dipole alignment do not count equally.

A useful effective atom number is

```math
N_{\rm eff}
=\frac{1}{|g_{\rm ref}|^2}
\sum_j|g_j|^2.
```

The more invariant microscopic resource is mode-weighted oscillator strength, not literal `N`.

---

## 14. Traveling-wave continuum limit — optical depth

For a dilute single-pass absorber,

```math
\boxed{
\mathrm{OD}=n\sigma L
=\frac{N_{\rm col}\sigma}{A}.
}
```

Beer-Lambert absorption gives

```math
\boxed{
P_{\rm abs}=1-e^{-\mathrm{OD}}.
}
```

With mode/interface factor `eta_mode` and conditional record probability `eta_rec`,

```math
P_R
=\eta_{\rm mode}\eta_{\rm rec}
(1-e^{-\mathrm{OD}}).
```

Therefore

```math
\boxed{
\mathrm{OD}_{\min}
=-\ln\left[
1-
\frac{\eta_{\rm req}}
{\eta_{\rm mode}\eta_{\rm rec}}
\right]
}
```

when the requested efficiency is below the non-absorption ceiling.

In the ideal high-efficiency single-pass limit,

```math
\boxed{
\mathrm{OD}_{\min}
=-\ln(2\epsilon).
}
```

This contrasts with resonant critical coupling: a weak absorber can reach unity **narrowband** capture by repeated coherent interaction, whereas a single-pass absorber must increase optical depth.

---

## 15. Semiconductor bridge — where electron-hole generation actually sits

For a simple semiconductor slab, factor the signal-record probability as

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

Here

```text
alpha L   = optical depth of the active semiconductor
eta_eh    = probability an absorbed photon creates the relevant useful excitation
P_col     = probability that excitation is separated/collected
P_read    = probability collected charge becomes the chosen accessible record.
```

In the minimal competing-hazard model,

```math
\boxed{
P_{\rm col}
=\frac{\Gamma_{\rm ext}}
{\Gamma_{\rm ext}+\Gamma_{\rm rec}}
=\frac{1}{1+\tau_{\rm ext}/\tau_{\rm rec}}.
}
```

Thus electron-hole generation is a **transduction / microscopic encoding stage**, not by itself the detector boundary.

---

## 16. Dark events complete the minimal decision model

Let dark clicks be an independent Poisson process with rate `R_d` over decision window `tau`.

Under no photon,

```math
p_0=1-e^{-R_d\tau}.
```

Under one photon,

```math
p_1
=1-(1-\eta_s)e^{-R_d\tau}.
```

For the binary click/no-click output, the exact total-variation distinguishability is

```math
\boxed{
\mathcal D_{\rm click}
=\eta_s e^{-R_d\tau}.
}
```

Hence equal-prior error is

```math
\boxed{
P_e
=\frac12
\left(1-\eta_s e^{-R_d\tau}\right).
}
```

Combining the semiconductor stages,

```math
\boxed{
\mathcal D_{\rm click}
=
\eta_{\rm mode}
(1-e^{-\alpha L})
\eta_{eh}
\frac{\Gamma_{\rm ext}}
{\Gamma_{\rm ext}+\Gamma_{\rm rec}}
P_{\rm read}
\,e^{-R_d\tau}.
}
```

This is **CONDITIONAL** on the independent-stage, binary-click model, but it gives a direct bridge from microscopic semiconductor physics to the original hypothesis-discrimination definition.

---

## 17. Dark-event impossibility boundary

Target

```math
P_e\le\epsilon
```

requires

```math
\eta_s e^{-R_d\tau}
\ge1-2\epsilon.
```

Since `eta_s<=1`, a necessary condition is

```math
\boxed{
R_d\tau
\le
-\ln(1-2\epsilon).
}
```

For small `epsilon`,

```math
\boxed{
R_d\tau\lesssim2\epsilon.
}
```

No amount of absorber thickness, atom number, gain, or carrier collection can overcome a dark-event budget that already violates this decision condition.

This is structurally analogous to the optical escape ceiling in the external-capture model.

---

## 18. Current strongest organizing picture

The detector boundary now looks like

```text
OPTICAL ACCESS
mode overlap / port topology
        |
        v
OPTICAL INTERACTION RESOURCE
G^2 = sum |g_j|^2
or optical depth alpha L
        |
        v
MICROSCOPIC TRANSDUCTION
electron-hole / other excitation
        |
        v
DYNAMICAL COMPETITION
acquisition or extraction versus optical/matter/recombination loss
        |
        v
RATE-MATCHED PERSISTENT RECORD
        |
        v
DECISION AGAINST DARK/READOUT NOISE
        |
        v
RESET / REUSE
```

Natural coordinates now include

```math
\eta_{\rm esc}=\kappa_{\rm in}/\kappa,
\qquad
C_N=4G^2/(\kappa\gamma),
\qquad
\Gamma/(4G^2/\kappa),
\qquad
B/(4G^2/\kappa),
```

and in a continuum semiconductor,

```math
\alpha L,
\qquad
\Gamma_{\rm ext}/\Gamma_{\rm rec},
\qquad
R_d\tau.
```

The strongest conceptual answer to the original question is now:

> **A photodetector is not reached at a universal atom number. Detection is a performance region of the complete optical–matter–record–decision dynamics. Atom count appears only through mode-weighted coupling, optical depth, or other constrained resources.**

---

## 19. Current frontier

The next strongest attack is to replace the binary click record with a continuous noisy electrical output:

```text
photon/no-photon hypotheses
-> current or voltage waveform
-> Gaussian / colored noise
-> optimum likelihood-ratio or matched-filter discrimination
-> finite integration time and bandwidth
-> responsivity / noise PSD / NEP / D*
-> identify what conventional metrics preserve or hide about detector-state distinguishability.
```

This should reveal whether conventional detector metrics are projections of the same decision problem and whether equal `D*` can conceal radically different temporal detection performance.

A focused primary-source prior-art audit remains mandatory before any novelty claim.

---

## 20. Mandatory caveats

- Trace distance / Helstrom discrimination are established results.
- Quantum-speed-limit geometry is established.
- `sqrt(N)` Dicke/Tavis--Cummings collective coupling is established.
- Cooperativity, input-output critical coupling, optical depth, and Beer-Lambert attenuation are established physical structures.
- The exact detector-boundary synthesis and the derived conditional rate laws have not yet undergone a focused prior-art audit.
- Current models omit many realistic complications: detuning/disorder, dephasing, multimode continua, thermal initial mixtures, realistic semiconductor bandstructure, correlated trapping, gain noise, timing jitter, continuous readout noise, and reset.
- Experiment 01 remains separate and untouched.
