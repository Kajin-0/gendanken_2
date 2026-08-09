# HgCdTe Transport–BTBT Phase Boundary — Which Mechanism Actually Sets the Fastest Field-Driven Transit?

**Date:** 2026-08-09  
**Status:** exact algebra combining an established empirical HgCdTe velocity-envelope form with the repository normalized BTBT model; transport coefficients remain composition/temperature/device-specific; no novelty claim

## 1. Purpose

`HGCDTE_NORMALIZED_BTBT_FRONTIER.md` normalized the direct band-to-band tunneling side of the problem but deliberately stopped before converting the allowed field into a detector speed, because low-field mobility cannot be extrapolated into the high-field HgCdTe regime.

The next question is narrower:

> If the high-field drift velocity is represented by an empirically calibrated HgCdTe velocity-field envelope, can we determine analytically whether the optimum useful field is set first by direct BTBT or by the turnover of the carrier velocity itself?

Yes.

The result is a **model-level phase boundary**, not a universal HgCdTe limit.

---

## 2. Primary-source transport boundary

Several primary HgCdTe APD studies establish that high-field carrier motion is not simply `v = mu F`.

Perrais et al., *Journal of Electronic Materials* **38**, 1790–1799 (2009), DOI `10.1007/s11664-009-0802-7`, extracted carrier velocities from MWIR APD impulse-response measurements. Their fit gave electron and hole velocity saturation above roughly `1.5 kV/cm`, with electron velocity about `2.3e7 cm/s`; the high-gain rise-time increase was partly attributed to reduced electron velocity associated with frequent impact ionization.

Rothman et al., *Journal of Electronic Materials* **43**, 2947–2954 (2014), DOI `10.1007/s11664-014-3155-9`, extracted hot-carrier velocity from SWIR APD response measurements and reported electron velocity reaching about `1e7 cm/s` near gain onset and decreasing to about `3e6 cm/s` by `100 kV/cm`.

Guerra et al., *Journal of Electronic Materials* **55**, 6628–6637 (2026), DOI `10.1007/s11664-026-12921-y`, use the empirical form

```math
\boxed{
v(F)
=\frac{\mu F}
{1+(F/d)^r}
}
```

for their simplified HgCdTe APD Monte Carlo model, with `mu`, `d`, and `r` fitted as functions of composition/device data. They explicitly caution that the far-high-field velocity dependence is not yet uniquely established and may require another formulation.

The present note therefore uses this equation only as a **generic empirical transport envelope**.

No coefficients are invented for `Hg_0.8Cd_0.2Te` at 77 K.

---

## 3. Normalize the velocity law

Define

```math
\boxed{u=F/d.}
```

Then

```math
v(F)
=\mu d\frac{u}{1+u^r}.
```

For the rectangular Ramo transit convention used in this repository,

```math
B_{\rm tr}
=c_t\frac{v}{L},
\qquad
c_t\simeq0.44295.
```

Define the natural transport-bandwidth scale

```math
\boxed{
B_0
=\frac{c_t\mu d}{L}.
}
```

Then the normalized transit response is simply

```math
\boxed{
b(u)
\equiv
\frac{B_{\rm tr}}{B_0}
=
\frac{u}{1+u^r}.
}
```

---

## 4. The velocity has one exact optimum for `r > 1`

Differentiate:

```math
\frac{db}{du}
=
\frac{1-(r-1)u^r}
{(1+u^r)^2}.
```

Thus, for

```math
r>1,
```

the field giving the maximum drift/transit speed is

```math
\boxed{
u_{\rm pk}
=(r-1)^{-1/r}.
}
```

Equivalently,

```math
\boxed{
F_{\rm pk}
=d(r-1)^{-1/r}.
}
```

At that field,

```math
\boxed{
b_{\rm pk}
=\frac{(r-1)^{1-1/r}}{r},
}
```

so

```math
\boxed{
B_{\rm pk}
=
\frac{c_t\mu d}{L}
\frac{(r-1)^{1-1/r}}{r}.
}
```

