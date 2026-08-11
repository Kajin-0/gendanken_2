"""Two-state hot->cold spatial closure stress.

Purpose
-------
Verify analytically and numerically that wavelength-independent hot-state
initialization adds one spatial mode rather than destroying the spectral-depth
hierarchy, and quantify the sensitivity to wavelength-dependent initialization
for the current HgCdTe quartet.

This is a theory stress, not a calibrated thermalization model for HgCdTe.
"""

from __future__ import annotations

import numpy as np


L_M = 7.6e-6
VC = 3.45e4
VH = 6.90e4
F0 = 0.5
FREQUENCY_HZ = 100e6
S = 1j * 2.0 * np.pi * FREQUENCY_HZ

Z4_M = np.asarray((2.5, 3.0, 3.5, 4.0)) * 1e-6
D4_M = L_M - Z4_M

Z6_M = np.asarray((2.25, 2.75, 3.25, 3.75, 4.25, 4.75)) * 1e-6
D6_M = L_M - Z6_M

# Generation-weighted mean total excess energies from the same Hansen/Moazzami
# quartet used by the manuscript, in eV.
EXCESS_E4_EV = np.asarray(
    (0.05235318022941468,
     0.05242755136863800,
     0.05247820828455033,
     0.05247262787235149)
)

GRADIENT_TARGET_PHASE_DEG = 0.01198
TEN_PERCENT_TARGET_DEG = 0.1 * GRADIENT_TARGET_PHASE_DEG


def cold_current(d: float, s: complex = S) -> complex:
    if abs(s) < 1e-30:
        return complex(d)
    return VC / s * (1.0 - np.exp(-s * d / VC))


def hot_current(d: float, rho: float, s: complex = S) -> complex:
    """Exact deterministic hot->cold expected raw-current transform."""
    if abs(s) < 1e-30:
        # The RF regression never uses this branch. A tiny-s limit is enough
        # for numerical continuity if called manually.
        s = 1e-30 + 0j

    A = (s * VH + rho * VC) / (s * (s + rho))
    Bc = -rho * VC**2 / (s * (VC * (s + rho) - s * VH))
    Bh = -A - Bc

    lambda_c = s / VC
    lambda_h = (s + rho) / VH
    return A + Bc * np.exp(-lambda_c * d) + Bh * np.exp(-lambda_h * d)


def mixed_current(d: float, rho: float, f_hot: float, s: complex = S) -> complex:
    return (1.0 - f_hot) * cold_current(d, s) + f_hot * hot_current(d, rho, s)


def log_four_color_closure(currents: np.ndarray) -> complex:
    differences = np.diff(currents)
    return complex(
        2.0 * np.log(differences[1])
        - np.log(differences[0])
        - np.log(differences[2])
    )


def hankel_minors(first_differences: np.ndarray) -> np.ndarray:
    return np.asarray(
        [
            first_differences[i] * first_differences[i + 2]
            - first_differences[i + 1] ** 2
            for i in range(3)
        ]
    )


def constant_fraction_stress(ell_um: float, f_hot: float = F0):
    rho = VH / (ell_um * 1e-6)
    currents4 = np.asarray([mixed_current(d, rho, f_hot) for d in D4_M])
    c4 = log_four_color_closure(currents4)

    currents6 = np.asarray([mixed_current(d, rho, f_hot) for d in D6_M])
    differences6 = np.diff(currents6)
    W = hankel_minors(differences6)
    rank2_residual = W[1] ** 2 - W[0] * W[2]

    return rho, c4, W, rank2_residual, differences6


def initialization_sensitivity(ell_um: float, slope_per_ev: float = 1.0):
    rho = VH / (ell_um * 1e-6)
    centered = EXCESS_E4_EV - EXCESS_E4_EV.mean()
    fractions = F0 + slope_per_ev * centered

    currents = np.asarray(
        [mixed_current(d, rho, f) for d, f in zip(D4_M, fractions)]
    )
    c = log_four_color_closure(currents)

    baseline = np.asarray([mixed_current(d, rho, F0) for d in D4_M])
    c0 = log_four_color_closure(baseline)
    return fractions, c - c0


