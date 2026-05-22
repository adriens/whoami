import argparse
import csv
import re
import unicodedata
from pathlib import Path

import yaml
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


def load_existing_ids(channel_dir: Path) -> set[str]:
    index_path = channel_dir / "_index.csv"
    if not index_path.exists():
        return set()
    with open(index_path, encoding="utf-8") as f:
        return {row["id"] for row in csv.DictReader(f)}


def list_video_ids(channel_url: str) -> list[str]:
    videos_url = channel_url.rstrip("/") + "/videos"
    ydl_opts = {"quiet": True, "extract_flat": True, "ignoreerrors": True, "no_warnings": True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(videos_url, download=False)
        entries = info.get("entries", [])
        ids = []
        for e in entries:
            if not e:
                continue
            if e.get("_type") == "playlist":
                ids.extend(v["id"] for v in e.get("entries", []) if v)
            else:
                ids.append(e["id"])
        return ids


def fetch_video(video_id: str) -> dict | None:
    ydl_opts = {"quiet": True, "ignoreerrors": True, "no_warnings": True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        return ydl.extract_info(f"https://youtu.be/{video_id}", download=False)


def format_date(upload_date: str | None) -> str:
    d = upload_date or "00000000"
    return f"{d[:4]}-{d[4:6]}-{d[6:]}" if len(d) == 8 else "0000-00-00"


def write_video(videos_dir: Path, video: dict):
    date_fmt = format_date(video.get("upload_date"))
    filename = f"{date_fmt}-{slugify(video.get('title', video['id']))}.md"

    frontmatter = {
        "id": video["id"],
        "title": video.get("title", ""),
        "url": f"https://youtu.be/{video['id']}",
        "published_at": date_fmt,
        "duration_seconds": video.get("duration"),
        "views": video.get("view_count"),
        "likes": video.get("like_count"),
        "tags": video.get("tags", []),
    }

    with open(videos_dir / filename, "w", encoding="utf-8") as f:
        f.write("---\n")
        yaml.dump(frontmatter, f, allow_unicode=True, default_flow_style=False)
        f.write("---\n\n")
        f.write(video.get("description") or "")


def append_index_row(index_path: Path, video: dict, write_header: bool):
    fields = ["id", "title", "url", "published_at", "duration_seconds", "views", "likes", "tags"]
    date_fmt = format_date(video.get("upload_date"))
    with open(index_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        if write_header:
            writer.writeheader()
        writer.writerow({
            "id": video["id"],
            "title": video.get("title", ""),
            "url": f"https://youtu.be/{video['id']}",
            "published_at": date_fmt,
            "duration_seconds": video.get("duration"),
            "views": video.get("view_count"),
            "likes": video.get("like_count"),
            "tags": ",".join(video.get("tags", [])),
        })


def main():
    parser = argparse.ArgumentParser(description="Fetch YouTube channel videos to markdown")
    parser.add_argument("--channel", required=True, choices=list(CHANNELS), help="Channel name")
    args = parser.parse_args()

    channel_url = CHANNELS[args.channel]
    channel_dir = DATA_DIR / args.channel
    videos_dir = channel_dir / "videos"
    videos_dir.mkdir(parents=True, exist_ok=True)

    existing_ids = load_existing_ids(channel_dir)
    index_path = channel_dir / "_index.csv"
    first_row = not index_path.exists()

    print(f"Listing videos from {args.channel}...")
    video_ids = list_video_ids(channel_url)
    new_ids = [vid_id for vid_id in video_ids if vid_id not in existing_ids]
    print(f"Total : {len(video_ids)} videos ({len(existing_ids)} déjà présents, {len(new_ids)} nouveaux)")

    for i, vid_id in enumerate(new_ids, 1):
        video = fetch_video(vid_id)
        if not video:
            print(f"  [{i}/{len(new_ids)}] SKIP {vid_id}")
            continue
        print(f"  [{i}/{len(new_ids)}] {(video.get('title') or '')[:70]}")
        write_video(videos_dir, video)
        append_index_row(index_path, video, write_header=first_row)
        first_row = False

    print(f"Done. Data in {channel_dir}/")


if __name__ == "__main__":
    main()
