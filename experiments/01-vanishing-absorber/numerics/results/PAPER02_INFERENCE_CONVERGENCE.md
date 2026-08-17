# Paper 02 inference convergence gate

**Overall:** PASS

This report tests numerical convergence of the inferred transport quantities, not only the raw closure phase.

## Field Mesh

| Metric | Coarse | Baseline | Fine | Final change | Tolerance | Gate |
|---|---:|---:|---:|---:|---:|:---:|
| D_100 | 0.0025265151 | 0.0026097951 | 0.0026535369 | 0.0165 | 0.02 | PASS |
| D_500 | 0.0024676836 | 0.0025486032 | 0.0025911236 | 0.0164 | 0.02 | PASS |
| D_1000 | 0.0022748093 | 0.0023489449 | 0.0023879485 | 0.0163 | 0.02 | PASS |
| w_100 | 25791.595 | 25700.984 | 25654.761 | 0.0018 | 0.005 | PASS |
| w_500 | 25846.393 | 25757.758 | 25712.567 | 0.00176 | 0.005 | PASS |
| w_1000 | 26006.945 | 25924.052 | 25881.865 | 0.00163 | 0.005 | PASS |
| D_low | 0.0025233312 | 0.0026063033 | 0.0026498865 | 0.0164 | 0.02 | PASS |
| w_low | 25796.716 | 25706.289 | 25660.163 | 0.0018 | 0.005 | PASS |
| law_residual_1ghz | 0.008550548 | 0.0088851757 | 0.0090603803 | 0.000175 | 0.002 | PASS |
| max_kernel_fit_1ghz | 0.00016742979 | 0.0001738487 | 0.00017720974 | 3.36e-06 | 2e-05 | PASS |
| D_out | -2.627984e-12 | 1.9037663e-12 | 8.6053765e-12 | 2.53e-09 | 0.01 | PASS |
| D_in | 0.0048757113 | 0.0048710536 | 0.0048686998 | 0.000483 | 0.02 | PASS |

## Source Quadrature

| Metric | Coarse | Baseline | Fine | Final change | Tolerance | Gate |
|---|---:|---:|---:|---:|---:|:---:|
| D_100 | 0.00261003 | 0.0026097951 | 0.0026097082 | 3.33e-05 | 0.02 | PASS |
| D_500 | 0.0025488384 | 0.0025486032 | 0.0025485159 | 3.43e-05 | 0.02 | PASS |
| D_1000 | 0.0023491799 | 0.0023489449 | 0.0023488566 | 3.76e-05 | 0.02 | PASS |
| w_100 | 25700.86 | 25700.984 | 25701.036 | 2.03e-06 | 0.005 | PASS |
| w_500 | 25757.637 | 25757.758 | 25757.809 | 2e-06 | 0.005 | PASS |
| w_1000 | 25923.94 | 25924.052 | 25924.102 | 1.9e-06 | 0.005 | PASS |
| D_low | 0.0026065383 | 0.0026063033 | 0.0026062164 | 3.34e-05 | 0.02 | PASS |
| w_low | 25706.166 | 25706.289 | 25706.341 | 2.03e-06 | 0.005 | PASS |
| law_residual_1ghz | 0.0088855962 | 0.0088851757 | 0.0088850529 | 1.23e-07 | 0.002 | PASS |
| max_kernel_fit_1ghz | 0.00017386241 | 0.0001738487 | 0.00017384002 | 8.67e-09 | 2e-05 | PASS |
| D_out | 1.9037663e-12 | 1.9037663e-12 | 1.9037663e-12 | 0 | 0.01 | PASS |
| D_in | 0.0048710536 | 0.0048710536 | 0.0048710536 | 0 | 0.02 | PASS |

## Trajectory Step

| Metric | Coarse | Baseline | Fine | Final change | Tolerance | Gate |
|---|---:|---:|---:|---:|---:|:---:|
| D_100 | 0.0026098231 | 0.0026097951 | 0.0026098081 | 5e-06 | 0.02 | PASS |
| D_500 | 0.0025486253 | 0.0025486032 | 0.0025486179 | 5.76e-06 | 0.02 | PASS |
| D_1000 | 0.0023489508 | 0.0023489449 | 0.0023489642 | 8.21e-06 | 0.02 | PASS |
| w_100 | 25700.951 | 25700.984 | 25700.962 | 8.43e-07 | 0.005 | PASS |
| w_500 | 25757.728 | 25757.758 | 25757.735 | 8.61e-07 | 0.005 | PASS |
| w_1000 | 25924.029 | 25924.052 | 25924.029 | 8.99e-07 | 0.005 | PASS |
| D_low | 0.0026063307 | 0.0026063033 | 0.0026063165 | 5.07e-06 | 0.02 | PASS |
| w_low | 25706.256 | 25706.289 | 25706.267 | 8.45e-07 | 0.005 | PASS |
| law_residual_1ghz | 0.0088855807 | 0.0088851757 | 0.0088851082 | 6.75e-08 | 0.002 | PASS |
| max_kernel_fit_1ghz | 0.00017383144 | 0.0001738487 | 0.00017385017 | 1.47e-09 | 2e-05 | PASS |
| D_out | 1.0843296e-08 | 1.9037663e-12 | 1.59686e-12 | 1.18e-10 | 0.01 | PASS |
| D_in | 0.004871081 | 0.0048710536 | 0.0048710462 | 1.53e-06 | 0.02 | PASS |

## Integrity checks

- **baseline**: PASS
- **mesh_coarse**: PASS
- **mesh_fine**: PASS
- **quadrature_coarse**: PASS
- **quadrature_fine**: PASS
- **step_coarse**: PASS
- **step_fine**: PASS

## Interpretation boundary

A PASS establishes numerical stability of this deterministic surrogate and its inverse under the declared refinement tests. It does not establish experimental feasibility, device calibration, or uniqueness of the physical interpretation.
