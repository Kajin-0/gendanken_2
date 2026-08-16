# Paper 02 Rev. 1 — Adversarial Scientific Review

**Date:** 2026-08-15  
**Target:** `PAPER02_MANUSCRIPT_REV1_ANON_2026-08-15.tex`  
**Disposition:** **PROMISING BUT NOT ACCEPTABLE AS WRITTEN; MAJOR REVISION REQUIRED**

This review deliberately assumes a technically hostile referee who accepts none of the manuscript's interpretive shortcuts without a mathematical or statistical bridge.

## Executive assessment

The central result is real and substantially stronger than the original finite-electrode stress: a deterministic zero-microscopic-diffusion response can acquire a positive homogeneous `D_eff` through finite-generation-kernel sampling of deterministic velocity heterogeneity, and the effect survives several unusually strong causal controls.

However, Rev. 1 still contains four weaknesses that a strong referee could use to reject the paper even if the underlying science is correct:

1. the local field-gradient theorem is not explicitly connected to the source-difference exponent that the spectral inverse actually estimates;
2. the manuscript uses a small full-vector one-mode residual as if it implied model acceptance, without yet giving a covariance-aware same-frequency rejection calculation;
3. the causal language around kernel support is stronger than the controls strictly prove, because the mean-preserving ablation necessarily changes higher kernel moments;
4. the HgCdTe optical-kernel construction and the limits of the realism comparison are under-described in the manuscript itself.

These are repairable. None currently invalidates the core counterexample.

---

# Major comments

## M1. The field-gradient theorem is mathematically under-connected to the measured inverse

Rev. 1 derives the exact deterministic planar Ramo equation

```math
\partial_z H=-1/L+i\omega H/v(z)
```

and later states the local quadratic exponent coefficient

```math
a_2(z)=
\frac{v'(z)}{v(z)^2}
\left[
\frac{(L-z)^2}{v(z)}-
\int_z^L\frac{L-u}{v(u)}du
\right].
```

But the manuscript does not define the infinitesimal source-difference exponent between those two statements.

A referee can reasonably ask:

> What exactly is being exponentiated? `H` itself is not a spatial exponential because of its affine offset. Why does a coefficient derived from `H_z` correspond to the `gamma` recovered from the one-mode channel inverse?

### Required repair

Define

```math
P(z,\omega)=\partial_z H(z,\omega)
```

and the local point-source spatial exponent

```math
\boxed{
\gamma_{\rm loc}(z,\omega)
=-\partial_z\ln[-L P(z,\omega)].
}
```

Equivalently, for source spacing `h`,

```math
\gamma_h(z,\omega)
=-\frac1h\ln\frac{P(z+h,\omega)}{P(z,\omega)},
```

with `h -> 0` giving `gamma_loc`.

Then show the low-frequency expansion explicitly. This directly connects the theorem to the first-difference/exponential structure used by the spectral-depth inverse.

Also state the scope correctly: this is a **local point-source theorem**. The finite-kernel result is not obtained by simply evaluating the theorem at the kernel mean; it follows only after the separate kernel-averaging/leakage analysis.

**Severity: major.**

---

## M2. `O(10^-4)` full-channel fit residual is not a statistical model-acceptance result

Rev. 1 repeatedly notes that accelerating deterministic profiles can return positive `D_eff` while the calibrated one-mode residual remains `O(10^-4)`.

The numerical quantity used in the current scripts is approximately

```math
\|J-J_{\rm fit}\|/\|J\|.
```

This is useful as a deterministic approximation metric, but it is not by itself a model-selection statistic. The norm of `J` includes large offset/amplitude components that are profiled out by the transport inverse. A small residual relative to the full signal can therefore look more impressive than the actual residual relative to the transport-sensitive information.

### Required repair

Under the same explicit equal-quadrature theoretical noise model already used for the multi-frequency analysis, compute the same-frequency profiled residual statistic.

At one frequency there are six complex channels = 12 real observations and three complex fitted parameters `(C,K,r)` = 6 real parameters, hence locally

```math
\nu=6
```

residual degrees of freedom.

For a pseudo-true fitted response `J_fit`, under per-quadrature noise `sigma`, the noncentrality is

```math
\Lambda_{1f}=\|J-J_{\rm fit}\|^2/\sigma^2
```

for isotropic independent noise, or the corresponding covariance-weighted form generally.

Report the channel SNR required to reject the one-mode model at the same significance/power convention used for the multi-RF test.

Ideally also compare that rejection threshold with the SNR required to establish `D_eff>0` at a stated significance. If positive `D_eff` cannot be statistically resolved before the one-mode model itself is rejected, the interpretation of a 'hidden' same-frequency confound must be weakened.

