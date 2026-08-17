# Paper 02 — Canonical Figure Bundle Index

**Date:** 2026-08-15  
**Status:** **CHECKED / REPRODUCIBLE WORKING FIGURES**  
**Purpose:** freeze the scientific data/plot spine before manuscript drafting. These are working publication panels, not yet a journal-specific final layout.

## 1. Reproducibility record

Workflow:

```text
.github/workflows/paper02-figure-bundle.yml
```

Builder:

```text
experiments/01-vanishing-absorber/numerics/paper02_build_figure_bundle.py
```

GitHub Actions run:

```text
run id       31918929841
artifact     paper02-canonical-figure-bundle
artifact id  9255770675
```

Downloaded artifact SHA-256:

```text
30820eb6564a4fdb827bf6350e83ffaf73454fa9bb414e35335cac255a1b8a3e
```

The workflow regenerated all source datasets from executable branch code before plotting. No research-note values were manually copied into the figures.

---

## 2. Artifact contents

Vector PDF and 300-dpi PNG versions are present for seven panels:

```text
paper02_figures/fig1_generation_kernels.pdf
paper02_figures/fig1_generation_kernels.png

paper02_figures/fig2_apparent_diffusion_velocity_profiles.pdf
paper02_figures/fig2_apparent_diffusion_velocity_profiles.png

paper02_figures/fig3_tail_ablation.pdf
paper02_figures/fig3_tail_ablation.png

paper02_figures/fig3b_remote_overlap.pdf
paper02_figures/fig3b_remote_overlap.png

paper02_figures/fig4_bias_law_validation.pdf
paper02_figures/fig4_bias_law_validation.png

paper02_figures/fig5_required_snr_vs_bandwidth.pdf
paper02_figures/fig5_required_snr_vs_bandwidth.png

paper02_figures/fig5b_refitted_diffusion_vs_bandwidth.pdf
paper02_figures/fig5b_refitted_diffusion_vs_bandwidth.png
```

Canonical source tables included in the same artifact:

```text
paper02_independent_velocity_profiles_results.csv
paper02_kernel_tail_ablation_results.csv
paper02_kernel_tail_ablation_overlap.csv
paper02_bias_bound_linearization.csv
paper02_end_to_end_rejection_bands.csv
paper02_end_to_end_rejection_frequency.csv
```

---

## 3. Panel meanings

### Figure 1 — finite calibrated generation kernels

Shows the six HgCdTe generation kernels across absorber depth together with the collector-side nonuniform-velocity region.

Scientific role:

- makes clear that every nominal mean source coordinate lies upstream of the region boundary;
- shows visually that finite kernel support nevertheless extends into the region;
- motivates why mean generation depth alone is an insufficient attribution coordinate.

This panel should appear near the initial measurement-model definition.

### Figure 2 — sign-controlled apparent diffusion

Plots recovered homogeneous `D_eff` against downstream endpoint-velocity ratio for independent linear and exponential deterministic velocity families.

Core visual result:

```text
R < 1  -> D_eff < 0
R = 1  -> D_eff ~= 0
R > 1  -> D_eff > 0
```

Scientific role:

- establishes sign-sensitive generality beyond the original electrostatic solver;
- demonstrates that positive apparent diffusion follows downstream acceleration rather than numerical noise;
- should be one of the main-text figures.

### Figure 3 — remote-tail causal ablation

Plots `D_eff` while continuously scaling only the generation-kernel weight inside the nonuniform region.

Scientific role:

- direct causal manipulation of remote-region optical support;
- shows monotonic recovery of positive apparent diffusion as the physical tail is restored;
- complements, but does not replace, the stronger mean-preserving zero-overlap control.

A final manuscript figure should probably add the mean-preserving zero-overlap result as a highlighted point/bar or adjacent panel.

### Figure 3b — physical remote overlap

Plots each physical channel's generation probability inside the nonuniform region against its mean generation depth.

