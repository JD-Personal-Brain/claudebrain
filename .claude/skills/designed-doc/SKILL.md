---
name: designed-doc
description: Make a designed, branded document or page for any person to read, the user included (a memo, plan, manual, playbook, brief, one-pager). Use whenever Claude is about to write something a person will read, without being asked, and when the user says "make a doc for X", asks for a memo or summary to share, or wants an existing doc updated. Never deliver these as .md files (rule R16).
---

# Make a designed doc

Anything a person reads, me included, is a designed page, never a Markdown file (R16).
The .md in `memos/` is only Claude's working copy of the words.

## 1. Start
- **First, decide who reads it (rule R16).** If any person will read it, me included (memos, plans, manuals, playbooks, summaries), it's a designed page: use this skill without being asked. Only files that only Claude uses (rules, skills, NOW.md, logs) stay plain.
- Ask only what's missing: who reads it, and is it a **one-pager** (to print or send as a PDF) or a **long doc** (to scroll)?
- If a designed version already exists (check NOW.md and the Artifact list), **update it in place** so the link stays the same.
- **Before editing an existing page, check that the live page isn't newer than its saved file (required, idea 38).** Another session may have published changes it hasn't merged into main yet. Read the live page with the Artifact tool and compare its text with its file in `designs/`. For the RM design page (a canvas), list its published files (Artifact tool, `action: "list"`, `scope: "files"`), read each with `path`, and compare each with the file of the same name in `designs/rm-analytics-canvas/`. If they match, go ahead. If the live page has wording the repo copy lacks, first run `git fetch origin` and look for that wording on main and on other branches (for example, `git grep -n "<wording>" $(git branch -r)`). Then either build on the newer version, so its changes are kept, or stop and tell the user which page differs and how. Never publish a page built from a copy older than what's live. *(From 2026-10-10, when the RM design page, the scrolling plan page and five other pages all had newer live edits than the repo.)*

## 2. Words first
- Write or update the working copy in `memos/<name>.md`.
- Use [X] for numbers we don't have yet. Every outside fact gets a source, checked before sharing.

## 3. Build it in the house style
Use this look unless the user asks for another one:
- **Fonts:** IBM Plex Serif for headings, IBM Plex Sans for text, IBM Plex Mono for small labels (Google Fonts).
- **Colors:** navy `#14213D` (header bands, key callouts), teal `#0F5F59` / `#0F766E` (labels, links, accents), amber `#FDF3E1` with `#8A4B00` (checks and backup plans), light ground `#F4F6F8`, white cards with `#D9DEE5` borders.
- **Layout:** a navy header with a small label, the title and a one-line outcome; then sections, each with a mono label, a serif heading and cards or tables.

Which format:
- **One-pager:** an artboard on a Design canvas, Letter size (816 × 1056 px), so it exports as a PDF.
- **Long doc:** one standalone HTML page that scrolls. Don't put a long doc on a single canvas artboard: the canvas shows only the first 8,000 px. If it must live on a canvas, split it into parts under about 7,000 px each.

## 4. Check it on screen (required, rule R7)
Before saying it's done:
1. Render it locally with Playwright (Chromium is at `/opt/pw-browsers/chromium`). Canvas artboards need the canvas's `dc-runtime.js` saved next to them as `support.js`, and must be served through a local web server (`python3 -m http.server`), never opened from disk: from disk the runtime drops table rows (from L7c).
2. Measure: a one-pager's last line must end inside 1,056 px; a long doc must not scroll sideways at 400 px wide.
3. Run `python3 .claude/skills/audit/check.py` and `node designs/render-check.js` (see the audit skill, step 2.2): together they fail on any empty table, cut-off canvas part, sideways scrolling or stray Markdown (required, from L7c and L19). If you changed a canvas part's length, update its frame height in `canvas.json`.
4. Look at one screenshot. Fix anything cut off, overlapping or empty, then publish.

## 5. Deliver
- Publish, then open it for the user. Say it's private until they share it from the page's Share menu.
- Put the link in NOW.md, save a draft, and ask before merging into main.
- If the words changed, update the .md working copy too.
- Save the page's HTML source in `designs/` and add it to `designs/README.md`, so any session can rebuild it.
- Add it to the Document Library: an item in `designs/library.json` under the right section's `items` (id, name, what, status, url, source), its .html file in `PAGE_FILE` in `designs/library-build.py`, then `python3 designs/library-build.py` and republish the library (the **documents** skill).