**Severity: major and potentially outcome-changing.**

---

## M3. The mean-preserving control proves that the mean is insufficient; it does not prove that support is the only relevant kernel variable

The strongest causal control removes all support in the nuisance region and exponentially tilts the surviving upstream distribution so that each original mean is restored exactly.

This is excellent evidence that

```text
mean generation depth alone is insufficient
```

and, together with the continuous tail-weight sweep, that nuisance-region support is a causal contributor.

But the modified kernels also change higher upstream moments and shape. Therefore the experiment does **not** establish the stronger uniqueness statement

```text
support is the causal optical variable
```

in the sense that no other shape functional matters.

### Required repair

Replace exclusive language such as

> “the causal optical variable is support rather than mean depth”

with

> “the controls show that mean depth alone is insufficient and that support in the heterogeneous region is a causal contributor to the bias.”

The exact leakage theorem already provides the stronger mathematical statement that only the restriction of `g_m(z)` to the nuisance region enters `E_m` when the point-source discrepancy is supported there. Within that theorem, detailed shape **inside** the region can matter in addition to total overlap probability `p_m`.

This nuance improves rather than weakens the paper.

**Severity: major claim-precision issue.**

---

## M4. The optical kernels are central to the result but appear in Rev. 1 as an unexplained imported object

The paper's strongest causal result depends on the full calibrated kernel shapes and their restricted probabilities inside the nonuniform region. Yet the main text does not say enough about how the conditional HgCdTe kernels are produced.

A referee should not have to inspect a repository script to learn whether these are Beer--Lambert kernels, transfer-matrix fields, empirical kernels, or arbitrarily chosen distributions.

### Required repair

Add a compact Methods subsection or supplementary-method statement specifying:

- absorber thickness and composition profile used for the conditional example;
- how wavelength is chosen to target the six mean depths;
- optical absorption model used to construct `g_m(z)`;
- normalization convention;
- whether reflection/interference are neglected;
- that the kernels are a **conditional theoretical optical model**, not experimentally calibrated kernels from a particular device;
- why the word “calibrated” in the abstract/theorems means “treated as independently known by the inverse,” not “experimentally calibrated in this paper.”

The last point is especially important. The current wording can be read as implying real calibration data that do not exist.

Consider replacing some occurrences of “calibrated kernels” with “known finite kernels” or “kernel-aware inverse” in the abstract/title-level claims.

**Severity: major reproducibility/wording issue.**

---

## M5. The statistical section is stronger than most of the paper, but the two layers of model rejection are not yet separated cleanly

There are two distinct model checks:

1. same-frequency channel-manifold rejection: does any `(C,K,r)` explain the six channels at a given RF?
2. multi-frequency physical-law rejection: do the recovered `gamma(omega)` values lie on one homogeneous `(D,w,kappa)` dispersion law?

Rev. 1 emphasizes the second and describes the first only through the raw `10^-4` residual.

This makes the phrase

> “survive both the calibrated same-frequency one-mode spectral manifold and the low-RF homogeneous drift-diffusion dispersion manifold”

statistically asymmetric.

### Required repair

After completing M2, present the two rejection layers with parallel notation and explicit assumptions. This may become one of the paper's strongest conceptual contributions:

```text
channel-space normal distance
    versus
frequency-law normal distance.
```

If the numerical ordering is unfavorable, report it honestly and narrow the claim.

**Severity: major.**

---

## M6. The HgCdTe realism section is an order-of-magnitude plausibility check, not validation of the false-D magnitude

The comparison

```text
Paper-02 added average field = 166.7 V/cm
published graded field       ~100--200 V/cm
```

is useful. However, the modeled field is a particular electrostatic potential profile under `0.30 V` bias and velocity saturation, whereas the published field is a composition-gradient built-in field in a different device architecture.

The same nominal `V/cm` does not guarantee the same `v(z)`, kernel overlap, junction field, carrier species, or terminal-current response.

Rev. 1 already contains caveats, but the wording “conditional HgCdTe stress uses thickness and internal-field scales independently reported” could still be read too strongly.

### Required repair

Keep the comparison, but make its logical status explicit in the first sentence of the section:

> “This section checks only whether the geometric and effective-field scales are demonstrated in HgCdTe; it does not validate the modeled velocity profile or the predicted `D_eff` for any published detector.”

Also distinguish the modeled **added nonuniform field scale** from the total applied-bias field.

**Severity: moderate-to-major.**

---

## M7. The title is slightly narrower than the actual theorem stack

The title says “Electrostatic heterogeneity,” while the most general checked result is written in terms of deterministic velocity heterogeneity and is demonstrated using prescribed velocity profiles not explicitly generated by electrostatics.

