# Paper 02 — optical-kernel / model-uncertainty stress

**Date:** 2026-08-16  
**Status:** **CHECKED THEORETICAL MODEL-UNCERTAINTY RESULT / REV. 5 REMAINS FROZEN PENDING MANUSCRIPT DISPOSITION**  
**Priority:** **PRIORITY UNPROVEN**  
**Scope:** controlled theoretical kernel-misspecification directions. The numerical amplitudes below are **not empirical instrument error bars, not wavelength-calibration specifications, and not experimental feasibility claims**.

## 1. Why this gate was necessary

The canonical Paper-02 counterexample assumes that the six wavelength-dependent optical generation kernels are known exactly by the inverse.

The covariance stress showed that the same-frequency attribution ordering is robust to a broad family of *measurement-noise metrics*, but measurement covariance and forward-model error are different problems.

The present gate asks:

> What happens when the physical transport is deterministic and has `D_micro=0`, but the true optical generation kernels differ slightly from the nominal theoretical kernels used by the inverse?

This is a direct test of the strongest remaining assumption in the canonical inverse.

---

## 2. General local nuisance geometry

The analytical framework is recorded in

```text
PAPER02_GENERALIZED_NUISANCE_GEOMETRY_2026-08-16.md
```

For real-stacked data

```math
y=f(\theta)+B\eta+n,
```

with measurement metric `W=Sigma^{-1}`, fitted-model Jacobian `G`, and a small fixed nuisance `eta`, the generalized least-squares pseudo-true shift is

```math
\delta\theta=(G^T W G)^{-1}G^T W B\eta+O(\|\eta\|^2).
```

With

```math
P_W=G(G^T W G)^{-1}G^T W,
```

the post-fit model discrepancy is

```math
(I-P_W)B\eta.
```

Thus a kernel-error direction can simultaneously have

```text
large tangent component -> large parameter bias
small normal component  -> weak same-frequency model rejection.
```

If the kernel nuisance is random zero-mean with known covariance, it may be marginalized at first order into an effective covariance. A fixed or biased kernel error cannot: its mean produces deterministic pseudo-true parameter bias.

---

## 3. Broad finite kernel-misspecification stress

Executable source:

```text
numerics/paper02_kernel_misspecification_stress.py
.github/workflows/paper02-kernel-misspecification-stress.yml
```

Successful artifact-producing run:

```text
run      31953612225
job      95180757817
artifact paper02-kernel-misspecification-stress
id       9265333990
SHA-256 b2a633d9dcbdb1fc0e3e34816292606c789f6a7aeec2521fd21ec8c6f5889623
```

The immediately preceding run `31953533087` completed the scientific calculation but failed in a shell here-document used only to print a compact summary. It produced no persisted artifact. That reporting failure is preserved as provenance; the scientific script was not reinterpreted to hide it.

### Transport truths tested

1. **heterogeneous exact:** exact full-contact planar deterministic counterexample, `D_micro=0`, no recombination;
2. **uniform-velocity null:** exact full-contact uniform deterministic transport, `D_micro=0`, with nominal kernels giving `D_eff` at numerical zero.

The uniform velocity is approximately

```text
2.92697e4 m/s.
```

### Kernel perturbation families

- common wavelength shifts `+/-1 nm`, `+/-5 nm`;
- channel-linear wavelength-registration slope with endpoint amplitudes `1 nm`, `5 nm`;
- channel-curvature wavelength-registration error at `1 nm`, `5 nm`;
- mean-preserving kernel-width scales `0.90`, `0.95`, `1.05`, `1.10`;
- mean-preserving symmetric tail mixing.

The inverse always uses the **nominal theoretical kernels**.

### Nominal uniform null

At 100 MHz:

```text
D_eff = -3.94e-13 m^2/s
```

and the 100-MHz-anchored 1-GHz law residual is

```text
2.90e-12.
```

Thus the nominal uniform calculation is a genuine numerical null.

### Key finite-amplitude observation

The +channel-linear 1-nm wavelength mode produces, in the uniform null,

