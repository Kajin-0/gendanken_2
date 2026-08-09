"""Phase-noise stress test for the published sample-B spectral timing matrix.

The calculation asks how many coarse transport modes survive wavelength-
dependent RF phase noise after the wavelength-independent common phase has
been projected out.

This is an illustrative inverse-conditioning experiment, not a claim about
sample B's actual carrier velocity or a specific instrument's phase accuracy.
"""

from __future__ import annotations

import numpy as np

from hgcdte_published_sample_b_forward_matrix import (
    LAMBDA_GRID,
    N_CELL,
    PABS_MIN,
    W_UM,
    optical_distribution,
)

FIELD_V_CM = 150.0
F_HZ = 1.0e9
V0_M_S = 1.0e5

SLOW_CENTER_UM = 2.30
SLOW_SIGMA_UM = 0.35
SLOW_FRACTION = 0.25

RANKS = (3, 5)
PHASE_NOISE_DEG = (0.03, 0.05, 0.10, 0.25)
N_MONTE_CARLO = 1000
SEED = 20260809


def build_phase_operator() -> tuple[np.ndarray, np.ndarray]:
    rows = []
    p_abs = []
    for wavelength in LAMBDA_GRID:
        p, _, _, timing_row = optical_distribution(wavelength, FIELD_V_CM)
        rows.append(timing_row)
        p_abs.append(p)

    rows = np.asarray(rows)
    p_abs = np.asarray(p_abs)
    keep = p_abs >= PABS_MIN
    A_um = rows[keep]

    # Project out the wavelength-independent timing/phase mode.
    A_delta_um = A_um - np.mean(A_um, axis=0, keepdims=True)

    # If q is in ps/um, A*q is ps. At f Hz, one ps produces
    # 360*f*1e-12 degrees of phase.
    phase_deg_per_ps = 360.0 * F_HZ * 1.0e-12
    B = -phase_deg_per_ps * A_delta_um
    return B, LAMBDA_GRID[keep]


def synthetic_transport_anomaly() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    dx_um = W_UM / N_CELL
    x_um = (np.arange(N_CELL) + 0.5) * dx_um

    gaussian = np.exp(
        -0.5 * ((x_um - SLOW_CENTER_UM) / SLOW_SIGMA_UM) ** 2
    )
    v_true = V0_M_S * (1.0 - SLOW_FRACTION * gaussian)

    # 1 um / v in ps = 1e6 / v.
    q_true_ps_um = 1.0e6 / v_true
    q0_ps_um = np.full_like(q_true_ps_um, 1.0e6 / V0_M_S)
    delta_q = q_true_ps_um - q0_ps_um
    return x_um, q_true_ps_um, delta_q


def main() -> None:
    B, wavelengths = build_phase_operator()
    x_um, _, delta_q = synthetic_transport_anomaly()

    U, singular, Vt = np.linalg.svd(B, full_matrices=False)
    phase_signal = B @ delta_q

    print("Published sample-B phase-noise stress test")
    print(f"field = {FIELD_V_CM:.0f} V/cm, f = {F_HZ/1e9:.1f} GHz")
    print(
        f"synthetic slowdown = {100*SLOW_FRACTION:.0f}% at "
        f"{SLOW_CENTER_UM:.2f} um, sigma={SLOW_SIGMA_UM:.2f} um"
    )
    print(
        f"wavelengths retained = {len(wavelengths)}, "
        f"{wavelengths[0]:.2f}-{wavelengths[-1]:.2f} um"
    )
    print(f"phase anomaly peak-to-peak = {np.ptp(phase_signal):.4f} deg")
    print()

    rng = np.random.default_rng(SEED)
    stored = {}

    for rank in RANKS:
        V = Vt[:rank].T
        target_projection = V @ (V.T @ delta_q)
        truncation_error = np.linalg.norm(target_projection - delta_q) / np.linalg.norm(
            delta_q
        )
        peak_x = x_um[np.argmax(target_projection)]
        amplitude_ratio = np.max(target_projection) / np.max(delta_q)

        print(f"rank {rank} noiseless recoverable projection")
        print(f"  full-profile truncation error = {truncation_error:.4f}")
        print(f"  peak position = {peak_x:.4f} um")
        print(f"  peak amplitude / true = {amplitude_ratio:.4f}")

        for sigma_deg in PHASE_NOISE_DEG:
            relative_errors_to_projection = []
            relative_errors_to_truth = []
            peak_errors = []

            for _ in range(N_MONTE_CARLO):
                noise = rng.normal(0.0, sigma_deg, phase_signal.size)
                noise -= np.mean(noise)
                y = phase_signal + noise

                coeff = (U[:, :rank].T @ y) / singular[:rank]
                estimate = V @ coeff

                relative_errors_to_projection.append(
                    np.linalg.norm(estimate - target_projection)
                    / np.linalg.norm(target_projection)
                )
                relative_errors_to_truth.append(
                    np.linalg.norm(estimate - delta_q) / np.linalg.norm(delta_q)
                )
                peak_errors.append(abs(x_um[np.argmax(estimate)] - SLOW_CENTER_UM))

            result = (
                float(np.median(relative_errors_to_projection)),
                float(np.median(relative_errors_to_truth)),
                float(np.quantile(peak_errors, 0.90)),
            )
            stored[(rank, sigma_deg)] = result
            print(
                f"  sigma_phi={sigma_deg:0.2f} deg: "
                f"median noise error vs rank-{rank} target={result[0]:.3f}, "
                f"median full-profile error={result[1]:.3f}, "
                f"90% peak-location error={result[2]:.3f} um"
            )
        print()

    # Stable qualitative regressions.
    assert 0.90 < np.ptp(phase_signal) < 1.00
    assert stored[(3, 0.10)][0] < 0.25
    assert stored[(3, 0.10)][2] < 0.20
    assert stored[(3, 0.25)][0] > 0.30
    assert stored[(5, 0.10)][0] > 0.60

    print(
        "PASS: coarse 3-mode anomaly localization survives ~0.1 deg phase noise; "
        "higher spatial rank requires substantially better phase precision"
    )


if __name__ == "__main__":
    main()
