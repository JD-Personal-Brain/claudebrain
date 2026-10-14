# Playbook: the field manual under the delivery machine

Page 4 of the four "How we deliver" pages. The Product Workflow
(`memos/role-workflow.md`) shows the steps, the Product Framework
(`product-framework.md`) sets the rules, and the Delivery Machine
(`delivery-machine.md`) marks each task Auto, Draft, Me or Partner. This folder
says **how to do it the first time**, sub-step by sub-step, and what to watch so
the second time can be automated.

**Read it as a designed page:** https://claude.ai/artifact/YPEZ2F4Zp4bYUDmeQPzef4 (built from these files by `designs/playbook-build.py`; edit the .md files here, then rebuild and republish).

Use it while doing the work: open the step's file, work through each sub-step
in order, and fill in its **first-time log** as you go.

## The files
| Step | File | Status |
|---|---|---|
| 1. Discover | `1-discover.md` | In use, reviewed 2026-10-14 |
| 2. Define | `2-define.md` | In use, reviewed 2026-10-14 |
| 3. Build | `3-build.md` | In use, reviewed 2026-10-14 |
| 4. Govern and test | `4-govern-and-test.md` | In use, reviewed 2026-10-14 |
| 5. Release and adopt | `5-release-and-adopt.md` | In use, reviewed 2026-10-14 |
| 6. Measure and iterate | `6-measure-and-iterate.md` | In use, reviewed 2026-10-14 |
| Agent library | `agents.md` | 33 general agents (M1 to M33); a short list closes the playbook page, and the full specs are on the Agent Library page |
| Controls | `controls.md` | 25 controls (K1 to K25); shown on the Controls Catalog page |

## How every sub-step is written
- **Goal:** what this sub-step is for, in one line.
- **Why it matters:** what goes wrong if it's skipped.
- **Know first:** the people, data and bank rules you need before starting.
- **First time, step by step:** the actual work, in order.
- **Output:** what it produces (a document, a number, a decision).
- **Done when:** how to tell it's finished.
- **Automation watch:** what to note while doing it, the agent it could become, the kind to use the first time and the kind to aim for (Auto, Draft or Me).
- **For RM analytics:** a short worked example from the first project.

## The first-time log (fill in for every sub-step)
This is what makes automation possible later: you can't automate work you
never wrote down.

| Field | What to write |
|---|---|
| Time spent | Hours, roughly |
| What I actually did | The real steps, including the ones not in the playbook |
| Inputs I needed | Data, documents, people |
| Where I waited | Who or what held it up, and for how long |
| What repeated | Anything I did more than once, or will do again next project |
| Automation check | Repeat? Stable? Safe alone? (yes or no each) |
| Agent idea | If all three are yes: what it would do, and Auto or Draft |

## Rules that apply to every step
- **No client data in an AI tool the bank hasn't approved**, even for a quick test.
- **Guesses about the bank are marked ⚠️** until confirmed. Replace them with facts as I learn them, and note the source.
- **Numbers we don't have yet are [X].** Never invent them.
- **At the gate,** run the automation check from `delivery-machine.md` on every Me and Draft task, and update the step's table there.

_Last updated: 2026-10-14_
