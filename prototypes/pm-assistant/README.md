# PM Assistant Prototype

A clickable concept of **The PM Assistant**: one AI assistant for each portfolio manager (PM), the credit
partner paired with a relationship manager (RM). It shows the plan's wave 1 capabilities working (the
borrower file and the review and memo drafts) and a wave 2 preview (early warning), with three agents
running live on Claude, on made-up sample data. It's a prototype to show we can build; the real product
comes from the six steps (Discover onward), so every fact about the bank in it is an assumption to confirm.

- **Live page:** https://claude.ai/artifact/8vFxUWVwtZbzZs7pL162HE (private until shared from its Share menu)
- **The tour as a video:** `pm-assistant-tour-v1.mp4` (about 1 minute 55 seconds, with a voiceover read by Kokoro, an open-source voice; the script is `video/narration.json`).
- **Built from:** Prompt 4 in `prompt-library.md`, with the user group changed to PMs; the product page (`memos/pm-assistant.md`), agents A7 to A9 and workflows B10 to B14 in the full plan (`memos/pm-assistant-framework.md`); controls in `playbook/controls.md`. Copied from the RM Assistant Prototype (`prototypes/rm-assistant/`, version 4), so both share one house style and structure.
- **The same sample world as the RM prototype:** Sam Okafor is the portfolio manager the RM prototype's Jordan Ellis refers credit to, and the 12 borrowers are Jordan's 12 clients, with the same loans.
- **Added for the prototype only:** the outside data feed (the 10-year Treasury yield), used as background on floating-rate loans. It isn't in the plan's agent specs or data contract; a real build would add it through the data contract (K5) first.

## What's in it

| Screen | Plan reference | What happens |
|---|---|---|
| Today | Ties the capabilities together | The PM's day on one screen: four numbers to click (reviews due, the watchlist, drafts waiting, items missing or late), reviews and requests coming due, and what's waiting for a decision. |
| Borrower file | Workflow B10, agent A7 | A7 checks the PM may see the borrower (K4), then calls five page tools (financials, loans and covenants, deposits and payments, documents and notes, market data), each step shown. Every figure carries its source, and code lists what's missing or late. Claude summarizes the file. The PM uses it, asks the RM for what's missing (a drafted note the PM sends) or flags an error. |
| Review and memo drafts | Workflows B11 and B12, agent A8 | Claude drafts the five routine sections of an annual review or credit memo from A7's file. The draft is marked "AI draft" and names the credit officer who decides; the risk rating and recommendation are left blank "For the PM's judgment". Code checks every number (K7), marks sections "needs input" where the file has a gap (K25), removes any rating or recommendation section the AI writes and scans for decisions and prices (K3, K8). Nothing is submitted until the PM writes the judgment and approves. |
| Early warning watchlist (wave 2 preview) | Workflows B13 and B14, agent A9 | Five rules in code (K22): statements late, covenant within 10% of its limit, covenant breached, deposits down 25% or more over 3 months, payment past due. Claude explains the flags with the numbers. The PM dismisses (with a reason), watches, or raises it through the bank's process. Below, the covenant and statement tracker (B14) lists every test and due item. |
| Controls and audit log | K1, K2, K3, K4, K7, K8, K12, K22, K25 | "Try to break it" (risk ratings, approvals, recommendations, prices, other PMs' borrowers, record changes and contacting borrowers are stopped in code, while a PM's ordinary credit questions pass); A9's rule set; the live audit log. |
| How we'd measure it | The five kinds of measures | Usage, quality, business impact, adoption, and risk and controls, counted from the session, each with a made-up sample pilot week. |
| How it's built | | The agents, the data, how it's tested, what a pilot would need, and where this sits in the product machine (sub-step 1.6). |

The **guided tour** plays on a first visit (about 1 minute 52 seconds, voiced), and anyone can pause, skip, mute or replay it.

**One borrower is incomplete on purpose:** Chequamegon Timber Works hasn't sent its FY2025 statements or its Q2 2026
compliance certificate, so its file lists them as late, its review draft marks two sections "needs input", and
approval is held until they're resolved (K25).

## How it works

- **Live AI:** inside claude.ai the page asks Claude through the artifact's `sample` capability (the same mechanism as the RM prototype), on the viewer's own Claude account (the first run asks the viewer's permission). A7's summary and A9's explanations use the quick model tier; A7 calls the page tools itself when tools are available; A8's draft uses the default tier. The page must be published with `capabilities: {sample: {}}`.
- **Without live AI** (outside claude.ai, or if the viewer says no), every screen plays the **recorded run** in `src/replay.js`, written by Claude during the build and labeled "Recorded run" on screen. A7's gathering is code, so it works for every borrower; the recorded summary covers three of them. The tour always uses recorded runs, so it never spends anyone's usage.
- **Number check (K7 and the accuracy bar):** as soon as an AI output is finished, every number in it is matched against the borrower file (including numbers written inside rates and requested terms, such as "Prime + 0.50%"); anything it can't trace is highlighted, and approval is held until the PM changes the draft so it matches. Dates, fiscal years and codes are skipped, and so are small whole numbers under 10.
- **Ratios and growth** are calculated in code by A7 from the statement figures and labeled "A7 calculation", so the AI never has to calculate a number.
- **Guardrails (K3, K8, K4, K2, K1):** checked in code before Claude is asked; Claude's prompt carries the same rules as a second line of defense, and every finished draft is scanned again. The code check is pattern matching, so it catches common phrasings, not every possible one; `tests/run-tests.js` lists the phrasings it must block and the ordinary questions it must allow.
- **Outside data:** the US 10-year Treasury yield (monthly average, Federal Reserve H.15, public domain), via the datahub.io copy on GitHub. A published page can't reach outside websites, so `scripts/fetch_market.py` saves a dated copy into `src/data/market.js` and the page shows that date. (The Federal Reserve's and FRED's own sites weren't reachable from the build sandbox; GitHub was.)

## Files

| Path | What it is |
|---|---|
| `src/page.html` | The page's markup |
| `src/styles.css` | The house style (the RM prototype's, plus the PM additions at the end), light and dark |
| `src/data/portfolio.js` | The sample PM, 12 borrowers (plus 2 of another PM's) |
| `src/data/market.js` | The outside data (generated; don't edit) |
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
| `CHANGELOG.md` | What changed in each version |

## How to change it

1. Edit the files in `src/` (or refresh the outside data: `python3 scripts/fetch_market.py`).
2. Build the next version: `python3 build.py 2` writes `prototype-v2.html`. Delivered versions are never overwritten, so every step is kept.
3. Test it: `PW=$(npm root -g)/playwright CHROMIUM=/opt/pw-browsers/chromium node tests/run-tests.js prototype-v2.html` (screenshots go to `$SHOTS`).
4. If the tour changed: `pip install kokoro-onnx soundfile`, get `kokoro-v1.0.onnx` and `voices-v1.0.bin` (see `video/narrate.py`), run `python3 video/narrate.py video/narration.json <clips folder>`, convert the clips to MP3 into `voice/` (`ffmpeg -i stepNN.wav -ac 1 -b:a 48k voice/stepNN.mp3`) with `lens.json`, rebuild, then `NARRATION=voice/lens.json OUT=<folder> node tests/record-video.js prototype-v2.html` and `python3 video/make-video.py <folder> <clips folder> pm-assistant-tour-v2.mp4`.
5. Add a line to `CHANGELOG.md`, publish the new file to the same page link, and save a draft to GitHub.

_Last updated: 2026-10-19_
