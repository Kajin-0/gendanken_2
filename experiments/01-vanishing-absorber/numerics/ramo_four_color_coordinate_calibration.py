"""Internal-coordinate calibration robustness of the four-color raw-current null.

Let four spectral channels be equally spaced in a calibrated coordinate mu, but
let the true physical source coordinate be z=f(mu). For one homogeneous raw
Ramo mode J(mu)=A+B exp[-gamma f(mu)].

Any affine f(mu)=a+b mu preserves exact equal physical spacing and therefore the
four-color closure exactly. For smooth nonlinear f and small spacing h,

    C4 = h^2 [gamma f'' - (ln f')''] + O(h^4)

at the quartet midpoint. For f=mu+delta with small delta,

    C4 = h^2 [gamma delta'' - delta'''] + ... .
"""

from __future__ import annotations

import numpy as np

GAMMA = 0.31 + 0.19j
A = 0.7 - 0.2j
B = 1.3 + 0.4j


def closure_from_positions(z: np.ndarray) -> complex:
    J = A + B * np.exp(-GAMMA * z)
    d = np.diff(J)
    return complex(2.0 * np.log(d[1]) - np.log(d[0]) - np.log(d[2]))


def sample_f(f, h: float, center: float = 0.0) -> np.ndarray:
    mu = center + h * np.asarray((-1.5, -0.5, 0.5, 1.5))
    return np.asarray([f(x) for x in mu])


def main() -> None:
    print("Four-color internal-coordinate calibration robustness")

    for a, b, h in ((1.7, 0.42, 0.6), (-2.0, 3.1, 0.17), (0.0, 0.73, 1.2)):
        z = sample_f(lambda mu: a + b * mu, h)
        C = closure_from_positions(z)
        print(f"affine a={a:+.2f}, b={b:.2f}, h={h:.2f}: |C4|={abs(C):.3e}")
        assert abs(C) < 5.0e-14

    a, b, c, d = 0.7, 1.2, 0.05, 0.01
    f = lambda mu: a + b * mu + c * mu**2 + d * mu**3
    fp = b
    fpp = 2.0 * c
    fppp = 6.0 * d
    lnfp_second = fppp / fp - (fpp / fp) ** 2
    coefficient = GAMMA * fpp - lnfp_second

    errors = []
    for h in (0.10, 0.05, 0.025, 0.0125):
        C = closure_from_positions(sample_f(f, h))
        observed = C / h**2
        error = abs(observed - coefficient)
        errors.append(error)
        print(
            f"h={h:.4f}: C4/h^2={observed.real:+.9e}{observed.imag:+.9e}j, "
            f"error={error:.3e}"
        )

    assert errors[-1] < errors[0] / 50.0

    print()
    print(
        "PASS: the four-color model-order null is exactly invariant to unknown "
        "affine depth calibration. Smooth nonlinear coordinate distortion "
        "enters only through local curvature, with the predicted h^2 law."
    )


if __name__ == "__main__":
    main()
