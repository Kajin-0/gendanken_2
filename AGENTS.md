# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gendanken_2`  
**Active experiment:** `experiments/01-vanishing-absorber/`  
**Current mode:** **open theoretical/experimental-method exploration; active frontier is few-mode differential wavelength × RF transport metrology in graded HgCdTe, with sample-B iso-kernel calibration and paired A/B validation; no novelty claim**

Read this file first.

The repository follows the physics rather than a predetermined theorem. Failed conjectures, corrections, counterexamples, and prior-art collisions are part of the result.

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

Do not use `first`, `new fundamental`, `universal`, etc. without a focused primary-source audit and `CLAIM_LEDGER.md` update.

---

## 3. Current research path

```text
vanishing-absorber thought experiment
-> universal active-volume route killed

abstract optical/network/control branches
-> successive resource loopholes

HgCdTe transport / tunneling / grading
-> material-specific branch

wavelength-resolved generation
-> spectral coordinate inside a monotonic gap

ballistic timing peak
-> proposed then killed as universal by momentum-scattering models

inverse reformulation
-> known optical kernels + timing -> internal delay-density modes

orientation correction
-> downstream collection uses CDF kernel
-> front collection uses survival kernel

identifiability correction
-> wavelength-independent boundary/common delay and broadening are gauge-like

published 2023 sample B
-> W ~3.7 um
-> nonlinear region removed
-> weak 100-200 V/cm linear gradient
-> smooth calibration/control case

published sample B dimensional optics
-> mean generation depth shifts by ~2.85 um over useful MWIR sweep
-> only a few spatial modes are strongly conditioned

phase-noise audit
-> subtle internal structure produces sub-degree residual phase
-> wavelength-dependent absorbed signal makes covariance heteroscedastic

optimal design
-> first 3 transport modes + common phase need ~4 information-rich wavelength bands
-> uniform dense sampling is inefficient

RF-frequency audit
-> usable first-moment phase band scales with transport speed
-> full complex fit required at higher normalized frequency

paired A/B protocol
-> same-source A-B subtraction cancels arbitrary wavelength-dependent source phase
-> sample A supplies nonlinear/high-field contrast

sample-B temperature iso-kernel design
-> mid/deep optical timing kernels can be held nearly invariant by retuning wavelength
-> fixed-wavelength temperature comparisons are optically confounded

compatibility correction
-> paired common-source cancellation and independent A/B iso-kernel wavelengths cannot be combined automatically
-> need one common JOINT iso-kernel wavelength schedule or explicit kernel modeling

CURRENT FRONTIER
-> recover sample A x(z)
-> build A_A(T,lambda) and A_B(T,lambda)
-> test whether a common joint iso-kernel schedule exists
-> then perform paired A/B transport-contrast validation.
```

---

## 4. Canonical reading order

1. `AGENTS.md`
2. `README.md`
3. `experiments/01-vanishing-absorber/CURRENT_STATE.md`
4. `experiments/01-vanishing-absorber/CLAIM_LEDGER.md`
5. `experiments/01-vanishing-absorber/HGCDTE_SPECTRAL_TIMING_LINEAR_INVERSE.md`
6. `experiments/01-vanishing-absorber/HGCDTE_PUBLISHED_SAMPLE_B_DIMENSIONAL_FORWARD_MATRIX.md`
7. `experiments/01-vanishing-absorber/HGCDTE_PUBLISHED_SAMPLE_B_HETEROSCEDASTIC_PHASE_NOISE.md`
8. `experiments/01-vanishing-absorber/HGCDTE_PUBLISHED_SAMPLE_B_OPTIMAL_MEASUREMENT_DESIGN.md`
9. `experiments/01-vanishing-absorber/HGCDTE_SAMPLE_B_RF_FREQUENCY_VALIDITY.md`
10. `experiments/01-vanishing-absorber/HGCDTE_TEMPERATURE_ISO_KERNEL_DESIGN.md`
11. `experiments/01-vanishing-absorber/HGCDTE_PAIRED_SAMPLE_AB_DIFFERENTIAL_PHASE.md`
12. `experiments/01-vanishing-absorber/HGCDTE_PAIRED_AB_TEMPERATURE_DESIGN.md`
13. `experiments/01-vanishing-absorber/HGCDTE_SPECTRAL_TIMING_TWO_MOMENT_INVERSE.md`
14. `experiments/01-vanishing-absorber/HGCDTE_SPECTRAL_TIMING_TOMOGRAPHY_PRIOR_ART_AUDIT.md`
15. `experiments/01-vanishing-absorber/RESEARCH_LOG.md`
16. `experiments/01-vanishing-absorber/ARCHIVE_STATUS.md`

