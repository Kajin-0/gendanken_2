# Paper 02 exact planar continuum cross-check

**Status:** **CHECKED POST-HOC EXACT-CONTINUUM CROSS-CHECK**

> This check was designed after the mesh-refinement result was known. It is therefore post-hoc and is not represented as a predeclared convergence gate.

The full-contact central stress has an exact one-dimensional electrostatic solution and planar weighting potential. This calculation removes the 2-D field mesh and trajectory stepping from the central inference and then applies the same six optical kernels and kernel-aware inverse.

## Exact-continuum inference

| RF | D_eff (m^2/s) | w_eff (m/s) | kernel-fit residual |
|---:|---:|---:|---:|
| 100 MHz | 2.618164535e-03 | 25693.305623 | 1.646618714e-05 |
| 500 MHz | 2.550830551e-03 | 25750.169102 | 8.346657244e-05 |
| 1000 MHz | 2.350617904e-03 | 25916.711843 | 1.741489437e-04 |

Low-band joint fit: `D=2.610343976e-03 m^2/s`, `w=25698.619292 m/s`.

100-MHz-anchored homogeneous-law residual at 1 GHz: `8.916297357e-03`.

## Numerical baseline versus exact continuum

| Metric | Numerical baseline | Exact continuum | Difference | Existing tolerance scale | Pass |
|---|---:|---:|---:|---:|:---:|
| D_eff_m2_per_s_100MHz | 2.609795073e-03 | 2.618164535e-03 | 3.196690271e-03 (rel) | 2.000000000e-02 | PASS |
| w_eff_m_per_s_100MHz | 2.570098362e+04 | 2.569330562e+04 | 2.988324467e-04 (rel) | 5.000000000e-03 | PASS |
| D_eff_m2_per_s_500MHz | 2.548603223e-03 | 2.550830551e-03 | 8.731775949e-04 (rel) | 2.000000000e-02 | PASS |
| w_eff_m_per_s_500MHz | 2.575775760e+04 | 2.575016910e+04 | 2.946970559e-04 (rel) | 5.000000000e-03 | PASS |
| D_eff_m2_per_s_1000MHz | 2.348944891e-03 | 2.350617904e-03 | 7.117335754e-04 (rel) | 2.000000000e-02 | PASS |
| w_eff_m_per_s_1000MHz | 2.592405241e+04 | 2.591671184e+04 | 2.832369240e-04 (rel) | 5.000000000e-03 | PASS |
| low_band_D_eff_m2_per_s | 2.606303328e-03 | 2.610343976e-03 | 1.547936813e-03 (rel) | 2.000000000e-02 | PASS |
| low_band_w_eff_m_per_s | 2.570628883e+04 | 2.569861929e+04 | 2.984414691e-04 (rel) | 5.000000000e-03 | PASS |
| law_residual_1ghz | 8.885176173e-03 | 8.916297357e-03 | 3.112118317e-05 (abs) | 2.000000000e-03 | PASS |
| max_kernel_fit_rel_through_1ghz | 1.738486964e-04 | 1.741489437e-04 | 3.002473436e-07 (abs) | 2.000000000e-05 | PASS |

## Exact point-source controls

Upstream sequence: `D_eff=4.491894823e-11 m^2/s`.

Inside-region sequence: `D_eff=4.870585772e-03 m^2/s`.

## Interpretation

Agreement here strengthens numerical attribution inside the declared deterministic surrogate. It does not establish experimental kernel calibration, device-level uniqueness, experimental feasibility, or novelty priority.
