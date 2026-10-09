"""Fetch YouTube transcripts for every video of a channel index.

Writes one plain-text file per video into <data_dir>/transcripts/<id>.txt and
records videos without transcript in transcripts/_unavailable.csv. Already
fetched (or known unavailable) videos are skipped, so the script can be
re-run to resume. Stops cleanly when YouTube rate-limits the IP (IpBlocked).

Usage:
    uv run scripts/fetch-youtube-transcripts.py [--data-dir data/youtube/devops-lab] [--delay 15]
"""

import argparse
import csv
import time
from pathlib import Path

from youtube_transcript_api import YouTubeTranscriptApi


def main():
    parser = argparse.ArgumentParser(description="Fetch YouTube transcripts (resumable)")
    parser.add_argument("--data-dir", default="data/youtube/devops-lab")
    parser.add_argument("--delay", type=float, default=15, help="seconds between requests")
    args = parser.parse_args()

    data_dir = Path(args.data_dir)
    out = data_dir / "transcripts"
    out.mkdir(parents=True, exist_ok=True)
    unavailable_csv = out / "_unavailable.csv"
    unavailable = {}
    if unavailable_csv.exists():
        unavailable = {r["id"]: r["reason"] for r in csv.DictReader(open(unavailable_csv, encoding="utf-8"))}

    rows = list(csv.DictReader(open(data_dir / "_index.csv", encoding="utf-8")))
    todo = [r for r in rows if not (out / f"{r['id']}.txt").exists() and r["id"] not in unavailable]
    print(f"{len(rows)} videos, {len(todo)} to fetch")

    api = YouTubeTranscriptApi()
    ok = 0
    for i, r in enumerate(todo, 1):
        vid = r["id"]
        try:
            transcript = api.fetch(vid, languages=["fr", "en"])
            (out / f"{vid}.txt").write_text(" ".join(e.text for e in transcript) + "\n", encoding="utf-8")
            ok += 1
        except Exception as e:
            name = type(e).__name__
            if "Block" in name or "TooMany" in name:
                print(f"Rate-limited by YouTube ({name}) after {ok} transcripts — re-run later to resume.")
                break
            unavailable[vid] = name
        print(f"{i}/{len(todo)} ok={ok} unavailable={len(unavailable)}", flush=True)
        time.sleep(args.delay)

    with open(unavailable_csv, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id", "reason"])
        w.writerows(sorted(unavailable.items()))
    done = len(list(out.glob("*.txt")))
    print(f"✓ {done}/{len(rows)} transcripts in {out} ({len(unavailable)} unavailable)")


if __name__ == "__main__":
    main()
