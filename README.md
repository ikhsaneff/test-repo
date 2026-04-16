# Cold Outreach Pipeline for B2B SaaS

A curated research base of 10 practitioners building and teaching cold outreach for B2B SaaS. The goal is to collect enough primary material to support a real, opinionated playbook instead of another generic guide.

## Why this topic

Of the eight options, cold outreach pipeline for B2B SaaS has the highest density of practitioners who publish in public: people running agencies, leading sales teams, or shipping product, who share teardown-level detail rather than surface-level thought leadership. The space is also mature enough to have clearly differentiated schools of thought: Braun's "poke the bear", Bay's multi-threaded sequences, Lavender's data-driven copy rules, Tatulea's signal-based outbound. That makes a comparative playbook genuinely useful.

## Why these 10 experts

Selection filter, applied in order:

1. Practitioner, not pundit. Runs an outbound team, agency, or product where their advice is tested weekly.
2. Publishes frequently in the last 6 to 12 months.
3. Differentiated POV, not just "personalize more".
4. Shares receipts: numbers, scripts, teardowns.

Final list: Jason Bay, Josh Braun, Jed Mahrle, Florin Tatulea, Will Allred, Leslie Venetz, Morgan Ingram, Nick Cegelski, Armand Farrokh, Kyle Coleman. Full rationale and verified recent content in [`research/sources.md`](research/sources.md).

## Where each expert actually publishes

Earlier drafts of this project assumed YouTube was the primary video channel for all 10 experts. It isn't. Most publish primarily on LinkedIn, with a podcast or newsletter as secondary. The collection strategy reflects that.

| Expert            | Primary        | Secondary        | Automation                        |
|-------------------|----------------|------------------|-----------------------------------|
| Jason Bay         | Podcast        | LinkedIn         | `scrape_linkedin.py` (podcast out of scope) |
| Josh Braun        | LinkedIn       | Newsletter, YT   | `scrape_linkedin.py`              |
| Jed Mahrle        | Newsletter     | LinkedIn         | `scrape_linkedin.py`              |
| Florin Tatulea    | LinkedIn       | Common Room blog | `scrape_linkedin.py`              |
| Will Allred       | LinkedIn       | Lavender blog    | `scrape_linkedin.py` + manual     |
| Leslie Venetz     | LinkedIn       | Book, YT         | `scrape_linkedin.py` + `fetch_youtube_transcripts.py` |
| Morgan Ingram     | YouTube        | LinkedIn         | `fetch_youtube_transcripts.py`    |
| Nick Cegelski     | Podcast        | LinkedIn, YT     | `scrape_linkedin.py` + `fetch_youtube_transcripts.py` (podcast out of scope) |
| Armand Farrokh    | Podcast        | LinkedIn         | `scrape_linkedin.py` (podcast out of scope) |
| Kyle Coleman      | LinkedIn       | Copy.ai blog     | `scrape_linkedin.py` + manual     |

## Repo structure

```
research/
├── sources.md                       # 10 experts: POV, verified recent activity, links
├── linkedin-posts/
│   └── <expert-slug>/
│       └── posts-YYYY-MM-DD.md      # 5 recent posts, consolidated
├── youtube-transcripts/
│   └── <channel-slug>/
│       └── YYYY-MM-DD-<videoId>-<slug>.md
└── other/
    └── reports/                     # Lavender benchmarks, Venetz book summaries
scripts/
├── fetch_youtube_transcripts.py     # Auto-discovers latest N videos via channel RSS
├── scrape_linkedin.py               # Attaches to running Chrome via CDP; humanlike pacing
└── requirements.txt
```

## Collection approach

### Automated

- **YouTube (Morgan Ingram, 30MPC, Leslie Venetz).** `scripts/fetch_youtube_transcripts.py` takes channel handles, resolves to channel IDs, parses the RSS feed, and pulls transcripts for the latest 8 videos per channel via `youtube-transcript-api`. No API key. Rerun-safe.
- **LinkedIn (all 10 experts).** Driving a logged-in Chrome session via DOM extraction on each expert's `/recent-activity/all/` page. Five recent substantive posts per expert saved as a consolidated `posts-2026-04-17.md` file with reactions, comment counts, permalinks, and body text.

### Manual

- Long-form blog posts (Lavender, Common Room, Copy.ai). Paste into `research/other/reports/` with the source URL.

### Deliberately out of scope

- Podcast episodes (Outbound Squad, 30MPC). Show notes are only synopsis of audio, not primary material.
- Newsletter issues (Practical Prospecting, Inside Selling). LinkedIn covers the authors.

## Status

- [x] Topic chosen + rationale documented
- [x] 10 experts selected with verified 2025 to 2026 activity
- [x] Repo skeleton with per-expert folders
- [x] YouTube transcript fetcher
- [x] LinkedIn scraper (CDP attach)
- [x] Run YouTube fetcher (17 transcripts across 30mpc, morgan-ingram, venetz)
- [x] LinkedIn collection (5 posts x 10 experts = 50 posts)
- [ ] Playbook draft (future milestone)
