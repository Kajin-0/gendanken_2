# Spectral Timing Transport Tomography — Focused Prior-Art Audit

**Date:** 2026-08-09  
**Status:** focused collision search; negative search is not priority evidence

## 1. Candidate statement under review

The repository is **not** claiming that wavelength-dependent absorption depth changes photodiode response time. That is established.

The narrower candidate is:

> In a monotonic graded-gap absorber, photon energy provides an internal position coordinate. If the wavelength-dependent generation kernel is known, wavelength-resolved timing can be inverted to recover a spatial carrier-delay / effective-velocity profile.

Sharp limit:

```math
\boxed{
v_{\rm eff}[x_g(E_\gamma)]
=\frac1{G\,dT/dE_\gamma}.
}
```

Finite-depth linear inverse:

```math
\boxed{
\bar T_i
=\int_0^L K_i(s)q(s)ds,
\qquad
q(s)=1/v_{\rm eff}(s),
}
```

with

```math
\boxed{
K_i(s)
=P(X_g\le s|E_{\gamma,i},{\rm abs}).
}
```

---

## 2. Wavelength-dependent generation depth and photodiode bandwidth are established

### Jang et al., IEEE Photonics Technology Letters 15, 281–283 (2003)

Title:

`Wavelength Dependent Characteristics of High-Speed Metamorphic Photodiodes`

DOI:

`10.1109/LPT.2002.806886`

The authors measured RF response at `0.85`, `1.33`, and `1.55 um` and reported approximately

```text
43 GHz
54 GHz
62 GHz
```

respectively for the stated condition.

Their interpretation explicitly uses the fact that different wavelengths generate carriers in different heterostructure layers, changing the carrier transit path.

This is direct prior art for

```text
wavelength
-> generation region
-> carrier transit
-> bandwidth.
```

None of those ingredients is new.

---

## 3. The same physics remains active in modern high-speed photodiodes

A 2026 high-speed InGaAs/GaAsSb detector study reports different bandwidths at `1.55 um` and `2.0 um` and attributes the difference to wavelength-dependent carrier-generation profiles.

Shorter-wavelength light is also absorbed in contact material, adding slow minority-carrier transport; longer-wavelength light is generated more selectively in the fast intrinsic region.

Thus

```text
spectral generation profile
-> timing / bandwidth
```

is established current photodiode physics.

---

## 4. Graded-bandgap acceleration is established

Primary high-speed detector literature uses graded bandgap / composition profiles to create internal carrier drive and reduce transit delay.

This includes

- uni-traveling-carrier photodiodes;
- zero-bias graded-band photodiodes;
- graded HgCdTe detectors and e-APDs.

Therefore

```text
graded bandgap
-> built-in carrier drive
-> faster response
```

is established.

---

## 5. HgCdTe already has direct position-resolved impulse-response prior art

### Perrais et al., Journal of Electronic Materials 38, 1790–1799 (2009)

Title:

`Study of the Transit-Time Limitations of the Impulse Response in Mid-Wave Infrared HgCdTe Avalanche Photodiodes`

DOI:

`10.1007/s11664-009-0802-7`

This is a particularly important collision.

The paper reports HgCdTe APD impulse-response measurements using **localized photoexcitation at varying positions in the depletion layer**.

That means the broad measurement concept

```text
choose carrier-generation position
-> measure impulse response / transit behavior
```

already exists directly in HgCdTe.

Therefore the repository cannot claim the idea of spatial transit-time mapping itself.

---

## 6. HgCdTe grading and timing are also established

### Singh et al., Solid-State Electronics 142, 41–46 (2018)

DOI:

`10.1016/j.sse.2018.02.002`

This work explicitly reports the effect of bandgap grading on HgCdTe e-APD impulse response and states that composition grading reduces diffusion so the response becomes transit-time limited.

Thus both

```text
position-dependent transit timing
```

and

```text
grading-dependent transit timing
```

are strong prior art in HgCdTe.

---

## 7. What remains potentially distinct

The focused search did not find an inspected primary detector source that explicitly uses

```text
known monotonic Eg(x)
+
wavelength sweep
->
internal generation-position scan
->
linear inversion of timing data
->
spatial q(x)=1/v_eff(x) reconstruction.
```