```text
D_eff(100 MHz) = 8.4510e-2 m^2/s
w_eff          = 2.89064e4 m/s
one-mode fit relative residual = 8.09e-7
S_D            = 84.94 dB
S_reject       = 128.45 dB.
```

So the positive apparent diffusion is not an optimizer blow-up or a negative/implausible-drift branch. It is a close one-mode fit with positive ordinary drift, and positive `D` becomes statistically detectable far before the same-frequency model manifold is rejectable under the declared reference covariance.

However, the broad one-sign finite sweep alone is **not** sufficient to classify a nuisance family as safe or unsafe because reversing a signed nuisance can reverse the sign of `D_eff`. That issue is handled below.

---

## 4. Exact affine depth-coordinate null control

An auxiliary affine control embedded in the first threshold run warped sampled kernel densities on a finite grid. It introduced boundary/interpolation error and **must not be used as theorem evidence**.

That control is explicitly superseded by

```text
numerics/paper02_exact_affine_depth_control.py
.github/workflows/paper02-exact-affine-depth-control.yml
```

Successful run:

```text
run      31953979410
artifact paper02-exact-affine-depth-control
id       9265427741
SHA-256 88ffda243e9a1698136cf6b4ab46a2eba9b3fb43e1ab7620427f970c402f3776
```

The corrected test retains the nominal kernel coordinate `u` exactly and evaluates the analytic uniform-drift response at

```math
z_{true}=z_c+b(u-z_c)
```

before integration.

For `b=0.990, 0.995, 1.000`, across 100 MHz, 500 MHz, and 1 GHz:

```text
max |D_eff|            = 4.67e-14 m^2/s
max relative w error   = 1.49e-14
max one-mode fit rel   = 7.73e-16.
```

At `b=0.990`, kernel means move by as much as **18 nm**, yet `D_eff` remains numerical zero.

This verifies the analytical affine-coordinate corollary:

```math
\gamma_{eff}=b\gamma,
\qquad
D_{eff}=D/b^2,
\qquad
w_{eff}=w/b.
```

Therefore, if true `D=0`, a **pure affine depth-scale error does not create positive diffusion**. The dangerous kernel errors are non-affine/channel-dependent registration or shape errors.

---

## 5. Local signed tangent/normal projection

Corrected executable source:

```text
numerics/paper02_kernel_nuisance_tangent_projection_v2.py
.github/workflows/paper02-kernel-nuisance-tangent-v2.yml
```

Successful run:

```text
run      31954048251
artifact paper02-kernel-nuisance-tangent-projection-v2
id       9265445464
SHA-256 55a6f31bad078d698ac6ebc8879f606b7d8b04fd584c8c5b78f63160cf130f13
```

The first version of this script imported `diffusion_gradient` from a 100-MHz-specific validation module. Its 100-MHz rows and all channel-space tangent/normal projections were correct, but its displayed `dD/d epsilon` values at 500 MHz and 1 GHz were scaled with the wrong fixed `OMEGA`. That defect is preserved and superseded by the frequency-aware v2 calculation above.

The local calculation uses a centered finite difference `h=0.001 nm` about **zero kernel error** in the exact uniform-velocity `D_micro=0` null. Finite nonlinear `D` agrees with the corrected first-order prediction to approximately:

```text
common mode      ~0.3–0.4%
linear mode      ~2.6e-4 relative
curvature mode   ~1e-5 relative
```

at the tested infinitesimal step.

### 100 MHz

| mode | sign giving positive D | dD/dA (m2/s/nm) | tangent/normal norm ratio | asymptotic S_reject/S_D |
|---|---:|---:|---:|---:|
| common | + | `+2.13665e-3` | `1.105e3` | `2.540` |
| linear | + | `+8.51294e-2` | `5.445e2` | `72.72` |
| curvature | - | `-8.89943e-1` | `10.90` | `13.98` |

All three signed directions are **bias-first in the infinitesimal limit** for the sign that makes apparent diffusion positive.

### 500 MHz

