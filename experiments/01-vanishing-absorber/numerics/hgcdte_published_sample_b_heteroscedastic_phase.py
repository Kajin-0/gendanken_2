"""Heteroscedastic phase-noise stress test for published HgCdTe sample B.

Uses the literature-constrained 150 V/cm optical matrix and asks how the
inverse changes when phase precision degrades as absorbed fraction falls.

Two deliberately simple limits are tested at fixed incident optical power:
- statistics-like: sigma_phi proportional to Pabs**(-1/2)
- additive-readout-like: sigma_phi proportional to Pabs**(-1)

These are scaling models, not complete instrument noise models.
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
SIGMA_SHORT_DEG = 0.10
N_MONTE_CARLO = 1000
SEED = 20260809

SLOW_CENTER_UM = 2.30
SLOW_SIGMA_UM = 0.35
SLOW_FRACTION = 0.25
RANK = 3


def build_matrix() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    rows = []
    pabs = []
    for wavelength in LAMBDA_GRID:
        p, _, _, timing_row = optical_distribution(wavelength, FIELD_V_CM)
        rows.append(timing_row)
        pabs.append(p)

    rows = np.asarray(rows)
    pabs = np.asarray(pabs)
    keep = pabs >= PABS_MIN
    return rows[keep], pabs[keep], LAMBDA_GRID[keep]


def anomaly() -> tuple[np.ndarray, np.ndarray]:
    dx_um = W_UM / N_CELL
    x_um = (np.arange(N_CELL) + 0.5) * dx_um
    gaussian = np.exp(-0.5 * ((x_um - SLOW_CENTER_UM) / SLOW_SIGMA_UM) ** 2)
    v_true = V0_M_S * (1.0 - SLOW_FRACTION * gaussian)
    q_true = 1.0e6 / v_true  # ps/um
    q0 = np.full_like(q_true, 1.0e6 / V0_M_S)
    return x_um, q_true - q0


def project_whiten(
    matrix: np.ndarray, data: np.ndarray, sigma: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    """Whiten diagonal covariance and project out common wavelength phase."""
    w = 1.0 / sigma
    B = matrix * w[:, None]
    y = data * w
    u = w.copy()
    Bp = B - u[:, None] * ((u @ B) / (u @ u))[None, :]
    yp = y - u * ((u @ y) / (u @ u))
    return Bp, yp


def run_case(
    A_um: np.ndarray,
    pabs: np.ndarray,
    delta_q: np.ndarray,
    x_um: np.ndarray,
    gamma: float,
    sigma_short_deg: float,
    rng: np.random.Generator,
) -> tuple[float, float, float, float, float]:
    phase_deg_per_ps = 360.0 * F_HZ * 1.0e-12
    M = -phase_deg_per_ps * A_um
    signal = M @ delta_q

    sigma = sigma_short_deg * (pabs[0] / pabs) ** gamma
    Mp, yp = project_whiten(M, signal, sigma)
    U, singular, Vt = np.linalg.svd(Mp, full_matrices=False)

    V = Vt[:RANK].T
    target = V @ (V.T @ delta_q)
    trunc = np.linalg.norm(target - delta_q) / np.linalg.norm(delta_q)

    errors = []
    locations = []
    for _ in range(N_MONTE_CARLO):
        noisy = signal + rng.normal(0.0, sigma)
        _, ypn = project_whiten(M, noisy, sigma)
        coeff = (U[:, :RANK].T @ ypn) / singular[:RANK]
        estimate = V @ coeff
        errors.append(np.linalg.norm(estimate - target) / np.linalg.norm(target))
        locations.append(abs(x_um[np.argmax(estimate)] - SLOW_CENTER_UM))

    return (
        float(sigma[-1]),
        float(np.median(errors)),
        float(np.quantile(locations, 0.90)),
        float(trunc),
        float(np.ptp(signal)),
    )


def main() -> None:
    A, pabs, wavelengths = build_matrix()
    x_um, delta_q = anomaly()
    rng = np.random.default_rng(SEED)

    print("Published sample-B heteroscedastic phase-noise test")
    print(f"short-wave sigma_phi = {SIGMA_SHORT_DEG:.3f} deg")
    print(
        f"wavelength range = {wavelengths[0]:.2f}-{wavelengths[-1]:.2f} um, "
        f"Pabs = {pabs[0]:.4f}->{pabs[-1]:.4f}"
    )
    print()

    results = {}
    for label, gamma in (
        ("equal", 0.0),
        ("statistics-like", 0.5),
        ("additive-like", 1.0),
    ):
        result = run_case(A, pabs, delta_q, x_um, gamma, SIGMA_SHORT_DEG, rng)
        results[label] = result
        print(label)
        print(f"  long-wave sigma_phi = {result[0]:.4f} deg")
        print(f"  median rank-3 noise error = {result[1]:.4f}")
        print(f"  90% peak-location error = {result[2]:.4f} um")
        print(f"  rank-3 optical truncation error = {result[3]:.4f}")
        print(f"  anomaly phase peak-to-peak = {result[4]:.4f} deg")
        print()

    ratio = pabs[0] / pabs[-1]
    print(f"absorbed-signal ratio short/long = {ratio:.3f}")
    print(f"equal-photon-statistics time/power factor = {ratio:.3f}")
    print(f"equal-additive-noise averaging-time factor = {ratio**2:.1f}")

    # Stable regression envelopes.
    assert 17.0 < ratio < 18.0
    assert 0.40 < results["statistics-like"][0] < 0.44
    assert 1.70 < results["additive-like"][0] < 1.82
    assert 0.24 < results["statistics-like"][1] < 0.33
    assert 0.40 < results["additive-like"][1] < 0.52
    assert 0.90 < results["equal"][4] < 1.00

    print("PASS: wavelength-dependent phase precision materially reduces usable inverse rank")


if __name__ == "__main__":
    main()
