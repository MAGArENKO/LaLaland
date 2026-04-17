#!/usr/bin/env python3
"""Scan drives/projects for agent-system signals and enhancement directions.

This tool is optimized for large local Windows/Linux file trees and focuses on
finding development opportunities around Argilla/Ollama/Docker/server-based
systems used for generating and teaching agents.
"""

from __future__ import annotations

import argparse
import ctypes
import json
import os
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

DEFAULT_KEYWORDS = [
    "argilla",
    "agrilla",
    "ollama",
    "docker",
    "docker-compose",
    "server",
    "agent",
    "training",
    "dataset",
    "mcp",
    "fastapi",
    "celery",
]

DEFAULT_PROJECT_MARKERS = {
    "pyproject.toml",
    "requirements.txt",
    "package.json",
    "Dockerfile",
    "docker-compose.yml",
    "docker-compose.yaml",
    "compose.yml",
    "compose.yaml",
    ".git",
}

DEFAULT_EXCLUDED_DIRS = {
    ".git",
    ".hg",
    ".svn",
    "node_modules",
    ".venv",
    "venv",
    "__pycache__",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".next",
    "dist",
    "build",
    "target",
    ".idea",
    ".vscode",
    "$RECYCLE.BIN",
    "System Volume Information",
}

TEXT_FILE_EXTENSIONS = {
    ".py",
    ".md",
    ".txt",
    ".json",
    ".yaml",
    ".yml",
    ".toml",
    ".ini",
    ".cfg",
    ".conf",
    ".env",
    ".js",
    ".ts",
    ".tsx",
    ".jsx",
    ".java",
    ".go",
    ".rs",
    ".c",
    ".cpp",
    ".h",
    ".hpp",
    ".cs",
    ".sh",
    ".ps1",
    ".sql",
    ".html",
    ".css",
    ".dockerfile",
}


@dataclass
class ScanHit:
    path: str
    keywords_in_path: list[str]
    keywords_in_content: list[str]
    snippet: str | None


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def detect_windows_drives() -> list[str]:
    """Detect mounted Windows drive letters (e.g. C:\\, D:\\)."""
    if os.name != "nt":
        return []

    drives: list[str] = []
    bitmask = ctypes.windll.kernel32.GetLogicalDrives()  # type: ignore[attr-defined]
    for i in range(26):
        if bitmask & (1 << i):
            letter = chr(ord("A") + i)
            drives.append(f"{letter}:\\")
    return drives


def compile_patterns(keywords: Iterable[str]) -> dict[str, re.Pattern[str]]:
    return {kw: re.compile(rf"\b{re.escape(kw)}\b", re.IGNORECASE) for kw in keywords}


def is_likely_text(path: Path, max_file_size_bytes: int) -> bool:
    try:
        if not path.is_file():
            return False
        if path.stat().st_size > max_file_size_bytes:
            return False
    except OSError:
        return False

    suffix = path.suffix.lower()
    if suffix in TEXT_FILE_EXTENSIONS:
        return True

    # Fast binary sniff for unknown extensions.
    try:
        with path.open("rb") as f:
            sample = f.read(2048)
    except OSError:
        return False
    return b"\x00" not in sample


def find_keywords(text: str, patterns: dict[str, re.Pattern[str]]) -> list[str]:
    found = [kw for kw, pattern in patterns.items() if pattern.search(text)]
    found.sort()
    return found


def first_matching_line(text: str, patterns: dict[str, re.Pattern[str]]) -> str | None:
    for line in text.splitlines():
        for pattern in patterns.values():
            if pattern.search(line):
                cleaned = line.strip()
                if len(cleaned) > 220:
                    return cleaned[:217] + "..."
                return cleaned
    return None


def iter_scan_files(
    root: Path,
    excluded_dirs: set[str],
    max_files: int | None = None,
) -> Iterable[Path]:
    count = 0
    for dirpath, dirnames, filenames in os.walk(root, topdown=True):
        dirnames[:] = [d for d in dirnames if d not in excluded_dirs and not d.startswith(".cache")]
        for filename in filenames:
            path = Path(dirpath) / filename
            yield path
            count += 1
            if max_files is not None and count >= max_files:
                return


def detect_project_roots(root: Path, excluded_dirs: set[str], max_files: int | None) -> set[Path]:
    project_roots: set[Path] = set()
    scanned = 0
    for dirpath, dirnames, filenames in os.walk(root, topdown=True):
        dirnames[:] = [d for d in dirnames if d not in excluded_dirs and not d.startswith(".cache")]
        entries = set(filenames) | set(dirnames)
        if entries & DEFAULT_PROJECT_MARKERS:
            project_roots.add(Path(dirpath))
        scanned += len(filenames)
        if max_files is not None and scanned >= max_files:
            break
    return project_roots


def assign_project(path: Path, project_roots: set[Path], root: Path) -> Path:
    best = root
    for candidate in project_roots:
        try:
            path.relative_to(candidate)
            if len(candidate.parts) > len(best.parts):
                best = candidate
        except ValueError:
            continue
    return best


