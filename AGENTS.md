# AGENTS.md - Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gendanken_2`  
**Active experiment:** `experiments/01-vanishing-absorber/`  
**Current mode:** **Rev. 3 manuscript hardening; strongest surviving result is a Shockley-Ramo-aware spectral-depth falsification hierarchy; HgCdTe is the leading worked example; priority remains unproven.**

Read this file first.

The repository follows the physics rather than a predetermined paper. Failed conjectures, observable corrections, numerical corrections, counterexamples, and prior-art collisions are part of the result and must not be erased.

## 1. Mandatory recovery order

For the current scientific frontier, read:

1. `experiments/01-vanishing-absorber/MANUSCRIPT_REV3.tex`
2. `experiments/01-vanishing-absorber/CURRENT_STATE.md`
3. `experiments/01-vanishing-absorber/REALISTIC_GEOMETRY_CLOSURE_STRESS.md`
4. `experiments/01-vanishing-absorber/PAPER_CLAIM_LEDGER.md`
5. the newest `PAPER_CLAIM_LEDGER_*ADDENDUM*.md` files
6. `experiments/01-vanishing-absorber/OBSERVATION_POLYNOMIAL_ANNIHILATION_THEOREM.md`
7. `experiments/01-vanishing-absorber/HOT_CARRIER_TWO_STATE_CLOSURE.md`
8. `experiments/01-vanishing-absorber/DC_RF_INVERSION_CONDITIONING_THEOREM.md`
9. supporting theorem/numerical files only as needed.

`MANUSCRIPT_DRAFT.tex` is retained as provenance but is no longer the latest integrated paper.

Live repository state overrides snapshots and recovery notes.

## 2. Mandatory write protocol

Before every write:

1. fetch the live target branch;
2. inspect intervening changes when needed;
3. fetch the exact current blob SHA before replacing a file;
4. never overwrite stale state;
5. preserve failed/corrected branches and why they failed;
6. make narrow edits where practical;
7. update canonical state when the scientific frontier changes.

Do not delete an old scientific result merely because it was superseded. Mark it explicitly and preserve the reason the direction changed.

## 3. Epistemic labels

Use explicitly when appropriate:

- **KNOWN**
- **DERIVED**
- **CHECKED**
- **CONDITIONAL**
- **CANDIDATE DISTINCT APPLICATION - PRIORITY UNPROVEN**
- **INVALIDATED**
- **SUPERSEDED**
- **OPEN**
- **NON-CLAIM**

A negative literature search is not novelty evidence.

Do not use `first`, `new fundamental`, `universal`, `novel`, etc. without a focused primary-source audit and claim-ledger update.

## 4. Current paper spine

### Gedanken I - four colors

For four equally spaced calibrated internal source coordinates in the homogeneous one-carrier planar Shockley-Ramo model,

```math
\boxed{(J_2-J_1)^2=(J_1-J_0)(J_3-J_2).}
```

The raw terminal current is affine-exponential in source depth. First differences remove the depth-independent observation term and isolate one spatial propagation multiplier.

Three source coordinates estimate the multiplier. The fourth is a parameter-free null.

Known unequal source coordinates remain overdetermined; equal spacing is not fundamental.

### Gedanken II - DC + RF

Uniform real drift-diffusion-recombination obeys

```math
D\gamma^2+w\gamma=\kappa+s.
```

DC plus one nonzero RF point determine `D`, `w`, and `kappa` within the model. Every later RF frequency introduces no new material coefficient and is therefore a falsification point.

The exact inversion determinant can be written

```math
\boxed{\Delta=-v(u^2+v^2)},
```

where

```math
\gamma(i\omega)-\gamma(0)=u+iv.
```

Practical conditioning is stricter than algebraic identifiability. With

```math
V_*=\sqrt{w^2+4D\kappa},
```

the balanced scale is

```math
\boxed{D\omega_*/V_*^2=\sqrt3}.
```

For the current illustrative HgCdTe scale this is near 14.1 GHz. The current 100 MHz-1 GHz band is much better for closure/timing tests than precision diffusion extraction.

### Gedanken III - six colors

If one mode fails, do not assign a mechanism immediately.

For

```math
d_m=a q_1^m+b q_2^m,
```

