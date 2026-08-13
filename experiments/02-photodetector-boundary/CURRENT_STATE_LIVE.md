# Current Live State — Experiment 02

**Date:** 2026-08-12  
**Status:** exploratory first-principles theory; microscopic interaction through decision and cyclic reset now mapped in minimal models  
**Priority:** unassessed; no novelty claim

This is the current state pointer. `CLAIM_LEDGER.md` is the epistemic boundary; `RESEARCH_LOG.md` preserves chronology. Detailed derivations are authoritative for algebra.

Active derivations:

1. `INTERACTION_ACTION_LOWER_BOUND.md`
2. `N_DIPOLE_SINGLE_MODE_MODEL.md`
3. `COHERENT_CAPTURE_TO_RECORD.md`
4. `TRAVELING_WAVE_CAPTURE.md`
5. `MODE_WEIGHTED_OPTICAL_DEPTH.md`
6. `SEMICONDUCTOR_DECISION_BRIDGE.md`
7. `CONTINUOUS_GAUSSIAN_DECISION.md`
8. `SIGNAL_DEPENDENT_NOISE.md`
9. `UNKNOWN_ARRIVAL_TIME.md`
10. `TASK_SPECIFIC_DETECTIVITY.md`
11. `RESET_AND_CYCLE_CLOSURE.md`

---

## 1. Strongest current answer

The starting question was:

> At what point does a collection of atoms become a photodetector?

The current answer is:

> **There is no universal atom-count transition. Detection is a relation among the optical task, the matter and optical interaction architecture, the accessible output process, temporal/noise constraints, and the observer's decision criterion. Under explicit constraints, minimum effective atom numbers, optical depths, rate ratios, event energies, or reset resources emerge.**

The detector boundary has therefore migrated from a boundary in matter to a boundary in **measurement performance**.

---

