# Matched-Contact Buried Gradient — Finite Recombination and Back-Boundary Bracket

**Date:** 2026-08-09  
**Status:** conditional Einstein drift-diffusion first-passage sensitivity study with bulk killing, two rigorous back-boundary limits, and common-field sensitivity; no calibrated device prediction; no novelty claim

## 1. Why this calculation is needed

The first matched-contact transport collision gave opposite overall timing trends in two simple limits:

```text
deterministic local drift
-> low-field compensation can dominate -> slower deep transit

Einstein drift-diffusion with reflecting back boundary
-> buried assisting field can dominate -> modest speedup.
```

That left an immediate question:

> **Is the drift-diffusion speedup merely an artifact of infinite carrier lifetime or the reflecting back boundary?**

This note tests that possibility before adding more microscopic transport physics.

As before, `F(z)>0` is used only as a conditional effective field magnitude that assists the collected minority carrier toward the front boundary `z=0`. No electron/hole band-edge force direction is asserted for a real device.

---

## 2. Killed drift-diffusion process

Use

```math
D=\mu V_T,
\qquad
V_T=k_BT/q,
```

and

```math
dz=-\mu F(z)dt+\sqrt{2D}\,dW.
```

Uniform bulk recombination is represented by Poisson killing with

```math
k=1/\tau_{\rm bulk}.
```

For a carrier starting at `z`, define the front-collection probability

```math
\boxed{
h(z)
=E\left[e^{-kT}I_{\rm front}\right].
}
```

Then

```math
\boxed{
D h''-\mu F h'-kh=0.
}
```

Define the time-weighted collected moment

```math
m(z)
=E\left[T e^{-kT}I_{\rm front}\right].
```

It obeys

```math
\boxed{
D m''-\mu F m'-km=-h.
}
```

For generated carriers that are actually collected, the conditional mean time is

```math
\boxed{
\langle T\rangle_{\rm coll}(z)=m(z)/h(z).
}
```

---

## 3. Two back-surface limits

Rather than inventing an unvalidated partial-surface-recombination coefficient, bracket the back boundary with two rigorous limits.

### Reflecting back

```math
h'(L)=0,
\qquad
m'(L)=0.
```

This reproduces the preceding first-passage model when `tau_bulk -> infinity`.

### Perfectly lossy / recombining back

```math
h(L)=0,
\qquad
m(L)=0.
```

Any carrier reaching the back boundary is removed.

Front collection remains

```math
h(0)=1,
\qquad
m(0)=0.
```

These two cases do not cover every real surface, but they sharply test whether the timing sign is a peculiarity of one boundary assumption.

---

## 4. Sensitivity coordinates

Use only explicit sensitivity values:

```text
mu_ref = 1e4 cm^2/(V s)

tau_bulk = infinity, 3 ns, 1 ns, 0.3 ns, 0.1 ns

additional common assisting field = 0, 100, 300 V/cm.
```

The lifetime and common-field values are **not claimed material parameters** for the thought device.

They are chosen to span from effectively transit-dominated to strong carrier selection/recombination and from pure composition-gradient drift to a substantial common drift field.

---

## 5. Keep optics fixed when comparing transport hypotheses

For each `beta` device, use its own known contrast generation distribution

```math
p_\beta(z|\lambda).
```

Compare

```text
null:
that same p_beta propagated through control transport

alternative:
that same p_beta propagated through beta transport.
```

Thus the timing difference isolates the transport consequence of the field redistribution once the contrast composition profile is known.

The mean collected time at wavelength `lambda` is

```math
\boxed{
\bar T(\lambda)
=
\frac{
\int p_\beta(z|\lambda)m(z)dz
}{
\int p_\beta(z|\lambda)h(z)dz
}.
}
```

The denominator also reports the relative collection probability.

---

## 6. Main result — the Einstein-family mean timing sign is robust

Across

```text
2 back boundaries
x 5 lifetime values
x 3 common-field values
= 30 transport environments per beta,
```

the wavelength-averaged contrast-minus-control timing shift remains **negative** for every `beta=1,2,3` case.

At the reference mobility:

