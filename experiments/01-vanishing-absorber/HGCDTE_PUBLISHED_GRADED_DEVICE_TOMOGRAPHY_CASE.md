# Published Graded HgCdTe Structures as a Spectral Timing Tomography Test Case

**Date:** 2026-08-09  
**Status:** primary-source device instantiation / proposed validation experiment; not a reanalysis of raw data; no novelty claim

## 1. Purpose

The spectral timing inverse is now mathematically defined:

```math
\bar T_i
=\int_0^L K_i(s)q(s)ds,
\qquad
q(s)=1/v_{\rm eff}(s).
```

The project should not continue using invented device profiles if published graded HgCdTe structures already contain most of the required ingredients.

This note examines two closely related primary-source structures from the Shanghai Institute of Technical Physics:

1. the 2022 high-speed zero-bias graded MWIR detector, which supplies a real timing architecture and a large measured composition gradient;
2. the 2023 compositionally graded detector study, which supplies processed physical thicknesses and direct spectral evidence that different portions of the graded profile contribute differently to collection.

Together they define a much more realistic validation target for the proposed spectral transport tomography.

---

## 2. 2022 high-speed graded MWIR detector

Primary source:

M. Sang, G. Xu, H. Qiao, X. Li,

`High speed uncooled MWIR infrared HgCdTe photodetector based on graded bandgap structure`,

*Journal of Infrared and Millimeter Waves* 41 (2022) 972-979,

DOI `10.11972/j.issn.1001-9014.2022.06.005`.

### Reported detector facts

The paper reports

```text
n-on-p HgCdTe homojunction
room-temperature operation
zero bias
VPE graded material
Cd fraction varying from x = 0.57 to x = 0.31 across the epilayer
p-type Hg-vacancy doping ~1e16 cm^-3
200 nm ZnS/CdTe double passivation
front-side illumination.
```

The VPE detector achieved

```math
\boxed{t_{\rm response}\approx1.33\ {m ns}}
```

or approximately

```math
\boxed{750\ {m MHz}}
```

under the paper's response-time convention.

A comparison LPE device had a response around `8.7 ns`.

The authors' one-dimensional model explicitly treats the composition-gradient built-in field as a carrier-transport mechanism.

---

## 3. Existing timing experiment did not perform the spectral position scan

The 2022 work used an ultrafast short-wave laser for timing characterization.

At approximately `1.55 um`, the photon energy is larger than the local gap across the reported MWIR graded profile and the light is strongly absorbed near the illuminated surface.

Therefore this timing experiment predominantly probes the **entrance-generation regime** of the current repository model:

```text
E_gamma >= Eg,in
-> first allowed generation position pinned at the physical entrance.
```

That is precisely the regime in which changing wavelength no longer scans the nominal generation coordinate through the graded layer.

Thus the published `1.55 um` impulse/frequency-response measurement is not a test of the proposed internal spectral position encoding.

---

## 4. Composition span implies a useful spectral encoding interval

To convert Cd fraction to a nominal local gap, use the standard Hansen-Schmit-Casselman empirical expression

```math
E_g(x,T)
=-0.302
+1.93x
-0.81x^2
+0.832x^3
+5.35\times10^{-4}(1-2x)T
```

in eV.

At `T=300 K`, the reported VPE endpoint compositions give approximately

```text
x = 0.57 -> Eg ≈ 0.667 eV -> lambda_g ≈ 1.86 um
x = 0.31 -> Eg ≈ 0.304 eV -> lambda_g ≈ 4.08 um.
```

Thus an approximate spectral coordinate range is

```math
\boxed{1.9\ {\rm um}\lesssim\lambda\lesssim4.1\ {\rm um}}
```

for the nominal local bandgap endpoints under this standard formula.

The measured detector response extends to roughly the mid-wave cutoff region, so the exact usable interval must be determined from the measured `x(z), T` and absorption profile rather than the simple endpoint calculation.

---

## 5. Important bandgap-equation input audit

The machine-readable 2022 article displays an HgCdTe gap expression whose cubic coefficient appears as

```text
0.132 x^3
```

whereas the standard Hansen-Schmit-Casselman expression is

