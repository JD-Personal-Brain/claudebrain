# Playbook: the field manual under the delivery machine

`product-framework.md` says **what** happens in each step and marks each task
Auto, Draft or Me (or Partner, for sign-offs). This folder says **how to do it the first time**, sub-step
by sub-step, and what to watch so the second time can be automated.

Use it while doing the work: open the step's file, work through each sub-step
in order, and fill in its **first-time log** as you go.

## The files
| Step | File | Status |
|---|---|---|
| 1. Discover | `1-discover.md` | Draft, 2026-10-09, waiting for my review |
| 2. Define | `2-define.md` | Draft, 2026-10-09, waiting for my review |
| 3. Build | `3-build.md` | Draft, 2026-10-09, waiting for my review |
| 4. Govern and test | `4-govern-and-test.md` | Draft, 2026-10-09, waiting for my review |
| 5. Release and adopt | `5-release-and-adopt.md` | Draft, 2026-10-09, waiting for my review |
| 6. Measure and iterate | `6-measure-and-iterate.md` | Draft, 2026-10-09, waiting for my review |

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
- **At the gate,** run the automation check from `product-framework.md` on every Me and Draft task, and update the step's table there.

_Last updated: 2026-10-09_
