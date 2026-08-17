# Published-HgCdTe scale check for Paper 02

**Date:** 2026-08-15  
**Status:** **CHECKED ORDER-OF-MAGNITUDE REALISM / NOT A CALIBRATED DEVICE PREDICTION / PRIORITY UNPROVEN**

## 1. Purpose

The Paper-02 mechanism is now analytically and numerically established in conditional theoretical models. The remaining realism question is whether its device dimensions and electrostatic perturbation are obviously outside demonstrated HgCdTe scales.

This note compares the existing stress model against independently published graded-HgCdTe structures. No fitting to those papers is performed.

The comparison is intentionally conservative:

> matching order of magnitude is evidence that the theoretical nuisance is physically plausible; it is **not** evidence that the published device has the predicted false diffusion coefficient.

---

## 2. Paper-02 conditional stress

The fine planar-depletion stress uses

```text
absorber thickness              L = 7.6 um
nonuniform collector-side width Wd = 3.0 um
total applied model bias        Vbias = 0.30 V
space-charge/depletion drop     Vsc = 0.05 V
microscopic diffusion           D = 0
recombination                   = 0
```

The added electrostatic drop corresponds to the average field scale

```math
\boxed{
E_{\rm sc,avg}=\frac{0.05\ \mathrm V}{3.0\ \mu\mathrm m}
=1.667\times10^4\ \mathrm{V/m}
=166.7\ \mathrm{V/cm}.
}
```

The total-bias average field scale is

```math
\frac{0.30\ \mathrm V}{7.6\ \mu\mathrm m}
=394.7\ \mathrm{V/cm}.
```

For the particular quadratic space-charge surrogate used by the finite-difference solver, the field changes across the 3 um region by a scale

```math
\Delta E_{\rm sc}
\sim\frac{2V_{\rm sc}}{W_d}
=333.3\ \mathrm{V/cm}.
```

The last number is a property of the chosen surrogate and should not be compared one-to-one with a published composition-gradient field. The most direct scale comparison is the integrated drop / average added field, `166.7 V/cm`.

---

## 3. Published 2023 graded HgCdTe structure

Primary source:

G.-Q. Xu et al.,
“Photoelectric characteristics of compositionally graded HgCdTe detector,”
*Journal of Infrared and Millimeter Waves* **42** (2023) 285–291,
DOI `10.11972/j.issn.1001-9014.2023.03.001`.

The paper fabricated two N-on-P devices after removing different amounts of a compositionally graded VPE HgCdTe layer.

The reported processed thicknesses are approximately

```math
\boxed{L_A\approx7.6\ \mu\mathrm m}
```

and

```math
\boxed{L_B\approx3.7\ \mu\mathrm m}.
```

Sample A retains part of the nonlinear composition region; sample B removes it.

The authors calculate composition-gradient built-in electric fields of roughly

```math
\boxed{100\text{--}200\ \mathrm{V/cm}}
```

in the linear-composition region and local surface values as high as approximately

```math
\boxed{2000\ \mathrm{V/cm}}
```

when the nonlinear composition region is retained.

They identify the composition-gradient built-in field acting on minority-carrier motion as the principal reason for the observed differences in photoelectric response between the samples.

---

## 4. Direct scale comparison

The clean comparison is

| Quantity | Paper-02 stress | Published 2023 HgCdTe |
|---|---:|---:|
| absorber/device layer scale | 7.6 um | sample A ~7.6 um |
| nonuniform-field average scale | 166.7 V/cm added over 3 um | ~100–200 V/cm in linear graded region |
| stronger local field scale | surrogate field variation ~333 V/cm | nonlinear surface field up to ~2000 V/cm |

The Paper-02 stress therefore does **not** require an order-of-magnitude larger field than a demonstrated graded HgCdTe structure.

In fact, its average added electrostatic field

```math
166.7\ \mathrm{V/cm}
```

falls directly inside the published

```math
100\text{--}200\ \mathrm{V/cm}
```

linear-composition field range.

Its chosen total thickness is numerically the same as the reported final thickness of sample A.

This comparison was not used to choose or tune the Paper-02 model parameters; the theoretical geometry already used `L=7.6 um`, `Wd=3 um`, and `Vsc=0.05 V` before this realism audit.

---

## 5. Published 2022 high-speed graded HgCdTe structure

Primary source:

M. Sang, G. Xu, H. Qiao, and X. Li,
“High speed uncooled MWIR infrared HgCdTe photodetector based on graded bandgap structure,”
*Journal of Infrared and Millimeter Waves* **41** (2022) 972–979,
DOI `10.11972/j.issn.1001-9014.2022.06.005`.

The paper reports a room-temperature graded n-on-p HgCdTe detector whose composition-gradient built-in field changes minority-carrier transport.

At 300 K and zero external bias, the VPE device is reported with

```math
\boxed{t_{\rm response}\approx1.33\ \mathrm{ns}}
```

