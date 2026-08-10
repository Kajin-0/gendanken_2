# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gendanken_2`  
**Active experiment:** `experiments/01-vanishing-absorber/`  
**Current mode:** **open theoretical/experimental-method exploration; strongest frontier is downstream translated-gradient HgCdTe wavelength × RF validation conditioned on independent minority-carrier transport calibration; no novelty claim**

Read this file first.

The repository follows the physics rather than a predetermined theorem. Failed conjectures, numerical corrections, counterexamples, and prior-art collisions are part of the result.

**There is still no manuscript.**

---

## 1. Mandatory repository protocol

Before every write:

1. fetch live `main` / current target;
2. inspect intervening changes when needed;
3. fetch the exact current blob SHA before replacing a file;
4. never overwrite stale state;
5. preserve failed/corrected branches;
6. make narrow edits where practical.

**Live `main` overrides snapshots and recovery notes.**

Do not delete an old result merely because it was superseded. Mark it explicitly and preserve why the direction changed.

---

## 2. Epistemic labels

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

Do not use `first`, `new fundamental`, `universal`, etc. without a focused primary-source audit and claim-ledger update.

---

## 3. Current research path

```text
vanishing-absorber thought experiment
-> universal active-volume route killed

abstract optical/network/control resource branches
-> successive loopholes and counterexamples

HgCdTe material branch
-> graded composition + wavelength-dependent generation

ballistic timing-peak idea
-> killed as universal by momentum-scattering dependence

inverse reformulation
-> known optical kernels + timing response -> differential transport modes

orientation correction
-> downstream collection uses CDF kernel
-> front collection uses survival kernel

published 2023 sample B
-> smooth calibration/control
-> few strongly conditioned spectral modes

published sample A
-> retained near-junction nonlinear/high-field region
-> short wavelengths restore raw visibility

published A/B identifiability audit
-> smooth A/B modes overlap strongly
-> contact/interface contribution can mimic A's near-junction fingerprint
-> published A/B is not a clean mechanism-control pair

purpose-built relocation pivot
-> keep boundaries/endpoints matched
-> translate one compact internal gradient feature
-> ask whether wavelength x RF fingerprint translates with it

old deterministic/ad-hoc timing studies
-> useful for geometry, edge-ramp, interdiffusion, boundary-confounding,
   randomization and replication principles
-> NOT current mechanism model

critical transport-orientation correction
-> high-Cd optical entrance
-> x decreases through p-type absorber
-> low-Cd collecting junction
-> gradient drive aligned with minority-electron collection

physics-derived first-passage model
-> backward drift-diffusion equation
-> complex RF transfer conditioned on DC collection
-> degree-scale relocation signal in broad transport stresses

complex-log numerical correction
-> direct finite differences of principal log(H) produced false high-RF Fisher gain
-> use d ln H/dp = (1/H) dH/dp

quasi-neutral p-type self-consistency
-> majority-hole band nearly pinned when N_A/N_v varies slowly
-> total minority-electron conduction-band slope ~ full dEg/dz
-> arbitrary interior chi_E multiplier superseded

2025 electron-affinity correction
-> ~2/3 intrinsic composition-driven gap change in conduction-band offset
-> consistent with full total equilibrium slope after electrostatic screening

empirical HgCdTe velocity law
-> v = mu F/[1+(F/d)^r]
-> existing transport/APD measurements constrain d,r scale
-> current ~1.9 kV/cm feature lies below several-kV/cm APD saturation-field scale

mechanism-identifiability audit
-> completely unbounded velocity-law shape remains nearly singular
-> broad physically motivated d,r constraints remove that artificial singularity

CURRENT FRONTIER
-> independently measure p-type minority-electron v(E,x), D(E,x), tau(E,x)
-> current witness compositions ~x=0.35, 0.43, 0.51
-> begin at 300 K over ~0.1-3 kV/cm
-> propagate witness-derived posterior through first-passage relocation model
-> only then reoptimize feature depths, wavelengths, RF, growth order, replication
-> continue unresolved 2024 laser-measurement prior-art audit
-> obtain real wavelength x RF covariance.
```

---

## 4. Canonical reading order

