#!/usr/bin/env python3
"""Adaptive Dev Team structure self-check.

Standard library only, deterministic, dependency-free.

Exit semantics:
  0 = no ERROR (WARNINGs allowed)
  1 = at least one ERROR

Run from anywhere; the skill root is derived from this file's location:
    python3 scripts/check-structure.py

Prove the checks actually fire (not a no-op validator):
    python3 scripts/check-structure.py --self-test
"""
import hashlib
import re
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_DIRS = [
    "roles", "builders", "specialists", "workflows",
    "protocols", "policies", "templates", "examples", "scripts",
]
# Optional per the Agent Skills specification: missing is NOT an error.
OPTIONAL_DIRS = ["references", "assets"]

REQUIRED_FILES = ["SKILL.md"]

REFERENCE_PREFIXES = (
    "roles/", "builders/", "specialists/", "workflows/", "protocols/",
    "policies/", "templates/", "examples/", "scripts/", "references/", "assets/",
)
REFERENCE_RE = re.compile(r"`((?:" + "|".join(REFERENCE_PREFIXES) + r")[^`\s]+?)`")
# A backticked bare markdown filename, e.g. `builder.md` (no directory part).
# Case-insensitive on purpose: `CHANGELOG.md`-style names must be seen too.
BARE_FILE_RE = re.compile(r"`([A-Za-z0-9][A-Za-z0-9._-]*\.md)`")
# A reference that intentionally points outside the skill package, e.g. `../CHANGELOG.md`.
OUTSIDE_RE = re.compile(r"`\.\./([^`\s]+?)`")

NEGATIVE_MARKERS = ("禁止", "forbidden", "invalid", "anti-pattern", "do not use", "must not")
MIN_WORKFLOW_LINES = 8
PLACEHOLDER_MARKERS = ("task matches profile", "dynamic from triage", "todo", "tbd", "placeholder")
NAME_RE = re.compile(r"[a-z0-9]+(-[a-z0-9]+)*")
WHEN_CLAUSES = ("use when", "use this", "when a", "when the", "trigger")


def markdown_files(root, skip_scripts=True):
    files = sorted(p for p in root.rglob("*.md") if ".git" not in p.parts)
    if skip_scripts:
        files = [p for p in files if p.suffix == ".md" and p.name != "check-structure.py"]
    return files


def parse_frontmatter(text):
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    fields = {}
    for line in text[3:end].splitlines():
        line = line.rstrip()
        if not line or line.lstrip().startswith("#") or ":" not in line:
            continue
        if line[0].isspace():
            continue  # nested value, e.g. metadata sub-keys
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip().strip('"').strip("'")
    return fields


def check_package_hygiene(root):
    """Flag files that must never ship in the distribution package."""
    errors, warnings = [], []
    for path in sorted(root.rglob("*")):
        if ".git" in path.parts:
            continue
        name = path.name
        if name == ".DS_Store":
            kind = "macOS metadata"
        elif name.startswith("._") or "__MACOSX" in path.parts:
            kind = "macOS AppleDouble metadata"
        elif name == "__pycache__" or name.endswith(".pyc"):
            kind = "Python bytecode cache"
        else:
            continue
        warnings.append(
            "PACKAGE HYGIENE: %s (%s) would leak into the distributable; remove it "
            "(zip -rX with COPYFILE_DISABLE=1 and -x avoids it by construction)"
            % (path.relative_to(root), kind)
        )
    return errors, warnings


def check_layout(root):
    errors, warnings = [], []
    for d in REQUIRED_DIRS:
        if not (root / d).is_dir():
            errors.append("MISSING REQUIRED DIR: %s/" % d)
    for d in OPTIONAL_DIRS:
        if not (root / d).is_dir():
            warnings.append("OPTIONAL DIR ABSENT: %s/ (allowed by the Agent Skills spec)" % d)
    for f in REQUIRED_FILES:
        if not (root / f).is_file():
            errors.append("MISSING REQUIRED FILE: %s" % f)
    return errors, warnings


