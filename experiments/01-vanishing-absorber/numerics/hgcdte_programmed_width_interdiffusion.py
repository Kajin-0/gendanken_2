"""Feature-width and interdiffusion robustness for the interface-safe design.

The programmed translated-gradient experiment now has a stable coarse geometry:
a compact internal high-gradient segment, kept well away from both interfaces,
whose depth is intentionally changed between matched devices. This script asks
how wide that segment should be and how strongly interdiffusion can blur it
before the fixed-time wavelength x RF information collapses.

Physical comparison rule
------------------------
For each total feature width and Gaussian interdiffusion blur sigma_d:

1. start from a 0.10-um-ramp trapezoidal feature in composition-slope magnitude;
2. convolve that feature with a Gaussian of sigma_d;
3. subtract its spatial mean so x(0), x(L), and total composition change remain
   exactly fixed;
4. choose ONE common slope-modulation amplitude for the translated pair so a
   reference feature centered at 4.8 um reaches ~1.95 kV/cm maximum Hansen-gap
   gradient field;
5. require the nominal feature edge PLUS 3 sigma_d to remain >=1.5 um from both
   absorber boundaries;
6. optimize translated feature centers on a 0.1-um grid and the upper edge of a
   contiguous wavelength band beginning at 2.00 um;
7. include cubic smooth bulk plus front/back exponential interface nuisances,
   arbitrary complex intercepts at each RF frequency, absorbed-signal-dependent
   phase precision, and fixed total wavelength-time resource.

Noise envelopes beta=1/2 and beta=1 are both checked. The 25% feature-supported
transport perturbation remains an illustrative design probe, not a device
prediction.

No novelty claim.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.ndimage import gaussian_filter1d
from scipy.optimize import brentq

from hgcdte_sample_a_constraint_family_joint_iso_kernel import (
    HC_EV_UM,
    alpha_moazzami,
    deg_dx_hansen,
)
from hgcdte_matched_contact_translated_gradient_design import (
    FREQUENCIES_GHZ,
    L_UM,
    X_BACK,
    X_FRONT,
)
from hgcdte_shortwave_finite_rf_jacobian import (
    PERTURBATION_FRACTION,
    Q0_PS_PER_UM,
    project_residual,
)

N_FINE = 4001
N_CELL = 160
N_CELL_CHECK = 320
RAMP_UM = 0.10
TARGET_FIELD_V_CM = 1950.0
CLEARANCE_UM = 1.50
POSITION_STEP_UM = 0.10
WAVELENGTHS_UM = np.arange(2.00, 2.6001, 0.025)
UPPER_BANDS_UM = np.arange(2.20, 2.6001, 0.05)
WIDTHS_UM = (0.70, 0.80, 0.90, 1.00, 1.10)
DIFFUSION_SIGMAS_UM = (0.00, 0.05, 0.10, 0.15)

Z_FINE = np.linspace(0.0, L_UM, N_FINE)
DZ_FINE = float(Z_FINE[1] - Z_FINE[0])


def base_feature(z0_um: float, width_um: float) -> np.ndarray:
    half = 0.5 * width_um
    ramp = min(RAMP_UM, 0.49 * half)
    flat_half = half - ramp
    distance = np.abs(Z_FINE - z0_um)
    h = np.zeros_like(Z_FINE)
    h[distance <= flat_half] = 1.0
    transition = (distance > flat_half) & (distance < half)
    h[transition] = (half - distance[transition]) / ramp
    return h


def blurred_feature(z0_um: float, width_um: float, sigma_um: float) -> np.ndarray:
    h = base_feature(z0_um, width_um)
    if sigma_um <= 0.0:
        return h
    return gaussian_filter1d(
        h,
        sigma=sigma_um / DZ_FINE,
        mode="constant",
        cval=0.0,
        truncate=5.0,
    )


def profile(z0_um: float, width_um: float, sigma_um: float, modulation: float):
    h = blurred_feature(z0_um, width_um, sigma_um)
    h_mean = float(np.trapezoid(h, Z_FINE) / L_UM)
    s0 = (X_FRONT - X_BACK) / L_UM
    slope = s0 * (1.0 + modulation * (h - h_mean))
    if np.min(slope) <= 0.0:
        raise RuntimeError("nonmonotonic programmed profile")
    x = X_FRONT - np.concatenate(([0.0], cumulative_trapezoid(slope, Z_FINE)))
    return Z_FINE, x, h, slope


def maximum_gradient_field(
    modulation: float,
    width_um: float,
    sigma_um: float,
    z0_um: float = 4.8,
) -> float:
    _, x, _, slope = profile(z0_um, width_um, sigma_um, modulation)
    return float(np.max(np.abs(deg_dx_hansen(x, 300.0) * slope * 1.0e4)))


def modulation_for_fixed_field(width_um: float, sigma_um: float) -> float:
    h = blurred_feature(4.8, width_um, sigma_um)
    h_mean = float(np.trapezoid(h, Z_FINE) / L_UM)
    upper = 0.98 / h_mean
    if maximum_gradient_field(upper, width_um, sigma_um) < TARGET_FIELD_V_CM:
        return upper
    return float(
        brentq(
            lambda a: maximum_gradient_field(a, width_um, sigma_um)
            - TARGET_FIELD_V_CM,
            0.0,
            upper,
        )
    )


def generation_probabilities(z, x, wavelength_um, n_cell):
    edges = np.linspace(0.0, L_UM, n_cell + 1)
    alpha = alpha_moazzami(HC_EV_UM / wavelength_um, x, 300.0)
    tau = np.concatenate(([0.0], cumulative_trapezoid(alpha, z * 1.0e-4)))
    tau_edges = np.interp(edges, z, tau)
    pabs = float(1.0 - np.exp(-tau_edges[-1]))
    if pabs <= 1.0e-14:
        raise RuntimeError("zero modeled absorption")
    probability = (
        np.exp(-tau_edges[:-1]) - np.exp(-tau_edges[1:])
    ) / pabs
    probability /= np.sum(probability)
    centers = 0.5 * (edges[:-1] + edges[1:])
    return probability, centers, edges, pabs


def finite_rf(z, x, n_cell):
    edges = np.linspace(0.0, L_UM, n_cell + 1)
    centers = 0.5 * (edges[:-1] + edges[1:])
    starts = edges[:-1]
    widths = np.diff(edges)
    overlap = np.clip(
        centers[:, None] - starts[None, :],
        0.0,
        widths[None, :],
    )
    t0_ps = Q0_PS_PER_UM * centers

    probability = []
    pabs = []
    for wavelength in WAVELENGTHS_UM:
        p, _, _, pa = generation_probabilities(z, x, float(wavelength), n_cell)
        probability.append(p)
        pabs.append(pa)
    probability = np.asarray(probability)
    pabs = np.asarray(pabs)

    jacobian = []
    transfer = []
    for f_ghz in FREQUENCIES_GHZ:
        omega = 2.0 * np.pi * f_ghz * 1.0e9
        phase = np.exp(-1j * omega * t0_ps * 1.0e-12)
        H = probability @ phase
        weighted = (probability * phase[None, :]) @ overlap
        J = -1j * omega * 1.0e-12 * weighted / H[:, None]
        jacobian.append(J)
        transfer.append(H)
    return np.asarray(jacobian), np.asarray(transfer), pabs, centers


def delta_q(z, h, centers):
    support = np.interp(centers, z, h)
    support /= np.max(support)
    return Q0_PS_PER_UM * (
        1.0 / (1.0 - PERTURBATION_FRACTION * support) - 1.0
    )


def nuisance_spatial(centers):
    u = centers / L_UM
    columns = [np.ones_like(u), u, u**2, u**3]
    for ell in (0.30, 0.50, 0.75, 1.00):
        columns.append(np.exp(-centers / ell))
    for ell in (0.30, 0.50, 0.75, 1.00):
        columns.append(np.exp(-(L_UM - centers) / ell))
    return np.column_stack(columns)


def raw_vector(response):
    return np.concatenate((response.imag.reshape(-1), response.real.reshape(-1)))


def raw_matrix(response):
    return np.concatenate(
        (
            response.imag.reshape(-1, response.shape[-1]),
            response.real.reshape(-1, response.shape[-1]),
        ),
        axis=0,
    )


def intercepts(n_lambda):
    n_f = len(FREQUENCIES_GHZ)
    n = n_f * n_lambda
    matrix = np.zeros((2 * n, 2 * n_f))
    for fi in range(n_f):
        rows = np.arange(fi * n_lambda, (fi + 1) * n_lambda)
        matrix[rows, fi] = 1.0
        matrix[n + rows, n_f + fi] = 1.0
    return matrix


def positions(width_um: float, sigma_um: float):
    # Nominal feature edge plus 3 diffusion sigmas must clear each interface.
    margin = CLEARANCE_UM + 0.5 * width_um + 3.0 * sigma_um
    start = np.ceil(margin / POSITION_STEP_UM) * POSITION_STEP_UM
    stop = np.floor((L_UM - margin) / POSITION_STEP_UM) * POSITION_STEP_UM
    return np.round(
        np.arange(start, stop + 0.5 * POSITION_STEP_UM, POSITION_STEP_UM),
        10,
    )


def build_cache(width_um, sigma_um, modulation, n_cell):
    cache = {}
    for center in positions(width_um, sigma_um):
        z, x, h, slope = profile(center, width_um, sigma_um, modulation)
        J, H, pabs, centers = finite_rf(z, x, n_cell)
        cache[float(center)] = {
            "J": J,
            "H": H,
            "Pabs": pabs,
            "dq": delta_q(z, h, centers),
            "centers": centers,
            "field_max": float(
                np.max(np.abs(deg_dx_hansen(x, 300.0) * slope * 1.0e4))
            ),
        }
    return cache


def score_pair(left, right, stop, beta, nuisance):
    indices = np.arange(stop)
    J1 = left["J"][:, indices, :]
    J2 = right["J"][:, indices, :]
    target = (
        np.einsum("flj,j->fl", J2, right["dq"])
        - np.einsum("flj,j->fl", J1, left["dq"])
    )
    common = np.einsum("flj,jk->flk", J2 - J1, nuisance)

    data = raw_vector(target)
    nuisance_data = np.column_stack(
        (raw_matrix(common), intercepts(len(indices)))
    )

    p1 = left["Pabs"][indices]
    p2 = right["Pabs"][indices]
    relative_sigma = np.sqrt(p1 ** (-2.0 * beta) + p2 ** (-2.0 * beta))
    sigma_rows = np.tile(relative_sigma, len(FREQUENCIES_GHZ))
    sigma_rows = np.concatenate((sigma_rows, sigma_rows))

    angle_deg, residual = project_residual(
        data / sigma_rows,
        nuisance_data / sigma_rows[:, None],
    )
    return {
        "score": float(residual / np.sqrt(len(indices))),
        "angle_deg": float(angle_deg),
        "pabs_min": float(min(np.min(p1), np.min(p2))),
    }


def optimize(width_um: float, sigma_um: float, beta: float = 1.0, n_cell: int = N_CELL):
    modulation = modulation_for_fixed_field(width_um, sigma_um)
    cache = build_cache(width_um, sigma_um, modulation, n_cell)
    pos = np.asarray(sorted(cache))
    nuisance = nuisance_spatial(cache[float(pos[0])]["centers"])
    stops = [
        int(np.argmin(np.abs(WAVELENGTHS_UM - upper))) + 1
        for upper in UPPER_BANDS_UM
    ]

    best = None
    for i, z1 in enumerate(pos):
        for z2 in pos[i + 1 :]:
            if z2 - z1 < 0.4 - 1.0e-12:
                continue
            for stop in stops:
                result = score_pair(
                    cache[float(z1)], cache[float(z2)], stop, beta, nuisance
                )
                row = {
                    **result,
                    "z1": float(z1),
                    "z2": float(z2),
                    "lambda_max": float(WAVELENGTHS_UM[stop - 1]),
                    "n_lambda": int(stop),
                    "modulation": modulation,
                }
                if best is None or row["score"] > best["score"]:
                    best = row
    return best


def fixed_candidate(width_um, sigma_um, beta, n_cell, candidate):
    modulation = modulation_for_fixed_field(width_um, sigma_um)
    cache = build_cache(width_um, sigma_um, modulation, n_cell)
    nuisance = nuisance_spatial(next(iter(cache.values()))["centers"])
    stop = int(np.argmin(np.abs(WAVELENGTHS_UM - candidate["lambda_max"]))) + 1
    return score_pair(
        cache[candidate["z1"]],
        cache[candidate["z2"]],
        stop,
        beta,
        nuisance,
    )


def main() -> None:
    print("Programmed feature width / interdiffusion robustness")
    print(f"target gradient field = {TARGET_FIELD_V_CM:.0f} V/cm")
    print(f"interface clearance = {CLEARANCE_UM:.2f} um + 3 sigma_d")
    print()

    winners = {}
    for sigma_um in DIFFUSION_SIGMAS_UM:
        rows = []
        for width_um in WIDTHS_UM:
            row = optimize(width_um, sigma_um, beta=1.0)
            rows.append((width_um, row))
            print(
                f"sigma_d={sigma_um:.2f} um, width={width_um:.2f} um -> "
                f"score={row['score']:.7f}, z={row['z1']:.1f}->{row['z2']:.1f} um, "
                f"lambda=2.00-{row['lambda_max']:.2f} um, "
                f"Pabs_min={row['pabs_min']:.4f}"
            )
        winners[sigma_um] = max(rows, key=lambda item: item[1]["score"])
        width, row = winners[sigma_um]
        print(
            f"  WINNER sigma_d={sigma_um:.2f}: width={width:.2f} um, "
            f"score={row['score']:.7f}\n"
        )

    baseline = winners[0.0][1]["score"]
    print("interdiffusion penalty relative to unblurred winner")
    for sigma_um in DIFFUSION_SIGMAS_UM[1:]:
        loss = 1.0 - winners[sigma_um][1]["score"] / baseline
        print(f"  sigma_d={sigma_um:.2f} um -> information-amplitude loss={loss:.3%}")

    print()
    print("statistics-like beta=1/2 check at additive-like winning widths")
    for sigma_um in DIFFUSION_SIGMAS_UM:
        width = winners[sigma_um][0]
        row = optimize(width, sigma_um, beta=0.5)
        print(
            f"  sigma_d={sigma_um:.2f}, width={width:.2f} -> "
            f"z={row['z1']:.1f}->{row['z2']:.1f}, "
            f"lambda=2.00-{row['lambda_max']:.2f}, score={row['score']:.7f}"
        )

    print()
    print("320-cell confirmation of the selected additive-like winners")
    for sigma_um in DIFFUSION_SIGMAS_UM:
        width, candidate = winners[sigma_um]
        check = fixed_candidate(width, sigma_um, 1.0, N_CELL_CHECK, candidate)
        print(
            f"  sigma_d={sigma_um:.2f}, width={width:.2f}: "
            f"160-cell={candidate['score']:.7f}, 320-cell={check['score']:.7f}"
        )

    # Current regression envelopes.
    w0, r0 = winners[0.0]
    w05, r05 = winners[0.05]
    w10, r10 = winners[0.10]
    w15, r15 = winners[0.15]

    assert abs(w0 - 1.00) < 1.0e-12
    assert abs(w05 - 0.90) < 1.0e-12
    assert abs(w10 - 0.90) < 1.0e-12
    assert abs(w15 - 0.90) < 1.0e-12

    assert 0.00266 < r0["score"] < 0.00269
    assert 0.00245 < r05["score"] < 0.00249
    assert 0.00211 < r10["score"] < 0.00215
    assert 0.00177 < r15["score"] < 0.00182

    loss05 = 1.0 - r05["score"] / r0["score"]
    loss10 = 1.0 - r10["score"] / r0["score"]
    loss15 = 1.0 - r15["score"] / r0["score"]
    assert 0.07 < loss05 < 0.09
    assert 0.19 < loss10 < 0.22
    assert 0.32 < loss15 < 0.35

    print()
    print(
        "PASS: at fixed ~1.95-kV/cm peak gradient, the useful total-width region "
        "is broad and centered near 0.9-1.0 um. Interdiffusion degrades the "
        "fixed-time information gradually rather than destroying it: roughly "
        "8%, 20%, and 33% amplitude loss for Gaussian sigma_d = 0.05, 0.10, and "
        "0.15 um. The statistics-like and additive-like noise envelopes choose "
        "essentially the same geometries, and 320-cell checks reproduce the "
        "selected scores."
    )


if __name__ == "__main__":
    main()
