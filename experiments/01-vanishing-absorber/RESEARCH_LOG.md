# Research Log — Experiment 01: The Vanishing Absorber

This file records why the research direction changed. Failed and superseded branches are preserved intentionally.

---

## 2026-08-08 — Experiment opened

Starting question:

> Can an ideal photodetector be made arbitrarily small, arbitrarily fast, arbitrarily sensitive, and still absorb essentially every incident photon?

Initial intuition:

```text
smaller active volume
-> fewer bulk dark events

passive optical confinement
-> recover absorption

possible cost
-> increased photon dwell time / reduced bandwidth.
```

The schematic `eta^2 B <= C V` relation was treated only as a conjectural target.

---

## One-port resonator — first exact model

Derived

```math
A(\omega)
=
\frac{4\gamma_e\gamma_a}
{(\omega-\omega_0)^2+(\gamma_e+\gamma_a)^2}
```

and absorbed-power modulation bandwidth

```math
B_{3\rm dB}
=\frac{\gamma_e+\gamma_a}{2\pi}.
```

At critical coupling,

```math
A_0=1,
\qquad
B_{3\rm dB}=\gamma_a/\pi.
```

The optical absorptance FWHM and detector modulation bandwidth were found to differ by a factor of two at critical coupling.

A toy independent bulk-dark-event metric was unexpectedly optimized at

```math
\gamma_e=2\gamma_a,
\qquad
A_0=8/9,
```

not exact critical coupling.

Direction: test whether `gamma_a` must scale with active volume.

---

## Active-volume route falsified

A shrinking-gap dielectric capacitor family was constructed with fixed capacitance and finite electric-energy participation while

```math
V_a\to0.
```

The field grows as the gap shrinks, allowing

```math
\gamma_a=\text{finite},
\qquad
\gamma_a/V_a\to\infty.
```

This killed the universal active-volume-only route.

Direction: replace continuum volume with microscopic transition resources.

---

## Thermal input channel

Exact Bose counting including bunching showed that when the signal and thermal background enter through the same optical channel, the chosen sensitivity-speed metric is optimized at critical coupling and depends on thermal mode occupation rather than active volume.

This was retained as an external-background result, not an internal-dark-count theorem.

---

## Single microscopic transition

A two-level optical transition plus irreversible dark state remained linear in the one-photon one-excitation sector.

Finite absorber number / saturation therefore did not create the missing speed ceiling.

Prior-art collision with Young, Sarovar & Leonard's quantum detector work closed several tempting novelty branches.

Direction: constrain finite-transition optical coupling.

---

## LDOS / finite emitter / oscillator-strength branch

Bandwidth-averaged LDOS theory supplied conditional coupling ceilings when material, environment, bandwidth, and emitter separation are constrained.

A finite transition-density form factor regularized the point-dipole ultraviolet divergence.

Oscillator-strength / extent inequalities still failed to close the problem before the formal enhanced rate reached

```math
\Gamma/\omega_0=O(1),
```

where weak-coupling Purcell/Markov theory breaks down.

Direction: diagonalize light and matter nonperturbatively.

---

## Nonperturbative Hopfield capture

A TRK-consistent two-mode Hopfield model showed that deep internal light-matter coupling can leave each resolved polariton perfectly rate matched while its external linewidth collapses.

This reproduced established deep-strong light-matter decoupling / Purcell-breakdown physics in detector-transfer language.

Counterexample proposed: retune bare frequencies so the useful dressed pole stays at a fixed detector frequency.

---

## Fixed-target Hopfield retuning theorem

Holding a lower dressed mode at fixed

```math
\omega_y=\omega_t>0
```

while allowing bare-frequency retuning and taking `g -> infinity` gave

```math
\min(\Gamma_L,\Gamma_R)\to0
```

for fixed local optical and detector reservoir resources.

Thus peak transfer and linewidth cannot both remain finite for the resolved target mode.

