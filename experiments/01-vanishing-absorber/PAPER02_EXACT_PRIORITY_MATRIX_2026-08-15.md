# Paper 02 — Exact Priority Matrix

**Date:** 2026-08-15  
**Status:** **FOCUSED PRIORITY AUDIT — DISTINCT COMBINATION STILL PLAUSIBLE; SUPERLATIVE NOVELTY CLAIMS NOT AUTHORIZED**  
**Rule:** `NOT LOCATED` means only that the present focused search did not find the item. It is not evidence of novelty.

## 1. Claim being audited

The candidate standalone claim has been narrowed to:

> In a wavelength-resolved semiconductor photodetector, calibrated finite generation-depth kernels can overlap a spatially remote deterministic velocity/electrostatic heterogeneity and drive a Shockley-Ramo terminal-current inverse to a positive, apparently admissible homogeneous diffusion coefficient even when microscopic diffusion is exactly zero. The resulting nuisance can remain close to both the calibrated same-frequency one-mode spectral manifold and the homogeneous low-RF drift-diffusion dispersion manifold. Its parameter bias is controlled by restricted kernel support and inverse conditioning, and its eventual rejection is a covariance/bandwidth problem.

Every broader component of that sentence has prior art. The audit asks whether the **integrated detector-specific inverse-identifiability result** is already present.

---

## 2. Comparison dimensions

Each source family is compared on the following dimensions:

1. **photodetector terminal-current observable**;
2. **wavelength-programmed / absorption-depth coordinate**;
3. **finite calibrated generation kernels** rather than a point-depth shorthand;
4. **spatially nonuniform deterministic field/velocity nuisance**;
5. **inverse target is a material diffusion coefficient or homogeneous transport parameter**;
6. **demonstrates positive apparent `D` from true microscopic `D=0`**;
7. **same-frequency spectral model/manifold can remain accepted**;
8. **multi-RF homogeneous transport law can remain approximately accepted over finite bandwidth**;
9. **zero-overlap or mean-preserving kernel-support causal control**;
10. **closed-form channel-to-root/material parameter-bias law**;
11. **covariance-aware statistical rejection/bandwidth criterion**.

The last six dimensions are the strongest separators from broad neighboring work.

---

## 3. Matrix

Legend:

```text
YES          clearly present in the cited work/family
PARTIAL      related but materially different
NO           source objective/model excludes the item
NOT LOCATED  not found in the present source/search; not novelty evidence
N/A          not meaningful for that source
```

