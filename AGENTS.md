# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gendanken_2`  
**Active experiment:** `experiments/01-vanishing-absorber/`  
**Current mode:** **open theoretical exploration; active frontier is self-consistent graded HgCdTe plus collection-boundary TAT/BTBT/defect allocation; no novelty claim**

Read this file first.

## 1. Repository discipline

Before every write:

1. fetch live `main` / current target;
2. inspect intervening changes when needed;
3. fetch exact current blob SHA before replacing a file;
4. never overwrite stale state;
5. preserve failed/corrected branches;
6. make narrow edits.

**Live `main` overrides all snapshots.**

## 2. Epistemic labels

Use explicitly:

- **KNOWN**
- **DERIVED**
- **CHECKED**
- **CONDITIONAL**
- **INVALIDATED**
- **OPEN**
- **NON-CLAIM**

A negative literature search is not novelty evidence.

Do not use `first`, `new fundamental`, `universal`, etc. without a focused primary-source audit and `CLAIM_LEDGER.md` update.

## 3. Current path

```text
active-volume thought experiment
-> volume bound killed by field concentration

finite absorber / LDOS / ultrastrong coupling
-> successive microscopic loopholes

finite passive network
-> harmonic two-access transfer-area theorem

active/adaptive/time-dependent control
-> pump, timing, storage and output-record resources

semiconductor contact / filters
-> detailed balance, lifetime broadening, delay

HgCdTe field-driven collection
-> normalized direct BTBT

bulk II onset
-> corrected by finite dead space / energy history

TAT
-> defect-mediated partial-gap tunneling can precede direct BTBT

homogeneous field shaping
-> cannot beat local speed–WKB leakage trade at fixed transit time

heterostructure allocation
-> field belongs where marginal leakage cost is smallest

bandgap grading
-> exact graded Kane WKB action; grading can suppress direct Zener overlap

self-consistent electrostatics
-> quasi-neutral p-type grading can pin the majority-hole band and leave gap slope as minority-electron drive

collection boundary
-> CURRENT FRONTIER: barrier-free extraction requires finite compensation voltage; unavoidable field must be placed in high-tolerance material while avoiding TAT/interface leakage.
```

## 4. Canonical reading order

1. `AGENTS.md`
2. `README.md`
3. `experiments/01-vanishing-absorber/CURRENT_STATE.md`
4. `experiments/01-vanishing-absorber/CLAIM_LEDGER.md`
5. `experiments/01-vanishing-absorber/HGCDTE_QUASINEUTRAL_GRADING_SELF_CONSISTENCY.md`
6. `experiments/01-vanishing-absorber/HGCDTE_GRADED_POISSON_ROBUSTNESS.md`
7. `experiments/01-vanishing-absorber/HGCDTE_LINEAR_GRADED_KANE_WKB.md`
8. `experiments/01-vanishing-absorber/HGCDTE_BOUNDARY_LAYER_TAT_TRADEOFF.md`
9. `experiments/01-vanishing-absorber/HGCDTE_ELECTROSTATIC_COMPENSATION_PEAK_FIELD_BOUND.md`
10. `experiments/01-vanishing-absorber/HGCDTE_TAT_TOLERANCE_FIELD_ALLOCATION.md`
11. `experiments/01-vanishing-absorber/HGCDTE_TAT_FIELD_SCALE.md`
12. `experiments/01-vanishing-absorber/HGCDTE_NONLOCAL_IONIZATION_SURROGATE.md`
13. `experiments/01-vanishing-absorber/RESEARCH_LOG.md`
14. `experiments/01-vanishing-absorber/ARCHIVE_STATUS.md`

There is still **no manuscript**.

## 5. Graded-Kane result retained

For the two-band/Kane model

```math
(E-U)^2=\Delta^2+(\hbar v_Kk)^2,
\qquad E_g=2\Delta,
```

and linear edges

```math
E_c=E_{c0}-S_cx,
\qquad
E_v=E_{v0}-S_vx,
```

the exact WKB action is

```math
\boxed{
\mathcal S(E)
=\frac{\pi\sqrt{S_cS_v}}
{4\hbar v_K}(x_c-x_v)^2.
}
```

At fixed useful conduction slope, the earlier symmetric grading parameter `eta` gave

```math
\frac{\mathcal S_Z(\eta)}{\mathcal S_Z(0)}
=\frac{(1-\eta)^2}{(1-2\eta)^{3/2}}.
```

The more physical partition-independent form is below.

## 6. Band-offset-invariant grading parameter

Define the local gap slope

```math
G=-dE_g/dx>0
```

and positive downhill slopes

```math
S_c=-dE_c/dx,
\qquad
S_v=-dE_v/dx.
```

