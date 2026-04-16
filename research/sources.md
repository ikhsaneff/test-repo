# Sources: 10 Experts on Cold Outreach for B2B SaaS

Curated list of 10 practitioners who publish in public. Each entry is honest about *where* they actually publish: primary channel first, secondary channels second. Use this file as the index for everything in `linkedin-posts/`, `youtube-transcripts/`, and `other/`.

**Selection filter**, applied to every candidate:

1. Practitioner, not pundit. Runs a team, agency, or product where the advice gets tested.
2. Publishes frequently in the last 6 to 12 months.
3. Differentiated POV (not just "personalize more").
4. Shares receipts: numbers, scripts, teardowns.

**Explicitly excluded**: sales "influencers" recycling frameworks with no current practice, course sellers whose only evidence is testimonial screenshots, and anyone not shipping outbound themselves in the last 2 years.

Verified as of **2026-04-16**.

## Channel reality check

An earlier draft of this project assumed YouTube was a primary channel for all 10 experts. **It isn't.** After verifying each, most publish primarily on LinkedIn + a podcast or LinkedIn + a newsletter. This file now reflects that reality, and the `research/youtube-transcripts/` subfolder only exists for the four experts who actually maintain active YouTube channels (Morgan Ingram, 30MPC, Leslie Venetz, Josh Braun).

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

## 4. Florin Tatulea, Head of Sales Development, Common Room

- **LinkedIn:** https://www.linkedin.com/in/florintatulea/ (LinkedIn Top Voice; ~74K followers)
- **Background:** previously Barley, Loopio
- **Primary channel:** LinkedIn
- **Secondary:** Common Room blog and videos; guest on podcasts

**Why included:** Currently *running* an SDR team. Publishes from inside, not from a training pulpit. Probably the clearest articulation of the "signal-based outbound" thesis.

**POV:** Shift from "Outbound 1.0" (spray-and-pray) to "Outbound 3.0" (signal-based + AI-powered precision). SDRs should focus on the 7% of prospects who know the problem and the 30% who could be educated into it.

**Verified recent material:**

- *The Revenue Leadership Podcast* ep. 31, *"The Rise of the 10X SDR"* with Kyle Norton
- Common Room blog: *"3 signals every sales rep should leverage"* (Jul 2025)
- Common Room blog and video: *"Plays that pay: how we deanonymize website activity to book more meetings"*
- Common Room blog: *"Plays that pay: how we track job changes to fuel pipeline growth"*

**Collection path:** `scrape_linkedin.py tatulea`. Save his guest-podcast episodes and Common Room pieces manually to `research/other/reports/common-room/`.

## 5. Will Allred, Co-founder, Lavender

- **LinkedIn:** https://www.linkedin.com/in/williamallred/
- **Company blog:** https://www.lavender.ai/blog (data-backed frameworks)
- **Primary channel:** LinkedIn
- **Secondary:** Lavender's published benchmark reports

**Why included:** Lavender sits on **billions** of sent emails and publishes benchmarks. Will's LinkedIn is the distilled version: word choice, length, sentiment rules, backed by numbers.

**POV:** Short, emotionally aware, personalized emails outperform long or clever ones. Tone matters as much as content. Data beats intuition.

**Verified data claims you can quote or test:**

- Cold emails without big paragraphs get **83% more replies**
- Detecting a single "informative" tone **reduces reply rates by 26%**
- Personalized emails get **10x more replies** vs. automated templates
- Operations: A-level emails reach **5.4% reply rate (+58% lift)**
- HR is the hardest department: 3.4% average; A-level emails lift it to 4.3% (+27%)
- Reply rates drop when an email has more than 1 question
- Source: Lavender *Cold Email Benchmark Report* (231,818 emails analyzed)

**Specific posts to grab:**

- *"Cold Email Wizardry 101: Understanding the Reader's Perspective"*
- *"The Ultimate Compilation of Lavender Sales Email Frameworks"* (updated)
- *"How to Build a Cold Email Personalization Process"*

**Collection path:** `scrape_linkedin.py allred` for posts, manual paste the benchmark report into `research/other/reports/lavender/`.

## 6. Leslie Venetz, Founder, The Sales-Led GTM Agency

- **LinkedIn:** https://www.linkedin.com/in/leslievenetz (LinkedIn Editorial Top Voice for Sales; 2024 Sales Innovator of the Year)
- **YouTube:** https://www.youtube.com/@LeslieVenetz (secondary)
- **Website:** https://salesledgtm.com/
- **Book:** *Profit-Generating Pipeline: A Proven Formula to Earn Trust and Drive Revenue*. **USA Today Top 50 bestseller** (2025).
- **Primary channel:** LinkedIn
- **Secondary:** Book, YouTube, weekly *Conversations with Leslie* series

**Why included:** Runs an agency that *executes* outbound for clients right now. 15+ years enterprise sales; 3x Head of Sales; has opened accounts like Walmart, JPMorgan, KraftHeinz.

**POV:** *"Warm outbounding is just good outbounding."* Personalize based on identity, intent, and context. #EarnTheRight.

**Verified recent material:**

- Guest on *Mark J. Carter* podcast (Jul 2025), *"The Power of Meaningful Sales Questions"*
- Common Room interview and video: *"Beyond intent: top takeaways from Leslie Venetz"*
- Weekly *Conversations with Leslie* series
- The book. Treat as canonical artifact (chapter summaries in `research/other/reports/venetz-book/`)

**Collection path:** `scrape_linkedin.py venetz` + `fetch_youtube_transcripts.py venetz` + book chapter notes.

## 7. Morgan Ingram, Sales creator and JB Sales Director of Sales Execution

