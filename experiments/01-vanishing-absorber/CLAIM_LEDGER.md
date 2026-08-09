# Claim Ledger — Experiment 01

**Updated:** 2026-08-09  
**Status:** exploratory; active frontier is wavelength-resolved generation and carrier timing in graded HgCdTe, with corrected photoexcitation energy partition; no novelty claim

This file is the epistemic boundary. `RESEARCH_LOG.md` preserves chronology; specialized derivation files preserve detailed assumptions and proofs.

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

## 1. Permanent invalidations / stopped universal routes

### H1 — active-volume-only universal detector limit

**Status:** INVALIDATED

Ideal field concentration permits finite optical participation while active material volume tends to zero.

### H2 — finite absorber count as one-photon speed limit

**Status:** INVALIDATED

The one-photon / one-excitation sector remains linear.

### H3 — largest internal coupling as universal multimode parameter

**Status:** INVALIDATED

Spectator strongly coupled sectors are counterexamples.

### H4 — finite internal storage rank as universal always-on capacity

**Status:** INVALIDATED

Adaptive branching and output continua export the missing distinguishability.

### H5 — local Landauer erasure as universal detector-event cost

**Status:** INVALIDATED

The useful output can carry the record information.

### H6 — spectral FWHM as architecture-independent carrier speed

**Status:** INVALIDATED

Multipole filters can retain spectral width while increasing delay/state weight.

### H7 — low-field mobility extrapolated into high-field HgCdTe

**Status:** INVALIDATED SHORTCUT

High-field HgCdTe transport is non-ohmic and velocity need not increase monotonically with field.

### H8 — direct BTBT must be the first HgCdTe high-field limiter

**Status:** INVALIDATED SHORTCUT

TAT and nonlocal hot-electron / impact-ionization physics can intervene earlier.

### H9 — nonuniform field alone improves homogeneous local WKB leakage at fixed transit time

**Status:** INVALIDATED in the stated homogeneous local model

Uniform field is optimal under the derived assumptions; heterogeneity is needed for a true allocation benefit.

### H10 — local `F_II(x)` can always be inserted into a tunneling tolerance envelope

**Status:** INVALIDATED GENERALIZATION

Thin/fast impact ionization is history dependent; carry a nonlocal carrier-energy state unless local equilibration has been justified.

### H11 — every downstream photoelectron may be treated as cold at the local conduction edge

**Status:** INVALIDATED

For `E_gamma > E_g(x)`, direct photoexcitation gives nonzero initial carrier excess energy. Wavelength-resolved hot-electron and transit calculations must include photon-excess partition.

---

## 2. Important supporting results from earlier abstract branches

### P1 — finite passive-network harmonic transfer-area bound

**Status:** DERIVED / CHECKED; mathematical ingredients are established prior theory; novelty not claimed

For a finite stable passive strictly proper network,

```math
L=\operatorname{Tr}\Gamma_L,
\qquad
R=\operatorname{Tr}\Gamma_R,
```