| mode | sign giving positive D | dD/dA (m2/s/nm) | tangent/normal norm ratio | asymptotic S_reject/S_D |
|---|---:|---:|---:|---:|
| common | + | `+8.21710e-5` | `1.080e3` | `2.389` |
| linear | + | `+3.40023e-3` | `3.232e2` | `43.12` |
| curvature | - | `-3.55398e-2` | `10.55` | `13.52` |

### 1 GHz

| mode | sign giving positive D | dD/dA (m2/s/nm) | tangent/normal norm ratio | asymptotic S_reject/S_D |
|---|---:|---:|---:|---:|
| common | + | `+1.80191e-5` | `1.013e3` | `1.970` |
| linear | + | `+8.46125e-4` | `1.856e2` | `24.69` |
| curvature | - | `-8.83997e-3` | `9.644` | `12.33` |

### Interpretation

The relevant asymptotic quantities scale as

```text
D_bias ~ A
normal residual ~ A
S_D ~ 1/|A|
S_reject ~ 1/|A|.
```

Thus, as a systematic calibration amplitude tends toward zero, both tests require larger SNR, but their **ordering approaches a finite geometry-controlled ratio**. A near-tangent nuisance can remain bias-first arbitrarily close to zero error.

This is why merely saying that a calibration error is "small" is not sufficient. Its orientation relative to the transport tangent matters.

---

## 6. Signed 100-MHz mode thresholds

Executable source:

```text
numerics/paper02_signed_kernel_mode_thresholds.py
.github/workflows/paper02-signed-kernel-mode-thresholds.yml
```

Successful run:

```text
run      31954087223
artifact paper02-signed-kernel-mode-thresholds
id       9265464316
SHA-256 a1f80b828df5c650052a7890b7cc64867e60519e5cdfd89ddb11676416e01828
```

The target for comparison is the exact heterogeneous-kernel counterexample at 100 MHz:

```text
D_target = 2.618164535e-3 m^2/s.
```

### Channel-linear wavelength-registration mode

Parameterization:

```text
delta_lambda_m = A * [-1,-0.6,-0.2,+0.2,+0.6,+1].
```

The positive sign creates positive apparent diffusion.

A uniform deterministic `D=0` device reproduces the central heterogeneous `D_target` at

```text
A = +0.0299713 nm
endpoint wavelength span = 0.0599426 nm
max absolute mean-generation-depth shift = 0.205754 nm.
```

At that point:

```text
D_eff    = 2.618164535e-3 m^2/s
w_eff    = 2.92655e4 m/s
S_D      = 115.221 dB
S_reject = 156.814 dB
fit rel  = 3.09e-8.
```

Thus the false material parameter is detectable about **41.6 dB of channel-SNR earlier** than same-frequency one-mode rejection in this controlled stress.

The signed scan remains bias-first for every positive amplitude tested from `1e-6 nm` through `5 nm`; no finite ordering crossover was found over that interval.

### Channel-curvature wavelength-registration mode

The curvature mode is normalized to unit maximum absolute channel error. The **negative** sign creates positive apparent diffusion.

It reproduces the same `D_target` at

```text
|A| = 0.00294205 nm
signed A = -0.00294205 nm
max absolute mean-generation-depth shift = 0.0200413 nm.
```

At that point:

```text
D_eff    = 2.618164545e-3 m^2/s
w_eff    = 2.92695e4 m/s
S_D      = 115.226 dB
S_reject = 138.136 dB
fit rel  = 2.65e-7.
```

The false `D` is therefore detectable about **22.9 dB of channel-SNR earlier** than same-frequency rejection in this stress.

The scan remains bias-first over the full tested magnitude interval `1e-6 nm` through `5 nm` for the positive-D sign. At very large curvature amplitudes the inferred drift can eventually become negative; those large-amplitude branches are not used to define a physically plausible false-positive material estimate.

### Common wavelength offset

The positive sign produces positive `D` infinitesimally, but it is much less efficient at generating the target false diffusion than the differential modes.

No `D_target` match was found within the declared `0–5 nm` search range. At `+5 nm`, the uniform null gives only

```text
D_eff ~= 1.57e-3 m^2/s.
```

The same-frequency ordering is nonmonotone at finite common shifts. The executable scan found ordering crossings near

