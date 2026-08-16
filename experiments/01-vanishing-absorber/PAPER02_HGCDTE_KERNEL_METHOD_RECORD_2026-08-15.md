# Paper 02 — Exact Conditional HgCdTe Kernel Method Record

**Date:** 2026-08-15  
**Status:** **MACHINE-EXTRACTED FROM EXECUTABLE SOURCE / CONDITIONAL THEORETICAL MODEL**

This record is generated directly from `numerics/hgcdte_ramo_four_color_gradient_prediction.py`. It is intended to prevent manuscript prose from drifting away from the executable optical model.

## Scope

These kernels are theoretical forward-model inputs used for the Paper-02 identifiability stress. They are not experimentally measured or calibrated kernels from a specific detector. Treating them as `known` in the inverse means the same generated kernel shapes are supplied to the inverse without optical-model uncertainty.

## Module constants

```json
{
  "D_EINSTEIN": 0.023266799807791984,
  "HC_EV_UM": 1.2398419843320025,
  "H_UM": 0.5,
  "KB": 1.380649e-23,
  "L_UM": 7.6,
  "MOBILITY_M2_VS": 0.9,
  "N": 12000,
  "Q": 1.602176634e-19,
  "Q_SLOW": {
    "dtype": "float64",
    "max": 3.111560149407825e-05,
    "min": 2.658996779037278e-05,
    "shape": [
      12001
    ]
  },
  "SAT_EXPONENT": 2.2,
  "SAT_FIELD_V_M": 800000.0,
  "TARGET_MEAN_DEPTHS_UM": [
    2.5,
    3.0,
    3.5,
    4.0
  ],
  "TAU": {
    "dtype": "float64",
    "max": 2.2045924207571763e-10,
    "min": 0.0,
    "shape": [
      12001
    ]
  },
  "T_K": 300.0,
  "V": {
    "dtype": "float64",
    "max": 37608.16891106059,
    "min": 32138.218513639036,
    "shape": [
      12001
    ]
  },
  "V_HARMONIC": 34473.49237184506,
  "X": {
    "dtype": "float64",
    "max": 0.55,
    "min": 0.32,
    "shape": [
      12001
    ]
  },
  "X_BACK": 0.32,
  "X_FRONT": 0.55,
  "Z_M": {
    "dtype": "float64",
    "max": 7.599999999999999e-06,
    "min": 0.0,
    "shape": [
      12001
    ]
  },
  "Z_UM": {
    "dtype": "float64",
    "max": 7.6,
    "min": 0.0,
    "shape": [
      12001
    ]
  }
}
```

## Six manuscript channels

| target mean [um] | wavelength [um] | absorbed probability | reintegrated mean [um] | sigma [um] |
|---:|---:|---:|---:|---:|
| 2.000 | 2.059342009 | 0.99999608 | 2.000000000 | 0.783254 |
| 2.500 | 2.134650687 | 0.999984721 | 2.500000000 | 0.787048 |
| 3.000 | 2.215042347 | 0.999943407 | 3.000000000 | 0.789835 |
| 3.500 | 2.301173443 | 0.999801116 | 3.500000000 | 0.790930 |
| 4.000 | 2.393906801 | 0.99933764 | 4.000000000 | 0.788849 |
| 4.500 | 2.494502544 | 0.997909184 | 4.500000000 | 0.780666 |

## Locally defined executable functions

The following functions are copied verbatim from the executable module by `inspect.getsource`. This is a reproducibility record, not proposed manuscript formatting.

### `alpha_moazzami`

```python
def alpha_moazzami(E: float):
    gap = eg_hansen(X)
    fraction = (E - gap) / E
    out = np.zeros_like(X)
    mask = fraction > 0.0
    out[mask] = k_moazzami(X[mask]) * fraction[mask] ** n_moazzami(X[mask])
    return np.maximum(out, 0.0)
```

### `analytic_point_source_low_rf_phase_deg`

