# Current State — Experiment 01: The Vanishing Absorber

**Date:** 2026-08-08  
**Status:** exploratory; passive/autonomous baseline mapped; active frequency-conversion and time-dependent-capture escapes under active audit; no novelty claim  

## 1. Guiding question

Can an ideal photodetector be made arbitrarily small, arbitrarily fast, arbitrarily sensitive, and still absorb essentially every incident photon?

The original geometric-volume conjecture failed. The current resource chain is

```text
propagating optical access
+
irreversible detector access
+
active pump/control resource when passive matching is exceeded
+
temporal-mode coverage for unknown arrival
+
external background and reset/dead-time capacity.
```

---

## 2. Canonical frontier

Read after root `AGENTS.md`:

1. `PASSIVE_MULTIMODE_TRANSFER_AREA_BOUND.md`
2. `PUBLICATION_BOUNDARY_AUDIT.md`
3. `ACTIVE_CONVERSION_SINGULAR_VALUE_BOUND.md`
4. `TIME_DEPENDENT_CAPTURE_AUDIT.md`
5. `TEMPORAL_UNCERTAINTY_MODE_CAPACITY.md`
6. `ALWAYS_ON_TEMPORAL_COVERAGE.md`
7. `ACTIVE_FREQUENCY_CONVERTER_BASELINE.md`
8. `MULTIMODE_ACTIVE_PUMP_RESOURCE.md`
9. `TRAVELING_WAVE_ACTIVE_CONVERTER.md`
10. `AUTONOMOUS_DETECTOR_CAPTURE_GAP.md`
11. `UNIFIED_THREE_LEVEL_CAPTURE_MACHINE.md`
12. older supporting branches only for provenance.

`CLAIM_LEDGER.md` is the epistemic boundary.

---

## 3. Stopped early routes

### Active volume

An explicit shrinking-gap passive continuum family has

```math
V_a\to0,
\qquad
\gamma_a=\text{finite},
\qquad
\gamma_a/V_a\to\infty.
```

Therefore passivity alone does not support a universal law such as

```text
eta^2 B <= C V_a.
```

### Finite absorber number

A single two-level absorber remains linear in the one-excitation sector for one incident photon. Finite absorber number / saturation alone does not impose the missing one-photon speed ceiling.

### Weak-coupling oscillator-strength closure

Finite emitter extent regularizes the point-dipole divergence, but the retained oscillator-strength / extent inequalities do not close the problem before the formal enhanced rate reaches `O(omega_0)`, where weak-coupling Purcell/Markov theory fails.

---

## 4. Supporting nonperturbative result

In the TRK-consistent two-mode Hopfield model, hold a lower dressed mode at fixed target frequency

```math
\omega_y=\omega_t>0
```

while retuning the bare frequencies and sending internal coupling `g -> infinity`.

For fixed local optical and detector reservoir resources,

```math
\boxed{
\min(\Gamma_L,\Gamma_R)\to0.
}
```

A resolved target resonance therefore cannot retain both finite peak transfer and finite linewidth.

If bare reservoirs are strengthened to compensate, maintaining target peak `eta_*` and linewidth `W_*` requires

```math
\boxed{
\max(\gamma_L,\gamma_R)
\ge
\Gamma_*
\sqrt{1+2g/\omega_t},
}
```

where

```math
\Gamma_*
=\frac{W_*}{4}
\left(1-\sqrt{1-\eta_*}\right).
```

Deep-strong decoupling is established prior physics. The exact fixed-target corollary remains only a candidate distinct supporting lemma; priority is unproven.

---

## 5. Strongest passive finite-network theorem

For a stable finite passive strictly proper optical-to-detector network,

```math
A=-iH-(\Gamma_L+\Gamma_R+\Gamma_I),
\qquad H=H^\dagger,
```

with

```math
L=\operatorname{Tr}\Gamma_L,
\qquad
R=\operatorname{Tr}\Gamma_R,
```

define

```math
\mathcal I_{L\to R}
=
\int_{-\infty}^{\infty}
\frac{d\omega}{2\pi}
\operatorname{Tr}[G_{RL}^\dagger G_{RL}].
```

Then