def check_frontmatter(root):
    errors, warnings = [], []
    skill = root / "SKILL.md"
    if not skill.is_file():
        return errors, warnings
    fields = parse_frontmatter(skill.read_text(encoding="utf-8"))
    if fields is None:
        errors.append("SKILL.md: missing YAML frontmatter (--- ... ---)")
        return errors, warnings
    name = fields.get("name")
    description = fields.get("description")
    if not name:
        errors.append("SKILL.md frontmatter: `name` is missing or empty")
    elif not NAME_RE.fullmatch(name) or len(name) > 64:
        errors.append(
            "SKILL.md frontmatter: `name`=%r must be lowercase letters/digits/hyphens, "
            "no leading/trailing hyphen, max 64 chars" % name
        )
    if not description:
        errors.append("SKILL.md frontmatter: `description` is missing or empty")
    elif len(description) > 1024:
        errors.append("SKILL.md frontmatter: `description` exceeds 1024 characters")
    elif not any(w in description.lower() for w in WHEN_CLAUSES):
        warnings.append("SKILL.md frontmatter: `description` has no clear 'when to use' clause")
    # The spec requires `name` to match the parent directory name exactly.
    if name and root.name != name:
        warnings.append(
            "SKILL.md frontmatter: SPEC DEVIATION - the Agent Skills specification requires "
            "`name` to match the parent directory name, but the directory is %r and `name` is %r. "
            "Fix with: git mv %s %s   (or document the deviation in README.md)"
            % (root.name, name, root.name, name)
        )
    return errors, warnings


def check_references(root):
    errors, warnings = [], []
    for path in markdown_files(root):
        rel = path.relative_to(root)
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for match in REFERENCE_RE.finditer(text):
            target = match.group(1).split("#")[0].rstrip(".,;:")
            # Skip globs and `<name>` templates: they are patterns, not paths.
            if any(ch in target for ch in "*<>{}") or "..." in target or target.endswith("/"):
                continue
            if not (root / target).exists():
                errors.append("%s: references missing local resource `%s`" % (rel, target))
        # Outside-package references must be explicit (`../X`) and must exist.
        for match in OUTSIDE_RE.finditer(text):
            target = match.group(1).split("#")[0].rstrip(".,;:")
            if any(ch in target for ch in "*<>{}") or "..." in target:
                continue
            if not (root.parent / target).exists():
                errors.append(
                    "%s: references missing outside-package resource `../%s`" % (rel, target)
                )
            else:
                warnings.append(
                    "%s: `../%s` lives outside the skill package and is not shipped in the "
                    "distributable (Intentional? Keep the `../` form so this stays explicit.)"
                    % (rel, target)
                )
        # Bare filenames are ambiguous; skip lines that document a counter-example.
        for line in text.splitlines():
            low = line.lower()
            if any(m in low for m in NEGATIVE_MARKERS):
                continue
            for match in BARE_FILE_RE.finditer(line):
                bare = match.group(1)
                if (root / bare).exists():
                    continue  # already Skill-root-relative and unambiguous
                if (path.parent / bare).exists():
                    errors.append(
                        "%s: bare reference `%s` resolves only as a sibling; §7.1 requires a "
                        "Skill-root-relative path: `%s`"
                        % (rel, bare, (path.parent / bare).relative_to(root).as_posix())
                    )
                else:
                    hits = [p for p in root.rglob(bare) if ".git" not in p.parts]
                    if not hits:
                        errors.append("%s: references unknown file `%s`" % (rel, bare))
                    else:
                        errors.append(
                            "%s: bare reference `%s` is ambiguous; use `%s`"
                            % (rel, bare, hits[0].relative_to(root).as_posix())
                        )
    return errors, warnings


