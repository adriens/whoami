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
    index_path = user_dir / "_notebooks_index.csv"
    if not index_path.exists():
        return set()
    with open(index_path, encoding="utf-8") as f:
        return {row["ref"] for row in csv.DictReader(f)}


def write_notebook(notebooks_dir: Path, k: object):
    slug = slugify(k.title or k.ref.split("/")[-1])
    filename = f"{slug}.md"
    last_run = str(getattr(k, "last_run_time", "") or "")[:10]

    frontmatter = {
        "ref": k.ref,
        "title": k.title or "",
        "url": f"https://www.kaggle.com/code/{k.ref}",
        "last_run": last_run,
        "language": getattr(k, "language", "") or "",
        "kernel_type": getattr(k, "kernel_type", "") or "",
        "total_votes": getattr(k, "total_votes", 0),
    }

    with open(notebooks_dir / filename, "w", encoding="utf-8") as f:
        f.write("---\n")
        yaml.dump(frontmatter, f, allow_unicode=True, default_flow_style=False)
        f.write("---\n\n")


def append_index_row(index_path: Path, k: object, write_header: bool):
    fields = ["ref", "title", "url", "last_run", "language", "kernel_type", "total_votes"]
    last_run = str(getattr(k, "last_run_time", "") or "")[:10]

    with open(index_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        if write_header:
            writer.writeheader()
        writer.writerow({
            "ref": k.ref,
            "title": k.title or "",
            "url": f"https://www.kaggle.com/code/{k.ref}",
            "last_run": last_run,
            "language": getattr(k, "language", "") or "",
            "kernel_type": getattr(k, "kernel_type", "") or "",
            "total_votes": getattr(k, "total_votes", 0),
        })


def main():
    parser = argparse.ArgumentParser(description="Fetch Kaggle notebooks to markdown")
    parser.add_argument("--user", required=True, help="Kaggle username")
    args = parser.parse_args()

    if not os.environ.get("KAGGLE_USERNAME"):
        os.environ.setdefault("KAGGLE_CONFIG_DIR", str(Path.home() / ".kaggle"))

    from kaggle.api.kaggle_api_extended import KaggleApi
    api = KaggleApi()
    api.authenticate()

    user_dir = DATA_DIR / args.user
    notebooks_dir = user_dir / "notebooks"
    notebooks_dir.mkdir(parents=True, exist_ok=True)

    existing_refs = load_existing_refs(user_dir)
    index_path = user_dir / "_notebooks_index.csv"
    first_row = not index_path.exists()

    print(f"Fetching notebooks for {args.user}...")
    all_notebooks = api.kernels_list(user=args.user)
    new_notebooks = [k for k in all_notebooks if k.ref not in existing_refs]
    print(f"Total : {len(all_notebooks)} notebooks ({len(existing_refs)} déjà présents, {len(new_notebooks)} nouveaux)")

    for i, k in enumerate(new_notebooks, 1):
        print(f"  [{i}/{len(new_notebooks)}] {(k.title or '')[:70]}")
        write_notebook(notebooks_dir, k)
        append_index_row(index_path, k, write_header=first_row)
        first_row = False

    print(f"Done. Data in {user_dir}/")


if __name__ == "__main__":
    main()