```python
def analytic_point_source_low_rf_phase_deg(frequency_hz: float) -> float:
    spline = CubicSpline(Z_UM, Q_SLOW)
    zc = 0.5 * (TARGET_MEAN_DEPTHS_UM[1] + TARGET_MEAN_DEPTHS_UM[2])
    q1_per_um = float(spline(zc, 1))
    q2_per_um2 = float(spline(zc, 2))

    # h^2[2 q'-(L-zc)q''] has units s/m * um; multiply by 1e-6
    # to obtain seconds because z derivatives were taken with z in um.
    coefficient_s = (
        -H_UM**2
        * (2.0 * q1_per_um - (L_UM - zc) * q2_per_um2)
        * 1.0e-6
    )
    return float(np.degrees(2.0 * np.pi * frequency_hz * coefficient_s))
```

### `channel_currents`

```python
def channel_currents(point_current: np.ndarray, kernels: list[np.ndarray]) -> np.ndarray:
    return np.asarray(
        [np.trapezoid(kernel * point_current, Z_UM) for kernel in kernels]
    )
```

### `closure`

```python
def closure(currents: np.ndarray) -> complex:
    differences = np.diff(currents)
    return complex(
        2.0 * np.log(differences[1])
        - np.log(differences[0])
        - np.log(differences[2])
    )
```

### `deg_dx_hansen`

```python
def deg_dx_hansen(x, T=T_K):
    return 1.93 - 1.62 * x + 3.0 * 0.832 * x**2 - 2.0 * 5.35e-4 * T
```

### `eg_hansen`

```python
def eg_hansen(x, T=T_K):
    return (
        -0.302
        + 1.93 * x
        + 5.35e-4 * T * (1.0 - 2.0 * x)
        - 0.81 * x**2
        + 0.832 * x**3
    )
```

### `k_moazzami`

```python
def k_moazzami(x, T=T_K):
    return (
        -20060.0
        + 115750.0 * x
        + 32.43 * T
        - 64170.0 * x**2
        + 0.43231 * T**2
        - 101.92 * x * T
    )
```

### `main`

```python
def main() -> None:
    wavelengths = np.asarray(
        [wavelength_for_mean(depth) for depth in TARGET_MEAN_DEPTHS_UM]
    )
    optical = [optical_kernel(wavelength) for wavelength in wavelengths]
    kernels = [row[3] for row in optical]

    print("Corrected HgCdTe four-color raw-Ramo gradient prediction")
    print(
        f"v min/harmonic/max = {V.min():.3f}/{V_HARMONIC:.3f}/{V.max():.3f} m/s"
    )
    print(f"Einstein D used in DOS correction = {D_EINSTEIN:.9f} m^2/s")
    print()

    for target, wavelength, row in zip(TARGET_MEAN_DEPTHS_UM, wavelengths, optical):
        pabs, mean, variance, _ = row
        print(
            f"mean={target:.1f} um -> lambda={wavelength:.9f} um, "
            f"Pabs={pabs:.9f}, sigma_z={np.sqrt(variance):.6f} um"
        )

    print()
    print("RF, variable transport, homogeneous optical floor, excess")
    table = {}
    for frequency in FREQUENCIES_HZ:
        variable = closure(channel_currents(point_current_variable(frequency), kernels))
        homogeneous = closure(
            channel_currents(point_current_homogeneous(frequency), kernels)
        )
        excess = variable - homogeneous
        table[int(frequency)] = (variable, homogeneous, excess)
        print(
            f"{frequency/1e6:7.1f} MHz: "
            f"phase={np.degrees(variable.imag):+.9f} deg, "
            f"opt={np.degrees(homogeneous.imag):+.9f} deg, "
            f"excess={np.degrees(excess.imag):+.9f} deg"
        )

    analytic_100 = analytic_point_source_low_rf_phase_deg(100e6)
    print()
    print(f"point-source low-RF theorem @100 MHz = {analytic_100:+.9f} deg")

    # Stable anchors for this explicit conditional model.
    targets = (
        (2.1345, 2.1348),
        (2.2149, 2.2152),
        (2.3010, 2.3014),
        (2.3937, 2.3941),
    )
    for wavelength, (lo, hi) in zip(wavelengths, targets):
        assert lo < wavelength < hi
    assert min(row[0] for row in optical) > 0.9993
    assert 3.21e4 < V.min() < 3.23e4
    assert 3.75e4 < V.max() < 3.77e4

    var100, opt100, exc100 = table[int(100e6)]
    var500, opt500, exc500 = table[int(500e6)]
    var1000, opt1000, exc1000 = table[int(1e9)]

    assert -0.0101 < np.degrees(var100.imag) < -0.0097
    assert 0.0023 < np.degrees(opt100.imag) < 0.0027
    assert -0.0126 < np.degrees(exc100.imag) < -0.0121

    assert -0.049 < np.degrees(var500.imag) < -0.047
    assert 0.011 < np.degrees(opt500.imag) < 0.013
    assert -0.061 < np.degrees(exc500.imag) < -0.059

    assert -0.088 < np.degrees(var1000.imag) < -0.084
    assert 0.022 < np.degrees(opt1000.imag) < 0.025
    assert -0.112 < np.degrees(exc1000.imag) < -0.108

    assert -0.0128 < analytic_100 < -0.0123

    print()
    print(
        "PASS: after correcting the observable and removing the upstream-boundary "
        "confound, this explicit high-Peclet HgCdTe stress gives a finite raw-"
        "Ramo four-color gradient closure.  The 100-MHz gradient-sensitive "
        "excess agrees closely with the independent point-source low-RF "
        "slowness-gradient theorem."
    )
```