def derive_project_flags(project_root: Path, keyword_counter: Counter[str]) -> dict[str, bool]:
    lower_keywords = {k.lower() for k, c in keyword_counter.items() if c > 0}
    entries = set()
    try:
        entries = {p.name for p in project_root.iterdir()}
    except OSError:
        pass

    return {
        "has_docker": "docker" in lower_keywords or "docker-compose.yml" in entries or "Dockerfile" in entries,
        "has_ollama": "ollama" in lower_keywords,
        "has_argilla": "argilla" in lower_keywords or "agrilla" in lower_keywords,
        "has_api_server": any(k in lower_keywords for k in {"server", "fastapi"}),
        "has_training_signals": any(k in lower_keywords for k in {"training", "dataset", "agent"}),
        "has_mcp_signals": "mcp" in lower_keywords,
    }


def build_project_recommendations(flags: dict[str, bool]) -> list[str]:
    recommendations: list[str] = []

    if flags["has_argilla"] and flags["has_ollama"] and flags["has_docker"]:
        recommendations.append(
            "Strong candidate for a local agent-training stack: add an orchestrator service "
            "that wires Ollama inference, Argilla annotation loops, and Docker-managed dependencies."
        )
    if flags["has_ollama"] and not flags["has_docker"]:
        recommendations.append(
            "Containerize inference dependencies to make Ollama-based workflows reproducible "
            "across machines and easier to orchestrate."
        )
    if flags["has_argilla"] and not flags["has_training_signals"]:
        recommendations.append(
            "Argilla detected but weak training signals; add dataset/evaluation pipelines to close the feedback loop."
        )
    if flags["has_training_signals"] and not flags["has_argilla"]:
        recommendations.append(
            "Training signals detected without Argilla; consider adding Argilla for human-in-the-loop labeling and QA."
        )
    if flags["has_docker"] and not flags["has_api_server"]:
        recommendations.append(
            "Docker setup exists but API/server signals are weak; add a control API (e.g. FastAPI) for agent orchestration."
        )
    if flags["has_api_server"] and not flags["has_mcp_signals"]:
        recommendations.append(
            "API server detected; consider introducing MCP-style tool contracts for cleaner multi-agent action interfaces."
        )
    if not recommendations:
        recommendations.append(
            "Create a minimal agent platform baseline: Docker Compose + FastAPI control plane + Ollama + Argilla + eval dataset."
        )
    return recommendations