1. `AGENTS.md`
2. `README.md`
3. `experiments/01-vanishing-absorber/CURRENT_STATE.md`
4. `experiments/01-vanishing-absorber/CLAIM_LEDGER_2026-08-10_TRANSPORT_CORRECTIONS.md`
5. `experiments/01-vanishing-absorber/CLAIM_LEDGER.md`
6. `experiments/01-vanishing-absorber/HGCDTE_DOWNSTREAM_DRIFT_DIFFUSION_RELOCATION.md`
7. `experiments/01-vanishing-absorber/HGCDTE_QUASINEUTRAL_EMPIRICAL_VELOCITY_RELOCATION.md`
8. `experiments/01-vanishing-absorber/HGCDTE_TRANSPORT_WITNESS_CALIBRATION_DESIGN.md`
9. `experiments/01-vanishing-absorber/HGCDTE_PHYSICAL_NUISANCE_RELOCATION_DESIGN.md`
10. `experiments/01-vanishing-absorber/HGCDTE_TRANSLATED_GRADIENT_PRIOR_ART_BOUNDARY.md`
11. `experiments/01-vanishing-absorber/HGCDTE_PROGRAMMED_TRANSLATED_GRADIENT_FEASIBILITY.md`
12. `experiments/01-vanishing-absorber/HGCDTE_PROGRAMMED_INTERFACE_SAFE_JOINT_DESIGN.md`
13. `experiments/01-vanishing-absorber/HGCDTE_PROGRAMMED_WIDTH_INTERDIFFUSION.md`
14. `experiments/01-vanishing-absorber/HGCDTE_LPE_TRANSLATED_GRADIENT_REACHABILITY.md`
15. `experiments/01-vanishing-absorber/HGCDTE_SHORTWAVE_MECHANISM_CONFOUNDING.md`
16. `experiments/01-vanishing-absorber/HGCDTE_SPECTRAL_TIMING_LINEAR_INVERSE.md`
17. `experiments/01-vanishing-absorber/HGCDTE_PUBLISHED_SAMPLE_B_DIMENSIONAL_FORWARD_MATRIX.md`
18. `experiments/01-vanishing-absorber/HGCDTE_SPECTRAL_TIMING_TOMOGRAPHY_PRIOR_ART_AUDIT.md`
19. `experiments/01-vanishing-absorber/RESEARCH_LOG.md`
20. `experiments/01-vanishing-absorber/RESEARCH_LOG_2026-08-10_CONTINUATION.md`
21. `experiments/01-vanishing-absorber/ARCHIVE_STATUS.md`

Where the dated transport claim addendum conflicts with an older transport/design entry in `CLAIM_LEDGER.md`, the addendum and live `CURRENT_STATE.md` take precedence.

---

## 5. Hard prior-art boundary

Do **not** claim novelty for

- wavelength-dependent absorption / generation depth;
- wavelength-dependent photodetector timing/bandwidth;
- graded-bandgap carrier transport;
- composition-gradient built-in fields in HgCdTe;
- high-speed / RF graded-HgCdTe response;
- graded-HgCdTe spectral response;
- wavelength/depth forward generation modeling;
- localized-position HgCdTe transit measurements;
- Shockley-Haynes HgCdTe minority-carrier transport measurement;
- optical-load-dependent HgCdTe transient response;
- programmable positive HgCdTe composition gradients by LPE.

Sang et al. 2022 already measure high-speed graded-HgCdTe response and model composition-gradient-induced carrier transport.

Rothman et al. 2010 already measure minority-electron drift velocity, diffusion coefficient and lifetime versus field in p-type HgCdTe.

Perrais et al. already use localized excitation to study HgCdTe transit timing.

Huo et al. 2024 already demonstrate controlled positive longitudinal HgCdTe composition gradients by LPE.

A 2024 paper titled

`Potential application of HgCdTe detector with composition gradient in laser measurement`

DOI `10.5768/JAO202445.0310009`

remains an unresolved close collision. Metadata are verified; full technical content has not been recovered.

Current allowed wording:

> **candidate inverse-metrology / translated-feature validation method; priority unproven.**

---

## 6. Active downstream inverse orientation

For collection at `L`, the low-frequency path-additive inverse is

```math
\boxed{
\bar T_i
=\int_0^L F_i(s)q_1(s)ds,
\qquad
F_i(s)=P(X_g\le s).
}
```

For front collection at `0`, the survival form remains

```math
\boxed{
\bar T_i
=\int_0^L S_i(s)q_1(s)ds,
\qquad
S_i(s)=P(X_g\ge s).
}
```

