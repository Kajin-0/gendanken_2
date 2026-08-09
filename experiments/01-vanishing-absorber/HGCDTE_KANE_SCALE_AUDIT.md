# HgCdTe Kane Scale Audit — What the Abstract Speed/Leakage Limits Mean for an Infrared Material

**Date:** 2026-08-08  
**Status:** material-scale interpretation using established simplified Kane dispersion and BTBT formulas; no novelty claim

## 1. Purpose

The preceding semiconductor branches produced several abstract quantum scales involving

```math
\hbar,
\qquad
\Delta E,
\qquad
\text{electric field},
\qquad
\text{collection length}.
```

Before turning them into apparent fundamental detector limits, this note asks whether those scales are actually relevant to HgCdTe.

HgCdTe is useful because near the semiconductor-semimetal transition its low-energy dispersion admits a simple Kane/pseudorelativistic description with an approximately composition- and temperature-independent characteristic velocity.

The goal is to distinguish

```text
asymptotic quantum ceiling
```

from

```text
realistic narrow-gap tunneling scale.
```

---

## 2. Established HgCdTe Kane velocity

Teppe et al., *Nature Communications* **7**, 12576 (2016), DOI `10.1038/ncomms12576`, used magneto-spectroscopy to show that near the HgCdTe topological transition the Kane-fermion characteristic velocity remains approximately

```math
\boxed{
v_K
\simeq
(1.07\pm0.05)\times10^6\ {\rm m/s}
}
```

across a broad range of temperatures and compositions near the transition.

Within the simplified Kane description they use the rest-mass relation

```math
\boxed{
E_g=2m_Kv_K^2.
}
```

These are prior band-structure results, not repository novelty.

---

## 3. Rewrite the direct-tunneling field scale

A standard direct-gap BTBT exponent used in HgCdTe device modeling has the structure

```math
\exp\!\left[
-
\frac{\pi\sqrt{m^*}E_g^{3/2}}
{2\sqrt2\,q\hbar F}
\right].
```

Define the characteristic field

```math
F_K
\equiv
\frac{\pi\sqrt{m^*}E_g^{3/2}}
{2\sqrt2\,q\hbar}.
```

If, **only for this simplified scaling audit**, the tunneling mass is identified with the Kane band-edge mass

```math
m^*=m_K
=\frac{E_g}{2v_K^2},
```

then

```math
\boxed{
F_K
\simeq
\frac{\pi E_g^2}
{4q\hbar v_K}.
}
```

This substitution should not be treated as a precision HgCdTe tunneling model; real multiband/nonparabolic tunneling masses and junction profiles require a more complete treatment.

---

## 4. Cutoff-wavelength scaling

Use the usual detector-scale optical-gap relation

```math
E_g\simeq\frac{hc}{\lambda_c}.
```

Then

```math
\boxed{
F_K
\simeq
\frac{\pi^3\hbar c^2}
{qv_K\lambda_c^2}.
}
```

Thus

```math
\boxed{
F_K\propto\lambda_c^{-2}.
}
```

This makes the long-wavelength penalty transparent:

> For the same dimensionless proximity to direct interband tunneling, the allowable electric-field scale falls approximately with the inverse square of cutoff wavelength in this simplified Kane picture.

The qualitative statement that narrow-gap/long-wavelength HgCdTe is increasingly vulnerable to tunneling is established device physics.

---

## 5. Characteristic Kane length

Define the natural band-edge length

```math
\boxed{
\ell_K
\equiv
\frac{\hbar v_K}{E_g}.
}
```

Using

```math
E_g=hc/\lambda_c,
```

```math
\boxed{
\ell_K
=\frac{v_K}{2\pi c}\lambda_c.
}
```

Therefore

```math
\boxed{
\ell_K\propto\lambda_c.
}
```

This is the characteristic distance over which the gap energy and Kane velocity combine into an `hbar v / Eg` quantum length.

It is the natural warning scale for the repository's earlier `L -> 0` parabolic/barrier models: once collection/barrier dimensions approach only a few `ell_K`, full multiband/nonparabolic quantum transport can no longer be ignored.

Do not call `ell_K` a universal minimum detector thickness.

---

## 6. Numerical scale table

Using

```math
v_K=1.07\times10^6\ {\rm m/s}
```

and

```math
E_g=hc/\lambda_c,
```

gives the following approximate scales.

| `lambda_c` | `E_g` | `F_K` | `ell_K` | `E_g/h` |
|---:|---:|---:|---:|---:|
| 3 um | 0.413 eV | 1.90e6 V/cm | 1.70 nm | 99.9 THz |
| 5 um | 0.248 eV | 6.86e5 V/cm | 2.84 nm | 60.0 THz |
| 8 um | 0.155 eV | 2.68e5 V/cm | 4.54 nm | 37.5 THz |
| 10 um | 0.124 eV | 1.71e5 V/cm | 5.68 nm | 30.0 THz |
| 12 um | 0.103 eV | 1.19e5 V/cm | 6.82 nm | 25.0 THz |
| 17 um | 0.0729 eV | 5.93e4 V/cm | 9.66 nm | 17.6 THz |
| 24 um | 0.0517 eV | 2.98e4 V/cm | 13.6 nm | 12.5 THz |

