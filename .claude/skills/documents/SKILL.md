---
name: documents
description: Show the Document Library, the one page listing every designed document in this repo, grouped by area with each document under its parent. Use when the user says "/documents", "show me my documents", "open the document library", "what documents do we have", "the library" or "where's the X page".
---

# Show the Document Library

The library lives at https://claude.ai/artifact/LTpbCT4kN4LcyEoYnh7vgj and is
pinned to the user's claude.ai sidebar. It's built from `designs/library.json`.

1. **Check it's complete.** Run `python3 .claude/skills/audit/check.py` from the repo root. It fails if any page in `designs/README.md` is missing from `designs/library.json`, or if the library page is out of date. If a document is missing, add it to `library.json` under the right area and parent, with its name, one line on what it's for, its status (In use, Waiting for review, Draft, In progress or Reference), its link and its working copy.
2. **Rebuild and republish** if anything changed: `python3 designs/library-build.py`, then publish `designs/library.html` to the same link.
3. **Open it** next to the chat with the Artifact tool (`action: "open"`).
4. **Tell the user in one line** what's new since last time, if anything.

## When a new designed page is made
The **designed-doc** skill adds every new page to `designs/README.md` and
`designs/library.json`, then rebuilds and republishes the library, so it's
always complete.
