import argparse
import csv
import re
import time
from pathlib import Path

import feedparser
import yaml

DATA_DIR = Path("data/goodreads")
RSS_URL = "https://www.goodreads.com/review/list_rss/{user_id}?shelf=read&per_page=200&page={page}"


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    return text[:80].strip("-")


def parse_date(value: str | None) -> str:
    if not value:
        return ""
    # feedparser renvoie des dates au format "Mon, 01 Jan 2024 00:00:00 +0000"
    # on extrait juste YYYY-MM-DD
    import email.utils
    try:
        parsed = email.utils.parsedate(value)
        if parsed:
            return f"{parsed[0]:04d}-{parsed[1]:02d}-{parsed[2]:02d}"
    except Exception:
        pass
    return value[:10] if len(value) >= 10 else value


def fetch_books(user_id: str) -> list[dict]:
    books = []
    page = 1
    while True:
        url = RSS_URL.format(user_id=user_id, page=page)
        feed = feedparser.parse(url)
        entries = feed.entries
        if not entries:
            break
        print(f"  page {page} — {len(entries)} livres")
        books.extend(entries)
        if len(entries) < 200:
            break
        page += 1
        time.sleep(1)
    return books


def extract_book(entry: dict) -> dict:
    return {
        "id": str(entry.get("book_id", "")),
        "title": entry.get("title", ""),
        "author": entry.get("author_name", entry.get("author", "")),
        "url": entry.get("link", ""),
        "isbn": entry.get("isbn", ""),
        "rating": entry.get("user_rating", ""),
        "average_rating": entry.get("average_rating", ""),
        "num_pages": entry.get("num_pages", ""),
        "date_read": parse_date(entry.get("user_read_at", "")),
        "date_added": parse_date(entry.get("user_date_added", "")),
        "published_year": entry.get("book_published", ""),
        "shelf": "read",
        "review": (entry.get("user_review") or "").strip(),
        "description": (entry.get("book_description") or "").strip(),
    }


def read_existing_tags(path: Path) -> list | None:
    """Récupère les tags manuels d'un fichier livre existant.

    Les tags sont une enrichissement manuel (taxonomie thématique) : le fetch
    réécrit le fichier à chaque run, il faut donc les préserver explicitement.
    """
    if not path.exists():
        return None
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    try:
        fm = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        return None
    tags = fm.get("tags")
    return tags if isinstance(tags, list) else None


def write_book(books_dir: Path, book: dict):
    date = book["date_read"] or book["date_added"] or "0000-00-00"
    filename = f"{date}-{slugify(book['title'] or book['id'])}.md"
    path = books_dir / filename

    frontmatter = {
        "id": book["id"],
        "title": book["title"],
        "author": book["author"],
        "url": book["url"],
        "isbn": book["isbn"],
        "rating": book["rating"],
        "average_rating": book["average_rating"],
        "num_pages": book["num_pages"],
        "date_read": book["date_read"],
        "published_year": book["published_year"],
        "shelf": book["shelf"],
        "tags": read_existing_tags(path) or [],
    }

    with open(path, "w", encoding="utf-8") as f:
        f.write("---\n")
        yaml.dump(frontmatter, f, allow_unicode=True, default_flow_style=False)
        f.write("---\n\n")
        if book["review"]:
            f.write(book["review"])
        elif book["description"]:
            f.write(book["description"])


def write_index(user_dir: Path, books: list[dict]):
    fields = ["id", "title", "author", "url", "isbn", "rating", "average_rating",
              "num_pages", "date_read", "published_year", "shelf"]
    with open(user_dir / "_index.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for b in books:
            writer.writerow({k: b[k] for k in fields})


def main():
    parser = argparse.ArgumentParser(description="Fetch Goodreads books to markdown")
    parser.add_argument("--user", required=True, help="Goodreads user ID (numerique)")
    args = parser.parse_args()

    user_dir = DATA_DIR / args.user
    books_dir = user_dir / "books"
    books_dir.mkdir(parents=True, exist_ok=True)

    print(f"Fetching Goodreads books for user {args.user}...")
    entries = fetch_books(args.user)
    books = [extract_book(e) for e in entries]
    print(f"Total : {len(books)} livres")

    print("Writing _index.csv...")
    write_index(user_dir, books)

    print("Writing markdown files...")
    for i, book in enumerate(books, 1):
        print(f"  [{i}/{len(books)}] {book['title'][:70]}")
        write_book(books_dir, book)

    print(f"Done. Data in {user_dir}/")


if __name__ == "__main__":
    main()
