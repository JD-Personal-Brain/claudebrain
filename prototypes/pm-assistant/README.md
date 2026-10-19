# PM Assistant Prototype

A clickable concept of **The PM Assistant**: one AI assistant for each portfolio manager (PM), the credit
partner paired with a relationship manager (RM). It shows the plan's wave 1 capabilities working (the
borrower file and the review and memo drafts) and a wave 2 preview (early warning), with three agents
running live on Claude, on made-up sample data. Current version: **4** (`prototype-v4.html`; versions 1 to 3 are kept unchanged). It's a prototype to show we can build; the real product
comes from the six steps (Discover onward), so every fact about the bank in it is an assumption to confirm.

- **Live page:** https://claude.ai/artifact/8vFxUWVwtZbzZs7pL162HE (private until shared from its Share menu)
- **The tour as a video:** `pm-assistant-tour-v4.mp4` (under 2 minutes, with a voiceover read by Kokoro, an open-source voice; the script is `video/narration.json`). Re-recorded for version 4: one line was re-voiced (the borrower file builder now "reads four sources itself: statements, loans, deposits and documents", with no mention of Federal Reserve rate data), and the other clips were reused. The version 1 to 3 videos are kept.
- **Built from:** Prompt 4 in `prompt-library.md`, with the user group changed to PMs; the product page (`memos/pm-assistant.md`), agents A7 to A9 and workflows B10 to B14 in the full plan (`memos/pm-assistant-framework.md`); controls in `playbook/controls.md`. Copied from the RM Assistant Prototype (`prototypes/rm-assistant/`, version 4), so both share one house style and structure.
- **The same sample world as the RM prototype:** Sam Okafor is the portfolio manager the RM prototype's Jordan Ellis refers credit to, and the 12 borrowers are Jordan's 12 clients, with the same loans.
- **No outside data feed:** everything the agents read is the sample borrower file. Versions 1 to 3 showed the 10-year Treasury yield as background in the borrower file; version 4 removed it (an Elon mode review, approved), because it never entered a draft, so it added code and a guardrail with nothing in the plan behind it (no agent spec or data contract line asks for it). A real build would add any outside data through the data contract (K5) first.

## What's in it

| Screen | Plan reference | What happens |
|---|---|---|
| Today | Ties the capabilities together | The PM's day on one screen: four numbers to click (reviews due, borrowers with early warning flags, drafts waiting, items missing or late), reviews and requests coming due, and what's waiting for a decision. The flags count and the early warning decisions are tagged "Wave 2 preview". |
| Borrower file | Workflow B10, agent A7 | A7 checks the PM may see the borrower (K4), then calls four page tools (financials, loans and covenants, deposits and payments, documents and notes), each step shown. Every figure carries its source, and code lists what's missing or late. Claude summarizes the file. The PM uses it, asks the RM for what's missing (a drafted note the PM sends) or flags an error. |
| Review and memo drafts | Workflows B11 and B12, agent A8 | Claude drafts the five routine sections of an annual review or credit memo from A7's file. The draft is marked "AI draft" and names the credit officer who decides; the borrower risk rating and recommendation are left blank "For the PM's judgment". Code checks every number (K7), marks sections "needs input" where the file has a gap (K25), removes any rating or recommendation section the AI writes and scans for decisions, prices and rate commentary (K3, K8). The draft states facts with sources and draws no conclusions; its last section, "Changes and items to note", lists plain facts only (for example "Requested line $4.5M; borrowing base $5.2M (Sep 30)"). The recommendation box notes it's "required only if the bank's credit policy asks for a recommendation (to confirm)". Approval is held until the PM writes the judgment; the button is "Approve as final", and **the assistant never submits**: the PM submits it through the bank's normal approval route. |
| Early warning flags (wave 2 preview) | Workflows B13 and B14, agent A9 | Five sample rules in code (K22), EW1 to EW5; a sample set for the prototype, since the real rules are credit risk's to set: statements late, covenant within 10% of its limit, covenant breached, deposits down 25% or more over 3 months, payment past due. Claude explains the flags with the numbers. A covenant breach (EW3) is tagged "Breach: the bank's waiver and rating process applies"; others "Look at this week" or "Keep an eye on". The screen notes the sample borrowers were chosen to show every rule, so a real book would flag far fewer. The PM dismisses (with a reason), watches, or raises it through the bank's process. Below, the covenant and statement tracker (B14) lists every test and due item. |
| Controls and audit log | K1, K2, K3, K4, K7, K8, K12, K22, K25 | "Try to break it" (borrower risk ratings, approvals, recommendations, prices, other PMs' borrowers, record changes and contacting borrowers are stopped in code, while a PM's ordinary credit questions pass); A9's rule set; the live audit log. |
| How we'd measure it | The five kinds of measures | Usage, quality, business impact, adoption, and risk and controls, counted from the session, each with a made-up sample pilot week. |
| How it's built | | The agents, the data, how it's tested, what a pilot would need, and where this sits in the product machine (sub-step 1.6). |

