#!/usr/bin/env python3
"""
Validate all internal markdown links in the documentation.

This script checks:
1. All .md files that are referenced in links
2. Relative paths resolve correctly
3. No double parentheses in links
"""

import os
import re
from pathlib import Path
from urllib.parse import urljoin

# Base configuration
DOCS_DIR = Path("docs")
BASEURL = "/oh-my-claude-sisyphus-docs"

# Jekyll permalink:pretty means file.md becomes file/
def md_to_url(md_path: str, base_dir: str = "") -> str:
    """Convert a .md file path to its Jekyll URL."""
    # Remove .md extension
    if md_path.endswith(".md"):
        md_path = md_path[:-3]
    # Add trailing slash for directories
    if not md_path.endswith("/"):
        md_path += "/"
    return urljoin(BASEURL + base_dir + "/", md_path)

def resolve_relative_link(link: str, source_file: Path) -> str:
    """Resolve a relative link to its absolute path."""
    source_dir = source_file.parent
    if link.startswith("../"):
        # Count how many ../ to navigate up
        parts = link.split("/")
        up_count = sum(1 for p in parts if p == "..")
        # Go up from source_dir
        target = source_dir
        for _ in range(up_count):
            target = target.parent
        # Add the remaining path parts
        remaining = [p for p in parts if p != ".." and p != ""]
        for part in remaining:
            target = target / part
        return target
    elif link.startswith("/"):
        # Absolute path from docs/
        return DOCS_DIR / link[1:]
    else:
        # Same directory
        return source_dir / link

def extract_links_from_file(file_path: Path) -> list:
    """Extract all markdown links from a file."""
    links = []
    content = file_path.read_text()

    # Match [text](url) format
    pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    for match in re.finditer(pattern, content):
        text, url = match.groups()
        # Skip external links and anchors
        if url.startswith("http") or url.startswith("#"):
            continue
        links.append({"text": text, "url": url, "line": content[:match.start()].count('\n') + 1})
    return links

def get_all_md_files() -> dict:
    """Get all .md files in docs directory."""
    md_files = {}
    for md_file in DOCS_DIR.rglob("*.md"):
        # Store relative path from docs/
        rel_path = md_file.relative_to(DOCS_DIR)
        md_files[str(rel_path)] = md_file
    return md_files

def validate_links():
    """Main validation function."""
    all_md_files = get_all_md_files()
    errors = []
    warnings = []

    print(f"Found {len(all_md_files)} markdown files")

    for rel_path, file_path in all_md_files.items():
        links = extract_links_from_file(file_path)

        for link in links:
            url = link["url"]

            # Check for double parentheses
            if url.startswith("(("):
                errors.append({
                    "file": rel_path,
                    "line": link["line"],
                    "link": link["text"],
                    "url": url,
                    "issue": "Double parentheses in URL"
                })
                continue

            # Check for .md in URL (should use directory path with permalink:pretty)
            if url.endswith(".md"):
                warnings.append({
                    "file": rel_path,
                    "line": link["line"],
                    "link": link["text"],
                    "url": url,
                    "issue": ".md in URL (should use /path/ format)"
                })
                # Check if the file exists
                target = resolve_relative_link(url, file_path)
                if not target.exists():
                    errors.append({
                        "file": rel_path,
                        "line": link["line"],
                        "link": link["text"],
                        "url": url,
                        "issue": f"Target file not found: {target}"
                    })
                continue

            # Check for relative paths without .md
            if "/" in url or url.startswith("../"):
                # Convert URL to expected file path
                # /path/ -> path.md
                # ../path/ -> go up, then path.md
                if url.startswith("/"):
                    # Absolute from docs root
                    check_path = url.strip("/") + ".md"
                elif url.startswith("../"):
                    # Relative - resolve it
                    check_path = resolve_relative_link(url + "index.md", file_path)
                else:
                    # Same directory
                    check_path = file_path.parent / (url + ".md")

                # Normalize
                if isinstance(check_path, Path):
                    try:
                        check_path = check_path.relative_to(DOCS_DIR)
                    except ValueError:
                        # Path is outside docs, try to resolve it
                        check_path = check_path.relative_to(check_path.anchor)
                    check_path = str(check_path)

                # Special case: index.md or overview files
                if check_path.endswith("/index.md"):
                    check_path = check_path[:-9]  # Remove /index.md
                if check_path.endswith("/index"):
                    check_path = check_path[:-6]

                # Check if file exists
                resolved = DOCS_DIR / check_path
                if not resolved.exists():
                    # Try with .md
                    if not resolved.with_suffix(".md").exists():
                        errors.append({
                            "file": rel_path,
                            "line": link["line"],
                            "link": link["text"],
                            "url": url,
                            "issue": f"Target not found: {check_path}"
                        })

    # Print results
    print("\n" + "="*60)
    print("VALIDATION RESULTS")
    print("="*60)

    if errors:
        print(f"\n❌ ERRORS: {len(errors)}")
        for e in errors:
            print(f"  {e['file']}:{e['line']}")
            print(f"    [{e['link']}]({e['url']})")
            print(f"    Issue: {e['issue']}\n")
    else:
        print("\n✅ No errors found!")

    if warnings:
        print(f"\n⚠️  WARNINGS: {len(warnings)}")
        for w in warnings:
            print(f"  {w['file']}:{w['line']}")
            print(f"    [{w['link']}]({w['url']})")
            print(f"    Issue: {w['issue']}\n")
    else:
        print("\n✅ No warnings!")

    return len(errors) == 0

if __name__ == "__main__":
    os.chdir(Path(__file__).parent.parent)
    success = validate_links()
    exit(0 if success else 1)