Targeted prior-art search found deep-strong decoupling, dressed decay suppression, heat-current suppression, and multimode decoupling, but no inspected source stating the exact fixed-target two-reservoir theorem.

Status kept conservative:

> **candidate distinct supporting lemma; priority unproven.**

---

## Reservoir-engineering escape quantified

Allowing the bare optical/detector reservoirs themselves to scale showed that the Hopfield no-go can be escaped by spending new external-access resource.

For target peak `eta_*` and linewidth `W_*`, at least one bare reservoir resource must grow asymptotically as `sqrt(g)` in the optimized fixed-target branch.

Direction: test multimode optics.

---

## Multimode passive audit

A spectator strong-coupling sector killed any theorem based only on the largest internal coupling anywhere in the Hamiltonian.

A bank of narrow useful resonances could tile a broad spectrum if useful mode count/density increased.

This exposed integrated optical-to-detector transfer as a more robust quantity than individual linewidth.

---

## Harmonic passive multimode theorem

The optical-to-detector transfer area was identified as an `H2` norm.

A first pass gave the loose bound

```math
\mathcal I\le2\min(L,R).
```

This was immediately superseded by a sharper Gramian-eigenbasis argument:

```math
\frac{\mathcal I}{2}
=
\sum_i
\frac{\ell_i r_i}
{\ell_i+r_i+\iota_i},
```

and therefore

```math
\boxed{
\mathcal I
\le
\frac{2LR}{L+R}.
}
```

A single passive resonance saturates it. Multimode equality requires common access ratio and no participating parasitic loss.

A numerical regression and a 4,000-network private stress test found no violations.

Direction: attack direct feedthrough and structured continua.

---

## Direct-feedthrough attack

Allowing a nonzero frequency-independent prompt block `D_RL` made the total all-frequency `H2` area diverge.

This was recorded as a real scope failure, not patched away: ideal feedthrough inserts infinite Markov bandwidth.

Over a finite band, prompt strength and resonant transfer can be bounded separately by an `L2` triangle inequality.

Direction: count prompt bandwidth as a boundary resource.

---

## Structured-reservoir audit

Reaction-coordinate / pseudomode logic showed that finite passive augmented realizations still obey the harmonic theorem.

If the augmented models converge in `H2` and terminal access budgets converge to finite values, the continuum limit inherits the same bound.

Thus spectral complexity alone is not an escape under finite passive embedding assumptions.

---

## Thermodynamic optical-access bridge

Yu, Raman & Fan's known one-free-space-channel thermodynamic coupling-rate ceiling was converted carefully from energy-decay to repository amplitude-decay convention:

```math
L_B\le W/(4\pi).
```

Combining with the harmonic access theorem gave a restricted receiving-side requirement

```math
R_B
\ge
\frac{\eta}{1-\eta}
\frac{W}{4\pi}.
```

The collision with existing broadband-absorption/rate-matching theory was documented explicitly.

Direction: remove the ideal one-way detector-sink assumption.

---

## Thermal irreversibility

For an `e <-> d` detector transition with energy release `Delta`, local detailed balance gives

```math
k_\uparrow/k_\downarrow
=e^{-\Delta/(k_BT)}.
```

Combining with the restricted detector-access requirement produced a reverse-activation / energy-bias relation.

A crucial restraint emerged:

> reverse activation is not automatically an observable dark count.

A complete detector cycle was needed.

---

## Major 2026 prior-art collision — autonomous detector machines

Schwarzhans et al., PRX Quantum 7, 033001 (2026), were found to already provide an autonomous nonequilibrium detector with work source, amplification/reset, internal dark counts, efficiency, jitter, dead time, and entropy production.

Their transient thermodynamic protocol starts with the target excitation already represented inside the target system and explicitly leaves capture as a possible additional source of cost/inefficiency.

Direction changed: do not reinvent generic detector thermodynamics; compare it to propagating optical capture.