```math
\boxed{
\mathcal I_{L\to R}
\le
\frac{2LR}{L+R}.
}
```

In the left controllability-Gramian eigenbasis,

```math
\boxed{
\frac{\mathcal I_{L\to R}}2
=
\sum_i
\frac{\ell_i r_i}
{\ell_i+r_i+\iota_i}.
}
```

A single passive resonance saturates the bound. Multimode equality requires no participating parasitic loss and a common access ratio `ell_i/r_i=L/R`.

For angular-frequency band width `W`,

```math
\boxed{
\overline T_B
\le
\frac{4\pi LR}{W(L+R)}.
}
```

This is an external-access resource law, not an absolute detector bandwidth theorem. `H2`/Lyapunov/passivity ingredients are standard; novelty is not claimed.

---

## 6. Passive scope audits

### Direct feedthrough

A nonzero frequency-independent prompt optical-to-detector block makes the total all-frequency `H2` area divergent because it inserts infinite Markov bandwidth.

Over finite band width `W`,

```math
\boxed{
\sqrt{\mathcal I_B}
\le
\sqrt{\frac{W}{2\pi}}\,\|D_{RL}\|_F
+
\sqrt{\frac{2LR}{L+R}}.
}
```

Prompt channel strength/bandwidth is an additional boundary resource.

### Structured reservoirs

If finite passive augmented realizations converge in `H2` with finite limiting terminal access budgets, the harmonic theorem survives the continuum limit.

Spectral complexity alone is not an escape under those assumptions.

---

## 7. Passive optical-to-thermodynamic bridge

Established one-free-space-channel thermodynamic coupling theory gives, in the repository amplitude-rate convention,

```math
\boxed{
L_B\le\frac{W}{4\pi}.
}
```

Combining with the harmonic theorem gives the restricted receiving-side requirement

```math
\boxed{
R_B
\ge
\frac{\eta}{1-\eta}
\frac{W}{4\pi}
}
```

for target band-averaged transfer `eta` under the stated modal/channel assumptions.

For a thermal detector localization transition with energy release `Delta`,

```math
\frac{k_\uparrow}{k_\downarrow}
=e^{-\Delta/(k_BT)}.
```

Using `k_down=2R_B`,

```math
\boxed{
k_\uparrow
\ge
\frac{\eta}{1-\eta}
\frac{W}{2\pi}
e^{-\Delta/(k_BT)}.
}
```

Reverse activation is not automatically an observable dark count.

---

## 8. Major prior-art boundary

### Young, Sarovar & Leonard (2018)

Already treat an incoming quantized few-photon field, absorption, amplification/monitored detector dynamics, efficiency, dark counts, and timing in one quantum framework.

### Schwarzhans et al. (2026)

Already treat an autonomous nonequilibrium detector work source, amplification/reset, internal dark counts, efficiency, jitter, dead time, and entropy production.

Their transient thermodynamic protocol treats the target excitation as already present rather than deriving a propagating spectral capture stage.

A targeted search has not found a primary source combining

```text
propagating spectral capture/access constraints
+
autonomous detector work/reset/dark-count thermodynamics
```

in one resource-accounting theory.

This is only a negative search result. Priority is unproven.

---

## 9. Unified three-level testbed

Use

```text
|0> reset/ground
|1> metastable detection-ready
|2> optically activated

0 <-> 1 : work/reset
1 <-> 2 : propagating optical signal
2 <-> 0 : counted detector output.
```

Conditioned on readiness, single-photon conversion has the usual two-access form

```math
\boxed{
T_{L\to R}(\omega)
=
\frac{4\Gamma_L\Gamma_R}
{(\omega-\omega_L)^2
+(\Gamma_L+\Gamma_R+\Gamma_I)^2}.
}
```

The counted output energy can exceed the incident photon energy because the ready state stores free energy:

```math
\hbar\omega_R
=\hbar\omega_L+(E_1-E_0).
```

For reversible population rates

```text
u:0->1, d:1->0, a:1->2, b:2->1, c:2->0, e:0->2,
```

define

```math
Z=ac+ae+au+bd+be+bu+cd+cu+de.
```

Then

```math
p_0=(ac+bd+cd)/Z,
```

```math
p_1=(be+bu+cu)/Z,
```

