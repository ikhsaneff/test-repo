# Sources: 10 Experts on Cold Outreach for B2B SaaS

Curated list of 10 practitioners who publish in public. Each entry: primary channel first, secondary channels second. Use this file as the index for everything in `linkedin-posts/`, `youtube-transcripts/`, and `other/`.

## Selection filter

1. Practitioner, not pundit. Runs a team, agency, or product where advice gets tested.
2. Publishes frequently in the last 6 to 12 months.
3. Differentiated POV (not just "personalize more").
4. Shares receipts: numbers, scripts, teardowns.

**Explicitly excluded**: sales "influencers" recycling frameworks with no current practice, course sellers whose only evidence is testimonial screenshots, and anyone not shipping outbound themselves in the last 2 years.

## Channel reality check

An earlier draft of this project assumed YouTube was a primary channel for all 10 experts. **It isn't.** After verifying each, most publish primarily on LinkedIn + a podcast or LinkedIn + a newsletter. The `research/youtube-transcripts/` subfolder will only exist for the four experts who actually maintain active YouTube channels (Morgan Ingram, 30MPC, Leslie Venetz, Josh Braun).

| Expert            | Primary        | Secondary        | Where to collect                                           |
|-------------------|----------------|------------------|------------------------------------------------------------|
| Jason Bay         | Podcast        | LinkedIn         | `linkedin-posts/bay/` (podcast out of scope)               |
| Josh Braun        | LinkedIn       | Newsletter, YT   | `linkedin-posts/braun/`, `youtube-transcripts/josh-braun/` |
| Jed Mahrle        | Newsletter     | LinkedIn         | `linkedin-posts/mahrle/`                                   |
| Florin Tatulea    | LinkedIn       | Common Room blog | `linkedin-posts/tatulea/`, `other/reports/common-room/`    |
| Will Allred       | LinkedIn       | Lavender blog    | `linkedin-posts/allred/`, `other/reports/lavender/`        |
| Leslie Venetz     | LinkedIn       | Book, YouTube    | `linkedin-posts/venetz/`, `other/reports/venetz-book/`, `youtube-transcripts/venetz/` |
| Morgan Ingram     | YouTube        | LinkedIn         | `youtube-transcripts/morgan-ingram/`, `linkedin-posts/ingram/` |
| Nick Cegelski     | Podcast        | LinkedIn, YT     | `linkedin-posts/cegelski/`, `youtube-transcripts/30mpc/` (podcast out of scope) |
| Armand Farrokh    | Podcast        | LinkedIn         | `linkedin-posts/farrokh/` (podcast out of scope)           |
| Kyle Coleman      | LinkedIn       | Copy.ai blog     | `linkedin-posts/coleman/`, `other/reports/copy-ai/`        |

---

## 1. Jason Bay, Founder, Outbound Squad

- **LinkedIn:** https://www.linkedin.com/in/jasondbay/
- **Podcast:** *Outbound Squad* (https://www.outboundsquad.com/podcast)
- **Website:** https://www.outboundsquad.com/
- **Primary channel:** Podcast
- **Secondary:** LinkedIn posts

**Why included:** Runs a training company for B2B SaaS sales teams. His frameworks are tested in customer SDR/AE orgs weekly. Publishes deep breakdowns, not aphorisms.

**POV:** Multi-threading and problem-first messaging. Human reps who *learn to use AI* beat both pure-human and pure-AI outbound. Anti-pattern: "I help X do Y" openers.

**Verified recent material to collect:**

- Podcast ep. 392, *"Using voicemails to increase cold email reply rates by 3x"*
- Podcast ep. 372, *"7 hard truths about outbound in 2025"*
- Recent episode on why AI isn't replacing SDRs (cites hiring data from AI companies)

**Collection path:** `scrape_linkedin.py bay`. Podcast episodes are his primary channel but out of scope for this pass (show notes are synopses only).

## 2. Josh Braun, Founder, Josh Braun Sales Training

- **LinkedIn:** https://www.linkedin.com/in/josh-braun/
- **YouTube:** https://www.youtube.com/@JoshBraun (~218 videos, shorts-heavy)
- **Newsletter:** *Inside Selling*
- **Website:** https://joshbraun.com/
- **Primary channel:** LinkedIn
- **Secondary:** Newsletter, short-form YouTube

**Why included:** Former head of sales at Basecamp / Jellyvision. Distinctive voice that contrasts cleanly with Bay and 30MPC.

**POV:** "Poke the Bear": open with tension, not pitch. Emphasis on detachment, radical honesty, non-needy language. Sellers fail by clinging to outcomes they can't control.

**Verified recent material:**

- Guest on *I Used To Be Crap At Sales* with Mark Ackers (April 9, 2025). Storytelling vs. pitching, mindfulness in communication.
- *30 Minutes to President's Club* ep. 63, *"Poking the Bear to create more conversations"*
- *Ditch The Pitch, Josh Braun Says Poke The Bear Instead!* on *My Sales Coach*

**Collection path:** `scrape_linkedin.py braun` is the main move. YouTube is short-form clips and is optional; run `fetch_youtube_transcripts.py josh-braun` if you want them.

## 3. Jed Mahrle, Founder, Practical Prospecting

- **LinkedIn:** https://www.linkedin.com/in/outboundsales
- **Newsletter:** https://content.practicalprospecting.io/ (migrated off Substack)
- **Background:** formerly Head of Outbound Sales at Mailshake
- **Primary channel:** Newsletter
- **Secondary:** LinkedIn

**Why included:** One of the few creators who publishes cold email copy alongside actual response-rate data. Newsletter has tens of thousands of subs; content built on 50+ client campaigns.

**POV:** Reply rate is the only metric that matters early. Opens and clicks are vanity.

**Verified recent newsletter issues (2026):**

- Issue (Mar 15, 2026), *"How we've averaged a 30% reply rate across all clients"*
- Issue (Feb 15, 2026), *"5 Ways to Find Your Competitors' Customers"*
- Issue 129 (Feb 1, 2026), *"The 3 Phases of Every Cold Email Campaign"*
- Issues from Jan 2026 on CTAs and A/B testing variables
- Issue 122, *"How to Write Cold Emails That Don't Sound Like Cold Emails"*

**Collection path:** `scrape_linkedin.py mahrle` for his LinkedIn. Newsletter archive is out of scope for this pass.

---

Remaining entries (Tatulea, Allred, Venetz, Ingram, Cegelski, Farrokh, Coleman) still to fill in.
