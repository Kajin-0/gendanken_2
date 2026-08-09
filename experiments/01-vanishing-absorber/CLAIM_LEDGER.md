# Claim Ledger — Experiment 01

**Updated:** 2026-08-09  
**Status:** exploratory; active frontier is an entrance-gap spectral initial-condition crossover in graded HgCdTe; the earlier universal timing-maximum interpretation is superseded; no novelty claim

This file is the epistemic boundary. `RESEARCH_LOG.md` preserves chronology and specialized derivation files preserve detailed proofs.

## Status vocabulary

- **KNOWN** — established external result used as input.
- **DERIVED** — exact consequence of stated repository assumptions.
- **CHECKED** — independently or numerically verified.
- **CONDITIONAL** — exact only inside a deliberately simplified model.
- **CANDIDATE DISTINCT** — potentially unusual formulation; priority unproven.
- **INVALIDATED** — explicit counterexample or correction found.
- **SUPERSEDED** — replaced by a stronger/corrected statement.
- **OPEN** — unresolved.
- **NON-CLAIM** — explicitly not asserted.

---

## 1. Permanent invalidations / stopped shortcuts

### H1 — active-volume-only universal detector limit
**Status:** INVALIDATED

Ideal field concentration can retain finite optical participation while active material volume tends to zero.

### H2 — finite absorber count as one-photon speed limit
**Status:** INVALIDATED

The one-photon / one-excitation sector remains linear.

### H3 — largest internal coupling as universal multimode resource
**Status:** INVALIDATED

Spectator strongly coupled sectors are counterexamples.

### H4 — finite internal storage rank as universal always-on capacity
**Status:** INVALIDATED

Adaptive branching and output continua export the missing distinguishability.

### H5 — local Landauer erasure as universal detector-event cost
**Status:** INVALIDATED

The useful output can itself carry the record information.

### H6 — spectral FWHM as architecture-independent carrier speed
**Status:** INVALIDATED

Multipole filters can retain spectral width while increasing delay/state weight.

### H7 — low-field mobility extrapolated to high-field HgCdTe
**Status:** INVALIDATED SHORTCUT

High-field HgCdTe transport is non-ohmic and velocity need not increase monotonically with field.

### H8 — direct BTBT must be the first HgCdTe high-field limiter
**Status:** INVALIDATED SHORTCUT

TAT and nonlocal hot-electron / impact-ionization physics can intervene earlier.

### H9 — nonuniform field alone improves homogeneous local WKB leakage at fixed transit time
**Status:** INVALIDATED in the stated homogeneous local model

Uniform field is optimal under the derived assumptions; heterogeneity is needed for a real allocation benefit.

### H10 — local `F_II(x)` can always be inserted into a tunneling tolerance envelope
**Status:** INVALIDATED GENERALIZATION

Thin/fast impact ionization is history dependent. Carry a nonlocal carrier-energy state unless local equilibration is justified.

### H11 — every downstream photoelectron may be treated as cold
**Status:** INVALIDATED

For `E_gamma > E_g(x)`, direct photoexcitation gives nonzero initial carrier excess energy.

### H12 — entrance-gap timing maximum is transport independent
**Status:** INVALIDATED GENERALIZATION / SUPERSEDED

The forward-ballistic model gives a local timing maximum at `E_gamma = E_g,in`, but strong-scattering drift-diffusion gives a rise into a plateau and a finite momentum-memory stochastic surrogate can give decline, plateau, or continued rise depending on the initial longitudinal momentum distribution.

The transport-independent object is the **entrance-gap initial-condition switch**, not a mandatory maximum.

---

## 2. Supporting results from earlier abstract branches

### P1 — finite passive-network harmonic transfer-area bound
**Status:** DERIVED / CHECKED; mathematical ingredients are established prior theory; novelty not claimed

```math
\boxed{
\mathcal I_{L\to R}
\le
\frac{2LR}{L+R},
\qquad
L=\operatorname{Tr}\Gamma_L,
\quad
R=\operatorname{Tr}\Gamma_R.
}
```

