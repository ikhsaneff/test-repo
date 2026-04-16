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

Earlier drafts of this project assumed YouTube was the primary video channel for all 10 experts. It isn't. Most publish primarily on LinkedIn, with YouTube or a long-form blog as secondary. The collection strategy reflects that.

| Expert            | Primary        | Secondary        | Automation                        |
|-------------------|----------------|------------------|-----------------------------------|
| Jason Bay         | LinkedIn       | Blog             | `scrape_linkedin.py`              |
| Josh Braun        | LinkedIn       | YouTube          | `scrape_linkedin.py`              |
| Jed Mahrle        | LinkedIn       |                  | `scrape_linkedin.py`              |
| Florin Tatulea    | LinkedIn       | Common Room blog | `scrape_linkedin.py`              |
| Will Allred       | LinkedIn       | Lavender blog    | `scrape_linkedin.py` + manual     |
| Leslie Venetz     | LinkedIn       | Book, YT         | `scrape_linkedin.py` + `fetch_youtube_transcripts.py` |
| Morgan Ingram     | YouTube        | LinkedIn         | `fetch_youtube_transcripts.py`    |
| Nick Cegelski     | YouTube        | LinkedIn         | `scrape_linkedin.py` + `fetch_youtube_transcripts.py` |
| Armand Farrokh    | LinkedIn       |                  | `scrape_linkedin.py`              |
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
