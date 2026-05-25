"""Fetch PyPI package metadata for a given list of packages."""

import argparse
import csv
import json
import time
import unicodedata
import re
from pathlib import Path

import requests

PYPI_API = "https://pypi.org/pypi"
DATA_DIR = Path("data/pypi")


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    return text[:80].strip("-")


def fetch_package(name: str) -> dict:
    resp = requests.get(f"{PYPI_API}/{name}/json", timeout=10)
    resp.raise_for_status()
    return resp.json()


def write_package(packages_dir: Path, data: dict):
    info = data["info"]
    name = info["name"]
    slug = slugify(name)
    version = info["version"]
    released_at = ""
    releases = data.get("releases", {})
    if version in releases and releases[version]:
        released_at = releases[version][0].get("upload_time", "")[:10]

    keywords = [k.strip() for k in (info.get("keywords") or "").split(",") if k.strip()]
    classifiers = info.get("classifiers", [])

    lines = [
        "---",
        f'slug: {slug}',
        f'name: "{name}"',
        f'version: "{version}"',
        f'url: "https://pypi.org/project/{name}/"',
        f'summary: "{(info.get("summary") or "").replace(chr(34), chr(39))}"',
        f'author: "{info.get("author") or info.get("author_email") or ""}"',
        f'license: "{info.get("license") or ""}"',
        f'released_at: "{released_at}"',
        f'requires_python: "{info.get("requires_python") or ""}"',
        f'home_page: "{info.get("home_page") or (info.get("project_urls") or {}).get("Homepage", "")}"',
        f'keywords: [{", ".join(keywords)}]',
        "---",
        "",
        info.get("summary") or "",
        "",
    ]
    (packages_dir / f"{slug}.md").write_text("\n".join(lines), encoding="utf-8")
    return {
        "slug": slug,
        "name": name,
        "version": version,
        "url": f"https://pypi.org/project/{name}/",
        "summary": info.get("summary") or "",
        "released_at": released_at,
        "requires_python": info.get("requires_python") or "",
        "keywords": ",".join(keywords),
    }


def write_index(user_dir: Path, rows: list[dict]):
    fields = ["slug", "name", "version", "url", "summary", "released_at", "requires_python", "keywords"]
    with open(user_dir / "_index.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_stats(user_dir: Path, username: str, rows: list[dict]):
    stats = {
        "username": username,
        "profile_url": f"https://pypi.org/user/{username}/",
        "package_count": len(rows),
        "packages": [r["name"] for r in rows],
        "last_fetched": __import__("datetime").date.today().isoformat(),
    }
    (user_dir / "_stats.json").write_text(
        json.dumps(stats, indent=2, ensure_ascii=False), encoding="utf-8"
    )


def main():
    parser = argparse.ArgumentParser(description="Fetch PyPI package metadata to markdown")
    parser.add_argument("--user", required=True, help="PyPI username (for folder naming)")
    parser.add_argument("--packages", required=True, nargs="+", help="PyPI package names to fetch")
    args = parser.parse_args()

    username = args.user
    user_dir = DATA_DIR / username
    packages_dir = user_dir / "packages"
    packages_dir.mkdir(parents=True, exist_ok=True)

    rows = []
    for i, pkg in enumerate(args.packages, 1):
        print(f"  [{i}/{len(args.packages)}] Fetching {pkg}...")
        data = fetch_package(pkg)
        row = write_package(packages_dir, data)
        rows.append(row)
        print(f"    version: {row['version']} — {row['summary'][:60]}")
        time.sleep(0.3)

    print("Writing _index.csv and _stats.json...")
    write_index(user_dir, rows)
    write_stats(user_dir, username, rows)
    print(f"Done. {len(rows)} package(s) in {user_dir}/")


if __name__ == "__main__":
    main()
