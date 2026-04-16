#!/usr/bin/env python3
"""
fetch_youtube_transcripts.py

Automatically fetches the latest N uploads from each configured YouTube channel
and pulls transcripts for them. No API key needed.

How it works:
1. For each channel, resolve its @handle to a channel ID by scraping the channel
   page once (only if a handle is given; you can also pre-set a channel ID).
2. Parse that channel's public RSS feed
   (https://www.youtube.com/feeds/videos.xml?channel_id=<ID>) to list the latest
   15 videos. If RSS returns zero entries (YouTube occasionally throttles the
   feed endpoint), fall back to scraping the channel /videos page.
3. For each of the most recent MAX_PER_CHANNEL videos, fetch the transcript via
   youtube-transcript-api and save as a dated Markdown file under
   research/youtube-transcripts/<slug>/.

Usage:
    pip install -r scripts/requirements.txt
    python scripts/fetch_youtube_transcripts.py              # all channels
    python scripts/fetch_youtube_transcripts.py 30mpc        # one channel

Rerun-safe: already-downloaded transcripts are skipped (tracked by video ID).
"""

from __future__ import annotations

import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Set

try:
    import feedparser
    import requests
    from youtube_transcript_api import (
        YouTubeTranscriptApi,
        TranscriptsDisabled,
        NoTranscriptFound,
        VideoUnavailable,
    )
except ImportError:
    print(
        "[error] Missing dependencies. Run: pip install -r scripts/requirements.txt",
        file=sys.stderr,
    )
    sys.exit(1)


CHANNELS: Dict[str, Dict[str, str]] = {
    "josh-braun":     {"handle": "@JoshBraun",     "channel_id": "UCBaTLnzqEInlHdC0N364aHw"},
    "morgan-ingram":  {"handle": "@MorganJIngram", "channel_id": "UCnhg__lkPcrdr2zqLu5kwUQ"},
    "venetz":         {"handle": "@LeslieVenetz",  "channel_id": "UCE8h2Dq5pHlaF69Y6dB-HsA"},
    "30mpc":          {"handle": "@30mpc",         "channel_id": "UCku-dqryeYBuzh_0xVKPExw"},
}

MAX_PER_CHANNEL = 8

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "research" / "youtube-transcripts"
UA = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}


def slugify(text: str) -> str:
    text = (text or "").lower().strip()
    text = re.sub(r"[^a-z0-9\- ]+", "", text)
    text = re.sub(r"\s+", "-", text)
    return text[:60] or "untitled"


def resolve_channel_id(handle_or_id: str) -> str:
    if handle_or_id.startswith("UC") and len(handle_or_id) >= 20:
        return handle_or_id
    handle = handle_or_id if handle_or_id.startswith("@") else f"@{handle_or_id}"
    url = f"https://www.youtube.com/{handle}"
    resp = requests.get(url, headers=UA, timeout=15)
    resp.raise_for_status()
    m = re.search(r'"channelId":"(UC[A-Za-z0-9_\-]{20,})"', resp.text)
    if not m:
        raise RuntimeError(f"Could not resolve channel ID for {handle}")
    return m.group(1)


def list_recent_videos(channel_id: str, limit: int) -> List[dict]:
    feed_url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
    # Fetch the RSS XML ourselves with a real browser UA — feedparser's default
    # UA gets 0 entries back from YouTube. Parse the bytes directly.
    try:
        resp = requests.get(feed_url, headers=UA, timeout=15)
        resp.raise_for_status()
        feed = feedparser.parse(resp.content)
    except Exception:
        feed = feedparser.parse(feed_url)
    out: List[dict] = []
    for entry in feed.entries[:limit]:
        vid = getattr(entry, "yt_videoid", None) or entry.id.split(":")[-1]
        published = (getattr(entry, "published", "") or "")[:10] or \
            datetime.utcnow().strftime("%Y-%m-%d")
        out.append({"id": vid, "title": entry.title, "published": published})

    # Fallback: scrape the channel /videos page for recent upload IDs. Used
    # when YouTube throttles the RSS feed or returns an empty feed.
    if not out:
        try:
            page = requests.get(
                f"https://www.youtube.com/channel/{channel_id}/videos",
                headers=UA, timeout=15,
            )
            page.raise_for_status()
            seen: Set[str] = set()
            for m in re.finditer(r'"videoId":"([A-Za-z0-9_\-]{11})"', page.text):
                vid = m.group(1)
                if vid in seen:
                    continue
                seen.add(vid)
                tm = re.search(
                    rf'"videoId":"{vid}".*?"text":"([^"]+)"', page.text, re.S,
                )
                title = tm.group(1) if tm else vid
                out.append({
                    "id": vid,
                    "title": title,
                    "published": datetime.utcnow().strftime("%Y-%m-%d"),
                })
                if len(out) >= limit:
                    break
        except Exception as exc:
            print(f"        [warn] channel page fallback failed: {exc}")
    return out


