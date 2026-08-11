"""Five-color / two-frequency exact closure for a finite-boundary scalar DD slab.

At fixed Laplace/RF frequency s, uniform scalar drift-diffusion obeys

    D u'' + w u' - s u = 0

with spatial roots r1,r2 satisfying

    r1+r2 = -w/D,
    r1*r2 = -s/D.

A finite reflecting boundary excites both roots. Equally spaced source responses
therefore form a rank-two sequence

    y_m = c1 q1^m + c2 q2^m, qk=exp(rk Delta z).

Five colors are enough to verify rank<=2 and identify the two q roots (four are
algebraically enough to solve the recurrence; the fifth is the closure point).
Across RF frequency, the recovered continuous-log spatial roots must give the
same real D,w.

The script verifies the theorem for arbitrary frequency-dependent mode
amplitudes (standing in for boundary/source-kernel factors) and contrasts an
arbitrary hidden two-mode propagation model that is rank two but fails the
scalar quadratic root-pair closure.
"""

from __future__ import annotations

import numpy as np


D_TRUE = 0.23
W_TRUE = 1.40
DZ = 0.37
FREQUENCIES = (0.35, 1.10, 2.40)


def dd_roots(omega: float):
    s = 1j * omega
    disc = np.sqrt(W_TRUE**2 + 4.0 * D_TRUE * s)
    return (
        (-W_TRUE + disc) / (2.0 * D_TRUE),
        (-W_TRUE - disc) / (2.0 * D_TRUE),
    )


def sequence_from_roots(r1: complex, r2: complex, omega: float):
    # Arbitrary nonzero amplitudes. Exact root closure does not depend on them.
    c1 = 1.0 + 0.08j * omega
    c2 = (0.13 + 0.04j) * (1.0 + 0.05 * omega)
    q1 = np.exp(r1 * DZ)
    q2 = np.exp(r2 * DZ)
    m = np.arange(5)
    return c1 * q1**m + c2 * q2**m


def recover_q_roots(y: np.ndarray):
    # Sequence recurrence: y_{m+2}=S y_{m+1}-P y_m,
    # with S=q1+q2 and P=q1*q2.
    A = np.asarray(
        ((y[1], -y[0]), (y[2], -y[1])), dtype=complex
    )
    b = np.asarray((y[2], y[3]), dtype=complex)
    S, P = np.linalg.solve(A, b)
    q = np.roots((1.0, -S, P))
    predicted_y4 = S * y[3] - P * y[2]
    return q, predicted_y4


def unwrap_log_to_reference(q: complex, reference: complex) -> complex:
    principal = np.log(q) / DZ
    candidates = [principal + 2j * np.pi * k / DZ for k in range(-4, 5)]
    return min(candidates, key=lambda value: abs(value - reference))


def infer_D_w(r1: complex, r2: complex, omega: float):
    product = r1 * r2
    D = -1j * omega / product
    w = -D * (r1 + r2)
    return D, w


def hankel3(y: np.ndarray):
    return np.asarray(
        ((y[0], y[1], y[2]), (y[1], y[2], y[3]), (y[2], y[3], y[4])),
        dtype=complex,
    )


def main() -> None:
    print("Five-color finite-boundary root-pair closure")
    recovered = []

    for omega in FREQUENCIES:
        true_roots = dd_roots(omega)
        y = sequence_from_roots(*true_roots, omega)
        q, y4_pred = recover_q_roots(y)

        # Match recovered spatial roots to the exact roots only to resolve log
        # branches in this numerical regression. Experimentally continuity in
        # omega/depth provides the branch tracking.
        r_candidates = [
            unwrap_log_to_reference(qi, true_roots[0]) for qi in q
        ]
        # Choose assignment minimizing total distance to the two exact branches.
        options = (
            (r_candidates[0], unwrap_log_to_reference(q[1], true_roots[1])),
            (unwrap_log_to_reference(q[1], true_roots[0]), unwrap_log_to_reference(q[0], true_roots[1])),
        )
        r1, r2 = min(
            options,
            key=lambda pair: abs(pair[0]-true_roots[0]) + abs(pair[1]-true_roots[1]),
        )

        D_rec, w_rec = infer_D_w(r1, r2, omega)
        recovered.append((D_rec, w_rec))

        det3 = np.linalg.det(hankel3(y))
        det_scale = np.linalg.norm(hankel3(y)) ** 3
        print(f"omega={omega:.3f}")
        print(f"  five-color recurrence |y4-y4pred|={abs(y[4]-y4_pred):.3e}")
        print(f"  relative 3x3 Hankel det={abs(det3)/det_scale:.3e}")
        print(f"  r1+r2={r1+r2}")
        print(f"  r1*r2={r1*r2}")
        print(f"  inferred D={D_rec}, w={w_rec}")

        assert abs(y[4] - y4_pred) < 2.0e-12
        assert abs(det3) / det_scale < 2.0e-13
        assert abs(D_rec.real / D_TRUE - 1.0) < 2.0e-11
        assert abs(D_rec.imag) < 2.0e-11
        assert abs(w_rec.real / W_TRUE - 1.0) < 2.0e-11
        assert abs(w_rec.imag) < 2.0e-11

    recovered = np.asarray(recovered)
    assert np.ptp(recovered[:, 0].real) < 2.0e-11
    assert np.ptp(recovered[:, 1].real) < 2.0e-11

    # Rank-two hidden-state counterexample: two homogeneous modes with roots that
    # do not satisfy one scalar DD quadratic over frequency. It still passes the
    # five-color rank-two determinant.
    print()
    print("arbitrary hidden rank-two counterexample")
    hidden_D = []
    hidden_w = []
    for omega in FREQUENCIES:
        r1 = -0.20 + 0.55j * omega
        r2 = -1.10 + 0.18j * omega + 0.04j * omega**2
        y = sequence_from_roots(r1, r2, omega)
        det3 = np.linalg.det(hankel3(y))
        scale = np.linalg.norm(hankel3(y)) ** 3
        D_app, w_app = infer_D_w(r1, r2, omega)
        hidden_D.append(D_app)
        hidden_w.append(w_app)
        print(
            f"  omega={omega:.3f}: rank2 rel det={abs(det3)/scale:.3e}, "
            f"D_app={D_app}, w_app={w_app}"
        )
        assert abs(det3) / scale < 2.0e-13

    hidden_D = np.asarray(hidden_D)
    hidden_w = np.asarray(hidden_w)
    assert np.max(np.abs(hidden_D.imag)) > 1.0e-2
    assert np.ptp(hidden_D.real) > 1.0e-2 or np.ptp(hidden_w.real) > 1.0e-2

    print()
    print(
        "PASS: five colors can establish rank-two spatial propagation, while the "
        "two recovered spatial roots provide a stronger scalar-boundary closure. "
        "For uniform finite-boundary drift-diffusion their sum is one real "
        "frequency-independent -w/D and their product is -i omega/D. An arbitrary "
        "hidden rank-two model can pass Hankel rank closure yet fail this root-pair "
        "law."
    )


if __name__ == "__main__":
    main()
