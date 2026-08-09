# Published Sample B — Wavelength-Dependent Phase Noise and Measurement Resource Cost

**Date:** 2026-08-09  
**Status:** first heteroscedastic-noise correction to the published sample-B inverse; scaling models, not a complete instrument covariance; no novelty claim

## 1. Why the equal-noise model is optimistic

The earlier phase-noise stress test assigned the same phase uncertainty to every wavelength.

The dimensional optical model does not support that assumption at fixed incident power.

Across the retained `Pabs >= 0.05` scan,

```text
2.80 um -> Pabs ~0.998
3.89 um -> Pabs ~0.0568.
```

Thus the absorbed signal changes by a factor

```math
\boxed{
R_P
\equiv
\frac{P_{\rm abs}(2.80)}
{P_{\rm abs}(3.89)}
\approx17.6.
}
```

A realistic covariance must therefore become wavelength dependent unless source power, averaging time, or another measurement resource is deliberately reallocated.

---

## 2. Two limiting phase-noise scalings

These are deliberately simple limits, not complete detector-noise models.

### Statistics-like limit

If phase precision is governed by counting/statistical SNR,

```math
\boxed{
\sigma_\phi(\lambda)
\propto
P_{\rm abs}(\lambda)^{-1/2}.
}
```

At fixed incident power and integration time, a `0.10 degree` short-wave phase uncertainty becomes about

```math
\boxed{0.42^\circ}
```

at the `3.89 um` end of the retained scan.

### Additive-readout-like limit

If the complex-signal amplitude is proportional to absorbed signal while additive readout noise is approximately wavelength independent,

```math
\boxed{
\sigma_\phi(\lambda)
\propto
P_{\rm abs}(\lambda)^{-1}.
}
```

The same `0.10 degree` short-wave phase uncertainty becomes about

```math
\boxed{1.76^\circ}
```

near `3.89 um`.

Real measurements may lie between or outside these limits depending on detector noise, source RIN, reference architecture, coherent averaging, and readout electronics.

---

## 3. Weighted inverse

Let diagonal phase covariance be

```math
\mathbf C_\phi
=\operatorname{diag}(\sigma_{\phi,i}^2).
```

Whiten with

```math
\mathbf W=\mathbf C_\phi^{-1/2}.
```

Because the wavelength-independent phase is a nuisance/gauge mode, project the whitened system orthogonal to

```math
\mathbf W\mathbf1.
```

The relevant inverse matrix is therefore

```math
\boxed{
\mathbf B
=\mathbf P_\perp
\mathbf W
\mathbf A,
}
```

not the unweighted optical matrix alone.

Thus **optical rank and experimental rank are different objects**.

---

## 4. Re-test the same synthetic transport anomaly

Use the previously defined illustrative anomaly

```text
baseline v = 1e5 m/s
25% slowdown
center = 2.30 um
Gaussian sigma = 0.35 um
1 GHz measurement.
```

Its residual spectral phase remains approximately

```math
0.935^\circ
```

peak-to-peak.

With `0.10 degree` phase uncertainty at the strongly absorbed short-wave end:

| noise model | phase uncertainty near 3.89 um | median rank-3 noise error | 90% peak-location error |
|---|---:|---:|---:|
| equal noise | 0.10 deg | ~0.17 | ~0.13 um |
| statistics-like | 0.42 deg | ~0.28 | ~0.45 um |
| additive-like | 1.76 deg | ~0.45 | ~0.59 um |

The equal-noise calculation therefore substantially overstates localization performance when optical power is not reallocated.

The precise numbers belong only to the stated anomaly and noise scalings.

---

## 5. Measurement-resource cost of equalizing phase precision

The near-cutoff wavelengths contain useful localization information but little absorbed signal.

To keep the **absorbed photon number** approximately constant in a statistics-limited experiment,

```math
P_{\rm in}t
\propto
1/P_{\rm abs}.
```

Thus the long-wave point requires about

```math
\boxed{17.6\times}
```

more incident-power × integration-time resource than the short-wave point.

If incident power is fixed, that is roughly `17.6x` longer averaging time.

In the simple additive-noise/coherent-averaging limit,

```math
\sigma_\phi
\propto
\frac1{P_{\rm abs}\sqrt t},
```

so equal phase precision at fixed incident power requires

```math
\boxed{
t\propto P_{\rm abs}^{-2}.}
```

The `3.89 um` point would then require roughly

```math
\boxed{(17.6)^2\approx309\times}
```

more averaging time.

Alternatively increasing incident power by approximately the absorbed-signal ratio can restore signal amplitude, but that may change detector injection level, heating, space charge, or transport and therefore corrupt the very quantity being measured.

---

## 6. Experimental consequence

The measurement should **not** use equal integration time and equal incident power merely for procedural symmetry.

A better strategy is to design the wavelength schedule from information and perturbation constraints:

```text
near-cutoff wavelengths
-> strong spatial localization
-> weak signal
-> allocate more averaging / carefully controlled power

short wavelengths
-> high signal
-> broad optical kernel
-> less averaging needed.
```

The safest resource to vary is usually averaging time rather than incident power, because changing optical injection can itself alter HgCdTe carrier transport.

This last statement is a design preference, not a universal theorem; the actual experiment must test linearity versus optical power.

---

## 7. Important new interpretation

The active inverse is now constrained by three nested filters:

```text
material composition profile
-> determines spectral spatial encoding

absorption kernel
-> limits recoverable spatial modes

wavelength-dependent measurement covariance
-> determines which of those modes are experimentally usable.
```

Therefore a singular-value plot of the optical matrix alone is insufficient to claim experimental resolution.

The correct object is a **noise-whitened, common-mode-projected information matrix**.

---

## 8. Claim boundary

### CHECKED NUMERICALLY / CONDITIONAL

For the stated sample-B envelope, synthetic anomaly, and phase-noise scaling models:

- fixed-power phase precision degrades strongly near cutoff;
- equal-noise Monte Carlo is optimistic;
- the rank-3 anomaly remains recoverable more weakly in a statistics-like model and degrades strongly in an additive-like model;
- equalizing phase precision can require large wavelength-dependent averaging resources.

### NOT ESTABLISHED

- the actual instrument noise regime;
- independent Gaussian wavelength noise;
- phase precision of a particular VNA/source/detector chain;
- allowable optical-power variation without transport perturbation;
- real sample-B reconstruction performance.

---

## 9. Next decisive work

Replace the two scaling limits with a measured or defensible **instrument-level covariance model**:

```text
source power and modulation depth versus wavelength
reference-path phase stability
receiver/readout noise
HgCdTe signal/noise versus optical loading
averaging-time dependence
RF-frequency correlations.
```

Then optimize wavelength and RF-frequency sampling by expected information per unit measurement time, subject to detector linearity.

Reproducibility:

`numerics/hgcdte_published_sample_b_heteroscedastic_phase.py`
