---
name: audit
description: Full audit of the work before it goes into main. Runs as the first step of every wrap-up, before offering to merge anything that changes frameworks, the playbook, skills, rules, memos or designed pages, and whenever the user says "audit", "check our work" or "is this clean?".
---

# Audit the work

Auditing is part of the process, not an extra. Nothing is offered for merging
into main until it passes this audit. Keep the report to the user short (rule R2).

## 1. Scope
- List every file changed since main: `git fetch origin main` then `git diff --name-only origin/main...HEAD`, plus any uncommitted changes.
- Add the files they depend on or that depend on them. For example, a change to the six steps (`memos/role-workflow.md`), the rules (`product-framework.md`) or the task tables (`product-machine.md`) also touches `playbook/`, the four "How we deliver" pages and any memo that copies it.
- Add every designed page whose source changed, and its published link (see `designs/README.md`).
- Always add `open-items.md`, the log of everything still open, even if the session didn't edit it: open items go out of date quickly, so every audit checks them.

## 2. Mechanical checks (always)
1. Run `python3 .claude/skills/audit/check.py` from the repo root. It checks that the Product Machine task tables and the playbook match, that every sub-step has all its fields, that no designed page has an empty table or shows a stray underscore left over from Markdown, that every page built from a working copy (product machine, playbook, product framework, tech stack, job description, prompting guide, bank business briefing, open items, Document Library, Workflow Maps, Agent Library, Steps Catalog, Controls Catalog) is up to date, and that every page in `designs/README.md` is in `designs/library.json`, and the other way round. It flags shorthand in NOW.md's "What's next": a rule, test, lesson or item number used without an explanation in the same brackets, or an item too short to explain itself. It also checks the Open Items log (`open-items.md`): no number used twice, the "At a glance" counts match the rows, every page still waiting for review and every idea that is new, suggested, marked "not yet" or approved but not built yet is in an open item of the log, and the log isn't older than NOW.md. It also fails on any wording listed in the glossary's "Old wording we've retired" table that is still left in a document or page, so a rename can't stop halfway; when this session renamed something, add the old wording to that table first. It also fails if any file cites an Open Items number (V, D, W or P) that isn't a live item. It can't tell whether a reference points to the right item, so after the log is renumbered, re-read each reference against its item. If a page was out of date, the checker rebuilds it: republish it.
2. **Render every designed page, every audit, not only the changed ones** (from L19): the design canvas's runtime is kept beside its parts as `designs/rm-analytics-canvas/support.js` (the startup check warns if it's missing), so just run `PW=$(npm root -g)/playwright node designs/render-check.js`. It renders all pages the way a reader sees them and fails on an empty table, sideways scrolling at phone width, stray Markdown, a blank render, or a canvas part taller than its frame (cut off at the bottom). It must report `problems: 0`. Then look at the screenshots of the pages that changed (in `/tmp/render-check`), including their bottoms.
3. For each published page: read it with the Artifact tool and confirm it matches the source in `designs/`. If it doesn't, find out why before changing anything.

## 2b. Alignment sweep (always, across ALL core documents)
The point of the audit is to keep every core document consistent, not only the
files this session touched. A stale line in an untouched file is still drift
(from L18: the library said the playbook had a "19-agent library" while the
Agent Library showed 39, and no audit caught it because neither file changed).
1. The reference pages are the source of truth for their subject: the **Agent Library** (agents), **Workflow Maps** (processes and workflows), **Steps Catalog** (sub-steps and their tasks), **Controls Catalog** (controls) and **Glossary** (`glossary.md`, the words we use). Each is built from working files, so first confirm it's up to date (step 2.1).
2. Start read-only reviewers in parallel (Agent tool), one per reference page (the glossary can share a reviewer with the Steps Catalog). Each builds the page's inventory from its sources, then checks **every** core document against it, changed or not: `product-framework.md`, `product-machine.md`, `playbook/`, `memos/`, `NOW.md`, `open-items.md`, `tech-stack.md`, `designs/library.json`, `designs/README.md`, hard-coded text in `designs/*-build.py`, the hand-made pages (`designs/rm-analytics-canvas/`, `designs/rm-analytics-plan.html`, `designs/role-workflow.html`) and the skills. They look for wrong counts, names that differ, items in one place but missing from another, wrong cross-references (sub-step, agent or control numbers) and hand-made pages older than their working copy. Each finding needs file and line, a quote, and the fix.
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
7. **Plain English:** could a newcomer follow it (rule R13)? Include NOW.md: every "What's next" item must say what the thing is and why it matters, not just its name (from L10d).
8. **Open items (scrub the whole log):** read every open item in `open-items.md`, not only the ones this session touched. For each: is it finished (then it belongs under "Closed" with the date), still open but changed (then its wording, "Who" or "Waits on" needs updating), or unchanged? Does it still match the file it came from? Did this session create anything unfinished that isn't in the log?

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
- Never limit the audit to changed files. The alignment sweep (2b) covers every core document every time.
- Never put reference pages on the user's review list (rule R22). Claude keeps them aligned.
- Never skip the audit because a change looks small. Today's empty tables came from a "simple" rebuild.
- Never say "clean" without proof: the checker's output, the render check's output, the reviewers' pass list and the screenshots.
- If a reviewer and Claude disagree, check the source text and say who was right.
