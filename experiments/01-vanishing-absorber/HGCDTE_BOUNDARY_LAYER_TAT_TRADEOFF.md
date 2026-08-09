# HgCdTe Boundary-Layer TAT Tradeoff — Barrier-Free Extraction Versus Junction Field

**Date:** 2026-08-09  
**Status:** analytic boundary-layer design inequality built from established band-offset compensation and TAT exponent physics; no novelty claim

## 1. Purpose

The graded-interior branch now suggests that a quasi-neutral p-type HgCdTe absorber can nearly pin the majority-hole valence band while a decreasing band gap supplies a downhill conduction-band slope for minority electrons.

That moves the likely dark-current bottleneck to the collection boundary, where the narrow-gap absorber must connect to a contact, depletion region, or wider-gap transport/barrier layer.

Question:

> Can a wider-gap boundary remain barrier-free for minority-electron extraction without requiring so much compensating electrostatic field that trap-assisted tunneling reopens the leakage problem?

The simplest model yields a direct width / transit-delay / trap-depth tradeoff.

---

## 2. Wide-gap boundary and band-offset partition

Let the local gap increase across the collection boundary by

```math
\Delta E_g>0.
```

Let

```math
0<\alpha<1
```

be the conduction-band share of the material-induced gap increase.

Before electrostatic compensation, write

```math
\Delta E_c^{\rm mat}=\alpha\Delta E_g,
```

```math
\Delta E_v^{\rm mat}=-(1-\alpha)\Delta E_g.
```

A potential-energy drop `qV_b` in the collection direction lowers both electron band edges by the same amount. Hence

```math
\boxed{
\Delta E_c
=\alpha\Delta E_g-qV_b,
}
```

```math
\boxed{
\Delta E_v
=-(1-\alpha)\Delta E_g-qV_b.
}
```

---

## 3. Barrier-free minority-electron extraction

To avoid an uphill conduction-band barrier for electrons moving toward collection, require

```math
\Delta E_c\le0.
```

Therefore

```math
\boxed{
qV_b\ge\alpha\Delta E_g.
}
```

The smallest electrostatic resource occurs at equality:

```math
\boxed{
qV_b=\alpha\Delta E_g.
}
```

At that point

```math
\boxed{
\Delta E_c=0,
}
```

while

```math
\boxed{
\Delta E_v=-\Delta E_g.
}
```

Thus the conduction edge can be made barrier free while the full gap increase is placed into separation from the valence band.

This general band-engineering idea is established in HgCdTe heterojunction and unipolar-barrier design literature; the present note uses it only as the boundary condition for a tunneling-resource calculation.

---

## 4. Minimum compensating field

Let the compensated boundary have physical thickness

```math
w.
```

If the electrostatic drop is approximately uniform through that transition, minimum compensation requires

```math
\boxed{
F_b
=\frac{\alpha\Delta E_g}{qw}.
}
```

When energies are expressed in electron-volts, the corresponding voltage drop in volts is numerically `alpha Delta Eg[eV]`.

The immediate tension is now visible:

```text
smaller w
-> shorter boundary transit distance
-> larger compensation field
-> stronger field-assisted leakage.
```

---

## 5. Import the established HgCdTe TAT exponent scale

`HGCDTE_TAT_FIELD_SCALE.md` uses the standard one-dimensional trap-to-conduction tunneling exponent

```math
\exp(-F_{\rm TAT}/F),
```

with

```math
\boxed{
F_{\rm TAT}
=\frac{4\sqrt{2m^*}\Delta_t^{3/2}}
{3q\hbar}.
}
```

Here

```math
\Delta_t=E_c-E_T
```

is the trap energy depth below the conduction band in the stated local convention.

At the minimally compensated boundary,

```math
\frac{F_{\rm TAT}}{F_b}
=\frac{qF_{\rm TAT}w}
{\alpha\Delta E_g}.
```

Therefore the field-dependent factor becomes

