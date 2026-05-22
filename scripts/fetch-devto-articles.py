import argparse
import csv
import time
import unicodedata
import re
from pathlib import Path

import requests
import yaml

DEVTO_API = "https://dev.to/api"
DATA_DIR = Path("data/dev_to")


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    return text[:80].strip("-")


def load_existing_ids(user_dir: Path) -> set[str]:
    index_path = user_dir / "_index.csv"
    if not index_path.exists():
        return set()
    with open(index_path, encoding="utf-8") as f:
        return {row["id"] for row in csv.DictReader(f)}


def fetch_articles(username: str, author_filter: str | None = None) -> list[dict]:
    articles = []
    page = 1
    while True:
        resp = requests.get(
            f"{DEVTO_API}/articles",
            params={"username": username, "per_page": 30, "page": page},
            timeout=10,
        )
        resp.raise_for_status()
        batch = resp.json()
        if not batch:
            break
        if author_filter:
            batch = [a for a in batch if a.get("user", {}).get("username") == author_filter]
        articles.extend(batch)
        print(f"  page {page} — {len(batch)} articles")
        page += 1
        time.sleep(0.5)
    return articles


def fetch_body(article_id: int) -> str:
    resp = requests.get(f"{DEVTO_API}/articles/{article_id}", timeout=10)
    resp.raise_for_status()
    return resp.json().get("body_markdown", "")


def is_dev_challenge(article: dict) -> bool:
    has_tag = "devchallenge" in article.get("tag_list", [])
    has_desc = (article.get("description") or "").startswith("This is a submission for")
    return has_tag or has_desc


def article_filename(article: dict) -> str:
    date = (article.get("published_at") or "0000-00-00")[:10]
    return f"{date}-{slugify(article['slug'])}.md"


def write_article(articles_dir: Path, article: dict):
    body = fetch_body(article["id"])
    time.sleep(0.3)

    frontmatter = {
        "id": article["id"],
        "title": article["title"],
        "url": article["url"],
        "published_at": article.get("published_at", ""),
        "tags": article.get("tag_list", []),
        "reactions": article.get("public_reactions_count", 0),
        "comments": article.get("comments_count", 0),
        "reading_time_minutes": article.get("reading_time_minutes", 0),
        "is_dev_challenge": is_dev_challenge(article),
    }

    with open(articles_dir / article_filename(article), "w", encoding="utf-8") as f:
        f.write("---\n")
        yaml.dump(frontmatter, f, allow_unicode=True, default_flow_style=False)
        f.write("---\n\n")
        f.write(body)


def write_index(user_dir: Path, articles: list[dict]):
    fields = ["id", "title", "url", "published_at", "tags", "reactions", "comments", "reading_time_minutes", "is_dev_challenge"]
    with open(user_dir / "_index.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for a in articles:
            writer.writerow({
                "id": a["id"],
                "title": a["title"],
                "url": a["url"],
                "published_at": a.get("published_at", ""),
                "tags": ",".join(a.get("tag_list", [])),
                "reactions": a.get("public_reactions_count", 0),
                "comments": a.get("comments_count", 0),
                "reading_time_minutes": a.get("reading_time_minutes", 0),
                "is_dev_challenge": is_dev_challenge(a),
            })


def main():
    parser = argparse.ArgumentParser(description="Fetch DEV.to articles to markdown")
    parser.add_argument("--user", required=True, help="DEV.to username ou organisation")
    parser.add_argument("--author", default=None, help="Filtrer par auteur (username)")
    args = parser.parse_args()

    username = args.user
    user_dir = DATA_DIR / username
    articles_dir = user_dir / "articles"
    articles_dir.mkdir(parents=True, exist_ok=True)

    existing_ids = load_existing_ids(user_dir)
    print(f"Fetching articles for @{username}{f' (auteur: {args.author})' if args.author else ''}...")
    articles = fetch_articles(username, author_filter=args.author)
    print(f"Total : {len(articles)} articles ({len(existing_ids)} déjà présents)")

    print("Writing _index.csv...")
    write_index(user_dir, articles)

    new_articles = [a for a in articles if str(a["id"]) not in existing_ids]
    print(f"Fetching {len(new_articles)} nouveaux articles...")
    for i, article in enumerate(new_articles, 1):
        print(f"  [{i}/{len(new_articles)}] {article['title'][:70]}")
        write_article(articles_dir, article)

    print(f"Done. Data in {user_dir}/")


if __name__ == "__main__":
    main()