Older ballistic-peak, normalized-kernel, optical-resource, and active-volume branches are provenance/supporting work, not the active claim.

---

## 5. Hard prior-art boundary

Do **not** claim novelty for

- wavelength-dependent absorption / generation depth;
- wavelength-dependent photodiode timing/bandwidth;
- graded-bandgap carrier transport;
- wavelength- and depth-dependent generation in graded HgCdTe;
- graded-HgCdTe forward response-time modeling;
- localized-position HgCdTe transit measurements.

Sang et al. 2022 already combine wavelength/depth generation with graded-HgCdTe forward transport/response modeling.

Perrais et al. already use localized excitation to study HgCdTe transit timing.

A 2024 same-group paper titled `Potential application of HgCdTe detector with composition gradient in laser measurement` remains an unresolved close collision. Its title/metadata are known; its technical content has not been recovered. Treat priority as unresolved until it is read.

---

## 6. Active inverse operator

Let `p_i(x)` be the known conditional generation density and `q_1(x)` the path-additive mean-delay density.

### Collection at `L`

```math
\boxed{
\bar T_i
=\int_0^L F_i(s)q_1(s)ds,
\qquad
F_i(s)=P(X_g\le s).
}
```

### Collection at `0`

```math
\boxed{
\bar T_i
=\int_0^L S_i(s)q_1(s)ds,
\qquad
S_i(s)=P(X_g\ge s).
}
```

Use **cell-integrated kernels**:

```math
\boxed{
A_{ij}=\int_{\mathrm{cell }j}K_i(s)ds,
}
```

so

```math
\boxed{\mathbf T=\mathbf A\mathbf q_1.}
```

Published samples A/B are front-collection / survival-kernel geometries.

Only under a local path-additive interpretation may one identify

```math
q_1=1/v_{\rm eff}.
```

---

## 7. Common-mode gauge

Do not claim arbitrary wavelength-independent common delay or broadening is uniquely separable from arbitrary boundary-localized internal transport.

Use

```text
differential phase/timing
independent common-chain calibration
boundary priors
or lower-dimensional physical models.
```

Regularization selecting one split is not structural identifiability evidence.

---

## 8. Two timing moments

For the orientation-correct kernel `K_i`, additive conditional cumulants give

```math
\boxed{\mu_i=\int K_iq_1,}
```

```math
\boxed{
\sigma_i^2
=\int K_iq_2
+\operatorname{Var}_{p_i}[m(X)].
}
```

Only under a local high-Peclet drift-diffusion approximation:

```math
q_1=1/v,
\qquad
q_2\simeq2D/v^3.
```

Do not call `q_2` microscopic diffusion without validation.

---

## 9. Complex-response observable

```math
H_i(\Omega)=\langle e^{-i\Omega T_i}\rangle.
```

Low-frequency cumulants:

```math
\arg H_i=-\Omega\mu_i+O(\Omega^3),
```

```math
\ln|H_i|=-\frac{\Omega^2}{2}\sigma_i^2+O(\Omega^4).
```

At higher normalized frequency fit the full complex transfer.

---

## 10. Published sample B — current calibration envelope

```text
W ~3.7 um
nominal x ~0.316
nonlinear interdiffusion region removed
junction at high-Cd end
remaining linear-gradient field ~100-200 V/cm.
```

Current 300 K central envelope uses correct Hansen gap plus Moazzami above-gap absorption.

Representative result:

```text
2.80 um -> Pabs~0.998, mean depth~0.677 um
3.88 um -> Pabs~0.070, mean depth~3.523 um.
```

Thus

```math
\Delta\langle z\rangle\approx2.85\ {\rm um}.
```

At illustrative `v_eff=1e5 m/s`, this is about `28.5 ps` or `10.25 degrees` at `1 GHz`.

Real optical matrix mode counts above relative thresholds `[1e-1,1e-2,1e-3,1e-4]`:

```text
100 V/cm -> [2,5,10,20]
150 V/cm -> [2,5,10,21]
200 V/cm -> [2,5,11,23].
```

Interpretation: **few-mode band-limited tomography**.

---

## 11. Experimental covariance / optimal design

Do not use equal phase noise as the default at fixed incident power.

Current retained-end absorbed-signal ratio is about `17.6`.

Illustrative fixed-power phase scalings:

```text
statistics-like: sigma_phi proportional to Pabs^(-1/2)
additive-like: sigma_phi proportional to Pabs^(-1).
```

The experimentally relevant matrix is noise-whitened and common-mode projected.

For a reduced target of 3 transport modes + 1 common-phase nuisance, D-optimal wavelength/time design uses about four support bands.

Statistics-like:

```text
2.800, 3.410, 3.632, 3.840 um.
```

Additive-like:

```text
2.800, 3.400, 3.596, 3.780 um.
```