```text
0.0746 nm, 0.1242 nm, 0.2100 nm.
```

These finite-amplitude common-mode crossings are secondary and should not be generalized beyond the declared optical model.

---

## 7. Sensitivity of the heterogeneous counterexample itself

A separate signed channel-linear scan (`paper02_kernel_calibration_threshold.py`, successful run `31953787613`, artifact id `9265395449`, SHA-256 `41ac30a96b8e2b839a91564d023392634a5a2589838eb77b7a92c68ed80d8214`) asks how much differential wavelength-registration error changes the **already-positive** heterogeneous exact `D_eff`.

At 100 MHz, a channel-linear slope amplitude of only

```text
+0.00455408 nm
```

raises the inferred `D_eff` by 10%, while reversing the slope with magnitude

```text
0.00454328 nm
```

lowers it by 10%.

These numbers demonstrate severe local sensitivity of the *numerical effective-parameter magnitude* to the exact theoretical-kernel map.

They must **not** be converted into an experimental wavelength-calibration requirement without a validated instrument/optical-error model. The controlled nuisance coordinate simultaneously changes the wavelength-to-depth kernel map, not merely a laser readout digit.

---

## 8. Scientific consequence for Paper 02

The model-uncertainty stress strengthens one part of Paper 02 and weakens another.

### Strengthened

The broader inverse-identifiability principle is stronger:

> positive apparent diffusion is not unique to deterministic velocity heterogeneity. A fixed optical-kernel misspecification with a component along the profiled transport-root tangent can also create positive apparent diffusion from a deterministic `D_micro=0` response while leaving a much smaller same-frequency normal residual.

The tangent/normal framework correctly predicts this behavior locally.

### Weakened / newly bounded

The conditional HgCdTe-like numerical value

```text
D_eff ~ 2.6e-3 m^2/s
```

cannot be interpreted as a robust material-attribution magnitude unless the generation kernels are independently known well enough in the **relevant nuisance subspace**.

Therefore the exact-known-kernel assumption is not a minor implementation detail. It is a load-bearing identifiability condition.

The safe claim is about the existence and geometry of attribution failure under declared model assumptions, not about experimentally recovering a uniquely meaningful diffusion coefficient from the six-channel response without optical-model uncertainty control.

---

## 9. Experimental-design consequence

Increasing electrical/readout SNR alone cannot solve a structural kernel/transport degeneracy. A useful calibration or extra measurement axis must constrain nuisance directions that overlap the transport-root tangent.

Candidate separation axes include, conditionally:

- independent optical/kernel characterization;
- additional wavelengths chosen to rotate the kernel-nuisance and transport tangents;
- RF frequency, because transport and optical-model errors need not share the same dispersion law;
- bias or temperature, if they change transport while leaving the optical mapping sufficiently constrained.

The correct design objective is not merely "more data" but **larger nuisance-conditioned transport information**, e.g. the Schur-complement information after profiling/calibrating optical nuisance coordinates.

---

## 10. Manuscript disposition

**Rev. 5 remains frozen.**

This result is scientifically substantive enough that the next canonical manuscript revision should not merely add a sentence to Limitations. A new revision should, at minimum:

1. generalize the tangent/normal discussion from measurement noise to deterministic kernel nuisance;
2. state explicitly that the pseudo-true `D_eff` depends on the forward model, inverse family, and weighting metric under misspecification;
3. add the exact affine-depth null control;
4. include one concise signed kernel-misspecification counterexample in the uniform `D=0` null;
5. distinguish exact-known theoretical kernels from experimentally uncertain kernels;
6. weaken any wording that could make `2.6e-3 m^2/s` sound like a calibration-robust material estimate;
7. retain the existing velocity-heterogeneity result as an independently established deterministic mechanism, not replace it with the kernel-error mechanism;
8. undergo a fresh priority audit because the enlarged manuscript now overlaps generic errors-in-variables / nuisance-identifiability literature more strongly;
9. undergo a new hostile review after compilation.

Paper 01 / anonymous Rev. 9 remains untouched.
