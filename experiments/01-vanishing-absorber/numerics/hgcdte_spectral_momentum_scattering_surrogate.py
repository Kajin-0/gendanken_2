"""Dimensionless momentum-scattering stress test for graded-HgCdTe spectral timing.

This is not a calibrated HgCdTe Monte Carlo model.

It tests whether the post-entrance-gap timing shape is robust when carriers
have finite velocity memory and stochastic momentum randomization.

Normalized geometry:
    Eg_out = 1
    Eg_in  = 2
    G      = 1
    L      = 1
    terminal drift velocity vd = 1

Photon coordinate:
    s = E_gamma - Eg_out

For s <= 1, high optical depth generates at the first allowed point and the
remaining distance is d=s with negligible local photon excess.
For s > 1, generation is pinned at the entrance and d=1 while local photon
excess is s-1.

Velocity follows an Ornstein-Uhlenbeck surrogate:
    dv = (vd-v)/tau_m dt + sqrt(2 sigma_v^2/tau_m) dW.

Three initial longitudinal velocity models are compared:
    cold      : v0 = 0
    directed  : v0 = +v_hot
    isotropic : v0 uniform[-v_hot, +v_hot]

The first is the strong-randomization reference.  The second preserves
forward ballistic memory.  The third is a simple isotropic-projection stress
test.  The script is designed to show that the post-knee shape is not
universal even though the generation-position rule changes at s=1.
"""

from __future__ import annotations

import math
import numpy as np


ENERGIES = np.array([0.25, 0.50, 0.75, 1.00, 1.50, 2.00])
TAU_M = 0.40
SIGMA_V = 0.10
HOT_SCALE = 1.50
DT = 1.0e-3
N_PARTICLES = 12000
SEED = 20260809


def simulate_mode(mode: str) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(SEED)
    means = []
    stds = []

    for s in ENERGIES:
        remaining_distance = min(float(s), 1.0)
        local_excess = max(float(s) - 1.0, 0.0)
        v_hot = HOT_SCALE * math.sqrt(local_excess)

        if mode == "cold":
            v = np.zeros(N_PARTICLES)
        elif mode == "directed":
            v = np.full(N_PARTICLES, v_hot)
        elif mode == "isotropic":
            if v_hot == 0.0:
                v = np.zeros(N_PARTICLES)
            else:
                v = rng.uniform(-v_hot, v_hot, N_PARTICLES)
        else:
            raise ValueError(mode)

        x = np.zeros(N_PARTICLES)
        t = np.zeros(N_PARTICLES)
        hit = np.full(N_PARTICLES, np.nan)
        alive = np.ones(N_PARTICLES, dtype=bool)

        noise_scale = math.sqrt(2.0 * SIGMA_V**2 / TAU_M)

        # The chosen parameters reach the boundary well before this limit.
        max_steps = 10000
        for _ in range(max_steps):
            idx = np.flatnonzero(alive)
            if idx.size == 0:
                break

            v_i = v[idx]
            v_i += ((1.0 - v_i) / TAU_M) * DT
            v_i += noise_scale * math.sqrt(DT) * rng.normal(size=idx.size)
            v[idx] = v_i

            x[idx] += v_i * DT
            t[idx] += DT

            crossed = idx[x[idx] >= remaining_distance]
            if crossed.size:
                hit[crossed] = t[crossed]
                alive[crossed] = False

        if np.isnan(hit).any():
            raise AssertionError("A trajectory failed to reach the collector")

        means.append(float(np.mean(hit)))
        stds.append(float(np.std(hit, ddof=1)))

    return np.array(means), np.array(stds)


def main() -> None:
    cold_mean, cold_std = simulate_mode("cold")
    directed_mean, directed_std = simulate_mode("directed")
    iso_mean, iso_std = simulate_mode("isotropic")

    knee = int(np.where(ENERGIES == 1.0)[0][0])

    # Below the entrance-gap knee the generation point moves upstream, so all
    # three models are identical and the mean delay rises.
    assert np.all(np.diff(cold_mean[: knee + 1]) > 0.0)
    assert np.allclose(cold_mean[: knee + 1], directed_mean[: knee + 1])
    assert np.allclose(cold_mean[: knee + 1], iso_mean[: knee + 1])

    # With no retained photon-dependent directed initial velocity, the
    # short-wave branch is approximately a plateau.
    plateau_spread = np.ptp(cold_mean[knee:])
    assert plateau_spread < 0.02 * cold_mean[knee]

    # Persistent forward velocity memory generates the ballistic-like decline.
    assert directed_mean[-1] < directed_mean[knee]

    # A symmetric hot longitudinal distribution is a counterexample to a
    # universal decline; here its mean is nearly flat/slightly larger and its
    # timing spread grows strongly.
    assert iso_mean[-1] >= 0.99 * iso_mean[knee]
    assert iso_std[-1] > 2.0 * iso_std[knee]

    print("energy coordinate s = E_gamma - Eg_out")
    print("energies:", ENERGIES)
    print("cold means:", np.round(cold_mean, 6))
    print("directed means:", np.round(directed_mean, 6))
    print("isotropic means:", np.round(iso_mean, 6))
    print("isotropic std:", np.round(iso_std, 6))
    print("PASS: entrance-gap geometry survives, post-knee shape is not universal")


if __name__ == "__main__":
    main()