### P2 — fixed-target Hopfield access collapse
**Status:** CANDIDATE DISTINCT supporting lemma; priority unproven

For the stated fixed-target two-mode Hopfield model with fixed local bath resources and `g -> infinity`,

```math
\boxed{
\min(\Gamma_L,\Gamma_R)\to0.
}
```

### P3 — active finite-mode conversion resource
**Status:** DERIVED bookkeeping result built on established singular-mode conversion theory

```math
\boxed{
N_p
\ge
\frac{M_c\arcsin^2\sqrt\eta}
{\Lambda\tau^2}.
}
```

These are provenance, not the active material frontier.

---

## 3. HgCdTe graded direct-Zener results

### G1 — exact linear graded-Kane WKB action
**Status:** DERIVED / CHECKED / CONDITIONAL

For linear edges,

```math
\boxed{
\mathcal S(E)
=\frac{\pi\sqrt{S_cS_v}}
{4\hbar v_K}(x_c-x_v)^2.
}
```

### G2 — band-offset-partition invariant geometry
**Status:** DERIVED

```math
\boxed{S_v=S_c-G,}
```

with

```math
G=-dE_g/dx.
```

### G3 — fixed-conduction-slope Zener ratio
**Status:** DERIVED / CHECKED / CONDITIONAL; priority unassessed

At fixed `S_c=S`, define `delta=G/S`:

```math
\boxed{
\frac{\mathcal S_Z(\delta)}
{\mathcal S_Z(0)}
=
\frac{(2-\delta)^2}
{4(1-\delta)^{3/2}},
\qquad 0\le\delta<1.
}
```

This concerns one smooth direct-Zener path only.

---

## 4. Self-consistent quasi-neutral grading

### Q1 — majority-band pinning in p-type quasi-neutral material
**Status:** DERIVED / CONDITIONAL

For nondegenerate holes with `p approximately N_A`,

```math
\boxed{
\frac{dE_v}{dx}
\simeq
k_BT\frac{d}{dx}\ln(N_A/N_v).
}
```

Nearly constant `N_A/N_v` gives approximately

```math
\boxed{E_v\approx\text{constant},}
```

and therefore for decreasing gap

```math
\boxed{S_c\approx G.}
```

### Q2 — uniformly depleted multi-micron grading is not the default physical picture
**Status:** CONDITIONAL design conclusion

The active baseline is a quasi-neutral graded interior plus short screening/depletion/boundary regions.

---

## 5. Collection-boundary results

### B1 — barrier-free compensation voltage
**Status:** DERIVED

```math
\boxed{
qV_b\ge\alpha\Delta E_g^{(b)}.
}
```

At equality the net conduction-edge step is zero.

### B2 — peak-field lower bound
**Status:** DERIVED

```math
\boxed{F_{\max}\ge V_b/w.}
```

### B3 — local tunneling voltage capacity
**Status:** DERIVED / CONDITIONAL

For local inverse-field mechanisms,

```math
\boxed{
F_{\rm allow}(x)
=\min_m\frac{F_m(x)}{\Sigma_m},
}
```

and feasibility requires

```math
\boxed{
V_b\le\int_0^wF_{\rm allow}(x)dx.
}
```

Use this for local TAT/BTBT models, not nonlocal II.

### B4 — maximin field allocation
**Status:** DERIVED

For one local exponent scale,

```math
\boxed{
F_{\rm opt}(x)
=\frac{V_bF_T(x)}{\int F_Tdx}.
}
```

### B5 — minimum-compensation boundary can be a relaxation region
**Status:** DERIVED / CONDITIONAL

At `qV_b=alpha Delta E_g^(b)`, the total conduction-edge step is flat while the gap rises. In the current mean-energy model, carrier excess can relax without adding new downhill conduction work.

---

## 6. Graded nonlocal carrier-energy results

### N1 — path-dependent mean-energy state
**Status:** DERIVED / CONDITIONAL

