#!/usr/bin/env python3
"""
scrape_linkedin.py

Collects recent LinkedIn posts for the 10 configured experts and saves each as a
dated Markdown file under research/linkedin-posts/<expert-slug>/.

Design goals (in order):
1. Look like a real human session — reuse the user's actual Chrome profile via
   Chrome DevTools Protocol attach (NOT a fresh headless browser), so cookies,
   fingerprint, extensions, and session history are identical to their real use.
2. Low footprint — randomized delays, small scroll increments, reading pauses,
   caps per profile, longer breaks between profiles, session ceiling.
3. Rerun-safe — if a post file already exists by permalink hash, skip it.

CAVEAT: any automated access to LinkedIn is against their ToS. This script tries
to minimize detectable bot-behavior signals, but cannot eliminate them. Use at
your own risk. Keep volume low; stop if you see any friction (captcha,
challenge, rate-limit page).

Setup (see scripts/SCRAPING.md for the step-by-step):
1. Close all Chrome windows.
2. Launch Chrome with remote debugging, e.g. on Windows PowerShell:
       & "C:/Program Files/Google/Chrome/Application/chrome.exe" `
         --remote-debugging-port=9222 `
         --user-data-dir="$env:LOCALAPPDATA/Google/Chrome/User Data"
   (on macOS:
       /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
         --remote-debugging-port=9222 \
         --user-data-dir="$HOME/Library/Application Support/Google/Chrome"
   )
3. In that Chrome, log into LinkedIn as you normally do. Browse for 30 sec.
4. In a terminal:
       pip install -r scripts/requirements.txt
       python -m playwright install chromium   # only if first time
       python scripts/scrape_linkedin.py               # all experts
       python scripts/scrape_linkedin.py bay braun     # specific slugs

Defaults (tune in the CONFIG block below):
- Max 18 posts per expert.
- 4-9s randomized delay after each post capture.
- 60-180s delay between experts.
- Hard cap: 3 experts per run (then stop; rerun later to continue).
"""

from __future__ import annotations

import hashlib
import json
import random
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

try:
    from playwright.sync_api import sync_playwright, Page, TimeoutError as PWTimeout
except ImportError:
    print(
        "[error] playwright not installed.\n"
        "        pip install -r scripts/requirements.txt\n"
        "        python -m playwright install chromium",
        file=sys.stderr,
    )
    sys.exit(1)


# ---------------------------------------------------------------------------
# CONFIG
# ---------------------------------------------------------------------------
EXPERTS: Dict[str, Dict[str, str]] = {
    "bay":      {"handle": "jasondbay",   "name": "Jason Bay"},
    "braun":    {"handle": "josh-braun",  "name": "Josh Braun"},
    "mahrle":   {"handle": "outboundsales","name": "Jed Mahrle"},
    "tatulea":  {"handle": "florintatulea","name": "Florin Tatulea"},
    "allred":   {"handle": "williamallred","name": "Will Allred"},
    "venetz":   {"handle": "leslievenetz", "name": "Leslie Venetz"},
    "ingram":   {"handle": "morganjingram","name": "Morgan Ingram"},
    "cegelski": {"handle": "nickcegelski", "name": "Nick Cegelski"},
    "farrokh":  {"handle": "armand-farrokh","name": "Armand Farrokh"},
    "coleman":  {"handle": "kyletcoleman","name": "Kyle Coleman"},
}

CDP_URL              = "http://localhost:9222"
MAX_POSTS_PER_EXPERT = 18
EXPERTS_PER_RUN      = 3          # hard cap — stop after this many then exit
DELAY_POST_SECS      = (4, 9)     # random range after capturing each post
DELAY_SCROLL_SECS    = (1.5, 3.5) # random range between small scrolls
DELAY_PROFILE_SECS   = (60, 180)  # random range between experts
READ_PAUSE_SECS      = (3, 7)     # pretend-to-read pause when a profile loads

ROOT = Path(__file__).resolve().parent.parent
OUT_BASE = ROOT / "research" / "linkedin-posts"


