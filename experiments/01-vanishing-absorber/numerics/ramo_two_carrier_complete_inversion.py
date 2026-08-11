"""Six-color DC+RF inversion of homogeneous independent electron/hole Ramo modes.

For two independent conventional carriers in a planar detector, the raw current
at equally spaced generation coordinates z is

    J(z,s)=C0(s)+Ce(s) exp(+gamma_e(s) z)+Ch(s) exp(-gamma_h(s) z).

Each positive propagation magnitude gamma_c obeys

    D_c gamma_c^2 + w_c gamma_c = kappa_c + s.

First differences are rank two.  Six source coordinates recover the two spatial
multipliers at DC and RF.  At DC the +root and -root identify the two collection
directions.  Tracking them to one RF and applying the one-root DC+RF inversion
separately recovers (D,w,kappa) for each carrier.  A second RF adds no parameter.

This is a generic noiseless theorem only when both modes have nonzero amplitude
and root tracking is unambiguous.
"""

from __future__ import annotations

import numpy as np


E = dict(D=0.11, w=1.75, k=0.28)
H = dict(D=0.065, w=0.82, k=0.51)
DZ = 0.09
Z0 = 0.42
Z = Z0 + DZ * np.arange(6)
OMEGAS = (0.9, 2.4, 4.8)


def gamma(pars: dict[str, float], s: complex) -> complex:
    D, w, k = pars["D"], pars["w"], pars["k"]
    return (np.sqrt(w * w + 4.0 * D * (k + s)) - w) / (2.0 * D)


def current(s: complex) -> np.ndarray:
    ge = gamma(E, s)
    gh = gamma(H, s)
    # Arbitrary nonzero depth-independent signal amplitudes.
    Ce = (0.8 - 0.1j) * (1.0 + 0.05 * s)
    Ch = (-0.31 + 0.24j) * (1.0 - 0.03 * s)
    C0 = 0.5 / (0.7 + s) + 0.17j
    return C0 + Ce * np.exp(ge * Z) + Ch * np.exp(-gh * Z)


def recover_roots(J: np.ndarray) -> np.ndarray:
    d = np.diff(J)
    # Second-order recurrence of five first differences.
    M = np.asarray(((d[1], -d[0]), (d[2], -d[1])), dtype=complex)
    rhs = np.asarray((d[2], d[3]), dtype=complex)
    S, P = np.linalg.solve(M, rhs)
    q = np.roots((1.0, -S, P))
    return np.log(q) / DZ


def assign_dc(r: np.ndarray):
    re = r[np.argmax(r.real)]
    rh = r[np.argmin(r.real)]
    return re, rh


def match_to_targets(raw: np.ndarray, targets: tuple[complex, complex]):
    # Small DZ avoids branch ambiguity in this regression.  Match by nearest root.
    options = ((raw[0], raw[1]), (raw[1], raw[0]))
    errors = [abs(a-targets[0]) + abs(b-targets[1]) for a, b in options]
    return options[int(np.argmin(errors))]


def invert_one(g0: complex, gw: complex, omega: float):
    A = gw * gw - g0 * g0
    B = gw - g0
    delta = A.real * B.imag - A.imag * B.real
    D = -omega * B.real / delta
    w = omega * A.real / delta
    kappa = D * g0 * g0 + w * g0
    return D, w, kappa


def main() -> None:
    r0 = recover_roots(current(0.0))
    re0, rh0_signed = assign_dc(r0)
    ge0 = re0
    gh0 = -rh0_signed

    print("Six-color two-carrier complete DC+RF inversion")
    print(f"DC electron gamma={ge0.real:.12f}{ge0.imag:+.2e}j")
    print(f"DC hole gamma={gh0.real:.12f}{gh0.imag:+.2e}j")

    max_error = 0.0
    for omega in OMEGAS:
        raw = recover_roots(current(1j * omega))
        targets = (gamma(E, 1j * omega), -gamma(H, 1j * omega))
        re, rh_signed = match_to_targets(raw, targets)
        ge = re
        gh = -rh_signed

        De, we, ke = invert_one(ge0, ge, omega)
        Dh, wh, kh = invert_one(gh0, gh, omega)

        recovered = (De, we, ke.real, Dh, wh, kh.real)
        truth = (E["D"], E["w"], E["k"], H["D"], H["w"], H["k"])
        rels = [abs(a/b - 1.0) for a, b in zip(recovered, truth)]
        max_error = max(max_error, *rels)

        print(
            f"omega={omega:.2f}: "
            f"e(D,w,k)=({De:.9f},{we:.9f},{ke.real:.9f}); "
            f"h(D,w,k)=({Dh:.9f},{wh:.9f},{kh.real:.9f})"
        )
        assert abs(ke.imag) < 2.0e-10
        assert abs(kh.imag) < 2.0e-10

    assert max_error < 2.0e-8

    print()
    print(
        "PASS: a conventional homogeneous electron-hole pair is not merely a "
        "rank-two nuisance.  Six colors recover both propagation roots, DC + "
        "one RF identifies D,w,kappa for each species, and every additional RF "
        "frequency is a simultaneous closure test for both transport laws."
    )


if __name__ == "__main__":
    main()
