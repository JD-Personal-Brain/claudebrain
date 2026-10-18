# RM Assistant Prototype

A clickable concept of **The RM Assistant**: one AI assistant for each relationship manager (RM).
It shows the plan's wave 1 capabilities working, with three agents running live on Claude, on
made-up sample data. It's a prototype to show we can build; the real product comes from the six
steps (Discover onward), so every fact about the bank in it is an assumption to confirm.

- **Live page:** https://claude.ai/artifact/RFM2o7cdren3TxesQBsjky (private until shared from its Share menu)
- **The tour as a video:** `rm-assistant-tour-v1.mp4` (about 2 minutes, with a voiceover read by Kokoro, an open-source voice; the script is `video/narration.json`)
- **Built from:** Prompt 4 in `prompt-library.md`; the product page (`memos/rm-assistant.md`), agents A1 to A3 and
  workflows B1 to B4 in the full plan (`memos/rm-analytics-framework.md`); controls in `playbook/controls.md`.
- **Added for the prototype only:** the outside data feed (the 10-year Treasury yield) and its "Rates context" rule. They
  aren't in the plan's agent specs or data contract; a real build would add them through the data contract (K5) first.

## What's in it

| Screen | Plan reference | What happens |
|---|---|---|
| Today (since version 4) | Ties the wave 1 capabilities together | The RM's day on one screen: four numbers to click, this week's meetings with their briefs, and what's waiting for a decision. |
| Monday opportunity list | Workflow B1, agents A1 and A2 | A1 checks the 12 clients against 5 rules, plus the rates context (code, no AI). A2 (Claude) explains the top 5. The RM accepts, changes or dismisses each one. |
| Pre-meeting client brief | Workflow B2, agent A3 | A3 (Claude) calls four page tools (client record, open insights, recent activity, market data), then writes a one-page brief with a source on every fact. |
| Meeting follow-up | Workflows B3 and B4, agent A3 | A3 (Claude) turns the RM's notes into a recap, a follow-up email, a CRM call note and next steps. Nothing is saved until the RM approves; the RM sends the email. |
| Controls and audit log | K1, K2, K3, K4, K7, K8, K12, K22, K24, K25 | "Try to break it" (guardrails stop credit decisions, prices, auto-send and other RMs' clients in code); A1's rule set; the live audit log. |
| Product manager view | The five kinds of measures | Usage, quality, business impact, adoption, and risk and controls, counted from the session. |
| How it's built | | The agents, the data, and where this sits in the product machine (sub-step 1.6). |
| Early warning (wave 2 preview, version 4) | Workflow B5 | Three rules in code (falling balances, payroll moved out, gone quiet) flag clients who may be drifting away, with a balance chart and the numbers. Never a credit signal. The RM plans a call or dismisses it. |
| Refer to treasury (wave 2 preview, version 4) | Workflow B6 | The Signal finder's treasury rules spot needs the treasury team serves; a drafted hand-off the RM changes, sends or skips, tracked from spotted to accepted (sample: nothing leaves the page). |

The **guided tour** plays on a first visit (under 2 minutes), and anyone can pause, skip or replay it.

## How it works

- **Live AI:** inside claude.ai the page asks Claude through the artifact's `sample` capability, on the
  viewer's own Claude account (the first run asks the viewer's permission). A2 uses the quick model tier;
  A3's brief uses page tools; the follow-up uses the default tier.
- **Without live AI** (outside claude.ai, or if the viewer says no), every screen plays the **recorded run**
  in `src/replay.js`, written by Claude during the build and labeled "Recorded run" on screen. The tour
  always uses recorded runs, so it never spends anyone's usage.
- **Number check (K7 and the accuracy bar):** as soon as an AI draft is finished, and before the RM can use it, every number in it
  is matched against the numeric data the agent was given; anything it can't trace (including amounts written
  in words) is highlighted. Small whole numbers under 10 are left unchecked, so counts like "3 talking points" pass.
- **Guardrails (K8, K4, K1):** checked in code before Claude is asked; Claude's prompt carries the same
  rules as a second line of defence. The code check is pattern matching, so it catches common phrasings, not
  every possible one; `tests/run-tests.js` lists the phrasings it must block and the innocent ones it must allow.
- **Outside data:** the US 10-year Treasury yield (monthly average, Federal Reserve H.15, public domain),
  via the datahub.io copy on GitHub. A published page can't reach outside websites, so
  `scripts/fetch_market.py` saves a dated copy into `src/data/market.js` and the page shows that date.

## Files

| Path | What it is |
|---|---|
| `src/page.html` | The page's markup |
| `src/styles.css` | The house style (the Document Library's tokens), light and dark |
| `src/data/book.js` | The sample RM, 12 clients (plus 2 of another RM's) and the meeting notes |
| `src/data/market.js` | The outside data (generated; don't edit) |
| `src/agents.js` | A1's rules, the guardrails, the number check, the audit log, the page tools and the prompts |
| `src/replay.js` | The recorded runs |
| `src/app.js` | The screens |
| `src/tour.js` | The guided tour |
| `build.py` | Inlines everything into one file, `prototype-v<N>.html` |
| `tests/run-tests.js` | Automated tests of the "done" checklist, with a test double standing in for Claude |
| `tests/record-video.js` | Records the tour as a video, each step timed to its voiceover line |
| `video/narration.json` | The voiceover script, one line per tour step |
| `video/narrate.py` | Reads the script aloud with Kokoro (code MIT, model Apache 2.0), one clip per step |
| `video/make-video.py` | Retimes the recording to real time and lays the voice down in sync |
| `CHANGELOG.md` | What changed in each version |

## How to change it

1. Edit the files in `src/` (or refresh the outside data: `python3 scripts/fetch_market.py`).
2. Build the next version: `python3 build.py 2` writes `prototype-v2.html`. Delivered versions are never
   overwritten, so every step is kept.
3. Test it: `PW=/opt/node-tools/node_modules/playwright node tests/run-tests.js prototype-v2.html`
   (screenshots go to `$SHOTS`).
4. Add a line to `CHANGELOG.md`, publish the new file to the same page link, and save a draft to GitHub.
- **Voice:** `voice/` holds the tour's voice, one MP3 per step (Kokoro, from `video/narration.json`) and their lengths; `build.py` puts them into the page.

_Last updated: 2026-10-18_