| Source / lineage | 1 terminal-current photodetector | 2 wavelength/depth coordinate | 3 finite kernels | 4 deterministic field/velocity nuisance | 5 inverse target material D/transport | 6 positive apparent D with true D=0 | 7 spectral-manifold survival | 8 multi-RF homogeneous-law survival | 9 support ablation | 10 parameter-bias law | 11 statistical rejection |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Glasser et al. OED, *Opt. Express* 2021 | YES | YES | PARTIAL/YES optical absorption profile | PARTIAL device transport model | NO — wavelength/OED target | NOT LOCATED | N/A | PARTIAL — RF phase vs modulation frequency, not false transport-law acceptance | NO | NO | NO |
| Liokumovitch et al. OED, *Opt. Lett.* 2021/2022 | YES | YES | PARTIAL | PARTIAL | NO — wavelength sensing | NOT LOCATED | N/A | PARTIAL | NO | NO | NO |
| Dutta et al. PIN OED, *Opt. Lett.* 2024 | YES | YES | PARTIAL | YES/PARTIAL — bias/depletion width changes OED | NO — OED tuning | NOT LOCATED | N/A | PARTIAL | NO | NO | NO |
| Mudgal et al. PN Si OED, *Opt. Lett.* 2024 | YES | YES | PARTIAL | PARTIAL | NO — OED characterization | NOT LOCATED | N/A | PARTIAL | NO | NO | NO |
| Kassa et al. multi-frequency OED spectroscopy, arXiv 2026 | YES | YES | physics encoded implicitly in measured device | device physics implicit | NO — spectral reconstruction | NOT LOCATED | data-driven feature space, not one-mode transport test | YES multi-frequency RF features, but not homogeneous transport-law acceptance | NO | NO | ML uncertainty, not nuisance-model rejection |
| Hu et al. PDA simulation, *Opt. Express* 2015 | YES | YES/PARTIAL — absorption region/depletion structure | YES in forward optical generation | YES | NO — forward detector response/nonlinearity | NOT LOCATED | N/A | YES forward modulation-frequency response, but no false homogeneous-D inverse | NO | NO | NO |
| classical PIN transient diffusion modeling | YES | YES/PARTIAL | YES/PARTIAL | PARTIAL | YES/PARTIAL — mobility/diffusion can be model parameters | NOT LOCATED as true-D=0 false positive | N/A | PARTIAL | NO | NO | NO |
| Emelianova et al. inhomogeneous-field TOF 2006 | semiconductor transient, not spectral photodetector inverse | NO | NO | YES | YES — mobility/DOS inference | NO/NOT LOCATED for `D=0 -> D_app>0` | N/A | NO | NO | NO | NO |
| Hattori et al. SSPG, *PRB* 1992 | photocarrier transport, not terminal-current spectral-depth | optical grating, not wavelength depth | NO | YES space-charge/model assumption | YES — diffusion length | NO | N/A | NO | NO | NO | NO |
| Hawks et al. planar transient-current theory, *PR Applied* 2015 | YES / planar terminal-current theory | NO | NO | YES | mostly forward/current interpretation | NOT LOCATED | N/A | N/A | NO | NO | NO |
| Johnson et al. redox MOF, *Chemical Science* 2025 | NO photodetector | NO | NO | YES — electric-field migration | YES — apparent diffusion coefficient | **YES in broad inverse sense:** migration makes transient diffusion fit overestimate apparent D; true transport still has intrinsic diffusion, so not the Paper-02 zero-D construction | N/A | transient rather than RF manifold | NO | PARTIAL model correction, not Paper-02 kernel/root law | NO |
| **Current Paper-02 result** | **YES** | **YES** | **YES, exact calibrated kernels** | **YES** | **YES** | **YES, forward microscopic D exactly zero** | **YES, residual O(10^-4)** | **YES, sub-percent through ~1 GHz for stress case** | **YES, including mean-preserving zero-overlap** | **YES, analytically validated** | **YES, noncentral-chi-square end-to-end design** |

---

## 4. Source-by-source claim boundary

### 4.1 OED lineage — closest observable collision

The OED literature is the closest neighbor in **what is measured**.

The 2021 foundational work explicitly treats wavelength-dependent absorption depth and carrier migration as a source of wavelength-dependent RF phase in a photodiode. Later work amplifies/tunes that phase response, and the 2026 preprint uses RF amplitude and phase at 15 modulation frequencies as a high-dimensional inverse feature space for spectral reconstruction.

Therefore Paper 02 must not claim as new:

```text
wavelength-dependent absorption depth -> carrier delay
carrier delay -> RF phase/amplitude
multi-frequency photodiode RF features contain wavelength/depth information
bias/depletion width can change the wavelength-dependent RF response
```

The **target of inversion differs materially**. OED uses the device transport response to infer wavelength/spectrum. Paper 02 asks when that same general type of observable can falsely infer a material transport coefficient if deterministic device-level heterogeneity is omitted.

No OED source examined in this focused audit was found to:

- set microscopic diffusion identically to zero;
- recover a positive homogeneous diffusion coefficient from deterministic velocity heterogeneity;
- analyze acceptance of a calibrated one-mode transport manifold;
- establish mean-preserving zero-overlap causality;
- derive the Paper-02 root-bias/support bound;
- derive covariance-weighted rejection bandwidth for that false material attribution.

Status: **strong observable overlap, no direct collision located with the current inverse-identifiability claim.**

---

### 4.2 Partially depleted absorber / photodiode transport modeling — closest forward-physics collision

PDA and classical high-speed PIN literature already contains the physical ingredients that Paper 02 must treat as established:

- absorption outside/inside a high-field region;
- drift and diffusion contributions;
- finite optical generation distributions;
- spatial electric-field structure;
- modulation-frequency-dependent response.

The current Paper-02 contribution cannot be “these ingredients interact.”

The distinction is the **inverse failure mode**: a deterministic zero-diffusion heterogeneous forward model is deliberately fit with the wrong homogeneous diffusion model and is shown to produce a positive admissible `D_eff` while passing specific model checks.

No direct source in this family was located that performs that exact inverse experiment or derives the support/conditioning attribution law.

Status: **strong forward-model overlap; inverse-attribution result not located.**

---

### 4.3 Inhomogeneous-field TOF — closest transport-inference collision

The 2006 inhomogeneous-field TOF work is direct prior art for the proposition that assuming a homogeneous field can corrupt extracted semiconductor transport information. It reports that field inhomogeneity can overestimate mobility and create an apparent density-of-states distribution different from the actual one.

Therefore Paper 02 cannot claim that field inhomogeneity creating false transport parameters is a new general principle.

The remaining distinctions are:

- wavelength-programmed internal source coordinate;
- finite calibrated generation kernels;
- terminal-current Shockley-Ramo response;
- positive false **diffusion coefficient** from microscopic `D=0`;
- survival of both spectral and RF model-manifold tests;
- support-ablation causality and quantitative bias/rejection laws.

Status: **direct conceptual collision at transport-inference level; no exact diffusion/kernal/RF collision located.**

---

### 4.4 Space-charge / diffusion-length inversion — broad parameter-bias collision

The SSPG literature establishes that an incorrect electrostatic/local-neutrality assumption can severely bias a diffusion-related inferred quantity.

This blocks any broad claim such as:

> device electrostatics can make an inferred diffusion quantity wrong.

Paper 02 must instead be specific about its observable, true-zero-D construction, finite generation kernels, model-manifold survival, and attribution bound.

Status: **broad inverse-bias concept established.**

---

### 4.5 Planar transient-current theory — observation-operator collision

Modern planar transient-current theory already stresses that the externally measured terminal current includes device/electrode/displacement-current structure and cannot be equated naively with internal carrier motion.

This blocks any generic novelty claim about Shockley-Ramo/terminal-current observation complicating material inference.

Paper 02 uses that established observation physics to derive a narrower inverse-identifiability result.

Status: **observation principle established; specific false-D result not located.**

---

### 4.6 2025 redox-MOF apparent diffusion — important cross-domain collision

Johnson et al., *Chemical Science* 2025, is an important conceptual collision outside semiconductor photodetectors.

They show that electric fields arising during transient transport can introduce migration contributions that make a simplified transient diffusion analysis **overestimate an experimentally determined apparent diffusion coefficient**. Their model explains why migration and diffusion cannot always be separated by a simplistic transient fit.

This means the broad statement

> electric-field-driven deterministic/non-diffusive transport can be absorbed into an apparent diffusion coefficient by a simplified inverse model

is **not generally new**.

Differences from Paper 02:

- redox-conducting MOF rather than semiconductor photodetector;
- electrochemical potential-step transient rather than wavelength-programmed Shockley-Ramo RF response;
- no finite optical generation kernels;
- no remote optical-support theorem;
- no microscopic `D=0` sign-reversal construction of the current type;
- no calibrated spectral one-mode / RF dispersion double-survival result;
- no Paper-02 root-bias and bandwidth-rejection framework.

Status: **generic apparent-diffusion/migration inverse principle established cross-domain; detector-specific mechanism remains potentially distinct.**

---

## 5. Strongest safe novelty posture if a manuscript were drafted now

The present audit does **not** justify wording such as:

```text
first demonstration that electric fields can mimic diffusion
first proof that nonuniform transport biases diffusion
new fundamental relationship between velocity gradients and diffusion
first use of wavelength-dependent RF phase to probe internal transport
```

Those formulations are too broad and collide with existing literature.

A defensible working posture is narrower:

> We identify and quantify a specific material-attribution failure mode in wavelength-resolved photodetector transport measurements: finite calibrated generation-depth kernels can couple spatially remote deterministic velocity heterogeneity into a Shockley-Ramo terminal-current response that is locally indistinguishable from positive homogeneous diffusion, even when microscopic diffusion is zero. We derive support- and conditioning-based bias bounds, establish causal zero-overlap controls, and quantify the RF bandwidth/precision needed to reject the false homogeneous model.

Even this sentence should be labeled **candidate distinct contribution** until the remaining full-text checks are complete.

---

## 6. Priority risk by component

| Component | Priority risk | Assessment |
|---|---|---|
| wavelength-dependent absorption depth | CLOSED / established | old photodiode physics and OED |
| RF phase from carrier transit/diffusion | CLOSED / established | OED lineage |
| multi-frequency photodiode inverse features | CLOSED / established | 2026 OED spectroscopy |
| nonuniform field biases transport extraction | CLOSED / established | TOF literature |
| electrostatics biases diffusion-related inference | CLOSED / established | SSPG and broader transport literature |
| electric-field migration can inflate apparent diffusion | CLOSED / established generically | 2025 redox-MOF work and related transport theory |
| terminal-current observation complicates internal inference | CLOSED / established | planar transient-current theory |
| finite generation kernels overlapping remote nuisance region | medium | physical ingredient established; exact inverse support theorem not located |
| true microscopic `D=0` -> positive photodetector `D_eff` from deterministic `v(z)` | medium-low after focused search, **not proven novel** | no direct detector collision located |
| simultaneous survival of calibrated one-mode spectral fit and homogeneous low-RF dispersion fit | lower, **not proven novel** | no direct source located |
| mean-preserving zero-overlap causal ablation | lower, **not proven novel** | appears methodological to current work |
| noise-weighted channel-leakage -> root/D bias law | medium | generic inverse/Jacobian theory established; detector-specific instantiation distinctness uncertain |
| end-to-end covariance/bandwidth rejection design for false `D` | medium-low, **not proven novel** | generic statistics established; detector-specific application not located |
| entire integrated package | **plausibly distinct** | no direct collision located in current focused audit |

---

## 7. Current priority verdict

The audit supports the following conservative conclusion:

```text
Broad novelty:                 NO
Ingredient-level novelty:      mostly NO / generic theory overlap
Detector-specific mechanism:   CANDIDATE DISTINCT
Integrated inverse framework:  CANDIDATE DISTINCT
Priority confidence:           insufficient for “first” or “novel fundamental” wording
Standalone-paper viability:    YES, if framed as a narrow systematic-error / identifiability theory
```

The most promising publication strategy is therefore **not** to sell a new transport phenomenon.

It is to present a rigorous detector-inference result:

> a concrete, causally validated nuisance mechanism that aliases into microscopic diffusion, together with quantitative attribution and falsification criteria.

That framing is both scientifically stronger and more defensible against the prior art located so far.

---

## 8. Remaining exact-source checks

Before upgrading priority status beyond `CANDIDATE DISTINCT`, complete:

1. full-text comparison with the 2021 foundational OED theory paper, especially whether any model parameters are inverted from RF phase rather than only forward-predicted;
2. full-text 2024 PIN OED paper for its depletion-width/bias model and any inverse transport claims;
3. full-text 2015 PDA paper for any effective-parameter reduction of the spatially resolved simulation;
4. citation-chaining from the 2006 inhomogeneous-field TOF paper for prior false-diffusion-coefficient analyses;
5. citation-chaining from the 2025 redox-MOF paper for older migration-induced apparent-diffusion literature;
6. focused searches for semiconductor `apparent diffusion coefficient`, `effective diffusion coefficient`, and homogeneous-fit errors caused by deterministic field gradients.

If none of those reveal a direct detector-specific collision, the safe manuscript claim can move from `PRIORITY UNPROVEN` to `DISTINCT COMBINATION SUPPORTED BY FOCUSED AUDIT`, still without unsupported `first` language.
