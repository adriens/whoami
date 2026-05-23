import argparse
import csv
import os
import re
import unicodedata
from pathlib import Path

import yaml

DATA_DIR = Path("data/kaggle")


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    return text[:80].strip("-")


def load_existing_refs(user_dir: Path) -> set[str]:
    index_path = user_dir / "_index.csv"
    if not index_path.exists():
        return set()
    with open(index_path, encoding="utf-8") as f:
        return {row["ref"] for row in csv.DictReader(f)}


def format_tags(tags: list) -> list[str]:
    if not tags:
        return []
    return [t["name"] if isinstance(t, dict) else str(t) for t in tags]


def write_dataset(datasets_dir: Path, d: object):
    slug = slugify(d.title or d.ref.split("/")[-1])
    filename = f"{slug}.md"

    tags = format_tags(getattr(d, "tags", []) or [])
    last_updated = str(getattr(d, "last_updated", "") or "")[:10]

    frontmatter = {
        "ref": d.ref,
        "title": d.title or "",
        "url": f"https://www.kaggle.com/datasets/{d.ref}",
        "last_updated": last_updated,
        "download_count": getattr(d, "download_count", 0),
        "vote_count": getattr(d, "vote_count", 0),
        "view_count": getattr(d, "view_count", 0),
        "total_bytes": getattr(d, "total_bytes", 0),
        "license_name": getattr(d, "license_name", ""),
        "tags": tags,
    }

    with open(datasets_dir / filename, "w", encoding="utf-8") as f:
        f.write("---\n")
        yaml.dump(frontmatter, f, allow_unicode=True, default_flow_style=False)
        f.write("---\n\n")
        subtitle = getattr(d, "subtitle", "") or ""
        description = getattr(d, "description", "") or ""
        if subtitle:
            f.write(f"{subtitle}\n\n")
        if description:
            f.write(description)


def append_index_row(index_path: Path, d: object, write_header: bool):
    fields = ["ref", "title", "url", "last_updated", "download_count", "vote_count", "view_count", "total_bytes", "license_name", "tags"]
    tags = ",".join(format_tags(getattr(d, "tags", []) or []))
    last_updated = str(getattr(d, "last_updated", "") or "")[:10]

    with open(index_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        if write_header:
            writer.writeheader()
        writer.writerow({
            "ref": d.ref,
            "title": d.title or "",
            "url": f"https://www.kaggle.com/datasets/{d.ref}",
            "last_updated": last_updated,
            "download_count": getattr(d, "download_count", 0),
            "vote_count": getattr(d, "vote_count", 0),
            "view_count": getattr(d, "view_count", 0),
            "total_bytes": getattr(d, "total_bytes", 0),
            "license_name": getattr(d, "license_name", ""),
            "tags": tags,
        })


def main():
    parser = argparse.ArgumentParser(description="Fetch Kaggle datasets to markdown")
    parser.add_argument("--user", required=True, help="Kaggle username")
    args = parser.parse_args()

    # En CI : KAGGLE_USERNAME + KAGGLE_KEY via env vars
    # En local : ~/.kaggle/kaggle.json
    if not os.environ.get("KAGGLE_USERNAME"):
        os.environ.setdefault("KAGGLE_CONFIG_DIR", str(Path.home() / ".kaggle"))

    from kaggle.api.kaggle_api_extended import KaggleApi
    api = KaggleApi()
    api.authenticate()

    user_dir = DATA_DIR / args.user
    datasets_dir = user_dir / "datasets"
    datasets_dir.mkdir(parents=True, exist_ok=True)

    existing_refs = load_existing_refs(user_dir)
    index_path = user_dir / "_index.csv"
    first_row = not index_path.exists()

    print(f"Fetching datasets for {args.user}...")
    all_datasets = api.dataset_list(user=args.user)
    new_datasets = [d for d in all_datasets if d.ref not in existing_refs]
    print(f"Total : {len(all_datasets)} datasets ({len(existing_refs)} déjà présents, {len(new_datasets)} nouveaux)")

    for i, d in enumerate(new_datasets, 1):
        print(f"  [{i}/{len(new_datasets)}] {d.title[:70]} ({getattr(d, 'download_count', 0)} dl)")
        write_dataset(datasets_dir, d)
        append_index_row(index_path, d, write_header=first_row)
        first_row = False

    print(f"Done. Data in {user_dir}/")


if __name__ == "__main__":
    main()