```math
\boxed{W_m=d_md_{m+2}-d_{m+1}^2
=ab(q_1q_2)^m(q_1-q_2)^2.}
```

A second mode must be statistically resolved before roots are interpreted.

For a homogeneous scalar finite-boundary mechanism,

```math
\boxed{r_++r_-=-w/D}
```

must be real and RF-independent.

The active interpretation rule is:

```text
four-color failure + unresolved second-mode witness
-> mechanism unresolved at current SNR
```

not

```text
four-color failure -> therefore velocity gradient.
```

## 5. Observable discipline - mandatory

Always state which response is modeled.

### Arrival / collection-flux observable

```math
U(d,s)=E[e^{-sT_d}].
```

For the homogeneous scalar first-passage semigroup this is exponential in propagation distance.

### Raw planar terminal-current observable

Under the minimal Shockley-Ramo geometry,

```math
\boxed{J(d,s)=C(s)[1-e^{-\gamma d}]}.
```

This is the active manuscript observable.

### DC-normalized terminal-current response

This is generally not the same spatial functional form as either object above.

Never import arrival-time identities into terminal current without deriving the signal-formation mapping.

## 6. Observation nonuniformity hierarchy

If the one-dimensional observation forcing gives

```math
J(z)=P_p(z)+B e^{rz},
```

then the `(p+1)`-th spatial difference removes the degree-`p` polynomial exactly:

```math
Y_m=\Delta^{p+1}J_m
=B(q-1)^{p+1}q^m.
```

Therefore

```math
\boxed{Y_1^2=Y_0Y_2},
\qquad
\boxed{N_{color}=p+4}.
```

Important cases:

```text
constant forcing  -> Delta   -> 4 colors
linear forcing    -> Delta^2 -> 5 colors
quadratic forcing -> Delta^3 -> 6 colors
```

A linear weighting trend can alternatively be identified as a rank-two root `q_weight=1`.

Do not forget the statistical price. The five-color versus four-color low-RF raw-current SNR cost scales approximately as

```math
\boxed{\mathrm{cost}_5/\mathrm{cost}_4\sim1.87|rh|^{-1}}.
```

The five-color theorem is **not** a universal cure for curved multidimensional geometry.

## 7. Hot-carrier classification

For the minimal hot-to-cold model,

```math
J_h(d,s)=A+B_c e^{-sd/v_c}+B_h e^{-(s+\rho)d/v_h},
```

with memory length

```math
\boxed{\ell_h=v_h\tau_h}.
```

If the same hot fraction is initialized at every wavelength, finite thermalization is exactly rank two and belongs on the six-color branch.

The dangerous effect is wavelength-dependent initialization.

Current HgCdTe quartet:

```text
generation-weighted mean excess-energy variation ~0.125 meV peak-to-peak
```

Generic strong long-memory stress:

```text
~0.25-0.8 percentage-point hot-fraction variation across quartet
-> false 100-MHz signal equal to 10% of present gradient target
```

These are sensitivity numbers, not material measurements.

## 8. Current conditional HgCdTe target

Use the corrected raw-Ramo four-color calculation, not the superseded reflecting-boundary three-color result.

```text
L = 7.6 um
T = 300 K
linear x = 0.55 -> 0.32
mean generation depths = 2.5, 3.0, 3.5, 4.0 um
lambda ~ 2.134651, 2.215042, 2.301173, 2.393907 um
Pabs > 0.9993
```

Gradient-sensitive closure phase:

```text
100 MHz -> -0.011978 deg
500 MHz -> -0.058727 deg
1 GHz   -> -0.110405 deg
```

Approximate `3 sigma` current-step amplitude SNR:

```text
100 MHz -> 96.1 dB
500 MHz -> 82.3 dB
1 GHz   -> 76.7 dB
```

These are **CONDITIONAL theory predictions**, not calibrated forecasts for an existing detector.

## 9. Current 2-D geometry hardening result

The executable stress is:

- `REALISTIC_GEOMETRY_CLOSURE_STRESS.md`
- `numerics/realistic_geometry_closure_stress.py`

It solves separate two-dimensional physical and Shockley-Ramo weighting potentials, follows saturated deterministic trajectories, and applies the same color hierarchy blindly.