For `r = 2`, this reduces to the intuitive result

```math
F_{\rm pk}=d,
\qquad
B_{\rm pk}=\frac{c_t\mu d}{2L}.
```

---

## 5. Add the normalized HgCdTe BTBT law

From `HGCDTE_NORMALIZED_BTBT_FRONTIER.md`, define

```math
x=F/F_K,
```

```math
j=J_{\rm BTBT}/J_K,
```

with

```math
\boxed{j=x^2e^{-1/x}.}
```

Now define the dimensionless competition parameter

```math
\boxed{
\rho
=\frac{d}{F_K}.
}
```

Since

```math
F=du,
```

we have

```math
\boxed{x=\rho u.}
```

Therefore the complete normalized transport–BTBT frontier is the parametric pair

```math
\boxed{
b(u)
=\frac{u}{1+u^r},
}
```

```math
\boxed{
j(u)
=(\rho u)^2
\exp[-1/(\rho u)].
}
```

Within the combined model, **all dimensional transport information appears only through `B_0`, while the competition between velocity turnover and direct BTBT is governed by `r` and `rho`.**

---

## 6. Direct BTBT is strictly monotone in field

For

```math
j(x)=x^2e^{-1/x},
```

```math
\frac{d\ln j}{dx}
=\frac{2}{x}+\frac{1}{x^2}>0.
```

Thus direct BTBT increases strictly with field throughout this model.

By contrast, the empirical transport envelope increases only until `F_pk` and then decreases.

Therefore

> **Every field `F > F_pk` is strictly Pareto-dominated within this stripped model: it produces a lower transit speed and a higher direct-BTBT current than `F_pk`.**

This is stronger than saying that velocity merely "saturates."

Once the velocity has turned over, more field is simultaneously worse for speed and direct tunneling.

---

## 7. Exact phase boundary for a specified BTBT current budget

Suppose the allowed direct-BTBT current density is

```math
J_*.
```

Define

```math
j_*=J_*/J_K.
```

The normalized field at which the BTBT budget is reached is already known exactly:

```math
\boxed{
x_J
=\frac1
{2W_0\!\left(1/(2\sqrt{j_*})\right)}.
}
```

Therefore the corresponding field in transport units is

```math
\boxed{
u_J
=\frac{x_J}{\rho}.
}
```

The fastest field allowed by both transport turnover and the BTBT budget is then

```math
\boxed{
u_{\rm opt}
=
\min\!\left[
(r-1)^{-1/r},
\frac{x_J}{\rho}
\right].
}
```

Hence

```math
\boxed{
B_{\rm tr,max}
=
B_0
\frac{u_{\rm opt}}
{1+u_{\rm opt}^r}.
}
```

This is the central result of this note.

---

## 8. Two regimes

The direct-BTBT current that would occur at the intrinsic velocity maximum is

```math
x_{\rm pk}
=\rho(r-1)^{-1/r},
```

```math
\boxed{
j_{\rm pk}
=
[\rho(r-1)^{-1/r}]^2
\exp\!\left[
-\frac{1}
{\rho(r-1)^{-1/r}}
\right].
}
```

Then the problem divides exactly into two regimes.

### Regime A — BTBT-limited before velocity turnover

If

```math
\boxed{j_*<j_{\rm pk},}
```

then

```math
F_J<F_{\rm pk},
```

and direct BTBT stops the field increase before the empirical transport law reaches its maximum velocity.

The optimum is

```math
F_{\rm opt}=F_J.
```

### Regime B — transport-turnover-limited before direct BTBT

If

```math
\boxed{j_*\ge j_{\rm pk},}
```

then the BTBT budget still permits the velocity maximum.

The optimum is

```math
\boxed{F_{\rm opt}=F_{\rm pk}.}
```

Increasing field beyond that point is not useful even before the BTBT current ceiling is reached.

This gives a precise answer to the question