---

## Major 2018 prior-art collision — incoming-field detector framework

Young, Sarovar & Leonard, PRA 98, 063835 (2018), already treat a quantized incoming few-photon field, absorption, detector dynamics, amplification, efficiency, dark counts, and timing in one framework.

This killed the generic claim that unifying capture and amplification is new.

The narrowed candidate junction became:

```text
externally normalized spectral capture/access constraints
+
autonomous thermodynamic detector work/reset/dark-count accounting.
```

A targeted search found no exact primary source at this intersection, but only as a negative search result.

---

## Unified three-level capture machine

A minimal analytic testbed was built with

```text
|0> reset/ground
|1> ready
|2> optically activated
```

and edges

```text
0 <-> 1 : reset/work
1 <-> 2 : incident optical channel
2 <-> 0 : counted output.
```

The ready-state photon conversion retained the familiar two-access matching structure while output photon energy could exceed input energy by consuming stored ready-state free energy.

The exact reversible three-edge steady state showed

```math
R_+
\neq
J_D
```

in general: gross forward click events and net thermodynamic detector current are different observables when reverse jumps exist.

This distinction prevented a false dark-count theorem.

---

## Readiness and NESS optical response

The reset pair gave stationary readiness

```math
p_r
=1/(1+e^{-\mathcal A_r}).
```

A serial reference model separated capture access, bandwidth, back-end efficiency, and readiness bias.

Weak-probe optical response around the nonequilibrium steady state was proportional to

```math
p_1-p_2.
```

In the non-inverted absorbing regime,

```math
0\le p_1-p_2\le1.
```

Therefore incoherent readiness pumping can restore but not exceed the fully ready passive absorptive population factor.

Direction: if the passive front end is to be beaten, use genuinely active/coherent optical control.

---

## Publication-boundary audit

A focused review concluded:

> **Continue the research. Do not write a manuscript yet.**

The passive/autonomous chain is coherent but currently vulnerable to the criticism that the principal formulas are corollaries or compositions of established frameworks.

A stronger opportunity is to quantify the explicit active resource required to beat the passive envelope.

---

## Active two-mode frequency-converter baseline

A pump-linearized two-mode converter gave

```math
T(\delta)
=
\frac{4G^2\Gamma_a\Gamma_b}
{|(\Gamma_a-i\delta)(\Gamma_b-i\delta)+G^2|^2}.
```

Unit peak requires

```math
G^2=\Gamma_a\Gamma_b.
```

The largest FWHM for fixed `G` occurs for symmetric rates, giving

```math
G_{\min}=W/(2\sqrt2).
```

If `G=g_0 sqrt(N_p)`,

```math
N_p\ge W^2/(8g_0^2).
```

Direct prior-art collision with established quantum-frequency-conversion theory means this is a calibrated baseline, not a novelty claim.

---

## Active multimode allocation

Splitting the target band among many converters can reduce pump photons only if each added mode brings new nonlinear coupling strength for free.

With aggregate budget

```math
\sum_i g_i^2\le G_0^2,
```

Cauchy-Schwarz gives

```math
N_{p,\rm tot}
\ge W^2/(8G_0^2).
```

The hidden resource moved from pump photons to aggregate nonlinear coupling strength.

---

## Traveling-wave active converter

The cavity-specific objection was attacked with undepleted three-wave mixing.

For shortest-branch unit conversion,

```math
qL=\pi/2.
```

The first half-maximum phase-mismatch constant is

```math
x_{1/2}\approx1.25457202234609.
```

If the first nonzero local mismatch derivative is order `m`,

```math
\Delta k\simeq D_m\delta^m/m!,
```

then

```math
q
\propto
|D_m|W^m,
```

and pump flux scales as `W^(2m)` in that fixed-device local-dispersion model.

This showed penalty migration into phase-matching dispersion, not a universal exponent.

---

## Active singular-value resource

