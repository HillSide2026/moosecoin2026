#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path

ALLOWLIST = {
    # Explicit frontmatter exceptions should be listed here as repo-relative paths.
}


def list_markdown_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "-z", "--", "*.md"],
        check=True,
        capture_output=True,
    )
    files = []
    for raw in result.stdout.split(b"\0"):
        if raw:
            files.append(Path(raw.decode("utf-8", errors="surrogateescape")))
    return files


def has_frontmatter(path: Path) -> bool:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return False
    if text.startswith("\ufeff"):
        text = text.lstrip("\ufeff")
    lines = text.splitlines()
    if not lines:
        return False
    if lines[0].strip() != "---":
        return False
    for line in lines[1:]:
        if line.strip() == "---":
            return True
    return False


def main() -> int:
    missing = []
    for path in list_markdown_files():
        posix_path = path.as_posix()
        if posix_path in ALLOWLIST:
            continue
        if not has_frontmatter(path):
            missing.append(posix_path)

    if missing:
        print(
            "Missing YAML frontmatter. Add a frontmatter block per 00_SYSTEM/SCHEMAS.md."
        )
        for path in missing:
            print(f"- {path}")
        return 1

    print("Frontmatter check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