def log(msg: str) -> None:
    ts = datetime.now().strftime("%H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)


def human_sleep(bounds: tuple) -> None:
    time.sleep(random.uniform(*bounds))


def safe_slug(text: str, maxlen: int = 60) -> str:
    text = (text or "").lower().strip()
    text = re.sub(r"[^a-z0-9\- ]+", "", text)
    text = re.sub(r"\s+", "-", text)
    return text[:maxlen] or "post"


def post_id_from_urn(urn: str) -> str:
    # urn like urn:li:activity:7123456789012345678
    m = re.search(r"activity[-:](\d+)", urn or "")
    return m.group(1) if m else hashlib.sha1((urn or "").encode()).hexdigest()[:16]


def already_have(out_dir: Path, activity_id: str) -> bool:
    if not out_dir.exists():
        return False
    for p in out_dir.glob("*.md"):
        if activity_id in p.name:
            return True
    return False


def natural_scroll(page: Page) -> None:
    """Scroll in small increments (300-600px) with small pauses — mimics reading."""
    increments = random.randint(3, 6)
    for _ in range(increments):
        px = random.randint(300, 650)
        page.mouse.wheel(0, px)
        human_sleep(DELAY_SCROLL_SECS)


def extract_visible_posts(page: Page) -> List[Dict]:
    """Pull all currently-rendered post nodes from the feed."""
    js = r"""
    () => {
      const posts = [];
      const containers = document.querySelectorAll('div.feed-shared-update-v2, div[data-urn^="urn:li:activity"]');
      containers.forEach(el => {
        const urn = el.getAttribute('data-urn') || '';
        // Body text: prefer .update-components-text, else the main content block
        const textEl = el.querySelector('.update-components-text, .feed-shared-inline-show-more-text');
        const text = textEl ? textEl.innerText.trim() : '';
        // Date stamp (absolute timestamp not always present; relative text like "2d •" is)
        const timeEl = el.querySelector('.update-components-actor__sub-description, time');
        const when = timeEl ? timeEl.innerText.trim().split('\n')[0] : '';
        // Reactions
        const reactionsEl = el.querySelector('.social-details-social-counts__reactions-count, span.social-details-social-counts__reactions-count');
        const reactions = reactionsEl ? reactionsEl.innerText.trim() : '';
        // Comments
        const commentsEl = el.querySelector('.social-details-social-counts__comments');
        const comments = commentsEl ? commentsEl.innerText.trim() : '';
        if (urn && text) posts.push({urn, text, when, reactions, comments});
      });
      return posts;
    }
    """
    return page.evaluate(js)


def approx_date_from_relative(rel: str) -> str:
    """'2d • Edited' -> YYYY-MM-DD (today minus 2 days). Falls back to today."""
    now = datetime.utcnow()
    m = re.match(r"\s*(\d+)\s*(mo|w|d|h|m|s|yr)", rel.lower())
    if not m:
        return now.strftime("%Y-%m-%d")
    n = int(m.group(1))
    unit = m.group(2)
    days = {"yr": 365, "mo": 30, "w": 7, "d": 1, "h": 0, "m": 0, "s": 0}.get(unit, 0) * n
    from datetime import timedelta
    return (now - timedelta(days=days)).strftime("%Y-%m-%d")


def save_post(out_dir: Path, expert_name: str, expert_handle: str, p: Dict) -> Optional[Path]:
    activity_id = post_id_from_urn(p.get("urn", ""))
    if already_have(out_dir, activity_id):
        return None
    date = approx_date_from_relative(p.get("when", ""))
    text = p.get("text", "").strip()
    first_line = text.split("\n", 1)[0][:50] if text else "post"
    fname = f"{date}-{activity_id}-{safe_slug(first_line)}.md"
    fpath = out_dir / fname
    permalink = f"https://www.linkedin.com/feed/update/urn:li:activity:{activity_id}/"
    front = (
        f"---\n"
        f"author: {expert_name}\n"
        f"handle: {expert_handle}\n"
        f"url: {permalink}\n"
        f"date_estimated: {date}\n"
        f"date_relative_seen: \"{p.get('when','')}\"\n"
        f"reactions: \"{p.get('reactions','')}\"\n"
        f"comments: \"{p.get('comments','')}\"\n"
        f"collected: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}\n"
        f"---\n\n"
    )
    fpath.write_text(front + text + "\n\n## Notes\n- \n", encoding="utf-8")
    return fpath


def collect_expert(page: Page, slug: str, info: Dict[str, str]) -> int:
    out_dir = OUT_BASE / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    url = f"https://www.linkedin.com/in/{info['handle']}/recent-activity/all/"
    log(f"{slug}: navigating to {url}")
    try:
        page.goto(url, wait_until="domcontentloaded", timeout=30_000)
    except PWTimeout:
        log(f"{slug}: page load timed out; moving on")
        return 0

    # Detect bot-check / challenge page early
    content = (page.content() or "")[:5000].lower()
    if ("security verification" in content
            or "/checkpoint/challenge" in page.url
            or "unusual activity" in content):
        log(f"{slug}: LinkedIn showed a challenge/verification — aborting this run")
        return 0

    human_sleep(READ_PAUSE_SECS)  # pretend to read the profile header

    seen_urns: set = set()
    collected: List[Dict] = []
    stagnation = 0
    while len(collected) < MAX_POSTS_PER_EXPERT and stagnation < 3:
        batch = extract_visible_posts(page)
        new = [p for p in batch if p["urn"] not in seen_urns]
        for p in new:
            seen_urns.add(p["urn"])
            collected.append(p)
            if len(collected) >= MAX_POSTS_PER_EXPERT:
                break
        if not new:
            stagnation += 1
        else:
            stagnation = 0
        natural_scroll(page)

    log(f"{slug}: collected {len(collected)} visible post(s); writing files")
    saved = 0
    for p in collected:
        path = save_post(out_dir, info["name"], info["handle"], p)
        if path:
            saved += 1
            log(f"  -> {path.relative_to(ROOT)}")
        human_sleep(DELAY_POST_SECS)
    return saved


def main(argv: List[str]) -> int:
    slugs = argv[1:] if len(argv) > 1 else list(EXPERTS.keys())
    unknown = [s for s in slugs if s not in EXPERTS]
    if unknown:
        print(f"[error] unknown slug(s): {unknown}", file=sys.stderr)
        print(f"        available: {', '.join(EXPERTS)}", file=sys.stderr)
        return 2

    log(f"connecting to Chrome at {CDP_URL} (make sure it's running with --remote-debugging-port=9222)")
    with sync_playwright() as pw:
        try:
            browser = pw.chromium.connect_over_cdp(CDP_URL)
        except Exception as exc:
            log(f"could not attach to Chrome: {exc}")
            log("start Chrome with --remote-debugging-port=9222 and try again; see scripts/SCRAPING.md")
            return 1

        context = browser.contexts[0] if browser.contexts else browser.new_context()
        page = context.new_page()

        total = 0
        for i, slug in enumerate(slugs):
            if i >= EXPERTS_PER_RUN:
                log(f"hit EXPERTS_PER_RUN={EXPERTS_PER_RUN}; stopping. Rerun to continue.")
                break
            info = EXPERTS[slug]
            log(f"=== expert {i+1}/{min(len(slugs), EXPERTS_PER_RUN)}: {slug} ({info['name']}) ===")
            try:
                total += collect_expert(page, slug, info)
            except Exception as exc:
                log(f"{slug}: unhandled error {exc!r}; moving on")
            # session break before next expert
            if i + 1 < min(len(slugs), EXPERTS_PER_RUN):
                pause = random.uniform(*DELAY_PROFILE_SECS)
                log(f"sleeping {pause:.0f}s before next expert...")
                time.sleep(pause)

        try:
            page.close()
        except Exception:
            pass
        log(f"done. {total} new post file(s) written.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