These are order-of-magnitude **Kane scaling estimates**, not calibrated junction-tunneling predictions.

---

## 7. A compact identity

The two characteristic scales satisfy

```math
F_K\ell_K
\simeq
\frac{\pi E_g}{4q}.
```

Thus the characteristic tunneling field acting across the characteristic Kane length corresponds to a voltage of order the bandgap voltage.

This is a useful normalization check:

```math
\boxed{
qF_K\ell_K
\sim E_g.
}
```

up to the `pi/4` coefficient of the adopted simplified tunneling exponent.

---

## 8. Compare the two repository limits

### A. Single-barrier quantum speed scale

`BALLISTIC_BARRIER_SPEED_LEAKAGE.md` produced an exponent controlled by

```math
\frac{\Delta E}
{\hbar\Omega_{\rm tr}}.
```

If the useful-dark energy scale is of order the detector gap,

```math
\Delta E\sim E_g,
```

the corresponding frequency scale is

```math
\boxed{
\frac{E_g}{h}
\sim
\frac{c}{\lambda_c}.
}
```

For MWIR/LWIR HgCdTe this is tens of THz.

Thus the ideal single-barrier quantum speed/leakage ceiling lies extremely far above the kHz-MHz response of many HgCdTe photoconductors and above the GHz regime of many practical infrared photodiodes/APDs.

This strongly suggests that the one-barrier `Delta E/(hbar Omega)` limit is an **asymptotic quantum ceiling**, not the practical bottleneck for ordinary devices.

### B. Field-driven BTBT scale

The BTBT characteristic field, by contrast, is only around

```text
10^4 - 10^6 V/cm
```

over the infrared cutoff range shown above.

Those fields are accessible in depletion and multiplication regions.

Therefore field-assisted tunneling can become technologically relevant long before the fundamental single-barrier transit scale is approached.

This is consistent with HgCdTe photodiode/APD literature in which TAT/BTBT become important under reverse bias.

---

## 9. Why long wavelength becomes difficult in two directions

Increasing cutoff wavelength gives simultaneously

```math
F_K\propto\lambda_c^{-2}
```

and

```math
\ell_K\propto\lambda_c.
```

So longer-wavelength HgCdTe has

1. a **lower characteristic field** for direct interband tunneling;
2. a **larger microscopic nonparabolic quantum length**.

This is an instructive material-level form of the original gedanken theme:

```text
smaller band gap
-> detect lower-energy photons
-> but electric and spatial scales separating useful transport from quantum leakage become less forgiving.
```

The statement is qualitative/material scaling, not a new detector theorem.

---

## 10. Relation to real transport parameters

HgCdTe can also have very high low-field electron mobility.

Published 77 K measurements include electron mobilities up to approximately

```math
2.8\times10^5\ {\rm cm^2/(V\,s)}
```

for very lightly doped `x ~= 0.22` epitaxial material and even higher near the zero-gap composition in some samples.

Hole mobilities in LWIR-composition material are much smaller.

Therefore a real detector can enter non-linear/high-field transport at fields well below the formal Kane velocity scale, depending on carrier type, scattering, alloy disorder, optical phonons, doping, and temperature.

Do not identify `v_K` with measured drift-saturation velocity.

`v_K` is a band-dispersion velocity parameter, not the same thing as the transport drift velocity in a scattering-limited device.

---

## 11. Current verdict

The abstract quantum leakage branches have clarified the hierarchy but have not yet produced a practical HgCdTe performance limit.

The hierarchy is approximately

```text
Eg / h
-> asymptotic quantum transit scale (tens of THz)

F_K
-> technologically relevant interband-tunneling field scale

measured drift/lifetime/RC scales
-> practical detector speed
```

Therefore the next useful physics should stay in the **field-driven HgCdTe transport regime**, not push the one-barrier quantum model further.

---

## 12. Next decisive HgCdTe question

The natural material-specific gedanken experiment is now:

> **For a fixed HgCdTe cutoff wavelength and collection-region thickness, what is the best transit bandwidth achievable before a specified direct-tunneling dark-current density is reached, and how does that scale with cutoff wavelength?**

`FIELD_DRIVEN_COLLECTION_TUNNELING.md` already supplies the symbolic elimination.

The next step should

1. insert a consistent HgCdTe Kane/BTBT parameterization;
2. use a physically justified drift-velocity model rather than `v=mu F` to arbitrarily high field;
3. sweep `lambda_c`, `L`, and dark-current target;
4. identify whether an approximately material-universal normalized curve emerges;
5. compare the result against actual reported HgCdTe photodiode/APD operating fields and response times.

Only after that numerical/material audit should this branch be considered for a paper-level claim.