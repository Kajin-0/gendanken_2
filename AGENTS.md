# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gendanken_2`  
**Active experiment:** `experiments/01-vanishing-absorber/`  
**Current mode:** **open theoretical exploration; active frontier is finite-length HgCdTe high-field transport and nonlocal impact ionization; no novelty claim**

Read this file first.

The project follows the physics rather than a predetermined theorem. Counterexamples, corrections, and prior-art collisions are progress.

## 1. Mandatory repository protocol

Other agents may edit `main` concurrently.

Before every write:

1. fetch live `main` / current target;
2. inspect intervening changes if needed;
3. fetch the exact current blob SHA immediately before replacing an existing file;
4. never overwrite a stale SHA;
5. preserve concurrent work and failed branches;
6. keep edits narrowly scoped.

**Live `main` overrides all snapshots.**

## 2. Epistemic labels are mandatory

Distinguish explicitly:

- **KNOWN** — established prior theory/experiment;
- **DERIVED** — follows from repository assumptions;
- **CHECKED** — independently/numerically verified;
- **CONDITIONAL** — exact only inside a deliberately simplified model;
- **INVALIDATED** — counterexample/correction found;
- **OPEN** — unresolved;
- **NON-CLAIM** — explicitly not asserted.

Never turn a negative literature search into a novelty claim.

No `new`, `first`, `fundamental`, `universal`, etc. without a focused primary-source audit and claim-ledger update.

## 3. Current research path

```text
weak resonant absorber
-> peak absorption can cost temporal bandwidth

active volume
-> killed as universal resource by field concentration

finite absorber / LDOS / ultrastrong coupling
-> successive microscopic loopholes

finite passive multimode network
-> exact harmonic two-access transfer-area bound

active / time-dependent / adaptive control
-> pump, timing, storage and output-record resources exposed

unrestricted output continuum
-> kills universal finite internal space-time capacity

semiconductor contact / energy filtering
-> detailed balance, lifetime broadening, filter-delay tradeoffs

field-driven HgCdTe collection
-> normalized direct BTBT

bulk high-field onset
-> corrected: not a finite-device II ceiling

finite dead space + energy relaxation
-> CURRENT FRONTIER: nonlocal P_II(F,L) from carrier energy history.
```

Do not return to an abstract universal-resource theorem unless the material branch exposes a genuinely missing invariant.

## 4. Canonical current reading order

1. `AGENTS.md`
2. `README.md`
3. `experiments/01-vanishing-absorber/CURRENT_STATE.md`
4. `experiments/01-vanishing-absorber/CLAIM_LEDGER.md`
5. `experiments/01-vanishing-absorber/HGCDTE_NONLOCAL_IONIZATION_SURROGATE.md`
6. `experiments/01-vanishing-absorber/HGCDTE_IMPACT_IONIZATION_DEAD_SPACE.md`
7. `experiments/01-vanishing-absorber/HGCDTE_FIELD_REGIME_MAP.md`
8. `experiments/01-vanishing-absorber/HGCDTE_TRANSPORT_BTBT_PHASE_BOUNDARY.md`
9. `experiments/01-vanishing-absorber/HGCDTE_NORMALIZED_BTBT_FRONTIER.md`
10. `experiments/01-vanishing-absorber/HGCDTE_KANE_SCALE_AUDIT.md`
11. `experiments/01-vanishing-absorber/RESEARCH_LOG.md`
12. `experiments/01-vanishing-absorber/ARCHIVE_STATUS.md`
13. older stages only for provenance.

There is still **no manuscript**.

## 5. Direct-BTBT normalization retained

Within the stated simplified Kane substitution,

```math
\boxed{
J_{\rm BTBT}
=\frac{q^3L}{4\pi^3\hbar^2v_K}
F^2e^{-F_K/F},
}
```

```math
\boxed{
F_K
=\frac{\pi^3\hbar c^2}
{qv_K\lambda_c^2},
}
```

and with `x=F/F_K`, `j=J/J_K`,

```math
\boxed{j=x^2e^{-1/x}.}
```

This is a material-scaling model, not a total dark-current model.

## 6. Critical correction — bulk II onset is not finite-device II probability

Primary bulk `Hg_0.8Cd_0.2Te`, 77 K Monte Carlo work reports hot-electron / impact-ionization physics at fields of order `10^2 V/cm`.

Do **not** convert this into

```text
1 um detector impact-ionizes at 100 V/cm.
```

A finite carrier must accumulate threshold energy over its actual history.

HgCdTe APD literature explicitly treats the process as history dependent / dead-space limited in thin multiplication regions.

## 7. Cold-injection dead-space relation

For

```math
E_{\rm th}=\chi E_g,
```

the field-work estimate is

```math
\boxed{
F_{\rm dead}
\simeq\frac{\chi E_g}{qL}.
}
```

With

```math
\ell_K=\hbar v_K/E_g,
```

