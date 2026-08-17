# Paper 02 — two-carrier closure result

**Date:** 2026-08-16  
**Status:** **CHECKED / MAJOR REVIEW ISSUE RESOLVED BY SCOPE NARROWING**

## Disposition

The Rev. 7 deterministic apparent-diffusion result is **not established as a generic electron–hole-pair photodiode result**. Rev. 8 should explicitly scope the central theorem/counterexample to a **single-mobile-carrier / unipolar Shockley–Ramo observable**.

This is a scientific narrowing, not an editorial disclaimer. Two independent pair-aware tests were run after the later adversarial review identified the missing carrier-species assumption.

## Exact pair forward model

With planar weighting potential `phi_w=z/L`, the second carrier was added with the polarity for which the two induced-current contributions add. The exact dc identity is

```text
H_down(z,0) = (L-z)/L
H_up(z,0)   = z/L
H_pair(z,0) = 1.
```

The sampled maximum pair-identity error was

```text
1.1102230246251565e-16.
```

Thus the new pair transfer is internally consistent with full planar Shockley–Ramo collection.

## Test 1 — both pair roots free

Predeclared gate:

```text
PAPER02_TWO_CARRIER_GATE_2026-08-16.md
```

Workflow:

```text
run 31965377545
artifact paper02-two-carrier-exact
artifact id 9268349788
artifact SHA-256 23c72abfdf39641a25e39948c712e9f158cf982edc40639b40e36facc1d92eb3
```

The uniform two-carrier null passed extremely strongly over the core speed-ratio sweep:

```text
max |D_down|                    6.579444100145674e-09 m^2/s
max centered two-mode residual 1.735154346493963e-13
```

Therefore a uniform pair is represented correctly by the two-mode finite-kernel inverse.

The heterogeneous two-free-root decomposition was **not physically stable**. Although the first script's automatic sign counter labelled three core rows positive, inspection showed that many heterogeneous fits drove the second root far from its known physical countercarrier value or onto the near-zero sign bound, while the downstream pseudo-root acquired very large positive or negative effective-D values. That automatic B2 physical interpretation is superseded. The raw rows remain valid evidence of underconstrained carrier decomposition.

## Test 2 — countercarrier propagation fixed to the known physical mode

Post-hoc follow-up:

```text
PAPER02_TWO_CARRIER_FOLLOWUP_2026-08-16.md
```

Workflow:

```text
run 31965573244
artifact paper02-two-carrier-known-countercarrier
artifact id 9268390922
artifact SHA-256 b95e36dc0d42e496499bd7cc0ba4221df01ddcafd47e93683e7824f2129ef687
```

Here the countercarrier root was fixed to its exact uniform-velocity value

```text
r_up = -i omega/v_up,
```

while its complex amplitude was still profiled as a nuisance. Only the downstream complex root was inferred.

The uniform pair null again passed. Across the 21 core rows (`v_up/v_down=0.1...10` at 100 MHz, 500 MHz, 1 GHz):

```text
positive downstream D rows: 1 / 21
minimum fitted D: -4.6471492227059946e-01 m^2/s
maximum fitted D: +1.4936279374425938e-03 m^2/s
```

The one positive case was `v_up/v_down=0.1` at 1 GHz and was already 36.5% below the single-carrier exact-continuum value. Most pair cases changed the sign of the downstream effective coefficient.

This means that adding a second carrier and allowing its contribution to be represented—even with its propagation root known—changes the pseudo-true downstream root materially. The original positive-D value cannot be promoted as a generic pair-transient material-attribution result.

## Scientific conclusion

### Established

The Rev. 7 counterexample remains valid for the model it actually solves: a deterministic single-mobile-carrier/unipolar Shockley–Ramo observable with `D_micro=0`.

### Not established

It is not established that the same positive `D_eff` persists for a generic electron–hole pair transient. The pair-aware tests show that the inferred downstream effective coefficient is strongly model/decomposition dependent once both carrier contributions are present.

### Required Rev. 8 wording

Rev. 8 must say explicitly, near the first definition of the forward observable and in the abstract/conclusion, that the central theorem/counterexample concerns a **unipolar or single-mobile-carrier terminal-current contribution**. It must not imply complete modeling of an ordinary two-carrier photodiode transient.

A suitable boundary is:

> The central construction treats one mobile carrier contribution to the planar Shockley–Ramo terminal current. It applies directly to unipolar observables and to regimes in which one carrier contribution is independently isolated or negligible; it is not a complete electron–hole pair model of a generic photodiode transient.

The new pair stress may be summarized as a scope test: when both carrier modes are admitted, carrier decomposition itself becomes an additional identifiability problem and the single-carrier positive effective coefficient is not invariant.

## Epistemic consequence

R8-1 is **resolved by narrowing**, not by claiming two-carrier robustness.

Do not perform parameter tuning designed to recover positive D in the pair sweep. Any later two-carrier extension is a separate research problem rather than a requirement for the present unipolar theorem/systematics paper.