A finite pumped conversion Hamiltonian

```math
H_{\rm conv}/\hbar
=\mathbf b^\dagger K\mathbf a+h.c.
```

was decomposed into singular conversion channels.

If `M_c` orthogonal channels each require efficiency `eta` in interaction time `tau`,

```math
\|K\|_F^2
\ge
\frac{M_c}{\tau^2}
\arcsin^2\sqrt\eta.
```

For pump-generated

```math
K=\sum_p\alpha_pK_p,
```

with pump photons `N_p=sum |alpha_p|^2` and pump-to-conversion Gram operator `C`,

```math
N_p
\ge
\frac{M_c\arcsin^2\sqrt\eta}
{\lambda_{\max}(C)\tau^2}.
```

Schmidt-mode conversion is established prior theory. The unresolved device/material resource became

```math
\Lambda=\lambda_{\max}(C).
```

Direction: attack genuinely time-dependent control before trying to prove a static material bound on `Lambda`.

---

## Time-dependent known-mode capture

A scalar time-controlled one-port loader was analyzed:

```math
\dot a
=-\kappa(t)a
+\sqrt{2\kappa(t)}s_{\rm in}.
```

Perfect zero-reflection loading uniquely requires

```math
\kappa(t)
=
\frac{P_{\rm in}(t)}
{2\int_{-\infty}^{t}P_{\rm in}(t')dt'}.
```

Hard finite pulse onsets generically require singular ideal coupling, matching established tunable single-photon absorber theory.

For bounded coupling `kappa <= kappa_max` over loading time `tau`, an exact Cauchy-Schwarz calculation gives

```math
\eta_{\rm cap}
\le
1-e^{-2\kappa_{\max}\tau}.
```

Thus known-time dynamic loading trades passive spectral matching for coupling-strength x loading-time resource.

---

## Unknown arrival — temporal-mode capacity

The known-mode result was then challenged with arrival-time uncertainty.

For a fixed linear capture protocol into `r` coherent storage dimensions and `M` orthogonal possible temporal input modes,

```math
\boxed{
\sum_{j=1}^{M}\eta_j\le r.
}
```

Therefore

```math
r\ge M\eta
```

is necessary for uniform target efficiency, and equal-prior average efficiency is at most `r/M`.

Interpretation:

> perfect dynamic matching of one scheduled temporal mode is not an always-on detector solution.

Unknown arrival requires storage-mode capacity, adaptive information, repeated reuse/reset, or an irreversible output continuum.

---

## Always-on temporal coverage — background and dead time

Accepting many temporal modes also accepts thermal-background photon modes.

For `M` accepted modes with thermal occupation `nbar` and efficiency at least `eta`,

```math
N_{\rm bg}
\ge
\bar n M\eta.
```

The long-time one-channel limit reproduces

```math
R_{\rm bg}
\simeq
\bar n\eta W/(2\pi).
```

In a minimal nonparalyzable detector with dead time `tau_d` and otherwise perfect raw efficiency,

```math
\eta_{\rm ext}
\le
\frac1{1+\bar nW\tau_d/(2\pi)}.
```

This closed the known-time/unknown-time gedanken at model level:

```text
scheduled mode
-> dynamic control can match it

always-on detector
-> must accept many temporal modes
-> irreversible output capacity restores coverage
-> admitted background consumes dead-time capacity.
```

---

## Current direction

The strongest unresolved abstraction is now a common **space-time mode resource law** for an actively controlled always-on detector.

The candidate accounting should include

```text
accepted spatiotemporal mode count
+
pump/control norm
+
irreversible output rank/capacity
+
background occupation
+
reset/dead-time capacity.
```

Before promoting any theorem, attack it with

- noncommuting time-dependent controls;
- adaptive measurement/feedforward;
- time-switched energy trapping;
- large-rank output continua;
- active gain / non-Foster matching.

No manuscript should be opened yet.