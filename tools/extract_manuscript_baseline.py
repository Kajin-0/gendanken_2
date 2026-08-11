#!/usr/bin/env python3
"""Extract and verify the immutable Rev. 3 manuscript baseline."""
from __future__ import annotations

import base64
import gzip
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXP = ROOT / "experiments" / "01-vanishing-absorber"
HISTORY = EXP / "manuscript_history"
PART_GLOB = "MANUSCRIPT_REV3_ANON_2026-08-11.tex.gz.b64.part*"
OUTPUT = EXP / "MANUSCRIPT_CURRENT.tex"
EXPECTED_SOURCE_SHA256 = "3ba57ed7c7bbe264038ffa4e6eabfc1ea90c1075d4989d4075d2589352cf6d8c"
EXPECTED_GZIP_SHA256 = "e413c1be218f4f3d33611381b6407137169abafb6fc22a6087f33f77b3c2ae3e"
EXPECTED_PARTS = 6


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    parts = sorted(HISTORY.glob(PART_GLOB))
    if len(parts) != EXPECTED_PARTS:
        raise SystemExit(
            f"Refusing extraction: expected {EXPECTED_PARTS} snapshot parts, found {len(parts)}"
        )

    encoded = "".join(part.read_text(encoding="ascii").strip() for part in parts)
    packed = base64.b64decode(encoded, validate=True)
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

    lines = len(source.decode("utf-8").splitlines())
    if lines != 696:
        raise SystemExit(f"Refusing extraction: expected 696 lines, recovered {lines}")

    OUTPUT.write_bytes(source)
    print(f"Wrote verified manuscript baseline: {OUTPUT}")
    print(f"source SHA-256: {source_hash}")
    print(f"lines: {lines}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
