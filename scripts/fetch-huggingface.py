import argparse
import csv
import re
import unicodedata
from pathlib import Path

import yaml

DATA_DIR = Path("data/huggingface")


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    return text[:80].strip("-")


def load_existing_ids(index_path: Path) -> set[str]:
    if not index_path.exists():
        return set()
    with open(index_path, encoding="utf-8") as f:
        return {row["id"] for row in csv.DictReader(f)}


def isodate(val) -> str:
    return str(val or "")[:10]


# ── Datasets ──────────────────────────────────────────────────────────────────

def write_dataset(datasets_dir: Path, d):
    slug = slugify(d.id.split("/")[-1])
    tags = [str(t) for t in (getattr(d, "tags", []) or [])]
    frontmatter = {
        "id": d.id,
        "author": getattr(d, "author", "") or "",
        "url": f"https://huggingface.co/datasets/{d.id}",
        "downloads": getattr(d, "downloads", 0) or 0,
        "likes": getattr(d, "likes", 0) or 0,
        "last_modified": isodate(getattr(d, "last_modified", "")),
        "tags": tags,
    }
    with open(datasets_dir / f"{slug}.md", "w", encoding="utf-8") as f:
        f.write("---\n")
        yaml.dump(frontmatter, f, allow_unicode=True, default_flow_style=False)
        f.write("---\n\n")
        desc = getattr(d, "description", "") or ""
        if desc:
            f.write(desc)


def append_dataset_row(index_path: Path, d, write_header: bool):
    fields = ["id", "author", "url", "downloads", "likes", "last_modified", "tags"]
    tags = ",".join(str(t) for t in (getattr(d, "tags", []) or []))
    with open(index_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        if write_header:
            writer.writeheader()
        writer.writerow({
            "id": d.id,
            "author": getattr(d, "author", "") or "",
            "url": f"https://huggingface.co/datasets/{d.id}",
            "downloads": getattr(d, "downloads", 0) or 0,
            "likes": getattr(d, "likes", 0) or 0,
            "last_modified": isodate(getattr(d, "last_modified", "")),
            "tags": tags,
        })


# ── Spaces ────────────────────────────────────────────────────────────────────

def write_space(spaces_dir: Path, s):
    slug = slugify(s.id.split("/")[-1])
    tags = [str(t) for t in (getattr(s, "tags", []) or [])]
    sdk = ""
    for t in tags:
        if t.lower() in ("gradio", "streamlit", "docker", "static"):
            sdk = t.lower()
            break
    frontmatter = {
        "id": s.id,
        "author": getattr(s, "author", "") or "",
        "url": f"https://huggingface.co/spaces/{s.id}",
        "sdk": sdk,
        "likes": getattr(s, "likes", 0) or 0,
        "last_modified": isodate(getattr(s, "last_modified", "")),
        "tags": tags,
    }
    with open(spaces_dir / f"{slug}.md", "w", encoding="utf-8") as f:
        f.write("---\n")
        yaml.dump(frontmatter, f, allow_unicode=True, default_flow_style=False)
        f.write("---\n\n")


def append_space_row(index_path: Path, s, write_header: bool):
    fields = ["id", "author", "url", "sdk", "likes", "last_modified", "tags"]
    tags = [str(t) for t in (getattr(s, "tags", []) or [])]
    sdk = ""
    for t in tags:
        if t.lower() in ("gradio", "streamlit", "docker", "static"):
            sdk = t.lower()
            break
    with open(index_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        if write_header:
            writer.writeheader()
        writer.writerow({
            "id": s.id,
            "author": getattr(s, "author", "") or "",
            "url": f"https://huggingface.co/spaces/{s.id}",
            "sdk": sdk,
            "likes": getattr(s, "likes", 0) or 0,
            "last_modified": isodate(getattr(s, "last_modified", "")),
            "tags": ",".join(tags),
        })


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Fetch HuggingFace datasets and spaces")
    parser.add_argument("--author", required=True, help="HuggingFace username or org")
    args = parser.parse_args()

    from huggingface_hub import list_datasets, list_spaces

    author_dir = DATA_DIR / args.author
    datasets_dir = author_dir / "datasets"
    spaces_dir = author_dir / "spaces"
    datasets_dir.mkdir(parents=True, exist_ok=True)
    spaces_dir.mkdir(parents=True, exist_ok=True)

    # Datasets
    ds_index = author_dir / "_datasets_index.csv"
    existing_ds = load_existing_ids(ds_index)
    print(f"Fetching datasets for {args.author}...")
    all_datasets = list(list_datasets(author=args.author))
    new_datasets = [d for d in all_datasets if d.id not in existing_ds]
    print(f"  {len(all_datasets)} datasets ({len(existing_ds)} déjà présents, {len(new_datasets)} nouveaux)")
    first = not ds_index.exists()
    for i, d in enumerate(new_datasets, 1):
        print(f"  [{i}/{len(new_datasets)}] {d.id}")
        write_dataset(datasets_dir, d)
        append_dataset_row(ds_index, d, write_header=first)
        first = False

    # Spaces
    sp_index = author_dir / "_spaces_index.csv"
    existing_sp = load_existing_ids(sp_index)
    print(f"Fetching spaces for {args.author}...")
    all_spaces = list(list_spaces(author=args.author))
    new_spaces = [s for s in all_spaces if s.id not in existing_sp]
    print(f"  {len(all_spaces)} spaces ({len(existing_sp)} déjà présents, {len(new_spaces)} nouveaux)")
    first = not sp_index.exists()
    for i, s in enumerate(new_spaces, 1):
        print(f"  [{i}/{len(new_spaces)}] {s.id}")
        write_space(spaces_dir, s)
        append_space_row(sp_index, s, write_header=first)
        first = False

    print(f"Done. Data in {author_dir}/")


if __name__ == "__main__":
    main()