```math
\boxed{
\mathcal T_{\rm TAT}^{({\rm exp})}
\sim
\exp\!\left[
-
\frac{qF_{\rm TAT}w}
{\alpha\Delta E_g}
\right].
}
```

---

## 6. Minimum boundary width for a target TAT exponent

Suppose the design requires the tunneling exponent to satisfy

```math
\frac{F_{\rm TAT}}{F_b}
\ge\Sigma_t,
```

where `Sigma_t` is a chosen exponent margin.

Then

```math
\boxed{
w
\ge
w_{\rm TAT}
\equiv
\frac{\alpha\Delta E_g}
{qF_{\rm TAT}}
\Sigma_t.
}
```

This is the central boundary-layer result.

It is not a complete TAT-current specification because the full current also depends on trap density, occupation, matrix element, electrostatics, and prefactors.

It says only that a barrier-free boundary cannot be made arbitrarily thin at fixed gap step and trap spectrum while retaining a chosen field-exponent margin.

---

## 7. Minimum boundary transit delay

Let a collected photoelectron cross the transition with characteristic speed

```math
v_b.
```

The geometric crossing time satisfies

```math
t_b\ge w/v_b.
```

Combining with the TAT width floor gives

```math
\boxed{
t_b
\ge
\frac{\alpha\Delta E_g}
{qF_{\rm TAT}v_b}
\Sigma_t.
}
```

Thus the local penalty migration is

```text
wide-gap boundary
-> suppresses direct narrow-gap overlap

barrier-free compensation
-> requires electrostatic field

field + traps
-> imposes minimum transition width

minimum width
-> finite carrier transit delay.
```

This is a boundary-specific model relation, not a universal detector bandwidth theorem.

---

## 8. Kane-scaled form

For the simplified narrow-gap Kane mass relation

```math
m^*\simeq E_{g,b}/(2v_K^2),
```

where `E_{g,b}` is the local boundary-region gap,

```math
\sqrt{2m^*}
=\frac{\sqrt{E_{g,b}}}{v_K}.
```

Write

```math
\delta_t=\Delta_t/E_{g,b}.
```

Then

```math
\boxed{
F_{\rm TAT}
=\frac{4E_{g,b}^2}
{3q\hbar v_K}
\delta_t^{3/2}.
}
```

The width floor becomes

```math
\boxed{
w_{\rm TAT}
=
\frac{3\alpha\hbar v_K}
{4}
\frac{\Delta E_g}
{E_{g,b}^2}
\frac{\Sigma_t}{\delta_t^{3/2}}.
}
```

This form exposes three useful trends within the simplified model:

1. increasing the boundary gap raises the TAT field scale roughly as `E_g,b^2`;
2. shallow traps close to the conduction band are severe because the required width grows as `delta_t^{-3/2}`;
3. the electrostatic cost grows only linearly with the imposed gap step `Delta E_g`.

Therefore a wider-gap boundary can genuinely help, provided it does not introduce shallow interface/trap states.

---

## 9. Equivalent trap-depth requirement at fixed geometry

For a chosen boundary width `w`, the compensation field is

```math
F_b=\alpha\Delta E_g/(qw).
```

Using the repository ratio

```math
F_{\rm TAT}/F_K
=\frac{16}{3\pi}\delta_t^{3/2},
```

a required exponent margin `Sigma_t` gives

```math
\boxed{
\delta_t
\ge
\left[
\frac{3\pi}{16}
\Sigma_t
\frac{F_b}{F_K(E_{g,b})}
\right]^{2/3}.
}
```

Equivalently,

```math
\boxed{
\Delta_t
\ge
E_{g,b}
\left[
\frac{3\pi}{16}
\Sigma_t
\frac{F_b}{F_K(E_{g,b})}
\right]^{2/3}.
}
```

This is a useful **trap-exclusion-depth** diagnostic: traps too close to the local conduction edge have too small a TAT exponent for the chosen compensated boundary field.

Again, it is an exponent criterion only, not a full current threshold.

---

## 10. Representative scale, not a device prediction

