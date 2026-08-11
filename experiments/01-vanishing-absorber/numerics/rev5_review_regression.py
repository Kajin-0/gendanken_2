#!/usr/bin/env python3
"""Numerical regression for Revision 5 adversarial-review corrections."""
from __future__ import annotations

import numpy as np

D = 0.02327
W = 3.45e4
H = 0.5e-6
KAPPA = 0.0
FREQS = np.array([100e6, 500e6, 1e9])
EXPECTED_SEP = np.array([9.1034664e-3, 4.52129326e-2, 8.86871650e-2])
EXPECTED_SNR_DB = np.array([116.2359, 88.3937, 76.6897])
EXPECTED_ANNIHILATION_DB = np.array([46.252, 32.319, 26.431])


def transport_gamma(freq: float) -> complex:
    s = 1j * 2.0 * np.pi * freq
    return (np.sqrt(W * W + 4.0 * D * (KAPPA + s)) - W) / (2.0 * D)


def finite_boundary_roots(freq: float) -> tuple[complex, complex]:
    s = 1j * 2.0 * np.pi * freq
    disc = np.sqrt(W * W + 4.0 * D * (KAPPA + s))
    # Roots of D r^2 + W r - (kappa+s) = 0.
    return ((-W + disc) / (2.0 * D), (-W - disc) / (2.0 * D))


def main() -> None:
    print("Revision 5 adversarial-review regression")
    print("RF       |1-q_tr|      best-case SNR   five-color penalty")
    products = []
    for f, sep_ref, snr_ref, ann_ref in zip(
        FREQS, EXPECTED_SEP, EXPECTED_SNR_DB, EXPECTED_ANNIHILATION_DB
    ):
        gamma = transport_gamma(float(f))
        q = np.exp(-gamma * H)
        sep = abs(1.0 - q)

        # From |q1-q2| >= 7.33 sqrt(eta), eta=sigma_J/|d|.
        eta = (sep / 7.33) ** 2
        snr_db = 20.0 * np.log10(1.0 / eta)

        cost5_over_cost4 = 1.87 / abs(gamma * H)
        ann_db = 20.0 * np.log10(cost5_over_cost4)

        rp, rm = finite_boundary_roots(float(f))
        qp, qm = np.exp(rp * H), np.exp(rm * H)
        product = qp * qm
        products.append(product)

        assert np.isclose(sep, sep_ref, rtol=3e-6)
        assert np.isclose(snr_db, snr_ref, atol=2e-3)
        assert np.isclose(ann_db, ann_ref, atol=2e-3)
        assert abs(product.imag) < 1e-13
        assert product.real > 0.0

        print(
            f"{f/1e6:4.0f} MHz  {sep:12.8f}   {snr_db:9.3f} dB     {ann_db:9.3f} dB"
        )

    # Branch-free finite-boundary product is RF independent and equals exp(-w h / D).
    expected_product = np.exp(-W * H / D)
    assert all(np.isclose(p.real, expected_product, rtol=1e-12, atol=1e-15) for p in products)
    assert np.ptp([p.real for p in products]) < 1e-13
    print(f"branch-free q+q- = {expected_product:.12f} (positive real and RF independent)")

    # The inherited field-rolloff factor is negligible at the sampled grading fields.
    e_sat = 8.0e5
    r_s = 2.2
    for e in (4.1e4, 4.5e4):
        reduction = 1.0 - 1.0 / (1.0 + (e / e_sat) ** r_s)
        assert 0.0014 < reduction < 0.0019
        print(f"field-rolloff reduction at {e:.2e} V/m = {100*reduction:.4f}%")

    # Same-optics homogeneous baseline relative to the quoted gradient-sensitive excess.
    homogeneous = np.array([0.00246, 0.01230, 0.02470])
    excess = np.array([0.01198, 0.05873, 0.11041])
    fractions = homogeneous / excess
    assert np.allclose(100.0 * fractions, [20.5342, 20.9433, 22.3712], atol=0.01)
    print("homogeneous-baseline fractions (%) =", ", ".join(f"{100*x:.2f}" for x in fractions))

    # Ten-percent-of-target one-sigma allocation used in nuisance table.
    tolerance = 0.1 * excess
    assert np.allclose(tolerance, [0.001198, 0.005873, 0.011041], atol=1e-12)
    print("10%-target baseline allocations (deg) =", ", ".join(f"{x:.6f}" for x in tolerance))

    print("PASS: Rev5 mode-resolution, branch-free root product, field-rolloff, and baseline-budget numbers verified.")


if __name__ == "__main__":
    main()
