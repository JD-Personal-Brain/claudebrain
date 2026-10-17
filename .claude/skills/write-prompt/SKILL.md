---
name: write-prompt
description: Write a prompt with the user, piece by piece, using prompting.md. Use when the user says "write a prompt for X", "help me with a prompt", "turn this into a prompt", or wants a reusable prompt for any task (emails, memos, summaries, analysis), even if they don't say "prompt".
---

# Write a prompt

Every prompt follows `prompting.md` (rule R12). The user is learning, so
show the pieces as you go, but keep each message tiny (rule R2).

## 1. Find out what it's for
Ask at most one question at a time, and only for what's missing:
- **Goal:** what should the answer let them do? What does "done" look like?
- **Inputs:** is there long material (notes, a document, data)? If yes, it goes first and the request last (tip 6).
- **Reuse:** one-off, or a prompt they'll reuse? Reusable ones get `[brackets]` to fill in.

If the conversation already answers these, don't ask again. If you assume
something, say it in one line so the user can correct it.

## 2. Draft it with the template
Use the pieces from `prompting.md` that the task needs. Goal, Context and
Output always; Tone when the feel matters; the rest for big, risky or reusable prompts.
- Give every rule a reason ("because ...").
- Wrap pasted material in tags, like `<notes>`.
- If the same setup would be re-typed every time, say so: it may belong in a skill or saved file instead.

## 3. Check it before handing it over
Run the checklist at the bottom of `prompting.md` and show the result in one
line (for example "Checklist: newcomer ✅ done-and-format ✅ reasons ✅ tone ✅").
Fix anything that fails first.

## 4. Hand it over
- Show the prompt in a code block so it's easy to copy. The prompt itself can
  be longer than the 5-line limit (R2); keep everything around it short.
- Add one line on how to use it, and one on how to ask for changes if the answer is off (see "When the answer is off" in `prompting.md`).
- If it's reusable, ask: "Save it in the Prompt Library (`prompt-library.md`)? (yes/no)". A saved prompt gets a number, a version and a "What changed" line; improving it later raises the version.