Take only as an illustrative scale:

```text
narrow-gap side Eg,a = 0.124 eV
boundary gap Eg,b = 0.250 eV
Delta Eg = 0.126 eV
alpha = 2/3
w = 50 nm
vK = 1.07e6 m/s
```

Minimum barrier-free compensation gives approximately

```math
F_b\approx1.68\times10^4\ {\rm V/cm}.
```

In the simplified Kane scaling,

```math
F_K(E_{g,b})\approx6.97\times10^5\ {\rm V/cm}.
```

For exponent margin

```math
\Sigma_t=10,
```

the trap-depth criterion is approximately

```math
\delta_t\gtrsim0.27,
```

or

```math
\Delta_t\gtrsim0.068\ {\rm eV}.
```

This should not be interpreted as a measured HgCdTe trap threshold. It only shows that a tens-of-nanometers compensated boundary can be benign for sufficiently deep traps while remaining very vulnerable to shallow states near the conduction edge.

The dominant uncertainty is therefore likely to be the **actual trap/interface spectrum and prefactor**, not the geometrical crossing time by itself.

---

## 11. Direct BTBT comparison

The same compensation field can be compared with the local wide-gap direct-Zener scale

```math
F_K(E_{g,b})
=\frac{\pi E_{g,b}^2}
{4q\hbar v_K}.
```

A direct-BTBT exponent margin `Sigma_Z` requires

```math
\boxed{
w
\ge
\frac{\alpha\Delta E_g}
{qF_K(E_{g,b})}
\Sigma_Z.
}
```

Because near-band-edge traps can have

```math
F_{\rm TAT}\ll F_K,
```

TAT generally supplies the stricter boundary-width criterion in the trap-limited regime.

This is consistent with the repository's earlier TAT/BTBT crossover analysis.

---

## 12. Prior-art boundary

The following ingredients are established prior HgCdTe detector physics:

- compositionally graded heterojunctions;
- wide-gap unipolar barrier layers;
- composition and doping modulation to remove minority-carrier band discontinuities;
- delta doping near barriers;
- TAT and direct BTBT in HgCdTe junctions.

In particular, HgCdTe nBn work has shown that composition grading plus doping modulation or delta doping can remove undesirable band discontinuities while maintaining minority-carrier collection and reducing dark current.

Therefore this note does **not** claim the boundary architecture as new.

The repository contribution here is only the stripped-down gedanken accounting:

> once barrier-free extraction fixes a minimum compensating potential drop, a chosen TAT exponent fixes a minimum transition width and therefore a minimum geometrical transit time.

The mathematical priority of that rearranged inequality is unassessed and no novelty claim is made.

---

## 13. Important caveats

The model assumes

- one-dimensional monotonic band transition;
- approximately uniform compensation field;
- a single local TAT exponent;
- no thermionic barrier/reflection for the useful electron at minimum compensation;
- no quantum reflection from rapid mass/composition variation;
- no interface dipoles beyond the adopted band-offset model;
- no self-consistent mobile-charge redistribution inside the boundary;
- no trap-density or occupation prefactor model;
- no nonlocal impact ionization;
- no Auger/SRH generation elsewhere in the device.

For `w` approaching a few microscopic Kane lengths, the local WKB/continuum treatment itself must be reconsidered.

---

## 14. Next decisive attack

The simple boundary result indicates that **shallow traps/interface states** are more dangerous than the geometrical delay in a plausible wide-gap transition.

The next step should therefore stop treating `Delta_t` as arbitrary.

Use measured or fitted HgCdTe trap energies/densities for relevant graded/junction structures and ask:

1. which trap energies dominate the exponent at 77 K?
2. how does the required compensation field alter trap occupation?
3. does delta doping needed for band alignment increase/decrease the local field maximum?
4. can the boundary remain TAT-limited below the direct-BTBT scale while adding negligible transit delay?
5. if so, the dominant material resource is no longer speed but **defect-spectrum control at the high-field boundary**.