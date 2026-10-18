---
name: audit
description: Full audit of the work before it goes into main. Runs as the first step of every wrap-up, before offering to merge anything that changes frameworks, the playbook, skills, rules, memos or designed pages, and whenever the user says "audit", "check our work" or "is this clean?".
---

# Audit the work

Auditing is part of the process, not an extra. Nothing is offered for merging
into main until it passes this audit. Keep the report to the user short (rule R2).

## 0. Pick the size (Audit Log improvement 3)
Say which size and why in one line, then run it. When unsure, go one size up.
- **Quick:** a small fix that doesn't change what any page says about the process, a count or a name (a typo, a date, one row). Run the three scripts in section 2 (checker, render check, nothing-lost) and look at the changed page. No reviewers.
- **Standard:** a normal session's work. Sections 1 to 7 below: the scripts, one fresh reviewer, fixes, a second reviewer.
- **Deep:** a reorganization, a rename across pages, new rules or controls, or before a milestone (sharing with the bank, applying the machine to a new user group). Standard, plus the full alignment sweep (2b) with one reviewer per reference page, and a walk-through reviewer who takes a made-up product through the steps to find where the work would stall.

## 1. Scope
- List every file changed since main: `git fetch origin main` then `git diff --name-only origin/main...HEAD`, plus any uncommitted changes.
- Add the files they depend on or that depend on them. For example, a change to the six steps (`memos/role-workflow.md`), the rules (`product-framework.md`) or the task tables (`product-machine.md`) also touches `playbook/`, the four "How we deliver" pages and any memo that copies it.
- Add every designed page whose source changed, and its published link (see `designs/README.md`).
- Always add `open-items.md`, the log of everything still open, even if the session didn't edit it: open items go out of date quickly, so every audit checks them.

## 2. Mechanical checks (always)
1. Run `python3 .claude/skills/audit/check.py` from the repo root. It runs every check listed at the top of `check.py` (the list there is the one home of what it checks): the Product Machine against the playbook, required fields, empty tables, stale built pages (it rebuilds them: republish any it rebuilt), the Document Library against `designs/README.md`, the Open Items log, shorthand in NOW.md, counts, gate and question wording, banned, retired and old page names, RM and PM spelling, section links, stray marks, requirement sources and agent names. When this session renamed something, add the old wording to the glossary's retired table first. It can't tell whether a reference points to the right item, so after the log is renumbered, re-read each reference against its item.
2. **Render every designed page, every audit, not only the changed ones** (from L19): run `PW=$(npm root -g)/playwright node designs/render-check.js`. It renders all pages the way a reader sees them and fails on an empty table, sideways scrolling at phone width, stray Markdown, a blank render, or a canvas part taller than its frame (cut off at the bottom). It must report `problems: 0`. Then look at the screenshots of the pages that changed (in `/tmp/render-check`), including their bottoms.
3. **Nothing lost (required, idea 46, rule R29).** Run `python3 .claude/skills/audit/lost-lines.py`. It lists every sentence that was in a working file on main and is now gone from the whole repo (not moved anywhere else). For each one, put it back, or name it in the audit report as reworded or cut on purpose, with the reason. Give the list to the first reviewer too.
4. For each published page: read it with the Artifact tool and confirm it matches the source in `designs/`. If it doesn't, find out why before changing anything.

## 2b. Alignment sweep (standard and deep audits, across ALL core documents)
The point of the audit is to keep every core document consistent, not only the
files this session touched. A stale line in an untouched file is still drift
(from L18: the library said the playbook had a "19-agent library" while the
Agent Library showed 39, and no audit caught it because neither file changed).
1. The reference pages are the source of truth for their subject: the **Agent Library** (agents), **Workflow Maps** (processes and workflows), **Steps Catalog** (sub-steps and their tasks), **Controls Catalog** (controls) and **Glossary** (`glossary.md`, the words we use). Each is built from working files, so first confirm it's up to date (step 2.1).
2. Start read-only reviewers in parallel (Agent tool): in a deep audit one per reference page (the glossary can share a reviewer with the Steps Catalog); in a standard audit one reviewer covers all of them. Each builds the page's inventory from its sources, then checks **every** core document against it, changed or not: `product-framework.md`, `product-machine.md`, `playbook/`, `memos/`, `NOW.md`, `open-items.md`, `tech-stack.md`, `designs/library.json`, `designs/README.md`, hard-coded text in `designs/*-build.py`, the hand-made pages (`designs/rm-analytics-canvas/`, `designs/rm-analytics-plan.html`, `designs/role-workflow.html`) and the skills. They look for wrong counts, names that differ, items in one place but missing from another, wrong cross-references (sub-step, agent or control numbers) and hand-made pages older than their working copy. Each finding needs file and line, a quote, and the fix.
3. Ask each reviewer to finish within about 40 steps and always end with its written report, so a long sweep can't lose its results.
4. Fix what they find (section 4). Anything the checker could catch automatically next time gets added to `check.py`.

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
7. **Plain English:** could a newcomer follow it (rule R2)? Include NOW.md: every "What's next" item must say what the thing is and why it matters, not just its name (from L10d).
8. **Open items (scrub the whole log):** read every open item in `open-items.md`, not only the ones this session touched. For each: is it finished (then it belongs under "Closed" with the date), still open but changed (then its wording, "Who" or "Waits on" needs updating), or unchanged? Does it still match the file it came from? Did this session create anything unfinished that isn't in the log?

## 4. Fix
- Fix every Must fix and Should fix. Fix Minor ones too, unless a fix would change a decision the user made.
- Anything that needs the user's decision goes on a short list for the report. Don't guess.

## 5. Second review: confirm the fixes
Start a second fresh reviewer with the list of findings and fixes. It checks
each one (pass or fail, with a quote) and looks for new problems the fixes
caused. Fix what it finds, then run the mechanical checks again.

## 6. Record it in the Audit Log (required, Audit Log improvement 2)
Add one row to "The record" in `memos/audit-log.md`, newest first: the date, what was audited, the size and how (in the "Size and how" column) (scripts, reviewers), findings by severity (Must fix, Should fix, Minor), the nothing-lost lines grouped by reason (reworded, moved, cut on purpose, with counts; the script's per-file counts help), and the result (fixed, open decisions, pull request). For a deep audit, also add an "Entry" section with the details. Then rebuild and republish the Audit Log page (`python3 designs/md-page-build.py`). The record is how we see whether quality is improving.

## 7. Report and learn
- Tell the user, in about 5 lines: how many findings by severity, the 3 that mattered most, that all are fixed (or what's left), and anything they need to decide.
- For each Must fix that came from Claude's own work, log a lesson with the **log-lesson** skill (what happened, the root cause and the fix).
- Only after a clean audit: offer to merge into main. On GitHub, every pull request also runs the audit checker automatically (`.github/workflows/audit-check.yml`), so a merge clicked on GitHub shows a red mark first if anything fails.

## Rules
- Never limit the audit to changed files. The checker covers every file every time, and the alignment sweep (2b) covers every core document in every standard and deep audit.
- Never put reference pages on the user's review list (rule R22). Claude keeps them aligned.
- Never skip the audit because a change looks small: a small change gets the quick size, not no audit. The empty tables of 2026-10-09 came from a "simple" rebuild.
- Never say "clean" without proof: the checker's output, the render check's output, the reviewers' pass list and the screenshots.
- If a reviewer and Claude disagree, check the source text and say who was right.
