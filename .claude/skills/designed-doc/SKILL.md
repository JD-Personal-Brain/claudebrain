---
name: designed-doc
description: Make a designed, branded document for other people to read (a memo, plan, brief, one-pager). Use when the user says "make a doc for X", asks for a memo or summary to share, or wants an existing doc updated. Never deliver these as .md files (rule R16).
---

# Make a designed doc

People-facing documents are designed pages, never Markdown files (R16).
The .md in `memos/` is only Claude's working copy of the words.

## 1. Start
- Ask only what's missing: who reads it, and is it a **one-pager** (to print or send as a PDF) or a **long doc** (to scroll)?
- If a designed version already exists (check NOW.md and the Artifact list), **update it in place** so the link stays the same.

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
1. Render it locally with Playwright (Chromium is at `/opt/pw-browsers/chromium`). Canvas artboards need the canvas's `dc-runtime.js` saved next to them as `support.js`.
2. Measure: a one-pager's last line must end inside 1,056 px; a long doc must not scroll sideways at 400 px wide.
3. Run `python3 .claude/skills/audit/check.py`: it fails on any empty table (required, from L7c).
4. Look at one screenshot. Fix anything cut off, overlapping or empty, then publish.

## 5. Deliver
- Publish, then open it for the user. Say it's private until they share it from the page's Share menu.
- Put the link in NOW.md, save a draft, and ask before merging into main.
- If the words changed, update the .md working copy too.
- Save the page's HTML source in `designs/` and add it to `designs/README.md`, so any session can rebuild it.
