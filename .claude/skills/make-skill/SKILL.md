---
name: make-skill
description: Turn an approved idea into something that runs. Use whenever the user says yes to an idea (at wrap-up or any time), says "make this a skill", "build this", "operationalize X", or when an idea in ideas.md is marked yes but has no home. Picks the right home (a new skill, a step in an existing skill, a rule with a test, or a one-off task), builds it, tests it and audits it.
---

# Make an idea run

An idea that doesn't land somewhere that runs gets lost. Every approved idea
gets a home in the same session (rule R17). Keep messages short (rule R2).

## 1. Pick the home
Ask these questions in order and stop at the first yes:

| Question | Home |
|---|---|
| Is it a job with steps that will come up again, on its own? | **New skill** in `.claude/skills/<name>/SKILL.md` |
| Is it part of a job a skill already does? | **A step in that skill** |
| Is it about how Claude behaves every time? | **A rule** in `learning/rules.md`, with a test in `learning/tests.md` |
| Does it only need doing once? | **A one-off task**: do it now, or add it to the Open Items log (the right track, or My workspace) |

Some ideas need two homes, for example a one-off fix plus a check so the
problem can't come back. Before adding a new skill, check the list of
existing skills: if one is close, add a step to it instead, so skills don't overlap.

Tell the user the home in one line, with the reason, before building.

## 2. Build it
**A new skill** has:
- A `description` that says exactly when to use it, including the words the user is likely to say, so it triggers without being asked.
- Numbered steps in plain English (rule R2).
- Its checks: how Claude proves each run worked (rule R7).
- What it produces, and where it's saved. If a person reads the result, it's a designed page (rule R16, the **designed-doc** skill).
- Any helper script inside the skill's own folder.

**A step in a skill:** add it where it happens in the job, numbered in order, with its reason.

**A rule:** one line, written as what to do, with "(from …)" naming its source. Rules at Level 2 or higher go at the top.

**A one-off task:** do it now if it's small. Otherwise add it to the Open Items log under the right track (or My workspace), with the one next step.

## 3. Test it
- **A skill or step:** add a test to `learning/tests.md` ("Say this" and "Pass if"). Then try it once on a real or sample case, and show the result.
- **A rule:** add its test to `learning/tests.md`.
- **A task:** show the proof it's done.

## 4. Record it
- In `ideas.md`, fill in the idea's **Where it runs** column and set its status to done, with the date.
- In NOW.md, list any new skill under "Where things stand", and add an agreement if the idea changes how we work.

## 5. Audit, then merge
Run the **audit** skill (rule R18). Only after it's clean, offer to merge into main.

## Rules
- Never mark an idea done until its home exists and has been tried once.
- If the right home isn't clear, give a recommendation and ask one question.