The published 2023 A/B structures use front collection.

The active purpose-built high-speed validation structure uses **downstream collection**.

Use cell-integrated kernels for low-frequency inversions.

Only under a local path-additive interpretation may one identify `q_1=1/v_eff`.

---

## 7. Active purpose-built orientation

Use conceptually

```text
z=0: high-Cd optical entrance
x(z): monotonically decreasing
p-type graded absorber
z=L: low-Cd collecting junction.
```

This aligns the composition-gradient minority-electron drive with collection.

If the low-Cd junction is on the epitaxial top side, substrate/backside illumination may be required.

Treat substrate/reflection/passivation optics as part of the known optical kernel; do not revert to the wrong junction/gradient orientation merely to simplify illumination.

---

## 8. First-passage complex response

The active reduced transport model is

```math
\boxed{
D u''+v(z)u'
-\left(\frac1{\tau_{\rm rec}}+s\right)u=0.
}
```

Use an absorbing collection boundary and reflecting/Robin-loss optical entrance.

At RF frequency `Omega`, `s=iOmega`.

The normalized transfer is

```math
\boxed{
H(\lambda,\Omega)
=
\frac{\int p(z|\lambda)u(z,i\Omega)dz}
{\int p(z|\lambda)u(z,0)dz}.
}
```

The old imposed `25%` local-delay/velocity perturbation is **not** the mechanism model anymore.

---

## 9. Permanent complex-derivative rule

At high RF, never finite-difference the principal complex logarithm directly unless branch continuity is explicitly enforced.

Use

```math
\boxed{
\frac{\partial\ln H}{\partial p}
=\frac{1}{H}\frac{\partial H}{\partial p}.
}
```

A previous false high-RF Fisher advance came from violating this rule and is permanently invalidated.

---

## 10. Quasi-neutral p-type transport rule

For a quasi-neutral p-type graded interior,

```math
E_v\simeq E_F+k_BT\ln(N_A/N_v),
```

therefore

```math
\boxed{
\frac{dE_c}{dz}
\simeq
\frac{dE_g}{dz}
+k_BT\frac{d}{dz}\ln\frac{N_A}{N_v}.
}
```

For slowly varying `N_A/N_v`, most of the total gap gradient appears as useful minority-electron conduction-band slope.

Do not use an arbitrary free scalar `chi_E` as the central interior field model.

Non-quasi-neutral junction/boundary regions still require explicit electrostatics.

---

## 11. Density-of-states correction

Use the reduced drift expression

```math
\boxed{
v_e
=-\frac{\mu}{q}\frac{dE_c}{dz}
+D\frac{d\ln N_c}{dz}.
}
```

For the present nondegenerate baseline with `m_e^* proportional to E_g`,

```math
\frac{d\ln N_c}{dz}
\simeq
\frac32\frac{d\ln E_g}{dz}.
```

This is a material correction, not an arbitrary free field mode.

---

## 12. Empirical velocity-law scale

Use as a compact sensitivity model

```math
\boxed{
v(F)=\frac{\mu F}{1+(|F|/d)^r}.}
```

Existing HgCdTe measurements/fits put representative `d` scales in the several-kV/cm range and `r` roughly order 2.

The current compact gradient gives a local force scale around `~1.9 kV/cm`, below those APD saturation-field scales.

Do not import low-temperature APD parameters as exact 300 K constants.

---

## 13. Current mechanism-identifiability rule

If the velocity-law shape is allowed completely unbounded amplitudes, wavelength × RF relocation data cannot uniquely attribute a measured transport change to the localized gradient.

In the current conditional three-depth model, unbounded `d,r` leave only about `~1.1 sigma` mechanism significance at the provisional `0.10 deg` component-noise scale.

But broad physically plausible constraints such as

```text
sigma_ln(d) ~0.7
sigma_r ~0.5
```

remove that artificial singularity in the central model.

These Fisher numbers are **not laboratory predictions**.

The correct response is independent transport calibration, not claiming that the relocation inverse can learn an arbitrary constitutive law by itself.

---

## 14. Decisive companion transport witnesses

Current first witness set:

```math
\boxed{x\approx0.35,\ 0.43,\ 0.51.}
```

These bracket the programmed high-gradient feature composition range `x~0.344-0.517`.

