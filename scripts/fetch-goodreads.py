import argparse
import csv
import json
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


def load_scraped(path: Path) -> list[dict]:
    """Charge un export JSON scrapé depuis l'étagère Goodreads (navigateur connecté).

    Goodreads a coupé les flux RSS (404 depuis ~oct. 2026) : l'étagère n'est plus
    lisible qu'en session authentifiée. Voir data/goodreads/README.md.
    """
    books = json.loads(path.read_text(encoding="utf-8"))
    return [{
        "id": str(b["id"]),
        "title": b["title"],
        "author": b["author"],
        # même format d'URL qu'à l'époque du RSS, pour ne pas bruiter les diffs
        "url": f"https://www.goodreads.com/review/show/{b['reviewId']}?utm_medium=api&utm_source=rss",
        "isbn": b.get("isbn", ""),
        "rating": b.get("rating", ""),
        "average_rating": b.get("average_rating", ""),
        "num_pages": b.get("num_pages", ""),
        "date_read": b.get("date_read", ""),
        "date_added": b.get("date_added", ""),
        "published_year": b.get("published_year", ""),
        "shelf": "read",
        "review": (b.get("review") or "").strip(),
        "description": "",
    } for b in books]


def read_existing(path: Path) -> tuple[list | None, str]:
    """Récupère les enrichissements manuels d'un fichier livre existant.

    Le fetch réécrit le fichier à chaque run, il faut donc préserver explicitement :
    - les tags (taxonomie thématique, enrichissement manuel) ;
    - le corps, pour pouvoir conserver une review saisie à la main tant que le
      RSS Goodreads ne l'expose pas encore (délai de synchro après écriture).
    """
    if not path.exists():
        return None, ""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None, ""
    if not text.startswith("---"):
        return None, ""
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, ""
    body = parts[2].strip()
    try:
        fm = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        return None, body
    tags = fm.get("tags")
    return (tags if isinstance(tags, list) else None), body


def write_book(books_dir: Path, book: dict):
    date = book["date_read"] or book["date_added"] or "0000-00-00"
    filename = f"{date}-{slugify(book['title'] or book['id'])}.md"
    path = books_dir / filename
    existing_tags, existing_body = read_existing(path)

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
        "tags": existing_tags or [],
    }

    with open(path, "w", encoding="utf-8") as f:
        f.write("---\n")
        yaml.dump(frontmatter, f, allow_unicode=True, default_flow_style=False)
        f.write("---\n\n")
        if book["review"]:
            f.write(book["review"])
        elif existing_body and existing_body != book["description"]:
            # Review saisie à la main, pas encore exposée par le RSS : on la garde
            f.write(existing_body)
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
    parser.add_argument("--from-json", type=Path, help="Export JSON scrapé (au lieu du RSS)")
    args = parser.parse_args()

    user_dir = DATA_DIR / args.user
    books_dir = user_dir / "books"
    books_dir.mkdir(parents=True, exist_ok=True)

    if args.from_json:
        print(f"Loading Goodreads books from {args.from_json}...")
        books = load_scraped(args.from_json)
    else:
        print(f"Fetching Goodreads books for user {args.user}...")
        books = [extract_book(e) for e in fetch_books(args.user)]
    print(f"Total : {len(books)} livres")
    if not books:
        # RSS vide = Goodreads injoignable/bloquant (ex. IP runner CI) — ne pas écraser l'index
        print("WARNING: flux RSS vide — données existantes conservées")
        return

    print("Writing _index.csv...")
    write_index(user_dir, books)

    print("Writing markdown files...")
    for i, book in enumerate(books, 1):
        print(f"  [{i}/{len(books)}] {book['title'][:70]}")
        write_book(books_dir, book)

    print(f"Done. Data in {user_dir}/")


if __name__ == "__main__":
    main()