def second_mode_significance_per_eta(ell_um: float, f_hot: float = F0) -> float:
    """Return Z2/eta for sigma_J = eta * mean(abs(first difference))."""
    _, _, W, _, differences = constant_fraction_stress(ell_um, f_hot)
    d0, d1, d2 = differences[:3]
    noise_coeff = np.sqrt(
        abs(d2) ** 2
        + abs(d2 + 2.0 * d1) ** 2
        + abs(d0 + 2.0 * d1) ** 2
        + abs(d0) ** 2
    )
    mean_step = float(np.mean(np.abs(differences)))
    return float(abs(W[0]) / (noise_coeff * mean_step))


def main() -> None:
    print("Two-state hot->cold closure stress")
    print(f"v_c={VC:.4g} m/s, v_h={VH:.4g} m/s, f0={F0}")
    print(f"RF={FREQUENCY_HZ/1e6:.1f} MHz")
    print()

    print("constant initialization: one-mode C4 and exact rank-two check")
    print("ell_h [um], C4 phase [deg], relative rank-two residual")

    rows = []
    for ell_um in (0.25, 0.5, 1.0, 2.0, 5.0, 10.0):
        _, c4, W, rank2_residual, _ = constant_fraction_stress(ell_um)
        scale = abs(W[0] * W[2]) + abs(W[1] ** 2) + 1e-300
        relative = abs(rank2_residual) / scale
        phase_deg = float(np.degrees(c4.imag))
        rows.append((ell_um, phase_deg, relative))
        print(f"{ell_um:6.2f}, {phase_deg:+.9e}, {relative:.3e}")

    print()
    print("wavelength-dependent initialization sensitivity")
    print("ell_h [um], allowed peak-to-peak Delta f for 10% target")

    allowed = []
    e_span = float(np.ptp(EXCESS_E4_EV))
    for ell_um in (0.25, 0.5, 1.0, 2.0, 5.0, 10.0):
        _, delta_c = initialization_sensitivity(ell_um, 1.0)
        sensitivity_deg_per_ev_inv = abs(float(np.degrees(delta_c.imag)))
        slope_limit = TEN_PERCENT_TARGET_DEG / sensitivity_deg_per_ev_inv
        delta_f = slope_limit * e_span
        allowed.append((ell_um, delta_f))
        print(f"{ell_um:6.2f}, {100.0*delta_f:.4f} %")

    print()
    z_per_eta = second_mode_significance_per_eta(5.0, F0)
    eta = 1.56e-5
    print(f"ell_h=5 um: Z2/eta={z_per_eta:.6e}")
    print(f"at eta={eta:.3e}, Z2={z_per_eta/eta:.3f} sigma")

    # Regression anchors.
    phase_by_ell = {ell: phase for ell, phase, _ in rows}
    assert abs(phase_by_ell[0.25]) < 1e-6
    assert 8e-4 < phase_by_ell[1.0] < 9.5e-4
    assert 0.0050 < phase_by_ell[5.0] < 0.0060

    allowed_by_ell = {ell: df for ell, df in allowed}
    assert 0.0023 < allowed_by_ell[2.0] < 0.0027
    assert 0.0027 < allowed_by_ell[5.0] < 0.0032

    # Rank-two closure should be satisfied to floating-point cancellation scale.
    for _, _, relative in rows:
        assert relative < 1e-5

    assert 1.0 < z_per_eta / eta < 2.0

    print()
    print(
        "PASS: wavelength-independent hot->cold thermalization is an exact "
        "two-spatial-mode process; wavelength-dependent initialization is the "
        "separate source-state systematic."
    )


if __name__ == "__main__":
    main()