The **guided tour** plays on a first visit (under 2 minutes, voiced), and anyone can pause, skip, mute or replay it.

**One borrower is incomplete on purpose:** Chequamegon Timber Works hasn't sent its FY2025 statements or its Q2 2026
compliance certificate, so its file lists them as late, its review draft marks two sections "needs input", and
approval is held until they're resolved (K25).

## How it works

- **Live AI:** inside claude.ai the page asks Claude through the artifact's `sample` capability (the same mechanism as the RM prototype), on the viewer's own Claude account (the first run asks the viewer's permission). A7's summary and A9's explanations use the quick model tier; A7 calls the page tools itself when tools are available; A8's draft uses the default tier. The page must be published with `capabilities: {sample: {}}`.
- **Without live AI** (outside claude.ai, or if the viewer says no), every screen plays the **recorded run** in `src/replay.js`, written by Claude during the build and labeled "Recorded run" on screen. A7's gathering is code, so it works for every borrower; the recorded summary covers three of them. The tour always uses recorded runs, so it never spends anyone's usage.
- **Number check (K7 and the accuracy bar):** as soon as an AI output is finished, every number in it is matched against the borrower file (including numbers written inside rates and requested terms, such as "Prime + 0.50%"); anything it can't trace is highlighted, and approval is held until the PM changes the draft so it matches. Dates, fiscal years and codes are skipped, and so are small whole numbers under 10.
- **Ratios and growth** are calculated in code by A7 from the statement figures and labeled "A7 calculation", so the AI never has to calculate a number.
- **Guardrails (K3, K8, K4, K2, K1):** checked in code before Claude is asked; Claude's prompt carries the same rules as a second line of defense, and every finished draft is scanned again. The code check is pattern matching, so it catches common phrasings, not every possible one; `tests/run-tests.js` lists the phrasings it must block and the ordinary questions it must allow.

## Files

| Path | What it is |
|---|---|
| `src/page.html` | The page's markup |
| `src/styles.css` | The house style (the RM prototype's, plus the PM additions at the end), light and dark |
| `src/data/portfolio.js` | The sample PM, 12 borrowers (plus 2 of another PM's) |
| `src/agents.js` | A7's page tools and missing list, A9's rules, the guardrails, the number check, the audit log and the prompts |
| `src/replay.js` | The recorded runs |
| `src/app.js` | The screens |
| `src/tour.js` | The guided tour |
| `build.py` | Inlines everything (and the voice clips) into one file, `prototype-v<N>.html` |
| `tests/run-tests.js` | Automated tests of the "done" checklist, with a test double standing in for Claude |
| `tests/record-video.js` | Records the tour as a video, each step timed to its voiceover line |
| `video/narration.json` | The voiceover script, one line per tour step |
| `video/narrate.py` | Reads the script aloud with Kokoro (code MIT, model Apache 2.0), one clip per step |
| `video/make-video.py` | Retimes the recording to real time and lays the voice down in sync |
| `voice/` | The tour's voice, one MP3 per step, and their lengths |
| `prototype-v1.html` to `prototype-v4.html` | The delivered versions, each kept unchanged (version 4 is current) |
| `pm-assistant-tour-v1.mp4` to `pm-assistant-tour-v4.mp4` | The tour as a video, one per version that changed the tour |
| `CHANGELOG.md` | What changed in each version |

## How to change it

1. Edit the files in `src/`.
2. Build the next version: `python3 build.py 5` writes `prototype-v5.html`. Delivered versions are never overwritten, so every step is kept.
3. Test it: `PW=$(npm root -g)/playwright CHROMIUM=/opt/pw-browsers/chromium node tests/run-tests.js prototype-v5.html` (screenshots go to `$SHOTS`).
4. If the tour changed: `pip install kokoro-onnx soundfile`, get `kokoro-v1.0.onnx` and `voices-v1.0.bin` (see `video/narrate.py`), run `python3 video/narrate.py video/narration.json <clips folder>`, convert the clips to MP3 into `voice/` (`ffmpeg -i stepNN.wav -ac 1 -b:a 48k voice/stepNN.mp3`) with `lens.json`, rebuild, then `NARRATION=voice/lens.json OUT=<folder> node tests/record-video.js prototype-v5.html` and `python3 video/make-video.py <folder> <clips folder> pm-assistant-tour-v5.mp4` (if it runs past 2 minutes, trim the silent tail with `ffmpeg -i in.mp4 -t 119.5 -c copy out.mp4`). If only the screens changed and not the narration, skip Kokoro: convert `voice/stepNN.mp3` back to 16-bit WAV clips (`ffmpeg -i voice/stepNN.mp3 -ac 1 -ar 24000 -sample_fmt s16 <clips folder>/stepNN.wav`, plus a copy of `lens.json`) and record.
5. Add a line to `CHANGELOG.md`, publish the new file to the same page link, and save a draft to GitHub.

_Last updated: 2026-10-19_
