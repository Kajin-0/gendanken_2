"""Purpose-built downstream-collection buried-feature design.

Motivation
----------
The published-device analysis inherited front collection at the high-Cd side.
For a purpose-built validation structure we can instead choose an orientation
that makes the optical spectral encoder and the graded-band transport direction
self-consistent.

Thought device:
- p-type quasi-neutral graded HgCdTe absorber;
- z=0: illuminated high-gap/high-Cd entrance, x=0.40;
- z=L: low-gap/low-Cd collecting junction, x=0.32;
- L=7.6 um, linear control profile.

Under the repository's p-type quasi-neutral pinning result, nearly constant
N_A/N_v gives dE_v/dz~0 and therefore dE_c/dz~dE_g/dz. Since E_g decreases
with z, minority-electron conduction-band energy decreases toward z=L, so the
gradient assists electron collection toward the low-gap side. This script does
not model the junction itself; it only uses that deliberately chosen transport
orientation.

The timing inverse for collection at L uses the downstream path rather than the
front-collection survival path. A finite-RF complex Jacobian is constructed for
baseline deterministic transit T0(z)=(L-z)/v0.

Candidate buried transport support:
    exp[-(z-z0)^2/(2 sigma_z^2)]
with z0=0.25-7.0 um and sigma_z=0.2-1.0 um.

Nuisance span:
- smooth bulk 1,z/L,(z/L)^2;
- collection-contact exponentials exp[-(L-z)/ell_c] with ell_c=0.2,0.5,0.75,1um.

Measurement:
- lambda=2.80-3.83 um, Pabs>=0.05;
- f=0.25,0.5,1,2,3 GHz;
- phase+log-magnitude;
- wavelength-independent complex response removed separately at each f;
- equal/statistics-like/additive-like absorbed-signal weighting.

No fabrication, microscopic transport, or novelty claim.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import cumulative_trapezoid

from hgcdte_sample_a_constraint_family_joint_iso_kernel import (
    HC_EV_UM,
    N_CELL,
    alpha_moazzami,
    deg_dx_hansen,
    eg_hansen,
)

L_UM = 7.6
X_ENTRANCE = 0.40
X_COLLECTOR = 0.32
N_FINE = 4001
N_CELL_LOCAL = N_CELL
BASELINE_V_M_S = 1.0e5
Q0_PS_PER_UM = 1.0e6 / BASELINE_V_M_S

FREQUENCIES_GHZ = (0.25, 0.50, 1.0, 2.0, 3.0)
LAMBDA_CANDIDATE = np.arange(2.80, 3.9001, 0.01)
PABS_MIN = 0.05
FEATURE_CENTERS_UM = np.arange(0.25, 7.0001, 0.25)
FEATURE_WIDTHS_UM = (0.20, 0.35, 0.50, 0.75, 1.00)
CONTACT_SCALES_UM = (0.20, 0.50, 0.75, 1.00)
NOISE_EXPONENTS = {
    "equal": 0.0,
    "statistics": 0.5,
    "additive": 1.0,
}


def control_profile():
    z = np.linspace(0.0, L_UM, N_FINE)
    x = X_ENTRANCE + (X_COLLECTOR - X_ENTRANCE) * z / L_UM
    dx_dz = np.full_like(z, (X_COLLECTOR - X_ENTRANCE) / L_UM)
    field = np.abs(deg_dx_hansen(x, 300.0) * dx_dz * 1.0e4)
    return z, x, field


def cell_geometry():
    edges = np.linspace(0.0, L_UM, N_CELL_LOCAL + 1)
    centers = 0.5 * (edges[:-1] + edges[1:])
    return edges, centers


def generation_probabilities(z_um, x, wavelength_um):
    edges, centers = cell_geometry()
    z_cm = z_um * 1.0e-4
    alpha = alpha_moazzami(HC_EV_UM / wavelength_um, x, 300.0)
    tau = np.concatenate(([0.0], cumulative_trapezoid(alpha, z_cm)))
    tau_edges = np.interp(edges, z_um, tau)
    p_abs = float(1.0 - np.exp(-tau_edges[-1]))
    if p_abs <= 1.0e-14:
        raise RuntimeError("Zero modeled absorption")
    probability = (
        np.exp(-tau_edges[:-1]) - np.exp(-tau_edges[1:])
    ) / p_abs
    probability /= np.sum(probability)
    return p_abs, probability, centers, edges


def downstream_path_overlap(centers, edges):
    """Path through each cell for carrier generated at center and collected at L."""
    starts = edges[:-1]
    ends = edges[1:]
    return np.maximum(
        0.0,
        ends[None, :] - np.maximum(starts[None, :], centers[:, None]),
    )


def retained_optics(z_um, x):
    pabs = []
    probabilities = []
    for wavelength in LAMBDA_CANDIDATE:
        p, probability, _, _ = generation_probabilities(z_um, x, wavelength)
        pabs.append(p)
        probabilities.append(probability)
    pabs = np.asarray(pabs)
    probabilities = np.asarray(probabilities)
    keep = pabs >= PABS_MIN
    return LAMBDA_CANDIDATE[keep], pabs[keep], probabilities[keep]


def downstream_finite_rf_jacobian(z_um, x):
    wavelengths, pabs, probabilities = retained_optics(z_um, x)
    edges, centers = cell_geometry()
    overlap = downstream_path_overlap(centers, edges)
    baseline_time_ps = Q0_PS_PER_UM * (L_UM - centers)

    jacobian = []
    transfer = []
    for f_ghz in FREQUENCIES_GHZ:
        omega = 2.0 * np.pi * f_ghz * 1.0e9
        phase = np.exp(-1j * omega * baseline_time_ps * 1.0e-12)
        H = probabilities @ phase
        weighted_overlap = (probabilities * phase[None, :]) @ overlap
        J = -1j * omega * 1.0e-12 * weighted_overlap / H[:, None]
        jacobian.append(J)
        transfer.append(H)

    return wavelengths, pabs, np.asarray(jacobian), np.asarray(transfer)


def centered_response(response):
    return response - np.mean(response, axis=1, keepdims=True)


def response_vector(jacobian, spatial):
    response = centered_response(np.einsum("flj,j->fl", jacobian, spatial))
    return np.concatenate((response.imag.ravel(), response.real.ravel()))


def response_matrix(jacobian, spatial_matrix):
    response = np.einsum("flj,jk->flk", jacobian, spatial_matrix)
    response = response - np.mean(response, axis=1, keepdims=True)
    phase = response.imag.reshape(-1, spatial_matrix.shape[1])
    magnitude = response.real.reshape(-1, spatial_matrix.shape[1])
    return np.concatenate((phase, magnitude), axis=0)


def whitening_vector(pabs, exponent):
    one = np.tile(pabs**exponent, len(FREQUENCIES_GHZ))
    return np.concatenate((one, one))


def projected_metrics(target, nuisance):
    u, singular, _ = np.linalg.svd(nuisance, full_matrices=False)
    rank = int(np.sum(singular > singular[0] * 1.0e-11))
    basis = u[:, :rank]
    residual = target - basis @ (basis.T @ target)
    residual_norm = float(np.linalg.norm(residual))
    fraction = residual_norm / float(np.linalg.norm(target))
    angle = float(np.degrees(np.arcsin(np.clip(fraction, 0.0, 1.0))))
    return angle, residual_norm


def main() -> None:
    z, x, field = control_profile()
    wavelengths, pabs, jacobian, transfer = downstream_finite_rf_jacobian(z, x)
    _, centers = cell_geometry()

    smooth = np.column_stack(
        (np.ones(N_CELL_LOCAL), centers / L_UM, (centers / L_UM) ** 2)
    )
    contact = np.column_stack(
        [
            np.exp(-(L_UM - centers) / scale)
            for scale in CONTACT_SCALES_UM
        ]
    )
    nuisance_raw = response_matrix(jacobian, np.column_stack((smooth, contact)))

    baseline_field = float(np.median(field))
    print("Purpose-built downstream-collection buried-feature design")
    print(
        f"x entrance->collector = {X_ENTRANCE:.3f}->{X_COLLECTOR:.3f}, "
        f"L={L_UM:.1f} um, median |dEg/dz| field ~{baseline_field:.1f} V/cm"
    )
    print(
        f"retained lambda={wavelengths[0]:.2f}-{wavelengths[-1]:.2f} um, "
        f"Pabs(last)={pabs[-1]:.4f}, min optical |H|={np.min(np.abs(transfer)):.6f}"
    )
    print()

    stored = {}
    for label, exponent in NOISE_EXPONENTS.items():
        whitening = whitening_vector(pabs, exponent)
        nuisance = nuisance_raw * whitening[:, None]
        records = []

        for width in FEATURE_WIDTHS_UM:
            for center in FEATURE_CENTERS_UM:
                feature = np.exp(-0.5 * ((centers - center) / width) ** 2)
                target = response_vector(jacobian, feature) * whitening
                angle, residual = projected_metrics(target, nuisance)
                records.append((width, center, angle, residual))

        stored[label] = records
        best = max(records, key=lambda row: row[3])
        print(
            f"{label}: global best sigma={best[0]:.2f} um, center={best[1]:.2f} um, "
            f"angle={best[2]:.4f} deg, residual={best[3]:.9f}"
        )

        width05 = [row for row in records if row[0] == 0.50]
        best05 = max(width05, key=lambda row: row[3])
        near_contact = min(width05, key=lambda row: abs(row[1] - 6.75))
        ratio = best05[3] / near_contact[3]
        print(
            f"  width=0.50 um best center={best05[1]:.2f} um, "
            f"angle={best05[2]:.4f} deg; near-contact center={near_contact[1]:.2f} um; "
            f"amplitude gain={ratio:.2f}x, information gain={ratio**2:.1f}x"
        )
        print()

    stats = stored["statistics"]
    additive = stored["additive"]

    stats_best = max(stats, key=lambda row: row[3])
    add_best = max(additive, key=lambda row: row[3])
    assert stats_best[0] == 1.00 and stats_best[1] == 2.75
    assert add_best[0] == 1.00 and add_best[1] == 2.75
    assert 3.25 < stats_best[2] < 3.28
    assert 2.91 < add_best[2] < 2.95

    stats05 = [row for row in stats if row[0] == 0.50]
    add05 = [row for row in additive if row[0] == 0.50]
    s05 = max(stats05, key=lambda row: row[3])
    a05 = max(add05, key=lambda row: row[3])
    assert s05[1] == 3.50 and a05[1] == 3.50
    assert 2.16 < s05[2] < 2.19
    assert 1.87 < a05[2] < 1.90

    s_near = min(stats05, key=lambda row: abs(row[1] - 6.75))
    a_near = min(add05, key=lambda row: abs(row[1] - 6.75))
    s_ratio = s05[3] / s_near[3]
    a_ratio = a05[3] / a_near[3]
    assert 13.2 < s_ratio < 13.5
    assert 12.7 < a_ratio < 13.0

    local_x = X_ENTRANCE + (X_COLLECTOR - X_ENTRANCE) * 3.50 / L_UM
    local_lambda = HC_EV_UM / eg_hansen(local_x, 300.0)
    print(
        f"narrow-feature center 3.50 um -> local x~{local_x:.6f}, "
        f"local gap wavelength ~{local_lambda:.4f} um"
    )
    print()
    print(
        "PASS: in a deliberately p-type high-gap-entrance / low-gap-collector "
        "orientation, the wavelength encoder and minority-electron grade force "
        "can be aligned. Realistic signal weighting moves the best broad feature "
        "to ~2.75 um depth; a narrower 0.50-um feature is best near ~3.50 um and "
        "carries ~165-180x more information than the same feature near the low-gap "
        "collecting contact. This purpose-built downstream orientation is the "
        "preferred validation geometry to develop further."
    )


if __name__ == "__main__":
    main()