```math
\boxed{
\mathcal I_{L\to R}
\le
\frac{2LR}{L+R}.
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

These remain provenance, not the current HgCdTe frontier.

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

At fixed `S_c=S`, `delta=G/S`,

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

The ratio diverges as `delta -> 1-` in the ideal two-turning-point model.

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

Nearly constant `N_A/N_v` gives

```math
\boxed{E_v\approx\text{constant},}
```

and therefore, for decreasing gap,

```math
\boxed{S_c\approx G.}
```

### Q2 — uniformly depleted multi-micron grading is not the default physical picture

**Status:** CONDITIONAL design conclusion

Uniform uncompensated charge gives a rapidly growing `N_eff L^2` Poisson burden. The active model is quasi-neutral graded interior plus short screening/boundary regions.

---

## 5. Collection-boundary electrostatic results

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

Use this for TAT and direct BTBT where the local WKB forms are valid; do not hide nonlocal II inside it.

### B4 — maximin field allocation

**Status:** DERIVED

For one local exponent scale,

```math
\boxed{
F_{\rm opt}(x)
=\frac{V_bF_T(x)}{\int F_Tdx}.
}
```

### B5 — minimum-compensation boundary relaxation

**Status:** DERIVED / CONDITIONAL

At

```math
qV_b=\alpha\Delta E_g^{(b)},
```

the boundary has `Delta E_c=0`; mean carrier energy relaxes while the local gap rises. A carrier entering below the deterministic mean-II threshold cannot acquire a new mean-threshold crossing in the monotonic boundary under the current model.

---

## 6. Graded nonlocal carrier-energy results

### N1 — general path-dependent mean-energy state

**Status:** DERIVED / CONDITIONAL

```math
\boxed{
\frac{d\varepsilon}{dx}
=S_c(x)-\frac{\varepsilon}{\ell_E(x)}.
}
```

For cold injection,

```math
\boxed{
\varepsilon(x)
=
\int_0^xS_c(s)
\exp\!\left[-\int_s^x\frac{du}{\ell_E(u)}\right]ds.
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
=\frac1a+W_0\!\left[-\frac1a e^{-1/a}\right].
}
```

and

```math
\boxed{L\ge\ell_Er_{\min}.}
```

### N4 — conditional total boundary/absorber transit floor

**Status:** DERIVED / CONDITIONAL

The absorber relaxation length, boundary cooling length, and local tunneling-width requirements combine through a maximum/sum construction in `HGCDTE_BOUNDARY_COOLING_TRANSIT_FLOOR.md`.

This is a best-case kinematic lower bound, not a calibrated response time.

---

## 7. Wavelength-resolved graded photodetection results

### S1 — wavelength sets earliest generation position and maximum remaining distance

**Status:** DERIVED / CONDITIONAL ON LOCAL-GAP ABSORPTION

For a linear graded gap and

```math
E_{g,\rm out}<E_\gamma<E_{g,\rm in},
```

```math
\boxed{
x_\gamma
=\frac{E_{g,\rm in}-E_\gamma}{G},
}
```

```math
\boxed{
d_\gamma
=\frac{E_\gamma-E_{g,\rm out}}{G}.}
```

Thus near-cutoff photons are energetically eligible only near the narrow-gap collection side.

### S2 — exact conditional optical-depth generation distribution

**Status:** KNOWN probability consequence / DERIVED application

For total eligible optical depth `tau_gamma`, conditioned on absorption,

```math
\boxed{
p(y|{\rm abs})
=\frac{e^{-y}}{1-e^{-\tau_\gamma}},
\qquad 0<y<\tau_\gamma.
}
```

For the illustrative local law `alpha=C(E_gamma-E_g)^beta` in a linear gradient, this maps exactly to a generation-position / remaining-distance distribution.

### S3 — downstream photoexcitation energy partition

**Status:** DERIVED / CONDITIONAL

Let `u=E_gamma-E_g(x)` be local photon excess and let the electron receive fraction `xi_e`:

```math
\boxed{\varepsilon_{\rm gen}=\xi_eu.}
```

The symmetric two-band Kane optical transition gives

```math
\boxed{\xi_e=1/2.}
```

Real HgCdTe `xi_e` is OPEN and requires a multiband optical-transition calculation.

### S4 — corrected mean exit energy

**Status:** DERIVED / CONDITIONAL

For constant gradient and relaxation length,

```math
\boxed{
\varepsilon_{\rm out}(u)
=
\xi_eu e^{-(\delta E-u)/(G\ell_E)}
+
G\ell_E
\left[1-e^{-(\delta E-u)/(G\ell_E)}\right].
}
```

Ballistic limit:

```math
\boxed{
\varepsilon_{\rm out}^{\rm bal}(u)
=\delta E-(1-\xi_e)u.
}
```

The earlier cold-downstream-generation formula is superseded.

### S5 — all-position ballistic wavelength safety criterion

**Status:** DERIVED / CONDITIONAL

The earliest allowed generation point remains the worst ballistic case, so

```math
\boxed{
\delta E<\chi E_{g,\rm out}
}
```

is sufficient for all generation positions to remain below the deterministic output mean threshold.

### S6 — exact ballistic timing kernel with nonzero initial energy

**Status:** DERIVED / CHECKED / CONDITIONAL

With `q=u/delta E`, `s=delta E/E_g,out`, and energy partition `xi_e`, the corrected dimensionless transit kernel is

```math
\boxed{
\theta(q;s,\xi_e)
=\phi(z_0^*,e)-\phi(z_s^*,e),
}
```

with

```math
\phi(z,e)=\sqrt{ez}+z^{3/2}/(3\sqrt e),
```

```math
e=1+s[1-(1-\xi_e)q],
```

```math
z_s^*=\xi_esq,
```

```math
z_0^*=s[1-(1-\xi_e)q].
```

### S7 — optically thick wavelength-delay asymptote

**Status:** DERIVED / CHECKED / CONDITIONAL; candidate underexplored connection, priority unproven

As optical depth tends large, generation concentrates at the earliest allowed point, so the delay becomes independent of `xi_e`:

```math
\boxed{
\theta_\infty(s)
=
\frac{\sqrt s}{\sqrt{1+s}}
\left(1+\frac43s\right).
}
```

Thus

```math
\boxed{
T_\infty(\lambda)
=\frac{E_{g,\rm out}}{Gv_K}
\theta_\infty(\lambda_c/\lambda-1).
}
```

Near cutoff,

```math
\boxed{T_\infty\propto\sqrt{\lambda_c-\lambda}}
```

inside the current idealized model.

A focused primary-source search found grading→speed and grading→spectral response separately, but not this exact wavelength→generation-position→timing analytic map. Negative search is not priority evidence.

### S8 — timing spread versus optical depth

**Status:** CHECKED NUMERICALLY / CONDITIONAL

Generation-position timing spread is not generally monotonic with optical depth. It may rise slightly from very thin to moderate optical depth before tending to zero in the optically thick limit.

Do not claim a universal `higher QE -> lower jitter` relation.

---

## 8. Established external ingredients — do not claim novelty

Known prior physics includes

- graded-gap and graded-composition HgCdTe detectors;
- composition-induced built-in/quasi-electric fields;
- grading-induced reduction of diffusion / faster HgCdTe response;
- spectral-response modeling of compositionally graded HgCdTe;
- tunable-pulse HgCdTe impulse-response measurements;
- HgCdTe heterojunction/barrier engineering;
- TAT, direct BTBT, SRH/Auger leakage and interface traps;
- electron-dominated HgCdTe impact ionization and dead-space effects;
- energy-dependent Monte Carlo treatment of HgCdTe e-APDs;
- standard direct interband transition kinematics, WKB, Kane, Poisson, and semiconductor transport theory.

---

## 9. Current open questions

### O1 — target-composition energy relaxation

Need defensible `ell_E(E,x)` or equivalent energy-loss data near the target HgCdTe composition and temperature.

### O2 — target-composition stochastic impact ionization

Need calibrated `Gamma_II(E,x)` before mean-threshold access becomes an actual probability/gain/noise prediction.

### O3 — HgCdTe optical excess-energy partition

Need a multiband optical-transition model for `xi_e(E_gamma,x)`; the symmetric `1/2` result is a model special case, not yet a material value.

### O4 — calibrated absorption coefficient

Need a primary-source implementable `alpha(E_gamma,x,T)` model for wavelength-resolved absolute QE and generation-position distributions.

### O5 — experimental wavelength-resolved timing collision

Need tunable-pulse data under fixed bias/readout, preferably with electronics de-embedded, to test the intrinsic `T(lambda)` trend.

### O6 — finite self-consistent device profile

Need one realistic `E_g(x), E_c(x), E_v(x)` profile under doping and bias.

### O7 — publication significance

Continue research. Do not open a manuscript yet. The wavelength-resolved graded timing map is more detector-specific and testable than the earlier abstract branches, but still requires material calibration or experimental collision.

---

## 10. Explicit non-claims

The project does **not** presently claim

- a universal photodetector sensitivity-speed theorem;
- a universal active-volume bound;
- that grading eliminates all tunneling;
- that a mean-energy threshold is a stochastic II onset;
- that TAT follows from exponent alone;
- that the current HgCdTe architecture is new;
- a calibrated 77 K HgCdTe speed/dark-current limit;
- `xi_e=1/2` as a real HgCdTe material constant;
- a universal monotonic QE-jitter law;
- novelty or priority for the spectral timing relation;
- manuscript readiness.
