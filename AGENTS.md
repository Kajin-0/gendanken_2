# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gendanken_2`  
**Active experiment:** `experiments/01-vanishing-absorber/`  
**Current mode:** **open theoretical exploration; active frontier is graded HgCdTe carrier drive versus nonlocal hot-electron physics plus boundary TAT/BTBT; no novelty claim**

Read this file first.

The project follows the physics rather than a predetermined theorem. Counterexamples and prior-art collisions are progress. Do not force the work back toward the original active-volume idea or prematurely toward a manuscript.

---

## 1. Mandatory repository protocol

Before every write:

1. fetch live `main` / current target;
2. inspect intervening changes when needed;
3. fetch the exact current blob SHA immediately before replacing a file;
4. never overwrite a stale SHA;
5. preserve failed/corrected branches;
6. make narrow edits where practical.

**Live `main` overrides all snapshots and recovery notes.**

---

## 2. Mandatory epistemic labels

Use explicitly:

- **KNOWN**
- **DERIVED**
- **CHECKED**
- **CONDITIONAL**
- **CANDIDATE DISTINCT — PRIORITY UNPROVEN**
- **INVALIDATED**
- **SUPERSEDED**
- **OPEN**
- **NON-CLAIM**

A negative literature search is not novelty evidence.

Do not use `first`, `new fundamental`, `universal`, etc. without a focused primary-source audit and `CLAIM_LEDGER.md` update.

---

## 3. Current path

```text
active-volume thought experiment
-> volume bound killed by field concentration

finite absorber / LDOS / ultrastrong coupling
-> successive microscopic loopholes

finite passive network
-> harmonic two-access transfer-area theorem

active/adaptive/time-dependent control
-> pump, timing, storage, output-record resources
-> unrestricted output continuum kills universal finite detector-only capacity

semiconductor contact / energy filters
-> detailed balance, lifetime broadening, multipole delay

HgCdTe field-driven collection
-> normalized direct BTBT
-> low-field mobility shortcut killed by high-field transport

TAT / nonlocal II
-> defect-mediated leakage and carrier energy history matter

homogeneous field shaping
-> cannot beat local speed/WKB leakage trade under stated model

heterostructure allocation
-> put field where marginal leakage cost is lowest

bandgap grading
-> direct-Zener geometry can be suppressed at fixed conduction drive

self-consistent quasi-neutral p-type grading
-> majority-hole band can be nearly pinned
-> gap slope becomes minority-electron drive

collection boundary
-> unavoidable barrier-canceling voltage must be carried by finite field
-> local TAT/BTBT voltage capacity

CURRENT FRONTIER
-> grading does not remove hot-electron energy input
-> exact graded mean-energy II phase boundary
-> minimally compensated wide-gap boundary acts as relaxation region.
```

---

## 4. Canonical reading order

1. `AGENTS.md`
2. `README.md`
3. `experiments/01-vanishing-absorber/CURRENT_STATE.md`
4. `experiments/01-vanishing-absorber/CLAIM_LEDGER.md`
5. `experiments/01-vanishing-absorber/HGCDTE_GRADED_NONLOCAL_II_PHASE_BOUNDARY.md`
6. `experiments/01-vanishing-absorber/HGCDTE_GRADED_ABSORBER_BOUNDARY_RELAXATION.md`
7. `experiments/01-vanishing-absorber/HGCDTE_QUASINEUTRAL_GRADING_SELF_CONSISTENCY.md`
8. `experiments/01-vanishing-absorber/HGCDTE_LINEAR_GRADED_KANE_WKB.md`
9. `experiments/01-vanishing-absorber/HGCDTE_BOUNDARY_LAYER_TAT_TRADEOFF.md`
10. `experiments/01-vanishing-absorber/HGCDTE_TAT_TOLERANCE_FIELD_ALLOCATION.md`
11. `experiments/01-vanishing-absorber/HGCDTE_ELECTROSTATIC_COMPENSATION_PEAK_FIELD_BOUND.md`
12. `experiments/01-vanishing-absorber/HGCDTE_NONLOCAL_IONIZATION_SURROGATE.md`
13. `experiments/01-vanishing-absorber/RESEARCH_LOG.md`
14. `experiments/01-vanishing-absorber/ARCHIVE_STATUS.md`

There is still **no manuscript**.

---

## 5. Strongest graded direct-Zener result

Define

```math
S_c=-dE_c/dx,
\qquad
S_v=-dE_v/dx,
\qquad
G=-dE_g/dx.
```

Because `E_g=E_c-E_v`,

```math
\boxed{S_v=S_c-G.}
```

At fixed useful conduction slope `S_c=S`, define

```math
\delta=G/S.
```

For the linear two-band/Kane two-turning-point model,

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

The action increases monotonically and diverges as `delta -> 1-`.

**Interpretation:** a gap gradient can provide conduction-band drive while removing the relative conduction/valence tilt that creates the ordinary direct-Zener overlap.

This is conditional and does not eliminate TAT, interface tunneling, or hot-carrier processes.

---

## 6. Self-consistent quasi-neutral p-type result

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

Therefore for a decreasing gap,

```math
\boxed{S_c\approx G.}
```

So the favorable direct-Zener geometry can emerge naturally from quasi-neutral equilibrium rather than requiring an artificial cancellation.

---

## 7. New nonlocal carrier-energy theorem

