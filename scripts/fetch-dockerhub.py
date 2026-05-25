"""Fetch Docker Hub public repositories for a given username."""

import argparse
import csv
import json
import time
import unicodedata
import re
from pathlib import Path

import requests

DOCKERHUB_API = "https://hub.docker.com/v2"
DATA_DIR = Path("data/dockerhub")


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    return text[:80].strip("-")


def fetch_repositories(username: str) -> list[dict]:
    repos = []
    url = f"{DOCKERHUB_API}/repositories/{username}/?page_size=100"
    while url:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        repos.extend(data.get("results", []))
        url = data.get("next")
        if url:
            time.sleep(0.3)
    return [r for r in repos if not r.get("is_private", False)]


def fetch_tags(username: str, repo_name: str) -> list[str]:
    url = f"{DOCKERHUB_API}/repositories/{username}/{repo_name}/tags?page_size=10"
    resp = requests.get(url, timeout=10)
    if resp.status_code != 200:
        return []
    return [t["name"] for t in resp.json().get("results", [])]


def write_image(images_dir: Path, repo: dict, tags: list[str]):
    name = repo["name"]
    slug = slugify(name)
    last_updated = (repo.get("last_updated") or "")[:10]

    lines = [
        "---",
        f'slug: {slug}',
        f'name: "{name}"',
        f'url: "https://hub.docker.com/r/{repo["namespace"]}/{name}"',
        f'description: "{(repo.get("description") or "").replace(chr(34), chr(39))}"',
        f'last_updated: "{last_updated}"',
        f'pull_count: {repo.get("pull_count", 0)}',
        f'star_count: {repo.get("star_count", 0)}',
        f'tags: [{", ".join(tags)}]',
        "---",
        "",
        repo.get("description") or "",
        "",
    ]
    (images_dir / f"{slug}.md").write_text("\n".join(lines), encoding="utf-8")


def write_index(user_dir: Path, repos: list[dict]):
    fields = ["slug", "name", "url", "description", "last_updated", "pull_count", "star_count"]
    with open(user_dir / "_index.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for r in repos:
            name = r["name"]
            writer.writerow({
                "slug": slugify(name),
                "name": name,
                "url": f"https://hub.docker.com/r/{r['namespace']}/{name}",
                "description": r.get("description") or "",
                "last_updated": (r.get("last_updated") or "")[:10],
                "pull_count": r.get("pull_count", 0),
                "star_count": r.get("star_count", 0),
            })


def write_stats(user_dir: Path, username: str, repos: list[dict]):
    total_pulls = sum(r.get("pull_count", 0) for r in repos)
    stats = {
        "username": username,
        "profile_url": f"https://hub.docker.com/u/{username}",
        "image_count": len(repos),
        "total_pulls": total_pulls,
        "last_fetched": __import__("datetime").date.today().isoformat(),
    }
    (user_dir / "_stats.json").write_text(
        json.dumps(stats, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"  total pulls: {total_pulls}")


def main():
    parser = argparse.ArgumentParser(description="Fetch Docker Hub public images to markdown")
    parser.add_argument("--user", required=True, help="Docker Hub username")
    args = parser.parse_args()

    username = args.user
    user_dir = DATA_DIR / username
    images_dir = user_dir / "images"
    images_dir.mkdir(parents=True, exist_ok=True)

    print(f"Fetching repositories for @{username}...")
    repos = fetch_repositories(username)
    repos.sort(key=lambda r: r.get("pull_count", 0), reverse=True)
    print(f"Found {len(repos)} public image(s).")

    for i, repo in enumerate(repos, 1):
        name = repo["name"]
        pulls = repo.get("pull_count", 0)
        print(f"  [{i}/{len(repos)}] {name} ({pulls} pulls)")
        tags = fetch_tags(username, name)
        time.sleep(0.2)
        write_image(images_dir, repo, tags)

    print("Writing _index.csv and _stats.json...")
    write_index(user_dir, repos)
    write_stats(user_dir, username, repos)
    print(f"Done. Data in {user_dir}/")


if __name__ == "__main__":
    main()