Current physical overlaps:

```text
2.0 um mean   0.60 %
2.5 um mean   1.65 %
3.0 um mean   4.20 %
3.5 um mean   9.78 %
4.0 um mean  20.60 %
4.5 um mean  38.89 %
```

Scientific role:

- quantifies the optical exposure variable `p_{m,R}` used in the leakage theorem;
- provides a compact bridge from the physical kernels to the parameter-bias bound.

### Figure 4 — first-order parameter-bias validation

Compares predicted and independently refitted `Delta D` for weak linear and exponential velocity perturbations.

Scientific role:

- validates that the tangent-space bias law quantitatively predicts the nonlinear inverse;
- supports the claim that the paper provides a reusable attribution calculation rather than only a counterexample.

For `|epsilon| <= 0.002`, the underlying data give maximum relative errors of approximately

```text
complex root shift   2.65e-6
propagated D          3.53e-4
```

The unity agreement is visually strong.

### Figure 5 — required channel SNR versus RF bandwidth

Plots the RMS-channel SNR required for 90% rejection power at `alpha=0.0027` under the explicit independent equal-quadrature noise model, after jointly re-fitting the wrong homogeneous `D,w` model over every cumulative RF band.

Key values:

```text
through 1.0 GHz   90.4 dB
through 1.5 GHz   79.9 dB
through 2.0 GHz   73.2 dB
through 3.0 GHz   64.2 dB
```

Scientific role:

- converts structural overdetermination into an actual experimental-design statement;
- shows that bandwidth can contribute much more nuisance discrimination than extreme precision confined to the low-RF tangent regime.

### Figure 5b — re-fitted homogeneous diffusion versus bandwidth

Shows the best-fit wrong homogeneous `D` as the fitting band expands.

Scientific role:

- makes clear that the nuisance does not abruptly fail at a single RF point;
- the wrong model continuously sacrifices parameter consistency to remain near the data;
- justifies using a profiled covariance-weighted model-manifold distance instead of one fixed-parameter residual.

This panel is naturally paired with Figure 5.

---

## 4. Visual QA

The generated PNGs were inspected after the workflow completed.

Checked:

```text
all seven panels rendered
axes and labels visible
no clipped legends
no empty datasets
no obvious unit mismatch
no obvious sign reversal relative to canonical numerical records
PDF and PNG counterparts present
```

The current plots intentionally use plain scientific Matplotlib defaults rather than decorative styling. Final journal styling can adjust typography, line weights, panel lettering, and multi-panel composition without changing scientific content.

Figure 1 has the densest legend and will likely benefit from a more compact final manuscript composition, but the data representation is readable and scientifically correct.

---

## 5. Canonical figure-data mapping

```text
Fig. 1
<- calibrated optical kernels from realistic_geometry_closure_stress.py

Fig. 2
<- paper02_independent_velocity_profiles_results.csv
<- paper02_independent_velocity_profiles.py

Fig. 3 / 3b
<- paper02_kernel_tail_ablation_results.csv
<- paper02_kernel_tail_ablation_overlap.csv
<- paper02_kernel_tail_ablation.py

Fig. 4
<- paper02_bias_bound_linearization.csv
<- paper02_bias_bound_linearization.py

Fig. 5 / 5b
<- paper02_end_to_end_rejection_bands.csv
<- paper02_end_to_end_rejection_frequency.csv
<- paper02_end_to_end_rejection_snr.py
```

The mean-preserving zero-overlap causal control is currently documented numerically but is not yet included in the canonical plot bundle. It should be incorporated into the final Figure 3 composition during manuscript figure layout.

---

## 6. Drafting rule

When drafting Paper 02, numerical values in the main figures and captions should come from this canonical bundle or directly from the associated scripts/artifacts.

Do not manually reconstruct plots from prose notes.

If a scientific quantity changes, regenerate the dataset and figure bundle through the workflow, then update this index rather than editing figure values by hand.
