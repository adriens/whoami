"""Fetch YouTube channel playlists metadata to markdown."""

import argparse
import csv
import json
import re
import unicodedata
from pathlib import Path

import yt_dlp

DATA_DIR = Path("data/youtube")

CHANNELS = {
    "devops-lab": "https://www.youtube.com/@devopslabs2812",
}


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    return text[:80].strip("-")


def fetch_playlists(channel_url: str) -> list[dict]:
    playlists_url = channel_url.rstrip("/") + "/playlists"
    ydl_opts = {
        "quiet": True,
        "extract_flat": True,
        "ignoreerrors": True,
        "no_warnings": True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(playlists_url, download=False) or {}

    results = []
    for entry in info.get("entries", []):
        if not entry:
            continue
        results.append({
            "id": entry.get("id", ""),
            "title": entry.get("title", ""),
            "url": entry.get("url") or f"https://www.youtube.com/playlist?list={entry.get('id','')}",
            "video_count": entry.get("playlist_count") or entry.get("video_count") or 0,
            "description": entry.get("description") or "",
        })
    return results


def fetch_playlist_detail(playlist_id: str) -> dict:
    url = f"https://www.youtube.com/playlist?list={playlist_id}"
    ydl_opts = {
        "quiet": True,
        "extract_flat": True,
        "ignoreerrors": True,
        "no_warnings": True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False) or {}
    video_ids = [e["id"] for e in info.get("entries", []) if e and e.get("id")]
    return {
        "id": info.get("id", playlist_id),
        "title": info.get("title", ""),
        "url": url,
        "description": info.get("description") or "",
        "video_count": len(video_ids),
        "video_ids": video_ids,
    }


def write_playlist(playlists_dir: Path, pl: dict):
    slug = slugify(pl["title"])
    video_ids_yaml = "\n".join(f"  - {v}" for v in pl.get("video_ids", []))

    content = f"""---
id: "{pl['id']}"
slug: {slug}
title: "{pl['title'].replace('"', "'")}"
url: "{pl['url']}"
video_count: {pl['video_count']}
---

{pl.get('description', '')}

## Videos ({pl['video_count']})

{video_ids_yaml}
"""
    (playlists_dir / f"{slug}.md").write_text(content, encoding="utf-8")
    return slug


def write_index(channel_dir: Path, playlists: list[dict]):
    fields = ["id", "slug", "title", "url", "video_count"]
    with open(channel_dir / "_playlists_index.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(playlists)


def main():
    parser = argparse.ArgumentParser(description="Fetch YouTube channel playlists to markdown")
    parser.add_argument("--channel", required=True, choices=list(CHANNELS))
    args = parser.parse_args()

    channel_url = CHANNELS[args.channel]
    channel_dir = DATA_DIR / args.channel
    playlists_dir = channel_dir / "playlists"
    playlists_dir.mkdir(parents=True, exist_ok=True)

    print(f"Fetching playlists for channel '{args.channel}'...")
    playlists = fetch_playlists(channel_url)
    print(f"Found {len(playlists)} playlist(s). Fetching details...")

    enriched = []
    for i, pl in enumerate(playlists, 1):
        print(f"  [{i}/{len(playlists)}] {pl['title'][:60]}")
        detail = fetch_playlist_detail(pl["id"])
        slug = write_playlist(playlists_dir, detail)
        enriched.append({**detail, "slug": slug})
        print(f"    {detail['video_count']} videos → {slug}.md")

    write_index(channel_dir, enriched)
    print(f"Done. {len(enriched)} playlist(s) in {channel_dir}/playlists/")


if __name__ == "__main__":
    main()