- **LinkedIn:** https://www.linkedin.com/in/morganjingram/
- **YouTube:** https://www.youtube.com/@MorganJIngram (*The SDR Chronicles*, 100+ videos)
- **Primary channel:** YouTube
- **Secondary:** LinkedIn

**Why included:** Longest longitudinal signal on this list. Has published outbound content consistently for 5+ years. Channel variety and video prospecting are his lane.

**POV:** Video and voice beat text-only. Videos should be movie-trailer length (45 to 50 seconds). Don't send video as the *first* touch. Use it as touch 3 after email and call engagement.

**Verified frameworks to capture:**

- The **10/30/10 Video Prospecting Formula**
- HubSpot: *"Using Video to Accelerate Your Sales Pipeline: Morgan Ingram's Master in Sales Series Part 1"*
- JB Sales OnDemand webinars: *"How To Master The Art Of Video Prospecting"*, *"Video Prospecting Tactics with JB Sales & Vidyard"*

**Collection path:** `fetch_youtube_transcripts.py morgan-ingram` is the main move. Plus `scrape_linkedin.py ingram`.

## 8. Nick Cegelski, Co-host, 30 Minutes to President's Club

- **LinkedIn:** https://www.linkedin.com/in/nickcegelski/
- **Podcast:** https://www.30mpc.com/podcast
- **YouTube:** https://www.youtube.com/@30mpc (podcast-as-video)
- **Book:** *Cold Calling Sucks (And That's Why It Works)*
- **Primary channel:** Podcast
- **Secondary:** LinkedIn, YouTube

**Why included:** 3x top enterprise seller, still carrying quota. Tactics come from closing deals this quarter, not memory. Podcast format forces specific scripts.

**POV:** Tactical beats strategic. Problem-proposition framework: lead with a vivid, emotionally charged problem the buyer feels, *then* briefly show how you solve it. Generic "optimize/streamline/AI-powered" language fails.

**Specific content to capture:**

- The full 30MPC cold-call framework: opener, pitch, objection handling
- The *"Heard the name tossed around"* opener technique
- Why context-first openers outperform permission begging
- Recent episodes breaking down why most cold-call pitches fail

**Collection path:** `fetch_youtube_transcripts.py 30mpc` + `scrape_linkedin.py cegelski`. Podcast show notes are synopsis-only and out of scope; the YouTube transcripts and LinkedIn posts carry the substantive material.

## 9. Armand Farrokh, Co-host, 30 Minutes to President's Club; VP Sales, Pave

- **LinkedIn:** https://www.linkedin.com/in/armand-farrokh/
- **Co-host:** *30 Minutes to President's Club* (with Nick Cegelski and Mark Kosoglow)
- **Book:** co-author of *Cold Calling Sucks (And That's Why It Works)*
- **Primary channel:** Podcast
- **Secondary:** LinkedIn

**Why included:** Became VP Sales at age 29 (ex-Carta, ex-Pave). Pairs with Nick: AE view plus VP view on the same tactic.

**POV:** Sales leaders own outbound *system design*; reps own execution. Most teams blame reps for system failures. Outbound is a leadership problem disguised as a rep problem.

**Specific content:**

- Podcast episodes where he solo-hosts or shares Pave internals
- His breakdowns of hiring and training SDR teams
- Recent LinkedIn posts on outbound as an *operating system* (not a cadence)

**Collection path:** `scrape_linkedin.py farrokh`. Co-hosts the 30MPC podcast with Nick, but podcast show notes are out of scope; Armand's LinkedIn is the primary capture point here.

## 10. Kyle Coleman, Global VP Marketing, ClickUp *(recently moved from Copy.ai CMO)*

- **LinkedIn:** https://www.linkedin.com/in/kyletcoleman
- **Previous publishing home:** Copy.ai (https://www.copy.ai/author/kyle-coleman)
- **Background:** 6th employee at Looker (acquired by Google for $2.6B); SDR and Marketing leadership at Clari during its ~10x ARR run; CMO at Copy.ai
- **Primary channel:** LinkedIn
- **Secondary:** Copy.ai blog archive

**Why included:** Crossover voice. Ran marketing *for* a company whose users were SDR teams, now running marketing at a large SaaS. Shares internal GTM experiments including outbound and ABM integration.

**POV:** Outbound is a GTM *system*, not a sales tactic. SDR messaging should ladder to campaign themes owned by marketing. AI doesn't kill the SDR role. It changes how SDRs are leveraged.

**Specific content to capture from the Copy.ai era:**

- *How will AI impact SDRs? Oddly accurate predictions by Kyle Coleman*
- *2025 Cold Email Guide* on Copy.ai
- *What You Need to Know About Outbound Sales Tools in 2025*
- *The Future of AI-Driven Sales with Kyle Coleman & Tomasz Tunguz*
- Keynote: *"How to Unify the GTM Using AI"*

**Collection path:** `scrape_linkedin.py coleman` + manual paste of the Copy.ai pieces into `research/other/reports/copy-ai/`.

---

## Collection checklist per expert

- [ ] 15 to 25 recent LinkedIn posts (dated, source-linked)
- [ ] Primary-channel material per the table above
- [ ] 1 *anchor artifact* (canonical framework, pinned post, book chapter, or keynote)
- [ ] A one-paragraph POV summary in their folder's `README.md`

## Known gaps and deliberate exclusions

- **No non-US voices.** Strong v2 candidate: Daniel Disney (UK, social selling). Excluded because his focus leans social/LinkedIn vs. pure cold outbound.
- **No ABM specialist** (e.g., Sangram Vajre, Kristina Jaramillo). Deliberate. Scope is *outbound pipeline*, not ABM programs.
- **No pure cold-calling coach** (e.g., Sara Uy, Ryan Reisert). Could be added in v2 if the playbook needs more call-specific material; Cegelski and Farrokh already cover calling heavily.
