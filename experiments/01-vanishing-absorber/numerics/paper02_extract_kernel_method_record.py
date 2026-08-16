"""Create an exact human-readable record of the conditional HgCdTe kernel model.

The purpose is manuscript reproducibility: capture the actual module constants,
locally defined functions, target mean depths, selected wavelengths, and kernel
moments used by Paper 02 without relying on a prose reconstruction.
"""

from __future__ import annotations

import inspect
import json
from pathlib import Path

import numpy as np

import hgcdte_ramo_four_color_gradient_prediction as h


def serializable_constant(name, value):
    if isinstance(value, (str, int, float, bool, type(None))):
        return value
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, np.ndarray):
        if value.size <= 100:
            return value.tolist()
        return {
            "shape": list(value.shape),
            "dtype": str(value.dtype),
            "min": float(np.min(value)),
            "max": float(np.max(value)),
        }
    return None


def main():
    constants = {}
    for name, value in sorted(vars(h).items()):
        if name.isupper():
            v = serializable_constant(name, value)
            if v is not None:
                constants[name] = v

    functions = []
    for name, obj in sorted(vars(h).items()):
        if inspect.isfunction(obj) and obj.__module__ == h.__name__:
            try:
                src = inspect.getsource(obj)
            except OSError:
                continue
            functions.append((name, src))

    target_depths = np.arange(2.0, 4.51, 0.5)
    rows = []
    for zbar in target_depths:
        wl = float(h.wavelength_for_mean(float(zbar)))
        row = h.optical_kernel(wl)
        # Current optical_kernel contract: row[0]=absorbed probability,
        # row[1]=mean depth, row[2]=variance, row[3]=normalized depth density.
        density = np.asarray(row[3], dtype=float)
        z = np.asarray(h.Z_UM, dtype=float)
        norm = float(np.trapezoid(density, z))
        mean = float(np.trapezoid(z * density, z) / norm)
        var = float(np.trapezoid((z - mean) ** 2 * density, z) / norm)
        rows.append(
            {
                "target_mean_um": float(zbar),
                "wavelength_um": wl,
                "absorbed_probability": float(row[0]),
                "reported_mean_um": float(row[1]),
                "reported_variance_um2": float(row[2]),
                "reintegrated_norm": norm,
                "reintegrated_mean_um": mean,
                "reintegrated_sigma_um": float(np.sqrt(var)),
            }
        )

    out = Path(__file__).resolve().parents[1] / "PAPER02_HGCDTE_KERNEL_METHOD_RECORD_2026-08-15.md"
    lines = [
        "# Paper 02 — Exact Conditional HgCdTe Kernel Method Record",
        "",
        "**Date:** 2026-08-15  ",
        "**Status:** **MACHINE-EXTRACTED FROM EXECUTABLE SOURCE / CONDITIONAL THEORETICAL MODEL**",
        "",
        "This record is generated directly from `numerics/hgcdte_ramo_four_color_gradient_prediction.py`. It is intended to prevent manuscript prose from drifting away from the executable optical model.",
        "",
        "## Scope",
        "",
        "These kernels are theoretical forward-model inputs used for the Paper-02 identifiability stress. They are not experimentally measured or calibrated kernels from a specific detector. Treating them as `known` in the inverse means the same generated kernel shapes are supplied to the inverse without optical-model uncertainty.",
        "",
        "## Module constants",
        "",
        "```json",
        json.dumps(constants, indent=2, sort_keys=True),
        "```",
        "",
        "## Six manuscript channels",
        "",
        "| target mean [um] | wavelength [um] | absorbed probability | reintegrated mean [um] | sigma [um] |",
        "|---:|---:|---:|---:|---:|",
    ]
    for r in rows:
        lines.append(
            f"| {r['target_mean_um']:.3f} | {r['wavelength_um']:.9f} | "
            f"{r['absorbed_probability']:.9g} | {r['reintegrated_mean_um']:.9f} | "
            f"{r['reintegrated_sigma_um']:.6f} |"
        )

    lines += [
        "",
        "## Locally defined executable functions",
        "",
        "The following functions are copied verbatim from the executable module by `inspect.getsource`. This is a reproducibility record, not proposed manuscript formatting.",
        "",
    ]
    for name, src in functions:
        lines += [f"### `{name}`", "", "```python", src.rstrip(), "```", ""]

    out.write_text("\n".join(lines), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