This is not wrong, because electrostatics are the detector-level physical motivation and conditional stress. But a hostile reader can ask whether the title claims a field theorem when the general numerical test is a velocity-profile theorem.

### Options

1. retain the current title and make the electrostatic origin of `v(z)` explicit as the target application;
2. use the more exact title

> **Deterministic velocity heterogeneity as apparent diffusion in wavelength-resolved photodetector transport**

3. use a broader but less mechanistic title

> **Device heterogeneity as apparent diffusion in wavelength-resolved photodetector transport**.

The second is scientifically tightest at present.

**Severity: moderate.**

---

# Prior-art and citation comments

## P1. The manuscript is under-cited for submission

The current bibliography is a boundary bibliography, not yet a submission bibliography. It lacks at least:

- original/standard Shockley--Ramo references;
- standard drift--diffusion / photodiode transit-response references;
- older absorption-depth / PIN response literature cited by the OED and PDA papers;
- the cross-domain apparent-diffusion/migration source that motivated narrowing the novelty claim;
- appropriate statistical/inverse references if the noncentral-chi-square and tangent-space machinery are presented as general tools rather than derived from first principles.

Rev. 2 need not reach the final 45--65 references, but the introduction/discussion should no longer make the literature landscape look artificially sparse.

## P2. Bibliographic metadata must be verified before submission

`PAPER02_REFERENCES.bib` intentionally contains provisional metadata. Some author lists are abbreviated and one or more titles may be paraphrased from search metadata. This is acceptable for Rev. 1 but not for submission.

Use publisher/primary-source metadata during Rev. 2/Rev. 3 bibliography hardening.

## P3. Generic apparent-diffusion novelty is closed

The paper must retain the boundary that electric-field-driven migration/heterogeneity being absorbed into an apparent diffusion coefficient is not a generally new inverse phenomenon. The detector-specific contribution is the finite-generation-kernel / Shockley--Ramo / double-manifold survival and quantitative attribution framework.

---

# Statistical and numerical comments

## S1. The 90--130 dB channel SNR numbers are easy to misread

Rev. 1 correctly defines the SNR relative to RMS full-channel amplitude, but most detector readers will instinctively compare the numbers to ordinary photocurrent or lock-in SNR. Add one sentence that the large values arise because the root is encoded in small inter-channel differential structure after two complex nuisance directions `(C,K)` are profiled out.

## S2. The end-to-end noise model is illustrative, not optimal

Equal SNR across all RF points, independent channels, and no calibration covariance is a useful reference case, not an experimental optimum. The manuscript should avoid presenting the SNR curve as a fundamental lower bound.

## S3. Kernel uncertainty is currently absent

The phrase “known/calibrated kernels” is an assumption. Real uncertainty in `g_m(z)` would itself create tangent and normal channel errors. This should be listed as an omitted nuisance in Discussion.

## S4. Finite-kernel generality is demonstrated with one conditional kernel family

The analytic leakage theorem is general, but the numerical false-positive magnitude is demonstrated with one HgCdTe-like six-kernel family. Do not imply that comparable `D_eff` magnitudes occur for arbitrary finite kernels. The sign-controlled velocity-profile generality is stronger than the kernel-family generality.

---

# Presentation comments

## T1. Rev. 1 is already close to a coherent paper, but it is still too theorem-dense in the middle

The manuscript should not reproduce the full derivational history. Keep the main text to the shortest derivations needed to establish:

1. local deterministic apparent diffusion;
2. remote support leakage;
3. profiled parameter bias;
4. statistical rejection.

Move algebraic details of Eq. `a2(z)`, full covariance derivation, and finite-spacing formulas to supplement if necessary.

## T2. “False diffusion” should remain secondary terminology

The paper is strongest when it says

```text
apparent/effective diffusion of the imposed homogeneous model
```

and reserves “false” for the **microscopic attribution**.

## T3. The mean-preserving control needs an explicit statement that the tilted kernels are mathematical causal controls

They are not claimed to correspond to a realizable optical material or spectrum. State this near the result, not only in repository notes.

---

# Referee decision

**Major revision.**

The work is scientifically interesting and the core counterexample appears internally consistent, but publication quality depends on closing M1--M5. M2 is the most important new numerical gate because it can change the strength of the manuscript's central “hidden confound” claim.

Recommended revision order:

```text
1. run covariance-aware same-frequency one-mode rejection test;
2. compare same-frequency rejection SNR with D-detection SNR;
3. explicitly connect H_z to gamma_loc in the theorem;
4. narrow support/mean causal language;
5. document the conditional kernel construction;
6. harden HgCdTe realism language;
7. update title if appropriate;
8. expand/verify bibliography;
9. create Rev. 2 and compile independently.
```