```math
\boxed{
\frac{d\varepsilon}{dx}
=S_c(x)-\frac{\varepsilon}{\ell_E(x)}.
}
```

### N2 — linear graded mean-II phase boundary
**Status:** DERIVED / CHECKED / CONDITIONAL; priority unassessed

For linear quasi-neutral grading, constant `ell_E`, and `E_th=chi E_g`,

```math
\boxed{
\zeta_{\rm II}(r,\chi)
=
\frac{\chi}
{\chi+(1-e^{-r})/r}.
}
```

Ballistic limit:

```math
\boxed{
\zeta_{\rm II}\to\frac{\chi}{1+\chi}.}
```

### N3 — relaxation-required grading span
**Status:** DERIVED / CHECKED / CONDITIONAL

When `zeta > chi/(1+chi)`, define

```math
\boxed{a=\chi(1-\zeta)/\zeta.}
```

Then

```math
\boxed{
r_{\min}
=\frac1a+W_0\!\left[-\frac1a e^{-1/a}\right],
\qquad
L\ge\ell_Er_{\min}.
}
```

These remain mean-energy constraints, not stochastic II onset theorems.

---

## 7. Wavelength-resolved graded photodetection

### S1 — earliest generation position
**Status:** DERIVED / CONDITIONAL ON LOCAL-GAP ABSORPTION

For a linear graded gap,

```math
\boxed{
x_g(E_\gamma)
=\max\!\left[
0,
\frac{E_{g,\rm in}-E_\gamma}{G}
\right].
}
```

### S2 — exact conditional generation distribution
**Status:** KNOWN probability consequence / DERIVED application

For total eligible optical depth `tau_gamma`, conditioned on absorption,

```math
\boxed{
p(y|{\rm abs})
=\frac{e^{-y}}{1-e^{-\tau_\gamma}}.
}
```

Finite optical depth smooths the sharp earliest-generation limit.

### S3 — photoelectron excess-energy partition
**Status:** DERIVED / CONDITIONAL

```math
\boxed{
\varepsilon_{\rm gen}
=\xi_e[E_\gamma-E_g(x)].
}
```

The symmetric two-band transition gives `xi_e=1/2`. The simplified flat-heavy-hole HgCdTe Kane limit motivates `xi_e approximately 1` as a relevant limiting baseline. A real multiband value remains OPEN.

### S4 — corrected finite-relaxation exit energy
**Status:** DERIVED / CONDITIONAL

Define `delta E=E_gamma-E_g,out` and `K=G ell_E`. For local photon excess `u`,

```math
\boxed{
\varepsilon_{\rm out}(u)
=K+(\xi_eu-K)
\exp[-(\delta E-u)/K].
}
```

The maximum over generation position occurs at an endpoint.

### S5 — ballistic timing kernel
**Status:** DERIVED / CHECKED / CONDITIONAL

The nonzero-initial-energy Kane timing kernel is retained as a ballistic special case. Its entrance-gap maximum is **not** universal after the momentum-scattering audit.

### S6 — exact drift-diffusion first-passage result
**Status:** DERIVED / CONDITIONAL; standard first-passage physics, no novelty claim

For

```math
dX=v_d dt+\sqrt{2D}\,dW_t,
```

and remaining distance `d`,

```math
\boxed{
\langle T|d\rangle=d/v_d,
}
```

```math
\boxed{
\operatorname{Var}(T|d)=2Dd/v_d^3.
}
```

For random generation distance `D_g`,

```math
\boxed{
\langle T\rangle=\langle D_g\rangle/v_d,
}
```

```math
\boxed{
\operatorname{Var}(T)
=\frac{2D\langle D_g\rangle}{v_d^3}
+\frac{\operatorname{Var}(D_g)}{v_d^2}.
}
```

Thus optical generation-position jitter and momentum-scattering/diffusion jitter separate explicitly in this limit.

### S7 — entrance-gap initial-condition switch
**Status:** DERIVED / CONDITIONAL ON THE SHARP HIGH-OPTICAL-DEPTH GEOMETRY; current strongest transport-independent spectral statement

