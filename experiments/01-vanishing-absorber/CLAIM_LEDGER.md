# Claim Ledger — Experiment 01

**Updated:** 2026-08-09  
**Status:** exploratory; active frontier is graded HgCdTe carrier drive versus nonlocal hot-electron physics plus boundary TAT/BTBT; no novelty claim

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

Ideal field concentration permits finite optical participation while active material volume tends to zero. Do not revive a universal `eta^2 B <= C V` law without new constraints.

### H2 — finite absorber count as the missing one-photon speed limit

**Status:** INVALIDATED

The one-photon / one-excitation sector remains linear.

### H3 — largest internal coupling as universal multimode control parameter

**Status:** INVALIDATED

Spectator strongly coupled sectors are counterexamples.

### H4 — finite coherent storage rank as universal always-on detector capacity

**Status:** INVALIDATED

Adaptive branching and unrestricted output continua can export the missing distinguishability.

### H5 — local Landauer erasure as a universal detector-event cost

**Status:** INVALIDATED

The useful output can itself carry the record information.

### H6 — spectral FWHM as architecture-independent carrier speed

**Status:** INVALIDATED

Multipole filters can keep spectral width fixed while increasing delay/storage-state weight.

### H7 — low-field mobility extrapolated to high-field HgCdTe

**Status:** INVALIDATED SHORTCUT

Primary high-field HgCdTe transport is non-ohmic; velocity need not increase monotonically with field.

### H8 — direct BTBT must be the first HgCdTe high-field limiter

**Status:** INVALIDATED SHORTCUT

TAT and nonlocal impact-ionization/hot-electron physics can intervene earlier depending on defect spectrum, geometry, and energy relaxation.

### H9 — nonuniform electric field alone improves homogeneous local WKB leakage at fixed transit time

**Status:** INVALIDATED in the stated homogeneous local model

Uniform field is the leakage-minimizing profile under the derived assumptions. Heterogeneity in material/defect/transport parameters is required for a genuine allocation benefit.

### H10 — local `F_II(x)` can always be inserted into a tunneling tolerance envelope

**Status:** INVALIDATED GENERALIZATION

In the thin/fast regime, impact ionization is history dependent. Use a nonlocal carrier-energy state unless local equilibration has been justified.

---

## 2. Important supporting results from earlier abstract branches

### P1 — finite passive-network harmonic transfer-area bound

**Status:** DERIVED / CHECKED; mathematical ingredients established prior theory; novelty not claimed

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

The band-averaged corollary is

```math
\boxed{
\overline T_B
\le
\frac{4\pi LR}{W(L+R)}.
}
```

This is retained as an external-access resource law, not an absolute detector bandwidth theorem.

### P2 — fixed-target Hopfield access collapse

**Status:** CANDIDATE DISTINCT supporting lemma; priority unproven

For the stated fixed-target two-mode Hopfield model with fixed local bath resources and `g -> infinity`,

```math
\boxed{
\min(\Gamma_L,\Gamma_R)\to0.
}
```

Deep-strong decoupling itself is established prior physics.

### P3 — active finite-mode conversion resource

**Status:** DERIVED bookkeeping result built on established Schmidt/singular-mode conversion theory

```math
\boxed{
N_p
\ge
\frac{M_c\arcsin^2\sqrt\eta}
{\Lambda\tau^2}.
}
```

`Lambda` remains an unbounded device/material resource in that abstraction.

These results are supporting provenance, not the current HgCdTe frontier.

---

## 3. HgCdTe graded direct-Zener results

### G1 — exact linear graded-Kane WKB action

**Status:** DERIVED / CHECKED / CONDITIONAL

For linear edges

```math
E_c=E_{c0}-S_cx,
\qquad
E_v=E_{v0}-S_vx,
```

```math
\boxed{
\mathcal S(E)
=\frac{\pi\sqrt{S_cS_v}}
{4\hbar v_K}(x_c-x_v)^2.
}
```

The constant-gap common-field limit recovers the simplified Kane/Zener exponent.

### G2 — band-offset-partition invariant geometry

**Status:** DERIVED

Define

```math
G=-dE_g/dx,
\quad
S_c=-dE_c/dx,
\quad
S_v=-dE_v/dx.
```

Then identically

```math
\boxed{S_v=S_c-G.}
```

The relative conduction/valence geometry does not depend on the bare band-offset partition parameter.

### G3 — fixed-conduction-slope Zener action ratio

**Status:** DERIVED / CHECKED / CONDITIONAL; exact formula priority unassessed

At fixed `S_c=S`, define

```math
\delta=G/S.
```

For the linear two-turning-point model,

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

The ratio increases monotonically and diverges as `delta -> 1-`.

This concerns one direct-Zener path only.

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

For nearly constant `N_A/N_v`,

```math
\boxed{E_v\approx\text{constant}.}
```

Hence with decreasing gap

```math
\boxed{S_c\approx G.}
```

This naturally approaches the favorable `delta -> 1` direct-Zener geometry for minority-electron collection.

### Q2 — uniformly depleted multi-micron grading is not the default physical picture

**Status:** CONDITIONAL design conclusion

Uniform uncompensated charge gives a Poisson correction scaling as `N_eff L^2`, which becomes severe rapidly with length. The current physical model is therefore

```text
quasi-neutral graded interior
+
short screening/depletion/boundary regions.
```

---

## 5. Collection-boundary electrostatic results

### B1 — barrier-free compensation voltage

**Status:** DERIVED

For a local gap increase `Delta Eg_b` with conduction-band share `alpha`, barrier-free electron extraction requires

```math
\boxed{
qV_b\ge\alpha\Delta E_g^{(b)}.
}
```

At equality the net conduction-edge step is zero.