The distinction is therefore not

```text
"we can measure transit time versus position."
```

That was already done by localized excitation.

The narrower candidate is

> **use the band-gap gradient itself as an internal spectral position encoder, so wavelength-resolved timing replaces a physically scanned/localized excitation spot and can be inverted into a spatial transport profile.**

This interpretation is more credible and more constrained.

---

## 8. Full finite-depth formulation strengthens the method beyond differentiation

The repository now writes the measured mean timing data as

```math
\boxed{
\mathbf T
=\mathbf A\mathbf q+c\mathbf1,
}
```

where

```math
q_j\approx1/v_{\rm eff}(x_j)
```

and the matrix rows are determined by the wavelength-dependent cumulative generation kernels.

This is preferable to numerical differentiation because

- finite optical depth is included directly;
- an unknown wavelength-independent electronics delay `c` can be fitted simultaneously;
- regularization can stabilize the spatial inversion;
- the output is an explicit transport profile rather than only a bandwidth trend.

---

## 9. Synthetic inversion result

The deterministic regression

`numerics/hgcdte_spectral_timing_linear_inverse.py`

uses

```text
nonuniform synthetic v(x)
finite optical generation kernels
unknown common delay
0.1% timing noise
```

and reconstructs the delay-density profile with smoothness regularization.

For the fixed regression case it recovers

```text
velocity RMS relative error ≈ 0.9%
```

and localizes the imposed slow-transport region to within approximately one spatial cell while also recovering the unknown common delay.

This is **not** an experimental performance claim.

It only shows that the linear inverse is numerically capable of recovering nonuniform transport information in a controlled synthetic case.

---

## 10. Reviewer-level risk

A skeptical reviewer can still reasonably say

> wavelength-dependent generation depth is old, position-dependent HgCdTe transit measurements are old, and the inversion is elementary once the geometry is written down.

That criticism remains serious.

The result becomes publication-relevant only if the **spectral encoding method provides a practical capability** beyond those ingredients, for example

- reconstructing a nonuniform velocity profile without spatially scanning the device;
- identifying a buried slow transport region;
- working through an inaccessible backside/frontside geometry where localized internal excitation is difficult;
- agreeing quantitatively with independent position-resolved measurements or Monte Carlo transport;
- extracting transport information from one tunable-wavelength optical access path.

The scientific value must come from the demonstrated inverse metrology, not from claiming the calculus identity itself.

---

## 11. Current collision verdict

### Established — no novelty claim

- wavelength-dependent absorption / generation depth;
- wavelength-dependent photodiode bandwidth;
- graded-bandgap carrier acceleration;
- graded HgCdTe impulse-response improvement;
- localized-position HgCdTe transit-time measurements;
- using optical excitation wavelength to probe semiconductor dynamics more broadly.

### Candidate underexplored method

The inspected literature did not locate the specific combination

```text
monotonic graded Eg(x)
+
spectral generation kernels
+
wavelength-resolved timing
+
regularized inverse reconstruction of spatial delay density.
```

**Status:** candidate underexplored measurement/inverse method; priority unproven.

Negative search is not novelty evidence.

---

## 12. Best validation path

The strongest validation is now obvious:

> compare the spectral inversion against an independent spatially localized excitation measurement on the same or equivalent graded structure.

Perrais-style localized excitation supplies exactly the kind of external benchmark needed.

A convincing validation sequence would be

1. independently know `E_g(x)`;
2. calculate or measure `p(x|lambda)`;
3. measure wavelength-resolved group delay / impulse centroid;
4. invert for `q(x)`;
5. independently measure position-resolved transit timing;
6. compare the two profiles.

Agreement would transform the present work from an elementary analytic rearrangement into a demonstrated non-contact/internal spectral transport tomography method.

---

## 13. Next decisive work

The next calculation should quantify **experimental spatial resolution** from

- optical generation-kernel width;
- source wavelength resolution;
- uncertainty in `E_g(x)`;
- timing precision;
- regularization / inversion conditioning.

Only after that should the project reassess whether this is a publishable method or simply a useful analysis tool.