Do not compute hot-electron energy from electrostatic field alone in a graded semiconductor.

Use the total conduction-band slope:

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

Thus grading can suppress direct Zener without removing hot-electron energy input.

For a linear quasi-neutral graded absorber

```math
E_g=E_{g0}-Gx,
\qquad
S_c=G,
```

constant `ell_E`, and threshold model

```math
E_{\rm th}=\chi E_g,
```

define

```math
\zeta=\Delta E_g/E_{g0},
\qquad
r=L/\ell_E.
```

Then the exact mean-energy threshold boundary is

```math
\boxed{
\zeta_{\rm II}(r,\chi)
=
\frac{\chi}
{\chi+(1-e^{-r})/r}.
}
```

Mean threshold access occurs for

```math
\boxed{\zeta\ge\zeta_{\rm II}.}
```

Ballistic limit:

```math
\boxed{
\zeta_{\rm II}\to\frac{\chi}{1+\chi}.
}
```

For `chi=1`, this is `1/2`.

This is a deterministic mean-energy boundary, not a zero-probability stochastic II theorem.

---

## 8. Collection-boundary local tunneling resource

For a wider-gap boundary with material gap increase `Delta Eg_b` and conduction-band share `alpha`, barrier-free electron extraction requires

```math
\boxed{qV_b\ge\alpha\Delta E_g^{(b)}.}
```

Any nonnegative field over width `w` obeys

```math
\boxed{F_{\max}\ge V_b/w.}
```

For local inverse-field tunneling mechanisms `m` with characteristic fields `F_m(x)` and required exponent margins `Sigma_m`, define

```math
\boxed{
F_{\rm allow}(x)
=\min_m\frac{F_m(x)}{\Sigma_m}.
}
```

Then the voltage is feasible under those local constraints iff

```math
\boxed{
V_b\le\int_0^wF_{\rm allow}(x)dx.
}
```

Use this for TAT and direct BTBT when their local WKB forms are valid.

**Do not insert nonlocal II into this local envelope** unless a local-equilibrium reduction has been justified.

---

## 9. Minimum-compensation boundary relaxation result

At

```math
\boxed{qV_b=\alpha\Delta E_g^{(b)},}
```

the net conduction-edge change is

```math
\boxed{\Delta E_c^{(b)}=0.}
```

The boundary adds no downhill conduction-band work.

Therefore

```math
\boxed{
\varepsilon_b(s)
=\varepsilon_a e^{-s/\ell_{E,b}},
}
```

while the local gap and approximate II threshold rise.

Hence if the electron enters below mean threshold, a monotonic minimally compensated wider-gap boundary cannot create a new mean-threshold crossing within the stated model.

Overcompensation restores boundary acceleration but spends extra local field and hot-electron resource.

---

## 10. Current physical interpretation

The active architecture now has a clean division of labor:

```text
quasi-neutral graded absorber
-> band-structure drive
-> direct-Zener suppression
-> nonlocal hot-electron constraint

wide-gap collection boundary
-> unavoidable electrostatic voltage
-> field placed in high-gap / low-defect material
-> local TAT/BTBT constraint
-> relaxation region at minimum compensation.
```

This is the current frontier.

---

## 11. Important stopped shortcuts

Do not restart casually:

- active-volume-only theorem;
- finite absorber count as one-photon speed limit;
- largest internal coupling as universal parameter;
- finite internal rank as always-on detector capacity;
- universal active `pump ~ W^2` law;
- spectral FWHM as transport speed in arbitrary filters;
- low-field mobility extrapolated into high-field HgCdTe;
- direct BTBT assumed first high-field limiter;
- bulk II onset treated as a finite-device threshold;
- nonuniform field alone assumed beneficial in homogeneous material;
- pure grading assumed to eliminate all tunneling;
- delta doping assumed to eliminate compensation field;
- local `F_II(x)` used without a local-equilibrium justification.

---

## 12. Current missing inputs

Need target-composition data for

```text
ell_E(E,x) / energy-loss rate
+
Gamma_II(E,x)
+
boundary trap energies, densities and capture cross sections
+
finite self-consistent band profile under doping and bias
+
high-field velocity law for transit time.
```

Do not invent interpolation coefficients from narrative literature statements.

---

## 13. Current numerical regressions

Relevant checks include

```text
numerics/hgcdte_graded_nonlocal_ii_phase_boundary.py
numerics/hgcdte_graded_kane_wkb.py
numerics/hgcdte_field_profile_variational.py
numerics/hgcdte_relaxation_length_phase_boundary.py
numerics/hgcdte_nonlocal_ii_surrogate.py
numerics/hgcdte_impact_dead_space.py
numerics/hgcdte_btbt_normalized_sweep.py
```

No CI is justified yet.

---

## 14. Next decisive work

Do **not** jump to a manuscript.

Build a finite graded-absorber + collection-boundary phase map with three simultaneous outputs:

```text
transit time
+
local TAT/BTBT margin
+
nonlocal carrier-energy / II margin.
```

Sweep `ell_E` parametrically until trustworthy target-composition transport data are available.

Then attack the result with

- non-linear composition profiles;
- realistic `N_A(x)` / `N_v(x)` variation;
- boundary overcompensation;
- measured trap spectra;
- stochastic II tails;
- interface states;
- self-consistent bias-dependent electrostatics.

Only after that should publication significance be reassessed.