```text
0.832 x^3.
```

These are not interchangeable.

For the same reported `x=0.57 -> 0.31` endpoints at 300 K, the printed `0.132` coefficient would imply approximately

```text
2.31 um -> 4.38 um
```

rather than the standard-formula

```text
1.86 um -> 4.08 um.
```

The repository must **not silently choose between them** when fitting the actual published detector.

The experimental tomography should use the authors' directly reconstructed composition/spectral profile or a corrected explicitly justified bandgap law.

This discrepancy is an input-audit item, not a scientific result.

---

## 6. Missing dimensional input in the 2022 machine-readable text

The accessible article gives the composition endpoints and explains that the VPE composition-depth profile was reconstructed from successive material removal / FTIR analysis, but the machine-readable text does not expose a sufficiently trustworthy numerical p-layer thickness `W_p` outside the figure.

Do **not** infer `W_p` from the measured `1.33 ns` response.

That would be circular because the purpose of the proposed measurement is precisely to infer transport timing from the known spatial profile.

The 2022 structure can therefore be used immediately in **normalized depth**

```math
z/W_p
```

but a dimensional tomography calculation needs the measured profile / figure data or author-supplied layer thickness.

---

## 7. 2023 follow-on graded HgCdTe samples provide physical thickness

Primary source:

G.-Q. Xu et al.,

`Photoelectric characteristics of compositionally graded HgCdTe detector`,

*Journal of Infrared and Millimeter Waves* 42 (2023) 285-291,

DOI `10.11972/j.issn.1001-9014.2023.03.001`.

This study deliberately fabricated the junction at different parts of a compositionally graded VPE HgCdTe epilayer.

The processed samples had reported final thicknesses

```math
\boxed{L_A\approx7.6\ {\rm um}}
```

and

```math
\boxed{L_B\approx3.7\ {\rm um}}.
```

Sample A retained part of the nonlinear composition region whereas sample B removed that nonlinear region.

---

## 8. Built-in field and spectral localization are directly observed in the 2023 study

The paper reports calculated composition-gradient built-in fields of roughly

```text
100-200 V/cm
```

for the linear-composition region and local surface values around

```text
2000 V/cm
```

for the retained nonlinear-gradient region under the reported processed condition.

The authors attribute differences in the two samples' photoelectric response primarily to the composition-gradient field acting on minority carriers.

Their temperature-dependent spectral response also demonstrates that different spectral portions sample different carrier-generation / collection behavior across the graded structure.

This is strong prior art for **qualitative spectral inference of spatial carrier collection**.

It is not yet the timing inverse proposed here.

---

## 9. Why the two papers complement each other

The 2022 study supplies

```text
large monotonic composition span
+
direct high-speed timing measurement
+
front-side illumination
+
FTIR-derived composition-depth methodology.
```

The 2023 study supplies

```text
physical processed thicknesses
+
controlled retention/removal of nonlinear graded region
+
calculated built-in-field differences
+
spectral evidence of spatially different carrier collection.
```

Neither study alone performs

```text
wavelength-resolved impulse/group-delay scan
+
known generation kernels
->
spatial inverse reconstruction of q(x)=1/v_eff(x).
```

Together they show that such a test is experimentally adjacent to demonstrated HgCdTe structures and methods rather than a purely hypothetical detector.

---

## 10. Concrete proposed experiment on a VPE graded structure

Use a VPE graded n-on-p HgCdTe detector whose `x(z)` profile has been independently measured by FTIR/etch profiling or another composition-depth method.

At fixed

```text
temperature
bias
illumination geometry
optical pulse energy
spot size
readout chain,
```

sweep a short-pulse source through the local graded absorption interval.

For a 2022-like `x=0.57 -> 0.31` room-temperature profile, a first planning range is approximately

```text
~2 um to ~4.5 um,
```

with the exact wavelengths set from the actual measured `E_g(z)` / absorption profile rather than assumed endpoints.

Measure

- low-frequency group delay versus wavelength; or
- impulse centroid versus wavelength.

Then calculate

```math
p_i(x)=p(x|\lambda_i,{\rm abs})
```

and solve