```text
which mechanism wins first?
```

once `mu`, `d`, `r`, `F_K`, `J_K`, and `J_*` are specified.

---

## 9. Long-wavelength interpretation

In the simplified Kane scaling,

```math
F_K
=\frac{\pi^3\hbar c^2}
{qv_K\lambda_c^2}.
```

Therefore

```math
\boxed{
\rho
=\frac{d}{F_K}
=\frac{dqv_K\lambda_c^2}
{\pi^3\hbar c^2}.
}
```

If the empirical turnover field `d` did not fall rapidly enough to compensate, increasing cutoff wavelength would increase `rho` approximately as

```math
\rho\propto d\lambda_c^2.
```

Because `j_pk` depends exponentially on `1/(rho u_pk)`, this can move a long-wavelength device rapidly toward the regime in which direct BTBT becomes relevant **before** the useful velocity envelope is exhausted.

This is a sharper statement than the isolated result `F_K ~ lambda_c^-2` because it compares the tunneling field scale with the actual transport-turnover scale.

However, `d(lambda_c,T,n,geometry)` is empirical and cannot presently be assumed constant.

---

## 10. What primary data already tell us qualitatively

The currently accessible primary literature does not give one universally accepted `Hg_0.8Cd_0.2Te`, 77 K, bulk `v(F)` interpolation across the full field range needed here.

What it does show is enough to establish the hierarchy of approximations:

- MWIR impulse-response data already show velocity saturation at fields of order `kV/cm`, not an unlimited `mu F` rise;
- SWIR data show that the electron velocity can decrease strongly at still higher fields;
- the 2026 empirical APD model explicitly uses a peaked velocity law and warns that its high-field continuation is not yet uniquely constrained;
- LWIR `lambda_c = 9 um`, 80 K APDs with `x ~= 0.235` were experimentally limited by tunneling current at higher reverse bias, demonstrating that the long-wave tunneling branch is technologically real.

Therefore the correct material question is not

```text
what is the mobility?
```

but

```text
where is F_pk relative to the BTBT field allowed by the stated dark-current budget?
```

---

## 11. Important non-claims

This note does **not** establish

- a calibrated `v(F)` curve for `Hg_0.8Cd_0.2Te` at 77 K;
- that Guerra et al.'s empirical velocity form is exact at arbitrarily large fields;
- that direct BTBT is the only relevant dark-current mechanism;
- that impact ionization merely modifies velocity rather than creating a separate performance constraint;
- that a single uniform field describes an optimized HgCdTe heterostructure;
- a fundamental sensitivity-speed-dark-current theorem;
- novelty of the velocity-envelope or BTBT ingredients.

---

## 12. What has actually been gained

The previous frontier required a full `v_d(F)` curve before saying anything useful.

That was too pessimistic.

Within a broad empirical HgCdTe transport family, the problem can already be reduced to a **phase boundary**:

```math
\boxed{
F_{\rm opt}
=
\min(F_{\rm pk},F_J).
}
```

The two physical mechanisms have distinct roles:

```text
transport physics
-> supplies the velocity-turnover field F_pk

BTBT physics
-> supplies the dark-current-limited field F_J.
```

Whichever field is smaller controls the fastest useful field-driven transit in this stripped model.

---

## 13. Next decisive step

Do not fit arbitrary coefficients merely to produce a completed speed curve.

Next:

1. recover or generate a defensible `v(F)` curve for near-`x=0.2` HgCdTe at approximately 77–80 K;
2. extract `F_pk` directly from that curve even if no closed interpolation is available;
3. compare `F_pk` against `F_J(lambda_c,L,J_*)` from the normalized BTBT model;
4. add impact-ionization and trap-assisted-tunneling constraints as independent field ceilings rather than burying them inside `v(F)`;
5. test whether the resulting optimum remains controlled by field physics or instead by carrier lifetime/diffusion/readout for realistic detector dimensions.

Only then should a material-specific speed–dark-current frontier be promoted.