### B2 — peak-field lower bound

**Status:** DERIVED

For any nonnegative one-dimensional compensating field over width `w`,

```math
\boxed{F_{\max}\ge V_b/w.}
```

Delta doping or depletion shaping can redistribute field but cannot lower the peak below this integral bound at fixed positive voltage and width.

### B3 — local tunneling voltage capacity

**Status:** DERIVED / CONDITIONAL

For local inverse-field mechanisms `m` with characteristic fields `F_m(x)` and required exponent margins `Sigma_m`, define

```math
\boxed{
F_{\rm allow}(x)
=\min_m\frac{F_m(x)}{\Sigma_m}.
}
```

Then the compensation voltage is feasible under those local constraints iff

```math
\boxed{
V_b\le\int_0^wF_{\rm allow}(x)dx.
}
```

At minimum barrier-free compensation,

```math
\boxed{
\frac{\alpha\Delta E_g^{(b)}}{q}
\le
\int_0^wF_{\rm allow}(x)dx.
}
```

In the current model, TAT and direct BTBT belong in this local envelope; nonlocal II generally does not.

### B4 — maximin field allocation

**Status:** DERIVED

For one local exponent scale `F_T(x)`, the field profile maximizing the worst local exponent is

```math
\boxed{
F_{\rm opt}(x)
=\frac{V_bF_T(x)}
{\int F_Tdx}.
}
```

Thus the optimum equalizes normalized tunneling stress.

---

## 6. New graded nonlocal carrier-energy results

### N1 — general graded-band mean-energy state

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
\int_0^x
S_c(s)
\exp\!\left[-\int_s^x\frac{du}{\ell_E(u)}\right]ds.
}
```

This makes impact-ionization access a path-dependent state constraint in the thin/fast regime.

### N2 — linear graded absorber phase boundary

**Status:** DERIVED / CHECKED / CONDITIONAL; exact formula priority unassessed

For

```math
E_v\approx\text{constant},
```

```math
E_g(x)=E_{g0}-Gx,
```

constant `ell_E`, and threshold surrogate

```math
E_{\rm th}(x)=\chi E_g(x),
```

define

```math
\zeta=\Delta E_g/E_{g0},
\qquad
r=L/\ell_E.
```

Then mean threshold access occurs when

```math
\boxed{
\zeta
\ge
\zeta_{\rm II}(r,\chi)
=
\frac{\chi}
{\chi+(1-e^{-r})/r}.
}
```

In the ballistic limit,

```math
\boxed{
\zeta_{\rm II}	o\frac{\chi}{1+\chi}.
}
```

For `chi=1`, the threshold is reached after a one-half fractional entrance-gap drop.

This is a mean-energy threshold, not a true stochastic zero-probability boundary.

### N3 — minimum-compensation wider-gap boundary cannot create a new mean crossing

**Status:** DERIVED / CONDITIONAL

At

```math
qV_b=\alpha\Delta E_g^{(b)},
```

```math
\Delta E_c^{(b)}=0.
```

Therefore the boundary mean energy relaxes as

```math
\boxed{
\varepsilon_b(s)
=\varepsilon_a e^{-s/\ell_{E,b}},
}
```

while the wider local gap makes the threshold increase.

If

```math
\varepsilon_a<\chi E_{g,a},
```

then

```math
\boxed{
\varepsilon_b(s)<\chi E_g(s)
}
```

throughout the monotonic wider-gap boundary in this model.

Overcompensation restores a downhill conduction slope and therefore adds both field stress and hot-electron drive.

---

## 7. Established external ingredients — do not claim novelty

Known prior physics includes

- graded-gap and graded-composition HgCdTe detectors;
- composition-induced built-in/quasi-electric fields;
- HgCdTe heterojunction and unipolar-barrier band engineering;
- TAT, direct BTBT, SRH/Auger leakage and interface traps;
- electron-dominated HgCdTe impact ionization and dead-space effects;
- energy-dependent Monte Carlo treatment of HgCdTe e-APDs;
- carrier-relaxation/collection regions in graded HgCdTe APD designs;
- standard WKB, Kane, Poisson, detailed-balance, and semiconductor transport theory.

---

## 8. Current open questions

### O1 — target-composition energy relaxation

**Status:** OPEN

Need defensible `ell_E(E,x)` or equivalent energy-loss data for the target narrow-gap HgCdTe composition near 77 K.

### O2 — target-composition energy-dependent II probability

**Status:** OPEN

Need calibrated `Gamma_II(E,x)` for the same material regime before turning the mean-energy phase boundary into a probability/gain/noise prediction.

### O3 — boundary trap spectrum and prefactors

**Status:** OPEN

Measured/fitted trap energies exist, but actual local `N_t`, occupation, capture cross sections, and interface-state densities for the intended graded boundary determine whether TAT current is acceptable.

### O4 — finite self-consistent device profile

**Status:** OPEN

Need one finite `E_g(x), E_c(x), E_v(x)` profile under doping and bias, not only local analytic segments.

### O5 — publication significance

**Status:** OPEN

Do not open a manuscript yet. The exact graded WKB and nonlocal phase-boundary reductions are interesting but require broader prior-art collision and a realistic phase map before a defensible headline claim can be stated.

---

## 9. Explicit non-claims

The project does **not** presently claim

- a universal photodetector sensitivity-speed theorem;
- a universal active-volume bound;
- that grading eliminates all tunneling;
- that a mean-energy threshold is a true stochastic II onset;
- that TAT can be predicted from exponent alone;
- that the current HgCdTe architecture is new;
- a calibrated HgCdTe 77 K speed/dark-current limit;
- novelty or priority for the exact graded-WKB or graded-II phase-boundary formulas;
- manuscript readiness.