### `n_moazzami`

```python
def n_moazzami(x, T=T_K):
    return 0.74487 - 0.44513 * x + (0.000799 - 0.000757 * x) * T
```

### `optical_kernel`

```python
def optical_kernel(wavelength_um: float):
    alpha = alpha_moazzami(HC_EV_UM / wavelength_um)
    tau = np.concatenate(
        ([0.0], cumulative_trapezoid(alpha, Z_UM * 1.0e-4))
    )
    density = alpha * 1.0e-4 * np.exp(-tau)
    pabs = float(1.0 - np.exp(-tau[-1]))
    density /= np.trapezoid(density, Z_UM)
    mean = float(np.trapezoid(Z_UM * density, Z_UM))
    variance = float(np.trapezoid((Z_UM - mean) ** 2 * density, Z_UM))
    return pabs, mean, variance, density
```

### `point_current_homogeneous`

```python
def point_current_homogeneous(frequency_hz: float) -> np.ndarray:
    omega = 2.0 * np.pi * frequency_hz
    distance_m = (L_UM - Z_UM) * 1.0e-6
    return (
        V_HARMONIC
        * (1.0 - np.exp(-1j * omega * distance_m / V_HARMONIC))
        / (1j * omega)
    )
```

### `point_current_variable`

```python
def point_current_variable(frequency_hz: float) -> np.ndarray:
    omega = 2.0 * np.pi * frequency_hz
    phase = np.exp(-1j * omega * TAU)
    inner = remaining_integral(phase)
    return np.exp(1j * omega * TAU) * inner
```

### `remaining_integral`

```python
def remaining_integral(y: np.ndarray) -> np.ndarray:
    cumulative = np.concatenate(([0.0], cumulative_trapezoid(y, Z_M)))
    return cumulative[-1] - cumulative
```

### `velocity_profile`

```python
def velocity_profile() -> np.ndarray:
    dx_dz_m = (X_BACK - X_FRONT) / (L_UM * 1.0e-6)
    force_field = np.abs(deg_dx_hansen(X) * dx_dz_m)
    v_field = (
        MOBILITY_M2_VS
        * force_field
        / (1.0 + (force_field / SAT_FIELD_V_M) ** SAT_EXPONENT)
    )

    # Reduced repository DOS-gradient correction:
    # Nc ~ (m*)^(3/2), m* ~ Eg, hence d ln Nc/dz ~ 3/2 d ln Eg/dz.
    gap = eg_hansen(X)
    dln_gap_dz = deg_dx_hansen(X) * dx_dz_m / gap
    v_dos = D_EINSTEIN * 1.5 * dln_gap_dz
    return v_field + v_dos
```

### `wavelength_for_mean`

```python
def wavelength_for_mean(target_um: float) -> float:
    return float(
        brentq(
            lambda wavelength: optical_kernel(wavelength)[1] - target_um,
            1.95,
            3.20,
        )
    )
```