## 2. Operational quantum criterion

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
\boxed{P_{e,\min}=\frac12(1-\mathcal D_D).}
```

This preserves the first fundamental correction:

```text
absorption != detection.
```

Perfect absorption can leave no accessible material record; a dispersive nonabsorptive interaction can create one.

---

## 3. Atom count only reappears after resource constraints

A universal positive final deposited-energy cost failed. In the stated pure/unitary finite-time model, a surviving resource is interaction action:

```math
\boxed{
\mathcal A_\Delta
\ge
\hbar\arcsin(1-2\epsilon).
}
```

Perfect discrimination requires `A_Delta >= pi hbar/2`.

If each constituent supplies at most action `a_max`,

```math
N
\ge
\left\lceil
\frac{\hbar\arcsin(1-2\epsilon)}{a_{\max}}
\right\rceil.
```

For identical resonant dipoles,

```math
\boxed{G=g\sqrt N,}
```

and perfect transient first-lobe transfer requires

```math
N_{\min}=\left\lceil(\pi/(2g\tau))^2\right\rceil.
```

These are constrained coupling/time results, not band-formation thresholds.

---

## 4. Persistent record requires rate matching

For a photon initially inside a lossy optical mode,

```math
\boxed{
P_R
=\frac{4G^2\Gamma}
{(\kappa+\gamma+\Gamma)[4G^2+\kappa(\gamma+\Gamma)]}.
}
```

The desired trapping rate has a finite optimum; for `gamma=0`, `Gamma_opt=2G`.

Thus

```text
more irreversibility != monotonically better detection.
```

---

## 5. External capture kills a peak-efficiency N threshold

For an incident traveling photon, clean one-port critical matching gives

```math
\boxed{\Gamma_{\rm match}=4G^2/\kappa.}
```

At resonance this can produce unit record conversion for any nonzero `G` if sufficiently slow/narrowband operation is allowed.

Therefore:

> **Peak monochromatic efficiency alone does not imply a positive minimum atom count. Weak coupling is paid for in bandwidth/time.**

Optimized external efficiency is

```math
\boxed{
\eta_{R,\max}
=\eta_{\rm esc}\frac{C_N}{1+C_N},
}
```

with `eta_esc=kappa_in/kappa` and `C_N=4G^2/(kappa gamma)`.

Finite photon bandwidth restores a constrained resource threshold.

---

## 6. Total N becomes mode-weighted coupling / optical depth

For unequal microscopic couplings,

```math
\boxed{G^2=\sum_j|g_j|^2.}
```

Only optically participating matter counts.

In a dilute traveling-wave continuum,

```math
\boxed{
\mathrm{OD}=n\sigma L
=\frac{N_{\rm col}\sigma}{A},
}
```

with `P_abs=1-e^-OD`.

Thus optical depth / oscillator-strength overlap is more invariant than total atom count in extended matter.

---

## 7. Semiconductor electron-hole bridge

For a minimal slab,

```math
\boxed{
\eta_s
=\eta_{\rm mode}(1-e^{-\alpha L})\eta_{eh}P_{\rm col}P_{\rm read}.
}
```

With independent extraction/recombination hazards,

```math
\boxed{
P_{\rm col}
=\frac{\Gamma_{\rm ext}}
{\Gamma_{\rm ext}+\Gamma_{\rm rec}}.
}
```

Electron-hole generation is therefore the semiconductor-specific **microscopic transduction stage**, not the complete detection event.

For independent Poisson dark clicks,

```math
\boxed{
\mathcal D_{\rm click}=\eta_s e^{-R_d\tau},
}
```

and target error requires the necessary condition

```math
\boxed{R_d\tau\le-\ln(1-2\epsilon).}
```

---

## 8. Continuous electrical output -> full decision geometry

For equal-covariance Gaussian output,

```math
H_0:y=n,\qquad H_1:y=s+n,
```

the optimum distance is

```math
\boxed{
d^2=\langle s,C^{-1}s\rangle
=\int\frac{|\tilde s(f)|^2}{S_n^{(2)}(f)}df.
}
```

and

```math
\boxed{P_e=Q(d/2).}
```

Input referring gives

```math
\boxed{
d^2=\int\frac{|\tilde p(f)|^2}{\mathrm{NEP}_2^2(f)}df.}
```

For a one-pole white-noise short-pulse benchmark,

```math
\boxed{
d^2
=\frac{E^2}{\tau\,\mathrm{NEP}^2}
=\frac{E^2D^{*2}}{A\tau}.}
```

Thus equal scalar `D*` does not imply equal event-detection performance.

---

## 9. Signal-dependent noise makes the complete distribution fundamental

For Gaussian hypotheses with `C_0 != C_1`, the optimum likelihood ratio is quadratic. A covariance change can carry information even when the mean does not change.

For Poisson counts,

```math
\ell(K)=K\ln(\mu_1/\mu_0)-(\mu_1-\mu_0),
```

and

```math
\boxed{
BC
=\exp[-(\sqrt{\mu_1}-\sqrt{\mu_0})^2/2].}
```

The familiar background-shot-noise SNR is only a local expansion of this full count-distribution geometry.

In the zero-background limit,

```math
\boxed{P_e=\frac12e^{-\lambda_sT}.}
```

Hence no single fixed-noise SNR law spans all counting regimes.

---

## 10. Unknown arrival time creates a search resource

For `M` independent candidate event times,

```math
\boxed{
\Lambda(z)=\frac1M\sum_{m=1}^M e^{dz_m-d^2/2}.}
```

A max-threshold benchmark gives

```math
P_{\rm FA}=1-\Phi(\eta)^M,
```

```math
P_{\rm miss}=\Phi(\eta-d)\Phi(\eta)^{M-1}.
```

At fixed small false-alarm probability the threshold grows approximately as `sqrt(2 ln M)`.

Thus intrinsic speed, search-window duration, and false-alarm budget are separate temporal resources.

---

## 11. Task-specific scalar exists; universal scalar ranking usually does not

For `p(t)=E q(t)` with normalized waveform shape,

```math
\boxed{
\mathcal K_D[q]
=\int\frac{|\tilde q(f)|^2}{\mathrm{NEP}_{2,D}^2(f)}df,
}
```

so

```math
\boxed{
E_{\min}(q,\epsilon)
=\frac{2Q^{-1}(\epsilon)}{\sqrt{\mathcal K_D[q]}}
}
```

for known-time equal-prior Gaussian readout.

Define

```math
W_D(f)=1/\mathrm{NEP}_{2,D}^2(f).
```

If `W_A>=W_B` pointwise over the allowed band, A dominates B for every waveform in the task class.

If `W_A-W_B` changes sign, there are tasks that reverse the ranking.

Therefore detector comparison is generally a **partial order**, not a universal one-dimensional leaderboard.

---

## 12. Thermodynamics re-enters at cycle closure, not necessarily acquisition

The naive statement

```text
every click dissipates at least k_BT ln2
```

remains rejected.

For a binary record with event probability `p`, logical entropy is

```math
\boxed{
h(p)=-p\ln p-(1-p)\ln(1-p).}
```

Under ideal degenerate-memory, quasistatic isothermal erasure assumptions, exact reset with no retained side information has scale

```math
\boxed{W_{\rm erase,min}\ge k_BT h(p).}
```

`k_BT ln2` is only the unbiased `p=1/2` case.

If the detector exports a copy of its record to an external register `R`, local reset can in principle use that side information; the relevant uncertainty becomes `H(M|R)`. For a perfect external copy, `H(M|R)=0`.

Thus:

```text
local reusable detector
!=
mandatory local k_BT ln2 heat per click.
```

The entropy has been exported rather than erased.

A nontrivial Landauer-like requirement reappears only after **global cycle closure** is imposed: detector, controller, and all record memories must return to standard states and no event copy may remain outside the accounting boundary.

Then the event-record entropy must eventually be removed somewhere under the stated thermodynamic assumptions.

---

## 13. Stability versus reset-speed control range

For an activated record with spontaneous rate

```math
\Gamma_d=\nu_0e^{-E_b/(k_BT)},
```

retention error `p_d` over `tau_rec` requires

```math
\boxed{
E_b
\ge
k_BT\ln\left[
\frac{\nu_0\tau_{\rm rec}}
{-\ln(1-p_d)}
\right].}
```

If reset lowers the barrier by `Delta E`, achieving reset failure `epsilon_r` within `tau_r` gives the conditional requirement

```math
\boxed{
\Delta E
\ge
k_BT\ln\left[
\frac{\tau_{\rm rec}\ln(1/\epsilon_r)}
{\tau_r[-\ln(1-p_d)]}
\right]
}
```

when positive and when the same activated-rate model applies.

This is a **control-range / stability-speed tradeoff**, not a universal dissipated-work bound.

---

## 14. Current strongest conceptual structure

```text
material constitution
-> optical access / mode overlap
-> mode-weighted interaction resource
-> microscopic transduction
-> acquisition/extraction versus loss
-> persistent record
-> complete conditional output process
-> timing / nuisance parameters
-> optimum likelihood decision
-> error probability
-> local reset / record export
-> optional global cycle closure.
```

Every attempted universal scalar has so far exposed an omitted resource:

```text
atom count       -> coupling/time and mode overlap
peak efficiency  -> bandwidth
more atoms       -> optical escape
more absorber    -> downstream loss and dark events
fixed-noise SNR  -> hypothesis-dependent noise statistics
D*               -> temporal/spectral task structure
known-time score -> timing-search complexity
local reset heat -> exported record capacity.
```

---

## 15. Current frontier

The next strongest lower-bound attack is global thermodynamic accounting.

Test whether the cycle-closure result survives when allowing

```text
correlations with the optical/environmental input as side information;
work extraction from the detected field;
nonequilibrium reservoirs and active pumps;
continuous reversible transduction with no explicit binary memory;
exported records that are never reset inside the accounting horizon.
```

The goal is to identify the **weakest precise closure assumptions** under which any nontrivial universal detector-cycle bound survives.

A focused primary-source prior-art audit remains mandatory before novelty language.