```math
\boxed{
\frac{F_{\rm dead}}{F_K}
=\frac{4\chi}{\pi}
\frac{\ell_K}{L}.
}
```

For `L >> ell_K`, ionization threshold accessibility can occur far below the direct-BTBT characteristic field.

This is a **cold-injection field-work estimate**, not a stochastic no-ionization theorem.

## 8. Current nonlocal surrogate

Use the mean-energy equation

```math
\boxed{
\dot\varepsilon
=qFv-\varepsilon/\tau_E.
}
```

Define

```math
\ell_E=v\tau_E,
```

```math
\boxed{
L_{\rm eff}
=\ell_E(1-e^{-L/\ell_E}).
}
```

Then

```math
\boxed{
\varepsilon(L)=qF L_{\rm eff},
}
```

and

```math
\boxed{
F_{\rm th}^{(\rm mean)}
=\frac{\Delta E_{\rm th}}
{qL_{\rm eff}}.
}
```

For cold injection, `E_th=chi E_g`,

```math
\boxed{
\frac{F_{\rm th}^{(\rm mean)}}{F_K}
=\frac{4\chi}{\pi}
\frac{\ell_K}{L_{\rm eff}}.
}
```

This bridges

```text
L << ell_E
-> finite dead space

L >> ell_E
-> bulk-like energy-relaxation limit.
```

The mean trajectory does not capture the stochastic high-energy tail.

## 9. Energy-dependent II rate and analytic test case

Modern HgCdTe APD modeling uses

```math
\Gamma_{\rm II}(E)
=A
\frac{(E/E_{\rm th}-1)^\alpha}
{(E/E_{\rm th})^\beta}
```

above threshold.

For the analytic test case `alpha=1`, `beta=0`, the repository derives a closed finite-length hazard and

```math
\boxed{P_{\rm II}=1-e^{-\Xi_{\rm II}}.}
```

The closed result is independently checked against direct numerical time integration.

Dimensionless variables:

```math
\theta=qF\ell_E/E_{\rm th},
\qquad
\ell=L/\ell_E,
\qquad
a=A\tau_E.
```

Mean threshold inside the device requires

```math
\boxed{\theta(1-e^{-\ell})>1.}
```

For the analytic rate test case,

```math
\boxed{P_{\rm II}=1-e^{-aH(\theta,\ell)}.}
```

## 10. External-data boundary

For `Hg_0.8Cd_0.2Te` at 77 K, Palermo et al. explicitly calculate

- drift velocity;
- mean electron energy;
- impact-ionization rate;
- velocity relaxation rate;
- energy relaxation rate;
- analytical interpolation formulas.

The accessible primary-source text does **not** expose the interpolation coefficients.

Do not reconstruct them from narrative statements and silently promote them to primary data.

The missing calibration is now precise:

```text
tau_E(F) or ell_E(F)
+
Gamma_II(E) / calibrated A,alpha,beta.
```

## 11. Current field-ordering statement

Safe statement:

> **Ordinary MWIR/LWIR HgCdTe enters strongly non-ohmic high-field transport before direct BTBT becomes appreciable in the simplified Kane/BTBT model. Finite impact-ionization probability is a separate nonlocal problem controlled by threshold energy, available acceleration length, energy relaxation and the energy-dependent ionization rate.**

Do not replace it by the stronger but false shortcut

```text
impact ionization limits every finite device at 100 V/cm.
```

## 12. Numerical state

Active material regressions:

```text
experiments/01-vanishing-absorber/numerics/hgcdte_btbt_normalized_sweep.py
experiments/01-vanishing-absorber/numerics/hgcdte_field_regime_map.py
experiments/01-vanishing-absorber/numerics/hgcdte_impact_dead_space.py
experiments/01-vanishing-absorber/numerics/hgcdte_nonlocal_ii_surrogate.py
```

No CI is justified yet.

## 13. Stopped ideas — do not restart casually

- active-volume-only universal bound;
- finite absorber count as one-photon speed limit;
- finite internal storage rank as always-on capacity;
- local Landauer work as universal detector cost;
- single-Lorentzian leakage law as universal;
- spectral FWHM as architecture-independent transport speed;
- low-field `mu F` extrapolation into HgCdTe high-field operation;
- direct BTBT assumed to be first high-field limiter for ordinary LWIR;
- bulk `~100 V/cm` II onset treated as finite-device II threshold.

## 14. Next decisive work

Do **not** invent missing HgCdTe coefficients.

Next:

1. use the dimensionless nonlocal surrogate to scan physically defensible ranges of `ell_E` and `A tau_E`;
2. determine which ranges actually change the allowed field / transit conclusion;
3. search for primary measurements or calculations that constrain only those sensitive ranges;
4. then add TAT as a separate field-dependent dark-current channel;
5. after the diode-like field problem is stable, compare with HgCdTe photoconductors, where lifetime and gain may dominate speed.

Only after these attacks should manuscript significance be reassessed.
