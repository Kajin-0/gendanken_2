#!/usr/bin/env python3
"""Extract and verify the immutable anonymous Rev. 4 manuscript baseline."""
from __future__ import annotations

import base64
import gzip
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXP = ROOT / "experiments" / "01-vanishing-absorber"
HISTORY = EXP / "manuscript_history"
PART_GLOB = "MANUSCRIPT_REV4_ANON_2026-08-11.tex.gz.b64.part*"
OUTPUT = EXP / "MANUSCRIPT_CURRENT.tex"
EXPECTED_SOURCE_SHA256 = "9da8c6094a58109873382b6b3c73c519b26f519e327f5ec8058009bc4896df00"
EXPECTED_GZIP_SHA256 = "fad3aeee778de42a7c9de278abec5676d6fb3d0effebd4994c7bbdb0950a3f68"
EXPECTED_PARTS = 3
EXPECTED_LINES = 817


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
