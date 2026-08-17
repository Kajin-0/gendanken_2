# Paper 03 Stage-A Regime Screen Result

**Date:** 2026-08-17  
**Status:** **CHECKED PREDECLARED SCREEN / SELECTION RESULT / NON-CLAIM**

## 1. Authoritative execution

```text
workflow = Paper 03 Stage A regime screen
run      = 32066483254
job      = 95499707699
conclusion = success
```

Artifact:

```text
name   = paper03-stageA-regime-screen
id     = 9300491520
digest = sha256:81ee3b3e6158ca18e28455e49d2667d6a05a2fcc1b87b268c9543defdbbc291c
```

The screen executed the exact lattice fixed in `PAPER03_STAGEA_REGIME_MAP_PREDECLARATION_2026-08-17.md`:

```text
60 detector points
180 nonzero-RF rows
81 x 61 spatial grid
9-point lateral quadrature
full calibrated optical support
kernel-aware all-six one-mode fit
local regular analytic rejection-SNR ranking coordinate
```

The screen is selection-only. No coarse point is promoted directly to Outcome A or B.

---

## 2. Broad coarse result

```text
order-one rows (mimic >=0.50) = 42 / 180
points with >=1 order-one row = 14 / 60
analytic hidden-risk rows = 0 / 180
points with analytic hidden-risk row = 0 / 60
```

Thus the screen finds many order-one confounds but **no** coarse row satisfying

```text
mimic >= 0.50
and
analytic warning margin <= 0 dB.
```

The smallest analytic warning margin among order-one rows is still positive:

```text
+2.827 dB
```

at screen point `A04`, the finite 50%-contact / no-depletion / `D=2.5e-3 m^2/s` / infinite-lifetime coordinate.

This is favorable coarse evidence for Outcome A, but it remains only an 81x61 analytic screen. The predeclared refinement/bootstrap rules are still mandatory.

---

## 3. Strongest coarse confound

The largest screened mimic fraction is

```text
1.7576 x the frozen transport target
```

at `B04`:

```text
fc = 0.50
Wd = 3.0 um
Vsc = 0.050 V
D = 2.5e-3 m^2/s
tau = infinity
beam sigma = 1.0 um
beam center = +1.5 um
```

This point is selected by both

```text
S1 maximum confound
S6 optical-offset stress.
```

A coarse mimic greater than one does not by itself imply a hidden failure of the hierarchy; the same point has a positive coarse analytic warning margin and must be refined before interpretation.

---

## 4. Predeclared S0--S7 selection outcome

After applying the committed rules and deduplicating identical physical coordinates, six unique points remain.

### R0 / A21 — nominal anchor

```text
selection: S0
fc=0.75, Wd=3 um, Vsc=0.05 V
D=2.5e-3 m^2/s, tau=infinity
beam sigma=2 um, center=0
screen max mimic=0.8766
screen min analytic margin=+7.157 dB
```

### R1 / B04 — maximum confound + optical-offset stress

```text
selection: S1 + S6
fc=0.50, Wd=3 um, Vsc=0.05 V
D=2.5e-3 m^2/s, tau=infinity
beam sigma=1 um, center=+1.5 um
screen max mimic=1.7576
screen min analytic margin=+12.192 dB
```

### R2 / A04 — worst / closest warning boundary

```text
selection: S2 + S3
fc=0.50, Wd=0, Vsc=0
D=2.5e-3 m^2/s, tau=infinity
beam sigma=2 um, center=0
screen max mimic=0.5589
screen min analytic margin=+2.827 dB
```

### R3 / A07 — strongest early warning among order-one rows

```text
selection: S4
fc=0.50, Wd=3 um, Vsc=0.05 V
D=1.0e-3 m^2/s, tau=infinity
beam sigma=2 um, center=0
screen max mimic=1.6655
screen min analytic margin=+15.842 dB
```

### R4 / B03 — largest calibrated one-mode mismatch

```text
selection: S5
fc=0.50, Wd=3 um, Vsc=0.05 V
D=2.5e-3 m^2/s, tau=infinity
beam sigma=1 um, center=0
screen max mimic=1.7265
screen min analytic margin=+18.771 dB
```

### R5 / A03 — weakest still-order-one confound

```text
selection: S7
fc=0.50, Wd=0, Vsc=0
D=2.5e-3 m^2/s, tau=5 ns
beam sigma=2 um, center=0
screen max mimic=0.5096
screen min analytic margin=+6.899 dB
```

The machine-readable frozen manifest is

```text
PAPER03_STAGEA_REGIME_SELECTION_MANIFEST_2026-08-17.json
```

No discretionary post-screen point was added.

---

## 5. Immediate refinement rule

Every selected point is recomputed at

```text
161 x 121
201 x 151
17-point lateral quadrature
```

and must retain

```text
<=2% of the frozen target
```

for the 161-to-201 historical raw-phase change at every nonzero RF before scientific interpretation.

After refinement, the already-predeclared bootstrap rules are:

```text
bootstrap S2 if refined order-one;
bootstrap distinct S3 if refined order-one;
bootstrap distinct S1 if refined max mimic >1;
reuse the completed nominal S0 bootstrap when the coordinate is unchanged.
```

Because S2 and S3 selected the same physical coordinate in this screen, they can require at most one new boundary-point bootstrap.

---

## 6. Current interpretation boundary

The screen makes a narrow-corner explanation less plausible because order-one mimic occurs at 42 RF rows across 14 points and includes no analytic hidden-risk row.

However:

```text
broad Outcome-A evidence -> NOT YET ESTABLISHED
Outcome-B evidence -> NOT FOUND IN COARSE SCREEN
```

The selected-point numerical refinement and required bootstrap calibration remain decisive. `science_interpretation_ready` remains false.