Begin at `300 K` and span approximately

```text
E = 0.1-3 kV/cm.
```

Measure directly

```text
v(E,x)
D(E,x)
tau(E,x).
```

A conceptual `100 um` transport distance corresponds to only `1-30 V` and gives transit times from sub-ns to tens of ns over broad HgCdTe transport stresses.

Use multiple propagation distances if possible to reject arbitrary time-zero offset.

Do not force Einstein diffusion if the witness data show hot-electron diffusion.

---

## 15. Purpose-built composition profile remains a design envelope

Current useful geometric scale remains approximately

```text
absorber thickness ~7.6 um
conceptual x_front ~0.55
conceptual x_back ~0.32
compact feature width ~0.9-1.0 um
edge transitions ~0.1 um
background gap-gradient force ~0.2 kV/cm
local compact feature force ~1.9 kV/cm.
```

The exact profile is not physically privileged.

Replace it by the **measured realized x(z)** for every fabricated structure.

---

## 16. Shape/fabrication lessons that remain valid

Even though exact old depth optima are superseded, several robust design lessons survive:

- both front and back interfaces must be modeled as confounders;
- feature relocation is stronger than a static feature/no-feature comparison;
- `25-100 nm` edge transitions were on an information plateau in the converged old geometry model;
- useful width was broad around `~0.9-1.1 um`;
- moderate interdiffusion degraded information gradually rather than catastrophically;
- MBE is the strongest first route for the compact programmed profile;
- MOCVD is a credible diffusion-aware alternative;
- single-run slider LPE does not demonstrate the compact `~10^3 cm^-1` local gradient regime required by the current design.

---

## 17. Randomization and replication

Keep these principles:

```text
decorrelate feature depth from chronological growth order
replicate selected feature depths
measure process covariates
fit run-to-run variance rather than assuming perfect matching.
```

Do **not** use the old exact six/eight-run orders as final prescriptions.

They were optimized with a superseded deterministic timing operator.

Recompute depth count, ordering, and replicate anchors after the witness-derived transport posterior and real measurement covariance are available.

---

## 18. Electrical / optical calibration rules

A purely wavelength-independent electrical transfer can be absorbed by one complex intercept per RF frequency/device.

The dangerous electrical terms are wavelength- or signal-state-dependent.

For the corrected high-Cd entrance geometry, include

```text
substrate transmission
reflection/interference
passivation / AR stack
wavelength calibration
and actual x(z)
```

in the optical kernel before freezing sparse wavelength supports.

---

## 19. Important nonclaims

Do not claim

- pointwise high-resolution `v(z)` imaging;
- absolute common timing from wavelength data alone;
- the old illustrative `25%` perturbation is physical;
- low-temperature APD `d,r` parameters apply unchanged at 300 K;
- Einstein diffusion is exact at high field;
- exact final feature depths, wavelengths, RF frequencies, or growth order are known;
- same-wafer translated HgCdTe growth has been demonstrated;
- novelty/priority;
- manuscript readiness.

---

## 20. Current blockers

1. direct `300 K` p-type `v(E,x),D(E,x),tau(E,x)` over the intended composition/field range;
2. witness-derived transport posterior rather than hand-set constitutive priors;
3. measured realized `x(z)` for purpose-built translated-gradient structures;
4. high-Cd-side/backside optical transfer including substrate/reflection effects;
5. measured wavelength × RF complex-response covariance;
6. calibrated electrical/junction transfer;
7. explicit non-quasi-neutral boundary/junction model where needed;
8. full technical content of DOI `10.5768/JAO202445.0310009`;
9. fabricated translated-gradient validation series.

---

## 21. Next decisive work

Do **not** add another generic inverse theorem, another arbitrary timing basis, or another exact growth-order optimization under hand-set transport parameters.

Next:

1. build a three-composition witness-derived posterior for `v(E,x),D(E,x),tau(E,x)`;
2. determine the measurement precision needed from the witness experiment;
3. allow `D(E,x)` to depart from Einstein independently;
4. propagate that posterior through the downstream first-passage model;
5. test whether three witness compositions are sufficient;
6. then reoptimize translated feature depths, wavelength/RF allocation, growth order, and replication;
7. continue the unresolved 2024 laser-measurement prior-art audit.

Only after the transport law and real covariance are independently constrained should manuscript readiness be reassessed.
