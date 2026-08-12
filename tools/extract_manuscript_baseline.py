#!/usr/bin/env python3
"""Extract and verify the immutable anonymous Rev. 8 manuscript baseline."""
from __future__ import annotations

import base64
import gzip
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXP = ROOT / "experiments" / "01-vanishing-absorber"
HISTORY = EXP / "manuscript_history"
PART_GLOB = "MANUSCRIPT_REV8_ANON_2026-08-11.tex.gz.b64.part*"
OUTPUT = EXP / "MANUSCRIPT_CURRENT.tex"
EXPECTED_SOURCE_SHA256 = "28eb3de954d50046f177e06e4b54eb1812414c03a1d53a933904f99fb3c49ba9"
EXPECTED_GZIP_SHA256 = "44af67c407d07b6e7d60bbc6760f14cbe0f44cf763a74e972a9b3322a5d8d2f7"
EXPECTED_PARTS = 7
EXPECTED_LINES = 1023


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

    text = source.decode("utf-8")
    lines = len(text.splitlines())
    if lines != EXPECTED_LINES:
        raise SystemExit(
            f"Refusing extraction: expected {EXPECTED_LINES} lines, recovered {lines}"
        )
    if r"\author{Anonymous}" not in text or "pdfauthor={Anonymous}" not in text:
        raise SystemExit("Refusing extraction: canonical author metadata is not anonymous")

    OUTPUT.write_bytes(source)
    print(f"Wrote verified anonymous manuscript baseline: {OUTPUT}")
    print(f"source SHA-256: {source_hash}")
    print(f"lines: {lines}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
