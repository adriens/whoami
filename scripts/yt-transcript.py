"""Fetch and print the transcript of a YouTube video.

Usage:
    uv run --with youtube-transcript-api scripts/yt-transcript.py <video_id_or_url>

Examples:
    uv run --with youtube-transcript-api scripts/yt-transcript.py _mW8nXVJAoQ
    uv run --with youtube-transcript-api scripts/yt-transcript.py https://youtu.be/_mW8nXVJAoQ
"""

import sys
import re
from youtube_transcript_api import YouTubeTranscriptApi


def extract_video_id(arg: str) -> str:
    match = re.search(r"(?:v=|youtu\.be/)([A-Za-z0-9_-]{11})", arg)
    return match.group(1) if match else arg


def main():
    if len(sys.argv) < 2:
        print("Usage: uv run --with youtube-transcript-api scripts/yt-transcript.py <video_id_or_url>")
        sys.exit(1)

    video_id = extract_video_id(sys.argv[1])
    api = YouTubeTranscriptApi()
    transcript = api.fetch(video_id, languages=["fr", "en"])
    for entry in transcript:
        print(entry.text)


if __name__ == "__main__":
    main()
