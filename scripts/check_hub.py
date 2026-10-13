#!/usr/bin/env python3
from __future__ import annotations

import json
import hashlib
import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "hub_manifest.json"
LINK_PATTERN = re.compile(r"(?<!!)\[[^]]*]\(([^)]+)\)")
HASH_PATTERN = re.compile(r"source-sha256:\s*([0-9a-f]{64})")


def file_hash(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def check_links(errors: list[str]) -> None:
    for markdown in ROOT.rglob("*.md"):
        if ".git" in markdown.parts:
            continue
        content = markdown.read_text(encoding="utf-8")
        for raw_target in LINK_PATTERN.findall(content):
            target = raw_target.strip().strip("<>").split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (markdown.parent / unquote(target)).resolve()
            if not resolved.exists():
                errors.append(f"broken link: {markdown.relative_to(ROOT)} -> {target}")


def check_manifest(errors: list[str], warnings: list[str]) -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    index = (ROOT / "INDEX.md").read_text(encoding="utf-8")
    for item in manifest.get("documents", []):
        source = ROOT / item["source"]
        output = ROOT / item["output"]
        if not source.exists():
            errors.append(f"missing source: {item['source']}")
        if not output.exists():
            errors.append(f"missing output: {item['output']}")
            continue
        if output.stat().st_size == 0:
            errors.append(f"empty output: {item['output']}")
        if source.exists():
            match = HASH_PATTERN.search(output.read_text(encoding="utf-8")[:500])
            if not match:
                warnings.append(f"missing source hash: {item['output']}")
            elif match.group(1) != file_hash(source):
                warnings.append(f"stale conversion: {item['output']}")
        if item["output"] not in index:
            warnings.append(f"not listed in INDEX.md: {item['output']}")
    for item in manifest.get("manual_conversions", []):
        output = ROOT / item["output"]
        if not output.exists():
            errors.append(f"missing manual output: {item['output']}")
        for source_name in item.get("sources", []):
            if not (ROOT / source_name).exists():
                errors.append(f"missing manual source: {source_name}")


def main() -> None:
    errors: list[str] = []
    warnings: list[str] = []
    check_links(errors)
    check_manifest(errors, warnings)
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        raise SystemExit(1)
    print(f"hub check passed with {len(warnings)} warning(s)")


if __name__ == "__main__":
    main()