def format_transcript(entries: List[dict]) -> str:
    lines: List[str] = []
    last_stamp = -60
    for e in entries:
        start = int(e.get("start", 0))
        text = (e.get("text") or "").replace("\n", " ").strip()
        if not text:
            continue
        if start - last_stamp >= 30:
            mm, ss = divmod(start, 60)
            lines.append(f"\n[{mm:02d}:{ss:02d}] {text}")
            last_stamp = start
        else:
            lines.append(text)
    return " ".join(lines).strip()


def existing_ids_in(channel_dir: Path) -> Set[str]:
    ids: Set[str] = set()
    if not channel_dir.exists():
        return ids
    for p in channel_dir.glob("*.md"):
        parts = p.stem.split("-")
        if len(parts) >= 4:
            ids.add(parts[3])
    return ids


def fetch_transcript(video_id: str) -> Optional[List[dict]]:
    try:
        if hasattr(YouTubeTranscriptApi, "get_transcript"):
            return YouTubeTranscriptApi.get_transcript(
                video_id, languages=["en", "en-US", "en-GB"]
            )
        api = YouTubeTranscriptApi()
        result = api.fetch(video_id, languages=["en", "en-US", "en-GB"])
        out: List[dict] = []
        for snip in result:
            out.append({
                "start": getattr(snip, "start", 0.0),
                "duration": getattr(snip, "duration", 0.0),
                "text": getattr(snip, "text", ""),
            })
        return out
    except (TranscriptsDisabled, NoTranscriptFound, VideoUnavailable):
        return None
    except Exception as exc:
        print(f"        [err] {video_id}: {exc!r}")
        return None


def write_transcript_file(channel_slug: str, video: dict, body: str) -> Path:
    channel_dir = OUT_DIR / channel_slug
    channel_dir.mkdir(parents=True, exist_ok=True)
    date = video.get("published") or datetime.utcnow().strftime("%Y-%m-%d")
    title_slug = slugify(video.get("title") or video["id"])
    fname = f"{date}-{video['id']}-{title_slug}.md"
    path = channel_dir / fname
    front = (
        f"---\n"
        f"channel: {channel_slug}\n"
        f"video_id: {video['id']}\n"
        f"url: https://www.youtube.com/watch?v={video['id']}\n"
        f"title: \"{(video.get('title') or '').strip()}\"\n"
        f"published: {date}\n"
        f"fetched: {datetime.utcnow().strftime('%Y-%m-%d')}\n"
        f"---\n\n# Transcript\n\n"
    )
    path.write_text(front + body + "\n", encoding="utf-8")
    return path


def process_channel(slug: str, cfg: dict) -> int:
    handle_or_id = cfg.get("channel_id") or cfg.get("handle")
    if not handle_or_id:
        print(f"[skip] {slug}: no handle or channel_id configured")
        return 0
    print(f"\n=== {slug} ({handle_or_id}) ===")
    try:
        channel_id = resolve_channel_id(handle_or_id)
    except Exception as exc:
        print(f"[err ] {slug}: could not resolve channel ID: {exc}")
        return 0

    videos = list_recent_videos(channel_id, MAX_PER_CHANNEL)
    if not videos:
        print(f"[note] {slug}: RSS and fallback both returned 0 entries")
        return 0

    already = existing_ids_in(OUT_DIR / slug)
    count = 0
    for v in videos:
        if v["id"] in already:
            print(f"[ skip ] {v['id']} already downloaded")
            continue
        print(f"[fetch] {v['published']} {v['id']} -- {v['title'][:70]}")
        entries = fetch_transcript(v["id"])
        if not entries:
            print(f"        [miss] no transcript available")
            continue
        body = format_transcript(entries)
        path = write_transcript_file(slug, v, body)
        print(f"        [ ok ] -> {path.relative_to(ROOT)}  ({len(entries)} segments)")
        count += 1
    return count


def main() -> int:
    only = sys.argv[1] if len(sys.argv) > 1 else None
    if only and only not in CHANNELS:
        print(f"[error] unknown channel: {only}", file=sys.stderr)
        print(f"        available: {', '.join(sorted(CHANNELS))}", file=sys.stderr)
        return 2

    total = 0
    for slug, cfg in CHANNELS.items():
        if only and slug != only:
            continue
        total += process_channel(slug, cfg)
    print(f"\nDone. Saved {total} new transcript(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