def build_global_recommendations(global_counts: Counter[str]) -> list[str]:
    lower = {k.lower() for k, v in global_counts.items() if v > 0}
    recs: list[str] = []
    if "ollama" in lower and "argilla" in lower and "docker" in lower:
        recs.append("Prioritize unifying existing Ollama + Argilla + Docker assets into one shared multi-repo platform spec.")
    else:
        recs.append(
            "Bootstrap a common stack blueprint with Docker Compose services for Ollama, Argilla, vector DB, and API gateway."
        )
    if "agent" in lower and "training" in lower:
        recs.append("Add an agent registry + versioned skill packs + evaluation gates before promoting experiments to production.")
    else:
        recs.append("Standardize project manifests around goals/actions/memory/environment to enable consistent agent governance.")
    if "mcp" not in lower:
        recs.append("Introduce MCP-compatible tool endpoints to decouple agent decision logic from environment-specific execution.")
    return recs


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Detailed drive/project scan for enhancement directions around agent-training systems."
    )
    parser.add_argument(
        "--roots",
        nargs="*",
        default=[],
        help=(
            "Root folders/drives to scan. If omitted on Windows, all drive letters are scanned "
            "(C:\\ D:\\ ...)."
        ),
    )
    parser.add_argument(
        "--keyword",
        action="append",
        default=[],
        help="Extra keyword to search (can be used multiple times).",
    )
    parser.add_argument(
        "--max-file-size-mb",
        type=float,
        default=2.0,
        help="Maximum file size to inspect for content matches.",
    )
    parser.add_argument(
        "--max-files-per-root",
        type=int,
        default=300000,
        help="Safety cap for total files traversed per root.",
    )
    parser.add_argument(
        "--max-hits",
        type=int,
        default=5000,
        help="Maximum number of hit records to store in output.",
    )
    parser.add_argument(
        "--output-dir",
        default="reports",
        help="Directory for generated JSON/Markdown reports.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    roots = [Path(p) for p in args.roots]
    if not roots:
        roots = [Path(p) for p in detect_windows_drives()]

    if not roots:
        print("No roots provided and no Windows drives auto-detected. Use --roots <path...>.")
        return 1

    keywords = sorted({kw.strip().lower() for kw in (DEFAULT_KEYWORDS + args.keyword) if kw.strip()})
    patterns = compile_patterns(keywords)
    excluded_dirs = set(DEFAULT_EXCLUDED_DIRS)
    max_file_size_bytes = int(args.max_file_size_mb * 1024 * 1024)

    started = now_iso()
    hits: list[ScanHit] = []
    files_scanned = 0
    skipped_binary_or_large = 0

    all_project_roots: set[Path] = set()
    file_to_project: dict[Path, Path] = {}
    project_keyword_counts: dict[Path, Counter[str]] = defaultdict(Counter)
    project_file_counts: Counter[Path] = Counter()

    for root in roots:
        if not root.exists():
            print(f"[warn] Root does not exist, skipping: {root}")
            continue

        root = root.resolve()
        print(f"[scan] {root}")
        project_roots = detect_project_roots(root, excluded_dirs, args.max_files_per_root)
        all_project_roots.update(project_roots)

        for path in iter_scan_files(root, excluded_dirs, args.max_files_per_root):
            files_scanned += 1
            project = assign_project(path, project_roots, root)
            file_to_project[path] = project
            project_file_counts[project] += 1

            path_match = find_keywords(str(path), patterns)
            content_match: list[str] = []
            snippet = None

            if is_likely_text(path, max_file_size_bytes):
                try:
                    text = path.read_text(encoding="utf-8", errors="ignore")
                    content_match = find_keywords(text, patterns)
                    if content_match:
                        snippet = first_matching_line(text, {k: patterns[k] for k in content_match})
                except OSError:
                    pass
            else:
                skipped_binary_or_large += 1

            matched_keywords = sorted(set(path_match + content_match))
            if matched_keywords:
                for kw in matched_keywords:
                    project_keyword_counts[project][kw] += 1

                if len(hits) < args.max_hits:
                    hits.append(
                        ScanHit(
                            path=str(path),
                            keywords_in_path=path_match,
                            keywords_in_content=content_match,
                            snippet=snippet,
                        )
                    )

    global_keyword_counts = Counter()
    for counter in project_keyword_counts.values():
        global_keyword_counts.update(counter)

    project_reports = []
    for project_root, file_count in project_file_counts.most_common():
        kw_counter = project_keyword_counts.get(project_root, Counter())
        flags = derive_project_flags(project_root, kw_counter)
        recommendations = build_project_recommendations(flags)
        project_reports.append(
            {
                "project_root": str(project_root),
                "files_seen": file_count,
                "keyword_hits": sum(kw_counter.values()),
                "keyword_frequencies": dict(kw_counter),
                "flags": flags,
                "recommendations": recommendations,
            }
        )

    report = {
        "scan_started_utc": started,
        "scan_finished_utc": now_iso(),
        "roots": [str(r) for r in roots],
        "keywords": keywords,
        "totals": {
            "files_scanned": files_scanned,
            "hits_recorded": len(hits),
            "projects_detected": len(project_reports),
            "skipped_binary_or_large_files": skipped_binary_or_large,
        },
        "global_keyword_frequencies": dict(global_keyword_counts),
        "global_recommendations": build_global_recommendations(global_keyword_counts),
        "projects": project_reports,
        "hits": [
            {
                "path": h.path,
                "keywords_in_path": h.keywords_in_path,
                "keywords_in_content": h.keywords_in_content,
                "snippet": h.snippet,
            }
            for h in hits
        ],
    }

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    json_path = output_dir / f"drive_enhancement_scan_{stamp}.json"
    md_path = output_dir / f"drive_enhancement_scan_{stamp}.md"

    json_path.write_text(json.dumps(report, indent=2, ensure_ascii=True), encoding="utf-8")

    lines = []
    lines.append("# Drive Enhancement Scan Report")
    lines.append("")
    lines.append(f"- Started (UTC): {report['scan_started_utc']}")
    lines.append(f"- Finished (UTC): {report['scan_finished_utc']}")
    lines.append(f"- Roots: {', '.join(report['roots'])}")
    lines.append(f"- Files scanned: {report['totals']['files_scanned']}")
    lines.append(f"- Projects detected: {report['totals']['projects_detected']}")
    lines.append(f"- Hits recorded: {report['totals']['hits_recorded']}")
    lines.append("")
    lines.append("## Global Recommendations")
    for item in report["global_recommendations"]:
        lines.append(f"- {item}")
    lines.append("")
    lines.append("## Top Keyword Frequencies")
    if report["global_keyword_frequencies"]:
        for keyword, count in sorted(report["global_keyword_frequencies"].items(), key=lambda kv: kv[1], reverse=True):
            lines.append(f"- `{keyword}`: {count}")
    else:
        lines.append("- No keyword hits found.")
    lines.append("")
    lines.append("## Top Project Opportunities")
    top_projects = sorted(project_reports, key=lambda p: p["keyword_hits"], reverse=True)[:15]
    if top_projects:
        for project in top_projects:
            lines.append(f"### {project['project_root']}")
            lines.append(
                f"- Files seen: {project['files_seen']} | Keyword hits: {project['keyword_hits']}"
            )
            lines.append(f"- Flags: {json.dumps(project['flags'], ensure_ascii=True)}")
            for rec in project["recommendations"]:
                lines.append(f"- Recommendation: {rec}")
            lines.append("")
    else:
        lines.append("- No project opportunities identified.")
        lines.append("")

    md_path.write_text("\n".join(lines), encoding="utf-8")

    print(f"[done] JSON report: {json_path}")
    print(f"[done] Markdown summary: {md_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
