#!/usr/bin/env python3
"""Extract and verify the immutable Rev. 3 manuscript baseline."""
from __future__ import annotations

import gzip
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXP = ROOT / "experiments" / "01-vanishing-absorber"
SNAPSHOT = EXP / "manuscript_history" / "Fisher_Spectral_Depth_Closure_Paper_REV3_2026-08-11.tex.gz"
OUTPUT = EXP / "MANUSCRIPT_CURRENT.tex"
EXPECTED_SOURCE_SHA256 = "76a3c5c0d26734773a5c60151e005f9b11225fa337520cb18eb358064fb48ad4"
EXPECTED_GZIP_SHA256 = "2732f2b64887c8694baddec54621795464ca4492f5b6f6d31de21ae738e6b29d"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    packed = SNAPSHOT.read_bytes()
    packed_hash = sha256(packed)
    if packed_hash != EXPECTED_GZIP_SHA256:
        raise SystemExit(
            f"Refusing extraction: gzip hash mismatch {packed_hash} != {EXPECTED_GZIP_SHA256}"
        )

    source = gzip.decompress(packed)
    source_hash = sha256(source)
    if source_hash != EXPECTED_SOURCE_SHA256:
        raise SystemExit(
            f"Refusing extraction: source hash mismatch {source_hash} != {EXPECTED_SOURCE_SHA256}"
        )

    OUTPUT.write_bytes(source)
    lines = len(source.decode("utf-8").splitlines())
    if lines != 696:
        raise SystemExit(f"Refusing extraction: expected 696 lines, recovered {lines}")

    print(f"Wrote verified manuscript baseline: {OUTPUT}")
    print(f"source SHA-256: {source_hash}")
    print(f"lines: {lines}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