and a measured frequency response around

```math
\boxed{750\ \mathrm{MHz}}.
```

The authors explicitly attribute the faster response relative to their LPE comparison device to the larger composition-gradient built-in field.

This is independent evidence that composition-gradient fields in HgCdTe are large enough to materially alter carrier transit dynamics on sub-nanosecond / GHz-adjacent timescales.

---

## 6. Important tension: nuisance realism versus discrimination bandwidth

The published scale comparison strengthens the **existence/plausibility** side of Paper 02, but it also exposes an important practical limitation.

Under the explicit theoretical equal-quadrature-noise model in `PAPER02_END_TO_END_REJECTION_SNR_RESULT_2026-08-15.md`, rejection of the current zero-diffusion deterministic nuisance with 90% power at `alpha=0.0027` requires approximately

```text
usable band through 750 MHz   RMS-channel SNR ~7.56e4  = 97.6 dB
usable band through 1.0 GHz   RMS-channel SNR ~3.31e4  = 90.4 dB
usable band through 1.5 GHz   RMS-channel SNR ~9.91e3  = 79.9 dB
usable band through 2.0 GHz   RMS-channel SNR ~4.58e3  = 73.2 dB
usable band through 3.0 GHz   RMS-channel SNR ~1.63e3  = 64.2 dB
```

The published 2022 graded device reaches approximately `750 MHz` total frequency response.

Therefore a device can plausibly inhabit the field/thickness regime in which the nuisance matters **while still operating near a bandwidth where the wrong homogeneous model is statistically difficult to reject under the reference noise model**.

This is not a prediction for the Sang et al. detector because

- its exact optical kernels are not the Paper-02 kernels;
- its field profile is not the Paper-02 profile;
- its readout covariance is unknown here;
- its timing experiment used approximately 1.55 um excitation rather than the wavelength-programmed six-channel measurement;
- its zero-bias junction/device electrostatics differ from the conditional `0.30 V` stress.

The comparison instead establishes a design-level tension:

> nuisance-generating transport heterogeneity is already demonstrated at HgCdTe field and bandwidth scales close to the theoretical study, while decisive separation from homogeneous diffusion may require substantially more RF information or stronger independent electrostatic constraints.

---

## 7. Why the comparison is conservative

The Paper-02 stress uses an average added field of only `166.7 V/cm`.

The 2023 work reports local nonlinear-region surface fields up to about `2000 V/cm`, more than an order of magnitude larger.

Paper 02 does **not** infer that a 2000 V/cm region would generate a correspondingly larger false diffusion coefficient. Velocity saturation, region width, optical overlap, field sign, and inverse conditioning all matter.

The only safe conclusion is that the stress field scale is not obviously excessive relative to published HgCdTe internal fields.

---

## 8. What is established by this scale check

### CHECKED

1. The Paper-02 `7.6 um` device thickness is directly comparable to a published `~7.6 um` graded HgCdTe sample.
2. The Paper-02 `0.05 V / 3 um = 166.7 V/cm` added field scale falls inside a published `100–200 V/cm` composition-gradient built-in-field range.
3. Published graded HgCdTe devices demonstrate that composition-gradient fields materially change carrier transport.
4. A published room-temperature graded HgCdTe detector has demonstrated approximately `750 MHz` response, placing GHz-adjacent transport dynamics within the material/device family.

### NOT ESTABLISHED

1. The published devices have the Paper-02 false diffusion coefficient.
2. The published 2023 sample has the same 3 um nonuniform-region width.
3. The Paper-02 space-charge surrogate reproduces the published composition-gradient electrostatics.
4. The published detectors would require the Paper-02 SNR values for model rejection.
5. A real experiment with the exact six wavelength kernels is feasible at the stated precision.

---

## 9. Gate-B verdict

The independent-realistic-scale gate is now substantially passed at the **order-of-magnitude physical plausibility** level:

```text
Paper-02 thickness scale     -> independently demonstrated
Paper-02 internal-field scale -> independently demonstrated
sub-GHz / GHz-adjacent HgCdTe transport response -> independently demonstrated
```

The result is therefore no longer defensibly dismissible as a counterexample built from an obviously unphysical electrostatic scale.

A fully calibrated real-device prediction remains future work and is not required for the present theoretical identifiability paper, provided the manuscript is explicit about the distinction.

---

## 10. Remaining publication gate

After this check, the dominant blocker is **priority**, not mechanism or scale.

Before drafting a standalone manuscript, the exact claim must still survive full-text comparison against the closest lineages:

- optoelectronic chromatic dispersion in photodiodes;
- partially depleted absorber modeling;
- inhomogeneous-field TOF transport inference;
- terminal-current/weighting-field inverse analyses;
- effective-diffusion descriptions of deterministic velocity heterogeneity.

If that audit does not reveal a direct collision, Paper 02 has enough analytical spine, causal controls, statistical design, and independent physical scale to justify manuscript drafting.