```math
p_2=(ae+au+de)/Z.
```

Gross forward click rate:

```math
\boxed{
R_+
=\frac{c(ae+au+de)}{Z}.
}
```

Net detector/cycle current:

```math
\boxed{
J_D
=\frac{uac-dbe}{Z}.
}
```

Thus gross event counts and net thermodynamic current are different observables when reverse jumps exist.

---

## 10. Readiness / NESS result

For reset pair `u:0->1`, `d:1->0`,

```math
p_r
=\frac1{1+e^{-\mathcal A_r}},
\qquad
\mathcal A_r=\ln(u/d).
```

In the dilute serial reference model,

```math
\boxed{
\overline\eta_{\rm ext}
\le
\frac{\eta_D}{1+e^{-\mathcal A_r}}
\frac{R_C}{R_C+W/(4\pi)}.
}
```

For a weak probe on the signal transition,

```math
\boxed{
\rho_{21}^{(1)}
=
\frac{i\Omega}{2}
\frac{p_1-p_2}{\gamma_\perp+i\Delta}.
}
```

In the non-inverted absorptive regime,

```math
0\le p_1-p_2\le1.
```

Thus incoherent readiness pumping can restore but not exceed the fully ready absorptive population factor. To leave the passive envelope requires true optical gain or coherent/parametric active control.

---

## 11. Publication-boundary audit

`PUBLICATION_BOUNDARY_AUDIT.md` concluded:

> **Do not write a manuscript yet.**

The passive/autonomous chain is coherent, but the strongest equations are either standard-system corollaries, compositions of strong prior results, or have uncertain mathematical priority.

The best route toward a more distinct theoretical result is to quantify the explicit active resource required to beat the passive envelope.

---

## 12. Active frequency-conversion baseline

For two pump-coupled resonant modes,

```math
\dot a=-\Gamma_a a-iGb+\sqrt{2\Gamma_a}s_{\rm in},
```

```math
\dot b=-\Gamma_b b-iG^*a,
```

the conversion probability is

```math
\boxed{
T(\delta)
=
\frac{4G^2\Gamma_a\Gamma_b}
{|(\Gamma_a-i\delta)(\Gamma_b-i\delta)+G^2|^2}.
}
```

Unit peak requires

```math
G^2=\Gamma_a\Gamma_b.
```

For prescribed unit-peak angular FWHM `W`, the minimum pump-enhanced coupling occurs at

```math
\Gamma_a=\Gamma_b=G
```

and obeys

```math
\boxed{
G_{\min}=\frac{W}{2\sqrt2}.
}
```

If `G=g_0 sqrt(N_p)`,

```math
\boxed{
N_p\ge\frac{W^2}{8g_0^2}.
}
```

This is a known-physics architecture baseline with direct quantum-frequency-conversion prior-art overlap, not a fundamental theorem.

---

## 13. Active multimode / traveling-wave stress tests

### Discrete channel allocation

If subchannel `i` obeys

```math
N_i\ge W_i^2/(8g_i^2)
```

and the aggregate nonlinear-coupling budget is

```math
\sum_i g_i^2\le G_0^2,
```

then

```math
\boxed{
N_{p,\rm tot}
\ge
\frac{W^2}{8G_0^2}.
}
```

Mode proliferation is not free if total nonlinear coupling strength is fixed.

### Traveling-wave converter

For shortest-branch unit conversion,

```math
qL=\pi/2.
```

The first half-maximum phase-mismatch constant is

```math
x_{1/2}\approx1.25457202234609.
```

If the first nonzero local phase-mismatch derivative is

```math
\Delta k(\delta)
\simeq D_m\delta^m/m!,
```

then

```math
\boxed{
q
=
\frac{\pi|D_m|}
{2^{m+2}m!x_{1/2}}
W^m,
}
```

so the pump flux scales as `W^(2m)` within this fixed-device local-dispersion model.

These exponents are architecture dependent; no universal `W^2` law is claimed.

---

## 14. Abstract active singular-value resource

For a finite number-conserving pumped converter,

```math
H_{\rm conv}/\hbar
=\mathbf b^\dagger K\mathbf a
+\mathbf a^\dagger K^\dagger\mathbf b.
```