```math
\boxed{
\mathbf T
=\mathbf A\mathbf q+c\mathbf1,
\qquad
q=1/v_{\rm eff}.
}
```

---

## 11. Validation against localized-position HgCdTe timing

Perrais et al. already measured HgCdTe APD impulse response with localized photoexcitation at varying positions in the depletion layer.

That prior work provides the correct validation philosophy.

The strongest experiment would compare on the same or closely matched structure:

```text
spectral internal position encoding
versus
localized spatial excitation.
```

Agreement between the independently recovered transit/delay profiles would directly test whether the graded spectral inversion is physically valid.

---

## 12. Approximate dimensional timing requirements

The 2023 thicknesses make the timing scale concrete without assuming a particular published transport velocity.

For illustration only, if

```math
v_{\rm eff}\sim10^5\ {\rm m/s},
```

then a spatial delay scale is

```math
1\ {\rm um}/v_{\rm eff}\sim10\ {\rm ps}.
```

Therefore

```text
7.6 um -> ~76 ps full-path scale
3.7 um -> ~37 ps full-path scale
4.0 um nonlinear region -> ~40 ps scale
```

under that illustrative velocity.

These are not predictions for the published samples.

They show that sub-micron-to-micron transport reconstruction requires picosecond-class differential timing even though the total published detector response can be nanosecond-scale because of other poles.

---

## 13. Why differential/group-delay timing remains preferable

The 2022 detector's measured total response is `1.33 ns`, much larger than a tens-of-picoseconds micron-scale carrier-travel contrast in the illustrative calculation above.

That does **not** automatically make the tomography impossible.

If the measured transfer function factorizes approximately as

```math
H_{\rm meas}(\Omega,\lambda)
=H_{\rm carrier}(\Omega,\lambda)
H_{\rm common}(\Omega),
```

then a wavelength-independent common delay can be fitted or canceled.

The challenge is differential timing precision, not the absolute width of the slowest common response component.

Any wavelength-dependent optical path or readout delay must be calibrated because it can mimic the transport signal.

---

## 14. Current practical feasibility verdict

The method is not yet demonstrated, but a published graded HgCdTe validation target now exists.

The 2022 / 2023 work establishes that

- composition profiles spanning useful MWIR energies can be fabricated;
- the gradient measurably alters carrier transport;
- fast timing hardware has already been applied to this material family;
- physical layer thicknesses of a few microns are realistic;
- spectral response already carries spatial collection information.

Therefore the proposed inverse experiment is **experimentally adjacent to demonstrated work**, not an exotic new fabrication program.

The remaining missing inputs are primarily

```text
actual x(z) profile in dimensional coordinates
+
calibrated alpha(lambda,z)
+
picosecond-class differential timing precision
+
independent validation of reconstructed transport.
```

---

## 15. Claim boundary

### Established prior work

- 2022 graded HgCdTe zero-bias fast detector and its measured response;
- VPE composition span `x=0.57 -> 0.31` reported in that structure;
- 2023 processed graded structures with `~7.6 um` and `~3.7 um` thicknesses;
- composition-gradient fields changing carrier collection;
- wavelength-dependent spectral response in graded HgCdTe;
- localized-position HgCdTe impulse-response measurements in earlier APD work.

### Internally derived / proposed

- treating the graded gap as a spectral internal position encoder;
- the linear timing inverse for spatial delay density;
- the proposed spectral-vs-localized validation experiment;
- the dimensional resolution accounting.

### Not established

- the exact dimensional `x(z)` of the 2022 VPE device from the currently accessible text;
- experimental inversion performance;
- a real reconstructed `v_eff(z)` profile;
- novelty / priority of the method.

---

## 16. Next decisive work

The theoretical branch has now reached the point where another generic analytic model has lower value than real data.

The next best steps are

1. obtain the actual dimensional composition profile / figure data for a published graded detector;
2. implement its wavelength-dependent optical generation kernels;
3. estimate timing/inverse resolution with its real layer thickness;
4. if raw timing data at multiple wavelengths do not exist, formulate the experiment as the primary proposed validation;
5. reassess publication readiness only after this real-device forward model is complete.