These are conditional design results, not universal wavelengths.

---

## 12. RF-frequency rule

For the current sample-B optical distributions and deterministic `T=z/v`, an illustrative `|H|>0.98` envelope is

```math
\boxed{f_{\max}\approx0.13\,v/W.}
```

This is optical-only and nonuniversal. Stochastic transport/electrical response may lower the usable band.

---

## 13. Published A/B validation logic

### Sample B

Smooth calibration/control case. The 2023 authors infer its remaining `100-200 V/cm` linear-gradient field does not strongly alter carrier motion.

### Sample A

Nonlinear/high-field contrast case. It retains part of the nonlinear interdiffusion region and reaches local composition-gradient field near `2e3 V/cm`.

The authors attribute the A/B photoelectric difference primarily to composition-gradient effects on minority-carrier motion.

---

## 14. Paired A/B differential phase

With the same coherent modulated source at the same wavelength/frequency,

```math
\boxed{
\Delta\phi_{AB}
=-\Omega
(\mathbf A_A\mathbf q_A-
 \mathbf A_B\mathbf q_B)
+\Delta\phi_{\rm path}
+\Delta\phi_{\rm elec}.
}
```

Arbitrary common source phase cancels.

A reciprocal device/arm swap can cancel stable arm asymmetry under its stated assumptions.

The paired observable is a transport **contrast**, not an absolute profile.

---

## 15. Temperature iso-kernel rule

Fixed-wavelength temperature sweeps are optically confounded because

```math
\mathbf A=\mathbf A(T,\lambda).
```

For one device, define

```math
\boxed{
\lambda_*(T)
=\arg\min_\lambda
\frac{
\|\mathbf A(T,\lambda)-\mathbf A(T_0,\lambda_0)\|_2
}{
\|\mathbf A(T_0,\lambda_0)\|_2
}.
}
```

Current sample-B results:

```text
300 K 3.410 um
-> 215 K 3.52095 um (~2.45% mismatch)
-> 115 K 3.65954 um (~5.08%)

300 K 3.632 um
-> 215 K 3.79272 um (~0.44%)
-> 115 K 4.00268 um (~0.84%)

300 K 3.840 um
-> 215 K 4.04232 um (~0.043%)
-> 115 K 4.31011 um (~0.112%).
```

The shallow 2.800-um reference cannot be cleanly reproduced at 115 K inside the spectral range used to establish the current absorption fit; do not use its unconstrained ~1.15-um mathematical optimum as a validated prediction.

---

## 16. Paired-temperature compatibility correction

Same-source A-B phase cancellation requires A and B to see the **same wavelength**.

Independent device iso-kernel wavelengths therefore cannot simply be combined.

Need a common joint schedule:

```math
\boxed{
\lambda_*(T)
=\arg\min_\lambda
\left[
w_A\epsilon_A^2(T,\lambda)
+w_B\epsilon_B^2(T,\lambda)
\right].
}
```

Whether a useful joint A/B iso-kernel schedule exists is OPEN until sample A's actual profile is recovered.

If it does not exist, retain same-wavelength paired measurement and model both temperature-dependent kernels explicitly.

---

## 17. Rejected route

Reverse/sapphire-side illumination was tested conceptually/numerically on the sample-B envelope. It added little strongly conditioned rank relative to the optical/systematic complexity.

**Status:** reject for now.

---

## 18. Important nonclaims

Do not claim

- pointwise high-resolution `v(z)` reconstruction;
- absolute common delay/broadening from wavelength data alone;
- calibrated sample-A/B velocity/diffusion;
- actual internal defects;
- existence of a useful joint A/B iso-kernel schedule;
- novelty/priority;
- manuscript readiness.

---

## 19. Active numerical regressions

```text
numerics/hgcdte_published_sample_b_forward_matrix.py
numerics/hgcdte_published_sample_b_phase_noise.py
numerics/hgcdte_published_sample_b_heteroscedastic_phase.py
numerics/hgcdte_published_sample_b_optimal_design.py
numerics/hgcdte_sample_b_frequency_validity.py
numerics/hgcdte_sample_b_iso_kernel_temperature.py
numerics/hgcdte_spectral_timing_two_moment_inverse.py
```

---

## 20. Next decisive work

Do **not** add another generic inverse theorem.

Priority:

1. recover/digitize sample A's `x(z)` profile;
2. build `A_A(T,lambda)` and `A_B(T,lambda)`;
3. test common joint iso-kernel temperature schedules;
4. obtain realistic wavelength × RF-frequency covariance;
5. validate sample B first, then paired A/B transport contrast;
6. read the unresolved 2024 laser-measurement paper before any novelty language.

Only after real-data or independently validated inversion should manuscript readiness be reassessed.