For a 75%-width top contact plus controlled 3 um depletion-like Poisson curvature, the geometry/depletion four-color phase excess over the planar same-optics baseline is:

```text
100 MHz -> -0.008841 deg = 0.738 x current gradient target
500 MHz -> -0.045827 deg = 0.780 x target
1 GHz   -> -0.095513 deg = 0.865 x target
```

Therefore the four-color gradient residual is **not geometry-proof**.

However, the same 100-MHz geometry produces a `3 sigma` second-mode witness near 84.6 dB current-step amplitude SNR, about 11.5 dB before the 96.1 dB SNR required for the current gradient claim. The 50%-contact depletion stress gives about 71.5 dB, or approximately 24.6 dB margin.

The fitted geometry roots also violate the homogeneous finite-boundary root-sum law.

The hierarchy therefore survived this first multidimensional attack in a weaker form:

```text
four colors -> detect failure
six colors  -> classify model order
RF roots    -> prevent premature mechanism assignment
```

This is conditional on the tested geometry family, not a theorem for arbitrary devices.

## 10. Major invalidations - never silently resurrect

### Generic terminal current equals first-passage characteristic function

**INVALIDATED.** Shockley-Ramo current is induced continuously.

### Generic terminal-current three-color geometric-mean law

**INVALIDATED.** The corrected raw-current null uses four source coordinates and first differences.

### Direct inverse-Gaussian skewness/kurtosis null on arbitrary photocurrent waveform

**INVALIDATED AS A GENERIC OBSERVABLE CLAIM.** The first-passage mathematics remains valid for the arrival propagator/recovered propagation exponent.

### Earlier large HgCdTe three-color phase mainly measures the bulk gradient

**INVALIDATED / SUPERSEDED.** A reflecting entrance boundary generated nearly all of that curvature.

### Rank two means a boundary

**INVALIDATED GENERALIZATION.** Electron-hole transport, hot-carrier relaxation, and observation-field modes can also be rank two.

### Five-color observation annihilation removes arbitrary detector geometry

**INVALIDATED GENERALIZATION.** It is exact for low-order one-dimensional polynomial observation forcing, not general curved 2-D weighting/depletion geometry.

### Four-color phase residual is mechanism-specific

**INVALIDATED GENERALIZATION.** The 2-D finite-electrode/depletion stress can mimic an order-unity fraction of the present HgCdTe gradient phase.

## 11. Hard prior-art boundary

Do not claim novelty for:

```text
Shockley-Ramo induced-current theory
photodiode impulse-response modeling
wavelength-dependent absorption/generation depth
wavelength-dependent photodiode RF phase/bandwidth
optoelectronic chromatic dispersion
multi-frequency photodiode characterization
frequency-domain drift-diffusion modeling
Prony/Hankel/system-identification mathematics
first-passage semigroups / inverse-Gaussian theory
algebraic convection-diffusion inversion
graded-HgCdTe transport/high-speed response
```

The candidate distinct application is narrower:

```text
calibrated spectral internal source coordinate
+
Shockley-Ramo-aware spatial differencing
+
minimal four-/six-color model-order closure
+
RF root-law falsification of ordinary photocarrier mechanisms
```

**Status: CANDIDATE DISTINCT APPLICATION - PRIORITY UNPROVEN.**

The close 2024 graded-HgCdTe laser-measurement paper is bibliographically confirmed but its full technical content has not been recovered in the present audit.

A negative search is not priority evidence.

## 12. Next decisive work

Do **not** reopen broad theorem generation unless a manuscript/reviewer objection requires it.

Priority now:

1. run one self-consistent 2-D semiconductor Poisson/drift-diffusion detector stress including diffusion and analyze its synthetic measurement blind with the same hierarchy;
2. deepen the primary-source priority audit, especially the close 2024 graded-HgCdTe paper;
3. perform final Rev. 3 compression, equation/cross-reference QA, and reproducibility audit;
4. only after these pass, choose a target journal and adapt formatting.

The objective is the smallest set of exact, falsifiable predictions that a skeptical reviewer cannot dismiss as an observable mismatch, an uncontrolled ordinary mechanism, or rediscovery of known photodiode response physics.
