---
name: new-use-case
description: Draft a full product plan (memo) for a new AI use case at Associated Bank, using the product framework. Use when the user says "new use case: X", "plan a product for X", or "how would I deliver X", for any banker or business problem they want to solve with AI.
---

# Plan a new use case

This turns one line ("new use case: treasury management officers") into a memo
organized by the six steps in `memos/role-workflow.md` and following the rules in
`product-framework.md`, like the RM plan
(`memos/rm-analytics-framework.md`, built around The RM Assistant), which is the worked example.

## 1. Confirm the basics
Ask only for what the user's message doesn't already say, one question at a time:
- **The use case:** the user group (which bankers or team) and the area of their work, in one sentence.
- **The goal:** what result should it bring (more revenue, hours saved, fewer errors)?
- **Anything the user has heard** from the bank about it.
Don't ask for anything already in the repo (rule R6).

## 2. Draft the memo
Use Prompt 2 in `prompt-library.md` as the brief, with this use case's Context and
user group swapped in. In short:
- Start from the product: one AI assistant for the group, its limits and its capabilities by moment in the user's work, each tied to the core use case it answers (as `memos/rm-assistant-detail.md` does; for this user group, each core use case's counterpart, see `glossary.md`).
- Write the six steps (`memos/role-workflow.md`) as one table, as `product-framework.md` sets out.
- Deliver the kit: three short pages for people (executive summary, product, plan) plus one detail document for AI (decided 2026-10-18, C50).
- Use only tools named in `tech-stack.md`. Keep the AI assistive (AI suggests, a person decides).
- Use [X] for numbers we don't have, never invented ones. Every outside fact gets a source, or is marked "I do not have a verified source for this."
- Aim for a first version of about 300 to 400 lines. Leave out the RM memo's appendices (agent specs, workflows) and market scan unless the user asks; offer them as a next step.

## 3. Audit it, then fix it
Check the draft against `memos/role-workflow.md` and `product-framework.md`, point by point (rule R21):
every step has a gate, governance runs through every step, all five kinds of
measures are there, the quality bar is set, only `tech-stack.md` tools are named,
unknown numbers are [X], and every capability is tied to a core use case. List the gaps, fix them, and
show the user a pass or fail list with proof.

## 4. Save and hand over
- Save it as `memos/<short-name>.md`. This is the working copy only.
- Build the designed version with the **designed-doc** skill without asking, because the user will read it (rule R16). Then show the link and a 5-line summary.
- Add it to the Document Library and `designs/README.md` (the designed-doc skill does this), save a draft to GitHub, and ask before merging into main.