Define

```math
\boxed{
\nu_g(E_\gamma)
=\max(0,E_\gamma-E_{g,\rm in}).
}
```

Then

```math
\frac{dx_g}{dE_\gamma}
=\begin{cases}
-1/G,&E_\gamma<E_{g,\rm in},\\
0,&E_\gamma>E_{g,\rm in},
\end{cases}
```

while

```math
\frac{d\nu_g}{dE_\gamma}
=\begin{cases}
0,&E_\gamma<E_{g,\rm in},\\
1,&E_\gamma>E_{g,\rm in}.
\end{cases}
```

For a timing functional `T=F(x_g,epsilon_g,...)`,

```math
\boxed{
\frac{dT}{dE_\gamma}
=-\frac1G F_x
\quad(E_\gamma<E_{g,\rm in}),
}
```

and

```math
\boxed{
\frac{dT}{dE_\gamma}
=\xi_eF_\varepsilon
\quad(E_\gamma>E_{g,\rm in}).
}
```

The **physical sensitivity channel changes** at `E_gamma=E_g,in`.

A visible cusp is not guaranteed because finite optical depth smooths the switch and the two transport sensitivities can match accidentally.

### S8 — post-crossover shape is transport-model dependent
**Status:** CHECKED across multiple deliberately simplified transport limits

The current model hierarchy gives

```text
forward ballistic memory
-> rise -> maximum -> decline

strong momentum randomization / constant drift
-> rise -> plateau

symmetric hot initial longitudinal distribution with finite memory
-> decline is not guaranteed; mean delay/variance can remain flat or rise.
```

Therefore the experiment should target an **entrance-gap spectral crossover**, with the post-crossover shape used to diagnose momentum/energy relaxation.

---

## 8. Established external ingredients — do not claim novelty

Known prior physics includes

- graded HgCdTe devices and spectral response;
- grading-induced carrier drift / faster response;
- microscopic HgCdTe scattering and Monte Carlo transport;
- hydrodynamic HgCdTe transport validated against Monte Carlo;
- tunable-pulse HgCdTe timing measurements;
- WKB, Kane, Poisson, drift-diffusion and semiconductor first-passage physics.

The focused search has not found an inspected primary HgCdTe source explicitly organizing wavelength-resolved timing around the entrance-gap switch from generation-position sensitivity to injected-state sensitivity.

Negative search is not novelty evidence.

---

## 9. Current open questions

### O1 — calibrated 77 K momentum and energy relaxation
Need defensible `nu_v(E,x)` / `tau_m(E,x)` and `nu_epsilon(E,x)` / `ell_E(E,x)` for the target composition.

### O2 — stochastic impact ionization
Need calibrated `Gamma_II(E,x)` before mean-energy thresholds become probability/gain/noise predictions.

### O3 — multiband optical excitation
Need `xi_e(E_gamma,x)` and angular/momentum distribution of the generated electron ensemble.

### O4 — calibrated absorption profile
Need an implementable primary-source `alpha(E_gamma,x,T)` to predict the spectral width of the crossover.

### O5 — wavelength-resolved timing data
Need fixed-bias/fixed-readout tunable-wavelength impulse or group-delay data for a known graded HgCdTe profile.

### O6 — publication significance
Continue research. Do not open a manuscript yet. The current entrance-gap switch is more robust than the earlier ballistic peak but still needs calibrated transport or experimental collision.

---

## 10. Explicit non-claims

The project does **not** presently claim

- a universal photodetector sensitivity-speed theorem;
- a universal active-volume bound;
- that grading eliminates all tunneling;
- that a mean-energy threshold is a true stochastic II onset;
- a calibrated HgCdTe 77 K speed/dark-current limit;
- a universal value of `xi_e`;
- a universal timing maximum at the entrance-gap wavelength;
- that a visible cusp must occur;
- novelty or priority for the entrance-gap timing crossover;
- manuscript readiness.
