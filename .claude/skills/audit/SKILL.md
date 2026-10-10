---
name: audit
description: Full audit of the work before it goes into main. Runs as the first step of every wrap-up, before offering to merge anything that changes frameworks, the playbook, skills, rules, memos or designed pages, and whenever the user says "audit", "check our work" or "is this clean?".
---

# Audit the work

Auditing is part of the process, not an extra. Nothing is offered for merging
into main until it passes this audit. Keep the report to the user short (rule R2).

## 1. Scope
- List every file changed since main: `git fetch origin main` then `git diff --name-only origin/main...HEAD`, plus any uncommitted changes.
- Add the files they depend on or that depend on them. For example, a framework change also touches `playbook/`, the delivery machine page, the playbook page and any memo that copies it.
- Add every designed page whose source changed, and its published link (see `designs/README.md`).
- Always add `open-items.md`, the log of everything still open, even if the session didn't edit it: open items go out of date quickly, so every audit checks them.

## 2. Mechanical checks (always)
1. Run `python3 .claude/skills/audit/check.py` from the repo root. It checks that the framework and playbook match, that every sub-step has all its fields, that no designed page has an empty table, that every page built from a working copy (delivery machine, playbook, product framework, tech stack, job notes, job description, prompting guide, bank business briefing, open items, Document Library, Workflow Maps, Agent Library) is up to date, and that every page in `designs/README.md` is in `designs/library.json`, and the other way round. It also checks the Open Items log (`open-items.md`): no number used twice, the "At a glance" counts match the rows, every page still waiting for review and every idea still waiting for an answer is in the log, and the log isn't older than NOW.md. If a page was out of date, the checker rebuilds it: republish it.
2. For each changed designed page: render it at 1280 and 400 pixels wide (design-canvas `.dc.html` files must be served through a local web server, `python3 -m http.server`, with the canvas runtime saved beside them as `support.js`: opened straight from disk, the runtime can't load itself and drops table rows, which is how the scrolling plan page lost its 12 tables) with Playwright (a browser tool Claude runs; Chromium is at `/opt/pw-browsers/chromium`), confirm nothing is empty, cut off or scrolling sideways, and look at one screenshot.
3. For each published page: read it with the Artifact tool and confirm it matches the source in `designs/`. If it doesn't, find out why before changing anything.

## 3. First review: a fresh reviewer
Start a separate reviewer (a second Claude helper that only reads, started with the Agent tool) with the changed files and
this checklist. Ask for each finding's severity (Must fix, Should fix or Minor),
where it is, a quote as proof, and the exact fix.
1. **Consistency:** do the files agree with each other (names, numbers, kinds, gates, steps)?
2. **Cross-references:** does every "see 2.7", "Appendix A", "section 3" or file name point to the right thing?
3. **Coverage:** is anything listed in one place missing from another?
4. **Facts:** any law, product feature or number stated as fact that might be wrong? Guesses about the bank marked ⚠️, unknown numbers shown as [X], outside facts with a source?
5. **Logic:** would anything stall or go in a circle if someone followed it for real? Is each output used, and does each gate have what it needs?
6. **Drift:** does each working copy (.md) match its designed page?
7. **Plain English:** could a newcomer follow it (rule R13)? Include NOW.md: every "What's next" item must say what the thing is and why it matters, not just its name (from L10d).
8. **Open items:** read `open-items.md` against this session's work. For every open item the session touched: is it finished (then it belongs under "Closed" with the date), still open but changed (then its wording, "Who" or "Waits on" needs updating), or unchanged? Did the session create anything unfinished that isn't in the log? Do the items still match the files they came from?

## 4. Fix
- Fix every Must fix and Should fix. Fix Minor ones too, unless a fix would change a decision the user made.
- Anything that needs the user's decision goes on a short list for the report. Don't guess.

## 5. Second review: confirm the fixes
Start a second fresh reviewer with the list of findings and fixes. It checks
each one (pass or fail, with a quote) and looks for new problems the fixes
caused. Fix what it finds, then run the mechanical checks again.

## 6. Report and learn
- Tell the user, in about 5 lines: how many findings by severity, the 3 that mattered most, that all are fixed (or what's left), and anything they need to decide.
- For each Must fix that came from Claude's own work, log a lesson with the **log-lesson** skill (what happened, the root cause and the fix).
- Only after a clean audit: offer to merge into main.

## Rules
- Never skip the audit because a change looks small. Today's empty tables came from a "simple" rebuild.
- Never say "clean" without proof: the checker's output, the reviewers' pass list and the screenshots.
- If a reviewer and Claude disagree, check the source text and say who was right.