Because `E_g=E_c-E_v`, identically

```math
\boxed{S_v=S_c-G.}
```

This relation is independent of how a composition-induced gap change is partitioned between conduction and valence bands.

At fixed `S_c=S`, define

```math
\boxed{\delta=G/S.}
```

Then for the linear two-turning-point model

```math
\boxed{
\frac{\mathcal S_Z(\delta)}{\mathcal S_Z(0)}
=\frac{(2-\delta)^2}
{4(1-\delta)^{3/2}},
\qquad 0\le\delta<1.
}
```

It increases monotonically and diverges as `delta -> 1-`.

For a finite linear region,

```math
\boxed{\delta=\Delta E_g/\Delta E_c.}
```

Thus the ideal direct-Zener geometric closure condition is

```math
\boxed{\Delta E_g\ge\Delta E_c.}
```

This does **not** eliminate TAT, interface tunneling, phonon-assisted processes, or boundary-layer electrostatics.

## 7. Quasi-neutral p-type self-consistency

For nondegenerate holes at equilibrium,

```math
p=N_v\exp[(E_v-E_F)/(k_BT)].
```

In a quasi-neutral p-type graded interior, `p approximately N_A`, so

```math
\boxed{
S_v
\simeq
-k_BT\frac{d}{dx}\ln(N_A/N_v).
}
```

Since

```math
S_c=S_v+G,
```

nearly constant `N_A/N_v` gives

```math
\boxed{
S_v\approx0,
\qquad
S_c\approx G,
\qquad
\delta\approx1.
}
```

Interpretation:

> equilibrium screening in a quasi-neutral p-type graded HgCdTe region can pin the majority-hole band while leaving the gap gradient as a minority-electron conduction-band drive.

This is conditional on quasi neutrality and the stated carrier statistics.

For n-type material the analogous equilibrium pinning acts primarily on the conduction band, naturally favoring minority-hole rather than minority-electron grading.

## 8. Poisson robustness

For a uniform uncompensated net charge `N_eff` across length `L`, a sufficient condition that the valence band never tilts downhill is

```math
\boxed{
\Delta E_g-\Delta E_c
\ge
\frac{q^2|N_{\rm eff}|L^2}{2\epsilon}.
}
```

The `N_eff L^2` scaling makes a uniformly depleted multi-micron narrow-gap graded region implausible at ordinary doping unless net charge is extremely small.

This is why the active physical picture is now

```text
quasi-neutral graded interior
+
short screening/depletion boundary layers.
```

## 9. Boundary band-alignment condition

Let a wider-gap collection transition increase the local gap by `Delta E_g > 0`, with conduction-band share `alpha`.

Before electrostatic compensation,

```math
\Delta E_c^{mat}=\alpha\Delta E_g.
```

Barrier-free minority-electron extraction requires

```math
\boxed{qV_b\ge\alpha\Delta E_g.}
```

At minimum compensation,

```math
\Delta E_c=0,
\qquad
\Delta E_v=-\Delta E_g.
```

Thus a wide-gap boundary can remain barrier free for electrons while increasing separation from the valence band.

This architecture is established prior HgCdTe heterojunction/barrier-detector physics; no novelty is claimed.

## 10. Peak-field bound: electrostatic shaping cannot erase the resource

For any one-sign field profile over boundary width `w`,

```math
V_b=\int_0^wF(x)dx.
```

Therefore

```math
\boxed{F_{\max}\ge V_b/w.}
```

With minimum barrier-free compensation,

```math
\boxed{
F_{\max}
\ge
\frac{\alpha\Delta E_g}{qw}.
}
```

Uniform field saturates this lower bound on peak field.

Doping modulation, delta doping, and depletion shaping can move the field into better material, but cannot produce the same electrostatic compensation voltage over width `w` with a smaller peak field than `V_b/w`.

## 11. Boundary TAT width / delay floor

For local TAT exponent scale

```math
\exp(-F_{\rm TAT}/F),
```

requiring exponent margin `Sigma_t` everywhere gives the necessary width condition

```math
\boxed{
w
\ge
\frac{\alpha\Delta E_g}
{qF_{\rm TAT}}
\Sigma_t.
}
```

If a carrier crosses with characteristic speed `v_b`, then

```math
\boxed{
t_b
\ge
\frac{\alpha\Delta E_g}
{qF_{\rm TAT}v_b}
\Sigma_t.
}
```

This is an exponent-level boundary relation, not a complete TAT-current theorem.

Measured/fitted HgCdTe defect work shows that trap energies and capture cross sections vary strongly by layer and structure; TAT can be important around `10^14 cm^-3` trap densities in LWIR material.

