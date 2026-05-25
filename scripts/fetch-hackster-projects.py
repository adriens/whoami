"""Fetch Hackster.io projects for a given username via Algolia + HTML scraping."""

import argparse
import csv
import json
import re
import time
import unicodedata
from html import unescape
from pathlib import Path

import requests

# Algolia credentials embedded in every Hackster.io page
ALGOLIA_APP_ID = "7YQJT9BHUX"
ALGOLIA_SEARCH_KEY = "c113f0569e873258342405ddf4a4dd09"
ALGOLIA_USER_INDEX = "hackster_production_user"
ALGOLIA_PROJECT_INDEX = "hackster_production_project"
ALGOLIA_BASE = f"https://{ALGOLIA_APP_ID}-dsn.algolia.net/1/indexes"

HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0"}
ALGOLIA_HEADERS = {
    "X-Algolia-Application-Id": ALGOLIA_APP_ID,
    "X-Algolia-API-Key": ALGOLIA_SEARCH_KEY,
    "Content-Type": "application/json",
}

DATA_DIR = Path("data/hackster")


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    return text[:80].strip("-")


def algolia_query(index: str, body: dict) -> dict:
    resp = requests.post(
        f"{ALGOLIA_BASE}/{index}/query",
        headers=ALGOLIA_HEADERS,
        json=body,
        timeout=10,
    )
    resp.raise_for_status()
    return resp.json()


def fetch_user_data(username: str) -> dict:
    """Get user profile + project list with tags from Algolia user index."""
    data = algolia_query(ALGOLIA_USER_INDEX, {"query": username, "hitsPerPage": 5})
    for hit in data.get("hits", []):
        if hit.get("user_name") == username:
            return hit
    return {}


def fetch_project_algolia(project_name: str, author_username: str) -> dict | None:
    """Search Algolia project index and return the hit matching the author."""
    data = algolia_query(ALGOLIA_PROJECT_INDEX, {"query": project_name, "hitsPerPage": 10})
    for hit in data.get("hits", []):
        authors = [a.get("user_name") for a in hit.get("authors", [])]
        if author_username in authors:
            return hit
    return None


def fetch_published_at(project_url: str) -> str:
    """Scrape the project page to extract the datePublished value."""
    resp = requests.get(project_url, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    m = re.search(r'datePublished["\s>]+([A-Za-z]+ +\d+, \d{4})', resp.text)
    if m:
        from datetime import datetime
        try:
            dt = datetime.strptime(m.group(1).strip(), "%B %d, %Y")
            return dt.strftime("%Y-%m-%d")
        except ValueError:
            pass
    return ""


def write_project(projects_dir: Path, project: dict, tags: list[str], published_at: str):
    name = project["name"]
    date = published_at or "0000-00-00"
    slug = f"{date}-{slugify(name)}"
    url = f"https://www.hackster.io{project['url']}"
    authors = [a["user_name"] for a in project.get("authors", [])]

    frontmatter = {
        "id": project["id"],
        "slug": slug,
        "name": name,
        "url": url,
        "published_at": date,
        "pitch": project.get("pitch", ""),
        "difficulty": project.get("difficulty", ""),
        "content_type": project.get("content_type", []),
        "respects": project.get("respects_count", 0),
        "impressions": project.get("impressions_count", 0),
        "tags": tags,
        "authors": authors,
    }

    filepath = projects_dir / f"{slug}.md"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("---\n")
        for k, v in frontmatter.items():
            if isinstance(v, list):
                f.write(f"{k}: [{', '.join(str(i) for i in v)}]\n")
            else:
                safe = str(v).replace('"', '\\"')
                f.write(f'{k}: "{safe}"\n')
        f.write("---\n\n")
        f.write(project.get("pitch", "") + "\n")

    return slug, frontmatter


def write_index(user_dir: Path, rows: list[dict]):
    fields = ["slug", "name", "url", "published_at", "difficulty", "content_type", "respects", "impressions", "tags", "authors"]
    with open(user_dir / "_index.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({
                **row,
                "tags": ",".join(row.get("tags", [])),
                "authors": ",".join(row.get("authors", [])),
                "content_type": ",".join(row.get("content_type", [])),
            })


def write_stats(user_dir: Path, user_data: dict, username: str, project_count: int):
    stats = {
        "username": username,
        "profile_url": f"https://www.hackster.io/{username}",
        "projects_count": project_count,
        "followers_count": user_data.get("followers_count", 0),
        "respects_count": sum(int(v) for v in [user_data.get("respects_count", 0)]),
        "last_fetched": __import__("datetime").date.today().isoformat(),
    }
    (user_dir / "_stats.json").write_text(json.dumps(stats, indent=2, ensure_ascii=False), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Fetch Hackster.io projects to markdown")
    parser.add_argument("--user", required=True, help="Hackster.io username")
    args = parser.parse_args()

    username = args.user
    user_dir = DATA_DIR / username
    projects_dir = user_dir / "projects"
    projects_dir.mkdir(parents=True, exist_ok=True)

    print(f"Fetching user data for @{username}...")
    user_data = fetch_user_data(username)
    if not user_data:
        print(f"User '{username}' not found in Algolia index.")
        return

    raw_projects = user_data.get("projects", [])
    print(f"Found {len(raw_projects)} project(s) in user index.")

    rows = []
    existing_ids = set()
    index_path = user_dir / "_index.csv"
    if index_path.exists():
        with open(index_path, encoding="utf-8") as f:
            existing_ids = {row["slug"] for row in csv.DictReader(f)}

    for raw in raw_projects:
        name = raw["name"]
        tags = raw.get("tags", [])
        print(f"\n  Project: {name}")

        project = fetch_project_algolia(name, username)
        if not project:
            print(f"    [skip] not found in project index for author @{username}")
            continue

        time.sleep(0.3)
        project_url = f"https://www.hackster.io{project['url']}"
        print(f"    url: {project_url}")
        print(f"    fetching published_at from HTML...")
        published_at = fetch_published_at(project_url)
        print(f"    published_at: {published_at or '(not found)'}")
        time.sleep(0.5)

        slug, meta = write_project(projects_dir, project, tags, published_at)
        rows.append(meta)
        print(f"    written: {slug}.md")

    print("\nWriting _index.csv...")
    write_index(user_dir, rows)
    write_stats(user_dir, user_data, username, len(rows))
    print(f"Done. {len(rows)} project(s) in {user_dir}/")


if __name__ == "__main__":
    main()