def check_placeholders(root):
    errors, warnings = [], []
    groups = {}
    for path in sorted((root / "workflows").glob("*.md")):
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        groups.setdefault(digest, []).append(path.name)
    for names in groups.values():
        if len(names) > 1:
            errors.append(
                "workflows: %d files have identical content (%s) - a file is not a capability"
                % (len(names), ", ".join(sorted(names)))
            )
    for path in sorted((root / "workflows").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        significant = [ln for ln in text.splitlines() if ln.strip() and not ln.startswith("#")]
        low = text.lower()
        marker = next((m for m in PLACEHOLDER_MARKERS if m in low), None)
        if len(significant) < MIN_WORKFLOW_LINES or marker:
            warnings.append(
                "workflows/%s: possible placeholder (%d content lines%s)"
                % (path.name, len(significant), ", marker %r" % marker if marker else "")
            )
    for path in markdown_files(root):
        if re.search(r"\bTODO\b|\bTBD\b", path.read_text(encoding="utf-8", errors="replace")):
            warnings.append("%s: contains TODO/TBD marker" % path.relative_to(root))
    return errors, warnings


def check_examples(root):
    errors, warnings = [], []
    for path in sorted((root / "examples").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        marked = "hypothetical" in text.lower() or "illustrative" in text.lower()
        if not marked:
            errors.append("examples/%s: not marked as hypothetical/illustrative" % path.name)
        # Unconditional: a hypothetical example must never claim verified completion,
        # whether or not it carries the hypothetical marking.
        if re.search(r"\[[xX]\]", text):
            warnings.append(
                "examples/%s: contains a checked box `[x]` - hypothetical examples keep items unchecked"
                % path.name
            )
        if "\u2705" in text:
            warnings.append(
                "examples/%s: contains a completion checkmark - hypothetical examples must not claim done"
                % path.name
            )
    return errors, warnings


def run_all(root):
    errors, warnings = [], []
    for check in (
        check_layout,
        check_package_hygiene,
        check_frontmatter,
        check_references,
        check_placeholders,
        check_examples,
    ):
        e, w = check(root)
        errors += e
        warnings += w
    return errors, warnings


def self_test():
    """Copy the skill to a temp dir, inject known defects, assert they are caught."""
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp) / "adaptive-dev-team"
        shutil.copytree(ROOT, root)
        # Mirror the real layout: `../CHANGELOG.md` is a repository-level file that
        # legitimately lives outside the skill package.
        repo_changelog = ROOT.parent / "CHANGELOG.md"
        if repo_changelog.is_file():
            shutil.copy2(repo_changelog, root.parent / "CHANGELOG.md")

        clean_errors, _ = run_all(root)
        assert not clean_errors, "baseline copy should be clean, got: %s" % clean_errors

        # 1. Duplicate a workflow verbatim -> placeholder ERROR.
        (root / "workflows" / "bugfix.md").write_text(
            (root / "workflows" / "refactor.md").read_text(encoding="utf-8"), encoding="utf-8"
        )
        # 2. Point at a missing resource -> reference ERROR.
        (root / "roles" / "leader.md").write_text(
            (root / "roles" / "leader.md").read_text(encoding="utf-8")
            + "\nSee `protocols/does-not-exist.md`.\n",
            encoding="utf-8",
        )
        # 3. Strip the hypothetical marking -> examples ERROR.
        (root / "examples" / "small-fix.md").write_text(
            (root / "examples" / "small-fix.md").read_text(encoding="utf-8")
            .replace("Hypothetical", "Example").replace("hypothetical", "example"),
            encoding="utf-8",
        )
        # 4. Break frontmatter name -> frontmatter ERROR.
        skill = root / "SKILL.md"
        skill.write_text(
            skill.read_text(encoding="utf-8").replace("name: adaptive-dev-team", "name: Bad_Name"),
            encoding="utf-8",
        )
        # 5. Check a box inside an already-marked hypothetical example -> WARNING.
        marked = root / "examples" / "normal-feature.md"
        marked.write_text(
            marked.read_text(encoding="utf-8") + "\n- [x] verified \u2705\n", encoding="utf-8"
        )
        # 6. Regress a builder to a sibling-only bare reference -> §7.1 ERROR.
        backend = root / "builders" / "backend.md"
        backend.write_text(
            backend.read_text(encoding="utf-8") + "\nSee `frontend.md`.\n", encoding="utf-8"
        )
        # 7. Reference an uppercase, out-of-package file bare -> ERROR
        #    (guards the case-insensitivity of the bare-name check).
        leader = root / "roles" / "leader.md"
        leader.write_text(
            leader.read_text(encoding="utf-8") + "\nSee `CHANGELOG.md`.\n", encoding="utf-8"
        )
        # 8. Drop macOS metadata into the package -> hygiene WARNING.
        (root / ".DS_Store").write_bytes(b"\x00")
        (root / "roles" / "._leader.md").write_bytes(b"\x00")

        errors, warnings = run_all(root)
        expected = {
            "identical content": False,
            "missing local resource": False,
            "not marked as hypothetical/illustrative": False,
            "`name`=": False,
            "resolves only as a sibling": False,
            "references unknown file `CHANGELOG.md`": False,
        }
        for key in expected:
            expected[key] = any(key in e for e in errors)
        missed = [k for k, found in expected.items() if not found]
        warn_expected = {"checked box", "completion checkmark", "PACKAGE HYGIENE"}
        warn_missed = [k for k in warn_expected if not any(k in w for w in warnings)]
        if missed or warn_missed:
            print("SELF-TEST FAILED: checks did not fire for: %s" % (missed + warn_missed))
            print("errors seen: %s" % errors)
            print("warnings seen: %s" % warnings)
            return 1
    print(
        "SELF-TEST OK: 6 injected defects + 3 warning classes detected, clean copy passes"
    )
    return 0


def main(argv):
    if "--self-test" in argv:
        return self_test()
    errors, warnings = run_all(ROOT)
    for w in warnings:
        print("WARNING: %s" % w)
    for e in errors:
        print("ERROR: %s" % e)
    if errors:
        print("\nStructure INVALID: %d error(s), %d warning(s)" % (len(errors), len(warnings)))
        return 1
    print("\nStructure OK: 0 errors, %d warning(s)" % len(warnings))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
