#!/usr/bin/env python3
"""Check that every file in members/ is filled in correctly.

Run it locally before you push:

    python scripts/check_members.py

In CI it also gets --base <ref> and warns about files changed outside members/.
"""

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MEMBERS = ROOT / "members"

# GitHub usernames: letters, digits and single hyphens, at most 39 characters.
USERNAME_RE = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9]|-(?=[A-Za-z0-9])){0,38}$")
FIELDS = ["GitHub", "Major", "Year", "Fun fact"]
FIELD_RE = re.compile(r"^\s*[-*]\s*\*\*(?P<name>[^*]+?):?\*\*:?\s*(?P<value>.*)$")
TEMPLATE_VALUES = {
    "your name",
    "@your-username",
    "your major",
    "freshman / sophomore / junior / senior / grad",
    "something interesting about you",
}
MAX_LINES = 40

IN_CI = os.environ.get("GITHUB_ACTIONS") == "true"


def report(level, path, message):
    rel = path.relative_to(ROOT).as_posix()
    if IN_CI:
        print(f"::{level} file={rel}::{message}")
    else:
        label = "ERROR" if level == "error" else "WARNING"
        print(f"{label}  {rel}: {message}")


def check_file(path):
    """Return a list of problems with one member file."""
    problems = []
    username = path.stem

    if path.suffix != ".md":
        return [f"Member files must end in .md (try renaming it to {username}.md)."]
    if not USERNAME_RE.match(username):
        problems.append(
            f"'{username}' isn't a valid GitHub username. Name the file exactly "
            "like your username, e.g. members/octocat.md."
        )

    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return ["The file isn't plain UTF-8 text. Save it as plain text and try again."]

    lines = text.splitlines()
    if len(lines) > MAX_LINES:
        problems.append(f"Keep it short: {len(lines)} lines is over the {MAX_LINES}-line limit.")

    first = next((line for line in lines if line.strip()), "")
    if not first.startswith("# "):
        problems.append("The first line should be your name as a heading, like '# Ada Lovelace'.")
    elif first[2:].strip().lower() in TEMPLATE_VALUES:
        problems.append("Replace '# Your Name' with your actual name.")

    found = {}
    for line in lines:
        match = FIELD_RE.match(line)
        if match:
            found[match["name"].strip().lower()] = match["value"].strip()

    for field in FIELDS:
        value = found.get(field.lower())
        if value is None:
            problems.append(f"Missing the '- **{field}:**' line. Compare your file to members/_template.md.")
        elif not value:
            problems.append(f"The '{field}' line is empty. Fill it in.")
        elif value.lower() in TEMPLATE_VALUES:
            problems.append(f"The '{field}' line still has the template text. Replace it with your own.")

    github = found.get("github", "")
    handle = github.lstrip("@")
    if handle and github.lower() not in TEMPLATE_VALUES and handle.lower() != username.lower():
        problems.append(
            f"Your GitHub line says @{handle}, but the file is named {path.name}. "
            "They should match."
        )

    return problems


def changed_outside_members(base):
    """Files changed on this branch compared to base, outside members/."""
    result = subprocess.run(
        ["git", "diff", "--name-only", f"{base}...HEAD"],
        cwd=ROOT, capture_output=True, text=True, check=True,
    )
    return [name for name in result.stdout.splitlines() if name and not name.startswith("members/")]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", help="git ref to compare against (used in CI)")
    args = parser.parse_args()

    files = sorted(
        p for p in MEMBERS.iterdir()
        if p.is_file() and not p.name.startswith("_") and p.name != "README.md"
    )

    failed = 0
    for path in files:
        problems = check_file(path)
        for problem in problems:
            report("error", path, problem)
        failed += bool(problems)

    if args.base:
        for name in changed_outside_members(args.base):
            report(
                "warning", ROOT / name,
                "This pull request changes a file outside members/. "
                "For the workshop you only need to add your own member file.",
            )

    if failed:
        print(f"\n{failed} of {len(files)} member file(s) need fixing. See the messages above.")
        return 1
    print(f"All {len(files)} member file(s) look good.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
