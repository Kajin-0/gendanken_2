# Paper 03 Stage-B operating-state validation lock

**Date:** 2026-08-17  
**Status:** **GENERIC VALIDATION CONTRACT / NON-CLAIM**

This is the first executable Stage-B layer under `PAPER03_STAGEB_MODEL_SPEC_2026-08-17.md`. It validates the coupled dark/bias Poisson + electron-continuity machinery before any detector-response or HgCdTe-specific interpretation. The authoritative result is the committed GitHub Actions run; a local implementation smoke test was used only to check algebra/runtime and is not scientific evidence.

## Synthetic validation structure

```text
W = 16 um; L = 7.6 um
eps_r = 12; T = 100 K
mu_n = 0.50 m^2/(V s); N_D = 1.0e19 m^-3
D_n = mu_n kT/q
finite selected top contact fraction = 0.75
full bottom contact; remaining top and side boundaries insulating
bottom: psi=0, n=N_D
built-in selected-top offset = -10 mV
top reservoir n = N_D exp(V_bi/V_T)
finite-bias validation: +30 mV external bias
```

These are explicit **synthetic validation values**, not HgCdTe literature parameters. At zero external bias `ln(n)-psi/V_T` is equal at both contacts under the code sign convention, giving an equilibrium-compatible zero-current test while retaining nontrivial self-consistent charge redistribution.

## Sign convention

```math
-\nabla\cdot(\epsilon\nabla\psi)=q(N_D-n),
```

```math
\mathbf E=-\nabla\psi,
```

```math
\mathbf J_n=-q\mu_n n\nabla\psi+qD_n\nabla n,
```

with `D_n=mu_n kT/q`. Carrier fluxes use Scharfetter--Gummel exponential fitting and the coupled state uses damped Gummel iteration.

## Locked gates for this layer

1. Constant-charge full-parallel-plate Poisson test: finest maximum potential error `<5e-6 V` and final refinement error reduction factor `>3` on `9x16 / 9x31 / 9x61`.
2. Neutral `n=N_D` full-contact limit: linear potential recovered to `<1e-12 V` maximum error.
3. Equilibrium-compatible coupled finite-contact state: Poisson and continuity relative residuals `<1e-8`, positive finite `n`, and all terminal/cut currents `<1e-8 A` per metre out-of-plane depth.
4. Finite-bias coupled state: both residuals `<1e-8`, positive finite `n`, horizontal-cut current nonconservation `<1e-5`, terminal imbalance `<1e-5`.
5. Nontrivial coupling: finite-bias `min(n/N_D)<0.80`; a neutral Laplace state is insufficient.

The coupled validation uses `31x23` only. This is deliberately **not** the Stage-B mesh-convergence gate.

Passing this layer does not establish three-mesh detector convergence, weighting/Ramo validation, small-signal spectral/RF transport, backward/forward reciprocity, HgCdTe material realism, blind-analysis success, Stage-B numerical establishment, or Paper-03 GO.