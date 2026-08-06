"""Merge ci.fail_on_warning: true into a skill-guard.yaml config.

skill-guard has no --fail-on-warning CLI flag; that behavior is config-driven
(ci.fail_on_warning in skill-guard.yaml). This script merges it into a copy
of the caller's config (if one was provided) so the action's fail-on-warning
input actually works instead of being passed as an invalid CLI flag.

Usage: merge_fail_on_warning.py <source-config-or-empty-string> <dest-path>
"""

from __future__ import annotations

import sys

from ruamel.yaml import YAML


def main() -> None:
    src, dest = sys.argv[1], sys.argv[2]

    yaml = YAML()
    yaml.preserve_quotes = True

    data = {}
    if src:
        with open(src) as f:
            data = yaml.load(f) or {}

    ci = data.get("ci")
    if not isinstance(ci, dict):
        ci = {}
        data["ci"] = ci
    ci["fail_on_warning"] = True

    with open(dest, "w") as f:
        yaml.dump(data, f)


if __name__ == "__main__":
    main()