If `M_c` orthogonal singular channels must each convert with probability at least `eta` during interaction time `tau`,

```math
\boxed{
\|K\|_F^2
\ge
\frac{M_c}{\tau^2}
\arcsin^2\sqrt\eta.
}
```

If

```math
K=\sum_p\alpha_pK_p,
\qquad
N_p=\sum_p|\alpha_p|^2,
```

and

```math
C_{pq}=\operatorname{Tr}(K_p^\dagger K_q),
\qquad
\Lambda=\lambda_{\max}(C),
```

then

```math
\boxed{
N_p
\ge
\frac{M_c\arcsin^2\sqrt\eta}
{\Lambda\tau^2}.
}
```

Schmidt/singular-mode frequency conversion is established prior theory. The added pump-norm bookkeeping has unassessed priority.

The physical material/device resource hidden inside `Lambda` is not yet bounded.

---

## 15. Time-dependent known-mode capture

For a single time-controlled lossless storage mode,

```math
\dot a=-\kappa(t)a+\sqrt{2\kappa(t)}s_{\rm in},
```

zero reflection fixes the exact perfect-loading schedule

```math
\boxed{
\kappa(t)
=
\frac{P_{\rm in}(t)}
{2\int_{-\infty}^{t}P_{\rm in}(t')dt'}.
}
```

Hard finite pulse onsets generically require `kappa ~ 1/(t-t0)` singular behavior, consistent with established tunable single-photon absorber theory.

With

```math
0\le\kappa(t)\le\kappa_{\max}
```

over loading duration `tau`, the exact optimal one-mode capture probability satisfies

```math
\boxed{
\eta_{\rm cap}
\le
1-e^{-2\kappa_{\max}\tau}.
}
```

Hence

```math
\boxed{
\kappa_{\max}\tau
\ge
\frac12\ln\frac1{1-\eta}.
}
```

This is a coupling-rate x loading-time resource, not directly a universal spectral-bandwidth theorem.

---

## 16. Unknown arrival becomes a temporal-mode capacity problem

Let a fixed linear capture protocol map the incoming temporal Hilbert space into an `r`-dimensional coherent storage space.

For `M` orthogonal possible input temporal modes with efficiencies `eta_j`,

```math
\boxed{
\sum_{j=1}^{M}\eta_j\le r.
}
```

Therefore uniform efficiency `eta` requires

```math
\boxed{
r\ge M\eta,}
```

and equal-prior average capture obeys

```math
\boxed{
\overline\eta\le r/M.
}
```

Arrival-time prior information is therefore a resource. A known temporal mode can be dynamically matched; an unknown arrival over many orthogonal modes requires storage capacity, adaptation, reuse/reset, or an irreversible output continuum.

---

## 17. Always-on temporal coverage admits background and consumes dead time

For `M` accepted modes with thermal occupation `nbar` and efficiency at least `eta`,

```math
\boxed{
N_{\rm bg}
\ge
\bar n M\eta.
}
```

For one spatial/polarization channel over long observation time with angular bandwidth `W`, this reproduces

```math
R_{\rm bg}
\simeq
\bar n\eta\frac{W}{2\pi}.
```

In a minimal nonparalyzable detector with dead time `tau_d` and otherwise perfect raw efficiency,

```math
\boxed{
\eta_{\rm ext}
\le
\frac{1}
{1+\bar n W\tau_d/(2\pi)}.
}
```

This is a model-level background-blocking result, not a universal dead-time theorem.

---

## 18. Current frontier

The active branch has now separated two cases cleanly:

```text
known/scheduled temporal mode
-> dynamic impedance matching can bypass a passive stationary spectral match
-> finite coupling x loading-time resource

unknown/always-on arrival
-> detector must cover many temporal modes
-> finite coherent storage has a rank limit
-> irreversible output continuum restores temporal coverage
-> accepted thermal modes create background counts and dead-time occupancy.
```

The next high-value question is whether these active and temporal results can be unified into a common **space-time mode resource law**:

> How do pump/control norm, number of accepted spatiotemporal modes, irreversible output capacity, and background occupation constrain an actively controlled always-on photodetector?

Do not open a manuscript yet. Do not add HgCdTe-specific transport yet.