## 12. Optimal placement of unavoidable field

Let `F_T(x)` be the local TAT characteristic field and require compensation voltage `V_b`.

To maximize the worst local TAT exponent, solve

```math
\min_F\max_x F(x)/F_T(x)
```

subject to

```math
\int Fdx=V_b.
```

The exact maximin allocation is

```math
\boxed{
F_{\rm opt}(x)
=\frac{V_bF_T(x)}
{\int F_T(x')dx'}.
}
```

The optimized minimum exponent is

```math
\boxed{
\Sigma_{\rm TAT}^{\rm maximin}
=\frac{\int F_T(x)dx}{V_b}.
}
```

Interpretation:

> put more electrostatic field where the material/trap spectrum can tolerate more field, so normalized tunneling stress is equalized.

A conservative generalized tolerance profile may be defined from

```math
F_{\rm tol}(x)
=\min[
F_{\rm TAT}/\Sigma_t,
F_K/\Sigma_Z,
F_{\rm II},
...].
```

A necessary one-dimensional feasibility condition is then

```math
\boxed{V_b\le\int F_{\rm tol}(x)dx.}
```

## 13. Homogeneous and heterogeneous field theorems retained

For homogeneous material with

```math
v(F)=\mu F/[1+(F/d)^r],
```

and local WKB leakage

```math
g(F)=AF^pe^{-K/F},
```

uniform field is the leakage-minimizing profile at fixed transit time in the stated model.

For heterogeneous material, the transit-constrained interior optimum obeys

```math
\boxed{
-\frac{\partial g/\partial F}
{\partial(1/v)/\partial F}
=\lambda.
}
```

Thus heterogeneity is the real field-allocation resource.

## 14. Competing mechanisms remain active

### TAT

```math
\boxed{
F_{\rm TAT}/F_K
=\frac{16}{3\pi}(\Delta_t/E_g)^{3/2}.
}
```

### Nonlocal II

```math
\boxed{
F_{\rm dead}/F_K
=(4\chi/\pi)(\ell_K/L).
}
```

with energy-history corrections through an effective relaxation length.

### Interface / boundary physics

Still unresolved:

- actual trap density and occupation through the graded boundary;
- interface dipoles;
- delta-doped sheet-charge field peaks;
- nonlocal II in the collection transition;
- quantum reflection for very abrupt composition changes;
- full self-consistent Fermi-Dirac Poisson solution.

## 15. Important stopped shortcuts

Do not restart casually:

- active-volume-only bound;
- finite absorber count as one-photon limit;
- finite internal rank as always-on capacity;
- spectral FWHM as architecture-independent transport speed;
- low-field mobility extrapolated into high-field HgCdTe;
- direct BTBT assumed first high-field limiter;
- bulk `100 V/cm` II onset treated as finite-device threshold;
- nonuniform field alone assumed to reduce homogeneous WKB leakage;
- pure grading assumed to eliminate all tunneling in a real device;
- uniformly depleted multi-micron graded absorber assumed without checking Poisson headroom;
- delta doping treated as removing the electrostatic compensation requirement.

## 16. Prior-art posture

Known prior work already covers

- graded HgCdTe devices;
- WKB graded-gap HgCdTe analysis;
- graded heterojunction barrier/no-barrier optimization;
- composition and doping modulation in HgCdTe barrier detectors;
- delta doping for band-discontinuity control;
- classic Kane/Zener tunneling;
- HgCdTe TAT and DLTS defect spectroscopy;
- HgCdTe APD field engineering.

The exact detector-facing formulas derived here are not currently claimed novel.

## 17. Current next step

Do **not** return to an abstract universal detector theorem yet.

Build a concrete finite collection boundary using experimentally anchored HgCdTe defect and band-profile inputs:

1. choose a p-type graded narrow-gap interior;
2. choose a wider-gap boundary profile `E_g(x)`;
3. use a modern electron-affinity/band-offset relation;
4. specify `N_A(x)` plus any delta-doped sheet;
5. solve Fermi-Dirac Poisson through the boundary;
6. compute the continuous `E_c(x), E_v(x)` profile;
7. evaluate full-profile direct Kane WKB action;
8. evaluate TAT using measured/fitted trap energies, densities and capture cross sections;
9. evaluate nonlocal II and carrier transit through the same profile;
10. compare the actual field profile with the maximin tolerance allocation above.

The decisive question is now:

> **Can a realistic HgCdTe boundary place the unavoidable electrostatic field in sufficiently wide-gap, low-defect material that the quasi-neutral graded interior retains its speed advantage without a compensating TAT/interface penalty?**

Only after this test should publication significance be reassessed.