### `beta=1`

```text
mean timing change:
-9.73 to -0.53 ps
```

### `beta=2`

```text
-17.27 to -1.07 ps
```

### `beta=3`

```text
-23.23 to -1.66 ps.
```

Thus finite lifetime, a perfectly lossy back surface, and a substantial common assisting field all reduce the magnitude but do **not** reverse the mean Einstein first-passage speedup over this sensitivity bracket.

---

## 7. Spectral timing signal remains finite throughout the bracket

After removing wavelength-independent delay, the transport-only spectral timing peak-to-peak spans:

### `beta=1`

```text
1.23-11.92 ps
-> 0.44-4.29 deg p-p at 1 GHz.
```

### `beta=2`

```text
2.34-21.17 ps
-> 0.84-7.62 deg.
```

### `beta=3`

```text
3.31-28.22 ps
-> 1.19-10.16 deg.
```

These absolute phase values inherit the reference mobility and simplified transport model. They are not device predictions.

The useful result is that the **spectral structure does not collapse** merely because finite lifetime or back loss is introduced.

---

## 8. `beta=3` keeps the same endpoint-differential sign throughout

A simple gauge-invariant sign diagnostic is

```math
\Delta T(3.83\,\mu{\rm m})
-
\Delta T(2.80\,\mu{\rm m}).
```

For `beta=3`, this remains negative in all 30 sensitivity environments:

```text
approximately -21.6 to -0.73 ps.
```

So the long-wave-generated carriers receive a larger timing reduction than the short-wave-generated carriers throughout this Einstein drift-diffusion bracket.

`beta=2` becomes nearly neutral in the most strongly selective reflecting / short-lifetime case, so the weaker members should not be overinterpreted from sign alone.

---

## 9. Collection efficiency changes as well as timing

Finite lifetime and back loss make the buried redistribution change which carriers survive to collection.

For `beta=3`, across wavelength and all sensitivity cases, the contrast/control collection-probability ratio spans roughly

```math
\boxed{0.85\text{ to }1.13.}
```

Thus amplitude/quantum-efficiency information is not merely a passive nuisance in a realistic transport model.

A measured device could show both

```text
timing redistribution
and
collection-probability redistribution.
```

That reinforces the value of fitting the **complex response plus amplitude** rather than phase alone, while also demanding a transport model that treats recombination consistently.

---

## 10. What this resolves

The drift-diffusion speedup is **not** solely caused by

```text
infinite lifetime
or
a reflecting back boundary.
```

It survives

```text
strong bulk killing
perfect back loss
and
large common assisting drift.
```

This substantially narrows the earlier model collision.

---

## 11. What this does not resolve

The deterministic local-drift limit still predicts a different overall transit trend for the stronger buried-gradient structures.

Therefore the unresolved issue is more fundamental:

> **How important is diffusion relative to local field-driven transit in the relevant graded HgCdTe operating regime?**

The generic drift-diffusion equation can be written

```math
D T''-\mu F T'=-1.
```

Defining

```math
\Theta\equiv D/\mu
```

gives

```math
\boxed{
\Theta U''-F U'=-1,
\qquad
U=\mu T.
}
```

The deterministic drift limit corresponds formally to

```math
\Theta\to0,
```

while a nondegenerate Einstein model gives

```math
\Theta=k_BT/q\approx25.85\ {\rm mV}
```

at 300 K.

This provides the natural continuous parameter connecting the two earlier transport limits.

---

## 12. Next decisive calculation

Sweep

```math
\Theta=D/\mu
```

continuously and find where the buried-gradient timing response changes sign.

That crossover is more informative than arguing qualitatively about whether the device is `drift dominated` or `diffusion dominated`.

The next useful output is therefore:

```text
critical D/mu for beta=1,2,3
critical D/mu after adding common assisting field
comparison with kBT/q at 300 K
and the spectral endpoint sign across the crossover.
```

If the physically plausible `D/mu` range lies safely on one side of the crossover, the timing prediction becomes much stronger.

Numerical implementation for this finite-recombination bracket:

`numerics/hgcdte_matched_contact_recombination_boundary.py`
